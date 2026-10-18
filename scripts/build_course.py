"""Build the bilingual, portable five-chapter course and Appendix A (source number 90)."""
from pathlib import Path
from html import escape
import argparse
import importlib.util
import sys
import re
import json
import hashlib
import subprocess
import os
import shutil
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify
from coursekit import P, H, T, EQUATIONS
from draw_figures import svg_for
from source_catalog import SOURCES
from unit_resources import resource_links, resource_sections

ROOT=Path(__file__).resolve().parents[1]
NODE=Path(os.environ.get('NODE_BINARY') or shutil.which('node') or 'node')
TITLE='Laser Induced PFC Droplet TP'
TITLE_ZH='激光诱导 PFC 液滴转印'
SLUG='Laser-Induced-PFC-Droplet-TP'
BASE='https://pfgaophilip.github.io/'+SLUG+'/'
DATE='2026-10-14'
PLANNED=[
 (1,'cavitation-and-jet-foundations','Cavitation and the mechanics of a directional jet','空化与定向射流的力学基础'),
 (2,'laser-heat-and-finite-pfc-inventory','Laser heating and finite PFC phase inventory','激光加热与有限 PFC 相存量'),
 (3,'arrays-to-coherent-jets-and-loads','From droplet arrays to coherent jets and defined loads','从液滴阵列到相干射流与明确载荷'),
 (4,'load-path-fracture-and-intact-transfer','Load paths, fracture and intact transfer','受力路径、断裂与完整转印'),
 (5,'jet-on-rigid-wall','Jet on a rigid wall: theory, calculation and verification','刚性壁面射流：理论、计算与核验'),
 (90,'hydrogel-versus-liquid-platforms','Hydrogel and conventional liquid platforms','水凝胶与常规液体平台'),
]
UNIT_MAP = {
 1:[('Chapter 1: Cavitation and jets','第1章：空化与射流基础'),('Spherical cavity dynamics, liquid inertia, pressure impulse, moving interfaces, and directional jet formation.','球形腔体动力学、液体惯性、压力冲量、运动界面与定向射流形成。'),('How does cavity pressure accelerate liquid, and why does a directional jet require asymmetry?','腔体压力如何加速液体？为什么形成定向射流必须有不对称性？')],
 2:[('Chapter 2: PFC versus ordinary droplets','第2章：PFC与普通液滴对比'),('Laser heating, nucleation, heat and mass transfer, material properties, and finite phase inventory.','激光加热、成核、传热传质、物性与有限相存量。'),('What changes when PFC replaces an ordinary droplet?','用 PFC 替代普通液滴会改变什么？')],
 3:[('Chapter 3: Arrays and calculations','第3章：阵列与计算'),('Array coupling, energy allocation, finite jets, impact, and the three-stage resolver.','阵列耦合、能量分配、有限射流、冲击与三阶段求解器。'),('How do array sites produce a finite mechanical output?','阵列位点如何产生有限力学输出？')],
 4:[('Chapter 4: Fracture and transfer','第4章：断裂与转印'),('Film/PVC loading, transient structural response, interface separation, and transfer criteria.','薄膜／PVC受载、瞬态结构响应、界面分离与转印判据。'),('Does the delivered load release the intended interface without destroying the payload?','实际传递的载荷能否释放目标界面，同时不损坏被转印对象？')],
 5:[('Chapter 5: Jet-on-Rigid-Wall Calculation','第5章：刚性壁面射流计算'),('Liquid-only impact theory, a finite-volume reference, and an axisymmetric COMSOL wall-band verification.','纯液体撞击理论、有限体积参考解与轴对称 COMSOL 壁面加密带核验。'),('What wall pressure can a rigid-wall jet reach, and how well do two independent solvers agree?','射流撞击刚性壁面可达到多大的壁面压力？两个独立求解器的一致性如何？')],
 90:[('Appendix A: Hydrogel versus liquid','附录A：水凝胶与液体平台'),('Gel confinement, response times, finite-energy models, and embedded-PFC comparisons.','凝胶约束、响应时间、有限能量模型与嵌入式 PFC 比较。'),('How does gel confinement change transfer?','凝胶约束如何改变转印？')],
}
MAP_HEADERS=[('Unit','单元'),('Contents','内容'),('Question','问题')]

def unit_map(numbers):
    rows=[]
    for n in numbers:
        row=list(UNIT_MAP[n]);row[0]=tuple('<strong>'+escape(x)+'</strong>' for x in row[0]);rows.append(row)
    return T(MAP_HEADERS,rows)

