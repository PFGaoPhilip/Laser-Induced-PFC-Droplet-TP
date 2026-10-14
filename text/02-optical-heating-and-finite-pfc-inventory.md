# Chapter 2: Optical heating and finite PFC inventory

# 第 2 章：光学加热与有限 PFC 物质量

## 2. Optical heating and finite PFC inventory

## 2. 光学加热与有限 PFC 物质量

Calculate the pressure history of one laser-heated PFC inclusion. Chapter 1 derived the response to prescribed internal pressure. This chapter supplies absorption, heating, activation, mass and energy balances. The emitted jet usually consists mainly of carrier liquid. Use PFC density for core inventory and carrier density for inertia. Lower activation threshold leaves emitted momentum and transfer repeatability unresolved.

本章计算单个激光加热 PFC 夹杂的压力历程。第一章推导给定内压下的响应，本章补充吸收、加热、激活、质量和能量平衡。喷出射流通常主要由载液组成。核心物质量采用 PFC 密度，惯性采用载液密度。较低激活阈值仍不能确定喷出动量与转印重复性。

**System and conventions.** Place an initially liquid spherical PFC core in aqueous carrier. Initial temperature is $T_0$ (K); carrier pressure is $p_c$ (Pa). Beam depth $z$ (m) increases along propagation. Transverse radius $r$ (m) measures distance from its axis. Time $t=0$ (s) precedes the pulse. Prescribe entering intensity and initial temperature field. Symmetry gives zero center heat flux. Specify an outer reservoir or resolve the surrounding carrier. Enforce contact flux continuity and the chosen contact law. Thermodynamic pressures are absolute. Unit normal $\boldsymbol n$ points from liquid into vapor. Positive flux denotes evaporation. Inside a bubble, this normal opposes outward radial unit vector $\boldsymbol e_r$.

**体系与约定。** 初始液态球形 PFC 核位于水相载液中。初温为 $T_0$（K），载液压力为 $p_c$（Pa）。光束深度 $z$（m）沿传播方向增加。横向半径 $r$（m）为距光轴距离。$t=0$（s）位于脉冲之前。给定入射强度与初始温度场。中心对称性给出零热通量。外边界采用指定热库，或解析周围载液。材料接触处满足通量连续及所选接触规律。热力学压力均为绝对压力。单位法向 $\boldsymbol n$ 从液体指向蒸气，正通量表示蒸发。气泡内部的该法向与向外径向单位矢量 $\boldsymbol e_r$ 相反。

**Approximation sequence.** The optical model neglects scattering and nonlinear absorption. Pre-phase heating omits pressure work and viscous heat in nearly incompressible phases. Nucleation assumes local isothermality and a nucleus much smaller than the liquid core. Uniform-bubble closure assumes common temperature and a dilute ideal mixture. Each approximation has its own validity range. The micron-sized teaching core does not represent a nanodroplet.

**近似顺序。** 光学模型忽略散射与非线性吸收。相变前的近不可压缩相加热忽略压力功和黏性热。成核假设局部等温且汽核远小于液核。均匀气泡闭合假设共同温度及稀薄理想混合物。每项近似均有独立适用范围。微米教学核心不代表纳米液滴。

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

Match a PFC-free aqueous control to the PFC case. Keep outer geometry, absorber location, absorbed energy and initial state comparable. Also match outlet and target load path. Simultaneous absorber or spot-size changes confound the material comparison. Measure activation, emitted mass and speed, useful impulse, intact yield and reset. Retained vapor can ease activation while cushioning later collapse.

将不含 PFC 的水相对照与 PFC 情形匹配。保持外部几何、吸收体位置、吸收能量和初态可比，并匹配出口及目标传力路径。同时改变吸收体或光斑会混淆材料比较。测量激活、喷出质量与速率、有用冲量、完整转印率及复位。残留蒸气可促进激活，同时缓冲后续塌缩。

## 2.1 Incident and absorbed energy

## 2.1 入射与吸收能量

**Step 1 — Define Gaussian fluence.** Fluence integrates irradiance over time. Specify its transverse profile. Define beam radius at the $e^{-2}$ level whenever quoting spot size.

**步骤 1——定义高斯能量面密度。** 能量面密度为辐照度的时间积分。先规定横向分布。标注光斑尺寸时，采用 $e^{-2}$ 水平定义光束半径。

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

**Step 2 — Integrate the beam plane.** The annular area is $2\pi r\,dr$. Substitute $x=2r^2/w^2$, giving $dx=4r\,dr/w^2$. Limits remain zero and infinity. The integral converges. The exponential decays to zero at infinity.

**步骤 2——积分光束平面。** 环形面积为 $2\pi r\,dr$。令 $x=2r^2/w^2$，则 $dx=4r\,dr/w^2$。积分限仍为零与无穷远。积分收敛，指数函数在无穷远趋零。

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

**Step 3 — Calculate intercepted energy.** End the same integral at centered aperture radius $b_a$ (m). Divide by total beam energy. Off-axis or irregular absorbers require their actual area integral.

**步骤 3——计算截获能量。** 将同一积分上限取为居中孔径半径 $b_a$（m），再除以总光束能量。偏轴或不规则吸收体须按实际区域积分。

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

