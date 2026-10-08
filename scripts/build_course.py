"""Build the bilingual, portable five-chapter teaching website from editable sources."""
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

ROOT=Path(__file__).resolve().parents[1]
NODE=Path(os.environ.get('NODE_BINARY') or shutil.which('node') or 'node')
TITLE='Laser Induced PFC Droplet TP'
TITLE_ZH='激光诱导 PFC 液滴转印'
SLUG='Laser-Induced-PFC-Droplet-TP'
BASE='https://pfgaophilip.github.io/'+SLUG+'/'
DATE='2026-10-09'
PLANNED=[
 (1,'cavitation-and-jet-foundations','Cavitation and the mechanics of a directional jet','空化与定向射流的力学基础'),
 (2,'laser-heat-and-finite-pfc-inventory','Laser heating and finite PFC phase inventory','激光加热与有限 PFC 相存量'),
 (3,'arrays-to-coherent-jets-and-loads','From droplet arrays to coherent jets and defined loads','从液滴阵列到相干射流与明确载荷'),
 (4,'load-path-fracture-and-intact-transfer','Load paths, fracture and intact transfer','受力路径、断裂与完整转印'),
 (5,'hydrogel-versus-liquid-platforms','Hydrogel and conventional liquid platforms','水凝胶与常规液体平台'),
]
UNIT_MAP = {
 1:[('Chapter 1: Cavitation and jets','第1章：空化与射流基础'),('Spherical cavity dynamics, liquid inertia, pressure impulse, moving interfaces, and directional jet formation.','球形腔体动力学、液体惯性、压力冲量、运动界面与定向射流形成。'),('How does cavity pressure accelerate liquid, and why does a directional jet require asymmetry?','腔体压力如何加速液体？为什么形成定向射流必须有不对称性？')],
 2:[('Chapter 2: PFC versus ordinary droplets','第2章：PFC与普通液滴对比'),('Laser energy deposition, nucleation, heat and mass transfer, PFC material properties, and finite-inventory phase thermodynamics.','激光能量沉积、成核、传热传质、PFC物性与有限存量相变热力学。'),('Under matched conditions, what does PFC actually change—and what does it not guarantee?','在匹配条件下，PFC究竟改变了什么，又不能保证什么？')],
 3:[('Chapter 3: Arrays and preliminary calculations','第3章：阵列与初步计算'),('Jet formation, transport and impact; bubble-array coupling, energy allocation, and finite pressure/velocity limits.','射流形成、输运与冲击；气泡阵列耦合、能量分配及有限压力／速度极限。'),('How do individual sites combine into a finite, physically consistent mechanical output?','单个位点如何共同形成有限且符合物理约束的力学输出？')],
 4:[('Chapter 4: Fracture and transfer','第4章：断裂与转印'),('Film/PVC loading, transient structural response, interface separation, and transfer criteria.','薄膜／PVC受载、瞬态结构响应、界面分离与转印判据。'),('Does the delivered load release the intended interface without destroying the payload?','实际传递的载荷能否释放目标界面，同时不损坏被转印对象？')],
 5:[('Appendix A: Hydrogel versus liquid','附录A：水凝胶与液体平台'),('Hydrogel confinement, constitutive resistance, response times, and architecture comparison.','水凝胶约束、本构阻力、响应时间与结构方案比较。'),('Does the gel improve the complete transfer process, or merely change the mechanism?','凝胶是在改善完整转印过程，还是仅仅改变了致动机制？')],
}
MAP_HEADERS=[('New unit','新单元'),('Main material consolidated','主要整合内容'),('Central learning question','核心学习问题')]

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

def filename(ch):return f'{ch["number"]:02d}-'+re.sub(r'^\d{2}-','',ch['slug'])+'.html'

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
    return ('<footer class="site-footer">'+P('Original teaching derivations and declared numerical controls. Literature observations are cited; no original papers, private project measurements or previous COMSOL results are distributed. Prepared '+DATE+'.',
            '原创教学推导及声明条件的数值对照。文献观测均注明出处；不分发论文原文、私人项目实测或此前 COMSOL 结果。编制于 '+DATE+'。')+'</footer></body></html>')

def status(ch,progress):
    value=progress['chapters'][f'C{ch["number"]:02d}']['status']
    labels={'pending':('Awaiting your explanations','待您解释'), 'in_review':('Under review','审阅中'),'mastered':('Mastered','已掌握')}
    en,zh=labels[value]
    return f'<span class="progress-badge" data-status="{value}">{en} / {zh}</span>'

