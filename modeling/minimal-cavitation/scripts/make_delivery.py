"""Build the portable reader, scientific plots, results and complete TeX source."""
from __future__ import annotations
import base64
import html
import json
import re
import shutil
import subprocess
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import markdown
from bs4 import BeautifulSoup

from reference import ROOT
from verify_results import read_native


def savefig(fig,name,locale="en"):
    if locale == "zh":
        from figure_labels import localize_figure
        localize_figure(fig)
        name += ".zh"
    for ext in ['png','svg']:
        fig.savefig(ROOT/'assets'/f'{name}.{ext}',dpi=190,bbox_inches='tight')
    plt.close(fig)


def plots(reg,locale="en"):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                         'axes.spines.top':False,'axes.spines.right':False,
                         'axes.grid':True,'grid.alpha':0.18})
    a=read_native(ROOT/'data/A_baseline_native.csv')
    b=read_native(ROOT/'data/B_open_baseline_native.csv')
    sealed=read_native(ROOT/'data/B_sealed_control_native.csv')
    fig,ax=plt.subplots(1,2,figsize=(10.8,4.0))
    for vals,label,col in [(a,'Rigid chamber','#3479cb'),(b,'Open gel chamber','#d16b34'),(sealed,'Sealed gel control','#757575')]:
        ax[0].plot(vals['time_s']*1e6,vals['u_m_s'],label=label,color=col)
    ax[0].set(xlabel='Time after initialization (µs)',ylabel='Outlet speed (m/s)',title='First outward ejection')
    ax[0].legend(frameon=False,fontsize=9)
    ax[1].plot(b['time_s']*1e6,b['elastic_Pa']/1000,label='Elastic resistance',color='#9460a5')
    ax[1].plot(b['time_s']*1e6,b['gel_wall_resistance_Pa']/1000,label='Elastic + viscous resistance',color='#d16b34')
    ax[1].plot(b['time_s']*1e6,b['jet_dynamic_Pa']/1000,label='Outlet dynamic pressure',color='#3479cb')
    ax[1].set(xlabel='Time after initialization (µs)',ylabel='Pressure scale (kPa)',title='Open-gel first event')
    ax[1].legend(frameon=False,fontsize=8)
    savefig(fig,'first_event_histories',locale)

    fig,ax=plt.subplots(1,2,figsize=(10.8,4.0))
    for rad,col in [(3,'#3479cb'),(5,'#d16b34'),(10,'#9460a5')]:
        cases=sorted([r for r in reg if r['name'].startswith('A_E') and abs(r['port_radius_m']-rad*1e-6)<1e-12],key=lambda r:r['source_energy_J'])
        en=np.array([r['source_energy_J']*1e9 for r in cases])
        vel=[r['native_max_jet_speed_m_s'] for r in cases]
        ceiling=[r['energy_only_speed_ceiling_m_s'] for r in cases]
        ax[0].plot(en,vel,'o-',label=f'Outlet radius {rad} µm',color=col)
        ax[1].plot(en,ceiling,'--',color=col,alpha=.7)
        ax[1].plot(en,vel,'o-',color=col,label=f'{rad} µm: solved / dashed ceiling')
    for x in ax:x.set(xlabel='Available post-activation work (nJ)',ylabel='Outlet speed (m/s)')
    ax[0].set_title('Maximum speed by case')
    ax[1].set_title('Solved speeds and energy ceilings')
    for x in ax:x.legend(frameon=False,fontsize=8)
    savefig(fig,'conditional_velocity_envelope',locale)

    fig,ax=plt.subplots(1,2,figsize=(10.8,4.1))
    energies=['kinetic_column_J','kinetic_gel_J','elastic_J','dissipation_J','emitted_energy_J','capillary_J']
    labels=['Column storage','Gel radial motion','Gel elastic work','Irreversible loss','Emitted jet','Meniscus work']
    colors=['#3479cb','#9460a5','#8ab3cc','#9b9b9b','#d16b34','#d6bd70']
    bottoms=np.zeros(2)
    for key,label,col in zip(energies,labels,colors):
        val=np.array([a[key][-1],b[key][-1]])/2e-9*100
        ax[0].bar(['Rigid','Open gel'],val,bottom=bottoms,label=label,color=col)
        bottoms+=val
    ax[0].bar(['Rigid','Open gel'],100-bottoms,bottom=bottoms,label='Source availability remaining',color='#eef0f5',edgecolor='#ccc')
    ax[0].set(ylabel='Share of 2 nJ source availability (%)',ylim=(0,100),title='Energy at first-ejection endpoints')
    handles, legend_labels = ax[0].get_legend_handles_labels()
    fig.legend(handles, legend_labels, frameon=False, fontsize=8, ncol=3,
               loc='lower center', bbox_to_anchor=(0.5, -0.26))
    ratio=np.array([np.max(b['u_m_s'])/np.max(a['u_m_s']),b['emitted_mass_kg'][-1]/a['emitted_mass_kg'][-1],b['emitted_energy_J'][-1]/a['emitted_energy_J'][-1],b['emitted_impulse_N_s'][-1]/a['emitted_impulse_N_s'][-1]])*100
    ax[1].barh(['Peak speed','Emitted mass','Emitted energy','Emitted impulse'],ratio,color=['#3479cb','#8ab3cc','#d16b34','#9460a5'])
    for i,v in enumerate(ratio):ax[1].text(v+.25,i,f'{v:.3f}%',va='center',fontsize=9)
    ax[1].set(xlabel='Open-gel / matched rigid output (%)',xlim=(0,max(ratio)*1.25),title='Finite-output transmission')
    fig.subplots_adjust(wspace=0.85)
    savefig(fig,'energy_and_transmission',locale)

    fig,ax=plt.subplots(1,2,figsize=(10.8,4))
    rr=np.linspace(1,1.2,201)
    for g,col in [(5000,'#3479cb'),(20000,'#d16b34'),(100000,'#9460a5')]:
        pel=g/2*(5-4/rr-rr**-4)
        ax[0].plot(rr,pel/1000,label=f'G = {g/1000:g} kPa',color=col)
    ax[0].set(xlabel='Wall radius / unstressed radius',ylabel='Elastic resistance (kPa)',title='Intact spherical gel')
    ax[0].legend(frameon=False)
    for vals,label,col in [(b,'Open channel','#d16b34'),(sealed,'Sealed control','#757575')]:
        ax[1].plot(vals['time_s']*1e6,vals['confinement_hemisphere_force_N']*1e6,label=label,color=col)
    ax[1].set(xlabel='Time after initialization (µs)',ylabel='One-hemisphere axial resistance (µN)',title='Hemisphere resistance, G = 20 kPa')
    ax[1].legend(frameon=False)
    savefig(fig,'gel_confinement',locale)


