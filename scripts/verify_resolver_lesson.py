"""Check current reader structure and protected inputs without simulation.

Optional --relocated PATH checks byte equality against an actual moved copy.
Browser interaction belongs to a separate recorded browser audit.
"""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import hashlib,json,ast,argparse
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
L=ROOT/'learning-records/resolver-progress'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
parser=argparse.ArgumentParser()
parser.add_argument('--relocated',type=Path)
args=parser.parse_args()
broken=[]
for p in [L/'index.html']:
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    for tag,attr in [('a','href'),('script','src'),('link','href')]:
        for e in soup.select(f'{tag}[{attr}]'):
            u=urlsplit(e[attr])
            if not u.scheme and u.path and not (p.parent/unquote(u.path)).is_file():broken.append(e[attr])
assert not broken,broken
assert soup.select('.chapter-body [lang="en"]') and soup.select('.chapter-body [lang="zh-CN"]')
for selector in ('nav.topbar','.page-layout','.sidebar','.reading','.chapter-header h1','.chapter-body'):
    assert soup.select_one(selector),selector
frozen=soup.select('a[data-frozen-source]')
assert len(frozen)==2 and all(link.has_attr('download') for link in frozen)
assert soup.select_one('script[src="assets/course-theme.js"]')
assert soup.select_one('script[src="assets/course-language.js"]')
assert len(soup.select('[data-tex]'))==9
progress=json.loads((L/'PROGRESS.json').read_text(encoding='utf-8'))
for stage in progress['stages']:assert stage['status'] in soup.get_text(),stage['status']
assert progress['strict_acceptance'] is False
assert progress['all_objective_values_null'] is True
assert progress['publication_status']=='HELD_NOT_PUBLISHED'
inputs=json.loads((L/'INPUT_MANIFEST.json').read_text(encoding='utf-8'))['copies']
for row in inputs:assert sha(L/row['copy'])==row['sha256'],row['copy']
files=[p for p in L.rglob('*') if p.is_file()]
relocated='NOT_RUN'
if args.relocated:
    for p in files:
        moved=args.relocated/p.relative_to(L)
        assert moved.is_file() and sha(p)==sha(moved),str(p.relative_to(L))
    relocated={'status':'PASS','files':len(files)}
for name in ['build_resolver_lesson.py','integrate_resolver_progress.py','build_course.py','package_site.py']:
    ast.parse((ROOT/'scripts'/name).read_text(encoding='utf-8'))
result={'status':'PASS','scope':'Current resolver reader structure, links, exact stage statuses and protected input hashes.','copied_input_hashes':len(inputs),'broken_lesson_links':broken,'bilingual_prose':'PRESENT','theme_and_language_scripts':'PRESENT','equation_sources':9,'relocation':relocated,'browser_interaction':'NOT_RUN_BY_THIS_SCRIPT','math_rendering':'NOT_RUN_BY_THIS_SCRIPT','analytical_examples':'NOT_RUN_BY_THIS_SCRIPT','native_build':'NOT_RUN','new_simulation':'NOT_RUN','publication':'HELD_NOT_PUBLISHED','historical_LESSON_QA':'Preserved unchanged; this record does not restate its browser claims.'}
(ROOT/'verification/resolver-reader-prose-audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