def load_chapters(partial=False,only=None):
    result=[]
    for n,slug,en,zh in PLANNED:
        if only and n not in only:continue
        p=ROOT/f'content/chapter{n:02d}.py'
        if not p.exists():
            if partial:continue
            raise FileNotFoundError(p)
        spec=importlib.util.spec_from_file_location(f'chapter{n:02d}',p)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        ch=mod.CHAPTER
        assert ch['number']==n,(p,ch['number'])
        assert len(ch['question_ids'])==3,(p,ch.get('question_ids'))
        result.append(ch)
    return result

def is_appendix(ch):return ch.get('kind')=='appendix'

def unit_id(ch):return ch['letter'] if is_appendix(ch) else f'C{ch["number"]:02d}'

def unit_label(ch):
    return ('Appendix '+ch['letter'],'附录 '+ch['letter']) if is_appendix(ch) else ('Chapter '+str(ch['number']),'第 '+str(ch['number'])+' 章')

def filename(ch):
    return f'{ch["number"]:02d}-'+re.sub(r'^\d{2}-','',ch['slug'])+'.html'

def route(ch):return ('appendices/' if is_appendix(ch) else 'chapters/')+filename(ch)

def course_units(config):return config['chapters']+config.get('appendices',[])

def render_html(source):
    """Render both display and inline math; outputs need no runtime/CDN renderer."""
    soup=BeautifulSoup(source,'html.parser')
    placeholders=[]
    for div in soup.select('.math-display[data-tex]'):
        placeholders.append((div,div['data-tex'],True))
    skipped={'script','style','code','pre','textarea','math','svg','head'}
    for node in list(soup.find_all(string=True)):
        if not isinstance(node,NavigableString) or not '$' in str(node):continue
        if any(p.name in skipped or 'math-display' in p.get('class',[]) for p in node.parents):continue
        s=str(node)
        found=list(re.finditer(r'(?<!\\)\$([^$\n]+?)(?<!\\)\$',s))
        if not found:continue
        chunks=[];cursor=0
        for m in found:
            chunks.append(NavigableString(s[cursor:m.start()]))
            span=soup.new_tag('span');span['class']='inline-math'
            chunks.append(span);placeholders.append((span,m[1],False));cursor=m.end()
        chunks.append(NavigableString(s[cursor:]))
        node.replace_with(*chunks)
    data=[{'tex':tex,'display':display} for _,tex,display in placeholders]
    if data:
        run=subprocess.run([str(NODE),str(ROOT/'scripts/render_math.cjs')],input=json.dumps(data,ensure_ascii=False),text=True,encoding='utf-8',stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
        if run.returncode:raise RuntimeError(run.stderr)
        rendered=json.loads(run.stdout)
        assert len(rendered)==len(placeholders)
        for (node,tex,display),html in zip(placeholders,rendered):
            frag=BeautifulSoup(html,'html.parser');node.clear();node.extend(list(frag.contents))
            if display:node['class']=['math-display','equation'];node['aria-label']=tex
    return str(soup)

def head(title,relative=''):
    return ('<!DOCTYPE html><html lang="en" data-theme="dark"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{escape(title)} · {TITLE}</title>'
            '<meta name="description" content="A bilingual, fully worked course in laser-induced PFC droplet cavitation, jets, arrays, fracture and hydrogel transfer.">'
            f'<link rel="stylesheet" href="{relative}assets/vendor/katex/katex.min.css">'
            f'<link rel="stylesheet" href="{relative}assets/course.css">'
            f'<script defer src="{relative}assets/course-theme.js"></script>'
            f'<script defer src="{relative}assets/course-progress.js"></script>'
            '</head><body>')

def topbar(relative=''):
    return (f'<nav class="topbar" aria-label="Main navigation"><a class="brand" href="{relative}index.html">Laser PFC TP / 激光 PFC 转印</a>'
            f'<a href="{relative}reference/defense.html">Defense &amp; mastery / 答辩与掌握</a>'
            f'<a href="{relative}reference/notation.html">Notation / 符号</a>'
            f'<a href="{relative}reference/sources.html">Sources / 来源</a></nav>')

def footer():
    return ('<footer class="site-footer">'+P('Teaching derivations and conditional model results. Sources accompany their claims. Revised '+DATE+'.',
            '教学推导与条件模型结果。各项引用附于对应结论。修订于 '+DATE+'。')+'</footer></body></html>')

def status(ch,progress):
    value=progress['units'][unit_id(ch)]['status']
    labels={'pending':('Awaiting answers','待作答'), 'in_review':('Under review','审阅中'),'mastered':('Mastered','已掌握')}
    en,zh=labels[value]
    return f'<span class="progress-badge" data-status="{value}">{en} / {zh}</span>'

def panel(ch):
    noun_en,noun_zh=('appendix','本附录') if is_appendix(ch) else ('chapter','本章')
    return ('<section class="submission-panel" id="submit">'+H('Submit your three answers','提交三个回答','submit-heading')
            +P(f'Answer in your own words, in either language. Paste your answers into the teaching chat. Review covers reasoning, assumptions, and limits. All three accepted answers establish {noun_en} mastery.',
               f'用自己的话作答，可选任一语言。将回答粘贴到教学对话。审阅包括推理、假设与限制。三个回答均被接受后，判定{noun_zh}已掌握。')
            +'<div class="actions"><button id="copy-responses" type="button">Copy three responses / 复制三个回答</button><button id="download-responses" type="button">Download responses / 下载回答</button></div>'
            +'<span id="save-status" class="save-status" role="status" aria-live="polite"></span><textarea id="submission-fallback" rows="12" hidden aria-label="Prepared submission / 整理后的提交文本"></textarea></section>')

def course_body(ch):
    supplement=resource_sections(ch['number'])
    defense_anchor={3:'defense',90:'gel-defense'}.get(ch['number'])
    if supplement and defense_anchor:
        marker='<div class="heading-pair"><h2 id="'+defense_anchor+'"'
        assert marker in ch['body'], 'Defense section anchor changed'
        return ch['body'].replace(marker,supplement+marker,1)
    return ch['body']

def chapter_page(ch,chapters,progress):
    raw=course_body(ch)
    bs=BeautifulSoup(raw,'html.parser')
    qs=[a['data-defense'] for a in bs.select('article[data-defense]')]
    assert qs==ch['question_ids'],(ch['number'],qs,ch['question_ids'])
    toc='<nav class="toc" aria-label="In this unit">'+''.join(f'<a href="#{escape(h["id"])}">{escape(h.get_text())}</a>' for h in bs.select('h2[id][lang="en"]'))+'</nav>'
    nav='<nav aria-label="Chapters and appendix">'+''.join(f'<a href="../{route(c)}">{escape(unit_label(c)[0])} · {escape(c["title_en"])}</a>' for c in chapters)+'</nav>'
    obj='<ul>'+''.join('<li>'+P(*o)+'</li>' for o in ch['objectives'])+'</ul>'
    en_label,zh_label=unit_label(ch)
    header='<header class="chapter-header"><p class="eyebrow">'+en_label+' / '+zh_label+' · THEORY → DERIVATION → DEFENSE</p>'
    header+=f'<h1 lang="en">{escape(ch["title_en"])}</h1><h1 class="zh" lang="zh-CN">{escape(ch["title_zh"])}</h1>'
    header+=f'<section class="unit-map" data-unit-map="{unit_id(ch)}">'+unit_map([ch['number']])+'</section>'
    header+=P(ch['summary_en'],ch['summary_zh'])+status(ch,progress)
    header+=H('Learning goals','学习目标','objectives')+obj
    header+=P('<strong>Prerequisite.</strong> '+ch['prerequisite_en'],'<strong>先修知识。</strong> '+ch['prerequisite_zh'])+'</header>'
    idx=chapters.index(ch);links=[]
    if idx>0:links.append('<a href="../'+route(chapters[idx-1])+'">← '+unit_label(chapters[idx-1])[0]+' / '+unit_label(chapters[idx-1])[1]+'</a>')
    else:links.append('<a href="../index.html">← Course home / 课程首页</a>')
    if idx+1<len(chapters):links.append('<a href="../'+route(chapters[idx+1])+'">'+unit_label(chapters[idx+1])[0]+' / '+unit_label(chapters[idx+1])[1]+' →</a>')
    else:links.append('<a href="../reference/defense.html">Final synthesis / 最终综合 →</a>')
    out=head(en_label+': '+ch['title_en'],'../')+topbar('../')+'<div class="page-layout"><aside class="sidebar"><h2>Course / 课程</h2>'+nav+'<h2>In this unit / 本单元内容</h2>'+toc+'</aside>'
    out+=f'<div class="reading" data-unit="{unit_id(ch)}" data-unit-kind="{ch.get("kind","chapter")}" data-chapter="{unit_id(ch)}">'+header+'<main class="chapter-body">'+raw+panel(ch)+'</main><nav class="chapter-navigation">'+''.join(links)+'</nav></div></div>'+footer()
    if is_appendix(ch):
        out=out.replace('</head>',f'<link rel="canonical" href="{BASE}{route(ch)}"></head>')
    return render_html(out)

def reference_page(title,en,zh,body,chapters):
    content=BeautifulSoup(body,'html.parser')
    nav='<nav aria-label="Chapters and appendix">'+''.join(
        f'<a href="../{route(c)}">{escape(unit_label(c)[0])} · {escape(c["title_en"])}</a>'
        for c in chapters)+'</nav>'
    toc='<nav class="toc" aria-label="On this page">'+''.join(
        f'<a href="#{escape(h["id"])}">{escape(h.get_text())}</a>'
        for h in content.select('h2[id][lang="en"]'))+'</nav>'
    header='<header class="chapter-header"><p class="eyebrow">Reference / 参考</p>'
    header+=H(en,zh,'reference-title',1)+'</header>'
    layout='<div class="page-layout"><aside class="sidebar"><h2>Course / 课程</h2>'
    layout+=nav+'<h2>In this unit / 本单元内容</h2>'+toc+'</aside>'
    layout+='<div class="reading">'+header+'<main class="chapter-body">'+body+'</main></div></div>'
    return render_html(head(title,'../')+topbar('../')+layout+footer())

def home(chapters,progress):
    b='<header class="chapter-header home-header"><p class="eyebrow">PROJECT-CENTERED THEORY / 项目导向理论 · FIVE CHAPTERS + APPENDIX A / 五章 + 附录 A</p>'
    b+=f'<h1 lang="en">{TITLE}</h1><h1 lang="zh-CN" class="zh">{TITLE_ZH}</h1>'
    b+=P('Follow a laser pulse through phase change, jet formation, and transfer. Derive each balance and check its limits.',
         '沿激光脉冲、相变、射流形成到转印展开学习。推导各项平衡并核验其限制。','lead')
    b+='<div class="chain">'+P('Laser absorption → heating and nucleation → finite phase inventory → bubble and spatial jet → transmitted load → fracture and placement.',
         '激光吸收 → 加热与成核 → 有限相存量 → 气泡与空间射流 → 传递载荷 → 断裂与定位。')+'</div>'
    b+=P('Five chapters and Appendix A contain worked derivations and examples. Each unit ends with three defense questions. Chapter 3 includes the resolver study. Chapter 5 chains theory, calculation and solver verification for a jet on a rigid wall. Appendix A includes both modeling studies.',
         '五章与附录 A 提供完整推导及例题。每单元设三个答辩问题。第三章包括求解器研究。第五章依次给出射流撞击刚性壁面的理论、计算与求解器核验。附录 A 包括两项建模研究。')
    b+='<div class="resource-nav"><a class="button" href="chapters/'+filename(chapters[0])+'">Begin Chapter 1 / 开始第一章</a><a class="button" href="reference/defense.html">How mastery works / 如何判定掌握</a><a class="button" href="text/course.md">Editable bilingual text / 可编辑双语文本</a></div></header>'
    b+='<main class="chapter-body"><section class="course-map" id="course-map" data-unit-map="all">'+H('Contents','目录','course-map-heading')+unit_map([n for n,*_ in PLANNED])+'</section>'
    b+='<section class="chapter-grid" aria-label="Five chapters and Appendix A">'
    for ch in chapters:
        b+='<article class="chapter-card"><span class="card-number">'+unit_label(ch)[0]+' / '+unit_label(ch)[1]+'</span>'
        b+=f'<h2 lang="en"><a href="{route(ch)}">{escape(ch["title_en"])}</a></h2><h2 class="zh" lang="zh-CN">{escape(ch["title_zh"])}</h2>'
        b+=P(ch['summary_en'],ch['summary_zh'])+resource_links(ch['number'])+status(ch,progress)+'<p><a href="'+route(ch)+'#'+ch['question_ids'][0]+'">Defense questions / 答辩问题 →</a></p></article>'
    b+='</section>'+H('Define the reported maximum','定义报告中的最大值','envelope')
    b+=P('Report verified single-shot output and repeatable intact transfer separately. State energy, PFC mass, geometry, measurement area, duration, and damage limits.',
         '分别报告已核验单次输出与可重复完整转印。注明能量、PFC 质量、几何、测量面积、持续时间与损伤限制。')
    b+=P('The complete folder works offline. Keep its assets together when forwarding. Draft answers stay in your browser until you submit them.',
         '完整文件夹可离线使用。转发时保留全部资源。草稿在提交前保存在您的浏览器中。')
    nav='<nav aria-label="Chapters and appendix">'+''.join(
        f'<a href="{route(c)}">{escape(unit_label(c)[0])} · {escape(c["title_en"])}</a>'
        for c in chapters)+'</nav>'
    toc='<nav class="toc" aria-label="On this page"><a href="#course-map-heading">Contents / 目录</a><a href="#envelope">Define the reported maximum / 定义报告中的最大值</a></nav>'
    layout='<div class="page-layout"><aside class="sidebar"><h2>Course / 课程</h2>'
    layout+=nav+'<h2>In this unit / 本单元内容</h2>'+toc+'</aside>'
    layout+='<div class="reading">'+b+'</main></div></div>'
    return render_html(head(TITLE)+topbar()+layout+footer())

def source_page(chapters):
    b=P('The supplied English course is preserved in sources/. New derivations and diagrams extend it. Chapter 3 contains the resolver study. Chapter 5 contains the rigid-wall jet chain. Appendix A contains the two gel-model studies.',
        '提供的英文课程保存在 sources/。新推导与示意图对其进行扩展。第三章包括求解器研究。第五章包括刚性壁面射流链。附录 A 包括两项凝胶模型研究。')
    b+=P('<a href="../Theses/index.html">Theses and chapter evidence map</a> · <a href="../Theses.md">Complete Markdown register</a>. Each entry records authors, identifiers, summaries, and evidence limits.',
         '<a href="../Theses/index.html">论文与章节证据映射</a> · <a href="../Theses.md">完整 Markdown 目录</a>。每项记录作者、标识符、摘要与证据边界。')
    b+=P('<a href="../sources/Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md">Original English source</a> · SHA256 <code>cb4c40df67841ed1b011150e8e5acff99f2c22866185e198553f1a1c353ee7b0</code>.',
         '<a href="../sources/Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md">原始英文来源</a> · SHA256 <code>cb4c40df67841ed1b011150e8e5acff99f2c22866185e198553f1a1c353ee7b0</code>。')
    b+=P('The <a href="../sources/Cavitation_Course_Before_After_Comparison_EN_ZH.md">before/after comparison</a> guides the course structure. Each source below states the claim it supports.',
         '<a href="../sources/Cavitation_Course_Before_After_Comparison_EN_ZH.md">重构前后对比</a>指导课程结构。下列各项来源注明其支持的结论。')
    b+=H('Primary references and scope','一手文献与引用范围','primary')+'<ol class="source-list">'
    for key,author,en,zh,doi,url,scope_en,scope_zh in SOURCES:
        b+=f'<li id="{key}">'+P(f'<strong>[{key.upper()}] {escape(author)}.</strong> <a href="{url}">{escape(en)}</a>. DOI: <a href="https://doi.org/{doi}">{doi}</a>.',
                                f'<strong>[{key.upper()}] {escape(author)}。</strong> <a href="{url}">{escape(zh)}</a>。DOI：<a href="https://doi.org/{doi}">{doi}</a>。')+P(scope_en,scope_zh)
        if key=='r8':
            heat_url='https://webbook.nist.gov/cgi/cbook.cgi?ID=C678262&Mask=2&Units=SI'
            b+=P(f'<a href="{heat_url}">Liquid heat capacity</a>: Chapter 2 states its measurement temperature and mass conversion.',f'<a href="{heat_url}">液相热容</a>：第二章注明测量温度与质量换算。')
        b+='</li>'
    b+='</ol>'+H('Verification versus physical validation','核验与物理验证的区别','validation')
    b+=P('Algebra, dimensions, conservation, and numerical comparisons check the adopted equations. Target transfer performance remains unvalidated. Missing: measured activation, flow, fracture, and reset behavior.',
         '代数、量纲、守恒与数值对照核验所采用的方程。目标转印性能仍未验证。缺少：激活、流动、断裂与复位行为的实测。')
    return reference_page('Sources','Sources and provenance','来源与出处',b,chapters)

def notation_page(chapters):
    b=P('Use SI units. Phase equilibrium and equations of state use absolute pressure. Pressure differences name their reference. Interface equations define the normal direction before use.',
         '使用国际单位制。相平衡与状态方程采用绝对压力。压差注明参考压力。界面方程在使用前定义法向方向。')
    b+=T([('Quantity and unit','物理量与单位'),('Symbol','符号')],[
      [('Bubble radius at time t (m).','时刻 t 的气泡半径（m）。'),(r'$R(t)$',r'$R(t)$')],
      [('Time measured from the event start (s).','自事件开始计量的时间（s）。'),('$t$','$t$')],
      [('Wall velocity (m/s). A dot denotes time differentiation.','壁面速度（m/s）。点号表示时间微分。'),(r'$\dot R$',r'$\dot R$')],
      [('Wall acceleration (m/s²). Two dots denote the second time derivative.','壁面加速度（m/s²）。两点号表示时间二阶导数。'),(r'$\ddot R$',r'$\ddot R$')],
      [('Initial liquid PFC core radius (m). Subscript 0 denotes the initial state.','初始液态 PFC 核半径（m）。下标 0 表示初始状态。'),('$a_0$','$a_0$')],
      [('Density (kg/m³). Material subscripts identify the phase.','密度（kg/m³）。材料下标注明所属相。'),(r'$\rho$',r'$\rho$')],
      [('Dynamic viscosity (Pa s).','动力黏度（Pa s）。'),(r'$\mu$',r'$\mu$')],
      [('Interfacial tension (N/m). Interface subscripts identify the boundary.','界面张力（N/m）。界面下标注明所属边界。'),(r'$\sigma$',r'$\sigma$')],
      [('Pressure impulse (Pa s).','压力冲量（Pa s）。'),(r'$\Pi$',r'$\Pi$')],
      [('Directed jet momentum (N s). Subscript j denotes the jet.','定向射流动量（N s）。下标 j 表示射流。'),('$P_j$','$P_j$')],
      [('Jet kinetic energy (J).','射流动能（J）。'),('$E_j$','$E_j$')],
      [('Energy-release rate (J/m²). Gel shear modulus carries a gel subscript.','能量释放率（J/m²）。凝胶剪切模量另加凝胶下标。'),('$G$','$G$')],
      [('Fracture energy (J/m²).','断裂能（J/m²）。'),(r'$\Gamma$',r'$\Gamma$')],
      [('Local cohesive strength (Pa). Subscript max denotes the peak traction.','局部内聚强度（Pa）。下标 max 表示峰值牵引。'),(r'$T_{\max}$',r'$T_{\max}$')],
    ])
    b+=P('Each equation names its basis and includes local symbol definitions. Chapter 1 places its compact symbol tables after the formulas. A variable diagram follows each equation group. Undimensioned diagrams are schematic.',
         '每个方程注明依据，并附局部符号定义。第1章将紧凑符号表置于公式之后。各公式组之后附变量示意图。未标尺寸的图为示意图。')
    b+=P('<a href="../verification/equations.json">Equation registry</a>: LaTeX, definitions, equation types, and diagram variables. <a href="../text/course.md">Bilingual Markdown</a>: editable prose and formulas.',
         '<a href="../verification/equations.json">方程注册表</a>：LaTeX、定义、方程类型与图中变量。<a href="../text/course.md">双语 Markdown</a>：可编辑正文与公式。')
    return reference_page('Notation','Notation and derivation conventions','符号与推导约定',b,chapters)

def defense_page(chapters,progress):
    b=P('Each unit has three questions. Answer in either language. Explain the mechanism, quantitative balance, assumptions, and failure conditions. Reference answers provide formulas and review criteria.',
         '每单元设三个问题。可选任一语言作答。解释机制、定量平衡、假设与失效条件。参考答案提供公式与审阅标准。')
    b+=P('Paste your answers into the teaching chat. Revise any gaps after feedback. Three accepted explanations establish unit mastery.',
         '将回答粘贴到教学对话。根据反馈补足缺失内容。三个解释均被接受后，判定该单元已掌握。','callout')
    for ch in chapters:
        bs=BeautifulSoup(ch['body'],'html.parser')
        b+=H(unit_label(ch)[0]+' · '+ch['title_en'],unit_label(ch)[1]+' · '+ch['title_zh'],'defense-a' if is_appendix(ch) else f'defense-c{ch["number"]}')+status(ch,progress)
        for article in bs.select('article[data-defense]'):
            en=article.select_one('h3[lang=en]').get_text();zh=article.select_one('h3[lang="zh-CN"]').get_text()
            b+=P(f'<a href="../{route(ch)}#{article["id"]}">{escape(en)}</a>',f'<a href="../{route(ch)}#{article["id"]}">{escape(zh)}</a>')
    b+=H('Project synthesis','项目综合','original-synthesis')
    b+=P('Connect three results: laser-to-jet conditions, energy-constrained array output, and selective fracture with intact transfer. Explain how gel changes each result.',
         '贯通三个结果：激光到射流的条件、受能量约束的阵列输出，以及选择性断裂与完整转印。解释凝胶如何改变各项结果。')
    b+=P('The displayed badges reflect the saved learning record. Research-stage closure leaves that record unchanged.',
         '所示状态标签对应已保存的学习记录。研究阶段关闭不会改变该记录。')
    return reference_page('Defense and mastery','Defense questions and mastery records','答辩问题与掌握记录',b,chapters)

def markdown_source(ch):
    soup=BeautifulSoup(course_body(ch),'html.parser')
    # Retain the same English / Chinese equation title in portable Markdown.
    for heading in soup.select('.equation-heading.inline-pair'):
        heading.replace_with(NavigableString('\n\n'+heading.get_text()+'\n\n'))
    for div in soup.select('.math-display[data-tex]'):div.replace_with(NavigableString('\n\n$$\n'+div['data-tex']+'\n$$\n\n'))
    for box in soup.select('textarea,label'):box.decompose()
    for summary in soup.select('summary'):summary.replace_with(NavigableString('\n\n**'+summary.get_text()+'**\n\n'))
    # Keep bilingual cell paragraphs inside one GFM cell, rather than emitting
    # disconnected empty one-column tables when paragraph tags are converted.
    tables={}
    def convert(fragment,strip):
        protected={};parsed=BeautifulSoup(fragment,'html.parser')
        for node in list(parsed.find_all(string=True)):
            def stash(match):
                token=f'COURSEMATH{len(protected)}PLACEHOLDER'
                protected[token]=match[0];return token
            value=re.sub(r'\$\$[\s\S]*?\$\$|\$[^$\n]+?\$',stash,str(node))
            node.replace_with(NavigableString(value))
        result=markdownify(str(parsed),heading_style='ATX',strip=strip)
        for token,math in protected.items():result=result.replace(token,'\n\n'+math+'\n\n' if math.startswith('$$') else math)
        return result
    for index,table in enumerate(soup.select('table')):
        def cell(node):
            paragraphs=node.select('.lang-pair > p')
            value='<br>'.join(convert(str(p),['td','th','div']).strip() for p in paragraphs) if paragraphs else convert(str(node),['td','th','div']).strip()
            return re.sub(r'\s*\n+\s*','<br>',value).replace('|',r'\|')
        headers=[cell(n) for n in table.select('thead th')]
        rows=[[cell(n) for n in tr.find_all('td',recursive=False)] for tr in table.select('tbody tr')]
        assert headers and all(len(row)==len(headers) for row in rows)
        token=f'COURSETABLE{index}PLACEHOLDER'
        tables[token]='\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |',*['| '+' | '.join(row)+' |' for row in rows]])
        table.replace_with(NavigableString('\n\n'+token+'\n\n'))
    prose=convert(str(soup),['section','article','div','details'])
    for token,table in tables.items():prose=prose.replace(token,table)
    return '# '+unit_label(ch)[0]+': '+ch['title_en']+'\n\n# '+unit_label(ch)[1]+'：'+ch['title_zh']+'\n\n'+prose

