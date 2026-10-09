# Chapter 2: From laser absorption to a finite PFC bubble

# 第 2 章：从激光吸收到有限 PFC 气泡

## 2. From laser absorption to a finite PFC bubble

## 2. 从激光吸收到有限 PFC 气泡

The objective is to determine what pressure history one laser-heated PFC inclusion can supply to the carrier liquid. Chapter 1 supplied the mechanical response to a prescribed bubble pressure; this chapter supplies the optical, thermal, activation, mass, and energy equations needed to calculate that pressure. The useful jet is usually predominantly carrier liquid. PFC density belongs to the core inventory; carrier density belongs to the surrounding inertia. A lower activation threshold is a possible benefit, but it does not establish a larger emitted momentum or a more repeatable transfer.

本章目标是确定一个激光加热的 PFC 夹杂能向载液提供怎样的压力历程。第一章给出了已知气泡压力下的力学响应；本章补充计算该压力所需的光学、热学、激活、质量和能量方程。有用射流通常主要由载液组成。PFC 密度用于核心库存，载液密度用于周围惯性。较低激活阈值可能有益，却不能据此证明喷出动量更大或转印更可重复。

**System and conventions.** Start with a spherical, initially liquid PFC core in an aqueous carrier, initially at temperature $T_0$ (K) and carrier pressure $p_c$ (Pa). The beam travels in the positive depth direction $z$ (m); transverse distance from its axis is $r$ (m). Time $t=0$ (s) precedes the pulse. Optical intensity entering an absorber is prescribed, the initial temperature field is prescribed, the sphere center has zero radial heat flux by symmetry, and the outer thermal boundary is a stated reservoir or an explicitly resolved carrier. At each material contact, enforce flux continuity and the declared contact law. All thermodynamic pressures are absolute. At a liquid–vapor interface, the dimensionless unit normal $\boldsymbol n$ points from liquid into vapor; evaporation flux is positive in this direction. For a bubble inside liquid this normal points inward, opposite the dimensionless outward radial unit vector $\boldsymbol e_r$.

**系统与约定。** 从水性载液中的球形液态 PFC 核心开始，初始温度为 $T_0$（K），载液压力为 $p_c$（Pa）。光束沿正深度方向 $z$（m）传播；离光轴的横向距离为 $r$（m）。$t=0$（s）位于脉冲之前。给定进入吸收体的光强与初始温度场，球心因对称性满足零径向热通量，外热边界设为明确的恒温环境或显式解析的载液。材料接触处满足热通量连续及所声明的接触定律。所有热力学压力均为绝对压力。液–汽界面的无量纲单位法向量 $\boldsymbol n$ 从液体指向蒸汽；沿此方向的蒸发通量为正。对于液体内部的气泡，此法向指向内侧，与无量纲向外径向单位向量 $\boldsymbol e_r$ 相反。

**Assumptions are introduced in stages.** The first optical control neglects scattering and nonlinear absorption. The pre-phase heat equation assumes negligible pressure-work and viscous heating within each nearly incompressible phase. The nucleation calculation adopts a locally isothermal capillarity model with a nucleus much smaller than its available liquid core. The final uniform-bubble closure assumes a common bulk temperature and uses an ideal mixture only when dilute. These are different approximations, not a single universally valid PFC model. A micron-scale teaching core is not a nanodroplet.

**逐步引入假设。** 首个光学参照忽略散射和非线性吸收。相变前的热方程假设每个近不可压缩相内的压力功与黏性生热可忽略。成核计算采用局部等温毛细模型，且汽核远小于可用液核。最后的均匀气泡闭合假设共同的体相温度，仅在稀薄条件下使用理想混合物。这些是不同近似，不能合并为普适 PFC 模型。微米级教学核心也不是纳米液滴。

| Symbol<br>符号 | Physical meaning<br>物理意义 | SI units<br>SI 单位 | Role and convention<br>作用与约定 |
| --- | --- | --- | --- |
| $F$ | Laser fluence<br>激光能量面密度 | J m⁻² | Pulse energy incident per unit area; it is a time integral, not an instantaneous irradiance.<br>单位面积接收的脉冲能量；是时间积分，而非瞬时辐照度。 |
| $I$ | Laser irradiance<br>激光辐照度 | W m⁻² | Instantaneous optical power per unit area; integrating it over the pulse gives fluence.<br>单位面积上的瞬时光功率；对脉冲历时积分得到能量面密度。 |
| $E_L$ | Incident laser-pulse energy<br>入射激光脉冲能量 | J | Total incident optical budget before interception, reflection and absorption losses.<br>截获、反射及吸收损失之前的总入射光能预算。 |
| $E_{\mathrm{abs}}$ | Absorbed optical energy<br>吸收光能 | J | Energy actually deposited in the defined absorber; not necessarily heat delivered to PFC.<br>实际沉积在指定吸收体中的能量；不一定等于传给 PFC 的热量。 |
| $T$ | Thermodynamic temperature<br>热力学温度 | K | Local state in the heat/phase balance; phase equilibrium and rate laws require its history.<br>热／相平衡中的局部状态；相平衡与速率规律需要其时间历程。 |
| $\rho$ | Local material mass density<br>局部材料质量密度 | kg m⁻³ | The material or phase must be specified; PFC heating density and carrier inertia density differ.<br>必须指定材料或相；PFC 加热密度与载液惯性密度不同。 |
| $c_p$ | Specific heat capacity at constant pressure<br>定压比热容 | J kg⁻¹ K⁻¹ | Sensible-heat capacity per mass; constant-property examples are declared approximations.<br>单位质量的显热容量；恒物性例题是明确声明的近似。 |
| $k$ | Thermal conductivity<br>导热系数 | W m⁻¹ K⁻¹ | Relates temperature gradient to conductive heat flux, not to fluid permeability.<br>关联温度梯度与导热热流，不是流体渗透率。 |
| $\alpha$ | Thermal diffusivity<br>热扩散率 | m² s⁻¹ | Conductivity divided by volumetric heat capacity; determines thermal communication time.<br>导热系数除以体积热容量；决定热传播时间。 |
| $a_0$ | Initial liquid-PFC core radius<br>初始液态 PFC 核半径 | m | Defines the initial finite liquid inventory; not the growing vapor-cavity radius.<br>确定初始有限液体存量；并非增长中的蒸气腔体半径。 |
| $R$ | Subsequent bubble radius<br>后续气泡半径 | m | Geometric cavity coordinate after activation; by itself it does not determine phase mass.<br>激活后的几何空腔坐标；仅凭它无法确定各相质量。 |
| $V_b$ | Bubble volume<br>气泡体积 | m³ | Volume enclosing the vapor/gas mixture; requires mass, temperature and pressure closure.<br>蒸气／气体混合物所在体积；需要质量、温度与压力闭合。 |
| $m_l$ | Remaining liquid-PFC mass<br>剩余液态 PFC 质量 | kg | Liquid reservoir remaining after signed interfacial phase transfer.<br>带符号界面相变传递之后剩余的液体储量。 |
| $m_v$ | PFC vapor mass<br>PFC 蒸气质量 | kg | Vapor inventory, constrained by the original core and any stated transport sources.<br>蒸气存量，受原始液核及所声明传输源约束。 |
| $j_s$ | Signed species phase-transfer mass flux<br>带符号组分相变质量通量 | kg m⁻² s⁻¹ | Mass crossing unit interfacial area per time; the chosen evaporation direction fixes its sign.<br>单位界面面积每单位时间穿过的质量；所选蒸发方向确定其符号。 |
| $\sigma_{pc}$ | PFC–carrier interfacial tension<br>PFC—载液界面张力 | N m⁻¹ | Acts at the original liquid-droplet boundary; not the vapor–PFC nucleation tension.<br>作用于原始液滴边界；不是蒸气—PFC 成核张力。 |
| $\sigma_{vp}$ | Vapor–liquid-PFC interfacial tension<br>蒸气—液态 PFC 界面张力 | N m⁻¹ | Belongs to the vapor nucleus inside PFC and its capillary/nucleation cost.<br>属于 PFC 内部蒸气核及其毛细／成核代价。 |
| $U_b$ | Bubble internal energy<br>气泡内能 | J | Thermodynamic energy of the cavity contents; changes by heat, phase enthalpy and boundary work.<br>腔内物质的热力学能量；由热、相变焓与边界功改变。 |
| $h_s$ | Transported species specific enthalpy<br>输运组分比焓 | J kg⁻¹ | Enthalpy carried with unit transferred species mass; phase and state must be specified.<br>单位传递组分质量携带的焓；必须指定相与状态。 |
| $M_s$ | Species molar mass<br>组分摩尔质量 | kg mol⁻¹ | Converts species mass to amount of substance in the chosen equation of state.<br>在所选状态方程中，将组分质量换算为物质的量。 |
| $L_{v,s}$ | Species-specific latent heat of vaporization<br>组分汽化比潜热 | J kg⁻¹ | Phase-change energy per converted species mass; the interface state and approximation are specified.<br>单位转化组分质量的相变能量；需指定界面状态与近似。 |
| $R_u$ | Universal molar gas constant<br>通用摩尔气体常数 | J mol⁻¹ K⁻¹ | Used with amount of substance, not silently with mass-specific variables.<br>与物质的量共同使用，不能默默代入质量比形式。 |

A fair PFC comparison uses a PFC-free aqueous droplet with matched outer geometry, absorber location, absorbed energy, initial temperature, pressure, outlet, and target load path. Changing absorber concentration or spot size simultaneously cannot isolate a material benefit. Compare activation probability, emitted mass and velocity, useful impulse, intact-transfer yield, and reset. A persistently vapor-filled inclusion can activate readily while cushioning the subsequent collapse.

公平的 PFC 对比应使用不含 PFC 的水性液滴，并匹配外部几何、吸收体位置、吸收能量、初始温度、压力、出口及目标受力路径。同时改变吸收体浓度或光斑大小，就不能分离材料优势。应比较激活概率、喷出质量与速度、有用冲量、完整转印成功率及复位。长期充满蒸汽的夹杂可能易于激活，却缓冲后续塌缩。

## 2.1 Count incident and absorbed energy correctly

## 2.1 正确计算入射与吸收能量

**Step 1 — prescribe a Gaussian fluence.** Fluence is the time integral of irradiance. Specify the transverse profile first, with the beam radius defined by the $e^{-2}$ level. This convention must accompany a quoted spot size.

**步骤 1——给定高斯能量密度。** 能量密度是辐照度的时间积分。先给定横向分布，将光束半径定义为 $e^{-2}$ 水平对应的半径。引用光斑尺寸时必须同时说明该约定。

**Symbols before Eq. (C2-E01).**

**式（C2-E01）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $F(r)$ is incident fluence at radial coordinate $r\ge0$ (J m⁻²)<br>$F(r)$ 为径向坐标 $r\ge0$ 处的入射能量密度（J m⁻²） | $F_0>0$ is on-axis fluence (J m⁻²)<br>$F_0>0$ 为轴上能量密度（J m⁻²） |
| $w>0$ is the transverse $e^{-2}$ beam radius (m)<br>$w>0$ 为横向 $e^{-2}$ 光束半径（m） | $r$ — Transverse distance from the laser-beam axis (m)<br>$r$ — 到激光光束轴线的横向距离（m） |

**Conventions and conditions.** $\exp$ is the natural exponential.

**约定与条件。** $\exp$ 为自然指数函数。

(C2-E01) · Prescribed optical profile / 给定的光学分布


$$
F(r)=F_0\exp(-2r^2/w^2)
$$


![Fluence varies across the beam; the quoted radius fixes its definition.](../assets/figures/c2-e01.svg)

Fluence varies across the beam; the quoted radius fixes its definition.

能量密度沿光束横向变化；所给半径明确其定义。

**Step 2 — integrate over the illuminated plane.** Annuli have area $2\pi r\,dr$. Set the dimensionless integration variable $x=2r^2/w^2$, so $dx=4r\,dr/w^2$ and both limits remain zero and infinity. The positive exponential is integrable; the upper endpoint vanishes.

**步骤 2——在照射平面上积分。** 环带面积为 $2\pi r\,dr$。令无量纲积分变量 $x=2r^2/w^2$，于是 $dx=4r\,dr/w^2$，上下限仍为零与无穷。正的指数函数可积，且上端点项趋于零。

**Symbols before Eq. (C2-E02).**

**式（C2-E02）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $E_L$ is total incident pulse energy (J)<br>$E_L$ 为总入射脉冲能量（J） | $F_0$ is on-axis fluence (J m⁻²)<br>$F_0$ 为轴上能量密度（J m⁻²） |
| $w>0$ — Transverse Gaussian beam radius at the e⁻² level (m)<br>$w>0$ — 横向高斯光束 e⁻² 半径（m） | $r\ge0$ — Transverse distance from the laser-beam axis (m)<br>$r\ge0$ — 到激光光束轴线的横向距离（m） |
| $x=2r^2/w^2$ is a dimensionless substitution variable<br>$x=2r^2/w^2$ 为无量纲换元变量 | $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** $e^x$ is the exponential; $\int$ and brackets denote integration and endpoint evaluation.

**约定与条件。** $e^x$ 为指数函数；$\int$ 与方括号表示积分及端点求值。

(C2-E02) · Exact integral of the prescribed profile / 给定分布的精确积分


$$
\begin{aligned}E_L&=2\pi F_0\int_0^\infty r e^{-2r^2/w^2}\,dr\\&=\frac{\pi w^2F_0}{2}\int_0^\infty e^{-x}\,dx\\&=\frac{\pi w^2F_0}{2}[-e^{-x}]_0^\infty=\frac{\pi w^2F_0}{2}.\end{aligned}
$$


![The Gaussian energy follows from summing annular contributions.](../assets/figures/c2-e02.svg)

The Gaussian energy follows from summing annular contributions.

高斯光束能量来自环带贡献之和。

**Step 3 — calculate interception rather than assuming all light hits the actuator.** For a centered circular absorber aperture of radius $b_a$ (m), terminate the same integral at that radius and divide by total beam energy. An off-axis droplet or irregular layer needs its actual area integral.

**步骤 3——计算截获比例，不假定全部光能照到驱动器。** 对半径为 $b_a$（m）的同轴圆形吸收体窗口，将同一积分截断于该半径，再除以光束总能量。偏轴液滴或不规则层需要对其实际面积积分。

**Symbols before Eq. (C2-E03).**

**式（C2-E03）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $f_{\mathrm{geo}}$ is intercepted energy fraction (dimensionless), with label geo meaning geometry<br>$f_{\mathrm{geo}}$ 为截获能量比例（无量纲），geo 下标表示几何 | $b_a\ge0$ is centered absorber-aperture radius (m)<br>$b_a\ge0$ 为同轴吸收体窗口半径（m） |
| $F(r)$ is Gaussian fluence (J m⁻²)<br>$F(r)$ 为高斯能量密度（J m⁻²） | $r$ is transverse integration distance (m)<br>$r$ 为横向积分距离（m） |
| $E_L>0$ is total pulse energy (J)<br>$E_L>0$ 为总脉冲能量（J） | $w>0$ is beam radius (m)<br>$w>0$ 为光束半径（m） |
| $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |  |

**Conventions and conditions.** $\exp$ and $\int$ denote exponential and integration.

**约定与条件。** $\exp$ 和 $\int$ 表示指数函数与积分。

(C2-E03) · Derived interception fraction / 推导得到的截获比例


$$
f_{\mathrm{geo}}=\frac{\int_0^{b_a}F(r)2\pi r\,dr}{E_L}=1-\exp(-2b_a^2/w^2),\qquad 0\le f_{\mathrm{geo}}\le1
$$


![The aperture removes the outer annuli from the useful incident energy.](../assets/figures/c2-e03.svg)

The aperture removes the outer annuli from the useful incident energy.

窗口使外侧环带不再计入有用入射能量。

**Step 4 — restore time.** Normalize the temporal pulse shape so that its integral is one. A rectangular pulse has a shape equal to the reciprocal pulse duration while the pulse is on. Thus a shorter pulse raises irradiance at the same fluence; it does not increase incident energy.

**步骤 4——恢复时间变量。** 将时间脉冲形状归一化，使其积分为一。矩形脉冲在开启时的形状值等于脉冲时长的倒数。因此，在能量密度相同时，缩短脉冲会提高辐照度，却不会提高入射能量。

**Symbols before Eq. (C2-E04).**

