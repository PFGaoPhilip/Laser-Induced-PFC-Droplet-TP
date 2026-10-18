r"""Chapter 5: jet on a rigid wall — theory, calculation and solver verification."""
import csv
import json
from pathlib import Path

from coursekit import P, H, E, T, cite, defense, note
from symbol_tables import glossary
from chapter05_spec import EQS

DATA = Path(__file__).resolve().parents[1] / 'sources/rigid_wall_ch5'
SPEC = {e['n']: e for e in EQS}


def eq(n):
    e = SPEC[n]
    sym_en = '; '.join(f"${s}$ — {en}" for s, en, zh, u in e['rows']) + '.'
    sym_zh = '；'.join(f"${s}$ — {zh}" for s, en, zh, u in e['rows']) + '。'
    return E(f"C5-E{n:02d}", e['tex'], sym_en, sym_zh, e['kind'],
             {"type": e['dtype'], "labels": e['labels'], "notes": e['dnotes']},
             e['cap_en'], e['cap_zh'])


def fig(name, cap_en, cap_zh):
    return (f'<figure class="formula-figure"><img src="../assets/figures/{name}.svg" '
            f'alt="{cap_en}" loading="lazy"><figcaption>' + P(cap_en, cap_zh) + '</figcaption></figure>')


def history(case):
    with open(DATA / f'{case}_history.csv', newline='') as f:
        rows = list(csv.DictReader(f))
    return {k: [float(r[k]) for r in rows] for k in rows[0]}


def peak(case, key='pWall'):
    return max(history(case)[key])


def mpa(x):
    return f'{x / 1e6:.3f}'


P_H = 174622895.4
band = json.loads((DATA / 'BAND_RESULTS.json').read_text(encoding='utf-8'))

ladder = []
previous = None
for case, elems, hdiv in [('B025', 16176, 40), ('B0125', 18468, 80), ('B00625', 26776, 160), ('B003125', 57668, 320)]:
    value = peak(case)
    central = peak(case, 'pWallC')
    change = '—' if previous is None else f'{abs(value - previous) / previous * 100:.2f}%'
    ladder.append([(f'$a/{hdiv}$', f'$a/{hdiv}$'), (f'{elems:,}', f'{elems:,}'), (mpa(value), mpa(value)),
                   (change, change), (f'{value / P_H:.4f}', f'{value / P_H:.4f}'),
                   (mpa(central), mpa(central))])
    previous = value

B = []
B.append(H("1. Problem, inputs and conventions", "1. 问题、输入与约定", "system"))
B.append(P(
    "Find the pressure that a liquid jet of prescribed speed exerts on a rigid wall. Follow three links in order. Theory gives a closed-form reference. A one-dimensional finite-volume code calculates the planar history. An axisymmetric COMSOL model verifies the finite jet.",
    "求给定速度的液体射流作用于刚性壁面的压力。依次沿三个环节推进。理论给出封闭形式的参照。一维有限体积程序计算平面历程。轴对称 COMSOL 模型核验有限射流。"))
B.append(P(
    "Fix the coordinates first. The rigid wall lies at $z=0$. The liquid occupies $z>0$ and moves toward $-z$. The radial coordinate $r$ measures distance from the jet axis. Time $t=0$ is the first contact of the liquid front with the wall. The jet radius $a$ and the incoming speed $U$ are supplied.",
    "先固定坐标。刚性壁面位于 $z=0$。液体占据 $z>0$ 并朝 $-z$ 运动。径向坐标 $r$ 为到射流轴线的距离。时间 $t=0$ 为液体前沿首次接触壁面的时刻。射流半径 $a$ 与入射速度 $U$ 为给定值。"))
B.append(P(
    "State the assumptions. The liquid is the only phase. There is no gas cushion, splash, wall elasticity or cavitation. The wall is flat, rigid and frictionless. The jet side is free, so its pressure is released to the reference pressure $p_j$. Only the first arrival is modelled, up to about one sound-crossing time of the jet radius.",
    "说明假设。液体是唯一的相。不含气垫、飞溅、壁面弹性或空化。壁面平坦、刚性且无摩擦。射流侧面为自由面，其压力释放到参考压力 $p_j$。仅模拟首次到达，时长约为声波穿过射流半径所需时间的一倍。"))
B.append(P(
    "Chapter 3 bounds the speed a source can give a finite jet. This chapter maps a given speed to a wall pressure. Whether a real source reaches that speed is not decided here. Physical validation against an experiment: Not established. Missing: a measured wall pressure for a real jet.",
    "第三章界定了能源能给有限射流的速度上限。本章把给定速度映射为壁面压力。真实能源能否达到该速度，本章不作判断。对照实验的物理验证：尚未确立。缺少：真实射流的壁面压力实测。"))
B.append(T(
    [("Input", "输入"), ("Value", "取值"), ("Role", "作用")],
    [
        [("Jet radius $a$", "射流半径 $a$"), ("1 μm (also 0.5 and 2 μm)", "1 μm（另取 0.5 与 2 μm）"), ("Length scale of the jet and the wall sensor.", "射流与壁面传感区的长度尺度。")],
        [("Incoming speed $U$", "入射速度 $U$"), ("99.02724 m s⁻¹ (also 50 and 150)", "99.02724 m s⁻¹（另取 50 与 150）"), ("Prescribed, uniform and not predicted.", "给定、均匀，并非预测值。")],
        [("Reference density $\\rho_j$", "参考密度 $\\rho_j$"), ("998.1539919 kg m⁻³", "998.1539919 kg m⁻³"), ("Density of the undisturbed jet.", "未扰动射流的密度。")],
        [("Reference pressure $p_j$", "参考压力 $p_j$"), ("101325 Pa", "101325 Pa"), ("Pressure of the jet and of the released side.", "射流及释放侧的压力。")],
        [("Stiffness $\\gamma$, $\\Pi$", "刚度 $\\gamma$、$\\Pi$"), ("4.4 and 600 MPa", "4.4 与 600 MPa"), ("Parameters of the liquid law in Eq. (C5-E01).", "式（C5-E01）液体律的参数。")],
        [("Viscosity $\\mu$", "黏度 $\\mu$"), ("1 mPa s", "1 mPa s"), ("Small; used only in the COMSOL model.", "很小；仅用于 COMSOL 模型。")],
        [("Column length $H$", "液柱长度 $H$"), ("4a", "4a"), ("Distance from the wall to the inflow boundary.", "壁面到入流边界的距离。")],
    ]))