def panel():
    return ('<section class="submission-panel" id="submit">'+H('Submit one explanation for each of the three questions','为三个问题各提交一段解释','submit-heading')
            +P('Write in your own words, in either language. Copy the three responses into the teaching chat. The teacher assesses causal reasoning, assumptions and limitations against the rubrics, records any correction, and marks the chapter mastered when all three are understood. A saved draft or completed form is not a mastery decision.',
               '请用自己的话作答，可选任一语言。将三个回答复制到教学对话。教师按评分标准评估因果推理、假设及限制，记录必要纠正，并在三个问题均被理解后将本章标记为已掌握。保存草稿或填写表单不等于掌握判定。')
            +'<div class="actions"><button id="copy-responses" type="button">Copy three responses / 复制三个回答</button><button id="download-responses" type="button">Download responses / 下载回答</button></div>'
            +'<span id="save-status" class="save-status" role="status" aria-live="polite"></span><textarea id="submission-fallback" rows="12" hidden aria-label="Prepared submission / 整理后的提交文本"></textarea></section>')

def chapter_page(ch,chapters,progress):
    raw=ch['body']
    bs=BeautifulSoup(raw,'html.parser')
    qs=[a['data-defense'] for a in bs.select('article[data-defense]')]
    assert qs==ch['question_ids'],(ch['number'],qs,ch['question_ids'])
    toc='<nav class="toc" aria-label="In this chapter">'+''.join(f'<a href="#{escape(h["id"])}">{escape(h.get_text())}</a>' for h in bs.select('h2[id][lang="en"]'))+'</nav>'
    nav='<nav aria-label="Chapters">'+''.join(f'<a href="{filename(c)}">{c["number"]:02d} · {escape(c["title_en"])}</a>' for c in chapters)+'</nav>'
    obj='<ul>'+''.join('<li>'+P(*o)+'</li>' for o in ch['objectives'])+'</ul>'
    header='<header class="chapter-header"><p class="eyebrow">Chapter '+str(ch['number'])+' / 第 '+str(ch['number'])+' 章 · THEORY → DERIVATION → DEFENSE</p>'
    header+=f'<h1 lang="en">{escape(ch["title_en"])}</h1><h1 class="zh" lang="zh-CN">{escape(ch["title_zh"])}</h1>'
    header+=f'<section class="unit-map" data-unit-map="C{ch["number"]:02d}">'+unit_map([ch['number']])+'</section>'
    header+=P(ch['summary_en'],ch['summary_zh'])+status(ch,progress)
    header+=H('What this chapter enables','本章学习目标','objectives')+obj
    header+=P('<strong>Prerequisite.</strong> '+ch['prerequisite_en'],'<strong>先修知识。</strong> '+ch['prerequisite_zh'])+'</header>'
    idx=chapters.index(ch);links=[]
    if idx>0:links.append('<a href="'+filename(chapters[idx-1])+'">← Previous chapter / 上一章</a>')
    else:links.append('<a href="../index.html">← Course home / 课程首页</a>')
    if idx+1<len(chapters):links.append('<a href="'+filename(chapters[idx+1])+'">Next chapter / 下一章 →</a>')
    else:links.append('<a href="../reference/defense.html">Final synthesis / 最终综合 →</a>')
    out=head(ch['title_en'],'../')+topbar('../')+'<div class="page-layout"><aside class="sidebar"><h2>Course / 课程</h2>'+nav+'<h2>In this chapter / 本章内容</h2>'+toc+'</aside>'
    out+=f'<div class="reading" data-chapter="C{ch["number"]:02d}">'+header+'<main class="chapter-body">'+raw+panel()+'</main><nav class="chapter-navigation">'+''.join(links)+'</nav></div></div>'+footer()
    return render_html(out)

def reference_page(title,en,zh,body):
    return render_html(head(title,'../')+topbar('../')+'<div class="reference-content"><main>'+H(en,zh,'reference-title',1)+body+'</main></div>'+footer())