def results_document(reg,audit):
    a=next(r for r in reg if r['name']=='A_baseline')
    b=next(r for r in reg if r['name']=='B_open_baseline')
    sealed=next(r for r in reg if r['name']=='B_sealed_control')
    strongest=max((r for r in reg if r['name'].startswith('A_')),key=lambda r:r['native_max_jet_speed_m_s'])
    sa,sb=a['last_native_state'],b['last_native_state']
    text=f'''# Results and interpretation

Both native models use **Global Equations**. Model A solves two flow states and three accumulators. Model B adds two gel-wall states. The nominal **10 ns pulse is represented by post-activation initial data**. Optical heating, nucleation and the activation pressure transient are excluded.

Baseline inputs: available work 2 nJ; initial gas radius 15 µm; chamber radius 30 µm; outlet radius 5 µm; effective inertance length 50 µm; density 1000 kg/m³; ambient pressure 100 kPa; adiabatic exponent 1.4. Connected chamber liquid sets the finite discharge budget. Gel inputs are G = 20 kPa and viscosity 0.010 Pa s. These inputs define the controls. PFC and hydrogel calibration remain unresolved.

| Defined output | Rigid chamber A | Open hydrogel B |
|---|---:|---:|
| Initial chamber overpressure | {a['native_max_source_gauge_Pa']/1000:.3f} kPa | {b['native_max_source_gauge_Pa']/1000:.3f} kPa |
| Highest first-ejection outlet speed | {a['native_max_jet_speed_m_s']:.5f} m/s | {b['native_max_jet_speed_m_s']:.5f} m/s |
| Highest outlet dynamic-pressure scale | {a['native_max_jet_dynamic_Pa']/1000:.4f} kPa | {b['native_max_jet_dynamic_Pa']/1000:.4f} kPa |
| Emitted mass over first ejection | {sa['emitted_mass_kg']*1e12:.5f} ng | {sb['emitted_mass_kg']*1e12:.5f} ng |
| Emitted energy | {sa['emitted_energy_J']*1e9:.6f} nJ | {sb['emitted_energy_J']*1e9:.6f} nJ |
| Emitted impulse | {sa['emitted_impulse_N_s']:.6e} N s | {sb['emitted_impulse_N_s']:.6e} N s |
| First outward ejection duration | {a['last_time_s']*1e6:.4f} µs | {b['last_time_s']*1e6:.4f} µs |
| Largest elastic confinement pressure | — | {b['native_max_elastic_Pa']/1000:.4f} kPa |
| Largest one-hemisphere elastic force | — | {b['native_max_hemisphere_force_N']*1e6:.4f} µN |

The highest sampled outlet speed occurs in **{strongest['name']}**: **{strongest['native_max_jet_speed_m_s']:.5f} m/s**. Source overpressure is **{strongest['native_max_source_gauge_Pa']/1000:.3f} kPa**. Outlet dynamic pressure is **{strongest['native_max_jet_dynamic_Pa']/1000:.3f} kPa**. The family samples work 0.5, 2 and 5 nJ. It samples outlet radii 3, 5 and 10 µm. Initial gas/chamber radii and inertance length stay fixed. These are conditional maxima within the sampled family. A universal limit is not established.

The baseline energy ceiling is **{a['energy_only_speed_ceiling_m_s']:.5f} m/s**. Its dynamic-pressure ceiling is **{a['energy_only_dynamic_pressure_ceiling_Pa']/1000:.3f} kPa**. The solution also spends energy on emission and meniscus work. Energy remains in column motion and the source. The solved maximum is therefore below these bounds.

Open-gel peak-speed transmission is **{audit['first_event_velocity_transmission']*100:.4f}%**. Emitted-energy transmission is **{audit['first_event_emitted_energy_transmission']*100:.5f}%**. Emitted-impulse transmission is **{audit['first_event_emitted_impulse_transmission']*100:.5f}%**. Integrate outlet fluxes to obtain energy and impulse. Peak-speed ratios cannot replace those integrals. Here gel motion receives energy and shortens the first ejection. General monotonic effects of modulus and viscosity are not established.

The sealed control emits zero mass, energy and impulse. Its maximum elastic pressure is {sealed['native_max_elastic_Pa']/1000:.4f} kPa. Its maximum inner-wall stretch is {sealed['native_max_stretch']:.5f}. The gel deforms while external discharge remains zero.

The observer diagnostic bounds mean arrest pressure from emitted impulse. It uses outlet area and a 1 µs interval. Peak impact pressure is not established. Missing: contact dynamics, arriving mass, target transmission and gel fracture.

![Native first-ejection histories](assets/first_event_histories.png)

![Conditional velocity family](assets/conditional_velocity_envelope.png)

![Energy allocation and emitted output](assets/energy_and_transmission.png)

![Defined gel resistance and confinement force](assets/gel_confinement.png)

Native verification passed for all {audit['native_case_count']} cases. Maximum normalized energy residual: {audit['maximum_native_energy_residual']:.3e}. Maximum native/reference waveform error: {audit['maximum_native_reference_normalized_waveform_error']:.3e}. Maximum pressure-communication diagnostic: {audit['maximum_communication_screen']:.5f}, below the stipulated 0.1 screen. Both baselines were reloaded and solved in a fresh COMSOL process. Peak velocities passed the 2 ns / 1 ns resolution check. These checks verify the specified implementation and temporal convergence. Experimental validation remains unresolved. Missing: PFC EOS/phase inventory, laser conversion, gel calibration and device geometry.

See [the full worked derivation](MODEL_SPEC.md), [native case register](data/native_case_register.json), [numerical audit](verification/NUMERICAL_AUDIT.json) and the two native files in [models/](models/).
'''
    (ROOT/'RESULTS.md').write_text(text,encoding='utf-8')
    return text