B.append(glossary(5))

B.append(H("2. Theory: the liquid law and the acoustic limit", "2. 理论：液体律与声学极限", "law"))
B.append(P(
    "Step 1 — Adopt a pressure law that depends on density alone. Eq. (C5-E01) is the stiffened-gas form. It is an adopted constitutive law, not a derivation from first principles. " + cite("r17") + " Both solvers below integrate this same law.",
    "步骤 1——采用仅依赖于密度的压力律。式（C5-E01）为刚化气体形式。它是采用的本构律，并非由第一性原理推导。 " + cite("r17") + " 下文两个求解器积分的都是这同一条定律。"))
B.append(eq(1))
B.append(P(
    "Step 2 — Differentiate the law. The factor $(\\rho/\\rho_j)^{\\gamma}$ gives $dp/d\\rho=\\gamma(p_j+\\Pi)\\rho^{\\gamma-1}/\\rho_j^{\\gamma}$. Replace $(p_j+\\Pi)(\\rho/\\rho_j)^{\\gamma}$ by $p+\\Pi$. This gives $c^2=\\gamma(p+\\Pi)/\\rho$. At the reference state, $c_0^2=4.4\\times6.00101325\\times10^{8}/998.1539919$. Hence $c_0=1626.447$ m s⁻¹. The check is dimensional: pressure over density is a squared speed.",
    "步骤 2——对该律求导。因子 $(\\rho/\\rho_j)^{\\gamma}$ 给出 $dp/d\\rho=\\gamma(p_j+\\Pi)\\rho^{\\gamma-1}/\\rho_j^{\\gamma}$。将 $(p_j+\\Pi)(\\rho/\\rho_j)^{\\gamma}$ 替换为 $p+\\Pi$，得到 $c^2=\\gamma(p+\\Pi)/\\rho$。在参考状态下，$c_0^2=4.4\\times6.00101325\\times10^{8}/998.1539919$，故 $c_0=1626.447$ m s⁻¹。量纲检验：压力除以密度是速度的平方。"))
B.append(P(
    "Step 3 — Take the rigid-wall limit of the Chapter 3 contact pressure. Chapter 3 matched liquid and receiver impedances and found the early pressure of Eq. (C3-E24). A rigid wall has $Z_r\\to\\infty$. The common contact velocity then tends to zero. The pressure tends to $Z_0U$ with $Z_0=\\rho_jc_0=1.6234\\times10^{6}$ Pa s m⁻¹. The opposite limit $Z_r\\to0$ gives zero pressure, as a free surface should.",
    "步骤 3——取第三章接触压力的刚性壁面极限。第三章匹配了液体与接收体的阻抗，得到式（C3-E24）的早期压力。刚性壁面有 $Z_r\\to\\infty$。共同接触速度趋于零，压力趋于 $Z_0U$，其中 $Z_0=\\rho_jc_0=1.6234\\times10^{6}$ Pa s m⁻¹。相反的极限 $Z_r\\to0$ 给出零压力，符合自由面。"))
B.append(eq(2))
B.append(P(
    "At $U=99.027$ m s⁻¹ the excess pressure $Z_0U$ is 160.765 MPa. The absolute value $p_A$ is 160.867 MPa. This is a linear estimate. It holds for $U/c_0\\ll1$. The next section removes that restriction.",
    "在 $U=99.027$ m s⁻¹ 时，超压 $Z_0U$ 为 160.765 MPa，绝对值 $p_A$ 为 160.867 MPa。这是线性估计，适用于 $U/c_0\\ll1$。下一节去掉这一限制。"))

B.append(H("3. Theory: the stopping shock and the Hugoniot pressure", "3. 理论：停止激波与 Hugoniot 压力", "shock"))
B.append(P(
    "Step 4 — Describe the stopping shock. At first contact a shock leaves the wall and travels toward $+z$ at lab speed $S$. Liquid behind it is at rest against the wall. Liquid ahead of it moves toward the wall at speed $U$. Its speed relative to the incoming liquid is $U_s=U+S$. Work in the frame of the shock. Liquid enters at speed $U_s$ and leaves at speed $S=U_s-U$.",
    "步骤 4——描述停止激波。首次接触时，激波离开壁面，以实验室速度 $S$ 朝 $+z$ 传播。激波后的液体相对壁面静止，激波前的液体以速度 $U$ 朝壁面运动。它相对入射液体的速度为 $U_s=U+S$。取激波参考系：液体以速度 $U_s$ 流入，以速度 $S=U_s-U$ 流出。"))
B.append(P(
    "Mass balance across the front gives $\\rho_jU_s=\\rho_1S$. Momentum balance gives $p_j+\\rho_jU_s^2=p_1+\\rho_1S^2$. Substitute $\\rho_1S=\\rho_jU_s$ into the second relation. Then $p_1-p_j=\\rho_jU_s(U_s-S)=\\rho_jU_sU$. These are the two relations of Eq. (C5-E03). They are exact for a planar steady shock and need no equation of state. " + cite("r16"),
    "跨波前的质量平衡给出 $\\rho_jU_s=\\rho_1S$。动量平衡给出 $p_j+\\rho_jU_s^2=p_1+\\rho_1S^2$。把 $\\rho_1S=\\rho_jU_s$ 代入第二式，得 $p_1-p_j=\\rho_jU_s(U_s-S)=\\rho_jU_sU$。这就是式（C5-E03）的两个关系。它们对平面定常激波精确成立，且不需要状态方程。 " + cite("r16")))
