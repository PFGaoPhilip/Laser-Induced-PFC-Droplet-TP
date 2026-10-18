"""Numbered objectives and chapter dependencies for all 33 derivation groups."""
import re
from bs4 import BeautifulSoup
from coursekit import H, P
from equation_symbols import equation_label

# Each entry explains the result's role, rather than repeating its equation title.
DATA = [
('Specify the cavity problem', '规定空腔问题',
 'Choose the initial radius, wall speed, and far-field conditions. These inputs make the radial dynamics in Section 1.3 a defined initial-value problem.',
 '选定初始半径、壁面速度与远场条件。这些输入使第1.3节的径向动力学成为明确的初值问题。'),
('Obtain the liquid velocity from cavity motion', '由空腔运动求载液速度',
 'Use the spherical conditions in Eq. (C1-E01). Volume conservation converts wall motion into the exterior velocity field needed for momentum and energy calculations.',
 '采用式（C1-E01）的球形条件。体积守恒把壁面运动转为外域速度场，为后续动量与能量计算提供输入。'),
('Prepare the velocity field for momentum integration', '为动量积分建立速度势',
 'Integrate the velocity from Eq. (C1-E02) and fix its reference. The resulting potential lets the radial momentum equation become a pressure relation.',
 '积分式（C1-E02）的速度并固定参考值。所得速度势使径向动量方程能够转化为压力关系。'),
('Separate fixed-position and moving-wall time changes', '区分固定位置与运动壁面的时间变化',
 'Differentiate the potential from Eq. (C1-E03). Bernoulli requires the fixed-position derivative, so this distinction prevents an incorrect wall-inertia term.',
 '对式（C1-E03）的速度势求导。伯努利关系需要固定位置导数，因此这一区分可避免错误的壁面惯性项。'),
('Connect liquid inertia to wall pressure', '将液体惯性与壁面压力联系起来',
 'Insert Eqs. (C1-E02)–(C1-E04) into the integrated momentum law. This expresses liquid-side wall pressure through radius, speed, and acceleration.',
 '将式（C1-E02）至（C1-E04）代入积分动量关系。由此用半径、速度与加速度表示壁面液体侧压力。'),
('Transfer bubble pressure across the interface', '将气泡压力传递至液体界面',
 'Apply normal-stress balance at the spherical wall. Surface tension and viscosity connect bubble pressure to the liquid pressure required by Eq. (C1-E05).',
 '在球形壁面应用法向应力平衡。表面张力与黏度将气泡压力连接至式（C1-E05）所需的液体压力。'),
('Assemble the radial equation of motion', '组合得到径向运动方程',
 'Combine Eqs. (C1-E05) and (C1-E06). The resulting Rayleigh–Plesset equation converts a prescribed pressure history into spherical cavity motion.',
 '联立式（C1-E05）与（C1-E06）。所得 Rayleigh–Plesset 方程将给定压力历程转为球形空腔运动。'),
('Identify the pressure input still needing closure', '明确仍需闭合的压力输入',
 'Separate vapor and permanent-gas contributions to the pressure in Eq. (C1-E07). Chapter 2 must supply their thermal, phase, and inventory evolution.',
 '将式（C1-E07）的压力分解为蒸气与非凝结气体贡献。第二章须提供其热、相变及物质量演化。'),
('Measure the inertia carried by the exterior liquid', '计算外部载液携带的动能',
 'Integrate the velocity field from Eq. (C1-E02). Exterior kinetic energy provides the energy measure for checking the radial pressure-driven motion.',
 '积分式（C1-E02）的速度场。外域动能提供能量尺度，用于检验压力驱动的径向运动。'),
('Convert stored energies into rates', '将储存能量转为变化率',
 'Differentiate Eq. (C1-E09), the surface energy, and cavity volume. Their rates allow the momentum equation to be checked as a power balance.',
 '对式（C1-E09）、表面能及空腔体积求导。这些变化率使动量方程能够通过功率平衡接受检验。'),
('Check where pressure work goes', '检验压力功的去向',
 'Combine the motion law in Eq. (C1-E07) with Eq. (C1-E10). This separates kinetic-energy storage, surface-energy storage, and viscous loss.',
 '将式（C1-E07）的运动规律与式（C1-E10）结合。由此区分动能储存、表面能储存与黏性损耗。'),
('Define a solvable ideal-collapse benchmark', '规定可解的理想塌缩基准',
 'Reduce Eq. (C1-E07) to collapse under a constant positive pressure difference. This restricted control problem supplies the trajectory and time benchmark below.',
 '将式（C1-E07）约化为恒定正压差下的塌缩。这一受限对照问题为下文提供轨迹与时间基准。'),
('Replace time by radius on the collapse branch', '在塌缩分支以半径替代时间',
 'Transform Eq. (C1-E12) into a first-order equation for squared speed. Its integrating factor prepares a trajectory satisfying the maximum-radius initial condition.',
 '将式（C1-E12）转为速度平方的一阶方程。其积分因子用于构造满足最大半径初始条件的轨迹。'),
('Recover inward speed and its integration constant', '求向内速度及积分常数',
 'Integrate Eq. (C1-E13) from the stationary maximum-radius state. Select the inward branch before using its reciprocal to calculate collapse time.',
 '从最大半径处的静止状态积分式（C1-E13）。先选取向内分支，再用速度倒数计算塌缩时间。'),
('Separate collapse time from geometric scale', '分离塌缩时间与几何尺度',
 'Integrate the reciprocal speed from Eq. (C1-E14). Nondimensionalizing radius isolates the universal integral from radius, density, and pressure scales.',
 '积分式（C1-E14）的速度倒数。将半径无量纲化，把通用积分与半径、密度及压力尺度分离。'),
('Evaluate the Rayleigh time coefficient', '计算瑞利塌缩时间系数',
 'Evaluate the dimensionless integral in Eq. (C1-E15). This establishes the coefficient used in the worked collapse-time calculation.',
 '计算式（C1-E15）的无量纲积分。由此确定塌缩时间算例所用的系数。'),
('Cross-check the ideal trajectory with pressure work', '用压力功交叉检验理想轨迹',
 'Insert Eq. (C1-E14) into the kinetic energy from Eq. (C1-E09). Agreement with pressure work checks the collapse branch and integration constant.',
 '将式（C1-E14）代入式（C1-E09）的动能。与压力功的一致性用于检验塌缩分支及积分常数。'),
('Put the ideal benchmark on a numerical scale', '给出理想基准的数值尺度',
 'Apply Eqs. (C1-E14)–(C1-E17) to the declared teaching inputs. This translates the benchmark into time, energy, and speed before testing its validity.',
 '将式（C1-E14）至（C1-E17）用于已声明的教学输入。由此先得到时间、能量与速度尺度，再检验适用性。'),
('Locate where the ideal speed needs further physics', '定位理想速度需要补充物理的位置',
 'Compare the ideal wall speed with a chosen Mach threshold. This diagnoses the incompressible trajectory without establishing a physical maximum speed.',
 '将理想壁面速度与选定的马赫数阈值比较。这用于诊断不可压缩轨迹，不确立实际最大速度。'),
('Summarize a pressure history as pressure impulse', '用压力冲量概括压力历程',
 'Move from spherical radius dynamics to spatial liquid response. Define a local time-integrated pressure field whose gradient enters the next momentum calculation.',
 '从球形半径动力学转向空间液体响应。定义局部压力时间积分场，其梯度将进入下一步动量计算。'),
('Convert pressure history into liquid velocity change', '将压力历程转为液体速度变化',
 'Use the pressure impulse defined in Eq. (C1-E20). Integrating momentum separates pressure, convective, and viscous contributions to velocity change. This exact model identity is the starting point for Eq. (C1-E22).',
 '采用式（C1-E20）定义的压力冲量。积分动量方程，分离压力、对流与黏性对速度变化的贡献。这一模型内精确恒等式是式（C1-E22）的起点。'),
('Decide when pressure impulse dominates the event', '判断事件何时由压力冲量主导',
 'Estimate the convective and viscous terms retained in Eq. (C1-E21). Under the stated short-event conditions, the reduced model links incompressibility to a pressure-impulse boundary problem.',
 '估计式（C1-E21）保留的对流与黏性项。在已声明的短事件条件下，约化模型将不可压缩条件连接至压力冲量边值问题。'),
('Show how a boundary selects the liquid-motion direction', '说明边界如何选择液体运动方向',
 'Solve the reduced model from Eq. (C1-E22) for a straight column. Inlet and outlet impulses select a gradient and therefore an axial velocity increment.',
 '对直液柱求解式（C1-E22）的约化模型。入口与出口冲量确定梯度，进而确定轴向速度增量。'),
('Check the scale and assumptions of the column result', '检验液柱结果的尺度与假设',
 'Apply Eq. (C1-E23) to a declared pressure pulse. Calculate velocity change and compare acoustic, convective, and viscous scales before interpreting that result.',
 '将式（C1-E23）用于给定压力脉冲。计算速度变化，并比较声学、对流与黏性尺度，再解释该结果。'),
('Explain why a spherical cavity cannot choose a jet direction', '说明球形空腔为何不能选择射流方向',
 'Contrast spherical symmetry with the directed column in Eq. (C1-E23). This identifies the geometric information missing from a radius-only model and motivates Section 1.7.',
 '对比球形对称性与式（C1-E23）的定向液柱。由此明确纯半径模型缺失的几何信息，并引出第1.7节。'),
('Replace the radius model with spatial liquid equations', '用空间液体方程替代纯半径模型',
 'Retain the mass and momentum laws across the actual liquid domain. These equations provide the spatial dynamics needed when boundaries and interface shape determine the jet.',
 '在实际液体区域保留质量与动量守恒规律。当边界及界面形状决定射流时，这些方程提供所需的空间动力学。'),
('Close the spatial model at its moving interface', '在运动界面闭合空间模型',
 'Add interface motion and traction conditions to Eq. (C1-E26). Their orientation and stress signs must recover the spherical jump in Eq. (C1-E06).',
 '为式（C1-E26）补充界面运动与牵引条件。其方向与应力符号须恢复式（C1-E06）的球形跃变关系。'),
('Construct a conditional pre-impact interface solver', '构造有条件的撞击前界面求解模型',
 'Reduce Eqs. (C1-E26) and (C1-E27) under the stated inviscid potential-flow assumptions. The resulting system evolves interface shape and can resolve directional pre-impact motion.',
 '在已声明的无黏势流假设下约化式（C1-E26）与（C1-E27）。所得系统演化界面形状，可解析撞击前的定向运动。'),
('Recover the radial model as a consistency check', '恢复径向模型以检验一致性',
 'Apply Eq. (C1-E28) to a sphere. Recovering the inviscid form of Eq. (C1-E07) checks the moving-interface signs and derivative convention.',
 '将式（C1-E28）用于球面。恢复无黏形式的式（C1-E07），用于检验运动界面的符号与导数约定。'),
('Check whether incompressibility is adequate for the event', '检验事件是否适用不可压缩近似',
 'Compare wall speed and event duration with acoustic scales. These separate diagnostics delimit both the pressure-impulse reduction and the incompressible interface model.',
 '将壁面速度与事件持续时间同声学尺度比较。这两个独立诊断分别限定压力冲量约化及不可压缩界面模型的适用范围。'),
('Connect bubble pressure to the transfer-jet explanation', '将气泡压力连接至转印射流解释',
 'Combine the radial balance and pressure composition from Section 1.3. Use them to explain the source of liquid motion, then identify the boundary information required for an external jet.',
 '结合第1.3节的径向平衡与压力组成。用它们解释液体运动的来源，再指出外部射流还需要的边界信息。'),
('Reconstruct the collapse benchmark and its limits', '重建塌缩基准及其限制',
 'Combine the trajectory, collapse-time coefficient, and energy check from Section 1.5. Explain their shared assumptions before discussing the ideal speed singularity.',
 '结合第1.5节的轨迹、塌缩时间系数与能量检验。在讨论理想速度奇异性之前，说明这些结果共有的假设。'),
('Connect pressure history, geometry, and response time', '贯通压力历程、几何与响应时间',
 'Combine Sections 1.6 and 1.7. Distinguish the exact momentum integral, its reduced column benchmark, and the additional spatial and acoustic inputs needed for a transfer-jet prediction.',
 '结合第1.6节与第1.7节。区分精确动量积分、其约化液柱基准，以及预测转印射流还需要的空间与声学输入。'),
]

