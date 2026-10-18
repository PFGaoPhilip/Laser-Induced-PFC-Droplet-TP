"""Audit complete, continuous reasoning steps and retained mathematical evidence."""
import json
import re
import hashlib
from collections import defaultdict
from pathlib import Path
from bs4 import BeautifulSoup
from verify_chapter01_narrative import verify_source

ROOT=Path(__file__).resolve().parents[1]

def main():
    path=ROOT/'chapters/01-cavity-pressure-inertia-and-directional-jets.html'
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    before=BeautifulSoup((ROOT/'reports/ch1_steps_20261019/chapter_before.html').read_text(encoding='utf-8'),'html.parser')
    units=soup.select('.equation-unit')
    headings=soup.select('.derivation-step')
    assert len(units)==len(headings)==33
    assert len({h['data-step-number'] for h in headings})==33
    assert [h['data-step-for'] for h in headings]==[u['id'] for u in units]
    sequences=defaultdict(list)
    equation_records={r['id']:r for r in json.loads((ROOT/'verification/equations.json').read_text(encoding='utf-8'))}
    records=[]
    for heading,unit in zip(headings,units):
        number=heading['data-step-number']
        section,index=number.rsplit('.',1)
        actual=re.match(r'\d+\.\d+',heading.find_previous('h2',lang='en').get_text(' ',strip=True))[0]
        assert section==actual
        sequences[section].append(int(index))
        assert heading.find_next(class_='equation-unit')==unit
        purpose=heading.find_next_sibling()
        assert 'step-purpose' in purpose.get('class',[])
        for lang,prefix in [('en','Step '+number),('zh-CN','步骤 '+number)]:
            assert heading.select_one('[lang="'+lang+'"]').get_text().startswith(prefix)
            text=purpose.select_one('p[lang="'+lang+'"]').get_text(' ',strip=True)
            assert (text.count('.')>=2 if lang=='en' else text.count('。')>=2)
        assert unit.find_previous_sibling().get_text(strip=True).startswith('Derivation.')
        old=before.find(id=unit['id'])
        verify_source(unit,equation_records[unit['id']])
        oldrows=old.select('.symbols td.symbol-definition')
        newrows=unit.select('.symbols td.symbol-definition')
        assert [n.get_text() for n in newrows[:len(oldrows)]]==[n.get_text() for n in oldrows]
        records.append({'equation':unit['id'],'step':number,'objective':heading.select_one('[lang=en]').get_text(' ',strip=True),'purpose':purpose.select_one('p[lang=en]').get_text(' ',strip=True),'math_and_compact_symbols_preserved':True})
    for indices in sequences.values():assert indices==list(range(1,len(indices)+1))
    text=soup.get_text(' ',strip=True)
    assert not re.search(r'\bStep\s+\d+\s*—',text)
    assert not re.search(r'步骤\s*\d+\s*——',text)
    # Existing twenty explanations survive; remove their obsolete prefix only.
    current={p.get_text() for p in soup.select('p[lang=en]')}
    retained=0
    for p in before.select('p[lang=en]'):
        if re.match(r'Step\s+\d+\s*—',p.get_text()):
            expected=re.sub(r'^Step\s+\d+\s*—\s*','',p.get_text())
            assert expected in current,expected
            retained+=1
    assert retained==20
    assert json.loads((ROOT/'verification/equations.json').read_text(encoding='utf-8'))==json.loads((ROOT/'reports/ch1_steps_20261019/equations_before.json').read_text(encoding='utf-8'))
    report={'status':'passed','base_commit':'2b2628cb1ebf06a014f699e96a016007effb7a5c','chapter_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'numbered_steps':33,'bilingual_objectives_and_purposes':33,'subchapter_numbering_contiguous':True,'existing_step_explanations_retained_and_renumbered':retained,'equation_registry_records_preserved':189,'rendered_mathematical_groups_preserved':33,'compact_symbol_tables_preserved':33,'steps':records,'scope':'Step coverage, ordering, numbering, original prose retention, and mathematical preservation. Purpose statements received an editorial self-review against the existing chapter.'}
    (ROOT/'reports/ch1_steps_20261019/STEPS_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='steps'}))

if __name__=='__main__':main()
