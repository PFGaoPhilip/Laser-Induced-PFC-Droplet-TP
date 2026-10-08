"""Meaningful integration gates for equations, bilingual structure and forwarding."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
import json
import re
import hashlib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from build_course import UNIT_MAP

ROOT=Path(__file__).resolve().parents[1]
checks=[]

def check(name,condition,detail=None):
    checks.append({'name':name,'passed':bool(condition),'detail':detail})

def main():
    settings=json.loads((ROOT/'COURSE_SETTINGS.json').read_text(encoding='utf-8'))
    units=settings['chapters']+settings.get('appendices',[])
    eqs=json.loads((ROOT/'verification/equations.json').read_text(encoding='utf-8'))
    paths=[ROOT/'index.html',*(ROOT/c['file'] for c in units),*sorted((ROOT/'reference').glob('*.html'))]
    docs={p:BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser') for p in paths}
    ids={p:{n['id'] for n in soup.select('[id]')} for p,soup in docs.items()}
    check('Four main chapters',len(settings['chapters'])==4)
    check('Appendix A is separate',len(settings.get('appendices',[]))==1 and settings['appendices'][0]['id']=='A')
    check('Exactly fifteen unit-defense questions',sum(len(c['defense_ids']) for c in units)==15)
    check('All equation IDs unique',len({e['id'] for e in eqs})==len(eqs))
    check('Source copy unchanged',hashlib.sha256((ROOT/'sources/Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md').read_bytes()).hexdigest()==settings['source_sha256'])
    check('Comparison copy unchanged',hashlib.sha256((ROOT/'sources/Cavitation_Course_Before_After_Comparison_EN_ZH.md').read_bytes()).hexdigest()==settings['comparison_sha256'])
    check('No automatic keyword mastery',settings['mastery_policy']['automatic_keyword_grading'] is False)
    displays=0;dependency_count=0;paired_count=0;html_rows=[]
    for p,soup in docs.items():
        rel=p.relative_to(ROOT).as_posix()
        check(rel+': day/night component',any('course-theme.js' in n.get('src','') for n in soup.select('script[src]')))
        check(rel+': no rendering errors',not soup.select('.katex-error'))
        allids=[n['id'] for n in soup.select('[id]')]
        check(rel+': unique DOM anchors',len(allids)==len(set(allids)))
        for group in soup.select('.lang-pair'):
            ps=group.find_all('p',recursive=False)
            check(rel+': bilingual paragraph pair',len(ps)==2 and ps[0].get('lang')=='en' and ps[1].get('lang')=='zh-CN')
            paired_count+=1
        for unit in soup.select('.equation-unit'):
            displays+=1
            symbols=unit.select_one('.symbols')
            formula=unit.select_one('.math-display')
            ordered=[n for n in unit.children if getattr(n,'name',None)]
            check(unit['id']+': local bilingual symbols before math',symbols is not None and formula is not None and ordered.index(symbols)<ordered.index(formula))
            check(unit['id']+': immediate physical-variable figure',formula is not None and formula.find_next_sibling().name=='figure' and 'formula-figure' in formula.find_next_sibling().get('class',[]))
            check(unit['id']+': static readable math and MathML',bool(formula and formula.select_one('.katex-html') and formula.select_one('math')))
        for n in soup.select('[src],link[href],a[href]'):
            val=n.get('src') or n.get('href')
            if not val:continue
            u=urlsplit(val)
            if u.scheme or u.netloc:
                if n.name in ['img','script'] or n.name=='link' and 'stylesheet' in n.get('rel',[]):check(rel+': no essential remote dependency',False,val)
                continue
            target=(p.parent/unquote(u.path)).resolve() if u.path else p
            check(rel+': local dependency '+val,target.exists())
            dependency_count+=1
            if u.fragment and target in ids:check(rel+': anchor '+val,unquote(u.fragment) in ids[target])
        html_rows.append({'file':rel,'bytes':p.stat().st_size,'equations':len(soup.select('.equation-unit')),'defenses':len(soup.select('article[data-defense]'))})
    check('Every registry display rendered once',displays==len(eqs),{'rendered':displays,'registered':len(eqs)})
    for ch in units:
        p=ROOT/ch['file'];soup=docs[p]
        glossaries=soup.select('table.symbol-glossary')
        check(ch['id']+': one detailed symbol glossary',len(glossaries)==1)
        if glossaries:
            for row in glossaries[0].select('tbody tr'):
                cells=row.find_all('td',recursive=False)
                annotation=cells[0].select_one('annotation[encoding="application/x-tex"]') if cells else None
                outside_subscripts=re.sub(r'\{[^{}]*\}','',annotation.get_text()) if annotation else ',;'
                check(ch['id']+': one variable per glossary row',len(cells)==4 and annotation is not None and ',' not in outside_subscripts and ';' not in outside_subscripts)
                check(ch['id']+': individual bilingual meaning and role',len(cells)==4 and len(cells[1].select('.lang-pair > p'))==2 and len(cells[3].select('.lang-pair > p'))==2 and bool(cells[2].get_text(strip=True)))
        check(ch['id']+': no Chapter 5 label',not re.search(r'Chapter\s+5\b|第\s*5\s*章|第五章',soup.get_text(' ',strip=True),re.I))
        check(ch['id']+': exactly three questions',len(soup.select('article[data-defense]'))==3)
        check(ch['id']+': expected IDs',[n['data-defense'] for n in soup.select('article[data-defense]')]==ch['defense_ids'])
        for defense in soup.select('article[data-defense]'):
            ans=defense.select_one('details.answer')
            content=[n for n in ans.children if getattr(n,'name',None) and n.name!='summary' and n.get('aria-hidden')!='true'] if ans else []
            check(defense['id']+': formula-first reference',bool(content and 'equation-unit' in content[0].get('class',[])))
            check(defense['id']+': semantic rubric',len(ans.select('li'))>=3 if ans else False)
    for legacy in settings.get('legacy_routes',[]):
        old=ROOT/legacy['file'];canonical=ROOT/legacy['canonical']
        check('Legacy hydrogel link shows updated Appendix A',old.is_file() and old.read_bytes()==canonical.read_bytes())
        if old.is_file():
            old_soup=BeautifulSoup(old.read_text(encoding='utf-8'),'html.parser')
            check('Legacy question and equation bookmarks preserved',all(old_soup.find(id=identifier) is not None for identifier in ['C5-Q1','C5-Q2','C5-Q3',*[f'C5-E{i:02d}' for i in range(1,25)]]))
    # Exact mapping cells plus the user's no-old-course-code constraint.
    mapping_locations=[(ROOT/'index.html','all',list(range(1,6)))]
    mapping_locations+=[(ROOT/ch['file'],ch['id'],[i+1]) for i,ch in enumerate(units)]
    for p,label,numbers in mapping_locations:
        region=docs[p].select_one(f'[data-unit-map="{label}"]')
        rows=region.select('tbody tr') if region else []
        check(label+': correspondence row count',len(rows)==len(numbers))
        for row,n in zip(rows,numbers):
            cells=row.find_all('td',recursive=False)
            for j,expected in enumerate(UNIT_MAP[n]):
                actual=tuple(x.get_text().strip() for x in cells[j].select('.lang-pair > p'))
                check(label+f': map row {n} column {j+1}',actual==expected,{'actual':actual,'expected':expected})
            material=cells[1].get_text(' ',strip=True)
            check(label+': main-material column has no old course identifiers',not re.search(r'\b[GJLTMA]\s*[-–]?\d{1,2}\b|Appendix\s*[AB]|附录\s*[AB]|[GJLT]系列',material),material)
    svg_rows=[]
    for eq in eqs:
        p=ROOT/'assets/figures'/f'{eq["id"].lower()}.svg'
        root=ET.fromstring(p.read_text(encoding='utf-8'))
        vb=[float(v) for v in root.attrib['viewBox'].split()]
        texts=root.findall('.//{http://www.w3.org/2000/svg}text')
        check(eq['id']+': SVG text within vertical bounds',all(float(t.attrib.get('y',0))<vb[3] for t in texts))
        check(eq['id']+': figure labels retained',len(eq['diagram'].get('labels',[]))>0 and len(texts)>=len(eq['diagram']['labels']))
        check(eq['id']+': no control characters in math',not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',eq['tex']))
        check(eq['id']+': Newton radius notation',not re.search(r'\\frac\{d\^?2?R\}\{dt\^?2?\}',eq['tex']))
        svg_rows.append({'id':eq['id'],'kind':eq['diagram']['type'],'labels':len(eq['diagram']['labels']),'height':vb[3]})
    css=(ROOT/'assets/vendor/katex/katex.min.css').read_text(encoding='utf-8')
    fonts=re.findall(r'url\(([^)]+)\)',css)
    for font in fonts:check('Local math font '+font,(ROOT/'assets/vendor/katex'/font.strip('"\'')).exists())
    high=ROOT/'verification/bilingual-terms.json'
    if high.exists():
        report=json.loads(high.read_text(encoding='utf-8'))
        check('Term-pair audit: zero one-sided marks',report['strict_pair_audit']['one_sided_colored_terms_remaining']==0)
        check('Distinct concepts have different pair colors',report['no_distinct_terms_share_a_color_in_any_paired_prose_group'])
    else:check('Term color audit exists',False)
    failure=[x for x in checks if not x['passed']]
    report={'status':'passed' if not failure else 'failed','check_count':len(checks),'failures':failure,'checks':checks,'chapters':len(settings['chapters']),'appendices':len(settings.get('appendices',[])),'chapter_questions':sum(len(c['defense_ids']) for c in units),'displayed_equations':displays,'bilingual_paragraph_pairs':paired_count,'local_dependencies':dependency_count,'local_math_fonts':len(fonts),'pages':html_rows,'figure_review':svg_rows,
      'scope':'Integration/structure/math-rendering/portability gates. Scientific calculation and semantic reviews are separate chapter and cross-review reports; these counts are not experimental validation.'}
    (ROOT/'verification/course-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','chapters','chapter_questions','displayed_equations','bilingual_paragraph_pairs','local_dependencies']}))
    if failure:print(json.dumps(failure[:12],ensure_ascii=False));sys_exit=1
    else:sys_exit=0
    raise SystemExit(sys_exit)

if __name__=='__main__':main()
