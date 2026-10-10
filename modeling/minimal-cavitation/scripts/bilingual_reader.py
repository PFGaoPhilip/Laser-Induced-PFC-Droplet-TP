"""Offline whole-page language editions using the reference course's term colors."""
from __future__ import annotations
import html
import re
from pathlib import Path
import markdown
from bs4 import BeautifulSoup, Comment, NavigableString
ROOT = Path(__file__).resolve().parents[1]
TERMS = [
 ('cavitation','cavitation / 空化',['laser-induced cavitation','cavitation','空化']),
 ('hydrogel','hydrogel / 水凝胶',['hydrogels','hydrogel','水凝胶']),
 ('confinement','confinement / 约束',['confinement','confined','约束']),
 ('jet-speed','jet speed / 射流速度',['jet velocity','jet speed','outlet speed','射流速度','出口速度']),
 ('jet','jet / 射流',['jetting','jets','jet','射流']),
 ('inertia','inertia / 惯性',['inertance','inertia','流体惯性','惯性']),
 ('kinetic-energy','kinetic energy / 动能',['kinetic energy','动能']),
 ('energy-budget','energy budget / 能量预算',['available work','energy accounting','energy budget','available energy','可用功','能量收支','能量预算']),
 ('equation-of-state','equation of state / 状态方程',['equation of state','EOS','状态方程']),
 ('pressure-impulse','pressure impulse / 冲量',['emitted impulse','axial impulse','pressure impulse','排出冲量','轴向冲量']),
 ('neo-hookean','neo-Hookean / 新胡克',['neo-Hookean','新胡克']),
 ('viscoelasticity','viscoelasticity / 黏弹性',['viscoelasticity','viscoelastic','黏弹性','粘弹性']),
 ('viscosity','viscosity / 黏度',['viscosity','viscous','黏度','粘度','黏性','粘性']),
 ('surface-tension','surface tension / 表面张力',['surface tension','表面张力']),
 ('capillary-pressure','capillary pressure / 毛细压力',['capillary pressure','capillary resistance','毛细压力','毛细阻力']),
 ('nucleation','nucleation / 成核',['nucleation','成核']),
 ('vaporization','vaporization / 汽化',['vaporization','汽化']),
 ('pfc','perfluorocarbon / 全氟碳',['perfluorocarbon','PFC','PFP','全氟碳']),
 ('phase-inventory','phase inventory / 相存量',['phase inventory','相存量']),
 ('mach-number','Mach number / 马赫数',['Mach','马赫数']),
 ('momentum','momentum / 动量',['momentum','动量']),
 ('rigid-wall','rigid wall / 刚性壁面',['rigid wall','rigid chamber','刚性壁面','刚性腔室']),
 ('traction','traction / 牵引',['traction','牵引']),
]
ALIASES = {alias.casefold():(key,title) for key,title,aliases in TERMS for alias in aliases}
def _pattern(alias):
    if re.search('[A-Za-z]',alias):
        return r'(?<![A-Za-z0-9_])'+re.escape(alias)+r'(?![A-Za-z0-9_])'
    return re.escape(alias)
TERM_RE = re.compile('|'.join(_pattern(a) for a in sorted(ALIASES,key=len,reverse=True)),re.I)

def highlight_terms(markup):
    soup=BeautifulSoup(markup,'html.parser')
    for node in list(soup.find_all(string=True)):
        if isinstance(node,Comment) or not isinstance(node,NavigableString): continue
        if any(p.name in ('code','pre','script','style','button','title','annotation','math')
               or 'math' in p.get('class',[]) or 'technical-term' in p.get('class',[]) for p in node.parents): continue
        value=str(node);matches=list(TERM_RE.finditer(value))
        if not matches: continue
        pieces=[];offset=0
        for match in matches:
            pieces.append(NavigableString(value[offset:match.start()]))
            key,title=ALIASES[match.group().casefold()]
            term=soup.new_tag('span',attrs={'class':'keyword technical-term','data-term':key,'title':title})
            term.string=match.group();pieces.append(term);offset=match.end()
        pieces.append(NavigableString(value[offset:]))
        for piece in pieces: node.insert_before(piece)
        node.extract()
    return str(soup)

def copy_term_style():
    css=(ROOT/'sources/interface-reference/theory-4-bilingual-terms.css.txt').read_text(encoding='utf-8')
    css=css.replace('html[data-theme="light"]','html[data-theme="day"]')
    css+='\n.technical-term{border-radius:3px;padding:0 .1em;font-weight:600}\n'
    (ROOT/'assets/terms.css').write_text(css,encoding='utf-8')

