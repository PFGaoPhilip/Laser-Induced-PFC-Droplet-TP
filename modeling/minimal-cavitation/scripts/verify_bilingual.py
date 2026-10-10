"""Audit translation preservation, complete editions, color coverage and MPH hashes."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]

def mathematical_expressions(text):
    return re.findall(r'\$\$.*?\$\$|\$(?:[^$\n]+)\$',text,re.S)
def numeric_tokens(text):
    # Sentence punctuation is not part of a decimal value.
    return re.findall(r'\d+(?:\.\d+)?(?:[eE][-+]?\d+)?',text)
def code_tokens(text):
    return re.findall(r'```[^\n]*\n(.*?)```|(?<!`)`([^`\n]+)`(?!`)',text,re.S)
def compare(english,chinese):
    en=(ROOT/english).read_text(encoding='utf-8');zh=(ROOT/chinese).read_text(encoding='utf-8')
    for label,extractor in [('math',mathematical_expressions),('numeric tokens',numeric_tokens),('code',code_tokens)]:
        a,b=extractor(en),extractor(zh)
        if a!=b:
            at=next((i for i,(x,y) in enumerate(zip(a,b)) if x!=y),min(len(a),len(b)))
            raise AssertionError(f'{english}: {label} mismatch at {at}: {a[at:at+2]} != {b[at:at+2]}')
    return {'english':english,'chinese':chinese,'mathematical_expressions':len(mathematical_expressions(en)),
            'numeric_tokens':len(numeric_tokens(en)),'code_entries':len(code_tokens(en)),
            'scope':'Exact ordered tokens; semantic review recorded separately in sources/i18n/.'}

def main():
    translations=[compare(a,b) for a,b in [('STEP_BY_STEP.md','STEP_BY_STEP.zh.md'),('MODEL_SPEC.md','MODEL_SPEC.zh.md'),('RESULTS.md','RESULTS.zh.md')]]
    pages=[]
    css=(ROOT/'assets/terms.css').read_text(encoding='utf-8')
    reference=(ROOT/'sources/interface-reference/theory-4-bilingual-terms.css.txt').read_text(encoding='utf-8')
    expected=reference.replace('html[data-theme="light"]','html[data-theme="day"]')+'\n.technical-term{border-radius:3px;padding:0 .1em;font-weight:600}\n'
    assert css==expected,'Reference semantic palette differs beyond the documented selector/padding adaptation.'
    for name in ('index.html','STEP_BY_STEP.html'):
        soup=BeautifulSoup((ROOT/name).read_text(encoding='utf-8'),'html.parser')
        ids=[node['id'] for node in soup.find_all(id=True)]
        assert len(ids)==len(set(ids)),name+' duplicate IDs'
        assert soup.html['lang']=='zh-CN' and soup.html['data-language']=='zh'
        assert len(soup.select('.reader-controls'))==1
        assert [n['id'] for n in soup.select('.reader-controls button')]==['language','theme']
        assert soup.select_one('[data-locale="en"]').has_attr('hidden')
        assert not soup.select_one('[data-locale="zh"]').has_attr('hidden')
        editions=[]
        for locale in ('en','zh'):
            pane=soup.select_one(f'[data-locale="{locale}"]')
            math_count=len(pane.select('.katex-display'))
            steps=[int(node['data-step']) for node in pane.select('input[data-step]')]
            assert math_count==(29 if name=='index.html' else 0)
            assert steps==(list(range(1,54)) if name=='STEP_BY_STEP.html' else [])
            assert not pane.select('code .technical-term, pre .technical-term, .katex .technical-term')
            terms=pane.select('.technical-term[data-term]');keys=sorted({node['data-term'] for node in terms})
            assert len(keys)>=12,keys
            for key in keys:assert f'data-term="{key}"' in css
            editions.append({'language':locale,'steps':len(steps),'display_equations':math_count,'highlighted_occurrences':len(terms),'semantic_term_ids':keys})
        # Every actual COMSOL input remains identical in the two complete guide editions.
        if name=='STEP_BY_STEP.html':
            code=lambda locale:[n.get_text() for n in soup.select(f'[data-locale="{locale}"] main code')]
            assert code('en')==code('zh')
        pages.append({'file':name,'unique_ids':len(ids),'editions':editions,'default_language':'zh'})
    audit=json.loads((ROOT/'verification/NUMERICAL_AUDIT.json').read_text(encoding='utf-8'))
    for row in audit['native_files']:
        assert hashlib.sha256((ROOT/'models'/row['file']).read_bytes()).hexdigest()==row['sha256']
    result={'status':'PASS','translations':translations,'pages':pages,'native_models':audit['native_files'],
            'term_palette':'Exact archived newer-reference stylesheet; only light-to-day selector and term padding adapted.',
            'interaction_verification':'Recorded separately; these checks do not replace browser interaction.',
            'semantic_review':'Chapter peer-review files under sources/i18n/.'}
    (ROOT/'verification/BILINGUAL_CONTENT_AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
