"""Package the self-contained editable figure gallery without publishing."""
from pathlib import Path
import hashlib
import json
import zipfile
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'assets/figures-editable'
ARCHIVE=ROOT/'delivery/English_Lesson_Figures_20261015.zip'


def main():
    doc=BeautifulSoup((BASE/'index.html').read_text(encoding='utf-8'),'html.parser')
    links=[n.get('src',n.get('href')) for n in doc.select('[src],[href]')]
    for link in links:
        target=(BASE/link).resolve()
        assert target.is_relative_to(BASE.resolve()) and target.is_file(),link
    files=sorted(p for p in BASE.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    manifest={'entry':'index.html','figures':178,'files':[{'file':p.relative_to(BASE).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
    ARCHIVE.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(ARCHIVE,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:z.write(p,'English_Lesson_Figures/'+p.relative_to(BASE).as_posix())
        z.writestr('English_Lesson_Figures/FILE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
    with zipfile.ZipFile(ARCHIVE) as z:
        assert z.testzip() is None
        for r in manifest['files']:
            assert hashlib.sha256(z.read('English_Lesson_Figures/'+r['file'])).hexdigest()==r['sha256']
    report={'status':'passed','files':len(files),'gallery_local_links':len(links),'archive':str(ARCHIVE.relative_to(ROOT)),'bytes':ARCHIVE.stat().st_size,'sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'zip_crc_and_all_file_hashes':'passed','published':False}
    (ROOT/'verification/english-figures-20261015/package-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))


if __name__=='__main__':main()
