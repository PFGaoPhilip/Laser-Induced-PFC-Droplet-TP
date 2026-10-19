"""Verify adjacent explanations and complete preservation of source mathematics."""
import hashlib
import json
import re
import sys
from collections import Counter
from copy import deepcopy
from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'content'))
from chapter01_handoff import PASSAGES, references, render_passage, DISPLAY, INLINE, formula_parts
import markdown

def canonical(node):
    node=deepcopy(node)
    for math in node.select('.katex'):
        annotation=math.select_one('annotation[encoding="application/x-tex"]')
        assert annotation is not None
        math.replace_with('$'+annotation.get_text()+'$')
    return re.sub(r'\s+',' ',node.get_text()).strip()

def source_prose(source):
    text=DISPLAY.sub('',references(source['markdown']))
    protected=[]
    def stash(m):
        protected.append(next(x for x in m.groups() if x))
        return f'CHECKINLINE{len(protected)-1}TOKEN'
    text=INLINE.sub(stash,text)
    soup=BeautifulSoup(markdown.markdown(text,extensions=['tables','sane_lists']),'html.parser')
    for p in soup.select('p'):
        if p.get_text(strip=True) in ['English','中文']:p.decompose()
    text=soup.get_text()
    for n,tex in enumerate(protected):text=text.replace(f'CHECKINLINE{n}TOKEN','$'+tex+'$')
    return text

def prose_characters(text):
    return Counter(c for c in text if not c.isspace() and c!='/')

def verify_handoff(unit):
    identifier=unit['id'];record=PASSAGES[identifier]
    actual=unit.select('.handoff-passage')
    assert len(actual)==len(record['passages'])
    covered=0
    for i,(box,source) in enumerate(zip(actual,record['passages'])):
        excerpt=source['markdown']
        assert hashlib.sha256(excerpt.encode('utf-8')).hexdigest()==source['excerpt_sha256']
        path=ROOT/'sources/chapter01-handoff-20261019'/source['source']
        if path.exists():
            assert hashlib.sha256(path.read_bytes()).hexdigest()==source['source_sha256']
            assert excerpt in path.read_text(encoding='utf-8')
        assert box['data-excerpt-sha256']==source['excerpt_sha256']
        expected=BeautifulSoup(render_passage(identifier,i,source),'html.parser')
        a=box.select('[data-handoff-text]');b=expected.select('[data-handoff-text]')
        assert [n['data-handoff-text'] for n in a]==[n['data-handoff-text'] for n in b]
        assert [canonical(n) for n in a]==[canonical(n) for n in b],(identifier,i,'source prose changed')
        # Independently count all original prose characters, including inline
        # mathematics. Pairing changes paragraph order across languages, but
        # must neither omit nor duplicate any source explanation.
        assert prose_characters(''.join(canonical(n) for n in a))==prose_characters(source_prose(source)),(identifier,i,'source prose coverage')
        displayed=box.select('.math-display')
        exp=expected.select('.math-display')
        attrs=['data-handoff-formula','data-handoff-row','data-source-tex','data-tex']
        assert [[n[x] for x in attrs] for n in displayed]==[[n[x] for x in attrs] for n in exp],(identifier,'source math changed')
        original=[next(x for x in m.groups() if x).strip() for m in DISPLAY.finditer(references(excerpt))]
        for j,tex in enumerate(original):
            tag=re.search(r'\\tag\{([^}]*)\}\s*$',tex)
            content=tex[:tag.start()].strip() if tag else tex.strip()
            source_rows=[n['data-source-tex'] for n in displayed if n['data-handoff-formula']==str(j)]
            assert source_rows
            reconstructed=r'\\'.join(source_rows)
            assert tokens(reconstructed) in [tokens(content),tokens(inner(content))],(identifier,i,j,'source mathematics coverage')
        covered+=len(original)
    return covered

def tokens(tex):
    # Tokenize control words before discarding whitespace. Thus different TeX
    # commands cannot become equal by removing their separating whitespace.
    return re.findall(r'\\[A-Za-z]+|\\.|[^\s]',tex)

def inner(tex):
    tex=tex.strip()
    match=re.fullmatch(r'\\begin\{(aligned|gathered)\}([\s\S]*)\\end\{\1\}',tex)
    return match[2].strip() if match else tex