def edition(markup,locale):
    soup=BeautifulSoup(highlight_terms(markup),'html.parser');mapping={};outline=0
    for node in soup.find_all(id=True):
        old=node['id'];canonical=old
        if node.name in ('h1','h2','h3') and not re.fullmatch(r'(section-[a-f]|references)',old):
            outline+=1;canonical=f'outline-{outline}'
        mapping[old]=f'{locale}-{canonical}';node['id']=mapping[old];node['data-anchor']=canonical
    for node in soup.find_all('a',href=True):
        href=node['href']
        if href.startswith('#'): node['href']='#'+mapping.get(href[1:],f'{locale}-{href[1:]}')
        elif re.match(r'(?:index|STEP_BY_STEP)\.html#',href):
            path,anchor=href.split('#',1);node['href']=path+'#'+locale+'-'+anchor
        if locale=='zh':
            for original,translated in [('STEP_BY_STEP.md','STEP_BY_STEP.zh.md'),('MODEL_SPEC.md','MODEL_SPEC.zh.md'),('RESULTS.md','RESULTS.zh.md')]:
                if node['href']==original: node['href']=translated
    if locale=='zh':
        for node in soup.find_all(['img','a']):
            key='src' if node.name=='img' else 'href'
            target=node.get(key,'')
            if target.startswith('assets/') and target.endswith(('.png','.svg')):
                candidate=Path(target).with_name(Path(target).stem+'.zh'+Path(target).suffix)
                if (ROOT/candidate).is_file():node[key]=candidate.as_posix()
    hidden=' hidden' if locale=='en' else '';language='en' if locale=='en' else 'zh-CN' 
    return f'<div class="locale-pane" data-locale="{locale}" lang="{language}"{hidden}>'+str(soup)+'</div>'

def page(filename,title,english,chinese,css=(),scripts=()):
    copy_term_style()
    head=''.join(f'<link rel="stylesheet" href="{p}">' for p in ['assets/reader.css','assets/terms.css','assets/interface.css',*css])
    js=''.join(f'<script src="{p}"></script>' for p in ['assets/theme.js',*scripts])
    controls='<div class="reader-controls" aria-label="阅读设置"><button id="language" type="button" aria-label="切换到 English">English</button><button id="theme" type="button" aria-label="切换到日间模式">日间模式</button></div>'
    body_class='guide-page' if filename=='STEP_BY_STEP.html' else 'report-page'
    doc='<!doctype html><html lang="zh-CN" data-language="zh" data-theme="night"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title>'+head+'</head><body class="'+body_class+'">'+edition(english,'en')+edition(chinese,'zh')+controls+js+'</body></html>'
    (ROOT/filename).write_text(doc,encoding='utf-8')