B.append(eq(3))
B.append(P(
    "Step 5 — Close the jump with energy conservation. The specific internal energy of the stiffened-gas liquid is $e=(p+\\gamma\\Pi)/[(\\gamma-1)\\rho]$. Energy conservation across the shock requires $e_1-e_j=\\tfrac12(p_1+p_j)(1/\\rho_j-1/\\rho_1)$. Write $\\rho_1=\\rho_j/(1-x)$ with $x=U/U_s$. Put $\\Delta=p_1-p_j$ and $B=p_j+\\gamma\\Pi$. Multiply the energy relation by $(\\gamma-1)\\rho_j$. It becomes $\\Delta(1-x)-Bx=\\tfrac12(\\gamma-1)x(2p_j+\\Delta)$.",
    "步骤 5——用能量守恒封闭跳跃。刚化气体液体的比内能为 $e=(p+\\gamma\\Pi)/[(\\gamma-1)\\rho]$。跨激波的能量守恒要求 $e_1-e_j=\\tfrac12(p_1+p_j)(1/\\rho_j-1/\\rho_1)$。令 $\\rho_1=\\rho_j/(1-x)$，其中 $x=U/U_s$。记 $\\Delta=p_1-p_j$、$B=p_j+\\gamma\\Pi$。将能量关系乘以 $(\\gamma-1)\\rho_j$，得 $\\Delta(1-x)-Bx=\\tfrac12(\\gamma-1)x(2p_j+\\Delta)$。"))
B.append(P(
    "Collect the terms in $\\Delta$. Then $\\Delta\\,[1-(\\gamma+1)x/2]=\\gamma(p_j+\\Pi)\\,x$. Momentum gives $\\Delta=\\rho_jU^2/x$. Insert it and use $c_0^2=\\gamma(p_j+\\Pi)/\\rho_j$. The result is $x^2+\\tfrac12(\\gamma+1)M^2x-M^2=0$ with $M=U/c_0$. Its positive root is $x=-k+\\sqrt{k^2+M^2}$ with $k=(\\gamma+1)M^2/4$. The Hugoniot pressure follows as $p_H=p_j+\\rho_jU^2/x$. " + cite("r16"),
    "合并 $\\Delta$ 的项，得 $\\Delta\\,[1-(\\gamma+1)x/2]=\\gamma(p_j+\\Pi)\\,x$。动量关系给出 $\\Delta=\\rho_jU^2/x$。代入并使用 $c_0^2=\\gamma(p_j+\\Pi)/\\rho_j$，得到 $x^2+\\tfrac12(\\gamma+1)M^2x-M^2=0$，其中 $M=U/c_0$。其正根为 $x=-k+\\sqrt{k^2+M^2}$，$k=(\\gamma+1)M^2/4$。Hugoniot 压力为 $p_H=p_j+\\rho_jU^2/x$。 " + cite("r16")))
B.append(eq(4))
B.append(P(
    "Check the limits and the number. For $M\\to0$, $x\\to M$ and $p_H\\to p_j+\\rho_jc_0U$, which is Eq. (C5-E02). At $U=99.02724$ m s⁻¹, $M=0.060886$, $k=0.0050046$ and $x=0.056086$. Hence $U_s=1765.62$ m s⁻¹, $\\rho_1/\\rho_j=1.0594$ and $p_H=174.6229$ MPa. A separate bisection on the energy residual in the C++ code gives the same 174.622895 MPa.",
    "检验极限与数值。当 $M\\to0$ 时，$x\\to M$，$p_H\\to p_j+\\rho_jc_0U$，即式（C5-E02）。在 $U=99.02724$ m s⁻¹ 时，$M=0.060886$，$k=0.0050046$，$x=0.056086$。于是 $U_s=1765.62$ m s⁻¹，$\\rho_1/\\rho_j=1.0594$，$p_H=174.6229$ MPa。C++ 程序对能量残差另作二分求根，得到相同的 174.622895 MPa。"))
B.append(P(
    "Step 6 — Keep the density-only law and drop the energy equation. This is the model that both solvers integrate. Mass and momentum still give $\\rho_1=\\rho_j(U+S)/S$ and $p_1-p_j=\\rho_j(U+S)U$. The law of Eq. (C5-E01) must also give $p_1$ at the density $\\rho_1$. Solve this condition for the root $S_B$.",
    "步骤 6——保留仅含密度的定律并舍去能量方程。这是两个求解器积分的模型。质量与动量仍给出 $\\rho_1=\\rho_j(U+S)/S$ 与 $p_1-p_j=\\rho_j(U+S)U$。式（C5-E01）的定律还须在密度 $\\rho_1$ 处给出 $p_1$。对该条件求根 $S_B$。"))
B.append(eq(5))
B.append(P(
    "At the nominal speed $S_B=1661.86$ m s⁻¹ and $p_B=174.155$ MPa. This lies 0.268% below $p_H$. The gap is the effect of dropping the energy equation. The acoustic estimate of Eq. (C5-E02) lies 7.9% below $p_H$ in absolute pressure. The nonlinear factor is $(p_H-p_j)/(Z_0U)=U_s/c_0=1.0856$.",
    "在名义速度下 $S_B=1661.86$ m s⁻¹，$p_B=174.155$ MPa，比 $p_H$ 低 0.268%。该差值是舍去能量方程的影响。式（C5-E02）的声学估计在绝对压力上比 $p_H$ 低 7.9%。非线性因子为 $(p_H-p_j)/(Z_0U)=U_s/c_0=1.0856$。"))

