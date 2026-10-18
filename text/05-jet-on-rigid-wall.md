# Chapter 5: Jet-on-rigid-wall calculation

# 第 5 章：刚性壁面射流计算

## 1. Problem, inputs and conventions

## 1. 问题、输入与约定

Find the pressure that a liquid jet of prescribed speed exerts on a rigid wall. Follow three links in order. Theory gives a closed-form reference. A one-dimensional finite-volume code calculates the planar history. An axisymmetric COMSOL model verifies the finite jet.

求给定速度的液体射流作用于刚性壁面的压力。依次沿三个环节推进。理论给出封闭形式的参照。一维有限体积程序计算平面历程。轴对称 COMSOL 模型核验有限射流。

Fix the coordinates first. The rigid wall lies at $z=0$. The liquid occupies $z>0$ and moves toward $-z$. The radial coordinate $r$ measures distance from the jet axis. Time $t=0$ is the first contact of the liquid front with the wall. The jet radius $a$ and the incoming speed $U$ are supplied.

先固定坐标。刚性壁面位于 $z=0$。液体占据 $z>0$ 并朝 $-z$ 运动。径向坐标 $r$ 为到射流轴线的距离。时间 $t=0$ 为液体前沿首次接触壁面的时刻。射流半径 $a$ 与入射速度 $U$ 为给定值。

State the assumptions. The liquid is the only phase. There is no gas cushion, splash, wall elasticity or cavitation. The wall is flat, rigid and frictionless. The jet side is free, so its pressure is released to the reference pressure $p_j$. Only the first arrival is modelled, up to about one sound-crossing time of the jet radius.

说明假设。液体是唯一的相。不含气垫、飞溅、壁面弹性或空化。壁面平坦、刚性且无摩擦。射流侧面为自由面，其压力释放到参考压力 $p_j$。仅模拟首次到达，时长约为声波穿过射流半径所需时间的一倍。

Chapter 3 bounds the speed a source can give a finite jet. This chapter maps a given speed to a wall pressure. Whether a real source reaches that speed is not decided here. Physical validation against an experiment: Not established. Missing: a measured wall pressure for a real jet.

第三章界定了能源能给有限射流的速度上限。本章把给定速度映射为壁面压力。真实能源能否达到该速度，本章不作判断。对照实验的物理验证：尚未确立。缺少：真实射流的壁面压力实测。

| Input<br>输入 | Value<br>取值 | Role<br>作用 |
| --- | --- | --- |
| Jet radius $a$<br>射流半径 $a$ | 1 μm (also 0.5 and 2 μm)<br>1 μm（另取 0.5 与 2 μm） | Length scale of the jet and the wall sensor.<br>射流与壁面传感区的长度尺度。 |
| Incoming speed $U$<br>入射速度 $U$ | 99.02724 m s⁻¹ (also 50 and 150)<br>99.02724 m s⁻¹（另取 50 与 150） | Prescribed, uniform and not predicted.<br>给定、均匀，并非预测值。 |
| Reference density $\rho_j$<br>参考密度 $\rho_j$ | 998.1539919 kg m⁻³<br>998.1539919 kg m⁻³ | Density of the undisturbed jet.<br>未扰动射流的密度。 |
| Reference pressure $p_j$<br>参考压力 $p_j$ | 101325 Pa<br>101325 Pa | Pressure of the jet and of the released side.<br>射流及释放侧的压力。 |
| Stiffness $\gamma$, $\Pi$<br>刚度 $\gamma$、$\Pi$ | 4.4 and 600 MPa<br>4.4 与 600 MPa | Parameters of the liquid law in Eq. (C5-E01).<br>式（C5-E01）液体律的参数。 |
| Viscosity $\mu$<br>黏度 $\mu$ | 1 mPa s<br>1 mPa s | Small; used only in the COMSOL model.<br>很小；仅用于 COMSOL 模型。 |
| Column length $H$<br>液柱长度 $H$ | 4a<br>4a | Distance from the wall to the inflow boundary.<br>壁面到入流边界的距离。 || Symbol<br>符号 | Physical meaning<br>物理意义 | SI units<br>SI 单位 | Role and convention<br>作用与约定 |
| --- | --- | --- | --- |
| $a$ | Jet radius<br>射流半径 | m | Radius of the liquid column; also the length scale of the wall sensor.<br>液柱半径；也是壁面传感区的长度尺度。 |
| $U$ | Prescribed impact speed<br>给定撞击速度 | m s⁻¹ | Uniform speed of the incoming liquid toward the wall; supplied, not predicted.<br>入射液体朝壁面的均匀速度；为给定值而非预测值。 |
| $z$ | Axial coordinate from the wall<br>距壁面的轴向坐标 | m | z = 0 is the rigid wall; the liquid lies at z > 0 and moves toward −z.<br>z = 0 为刚性壁面；液体位于 z > 0 并朝 −z 运动。 |
| $r$ | Radial coordinate<br>径向坐标 | m | Distance from the jet axis in the axisymmetric model.<br>轴对称模型中到射流轴线的距离。 |
| $t$ | Time from first contact<br>自首次接触起的时间 | s | Zero when the liquid front first touches the wall.<br>液体前沿首次接触壁面时为零。 |
| $\rho$ | Liquid density<br>液体密度 | kg m⁻³ | Field variable; equals $ρ_{j}$ at the reference pressure.<br>场变量；在参考压力下等于 $ρ_{j}$。 |
| $\rho_j$ | Reference liquid density<br>参考液体密度 | kg m⁻³ | 998.1539919 kg m⁻³ at $p_{j}$; the incoming jet state.<br>在 $p_{j}$ 下为 998.1539919 kg m⁻³；入射射流状态。 |
| $p$ | Absolute pressure<br>绝对压力 | Pa | Pressure field; excess pressure is p − $p_{j}$.<br>压力场；超压为 p − $p_{j}$。 |
| $p_j$ | Reference pressure<br>参考压力 | Pa | 101325 Pa; pressure of the undisturbed jet and of the released side.<br>101325 Pa；未扰动射流及侧向释放边界的压力。 |
| $\gamma$ | Stiffness exponent<br>刚度指数 | 1 | 4.4 in the adopted stiffened-gas law.<br>所采用刚化气体律中的 4.4。 |
| $\Pi$ | Stiffness pressure<br>刚度压力 | Pa | 6.00 × 10⁸ Pa; sets the liquid compressibility together with γ.<br>6.00 × 10⁸ Pa；与 γ 共同决定液体可压缩性。 |
| $c$ | Local sound speed<br>局部声速 | m s⁻¹ | Equals dp/dρ under the square root; varies with pressure.<br>根号内 dp/dρ 的结果；随压力变化。 |
| $c_0$ | Reference sound speed<br>参考声速 | m s⁻¹ | 1626.447 m s⁻¹ at the reference state.<br>参考状态下为 1626.447 m s⁻¹。 |
| $Z_0$ | Reference acoustic impedance<br>参考声阻抗 | Pa s m⁻¹ | Product $ρ_{j}$ $c_{0}$; the Chapter 3 liquid impedance at the reference state.<br>乘积 $ρ_{j}$ $c_{0}$；第三章在参考状态下的液体阻抗。 |
| $M$ | Impact Mach number<br>撞击马赫数 | 1 | U/$c_{0}$; measures how far the jump is from the linear limit.<br>U/$c_{0}$；衡量跳跃偏离线性极限的程度。 |
| $U_s$ | Shock speed relative to the incoming liquid<br>相对入射液体的激波速度 | m s⁻¹ | Speed at which the compressed region grows into the arriving liquid.<br>受压区域向入射液体推进的速度。 |
| $x$ | Velocity ratio across the shock<br>激波两侧速度比 | 1 | U/$U_{s}$; equals the fractional density jump 1 − $ρ_{j}$/$ρ_{1}$.<br>U/$U_{s}$；等于密度相对跃升 1 − $ρ_{j}$/$ρ_{1}$。 |
| $p_H$ | Hugoniot wall pressure<br>Hugoniot 壁面压力 | Pa | Planar, fully confined shock pressure from the energy-conserving jump; the reference.<br>来自能量守恒跳跃的平面完全受限激波压力；作为参照。 |
| $p_B$ | Barotropic shock pressure<br>正压激波压力 | Pa | Planar shock pressure under the barotropic law used by both solvers.<br>两个求解器所用正压律下的平面激波压力。 |
| $\bar p_R$ | Area-weighted wall pressure<br>面积加权壁面压力 | Pa | Mean of p over the wall disk r ≤ R; R = a is the full sensor, R = a/2 the centre.<br>p 在壁面圆盘 r ≤ R 上的平均；R = a 为全传感区，R = a/2 为中心区。 |
| $\tau$ | Dimensionless time<br>无量纲时间 | 1 | $c_{0}$ t / a; one unit is the time for sound to cross the jet radius.<br>$c_{0}$ t / a；一个单位为声波穿过射流半径的时间。 |
| $\Lambda$ | Finite-area peak factor<br>有限面积峰值因子 | 1 | Peak of the full-sensor mean divided by $p_{H}$.<br>全传感区平均峰值与 $p_{H}$ 之比。 |
| $\dot K$ | Incident kinetic-energy flux<br>入射动能通量 | W | ½ $ρ_{j}$ U³ π a²; liquid energy crossing a plane, not work on the wall.<br>½ $ρ_{j}$ U³ π a²；穿过平面的液体能量，并非对壁面做功。 |
| $\dot m$ | Incident mass flow rate<br>入射质量流率 | kg s⁻¹ | $ρ_{j}$ U π a²; mass crossing the observation plane per unit time.<br>$ρ_{j}$ U π a²；单位时间穿过观察平面的质量。 |
| $\varepsilon$ | Relative error<br>相对误差 | 1 | Absolute difference divided by the stated reference value.<br>绝对差除以所注明的参考值。 |

## 2. Theory: the liquid law and the acoustic limit

## 2. 理论：液体律与声学极限

