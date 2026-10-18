"""Insert numbered reasoning steps while preserving rendered mathematical units."""
import json
import sys
from bs4 import BeautifulSoup
from build_course import ROOT, load_chapters, EQUATIONS, filename, markdown_source
sys.path.insert(0,str(ROOT/'content'))
from chapter01_step_roles import normalize_existing_steps

def main():
    registry=json.loads((ROOT/'verification/equations.json').read_text(encoding='utf-8'))
    chapters=load_chapters()
    assert EQUATIONS==registry
    chapter=next(c for c in chapters if c['number']==1)
    raw=BeautifulSoup(chapter['body'],'html.parser')
    path=ROOT/'chapters'/filename(chapter)
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    old_units=[str(u) for u in soup.select('.equation-unit')]
    for heading in raw.select('.derivation-step'):
        unit=soup.find(id=heading['data-step-for'])
        assert unit and not soup.select(f'[data-step-for="{unit["id"]}"]')
        derivation=unit.find_previous_sibling()
        assert derivation.get_text(strip=True).startswith('Derivation.')
        purpose=heading.find_next_sibling()
        assert 'step-purpose' in purpose.get('class',[])
        derivation.insert_before(BeautifulSoup(str(heading)+str(purpose),'html.parser'))
    target=soup.find(id='spherical-control').parent
    target.insert_before(BeautifulSoup(str(raw.select_one('.chapter-route')),'html.parser'))
    output=normalize_existing_steps(str(soup))
    parsed=BeautifulSoup(output,'html.parser')
    assert [str(u) for u in parsed.select('.equation-unit')]==old_units
    path.write_bytes(output.encode('utf-8'))
    (ROOT/'text'/filename(chapter).replace('.html','.md')).write_text(markdown_source(chapter),encoding='utf-8')
    (ROOT/'text/course.md').write_text('\n\n---\n\n'.join((ROOT/'text'/filename(c).replace('.html','.md')).read_text(encoding='utf-8') for c in chapters),encoding='utf-8')
    print(json.dumps({'numbered_steps':len(parsed.select('.derivation-step')),'rendered_equation_units_preserved':len(old_units),'registry_records_preserved':len(registry)}))

if __name__=='__main__':main()