B.append(H("4. Theory: the finite sensor, edge release and scales", "4. 理论：有限传感区、边缘释放与尺度", "finite"))
B.append(P(
    "Step 7 — Define what is measured. The planar result of Section 3 holds under a column that fills the wall. A real jet has a free side from the first instant. Report the wall pressure as a mean over a fixed disk. Eq. (C5-E06) uses the axisymmetric area weight $2r\\,dr/R^2$. The disk radius $R$ is $a$ for the full sensor and $a/2$ for the centre. This follows the fixed-observer rule of Eq. (C3-E26).",
    "步骤 7——定义被测量。第 3 节的平面结果适用于充满壁面的液柱。真实射流自首次接触起就有自由侧边。将壁面压力报告为固定圆盘上的平均值。式（C5-E06）采用轴对称面积权重 $2r\\,dr/R^2$。圆盘半径 $R$ 对全传感区取 $a$，对中心区取 $a/2$。这遵循式（C3-E26）的固定观测量规则。"))
B.append(eq(6))
B.append(P(
    "Step 8 — Estimate the effect of the free side. Pressure release starts at the edge $r=a$ at first contact. Let it advance inward at $c_0$. After the dimensionless time $\\tau=c_0t/a$ it has reached the annulus $a(1-\\tau)<r\\le a$. The fraction of the disk area in that annulus is $f_{\\mathrm{rel}}=1-(1-\\tau)^2$. If the annulus keeps no excess pressure and the core keeps $p_H$, the mean falls to $p_H(1-\\tau)^2$. This is a scale estimate. It fixes the sign and size of the gap, not its value.",
    "步骤 8——估计自由侧边的影响。压力释放自首次接触起从边缘 $r=a$ 开始，设其以 $c_0$ 向内推进。经无量纲时间 $\\tau=c_0t/a$ 后，它到达环带 $a(1-\\tau)<r\\le a$。该环带占圆盘面积的比例为 $f_{\\mathrm{rel}}=1-(1-\\tau)^2$。若环带不保留超压而核心保持 $p_H$，平均值降为 $p_H(1-\\tau)^2$。这是尺度估计，它确定差值的符号与大小，而不确定其数值。"))
B.append(eq(7))
B.append(P(
    "Step 9 — Count the energy that crosses a plane upstream of the wall. The plane $z=2a$ is hit by the incident liquid before the reflected shock arrives. The reflected shock needs about $2a/(U_s-U)=1.20$ ns to climb back for $a=1$ μm. Use the window $t_w=1$ ns. The kinetic-energy flux $\\dot K=\\tfrac12\\rho_jU^3\\pi a^2$ is 1.5226 mW. Energy through the plane in 1 ns is 1.5226 pJ. This is liquid energy crossing a plane. A rigid wall does no work on the liquid, so it receives none.",
    "步骤 9——计量穿过壁面上游平面的能量。入射液体在反射激波到达之前先经过平面 $z=2a$。对 $a=1$ μm，反射激波返回该平面约需 $2a/(U_s-U)=1.20$ ns。取时间窗 $t_w=1$ ns。动能通量 $\\dot K=\\tfrac12\\rho_jU^3\\pi a^2$ 为 1.5226 mW，1 ns 内穿过平面的能量为 1.5226 pJ。这是穿过平面的液体能量。刚性壁面不对液体做功，因此也不接收功。"))
B.append(eq(8))
B.append(P(
    "Step 10 — State the validity range. The nominal Mach number is $M=0.0609$. The tested range is $0.031\\le M\\le0.092$. The sound-crossing time of the jet radius is $a/c_0=0.615$ ns for $a=1$ μm. The compression behind the shock is only 5.9%. That is why the barotropic law stays within 0.27% of the energy law. No conclusion is claimed outside this range.",
    "步骤 10——说明适用范围。名义马赫数为 $M=0.0609$，检验范围为 $0.031\\le M\\le0.092$。$a=1$ μm 时，声波穿过射流半径的时间 $a/c_0$ 为 0.615 ns。激波后的压缩仅 5.9%，因此正压律与能量律相差不超过 0.27%。超出此范围不作任何结论。"))
B.append(eq(9))

B.append(H("5. Calculation: the one-dimensional reference solver", "5. 计算：一维参考求解器", "calc"))
B.append(P(
    "Step 11 — Write the planar problem as conservation laws. Eq. (C5-E10) holds mass and momentum in conservative form. Conservative form lets a shock form and move at the correct speed. The wall is a mirrored state with $u=0$. The inflow boundary holds the state $(\\rho_j,-U)$. The initial state is the uniform inflow state.",
    "步骤 11——把平面问题写成守恒律。式（C5-E10）以守恒形式表示质量与动量。守恒形式使激波得以形成并以正确速度运动。壁面为 $u=0$ 的镜像状态。入流边界保持状态 $(\\rho_j,-U)$，初态为均匀入流状态。"))
B.append(eq(10))
B.append(P(
    "Step 12 — Discretize with a dissipative flux and a two-stage time step. Cell size is $\\Delta z=H/N=4\\ \\mu\\mathrm m/4000=1$ nm. The face flux averages the two physical fluxes and subtracts $\\alpha/2$ times the state jump. The speed $\\alpha$ is the larger value of $|u|+c$ on the two sides. " + cite("r19") + " " + cite("r18") + " The Heun step is a predictor followed by the average of two spatial operators. It is second order in time and first order in space.",
    "步骤 12——用耗散通量与两步时间推进离散。单元尺寸 $\\Delta z=H/N=4\\ \\mu\\mathrm m/4000=1$ nm。界面通量取两侧物理通量的平均，再减去状态跳跃的 $\\alpha/2$ 倍。速度 $\\alpha$ 取两侧 $|u|+c$ 的较大者。 " + cite("r19") + " " + cite("r18") + " Heun 步先预测，再取两次空间算子的平均。它在时间上为二阶，在空间上为一阶。"))