def verify_source(unit,record):
    supplied=PASSAGES.get(record['id'])
    if supplied:
        verify_handoff(unit)
        if not supplied['supplement']:return
    text=record['tex']
    assert text.startswith(r'\begin{gathered}') and text.endswith(r'\end{gathered}')
    derivation,result=text[len(r'\begin{gathered}'):-len(r'\end{gathered}')].split(r'\\[6pt]',1)
    for phase,original in [('derivation',derivation),('result',result)]:
        displayed=unit.select(f'.derivation-flow .math-display[data-phase="{phase}"]')
        assert displayed,(record['id'],phase)
        reconstructed=r'\\'.join(n['data-source-tex'] for n in displayed)
        assert tokens(reconstructed)==tokens(inner(original)),(record['id'],phase,'source mathematics changed')

def main():
    path=ROOT/'chapters/01-cavity-pressure-inertia-and-directional-jets.html'
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    registry=json.loads((ROOT/'verification/equations.json').read_text(encoding='utf-8'))
    baseline=json.loads((ROOT/'reports/ch1_interleaved_20261019/equations_before.json').read_text(encoding='utf-8'))
    assert [r for r in registry if r['id'].startswith('C1-')]==[r for r in baseline if r['id'].startswith('C1-')]
    equations={r['id']:r for r in registry}
    assert len(soup.select('.equation-unit'))==33
    assert not soup.select('.katex-error')
    rows=[]
    for unit in soup.select('.equation-unit'):
        flow=unit.select_one(':scope > .derivation-flow')
        assert flow is not None
        children=flow.find_all(recursive=False)
        formulas=flow.select('.math-display')
        panels=flow.select('.derivation-panel')
        assert panels
        for panel in panels:
            children=panel.find_all(recursive=False)
            assert 'derivation-reason' in children[0].get('class',[])
            assert 'math-display' in children[1].get('class',[])
            assert 'math-display' in children[-1].get('class',[])
        assert all(f.find_parent(class_='derivation-panel') for f in formulas)
        assert len(formulas)>=3
        for formula in formulas:
            explanation=formula.find_previous_sibling()
            assert explanation is not None
            assert 'derivation-reason' in explanation.get('class',[])
            assert 'math-display' in formula.get('class',[])
            assert explanation.find_next_sibling()==formula
            assert all(explanation.select_one(f'p[lang="{lang}"]').get_text(strip=True) for lang in ['en','zh-CN'])
            assert formula.select_one('.katex-html') and formula.select_one('math')
            # At most two lines when a single equation requires wrapping.
            if not formula.has_attr('data-handoff-formula'):
                assert formula['data-tex'].count(r'\\')<=1
            elif formula['data-tex'].count(r'\\')>1:
                # One simultaneous boundary-condition system or one equality
                # wrapped across additive terms is not a derivation chain.
                assert r'\begin{cases}' in formula['data-tex'] or re.search(r'\\\\\s*&\s*[+-]',formula['data-tex'])
        assert not unit.select(':scope > .math-display')
        assert len(unit.select('.symbols'))==1
        assert flow.find_next_sibling()==unit.select_one('.symbols')
        verify_source(unit,equations[unit['id']])
        rows.append({'id':unit['id'],'explanation_equation_pairs':len(formulas),'source':'preserved handoff passages' if unit['id'] in PASSAGES else 'matching-style supplement','all_source_math_retained':True,'symbols_after_complete_derivation':True})
    report={'status':'passed','groups':33,'original_handoff_groups':len(PASSAGES),'original_handoff_passages':sum(len(v['passages']) for v in PASSAGES.values()),'matching_style_groups':33-len(PASSAGES),'explanation_equation_pairs':sum(r['explanation_equation_pairs'] for r in rows),'large_combined_derivation_displays':0,'equation_registry_records_preserved':len(registry),'source_tex_token_coverage':'exact handoff display tokens; exact registry derivation/result tokens for supplements','source_prose_coverage':'all selected source prose characters retained; exact paragraph content and displayed sequence verified','bilingual_explanations_before_every_formula':True,'chapter_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'reference':'content/chapter01_handoff.json','equations':rows,'scope':'Presentation, bilingual adjacency, exact selected-source prose/math preservation, and rendering. Source chains receive added explanations between unchanged rows. A single equality may wrap; simultaneous boundary data retain necessary rows. This audit does not establish new physical validation.'}
    assert len(soup.select('.math-display'))==report['explanation_equation_pairs']
    assert all(n.find_parent(class_='equation-unit') for n in soup.select('.math-display'))
    report['all_chapter_displays_covered']=True
    (ROOT/'reports/ch1_interleaved_20261019/NARRATIVE_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='equations'}))

if __name__=='__main__':main()