**式（C2-E04）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $f(t)\ge0$ is normalized pulse shape (s⁻¹)<br>$f(t)\ge0$ 为归一化脉冲形状（s⁻¹） | $t$ is time (s)<br>$t$ 为时间（s） |
| $I(r,t)$ is irradiance (W m⁻²)<br>$I(r,t)$ 为辐照度（W m⁻²） | $F(r)$ — Local laser fluence (J m⁻²)<br>$F(r)$ — 局部激光能量面密度（J m⁻²） |
| $F_0$ — On-axis laser fluence (J m⁻²)<br>$F_0$ — 轴上激光能量面密度（J m⁻²） | $r$ is transverse distance (m)<br>$r$ 为横向距离（m） |
| $I_{\mathrm{peak}}$ is central peak irradiance (W m⁻²)<br>$I_{\mathrm{peak}}$ 为中心峰值辐照度（W m⁻²） | $\tau_L>0$ is rectangular laser-pulse duration (s), with L naming laser<br>$\tau_L>0$ 为矩形激光脉冲时长（s），L 表示激光 |

**Conventions and conditions.** $\int$ is time integration.

**约定与条件。** $\int$ 为时间积分。

(C2-E04) · Temporal profile definition / 时间分布的定义


$$
\int_{-\infty}^{\infty} f(t)\,dt=1,\qquad I(r,t)=F(r)f(t),\qquad I_{\mathrm{peak}}=F_0/\tau_L\quad\text{(rectangular pulse)}
$$


![A pulse waveform specifies when the energy is deposited.](../assets/figures/c2-e04.svg)

A pulse waveform specifies when the energy is deposited.

脉冲波形规定能量何时沉积。

**Step 5 — solve absorption-only transport.** Conservation of beam power in a thin slab says that the decrement of irradiance equals deposited heat per unit volume times thickness. With constant positive absorption coefficient, separate the irradiance differential, integrate from the entry face to depth, and exponentiate. The optical transit is treated as instantaneous on the thermal timescale.

**步骤 5——求解仅有吸收的光传输。** 薄层内光功率守恒说明，辐照度减少量等于单位体积沉积热量乘以厚度。取正常数吸收系数，分离辐照度微分，从入口面到指定深度积分，再取指数。在热学时间尺度上将光传播视为瞬时。

**Symbols before Eq. (C2-E05).**

**式（C2-E05）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $z\ge0$ is absorber depth (m)<br>$z\ge0$ 为吸收体深度（m） | $I(z)>0$ — Irradiance inside the absorber (W m⁻²)<br>$I(z)>0$ — 吸收体内部辐照度（W m⁻²） |
| $I_{\mathrm{in}}>0$ — Irradiance entering the absorber (W m⁻²)<br>$I_{\mathrm{in}}>0$ — 进入吸收体的辐照度（W m⁻²） | $\mu_a>0$ is constant absorption coefficient (m⁻¹), with a labeling absorption<br>$\mu_a>0$ 为常数吸收系数（m⁻¹），a 表示吸收 |
| $Q_{\mathrm{abs}}$ is volumetric optical heat deposition (W m⁻³)<br>$Q_{\mathrm{abs}}$ 为光学体积生热率（W m⁻³） | $I^{\prime}$ — Dummy irradiance integration variable (W m⁻²)<br>$I^{\prime}$ — 辐照度积分哑变量（W m⁻²） |
| $z^{\prime}$ — Dummy depth integration coordinate (m)<br>$z^{\prime}$ — 深度积分哑坐标（m） | $I$ — Laser irradiance (W m⁻²)<br>$I$ — 激光辐照度（W m⁻²） |

**Conventions and conditions.** $\partial_z$ denotes differentiation in depth; $z$; $\int$ denotes integration; $e^x$ denotes the exponential; Zero input gives identically zero deposition without dividing by irradiance.

**约定与条件。** $\partial_z$ 表示对深度求导；$z$ 相同；$\int$ 表示积分；$e^x$ 表示指数函数；零输入时沉积恒为零，无须除以辐照度。

(C2-E05) · Beer–Lambert constitutive model and solution / Beer–Lambert 本构模型及其解


$$
\begin{aligned}\partial_z I&=-\mu_a I,& Q_{\mathrm{abs}}&=\mu_a I,\\ \int_{I_{\mathrm{in}}}^{I(z)}\frac{dI^{\prime}}{I^{\prime}}&=-\int_0^z\mu_a\,dz^{\prime},&I(z)&=I_{\mathrm{in}}e^{-\mu_a z}.\end{aligned}
$$


![The absorber deposits heat over a finite optical depth.](../assets/figures/c2-e05.svg)

The absorber deposits heat over a finite optical depth.

吸收体在有限光学深度内沉积热量。

**Step 6 — integrate deposited heat.** Integrating in depth turns the volumetric source back into absorbed power per area. Integrating the normalized pulse and then the intercepted area gives the total energy. With one front-face reflected fraction, multiply the fraction entering the slab once. The effective absorptance below already includes this reflection; it must not be multiplied by a second reflection correction.

**步骤 6——积分沉积热量。** 对深度积分，将体积热源变回单位面积吸收功率；再对归一化脉冲和截获面积积分，得到总能量。若存在一个前表面反射比例，将进入薄层的比例乘入一次。下式的有效吸收率已包含该反射，不能再次乘上反射修正。

**Symbols before Eq. (C2-E06).**

**式（C2-E06）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $h_a>0$ is uniform absorber thickness (m)<br>$h_a>0$ 为均匀吸收体厚度（m） | $z$ is depth (m)<br>$z$ 为深度（m） |
| $Q_{\mathrm{abs}}$ is volumetric heat source (W m⁻³)<br>$Q_{\mathrm{abs}}$ 为体积热源（W m⁻³） | $I_{\mathrm{in}}$ is irradiance entering the slab (W m⁻²)<br>$I_{\mathrm{in}}$ 为进入薄层的辐照度（W m⁻²） |
| $\mu_a$ is absorption coefficient (m⁻¹)<br>$\mu_a$ 为吸收系数（m⁻¹） | $\mathcal R_\lambda\in[0,1]$ — Front-face reflected energy fraction (dimensionless)<br>$\mathcal R_\lambda\in[0,1]$ — 前表面反射能量比例（无量纲） |
| $A_\lambda$ is effective incident-light absorptance (dimensionless)<br>$A_\lambda$ 为相对于入射光的有效吸收率（无量纲） | $f_{\mathrm{geo}}$ is intercepted fraction (dimensionless)<br>$f_{\mathrm{geo}}$ 为截获比例（无量纲） |
| $E_L$ — Incident laser-pulse energy (J)<br>$E_L$ — 入射激光脉冲能量（J） | $E_{\mathrm{abs}}$ — Absorbed optical energy (J)<br>$E_{\mathrm{abs}}$ — 吸收光能（J） |
| $\Omega_a$ is absorbing volume (m³)<br>$\Omega_a$ 为吸收体体积（m³） | $dV$ its volume element (m³)<br>$dV$ 为其体积元（m³） |
| $t$ — Time (s)<br>$t$ — 时间（s） | $dt$ — Time integration element (s)<br>$dt$ — 时间积分微元（s） |
| $\lambda$ — Laser wavelength (m)<br>$\lambda$ — 激光波长（m） |  |

**Conventions and conditions.** $\int$ is integration; $e^x$ is the exponential.

**约定与条件。** $\int$ 为积分；$e^x$ 为指数函数。

(C2-E06) · Derived optical-energy balance / 推导得到的光能平衡


$$
\begin{aligned}\int_0^{h_a}Q_{\mathrm{abs}}\,dz&=I_{\mathrm{in}}(1-e^{-\mu_a h_a}),\\ A_\lambda&=(1-\mathcal R_\lambda)(1-e^{-\mu_a h_a}),\\ E_{\mathrm{abs}}&=f_{\mathrm{geo}}A_\lambda E_L=\int\!\int_{\Omega_a}Q_{\mathrm{abs}}\,dV\,dt.\end{aligned}
$$


![Interception, reflection, and internal absorption each act once.](../assets/figures/c2-e06.svg)

Interception, reflection, and internal absorption each act once.

截获、反射与内部吸收各作用一次。

Checks are physical: absorptance tends to zero as optical thickness tends to zero, and tends to the entering fraction for an optically thick layer. $Q_{\mathrm{abs}}$ has units W m⁻³ because absorption coefficient multiplies W m⁻². Its volume–time integral has units J. The model fails when scattering, multiple reflections, saturation, or plasma formation matters. A boundary heat source may replace the resolved layer if it represents the same energy; adding both counts that energy twice.

物理检验如下：光学厚度趋于零时吸收率趋于零；薄层光学足够厚时，吸收率趋于进入薄层的比例。吸收系数乘以 W m⁻²，使 $Q_{\mathrm{abs}}$ 的单位为 W m⁻³；其体积–时间积分的单位为 J。散射、多次反射、饱和或等离子体形成重要时，该模型失效。若边界热源代表相同能量，可以替代解析薄层；同时添加两者会重复计能。