B.append(eq(11))
B.append(P(
    "Step 13 — Read the planar reference. Run the code for the confined column at $U=99.02724$ m s⁻¹. Average the wall pressure over 0.2 to 2 ns. Compare it with the exact planar pressures. Every entry names its reference value.",
    "步骤 13——读取平面参考解。对受限液柱在 $U=99.02724$ m s⁻¹ 下运行程序，取 0.2 至 2 ns 的壁面压力平均值，并与精确平面压力比较。每一项都注明其参考值。"))
B.append(T(
    [("Quantity", "量"), ("Value (MPa, absolute)", "数值（MPa，绝对压力）"), ("Relative to $p_B$", "相对 $p_B$"), ("Relative to $p_H$", "相对 $p_H$")],
    [
        [("Acoustic estimate $p_A$", "声学估计 $p_A$"), ("160.867", "160.867"), ("−7.63%", "−7.63%"), ("−7.88%", "−7.88%")],
        [("Barotropic shock $p_B$", "正压激波 $p_B$"), ("174.155", "174.155"), ("0 (reference)", "0（参照）"), ("−0.27%", "−0.27%")],
        [("Hugoniot $p_H$", "Hugoniot $p_H$"), ("174.623", "174.623"), ("+0.27%", "+0.27%"), ("0 (reference)", "0（参照）")],
        [("C++ plateau, 4000 cells", "C++ 平台，4000 单元"), ("174.148", "174.148"), ("−0.004%", "−0.004%"), ("−0.27%", "−0.27%")],
    ]))
B.append(P(
    "The C++ plateau agrees with the barotropic shock to 0.004%. This is the check that the discretization reproduces its own exact law. The remaining 0.27% to $p_H$ is the energy equation that the model omits.",
    "C++ 平台与正压激波的偏差为 0.004%。这检验了离散格式再现了它自身的精确定律。与 $p_H$ 相差的 0.27% 来自模型舍去的能量方程。"))

B.append(H("6. Verification: the COMSOL axisymmetric model", "6. 核验：COMSOL 轴对称模型", "model"))
B.append(P(
    "Step 14 — State the finite-element model. It is a compressible laminar-flow study in axisymmetric $(r,z)$ coordinates. Eq. (C5-E12) adds radial motion and a small viscosity to the same liquid. The density follows the pressure through the inverse of Eq. (C5-E01). There is no gas phase.",
    "步骤 14——给出有限元模型。它是轴对称 $(r,z)$ 坐标下的可压缩层流研究。式（C5-E12）在同一种液体上增加径向运动与很小的黏性。密度通过式（C5-E01）的逆关系随压力变化。不含气相。"))
B.append(eq(12))
B.append(P(
    "Step 15 — Set the boundaries and the initial state. The domain is $0\\le r\\le a$ and $0\\le z\\le4a$. The wall is a slip wall. The inflow boundary carries the speed $U$. The side boundary is an outlet at $p_j$, which creates the free side. The liquid starts with a thin onset layer $w=-U\\tanh(z/\\delta)$, $\\delta=0.02a$, so that the wall holds it at rest at $t=0$.",
    "步骤 15——设定边界与初态。计算域为 $0\\le r\\le a$、$0\\le z\\le4a$。壁面为滑移壁面。入流边界给定速度 $U$。侧边界为压力 $p_j$ 的出口，由此形成自由侧边。液体以薄过渡层 $w=-U\\tanh(z/\\delta)$、$\\delta=0.02a$ 开始，使壁面在 $t=0$ 时将其约束为静止。"))
B.append(eq(13))
B.append(P(
    "Step 16 — Fix the observers before the comparison. Eq. (C5-E14) defines the transport observers at the plane $z=2a$ and the area-weighted wall pressure at $z=0$. The same integrals serve every mesh and every case. Mass flux and kinetic-energy flux through the plane check the prescribed inflow. The mass-flux-weighted incident speed over 0 to 1 ns is 99.0272 m s⁻¹, which differs from $U$ by less than $10^{-5}$ percent. The incident energy over the same window is 1.52258 pJ, which differs from Eq. (C5-E08) by less than $10^{-5}$ percent.",
    "步骤 16——比较之前先固定观测量。式（C5-E14）定义了平面 $z=2a$ 处的输运观测量与 $z=0$ 处的面积加权壁面压力。同一组积分适用于每一种网格和每一个工况。穿过平面的质量通量与动能通量用于检验给定的入流。0 至 1 ns 内质量通量加权的入射速度为 99.0272 m s⁻¹，与 $U$ 的偏差小于百分之 $10^{-5}$。同一时间窗内的入射能量为 1.52258 pJ，与式（C5-E08）的偏差小于百分之 $10^{-5}$。"))
B.append(eq(14))

B.append(H("7. Verification: convergence, balances and the cross-check", "7. 核验：收敛、平衡与交叉检验", "verify"))
B.append(P(
    "Step 17 — Judge mesh convergence by the peak of the full-sensor mean. Global refinement beyond about 64,000 elements exceeds the available memory. The peak forms about 0.03 ns after contact and within about 0.05 $a$ of the wall. So refine only a wall band $r\\le a$, $z\\le0.15a$ and keep the rest of the mesh fixed. Eq. (C5-E15) defines the relative error and the successive change. The denominator of the change is the previous, coarser value.",
    "步骤 17——以全传感区平均的峰值判断网格收敛。全局加密超过约 64,000 单元时超出可用内存。峰值在接触后约 0.03 ns、距壁面约 0.05 $a$ 以内形成。因此仅加密壁面带 $r\\le a$、$z\\le0.15a$，其余网格保持不变。式（C5-E15）定义了相对误差与逐次变化量，变化量的分母为前一个较粗网格的值。"))
