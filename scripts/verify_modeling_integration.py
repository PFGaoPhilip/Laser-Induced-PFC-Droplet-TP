"""Audit native-model integrity and the moved publication's local dependencies."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import hashlib
import json
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'publication/site'
SOURCE=ROOT.parent/'LEARN_20260929/modeling/20261010-minimal-cavitation'
def main():
    errors=[]; checked=0
    anchors={}
    for p in DEST.rglob('*.html'):
        s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
        theme_script=any('theme' in x.get('src','') for x in s.select('script[src]'))
        study_theme=s.select_one('#theme-toggle') is not None and s.select_one('script[src="assets/reader.js"]') is not None
        inline_theme=s.select_one('#theme, #theme-toggle') is not None
        if not (theme_script or study_theme or inline_theme):errors.append(str(p.relative_to(DEST))+': no theme control')
        for n in s.select('[href],[src]'):
            link=n.get('href',n.get('src','')); url=urlsplit(link)
            if url.scheme or url.netloc or not url.path:continue
            target=(p.parent/unquote(url.path)).resolve(); checked+=1
            if not target.is_relative_to(DEST.resolve()) or not target.exists():errors.append(str(p.relative_to(DEST))+': '+link)
            elif url.fragment and target.suffix=='.html':
                if target not in anchors:
                    doc=s if target==p.resolve() else BeautifulSoup(target.read_text(encoding='utf-8'),'html.parser')
                    anchors[target]={n['id'] for n in doc.select('[id]')}
                if unquote(url.fragment) not in anchors[target]:errors.append(str(p.relative_to(DEST))+': missing anchor '+link)
    native=[]
    for p in (SOURCE/'models').glob('*.mph'):
        target=DEST/'modeling/minimal-cavitation/models'/p.name
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        same=hashlib.sha256(target.read_bytes()).hexdigest()==digest
        native.append({'file':p.name,'sha256':digest,'matches_accepted_source':same})
        if not same:errors.append('Native model changed: '+p.name)
    report={'status':'passed' if not errors else 'failed','html_pages':len(list(DEST.rglob('*.html'))),'local_dependencies_and_links_checked':checked,'native_models':native,'errors':errors,'source_copy':'modeling/minimal-cavitation','scope':'Portable relative links, anchors, theme controls and byte-identical accepted native models. Scientific verification is preserved from the source delivery.'}
    (ROOT/'verification/modeling-integration-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))
    assert not errors
if __name__=='__main__':main()