def step_number(identifier):
    number=int(identifier[-2:])
    start=next(start for start,end in [(1,1),(2,8),(9,11),(12,19),(20,25),(26,30),(31,33)] if start<=number<=end)
    section=equation_label(identifier).split('-')[0][1:]
    return f'{section}.{number-start+1}'

def introduction(identifier):
    title_en,title_zh,en,zh=DATA[int(identifier[-2:])-1]
    number=step_number(identifier)
    level=4 if identifier in {'C1-E18','C1-E19','C1-E31','C1-E32','C1-E33'} else 3
    heading=H(f'Step {number} — {title_en}',f'步骤 {number}——{title_zh}',
              'step-'+number.replace('.','-'),level)
    heading=heading.replace('class="heading-pair"',f'class="heading-pair derivation-step" data-step-for="{identifier}" data-step-number="{number}"',1)
    return heading+P('<strong>Purpose in this chapter.</strong> '+en,
                     '<strong>本章作用。</strong> '+zh,'step-purpose')

def normalize_existing_steps(html):
    """Retain all old explanations under their newly numbered step heading."""
    soup=BeautifulSoup(html,'html.parser')
    for heading in soup.select('.derivation-step'):
        previous=heading.find_previous_sibling()
        if previous is None:continue
        strong=previous.select_one('p[lang=en] > strong')
        if not strong or not re.match(r'Step\s+[\d.]+\s*—',strong.get_text()):continue
        for node in list(previous.find_all(string=True)):
            value=re.sub(r'^(?:Step|步骤)\s*[\d.]+\s*—+\s*','',str(node))
            if value!=str(node):node.replace_with(value)
        heading.find_next_sibling().insert_after(previous.extract())
    return str(soup)
