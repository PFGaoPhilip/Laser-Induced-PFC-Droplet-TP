"""Portable, pre-rendered equation reader and complete editable LaTeX source."""
import hashlib,html,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
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


def main():
    REQUESTS.clear();build=ROOT/'build';build.mkdir(exist_ok=True)
    documents=[('comparison','REPORT.md'),('derivation','DERIVATION.md'),('handoff','IMPLEMENTATION_HANDOFF.md'),('sources','SOURCES.md')]
    sections=[];sources={}
    for name,path in documents:
        source=(ROOT/path).read_text(encoding='utf8');sources[path]=hashlib.sha256(source.encode()).hexdigest()
        sections.append(f'<section id="{name}" class="document"'+('' if name=='comparison' else ' hidden')+'>'+render(source,'html')+'</section>')
    tex=PREAMBLE+render((ROOT/'DERIVATION.md').read_text(encoding='utf8'),'tex')+'\n\\newpage\n'+render((ROOT/'SOURCES.md').read_text(encoding='utf8'),'tex')+'\n\\end{document}\n'
    (ROOT/'DERIVATION.tex').write_text(tex,encoding='utf8')
    (build/'math_requests.json').write_text(json.dumps(REQUESTS),encoding='utf8')
    result=subprocess.run(['node',str(ROOT/'scripts/prerender_math.cjs'),str(build/'math_requests.json'),str(build/'math_rendered.json')],capture_output=True,text=True,check=True)
    rendered=json.loads((build/'math_rendered.json').read_text(encoding='utf8'))
    body='\n'.join(sections)
    for item in rendered:body=body.replace(item['token'],item['html'])
    states=(ROOT/'data/reader_states.json').read_text(encoding='utf8')
    page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Embedded PFC feasibility and parameters</title>
<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/reader.css"></head><body>
<header><a class="brand" href="#comparison">PFC / Hydrogel</a><nav aria-label="Documents"><a href="https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/">Theory course</a><button data-doc="comparison" aria-pressed="true">Comparison</button><button data-doc="derivation" aria-pressed="false">Derivation</button><button data-doc="handoff" aria-pressed="false">Implementation</button><button data-doc="sources" aria-pressed="false">Sources</button></nav><button id="theme-toggle" type="button">Night mode</button></header>
<main><div class="status">Conditional finite-PFC controls numerically verified. Target laser activation, fracture/channel formation, collapse jets and impact pressure remain unvalidated.</div>
<div class="downloads"><a href="Embedded_PFC_Feasibility_Public_20261011.zip">Download study folder</a><a href="output/pdf/FINITE_PFC_DERIVATION.pdf">Printable derivation</a><a href="DERIVATION.tex">LaTeX source</a><a href="REPORT.md">Report source</a><a href="README.md">Reproduce</a></div>
<section id="selector"><h2>Compare a calculated phase/mechanical state</h2><p>Choose among the solved equilibrium controls at stretch 2.1 and stipulated outer tension 54 mN/m. These state energies are not optical activation thresholds.</p>
<div class="controls"><label>PFC species<select id="fluid"><option value="n-Perfluoropentane">PFP</option><option value="n-Perfluorohexane">PFH</option></select></label><label>Initial liquid diameter (µm)<select id="diameter"><option>0.3</option><option selected>0.6</option><option>3</option><option>6</option><option>12</option></select></label><label>Stipulated shear modulus (kPa)<select id="modulus"><option>5</option><option selected>20</option><option>100</option></select></label></div><div id="state-output" aria-live="polite"></div>
<p class="small">Uniform-temperature, curved-equilibrium PFC; finite mass and surviving liquid shell; infinite intact gel. No nucleation, fracture or outlet is inferred.</p></section>
@@BODY@@<footer>Offline equations, plots, fonts and selector data are bundled. Scientific source links are optional external references. Numerical verification and specimen-level physical validation are distinct.</footer></main>
<script type="application/json" id="state-data">@@DATA@@</script><script src="assets/reader.js"></script></body></html>'''
    (ROOT/'index.html').write_text(page.replace('@@BODY@@',body).replace('@@DATA@@',states),encoding='utf8')
    audit=dict(source_hashes=sources,rendered_expressions=len(rendered),display_equations=sum(x['display'] for x in REQUESTS),katex_errors=0,offline_dependencies=True,renderer=json.loads(result.stdout))
    assert audit['display_equations']==32
    (ROOT/'verification/DOCUMENT_BUILD.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
    print(json.dumps(audit))

if __name__=='__main__':main()
