"""Portable, pre-rendered equation reader and complete editable LaTeX source."""
import hashlib,html,json,re,shutil,subprocess,tempfile
from pathlib import Path
from reader_text import translated_block
from reader_figures import translate_figures
ROOT=Path(__file__).resolve().parents[1]
COURSE=ROOT.parents[1]
REQUESTS=[]
TOKENS=re.compile(r'(\$[^$\n]+\$|`[^`]+`|\*\*.+?\*\*|!?\[[^\]]+\]\([^\)]+\))')


def tex_escape(text):
    mapping={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_',
             '{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}',
             'µ':r'\textmu{}','³':r'\textsuperscript{3}','²':r'\textsuperscript{2}',
             '×':r'\ensuremath{\times}','±':r'\ensuremath{\pm}','–':'-','—':' - ',
             '’':"'",'‘':"'",'“':'``','”':"''",'⁻':r'\textsuperscript{-}',
             '∞':r'\ensuremath{\infty}','≥':r'\ensuremath{\ge}','≤':r'\ensuremath{\le}'}
    return ''.join(mapping.get(c,c) for c in text)


def math_html(tex,display=False):
    token=f'@@MATH_{len(REQUESTS)}@@'
    REQUESTS.append(dict(token=token,tex=tex,display=display));return token


def inline(text,target):
    parts=[]
    for token in TOKENS.split(text):
        if not token:continue
        if token.startswith('$'):
            parts.append(token if target=='tex' else math_html(token[1:-1]))
        elif token.startswith('`'):
            parts.append(r'\path{'+token[1:-1]+'}' if target=='tex' else '<code>'+html.escape(token[1:-1])+'</code>')
        elif token.startswith('**'):
            content=inline(token[2:-2],target)
            parts.append(r'\textbf{'+content+'}' if target=='tex' else '<strong>'+content+'</strong>')
        elif token.startswith(('![','[')):
            image=token.startswith('!');label,dest=re.match(r'!?\[([^\]]+)\]\(([^\)]+)\)',token).groups()
            if image:
                parts.append(r'\includegraphics[width=\linewidth]{'+dest+'}' if target=='tex' else '<img class="figure" loading="lazy" src="'+html.escape(dest,quote=True)+'" alt="'+html.escape(label,quote=True)+'">')
            elif target=='tex':
                # The final PDF lives two levels below the document sources.
                pdf_dest=('../../'+dest) if not re.match(r'^[a-z]+:',dest) and not dest.startswith('#') else dest
                parts.append(r'\href{'+pdf_dest.replace('%',r'\%')+'}{'+inline(label,target)+'}')
            else:
                jump={'DERIVATION.md':'#derivation','IMPLEMENTATION_HANDOFF.md':'#handoff','SOURCES.md':'#sources'}.get(dest,dest)
                parts.append('<a href="'+html.escape(jump,quote=True)+'">'+inline(label,target)+'</a>')
        else:parts.append(tex_escape(token) if target=='tex' else html.escape(token))
    return ''.join(parts)