def home(chapters,progress):
    b='<header class="hero"><p class="eyebrow">PROJECT-CENTERED THEORY / 项目导向理论 · FIVE CHAPTERS / 五章</p>'
    b+=f'<h1 lang="en">{TITLE}</h1><h1 lang="zh-CN" class="zh">{TITLE_ZH}</h1>'
    b+=P('From an absorbed laser pulse to an intact transferred object: learn the physical conditions at every link, derive the useful calculations, and defend the reasoning in your own words.',
         '从吸收的激光脉冲到完整转印的物体：学习各环节的物理条件，推导有用的计算，并用自己的话论证推理。','lead')
    b+='<div class="chain">'+P('Laser absorption → heating and nucleation → finite phase inventory → bubble and spatial jet → transmitted load → fracture and placement.',
         '激光吸收 → 加热与成核 → 有限相存量 → 气泡与空间射流 → 传递载荷 → 断裂与定位。')+'</div>'
    b+=P('The source’s four chapters and hydrogel appendix become five substantial chapters. Each includes assumptions, locally defined symbols, numbered derivations, variable diagrams, worked controls and exactly three oral-defense questions. Reference answers follow the questions; your explanations establish mastery.',
         '源文件的四章及水凝胶附录组成五个实质性章节。每章包括假设、公式前的符号定义、编号推导、变量示意图、完整例题及恰好三个口头答辩式问题。参考答案位于问题之后；通过您的解释判定掌握。')
    b+='<div class="resource-nav"><a class="button" href="chapters/'+filename(chapters[0])+'">Begin Chapter 1 / 开始第一章</a><a class="button" href="reference/defense.html">How mastery works / 如何判定掌握</a><a class="button" href="text/course.md">Editable bilingual text / 可编辑双语文本</a></div></header>'
    b+='<section class="course-map" id="course-map" data-unit-map="all">'+H('One route: the unit, its source, its central question','一条主线：单元、整合来源及核心问题','course-map-heading')+unit_map([n for n,*_ in PLANNED])
    b+=P('The fifth unit retains its source label “Appendix A: Hydrogel versus liquid” in this map and is taught as Chapter 5. The correspondence identifies selected source material; it does not claim every old paragraph was retained.',
         '第五单元在本表保留源名称“附录A：水凝胶与液体平台”，并作为第五章讲授。对应关系表明所选来源内容，不宣称保留旧版每一段文字。')+'</section>'
    b+='<section class="chapter-grid" aria-label="Five chapters">'
    for ch in chapters:
        b+='<article class="chapter-card"><span class="card-number">CHAPTER '+str(ch['number'])+' / 第 '+str(ch['number'])+' 章</span>'
        b+=f'<h2 lang="en"><a href="chapters/{filename(ch)}">{escape(ch["title_en"])}</a></h2><h2 class="zh" lang="zh-CN">{escape(ch["title_zh"])}</h2>'
        b+=P(ch['summary_en'],ch['summary_zh'])+status(ch,progress)+'<p><a href="chapters/'+filename(ch)+'#'+ch['question_ids'][0]+'">Three defense questions / 三个答辩问题 →</a></p></article>'
    b+='</section>'+H('The useful maximum is a defined operating envelope','有用的最大值来自明确的工作范围','envelope')
    b+=P('Report two outcomes separately: the largest verified single-shot pressure or finite-mass velocity, and the repeatable intact-transfer envelope. State energy, inventory, geometry, load path, observation area/time and damage constraints. A singular ideal radius, an assigned efficiency or a pressure spike does not establish the project’s maximum.',
         '分别报告两个结果：已核验的最高单次压力或有限质量速度，以及可重复完整转印范围。声明能量、存量、几何、受力路径、观测面积／时间及损伤限制。理想半径奇异性、预设效率或压力尖峰不能确立项目最大值。','callout')
    b+=P('All essential mathematics, diagrams, fonts and scripts are local. Scholarly links are optional reading; original papers are excluded. The complete folder and its ZIP work offline. Your typed responses are stored only in your browser and are sent for review only when you copy them into the teaching chat.',
         '所有必要数学、示意图、字体及脚本均在本地。学术链接供延伸阅读，不包含论文原文。完整文件夹及 ZIP 可离线使用。您输入的回答仅存于浏览器，只有在复制到教学对话后才被提交审阅。')
    return render_html(head(TITLE)+topbar()+'<main class="home">'+b+'</main>'+footer())

