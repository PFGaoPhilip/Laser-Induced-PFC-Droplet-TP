"""Refresh Chapter 1 equation units without rebuilding unrelated lesson pages."""
import json
from pathlib import Path
from bs4 import BeautifulSoup
from build_course import ROOT, load_chapters, render_html, markdown_source, filename, EQUATIONS

def main():
    old=json.loads((ROOT/'verification/equations.json').read_text(encoding='utf-8'))
    chapters=load_chapters()
    assert EQUATIONS==old,'Layout changes must preserve every equation registry record'
    chapter=next(c for c in chapters if c['number']==1)
    raw=BeautifulSoup(chapter['body'],'html.parser')
    units=raw.select('.equation-unit')
    rendered=BeautifulSoup(render_html(''.join(str(u) for u in units)),'html.parser')
    path=ROOT/'chapters'/filename(chapter)
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    for unit in rendered.select('.equation-unit'):
        heading=unit.select_one('.equation-heading')
        for node in list(heading.children):
            if not getattr(node,'name',None):node.extract()
        oldunit=soup.find(id=unit['id'])
        assert oldunit is not None
        oldunit.replace_with(unit)
    path.write_bytes(str(soup).encode('utf-8'))
    (ROOT/'text'/filename(chapter).replace('.html','.md')).write_text(markdown_source(chapter),encoding='utf-8')
    (ROOT/'text/course.md').write_text('\n\n---\n\n'.join((ROOT/'text'/filename(c).replace('.html','.md')).read_text(encoding='utf-8') for c in chapters),encoding='utf-8')
    # Keep generated notation prose consistent with the bilingual source correction.
    path=ROOT/'reference/notation.html'
    text=path.read_text(encoding='utf-8').replace('每个方程注明依据，并提前定义符号。各章公式之后附变量示意图。未标尺寸的图为示意图。',
          '每个方程注明依据，并附局部符号定义。第1章将紧凑符号表置于公式之后。各公式组之后附变量示意图。未标尺寸的图为示意图。')
    path.write_bytes(text.encode('utf-8'))
    print(json.dumps({'chapter01_units_refreshed':len(units),'all_equation_registry_records_unchanged':len(EQUATIONS)}))

if __name__=='__main__':main()