B.append(eq(15))
B.append(T(
    [("Band size $h$", "加密带尺寸 $h$"), ("Elements", "单元数"), ("Peak full sensor (MPa)", "全传感区峰值（MPa）"), ("Change $\\Delta_k$", "变化量 $\\Delta_k$"), ("Peak / $p_H$", "峰值 / $p_H$"), ("Peak centre $r\\le a/2$ (MPa)", "中心区峰值 $r\\le a/2$（MPa）")],
    ladder))
B.append(P(
    "The successive changes fall from 1.98% to 0.44% and then to 0.02%. The converged full-sensor peak is 162.6 MPa. It is 0.931 of $p_H$, that is 6.9% below the reference. The converged centre-disk peak is 174.37 MPa, 0.14% from $p_H$.",
    "逐次变化量由 1.98% 降至 0.44%，再降至 0.02%。收敛的全传感区峰值为 162.6 MPa，为 $p_H$ 的 0.931 倍，即比参照值低 6.9%。收敛的中心圆盘峰值为 174.37 MPa，与 $p_H$ 相差 0.14%。"))
B.append(P(
    "Step 18 — Check the time step. A run with strict steps and relative tolerance $10^{-3}$ on the 16,136-element mesh gives a full-sensor peak of 168.106 MPa. The automatic-step run gives 169.359 MPa. They differ by 0.74% of the automatic value. A time-step study at the finest band is not done.",
    "步骤 18——检查时间步。在 16,136 单元网格上，采用严格步长、相对容差 $10^{-3}$ 的运行给出全传感区峰值 168.106 MPa，自动步长运行给出 169.359 MPa，二者相差自动步长值的 0.74%。最细加密带上的时间步研究尚未进行。"))
B.append(P(
    "Step 19 — Audit the conservation laws. Close the column on the sides so nothing leaves sideways. Eq. (C5-E16) then compares the change of axial momentum and of mass with their own boundary integrals over 0 to 3 ns. The momentum residual is 0.106% and the mass residual is 0.018%. These residuals test the solver, not the physics.",
    "步骤 19——审计守恒律。将液柱侧面封闭，使侧向无流出。式（C5-E16）在 0 至 3 ns 内把轴向动量与质量的变化同各自的边界积分比较。动量残差为 0.106%，质量残差为 0.018%。这些残差检验的是求解器，而不是物理。"))
B.append(eq(16))
B.append(P(
    "Step 20 — Compare the two solvers on the same problem. Both integrate the confined planar column with the same law, inputs, wall and inflow. Interpolate the C++ history onto the 361 COMSOL sample times between 0.2 and 2.0 ns. Eq. (C5-E17) gives a relative L2 difference of 0.034% and a largest pointwise difference of 0.096%. The plateaus are 174.205 MPa (COMSOL) and 174.148 MPa (C++), a difference of 0.032%. The COMSOL plateau lies 0.24% below $p_H$ and 0.028% above $p_B$.",
    "步骤 20——在同一问题上比较两个求解器。二者以相同的定律、输入、壁面和入流积分受限平面液柱。把 C++ 历程插值到 0.2 至 2.0 ns 间的 361 个 COMSOL 样本时刻。式（C5-E17）给出相对 L2 差 0.034%，最大逐点差 0.096%。平台分别为 174.205 MPa（COMSOL）与 174.148 MPa（C++），相差 0.032%。COMSOL 平台比 $p_H$ 低 0.24%，比 $p_B$ 高 0.028%。"))
B.append(eq(17))
B.append(P(
    "The agreement shows that two codes with different numerics implement the same model. It does not show that the model matches a real jet.",
    "该一致性表明数值方法不同的两个程序实现了同一个模型。它并不表明该模型与真实射流一致。"))

B.append(H("8. Sensitivity and the delivered relations", "8. 敏感性与交付关系", "relations"))
B.append(P(
    "Step 21 — Vary the speed and the radius at the converged band size $h=a/160$. Eq. (C5-E18) defines the peak factor $\\Lambda_i$ of each case and its spread. Five cases cover $U=50$ to 150 m s⁻¹ and $a=0.5$ to 2 μm. These ranges are scenario choices, not confidence intervals.",
    "步骤 21——在收敛的加密带尺寸 $h=a/160$ 下改变速度与半径。式（C5-E18）定义了各工况的峰值因子 $\\Lambda_i$ 及其离散度。五个工况覆盖 $U=50$ 至 150 m s⁻¹、$a=0.5$ 至 2 μm。这些范围是情景选择，并非置信区间。"))
case_labels = {'B00625': ('99.03', '1'), 'BU050': ('50', '1'), 'BU150': ('150', '1'), 'BA05': ('99.03', '0.5'), 'BA2': ('99.03', '2')}
sens = []
for case in ('BU050', 'B00625', 'BU150', 'BA05', 'BA2'):
    r = band[case]
    u, a_um = case_labels[case]
    cells = [u, a_um, mpa(r['p_H']), mpa(r['p_area']), f"{r['ratio_area']:.4f}", f"{r['err_central_pct']:.2f}%"]
    sens.append([(c, c) for c in cells])
B.append(T(
    [("$U$ (m s⁻¹)", "$U$（m s⁻¹）"), ("$a$ (μm)", "$a$（μm）"), ("$p_H$ (MPa)", "$p_H$（MPa）"), ("Peak full sensor (MPa)", "全传感区峰值（MPa）"), ("$\\Lambda$", "$\\Lambda$"), ("Centre error vs $p_H$", "中心区相对 $p_H$ 误差")],
    sens))
B.append(eq(18))
B.append(P(
    "The five peak factors lie between 0.9303 and 0.9314. Their spread is 0.12% of the mean. The scaled histories coincide for $\\tau\\le0.49$, the longest time covered by the band runs.",
    "五个峰值因子介于 0.9303 与 0.9314 之间，离散度为平均值的 0.12%。无量纲历程在 $\\tau\\le0.49$ 内重合，这是加密带运行覆盖的最长时间。"))