def source_page():
    b=P('Course basis: the user-supplied English course, copied unchanged for provenance; the newly authored teaching text and diagrams extend its derivations. The source’s hydrogel appendix is promoted to Chapter 5. Software procedures and previous simulations are not theoretical evidence.',
        '课程依据：用户提供的英文课程，为保留来源而原样复制；新编教学文本及示意图扩展其推导。原文件水凝胶附录升为第五章。软件操作及此前模拟不作为理论证据。')
    b+=P('<a href="../sources/Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md">Original English source</a> · SHA256 <code>cb4c40df67841ed1b011150e8e5acff99f2c22866185e198553f1a1c353ee7b0</code>.',
         '<a href="../sources/Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md">原始英文来源</a> · SHA256 <code>cb4c40df67841ed1b011150e8e5acff99f2c22866185e198553f1a1c353ee7b0</code>。')
    b+=P('The <a href="../sources/Cavitation_Course_Before_After_Comparison_EN_ZH.md">user-supplied before/after comparison</a> sets the editorial direction: a single integrated project route, necessary transient physics, connected worked examples and explicit unresolved links. The current website expands to five web chapters with three defenses each as requested.',
         '<a href="../sources/Cavitation_Course_Before_After_Comparison_EN_ZH.md">用户提供的重构前后对比</a>确立编辑方向：单一整合的项目路线、必要瞬态物理、贯穿例题及明确的未解决环节。本网站按本次要求扩展为五个网页章节，每章三个答辩问题。')
    b+=H('Primary references and scope','一手文献与引用范围','primary')+'<ol class="source-list">'
    for key,author,en,zh,doi,url,scope_en,scope_zh in SOURCES:
        b+=f'<li id="{key}">'+P(f'<strong>[{key.upper()}] {escape(author)}.</strong> <a href="{url}">{escape(en)}</a>. DOI: <a href="https://doi.org/{doi}">{doi}</a>.',
                                f'<strong>[{key.upper()}] {escape(author)}。</strong> <a href="{url}">{escape(zh)}</a>。DOI：<a href="https://doi.org/{doi}">{doi}</a>。')+P(scope_en,scope_zh)
        if key=='r8':
            heat_url='https://webbook.nist.gov/cgi/cbook.cgi?ID=C678262&Mask=2&Units=SI'
            b+=P(f'<a href="{heat_url}">Separate liquid heat-capacity entry</a>: the reported measurement temperature and molar-to-mass conversion are retained in Chapter 2.',f'<a href="{heat_url}">单独的液相热容条目</a>：第二章保留所报告的测量温度及摩尔量到质量量的换算。')
        b+='</li>'
    b+='</ol>'+H('Verification versus physical validation','核验与物理验证的区别','validation')
    b+=P('Algebraic, dimensional, conservation and numerical controls check the declared models. They do not calibrate a target formulation or establish experimental transfer performance. Every claimed new material benefit remains conditional until its optical, phase, flow, fracture and reset links are measured or resolved in the appropriate model.',
         '代数、量纲、守恒及数值对照核验已声明模型；不能据此标定目标配方或确立实验转印性能。每项新材料优势在其光学、相变、流动、断裂及复位环节被测量或由适当模型解析之前，均为条件性结论。')
    return reference_page('Sources','Sources and provenance','来源与出处',b)

def notation_page():
    b=P('SI units are used. Absolute pressure belongs in phase equilibrium and equations of state. Mechanical pressure differences state their reference. Each chapter defines its own normal orientation before interface equations; a liquid-to-vapor normal and a solid-to-liquid normal serve different interfaces.',
         '使用国际单位制。相平衡及状态方程使用绝对压力。力学压差明确其参考压力。各章在界面方程之前定义法向；液体指向蒸气的法向与固体指向液体的法向用于不同界面。')
    b+=T([('Notation','符号'),('Role and unit','作用与单位')],[
      [(r'$R(t),\dot R,\ddot R$',r'$R(t),\dot R,\ddot R$'),('Bubble radius (m), wall velocity (m/s), wall acceleration (m/s²). Newton dots are time derivatives.','气泡半径（m）、壁面速度（m/s）、壁面加速度（m/s²）。牛顿点号表示时间导数。')],
      [('$a_0$','$a_0$'),('Initial liquid PFC core radius (m); not the bubble maximum radius or stress-free gel cavity radius.','初始液态 PFC 核半径（m）；不是气泡最大半径或凝胶无应力腔体半径。')],
      [(r'$\rho,\mu,\sigma$',r'$\rho,\mu,\sigma$'),('Density (kg/m³), dynamic viscosity (Pa s), interfacial tension (N/m). Material/interface subscripts identify where they apply.','密度（kg/m³）、动力黏度（Pa s）、界面张力（N/m）。材料／界面下标指明适用位置。')],
      [(r'$\Pi, P_j, E_j$',r'$\Pi, P_j, E_j$'),('Pressure impulse (Pa s), directed jet momentum (N s), jet kinetic energy (J): different quantities.','压力冲量（Pa s）、定向射流动量（N s）、射流动能（J）：三种不同物理量。')],
      [(r'$G,\Gamma,T_{\max}$',r'$G,\Gamma,T_{\max}$'),('Energy-release rate (J/m²), fracture energy (J/m²), local cohesive strength (Pa); gel shear modulus has an explicit gel subscript.','能量释放率（J/m²）、断裂能（J/m²）、局部内聚强度（Pa）；凝胶剪切模量具有明确凝胶下标。')],
    ])
    b+=P('Definitions, identities, balance laws, constitutive choices, approximations, empirical correlations and hypotheses are labeled beside the equations. Every display repeats all local symbols and units before the formula and follows it immediately with a physical-variable diagram. Figure geometry is illustrative unless explicitly dimensioned.',
         '定义、恒等式、平衡律、本构选择、近似、经验关联式及假说在方程旁标明。每个公式前均重复本式所有符号及单位，公式后立即附物理变量示意图。示意几何除非明确标尺寸，否则仅用于说明。')
    b+=P('<a href="../verification/equations.json">Editable equation registry</a> preserves complete LaTeX, symbol declarations, classification, diagram variables and stable identifiers. <a href="../text/course.md">Bilingual Markdown</a> retains the complete formula text for later annotation.',
         '<a href="../verification/equations.json">可编辑方程注册表</a>保存完整 LaTeX、符号定义、类型、示意图变量及稳定编号。<a href="../text/course.md">双语 Markdown</a>保留完整公式文本，便于后续批注。')
    return reference_page('Notation','Notation and derivation conventions','符号与推导约定',b)

