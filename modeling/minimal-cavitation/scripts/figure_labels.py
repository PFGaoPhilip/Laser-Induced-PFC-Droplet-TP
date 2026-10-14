"""Chinese label editions of the project's own figures; source data stay fixed."""
from pathlib import Path
import xml.etree.ElementTree as ET

LABELS = {
 'Finite source routes to liquid outlet and hydrogel wall':'有限源通向液体出口与水凝胶壁面的能量路径',
 'Model Builder, Settings, Graphics and result areas':'模型树、设置、绘图与结果区域',
 'Rigid chamber':'刚性腔室','Open gel chamber':'开放通道凝胶腔室','Sealed gel control':'密封凝胶对照',
 'Time after initialization (µs)':'初始化后时间 (µs)','Outlet speed (m/s)':'出口速度 (m/s)',
 'First outward ejection':'首次向外排液','Elastic resistance':'弹性阻力',
 'Elastic + viscous resistance':'弹性 + 黏性阻力','Outlet dynamic pressure':'出口动压',
 'Pressure scale (kPa)':'压力尺度 (kPa)','Open-gel first event':'开放通道凝胶的首次过程',
 'Available post-activation work (nJ)':'激活后可用功 (nJ)',
 'Maximum speed by case':'各算例最大速率',
 'Solved speeds and energy ceilings':'求解速率与能量上限',
 'Column storage':'液柱储存动能','Gel radial motion':'凝胶径向运动','Gel elastic work':'凝胶弹性功',
 'Irreversible loss':'不可逆损失','Emitted jet':'排出射流','Meniscus work':'弯月面功',
 'Rigid':'刚性','Open gel':'开放通道凝胶','Source availability remaining':'剩余源可用功',
 'Share of 2 nJ source availability (%)':'占 2 nJ 源可用功的比例 (%)',
 'Energy at first-ejection endpoints':'首次排液终点能量',
 'Peak speed':'峰值速度','Emitted mass':'排出质量','Emitted energy':'排出动能','Emitted impulse':'排出冲量',
 'Open-gel / matched rigid output (%)':'开放通道凝胶 / 匹配刚性输出 (%)',
 'Finite-output transmission':'有限输出传导',
 'Wall radius / unstressed radius':'壁面半径 / 无应力半径','Elastic resistance (kPa)':'弹性阻力 (kPa)',
 'Intact spherical gel':'完整球形凝胶',
 'Open channel':'开放通道','Sealed control':'密封对照',
 'One-hemisphere axial resistance (µN)':'单半球轴向阻力 (µN)',
 'Hemisphere resistance, G = 20 kPa':'半球阻力，G = 20 kPa',
 'Finite initialized source':'有限初始化源','p0 + gas volume → available E0':'p0 + 气体体积 → 可用功 E0',
 'Pressure falls as Vg grows':'Vg 增大时压力下降','One short activation; initial data':'单次短时激活；初始数据',
 'Liquid outlet — A and open B':'液体出口 — A 与开放 B',
 'U → emitted mass, energy Eout, impulse Iout':'U → 排出质量、动能 Eout、冲量 Iout',
 'Column storage Kjet remains a separate output':'液柱储存动能 Kjet 单独记录',
 'Gel wall — Model B':'凝胶壁面 — 模型 B',
 'R, Uw → elastic pressure and hemisphere force':'R、Uw → 弹性压力与半球合力',
 'Radial inertia + stored elastic work + loss':'径向惯性 + 储存弹性功 + 损失',
 'Discharge increases Vg':'排出使 Vg 增大','Wall expansion increases Vg':'壁面膨胀使 Vg 增大',
 'A: fixed wall     B open: two energy routes     B sealed: wall route, zero discharge':'A：固定壁面　B 开放：两条能量路径　B 密封：壁面路径，零排出',
 '1 · Model Builder':'1 · 模型树（Model Builder）','2 · Settings':'2 · 设置（Settings）','3 · Graphics':'3 · 绘图（Graphics）',
 'Global Definitions':'全局定义（Global Definitions）','Parameters 1':'参数（Parameters 1）',
 'Component c':'组件 c','Definitions → Variables':'Definitions → Variables',
 'Global Equations 1':'全局方程（Global Equations 1）','Selected equation row:':'当前选中的方程行：',
 'Name: vv':'名称：vv','f: tau*(vvt-acc/Us)':'f: tau*(vvt-acc/Us)',
 'Initial u: 0     Initial ut: 0':'初始 u：0　初始 ut：0','Commit cells with Tab':'按 Tab 提交单元格输入',
 'First ejection time':'首次排出过程的时间','Bottom: Progress · Messages · Log · numerical result tables':'底部：进度 · 消息 · 日志 · 数值结果表',
}

def cjk_font():
    from matplotlib import font_manager
    available={entry.name for entry in font_manager.fontManager.ttflist}
    for name in ('Microsoft YaHei','Noto Sans CJK SC','SimHei','SimSun','DengXian'):
        if name in available:return name
    raise RuntimeError('A CJK font is required to render Chinese scientific plot labels.')

def localize_figure(fig):
    from matplotlib.text import Text
    from matplotlib.ticker import FixedLocator, FixedFormatter
    font=cjk_font()
    for axes in fig.axes:
        for axis in (axes.xaxis,axes.yaxis):
            values=[label.get_text() for label in axis.get_ticklabels()]
            if any(value in LABELS for value in values):
                axis.set_major_locator(FixedLocator(axis.get_majorticklocs()))
                axis.set_major_formatter(FixedFormatter([LABELS.get(value,value) for value in values]))
    for text in fig.findobj(Text):
        value=text.get_text();translated=LABELS.get(value)
        if translated is None and value.startswith('Outlet radius '):translated=value.replace('Outlet radius ','出口半径 ')
        if translated is None and ' µm: solved / dashed ceiling' in value:translated=value.replace(' µm: solved / dashed ceiling',' µm：实线求解 / 虚线上限')
        if translated is not None:text.set_text(translated)
        text.set_fontfamily(font)

def localized_schematics(root):
    for name in ('guide-mechanisms','guide-interface'):
        tree=ET.parse(root/'assets'/f'{name}.svg')
        for node in tree.iter():
            if node.text in LABELS:node.text=LABELS[node.text]
            if 'font-family' in node.attrib:node.set('font-family','Microsoft YaHei,Segoe UI,Arial,sans-serif')
            if node.get('aria-label') in LABELS:node.set('aria-label',LABELS[node.get('aria-label')])
            # Leave enough room for the localized headings in the original panels.
            if name=='guide-interface' and node.get('y')=='53':node.set('font-size','20')
            if name=='guide-mechanisms' and node.get('x')=='32' and node.get('y')=='38':node.set('font-size','17')
        tree.write(root/'assets'/f'{name}.zh.svg',encoding='utf-8',xml_declaration=True)
