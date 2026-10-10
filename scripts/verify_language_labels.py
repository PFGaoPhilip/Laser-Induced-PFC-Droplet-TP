"""Regression checks for the six screenshot failures and repeated localization."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
def main():
    settings=json.loads((ROOT/'COURSE_SETTINGS.json').read_text(encoding='utf-8'))
    pages=[ROOT/'index.html',*(ROOT/x['file'] for x in settings['chapters']+settings['appendices']+settings['legacy_routes']),*sorted((ROOT/'reference').glob('*.html'))]
    before={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in pages}
    subprocess.run([sys.executable,'-B',str(ROOT/'scripts/integrate_modeling.py'),'--course-only'],check=True)
    errors=[];labels=0
    for p in pages:
        if hashlib.sha256(p.read_bytes()).hexdigest()!=before[p]:errors.append(p.name+': repeated localization changed the HTML')
        soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
        for a in soup.select('.toc a[href^="#"]'):
            target=soup.find(id=a['href'][1:]); zh=target.parent.find(target.name,lang='zh-CN',recursive=False)
            spans=a.find_all('span',recursive=False)
            if len(spans)!=2 or [n.get('lang') for n in spans]!=['en','zh-CN']:
                errors.append(p.name+': invalid TOC language structure');continue
            if spans[0].get_text()!=target.get_text() or spans[1].get_text()!=zh.get_text():errors.append(p.name+': TOC label differs from its heading')
            if re.search('[\u4e00-\u9fff]',spans[0].get_text()):errors.append(p.name+': Chinese inside English TOC label')
            labels+=1
        for node in soup.select('.eyebrow, .sidebar > h2, .sidebar nav:not(.toc) a'):
            en=node.find('span',lang='en',recursive=False);zh=node.find('span',lang='zh-CN',recursive=False)
            if not en or not zh:errors.append(p.name+': missing separate UI labels');continue
            if re.search('[\u4e00-\u9fff]',en.get_text()):errors.append(p.name+': Chinese inside English UI label')
            if re.search('FOUR CHAPTERS|THEORY|DERIVATION|DEFENSE|Chapter|Appendix',zh.get_text()):errors.append(p.name+': English UI phrase inside Chinese label')
    report={'status':'passed' if not errors else 'failed','pages':len(pages),'toc_labels_checked':labels,'repeated_localization_byte_identical':not any('changed the HTML' in x for x in errors),'errors':errors,'scope':'Exact English/Chinese sidebar labels from source headings, localized banners/navigation, and unchanged HTML after a second localization pass.'}
    (ROOT/'verification/language-labels-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report));assert not errors
if __name__=='__main__':main()