def defense_page(chapters,progress):
    b=P('Each chapter has exactly three defense questions. You may answer concisely in your own words and use either language. Explain what drives what, identify the relevant quantitative balance, and state an assumption or failure condition. The reference answer begins with the original formulas, then gives the physical reasoning and rubric.',
         '每章恰好三个答辩问题。您可用自己的话简要作答，并选用任一语言。解释物理驱动关系、识别相关定量平衡，并说明假设或失效条件。参考答案首先引用原公式，再给出物理推理及掌握标准。')
    b+=P('The review process is: save/copy your three explanations → paste them into the teaching chat → receive targeted feedback → correct any missing concept → all three accepted → chapter marked mastered in the persistent course record and next published version. A keyword match, click, saved response or access counter cannot make that decision.',
         '审阅流程：保存／复制三段解释 → 粘贴到教学对话 → 获得针对性反馈 → 纠正缺失概念 → 三项全部被接受 → 在持久课程记录及下一发布版本中将本章标记为已掌握。关键词匹配、点击、保存回答或访问计数不能作出该判定。','callout')
    for ch in chapters:
        bs=BeautifulSoup(ch['body'],'html.parser')
        b+=H('Chapter '+str(ch['number'])+' · '+ch['title_en'],'第 '+str(ch['number'])+' 章 · '+ch['title_zh'],f'defense-c{ch["number"]}')+status(ch,progress)
        for article in bs.select('article[data-defense]'):
            en=article.select_one('h3[lang=en]').get_text();zh=article.select_one('h3[lang="zh-CN"]').get_text()
            b+=P(f'<a href="../chapters/{filename(ch)}#{article["id"]}">{escape(en)}</a>',f'<a href="../chapters/{filename(ch)}#{article["id"]}">{escape(zh)}</a>')
    b+=H('The source’s three final research defenses','源文件的三个最终研究答辩','original-synthesis')
    b+=P('After the five chapter defenses, connect the answers across the whole project: (1) laser-to-useful-jet conditions, (2) array calculation without an assumed droplet-count pressure multiplier, and (3) intact fracture/transfer and hydrogel changes. These are synthesis prompts drawn from the source, not three additional chapter mastery gates.',
         '完成五章答辩后，将回答贯通整个项目：（1）激光到有用射流的条件；（2）不预设液滴数量压力倍增的阵列计算；（3）完整断裂／转印及水凝胶带来的变化。这些是源文件的综合论题，不是额外的三个章节掌握门槛。')
    b+=P('All five new chapters begin pending. Previously accepted cavitation knowledge is useful background, but it is not used to claim mastery of newly expanded phase, array, fracture or gel derivations.',
         '五个新章初始均为待掌握。此前已被接受的空化知识可作为背景，但不能据此宣称已掌握本次扩展的相变、阵列、断裂或凝胶推导。')
    return reference_page('Defense and mastery','Defense questions and mastery records','答辩问题与掌握记录',b)

