"""Focused regression checks for the owner-authorized Chapter 1 rewrite."""
from pathlib import Path
import argparse,hashlib,json,re,zipfile,sys
from bs4 import BeautifulSoup
from equation_symbols import equation_label

ROOT=Path(__file__).resolve().parents[1]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def audit(root):
    equations=json.loads((root/'verification/equations.json').read_text(encoding='utf-8'))
    chapter=[e for e in equations if e['id'].startswith('C1-')]
    expected=[f'C1-E{n:02d}' for n in range(1,34)]
    assert [e['id'] for e in chapter]==expected
    soup=BeautifulSoup((root/'chapters/01-cavity-pressure-inertia-and-directional-jets.html').read_text(encoding='utf-8'),'html.parser')
    assert [e['id'] for e in soup.select('.equation-unit')]==expected
    assert not soup.select('.katex-error')
    assert len(soup.select('article.defense'))==3
    evidence=[]
    for e in chapter:
        box=soup.find(id=e['id'])
        assert e['tex'].startswith(r'\begin{gathered}')
        # At least three intermediate mathematical lines inside every block.
        first=e['tex'].split(r'\end{aligned}',1)[0]
        count=first.count('\\\\')+1
        assert count>=3,(e['id'],count)
        assert box.select_one('.math-display .katex-html')
        children=box.find_all(recursive=False)
        assert children[0].select_one('p[lang=en]').get_text().startswith('('+equation_label(e['id'])+')')
        assert 'math-display' in children[1]['class']
        assert 'symbols' in children[2]['class']
        assert len(box.select('.symbols'))==1
        assert not box.select(':scope > .symbol-conventions')
        assert 'before Eq.' not in box.select_one('.symbol-panel-heading').get_text()
        assert box.find_previous_sibling().get_text(strip=True).startswith('Derivation.')
        assert len(box.select('.symbols td.symbol-definition p[lang=en]'))>=1
        assert len(box.select('.symbols td.symbol-definition p[lang="zh-CN"]'))>=1
        assert len(box.select('.formula-figure'))==1
        evidence.append({'id':e['id'],'intermediate_lines_at_least':count,'multiline_derivation':True,'local_bilingual_declarations':True,'titled':True,'compact_symbols_after_formulas':True,'duplicate_definition_paragraph_removed':True})
    text=soup.get_text(' ')
    assert 'C1-E34' not in text
    assert 'D_{rr}' not in str(soup) and 'D_{\\theta\\theta}' not in str(soup)
    assert '6.66667' in text and '0.0666667' in text
    rows=json.loads((root/'assets/figures-editable/manifest.json').read_text(encoding='utf-8'))
    assert {r['id'] for r in rows if r['id'].startswith('c1-')}=={x.lower() for x in expected}
    for r in rows:
        for field in ('svg','pptx','scene'):assert (root/'assets/figures-editable'/r[field]).is_file()
    base=json.loads((root/'verification/lesson-revision-baseline.json').read_text(encoding='utf-8'))
    assert {e['id']:e['tex'] for e in equations if not e['id'].startswith('C1-')}=={k:v for k,v in base['equations'].items() if not k.startswith('C1-')}
    return {'status':'passed','equation_count':33,'other_equations_preserved':len(equations)-33,'editable_figures':len(rows),'equations':evidence,'scope':'Structure, local math rendering, ID migration, and preservation; scientific review and browser evidence are separate.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);args=p.parse_args()
    result=audit(args.root)
    (ROOT/'reports/ch1_defense_revision/VERIFICATION_REPORT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='equations'}))