def settings(chapters):
    def record(ch):
        return {'id':unit_id(ch),'kind':ch.get('kind','chapter'),'label':unit_label(ch)[0],'label_zh':unit_label(ch)[1],'file':route(ch),'title':ch['title_en'],'title_zh':ch['title_zh'],'defense_ids':ch['question_ids'],'unit_map_row':UNIT_MAP[ch['number']]}
    return {'title':TITLE,'title_zh':TITLE_ZH,'repository':f'PFGaoPhilip/{SLUG}','url':BASE,'source_sha256':'cb4c40df67841ed1b011150e8e5acff99f2c22866185e198553f1a1c353ee7b0','comparison_sha256':'e5462de2b8ca7e717a4e9f0a26cc5c2a9fc0e1d8c054f48d087cd2a27fc0d87f','prepared':DATE,
      'languages':['en','zh-CN'],'default_theme':'dark','offline_assets':True,'formula_figure_required':True,'local_symbols_before_every_display':False,
      'local_symbol_placement':{'default':'before','C01':'after','chapter01_order':['derivation','equation_title','formulas','compact_symbol_table','figure','check']},
      'mastery_policy':{'questions_per_chapter':3,'own_words_sufficient':True,'equation_memorization_required':False,'decision':'teacher_review_all_three','automatic_keyword_grading':False,'publication_is_not_mastery':True},
      'chapters':[record(ch) for ch in chapters if not is_appendix(ch)],
      'appendices':[record(ch) for ch in chapters if is_appendix(ch)],
      'resource_ownership':{'resolver':'C03','minimal_cavitation':'A','embedded_pfc':'A'},
      'unit_order':[unit_id(ch) for ch in chapters],
      'legacy_routes':[{'file':'chapters/05-hydrogel-versus-liquid.html','canonical':'appendices/90-hydrogel-versus-liquid.html'},{'file':'appendices/a-hydrogel-versus-liquid.html','canonical':'appendices/90-hydrogel-versus-liquid.html'}],
      'causal_chain':['absorption','heat transport','activation','finite phase inventory','bubble pressure and flow','spatial jet','transmitted load','fracture','intact placement','reset'],
      'architectures':['PFC in aqueous droplet stamp','PFC-containing liquid layer: direct film loading','PFC-containing liquid layer: intact PVC-mediated loading','open liquid pocket in gel','PFC embedded in bulk gel','sealed gel/composite cavity'],
      'maximum_reports':['highest verified single-shot defined pressure or finite-mass speed','repeatable intact-transfer envelope']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--partial',action='store_true');parser.add_argument('--only',type=int,nargs='+');args=parser.parse_args()
    for d in ['chapters','appendices','text','reference','verification','assets/figures','learning-records']:(ROOT/d).mkdir(exist_ok=True,parents=True)
    chapters=load_chapters(args.partial,args.only)
    if not chapters:print('No completed chapter modules yet.');return
    progress_path=ROOT/'learning-records/progress.json'
    if progress_path.exists():progress=json.loads(progress_path.read_text(encoding='utf-8'))
    else:progress={'course':TITLE,'units':{unit_id(ch):{'status':'pending','accepted_question_ids':[],'evidence':[]} for ch in chapters}}
    if 'chapters' in progress:progress['units']=progress.pop('chapters')
    for ch in chapters:progress['units'].setdefault(unit_id(ch),{'status':'pending','accepted_question_ids':[],'evidence':[]})
    progress_path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    assert len({e['id'] for e in EQUATIONS})==len(EQUATIONS),'Duplicate equation ID'
    for eq in EQUATIONS:(ROOT/'assets/figures'/f'{eq["id"].lower()}.svg').write_text(svg_for(eq),encoding='utf-8')
    for ch in chapters:
        rendered=chapter_page(ch,chapters,progress)
        (ROOT/route(ch)).write_text(rendered,encoding='utf-8')
        if is_appendix(ch):
            for legacy in ('chapters/05-hydrogel-versus-liquid.html','appendices/a-hydrogel-versus-liquid.html'):(ROOT/legacy).write_text(rendered,encoding='utf-8')
        (ROOT/'text'/filename(ch).replace('.html','.md')).write_text(markdown_source(ch),encoding='utf-8')
    (ROOT/'text/course.md').write_text('\n\n---\n\n'.join((ROOT/'text'/filename(ch).replace('.html','.md')).read_text(encoding='utf-8') for ch in chapters),encoding='utf-8')
    (ROOT/'index.html').write_text(home(chapters,progress),encoding='utf-8')
    (ROOT/'reference/sources.html').write_text(source_page(chapters),encoding='utf-8')
    (ROOT/'reference/notation.html').write_text(notation_page(chapters),encoding='utf-8')
    (ROOT/'reference/defense.html').write_text(defense_page(chapters,progress),encoding='utf-8')
    (ROOT/'verification/equations.json').write_text(json.dumps(EQUATIONS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'COURSE_SETTINGS.json').write_text(json.dumps(settings(chapters),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'.nojekyll').write_text('',encoding='utf-8')
    print(json.dumps({'chapters':sum(not is_appendix(ch) for ch in chapters),'appendices':sum(is_appendix(ch) for ch in chapters),'equations':len(EQUATIONS),'questions':sum(len(c['question_ids']) for c in chapters),'offline_math':True,'mastery':'awaits learner evidence'}))
    if not args.partial and not args.only:
        from integrate_modeling import integrate
        integrate(include_modeling=False)
        if (ROOT/'modeling/embedded-pfc-feasibility/index.html').is_file():
            from integrate_embedded_pfc import integrate_links
            integrate_links()
    if (ROOT/'learning-records/resolver-progress/PROGRESS.json').is_file():
        from integrate_resolver_progress import integrate_links
        integrate_links()

    if (ROOT/'assets/figures-editable/manifest.json').is_file():
        from integrate_english_figures import integrate as integrate_english
        integrate_english()

if __name__=='__main__':main()