B.append(P(
    "Step 22 — Read the gap with the scale estimate. The peak occurs at 0.029 ns, so $\\tau_{\\mathrm{pk}}=0.0472$. Eq. (C5-E07) then gives $f_{\\mathrm{rel}}=0.0921$ and a full-release value of $(1-\\tau_{\\mathrm{pk}})^2=0.908$. The computed factor 0.931 lies between 0.908 and 1. So the annulus keeps about a quarter of its excess pressure. The gap exists because the free side acts from the first instant. It is not a mesh effect, since the band refinement changes the peak by only 0.02% at the finest level.",
    "步骤 22——用尺度估计解读该差值。峰值出现在 0.029 ns，故 $\\tau_{\\mathrm{pk}}=0.0472$。式（C5-E07）给出 $f_{\\mathrm{rel}}=0.0921$，完全释放值为 $(1-\\tau_{\\mathrm{pk}})^2=0.908$。算得的因子 0.931 介于 0.908 与 1 之间，说明环带保留了约四分之一的超压。该差值的出现，是因为自由侧边自首次接触起就在起作用。它不是网格效应，因为加密带在最细一级仅使峰值改变 0.02%。"))
B.append(P(
    "Step 23 — State the delivered relations. Eq. (C5-E19) collects them. The centre disk follows the Hugoniot pressure. The full sensor follows $0.931\\,p_H$. The high-pressure interval lasts about $a/c_0$, which is 0.61 ns for $a=1$ μm. The pressure map multiplies the Chapter 3 ceiling $Z_0U$ by the factor $U_s/c_0=1.0856$.",
    "步骤 23——陈述交付的关系。式（C5-E19）汇总如下。中心圆盘遵循 Hugoniot 压力，全传感区遵循 $0.931\\,p_H$。高压阶段持续约 $a/c_0$，对 $a=1$ μm 为 0.61 ns。压力映射把第三章的上限 $Z_0U$ 乘以因子 $U_s/c_0=1.0856$。"))
B.append(eq(19))
B.append(P(
    "State the limits. The result holds for a liquid-only barotropic column, a rigid flat wall and the first arrival. The tested ranges are $0.031\\le M\\le0.092$ and $0.5\\le a\\le2$ μm. After $\\tau\\approx1$ the computed wall pressure turns negative in absolute value, which is not physical here because cavitation is not modelled. A gas cushion, an elastic wall and the bubble-to-jet physics upstream are not covered.",
    "说明局限。该结果适用于纯液体正压液柱、刚性平壁与首次到达。检验范围为 $0.031\\le M\\le0.092$ 与 $0.5\\le a\\le2$ μm。$\\tau\\approx1$ 之后，算得的壁面压力绝对值变为负，这在此不具物理意义，因为未建立空化模型。气垫、弹性壁面以及上游的气泡到射流物理均未涵盖。"))

B.append(H("9. Oral questions", "9. 口头问题", "defense"))
answer1 = eq(20)
answer1 += P(
    "Start from the energy bound. Chapter 3 limits the speed by the energy available to the finite jet mass. This chapter takes the speed as given and maps it to pressure. At 99.027 m s⁻¹ the linear ceiling is 160.765 MPa excess. The nonlinear factor 1.0856 gives 174.52 MPa excess, which is the Hugoniot level. Over the full sensor the peak is 0.931 of the absolute Hugoniot pressure, 162.6 MPa. These numbers hold for the prescribed speed. They say nothing on whether a source delivers that speed.",
    "从能量上界出发。第三章用有限射流质量可得的能量来限制速度。本章把速度当作给定值并映射为压力。在 99.027 m s⁻¹ 时，线性上限为 160.765 MPa 超压。非线性因子 1.0856 给出 174.52 MPa 超压，即 Hugoniot 水平。在整个传感区上，峰值为绝对 Hugoniot 压力的 0.931 倍，即 162.6 MPa。这些数值对应于给定速度，并不说明能源能否提供该速度。")
answer1 += P(
    "A bound and a map are different claims. The bound says a speed cannot be exceeded. The map says what pressure follows from a speed under stated assumptions. Neither is a prediction of the pressure a given laser pulse produces. That needs the upstream chain of Chapters 1 to 3 and a measurement.",
    "上界与映射是不同的结论。上界说明速度不可超过某值。映射说明在所述假设下某一速度对应何种压力。二者都不是对给定激光脉冲所产生压力的预测。那需要第一至第三章的上游链条以及实测。")
B.append(defense("C5-Q1",
    "Which wall pressure does this chain establish for a prescribed 99.03 m/s jet, and what stays conditional?",
    "该链条对给定的 99.03 m/s 射流确立了何种壁面压力？哪些仍是有条件的？", answer1,
    [("Separates the Chapter 3 speed bound from the speed-to-pressure map and states that the speed is prescribed.", "区分第三章的速度上界与速度到压力的映射，并说明速度为给定值。"),
     ("Quotes the linear ceiling, the Hugoniot level and the full-sensor factor with their reference values.", "引用线性上限、Hugoniot 水平和全传感区因子，并注明各自的参照值。"),
     ("Names the conditions: liquid only, rigid flat wall, barotropic law, first arrival and the tested ranges.", "指出条件：纯液体、刚性平壁、正压律、首次到达以及检验范围。")]))

answer2 = eq(21)
answer2 += P(
    "The free side of the jet acts from first contact. A release front from the edge reaches the radius $a(1-\\tau)$ at dimensionless time $\\tau$. At the peak time 0.029 ns, $\\tau=0.0472$ and the released annulus holds 9.2% of the disk area. Full release of that annulus gives $0.908\\,p_H$. The computed factor 0.931 requires the annulus to keep about a quarter of its excess pressure. The sign and size agree with the scale estimate.",
    "射流的自由侧边自首次接触起就在起作用。边缘的释放前沿在无量纲时间 $\\tau$ 到达半径 $a(1-\\tau)$。在峰值时刻 0.029 ns，$\\tau=0.0472$，已释放环带占圆盘面积的 9.2%。该环带完全释放时给出 $0.908\\,p_H$。算得的因子 0.931 要求环带保留约四分之一的超压。符号与大小与尺度估计一致。")