Step 1 — Adopt a pressure law that depends on density alone. Eq. (C5-E01) is the stiffened-gas form. It is an adopted constitutive law, not a derivation from first principles. [[R17]](../reference/sources.html#r17) Both solvers below integrate this same law.

步骤 1——采用仅依赖于密度的压力律。式（C5-E01）为刚化气体形式。它是采用的本构律，并非由第一性原理推导。 [[R17]](../reference/sources.html#r17) 下文两个求解器积分的都是这同一条定律。

**Symbols before Eq. (C5-E01).**

**式（C5-E01）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p$ — Absolute pressure (Pa)<br>$p$ — 绝对压力（Pa） | $\rho$ — Liquid density (kg m⁻³)<br>$\rho$ — 液体密度（kg m⁻³） |
| $\rho_j$ — Reference density 998.1539919 at the reference pressure (kg m⁻³)<br>$\rho_j$ — 参考压力下的参考密度 998.1539919（kg m⁻³） | $p_j$ — Reference pressure 101325 (Pa)<br>$p_j$ — 参考压力 101325（Pa） |
| $\Pi$ — Stiffness pressure 6.00 × 10⁸ (Pa)<br>$\Pi$ — 刚度压力 6.00 × 10⁸（Pa） | $\gamma$ — Stiffness exponent 4.4 (dimensionless)<br>$\gamma$ — 刚度指数 4.4（无量纲） |
| $c$ — Local sound speed (m s⁻¹)<br>$c$ — 局部声速（m s⁻¹） | $c_0$ — Reference sound speed (m s⁻¹)<br>$c_0$ — 参考声速（m s⁻¹） |
| $d/d\rho$ — Derivative operator with respect to density (m³ kg⁻¹)<br>$d/d\rho$ — 对密度的导数算符（m³ kg⁻¹） |  |

**Conventions and conditions.** Pressure depends on density alone (barotropic); Valid while temperature change is negligible; The law fixes $c_{0}$ = 1626.447 m s⁻¹.

**约定与条件。** 压力仅依赖于密度（正压）；温度变化可忽略时成立；该律给出 $c_{0}$ = 1626.447 m s⁻¹。

(C5-E01) · Adopted barotropic stiffened-gas law and exact sound speed / 采用的正压刚化气体律与精确声速


$$
\begin{aligned}p(\rho)&=(p_j+\Pi)\left(\frac{\rho}{\rho_j}\right)^{\gamma}-\Pi,\\ c^{2}&=\frac{dp}{d\rho}=\frac{\gamma\,[\,p(\rho)+\Pi\,]}{\rho},\qquad c_0=\sqrt{\frac{\gamma\,(p_j+\Pi)}{\rho_j}}.\end{aligned}
$$


![One density-only law fixes pressure and sound speed for every later step.](../assets/figures/c5-e01.svg)

One density-only law fixes pressure and sound speed for every later step.

一条仅含密度的状态律为后续每一步确定压力与声速。

Step 2 — Differentiate the law. The factor $(\rho/\rho_j)^{\gamma}$ gives $dp/d\rho=\gamma(p_j+\Pi)\rho^{\gamma-1}/\rho_j^{\gamma}$. Replace $(p_j+\Pi)(\rho/\rho_j)^{\gamma}$ by $p+\Pi$. This gives $c^2=\gamma(p+\Pi)/\rho$. At the reference state, $c_0^2=4.4\times6.00101325\times10^{8}/998.1539919$. Hence $c_0=1626.447$ m s⁻¹. The check is dimensional: pressure over density is a squared speed.

步骤 2——对该律求导。因子 $(\rho/\rho_j)^{\gamma}$ 给出 $dp/d\rho=\gamma(p_j+\Pi)\rho^{\gamma-1}/\rho_j^{\gamma}$。将 $(p_j+\Pi)(\rho/\rho_j)^{\gamma}$ 替换为 $p+\Pi$，得到 $c^2=\gamma(p+\Pi)/\rho$。在参考状态下，$c_0^2=4.4\times6.00101325\times10^{8}/998.1539919$，故 $c_0=1626.447$ m s⁻¹。量纲检验：压力除以密度是速度的平方。

Step 3 — Take the rigid-wall limit of the Chapter 3 contact pressure. Chapter 3 matched liquid and receiver impedances and found the early pressure of Eq. (C3-E24). A rigid wall has $Z_r\to\infty$. The common contact velocity then tends to zero. The pressure tends to $Z_0U$ with $Z_0=\rho_jc_0=1.6234\times10^{6}$ Pa s m⁻¹. The opposite limit $Z_r\to0$ gives zero pressure, as a free surface should.

步骤 3——取第三章接触压力的刚性壁面极限。第三章匹配了液体与接收体的阻抗，得到式（C3-E24）的早期压力。刚性壁面有 $Z_r\to\infty$。共同接触速度趋于零，压力趋于 $Z_0U$，其中 $Z_0=\rho_jc_0=1.6234\times10^{6}$ Pa s m⁻¹。相反的极限 $Z_r\to0$ 给出零压力，符合自由面。

**Symbols before Eq. (C5-E02).**

**式（C5-E02）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{early}}$ — Early compressive contact pressure from Chapter 3 matching (Pa)<br>$p_{\mathrm{early}}$ — 第三章匹配得到的早期压缩接触压力（Pa） | $Z_l$ — Liquid longitudinal impedance (Pa s m⁻¹)<br>$Z_l$ — 液体纵向阻抗（Pa s m⁻¹） |
| $Z_r$ — Receiver longitudinal impedance (Pa s m⁻¹)<br>$Z_r$ — 接收体纵向阻抗（Pa s m⁻¹） | $U$ — Prescribed incoming speed 99.027 (m s⁻¹)<br>$U$ — 给定入射速度 99.027（m s⁻¹） |
| $Z_0$ — Reference acoustic impedance $ρ_{j}$ $c_{0}$ (Pa s m⁻¹)<br>$Z_0$ — 参考声阻抗 $ρ_{j}$ $c_{0}$（Pa s m⁻¹） | $p_A$ — Absolute acoustic wall pressure (Pa)<br>$p_A$ — 绝对声学壁面压力（Pa） |
| $p_j$ — Reference pressure (Pa)<br>$p_j$ — 参考压力（Pa） | $\rho_j$ — Reference density (kg m⁻³)<br>$\rho_j$ — 参考密度（kg m⁻³） |
| $c_0$ — Reference sound speed (m s⁻¹)<br>$c_0$ — 参考声速（m s⁻¹） |  |

**Conventions and conditions.** $Z_{l}$ = $Z_{0}$ at linear order; Rigid wall: $Z_{r}$ → ∞ gives zero contact velocity; $Z_{0}$ U = 160.765 MPa at U = 99.027 m s⁻¹.

**约定与条件。** 线性阶下 $Z_{l}$ = $Z_{0}$；刚性壁面：$Z_{r}$ → ∞ 使接触速度为零；U = 99.027 m s⁻¹ 时 $Z_{0}$ U = 160.765 MPa。

(C5-E02) · Rigid-wall limit of the Chapter 3 acoustic matching / 第三章声学匹配的刚性壁面极限


$$
\begin{aligned}p_{\mathrm{early}}&=\frac{Z_lZ_r}{Z_l+Z_r}\,U\ \xrightarrow{\ Z_r\to\infty\ }\ Z_0U,\qquad Z_0=\rho_jc_0,\\ p_A&=p_j+Z_0U.\end{aligned}
$$


![Letting the receiver impedance grow without bound turns the Chapter 3 contact pressure into ρc times speed.](../assets/figures/c5-e02.svg)

Letting the receiver impedance grow without bound turns the Chapter 3 contact pressure into ρc times speed.

令接收体阻抗趋于无穷，第三章的接触压力变为 ρc 乘速度。

At $U=99.027$ m s⁻¹ the excess pressure $Z_0U$ is 160.765 MPa. The absolute value $p_A$ is 160.867 MPa. This is a linear estimate. It holds for $U/c_0\ll1$. The next section removes that restriction.

在 $U=99.027$ m s⁻¹ 时，超压 $Z_0U$ 为 160.765 MPa，绝对值 $p_A$ 为 160.867 MPa。这是线性估计，适用于 $U/c_0\ll1$。下一节去掉这一限制。

## 3. Theory: the stopping shock and the Hugoniot pressure

## 3. 理论：停止激波与 Hugoniot 压力

Step 4 — Describe the stopping shock. At first contact a shock leaves the wall and travels toward $+z$ at lab speed $S$. Liquid behind it is at rest against the wall. Liquid ahead of it moves toward the wall at speed $U$. Its speed relative to the incoming liquid is $U_s=U+S$. Work in the frame of the shock. Liquid enters at speed $U_s$ and leaves at speed $S=U_s-U$.

步骤 4——描述停止激波。首次接触时，激波离开壁面，以实验室速度 $S$ 朝 $+z$ 传播。激波后的液体相对壁面静止，激波前的液体以速度 $U$ 朝壁面运动。它相对入射液体的速度为 $U_s=U+S$。取激波参考系：液体以速度 $U_s$ 流入，以速度 $S=U_s-U$ 流出。

Mass balance across the front gives $\rho_jU_s=\rho_1S$. Momentum balance gives $p_j+\rho_jU_s^2=p_1+\rho_1S^2$. Substitute $\rho_1S=\rho_jU_s$ into the second relation. Then $p_1-p_j=\rho_jU_s(U_s-S)=\rho_jU_sU$. These are the two relations of Eq. (C5-E03). They are exact for a planar steady shock and need no equation of state. [[R16]](../reference/sources.html#r16)

跨波前的质量平衡给出 $\rho_jU_s=\rho_1S$。动量平衡给出 $p_j+\rho_jU_s^2=p_1+\rho_1S^2$。把 $\rho_1S=\rho_jU_s$ 代入第二式，得 $p_1-p_j=\rho_jU_s(U_s-S)=\rho_jU_sU$。这就是式（C5-E03）的两个关系。它们对平面定常激波精确成立，且不需要状态方程。 [[R16]](../reference/sources.html#r16)

**Symbols before Eq. (C5-E03).**

**式（C5-E03）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\rho_1$ — Density behind the shock (kg m⁻³)<br>$\rho_1$ — 激波后密度（kg m⁻³） | $\rho_j$ — Density of the incoming liquid (kg m⁻³)<br>$\rho_j$ — 入射液体密度（kg m⁻³） |
| $U_s$ — Shock speed relative to the incoming liquid (m s⁻¹)<br>$U_s$ — 相对入射液体的激波速度（m s⁻¹） | $U$ — Incoming liquid speed toward the wall (m s⁻¹)<br>$U$ — 入射液体朝壁面的速度（m s⁻¹） |
| $p_1$ — Absolute pressure behind the shock (Pa)<br>$p_1$ — 激波后绝对压力（Pa） | $p_j$ — Absolute pressure ahead of the shock (Pa)<br>$p_j$ — 激波前绝对压力（Pa） |
| $x$ — Velocity ratio U/$U_{s}$ (dimensionless)<br>$x$ — 速度比 U/$U_{s}$（无量纲） |  |

**Conventions and conditions.** Liquid behind the shock is at rest against the wall; Mass and momentum jump conditions need no equation of state; In the frame of the shock the incoming speed is $U_{s}$ and the outgoing speed is $U_{s}$ − U.

**约定与条件。** 激波后的液体相对壁面静止；质量与动量跳跃条件不需要状态方程；在激波参考系中，入流速度为 $U_{s}$，出流速度为 $U_{s}$ − U。

(C5-E03) · Mass and momentum jump across the stopping shock / 停止激波两侧的质量与动量跳跃


$$
\begin{aligned}\rho_1\,(U_s-U)&=\rho_j\,U_s,\\ p_1-p_j&=\rho_j\,U_s\,U,\\ x&\equiv\frac{U}{U_s}=1-\frac{\rho_j}{\rho_1}.\end{aligned}
$$


![A shock that stops the liquid obeys mass and momentum balance across its thin front.](../assets/figures/c5-e03.svg)

A shock that stops the liquid obeys mass and momentum balance across its thin front.

使液体停止的激波，其薄波前两侧服从质量与动量平衡。

Step 5 — Close the jump with energy conservation. The specific internal energy of the stiffened-gas liquid is $e=(p+\gamma\Pi)/[(\gamma-1)\rho]$. Energy conservation across the shock requires $e_1-e_j=\tfrac12(p_1+p_j)(1/\rho_j-1/\rho_1)$. Write $\rho_1=\rho_j/(1-x)$ with $x=U/U_s$. Put $\Delta=p_1-p_j$ and $B=p_j+\gamma\Pi$. Multiply the energy relation by $(\gamma-1)\rho_j$. It becomes $\Delta(1-x)-Bx=\tfrac12(\gamma-1)x(2p_j+\Delta)$.

步骤 5——用能量守恒封闭跳跃。刚化气体液体的比内能为 $e=(p+\gamma\Pi)/[(\gamma-1)\rho]$。跨激波的能量守恒要求 $e_1-e_j=\tfrac12(p_1+p_j)(1/\rho_j-1/\rho_1)$。令 $\rho_1=\rho_j/(1-x)$，其中 $x=U/U_s$。记 $\Delta=p_1-p_j$、$B=p_j+\gamma\Pi$。将能量关系乘以 $(\gamma-1)\rho_j$，得 $\Delta(1-x)-Bx=\tfrac12(\gamma-1)x(2p_j+\Delta)$。

Collect the terms in $\Delta$. Then $\Delta\,[1-(\gamma+1)x/2]=\gamma(p_j+\Pi)\,x$. Momentum gives $\Delta=\rho_jU^2/x$. Insert it and use $c_0^2=\gamma(p_j+\Pi)/\rho_j$. The result is $x^2+\tfrac12(\gamma+1)M^2x-M^2=0$ with $M=U/c_0$. Its positive root is $x=-k+\sqrt{k^2+M^2}$ with $k=(\gamma+1)M^2/4$. The Hugoniot pressure follows as $p_H=p_j+\rho_jU^2/x$. [[R16]](../reference/sources.html#r16)

合并 $\Delta$ 的项，得 $\Delta\,[1-(\gamma+1)x/2]=\gamma(p_j+\Pi)\,x$。动量关系给出 $\Delta=\rho_jU^2/x$。代入并使用 $c_0^2=\gamma(p_j+\Pi)/\rho_j$，得到 $x^2+\tfrac12(\gamma+1)M^2x-M^2=0$，其中 $M=U/c_0$。其正根为 $x=-k+\sqrt{k^2+M^2}$，$k=(\gamma+1)M^2/4$。Hugoniot 压力为 $p_H=p_j+\rho_jU^2/x$。 [[R16]](../reference/sources.html#r16)

**Symbols before Eq. (C5-E04).**

**式（C5-E04）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $e$ — Specific internal energy of the stiffened-gas liquid (J kg⁻¹)<br>$e$ — 刚化气体液体的比内能（J kg⁻¹） | $e_1$ — Specific internal energy behind the shock (J kg⁻¹)<br>$e_1$ — 激波后比内能（J kg⁻¹） |
| $e_j$ — Specific internal energy of the incoming liquid (J kg⁻¹)<br>$e_j$ — 入射液体比内能（J kg⁻¹） | $k$ — Auxiliary constant (γ+1)M²/4 (dimensionless)<br>$k$ — 辅助常数 (γ+1)M²/4（无量纲） |
| $M$ — Impact Mach number U/$c_{0}$ (dimensionless)<br>$M$ — 撞击马赫数 U/$c_{0}$（无量纲） | $x$ — Velocity ratio U/$U_{s}$ from Eq. (C5-E03) (dimensionless)<br>$x$ — 来自式（C5-E03）的速度比 U/$U_{s}$（无量纲） |
| $p_H$ — Hugoniot wall pressure (Pa)<br>$p_H$ — Hugoniot 壁面压力（Pa） | $\gamma$ — Stiffness exponent 4.4 (dimensionless)<br>$\gamma$ — 刚度指数 4.4（无量纲） |
| $\Pi$ — Stiffness pressure 6.00 × 10⁸ (Pa)<br>$\Pi$ — 刚度压力 6.00 × 10⁸（Pa） | $c_0$ — Reference sound speed (m s⁻¹)<br>$c_0$ — 参考声速（m s⁻¹） |
| $U$ — Prescribed impact speed (m s⁻¹)<br>$U$ — 给定撞击速度（m s⁻¹） |  |

**Conventions and conditions.** Energy closure assumes a fully caloric stiffened gas; Root x is positive and below 1; M → 0 recovers $p_{H}$ → $p_{j}$ + $Z_{0}$ U.

**约定与条件。** 能量闭合假设为完全量热的刚化气体；根 x 为正且小于 1；M → 0 时回到 $p_{H}$ → $p_{j}$ + $Z_{0}$ U。

(C5-E04) · Energy-conserving Hugoniot pressure in closed form / 能量守恒的 Hugoniot 压力封闭形式


$$
\begin{aligned}e(p,\rho)&=\frac{p+\gamma\Pi}{(\gamma-1)\,\rho},\qquad e_1-e_j=\tfrac12\,(p_1+p_j)\left(\frac1{\rho_j}-\frac1{\rho_1}\right),\\ &x^{2}+\frac{(\gamma+1)M^{2}}{2}\,x-M^{2}=0\ \Longrightarrow\ x=-k+\sqrt{k^{2}+M^{2}},\\ &k=\frac{(\gamma+1)M^{2}}{4},\qquad M=\frac{U}{c_0},\qquad p_H=p_j+\frac{\rho_jU^{2}}{x}.\end{aligned}
$$


![Energy conservation closes the jump and gives one closed-form reference pressure.](../assets/figures/c5-e04.svg)

Energy conservation closes the jump and gives one closed-form reference pressure.

能量守恒使跳跃条件封闭，并给出唯一的封闭形式参照压力。

Check the limits and the number. For $M\to0$, $x\to M$ and $p_H\to p_j+\rho_jc_0U$, which is Eq. (C5-E02). At $U=99.02724$ m s⁻¹, $M=0.060886$, $k=0.0050046$ and $x=0.056086$. Hence $U_s=1765.62$ m s⁻¹, $\rho_1/\rho_j=1.0594$ and $p_H=174.6229$ MPa. A separate bisection on the energy residual in the C++ code gives the same 174.622895 MPa.

检验极限与数值。当 $M\to0$ 时，$x\to M$，$p_H\to p_j+\rho_jc_0U$，即式（C5-E02）。在 $U=99.02724$ m s⁻¹ 时，$M=0.060886$，$k=0.0050046$，$x=0.056086$。于是 $U_s=1765.62$ m s⁻¹，$\rho_1/\rho_j=1.0594$，$p_H=174.6229$ MPa。C++ 程序对能量残差另作二分求根，得到相同的 174.622895 MPa。

Step 6 — Keep the density-only law and drop the energy equation. This is the model that both solvers integrate. Mass and momentum still give $\rho_1=\rho_j(U+S)/S$ and $p_1-p_j=\rho_j(U+S)U$. The law of Eq. (C5-E01) must also give $p_1$ at the density $\rho_1$. Solve this condition for the root $S_B$.

步骤 6——保留仅含密度的定律并舍去能量方程。这是两个求解器积分的模型。质量与动量仍给出 $\rho_1=\rho_j(U+S)/S$ 与 $p_1-p_j=\rho_j(U+S)U$。式（C5-E01）的定律还须在密度 $\rho_1$ 处给出 $p_1$。对该条件求根 $S_B$。

**Symbols before Eq. (C5-E05).**

**式（C5-E05）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $S$ — Lab-frame shock speed toward +z (m s⁻¹)<br>$S$ — 实验室参考系中朝 +z 的激波速度（m s⁻¹） | $S_B$ — Root of the barotropic condition (m s⁻¹)<br>$S_B$ — 正压条件的根（m s⁻¹） |
| $\rho_1$ — Density behind the shock (kg m⁻³)<br>$\rho_1$ — 激波后密度（kg m⁻³） | $\rho_j$ — Incoming density (kg m⁻³)<br>$\rho_j$ — 入射密度（kg m⁻³） |
| $U$ — Incoming speed (m s⁻¹)<br>$U$ — 入射速度（m s⁻¹） | $U_s$ — Shock speed relative to the incoming liquid (m s⁻¹)<br>$U_s$ — 相对入射液体的激波速度（m s⁻¹） |
| $p(\rho_1)$ — Pressure from the law of Eq. (C5-E01) at density $ρ_{1}$ (Pa)<br>$p(\rho_1)$ — 由式（C5-E01）在密度 $ρ_{1}$ 处给出的压力（Pa） | $p_j$ — Incoming pressure (Pa)<br>$p_j$ — 入射压力（Pa） |
| $p_B$ — Barotropic shock pressure (Pa)<br>$p_B$ — 正压激波压力（Pa） |  |

**Conventions and conditions.** Mass and momentum are kept; the energy equation is dropped; $S_{B}$ solves p($ρ_{1}$) = $p_{j}$ + $ρ_{j}$(U+S)U; This is the law both solvers integrate.

**约定与条件。** 保留质量与动量；舍去能量方程；$S_{B}$ 求解 p($ρ_{1}$) = $p_{j}$ + $ρ_{j}$(U+S)U；两个求解器积分的正是这一定律。

(C5-E05) · Barotropic shock pressure used by both solvers / 两个求解器所用的正压激波压力


$$
\begin{aligned}\rho_1&=\rho_j\,\frac{U+S}{S},\qquad U_s=U+S,\\ p(\rho_1)&=p_j+\rho_j\,(U+S)\,U,\qquad p_B=p_j+\rho_j\,(U+S_B)\,U.\end{aligned}
$$


![Replacing the energy equation by the density-only law shifts the planar pressure by a fraction of a percent.](../assets/figures/c5-e05.svg)

Replacing the energy equation by the density-only law shifts the planar pressure by a fraction of a percent.

以仅含密度的定律替代能量方程，使平面压力改变不足百分之一。

At the nominal speed $S_B=1661.86$ m s⁻¹ and $p_B=174.155$ MPa. This lies 0.268% below $p_H$. The gap is the effect of dropping the energy equation. The acoustic estimate of Eq. (C5-E02) lies 7.9% below $p_H$ in absolute pressure. The nonlinear factor is $(p_H-p_j)/(Z_0U)=U_s/c_0=1.0856$.

在名义速度下 $S_B=1661.86$ m s⁻¹，$p_B=174.155$ MPa，比 $p_H$ 低 0.268%。该差值是舍去能量方程的影响。式（C5-E02）的声学估计在绝对压力上比 $p_H$ 低 7.9%。非线性因子为 $(p_H-p_j)/(Z_0U)=U_s/c_0=1.0856$。

## 4. Theory: the finite sensor, edge release and scales

## 4. 理论：有限传感区、边缘释放与尺度

Step 7 — Define what is measured. The planar result of Section 3 holds under a column that fills the wall. A real jet has a free side from the first instant. Report the wall pressure as a mean over a fixed disk. Eq. (C5-E06) uses the axisymmetric area weight $2r\,dr/R^2$. The disk radius $R$ is $a$ for the full sensor and $a/2$ for the centre. This follows the fixed-observer rule of Eq. (C3-E26).

步骤 7——定义被测量。第 3 节的平面结果适用于充满壁面的液柱。真实射流自首次接触起就有自由侧边。将壁面压力报告为固定圆盘上的平均值。式（C5-E06）采用轴对称面积权重 $2r\,dr/R^2$。圆盘半径 $R$ 对全传感区取 $a$，对中心区取 $a/2$。这遵循式（C3-E26）的固定观测量规则。

**Symbols before Eq. (C5-E06).**

**式（C5-E06）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\bar p_R$ — Area-weighted mean absolute pressure on the wall disk (Pa)<br>$\bar p_R$ — 壁面圆盘上的面积加权平均绝对压力（Pa） | $R$ — Sensor radius, a or a/2 (m)<br>$R$ — 传感区半径，取 a 或 a/2（m） |
| $p(r,0,t)$ — Wall pressure at radius r, z = 0 (Pa)<br>$p(r,0,t)$ — 半径 r、z = 0 处的壁面压力（Pa） | $r$ — Radial coordinate (m)<br>$r$ — 径向坐标（m） |
| $a$ — Jet radius (m)<br>$a$ — 射流半径（m） | $t$ — Time from first contact (s)<br>$t$ — 自首次接触起的时间（s） |
| $\tau$ — Dimensionless time $c_{0}$ t / a (dimensionless)<br>$\tau$ — 无量纲时间 $c_{0}$ t / a（无量纲） | $c_0$ — Reference sound speed (m s⁻¹)<br>$c_0$ — 参考声速（m s⁻¹） |
| $\Lambda$ — Finite-area peak factor (dimensionless)<br>$\Lambda$ — 有限面积峰值因子（无量纲） | $p_H$ — Hugoniot wall pressure (Pa)<br>$p_H$ — Hugoniot 壁面压力（Pa） |

**Conventions and conditions.** The weight 2r/R² is the area element of an axisymmetric disk; A line average along r without that weight is a different observable; Peak is taken over the first-arrival window.

**约定与条件。** 权重 2r/R² 是轴对称圆盘的面积微元；沿 r 不带该权重的线平均是另一个观测量；峰值取自首次到达时间窗。

(C5-E06) · Area-weighted wall observer and dimensionless time / 面积加权壁面观测量与无量纲时间


$$
\begin{aligned}\bar p_R(t)&=\frac{2}{R^{2}}\int_0^{R}p(r,0,t)\,r\,dr,\qquad R\in\left\{a,\ \tfrac a2\right\},\\ \tau&=\frac{c_0\,t}{a},\qquad \Lambda=\frac{\max_t\,\bar p_a(t)}{p_H}.\end{aligned}
$$


![The reported wall pressure is a mean over a fixed disk with area weights.](../assets/figures/c5-e06.svg)

The reported wall pressure is a mean over a fixed disk with area weights.

所报告的壁面压力是固定圆盘上带面积权重的平均值。

Step 8 — Estimate the effect of the free side. Pressure release starts at the edge $r=a$ at first contact. Let it advance inward at $c_0$. After the dimensionless time $\tau=c_0t/a$ it has reached the annulus $a(1-\tau)<r\le a$. The fraction of the disk area in that annulus is $f_{\mathrm{rel}}=1-(1-\tau)^2$. If the annulus keeps no excess pressure and the core keeps $p_H$, the mean falls to $p_H(1-\tau)^2$. This is a scale estimate. It fixes the sign and size of the gap, not its value.

步骤 8——估计自由侧边的影响。压力释放自首次接触起从边缘 $r=a$ 开始，设其以 $c_0$ 向内推进。经无量纲时间 $\tau=c_0t/a$ 后，它到达环带 $a(1-\tau)<r\le a$。该环带占圆盘面积的比例为 $f_{\mathrm{rel}}=1-(1-\tau)^2$。若环带不保留超压而核心保持 $p_H$，平均值降为 $p_H(1-\tau)^2$。这是尺度估计，它确定差值的符号与大小，而不确定其数值。

**Symbols before Eq. (C5-E07).**

**式（C5-E07）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $f_{\mathrm{rel}}$ — Fraction of the wall disk reached by edge release (dimensionless)<br>$f_{\mathrm{rel}}$ — 边缘释放已到达的壁面圆盘面积分数（无量纲） | $\tau$ — Dimensionless time $c_{0}$ t / a (dimensionless)<br>$\tau$ — 无量纲时间 $c_{0}$ t / a（无量纲） |
| $\bar p_a$ — Full-sensor mean wall pressure (Pa)<br>$\bar p_a$ — 全传感区平均壁面压力（Pa） | $p_H$ — Hugoniot wall pressure (Pa)<br>$p_H$ — Hugoniot 壁面压力（Pa） |
| $a$ — Jet radius (m)<br>$a$ — 射流半径（m） | $c_0$ — Sound speed carrying the release inward (m s⁻¹)<br>$c_0$ — 向内传播释放的声速（m s⁻¹） |

**Conventions and conditions.** Order-of-magnitude scale, not a prediction; Assumes a release front advancing inward at $c_{0}$ from r = a; Pressure inside the front is taken equal to $p_{H}$.

**约定与条件。** 数量级尺度估计，并非预测；假设释放前沿自 r = a 起以 $c_{0}$ 向内推进；前沿内部压力取为 $p_{H}$。

(C5-E07) · Edge-release scale estimate for the finite sensor / 有限传感区的边缘释放尺度估计


$$
\begin{aligned}f_{\mathrm{rel}}(\tau)&=1-(1-\tau)^{2},\qquad 0\le\tau\le1,\\ \frac{\bar p_a(\tau)}{p_H}&\approx 1-f_{\mathrm{rel}}(\tau)=(1-\tau)^{2}\quad\text{if the released annulus keeps no excess pressure.}\end{aligned}
$$


![Because the jet edge is free from first contact, an annulus relaxes while the core holds p_H.](../assets/figures/c5-e07.svg)

Because the jet edge is free from first contact, an annulus relaxes while the core holds p\_H.

射流边缘自首次接触起即为自由面，环带松弛而核心仍保持 p\_H。

Step 9 — Count the energy that crosses a plane upstream of the wall. The plane $z=2a$ is hit by the incident liquid before the reflected shock arrives. The reflected shock needs about $2a/(U_s-U)=1.20$ ns to climb back for $a=1$ μm. Use the window $t_w=1$ ns. The kinetic-energy flux $\dot K=\tfrac12\rho_jU^3\pi a^2$ is 1.5226 mW. Energy through the plane in 1 ns is 1.5226 pJ. This is liquid energy crossing a plane. A rigid wall does no work on the liquid, so it receives none.

步骤 9——计量穿过壁面上游平面的能量。入射液体在反射激波到达之前先经过平面 $z=2a$。对 $a=1$ μm，反射激波返回该平面约需 $2a/(U_s-U)=1.20$ ns。取时间窗 $t_w=1$ ns。动能通量 $\dot K=\tfrac12\rho_jU^3\pi a^2$ 为 1.5226 mW，1 ns 内穿过平面的能量为 1.5226 pJ。这是穿过平面的液体能量。刚性壁面不对液体做功，因此也不接收功。

**Symbols before Eq. (C5-E08).**

**式（C5-E08）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $A_j$ — Jet cross-section area (m²)<br>$A_j$ — 射流横截面积（m²） | $a$ — Jet radius (m)<br>$a$ — 射流半径（m） |
| $\dot m$ — Incident mass flow rate (kg s⁻¹)<br>$\dot m$ — 入射质量流率（kg s⁻¹） | $\dot K$ — Incident kinetic-energy flux (W)<br>$\dot K$ — 入射动能通量（W） |
| $K$ — Kinetic energy crossing the plane up to time t (J)<br>$K$ — 截至时间 t 穿过平面的动能（J） | $\rho_j$ — Incoming density (kg m⁻³)<br>$\rho_j$ — 入射密度（kg m⁻³） |
| $U$ — Incoming speed (m s⁻¹)<br>$U$ — 入射速度（m s⁻¹） | $t_w$ — Incident-flux window (s)<br>$t_w$ — 入射通量时间窗（s） |
| $U_s$ — Shock speed relative to the incoming liquid (m s⁻¹)<br>$U_s$ — 相对入射液体的激波速度（m s⁻¹） |  |

**Conventions and conditions.** Plane z = 2a lies upstream of the wall; The window ends before the reflected shock reaches the plane; Flux is liquid energy crossing the plane; the rigid wall receives no work.

**约定与条件。** 平面 z = 2a 位于壁面上游；时间窗在反射激波到达该平面之前结束；通量是穿过平面的液体能量；刚性壁面不接收功。

(C5-E08) · Incident mass and kinetic-energy flux through the observation plane / 穿过观察平面的入射质量与动能通量


$$
\begin{aligned}A_j&=\pi a^{2},\qquad \dot m=\rho_j\,U\,A_j,\qquad \dot K=\tfrac12\,\rho_j\,U^{3}A_j,\\ K(t)&=\dot K\,t\quad\text{for }t\le t_w,\qquad t_w<\frac{2a}{U_s-U}.\end{aligned}
$$


![The energy delivered to the plane is a kinetic-energy flux times the window, which bounds nothing at the wall.](../assets/figures/c5-e08.svg)

The energy delivered to the plane is a kinetic-energy flux times the window, which bounds nothing at the wall.

到达平面的能量等于动能通量乘以时间窗，它并不约束壁面。

Step 10 — State the validity range. The nominal Mach number is $M=0.0609$. The tested range is $0.031\le M\le0.092$. The sound-crossing time of the jet radius is $a/c_0=0.615$ ns for $a=1$ μm. The compression behind the shock is only 5.9%. That is why the barotropic law stays within 0.27% of the energy law. No conclusion is claimed outside this range.

步骤 10——说明适用范围。名义马赫数为 $M=0.0609$，检验范围为 $0.031\le M\le0.092$。$a=1$ μm 时，声波穿过射流半径的时间 $a/c_0$ 为 0.615 ns。激波后的压缩仅 5.9%，因此正压律与能量律相差不超过 0.27%。超出此范围不作任何结论。

**Symbols before Eq. (C5-E09).**

**式（C5-E09）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $M$ — Impact Mach number (dimensionless)<br>$M$ — 撞击马赫数（无量纲） | $U$ — Prescribed speed, 50 to 150 (m s⁻¹)<br>$U$ — 给定速度，50 至 150（m s⁻¹） |
| $c_0$ — Reference sound speed (m s⁻¹)<br>$c_0$ — 参考声速（m s⁻¹） | $t_a$ — Time for sound to cross the jet radius (s)<br>$t_a$ — 声波穿过射流半径的时间（s） |
| $a$ — Jet radius, 0.5 to 2 μm (m)<br>$a$ — 射流半径，0.5 至 2 μm（m） | $\rho_1/\rho_j$ — Compression ratio behind the shock (dimensionless)<br>$\rho_1/\rho_j$ — 激波后压缩比（无量纲） |
| $x$ — Velocity ratio at U = 99.027 m s⁻¹ (dimensionless)<br>$x$ — U = 99.027 m s⁻¹ 时的速度比（无量纲） | $p_H$ — Hugoniot pressure (Pa)<br>$p_H$ — Hugoniot 压力（Pa） |
| $p_B$ — Barotropic pressure (Pa)<br>$p_B$ — 正压压力（Pa） |  |

**Conventions and conditions.** Tested range of M is 0.031 to 0.092; a = 1 μm gives $t_{a}$ = 0.615 ns; Compression of 5.9% keeps the barotropic law close to the energy law.

**约定与条件。** M 的检验范围为 0.031 至 0.092；a = 1 μm 时 $t_{a}$ = 0.615 ns；5.9% 的压缩使正压律接近能量律。

(C5-E09) · Dimensionless groups and validity range of the model / 模型的无量纲数与适用范围


$$
\begin{aligned}M&=\frac{U}{c_0}\in[0.031,\ 0.092],\qquad t_a=\frac{a}{c_0},\\ \frac{\rho_1}{\rho_j}&=\frac{1}{1-x}=1.0594,\qquad \frac{p_H-p_B}{p_H}=0.268\%.\end{aligned}
$$


![Small Mach number and small compression are what let a barotropic liquid stand in for the full energy law.](../assets/figures/c5-e09.svg)

Small Mach number and small compression are what let a barotropic liquid stand in for the full energy law.

小马赫数与小压缩，使正压液体可以替代完整能量律。

## 5. Calculation: the one-dimensional reference solver

## 5. 计算：一维参考求解器

Step 11 — Write the planar problem as conservation laws. Eq. (C5-E10) holds mass and momentum in conservative form. Conservative form lets a shock form and move at the correct speed. The wall is a mirrored state with $u=0$. The inflow boundary holds the state $(\rho_j,-U)$. The initial state is the uniform inflow state.

步骤 11——把平面问题写成守恒律。式（C5-E10）以守恒形式表示质量与动量。守恒形式使激波得以形成并以正确速度运动。壁面为 $u=0$ 的镜像状态。入流边界保持状态 $(\rho_j,-U)$，初态为均匀入流状态。

**Symbols before Eq. (C5-E10).**

**式（C5-E10）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\rho$ — Liquid density (kg m⁻³)<br>$\rho$ — 液体密度（kg m⁻³） | $u$ — Axial velocity, negative toward the wall (m s⁻¹)<br>$u$ — 轴向速度，朝壁面为负（m s⁻¹） |
| $p(\rho)$ — Pressure from Eq. (C5-E01) (Pa)<br>$p(\rho)$ — 来自式（C5-E01）的压力（Pa） | $z$ — Axial coordinate from the wall (m)<br>$z$ — 距壁面的轴向坐标（m） |
| $t$ — Time (s)<br>$t$ — 时间（s） | $H$ — Column length 4 μm (m)<br>$H$ — 液柱长度 4 μm（m） |
| $\rho_j$ — Inflow density (kg m⁻³)<br>$\rho_j$ — 入流密度（kg m⁻³） | $U$ — Inflow speed (m s⁻¹)<br>$U$ — 入流速度（m s⁻¹） |
| $\partial_t$ — Partial derivative with respect to time (s⁻¹)<br>$\partial_t$ — 对时间的偏导数（s⁻¹） | $\partial_z$ — Partial derivative with respect to axial position (m⁻¹)<br>$\partial_z$ — 对轴向位置的偏导数（m⁻¹） |

**Conventions and conditions.** Planar column, no radial variation; Viscosity omitted in this reference; Initial state is the uniform inflow state.

**约定与条件。** 平面液柱，无径向变化；该参考解忽略黏性；初态为均匀入流状态。

(C5-E10) · One-dimensional conservative equations of the reference solver / 参考求解器的一维守恒方程


$$
\begin{aligned}\partial_t\rho+\partial_z(\rho u)&=0,\\ \partial_t(\rho u)+\partial_z\!\left(\rho u^{2}+p(\rho)\right)&=0,\\ u(0,t)=0,&\qquad (\rho,u)\big|_{z=H}=(\rho_j,\,-U).\end{aligned}
$$


![Mass and momentum in conservative form let a shock form and travel at the correct speed.](../assets/figures/c5-e10.svg)

Mass and momentum in conservative form let a shock form and travel at the correct speed.

守恒形式的质量与动量方程使激波得以形成并以正确速度传播。

Step 12 — Discretize with a dissipative flux and a two-stage time step. Cell size is $\Delta z=H/N=4\ \mu\mathrm m/4000=1$ nm. The face flux averages the two physical fluxes and subtracts $\alpha/2$ times the state jump. The speed $\alpha$ is the larger value of $|u|+c$ on the two sides. [[R19]](../reference/sources.html#r19) [[R18]](../reference/sources.html#r18) The Heun step is a predictor followed by the average of two spatial operators. It is second order in time and first order in space.

步骤 12——用耗散通量与两步时间推进离散。单元尺寸 $\Delta z=H/N=4\ \mu\mathrm m/4000=1$ nm。界面通量取两侧物理通量的平均，再减去状态跳跃的 $\alpha/2$ 倍。速度 $\alpha$ 取两侧 $|u|+c$ 的较大者。 [[R19]](../reference/sources.html#r19) [[R18]](../reference/sources.html#r18) Heun 步先预测，再取两次空间算子的平均。它在时间上为二阶，在空间上为一阶。

**Symbols before Eq. (C5-E11).**

**式（C5-E11）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol Q$ — Vector of conserved variables ρ and ρu (kg m⁻³; kg m⁻² s⁻¹)<br>$\boldsymbol Q$ — 守恒变量向量 ρ 与 ρu（kg m⁻³; kg m⁻² s⁻¹） | $\boldsymbol F$ — Physical flux vector (kg m⁻² s⁻¹; Pa)<br>$\boldsymbol F$ — 物理通量向量（kg m⁻² s⁻¹; Pa） |
| $N$ — Number of cells, 4000 (dimensionless)<br>$N$ — 网格单元数，4000（无量纲） | $H$ — Column length 4 μm (m)<br>$H$ — 液柱长度 4 μm（m） |
| $\Delta z$ — Cell size H/N, 1 nm (m)<br>$\Delta z$ — 单元尺寸 H/N，1 nm（m） | $\boldsymbol F_{i+\frac12}$ — Numerical flux at the face between cells i and i+1 (kg m⁻² s⁻¹; Pa)<br>$\boldsymbol F_{i+\frac12}$ — 单元 i 与 i+1 之间界面的数值通量（kg m⁻² s⁻¹; Pa） |
| $\boldsymbol Q_L$ — State left of the face (kg m⁻³; kg m⁻² s⁻¹)<br>$\boldsymbol Q_L$ — 界面左侧状态（kg m⁻³; kg m⁻² s⁻¹） | $\boldsymbol Q_R$ — State right of the face (kg m⁻³; kg m⁻² s⁻¹)<br>$\boldsymbol Q_R$ — 界面右侧状态（kg m⁻³; kg m⁻² s⁻¹） |
| $\alpha$ — Largest local wave speed (Rusanov) (m s⁻¹)<br>$\alpha$ — 最大局部波速（Rusanov）（m s⁻¹） | $c_L$ — Sound speed of Eq. (C5-E01) left of the face (m s⁻¹)<br>$c_L$ — 界面左侧由式（C5-E01）给出的声速（m s⁻¹） |
| $c_R$ — Sound speed of Eq. (C5-E01) right of the face (m s⁻¹)<br>$c_R$ — 界面右侧由式（C5-E01）给出的声速（m s⁻¹） | $\mathcal L$ — Spatial operator −∂\_z F discretized by the face fluxes (kg m⁻³ s⁻¹; Pa m⁻¹)<br>$\mathcal L$ — 由界面通量离散的空间算子 −∂\_z F（kg m⁻³ s⁻¹; Pa m⁻¹） |
| $\Delta t$ — Time step 0.4 Δz / (U + 1.2 $c_{wall}$) (s)<br>$\Delta t$ — 时间步 0.4 Δz / (U + 1.2 $c_{wall}$)（s） | $\boldsymbol Q^{*}$ — Predictor state (kg m⁻³; kg m⁻² s⁻¹)<br>$\boldsymbol Q^{*}$ — 预测态（kg m⁻³; kg m⁻² s⁻¹） |
| $\boldsymbol Q^{n}$ — Old state (kg m⁻³; kg m⁻² s⁻¹)<br>$\boldsymbol Q^{n}$ — 旧状态（kg m⁻³; kg m⁻² s⁻¹） | $\boldsymbol Q^{n+1}$ — New state (kg m⁻³; kg m⁻² s⁻¹)<br>$\boldsymbol Q^{n+1}$ — 新状态（kg m⁻³; kg m⁻² s⁻¹） |

**Conventions and conditions.** First-order in space, second-order in time (Heun); Dissipation scales with α, so shocks stay stable; Face fluxes at the wall use a mirrored ghost state.

**约定与条件。** 空间一阶、时间二阶（Heun）；耗散量与 α 成比例，激波保持稳定；壁面界面通量采用镜像虚拟状态。

(C5-E11) · Rusanov flux with Heun time stepping / Rusanov 通量与 Heun 时间推进


$$
\begin{aligned}\boldsymbol Q&=\begin{pmatrix}\rho\\ \rho u\end{pmatrix},\quad \boldsymbol F=\begin{pmatrix}\rho u\\ \rho u^{2}+p\end{pmatrix},\quad \Delta z=\frac{H}{N},\\ \boldsymbol F_{i+\frac12}&=\tfrac12(\boldsymbol F_L+\boldsymbol F_R)-\tfrac12\,\alpha\,(\boldsymbol Q_R-\boldsymbol Q_L),\quad \alpha=\max(|u_L|+c_L,\ |u_R|+c_R),\\ \boldsymbol Q^{*}&=\boldsymbol Q^{n}+\Delta t\,\mathcal L(\boldsymbol Q^{n}),\quad \boldsymbol Q^{n+1}=\boldsymbol Q^{n}+\tfrac12\Delta t\,[\mathcal L(\boldsymbol Q^{n})+\mathcal L(\boldsymbol Q^{*})].\end{aligned}
$$


![A simple dissipative flux and a two-stage time step are enough to carry the shock to the wall.](../assets/figures/c5-e11.svg)

A simple dissipative flux and a two-stage time step are enough to carry the shock to the wall.

简单的耗散通量与两步时间推进足以把激波推进到壁面。

Step 13 — Read the planar reference. Run the code for the confined column at $U=99.02724$ m s⁻¹. Average the wall pressure over 0.2 to 2 ns. Compare it with the exact planar pressures. Every entry names its reference value.

步骤 13——读取平面参考解。对受限液柱在 $U=99.02724$ m s⁻¹ 下运行程序，取 0.2 至 2 ns 的壁面压力平均值，并与精确平面压力比较。每一项都注明其参考值。

| Quantity<br>量 | Value (MPa, absolute)<br>数值（MPa，绝对压力） | Relative to $p_B$<br>相对 $p_B$ | Relative to $p_H$<br>相对 $p_H$ |
| --- | --- | --- | --- |
| Acoustic estimate $p_A$<br>声学估计 $p_A$ | 160.867<br>160.867 | −7.63%<br>−7.63% | −7.88%<br>−7.88% |
| Barotropic shock $p_B$<br>正压激波 $p_B$ | 174.155<br>174.155 | 0 (reference)<br>0（参照） | −0.27%<br>−0.27% |
| Hugoniot $p_H$<br>Hugoniot $p_H$ | 174.623<br>174.623 | +0.27%<br>+0.27% | 0 (reference)<br>0（参照） |
| C++ plateau, 4000 cells<br>C++ 平台，4000 单元 | 174.148<br>174.148 | −0.004%<br>−0.004% | −0.27%<br>−0.27% |

The C++ plateau agrees with the barotropic shock to 0.004%. This is the check that the discretization reproduces its own exact law. The remaining 0.27% to $p_H$ is the energy equation that the model omits.

C++ 平台与正压激波的偏差为 0.004%。这检验了离散格式再现了它自身的精确定律。与 $p_H$ 相差的 0.27% 来自模型舍去的能量方程。

## 6. Verification: the COMSOL axisymmetric model

## 6. 核验：COMSOL 轴对称模型

Step 14 — State the finite-element model. It is a compressible laminar-flow study in axisymmetric $(r,z)$ coordinates. Eq. (C5-E12) adds radial motion and a small viscosity to the same liquid. The density follows the pressure through the inverse of Eq. (C5-E01). There is no gas phase.

步骤 14——给出有限元模型。它是轴对称 $(r,z)$ 坐标下的可压缩层流研究。式（C5-E12）在同一种液体上增加径向运动与很小的黏性。密度通过式（C5-E01）的逆关系随压力变化。不含气相。

**Symbols before Eq. (C5-E12).**

**式（C5-E12）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\rho$ — Liquid density (kg m⁻³)<br>$\rho$ — 液体密度（kg m⁻³） | $\boldsymbol u$ — Velocity vector with components ($u_{r}$, w) (m s⁻¹)<br>$\boldsymbol u$ — 速度向量，分量为 ($u_{r}$, w)（m s⁻¹） |
| $p$ — Absolute pressure (Pa)<br>$p$ — 绝对压力（Pa） | $\mu$ — Dynamic viscosity 1 mPa s (Pa s)<br>$\mu$ — 动力黏度 1 mPa s（Pa s） |
| $\boldsymbol I$ — Identity tensor (dimensionless)<br>$\boldsymbol I$ — 单位张量（无量纲） | $\rho_j$ — Reference density (kg m⁻³)<br>$\rho_j$ — 参考密度（kg m⁻³） |
| $p_j$ — Reference pressure (Pa)<br>$p_j$ — 参考压力（Pa） | $\Pi$ — Stiffness pressure of Eq. (C5-E01) (Pa)<br>$\Pi$ — 式（C5-E01）的刚度压力（Pa） |
| $\gamma$ — Stiffness exponent of Eq. (C5-E01) (dimensionless)<br>$\gamma$ — 式（C5-E01）的刚度指数（无量纲） | $\nabla$ — Gradient in axisymmetric (r, z) coordinates (m⁻¹)<br>$\nabla$ — 轴对称 (r, z) 坐标中的梯度（m⁻¹） |
| $\mathsf T$ — Transpose (dimensionless)<br>$\mathsf T$ — 转置（无量纲） |  |

**Conventions and conditions.** Axisymmetric compressible laminar flow, no gas phase; Density follows pressure through the inverse of Eq. (C5-E01); Viscosity is small and does not set the plateau.

**约定与条件。** 轴对称可压缩层流，无气相；密度通过式（C5-E01）的逆关系随压力变化；黏性很小，不决定压力平台。

(C5-E12) · Axisymmetric compressible flow equations of the COMSOL model / COMSOL 模型的轴对称可压缩流动方程


$$
\begin{aligned}\partial_t\rho+\nabla\!\cdot(\rho\boldsymbol u)&=0,\\ \rho\left(\partial_t\boldsymbol u+\boldsymbol u\!\cdot\!\nabla\boldsymbol u\right)&=-\nabla p+\nabla\!\cdot\!\left[\mu\left(\nabla\boldsymbol u+\nabla\boldsymbol u^{\mathsf T}\right)-\tfrac23\mu\,(\nabla\!\cdot\boldsymbol u)\,\boldsymbol I\right],\\ \rho&=\rho_j\left(\frac{p+\Pi}{p_j+\Pi}\right)^{1/\gamma}.\end{aligned}
$$


![The finite-element model solves the same liquid with radial motion and a small viscosity added.](../assets/figures/c5-e12.svg)

The finite-element model solves the same liquid with radial motion and a small viscosity added.

有限元模型求解同一种液体，并增加径向运动与很小的黏性。

Step 15 — Set the boundaries and the initial state. The domain is $0\le r\le a$ and $0\le z\le4a$. The wall is a slip wall. The inflow boundary carries the speed $U$. The side boundary is an outlet at $p_j$, which creates the free side. The liquid starts with a thin onset layer $w=-U\tanh(z/\delta)$, $\delta=0.02a$, so that the wall holds it at rest at $t=0$.

步骤 15——设定边界与初态。计算域为 $0\le r\le a$、$0\le z\le4a$。壁面为滑移壁面。入流边界给定速度 $U$。侧边界为压力 $p_j$ 的出口，由此形成自由侧边。液体以薄过渡层 $w=-U\tanh(z/\delta)$、$\delta=0.02a$ 开始，使壁面在 $t=0$ 时将其约束为静止。

**Symbols before Eq. (C5-E13).**

**式（C5-E13）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol n$ — Unit normal to the boundary (dimensionless)<br>$\boldsymbol n$ — 边界单位法向量（无量纲） | $\boldsymbol u$ — Velocity vector (m s⁻¹)<br>$\boldsymbol u$ — 速度向量（m s⁻¹） |
| $u_z$ — Axial velocity component (m s⁻¹)<br>$u_z$ — 轴向速度分量（m s⁻¹） | $w$ — Axial velocity w(r,z,t) (m s⁻¹)<br>$w$ — 轴向速度 w(r,z,t)（m s⁻¹） |
| $\boldsymbol e_z$ — Unit vector along +z (dimensionless)<br>$\boldsymbol e_z$ — 沿 +z 的单位向量（无量纲） | $U$ — Inflow speed (m s⁻¹)<br>$U$ — 入流速度（m s⁻¹） |
| $a$ — Jet radius (m)<br>$a$ — 射流半径（m） | $p_j$ — Release pressure and initial pressure (Pa)<br>$p_j$ — 释放压力与初始压力（Pa） |
| $\delta$ — Onset thickness 0.02 a (m)<br>$\delta$ — 起始过渡厚度 0.02 a（m） | $\tanh$ — Hyperbolic tangent (dimensionless)<br>$\tanh$ — 双曲正切（无量纲） |

**Conventions and conditions.** Domain r from 0 to a and z from 0 to 4a; The release side stands for a free jet surface; Axisymmetric normals are $n_{r}$ and $n_{z}$.

**约定与条件。** 计算域 r 从 0 到 a，z 从 0 到 4a；释放侧代表射流自由表面；轴对称法向分量为 $n_{r}$ 与 $n_{z}$。

(C5-E13) · Boundary and initial conditions of the axisymmetric model / 轴对称模型的边界条件与初始条件


$$
\begin{aligned}&\text{wall }z=0:\ \boldsymbol u\!\cdot\!\boldsymbol n=0\ (\text{slip}),\qquad \text{axis }r=0:\ \partial_ru_z=0,\\ &\text{inflow }z=4a:\ \boldsymbol u=-U\,\boldsymbol e_z,\qquad \text{side }r=a:\ p=p_j\ (\text{release}),\\ &\text{initial: }\ w(r,z,0)=-U\tanh\frac{z}{\delta},\quad p(r,z,0)=p_j,\quad \delta=0.02a.\end{aligned}
$$


![A free side and a rigid slip wall are the only boundaries that change the planar picture.](../assets/figures/c5-e13.svg)

A free side and a rigid slip wall are the only boundaries that change the planar picture.

自由侧边与刚性滑移壁面是仅有的改变平面图景的边界。

Step 16 — Fix the observers before the comparison. Eq. (C5-E14) defines the transport observers at the plane $z=2a$ and the area-weighted wall pressure at $z=0$. The same integrals serve every mesh and every case. Mass flux and kinetic-energy flux through the plane check the prescribed inflow. The mass-flux-weighted incident speed over 0 to 1 ns is 99.0272 m s⁻¹, which differs from $U$ by less than $10^{-5}$ percent. The incident energy over the same window is 1.52258 pJ, which differs from Eq. (C5-E08) by less than $10^{-5}$ percent.

步骤 16——比较之前先固定观测量。式（C5-E14）定义了平面 $z=2a$ 处的输运观测量与 $z=0$ 处的面积加权壁面压力。同一组积分适用于每一种网格和每一个工况。穿过平面的质量通量与动能通量用于检验给定的入流。0 至 1 ns 内质量通量加权的入射速度为 99.0272 m s⁻¹，与 $U$ 的偏差小于百分之 $10^{-5}$。同一时间窗内的入射能量为 1.52258 pJ，与式（C5-E08）的偏差小于百分之 $10^{-5}$。

**Symbols before Eq. (C5-E14).**

**式（C5-E14）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\dot m_p$ — Computed mass flow through the plane (kg s⁻¹)<br>$\dot m_p$ — 计算得到的穿过平面的质量流率（kg s⁻¹） | $\dot K_p$ — Computed kinetic-energy flux through the plane (W)<br>$\dot K_p$ — 计算得到的穿过平面的动能通量（W） |
| $U_{\mathrm{inc}}$ — Mass-flux-weighted incident speed (m s⁻¹)<br>$U_{\mathrm{inc}}$ — 质量通量加权的入射速度（m s⁻¹） | $\bar p_R$ — Area-weighted wall pressure of Eq. (C5-E06) (Pa)<br>$\bar p_R$ — 式（C5-E06）的面积加权壁面压力（Pa） |
| $w$ — Axial velocity (m s⁻¹)<br>$w$ — 轴向速度（m s⁻¹） | $u_r$ — Radial velocity (m s⁻¹)<br>$u_r$ — 径向速度（m s⁻¹） |
| $\rho$ — Density (kg m⁻³)<br>$\rho$ — 密度（kg m⁻³） | $\max(-w,0)$ — Positive part of the inward axial speed (m s⁻¹)<br>$\max(-w,0)$ — 朝壁面轴向速度的正部（m s⁻¹） |
| $t_w$ — Incident-flux window 1 ns (s)<br>$t_w$ — 入射通量时间窗 1 ns（s） | $a$ — Jet radius (m)<br>$a$ — 射流半径（m） |
| $R$ — Sensor radius (m)<br>$R$ — 传感区半径（m） | $r$ — Radial coordinate (m)<br>$r$ — 径向坐标（m） |

**Conventions and conditions.** Integrals use the 2πr weight of the axisymmetric model; Only inward flux counts at the plane; These are the numbers that check the transport and the wall observer.

**约定与条件。** 积分采用轴对称模型的 2πr 权重；平面处仅计入朝壁面的通量；这些数用于检验输运与壁面观测量。

(C5-E14) · Observers evaluated in the COMSOL model / COMSOL 模型中计算的观测量


$$
\begin{aligned}\dot m_p&=\int_0^{a}\rho\,\max(-w,0)\,2\pi r\,dr\Big|_{z=2a},\qquad \dot K_p=\int_0^{a}\tfrac12\rho\,(u_r^{2}+w^{2})\max(-w,0)\,2\pi r\,dr\Big|_{z=2a},\\ U_{\mathrm{inc}}&=\frac{\int_0^{t_w}\!\!\int_0^a\rho\,\max(-w,0)\,(-w)\,2\pi r\,dr\,dt}{\int_0^{t_w}\dot m_p\,dt},\qquad \bar p_R=\frac{\int_0^R p\,2\pi r\,dr}{\pi R^{2}}\Big|_{z=0}.\end{aligned}
$$


![One set of fixed integrals defines every number reported from the finite-element model.](../assets/figures/c5-e14.svg)

One set of fixed integrals defines every number reported from the finite-element model.

一组固定的积分定义了有限元模型报告的每个数值。

## 7. Verification: convergence, balances and the cross-check

## 7. 核验：收敛、平衡与交叉检验

Step 17 — Judge mesh convergence by the peak of the full-sensor mean. Global refinement beyond about 64,000 elements exceeds the available memory. The peak forms about 0.03 ns after contact and within about 0.05 $a$ of the wall. So refine only a wall band $r\le a$, $z\le0.15a$ and keep the rest of the mesh fixed. Eq. (C5-E15) defines the relative error and the successive change. The denominator of the change is the previous, coarser value.

步骤 17——以全传感区平均的峰值判断网格收敛。全局加密超过约 64,000 单元时超出可用内存。峰值在接触后约 0.03 ns、距壁面约 0.05 $a$ 以内形成。因此仅加密壁面带 $r\le a$、$z\le0.15a$，其余网格保持不变。式（C5-E15）定义了相对误差与逐次变化量，变化量的分母为前一个较粗网格的值。

**Symbols before Eq. (C5-E15).**

**式（C5-E15）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\varepsilon$ — Relative error (dimensionless)<br>$\varepsilon$ — 相对误差（无量纲） | $X$ — Computed quantity (units of the compared quantity)<br>$X$ — 被评价的计算量（units of the compared quantity） |
| $X_{\mathrm{ref}}$ — Stated reference value (units of the compared quantity)<br>$X_{\mathrm{ref}}$ — 所注明的参考值（units of the compared quantity） | $\Delta_k$ — Successive change on refinement step k (dimensionless)<br>$\Delta_k$ — 第 k 次加密的相邻变化（无量纲） |
| $\bar P_k$ — Peak full-sensor wall pressure on band size $h_{k}$ (Pa)<br>$\bar P_k$ — 带宽 $h_{k}$ 上的全传感区壁面压力峰值（Pa） | $\bar p_a$ — Full-sensor mean wall pressure (Pa)<br>$\bar p_a$ — 全传感区平均壁面压力（Pa） |
| $h_k$ — Maximum element size in the wall band r ≤ a, z ≤ 0.15 a (m)<br>$h_k$ — 壁面加密带 r ≤ a、z ≤ 0.15 a 内的最大单元尺寸（m） | $k$ — Refinement index, 1 to 4 (dimensionless)<br>$k$ — 加密序号，取 1 至 4（无量纲） |

**Conventions and conditions.** Every error names its reference value; Output spacing is 0.001 ns; The band is refined alone because global refinement exceeds memory.

**约定与条件。** 每个误差都注明其参考值；输出间隔为 0.001 ns；仅加密壁面带，因为全局加密超出内存。

(C5-E15) · Relative error and successive-refinement change / 相对误差与逐次加密变化量


$$
\begin{aligned}\varepsilon(X;X_{\mathrm{ref}})&=\frac{|X-X_{\mathrm{ref}}|}{|X_{\mathrm{ref}}|},\qquad \Delta_k=\varepsilon\!\left(\bar P_k;\ \bar P_{k-1}\right),\\ \bar P_k&=\max_{0\le t\le0.3\,\mathrm{ns}}\bar p_a(t)\ \text{on band size }h_k,\qquad h_k=\frac{a}{40},\frac{a}{80},\frac{a}{160},\frac{a}{320}.\end{aligned}
$$


![Mesh convergence is judged by how little the peak moves when only the wall band is refined.](../assets/figures/c5-e15.svg)

Mesh convergence is judged by how little the peak moves when only the wall band is refined.

网格收敛以仅加密壁面带时峰值的变化量大小来判断。

| Band size $h$<br>加密带尺寸 $h$ | Elements<br>单元数 | Peak full sensor (MPa)<br>全传感区峰值（MPa） | Change $\Delta_k$<br>变化量 $\Delta_k$ | Peak / $p_H$<br>峰值 / $p_H$ | Peak centre $r\le a/2$ (MPa)<br>中心区峰值 $r\le a/2$（MPa） |
| --- | --- | --- | --- | --- | --- |
| $a/40$<br>$a/40$ | 16,176<br>16,176 | 166.593<br>166.593 | —<br>— | 0.9540<br>0.9540 | 175.607<br>175.607 |
| $a/80$<br>$a/80$ | 18,468<br>18,468 | 163.299<br>163.299 | 1.98%<br>1.98% | 0.9352<br>0.9352 | 174.302<br>174.302 |
| $a/160$<br>$a/160$ | 26,776<br>26,776 | 162.579<br>162.579 | 0.44%<br>0.44% | 0.9310<br>0.9310 | 174.284<br>174.284 |
| $a/320$<br>$a/320$ | 57,668<br>57,668 | 162.608<br>162.608 | 0.02%<br>0.02% | 0.9312<br>0.9312 | 174.373<br>174.373 |

The successive changes fall from 1.98% to 0.44% and then to 0.02%. The converged full-sensor peak is 162.6 MPa. It is 0.931 of $p_H$, that is 6.9% below the reference. The converged centre-disk peak is 174.37 MPa, 0.14% from $p_H$.

逐次变化量由 1.98% 降至 0.44%，再降至 0.02%。收敛的全传感区峰值为 162.6 MPa，为 $p_H$ 的 0.931 倍，即比参照值低 6.9%。收敛的中心圆盘峰值为 174.37 MPa，与 $p_H$ 相差 0.14%。

Step 18 — Check the time step. A run with strict steps and relative tolerance $10^{-3}$ on the 16,136-element mesh gives a full-sensor peak of 168.106 MPa. The automatic-step run gives 169.359 MPa. They differ by 0.74% of the automatic value. A time-step study at the finest band is not done.

步骤 18——检查时间步。在 16,136 单元网格上，采用严格步长、相对容差 $10^{-3}$ 的运行给出全传感区峰值 168.106 MPa，自动步长运行给出 169.359 MPa，二者相差自动步长值的 0.74%。最细加密带上的时间步研究尚未进行。

Step 19 — Audit the conservation laws. Close the column on the sides so nothing leaves sideways. Eq. (C5-E16) then compares the change of axial momentum and of mass with their own boundary integrals over 0 to 3 ns. The momentum residual is 0.106% and the mass residual is 0.018%. These residuals test the solver, not the physics.

步骤 19——审计守恒律。将液柱侧面封闭，使侧向无流出。式（C5-E16）在 0 至 3 ns 内把轴向动量与质量的变化同各自的边界积分比较。动量残差为 0.106%，质量残差为 0.018%。这些残差检验的是求解器，而不是物理。

**Symbols before Eq. (C5-E16).**

**式（C5-E16）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $P_z$ — Axial momentum of the liquid in the domain (kg m s⁻¹)<br>$P_z$ — 计算域内液体的轴向动量（kg m s⁻¹） | $F_{\mathrm{wall}}$ — Pressure force on the wall, ∫ p dA (N)<br>$F_{\mathrm{wall}}$ — 壁面压力，∫ p dA（N） |
| $F_{\mathrm{top}}$ — Inflow pressure force plus momentum flux, ∫(p + ρw²) dA (N)<br>$F_{\mathrm{top}}$ — 入流压力加动量通量，∫(p + ρw²) dA（N） | $M$ — Liquid mass in the domain (kg)<br>$M$ — 计算域内液体质量（kg） |
| $\dot m_{\mathrm{top}}$ — Net mass flow into the domain through the top (kg s⁻¹)<br>$\dot m_{\mathrm{top}}$ — 经顶部净流入计算域的质量流率（kg s⁻¹） | $V$ — Domain volume (axisymmetric) (m³)<br>$V$ — 计算域体积（轴对称）（m³） |
| $e_P$ — Momentum balance residual (dimensionless)<br>$e_P$ — 动量平衡残差（无量纲） | $e_M$ — Mass balance residual (dimensionless)<br>$e_M$ — 质量平衡残差（无量纲） |
| $t$ — Current time (s)<br>$t$ — 当前时间（s） | $t\prime$ — Integration variable (s)<br>$t\prime$ — 积分变量（s） |
| $w$ — Axial velocity (m s⁻¹)<br>$w$ — 轴向速度（m s⁻¹） |  |

**Conventions and conditions.** Confined case: side wall set to slip so nothing leaves sideways; Forces are signed with +z positive; Balance is checked over 0 to 3 ns.

**约定与条件。** 受限情形：侧壁取滑移，侧向无流出；力以 +z 为正；在 0 至 3 ns 内检验平衡。

(C5-E16) · Time-integrated momentum and mass balance of the confined model / 受限模型的时间积分动量与质量平衡


$$
\begin{aligned}\Delta P_z(t)&=P_z(t)-P_z(0)=\int_0^{t}\left(F_{\mathrm{wall}}-F_{\mathrm{top}}\right)dt',\qquad P_z=\int_V\rho w\,dV,\\ \Delta M(t)&=M(t)-M(0)=-\int_0^{t}\dot m_{\mathrm{top}}\,dt',\qquad M=\int_V\rho\,dV,\\ e_P&=\frac{\max_t|\Delta P_z-\int(F_{\mathrm{wall}}-F_{\mathrm{top}})dt'|}{\max_t|\Delta P_z|},\quad e_M\ \text{defined likewise.}\end{aligned}
$$


![Integrating forces and flows over the event must reproduce the change in momentum and mass.](../assets/figures/c5-e16.svg)

Integrating forces and flows over the event must reproduce the change in momentum and mass.

对整个事件的力与流量积分，必须再现动量与质量的变化。

Step 20 — Compare the two solvers on the same problem. Both integrate the confined planar column with the same law, inputs, wall and inflow. Interpolate the C++ history onto the 361 COMSOL sample times between 0.2 and 2.0 ns. Eq. (C5-E17) gives a relative L2 difference of 0.034% and a largest pointwise difference of 0.096%. The plateaus are 174.205 MPa (COMSOL) and 174.148 MPa (C++), a difference of 0.032%. The COMSOL plateau lies 0.24% below $p_H$ and 0.028% above $p_B$.

步骤 20——在同一问题上比较两个求解器。二者以相同的定律、输入、壁面和入流积分受限平面液柱。把 C++ 历程插值到 0.2 至 2.0 ns 间的 361 个 COMSOL 样本时刻。式（C5-E17）给出相对 L2 差 0.034%，最大逐点差 0.096%。平台分别为 174.205 MPa（COMSOL）与 174.148 MPa（C++），相差 0.032%。COMSOL 平台比 $p_H$ 低 0.24%，比 $p_B$ 高 0.028%。

**Symbols before Eq. (C5-E17).**

**式（C5-E17）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\delta_2$ — Relative L2 difference of the two wall histories (dimensionless)<br>$\delta_2$ — 两条壁面压力历程的相对 L2 差（无量纲） | $\delta_\infty$ — Largest pointwise relative difference (dimensionless)<br>$\delta_\infty$ — 最大逐点相对差（无量纲） |
| $p^{C}_m$ — COMSOL wall pressure at sample m (Pa)<br>$p^{C}_m$ — 样本 m 处的 COMSOL 壁面压力（Pa） | $p^{X}_m$ — C++ wall pressure interpolated to the same time (Pa)<br>$p^{X}_m$ — 线性插值到同一时刻的 C++ 壁面压力（Pa） |
| $N_s$ — Number of common samples, 361 (dimensionless)<br>$N_s$ — 共同样本数，361（无量纲） | $m$ — Sample index (dimensionless)<br>$m$ — 样本序号（无量纲） |
| $\bar p_{\mathrm{pl}}$ — Plateau pressure, mean over the window (Pa)<br>$\bar p_{\mathrm{pl}}$ — 压力平台，窗口内平均（Pa） | $t_m$ — Sample time spaced by 5 ps (s)<br>$t_m$ — 间隔 5 ps 的样本时间（s） |

**Conventions and conditions.** Both solvers use the same law, inputs, wall and inflow; The window starts after the arrival transient; Agreement tests the implementation of one model.

**约定与条件。** 两个求解器采用同一定律、输入、壁面与入流；时间窗在到达瞬态之后开始；一致性检验的是同一模型的实现。

(C5-E17) · Cross-solver comparison metrics for the confined column / 受限液柱的跨求解器比较指标


$$
\begin{aligned}\delta_{2}&=\sqrt{\frac{\sum_{m=1}^{N_s}\left(p^{C}_m-p^{X}_m\right)^{2}}{\sum_{m=1}^{N_s}\left(p^{X}_m\right)^{2}}},\qquad \delta_{\infty}=\max_m\frac{|p^{C}_m-p^{X}_m|}{p^{X}_m},\\ \bar p_{\mathrm{pl}}&=\frac{1}{N_s}\sum_{m=1}^{N_s}p_m,\qquad t_m\in[0.2,\ 2.0]\ \mathrm{ns},\quad N_s=361.\end{aligned}
$$


![Two codes with different numerics reach the same plateau history, which checks the implementation.](../assets/figures/c5-e17.svg)

Two codes with different numerics reach the same plateau history, which checks the implementation.

两个数值方法不同的程序得到同一平台历程，这检验了实现的正确性。

The agreement shows that two codes with different numerics implement the same model. It does not show that the model matches a real jet.

该一致性表明数值方法不同的两个程序实现了同一个模型。它并不表明该模型与真实射流一致。

## 8. Sensitivity and the delivered relations

## 8. 敏感性与交付关系

Step 21 — Vary the speed and the radius at the converged band size $h=a/160$. Eq. (C5-E18) defines the peak factor $\Lambda_i$ of each case and its spread. Five cases cover $U=50$ to 150 m s⁻¹ and $a=0.5$ to 2 μm. These ranges are scenario choices, not confidence intervals.

步骤 21——在收敛的加密带尺寸 $h=a/160$ 下改变速度与半径。式（C5-E18）定义了各工况的峰值因子 $\Lambda_i$ 及其离散度。五个工况覆盖 $U=50$ 至 150 m s⁻¹、$a=0.5$ 至 2 μm。这些范围是情景选择，并非置信区间。

| $U$ (m s⁻¹)<br>$U$（m s⁻¹） | $a$ (μm)<br>$a$（μm） | $p_H$ (MPa)<br>$p_H$（MPa） | Peak full sensor (MPa)<br>全传感区峰值（MPa） | $\Lambda$<br>$\Lambda$ | Centre error vs $p_H$<br>中心区相对 $p_H$ 误差 |
| --- | --- | --- | --- | --- | --- |
| 50<br>50 | 1<br>1 | 84.712<br>84.712 | 78.860<br>78.860 | 0.9309<br>0.9309 | 0.04%<br>0.04% |
| 99.03<br>99.03 | 1<br>1 | 174.623<br>174.623 | 162.579<br>162.579 | 0.9310<br>0.9310 | 0.19%<br>0.19% |
| 150<br>150 | 1<br>1 | 275.817<br>275.817 | 256.594<br>256.594 | 0.9303<br>0.9303 | 0.43%<br>0.43% |
| 99.03<br>99.03 | 0.5<br>0.5 | 174.623<br>174.623 | 162.455<br>162.455 | 0.9303<br>0.9303 | 0.17%<br>0.17% |
| 99.03<br>99.03 | 2<br>2 | 174.623<br>174.623 | 162.637<br>162.637 | 0.9314<br>0.9314 | 0.18%<br>0.18% |

**Symbols before Eq. (C5-E18).**

**式（C5-E18）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Lambda_i$ — Peak factor of case i (dimensionless)<br>$\Lambda_i$ — 工况 i 的峰值因子（无量纲） | $\bar p_{a,i}$ — Full-sensor wall pressure of case i (Pa)<br>$\bar p_{a,i}$ — 工况 i 的全传感区壁面压力（Pa） |
| $p_{H,i}$ — Hugoniot pressure of case i from Eq. (C5-E04) (Pa)<br>$p_{H,i}$ — 工况 i 由式（C5-E04）得到的 Hugoniot 压力（Pa） | $i$ — Case index over the five converged cases (dimensionless)<br>$i$ — 五个收敛工况的序号（无量纲） |
| $\sigma_\Lambda$ — Relative spread of the peak factor (dimensionless)<br>$\sigma_\Lambda$ — 峰值因子的相对离散度（无量纲） | $\overline{\Lambda}$ — Mean peak factor over the cases (dimensionless)<br>$\overline{\Lambda}$ — 各工况峰值因子的平均（无量纲） |
| $g(\tau)$ — Common normalized pressure history (dimensionless)<br>$g(\tau)$ — 共同的无量纲压力历程（无量纲） | $\tau$ — Dimensionless time $c_{0}$ t / a (dimensionless)<br>$\tau$ — 无量纲时间 $c_{0}$ t / a（无量纲） |

**Conventions and conditions.** Cases vary U from 50 to 150 m s⁻¹ and a from 0.5 to 2 μm; The ranges are scenario choices, not confidence intervals; Collapse is checked only up to τ = 0.49.

**约定与条件。** 各工况使 U 在 50 至 150 m s⁻¹、a 在 0.5 至 2 μm 之间变化；这些范围是情景选择，并非置信区间；仅检验 τ ≤ 0.49 内的坍缩。

(C5-E18) · Scaling collapse and spread of the finite-area factor / 有限面积因子的尺度坍缩与离散度


$$
\begin{aligned}\Lambda_i&=\frac{\max_t\,\bar p_{a,i}(t)}{p_{H,i}},\qquad i\in\{\text{five cases}\},\\ \sigma_\Lambda&=\frac{\max_i\Lambda_i-\min_i\Lambda_i}{\overline{\Lambda}},\qquad \frac{\bar p_{a}(\tau)}{p_H}=g(\tau)\ \text{for all cases, }\tau\le0.49.\end{aligned}
$$


![When pressure is scaled by p_H and time by a/c_0, all five cases fall on one history.](../assets/figures/c5-e18.svg)

When pressure is scaled by p\_H and time by a/c\_0, all five cases fall on one history.

当压力以 p\_H 无量纲化、时间以 a/c\_0 无量纲化后，五个工况落在同一历程上。

The five peak factors lie between 0.9303 and 0.9314. Their spread is 0.12% of the mean. The scaled histories coincide for $\tau\le0.49$, the longest time covered by the band runs.

五个峰值因子介于 0.9303 与 0.9314 之间，离散度为平均值的 0.12%。无量纲历程在 $\tau\le0.49$ 内重合，这是加密带运行覆盖的最长时间。

Step 22 — Read the gap with the scale estimate. The peak occurs at 0.029 ns, so $\tau_{\mathrm{pk}}=0.0472$. Eq. (C5-E07) then gives $f_{\mathrm{rel}}=0.0921$ and a full-release value of $(1-\tau_{\mathrm{pk}})^2=0.908$. The computed factor 0.931 lies between 0.908 and 1. So the annulus keeps about a quarter of its excess pressure. The gap exists because the free side acts from the first instant. It is not a mesh effect, since the band refinement changes the peak by only 0.02% at the finest level.

步骤 22——用尺度估计解读该差值。峰值出现在 0.029 ns，故 $\tau_{\mathrm{pk}}=0.0472$。式（C5-E07）给出 $f_{\mathrm{rel}}=0.0921$，完全释放值为 $(1-\tau_{\mathrm{pk}})^2=0.908$。算得的因子 0.931 介于 0.908 与 1 之间，说明环带保留了约四分之一的超压。该差值的出现，是因为自由侧边自首次接触起就在起作用。它不是网格效应，因为加密带在最细一级仅使峰值改变 0.02%。

Step 23 — State the delivered relations. Eq. (C5-E19) collects them. The centre disk follows the Hugoniot pressure. The full sensor follows $0.931\,p_H$. The high-pressure interval lasts about $a/c_0$, which is 0.61 ns for $a=1$ μm. The pressure map multiplies the Chapter 3 ceiling $Z_0U$ by the factor $U_s/c_0=1.0856$.

步骤 23——陈述交付的关系。式（C5-E19）汇总如下。中心圆盘遵循 Hugoniot 压力，全传感区遵循 $0.931\,p_H$。高压阶段持续约 $a/c_0$，对 $a=1$ μm 为 0.61 ns。压力映射把第三章的上限 $Z_0U$ 乘以因子 $U_s/c_0=1.0856$。

**Symbols before Eq. (C5-E19).**

**式（C5-E19）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\bar p_{a/2}$ — Centre-disk wall pressure, r ≤ a/2 (Pa)<br>$\bar p_{a/2}$ — 中心圆盘壁面压力，r ≤ a/2（Pa） | $\bar p_a$ — Full-sensor wall pressure, r ≤ a (Pa)<br>$\bar p_a$ — 全传感区壁面压力，r ≤ a（Pa） |
| $p_H(U)$ — Hugoniot pressure at the given speed (Pa)<br>$p_H(U)$ — 给定速度下的 Hugoniot 压力（Pa） | $\Lambda$ — Finite-area peak factor 0.931 (dimensionless)<br>$\Lambda$ — 有限面积峰值因子 0.931（无量纲） |
| $t_{\mathrm{hi}}$ — Duration of the high-pressure interval (s)<br>$t_{\mathrm{hi}}$ — 高压阶段的持续时间（s） | $a$ — Jet radius (m)<br>$a$ — 射流半径（m） |
| $c_0$ — Reference sound speed (m s⁻¹)<br>$c_0$ — 参考声速（m s⁻¹） | $Z_0$ — Reference acoustic impedance (Pa s m⁻¹)<br>$Z_0$ — 参考声阻抗（Pa s m⁻¹） |
| $U_s$ — Shock speed relative to the incoming liquid (m s⁻¹)<br>$U_s$ — 相对入射液体的激波速度（m s⁻¹） | $p_j$ — Reference pressure (Pa)<br>$p_j$ — 参考压力（Pa） |

**Conventions and conditions.** Valid for liquid-only, barotropic, rigid flat wall, first arrival; U/$c_{0}$ between 0.031 and 0.092; Wall tension after τ ≈ 1 is not physical here because cavitation is not modelled.

**约定与条件。** 适用于纯液体、正压、刚性平壁、首次到达；U/$c_{0}$ 在 0.031 至 0.092 之间；τ ≈ 1 之后的壁面拉应力在此不具物理意义，因为未建立空化模型。

(C5-E19) · Delivered rigid-wall relations and link to the Chapter 3 ceiling / 交付的刚性壁面关系及其与第三章上限的联系


$$
\begin{aligned}\max_t\bar p_{a/2}&=p_H(U)\,(1\pm0.0043),\qquad \max_t\bar p_{a}=\Lambda\,p_H(U),\quad \Lambda=0.931,\\ t_{\mathrm{hi}}&\simeq\frac{a}{c_0},\qquad \frac{p_H-p_j}{Z_0U}=\frac{U_s}{c_0}=1.0856.\end{aligned}
$$


![The result is a speed-to-pressure map; whether a given source produces that speed belongs to Chapters 1 to 3.](../assets/figures/c5-e19.svg)

The result is a speed-to-pressure map; whether a given source produces that speed belongs to Chapters 1 to 3.

所得结果是“速度到压力”的映射；某一能源能否产生该速度属于第一至第三章。

State the limits. The result holds for a liquid-only barotropic column, a rigid flat wall and the first arrival. The tested ranges are $0.031\le M\le0.092$ and $0.5\le a\le2$ μm. After $\tau\approx1$ the computed wall pressure turns negative in absolute value, which is not physical here because cavitation is not modelled. A gas cushion, an elastic wall and the bubble-to-jet physics upstream are not covered.

说明局限。该结果适用于纯液体正压液柱、刚性平壁与首次到达。检验范围为 $0.031\le M\le0.092$ 与 $0.5\le a\le2$ μm。$\tau\approx1$ 之后，算得的壁面压力绝对值变为负，这在此不具物理意义，因为未建立空化模型。气垫、弹性壁面以及上游的气泡到射流物理均未涵盖。

## 9. Oral questions

## 9. 口头问题

### Which wall pressure does this chain establish for a prescribed 99.03 m/s jet, and what stays conditional?

### 该链条对给定的 99.03 m/s 射流确立了何种壁面压力？哪些仍是有条件的？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C5-E20).**

**式（C5-E20）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{wall}}$ — Mean wall pressure over the stated disk (Pa)<br>$p_{\mathrm{wall}}$ — 所述圆盘上的平均壁面压力（Pa） | $p_j$ — Reference pressure (Pa)<br>$p_j$ — 参考压力（Pa） |
| $U_s/c_0$ — Nonlinear factor 1.0856 (dimensionless)<br>$U_s/c_0$ — 非线性因子 1.0856（无量纲） | $Z_0$ — Reference acoustic impedance (Pa s m⁻¹)<br>$Z_0$ — 参考声阻抗（Pa s m⁻¹） |
| $U$ — Impact speed (m s⁻¹)<br>$U$ — 撞击速度（m s⁻¹） | $\Lambda$ — Finite-area peak factor (dimensionless)<br>$\Lambda$ — 有限面积峰值因子（无量纲） |
| $p_H$ — Hugoniot pressure (Pa)<br>$p_H$ — Hugoniot 压力（Pa） | $E_{\mathrm{av}}$ — Kinetic energy available to the jet (Chapter 3) (J)<br>$E_{\mathrm{av}}$ — 可用于射流的动能（第三章）（J） |
| $m_j$ — Jet mass (Chapter 3) (kg)<br>$m_j$ — 射流质量（第三章）（kg） |  |

**Conventions and conditions.** The speed bound is conditional on how much energy reaches the jet; The pressure map is conditional on U; Together they form one conditional chain.

**约定与条件。** 速度上界取决于有多少能量到达射流；压力映射取决于 U；二者合成一条有条件的链。

(C5-E20) · Reference formulas: speed bound and pressure map together / 参考公式：速度上界与压力映射合并


$$
\begin{aligned}p_{\mathrm{wall}}&\le p_j+\frac{U_s}{c_0}\,Z_0\,U\quad(\text{centre disk}),\qquad p_{\mathrm{wall}}\approx\Lambda\,p_H\quad(\text{full sensor}),\\ U&\le\sqrt{\frac{2E_{\mathrm{av}}}{m_j}}\quad(\text{Chapter 3 energy bound}).\end{aligned}
$$


![A speed bound and a pressure map are two separate claims joined only by the prescribed speed.](../assets/figures/c5-e20.svg)

A speed bound and a pressure map are two separate claims joined only by the prescribed speed.

速度上界与压力映射是两个独立结论，仅通过给定速度相连。

Start from the energy bound. Chapter 3 limits the speed by the energy available to the finite jet mass. This chapter takes the speed as given and maps it to pressure. At 99.027 m s⁻¹ the linear ceiling is 160.765 MPa excess. The nonlinear factor 1.0856 gives 174.52 MPa excess, which is the Hugoniot level. Over the full sensor the peak is 0.931 of the absolute Hugoniot pressure, 162.6 MPa. These numbers hold for the prescribed speed. They say nothing on whether a source delivers that speed.

从能量上界出发。第三章用有限射流质量可得的能量来限制速度。本章把速度当作给定值并映射为压力。在 99.027 m s⁻¹ 时，线性上限为 160.765 MPa 超压。非线性因子 1.0856 给出 174.52 MPa 超压，即 Hugoniot 水平。在整个传感区上，峰值为绝对 Hugoniot 压力的 0.931 倍，即 162.6 MPa。这些数值对应于给定速度，并不说明能源能否提供该速度。

A bound and a map are different claims. The bound says a speed cannot be exceeded. The map says what pressure follows from a speed under stated assumptions. Neither is a prediction of the pressure a given laser pulse produces. That needs the upstream chain of Chapters 1 to 3 and a measurement.

上界与映射是不同的结论。上界说明速度不可超过某值。映射说明在所述假设下某一速度对应何种压力。二者都不是对给定激光脉冲所产生压力的预测。那需要第一至第三章的上游链条以及实测。

#### Review criteria

#### 审阅标准

* Separates the Chapter 3 speed bound from the speed-to-pressure map and states that the speed is prescribed.

  区分第三章的速度上界与速度到压力的映射，并说明速度为给定值。
* Quotes the linear ceiling, the Hugoniot level and the full-sensor factor with their reference values.

  引用线性上限、Hugoniot 水平和全传感区因子，并注明各自的参照值。
* Names the conditions: liquid only, rigid flat wall, barotropic law, first arrival and the tested ranges.

  指出条件：纯液体、刚性平壁、正压律、首次到达以及检验范围。

### Is the 6.9% gap between the full-sensor peak and the Hugoniot pressure a mesh artifact or edge release? Which evidence decides?

### 全传感区峰值与 Hugoniot 压力之间 6.9% 的差值是网格伪影还是边缘释放？哪些证据能决定？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C5-E21).**

**式（C5-E21）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Lambda$ — Finite-area peak factor (dimensionless)<br>$\Lambda$ — 有限面积峰值因子（无量纲） | $\bar P_{\max}$ — Peak full-sensor pressure (Pa)<br>$\bar P_{\max}$ — 全传感区压力峰值（Pa） |
| $p_H$ — Hugoniot pressure (Pa)<br>$p_H$ — Hugoniot 压力（Pa） | $f_{\mathrm{rel}}$ — Released area fraction from Eq. (C5-E07) (dimensionless)<br>$f_{\mathrm{rel}}$ — 来自式（C5-E07）的已释放面积分数（无量纲） |
| $\kappa$ — Fraction of the excess lost inside the released annulus (dimensionless)<br>$\kappa$ — 释放环带内损失的超压比例（无量纲） | $\tau_{\mathrm{pk}}$ — Dimensionless time of the peak (dimensionless)<br>$\tau_{\mathrm{pk}}$ — 峰值出现的无量纲时间（无量纲） |
| $t_{\mathrm{pk}}$ — Time of the peak, 0.029 ns (s)<br>$t_{\mathrm{pk}}$ — 峰值时刻，0.029 ns（s） | $c_0$ — Reference sound speed (m s⁻¹)<br>$c_0$ — 参考声速（m s⁻¹） |
| $a$ — Jet radius (m)<br>$a$ — 射流半径（m） |  |

**Conventions and conditions.** κ = 1 means the annulus keeps no excess pressure; Computed κ lies between 0 and 1; The estimate explains the sign and size of the gap, not its digits.

**约定与条件。** κ = 1 表示环带不保留超压；算得的 κ 介于 0 与 1 之间；该估计解释差值的符号与大小，而非具体数字。

(C5-E21) · Reference formulas: edge-release explanation of the finite-area factor / 参考公式：用边缘释放解释有限面积因子


$$
\begin{aligned}\Lambda&=\frac{\bar P_{\max}}{p_H}\approx 1-\kappa\,f_{\mathrm{rel}}(\tau_{\mathrm{pk}}),\quad f_{\mathrm{rel}}(\tau)=1-(1-\tau)^{2},\\ \tau_{\mathrm{pk}}&=\frac{c_0t_{\mathrm{pk}}}{a},\qquad t_{\mathrm{pk}}=0.029\ \mathrm{ns},\quad \kappa=\frac{1-\Lambda}{f_{\mathrm{rel}}(\tau_{\mathrm{pk}})}.\end{aligned}
$$


![A released annulus that keeps part of its excess pressure accounts for a peak factor between 0.908 and 1.](../assets/figures/c5-e21.svg)

A released annulus that keeps part of its excess pressure accounts for a peak factor between 0.908 and 1.

释放环带保留部分超压，可解释峰值因子介于 0.908 与 1 之间。

The free side of the jet acts from first contact. A release front from the edge reaches the radius $a(1-\tau)$ at dimensionless time $\tau$. At the peak time 0.029 ns, $\tau=0.0472$ and the released annulus holds 9.2% of the disk area. Full release of that annulus gives $0.908\,p_H$. The computed factor 0.931 requires the annulus to keep about a quarter of its excess pressure. The sign and size agree with the scale estimate.

射流的自由侧边自首次接触起就在起作用。边缘的释放前沿在无量纲时间 $\tau$ 到达半径 $a(1-\tau)$。在峰值时刻 0.029 ns，$\tau=0.0472$，已释放环带占圆盘面积的 9.2%。该环带完全释放时给出 $0.908\,p_H$。算得的因子 0.931 要求环带保留约四分之一的超压。符号与大小与尺度估计一致。

Evidence against a mesh artifact: the band refinement changes the peak by 1.98%, 0.44% and 0.02%. The factor is the same within 0.12% for five speeds and radii. The centre disk, which the release has not reached, stays within 0.43% of $p_H$. A mesh artifact would not be confined to the full-area average and would not collapse with $\tau$.

反对网格伪影的证据：加密带使峰值依次改变 1.98%、0.44% 和 0.02%；五组速度与半径下该因子的偏差在 0.12% 以内；释放尚未到达的中心圆盘保持在 $p_H$ 的 0.43% 以内。网格伪影不会只出现在全面积平均上，也不会随 $\tau$ 坍缩。

#### Review criteria

#### 审阅标准

* Explains the free side acting from first contact and the released annulus with the area fraction of Eq. (C5-E07).

  解释自由侧边自首次接触起的作用，并用式（C5-E07）的面积分数说明已释放环带。
* Uses the band-refinement sequence, the centre disk and the five-case collapse as separate pieces of evidence.

  把加密带序列、中心圆盘和五工况坍缩作为各自独立的证据。
* States that the scale estimate fixes sign and size, not the digits, and that 0.931 comes from the simulation.

  说明尺度估计只确定符号与大小而非数字，0.931 来自模拟。

### What does the 0.034% solver agreement establish, and which uses of the 162.6 MPa result stay unsupported?

### 0.034% 的求解器一致性确立了什么？162.6 MPa 的哪些用途仍无依据？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C5-E22).**

**式（C5-E22）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $M$ — Impact Mach number (dimensionless)<br>$M$ — 撞击马赫数（无量纲） | $a$ — Jet radius (m)<br>$a$ — 射流半径（m） |
| $\tau$ — Dimensionless time $c_{0}$ t / a (dimensionless)<br>$\tau$ — 无量纲时间 $c_{0}$ t / a（无量纲） | $\delta_2$ — Relative L2 difference between the two solvers (dimensionless)<br>$\delta_2$ — 两个求解器间的相对 L2 差（无量纲） |
| $\mu\mathrm m$ — Micrometre, 10⁻⁶ m (m)<br>$\mu\mathrm m$ — 微米，10⁻⁶ m（m） |  |

**Conventions and conditions.** Gas cushion, splash, elastic wall and cavitation are outside the model; Pressure after τ ≈ 1 includes negative absolute values and is not physical here; Agreement of two solvers of one model is verification, not validation.

**约定与条件。** 气垫、飞溅、弹性壁面与空化均在模型之外；τ ≈ 1 之后的压力含负的绝对值，在此不具物理意义；同一模型的两个求解器一致属于核验，而非验证。

(C5-E22) · Reference formulas: validity range and limits of the verification / 参考公式：适用范围与核验的局限


$$
\begin{aligned}\text{valid for}\quad &M\in[0.031,\,0.092],\ \ a\in[0.5,\,2]\ \mu\mathrm m,\ \ \tau\le 1,\\ &\text{liquid only, rigid flat wall, barotropic law of Eq. (C5-E01)},\\ \delta_2&=0.034\%\ \Longrightarrow\ \text{implementation agrees;}\\ &\text{the model is not tested against experiment.}\end{aligned}
$$


![The verification covers one model over a stated range; it does not reach beyond that range.](../assets/figures/c5-e22.svg)

The verification covers one model over a stated range; it does not reach beyond that range.

核验只覆盖所述范围内的单一模型，不超出该范围。

The relative L2 difference of 0.034% between the C++ and COMSOL histories shows that two implementations of one model agree. Both use the same stiffened-gas law, inputs, wall and inflow. A shared modelling error would appear in both. So the agreement cannot validate the law, the neglect of gas or the rigid wall. It supports a statement about numerics only.

C++ 与 COMSOL 历程之间 0.034% 的相对 L2 差表明同一模型的两个实现是一致的。二者使用相同的刚化气体律、输入、壁面和入流。共同的建模误差会同时出现在两者之中。因此这一致性不能验证该定律、对气相的忽略或刚性壁面，它只支持关于数值的陈述。

The 162.6 MPa result is supported as a numerical result for a liquid-only column at $0.031\le M\le0.092$ and $0.5\le a\le2$ μm during the first arrival. It is not supported as a prediction of a measured wall pressure, as a value after $\tau\approx1$, or as a value with a gas cushion or an elastic wall. Physical validation: Not established. Missing: a measured wall pressure for a real jet.

162.6 MPa 作为数值结果成立，条件是纯液体液柱、$0.031\le M\le0.092$、$0.5\le a\le2$ μm 且处于首次到达阶段。它不支持作为实测壁面压力的预测，不支持 $\tau\approx1$ 之后的数值，也不支持含气垫或弹性壁面的情形。物理验证：尚未确立。缺少：真实射流的壁面压力实测。

#### Review criteria

#### 审阅标准

* Distinguishes verification of an implementation from validation of the model against experiment.

  区分对实现的核验与对模型的实验验证。
* Lists the supported range: liquid only, rigid flat wall, tested Mach and radius ranges, first arrival.

  列出支持的范围：纯液体、刚性平壁、检验过的马赫数与半径范围、首次到达。
* Names unsupported uses: a measured pressure, times after $\tau\approx1$, a gas cushion and an elastic wall.

  指出无依据的用途：实测压力、$\tau\approx1$ 之后的时间、气垫与弹性壁面。