**Step 4 — Include pulse duration.** Normalize the temporal pulse shape to unit integral. A rectangular pulse has height equal to reciprocal duration. Shorter duration raises irradiance at fixed fluence. Incident energy stays fixed.

**步骤 4——加入脉冲时长。** 将时间脉冲形状归一化为单位积分。矩形脉冲高度等于时长的倒数。能量面密度固定时，缩短时长会提高辐照度，入射能量保持不变。

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

**Step 5 — Solve absorption transport.** Irradiance loss across a slab equals deposited heat per volume × thickness. Assume constant positive absorption coefficient. Separate and integrate from entry face to depth, then exponentiate. Optical transit is instantaneous relative to thermal evolution.

**步骤 5——求解吸收输运。** 薄层辐照度损失等于单位体积沉积热量乘以厚度。假设吸收系数为正常数。分离变量，从入射面积分至指定深度，再取指数。相对于热演化，将光传播视为瞬时过程。

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

**Step 6 — Integrate deposited heat.** Integrate the volume source over depth to obtain absorbed power/area. Integrate pulse time and intercepted area to obtain energy. Apply the entering fraction from front-face reflection once. The defined effective absorptance already contains that reflection.

**步骤 6——积分沉积热。** 对体积源沿深度积分，得到单位面积吸收功率。再对脉冲时间及截获面积积分，得到能量。前表面反射造成的入射比例计入一次。所定义有效吸收率已包含该反射。

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

Absorptance approaches zero at zero optical thickness. At large thickness, it approaches the entering fraction. $Q_{\mathrm{abs}}$ has units W m⁻³; its volume–time integral has units J. Scattering, multiple reflection, saturation and plasma formation require other models. A boundary source can replace an equivalent resolved layer. Including both duplicates the deposited energy.

光学厚度趋零时，吸收率趋零。厚度很大时，吸收率趋于进入比例。$Q_{\mathrm{abs}}$ 单位为 W m⁻³，其体积—时间积分为 J。散射、多次反射、饱和及等离子体形成需其他模型。等效边界热源可替代解析层，同时加入两者会重复计入能量。