def guide_body(source,locale):
    zh=locale=='zh';soup=BeautifulSoup(markdown.markdown(source,extensions=['tables','fenced_code']),'html.parser')
    first=soup.find('h1')
    if first: first.decompose()
    output=[];cards=[];sections=[];current=None
    for node in list(soup.children):
        if getattr(node,'name',None)=='h3':
            match=re.fullmatch(r'(?:Step|步骤)\s+(\d+)\s+—\s+(.+)',node.get_text(' ',strip=True))
            if not match: raise ValueError('Unexpected step heading: '+node.get_text())
            number,title=int(match[1]),match[2]
            current=soup.new_tag('article',attrs={'class':'guide-step','id':f'step-{number:02d}'})
            head=soup.new_tag('div',attrs={'class':'step-heading'})
            label=f'标记步骤 {number:02d} 已完成' if zh else f'Mark Step {number:02d} complete'
            check=soup.new_tag('input',attrs={'type':'checkbox','data-step':str(number),'id':f'check-{number:02d}','aria-label':label})
            badge=soup.new_tag('span',attrs={'class':'step-number'});badge.string=f'{number:02d}'
            title_node=soup.new_tag('h3');title_node.string=title
            head.append(check);head.append(badge);head.append(title_node);current.append(head)
            output.append(current);cards.append(number)
        elif getattr(node,'name',None)=='h2':
            current=None;text=node.get_text(' ',strip=True)
            ident='section-'+text[0].lower() if re.match(r'^[A-F] —',text) else 'references'
            node['id']=ident;node['class']='guide-section';output.append(node);sections.append((ident,text))
        elif current is not None: current.append(node)
        else: output.append(node)
    if cards!=list(range(1,54)): raise AssertionError('Expected all 53 translated steps')
    labels={'位置':'where','检查':'check','对照检查':'check-against','操作':'do','输入':'enter','排错':'if-stuck','原因':'why','完成记录':'completion-record'}
    for article in output:
        if getattr(article,'name',None)!='article': continue
        if not any(re.search(r'(^Check|检查|核查|核对)',n.get_text()) for n in article.find_all('strong')):
            raise AssertionError('Each translated card needs a check: '+article['id'])
        for p in article.find_all('p'):
            strong=p.find('strong',recursive=False)
            if strong:
                word=re.split('[:：]',strong.get_text())[0]
                klass=next((v for k,v in labels.items() if word.startswith(k)),word.lower().replace(' ','-'))
                if re.search('检查|核查|核对',word):klass='check'
                p['class']='guide-'+klass
    for pre in [e for node in output if hasattr(node,'find_all') for e in node.find_all('pre')]:
        button=soup.new_tag('button',attrs={'class':'copy-block','type':'button'});button.string='复制文本' if zh else 'Copy text';pre.insert_before(button)
    for table in [e for node in output if hasattr(node,'find_all') for e in node.find_all('table')]: table['class']='guide-table'
    nav=''.join('<a href="#'+ident+'">'+html.escape(text)+'</a>' for ident,text in sections if ident!='references')
    if zh:
        header='<header><p class="eyebrow">COMSOL 6.4 · 从空白模型开始 · 53 个操作步骤</p><h1>一步步建立两个简洁模型</h1><p>明确输入、逐步检查、保存节点与结果定义。</p><nav><a href="index.html">结果与完整理论</a><a href="STEP_BY_STEP.zh.md">中文 Markdown</a><a href="resources/gui/">输入文件</a><a href="#step-01">从步骤 01 开始</a><a href="#step-32">水凝胶模型</a><a href="#step-51">排错</a></nav></header>'
        progress,reset,bar='已完成 0 / 53 步','重置勾选','已完成步骤'
        footer='参数、变量与方程表来自两个已通过验证的原生模型。插图为示意图。阅读资源与输入文件均包含在本文件夹内。'
    else:
        header='<header><p class="eyebrow">COMSOL 6.4 · From a blank model · 53 numbered steps</p><h1>Build the two minimal models,<br>step by step</h1><p>Exact entries, visible checks, saved checkpoints and defined outputs.</p><nav><a href="index.html">Results &amp; full theory</a><a href="STEP_BY_STEP.md">Markdown guide</a><a href="resources/gui/">Input files</a><a href="#step-01">Start Step 01</a><a href="#step-32">Start hydrogel</a><a href="#step-51">Troubleshooting</a></nav></header>'
        progress,reset,bar='0 of 53 steps completed','Reset checks','Completed steps'
        footer='All parameter, variable and equation tables come from the two accepted native files. Figures labeled schematic are not screenshots. This folder includes its reader assets and import files.'
    toolbar='<div class="guide-toolbar"><div class="guide-toolbar-inner"><span data-guide-progress role="status">'+progress+'</span><progress data-guide-progress-bar max="53" value="0" aria-label="'+bar+'"></progress><button data-reset-progress type="button">'+reset+'</button></div><nav class="guide-section-nav">'+nav+'</nav></div>'
    return header+toolbar+'<main>'+''.join(str(e) for e in output)+'</main><footer>'+footer+'</footer>'

def write_guide(english):
    chinese='\n\n'.join((ROOT/'sources/i18n'/p).read_text(encoding='utf-8').strip() for p in ('guide-abc.zh.md','guide-def.zh.md'))+'\n'
    (ROOT/'STEP_BY_STEP.zh.md').write_text(chinese,encoding='utf-8')
    from figure_labels import localized_schematics
    localized_schematics(ROOT)
    page('STEP_BY_STEP.html','简洁空化与水凝胶模型 · 53 步 COMSOL 教程',guide_body(english,'en'),guide_body(chinese,'zh'),css=('assets/guide.css',),scripts=('assets/guide.js',))

def write_report(english,chinese):
    page('index.html','简洁空化与水凝胶模型 · 结果与完整推导',english,chinese,css=('assets/vendor/katex/katex.min.css',))
