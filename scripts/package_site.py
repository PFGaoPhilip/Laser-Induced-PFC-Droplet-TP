"""Curated new-repository export and forwarding ZIP; never publishes private records."""
from pathlib import Path
import json
import hashlib
import shutil
import re
import zipfile
import subprocess
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
    if settings.get('resolver_progress',{}).get('publication_status')=='HELD_NOT_PUBLISHED':
        raise RuntimeError('Resolver lesson publication is held by owner instruction.')
    authorization=json.loads((ROOT/settings['publication_authorization']['record']).read_text(encoding='utf-8'))
    assert authorization['status']=='AUTHORIZED' and authorization['owner_instruction']=='Update to GitHub.'
    assert authorization['repository']==settings['repository']
    protected_inputs={Path('learning-records/resolver-progress')/row['copy']:row['sha256']
                      for row in json.loads((ROOT/'learning-records/resolver-progress/INPUT_MANIFEST.json').read_text(encoding='utf-8'))['copies']}
    units=settings['chapters']+settings.get('appendices',[])
    selected={Path('index.html'),Path('.nojekyll'),Path('.gitignore'),Path('README.md'),Path('MISSION.md'),Path('RESOURCES.md'),Path('Theses.md'),Path('COURSE_SETTINGS.json')}
    selected.update(Path(c['file']) for c in units+settings.get('legacy_routes',[]))
    selected.update(p.relative_to(ROOT) for folder in ['assets','reference','modeling','Theses'] for p in (ROOT/folder).rglob('*') if p.is_file())
    selected.update(p.relative_to(ROOT) for p in (ROOT/'learning-records/resolver-progress').rglob('*') if p.is_file())
    selected.add(Path('text/course.md'))
    selected.update(Path('text')/Path(c['file']).with_suffix('.md').name for c in units)
    selected.update(Path('sources')/name for name in ['Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md','Cavitation_Course_Before_After_Comparison_EN_ZH.md'])
    selected.update(p.relative_to(ROOT) for p in (ROOT/'content').glob('*.py'))
    selected.add(Path('content/equation_symbol_rows.json'))
    selected.update(p.relative_to(ROOT) for p in (ROOT/'scripts').glob('*') if p.is_file() and p.suffix in ['.py','.cjs'])
    if (DEST/'.git').exists():
        previous=json.loads(subprocess.check_output(['git','-C',str(DEST),'show','HEAD:PUBLIC_FILE_MANIFEST.json'],text=True,encoding='utf-8'))
    else:
        prior=next((p for p in (ROOT/'PUBLIC_FILE_MANIFEST.json',DEST/'PUBLIC_FILE_MANIFEST.json') if p.is_file()),None)
        previous=json.loads(prior.read_text(encoding='utf-8')) if prior else {'files':[]}
    public_verification={row['path'] for row in previous['files'] if row['path'].startswith('verification/')}
    selected.update(p.relative_to(ROOT) for p in (ROOT/'verification').glob('*.json') if p.relative_to(ROOT).as_posix() in public_verification or p.name in {'modeling-integration-audit.json','language-views-audit.json','language-labels-audit.json','embedded-pfc-publication-audit.json','embedded-pfc-browser-audit.json'})
    selected.update(p.relative_to(ROOT) for p in (ROOT/'verification').glob('chapter*-check.py'))
    selected.update(p.relative_to(ROOT) for p in (ROOT/'verification').glob('*.cjs'))
    selected.update(p.relative_to(ROOT) for p in (ROOT/'verification').glob('diagram-review-[0-9][0-9].png'))
    selected.update(Path('verification')/name for name in ['symbol-layout-desktop.png','symbol-layout-mobile.png'])
    selected.update(Path('verification')/name for name in ['equation-heading-desktop.png','equation-heading-mobile.png'])
    selected.update(Path('verification')/name for name in [
        'GITHUB_PUBLICATION_AUTHORIZATION_20261014.json','lesson-revision-baseline.json',
        'lesson-revision-audit.json','chapter-prose-audit.json','chapter-prose-revision.md',
        'report-prose-revision.md','independent-editorial-review.md','github-release-audit.json'])
    selected.update(Path('verification/english-figures-20261015')/name for name in
                    ['figure-audit.json','protected-baseline.json','lesson-audit.json','browser-audit.json','relocation-audit.json'])
    selected.add(Path('scripts/render_science_decks.ps1'))
    selected={p for p in selected if not {'__pycache__','build','tmp','.tools'}.intersection(p.parts)}
    # These are authored public sources, local dependencies and evidence, not private PDFs or response records.
    forbidden_ext={'.pdf','.zip','.mph','.docx','.pptx','.pem','.key','.sqlite','.db','.exe','.dll'}
    secret=re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----')
    computer=re.compile(r'file:/{3}|(?<![A-Za-z0-9])[A-Za-z]:[\\/](?:Users|Program Files|Windows|AppData|ProgramData|Temp|tmp|L\. Jay|Documents|home)',re.I)
    problems=[]
    for relative in sorted(selected):
        p=ROOT/relative
        assert p.resolve().is_relative_to(ROOT.resolve()) and p.is_file(),p
        public_model_file=relative.parts[0]=='modeling' and p.suffix.lower() in {'.mph','.zip'}
        authored_study_pdf=relative.as_posix()=='modeling/embedded-pfc-feasibility/output/pdf/FINITE_PFC_DERIVATION.pdf'
        authored_resolver_pdf=relative.as_posix()=='learning-records/resolver-progress/evidence/Stage3_Engineering_20261014/report/STAGE3_ENGINEERING_REPORT.pdf'
        authored_figure_pptx=relative.parts[:2]==('assets','figures-editable') and p.suffix.lower()=='.pptx'
        if p.suffix.lower() in forbidden_ext and not (public_model_file or authored_study_pdf or authored_resolver_pdf or authored_figure_pptx):problems.append(str(relative))
        if p.suffix.lower() in {'.html','.md','.json','.py','.js','.cjs','.css','.svg','.c','.h','.sh','.tex','.txt','.stdout','.stderr'}:
            text=p.read_text(encoding='utf-8')
            if secret.search(text):problems.append('credential pattern '+str(relative))
            if computer.search(text) and 'vendor' not in p.parts:
                # Sealed scientific provenance records contain historical build paths.
                # They are supplementary evidence, never runtime asset addresses.
                if relative in protected_inputs:
                    assert sha(p)==protected_inputs[relative], 'Changed sealed provenance: '+str(relative)
                elif relative.parts[:2]==('assets','figures-editable') and relative.name.endswith('.scene.json'):
                    scene=json.loads(text)
                    provenance=scene.pop('_source_svg',None)
                    def _strings(node):
                        if isinstance(node,str):
                            yield node
                        elif isinstance(node,dict):
                            for v in node.values():
                                yield from _strings(v)
                        elif isinstance(node,list):
                            for v in node:
                                yield from _strings(v)
                    assert not any(computer.search(v) for v in _strings(scene)), 'Unexpected local path in scene: '+str(relative)
                    assert (provenance is None) or Path(provenance).resolve().is_relative_to(ROOT.resolve()),str(relative)
                else:problems.append('local computer reference '+str(relative))
        target=DEST/relative;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,target)
        if relative==Path('verification/lesson-revision-baseline.json'):
            public_baseline=json.loads(target.read_text(encoding='utf-8'))
            public_baseline['learning_units']={}
            public_baseline['privacy']='Private learner-status evidence omitted from this public baseline.'
            target.write_text(json.dumps(public_baseline,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
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
    report={'status':'passed','files':len(selected)+1,'bytes':ZIP.stat().st_size,'zip_sha256':sha(ZIP),'zip_crc':'passed','manifest_hashes':'passed','excluded':'Third-party paper PDFs, private learner responses/evidence, personal skills, local sessions/work logs and credentials. Authored study/report PDFs and hash-preserved scientific provenance are included.','essential_offline_assets':True}
    (ROOT/'verification/package-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))

if __name__=='__main__':main()