def markdown_source(ch):
    soup=BeautifulSoup(ch['body'],'html.parser')
    for div in soup.select('.math-display[data-tex]'):div.replace_with(NavigableString('\n\n$$\n'+div['data-tex']+'\n$$\n\n'))
    for box in soup.select('textarea,label'):box.decompose()
    for summary in soup.select('summary'):summary.replace_with(NavigableString('\n\n**'+summary.get_text()+'**\n\n'))
    return '# '+ch['title_en']+'\n\n# '+ch['title_zh']+'\n\n'+markdownify(str(soup),heading_style='ATX',strip=['section','article','div','details'])

def settings(chapters):
    return {'title':TITLE,'title_zh':TITLE_ZH,'repository':f'PFGaoPhilip/{SLUG}','url':BASE,'source_sha256':'cb4c40df67841ed1b011150e8e5acff99f2c22866185e198553f1a1c353ee7b0','comparison_sha256':'e5462de2b8ca7e717a4e9f0a26cc5c2a9fc0e1d8c054f48d087cd2a27fc0d87f','prepared':DATE,
      'languages':['en','zh-CN'],'default_theme':'dark','offline_assets':True,'formula_figure_required':True,'local_symbols_before_every_display':True,
      'mastery_policy':{'questions_per_chapter':3,'own_words_sufficient':True,'equation_memorization_required':False,'decision':'teacher_review_all_three','automatic_keyword_grading':False,'publication_is_not_mastery':True},
      'chapters':[{'id':f'C{ch["number"]:02d}','file':'chapters/'+filename(ch),'title':ch['title_en'],'title_zh':ch['title_zh'],'defense_ids':ch['question_ids'],'unit_map_row':UNIT_MAP[ch['number']]} for ch in chapters],
      'causal_chain':['absorption','heat transport','activation','finite phase inventory','bubble pressure and flow','spatial jet','transmitted load','fracture','intact placement','reset'],
      'architectures':['PFC in aqueous droplet stamp','PFC-containing liquid layer: direct film loading','PFC-containing liquid layer: intact PVC-mediated loading','open liquid pocket in gel','PFC embedded in bulk gel','sealed gel/composite cavity'],
      'maximum_reports':['highest verified single-shot defined pressure or finite-mass speed','repeatable intact-transfer envelope']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--partial',action='store_true');parser.add_argument('--only',type=int,nargs='+');args=parser.parse_args()
    for d in ['chapters','text','reference','verification','assets/figures','learning-records']:(ROOT/d).mkdir(exist_ok=True,parents=True)
    chapters=load_chapters(args.partial,args.only)
    if not chapters:print('No completed chapter modules yet.');return
    progress_path=ROOT/'learning-records/progress.json'
    if progress_path.exists():progress=json.loads(progress_path.read_text(encoding='utf-8'))
    else:progress={'course':TITLE,'chapters':{f'C{n:02d}':{'status':'pending','accepted_question_ids':[],'evidence':[]} for n,*_ in PLANNED}}
    progress_path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    assert len({e['id'] for e in EQUATIONS})==len(EQUATIONS),'Duplicate equation ID'
    for eq in EQUATIONS:(ROOT/'assets/figures'/f'{eq["id"].lower()}.svg').write_text(svg_for(eq),encoding='utf-8')
    for ch in chapters:
        (ROOT/'chapters'/filename(ch)).write_text(chapter_page(ch,chapters,progress),encoding='utf-8')
        (ROOT/'text'/filename(ch).replace('.html','.md')).write_text(markdown_source(ch),encoding='utf-8')
    (ROOT/'text/course.md').write_text('\n\n---\n\n'.join((ROOT/'text'/filename(ch).replace('.html','.md')).read_text(encoding='utf-8') for ch in chapters),encoding='utf-8')
    (ROOT/'index.html').write_text(home(chapters,progress),encoding='utf-8')
    (ROOT/'reference/sources.html').write_text(source_page(),encoding='utf-8')
    (ROOT/'reference/notation.html').write_text(notation_page(),encoding='utf-8')
    (ROOT/'reference/defense.html').write_text(defense_page(chapters,progress),encoding='utf-8')
    (ROOT/'verification/equations.json').write_text(json.dumps(EQUATIONS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'COURSE_SETTINGS.json').write_text(json.dumps(settings(chapters),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'.nojekyll').write_text('',encoding='utf-8')
    print(json.dumps({'chapters':len(chapters),'equations':len(EQUATIONS),'questions':sum(len(c['question_ids']) for c in chapters),'offline_math':True,'mastery':'awaits learner evidence'}))

if __name__=='__main__':main()
