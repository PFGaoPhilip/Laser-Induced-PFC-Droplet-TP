"""Apply the owner's subsection labels without rerendering mathematical content."""
import hashlib
import json
import re
from bs4 import BeautifulSoup
from build_course import ROOT, load_chapters, EQUATIONS, markdown_source, filename
from equation_symbols import equation_label, relabel_chapter01_references

def main():
    path=ROOT/'chapters/01-cavity-pressure-inertia-and-directional-jets.html'
    source=path.read_text(encoding='utf-8')
    before=BeautifulSoup(source,'html.parser')
    after=BeautifulSoup(relabel_chapter01_references(source),'html.parser')
    for unit in after.select('.equation-unit'):
        label=equation_label(unit['id'])
        zh=unit.select_one('.equation-heading > p[lang="zh-CN"]')
        if not zh.get_text().startswith('('+label+')'):
            zh.insert(0,'('+label+') · ')
        section=re.match(r'\d+\.\d+',unit.find_previous('h2',lang='en').get_text(' ',strip=True))[0]
        assert label.startswith('C'+section+'-'),(unit['id'],section,label)
    protected='.katex,math,.technical-term'
    assert [str(n) for n in before.select(protected)]==[str(n) for n in after.select(protected)]
    def links(soup):return [(n.name,n.get('href'),n.get('src'),n.get('id')) for n in soup.select('[id],a,link,img,script')]
    assert links(before)==links(after)
    output=str(after)
    path.write_bytes(output.encode('utf-8'))
    highpath=ROOT/'verification/bilingual-terms.json'
    report=json.loads(highpath.read_text(encoding='utf-8'))
    record=next(r for r in report['checks'] if r['file']==path.relative_to(ROOT).as_posix())
    record['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    record['post_highlight_display_label_update']={'owner_request':'Use corresponding subchapters, such as C1.6 and C1.7','all_33_labels_match_containing_h2':True,'math_technical_marks_links_and_anchors_preserved':True}
    highpath.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    old=json.loads((ROOT/'verification/equations.json').read_text(encoding='utf-8'))
    chapters=load_chapters()
    assert EQUATIONS==old
    chapter=next(c for c in chapters if c['number']==1)
    (ROOT/'text'/filename(chapter).replace('.html','.md')).write_text(markdown_source(chapter),encoding='utf-8')
    (ROOT/'text/course.md').write_text('\n\n---\n\n'.join((ROOT/'text'/filename(c).replace('.html','.md')).read_text(encoding='utf-8') for c in chapters),encoding='utf-8')
    print(json.dumps({'subchapter_labels':33,'all_labels_match_containing_section':True,'mathematics_and_anchors_preserved':True}))

if __name__=='__main__':main()