Optical activation has been observed in specified absorber-containing PFC formulations. Strohm et al. used PbS-loaded PFP and a 1064 nm laser; Wei et al. used gold-containing PFH nanoemulsion. These primary studies establish optical routes, not a universal optical threshold, a liquid-jet speed, or a transfer yield. Absorber position and formulation remain experimental inputs. [[R6]](../reference/sources.html#r6) [[R7]](../reference/sources.html#r7)

在明确的含吸收体 PFC 配方中，已观测到光激活。Strohm 等使用含 PbS 的 PFP 与 1064 nm 激光；Wei 等使用含金颗粒的 PFH 纳米乳液。这些原始研究确立了光学激活途径，却没有提供普适光阈值、液体射流速度或转印成功率。吸收体位置和配方仍是实验输入。[[R6]](../reference/sources.html#r6) [[R7]](../reference/sources.html#r7)

## 2.2 Heat must reach the core on the event timescale

## 2.2 热量必须在事件时间尺度内到达核心

**Step 7 — apply thermal-energy conservation.** Before phase change, a material parcel gains sensible enthalpy through conduction and optical deposition. In a nearly incompressible phase with constant properties, negligible viscous heating and negligible pressure-work, use heat capacity at nearly constant pressure. Moving fluid contributes material advection; a solid absorber uses zero velocity. The divergence term is heat influx because conductive flux points down the temperature gradient.

**步骤 7——应用热能守恒。** 相变前，物质微团通过传导与光沉积获得显热焓。对于性质为常数、黏性生热及压力功可忽略的近不可压缩相，使用近恒压比热容。流动液体产生物质对流项；固体吸收层的速度取零。传导热流指向温度下降方向，因此散度项表示热量流入。

**Symbols before Eq. (C2-E07).**

**式（C2-E07）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol q$ is conductive heat flux (W m⁻²)<br>$\boldsymbol q$ 为传导热通量（W m⁻²） | $k>0$ is thermal conductivity (W m⁻¹ K⁻¹)<br>$k>0$ 为导热系数（W m⁻¹ K⁻¹） |
| $T$ is temperature (K)<br>$T$ 为温度（K） | $\rho>0$ is phase density (kg m⁻³)<br>$\rho>0$ 为该相密度（kg m⁻³） |
| $c_p>0$ is constant specific heat capacity (J kg⁻¹ K⁻¹)<br>$c_p>0$ 为常数比热容（J kg⁻¹ K⁻¹） | $t$ is time (s)<br>$t$ 为时间（s） |
| $\boldsymbol u$ is material velocity (m s⁻¹)<br>$\boldsymbol u$ 为物质速度（m s⁻¹） | $Q_{\mathrm{abs}}$ is optical heating (W m⁻³)<br>$Q_{\mathrm{abs}}$ 为光生热率（W m⁻³） |

**Conventions and conditions.** $D/Dt$ is the material derivative; $\partial_t$ is the fixed-position time derivative; $\nabla$ and $\nabla\cdot$ are spatial gradient and divergence (m⁻¹); the centered dot here is a vector contraction, not punctuation.

**约定与条件。** $D/Dt$ 为物质导数；$\partial_t$ 为固定位置时间导数；$\nabla$ 与 $\nabla\cdot$ 为空间梯度和散度（m⁻¹）；式中的中心点表示向量缩并，不是标点。

(C2-E07) · Reduced heat equation and Fourier constitutive law / 简化热传导方程与傅里叶本构定律


$$
\boldsymbol q=-k\nabla T,\qquad \rho c_p\frac{DT}{Dt}=\rho c_p(\partial_tT+\boldsymbol u\cdot\nabla T)=-\nabla\cdot\boldsymbol q+Q_{\mathrm{abs}}=\nabla\cdot(k\nabla T)+Q_{\mathrm{abs}}
$$


![Heating the absorber and heating the PFC are separate parts of the thermal path.](../assets/figures/c2-e07.svg)

Heating the absorber and heating the PFC are separate parts of the thermal path.

加热吸收体与加热 PFC 是热路径中的不同环节。

**Step 8 — close material contacts.** At an absorber–core contact, take the normal from material A into material B. Positive normal heat flux travels from A to B. With no interfacial thermal storage, the flux is continuous; a nonnegative contact resistance permits a temperature jump. A zero resistance gives continuous temperature. This contact is not the liquid–vapor Stefan interface below.

**步骤 8——闭合材料接触条件。** 在吸收体–核心接触面，将法向从材料 A 指向材料 B。正法向热通量从 A 流向 B。无界面热储存时，热通量连续；非负接触热阻允许温度跳跃。热阻为零时温度连续。该接触面不同于后文的液–汽 Stefan 界面。

**Symbols before Eq. (C2-E08).**

**式（C2-E08）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $q_n$ is signed normal heat flux (W m⁻²)<br>$q_n$ 为带符号法向热通量（W m⁻²） | $\boldsymbol q_A$ — Conductive heat flux in material A (W m⁻²)<br>$\boldsymbol q_A$ — 材料 A 中的传导热通量（W m⁻²） |
| $\boldsymbol q_B$ — Conductive heat flux in material B (W m⁻²)<br>$\boldsymbol q_B$ — 材料 B 中的传导热通量（W m⁻²） | $\boldsymbol n_{AB}$ is unit normal from A into B (dimensionless)<br>$\boldsymbol n_{AB}$ 为从 A 指向 B 的单位法向（无量纲） |
| $T_A$ — Temperature on contact side A (K)<br>$T_A$ — 接触面 A 侧温度（K） | $T_B$ — Temperature on contact side B (K)<br>$T_B$ — 接触面 B 侧温度（K） |
| $\mathcal R_T\ge0$ is area-specific thermal contact resistance (m² K W⁻¹)<br>$\mathcal R_T\ge0$ 为单位面积热接触阻力（m² K W⁻¹） |  |

**Conventions and conditions.** $\cdot$ denotes a vector dot product.

**约定与条件。** $\cdot$ 表示向量点积。

(C2-E08) · Thermal-contact boundary conditions / 热接触边界条件


$$
q_n=\boldsymbol q_A\cdot\boldsymbol n_{AB}=\boldsymbol q_B\cdot\boldsymbol n_{AB},\qquad T_A-T_B=\mathcal R_T q_n
$$


![Contact resistance delays heat transfer even after the light has been absorbed.](../assets/figures/c2-e08.svg)

Contact resistance delays heat transfer even after the light has been absorbed.

即使光已被吸收，接触热阻仍会延迟热传递。

**Step 9 — derive diffusion scales.** In a motionless constant-property region, divide the heat equation by volumetric heat capacity. Substitute a temperature change over time and a second spatial derivative over heating distance. Equating those orders gives a diffusion time; solving it for distance gives penetration during a specified heating duration. These are scaling estimates, not a sharp thermal-front solution. The heating duration can include post-pulse conduction and need not equal the optical pulse width.

**步骤 9——推导扩散尺度。** 在静止、常性质区域，将热方程除以体积热容。分别用时间内温度变化和加热距离上的二阶空间导数估计项量级。平衡这些量级得到扩散时间；反解距离得到指定加热时长内的渗透尺度。这是尺度估计，不是具有锐利热前沿的精确解。加热时长可包括脉冲后的传导，不必等于光脉冲宽度。

**Symbols before Eq. (C2-E09).**

**式（C2-E09）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\alpha>0$ is thermal diffusivity (m² s⁻¹)<br>$\alpha>0$ 为热扩散率（m² s⁻¹） | $k$ — Thermal conductivity (W m⁻¹ K⁻¹)<br>$k$ — 导热系数（W m⁻¹ K⁻¹） |
| $\rho$ — Local material mass density (kg m⁻³)<br>$\rho$ — 局部材料质量密度（kg m⁻³） | $c_p$ — Specific heat capacity at constant pressure (J kg⁻¹ K⁻¹)<br>$c_p$ — 定压比热容（J kg⁻¹ K⁻¹） |
| $\Delta T\ne0$ is characteristic temperature change (K)<br>$\Delta T\ne0$ 为特征温度变化（K） | $L_h>0$ is heating distance (m)<br>$L_h>0$ 为加热距离（m） |
| $t_{\mathrm{th}}$ is diffusion time estimate (s)<br>$t_{\mathrm{th}}$ 为扩散时间估计（s） | $\tau_h>0$ is available heating duration (s)<br>$\tau_h>0$ 为可用加热时长（s） |
| $\delta_T$ is penetration estimate (m)<br>$\delta_T$ 为渗透深度估计（m） |  |

**Conventions and conditions.** $\sim$ means order-of-magnitude scaling, not equality.

**约定与条件。** $\sim$ 表示量级尺度关系，不表示严格相等。

(C2-E09) · Diffusive scaling derived from the heat equation / 由热传导方程推导的扩散尺度关系


$$
\alpha=\frac{k}{\rho c_p},\qquad \frac{\Delta T}{t_{\mathrm{th}}}\sim\alpha\frac{\Delta T}{L_h^2},\qquad t_{\mathrm{th}}\sim\frac{L_h^2}{\alpha},\qquad \delta_T\sim\sqrt{\alpha\tau_h}
$$


![Compare heat penetration with the distance to the PFC, not only with beam width.](../assets/figures/c2-e09.svg)

Compare heat penetration with the distance to the PFC, not only with beam width.

应比较热渗透尺度与到达 PFC 的距离，而不只是光束宽度。

**Worked thermal control.** Declare PFP-like teaching coefficients: density 1630 kg m⁻³, heat capacity 654 J kg⁻¹ K⁻¹, and conductivity 0.050 W m⁻¹ K⁻¹. Only the rounded near-293 K heat capacity is tied to the cited NIST datum; the other constants are supplied teaching inputs. Use a 5 μm heating distance and a 10 ns heating duration.

**热学参照计算。** 声明近似 PFP 的教学系数：密度 1630 kg m⁻³、比热容 654 J kg⁻¹ K⁻¹、导热系数 0.050 W m⁻¹ K⁻¹。只有取整的近 293 K 比热容对应所引 NIST 数据；其余常数是给定教学输入。取加热距离为 5 μm，加热时长为 10 ns。

**Symbols before Eq. (C2-E10).**

**式（C2-E10）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\alpha_d$ is declared PFC-liquid diffusivity (m² s⁻¹), with d labeling droplet liquid<br>$\alpha_d$ 为所声明 PFC 液体的热扩散率（m² s⁻¹），d 表示液滴液体 | $t_{\mathrm{th}}$ is diffusion-time estimate (s)<br>$t_{\mathrm{th}}$ 为扩散时间估计（s） |
| $\delta_T$ is penetration estimate (m)<br>$\delta_T$ 为渗透深度估计（m） |  |

**Conventions and conditions.** The numerator 0.050 is conductivity in W m⁻¹ K⁻¹; 1630 is density in kg m⁻³; 654 is specific heat in J kg⁻¹ K⁻¹; $5\times10^{-6}$ is distance in m; $10^{-8}$ is duration in s; Powers are numerical exponents, and $\sim$ denotes a scale estimate.

**约定与条件。** 分子 0.050 为导热系数，单位 W m⁻¹ K⁻¹；1630 为密度，单位 kg m⁻³；654 为比热容，单位 J kg⁻¹ K⁻¹；$5\times10^{-6}$ 为距离，单位 m；$10^{-8}$ 为时长，单位 s；幂为数值指数，$\sim$ 表示尺度估计。

(C2-E10) · Declared-input thermal calculation / 采用明确给定输入的热学计算


$$
\begin{aligned}\alpha_d&=\frac{0.050}{1630(654)}=4.69034\times10^{-8}\ \mathrm{m^2\,s^{-1}},\\t_{\mathrm{th}}&\sim\frac{(5\times10^{-6})^2}{4.69034\times10^{-8}}=5.33010\times10^{-4}\ \mathrm{s},\\\delta_T&\sim\sqrt{(4.69034\times10^{-8})(10^{-8})}=2.16572\times10^{-8}\ \mathrm{m}.\end{aligned}
$$


![A short pulse does not imply uniform temperature in a micron-scale core.](../assets/figures/c2-e10.svg)

A short pulse does not imply uniform temperature in a micron-scale core.

短脉冲不意味着微米级核心内温度均匀。

The penetration estimate is only 0.00433 of the chosen heating distance. Without distributed heat deposition, the 10 ns pulse cannot justify uniform core temperature. Reducing distance to 100 nm reduces this constant-coefficient diffusion scale to 0.213 μs, still longer than 10 ns. Hotspots, aggregation, and shell contact can matter more than a bulk-average temperature. Optical breakdown is a distinct source mechanism and requires optical conditions and observations that support it; it is not added to a thermal-vaporization model by default.

渗透尺度仅为所选加热距离的 0.00433。若无分布式热沉积，10 ns 脉冲不足以支持核心温度均匀的假设。将距离降为 100 nm，会使该常系数扩散尺度降为 0.213 μs，仍长于 10 ns。热点、聚集及壳层接触可能比体平均温度更重要。光学击穿是不同的源机制，需要相应光学条件及观测支持，不能默认添加到热汽化模型中。

## 2.3 Volatility, confinement, and activation are different

## 2.3 挥发性、约束与激活并不相同

**Step 10 — distinguish initial liquid pressure from ambient pressure.** A spherical PFC–carrier interface carries capillary stress. Add a declared shell-supported excess pressure when the shell has one. This static reference ignores rapid acceleration and shell-rate effects, which need a dynamic constitutive law.

**步骤 10——区分初始液体压力与环境压力。** 球形 PFC–载液界面承受毛细应力；若壳层能承压，还应加上明确的壳层支撑超压。该静态参照忽略快速加速度与壳层速率效应；这些需要动态本构定律。

**Symbols before Eq. (C2-E11).**

**式（C2-E11）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_d$ is initial PFC-liquid pressure (Pa)<br>$p_d$ 为初始 PFC 液体压力（Pa） | $p_c$ carrier pressure (Pa)<br>$p_c$ 为载液压力（Pa） |
| $a>0$ is PFC-core radius (m)<br>$a>0$ 为 PFC 核心半径（m） | $\sigma_{pc}\ge0$ is PFC–carrier interfacial tension (N m⁻¹), with pc naming those phases<br>$\sigma_{pc}\ge0$ 为 PFC–载液界面张力（N m⁻¹），pc 表示这两个相 |
| $\Pi_{\mathrm{shell}}$ is shell-supported excess pressure (Pa)<br>$\Pi_{\mathrm{shell}}$ 为壳层支撑超压（Pa） |  |

**Conventions and conditions.** $\simeq$ is the static spherical approximation; The numerical interfacial tension 0.020 is a teaching input in N m⁻¹, the radii are in m, and 1 kPa = 1000 Pa.

**约定与条件。** $\simeq$ 表示静态球形近似；数值界面张力 0.020 是教学输入，单位 N m⁻¹；半径单位为 m；1 kPa = 1000 Pa。

(C2-E11) · Static capillary and shell-pressure control / 静态毛细压力与壳层压力对照模型


$$
p_d\simeq p_c+\frac{2\sigma_{pc}}{a}+\Pi_{\mathrm{shell}},\qquad \frac{2(0.020)}{5\times10^{-6}}=8.00\ \mathrm{kPa},\qquad\frac{2(0.020)}{10^{-7}}=400\ \mathrm{kPa}
$$


![The smaller inclusion has a larger capillary contribution at the same tension.](../assets/figures/c2-e11.svg)

The smaller inclusion has a larger capillary contribution at the same tension.

界面张力相同时，较小夹杂的毛细压力贡献更大。

Use named compounds rather than a generic “PFC boiling point.” The following NIST entries refer to neat compounds. The displayed boiling ranges are different tabulated datasets, not uncertainty bands for a formulation. Convert molar heat capacity or enthalpy to mass-specific values by dividing by the stated molar mass. [[R8]](../reference/sources.html#r8) [[R9]](../reference/sources.html#r9) [[R15]](../reference/sources.html#r15)

应使用明确化合物，而不是笼统的“PFC 沸点”。下列 NIST 条目指纯化合物。列出的沸点范围来自不同数据集，不是某配方的不确定性区间。摩尔热容或焓除以所给摩尔质量，才得到质量比性质。[[R8]](../reference/sources.html#r8) [[R9]](../reference/sources.html#r9) [[R15]](../reference/sources.html#r15)

| Compound and identity<br>化合物与身份 | Bulk reference<br>体相参照 | Proper scope<br>正确用途 |
| --- | --- | --- |
| PFP: C₅F₁₂; CAS 678-26-2; molar mass 0.2880343 kg mol⁻¹<br>PFP：C₅F₁₂；CAS 678-26-2；摩尔质量 0.2880343 kg mol⁻¹ | Normal-boiling entries 302.6–303.2 K; liquid heat-capacity datum 188.3 J mol⁻¹ K⁻¹ at 293 K, giving 653.74 J kg⁻¹ K⁻¹.<br>正常沸点条目 302.6–303.2 K；293 K 液体热容数据为 188.3 J mol⁻¹ K⁻¹，对应 653.74 J kg⁻¹ K⁻¹。 | Compound-specific thermal reference; not a coated-droplet activation law.<br>特定化合物热学参照；不是包覆液滴激活定律。 |
| PFH: C₆F₁₄; CAS 355-42-0; molar mass 0.3380418 kg mol⁻¹<br>PFH：C₆F₁₄；CAS 355-42-0；摩尔质量 0.3380418 kg mol⁻¹ | Normal-boiling entries 330.3–333 K; vaporization enthalpy 31.5 kJ mol⁻¹ at 316 K, giving 93.18 kJ kg⁻¹.<br>正常沸点条目 330.3–333 K；316 K 汽化焓为 31.5 kJ mol⁻¹，对应 93.18 kJ kg⁻¹。 | Retain temperature and dataset; do not transfer this value to every PFC.<br>保留温度及数据集；不能将此值套用到所有 PFC。 |
| Water: H₂O; molar mass 0.0180153 kg mol⁻¹<br>水：H₂O；摩尔质量 0.0180153 kg mol⁻¹ | Normal-boiling compilation approximately 373.17 K.<br>正常沸点汇编约为 373.17 K。 | PFC-free thermal comparison at matched temperature and pressure.<br>在相同温度与压力下的不含 PFC 热学参照。 |

**Step 11 — calculate equilibrium vapor pressure within the correlation domain.** NIST tabulates the Barber–Cady Antoine fit for PFP. The logarithm acts on pressure divided by one bar, so its argument is dimensionless. The fit coefficients are empirical, not derived from the optical heating model. [[R8]](../reference/sources.html#r8)

**步骤 11——在关联式适用域内计算平衡蒸汽压。** NIST 列出了 PFP 的 Barber–Cady Antoine 拟合。对压力除以一巴后的比值取对数，故对数自变量无量纲。拟合系数是经验数据，并非由光加热模型推导。[[R8]](../reference/sources.html#r8)

**Symbols before Eq. (C2-E12).**

**式（C2-E12）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{sat,PFP}}(T)$ is bulk equilibrium PFP vapor pressure (Pa), sat labeling saturation<br>$p_{\mathrm{sat,PFP}}(T)$ 为体相平衡 PFP 蒸汽压（Pa），sat 表示饱和 | $T$ is absolute temperature in the stated range (K)<br>$T$ 为所给范围内的绝对温度（K） |

**Conventions and conditions.** $\log_{10}$ is the base-ten logarithm; One bar equals $10^5$ Pa; Empirical coefficient 4.2063 is dimensionless; 1103.454 K and 39.77 K have temperature units; The denominator is positive throughout the stated domain.

**约定与条件。** $\log_{10}$ 为常用对数；一巴等于 $10^5$ Pa；经验系数 4.2063 无量纲；1103.454 K 和 39.77 K 具有温度单位；所给范围内分母为正。

(C2-E12) · Verified empirical PFP property correlation / 已核验的 PFP 物性经验关联式


$$
\log_{10}\!\left(\frac{p_{\mathrm{sat,PFP}}(T)}{10^5\ \mathrm{Pa}}\right)=4.2063-\frac{1103.454\ \mathrm{K}}{T-39.77\ \mathrm{K}},\qquad282.82\ \mathrm{K}\le T\le337.94\ \mathrm{K}
$$


![The saturation curve concerns an equilibrium state, not automatic activation.](../assets/figures/c2-e12.svg)

The saturation curve concerns an equilibrium state, not automatic activation.

饱和曲线描述平衡状态，而不是自动激活。

Evaluating Eq. (C2-E12) gives 70.60 kPa at 293 K, 103.35 kPa at 303 K, and 204.33 kPa at 323 K. For water use its stated temperature interval, rather than extrapolating one coefficient set. The NIST water coefficients below produce 2.315 kPa at 293 K and 12.248 kPa at 323 K. These are calculated comparisons, not project measurements. [[R15]](../reference/sources.html#r15)

式（C2-E12）给出 293 K 时 70.60 kPa、303 K 时 103.35 kPa、323 K 时 204.33 kPa。水应使用对应温区的系数，不能外推同一组系数。下列 NIST 水系数给出 293 K 时 2.315 kPa、323 K 时 12.248 kPa。这些是计算对比，不是项目测量。[[R15]](../reference/sources.html#r15)

**Symbols before Eq. (C2-E13).**

**式（C2-E13）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{sat,w}}$ is bulk equilibrium water vapor pressure (Pa), w labeling water<br>$p_{\mathrm{sat,w}}$ 为体相平衡水蒸汽压（Pa），w 表示水 | $T$ is temperature (K), restricted to either listed interval<br>$T$ 为温度（K），限定在两个所列区间之一 |
| $T/\mathrm K$ is the numerical temperature in kelvin (dimensionless)<br>$T/\mathrm K$ 为以开尔文计的温度数值（无量纲） |  |

**Conventions and conditions.** $\log_{10}$ is the base-ten logarithm of pressure relative to one bar ($10^5$ Pa); The leading coefficients are dimensionless; all coefficients multiplied by K have temperature units; No value is assigned to the 303–304 K gap by these two branches.

**约定与条件。** $\log_{10}$ 为相对于一巴（$10^5$ Pa）的压力比值的常用对数；首项系数无量纲；乘以 K 的系数具有温度单位；这两个分支未给出 303–304 K 间隙的值。

(C2-E13) · Verified empirical water property correlations / 已核验的水物性经验关联式


$$
\log_{10}\!\left(\frac{p_{\mathrm{sat,w}}(T)}{10^5\ \mathrm{Pa}}\right)=\begin{cases}5.40221-1838.675\ \mathrm{K}/(T-31.737\ \mathrm{K}),&273\le T/\mathrm{K}\le303,\\5.20389-1733.926\ \mathrm{K}/(T-39.485\ \mathrm{K}),&304\le T/\mathrm{K}\le333.\end{cases}
$$


![Water provides a matched-temperature reference, not a guaranteed vapor reservoir.](../assets/figures/c2-e13.svg)

Water provides a matched-temperature reference, not a guaranteed vapor reservoir.

水提供同温参照，却不是有保证的蒸汽库。

At 323 K and 100 kPa carrier pressure, the declared 5 μm shell-free PFP core has initial liquid pressure 108 kPa, below the 204.33 kPa equilibrium PFP reference. The 100 nm core has 500 kPa liquid pressure, above it. Thus the same temperature can provide positive bulk driving for the larger core and no positive driving in this smaller-core control. This conclusion uses the stated constant tension and neglects shell stress; neither temperature is a measured onset threshold.

在 323 K、载液压力 100 kPa 下，所声明的无壳 5 μm PFP 核初始液体压力为 108 kPa，低于 204.33 kPa 的 PFP 平衡参照；100 nm 核的液体压力为 500 kPa，高于该值。因此，同一温度可能对较大核心提供正体相驱动力，却在此较小核心参照中没有正驱动力。此结论使用声明的常界面张力并忽略壳层应力；这两个温度都不是测得的起始阈值。

**Step 12 — construct the capillarity free energy.** Define a vapor nucleus inside the liquid PFC, not a whole-core interface. Under the local isothermal, bulk-reservoir approximation, forming the new interface costs tension times area; replacing liquid by favorable vapor gains driving pressure times volume. The vapor–PFC tension is not the PFC–carrier tension in Eq. (C2-E11).

**步骤 12——构造毛细自由能。** 在液态 PFC 内定义汽核，而非整个核心的外界面。在局部等温、体相库近似下，产生新界面的代价是界面张力乘面积；有利蒸汽替代液体的收益是驱动压差乘体积。蒸汽–PFC 张力不同于式（C2-E11）中的 PFC–载液张力。

**Symbols before Eq. (C2-E14).**

**式（C2-E14）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Delta p_n$ is vapor-nucleation driving pressure (Pa), n labeling nucleation<br>$\Delta p_n$ 为汽化成核驱动压差（Pa），n 表示成核 | $p_{\mathrm{sat,PFC}}(T_i)$ is bulk PFC saturation pressure at local interface temperature $T_i$ (Pa and K)<br>$p_{\mathrm{sat,PFC}}(T_i)$ 为局部界面温度 $T_i$ 下的体相 PFC 饱和蒸汽压（Pa 和 K） |
| $p_d$ is PFC-liquid pressure (Pa)<br>$p_d$ 为 PFC 液体压力（Pa） | $W(r_n)$ is nucleus formation free energy (J)<br>$W(r_n)$ 为汽核形成自由能（J） |
| $r_n\ge0$ is vapor-nucleus radius (m)<br>$r_n\ge0$ 为汽核半径（m） | $\sigma_{vp}>0$ is vapor–PFC tension (N m⁻¹), vp naming the interface<br>$\sigma_{vp}>0$ 为蒸汽–PFC 张力（N m⁻¹），vp 表示该界面 |
| $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） | $T_i$ — Local phase-interface temperature (K)<br>$T_i$ — 局部相界面温度（K） |

**Conventions and conditions.** The model assumes fixed $T_i,p_d$; $r_n$ small compared with the PFC core.

**约定与条件。** 模型假设 $T_i,p_d$ 固定，且 $r_n$ 远小于 PFC 核心。

(C2-E14) · Classical homogeneous capillarity approximation / 经典均相成核的毛细近似


$$
\Delta p_n=p_{\mathrm{sat,PFC}}(T_i)-p_d,\qquad W(r_n)=4\pi\sigma_{vp}r_n^2-\frac{4\pi}{3}\Delta p_n r_n^3
$$


![The barrier belongs to creating a new internal vapor interface.](../assets/figures/c2-e14.svg)

The barrier belongs to creating a new internal vapor interface.

势垒来自生成新的内部蒸汽界面。

**Step 13 — find the stationary point and its branch.** Differentiate the two powers of nucleus radius. For positive driving pressure, the nonzero stationary radius is obtained by dividing the bracket by positive radius and driving pressure. The second derivative there is negative, so it is a barrier maximum. For nonpositive driving pressure, the derivative is positive for every positive radius and there is no positive critical-radius branch in this model.

**步骤 13——求驻点并区分分支。** 对汽核半径的两个幂求导。驱动压差为正时，除以正半径与正压差，可得到非零驻点半径。在该点二阶导数为负，因此是势垒最大值。驱动压差非正时，每个正半径处的导数均为正，在本模型中不存在正临界半径分支。

**Symbols before Eq. (C2-E15).**

**式（C2-E15）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $W$ is nucleus free energy (J)<br>$W$ 为汽核自由能（J） | $r_n>0$ is nucleus radius (m)<br>$r_n>0$ 为汽核半径（m） |
| $\sigma_{vp}>0$ is vapor–PFC interfacial tension (N m⁻¹)<br>$\sigma_{vp}>0$ 为蒸汽–PFC 界面张力（N m⁻¹） | $\Delta p_n$ is fixed driving pressure (Pa)<br>$\Delta p_n$ 为固定驱动压差（Pa） |
| $r_*$ is the positive critical radius (m), with star labeling the stationary point and requiring $\Delta p_n>0$<br>$r_*$ 为正临界半径（m），星号标记驻点，且要求 $\Delta p_n>0$ | $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** $d/dr_n$ is radius differentiation, $|_{r_*}$ denotes evaluation there; The first derivative has units J m⁻¹ and the second J m⁻².

**约定与条件。** $d/dr_n$ 为对半径求导，$|_{r_*}$ 表示在该点求值；一阶导数单位为 J m⁻¹，二阶导数为 J m⁻²。

(C2-E15) · Derived critical radius and branch check / 推导得到的临界半径与分支检验


$$
\begin{aligned}\frac{dW}{dr_n}&=8\pi\sigma_{vp}r_n-4\pi\Delta p_n r_n^2=4\pi r_n(2\sigma_{vp}-\Delta p_n r_n),\\r_*&=2\sigma_{vp}/\Delta p_n\quad(\Delta p_n>0),\\\left.\frac{d^2W}{dr_n^2}\right|_{r_*}&=8\pi\sigma_{vp}-8\pi\Delta p_n r_*=-8\pi\sigma_{vp}<0.\end{aligned}
$$


![The stationary point is a maximum, not a stable equilibrium nucleus.](../assets/figures/c2-e15.svg)

The stationary point is a maximum, not a stable equilibrium nucleus.

该驻点是最大值，不是稳定平衡汽核。

**Step 14 — substitute the critical radius explicitly.** Square and cube the positive radius, then subtract the two coefficients. The barrier falls as driving pressure increases, but remains positive at any finite positive driving pressure and positive tension.

**步骤 14——显式代入临界半径。** 对正半径平方、立方，再将两项系数相减。随驱动压差增加，势垒降低；但对有限正驱动压差及正张力，势垒仍为正。

**Symbols before Eq. (C2-E16).**

**式（C2-E16）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $W_*=W(r_*)$ is critical-nucleus free-energy barrier (J), with star labeling the critical value<br>$W_*=W(r_*)$ 为临界汽核自由能势垒（J），星号标记临界值 | $\sigma_{vp}>0$ is vapor–PFC interfacial tension (N m⁻¹)<br>$\sigma_{vp}>0$ 为蒸汽–PFC 界面张力（N m⁻¹） |
| $\Delta p_n>0$ is driving pressure (Pa)<br>$\Delta p_n>0$ 为驱动压差（Pa） | $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** superscripts 2 and 3 are powers; This result inherits the homogeneous, locally isothermal, small-nucleus assumptions.

**约定与条件。** 上标 2、3 表示幂；该结果继承均匀成核、局部等温及小汽核假设。

(C2-E16) · Derived homogeneous barrier height / 推导得到的均相成核势垒高度


$$
\begin{aligned}W_*&=4\pi\sigma_{vp}\frac{4\sigma_{vp}^2}{\Delta p_n^2}-\frac{4\pi}{3}\Delta p_n\frac{8\sigma_{vp}^3}{\Delta p_n^3}\\&=\left(16-\frac{32}{3}\right)\frac{\pi\sigma_{vp}^3}{\Delta p_n^2}=\frac{16\pi\sigma_{vp}^3}{3\Delta p_n^2}.\end{aligned}
$$


![Positive superheat driving does not make the nucleation barrier vanish.](../assets/figures/c2-e16.svg)

Positive superheat driving does not make the nucleation barrier vanish.

正的过热驱动力并不会使成核势垒消失。

The units check is $\mathrm{(N/m)^3/Pa^2=N\,m=J}$. The critical radius scales as tension divided by pressure, hence has units m. If the computed nucleus is comparable to the core radius, the reservoir approximation fails. Absorber surfaces, shell defects, dissolved gas, and wetting can replace homogeneous nucleation by a heterogeneous route. A seed imposed after the pulse defines a post-nucleation calculation; it is not a prediction of onset.

单位检验为 $\mathrm{(N/m)^3/Pa^2=N\,m=J}$。临界半径按张力除以压力缩放，故单位为 m。若计算得到的汽核与核心半径相当，体相库近似失效。吸收体表面、壳层缺陷、溶解气体及润湿可能使均匀成核转为异质成核。脉冲后人为给定的种子仅定义成核后计算，不是起始预测。

**Step 15 — turn a rate into a probability only under a stated stochastic model.** For independent Poisson nucleation events, survival over a small interval loses the expected number of events times its current value. Integrate its logarithmic derivative with initial survival one. The result applies even when the rate varies in space and time; it does not determine that rate. A formulation-specific empirical activation law is preferable when the homogeneous premise is false.

**步骤 15——只有明确随机模型，才能将速率变为概率。** 对独立 Poisson 成核事件，短时间内的未成核概率减少量等于当前值乘以预期事件数。以初始未成核概率为一，积分其对数导数。即使速率随时空变化，该结果仍适用；但它不提供速率本身。均匀成核前提不成立时，更应采用特定配方的经验激活定律。

**Symbols before Eq. (C2-E17).**

**式（C2-E17）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $J(T,p)\ge0$ is prescribed nucleation rate (m⁻³ s⁻¹) at local temperature $T$ (K) and pressure $p$ (Pa)<br>$J(T,p)\ge0$ 为给定的成核速率（m⁻³ s⁻¹），取决于局部温度 $T$（K）与压力 $p$（Pa） | $V_d(t)$ denotes the remaining liquid-core region and its volume (m³), d labeling droplet<br>$V_d(t)$ 表示剩余液核区域及其体积（m³），d 表示液滴 |
| $\Lambda(t)$ is total event rate (s⁻¹)<br>$\Lambda(t)$ 为总事件速率（s⁻¹） | $S(t)$ is no-event survival probability (dimensionless)<br>$S(t)$ 为未发生事件的概率（无量纲） |
| $P_{\mathrm{act}}$ activation probability (dimensionless)<br>$P_{\mathrm{act}}$ 为激活概率（无量纲） | $t\ge0$ — Time (s)<br>$t\ge0$ — 时间（s） |
| $dV$ is volume element (m³)<br>$dV$ 为体积元（m³） | $T$ — Thermodynamic temperature (K)<br>$T$ — 热力学温度（K） |
| $p$ — Local or prescribed thermodynamic pressure as specified (Pa)<br>$p$ — 按情景指定的局部或给定热力学压力（Pa） |  |

**Conventions and conditions.** $d/dt$, $\int$, $\ln$, and $e^x$ denote differentiation, integration, natural logarithm, and exponential; The derivation assumes finite integrated nonnegative rate and independent Poisson events.

**约定与条件。** $d/dt$、$\int$、$\ln$、$e^x$ 表示求导、积分、自然对数和指数函数；推导要求积分非负速率有限，且事件满足独立 Poisson 模型。

(C2-E17) · Derived probability under a prescribed Poisson rate / 给定泊松事件率下推导的概率


$$
\begin{aligned}\Lambda(t)&=\int_{V_d(t)}J(T, p)\,dV,\qquad\frac{dS}{dt}=-\Lambda(t)S,\qquad S(0)=1,\\\ln S(t)&=-\int_0^t\Lambda(t^{\prime})\,dt^{\prime},\qquad P_{\mathrm{act}}(t)=1-S(t)=1-e^{-\int_0^t\int_{V_d(t^{\prime})}J(T,p)\,dV\,dt^{\prime}}.\end{aligned}
$$


![Activation probability requires the rate and the time spent in the activating state.](../assets/figures/c2-e17.svg)

Activation probability requires the rate and the time spent in the activating state.

激活概率需要速率及处于可激活状态的时长。

## 2.4 Close phase mass and energy without an infinite reservoir

## 2.4 用有限库存闭合相质量与能量

**Step 16 — conserve compound inventory.** Initial PFC mass is liquid density times core volume. Later liquid, vapor, dissolved, and escaped PFC exhaust that same initial mass when there is no external supply. Escaped mass is a cumulative ledger, not vapor remaining inside the bubble. The water carrier cannot replenish PFC.

**步骤 16——守恒化合物库存。** 初始 PFC 质量等于液体密度乘以核心体积。无外部供应时，后续液体、蒸汽、溶解及逸出 PFC 的总和就是该初始质量。逸出质量是累计账目，不是气泡内的剩余蒸汽。水性载液不能补充 PFC。

**Symbols before Eq. (C2-E18).**

**式（C2-E18）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_{\mathrm{PFC},0}$ is initial PFC mass (kg), 0 labeling the initial state<br>$m_{\mathrm{PFC},0}$ 为初始 PFC 质量（kg），0 表示初始状态 | $\rho_d>0$ is initial PFC-liquid density (kg m⁻³), d labeling droplet<br>$\rho_d>0$ 为初始 PFC 液体密度（kg m⁻³），d 表示液滴 |
| $a_0>0$ is initial core radius (m)<br>$a_0>0$ 为初始核心半径（m） | $m_l$ — Remaining liquid-PFC mass (kg)<br>$m_l$ — 剩余液态 PFC 质量（kg） |
| $m_v$ — PFC vapor mass (kg)<br>$m_v$ — PFC 蒸气质量（kg） | $m_{\mathrm{diss}}$ — Dissolved PFC mass (kg)<br>$m_{\mathrm{diss}}$ — 溶解 PFC 质量（kg） |
| $m_{\mathrm{esc}}\ge0$ — Cumulative escaped PFC mass (kg)<br>$m_{\mathrm{esc}}\ge0$ — 累计逸出 PFC 质量（kg） | $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** the l, v, diss, and esc labels name those compartments; The bound assumes no subsequent PFC supply.

**约定与条件。** l、v、diss、esc 分别标记这些部分；质量上界假设后续没有 PFC 供应。

(C2-E18) · Exact compound-mass ledger under the stated closed supply / 所述封闭供给条件下化合物质量的精确收支


$$
m_{\mathrm{PFC},0}=\frac{4\pi}{3}\rho_da_0^3,\qquad m_l+m_v+m_{\mathrm{diss}}+m_{\mathrm{esc}}=m_{\mathrm{PFC},0},\qquad 0\le m_v\le m_{\mathrm{PFC},0}
$$


![The compound ledger survives expansion, condensation, dissolution, and venting.](../assets/figures/c2-e18.svg)

The compound ledger survives expansion, condensation, dissolution, and venting.

化合物账目在膨胀、凝结、溶解及排气过程中均成立。

**Step 17 — locate the actual phase-change surface.** Integrate species flux over the interface that this species contacts. The full spherical area is available only if that species contacts the complete surface and its flux is uniform. A residual PFC inclusion in water may instead provide a much smaller vaporization surface.

**步骤 17——定位实际相变表面。** 应在该组分接触的界面上积分其通量。只有该组分接触整个球面且通量均匀，才可使用全球面积。水中残余 PFC 夹杂可能只提供更小的汽化表面。

**Symbols before Eq. (C2-E19).**

**式（C2-E19）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_{v,s}$ is vapor mass of species $s$ (kg), where $s$ labels a specified species such as PFC or water<br>$m_{v,s}$ 为组分 $s$ 的蒸汽质量（kg） | $j_s$ is signed liquid-to-vapor mass flux (kg m⁻² s⁻¹)<br>$j_s$ 为带符号液到汽质量通量（kg m⁻² s⁻¹） |
| $\Gamma_s$ is the species-contacting interface (—)<br>$\Gamma_s$ 为该组分接触的界面（—） | $dA$ is its area element (m²)<br>$dA$ 为面积元（m²） |
| $R>0$ is spherical interface radius (m) only in the special second formula<br>$R>0$ 仅在第二个特殊式中表示球形界面半径（m） | $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |
| $s$ — Species index (dimensionless)<br>$s$ — 组分指标（无量纲） |  |

**Conventions and conditions.** a dot is a time derivative (kg s⁻¹); the phase label isolates the phase-change contribution, excluding escape and dissolution; $\int$ is surface integration.

**约定与条件。** 上点表示时间导数（kg s⁻¹）；phase 标记单独的相变贡献，不含逸出与溶解；$\int$ 为面积积分。

(C2-E19) · Species phase-mass balance / 组分的分相质量平衡


$$
\left.\dot m_{v,s}\right|_{\mathrm{phase}}=\int_{\Gamma_s}j_s\,dA,\qquad \left.\dot m_{v,s}\right|_{\mathrm{phase}}=4\pi R^2j_s\quad\text{only for uniform complete spherical contact}
$$


![A bubble surface and a PFC evaporation surface need not be identical.](../assets/figures/c2-e19.svg)

A bubble surface and a PFC evaporation surface need not be identical.

气泡表面与 PFC 蒸发表面未必相同。

**Step 18 — derive the phase-change velocity slip.** At a single-component interface, fluid crosses the moving interface at the same mass flux on each side. In a bubble, the liquid-to-vapor normal is inward. Taking its dot product with radial liquid velocity minus interface velocity gives radius speed minus liquid speed. Solve that signed equality for the liquid speed. A velocity potential using interface speed as liquid speed inherits the small-slip approximation.

**步骤 18——推导相变速度滑移。** 单组分界面两侧，流体穿过运动界面的质量通量相同。对气泡，液到汽法向指向内侧；径向液速减去界面速度，再与该法向点乘，得到半径速度减液体速度。解这个带符号等式得到液速。若速度势将界面速度当作液速，就继承了小滑移近似。

**Symbols before Eq. (C2-E20).**

**式（C2-E20）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $j_s$ is single-component phase mass flux (kg m⁻² s⁻¹), s labeling that component<br>$j_s$ 为单组分相变质量通量（kg m⁻² s⁻¹），s 标记该组分 | $\rho_l$ — Adjacent liquid density (kg m⁻³)<br>$\rho_l$ — 邻接液体密度（kg m⁻³） |
| $\rho_v>0$ — Adjacent vapor density (kg m⁻³)<br>$\rho_v>0$ — 邻接蒸气密度（kg m⁻³） | $\boldsymbol u_l$ — Adjacent liquid velocity (m s⁻¹)<br>$\boldsymbol u_l$ — 邻接液体速度（m s⁻¹） |
| $\boldsymbol u_v$ — Adjacent vapor velocity (m s⁻¹)<br>$\boldsymbol u_v$ — 邻接蒸气速度（m s⁻¹） | $\boldsymbol v_\Gamma$ is interface velocity (m s⁻¹)<br>$\boldsymbol v_\Gamma$ 为界面速度（m s⁻¹） |
| $\boldsymbol n$ is unit normal liquid→vapor (dimensionless)<br>$\boldsymbol n$ 为液→汽单位法向（无量纲） | $\boldsymbol e_r$ outward radial unit vector (dimensionless)<br>$\boldsymbol e_r$ 为向外径向单位向量（无量纲） |
| $R>0$ is bubble radius (m)<br>$R>0$ 为气泡半径（m） | $\dot R$ its time derivative (m s⁻¹)<br>$\dot R$ 为其时间导数（m s⁻¹） |
| $u_l(R)$ is outward radial liquid velocity at the interface (m s⁻¹)<br>$u_l(R)$ 为界面处向外径向液速（m s⁻¹） |  |

**Conventions and conditions.** $\cdot$ is a vector dot product.

**约定与条件。** $\cdot$ 为向量点积。

(C2-E20) · Exact single-component interface mass jump / 单组分界面的精确质量跃迁条件


$$
\begin{aligned}j_s&=\rho_l(\boldsymbol u_l-\boldsymbol v_\Gamma)\cdot\boldsymbol n=\rho_v(\boldsymbol u_v-\boldsymbol v_\Gamma)\cdot\boldsymbol n,\\\boldsymbol n&=-\boldsymbol e_r,\quad\boldsymbol v_\Gamma=\dot R\boldsymbol e_r,\quad j_s=\rho_l[\dot R-u_l(R)],\\u_l(R)&=\dot R-j_s/\rho_l.\end{aligned}
$$


![The interface need not move at the same speed as the adjacent liquid.](../assets/figures/c2-e20.svg)

The interface need not move at the same speed as the adjacent liquid.

界面不必以邻接液体的速度运动。

The phase-slip approximation requires $|j_s|/\rho_l$ small relative to the relevant liquid or interface velocity scale. At a turning point, division by zero radius speed cannot be a useful criterion; choose a finite event velocity scale and check absolute slip. Strong evaporation can also contribute recoil stress through the momentum jump. Reusing Chapter 1’s simple spherical stress relation requires that recoil be negligible or explicitly added. Mixtures require species diffusion and composition boundary conditions, not the pure-component jump applied independently without a common mass balance.

相变滑移近似要求 $|j_s|/\rho_l$ 相对于相关液体或界面速度尺度足够小。在转折点，除以零半径速度不能形成有效判据；应选有限事件速度尺度并检查绝对滑移。强蒸发还可通过动量跳跃产生反冲应力。复用第一章的简单球形应力关系，要求反冲可忽略或显式补入。混合物需要组分扩散与组成边界条件，不能无共同质量守恒而对每个组分独立套用纯组分跳跃式。

**Step 19 — derive the Stefan sign from interfacial energy conservation.** With no surface heat storage and negligible kinetic and mechanical jump corrections, conductive heat arriving from the liquid, minus that leaving toward vapor, pays the enthalpy needed to change phase. The enthalpy difference uses the same temperature and reference convention on both sides. Reverse the heat supply and flux becomes negative: condensation releases latent enthalpy.

**步骤 19——由界面能量守恒确定 Stefan 符号。** 无表面热储存、且动能及力学跳跃修正可忽略时，从液体到达的传导热减去流向蒸汽的热，为相变所需焓提供能量。焓差在两侧采用相同温度与参考约定。热供应反向时，通量为负：凝结释放潜焓。

**Symbols before Eq. (C2-E21).**

**式（C2-E21）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $L_{v,s}>0$ is latent enthalpy per species mass (J kg⁻¹)<br>$L_{v,s}>0$ 为单位组分质量的潜焓（J kg⁻¹） | $h_{v,s}$ — Specific vapor enthalpy of species s at the actual boundary state (J kg⁻¹)<br>$h_{v,s}$ — 实际边界状态下组分 s 的蒸气比焓（J kg⁻¹） |
| $h_{l,s}$ — Specific liquid enthalpy of species s at the interface (J kg⁻¹)<br>$h_{l,s}$ — 界面处组分 s 的液体比焓（J kg⁻¹） | $j_s$ is signed evaporation flux (kg m⁻² s⁻¹)<br>$j_s$ 为带符号蒸发通量（kg m⁻² s⁻¹） |
| $\boldsymbol q_l$ — Liquid-side conductive heat flux (W m⁻²)<br>$\boldsymbol q_l$ — 液体侧传导热通量（W m⁻²） | $\boldsymbol q_v$ — Vapor-side conductive heat flux (W m⁻²)<br>$\boldsymbol q_v$ — 蒸气侧传导热通量（W m⁻²） |
| $\boldsymbol n$ points liquid→vapor (dimensionless)<br>$\boldsymbol n$ 从液指向汽（无量纲） | $\eta\in\{l,v\}$ labels phase (dimensionless)<br>$\eta\in\{l,v\}$ 表示相（无量纲） |
| $k_\eta$ — Thermal conductivity of the selected phase (W m⁻¹ K⁻¹)<br>$k_\eta$ — 所选相的导热系数（W m⁻¹ K⁻¹） | $T_\eta$ — Temperature of the selected phase (K)<br>$T_\eta$ — 所选相的温度（K） |

**Conventions and conditions.** $\nabla$ is spatial gradient (m⁻¹); $\cdot$ is a vector dot product; All terms in the heat jump have units W m⁻².

**约定与条件。** $\nabla$ 为空间梯度（m⁻¹）；$\cdot$ 为向量点积；热跳跃式各项单位均为 W m⁻²。

(C2-E21) · Reduced interfacial energy jump and Fourier law / 简化界面能量跃迁条件与傅里叶定律


$$
L_{v,s}=h_{v,s}-h_{l,s}>0,\qquad j_sL_{v,s}=(\boldsymbol q_l-\boldsymbol q_v)\cdot\boldsymbol n,\qquad\boldsymbol q_\eta=-k_\eta\nabla T_\eta\quad(\eta=l,v)
$$


![The liquid-to-vapor normal fixes the signs of heat and phase flux.](../assets/figures/c2-e21.svg)

The liquid-to-vapor normal fixes the signs of heat and phase flux.

液到汽法向确定热通量及相变通量符号。

For a separate single-component sign control, declare heat supply projected along the liquid-to-vapor normal of 0.95 MW m⁻², zero projected vapor-side conductive loss, and latent enthalpy 95 kJ kg⁻¹. The Stefan flux is 10 kg m⁻² s⁻¹. A stipulated adjacent liquid density of 1000 kg m⁻³ gives liquid velocity slip 0.010 m s⁻¹. This density belongs to the evaporating liquid in this control, not automatically to the aqueous carrier or the PFC interface. With the teaching PFC density 1630 kg m⁻³, the same flux instead gives 0.006135 m s⁻¹ slip at that PFC interface. Reversing the heat supply reverses both flux and slip. This check establishes units and sign; it does not establish actual interface temperature or rate in a PFC nanoemulsion.

对单独的单组分符号对照，声明沿液到汽法向的热供应为 0.95 MW m⁻²、蒸汽侧投影传导损失为零、潜焓为 95 kJ kg⁻¹。Stefan 通量为 10 kg m⁻² s⁻¹。指定相邻液相密度为 1000 kg m⁻³，可得液体速度滑移 0.010 m s⁻¹。此密度属于该对照中发生汽化的液体，并非自动属于水载液或 PFC 界面。若采用教学 PFC 密度 1630 kg m⁻³，同一通量在该 PFC 界面对应的滑移为 0.006135 m s⁻¹。反转热供应，通量及滑移均反向。该检验只确立单位与符号，没有确立 PFC 纳米乳液的真实界面温度或速率。

**Step 20 — apply the first law to the moving bubble.** Choose the vapor domain as a uniform-state open control. Incoming mass carries enthalpy, including the flow work required to enter. Expansion performs pressure work on the surroundings. Conductive heat input is separately counted. The scalar equation below omits resolved internal kinetic energy and surface storage; outgoing mass carries its actual outgoing enthalpy. It requires a consistent boundary state, not one enthalpy assigned indiscriminately to all fluxes.

**步骤 20——对运动气泡应用第一定律。** 选择蒸汽域作为均匀状态的开放控制体。流入质量携带焓，包括进入所需的流动功；膨胀对周围做压力功；传导热输入单独计入。下式标量方程忽略显式内部动能及表面储能；流出质量携带实际流出焓。它要求一致的边界状态，不能对所有通量不加区别地赋予同一个焓。

**Symbols before Eq. (C2-E22).**

**式（C2-E22）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $U_b$ is bubble internal energy (J)<br>$U_b$ 为气泡内能（J） | $\dot Q_b$ is net conductive heat into the bubble (W), excluding transported mass enthalpy<br>$\dot Q_b$ 为进入气泡的净传导热（W），不含随质量输运的焓 |
| $p_b$ is uniform absolute bubble pressure (Pa)<br>$p_b$ 为均匀绝对气泡压力（Pa） | $V_b$ is bubble volume (m³)<br>$V_b$ 为气泡体积（m³） |
| $R>0$ is radius in the spherical control (m)<br>$R>0$ 为球形参照的半径（m） | $h_{v,s}$ is boundary specific vapor enthalpy of species s (J kg⁻¹)<br>$h_{v,s}$ 为组分 s 的边界蒸汽比焓（J kg⁻¹） |
| $\dot m_{v,s}$ is its signed net mass-entry rate (kg s⁻¹)<br>$\dot m_{v,s}$ 为其带符号净流入质量速率（kg s⁻¹） | $s=1,\ldots,N_s$ — Species index, from 1 through the declared species count (dimensionless)<br>$s=1,\ldots,N_s$ — 从 1 到所声明组分数的组分指标（无量纲） |
| $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） | $N_s$ — Number of declared species (dimensionless)<br>$N_s$ — 声明的组分数（无量纲） |

**Conventions and conditions.** $\sum$ is summation; a dot is a time derivative; Distinct entry/exit states require distinct summed boundary terms.

**约定与条件。** $\sum$ 为求和；上点为时间导数；不同流入／流出状态要求分别求和其边界项。

(C2-E22) · Uniform-state open-bubble first-law model / 均匀状态开放气泡的热力学第一定律模型


$$
\dot U_b=\dot Q_b-p_b\dot V_b+\sum_{s=1}^{N_s}h_{v,s}\dot m_{v,s},\qquad V_b=\frac{4\pi}{3}R^3,\qquad\dot V_b=4\pi R^2\dot R
$$


![Mass enthalpy and conductive heat are different terms in the bubble ledger.](../assets/figures/c2-e22.svg)

Mass enthalpy and conductive heat are different terms in the bubble ledger.

质量焓与传导热是气泡账目中的不同项。

**Step 21 — expose the temperature derivative.** For a common bulk temperature and ideal species energies depending only on temperature, differentiate every mass–specific-energy product. The specific heat at constant volume is the derivative of specific internal energy. Subtract the bulk specific internal energy from the boundary specific enthalpy. The difference is pure pressure flow work only when both refer to the same thermodynamic state; when entry temperature differs from bulk temperature, it also includes the boundary-to-bulk sensible internal-energy difference. This expansion makes changing vapor mass visible instead of hiding it in a fitted polytropic exponent.

**步骤 21——展开温度导数。** 对共同体相温度、且理想组分内能只依赖温度的情形，对每个质量乘比内能的乘积求导。定容比热是比内能对温度的导数。从边界比焓中减去体相比内能。只有两者对应同一热力学状态时，差值才纯粹是压力流动功；若流入温度与体相温度不同，差值还包括边界与体相之间的显热内能差。该展开明确显示蒸汽质量变化，而不是将其藏入拟合多方指数。

**Symbols before Eq. (C2-E23).**

**式（C2-E23）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $U_b$ is internal energy (J)<br>$U_b$ 为内能（J） | $m_{v,s}$ is species vapor mass (kg)<br>$m_{v,s}$ 为组分蒸汽质量（kg） |
| $e_s(T_b)$ is specific internal energy using a consistent reference (J kg⁻¹)<br>$e_s(T_b)$ 为采用一致参考的比内能（J kg⁻¹） | $T_b$ is common bubble temperature (K)<br>$T_b$ 为共同气泡温度（K） |
| $c_{v,s}=de_s/dT_b$ is constant-volume specific heat (J kg⁻¹ K⁻¹)<br>$c_{v,s}=de_s/dT_b$ 为定容比热（J kg⁻¹ K⁻¹） | $h_{v,s}$ is actual boundary specific enthalpy (J kg⁻¹)<br>$h_{v,s}$ 为实际边界比焓（J kg⁻¹） |
| $\dot Q_b$ is conductive heat input (W)<br>$\dot Q_b$ 为传导热输入（W） | $p_b$ — Uniform total absolute bubble pressure (Pa)<br>$p_b$ — 均匀总绝对气泡压力（Pa） |
| $V_b$ — Bubble volume (m³)<br>$V_b$ — 气泡体积（m³） | $s=1,\ldots,N_s$ — Species index, from 1 through the declared species count (dimensionless)<br>$s=1,\ldots,N_s$ — 从 1 到所声明组分数的组分指标（无量纲） |
| $N_s$ — Number of declared species (dimensionless)<br>$N_s$ — 声明的组分数（无量纲） |  |

**Conventions and conditions.** a dot denotes a time derivative; $d/dT_b$ is temperature differentiation; Boundary temperature may differ from $T_b$ and must then be used in $h_{v,s}$.

**约定与条件。** 上点表示时间导数；$d/dT_b$ 为温度求导；边界温度可不同于 $T_b$，此时 $h_{v,s}$ 必须使用边界温度。

(C2-E23) · Product-rule derivation of thermal closure / 通过乘积求导法则推导热学闭合关系


$$
\begin{aligned}U_b&=\sum_{s=1}^{N_s}m_{v,s}e_s(T_b),\qquad c_{v,s}=de_s/dT_b,\\\dot U_b&=\left(\sum_s m_{v,s}c_{v,s}\right)\dot T_b+\sum_s e_s\dot m_{v,s},\\\left(\sum_s m_{v,s}c_{v,s}\right)\dot T_b&=\dot Q_b-p_b\dot V_b+\sum_s(h_{v,s}-e_s)\dot m_{v,s}.\end{aligned}
$$


![A variable vapor mass makes a fixed-mass polytropic shortcut conditional.](../assets/figures/c2-e23.svg)

A variable vapor mass makes a fixed-mass polytropic shortcut conditional.

蒸汽质量变化，使固定质量多方捷径只能有条件成立。

The Stefan interface balance and bubble first law must share enthalpy references. The interface heat pays for converting liquid enthalpy into vapor enthalpy; that vapor then enters with its already specified enthalpy. Adding an independent latent source to Eq. (C2-E22) counts the conversion twice. With fixed mass, no conductive heat, and positive expansion rate, the bubble energy decreases. Condensation and cooling can reduce its pressure; if mass exchange is too slow, retained vapor can cushion collapse. Dissolution, permanent gas, and escape each need their own balances.

Stefan 界面平衡与气泡第一定律必须使用共同焓参考。界面热将液体焓转为蒸汽焓，随后蒸汽携带已指定的焓进入气泡。在式（C2-E22）中再添加独立潜热源，会将该转化重复计算。质量固定、无传导热且膨胀速率为正时，气泡能量降低。凝结及冷却可降低压力；若质量交换过慢，保留蒸汽可缓冲塌缩。溶解、永久气体和逸出各需独立守恒式。

A post-nucleation uniform-bubble calculation also needs a nonzero seed volume, initial species masses and temperature, and initial interface shape and velocity. Those inputs must satisfy the original inventory and energy ledger. A fitted probability of onset does not determine them. With no vapor yet present, the liquid heating and activation description applies; do not divide by zero vapor heat capacity to start the uniform-bubble temperature equation.

成核后的均匀气泡计算还需要非零种子体积、初始组分质量与温度、以及初始界面形状与速度。这些输入必须满足原始库存与能量账目。拟合的起始概率并不确定这些量。尚无蒸汽时，应使用液体加热及激活描述；不能除以零蒸汽热容来启动均匀气泡温度方程。

**Step 22 — close pressure with a finite mass and an equation of state.** In a dilute ideal mixture, each partial pressure follows from that species mole number, common temperature, and volume. Sum partial pressures, including noncondensable gas. A real-fluid or mixture equation of state must replace this approximation during high-density compression; neither an Antoine curve nor a fixed polytropic exponent supplies that missing closure.

**步骤 22——用有限质量与状态方程闭合压力。** 在稀薄理想混合物中，每种分压由该组分摩尔数、共同温度及体积决定。各分压求和时包含不可凝气体。高密度压缩时，必须用真实流体或混合物状态方程替代理想近似；Antoine 曲线或固定多方指数均不能补足该缺失闭合。

**Symbols before Eq. (C2-E24).**

**式（C2-E24）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{v,s}$ is ideal partial pressure of species s (Pa), v naming the vapor-domain component<br>$p_{v,s}$ 为组分 s 的理想分压（Pa），v 标记蒸汽域组分 | $V_b>0$ is bubble volume (m³)<br>$V_b>0$ 为气泡体积（m³） |
| $m_{v,s}\ge0$ is its mass (kg)<br>$m_{v,s}\ge0$ 为其质量（kg） | $M_s>0$ is molar mass (kg mol⁻¹)<br>$M_s>0$ 为摩尔质量（kg mol⁻¹） |
| $R_u=8.314462618$ J mol⁻¹ K⁻¹ is the universal gas constant<br>$R_u=8.314462618$ J mol⁻¹ K⁻¹ 为通用气体常数 | $T_b>0$ is bulk temperature (K)<br>$T_b>0$ 为体相温度（K） |
| $p_b$ is total pressure (Pa)<br>$p_b$ 为总压力（Pa） | $s=1,\ldots,N_s$ — Species index, from 1 through the declared species count (dimensionless)<br>$s=1,\ldots,N_s$ — 从 1 到所声明组分数的组分指标（无量纲） |
| $\mathcal P$ is a specified equation-of-state function (—)<br>$\mathcal P$ 为明确的状态方程函数（—） | $\rho_b$ mixture density (kg m⁻³)<br>$\rho_b$ 为混合物密度（kg m⁻³） |
| $e_b$ specific internal energy (J kg⁻¹)<br>$e_b$ 为比内能（J kg⁻¹） | $\boldsymbol Y$ the species mass-fraction vector (dimensionless, entries summing to one)<br>$\boldsymbol Y$ 为组分质量分数向量（无量纲，各分量之和为一） |
| $N_s$ — Number of declared species (dimensionless)<br>$N_s$ — 声明的组分数（无量纲） |  |

**Conventions and conditions.** $\sum$ is summation; EOS means equation of state.

**约定与条件。** $\sum$ 为求和；EOS 指状态方程。

(C2-E24) · Ideal-mixture constitutive control and required refinement / 理想混合物本构对照模型与所需改进


$$
p_{v,s}V_b=\frac{m_{v,s}}{M_s}R_uT_b,\qquad p_b=\sum_{s=1}^{N_s}p_{v,s},\qquad p_b=\mathcal P(\rho_b,e_b,\boldsymbol Y)\quad\text{for a stated real-mixture EOS}
$$


![The pressure responds to species masses, temperature, and changing volume.](../assets/figures/c2-e24.svg)

The pressure responds to species masses, temperature, and changing volume.

压力响应组分质量、温度及体积变化。

**Step 23 — display the three causes of changing partial pressure.** For positive species mass, temperature, pressure, and volume, take the logarithm of the ideal equation and differentiate. The mass, temperature, and compression terms then appear separately. At zero species mass use Eq. (C2-E24) directly instead of taking a logarithm.

**步骤 23——明确分压变化的三个原因。** 当组分质量、温度、压力和体积为正时，对理想方程取对数并求导。质量、温度和压缩项便分别显现。组分质量为零时直接使用式（C2-E24），不要取对数。

**Symbols before Eq. (C2-E25).**

**式（C2-E25）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{v,s}>0$ is species partial pressure (Pa)<br>$p_{v,s}>0$ 为组分分压（Pa） | $m_{v,s}>0$ is its vapor-domain mass (kg), s labeling species<br>$m_{v,s}>0$ 为其蒸汽域质量（kg），s 表示组分 |
| $T_b>0$ is bubble temperature (K)<br>$T_b>0$ 为气泡温度（K） | $V_b>0$ is volume (m³)<br>$V_b>0$ 为体积（m³） |
| $R>0$ is radius for a spherical bubble (m)<br>$R>0$ 为球形气泡半径（m） |  |

**Conventions and conditions.** a dot is a time derivative; Every ratio has units s⁻¹; the final equality uses $V_b=4\pi R^3/3$ and is restricted to spherical geometry.

**约定与条件。** 上点表示时间导数；各比值单位均为 s⁻¹；最后一个等式使用 $V_b=4\pi R^3/3$，仅限球形几何。

(C2-E25) · Derived ideal-pressure evolution identity / 推导得到的理想气体压力演化恒等式


$$
\frac{\dot p_{v,s}}{p_{v,s}}=\frac{\dot m_{v,s}}{m_{v,s}}+\frac{\dot T_b}{T_b}-\frac{\dot V_b}{V_b}=\frac{\dot m_{v,s}}{m_{v,s}}+\frac{\dot T_b}{T_b}-3\frac{\dot R}{R}\quad\text{(sphere)}
$$


![A radius-only gas law hides mass and thermal changes.](../assets/figures/c2-e25.svg)

A radius-only gas law hides mass and thermal changes.

仅由半径决定的气体定律会隐藏质量与热变化。

**Step 24 — cap an equilibrium control by available inventory.** For a closed, nondissolving PFC supply at prescribed temperature and free vapor volume, the saturated vapor mass is pressure times volume divided by the species gas constant and temperature. If that required mass exceeds the original supply, all PFC is vapor and the ideal partial pressure falls below saturation. This algebraic control assumes fast phase equilibration, negligible curved-interface corrections, and thermodynamic coexistence conditions; it is not a nonequilibrium evaporation-rate law.

**步骤 24——以可用库存限制平衡参照。** 对闭合、不溶解的 PFC 供应，在给定温度与自由蒸汽体积下，饱和蒸汽质量等于压力乘体积，再除以组分气体常数与温度。若所需质量超过原供应，PFC 全部成为蒸汽，理想分压低于饱和。该代数参照假设相平衡迅速、曲面界面修正可忽略并满足热力学共存条件；它不是非平衡蒸发速率定律。

**Symbols before Eq. (C2-E26).**

**式（C2-E26）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_{v,\mathrm{eq}}$ is equilibrium PFC vapor mass (kg), eq labeling the restricted equilibrium control<br>$m_{v,\mathrm{eq}}$ 为平衡 PFC 蒸汽质量（kg），eq 标记受限平衡参照 | $m_{\mathrm{PFC},0}$ is finite initial supply (kg)<br>$m_{\mathrm{PFC},0}$ 为有限初始供应（kg） |
| $M_{\mathrm{PFC}}$ is PFC molar mass (kg mol⁻¹)<br>$M_{\mathrm{PFC}}$ 为 PFC 摩尔质量（kg mol⁻¹） | $p_{\mathrm{sat,PFC}}(T_b)$ is bulk saturation pressure (Pa)<br>$p_{\mathrm{sat,PFC}}(T_b)$ 为体相饱和蒸汽压（Pa） |
| $p_{v,\mathrm{PFC,eq}}$ is ideal equilibrium PFC partial pressure (Pa)<br>$p_{v,\mathrm{PFC,eq}}$ 为理想平衡 PFC 分压（Pa） | $T_b>0$ is prescribed temperature (K)<br>$T_b>0$ 为给定温度（K） |
| $V_b>0$ is available vapor volume (m³)<br>$V_b>0$ 为可用蒸汽体积（m³） | $R_u$ is universal gas constant (J mol⁻¹ K⁻¹)<br>$R_u$ 为通用气体常数（J mol⁻¹ K⁻¹） |

**Conventions and conditions.** The supply is closed and nondissolving, and mass exchange is assumed fast; $\min$ selects the lesser nonnegative argument.

**约定与条件。** 供应闭合且不溶解，并假设质量交换迅速；$\min$ 选择较小非负值。

(C2-E26) · Finite-inventory equilibrium benchmark / 有限存量的平衡基准模型


$$
m_{v,\mathrm{eq}}=\min\!\left[m_{\mathrm{PFC},0},\frac{M_{\mathrm{PFC}}p_{\mathrm{sat,PFC}}(T_b)V_b}{R_uT_b}\right],\qquad p_{v,\mathrm{PFC,eq}}=\min\!\left[p_{\mathrm{sat,PFC}}(T_b),\frac{m_{\mathrm{PFC},0}R_uT_b}{M_{\mathrm{PFC}}V_b}\right]
$$


![The saturation branch ends when the finite liquid inventory is exhausted.](../assets/figures/c2-e26.svg)

The saturation branch ends when the finite liquid inventory is exhausted.

有限液体库存耗尽时，饱和分支终止。

## 2.5 A complete single-core numerical benchmark

## 2.5 完整单核心数值参照

Declare a 5 μm initial PFP-like liquid core at 293 K, final reference vapor temperature 323 K, density 1630 kg m⁻³, constant liquid heat capacity 654 J kg⁻¹ K⁻¹, and constant latent enthalpy 95 kJ kg⁻¹. The molar mass is the named PFP value. The size, density, constant transport model, latent value, and final state are teaching inputs. They do not describe a verified nanodroplet formulation. The constant latent enthalpy is not presented as a NIST value at 323 K.

声明一个初始温度 293 K、半径 5 μm 的近似 PFP 液核，最终参照蒸汽温度为 323 K，密度为 1630 kg m⁻³，常液相比热容为 654 J kg⁻¹ K⁻¹，常潜焓为 95 kJ kg⁻¹。摩尔质量采用明确的 PFP 数值。尺寸、密度、常系数传输模型、潜焓值与最终状态都是教学输入，不代表已验证的纳米液滴配方。此常潜焓并未被表述为 323 K 下的 NIST 数值。

**Step 25 — evaluate initial mass.** Cube the radius in meters, multiply by density, and use the sphere-volume factor. One nanogram is $10^{-12}$ kg, not $10^{-9}$ kg.

**步骤 25——计算初始质量。** 将以米计的半径立方，乘密度及球体积系数。一纳克是 $10^{-12}$ kg，而不是 $10^{-9}$ kg。

**Symbols before Eq. (C2-E27).**

**式（C2-E27）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_{\mathrm{PFC},0}$ is initial PFC mass (kg), 0 labeling initial state<br>$m_{\mathrm{PFC},0}$ 为初始 PFC 质量（kg），0 表示初态 | $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** 1630 is density in kg m⁻³; $5\times10^{-6}$ is initial radius in m; the cube is a power; ng denotes nanogram; $1$ ng = $10^{-12}$ kg.

**约定与条件。** 1630 为以 kg m⁻³ 计的密度；$5\times10^{-6}$ 为以 m 计的初始半径；立方表示幂；ng 为纳克；$1$ ng = $10^{-12}$ kg。

(C2-E27) · Finite-mass worked calculation / 有限质量的完整示例计算


$$
m_{\mathrm{PFC},0}=\frac{4\pi}{3}(1630)(5\times10^{-6})^3=8.534660\times10^{-13}\ \mathrm{kg}=0.853466\ \mathrm{ng}
$$


![A mass ledger begins with the actual core volume.](../assets/figures/c2-e27.svg)

A mass ledger begins with the actual core volume.

质量账目从实际核心体积开始。

**Step 26 — estimate preparation enthalpy.** A declared near-constant-pressure path first heats liquid and then converts it to the chosen vapor reference, using constant coefficients. The sensible term is mass times heat capacity times temperature rise; the latent term is mass times latent enthalpy. This is a preparation-energy screen. It omits the detailed pressure path, carrier heating, shell work, gradients, and losses, and is not automatically an activation threshold or jet energy.

**步骤 26——估计制备焓。** 声明一个近恒压路径，先加热液体，再用常系数将其转为所选蒸汽参照。显热项为质量乘比热容乘温升；潜热项为质量乘潜焓。这是制备能量筛选，忽略详细压力路径、载液加热、壳层做功、梯度及损失，不能自动等同于激活阈值或射流能量。

**Symbols before Eq. (C2-E28).**

**式（C2-E28）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $Q_{\mathrm{sens}}$ — Estimated sensible preparation energy (J)<br>$Q_{\mathrm{sens}}$ — 估计的显热制备能量（J） | $Q_{\mathrm{lat}}$ — Estimated latent preparation energy (J)<br>$Q_{\mathrm{lat}}$ — 估计的潜热制备能量（J） |
| $Q_{\mathrm{prep}}$ — Estimated total preparation energy (J)<br>$Q_{\mathrm{prep}}$ — 估计的总制备能量（J） | $m_{\mathrm{PFC},0}$ is mass (kg)<br>$m_{\mathrm{PFC},0}$ 为质量（kg） |
| $c_{p,d}=654$ J kg⁻¹ K⁻¹ is constant liquid heat capacity<br>$c_{p,d}=654$ J kg⁻¹ K⁻¹ 为常液相比热容 | $T_*=323$ K is final reference temperature, star labeling the selected state rather than a critical nucleus<br>$T_*=323$ K 为最终参照温度，此处星号标记所选状态，不是临界汽核 |
| $T_0=293$ K is initial temperature<br>$T_0=293$ K 为初始温度 | $L_v=95000$ J kg⁻¹ is declared latent enthalpy<br>$L_v=95000$ J kg⁻¹ 为声明的潜焓 |

**Conventions and conditions.** nJ means $10^{-9}$ J; $\approx$ denotes the constant-property preparation estimate.

**约定与条件。** nJ 表示 $10^{-9}$ J；$\approx$ 表示常性质制备估计。

(C2-E28) · Declared preparation-path enthalpy estimate / 给定制备路径的焓估算


$$
\begin{aligned}Q_{\mathrm{sens}}&\approx m_{\mathrm{PFC},0}c_{p,d}(T_*-T_0)=(8.534660\times10^{-13})(654)(323-293)=16.7450\ \mathrm{nJ},\\Q_{\mathrm{lat}}&\approx m_{\mathrm{PFC},0}L_v=(8.534660\times10^{-13})(95000)=81.0793\ \mathrm{nJ},\\Q_{\mathrm{prep}}&\approx Q_{\mathrm{sens}}+Q_{\mathrm{lat}}=97.8243\ \mathrm{nJ}.\end{aligned}
$$


![Most of this declared preparation estimate is latent enthalpy.](../assets/figures/c2-e28.svg)

Most of this declared preparation estimate is latent enthalpy.

该制备估计中的大部分能量是潜焓。

**Refinement of the preparation path.** For an equilibrium near-isobaric path with initial subcooled liquid and final superheated vapor, liquid heats only to the saturation temperature at that pressure, then vaporizes, then the vapor heats to its final temperature. Integrate the appropriate phase heat capacities over those separate intervals. The 97.82 nJ screen replaces this full enthalpy path by a constant liquid heat capacity over the whole 30 K rise plus a fixed latent value; it is therefore not an exact endpoint enthalpy. Vapor heat capacity and the actual pressure path are needed to refine it.

**制备路径的改进。** 对初始过冷液体、最终过热蒸汽的近平衡等压路径，液体仅加热到该压力下的饱和温度，随后汽化，最后将蒸汽加热到最终温度。应分别在这些区间积分对应相的比热容。97.82 nJ 筛选用全程 30 K 温升中的常液相比热及固定潜焓替代完整焓路径，因此并非精确端态焓。进一步改进需要蒸汽比热容与实际压力路径。

**Symbols before Eq. (C2-E29).**

**式（C2-E29）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $Q_{\mathrm{iso}}$ is heat needed for the stated constant-pressure preparation path (J), iso labeling isobaric<br>$Q_{\mathrm{iso}}$ 为所述恒压制备路径的需热（J），iso 表示等压 | $m_{\mathrm{PFC},0}$ is conserved PFC mass (kg)<br>$m_{\mathrm{PFC},0}$ 为守恒 PFC 质量（kg） |
| $p$ is prescribed constant pressure (Pa)<br>$p$ 为给定常压力（Pa） | $T_0$ — Initial liquid temperature (K)<br>$T_0$ — 初始液体温度（K） |
| $T_{\mathrm{sat}}$ — Liquid–vapor coexistence temperature at the prescribed pressure (K)<br>$T_{\mathrm{sat}}$ — 给定压力下的液—汽共存温度（K） | $T_*$ — Selected final vapor temperature on the constant-pressure path (K)<br>$T_*$ — 恒压路径上选定的最终蒸气温度（K） |
| $T$ is dummy integration temperature (K)<br>$T$ 为积分哑温度（K） | $c_{p,l}$ — Temperature- and pressure-dependent liquid specific heat at constant pressure (J kg⁻¹ K⁻¹)<br>$c_{p,l}$ — 依赖温度与压力的液体定压比热（J kg⁻¹ K⁻¹） |
| $c_{p,v}$ — Temperature- and pressure-dependent vapor specific heat at constant pressure (J kg⁻¹ K⁻¹)<br>$c_{p,v}$ — 依赖温度与压力的蒸气定压比热（J kg⁻¹ K⁻¹） | $L_v(T_{\mathrm{sat}},p)$ is latent enthalpy at coexistence (J kg⁻¹)<br>$L_v(T_{\mathrm{sat}},p)$ 为共存状态潜焓（J kg⁻¹） |

**Conventions and conditions.** $\int$ denotes temperature integration; No heat losses or other work are included; pressure work is already contained in this enthalpy path.

**约定与条件。** $\int$ 为温度积分；未计入热损失或其他做功；压力功已包含在该焓路径中。

(C2-E29) · Refined constant-pressure enthalpy path / 细化的恒压焓变化路径


$$
Q_{\mathrm{iso}}=m_{\mathrm{PFC},0}\!\left[\int_{T_0}^{T_{\mathrm{sat}}}c_{p,l}(T,p)\,dT+L_v(T_{\mathrm{sat}},p)+\int_{T_{\mathrm{sat}}}^{T_*}c_{p,v}(T,p)\,dT\right],\qquad T_0<T_{\mathrm{sat}}\le T_*
$$


![A rigorous preparation path uses the heat capacity of each phase over its own interval.](../assets/figures/c2-e29.svg)

A rigorous preparation path uses the heat capacity of each phase over its own interval.

严谨制备路径在各相自身温区使用对应比热容。

**Step 27 — find a radius associated with a specified vapor state.** As a separate mass-conservation test, fully vaporize that supply at 323 K and 100 kPa PFC partial pressure using the ideal-vapor control. Equate bubble volume from the gas law to core mass divided by original density times the expansion factor. Cancel the positive sphere factor and cube-root the positive ratio. This computes a state-associated inventory radius; it does not solve the dynamics or give maximum radius.

**步骤 27——求指定蒸汽状态对应的半径。** 作为独立质量守恒检验，采用理想蒸汽参照，将该库存全部汽化至 323 K、PFC 分压 100 kPa。将气体定律的气泡体积与核心质量除以初始密度再乘膨胀倍数相等。约去正的球体积系数，对正比值开立方根。该计算得到状态对应的库存半径，并未求解动力学或最大半径。

**Symbols before Eq. (C2-E30).**

**式（C2-E30）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $R_{b,\mathrm{inv}}>0$ is ideal inventory-state bubble radius (m), b naming bubble and inv naming inventory<br>$R_{b,\mathrm{inv}}>0$ 为理想库存状态气泡半径（m），b 表示气泡，inv 表示库存 | $a_0=5$ μm is initial core radius<br>$a_0=5$ μm 为初始核心半径 |
| $m_{\mathrm{PFC},0}$ is initial mass (kg)<br>$m_{\mathrm{PFC},0}$ 为初始质量（kg） | $\rho_d=1630$ kg m⁻³ is original liquid density<br>$\rho_d=1630$ kg m⁻³ 为初始液体密度 |
| $R_u=8.314462618$ J mol⁻¹ K⁻¹ is gas constant<br>$R_u=8.314462618$ J mol⁻¹ K⁻¹ 为气体常数 | $T_*=323$ K is chosen final reference<br>$T_*=323$ K 为选定最终参照 |
| $M_{\mathrm{PFC}}=0.2880343$ kg mol⁻¹ is PFP molar mass<br>$M_{\mathrm{PFC}}=0.2880343$ kg mol⁻¹ 为 PFP 摩尔质量 | $p_{v,\mathrm{PFC}}=10^5$ Pa is chosen partial pressure<br>$p_{v,\mathrm{PFC}}=10^5$ Pa 为所选分压 |
| $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |  |

**Conventions and conditions.** powers 3 and 1/3 denote cube and positive cube root; The ratio is dimensionless.

**约定与条件。** 幂 3 和 1/3 表示立方及正立方根；该比值无量纲。

(C2-E30) · Derived ideal-vapor inventory radius / 由理想蒸气存量推导的半径


$$
\begin{aligned}\frac{4\pi}{3}R_{b,\mathrm{inv}}^3&=\frac{m_{\mathrm{PFC},0}R_uT_*}{M_{\mathrm{PFC}}p_{v,\mathrm{PFC}}}=\frac{4\pi}{3}\rho_da_0^3\frac{R_uT_*}{M_{\mathrm{PFC}}p_{v,\mathrm{PFC}}},\\\left(\frac{R_{b,\mathrm{inv}}}{a_0}\right)^3&=\frac{\rho_dR_uT_*}{M_{\mathrm{PFC}}p_{v,\mathrm{PFC}}}=151.9778,\\R_{b,\mathrm{inv}}&=a_0(151.9778)^{1/3}=26.6827\ \mu\mathrm m.\end{aligned}
$$


![The expansion ratio follows from mass conservation at a stated pressure and temperature.](../assets/figures/c2-e30.svg)

The expansion ratio follows from mass conservation at a stated pressure and temperature.

膨胀比来自指定压力与温度下的质量守恒。

At 323 K, the 100 kPa PFC reference is below 204.33 kPa saturation. It is fully vaporized and unsaturated, not coexistence with an unlimited liquid reservoir. Its ideal gas law can be checked by inserting the computed radius and recovering 100 kPa. At a larger 30 μm radius and the same temperature, even placing the entire supply in vapor gives only 70.36 kPa PFC partial pressure. Maintaining saturation there would require more PFC than the original core contains. Added water vapor or gas can alter total pressure, but requires its own inventory and energy accounting.

323 K 时，100 kPa 的 PFC 参照低于 204.33 kPa 饱和压力。它是完全汽化、未饱和状态，不是与无限液体库共存。将计算半径代回理想气体定律，可恢复 100 kPa，完成检验。在更大的 30 μm 半径及同温度下，即使全部库存均在蒸汽中，PFC 分压也仅为 70.36 kPa。此时维持饱和将需要超过原核心的 PFC。额外水蒸汽或气体可改变总压力，但必须有各自的库存与能量账目。

**Step 28 — connect the optical and thermal energy screens without claiming an activation threshold.** Declare incident energy 1 μJ, beam radius 20 μm, centered aperture radius 10 μm, absorber thickness 5 μm, absorption coefficient $2\times10^5$ m⁻¹, and reflected fraction 0.10. Calculate the intercepted fraction and absorptance before comparing energy. These values specify a hypothetical slab and are independent of the optical studies cited earlier.

**步骤 28——连接光学与热学能量筛选，不将其声称为激活阈值。** 声明入射能量 1 μJ、光束半径 20 μm、同轴窗口半径 10 μm、吸收层厚度 5 μm、吸收系数 $2\times10^5$ m⁻¹、反射比例 0.10。比较能量前先计算截获比例与吸收率。这些值定义假想薄层，与此前引用的光学研究相互独立。

**Symbols before Eq. (C2-E31).**

**式（C2-E31）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $f_{\mathrm{geo}}$ is interception fraction (dimensionless)<br>$f_{\mathrm{geo}}$ 为截获比例（无量纲） | $A_\lambda$ is effective absorptance at the chosen wavelength $\lambda$ (m)<br>$A_\lambda$ 为所选波长 $\lambda$（m）处的有效吸收率 |
| $E_{\mathrm{abs}}$ is absorbed energy (J)<br>$E_{\mathrm{abs}}$ 为吸收能量（J） | $Q_{\mathrm{prep}}$ is declared preparation-energy estimate (J)<br>$Q_{\mathrm{prep}}$ 为声明的制备能量估计（J） |
| $\eta_{\mathrm{th,min}}$ is the minimum heat-delivery fraction in this loss-excluding estimate, th naming thermal and min minimum (dimensionless)<br>$\eta_{\mathrm{th,min}}$ 为该不含损失估计中的最低热输送比例，th 表示热学，min 表示最低（无量纲） | $\lambda$ — Laser wavelength (m)<br>$\lambda$ — 激光波长（m） |

**Conventions and conditions.** both are dimensionless; The 10 and 20 are aperture and beam radii in the same μm unit; 0.10 is reflection fraction; $2\times10^5$ is absorption coefficient in m⁻¹; $5\times10^{-6}$ is thickness in m; μJ and nJ mean $10^{-6}$ J; $10^{-9}$ J; $e^x$ is the exponential.

**约定与条件。** 两者无量纲；10 和 20 是使用相同 μm 单位的窗口与光束半径；0.10 是反射比例；$2\times10^5$ 是以 m⁻¹ 计的吸收系数；$5\times10^{-6}$ 是以 m 计的厚度；μJ 与 nJ 分别为 $10^{-6}$ J 和 $10^{-9}$ J；$e^x$ 为指数函数。

(C2-E31) · Declared optical-to-heat energy screen / 给定光能转热能过程的能量筛查


$$
\begin{aligned}f_{\mathrm{geo}}&=1-e^{-2(10/20)^2}=0.393469,\\A_\lambda&=(1-0.10)[1-e^{-(2\times10^5)(5\times10^{-6})}]=0.568909,\\E_{\mathrm{abs}}&=(0.393469)(0.568909)(1\ \mu\mathrm J)=223.848\ \mathrm{nJ},\\\eta_{\mathrm{th,min}}&=Q_{\mathrm{prep}}/E_{\mathrm{abs}}=97.8243/223.848=0.437012.\end{aligned}
$$


![The preparation estimate demands at least 43.7% of the declared absorbed energy.](../assets/figures/c2-e31.svg)

The preparation estimate demands at least 43.7% of the declared absorbed energy.

该制备估计要求至少 43.7% 的所声明吸收能量。

If only 20% of this absorbed energy reaches the chosen core, the delivered heat is 44.77 nJ, below the declared 97.82 nJ full-preparation estimate. If 50% reaches it, the 111.92 nJ budget clears that estimate but still does not demonstrate nucleation, spatial uniformity, shell opening, or useful pressure work. With unchanged coefficients and reference states, halving core radius divides mass and preparation enthalpy by eight while preserving the ideal volume expansion factor; its capillary pressure doubles. Thus small size simultaneously changes inventory, heating distance, and confinement.

若仅 20% 吸收能量到达所选核心，所送热量为 44.77 nJ，低于声明的 97.82 nJ 完全制备估计。若达到 50%，111.92 nJ 的预算超过该估计，却仍不能证明成核、空间均温、壳层开启或有用压力功。在系数与参照状态不变时，核心半径减半会使质量与制备焓降为八分之一，同时保持理想体积膨胀倍数；毛细压力却加倍。因此，小尺寸会同时改变库存、加热距离及约束。

**Handoff to the connected calculation.** Chapter 3 repeats this exact 5 μm teaching-core inventory across 25 sites: total PFC mass is 21.3367 ng and the summed preparation screen is 2.44561 μJ. Those totals are a source mass/enthalpy ledger. They are not a freely available 2.44561 μJ jet budget, and the hypothetical optical slab above is not a calibration of those cells. Chapter 3 states the separate-cell assumption and declares any mechanical-conversion fraction before calculating finite emitted liquid mass and energy.

**贯穿算例的交接。** 第三章在 25 个位点重复使用此相同的 5 μm 教学核心库存：PFC 总质量为 21.3367 ng，制备筛选之和为 2.44561 μJ。这些总量是源质量／焓账目，不能当作可自由使用的 2.44561 μJ 射流预算；上面的假想光学薄层也不是这些单元的标定。第三章将明确独立单元假设，并在计算有限喷出液体质量与能量之前声明任何力学转换比例。

**Unresolved project inputs.** To predict a target formulation, identify its PFC compound and purity; size distribution; shell and interfacial laws; absorber spectrum, loading, and location; carrier transport; thermal contact; nucleation or activation statistics; phase kinetics; permanent gas; and a valid high-state EOS. This chapter establishes a consistent theory and verified teaching controls. It does not establish the project’s laser threshold, pressure maximum, or jet velocity. Chapter 3 uses site-specific source histories to analyze arrays and useful output.

**尚未解决的项目输入。** 预测目标配方需要明确 PFC 化合物与纯度、尺寸分布、壳层及界面定律、吸收体光谱／载量／位置、载液传输、热接触、成核或激活统计、相变动力学、永久气体及有效高状态 EOS。本章建立一致理论及已核验教学参照，尚未确立项目激光阈值、最高压力或射流速度。第三章将使用各位点源历程分析阵列及有用输出。

## 2.6 Three research-defense questions

## 2.6 三道研究答辩题

### A PFC formulation absorbs a stronger laser pulse but produces no useful jet. How would you explain and investigate the missing links?

### PFC 配方吸收了更强激光脉冲，却没有产生有用射流。你会如何解释并查明缺失环节？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C2-E32).**

**式（C2-E32）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $E_L$ — Incident laser-pulse energy (J)<br>$E_L$ — 入射激光脉冲能量（J） | $E_{\mathrm{abs}}$ — Absorbed optical energy (J)<br>$E_{\mathrm{abs}}$ — 吸收光能（J） |
| $w>0$ is Gaussian beam radius (m)<br>$w>0$ 为高斯光束半径（m） | $F_0$ is central fluence (J m⁻²)<br>$F_0$ 为中心能量密度（J m⁻²） |
| $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） | $f_{\mathrm{geo}}$ — Intercepted incident-energy fraction (dimensionless)<br>$f_{\mathrm{geo}}$ — 截获的入射能量比例（无量纲） |
| $A_\lambda$ — Effective absorptance of incident light (dimensionless)<br>$A_\lambda$ — 相对于入射光的有效吸收率（无量纲） | $\lambda$ labeling wavelength (m)<br>$\lambda$ 标记波长（m） |
| $t_{\mathrm{th}}$ is diffusion-time estimate (s)<br>$t_{\mathrm{th}}$ 为扩散时间估计（s） | $L_h>0$ is heating distance (m)<br>$L_h>0$ 为加热距离（m） |
| $\alpha>0$ is diffusivity (m² s⁻¹)<br>$\alpha>0$ 为扩散率（m² s⁻¹） | $\tau_h$ is heating duration (s)<br>$\tau_h$ 为加热时长（s） |
| $\delta_T$ is penetration scale (m)<br>$\delta_T$ 为渗透尺度（m） |  |

**Conventions and conditions.** $\sim$ denotes scaling.

**约定与条件。** $\sim$ 表示尺度关系。

(C2-E32) · Original formulas for Defense 1 / 答辩问题 1 的原始公式


$$
E_L=\frac{\pi w^2F_0}{2},\qquad E_{\mathrm{abs}}=f_{\mathrm{geo}}A_\lambda E_L,\qquad t_{\mathrm{th}}\sim L_h^2/\alpha,\qquad\delta_T\sim\sqrt{\alpha\tau_h}
$$


![Original optical and thermal formulas used in the reference answer.](../assets/figures/c2-e32.svg)

Original optical and thermal formulas used in the reference answer.

参考答案使用的原始光学与热学公式。

First identify where light is actually absorbed. At fixed pulse energy, a smaller spot raises local fluence; at fixed fluence, a shorter pulse raises irradiance. Neither operation proves that the PFC receives the heat. The intercepted area, absorption spectrum and thickness, reflection, and absorber location determine the absorber budget. Next compare the distance to the core with thermal penetration during the available event time and account for contact resistance and carrier loss. The 5 μm, 10 ns control has only about 22 nm penetration, so surface heating cannot be declared uniform-core heating. A dispersed absorber changes that geometry and must be resolved or justified.

首先确定光实际在哪里吸收。脉冲能量固定时，较小光斑提高局部能量密度；能量密度固定时，较短脉冲提高辐照度。两者都不能证明 PFC 收到热量。截获面积、吸收光谱与厚度、反射及吸收体位置决定吸收体预算。随后比较到核心的距离与可用事件时长内的热渗透，并考虑接触热阻及载液损失。5 μm、10 ns 参照只有约 22 nm 的渗透，因此不能将表面加热声明为核心均温加热。分散吸收体改变该几何，需要解析或论证。

In the declared example 223.85 nJ is absorbed and about 97.82 nJ is the selected preparation estimate; at least 43.7% heat delivery would be required even before the omitted losses. Passing that screen is not onset proof. Activation, finite phase inventory, pressure work, and directional jet formation follow as separate causal stages. A matched PFC-free control must keep these optical and geometric inputs comparable, rather than attribute an absorber change to PFC chemistry.

在声明示例中，吸收 223.85 nJ，所选制备估计约 97.82 nJ；即使还未计入省略损失，也至少需要 43.7% 热输送。通过该筛选不是起始证明。激活、有限相库存、压力功及定向射流形成是后续独立因果阶段。匹配的不含 PFC 参照必须使这些光学及几何输入可比，不能将吸收体改变归因于 PFC 化学。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Distinguishes incident energy, absorbed energy, irradiance, and heat delivered to PFC; traces absorber location and heat-transfer time.

  区分入射能量、吸收能量、辐照度与送达 PFC 的热量；追踪吸收体位置及热传递时间。
* Explains how spot size, duration, penetration, and a finite energy budget affect the source without calling an energy screen an activation threshold.

  说明光斑、时长、渗透及有限能量预算如何影响源，而不将能量筛选称为激活阈值。
* Identifies activation and geometry-dependent pressure-to-jet conversion as additional stages, and specifies a fair PFC-free comparison.

  指出激活与依赖几何的压力到射流转化是额外阶段，并给出公平的不含 PFC 对照。

### Why can a low-boiling PFC nanodroplet remain liquid during laser heating, and why is one failed activation not evidence of impossibility?

### 为什么低沸点 PFC 纳米液滴在激光加热时仍可能保持液态？为什么一次激活失败不能证明不可能？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C2-E33).**

**式（C2-E33）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_d$ — Initial liquid-PFC core pressure (Pa)<br>$p_d$ — 初始液态 PFC 核压力（Pa） | $p_c$ — Carrier-liquid pressure (Pa)<br>$p_c$ — 载液压力（Pa） |
| $\Pi_{\mathrm{shell}}$ — Shell-supported excess pressure (Pa)<br>$\Pi_{\mathrm{shell}}$ — 壳层支撑超压（Pa） | $a>0$ is core radius (m)<br>$a>0$ 为核心半径（m） |
| $\sigma_{pc}$ is PFC–carrier tension (N m⁻¹)<br>$\sigma_{pc}$ 为 PFC–载液张力（N m⁻¹） | $p_{\mathrm{sat,PFC}}(T_i)$ is equilibrium PFC vapor pressure (Pa) at local interface temperature $T_i$ (K)<br>$p_{\mathrm{sat,PFC}}(T_i)$ 为局部界面温度 $T_i$（K）处的平衡 PFC 蒸汽压（Pa） |
| $\Delta p_n>0$ is nucleation driving pressure (Pa)<br>$\Delta p_n>0$ 为成核驱动压差（Pa） | $\sigma_{vp}>0$ is vapor–PFC tension (N m⁻¹)<br>$\sigma_{vp}>0$ 为蒸汽–PFC 张力（N m⁻¹） |
| $r_*$ is critical nucleus radius (m)<br>$r_*$ 为临界汽核半径（m） | $W_*$ is barrier (J)<br>$W_*$ 为势垒（J） |
| $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） | $T_i$ — Local phase-interface temperature (K)<br>$T_i$ — 局部相界面温度（K） |

**Conventions and conditions.** star labels critical values; $\simeq$ denotes the static core-pressure approximation; Critical formulas assume homogeneous small-nucleus capillarity.

**约定与条件。** 星号标记临界值；$\simeq$ 表示静态核压力近似；临界公式假设均匀小汽核毛细模型。

(C2-E33) · Original formulas for Defense 2 / 答辩问题 2 的原始公式


$$
p_d\simeq p_c+2\sigma_{pc}/a+\Pi_{\mathrm{shell}},\quad \Delta p_n=p_{\mathrm{sat,PFC}}(T_i)-p_d,\quad r_*=2\sigma_{vp}/\Delta p_n,\quad W_*=16\pi\sigma_{vp}^3/(3\Delta p_n^2)\quad(\Delta p_n>0)
$$


![Original confinement and nucleation formulas used in the reference answer.](../assets/figures/c2-e33.svg)

Original confinement and nucleation formulas used in the reference answer.

参考答案使用的原始约束与成核公式。

**Symbols before Eq. (C2-E34).**

**式（C2-E34）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $P_{\mathrm{act}}$ is activation probability (dimensionless)<br>$P_{\mathrm{act}}$ 为激活概率（无量纲） | $J(T,p)\ge0$ is supplied Poisson event rate (m⁻³ s⁻¹), evaluated at local temperature $T$ (K) and pressure $p$ (Pa)<br>$J(T,p)\ge0$ 为给定 Poisson 事件速率（m⁻³ s⁻¹），取局部温度 $T$（K）与压力 $p$（Pa） |
| $V_d(t^{\prime})$ is remaining PFC-liquid region, d labeling droplet (m³)<br>$V_d(t^{\prime})$ 为剩余 PFC 液体区域，d 表示液滴（m³） | $t\ge0$ — Time (s)<br>$t\ge0$ — 时间（s） |
| $dV$ is volume element (m³)<br>$dV$ 为体积元（m³） | $T$ — Thermodynamic temperature (K)<br>$T$ — 热力学温度（K） |
| $p$ — Local or prescribed thermodynamic pressure as specified (Pa)<br>$p$ — 按情景指定的局部或给定热力学压力（Pa） |  |

**Conventions and conditions.** $\int$ is integration; $\exp$ is the natural exponential; Independent events and finite integrated rate are assumed.

**约定与条件。** $\int$ 为积分；$\exp$ 为自然指数函数；假设事件独立且积分速率有限。

(C2-E34) · Original activation-probability formula / 原始激活概率公式


$$
P_{\mathrm{act}}=1-\exp\!\left[-\int_0^t\int_{V_d(t^{\prime})}J(T,p)\,dV\,dt^{\prime}\right]
$$


![The probability formula does not replace the missing material-specific rate.](../assets/figures/c2-e34.svg)

The probability formula does not replace the missing material-specific rate.

概率公式不能替代缺失的材料特定速率。

A low bulk boiling point means bulk liquid and vapor coexist at relatively low temperature and specified pressure. A small coated core has a different liquid pressure because capillarity scales as inverse radius and the shell may add resistance. At 323 K, the declared 5 μm control is at 108 kPa and has positive PFP reference driving, but the 100 nm control is at 500 kPa and does not. Even positive driving leaves a barrier: the internal vapor–PFC tension sets the critical nucleus and must not be replaced by the outer tension. The rate and time in the hot state determine event probability; heterogeneity may require a measured activation law.

低体相沸点意味着在明确压力下，体相液体和蒸汽能在较低温度共存。小包覆核心的液体压力不同，因为毛细压力与半径成反比，且壳层可能增加阻力。323 K 时，声明的 5 μm 参照位于 108 kPa，具有正 PFP 参照驱动力；100 nm 参照位于 500 kPa，则没有。即使驱动力为正，势垒仍存在：内部蒸汽–PFC 张力决定临界汽核，不能由外界面张力替换。速率及热状态持续时间决定事件概率；异质过程可能需要测量激活定律。

No activation in one exposure can mean insufficient heat, unfavorable confinement, a low probability, or an unsuitable nucleation site, not necessarily impossibility. A simulation seeded after onset answers what follows that seed and must not be described as predicting the optical threshold. Useful tests separately observe absorbed energy, onset statistics, core or shell state, and bubble evolution under the same exposure.

一次照射未激活，可能意味着热量不足、约束不利、概率低或成核位点不合适，不一定意味着不可能。起始后给种子的模拟只回答该种子后续怎样，不能称为预测光学阈值。有用检验应在同样照射下分别观测吸收能量、起始统计、核心或壳层状态及气泡演化。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Explains bulk saturation versus the pressure inside a finite core, including inverse-radius capillarity and shell stress.

  解释体相饱和与有限核心内部压力的区别，包含反半径毛细压力及壳层应力。
* Distinguishes the PFC–carrier and vapor–PFC tensions and explains the positive-driving branch, barrier, and finite hot-state duration.

  区分 PFC–载液与蒸汽–PFC 张力，并解释正驱动分支、势垒及有限热状态时长。
* Treats activation statistically when appropriate and separates seeded dynamics from a demonstrated onset prediction.

  适当时以统计过程看待激活，并区分种子后的动力学与已证明的起始预测。

### How would you build a mass- and energy-consistent PFC pressure history, and why is its inventory radius neither a maximum bubble radius nor a jet-speed prediction?

### 你会如何建立质量与能量一致的 PFC 压力历程？为什么库存半径既不是最大气泡半径，也不是射流速度预测？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C2-E35).**

**式（C2-E35）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_{\mathrm{PFC},0}$ is initial PFC mass (kg)<br>$m_{\mathrm{PFC},0}$ 为初始 PFC 质量（kg） | $\rho_d$ is initial liquid density (kg m⁻³)<br>$\rho_d$ 为初始液体密度（kg m⁻³） |
| $a_0$ is initial core radius (m)<br>$a_0$ 为初始核心半径（m） | $m_l$ — Remaining liquid-PFC mass (kg)<br>$m_l$ — 剩余液态 PFC 质量（kg） |
| $m_v$ — PFC vapor mass (kg)<br>$m_v$ — PFC 蒸气质量（kg） | $m_{\mathrm{diss}}$ — Dissolved PFC mass (kg)<br>$m_{\mathrm{diss}}$ — 溶解 PFC 质量（kg） |
| $m_{\mathrm{esc}}$ — Cumulative escaped PFC mass (kg)<br>$m_{\mathrm{esc}}$ — 累计逸出 PFC 质量（kg） | $p_{v,\mathrm{PFC}}$ is ideal PFC partial pressure (Pa)<br>$p_{v,\mathrm{PFC}}$ 为理想 PFC 分压（Pa） |
| $V_b>0$ is bubble volume (m³)<br>$V_b>0$ 为气泡体积（m³） | $M_{\mathrm{PFC}}$ is molar mass (kg mol⁻¹)<br>$M_{\mathrm{PFC}}$ 为摩尔质量（kg mol⁻¹） |
| $R_u$ is universal gas constant (J mol⁻¹ K⁻¹)<br>$R_u$ 为通用气体常数（J mol⁻¹ K⁻¹） | $T_b>0$ is bulk temperature (K)<br>$T_b>0$ 为体相温度（K） |
| $\pi$ is the circular constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |  |

**Conventions and conditions.** 0 denotes initial state and other subscripts name compartments; No external compound supply is allowed.

**约定与条件。** 0 表示初态，其余下标标记分区；不允许外部化合物供应。

(C2-E35) · Original inventory and pressure formulas for Defense 3 / 答辩问题 3 的原始存量与压力公式


$$
m_{\mathrm{PFC},0}=\frac{4\pi}{3}\rho_da_0^3,\qquad m_l+m_v+m_{\mathrm{diss}}+m_{\mathrm{esc}}=m_{\mathrm{PFC},0},\qquad p_{v,\mathrm{PFC}}V_b=\frac{m_v}{M_{\mathrm{PFC}}}R_uT_b
$$


![Original finite-inventory formulas used in the reference answer.](../assets/figures/c2-e35.svg)

Original finite-inventory formulas used in the reference answer.

参考答案使用的原始有限库存公式。

**Symbols before Eq. (C2-E36).**

**式（C2-E36）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $j_s$ is signed phase flux (kg m⁻² s⁻¹)<br>$j_s$ 为带符号相变通量（kg m⁻² s⁻¹） | $L_{v,s}$ is latent enthalpy (J kg⁻¹)<br>$L_{v,s}$ 为潜焓（J kg⁻¹） |
| $\boldsymbol q_l$ — Liquid-side conductive heat flux (W m⁻²)<br>$\boldsymbol q_l$ — 液体侧传导热通量（W m⁻²） | $\boldsymbol q_v$ — Vapor-side conductive heat flux (W m⁻²)<br>$\boldsymbol q_v$ — 蒸气侧传导热通量（W m⁻²） |
| $\boldsymbol n$ is unit liquid→vapor normal (dimensionless)<br>$\boldsymbol n$ 为液→汽单位法向（无量纲） | $U_b$ is bubble internal energy (J)<br>$U_b$ 为气泡内能（J） |
| $\dot Q_b$ is conductive heat input excluding mass enthalpy (W)<br>$\dot Q_b$ 为不含质量焓的传导热输入（W） | $p_b$ is pressure (Pa)<br>$p_b$ 为压力（Pa） |
| $V_b$ is volume (m³)<br>$V_b$ 为体积（m³） | $h_{v,s}$ is boundary specific vapor enthalpy (J kg⁻¹)<br>$h_{v,s}$ 为边界蒸汽比焓（J kg⁻¹） |
| $m_{v,s}$ is species mass (kg)<br>$m_{v,s}$ 为组分质量（kg） | $R$ is spherical bubble radius (m)<br>$R$ 为球形气泡半径（m） |
| $\dot R$ its wall speed (m s⁻¹)<br>$\dot R$ 为壁速（m s⁻¹） | $u_l(R)$ adjacent radial liquid speed (m s⁻¹)<br>$u_l(R)$ 为邻接径向液速（m s⁻¹） |
| $\rho_l$ liquid density (kg m⁻³)<br>$\rho_l$ 为液体密度（kg m⁻³） |  |

**Conventions and conditions.** $\sum_s$ sums all declared species; A dot is a time derivative and $\cdot$ is a vector dot product; Interface heat and slip formulas assume the stated single-component reduced jump.

**约定与条件。** $\sum_s$ 对所有声明组分求和；上点表示时间导数，$\cdot$ 表示向量点积；界面热及滑移公式采用所声明单组分简化跳跃假设。

(C2-E36) · Original phase-energy and velocity-slip formulas / 原始相变能量与速度滑移公式


$$
j_sL_{v,s}=(\boldsymbol q_l-\boldsymbol q_v)\cdot\boldsymbol n,\qquad\dot U_b=\dot Q_b-p_b\dot V_b+\sum_s h_{v,s}\dot m_{v,s},\qquad u_l(R)=\dot R-j_s/\rho_l
$$


![Original conservation formulas prevent unlimited vapor and duplicated latent energy.](../assets/figures/c2-e36.svg)

Original conservation formulas prevent unlimited vapor and duplicated latent energy.

原始守恒公式防止无限蒸汽及重复潜热计入。

Begin with the measured or declared core mass and conserve it across liquid, vapor, dissolved, and escaped compartments. The ideal PFC partial pressure follows from vapor mass, temperature, and volume; total pressure also includes water vapor and permanent gas. Saturation is only an equilibrium branch when enough liquid and fast heat/mass exchange sustain it. Once all PFC has vaporized, expansion lowers its pressure at fixed temperature. The 5 μm control contains only 0.8535 ng and gives a 26.68 μm inventory radius at 323 K and 100 kPa, not a dynamical maximum. At 30 μm it can supply only 70.36 kPa PFC partial pressure in that ideal control.

应从测得或声明的核心质量出发，在液体、蒸汽、溶解与逸出分区间守恒。理想 PFC 分压由蒸汽质量、温度及体积决定；总压力还包含水蒸汽与永久气体。只有液体足够、热质交换快速时，饱和才是可维持的平衡分支。PFC 全部汽化后，在温度固定时膨胀使其压力降低。5 μm 参照仅含 0.8535 ng，在 323 K、100 kPa 下得到 26.68 μm 库存半径，而不是动力学最大值。在 30 μm 时，该理想参照仅能提供 70.36 kPa PFC 分压。

Next use the Stefan balance to determine signed evaporation or condensation from interface heat, and use the open first law for pressure work and transported enthalpy. Do not add latent heating a second time. Phase change can make wall speed differ from liquid speed; a simple RP closure must check slip and recoil. Rapid compression can retain nonequilibrium vapor, and permanent gas persists after condensation. A high-state real EOS, thermal transport, and resolved geometry are necessary refinements. The useful jet remains predominantly carrier liquid and requires Chapter 1/3’s mechanical and directional closure; an inventory expansion ratio is not a jet-speed prediction.

随后用 Stefan 平衡根据界面热确定带符号蒸发或凝结，用开放第一定律计入压力功及输运焓；不能再计一次潜热。相变可使壁速不同于液速，简单 RP 闭合必须检查滑移与反冲。快速压缩可保留非平衡蒸汽，凝结后永久气体仍在。高状态真实 EOS、热传输及解析几何是必要改进。有用射流仍主要是载液，需要第一／三章的力学与方向闭合；库存膨胀比不是射流速度预测。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Conserves finite PFC across all relevant compartments and explains when saturation can and cannot be sustained.

  在所有相关分区间守恒有限 PFC，并说明饱和何时可维持、何时不能。
* Explains signed Stefan transfer, open-system enthalpy and pressure work, and avoids duplicated latent heat; recognizes phase-change velocity slip.

  解释带符号 Stefan 传输、开放系统焓与压力功，并避免重复潜热；认识相变速度滑移。
* Separates assumed inventory state from nonlinear dynamics and useful carrier-jet output; identifies retained vapor, gas, and EOS limits.

  区分假定库存状态、非线性动力学及有用载液射流输出；指出残留蒸汽、气体及 EOS 限制。