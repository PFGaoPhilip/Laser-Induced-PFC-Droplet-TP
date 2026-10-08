"""Curated new-repository export and forwarding ZIP; never publishes private records."""
from pathlib import Path
import json
import hashlib
import shutil
import re
import zipfile
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'publication/site'
ZIP=ROOT/'publication/Laser-Induced-PFC-Droplet-TP-offline.zip'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    assert ROOT.is_dir() and DEST.resolve().is_relative_to(ROOT.resolve())
    audit=json.loads((ROOT/'verification/course-audit.json').read_text(encoding='utf-8'))
    assert audit['status']=='passed','Course gate failed'
    settings=json.loads((ROOT/'COURSE_SETTINGS.json').read_text(encoding='utf-8'))
    selected={Path('index.html'),Path('.nojekyll'),Path('.gitignore'),Path('README.md'),Path('MISSION.md'),Path('NOTES.md'),Path('RESOURCES.md'),Path('COURSE_SETTINGS.json')}
    selected.update(Path(c['file']) for c in settings['chapters'])
    selected.update(p.relative_to(ROOT) for folder in ['assets','reference'] for p in (ROOT/folder).rglob('*') if p.is_file())
    selected.add(Path('text/course.md'))
    selected.update(Path('text')/Path(c['file']).with_suffix('.md').name for c in settings['chapters'])
    selected.update(Path('sources')/name for name in ['Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md','Cavitation_Course_Before_After_Comparison_EN_ZH.md'])
    selected.update(p.relative_to(ROOT) for p in (ROOT/'content').glob('chapter*.py'))
    selected.update(p.relative_to(ROOT) for p in (ROOT/'scripts').glob('*') if p.is_file() and p.suffix in ['.py','.cjs'])
    selected.update(p.relative_to(ROOT) for p in (ROOT/'verification').glob('*.json') if not any(tag in p.name for tag in ['publication','cleanup','package-audit']))
    selected.update(p.relative_to(ROOT) for p in (ROOT/'verification').glob('chapter*-check.py'))
    selected.update(p.relative_to(ROOT) for p in (ROOT/'verification').glob('*.cjs'))
    selected.update(p.relative_to(ROOT) for p in (ROOT/'verification').glob('diagram-review-[0-9][0-9].png'))
    selected={p for p in selected if '__pycache__' not in p.parts}
    # These are authored public sources, local dependencies and evidence, not private PDFs or response records.
    forbidden_ext={'.pdf','.zip','.mph','.docx','.pptx','.pem','.key','.sqlite','.db','.exe','.dll'}
    secret=re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----')
    computer=re.compile(r'file:/{3}|(?<![A-Za-z0-9])[A-Z]:[\\/]',re.I)
    problems=[]
    for relative in sorted(selected):
        p=ROOT/relative
        assert p.resolve().is_relative_to(ROOT.resolve()) and p.is_file(),p
        if p.suffix.lower() in forbidden_ext:problems.append(str(relative))
        if p.suffix.lower() in {'.html','.md','.json','.py','.js','.cjs','.css','.svg'}:
            text=p.read_text(encoding='utf-8')
            if secret.search(text):problems.append('credential pattern '+str(relative))
            if computer.search(text) and 'vendor' not in p.parts:problems.append('local computer reference '+str(relative))
        target=DEST/relative;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,target)
    assert not problems,problems
    # Prune only obsolete task-created export files; preserve the new checkout's Git metadata.
    for p in list(DEST.rglob('*')):
        if p.is_file() and '.git' not in p.relative_to(DEST).parts and p.relative_to(DEST) not in selected and p.name!='PUBLIC_FILE_MANIFEST.json':
            assert p.resolve().is_relative_to(DEST.resolve());p.unlink()
    manifest={'repository':settings['repository'],'entry':'index.html','files':[{'path':p.as_posix(),'bytes':(DEST/p).stat().st_size,'sha256':sha(DEST/p)} for p in sorted(selected)],'original_pdfs':0,'private_learner_records':0,'essential_remote_resources':0}
    (DEST/'PUBLIC_FILE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
        for rel in [*sorted(selected),Path('PUBLIC_FILE_MANIFEST.json')]:z.write(DEST/rel,rel.as_posix())
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in manifest['files']:assert hashlib.sha256(z.read(row['path'])).hexdigest()==row['sha256']
    report={'status':'passed','files':len(selected)+1,'bytes':ZIP.stat().st_size,'zip_sha256':sha(ZIP),'zip_crc':'passed','manifest_hashes':'passed','excluded':'Original PDFs, private learner responses/evidence, personal skill files, operational authoring briefs, machine-specific runtime data and credentials.','essential_offline_assets':True}
    (ROOT/'verification/package-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))

if __name__=='__main__':main()