def render_md(text):
    slots=[]
    def slot(tex,display):
        i=len(slots);slots.append((tex.strip(),display));return f'MATHSLOT{i}END'
    text=re.sub(r'\$\$(.*?)\$\$',lambda m:'\n\n'+slot(m.group(1),True)+'\n\n',text,flags=re.S)
    text=re.sub(r'\$([^$\n]+)\$',lambda m:slot(m.group(1),False),text)
    rendered=markdown.markdown(text,extensions=['tables','fenced_code','toc'])
    for i,(tex,display) in enumerate(slots):
        code=base64.b64encode(tex.encode()).decode()
        element=f'<{"div" if display else "span"} class="math{" display" if display else ""}" data-tex="{code}"></{"div" if display else "span"}>'
        marker=f'MATHSLOT{i}END'
        if display:rendered=rendered.replace('<p>'+marker+'</p>',element)
        else:rendered=rendered.replace(marker,element)
    return rendered,slots


def tex_document(text):
    rendered,slots=render_md(text)
    soup=BeautifulSoup(rendered,'html.parser')
    def esc(t):
        mapping={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
        return ''.join(mapping.get(c,c) for c in t)
    def convert(node):
        if isinstance(node,str):return esc(node)
        if node.get('data-tex'):
            tex=base64.b64decode(node['data-tex']).decode()
            return '\n\\begin{equation*}\n'+tex+'\n\\end{equation*}\n' if 'display' in node.get('class',[]) else r'\('+tex+r'\)'
        inner=''.join(convert(c) for c in node.children)
        name=node.name
        if name in ['h1','h2','h3']:
            cmd={'h1':'section*','h2':'subsection*','h3':'subsubsection*'}[name]
            return '\n\\'+cmd+'{'+inner+'}\n'
        if name=='p':return inner+'\n\n'
        if name=='strong':return r'\textbf{'+inner+'}'
        if name=='em':return r'\emph{'+inner+'}'
        if name=='code':return r'\texttt{'+inner+'}'
        if name=='a':return r'\href{'+esc(node.get('href',''))+'}{'+inner+'}'
        if name=='table':
            rows=[]
            for row in node.find_all('tr'):
                cells=[convert(c) for c in row.find_all(['th','td'],recursive=False)]
                rows.append(' & '.join(cells)+r' \\')
            return '\n\\begin{longtable}{p{0.22\\textwidth}p{0.53\\textwidth}p{0.16\\textwidth}}\n'+ '\n'.join(rows)+'\n\\end{longtable}\n'
        return inner
    body=''.join(convert(c) for c in soup.children)
    head=r'''% Complete editable mathematical source; compile with LuaLaTeX.
\documentclass[11pt]{article}
\usepackage[a4paper,margin=22mm]{geometry}
\usepackage{fontspec}
\setmainfont{TeX Gyre Termes}
\usepackage{amsmath,amssymb,longtable,hyperref}
\hypersetup{colorlinks=true,urlcolor=blue}
\setlength{\emergencystretch}{3em}
\begin{document}
'''
    (ROOT/'THEORY_DERIVATION.tex').write_text(head+body+'\n\\end{document}\n',encoding='utf-8')


def main(readers_only=False):
    audit=json.loads((ROOT/'verification/NUMERICAL_AUDIT.json').read_text(encoding='utf-8'))
    if audit['status']!='PASS':raise RuntimeError('Numeric acceptance required before reader generation')
    reg=json.loads((ROOT/'data/native_case_register.json').read_text(encoding='utf-8'))
    if not readers_only:
        plots(reg)
        plots(reg, "zh")
    results=results_document(reg,audit)
    spec=(ROOT/'MODEL_SPEC.md').read_text(encoding='utf-8')
    tex_document(spec)
    origin=ROOT.parents[2]/'Laser_Induced_PFC_Droplet_TP/assets/vendor/katex'
    dest=ROOT/'assets/vendor/katex';dest.mkdir(parents=True,exist_ok=True)
    if not all((dest/f).is_file() for f in ['katex.min.css','katex.min.js']) or not (dest/'fonts').is_dir():
        for f in ['katex.min.css','katex.min.js']:shutil.copy2(origin/f,dest/f)
        shutil.copytree(origin/'fonts',dest/'fonts',dirs_exist_ok=True)
    results_html,_=render_md(results)
    spec_html,slots=render_md(spec)
    intro='''<header><p class="eyebrow">Single event · Finite energy · Two models</p><h1>Minimal cavitation &amp; hydrogel models</h1><p>Calculate outlet discharge and gel loading from a finite source.</p><nav><a href="STEP_BY_STEP.html">53-step COMSOL guide</a><a href="#results">Results</a><a href="#models">Models and rebuild</a><a href="#theory">Derivation</a><a href="verification/NUMERICAL_AUDIT.json">Audit</a></nav></header>'''
    model_links='''<section id="models"><h2>Models and rebuild</h2><p>The <a href="STEP_BY_STEP.html">53-step guide</a> builds both models from a blank 0D model. It provides inputs, solver settings, stopping rules and output checks. <a href="STEP_BY_STEP.md">Markdown guide</a> · <a href="resources/gui/">Input files</a>.</p><p><a href="models/Model_A_Finite_Energy_Pressure_Jet.mph">Model A — finite-energy outlet discharge</a><br><a href="models/Model_B_Hydrogel_Confinement_Jet_Transmission.mph">Model B — gel confinement and outlet transmission</a></p><p>Open the MPH files in COMSOL 6.4. Each includes one component, Global Equations and a transient study. Result tables and time histories are saved. These scalar models need no spatial mesh. Model B's <code>outletOpen</code> selects an existing channel or sealed control.</p><p><code>.\Run-Rebuild.ps1</code> rebuilds the native case family. <code>.\Run-Verify.ps1</code> reloads and checks baselines. <code>.\Run-CheckGuide.ps1</code> checks imports and A-to-B conversion in memory. Install <a href="requirements.txt">requirements.txt</a> for Python checks. Run <code>python scripts/reference.py</code> and <code>python scripts/verify_results.py</code>. Parameter changes and validity limits appear in <a href="README.md">README.md</a>.</p><p><a href="THEORY_DERIVATION.tex">Editable LaTeX</a> · <a href="MODEL_SPEC.md">Derivation source</a> · <a href="data/case_inputs.json">Case inputs</a> · <a href="PUBLICATION.md">Reader provenance</a></p></section>'''
    from bilingual_reader import write_report
    english_body = intro + '<main><section id="results">' + results_html + '</section>' + model_links + '<details id="theory"><summary>Complete worked derivation: 29 equation blocks with symbols, assumptions and checks</summary><article>' + spec_html + '</article></details></main><footer>Independent numerical integration, native COMSOL checks and self-audit are distinguished from independent expert review.</footer>'
    english_body = re.sub(r'<button id="theme".*?</button>', '', english_body)
    chinese_results, _ = render_md((ROOT/'RESULTS.zh.md').read_text(encoding='utf-8'))
    chinese_spec, _ = render_md((ROOT/'MODEL_SPEC.zh.md').read_text(encoding='utf-8'))
    chinese_intro = '<header><p class="eyebrow">单次事件 · 有限能量 · 两个模型</p><h1>简洁空化与水凝胶模型</h1><p>由有限源计算出口排液与凝胶载荷。</p><nav><a href="STEP_BY_STEP.html">53 步 COMSOL 指南</a><a href="#results">结果</a><a href="#models">模型与重建</a><a href="#theory">推导</a><a href="verification/NUMERICAL_AUDIT.json">核验</a></nav></header>'
    chinese_models = '<section id="models"><h2>模型与重建</h2><p><a href="STEP_BY_STEP.html">53 步指南</a>从空白 0D 模型建立两个模型。它给出输入、求解器设置、停止规则和输出检查。<a href="STEP_BY_STEP.zh.md">中文 Markdown</a> · <a href="resources/gui/">输入文件</a>。</p><p><a href="models/Model_A_Finite_Energy_Pressure_Jet.mph">模型 A — 有限能量出口排液</a><br><a href="models/Model_B_Hydrogel_Confinement_Jet_Transmission.mph">模型 B — 凝胶约束与出口传导</a></p><p>在 COMSOL 6.4 中打开 MPH 文件。每个文件含一个组件、全局方程及瞬态研究。结果表与时间历程已保存。标量模型无需空间网格。模型 B 的 <code>outletOpen</code> 选择已有通道或密封对照。</p><p><code>.\\Run-Rebuild.ps1</code> 重建原生案例族。<code>.\\Run-Verify.ps1</code> 重新载入并检查基准。<code>.\\Run-CheckGuide.ps1</code> 在内存中检查导入及 A 至 B 转换。安装 <a href="requirements.txt">requirements.txt</a> 后运行 Python 检查：<code>python scripts/reference.py</code>、<code>python scripts/verify_results.py</code>。参数修改与适用范围见 <a href="README.md">README.md</a>。</p><p><a href="THEORY_DERIVATION.tex">可编辑 LaTeX</a> · <a href="MODEL_SPEC.zh.md">推导源码</a> · <a href="data/case_inputs.json">案例输入</a> · <a href="PUBLICATION.md">读者文件来源</a></p></section>'
    chinese_body = chinese_intro + '<main><section id="results">' + chinese_results + '</section>' + chinese_models + '<details id="theory"><summary>完整推导：29 个公式块、符号、假设与检查</summary><article>' + chinese_spec + '</article></details></main><footer>独立数值积分、原生 COMSOL 检查与自审，与独立专家评审分别记录。</footer>'
    write_report(english_body, chinese_body)
    subprocess.run(['node',str(ROOT/'scripts/prerender_math.cjs'),str(ROOT/'index.html')],check=True)
    print('Bilingual reader and eight scientific PNG/SVG pairs generated. Math displays per language:',len(re.findall(r'\$\$',spec))//2)


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--readers-only',action='store_true',help='Rebuild reader and TeX from existing audited plots and data.')
    main(readers_only=parser.parse_args().readers_only)