answer2 += P(
    "Evidence against a mesh artifact: the band refinement changes the peak by 1.98%, 0.44% and 0.02%. The factor is the same within 0.12% for five speeds and radii. The centre disk, which the release has not reached, stays within 0.43% of $p_H$. A mesh artifact would not be confined to the full-area average and would not collapse with $\\tau$.",
    "反对网格伪影的证据：加密带使峰值依次改变 1.98%、0.44% 和 0.02%；五组速度与半径下该因子的偏差在 0.12% 以内；释放尚未到达的中心圆盘保持在 $p_H$ 的 0.43% 以内。网格伪影不会只出现在全面积平均上，也不会随 $\\tau$ 坍缩。")
B.append(defense("C5-Q2",
    "Is the 6.9% gap between the full-sensor peak and the Hugoniot pressure a mesh artifact or edge release? Which evidence decides?",
    "全传感区峰值与 Hugoniot 压力之间 6.9% 的差值是网格伪影还是边缘释放？哪些证据能决定？", answer2,
    [("Explains the free side acting from first contact and the released annulus with the area fraction of Eq. (C5-E07).", "解释自由侧边自首次接触起的作用，并用式（C5-E07）的面积分数说明已释放环带。"),
     ("Uses the band-refinement sequence, the centre disk and the five-case collapse as separate pieces of evidence.", "把加密带序列、中心圆盘和五工况坍缩作为各自独立的证据。"),
     ("States that the scale estimate fixes sign and size, not the digits, and that 0.931 comes from the simulation.", "说明尺度估计只确定符号与大小而非数字，0.931 来自模拟。")]))

answer3 = eq(22)
answer3 += P(
    "The relative L2 difference of 0.034% between the C++ and COMSOL histories shows that two implementations of one model agree. Both use the same stiffened-gas law, inputs, wall and inflow. A shared modelling error would appear in both. So the agreement cannot validate the law, the neglect of gas or the rigid wall. It supports a statement about numerics only.",
    "C++ 与 COMSOL 历程之间 0.034% 的相对 L2 差表明同一模型的两个实现是一致的。二者使用相同的刚化气体律、输入、壁面和入流。共同的建模误差会同时出现在两者之中。因此这一致性不能验证该定律、对气相的忽略或刚性壁面，它只支持关于数值的陈述。")
answer3 += P(
    "The 162.6 MPa result is supported as a numerical result for a liquid-only column at $0.031\\le M\\le0.092$ and $0.5\\le a\\le2$ μm during the first arrival. It is not supported as a prediction of a measured wall pressure, as a value after $\\tau\\approx1$, or as a value with a gas cushion or an elastic wall. Physical validation: Not established. Missing: a measured wall pressure for a real jet.",
    "162.6 MPa 作为数值结果成立，条件是纯液体液柱、$0.031\\le M\\le0.092$、$0.5\\le a\\le2$ μm 且处于首次到达阶段。它不支持作为实测壁面压力的预测，不支持 $\\tau\\approx1$ 之后的数值，也不支持含气垫或弹性壁面的情形。物理验证：尚未确立。缺少：真实射流的壁面压力实测。")
B.append(defense("C5-Q3",
    "What does the 0.034% solver agreement establish, and which uses of the 162.6 MPa result stay unsupported?",
    "0.034% 的求解器一致性确立了什么？162.6 MPa 的哪些用途仍无依据？", answer3,
    [("Distinguishes verification of an implementation from validation of the model against experiment.", "区分对实现的核验与对模型的实验验证。"),
     ("Lists the supported range: liquid only, rigid flat wall, tested Mach and radius ranges, first arrival.", "列出支持的范围：纯液体、刚性平壁、检验过的马赫数与半径范围、首次到达。"),
     ("Names unsupported uses: a measured pressure, times after $\\tau\\approx1$, a gas cushion and an elastic wall.", "指出无依据的用途：实测压力、$\\tau\\approx1$ 之后的时间、气垫与弹性壁面。")]))

body = "".join(B)

CHAPTER = {
    r"number": 5,
    r"kind": r"chapter",
    r"slug": r"05-jet-on-rigid-wall",
    r"title_en": r"Jet-on-rigid-wall calculation",
    r"title_zh": r"刚性壁面射流计算",
    r"summary_en": "Map a prescribed jet speed to a wall pressure. Chain closed-form theory, a finite-volume calculation and a COMSOL verification.",
    r"summary_zh": "把给定射流速度映射为壁面压力。依次给出封闭形式理论、有限体积计算与 COMSOL 核验。",
    r"body": body,
    r"question_ids": [r"C5-Q1", r"C5-Q2", r"C5-Q3"],
    r"objectives": [
        (r"Derive the acoustic and Hugoniot wall pressures of a liquid stopped by a rigid wall.", r"推导被刚性壁面截停的液体的声学壁面压力与 Hugoniot 壁面压力。"),
        (r"Calculate the planar history with a finite-volume code and read the area-weighted finite-jet observer.", r"用有限体积程序计算平面历程，并读取面积加权的有限射流观测量。"),
        (r"Verify the result with an axisymmetric model, convergence, balances and a cross-solver comparison, and state its limits.", r"用轴对称模型、收敛性、平衡与跨求解器比较核验结果，并说明其局限。"),
    ],
    r"prerequisite_en": "Prerequisites: Chapter 3’s finite jet, acoustic impact matching and fixed observer.",
    r"prerequisite_zh": "前提：第三章的有限射流、声学撞击匹配与固定观测量。",
}