Strohm et al. optically activated PbS-loaded PFP at 1064 nm. Wei et al. used gold-containing PFH nanoemulsion. These studies establish formulation-specific optical activation routes. Universal threshold, jet speed and transfer yield remain unestablished. Absorber placement and formulation require experimental inputs. [[R6]](../reference/sources.html#r6) [[R7]](../reference/sources.html#r7)

Strohm 等用 1064 nm 激光激活含 PbS 的 PFP。Wei 等采用含金 PFH 纳米乳液。这些研究确立了特定配方的光学激活路径。通用阈值、射流速率及转印率尚未确立。吸收体位置与配方须由实验给定。 [[R6]](../reference/sources.html#r6) [[R7]](../reference/sources.html#r7)

## 2.2 Heat delivery and event time

## 2.2 热输送与事件时间

**Step 7 — Conserve thermal energy.** Before phase change, conduction and absorption change sensible enthalpy. Assume constant properties in nearly incompressible phases. Omit viscous heating and pressure work. Use near-constant-pressure heat capacity. Moving liquid advects heat; a solid absorber has zero velocity. Conductive flux points down the temperature gradient. Its negative divergence supplies heat influx.

**步骤 7——热能守恒。** 相变前，传导与吸收改变显焓。近不可压缩相采用常物性，忽略黏性热与压力功，使用近恒压热容。运动液体对流输热，固体吸收体速度为零。传导热通量指向温度降低方向，其负散度表示热流入。

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

**Step 8 — Close thermal contacts.** Orient the normal from material A into B. Positive normal heat flux travels from A to B. Without surface heat storage, flux is continuous. Nonnegative contact resistance permits a temperature jump. Zero resistance gives temperature continuity. This contact differs from the phase-change interface below.

**步骤 8——闭合热接触。** 法向从材料 A 指向 B，正法向热通量由 A 流向 B。无界面热储存时，通量连续。非负接触热阻允许温度跳跃，零热阻给出温度连续。该接触不同于下文相变界面。

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

**Step 9 — Derive diffusion scales.** Divide the motionless heat equation by volumetric heat capacity. Estimate its time derivative and spatial second derivative over the heating distance. Balance them to obtain diffusion time and penetration length. These are scales rather than sharp thermal fronts. Heating duration may include conduction after the optical pulse.

**步骤 9——推导扩散尺度。** 将静止介质热方程除以体积热容。按加热距离估算时间导数与空间二阶导数。平衡两者，得到扩散时间和渗透长度。它们是尺度估计，并非尖锐热前沿。加热时长可包含光脉冲之后的传导。

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

**Thermal example.** Prescribe density 1630 kg m⁻³, heat capacity 654 J kg⁻¹ K⁻¹, and conductivity 0.050 W m⁻¹ K⁻¹. The rounded near-293 K heat capacity uses the cited NIST datum. Density and conductivity are teaching inputs. Heating distance is 5 μm; duration is 10 ns.

**热学示例。** 规定密度 1630 kg m⁻³、热容 654 J kg⁻¹ K⁻¹、导热率 0.050 W m⁻¹ K⁻¹。近 293 K 的舍入热容采用所引 NIST 数据。密度与导热率为教学输入。加热距离为 5 μm，时长为 10 ns。

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

Penetration is 0.00433 of the heating distance. Uniform core temperature requires distributed heating or additional diffusion time. At 100 nm, the diffusion estimate falls to 0.213 μs. That still exceeds 10 ns. Hotspots, aggregation and shell contact can dominate local heating. Optical breakdown requires its own optical conditions and observations.

渗透长度为加热距离的 0.00433 倍。核心均温需要分布式加热或额外扩散时间。距离降至 100 nm 时，扩散估计降至 0.213 μs，仍长于 10 ns。热点、团聚和壳层接触可主导局部加热。光学击穿需独立的光学条件及观测依据。

## 2.3 Vapor pressure, confinement and activation

## 2.3 蒸气压、约束与激活

**Step 10 — Set initial core pressure.** A spherical PFC–carrier interface creates capillary pressure. Add shell-supported overpressure when present. This static reference omits acceleration and shell-rate effects. Those require a dynamic constitutive law.

**步骤 10——规定初始核心压力。** 球形 PFC—载液界面产生毛细压力。存在壳层承压时，加上壳层过压。静态参照忽略加速度与壳层速率效应，后者需动力学本构规律。

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

Specify the compound for every quoted boiling point. NIST entries below describe neat compounds. Tabulated boiling ranges represent different datasets, not formulation uncertainty. Divide molar heat capacity or enthalpy by molar mass for mass-specific values. [[R8]](../reference/sources.html#r8) [[R9]](../reference/sources.html#r9) [[R15]](../reference/sources.html#r15)

每个沸点须注明具体化合物。下列 NIST 条目描述纯物质。表中沸点范围来自不同数据集，并非配方不确定度。摩尔热容或焓除以摩尔质量，得到质量比值。 [[R8]](../reference/sources.html#r8) [[R9]](../reference/sources.html#r9) [[R15]](../reference/sources.html#r15)

| Compound and identity<br>化合物与身份 | Bulk reference<br>体相参照 | Proper scope<br>正确用途 |
| --- | --- | --- |
| PFP: C₅F₁₂; CAS 678-26-2; molar mass 0.2880343 kg mol⁻¹<br>PFP：C₅F₁₂；CAS 678-26-2；摩尔质量 0.2880343 kg mol⁻¹ | Normal-boiling entries 302.6–303.2 K; liquid heat-capacity datum 188.3 J mol⁻¹ K⁻¹ at 293 K, giving 653.74 J kg⁻¹ K⁻¹.<br>正常沸点条目 302.6–303.2 K；293 K 液体热容数据为 188.3 J mol⁻¹ K⁻¹，对应 653.74 J kg⁻¹ K⁻¹。 | Compound-specific thermal reference; not a coated-droplet activation law.<br>特定化合物热学参照；不是包覆液滴激活定律。 |
| PFH: C₆F₁₄; CAS 355-42-0; molar mass 0.3380418 kg mol⁻¹<br>PFH：C₆F₁₄；CAS 355-42-0；摩尔质量 0.3380418 kg mol⁻¹ | Normal-boiling entries 330.3–333 K; vaporization enthalpy 31.5 kJ mol⁻¹ at 316 K, giving 93.18 kJ kg⁻¹.<br>正常沸点条目 330.3–333 K；316 K 汽化焓为 31.5 kJ mol⁻¹，对应 93.18 kJ kg⁻¹。 | Retain temperature and dataset; do not transfer this value to every PFC.<br>保留温度及数据集；不能将此值套用到所有 PFC。 |
| Water: H₂O; molar mass 0.0180153 kg mol⁻¹<br>水：H₂O；摩尔质量 0.0180153 kg mol⁻¹ | Normal-boiling compilation approximately 373.17 K.<br>正常沸点汇编约为 373.17 K。 | PFC-free thermal comparison at matched temperature and pressure.<br>在相同温度与压力下的不含 PFC 热学参照。 |

**Step 11 — Evaluate equilibrium vapor pressure.** Use the NIST Barber–Cady Antoine fit within its temperature range. Pressure divided by one bar makes the logarithm dimensionless. The coefficients are empirical inputs. [[R8]](../reference/sources.html#r8)

**步骤 11——计算平衡蒸气压。** 在温度适用范围内采用 NIST Barber–Cady Antoine 拟合。压力除以一 bar，使对数自变量无量纲。系数为经验输入。 [[R8]](../reference/sources.html#r8)

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

Eq. (C2-E12) gives PFP pressures of 70.60 kPa at 293 K, 103.35 kPa at 303 K, and 204.33 kPa at 323 K. Use water coefficients within their stated interval. They give 2.315 kPa at 293 K and 12.248 kPa at 323 K. These are calculated reference values. [[R15]](../reference/sources.html#r15)

式（C2-E12）给出 PFP 蒸气压：293 K 时 70.60 kPa，303 K 时 103.35 kPa，323 K 时 204.33 kPa。水系数须在注明温区内使用。所得值为 293 K 时 2.315 kPa、323 K 时 12.248 kPa。这些是计算参照值。 [[R15]](../reference/sources.html#r15)

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

At 323 K and 100 kPa carrier pressure, the 5 μm core has 108 kPa liquid pressure. This is below the 204.33 kPa PFP equilibrium reference. The 100 nm core has 500 kPa liquid pressure, above that reference. Bulk driving is positive for the larger core and nonpositive for the smaller core. This control assumes constant tension and zero shell stress. Measured onset temperatures remain unestablished.

在 323 K、载液压力 100 kPa 下，5 μm 核心液压为 108 kPa，低于 204.33 kPa 的 PFP 平衡参照。100 nm 核心液压为 500 kPa，高于该参照。大核心体相驱动为正，小核心驱动不为正。此对照假设张力恒定、壳层应力为零。实测起始温度尚未确立。

**Step 12 — Construct nucleus free energy.** Place a vapor nucleus inside liquid PFC. Assume local isothermality and a bulk liquid reservoir. New interface costs tension × area. Favorable vapor gains driving pressure × volume. Use vapor–PFC tension for this internal interface. Eq. (C2-E11) uses PFC–carrier tension at the outer interface.

**步骤 12——建立汽核自由能。** 汽核位于液态 PFC 内部。假设局部等温与体相液体储库。新界面消耗张力 × 面积，有利蒸气获得驱动压差 × 体积。内部界面采用蒸气—PFC 张力。式（C2-E11）外界面采用 PFC—载液张力。

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

**Step 13 — Find the critical branch.** Differentiate both radius powers. For positive driving, divide the nonzero-radius bracket by positive driving pressure. The second derivative is negative at the critical radius. It is a barrier maximum. For nonpositive driving, the derivative stays positive at positive radius. No positive critical-radius branch exists in that case.

**步骤 13——求临界分支。** 对两个半径幂求导。正驱动时，将非零半径括号除以正驱动压差。临界半径处二阶导数为负，对应势垒最大值。驱动不为正时，所有正半径处导数为正，因此不存在正临界半径分支。

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

**Step 14 — Evaluate the barrier.** Substitute the squared and cubed critical radius. Subtract the coefficients explicitly. Increasing driving pressure lowers the barrier. Finite positive driving and tension leave a positive barrier.

**步骤 14——计算势垒。** 代入临界半径的平方与三次方，并明确相减系数。增大驱动压差会降低势垒。有限正驱动与正张力仍给出正势垒。

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

The barrier unit is $\mathrm{(N/m)^3/Pa^2=N\,m=J}$. Tension/pressure gives critical-radius units m. A nucleus comparable to core size violates the reservoir approximation. Surfaces, defects, dissolved gas and wetting can favor heterogeneous nucleation. An imposed seed defines post-nucleation dynamics. Onset prediction then remains unestablished.

势垒单位为 $\mathrm{(N/m)^3/Pa^2=N\,m=J}$。张力／压力给出临界半径单位 m。汽核接近核心尺寸时，储库近似失效。表面、缺陷、溶解气体与润湿可促进异质成核。人为种子规定成核后的动力学，起始预测仍未确立。

**Step 15 — Derive activation probability.** Assume independent Poisson events. In a short interval, survival loses event expectation × current survival. Integrate the logarithmic derivative from initial survival one. Spatially and temporally varying rates fit this model. The rate itself requires a separate law. Use measured activation behavior when homogeneous nucleation is unsuitable.

**步骤 15——推导激活概率。** 假设独立 Poisson 事件。短时间内，存活概率减少量为事件期望数乘当前存活概率。从初始存活概率一积分对数导数。模型允许速率随时空变化。速率本身需独立规律。均质成核不适用时，应采用测量激活规律。

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

## 2.4 Phase mass and energy balances

## 2.4 相质量与能量平衡

**Step 16 — Conserve PFC inventory.** Initial mass equals liquid density × core volume. Without external supply, liquid, vapor, dissolved and escaped PFC sum to that mass. Escaped mass is cumulative. It differs from vapor retained inside the bubble. Water supplies no additional PFC.

**步骤 16——PFC 物质量守恒。** 初始质量等于液体密度 × 核心体积。无外部供给时，液体、蒸气、溶解及逸出 PFC 之和等于初始质量。逸出质量按累计记账，与气泡内保留蒸气不同。水不能补充 PFC。

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

**Step 17 — Identify the phase-change surface.** Integrate species flux over its contacted interface. Full spherical area requires full species contact and uniform flux. Residual PFC in water can have a smaller vaporization surface.

**步骤 17——确定相变表面。** 在组分实际接触的界面上积分通量。采用完整球面面积需该组分接触全表面且通量均匀。水中残留 PFC 可具有更小汽化表面。

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

**Step 18 — Derive velocity slip.** A single-component phase boundary has equal mass flux on both sides. Inside a bubble, the liquid-to-vapor normal points inward. Project liquid velocity minus interface velocity onto that normal. The result is wall speed minus radial liquid speed. Solve for liquid speed. Equating potential-flow speed to wall speed then assumes small slip.

**步骤 18——推导速度滑移。** 单组分相界面两侧质量通量相等。气泡内液体指向蒸气的法向朝内。将液体速度减界面速度投影至该法向，得到壁面速度减径向液速。由此求液速。将势流液速等同壁速需要小滑移假设。

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

Require $|j_s|/\rho_l$ below a relevant liquid or interface speed scale. At a turning point, use finite event speed instead of zero wall speed. Strong evaporation can add recoil stress. Check it before reusing Chapter 1’s simple wall stress. Mixtures require species diffusion, composition conditions and common mass balance.

要求 $|j_s|/\rho_l$ 小于相关液体或界面速率尺度。转折点处采用有限事件速率，避免除以零壁速。强蒸发可增加反冲应力。复用第一章简单壁面应力前须检验反冲。混合物需要组分扩散、组成条件和共同质量平衡。

**Step 19 — Derive the Stefan sign.** Omit surface heat storage and kinetic/mechanical jump corrections. Liquid-side conductive influx minus vapor-side outflux supplies phase-change enthalpy. Evaluate both enthalpies at matching temperature and reference conventions. Reversing heat supply gives negative flux. Condensation then releases latent enthalpy.

**步骤 19——推导 Stefan 符号。** 忽略界面热储存及动能、力学跳跃修正。液侧传导流入减汽侧流出，供给相变焓。两侧焓采用一致温度与参考约定。反转供热会产生负通量，凝结释放潜焓。

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

For a sign control, prescribe normal heat supply 0.95 MW m⁻², zero vapor-side loss, and latent enthalpy 95 kJ kg⁻¹. Stefan flux is 10 kg m⁻² s⁻¹. With adjacent density 1000 kg m⁻³, slip is 0.010 m s⁻¹. With PFC density 1630 kg m⁻³, slip is 0.006135 m s⁻¹. Density belongs to the actual evaporating phase. Reversing heat reverses flux and slip. This checks units and sign. Actual nanoemulsion interface state remains unestablished.

符号对照给定法向供热 0.95 MW m⁻²、汽侧损失为零、潜焓 95 kJ kg⁻¹。Stefan 通量为 10 kg m⁻² s⁻¹。邻接密度取 1000 kg m⁻³ 时，滑移为 0.010 m s⁻¹。PFC 密度取 1630 kg m⁻³ 时，滑移为 0.006135 m s⁻¹。密度应属于实际蒸发相。反转供热会反转通量与滑移。这检验单位与符号。实际纳米乳液界面状态尚未确立。

**Step 20 — Apply the bubble first law.** Use a uniform-state open vapor control volume. Incoming mass carries enthalpy, including entry flow work. Expansion performs work on the surroundings. Count conductive heat separately. Omit resolved internal kinetic energy and surface storage. Outgoing mass carries its own boundary enthalpy. Each flux requires a consistent boundary state.

**步骤 20——应用气泡第一定律。** 将蒸气作为均匀状态开放控制体。流入质量携带焓，包括进入所需流动功。膨胀对外做功，传导热单独计入。忽略解析内部动能和界面储存。流出质量携带其边界焓。各通量均需一致边界状态。

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

**Step 21 — Expand the temperature derivative.** Assume common temperature and ideal species energies dependent on temperature. Differentiate each mass × specific-energy product. Constant-volume specific heat is the specific-energy derivative. Subtract bulk internal energy from boundary enthalpy. This gives pressure flow work when both states match. Different entry temperature adds a sensible internal-energy difference. The expansion retains changing vapor mass explicitly.

**步骤 21——展开温度导数。** 假设共同温度，理想组分内能随温度变化。对各质量 × 比内能乘积求导。定容比热等于比内能温度导数。边界焓减去体相比内能，在状态一致时给出压力流动功。入口温度不同时，还包含显内能差。展开式明确保留蒸气质量变化。

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

Use consistent enthalpy references in Stefan and bubble balances. Interface heat creates the specified incoming vapor enthalpy. Adding another latent source to Eq. (C2-E22) duplicates that conversion. Fixed-mass adiabatic expansion lowers bubble energy. Cooling and condensation can lower pressure. Slow mass exchange can retain vapor and cushion collapse. Dissolution, permanent gas and escape need separate balances.

Stefan 与气泡平衡采用一致焓参考。界面热产生指定的流入蒸气焓。再向式（C2-E22）加入潜热源会重复计入转化。固定质量绝热膨胀降低气泡能量。冷却与凝结可降低压力。质量交换慢时可保留蒸气并缓冲塌缩。溶解、非凝结气体及逸出需独立平衡。

Specify nonzero seed volume, species masses and temperature after nucleation. Also specify initial interface shape and velocity. All seeds must satisfy inventory and energy balances. Onset probability leaves these states unresolved. Before vapor appears, use liquid heating and activation equations. Zero vapor heat capacity excludes starting with the bubble temperature equation.

成核后须指定非零种子体积、组分质量和温度，以及初始界面形状和速度。所有种子均须满足物质与能量平衡。起始概率不能确定这些状态。蒸气出现前采用液体加热及激活方程。蒸气热容为零时，不能用气泡温度方程启动。

**Step 22 — Close pressure with an EOS.** In a dilute ideal mixture, each partial pressure follows species moles, common temperature and volume. Sum all species, including permanent gas. High-density compression requires a real-fluid or mixture EOS. Antoine saturation and a fixed polytropic exponent leave that state closure unresolved.

**步骤 22——用状态方程闭合压力。** 稀薄理想混合物中，各分压由组分摩尔数、共同温度和体积决定。求和所有组分，包括非凝结气体。高密度压缩需要真实流体或混合物状态方程。Antoine 饱和关系与固定多方指数不能闭合该状态。

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

**Step 23 — Separate pressure-change terms.** Require positive species mass, temperature, pressure and volume. Take the ideal-law logarithm and differentiate. The terms represent mass change, temperature change and compression. At zero species mass, use Eq. (C2-E24) directly.

**步骤 23——分离压力变化项。** 要求组分质量、温度、压力及体积为正。对理想定律取对数并求导，分离质量变化、温度变化及压缩项。组分质量为零时，直接采用式（C2-E24）。

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

**Step 24 — Limit saturation by inventory.** Prescribe temperature and free vapor volume in a closed nondissolving control. Saturated mass equals pressure × volume/(gas constant × temperature). If it exceeds supply, all PFC vaporizes and partial pressure falls below saturation. Assume rapid equilibrium, negligible curvature corrections and coexistence conditions. This algebra supplies an equilibrium control, not a rate law.

**步骤 24——用物质量限制饱和。** 在封闭、无溶解对照中给定温度及自由蒸气体积。饱和质量等于压力 × 体积／（气体常数 × 温度）。所需质量超过供给时，PFC 全部汽化，分压低于饱和。假设快速平衡、曲率修正可忽略并满足共存条件。该代数关系是平衡对照，并非速率规律。

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

## 2.5 Single-core numerical example

## 2.5 单核心数值示例

Prescribe a 5 μm PFP-like liquid core at 293 K. Final vapor reference temperature is 323 K. Use density 1630 kg m⁻³, liquid heat capacity 654 J kg⁻¹ K⁻¹, and latent enthalpy 95 kJ kg⁻¹. Molar mass is the named PFP value. Size, density, constant coefficients and final state are teaching inputs. The latent value is not a 323 K NIST datum. Verified nanoformulation properties remain unestablished.

规定 293 K、半径 5 μm 的类 PFP 液核。最终蒸气参照温度为 323 K。采用密度 1630 kg m⁻³、液体热容 654 J kg⁻¹ K⁻¹、潜焓 95 kJ kg⁻¹。摩尔质量采用具名 PFP 数值。尺寸、密度、常系数及最终状态为教学输入。潜焓并非 323 K 的 NIST 数据。已验证纳米配方物性尚未确立。

**Step 25 — Calculate initial mass.** Cube radius in meters. Multiply by density and the sphere-volume factor. One nanogram equals $10^{-12}$ kg.

**步骤 25——计算初始质量。** 将以米计的半径取三次方，乘以密度和球体积系数。一纳克等于 $10^{-12}$ kg。

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

**Step 26 — Estimate preparation enthalpy.** Prescribe heating followed by vaporization near constant pressure. Use constant heat capacity and latent enthalpy. Sensible energy equals mass × heat capacity × temperature rise. Latent energy equals mass × latent enthalpy. This screen omits pressure-path detail, carrier heat, shell work, gradients and losses. Activation threshold and jet energy remain unestablished.

**步骤 26——估算制备焓。** 规定近恒压下先加热再汽化，采用恒定热容和潜焓。显热等于质量 × 热容 × 温升，潜热等于质量 × 潜焓。该筛选省略详细压力路径、载液加热、壳层功、梯度及损失。激活阈值与射流能量尚未确立。

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

**Refine the enthalpy path.** At near-constant pressure, heat subcooled liquid to saturation. Vaporize it, then heat vapor to the final temperature. Integrate each phase heat capacity over its own interval. The 97.82 nJ screen instead applies liquid heat capacity over 30 K plus fixed latent enthalpy. Exact endpoint enthalpy requires vapor heat capacity and the actual pressure path.

**细化焓路径。** 近恒压下先将过冷液体加热至饱和，再汽化，然后将蒸气加热至最终温度。分别在各温区积分对应相热容。97.82 nJ 筛选则在整个 30 K 温升使用液体热容，再加固定潜焓。精确终态焓需要蒸气热容及实际压力路径。

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

**Step 27 — Calculate an inventory radius.** Fully vaporize the supply at 323 K and 100 kPa PFC partial pressure. Use the ideal-vapor control. Equate gas-law volume to initial volume × expansion factor. Cancel the positive sphere factor and take the positive cube root. The resulting radius belongs to the prescribed state. Dynamical maximum remains unestablished.

**步骤 27——计算物质量对应半径。** 在 323 K、PFC 分压 100 kPa 下完全汽化该供给，采用理想蒸气对照。令气体定律体积等于初始体积乘膨胀倍数。约去正球体系数并取正立方根。所得半径属于指定状态。动力学最大值尚未确立。

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

At 323 K, 100 kPa lies below PFP saturation at 204.33 kPa. The control is fully vaporized and unsaturated. Substituting its computed radius into the ideal law recovers 100 kPa. At 30 μm, the entire inventory supplies 70.36 kPa PFC pressure. Sustained saturation there requires more PFC. Water vapor or gas adds pressure with separate mass and energy balances.

323 K 时，100 kPa 低于 PFP 饱和压 204.33 kPa。对照完全汽化且未饱和。将所得半径代回理想定律可恢复 100 kPa。30 μm 时，全部物质量提供 70.36 kPa PFC 分压。维持该尺寸饱和需要更多 PFC。水蒸气或气体可增加压力，但需独立质量与能量平衡。

**Step 28 — Compare absorbed and preparation energies.** Prescribe incident energy 1 μJ and beam radius 20 μm. Use centered aperture radius 10 μm, thickness 5 μm, absorption coefficient $2\times10^5$ m⁻¹, and reflection 0.10. Calculate interception and absorptance first. This hypothetical slab is independent of the cited activation experiments.

**步骤 28——比较吸收与制备能量。** 规定入射能量 1 μJ、光束半径 20 μm。居中孔径半径为 10 μm，厚度 5 μm，吸收系数 $2\times10^5$ m⁻¹，反射比例 0.10。先计算截获与吸收率。该假想薄层独立于所引激活实验。

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

At 20% delivery, core heat is 44.77 nJ, below 97.82 nJ. At 50%, 111.92 nJ clears that screen. Nucleation, uniformity, shell opening and useful work remain unestablished. With fixed coefficients and states, halving radius reduces mass and preparation enthalpy eightfold. Ideal expansion factor stays fixed; capillary pressure doubles. Size changes inventory, diffusion distance and confinement together.

20% 输送时，核心热量为 44.77 nJ，低于 97.82 nJ。50% 时，111.92 nJ 超过筛选值。成核、均温、壳层开启及有用功尚未确立。系数与状态固定时，半径减半使质量与制备焓降至八分之一。理想膨胀倍数不变，毛细压力加倍。尺寸同时改变物质量、扩散距离与约束。

**Use in Chapter 3.** Twenty-five identical 5 μm cores contain 21.3367 ng PFC. Their preparation screens sum to 2.44561 μJ. These totals describe source mass and enthalpy. Available jet energy requires a separate conversion calculation. The optical slab above does not calibrate those cells. Chapter 3 states cell separation and conversion assumptions before calculating output.

**第三章的应用。** 二十五个相同 5 μm 核心含 21.3367 ng PFC，制备筛选值合计 2.44561 μJ。这些总量描述源质量和焓。可用射流能量需另算转换。上文光学薄层没有标定这些单元。第三章先规定单元分隔及转换假设，再计算输出。

**Missing formulation inputs.** Specify compound, purity, size distribution, shell and interface laws. Measure absorber spectrum, loading, location and thermal contact. Supply carrier transport, activation statistics, phase kinetics, permanent gas and high-state EOS. Project threshold, pressure maximum and jet velocity: Not established. Chapter 3 uses specified site histories for array calculations.

**缺失配方输入。** 须规定化合物、纯度、尺寸分布、壳层及界面规律。测量吸收体光谱、载量、位置及热接触。给出载液输运、激活统计、相变动力学、非凝结气体及高状态状态方程。项目阈值、最高压力和射流速率尚未确立。第三章采用规定的位点历程计算阵列。

## 2.6 Oral questions

## 2.6 口头问题

### Absorption increases, but no useful jet forms. Which links would you investigate?

### 吸收增加，却未形成有用射流。你会检验哪些环节？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

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

Locate the absorber first. A smaller spot raises fluence at fixed energy. A shorter pulse raises irradiance at fixed fluence. Heat reaching PFC depends on interception, spectrum, thickness, reflection and absorber position. Compare core distance with thermal penetration and include contact resistance. The 5 μm, 10 ns control penetrates about 22 nm. Surface heating leaves uniform core temperature unestablished. Distributed absorbers require their actual deposition geometry.

先确定吸收体位置。能量固定时，小光斑提高能量面密度；面密度固定时，短脉冲提高辐照度。到达 PFC 的热取决于截获、光谱、厚度、反射和吸收体位置。比较核心距离与热渗透，并计入接触热阻。5 μm、10 ns 对照渗透约 22 nm。表面加热下核心均温尚未确立。分布吸收体需采用实际沉积几何。

The example absorbs 223.85 nJ against a 97.82 nJ preparation screen. Delivery must exceed 43.7% before additional losses. Passing this screen leaves onset unresolved. Activation, phase inventory, pressure work and jet direction require separate calculations. Match optical and geometric inputs in the PFC-free control.

示例吸收 223.85 nJ，制备筛选为 97.82 nJ。未计额外损失时，输送比例已须超过 43.7%。通过筛选仍未确定起始。激活、相变物质量、压力功及射流方向需分别计算。不含 PFC 对照须匹配光学与几何输入。

#### Review criteria

#### 审阅标准

* Distinguishes incident energy, absorbed energy, irradiance, and heat delivered to PFC; traces absorber location and heat-transfer time.

  区分入射能量、吸收能量、辐照度与送达 PFC 的热量；追踪吸收体位置及热传递时间。
* Explains how spot size, duration, penetration, and a finite energy budget affect the source without calling an energy screen an activation threshold.

  说明光斑、时长、渗透及有限能量预算如何影响源，而不将能量筛选称为激活阈值。
* Identifies activation and geometry-dependent pressure-to-jet conversion as additional stages, and specifies a fair PFC-free comparison.

  指出激活与依赖几何的压力到射流转化是额外阶段，并给出公平的不含 PFC 对照。

### Explain confinement and activation probability in a low-boiling nanodroplet.

### 解释低沸点纳米液滴中的约束及激活概率。

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

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

Bulk boiling describes coexistence at specified pressure. Core pressure also includes inverse-radius capillarity and shell stress. At 323 K, the 5 μm control has positive PFP driving at 108 kPa. The 100 nm control has nonpositive driving at 500 kPa. Positive driving still leaves a nucleation barrier. Internal vapor–PFC tension sets that barrier. Rate and hot-state duration determine activation probability. Heterogeneous systems may need measured activation laws.

体相沸腾描述指定压力下的共存。核心压力还包含反半径毛细压力及壳层应力。323 K 时，5 μm 对照在 108 kPa 具有正 PFP 驱动，100 nm 对照在 500 kPa 的驱动不为正。正驱动仍有成核势垒，势垒由内部蒸气—PFC 张力决定。速率与热态时长决定激活概率。异质系统可能需测量激活规律。

One failed exposure can reflect insufficient heat, confinement, low probability or unsuitable nucleation sites. A seeded simulation predicts evolution from its prescribed seed. Optical onset remains unestablished. Measure absorbed energy, onset statistics, shell/core state and bubble evolution under matched exposure.

单次失败可由热量不足、约束、低概率或不合适成核位点导致。种子模拟预测从指定种子开始的演化。光学起始仍未确立。应在匹配照射下测量吸收能量、起始统计、壳层／核心状态及气泡演化。

#### Review criteria

#### 审阅标准

* Explains bulk saturation versus the pressure inside a finite core, including inverse-radius capillarity and shell stress.

  解释体相饱和与有限核心内部压力的区别，包含反半径毛细压力及壳层应力。
* Distinguishes the PFC–carrier and vapor–PFC tensions and explains the positive-driving branch, barrier, and finite hot-state duration.

  区分 PFC–载液与蒸汽–PFC 张力，并解释正驱动分支、势垒及有限热状态时长。
* Treats activation statistically when appropriate and separates seeded dynamics from a demonstrated onset prediction.

  适当时以统计过程看待激活，并区分种子后的动力学与已证明的起始预测。

### Build a conserving pressure history. What does an inventory radius establish?

### 建立守恒的压力历程。物质量对应半径能确立什么？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

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

Conserve measured or declared PFC across liquid, vapor, dissolved and escaped compartments. Ideal PFC pressure follows vapor mass, temperature and volume. Total pressure also includes water vapor and permanent gas. Sustained saturation needs liquid supply and rapid heat/mass exchange. Once fully vaporized, fixed-temperature expansion lowers PFC pressure. The 5 μm core contains 0.8535 ng. Its 323 K, 100 kPa inventory radius is 26.68 μm. At 30 μm, its ideal PFC pressure is 70.36 kPa. Dynamical maximum remains unestablished.

在液体、蒸气、溶解及逸出分区间守恒测得或声明的 PFC。理想 PFC 压力由蒸气质量、温度和体积决定。总压还含水蒸气及非凝结气体。持续饱和需液体供给和快速传热传质。全部汽化后，恒温膨胀降低 PFC 压力。5 μm 核心含 0.8535 ng。323 K、100 kPa 下物质量对应半径为 26.68 μm。30 μm 时理想 PFC 分压为 70.36 kPa。动力学最大值尚未确立。

Use Stefan balance for signed phase flux. Use the open first law for work and transported enthalpy. Count phase conversion once. Check slip and recoil before using simple Rayleigh–Plesset closure. Rapid compression can retain vapor; permanent gas persists after condensation. Refine high-state EOS, thermal transport and geometry as needed. Chapters 1 and 3 determine directional carrier motion. Inventory expansion leaves jet speed unresolved.

采用 Stefan 平衡计算带符号相变通量，用开放第一定律计入功和输运焓。相变转化计入一次。使用简单 Rayleigh–Plesset 闭合前须检查滑移与反冲。快速压缩可保留蒸气，凝结后非凝结气体仍存在。按需细化高状态状态方程、热输运与几何。第一、三章确定载液定向运动。物质量膨胀仍未确定射流速率。

#### Review criteria

#### 审阅标准

* Conserves finite PFC across all relevant compartments and explains when saturation can and cannot be sustained.

  在所有相关分区间守恒有限 PFC，并说明饱和何时可维持、何时不能。
* Explains signed Stefan transfer, open-system enthalpy and pressure work, and avoids duplicated latent heat; recognizes phase-change velocity slip.

  解释带符号 Stefan 传输、开放系统焓与压力功，并避免重复潜热；认识相变速度滑移。
* Separates assumed inventory state from nonlinear dynamics and useful carrier-jet output; identifies retained vapor, gas, and EOS limits.

  区分假定库存状态、非线性动力学及有用载液射流输出；指出残留蒸汽、气体及 EOS 限制。