def blocks(source):
    lines=source.splitlines();idx=0
    while idx<len(lines):
        line=lines[idx]
        if not line.strip():idx+=1;continue
        if line=='$$':
            end=idx+1
            while end<len(lines) and lines[end]!='$$':end+=1
            if end==len(lines):raise ValueError('Unclosed display math')
            yield 'equation','\n'.join(lines[idx+1:end]);idx=end+1
        elif line.startswith('#'):
            m=re.match(r'(#+) (.*)',line);yield 'heading',(len(m[1]),m[2]);idx+=1
        elif line.startswith('|'):
            data=[]
            while idx<len(lines) and lines[idx].startswith('|'):
                row=[x.strip() for x in lines[idx].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[:\- ]+',x) for x in row):data.append(row)
                idx+=1
            yield 'table',data
        elif line.startswith('- '):
            data=[]
            while idx<len(lines) and lines[idx].startswith('- '):data.append(lines[idx][2:]);idx+=1
            yield 'list',data
        else:
            data=[line];idx+=1
            while idx<len(lines) and lines[idx].strip() and not lines[idx].startswith(('#','|','- ')) and lines[idx]!='$$':
                data.append(lines[idx]);idx+=1
            yield 'paragraph',' '.join(data)


PREAMBLE=r'''\documentclass[10pt,a4paper]{article}
\usepackage[margin=19mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,booktabs,longtable,array,microtype,needspace,graphicx,textcomp}
\usepackage{xurl}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\setlength{\tabcolsep}{4pt}
\setlength{\emergencystretch}{3em}
\allowdisplaybreaks[2]
\hypersetup{pdftitle={Finite-PFC embedding: complete reduced-model derivation},pdfauthor={Conditional model study}}
\begin{document}
'''


def render(source,target):
    out=[]
    for kind,v in blocks(source):
        if kind=='heading':
            level,title=v
            if target=='html':out.append(f'<h{level}>'+inline(title,target)+f'</h{level}>')
            elif level==1:out.append(r'\begin{center}\Large\bfseries '+inline(title,target)+r'\end{center}')
            else:out.append(r'\needspace{6\baselineskip}'+'\n'+('\\section*' if level==2 else '\\subsection*')+'{'+inline(title,target)+'}')
        elif kind=='paragraph':
            if target=='html':out.append('<p>'+inline(v,target)+'</p>')
            else:
                if v.startswith('**Symbols before'):out.append(r'\needspace{8\baselineskip}')
                out.append(inline(v,target)+'\n')
        elif kind=='equation':
            if target=='html':out.append('<div class="equation">'+math_html(v,True)+'</div>')
            else:
                body=v.strip()
                if body.startswith(r'\begin{aligned}') and body.endswith(r'\end{aligned}'):
                    body=body[len(r'\begin{aligned}'):-len(r'\end{aligned}')].strip()
                # Smaller print math preserves the complete long energy balances.
                out.append(r'{\small\begin{align*}'+'\n'+body+'\n'+r'\end{align*}}')
        elif kind=='table':
            count=len(v[0])
            if any(len(row)!=count for row in v):raise ValueError('Unequal table columns')
            if target=='html':
                head=''.join('<th scope="col">'+inline(c,target)+'</th>' for c in v[0])
                body=''.join('<tr>'+''.join('<td>'+inline(c,target)+'</td>' for c in row)+'</tr>' for row in v[1:])
                out.append('<div class="table-wrap"><table><thead><tr>'+head+'</tr></thead><tbody>'+body+'</tbody></table></div>')
            else:
                widths=[.31,.45,.18] if v[0][0]=='Symbol' else ([.08,.36,.50] if v[0][0]=='ID' else [.94/count]*count)
                spec=''.join(r'>{\raggedright\arraybackslash}p{'+str(x)+r'\linewidth}' for x in widths)
                out.append(r'\begin{longtable}{'+spec+'}\n'+r'\toprule')
                out.append(' & '.join(r'\textbf{'+inline(c,target)+'}' for c in v[0])+r'\\\midrule\endhead')
                out.extend(' & '.join(inline(c,target) for c in row)+r'\\[4pt]' for row in v[1:])
                out.append(r'\bottomrule\end{longtable}')
        elif kind=='list':
            out.append('<ul>'+''.join('<li>'+inline(x,target)+'</li>' for x in v)+'</ul>' if target=='html' else r'\begin{itemize}'+'\n'+'\n'.join(r'\item '+inline(x,target) for x in v)+'\n'+r'\end{itemize}')
    return '\n'.join(out)


def source_block(kind, value):
    """Serialize editable English/Chinese source without changing equations."""
    if kind=='heading': return '#' * value[0] + ' ' + value[1]
    if kind=='paragraph': return value
    if kind=='equation': return '$$\n'+value+'\n$$'
    if kind=='list': return '\n'.join('- '+item for item in value)
    if kind=='table':
        rows=['| '+' | '.join(row)+' |' for row in value]
        rows.insert(1,'|'+'|'.join('---' for _ in value[0])+'|')
        return '\n'.join(rows)
    raise ValueError(kind)


def pair(english,chinese,tag='span'):
    if english == chinese:
        return inline(english,'html')
    return ('<'+tag+' lang="en">'+inline(english,'html')+'</'+tag+'>'
            '<'+tag+' lang="zh-CN" class="zh">'+inline(chinese,'html')+'</'+tag+'>')


def render_bilingual(document,source):
    output=[];english_source=[];chinese_source=[];counts={'blocks':0,'paired':0,'tables':0}
    source_blocks=list(blocks(source))
    for index,(kind,value) in enumerate(source_blocks):
        en,zh=translated_block(document,index,kind,value)
        if (kind=='paragraph' and index+1<len(source_blocks)
                and source_blocks[index+1][0]=='equation'):
            formula=source_blocks[index+1][1]
            if r'\pi' in formula and not re.search(r'\bpi\b|\\pi',en,re.I):
                en+=' $\\pi$ is the dimensionless circle constant.'
            if r'\pi' in formula and '$\\pi$' not in zh and '圆周率' not in zh:
                zh+=' $\\pi$ 为无量纲圆周率。'
            if r'\tag{E15}' in formula:
                if '$b$ is the positive core radius' not in en:
                    en+=' $b$ is the positive core radius (m).'
                if '$b$ 为正蒸气核半径' not in zh:
                    zh+=' $b$ 为正蒸气核半径（m）。'
        english_source.append(source_block(kind,en));chinese_source.append(source_block(kind,zh))
        counts['blocks']+=1
        marker=f'data-source-block="{document}:{index}"'
        if kind=='equation':
            output.append('<div class="math-display equation" '+marker+'>'+math_html(value,True)+'</div>')
            continue
        counts['paired']+=1
        if kind=='heading':
            level,title=en
            level=min(level+1,6)
            output.append(f'<div class="heading-pair" {marker}>'+pair(title,zh[1],f'h{level}')+'</div>')
        elif kind=='paragraph':
            images=[re.fullmatch(r'!\[([^\]]+)\]\(([^\)]+)\)',text) for text in [en,zh]]
            if all(images):
                output.append('<figure '+marker+'>'+''.join(
                    '<img class="figure" lang="'+lang+'" loading="lazy" src="'+html.escape(image[2],quote=True)+'" alt="'+html.escape(image[1],quote=True)+'">'
                    for lang,image in zip(['en','zh-CN'],images))+'<figcaption>'+pair(images[0][1],images[1][1])+'</figcaption></figure>')
            else:
                output.append('<div class="lang-pair" '+marker+'>'+pair(en,zh,'p')+'</div>')
        elif kind=='list':
            output.append('<ul '+marker+'>'+''.join('<li>'+pair(a,b)+'</li>' for a,b in zip(en,zh))+'</ul>')
        elif kind=='table':
            counts['tables']+=1
            header=''.join('<th scope="col">'+pair(a,b)+'</th>' for a,b in zip(en[0],zh[0]))
            rows=''.join('<tr>'+''.join('<td>'+pair(a,b)+'</td>' for a,b in zip(aa,bb))+'</tr>' for aa,bb in zip(en[1:],zh[1:]))
            output.append('<div class="table-wrap" '+marker+'><table><thead><tr>'+header+'</tr></thead><tbody>'+rows+'</tbody></table></div>')
    return '\n'.join(output),'\n\n'.join(english_source)+'\n','\n\n'.join(chinese_source)+'\n',counts


def main():
    REQUESTS.clear()
    canonical_styles={}
    for name in ['course.css','course-language.css','bilingual-terms.css']:
        origin=COURSE/'assets'/name;destination=ROOT/'assets'/name
        if (COURSE/'chapters/01-cavity-pressure-inertia-and-directional-jets.html').is_file():
            shutil.copy2(origin,destination)
        if not destination.is_file():
            raise FileNotFoundError('Missing bundled canonical stylesheet: '+name)
        canonical_styles[name]=hashlib.sha256(destination.read_bytes()).hexdigest()
    figure_translations=translate_figures(ROOT)
    documents=[('comparison','REPORT.md'),('derivation','DERIVATION.md'),('handoff','IMPLEMENTATION_HANDOFF.md'),('sources','SOURCES.md')]
    sections=[];sources={};coverage={}
    for name,path in documents:
        source=(ROOT/path).read_text(encoding='utf8')
        rendered_document,en,zh,coverage[path]=render_bilingual(path,source)
        (ROOT/path).write_text(en,encoding='utf8')
        (ROOT/Path(path).with_suffix('.zh.md')).write_text(zh,encoding='utf8')
        sources[path]=hashlib.sha256(en.encode()).hexdigest()
        sources[str(Path(path).with_suffix('.zh.md'))]=hashlib.sha256(zh.encode()).hexdigest()
        sections.append(f'<section id="{name}" class="document"'+('' if name=='comparison' else ' hidden')+'>'+rendered_document+'</section>')
    # Keep the accepted original English PDF and its matching LaTeX untouched.
    # Temporary equation requests are removed after the static rendering step.
    with tempfile.TemporaryDirectory(prefix='embedded-reader-') as temp:
        build=Path(temp)
        (build/'math_requests.json').write_text(json.dumps(REQUESTS),encoding='utf8')
        result=subprocess.run(['node',str(ROOT/'scripts/prerender_math.cjs'),str(build/'math_requests.json'),str(build/'math_rendered.json')],capture_output=True,text=True,check=True)
        rendered=json.loads((build/'math_rendered.json').read_text(encoding='utf8'))
    body='\n'.join(sections)
    for item in rendered:body=body.replace(item['token'],item['html'])
    states=(ROOT/'data/reader_states.json').read_text(encoding='utf8')
    navigation_file=ROOT/'assets/course-navigation.json'
    if (COURSE/'COURSE_SETTINGS.json').is_file():
        settings=json.loads((COURSE/'COURSE_SETTINGS.json').read_text(encoding='utf8'))
        navigation=dict(url=settings['url'],units=[{key:unit[key] for key in ['file','label','label_zh','title','title_zh']} for unit in settings['chapters']+settings['appendices']])
        navigation_file.write_text(json.dumps(navigation,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    navigation=json.loads(navigation_file.read_text(encoding='utf8'))
    site=navigation['url']
    course_nav=''.join('<a data-course-path="'+unit['file']+'" href="'+site+unit['file']+'"><span lang="en">'+inline(unit['label']+' · '+unit['title'],'html')+'</span><span lang="zh-CN">'+inline(unit['label_zh']+' · '+unit['title_zh'],'html')+'</span></a>' for unit in navigation['units'])
    page='''<!doctype html><html lang="en" data-language="bilingual" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PFC droplets in hydrogel · Appendix A</title>
<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/course.css"><link rel="stylesheet" href="assets/course-language.css"><link rel="stylesheet" href="assets/bilingual-terms.css"><link rel="stylesheet" href="assets/reader.css"></head><body>
<div class="theme-tools" role="toolbar" aria-label="Reading controls / 阅读设置"><button id="theme-toggle" type="button"><span lang="en">Day mode</span><span lang="zh-CN">日间</span></button><button id="language-toggle" type="button" aria-label="Switch reading language">English</button></div>
<nav class="topbar" aria-label="Main navigation"><a class="brand" data-course-path="index.html" href="https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/index.html"><span lang="en">Laser PFC TP</span><span lang="zh-CN">激光 PFC 转印</span></a><a id="appendix-return" data-course-path="appendices/a-hydrogel-versus-liquid.html" href="https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/appendices/a-hydrogel-versus-liquid.html"><span lang="en">Appendix A</span><span lang="zh-CN">附录 A</span></a></nav>
<div class="page-layout"><aside class="sidebar"><h2><span lang="en">Course</span><span lang="zh-CN">课程</span></h2><nav aria-label="Chapters and appendix">@@COURSE_NAV@@</nav><h2><span lang="en">In this study</span><span lang="zh-CN">本研究内容</span></h2><nav class="reader-doc-nav" aria-label="Study documents / 研究文档"><button data-doc="comparison" aria-pressed="true"><span lang="en">Comparison</span><span lang="zh-CN">比较</span></button><button data-doc="derivation" aria-pressed="false"><span lang="en">Derivation</span><span lang="zh-CN">推导</span></button><button data-doc="handoff" aria-pressed="false"><span lang="en">Validation plan</span><span lang="zh-CN">验证计划</span></button><button data-doc="sources" aria-pressed="false"><span lang="en">Sources</span><span lang="zh-CN">来源</span></button></nav></aside>
<div class="reading"><header class="chapter-header"><p class="eyebrow"><span lang="en">Appendix A · Finite PFC study</span><span lang="zh-CN">附录 A · 有限 PFC 研究</span></p><h1 lang="en">PFC droplets in hydrogel</h1><h1 class="zh" lang="zh-CN">水凝胶中的 PFC 液滴</h1><div class="scope lang-pair"><p lang="en">Finite-PFC models pass numerical checks. Target laser activation, fracture, jets and impact pressure remain unresolved.</p><p class="zh" lang="zh-CN">有限 PFC 模型通过数值检验。目标激光激活、断裂、射流与冲击压力仍未解决。</p></div>
<div class="downloads resource-nav unit-resources"><a href="output/pdf/FINITE_PFC_DERIVATION.pdf"><span lang="en">Original English PDF</span><span lang="zh-CN">原始英文 PDF</span></a><a href="DERIVATION.tex"><span lang="en">Original LaTeX</span><span lang="zh-CN">原始 LaTeX</span></a><a href="REPORT.md"><span lang="en">English source</span><span lang="zh-CN">英文源文件</span></a><a href="REPORT.zh.md"><span lang="en">Chinese source</span><span lang="zh-CN">中文源文件</span></a><a href="README.md"><span lang="en">Reproduce</span><span lang="zh-CN">复现</span></a></div></header>
<main class="chapter-body"><section id="selector" class="worked"><div class="heading-pair"><h2 lang="en">Compare solved equilibrium states</h2><h2 class="zh" lang="zh-CN">比较已求解平衡状态</h2></div><div class="lang-pair"><p lang="en">Select a state at stretch 2.1 and outer tension 54 mN/m. State energy does not establish an optical activation threshold.</p><p class="zh" lang="zh-CN">选择伸长比 2.1、外张力 54 mN/m 的状态。状态能量无法确立光学激活阈值。</p></div>
<div class="controls"><label><span lang="en">PFC species</span><span lang="zh-CN">PFC 种类</span><select id="fluid"><option value="n-Perfluoropentane">PFP</option><option value="n-Perfluorohexane">PFH</option></select></label><label><span lang="en">Initial liquid diameter (µm)</span><span lang="zh-CN">初始液态直径 (µm)</span><select id="diameter"><option>0.3</option><option selected>0.6</option><option>3</option><option>6</option><option>12</option></select></label><label><span lang="en">Stipulated shear modulus (kPa)</span><span lang="zh-CN">预设剪切模量 (kPa)</span><select id="modulus"><option>5</option><option selected>20</option><option>100</option></select></label></div><div id="state-output" aria-live="polite"></div>
<div class="lang-pair small"><p lang="en">Finite PFC mass; surviving liquid shell; uniform temperature; curved phase equilibrium; infinite intact gel. Nucleation, fracture and outlets remain outside this control.</p><p class="zh" lang="zh-CN">有限 PFC 质量、剩余液体壳层、均匀温度、曲面相平衡及无限完整凝胶。成核、断裂与出口仍在该对照范围之外。</p></div></section>
@@BODY@@</main></div></div><footer class="site-footer"><div class="lang-pair"><p lang="en">Equations, plots, fonts and state data work offline. Move the entire study folder. Scholarly links are external references.</p><p class="zh" lang="zh-CN">方程、图表、字体与状态数据支持离线阅读。移动时请保留整个研究文件夹。论文链接为外部参考。</p></div></footer>
<script type="application/json" id="state-data">@@DATA@@</script><script src="assets/reader.js"></script></body></html>'''
    (ROOT/'index.html').write_text(page.replace('@@BODY@@',body).replace('@@DATA@@',states).replace('@@COURSE_NAV@@',course_nav),encoding='utf8')
    audit=dict(source_hashes=sources,rendered_expressions=len(rendered),display_equations=sum(x['display'] for x in REQUESTS),katex_errors=0,offline_dependencies=True,renderer=json.loads(result.stdout),bilingual_coverage=coverage,languages=['bilingual','en','zh'],accepted_english_pdf_preserved=True,figure_translations=figure_translations,canonical_styles=canonical_styles,frontend='canonical chapter layout; fixed lower-right theme-tools')
    assert audit['display_equations']==32
    (ROOT/'verification/BILINGUAL_DOCUMENT_BUILD_20261014.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
    print(json.dumps(audit))

if __name__=='__main__':main()
