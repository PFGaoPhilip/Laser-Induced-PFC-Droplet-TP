# Chapter 1: Cavity pressure, carrier inertia and directional jets

# 第 1 章：空腔压力、载液惯性与定向射流

## 1.1 Cavity growth, collapse and ejection

## 1.1 空腔增长、塌缩与喷射

This chapter derives how a cavity accelerates the surrounding liquid. It then identifies the boundaries needed to direct a jet. A PFC droplet starts as a finite liquid inventory. A bubble contains vapor, permanent gas, or both. Their radii measure different objects. Remaining PFC mass requires a separate inventory balance.

本章推导空腔如何加速周围液体，并确定射流定向所需的边界。PFC 液滴起初具有有限的液体物质量。气泡含蒸气、非凝结气体或两者。两者半径描述不同对象。剩余 PFC 质量需要单独的物质平衡。

Pressure reduction and thermal vaporization can each create a moving cavity. Here, laser-induced cavitation covers heating, activation, growth, collapse and possible jetting. Identify the activation mechanism for each case. Chapter 2 supplies absorption, heat transfer, nucleation and phase inventory. This chapter takes internal pressure as a prescribed input.

降压与热汽化均可产生运动空腔。这里的激光诱导空化包括加热、激活、增长、塌缩及可能的射流。每个情形都需明确激活机制。第二章给出吸收、传热、成核与相变物质量。本章将内部压力作为给定输入。

| Mechanism<br>机制 | Moving liquid and boundary<br>运动液体与边界 | What establishes the classification<br>判定依据 |
| --- | --- | --- |
| Expansion-driven ejection<br>膨胀驱动喷射 | The growing cavity displaces carrier toward an outlet or meniscus; the emitted jet is outside the cavity.<br>增长空腔将载液推向出口或弯月面；喷出射流位于空腔之外。 | Track cavity growth and the outgoing liquid together.<br>同时追踪空腔增长与向外喷出的液体。 |
| Collapse-driven re-entrant jet<br>塌缩驱动的再入射流 | An asymmetric liquid interface penetrates the collapsing cavity and can strike its opposite side or a wall.<br>非对称液体界面穿入塌缩空腔，可撞击另一侧界面或壁面。 | Show penetration into the cavity; do not rename it an external transfer jet.<br>观测射流穿入空腔；不能直接把它称为外部转印射流。 |
| Sealed-cavity inflation<br>密闭空腔膨胀 | Pressure deforms an intact membrane or stamp; liquid need not cross a gap.<br>压力使完整膜或印章变形；液体不必跨越间隙。 | Locate the closed boundary and the transmitted deformation.<br>确定封闭边界及其传递的变形。 |
| Liquid-bridge stretching<br>液桥拉伸 | A moving solid pulls a filament; the filament need not originate as a cavitation jet.<br>运动固体拉出液丝；液丝不一定起源于空化射流。 | Establish which moved first: the liquid tip or the solid.<br>辨明最先运动的是液体前端还是固体。 |

Mechanism identification requires the cavity boundary and liquid trajectories. Also track the outlet, receiver and event order. A bright cavity and detached payload leave the mechanism unresolved. The cited meniscus and collapse studies use different geometries. Apply their results after matching the boundary conditions. [[R3]](../reference/sources.html#r3) [[R4]](../reference/sources.html#r4)

判断机制需要观测空腔边界和液体轨迹，还需追踪出口、受载表面和事件顺序。明亮空腔与脱离载荷不足以确定机制。所引弯月面与塌缩研究采用不同几何。应用其结果前须匹配边界条件。 [[R3]](../reference/sources.html#r3) [[R4]](../reference/sources.html#r4)

**Chapter route.** Sections 1.2–1.5 establish radial motion, energy, and collapse time. Section 1.6 connects pressure history to directed liquid motion. Section 1.7 supplies the spatial interface model. Section 1.8 connects these results in the reference answers.

**本章路线。** 第1.2至1.5节建立径向运动、能量与塌缩时间。第1.6节将压力历程连接至定向液体运动。第1.7节给出空间界面模型。第1.8节在参考答案中贯通这些结果。

## 1.2 Spherical model and conventions

## 1.2 球形模型与约定

Model one spherical cavity in an infinite incompressible Newtonian carrier. Fix its center. Radius increases outward into the liquid. Positive wall velocity means expansion. Density, viscosity and effective surface tension remain constant. Omit gravity, bulk vorticity, phase-transfer velocity slip and gas viscous stress. Internal pressure is spatially uniform and may vary with time. The model describes one transient without periodic acoustic forcing.

模型为无限不可压缩牛顿载液中的单个球形空腔。中心固定，径向坐标向液体外侧增加。正壁面速度表示膨胀。密度、黏度和有效表面张力保持恒定。忽略重力、体内涡量、相变速度滑移及气相黏性应力。内部压力空间均匀，可随时间变化。模型描述单次瞬态，不施加周期声驱动。

| Symbol<br>符号 | Physical meaning<br>物理意义 | SI units<br>SI 单位 | Role and convention<br>作用与约定 |
| --- | --- | --- | --- |
| $t$ | Elapsed time<br>经过时间 | s | Independent time coordinate; the initial instant is t = 0.<br>独立时间坐标；初始时刻取 t = 0。 |
| $r$ | Liquid radial coordinate<br>液体径向坐标 | m | Distance from the fixed cavity center to an observation point in the carrier; r ≥ R.<br>从固定空腔中心到载液中观察点的距离；r ≥ R。 |
| $R$ | Instantaneous cavity radius<br>瞬时空腔半径 | m | Locates the moving liquid–bubble interface; it is not the initial PFC-core radius.<br>定位运动的液体—气泡界面；并非初始 PFC 核半径。 |
| $\dot R$ | Wall radial velocity<br>壁面径向速度 | m s⁻¹ | First time derivative of R; positive means expansion and negative means collapse.<br>R 对时间的一阶导数；正值表示膨胀，负值表示塌缩。 |
| $\ddot R$ | Wall radial acceleration<br>壁面径向加速度 | m s⁻² | Second time derivative of R; its sign describes velocity change, not motion direction alone.<br>R 对时间的二阶导数；其符号描述速度变化，不能单独代表运动方向。 |
| $R_0$ | Prescribed initial cavity radius<br>给定初始空腔半径 | m | Positive initial value R(0); a state input to the mechanical model.<br>正的初始值 R(0)；是力学模型的状态输入。 |
| $U_0$ | Initial wall velocity<br>初始壁面速度 | m s⁻¹ | Prescribed value of the first time derivative of R at the initial instant.<br>初始时刻给定的 R 的一阶时间导数。 |
| $\rho$ | Carrier mass density<br>载液质量密度 | kg m⁻³ | Sets surrounding-liquid inertia; it must not be replaced by PFC vapor density.<br>决定周围液体的惯性；不能替换成 PFC 蒸气密度。 |
| $\mu$ | Carrier dynamic viscosity<br>载液动力黏度 | Pa s | Newtonian stress coefficient; viscous resistance dissipates energy in either motion direction.<br>牛顿流体应力系数；黏性阻力在两个运动方向均耗散能量。 |
| $\sigma$ | Effective bubble–carrier surface tension<br>有效气泡—载液表面张力 | N m⁻¹ | Belongs to the specified interface; contributes the spherical capillary pressure 2σ/R.<br>属于指定界面；产生球形毛细压力 2σ/R。 |
| $p_b$ | Uniform bubble absolute pressure<br>均匀气泡绝对压力 | Pa | Pressure on the cavity side of the interface; its history is supplied here.<br>界面空腔侧压力；本章将其时间历程作为输入。 |
| $p_l$ | Adjacent-liquid absolute pressure<br>邻近液体绝对压力 | Pa | Liquid-side pressure at the moving interface; stress balance relates it to bubble pressure.<br>运动界面的液体侧压力；通过应力平衡与泡内压力关联。 |
| $p_\infty$ | Far-field absolute pressure<br>远场绝对压力 | Pa | Pressure prescribed far from the cavity; pressure differences drive acceleration.<br>远离空腔处的给定压力；加速度由压力差驱动。 |
| $p$ | Liquid pressure field<br>液体压力场 | Pa | Pressure at a general liquid observation point, evaluated at the stated position and time.<br>指定位置与时间的普通液体观察点压力。 |
| $u$ | Scalar radial carrier velocity<br>标量载液径向速度 | m s⁻¹ | Positive outward from the center; differs from the spatial velocity vector below.<br>从中心向外取正；与下文空间速度矢量区别使用。 |
| $C(t)$ | Radial volume-flux factor<br>径向体积流量因子 | m³ s⁻¹ | Continuity makes r²u independent of r; this function is not a material constant.<br>连续性使 r²u 与 r 无关；该函数并非材料常数。 |
| $\phi$ | Velocity potential<br>速度势 | m² s⁻¹ | Its spatial derivative gives radial velocity; the reference value is fixed at infinity.<br>其空间导数给出径向速度；参考值固定在无穷远。 |
| $V_b$ | Cavity volume<br>空腔体积 | m³ | Geometric volume enclosed by the bubble boundary; pressure work uses its rate of change.<br>气泡边界围成的几何体积；压力功使用其变化率。 |
| $K_l$ | Carrier kinetic energy<br>载液动能 | J | Integrates motion throughout the exterior liquid, rather than mass inside the bubble.<br>对外部液体的运动进行积分，而不是计算气泡内部质量。 |
| $E_\sigma$ | Interfacial energy<br>界面能 | J | Surface tension multiplied by spherical interface area under the constant-tension assumption.<br>在张力恒定假设下，等于表面张力乘球形界面面积。 |
| $R_{\max}$ | Radius at the start of ideal collapse<br>理想塌缩开始时的半径 | m | Maximum cavity radius with zero initial wall velocity in the Rayleigh control.<br>Rayleigh 对照中壁面初始速度为零时的最大空腔半径。 |
| $p_v$ | Stipulated constant vapor pressure<br>假定恒定蒸气压 | Pa | Ideal-collapse internal-pressure input; real thermal or finite-inventory evolution may change it.<br>理想塌缩的内部压力输入；实际热过程或有限存量变化可能改变它。 |
| $\Delta p_c$ | Positive ideal-collapse pressure difference<br>正的理想塌缩压差 | Pa | Defined as far-field pressure minus the stipulated vapor pressure in this control.<br>在该对照中定义为远场压力减去假定蒸气压。 |
| $t_c$ | Ideal collapse time<br>理想塌缩时间 | s | Time from the initial maximum radius to the excluded zero-radius limit of the ideal model.<br>从初始最大半径到理想模型所排除的零半径极限的时间。 |
| $E_B$ | Displaced-volume pressure-work scale<br>排开体积的压力功尺度 | J | Uses the stated pressure difference and initial cavity volume; not an assigned jet energy.<br>由所声明压差与初始空腔体积构成；并非预设的射流能量。 |
| $\boldsymbol x$ | Spatial position vector<br>空间位置矢量 | m | Locates a point in the nonspherical liquid domain.<br>定位非球形液体域中的一点。 |
| $\boldsymbol u$ | Spatial carrier velocity vector<br>空间载液速度矢量 | m s⁻¹ | Contains direction and spatial variation needed for a jet; scalar wall speed is insufficient.<br>包含射流所需的方向与空间变化；标量壁面速度不足以替代它。 |
| $\Pi$ | Pressure impulse per unit area<br>单位面积压力冲量 | Pa s | Time integral of the specified excess pressure; its gradient changes liquid velocity.<br>指定超压对时间的积分；其梯度改变液体速度。 |
| $\Gamma$ | Moving liquid–gas interface<br>运动液—气界面 | — | Geometric surface, not fracture energy; its position evolves with the interface condition.<br>几何曲面，不是断裂能；其位置按界面条件演化。 |
| $\boldsymbol n$ | Liquid-to-gas unit normal<br>液体指向气体的单位法向 | 1 | Fixes traction and signed-curvature conventions; reversing it changes those signs.<br>确定牵引与带符号曲率约定；反转法向会改变相关符号。 |
| $\kappa$ | Signed sum of principal curvatures<br>带符号的两主曲率之和 | m⁻¹ | For the stated liquid-to-gas normal on a spherical cavity, κ = −2/R.<br>对于所声明的球形空腔液体指向气体法向，κ = −2/R。 |

Superscripts denote powers unless stated otherwise. Bold symbols denote vectors or tensors. π is the dimensionless circle constant. Gradient, divergence and Laplacian use Cartesian definitions. Partial time derivatives hold position fixed. Each display defines its symbols locally. The positive initial radius permits division by radius. Zero radius is an excluded limit.

除非另行说明，上标表示幂，粗体表示矢量或张量。π 是无量纲圆周率。梯度、散度与拉普拉斯算子采用笛卡尔定义。时间偏导保持位置固定。每个公式组后附局部符号定义。初始半径为正，允许除以半径。零半径属于模型排除的极限。

### Step 1.2.1 — Specify the cavity problem

### 步骤 1.2.1——规定空腔问题

**Purpose in this chapter.** Choose the initial radius, wall speed, and far-field conditions. These inputs make the radial dynamics in Section 1.3 a defined initial-value problem.

**本章作用。** 选定初始半径、壁面速度与远场条件。这些输入使第1.3节的径向动力学成为明确的初值问题。

**Derivation.**

**推导。**

(C1.2-E01) · Prescribed initial and boundary conditions / (C1.2-E01) · 给定的初始条件与边界条件

In C1.2-E01, the symbol is **$\dot R(0)$**, not $R(0)$. The equation specifies two initial conditions: $R(0)=R_0>0$ (initial cavity radius) and $\dot R(0)=U_0$ (initial radial wall velocity).

C1.2-E01 写的是 **$\dot R(0)$**，而不是 $R(0)$。它给出两个初始条件：$R(0)=R_0>0$（空腔初始半径），以及 $\dot R(0)=U_0$（空腔壁面的初始径向速度）。

$U_0$ is **a general initial-condition parameter**, not a claim that the cavity must already be moving. The Rayleigh–Plesset equation is second-order in time, so the radius and wall velocity both need to be specified. Setting $U_0=0$ is fully allowed.

$U_0$ **只是通用的初始条件参数**，并不意味着空腔在初始时刻必须运动。Rayleigh–Plesset 方程是关于时间的二阶方程，因此必须同时指定初始半径与初始壁面速度；完全可以令 $U_0=0$。

The choice depends on the initial event. If time zero is **before activation, with the cavity at rest**, choose $U_0=0$; a subsequent pressure imbalance can still give $\ddot R(0)\ne0$. If time zero is **partway through growth or collapse**, $U_0$ may be nonzero (positive for expansion, negative for collapse). At the **maximum radius immediately before an ideal collapse**, $U_0=0$, precisely as specified in Section 1.5.

具体取值取决于时间原点：如果从**空化激活之前的静止状态**开始，取 $U_0=0$，但随后压力不平衡仍可使 $\ddot R(0)\ne0$；如果从**已经发生的增长或塌缩过程中的某一时刻**开始，则 $U_0$ 可以不为零（增长为正、塌缩为负）；如果从**理想塌缩前的最大半径时刻**开始，则 $U_0=0$，这也正是第 1.5 节采用的条件。

**Therefore, C1.2-E01 is the general formulation; zero initial velocity is a physically important special case, not a universal condition.** The value must be consistent with the chosen initial state and pressure history.

**因此，C1.2-E01 给出一般形式，而初始速度为零是重要的物理特例，并不是普遍条件。** 初始值必须与所选时间原点及压力历程相容。

**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Define wall speed and acceleration as successive time derivatives of radius.

将壁面速度与加速度定义为半径的一阶和二阶时间导数。



$$
\begin{aligned}\dot R&=dR/dt,\qquad \ddot R=d\dot R/dt,\end{aligned}
$$



Evaluate the radial momentum law at the chosen initial instant. All pressure, capillary, viscous, and squared-speed terms remain present.

在选定初始时刻计算径向动量关系。保留压力、毛细、黏性及速度平方各项。



$$
\begin{aligned}\rho R_0\ddot R(0)&=p_b(0)-p_\infty(0)-2\sigma/R_0-4\mu U_0/R_0-\tfrac32\rho U_0^2,\end{aligned}
$$



Set the initial wall speed to zero. The viscous and squared-speed terms vanish, but a pressure imbalance can still produce acceleration.

令初始壁面速度为零。黏性项与速度平方项消失，但压力失衡仍可产生加速度。



$$
\begin{aligned}U_0=0\quad&\Longrightarrow\quad
    \ddot R(0)=\frac{p_b(0)-p_\infty(0)-2\sigma/R_0}{\rho R_0}.\end{aligned}
$$



Prescribe a positive initial cavity radius.

给定正的空腔初始半径。



$$
R(0)=R_0>0
$$



Prescribe initial wall speed separately; it may be zero.

独立给定初始壁面速度，其值可以为零。



$$
\dot R(0)=U_0
$$



Complete the exterior problem with zero far-field velocity and prescribed far-field pressure.

用零远场速度与给定远场压力补全外域问题。



$$
u(r,t)\to0,\quad p(r,t)\to p_\infty(t)\quad(r\to\infty)
$$



**Symbols for Eq. (C1.2-E01).**

**式（C1.2-E01）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $R$ is the cavity radius (m)<br>$R$ 为空腔半径（m） | $t$ is time (s), with 0 the chosen initial instant<br>$t$ 为时间（s），0 为选定的初始时刻 |
| $R_0$ is its prescribed positive initial value (m)<br>$R_0$ 为给定的正初始半径（m） | $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） |
| $U_0$ its initial value (m s⁻¹)<br>$U_0$ 为其初值（m s⁻¹） | $r$ is radial position (m)<br>$r$ 为径向位置（m） |
| $u$ is radial liquid speed (m s⁻¹)<br>$u$ 为液体径向速度（m s⁻¹） | $p$ is liquid pressure (Pa)<br>$p$ 为液体压力（Pa） |
| $p_\infty$ is prescribed far-field pressure (Pa)<br>$p_\infty$ 为给定远场压力（Pa） | $\rho$ — positive carrier density (kg m⁻³)<br>$\rho$ — 正载液密度（kg m⁻³） |
| $p_b$ — bubble pressure (Pa)<br>$p_b$ — 气泡压力（Pa） | $\sigma$ — constant surface tension (N m⁻¹)<br>$\sigma$ — 常数表面张力（N m⁻¹） |
| $\mu$ — dynamic viscosity (Pa s)<br>$\mu$ — 动力黏度（Pa s） | $\ddot R$ — wall acceleration (m s⁻²)<br>$\ddot R$ — 壁面加速度（m s⁻²） |

**Conventions and conditions.** The arrow denotes the far-field limit; All pressures share an absolute reference.

**约定与条件。** 箭头表示远场极限；全部压力采用同一绝对参考值。

![The evolving spherical boundary and the prescribed far-field state.](../assets/figures/c1-e01.svg)

The evolving spherical boundary and the prescribed far-field state.

运动球形边界与给定的远场状态。

**Check and interpretation.** Positive initial pressure excess over capillarity gives outward acceleration. Initial zero speed therefore does not imply equilibrium. The acceleration expression has units Pa/(kg m⁻²) = m s⁻².

**检验与解释。** 初始内外压差超过毛细压差时产生向外加速度。因此初速为零不代表平衡。加速度表达式单位为 Pa/(kg m⁻²) = m s⁻²。

## 1.3 Rayleigh–Plesset derivation

## 1.3 Rayleigh–Plesset 方程推导

### Step 1.3.1 — Obtain the liquid velocity from cavity motion

### 步骤 1.3.1——由空腔运动求载液速度

**Purpose in this chapter.** Use the spherical conditions in Eq. (C1.2-E01). Volume conservation converts wall motion into the exterior velocity field needed for momentum and energy calculations.

**本章作用。** 采用式（C1.2-E01）的球形条件。体积守恒把壁面运动转为外域速度场，为后续动量与能量计算提供输入。

**Conserve carrier volume.** Radial incompressibility makes volume flux independent of radius. Integrate its radial derivative. Apply equal normal liquid and interface velocities at the wall. Vapor density does not enter this carrier-flow calculation.

**载液体积守恒。** 径向不可压缩流的体积流量与半径无关。积分径向导数，再令壁面处液体法向速度等于界面速度。这一载液流动计算不需要蒸气密度。

**Derivation.** Apply mass conservation to a spherical shell. Constant density reduces it to zero divergence. Integrate in radius at fixed time. The integration function can depend on time. A material cavity wall supplies the final boundary value. Appreciable phase transfer changes that boundary value.

**推导。** 对球壳应用质量守恒。密度为常数时，散度为零。在固定时间对半径积分，积分函数仍可随时间变化。物质空腔壁面提供最终边界值。相变传质显著时，该边界值需要修改。

(C1.3-E02) · Exact continuity within the spherical model / (C1.3-E02) · 球形模型内的精确连续性关系

A fixed spherical shell has constant liquid mass when density is constant and the shell remains entirely liquid.

密度恒定且固定球壳始终属于液体时，壳内液体质量保持不变。



$$
\begin{aligned}\frac{d}{dt}\left[\rho\frac{4\pi}{3}((r+\delta r)^3-r^3)\right]&=0,\end{aligned}
$$



Equate mass inflow at the inner surface to mass outflow at the outer surface. Both fluxes use outward radial velocity.

令内球面的质量流入等于外球面的质量流出。两项通量均采用向外径向速度。



$$
\begin{aligned}4\pi\rho r^2u(r,t)-4\pi\rho(r+\delta r)^2u(r+\delta r,t)&=0,\end{aligned}
$$



Divide the flux difference by shell thickness and take its zero-thickness limit. This gives the radial derivative of the volume-flux factor.

将通量差除以球壳厚度，再取厚度趋零极限。由此得到体积通量因子的径向导数。



$$
\begin{aligned}\lim_{\delta r\to0}\frac{(r+\delta r)^2u(r+\delta r,t)-r^2u(r,t)}{\delta r}&=\partial_r(r^2u)=0,\end{aligned}
$$



Divide by the positive squared radius to obtain the spherical divergence form of incompressibility.

除以正的半径平方，得到不可压缩条件的球坐标散度形式。



$$
\begin{aligned}0&=\frac{1}{r^2}\frac{\partial(r^2u)}{\partial r},\end{aligned}
$$



Integrate with respect to radius at fixed time. The integration function may vary with time but cannot vary with radius.

在固定时间对半径积分。积分函数可以随时间变化，但不能随半径变化。



$$
\begin{aligned}\frac{\partial(r^2u)}{\partial r}&=0
      \quad\Longrightarrow\quad r^2u=C(t),\end{aligned}
$$



Apply equal liquid and interface normal speeds at the material cavity wall. This determines the integration function.

在物质空腔壁面令液体与界面法向速度相等。由此确定积分函数。



$$
\begin{aligned}u(R,t)&=\dot R\quad\Longrightarrow\quad C(t)=R^2\dot R,\end{aligned}
$$



Check the inverse-square decay at twice the wall radius. The ratio is defined here for nonzero wall speed.

在两倍壁面半径处检验平方反比衰减。此处速度比要求壁面速度非零。



$$
\begin{aligned}\frac{u(2R,t)}{\dot R}&=\frac{R^2}{(2R)^2}=\frac14\quad(\dot R\ne0).\end{aligned}
$$



The integrated continuity equation leaves a time-dependent radial flux factor.

积分连续性方程后，留下随时间变化的径向通量因子。



$$
\frac{1}{r^2}\frac{\partial(r^2u)}{\partial r}=0\ \Longrightarrow\ r^2u=C(t)
$$



The material-wall condition fixes that factor.

物质壁面条件确定该因子。



$$
u(R,t)=\dot R\ \Longrightarrow\ C(t)=R^2\dot R
$$



Divide by squared radius to recover the exterior velocity used below.

除以半径平方，恢复下文所用外域速度。



$$
u(r,t)=\frac{R^2\dot R}{r^2}
$$



**Symbols for Eq. (C1.3-E02).**

**式（C1.3-E02）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $r\ge R(t)>0$ is radial position (m)<br>$r\ge R(t)>0$ 为径向位置（m） | $R$ is cavity radius (m)<br>$R$ 为空腔半径（m） |
| $t$ is time (s)<br>$t$ 为时间（s） | $u$ is radial carrier velocity (m s⁻¹)<br>$u$ 为载液径向速度（m s⁻¹） |
| $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $C(t)$ is the radius-independent flux factor (m³ s⁻¹), not a material constant<br>$C(t)$ 为与径向位置无关的流量因子（m³ s⁻¹），并非材料常数 |
| $\rho$ — positive constant liquid density (kg m⁻³)<br>$\rho$ — 正常数液体密度（kg m⁻³） | $\delta r$ — positive fixed shell thickness (m)<br>$\delta r$ — 固定球壳正厚度（m） |
| $\pi$ — circle constant (1)<br>$\pi$ — 圆周率（1） | $\partial_r$ — radial derivative at fixed time (m⁻¹)<br>$\partial_r$ — 固定时间的径向导数（m⁻¹） |

**Conventions and conditions.** $\partial/\partial r$ differentiates at fixed time; The implication arrows indicate integration and use of the interface condition; The fixed shell stays liquid; $r\ge R(t)>0$.

**约定与条件。** $\partial/\partial r$ 表示固定时间下的径向求导；箭头表示积分及应用界面条件；固定球壳始终属于液体；$r\ge R(t)>0$。

![Inverse-square velocity decay places the inertia in the surrounding carrier.](../assets/figures/c1-e02.svg)

Inverse-square velocity decay places the inertia in the surrounding carrier.

速度按距离平方反比衰减，惯性来自周围载液。

**Check and interpretation.** The flux factor divided by radius squared has velocity units. Setting wall speed to zero gives a stationary liquid everywhere.

**检验与解释。** 通量因子除以半径平方具有速度单位。壁面速度为零时，全部液体静止。

### Step 1.3.2 — Prepare the velocity field for momentum integration

### 步骤 1.3.2——为动量积分建立速度势

**Purpose in this chapter.** Integrate the velocity from Eq. (C1.3-E02) and fix its reference. The resulting potential lets the radial momentum equation become a pressure relation.

**本章作用。** 积分式（C1.3-E02）的速度并固定参考值。所得速度势使径向动量方程能够转化为压力关系。

**Fix the potential reference.** Integrate velocity from infinity to the observation point. The potential applies outside the cavity. Zero potential at infinity fixes the time-dependent integration constant.

**固定速度势参考值。** 从无穷远积分速度至观察点。速度势适用于空腔外域。令无穷远速度势为零，确定随时间变化的积分常数。

**Derivation.**

**推导。**

(C1.3-E03) · Derived velocity potential / (C1.3-E03) · 推导得到的速度势

#### 1. Why can we introduce a velocity potential?

#### 为什么可以引入速度势？

Under the assumptions of Chapter 1, the exterior liquid flow is spherically symmetric and purely radial. Its vorticity is zero. Therefore, a scalar velocity potential exists such that:

在第一章的假设下，外部液体流动具有球对称性，而且只有径向速度分量，因此旋度为零。于是可以定义标量速度势：



$$
\boxed{\boldsymbol u=\nabla\phi}
$$



From C1.3-E02, incompressibility gives:

根据 C1.3-E02，不可压缩条件给出：



$$
u(r,t)=\frac{R^2\dot R}{r^2}
$$



Integrating with respect to $r$, and choosing $\phi(\infty,t)=0$, we obtain C1.3-E03:

对 $r$ 积分，并选择 $\phi(\infty,t)=0$，便得到 C1.3-E03：



$$
\boxed{\phi(r,t)=-\frac{R^2\dot R}{r}}
$$



Thus, the potential is simply another mathematical representation of the velocity field already obtained from mass conservation.

因此，速度势只是对已经通过质量守恒得到的速度场进行另一种数学表示。

#### 2. What does it simplify?

#### 它简化了什么？

The radial Euler momentum equation contains both local acceleration and convective acceleration:

径向欧拉动量方程同时包含局部加速度和对流加速度：



$$
\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial r}=-\frac{1}{\rho}\frac{\partial p}{\partial r}
$$



Using $\boldsymbol u=\nabla\phi$ for irrotational flow allows us to integrate this equation into the unsteady Bernoulli relation:

对于无旋流动，利用 $\boldsymbol u=\nabla\phi$，可以将其积分为非定常伯努利关系：



$$
\boxed{\frac{\partial\phi}{\partial t}+\frac12|\nabla\phi|^2+\frac{p}{\rho}=\frac{p_\infty}{\rho}}
$$



Here, the time derivative is taken at a fixed spatial position, and the right-hand side follows from the zero-potential, zero-velocity reference at infinity.

这里的时间偏导数是在固定空间位置计算的，右端则由无穷远处速度势和速度均为零的参考条件确定。

Substituting C1.3-E03 and evaluating at the moving cavity boundary $r=R(t)$, we obtain:

将 C1.3-E03 代入，并在运动空腔边界 $r=R(t)$ 处取值，可得：



$$
\begin{aligned}\left.\frac{\partial\phi}{\partial t}\right|_{r=R}&=-(2\dot R^2+R\ddot R),\end{aligned}
$$



Use the material-wall condition to identify liquid speed at the interface.

利用物质壁面的运动学条件确定界面处液体速度。



$$
\begin{aligned}u(R,t)&=\dot R,\end{aligned}
$$



Evaluate Bernoulli at the wall and isolate the pressure difference.

在壁面计算伯努利关系，并解出压力差。



$$
\begin{aligned}\frac{p_l-p_\infty}{\rho}&=-\left.\frac{\partial\phi}{\partial t}\right|_{r=R}-\frac12\dot R^2\end{aligned}
$$



Insert the fixed-position derivative and combine the squared-speed terms.

代入固定位置导数，并合并速度平方项。



$$
\begin{aligned}\frac{p_l-p_\infty}{\rho}&=\boxed{R\ddot R+\frac32\dot R^2}.\end{aligned}
$$



This is C1.3-E05, which directly supplies the liquid-inertia term of the Rayleigh–Plesset equation.

这就是 C1.3-E05，它直接给出了 Rayleigh–Plesset 方程中的液体惯性项。

#### 3. Is the velocity potential necessary?

#### 速度势是必需的吗？

**No.** We can substitute C1.3-E02 directly into the radial Euler equation and integrate the pressure gradient from the cavity surface to infinity. The resulting pressure–inertia equation is identical.

**不是必需的。** 我们完全可以将 C1.3-E02 直接代入径向欧拉方程，再从空腔表面积分压力梯度至无穷远，得到完全相同的压力—惯性关系。

The advantage of $\phi$ is mathematical convenience. It also provides a natural formulation for the potential-flow models later used to examine bubble interactions and nonspherical jet formation. Those applications require their own boundary conditions and do not establish that every cavitation flow is irrotational.

速度势的优势在于数学上的便利性。它还为后续研究气泡相互作用以及非球对称射流形成的势流模型提供了自然的数学框架。但这些应用需要各自的边界条件，不能据此认为所有空化流动都满足无旋条件。

**Defense conclusion:** C1.3-E03 is a mathematical bridge from the incompressible velocity field to the pressure–inertia relationship. It simplifies the derivation but is not indispensable, and its validity depends on the irrotational-flow assumption.

**答辩结论：** C1.3-E03 是连接不可压缩速度场与压力—惯性关系的数学桥梁。它能简化推导，但并非不可替代，其适用性依赖于无旋流动假设。

**Symbols for Eq. (C1.3-E03).**

**式（C1.3-E03）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\phi$ is velocity potential (m² s⁻¹)<br>$\phi$ 为速度势（m² s⁻¹） | $r$ is liquid radial position (m)<br>$r$ 为液体径向位置（m） |
| $R$ cavity radius (m)<br>$R$ 为空腔半径（m） | $t$ is time (s)<br>$t$ 为时间（s） |
| $s$ is a dummy radial integration coordinate (m)<br>$s$ 为径向积分哑变量（m） | $u$ is radial velocity (m s⁻¹)<br>$u$ 为径向速度（m s⁻¹） |
| $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $\boldsymbol u$ — liquid velocity vector (m s⁻¹)<br>$\boldsymbol u$ — 液体速度矢量（m s⁻¹） |
| $\boldsymbol e_r$ — outward radial unit vector (1)<br>$\boldsymbol e_r$ — 向外径向单位矢量（1） | $\nabla\times$ — spatial curl operator (m⁻¹)<br>$\nabla\times$ — 空间旋度算子（m⁻¹） |
| $\boldsymbol0$ — zero vorticity vector (s⁻¹)<br>$\boldsymbol0$ — 零涡量矢量（s⁻¹） | $g(t)$ — velocity-potential gauge function (m² s⁻¹)<br>$g(t)$ — 速度势规范函数（m² s⁻¹） |
| $\rho$ — constant carrier density (kg m⁻³)<br>$\rho$ — 恒定载液密度（kg m⁻³） | $p$ — local liquid pressure (Pa)<br>$p$ — 局部液体压强（Pa） |
| $p_\infty$ — far-field pressure (Pa)<br>$p_\infty$ — 远场压强（Pa） | $p_l$ — liquid-side wall pressure (Pa)<br>$p_l$ — 壁面液体侧压强（Pa） |
| $\ddot R$ — wall acceleration (m s⁻²)<br>$\ddot R$ — 壁面加速度（m s⁻²） | $\nabla$ — spatial gradient (m⁻¹)<br>$\nabla$ — 空间梯度（m⁻¹） |
| $\partial_t$ — time derivative at fixed position (s⁻¹)<br>$\partial_t$ — 固定位置时间导数（s⁻¹） |  |

**Conventions and conditions.** the integral is an improper integral convergent for $r\ge R>0$; $\partial/\partial r$ is the fixed-time spatial derivative.

**约定与条件。** 该广义积分在 $r\ge R>0$ 时收敛；$\partial/\partial r$ 为固定时间的空间导数。

![The potential reference is fixed at infinity before differentiation.](../assets/figures/c1-e03.svg)

The potential reference is fixed at infinity before differentiation.

在求导之前，先固定无穷远处的速度势参考值。

**Check and interpretation.** Spatial differentiation recovers positive outward velocity during expansion. Potential has units length × speed. The construction excludes rotational flow and unresolved vortex sheets.

**检验与解释。** 空间求导恢复膨胀时向外的正速度。速度势单位为长度乘速度。该构造排除了旋转流动和未解析涡片。

### Step 1.3.3 — Separate fixed-position and moving-wall time changes

### 步骤 1.3.3——区分固定位置与运动壁面的时间变化

**Purpose in this chapter.** Differentiate the potential from Eq. (C1.3-E03). Bernoulli requires the fixed-position derivative, so this distinction prevents an incorrect wall-inertia term.

**本章作用。** 对式（C1.3-E03）的速度势求导。伯努利关系需要固定位置导数，因此这一区分可避免错误的壁面惯性项。

**Differentiate at fixed position.** Hold the denominator fixed while differentiating the potential numerator. Then evaluate the result at the moving wall. Differentiating the wall value instead includes a convective contribution.

**在固定位置求导。** 保持速度势分母不变，对分子求时间导数。随后在运动壁面处取值。直接对壁面取值求导会包含对流贡献。

**Derivation.**

**推导。**

(C1.3-E04) · Exact Eulerian and moving-point derivatives / (C1.3-E04) · 精确的欧拉导数与运动点导数

From C1.3-E03,

根据 C1.3-E03：



$$
\phi(r,t)=-\frac{R^2\dot R}{r}.
$$



Differentiating with respect to time **at fixed $r$** gives

在**固定 $r$** 的条件下对时间求偏导：



$$
\frac{\partial\phi}{\partial t}=-\frac{2R\dot R^2+R^2\ddot R}{r}.
$$



Then evaluating at $r=R(t)$,

随后在 $r=R(t)$ 处取值：



$$
\left.\frac{\partial\phi}{\partial t}\right|_{r=R}=-2\dot R^2-R\ddot R. \tag{8}
$$



**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Apply the product rule to the radius-squared times wall-speed numerator. Both radius factors depend on time.

对半径平方与壁面速度的乘积应用乘积法则。两个半径因子均随时间变化。



$$
\begin{aligned}\frac{d(R^2\dot R)}{dt}&=2R\dot R\dot R+R^2\ddot R,\end{aligned}
$$



Apply the chain rule along the moving wall. The total derivative includes the fixed-position derivative and the radial transport term.

沿运动壁面应用链式法则。全导数包含固定位置导数与径向输运项。



$$
\begin{aligned}\frac{d\phi(R(t),t)}{dt}&=\left.\partial_t\phi\right|_{r=R}
       +\dot R\left.\partial_r\phi\right|_{r=R},\end{aligned}
$$



Insert the fixed-position potential derivative and the wall velocity. The transport contribution is the squared wall speed.

代入固定位置速度势导数及壁面速度。输运项为壁面速度的平方。



$$
\begin{aligned}\frac{d\phi(R(t),t)}{dt}&=-(2\dot R^2+R\ddot R)+\dot R\dot R\end{aligned}
$$



Combine the two squared-speed contributions. This gives the moving-wall derivative, which differs from the fixed-position derivative.

合并两个速度平方项。由此得到运动壁面导数，它与固定位置导数不同。



$$
\begin{aligned}\frac{d\phi(R(t),t)}{dt}&=-\dot R^2-R\ddot R.\end{aligned}
$$



Hold the observation radius fixed while differentiating the potential.

对速度势求导时保持观察半径固定。



$$
\left.\frac{\partial\phi}{\partial t}\right|_r=-\frac{2R\dot R^2+R^2\ddot R}{r}
$$



Evaluate this fixed-position derivative at the instantaneous wall radius.

在瞬时壁面半径处计算该固定位置导数。



$$
\left.\frac{\partial\phi}{\partial t}\right|_{r=R}=-(2\dot R^2+R\ddot R)
$$



Keep the moving-wall total derivative distinct when it is used later.

后续使用时，须区分沿运动壁面的全导数。



$$
\frac{d\phi(R(t),t)}{dt}=-\dot R^2-R\ddot R
$$



**Symbols for Eq. (C1.3-E04).**

**式（C1.3-E04）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\phi$ is velocity potential (m² s⁻¹)<br>$\phi$ 为速度势（m² s⁻¹） | $t$ is time (s)<br>$t$ 为时间（s） |
| $r$ is fixed radial position (m)<br>$r$ 为固定径向位置（m） | $R(t)>0$ is moving cavity radius (m)<br>$R(t)>0$ 为运动空腔半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |

**Conventions and conditions.** vertical bars specify where the derivative is taken or evaluated; $d/dt$ follows the moving wall value; Each derivative has units m² s⁻².

**约定与条件。** 竖线表示求导或取值条件；$d/dt$ 跟随运动壁面的取值；各导数的单位均为 m² s⁻²。

![A fixed liquid observation point and a moving interface point have different time derivatives.](../assets/figures/c1-e04.svg)

A fixed liquid observation point and a moving interface point have different time derivatives.

固定液体观察点与运动界面点对应不同的时间导数。

**Check and interpretation.** The moving derivative exceeds the Eulerian wall evaluation by wall speed squared. Both derivatives have energy-per-mass units.

**检验与解释。** 运动导数比欧拉导数的壁面取值大一个壁面速度平方。两者均具有单位质量能量的单位。

### Step 1.3.4 — Connect liquid inertia to wall pressure

### 步骤 1.3.4——将液体惯性与壁面压力联系起来

**Purpose in this chapter.** Insert Eqs. (C1.3-E02)–(C1.3-E04) into the integrated momentum law. This expresses liquid-side wall pressure through radius, speed, and acceleration.

**本章作用。** 将式（C1.3-E02）至（C1.3-E04）代入积分动量关系。由此用半径、速度与加速度表示壁面液体侧压力。

**Integrate radial momentum.** The exterior field is irrotational with zero vector Laplacian. Bulk viscous force therefore vanishes. Viscous wall stress and dissipation remain. Reference unsteady Bernoulli to infinity. Insert the fixed-position derivative and wall velocity. Subtracting one half from two gives the inertial coefficient.

**积分径向动量。** 外域流场无旋，矢量拉普拉斯为零，因而体内黏性力为零。壁面黏性应力和耗散仍存在。以无穷远为参考应用非定常伯努利方程。代入固定位置导数与壁面速度。二减去二分之一得到惯性项系数。

**Derivation.**

**推导。**

(C1.3-E05) · Derived inertial pressure / (C1.3-E05) · 推导得到的惯性压力

#### 1. Derive unsteady Bernoulli from momentum conservation

#### 1. 从动量守恒推导非定常伯努利方程

Under the chapter's assumptions of constant liquid density, incompressibility, spherical symmetry, irrotational flow, and no body force, the bulk radial momentum equation is

在本章采用的恒定液体密度、不可压缩、球对称、无旋流动及无体积力假设下，流体内部的径向动量方程为：



$$
\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial r}=-\frac{1}{\rho}\frac{\partial p}{\partial r}. \tag{1}
$$



The bulk viscous-force term vanishes for this velocity field, although viscous normal stress remains at the cavity interface. From C1.3-E03, $u=\partial\phi/\partial r$. Therefore,

对于这里的速度场，流体内部的黏性体积力项为零，但空腔界面处仍存在黏性法向应力。根据 C1.3-E03，$u=\partial\phi/\partial r$，因此：



$$
\frac{\partial u}{\partial t}=\frac{\partial}{\partial r}\left(\frac{\partial\phi}{\partial t}\right), \tag{2}
$$



and

以及：

Apply the spatial chain rule to one half of the squared radial speed.

对径向速度平方的一半应用空间链式法则。



$$
u\frac{\partial u}{\partial r}=\frac{\partial}{\partial r}\left(\frac{u^2}{2}\right). \tag{3}
$$



Substituting (2) and (3) into (1):

将式 (2)、(3) 代入式 (1)：



$$
\frac{\partial}{\partial r}\left(\frac{\partial\phi}{\partial t}+\frac{u^2}{2}+\frac{p}{\rho}\right)=0. \tag{4}
$$



Integrating with respect to $r$, we obtain a function that can depend on time:

对 $r$ 积分，得到一个可以随时间变化的积分函数：



$$
\boxed{\frac{\partial\phi}{\partial t}+\frac{u^2}{2}+\frac{p}{\rho}=C(t).} \tag{5}
$$



This is the unsteady Bernoulli equation for the present potential flow.

这才是本问题所用的非定常伯努利方程。

#### 2. Determine the integration function using the far-field condition

#### 2. 用远场边界条件确定积分函数

C1.2-E01 and C1.3-E03 prescribe

C1.2-E01 和 C1.3-E03 已经规定：



$$
\begin{cases}u(\infty,t)=0,\\p(\infty,t)=p_\infty(t),\\\phi(\infty,t)=0.\end{cases}
$$



Because the potential at infinity is identically zero at all times, its time derivative there also vanishes. Evaluating (5) at infinity gives

由于无穷远处的速度势在所有时刻均为零，其时间导数也为零。因此在无穷远处对式 (5) 取值：



$$
0+0+\frac{p_\infty(t)}{\rho}=C(t).
$$



Consequently,

因此：

Insert the far-field value of the integration function and use velocity as the potential gradient.

代入积分函数的远场值，并将速度写成速度势的梯度。



$$
\boxed{\frac{\partial\phi}{\partial t}+\frac12|\nabla\phi|^2+\frac{p}{\rho}=\frac{p_\infty(t)}{\rho}.} \tag{6}
$$



**This is precisely the equation you identified. It should appear explicitly between C1.3-E03/C1.3-E04 and C1.3-E05.**

**这正是您指出的那个公式。它应当明确出现在 C1.3-E03/C1.3-E04 与 C1.3-E05 之间。**

#### 3. Recover C1.3-E05 at the moving cavity boundary

#### 3. 在运动空腔边界恢复 C1.3-E05

Rearranging equation (6) and evaluating it at $r=R(t)$, where liquid pressure is $p_l$, gives

整理式 (6)，并在 $r=R(t)$ 的运动边界处取值，此处液体压力为 $p_l$，得到：



$$
\frac{p_l-p_\infty}{\rho}=-\left.\frac{\partial\phi}{\partial t}\right|_{r=R}-\frac12u(R,t)^2. \tag{7}
$$



From C1.3-E03,

根据 C1.3-E03：



$$
\phi(r,t)=-\frac{R^2\dot R}{r}.
$$



Differentiating with respect to time **at fixed $r$** gives

在**固定 $r$** 的条件下对时间求偏导：



$$
\frac{\partial\phi}{\partial t}=-\frac{2R\dot R^2+R^2\ddot R}{r}.
$$



Then evaluating at $r=R(t)$,

随后在 $r=R(t)$ 处取值：



$$
\left.\frac{\partial\phi}{\partial t}\right|_{r=R}=-2\dot R^2-R\ddot R. \tag{8}
$$



The kinematic boundary condition supplies $u(R,t)=\dot R$. Substitution into equation (7) yields

运动学边界条件给出 $u(R,t)=\dot R$。将其与式 (8) 代入式 (7)：



$$
\begin{aligned}\frac{p_l-p_\infty}{\rho}&=-(-2\dot R^2-R\ddot R)-\frac12\dot R^2\end{aligned}
$$



Remove the outer minus sign while retaining the kinetic contribution.

展开外部负号，同时保留动能项。



$$
\begin{aligned}\frac{p_l-p_\infty}{\rho}&=R\ddot R+2\dot R^2-\frac12\dot R^2\end{aligned}
$$



Combine two minus one half to obtain three halves.

将二减去二分之一合并为二分之三。



$$
\begin{aligned}\frac{p_l-p_\infty}{\rho}&=\boxed{R\ddot R+\frac32\dot R^2}.\end{aligned}
$$



This reproduces C1.3-E05 exactly. The coefficient $3/2$ follows from the acceleration and kinetic-energy contributions; it is not an empirical coefficient.

这就完整恢复了 C1.3-E05。系数 $3/2$ 来自加速度项和动能项的合并，并不是经验系数。

**Symbols for Eq. (C1.3-E05).**

**式（C1.3-E05）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $p_l$ is liquid pressure at the wall (Pa)<br>$p_l$ 为壁面液体压力（Pa） | $p_\infty$ far-field pressure (Pa)<br>$p_\infty$ 为远场压力（Pa） |
| $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） | $\phi$ is velocity potential (m² s⁻¹)<br>$\phi$ 为速度势（m² s⁻¹） |
| $t$ is time (s)<br>$t$ 为时间（s） | $r$ is radial position (m)<br>$r$ 为径向位置（m） |
| $R>0$ cavity radius (m)<br>$R>0$ 为空腔半径（m） | $u$ is radial velocity (m s⁻¹)<br>$u$ 为径向速度（m s⁻¹） |
| $\dot R$ wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $\ddot R$ is wall acceleration (m s⁻²)<br>$\ddot R$ 为壁面加速度（m s⁻²） |
| $\boldsymbol u$ — liquid velocity, $\nabla\phi$ (m s⁻¹)<br>$\boldsymbol u$ — 液体速度，即 $\nabla\phi$（m s⁻¹） | $\nabla$ — spatial gradient operator (m⁻¹)<br>$\nabla$ — 空间梯度算子（m⁻¹） |
| $\nabla\cdot$ — spatial divergence operator (m⁻¹)<br>$\nabla\cdot$ — 空间散度算子（m⁻¹） | $\nabla\times$ — spatial curl operator (m⁻¹)<br>$\nabla\times$ — 空间旋度算子（m⁻¹） |
| $\nabla^2$ — vector Laplacian operator (m⁻²)<br>$\nabla^2$ — 矢量拉普拉斯算子（m⁻²） | $u_i$ — Cartesian velocity component indexed by $i$ (m s⁻¹)<br>$u_i$ — 指标 $i$ 对应的笛卡尔速度分量（m s⁻¹） |
| $u_j$ — Cartesian velocity component indexed by $j$ (m s⁻¹)<br>$u_j$ — 指标 $j$ 对应的笛卡尔速度分量（m s⁻¹） | $i$ — Cartesian component index, 1, 2 or 3 (1)<br>$i$ — 笛卡尔分量指标，取 1、2 或 3（1） |
| $j$ — Cartesian component index, 1, 2 or 3 (1)<br>$j$ — 笛卡尔分量指标，取 1、2 或 3（1） | $\partial_i$ — coordinate derivative indexed by $i$ (m⁻¹)<br>$\partial_i$ — 指标 $i$ 对应的坐标导数（m⁻¹） |
| $\partial_j$ — coordinate derivative indexed by $j$ (m⁻¹)<br>$\partial_j$ — 指标 $j$ 对应的坐标导数（m⁻¹） | $\sum$ — summation over the indicated index (1)<br>$\sum$ — 对指定指标求和（1） |
| $B_0(t)$ — Bernoulli integration function (m² s⁻²)<br>$B_0(t)$ — 伯努利积分函数（m² s⁻²） | $p$ — local liquid pressure (Pa)<br>$p$ — 局部液体压力（Pa） |
| $C(t)$ — Bernoulli integration function; same role as $B_0(t)$ (m² s⁻²)<br>$C(t)$ — 伯努利积分函数；与 $B_0(t)$ 作用相同（m² s⁻²） |  |

**Conventions and conditions.** $\partial_t$ is taken at fixed position before wall evaluation; Zero vorticity gives $\partial_j u_i=\partial_i u_j$; smooth fields permit derivative exchange; $|\ |$ denotes Euclidean magnitude; $\infty$ denotes the far-field limit.

**约定与条件。** $\partial_t$ 必须先在固定位置求导，再于壁面取值；无旋条件给出 $\partial_j u_i=\partial_i u_j$；光滑场允许交换导数；$|\ |$ 表示欧氏模长；$\infty$ 表示远场极限。

![Liquid inertia relates the interface pressure to wall acceleration and squared speed.](../assets/figures/c1-e05.svg)

Liquid inertia relates the interface pressure to wall acceleration and squared speed.

液体惯性把界面压力与壁面加速度及速度平方联系起来。

**Check and interpretation.** The coefficient is 2 − 1/2 = 3/2. Constant potential gauge has been fixed; an arbitrary time gauge would change the integration function together with the potential derivative.

**检验与解释。** 系数为 2 − 1/2 = 3/2。速度势规范已经固定；若使用任意时间规范，积分函数会与速度势导数一同改变。

### Step 1.3.5 — Transfer bubble pressure across the interface

### 步骤 1.3.5——将气泡压力传递至液体界面

**Purpose in this chapter.** Apply normal-stress balance at the spherical wall. Surface tension and viscosity connect bubble pressure to the liquid pressure required by Eq. (C1.3-E05).

**本章作用。** 在球形壁面应用法向应力平衡。表面张力与黏度将气泡压力连接至式（C1.3-E05）所需的液体压力。

**Balance normal stress.** Expansion gives a negative radial strain rate at the wall. The capillary jump lowers liquid pressure relative to cavity pressure. Balance normal traction with Newtonian viscous stress included.

**平衡法向应力。** 膨胀时壁面径向应变率为负。毛细压差使液体侧压力低于腔内压力。将牛顿黏性应力计入法向牵引平衡。

**Derivation.** Use a normal pointing from liquid into gas. At an inner spherical cavity this normal points inward and curvature is negative. The normal stress jump gives the liquid pressure. Differentiate the radial speed to evaluate the normal viscous traction.

**推导。** 法向从液体指向气体。内球形空腔的该法向向内，曲率为负。法向应力跳跃给出液体压力。对径向速度求导，计算法向黏性牵引。

(C1.3-E06) · Newtonian stress and capillary boundary condition / (C1.3-E06) · 牛顿流体应力与毛细边界条件

The liquid-to-gas normal of an inner spherical cavity points inward. Extend it radially without radial variation to evaluate its divergence.

内球形空腔的液体指向气体法向朝内。沿径向作不变延拓，以计算其散度。



$$
\begin{aligned}\boldsymbol n&=-\boldsymbol e_r,\qquad
    \nabla_s\cdot\boldsymbol n=\nabla\cdot\boldsymbol n
      =\frac1{r^2}\partial_r(-r^2)=-2/r,\end{aligned}
$$



Evaluate the normal divergence at the wall. The chosen orientation gives negative spherical curvature.

在壁面处计算法向散度。所选方向给出负的球形曲率。



$$
\begin{aligned}\kappa&=(\nabla_s\cdot\boldsymbol n)|_{r=R}=-2/R,\end{aligned}
$$



Project the normal-stress jump onto the interface normal. Keep capillary pressure and liquid normal viscous stress.

将法向应力跃变投影至界面法向。保留毛细压力与液体法向黏性应力。



$$
\begin{aligned}p_l-p_b&=\sigma\kappa+2\mu\partial_r u|_{r=R},\end{aligned}
$$



Differentiate the radial velocity while holding the instantaneous wall radius and wall speed fixed.

对径向速度求空间导数，同时保持该时刻的壁面半径与速度不变。



$$
\begin{aligned}\partial_r(R^2\dot R r^{-2})&=-2R^2\dot R r^{-3},\end{aligned}
$$



Evaluate that derivative at the wall and multiply by twice the viscosity. This supplies the viscous pressure correction.

在壁面处计算该导数，并乘以两倍黏度。由此得到黏性压力修正。



$$
\begin{aligned}2\mu\partial_r u|_{r=R}&=2\mu(-2\dot R/R)=-4\mu\dot R/R.\end{aligned}
$$



Collect the evaluated wall velocity gradient.

汇总在壁面处计算的速度梯度。



$$
\left.\frac{\partial u}{\partial r}\right|_{r=R}=\left.-\frac{2R^2\dot R}{r^3}\right|_{r=R}=-\frac{2\dot R}{R}
$$



Insert that gradient and spherical curvature into liquid-side wall pressure.

将该梯度与球形曲率代入壁面液体侧压力。



$$
p_l=p_b-\frac{2\sigma}{R}+2\mu\left.\frac{\partial u}{\partial r}\right|_{r=R}=p_b-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}
$$



**Symbols for Eq. (C1.3-E06).**

**式（C1.3-E06）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $u$ — Radial liquid velocity (m s⁻¹)<br>$u$ — 液体径向速度（m s⁻¹） | $\dot R$ — Bubble-wall radial velocity (m s⁻¹)<br>$\dot R$ — 气泡壁面径向速度（m s⁻¹） |
| $r$ — Radial liquid position (m)<br>$r$ — 液体径向位置（m） | $R>0$ — Positive cavity radius (m)<br>$R>0$ — 正的空腔半径（m） |
| $p_l$ — Liquid-side pressure at the cavity wall (Pa)<br>$p_l$ — 空腔壁面处的液体侧压力（Pa） | $p_b$ — Spatially uniform bubble pressure (Pa)<br>$p_b$ — 空间均匀的气泡压力（Pa） |
| $\sigma\ge0$ — Nonnegative surface tension (N m⁻¹)<br>$\sigma\ge0$ — 非负表面张力（N m⁻¹） | $\mu\ge0$ — Nonnegative carrier dynamic viscosity (Pa s)<br>$\mu\ge0$ — 非负载液动力黏度（Pa s） |
| $\partial_r u$ — Radial strain rate, evaluated at the wall (s⁻¹)<br>$\partial_r u$ — 在壁面取值的径向应变率（s⁻¹） | $\boldsymbol n$ — unit normal directed from liquid into gas (1)<br>$\boldsymbol n$ — 液体指向气体的单位法向（1） |
| $\boldsymbol e_r$ — outward radial unit vector (1)<br>$\boldsymbol e_r$ — 向外径向单位矢量（1） | $\kappa$ — signed interface curvature (m⁻¹)<br>$\kappa$ — 带符号界面曲率（m⁻¹） |
| $\nabla_s\cdot$ — surface divergence operator (m⁻¹)<br>$\nabla_s\cdot$ — 表面散度算子（m⁻¹） | $\nabla\cdot$ — volume divergence operator (m⁻¹)<br>$\nabla\cdot$ — 体散度算子（m⁻¹） |

**Conventions and conditions.** wall evaluation is performed at $r=R$; Extend the unit normal radially without radial variation; its normal derivative vanishes, so surface and volume divergences agree at the sphere.

**约定与条件。** 壁面取值在 $r=R$ 处进行；将单位法向沿径向作不变延拓；其法向导数为零，因此表面散度与体散度在球面一致。

![Capillary and viscous stresses act at the interface even when the radial bulk viscous force is zero.](../assets/figures/c1-e06.svg)

Capillary and viscous stresses act at the interface even when the radial bulk viscous force is zero.

即使径向体内黏性力为零，毛细与黏性应力仍作用于界面。

**Check and interpretation.** For a static sphere the gas pressure exceeds liquid pressure by 2σ/R. The viscous pressure reverses with velocity. This local traction calculation remains necessary after deleting the separate tensor-dissipation check.

**检验与解释。** 静止球面气压比液压高 2σ/R。黏性压力随速度反向。删除独立张量耗散检验后，仍需保留此局部牵引计算。

### Step 1.3.6 — Assemble the radial equation of motion

### 步骤 1.3.6——组合得到径向运动方程

**Purpose in this chapter.** Combine Eqs. (C1.3-E05) and (C1.3-E06). The resulting Rayleigh–Plesset equation converts a prescribed pressure history into spherical cavity motion.

**本章作用。** 联立式（C1.3-E05）与（C1.3-E06）。所得 Rayleigh–Plesset 方程将给定压力历程转为球形空腔运动。

**Combine inertia and traction.** Insert Eq. (C1.3-E06) into Eq. (C1.3-E05). Multiply by carrier density to obtain radial momentum balance. Internal pressure still requires a source model. Use aqueous carrier density for the exterior inertia. PFC density describes a different material domain.

**合并惯性与牵引。** 将式（C1.3-E06）代入式（C1.3-E05），再乘以载液密度，得到径向动量平衡。内部压力仍需源模型。外域惯性采用水相载液密度。PFC 密度对应另一材料区域。

**Derivation.** Multiply the inertial-pressure relation by density. Replace liquid wall pressure with the traction balance. Collect all pressures with their signs. Divide by positive density and radius when acceleration is required.

**推导。** 将惯性压力关系乘以密度。以牵引平衡替换壁面液压，按符号整理各项压力。需要加速度时，再除以正密度与正半径。

(C1.3-E07) · Rayleigh–Plesset under the declared assumptions / (C1.3-E07) · 所述假设下的 Rayleigh–Plesset 方程

Start with the liquid-side pressure–inertia relation obtained from Bernoulli.

从伯努利关系得到的液体侧压力—惯性关系出发。



$$
\begin{aligned}\rho(R\ddot R+\tfrac32\dot R^2)&=p_l-p_\infty,\end{aligned}
$$



Replace liquid-side wall pressure with bubble pressure minus the capillary and viscous corrections.

用气泡压力减去毛细与黏性修正，替代壁面液体侧压力。



$$
\begin{aligned}p_l-p_\infty&=(p_b-2\sigma/R-4\mu\dot R/R)-p_\infty,\end{aligned}
$$



Divide by positive density and radius, then isolate acceleration. The squared-speed term must also be subtracted.

除以正的密度与半径，再解出加速度。还必须减去速度平方项。



$$
\begin{aligned}\ddot R&=\frac{p_b-p_\infty-2\sigma/R-4\mu\dot R/R}{\rho R}
       -\frac{3\dot R^2}{2R},\end{aligned}
$$



Set both speed and acceleration to zero. The remaining pressure excess must equal the spherical capillary pressure.

令速度与加速度均为零。剩余内外压差必须等于球形毛细压力。



$$
\begin{aligned}\dot R=\ddot R=0&\quad\Longrightarrow\quad p_b-p_\infty=2\sigma/R.\end{aligned}
$$



Equating interface pressure with liquid inertia gives the complete constant-property spherical motion law.

令界面压力与液体惯性相等，得到完整的常物性球形运动规律。



$$
\rho\left(R\ddot R+\frac32\dot R^2\right)=p_b-p_\infty-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}
$$



**Symbols for Eq. (C1.3-E07).**

**式（C1.3-E07）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） | $R>0$ is cavity radius (m)<br>$R>0$ 为空腔半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） |
| $\sigma$ is constant surface tension (N m⁻¹)<br>$\sigma$ 为常数表面张力（N m⁻¹） | $\mu$ is constant carrier viscosity (Pa s)<br>$\mu$ 为常数载液黏度（Pa s） |

**Conventions and conditions.** Every term is a pressure.

**约定与条件。** 各项均具有压力单位。

![The spherical pressure–inertia balance has a scalar radial state.](../assets/figures/c1-e07.svg)

The spherical pressure–inertia balance has a scalar radial state.

球形压力—惯性平衡只具有标量径向状态。

**Check and interpretation.** The inviscid limit removes the viscous term continuously. At rest capillarity requires positive bubble overpressure. Each original balance term has units Pa.

**检验与解释。** 无黏极限连续消去黏性项。静止时毛细作用要求气泡内过压为正。原平衡各项单位均为 Pa。

Every term has pressure units: density × length × acceleration, tension/radius, and viscosity × speed/radius. At rest, internal overpressure equals the capillary jump. During collapse, the viscous term resists inward motion. To obtain acceleration, also subtract the squared-speed term. This matches the classical spherical model. [[R1]](../reference/sources.html#r1) [[Brennen, Ch. 2]](https://media.library.caltech.edu/CaltechBOOK%3A1995.001/chap2.htm)

各项均为压力：密度 × 长度 × 加速度、张力／半径，以及黏度 × 速度／半径。静止时，内部过压等于毛细压差。塌缩时，黏性项阻碍向内运动。求加速度时还须减去速度平方项。结果与经典球形模型一致。 [[R1]](../reference/sources.html#r1) [[Brennen，第 2 章]](https://media.library.caltech.edu/CaltechBOOK%3A1995.001/chap2.htm)

### Step 1.3.7 — Identify the pressure input still needing closure

### 步骤 1.3.7——明确仍需闭合的压力输入

**Purpose in this chapter.** Separate vapor and permanent-gas contributions to the pressure in Eq. (C1.3-E07). Chapter 2 must supply their thermal, phase, and inventory evolution.

**本章作用。** 将式（C1.3-E07）的压力分解为蒸气与非凝结气体贡献。第二章须提供其热、相变及物质量演化。

**Derivation.** This is an adopted ideal-mixture closure. For components sharing temperature and volume, each ideal-gas partial pressure is proportional to its amount. Add component amounts to obtain total pressure. These algebraic steps do not determine evaporation, temperature, or saturation. Real mixtures can require a different equation of state.

**推导。** 这里采用理想混合物闭合。共享温度和体积的各理想气体分压正比于物质的量。将各组分物质的量相加，得到总压力。该代数过程不能确定蒸发、温度或饱和状态。实际混合物可能需要不同状态方程。

(C1.3-E08) · Pressure composition requiring thermodynamic closure / (C1.3-E08) · 需要热力学闭合的压力组成关系

Adopt an ideal-mixture component equation of state with common gas temperature and positive bubble volume.

采用具有共同气体温度与正气泡体积的理想混合物组分状态方程。



$$
\begin{aligned}p_iV_b&=n_i\mathcal R T_b\quad (i\in\{v,\mathrm{PFC};v,w;g\}),\end{aligned}
$$



Sum the component equations. The total amount is the sum of PFC vapor, water vapor, and permanent-gas amounts.

对各组分状态方程求和。总物质的量为 PFC 蒸气、水蒸气及非凝结气体物质的量之和。



$$
\begin{aligned}p_bV_b&=\left(n_{v,\mathrm{PFC}}+n_{v,w}+n_g\right)\mathcal R T_b,\end{aligned}
$$



Divide by bubble volume and separate the three terms. Each term is the corresponding partial pressure.

除以气泡体积，并将三项分开。每一项均为相应组分的分压。



$$
\begin{aligned}p_b&=\frac{n_{v,\mathrm{PFC}}\mathcal R T_b}{V_b}
      +\frac{n_{v,w}\mathcal R T_b}{V_b}+\frac{n_g\mathcal R T_b}{V_b}.\end{aligned}
$$



Identify each equation-of-state contribution as a partial pressure. Their sum is the bubble pressure used by the radial model.

将每一项状态方程贡献识别为分压。其总和为径向模型所用气泡压力。



$$
p_b=p_{v,\mathrm{PFC}}+p_{v,w}+p_g
$$



**Symbols for Eq. (C1.3-E08).**

**式（C1.3-E08）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $p_b$ is uniform total bubble pressure (Pa)<br>$p_b$ 为空间均匀的气泡总压力（Pa） | $p_{v,\mathrm{PFC}}$ is the PFC-vapor partial pressure (Pa)<br>$p_{v,\mathrm{PFC}}$ 为 PFC 蒸气分压（Pa） |
| $p_{v,w}$ water-vapor partial pressure (Pa)<br>$p_{v,w}$ 为水蒸气分压（Pa） | $p_g$ permanent-gas partial pressure (all Pa)<br>$p_g$ 为非凝结气体分压（均为 Pa） |
| $i$ — component index: PFC vapor, water vapor or permanent gas (1)<br>$i$ — 组分指标：PFC 蒸气、水蒸气或非凝结气体（1） | $p_i$ — component partial pressure (Pa)<br>$p_i$ — 组分分压（Pa） |
| $n_i$ — component amount of substance (mol)<br>$n_i$ — 组分物质的量（mol） | $V_b$ — positive bubble volume (m³)<br>$V_b$ — 气泡正体积（m³） |
| $\mathcal R$ — universal gas constant (J mol⁻¹ K⁻¹)<br>$\mathcal R$ — 通用气体常数（J mol⁻¹ K⁻¹） | $T_b$ — positive common gas temperature (K)<br>$T_b$ — 共同气体正温度（K） |

**Conventions and conditions.** Subscript $v$ labels vapor, PFC its chemical family; Additivity assumes a gas-mixture pressure description with the stated partial pressures; $w$ water; $g$ noncondensable gas.

**约定与条件。** 下标 $v$ 表示蒸气，PFC 表示该化学物质族；相加关系采用具有上述分压定义的气体混合物压力描述；$w$ 表示水；$g$ 表示非凝结气体。

![The mechanical input comes from the evolving contents, not from radius alone.](../assets/figures/c1-e08.svg)

The mechanical input comes from the evolving contents, not from radius alone.

力学输入来自不断变化的气泡内容物，不能仅由半径决定。

**Check and interpretation.** Pressure × volume has energy units. A vanishing component amount removes its partial pressure. Missing: component mass-transfer rates, energy balance and appropriate phase equilibrium or kinetics.

**检验与解释。** 压力乘体积具有能量单位。某组分物质的量为零时，其分压为零。缺少：组分传质率、能量平衡以及适用的相平衡或相变动力学。

A fixed-mass polytropic gas control requires its stated thermal assumptions. Evaporation and condensation exchange mass and latent heat. A permanent-gas closure omits those exchanges. Uniform internal pressure requires communication faster than state evolution. Chapter 2 supplies a finite-inventory closure. [[R5]](../reference/sources.html#r5)

固定质量多方气体对照要求满足其热学假设。蒸发和凝结交换质量与潜热，非凝结气体闭合省略了这些交换。均匀内压要求内部通信快于状态演化。第二章给出有限物质量闭合。 [[R5]](../reference/sources.html#r5)

## 1.4 Carrier energy balance

## 1.4 载液能量平衡

### Step 1.4.1 — Measure the inertia carried by the exterior liquid

### 步骤 1.4.1——计算外部载液携带的动能

**Purpose in this chapter.** Integrate the velocity field from Eq. (C1.3-E02). Exterior kinetic energy provides the energy measure for checking the radial pressure-driven motion.

**本章作用。** 积分式（C1.3-E02）的速度场。外域动能提供能量尺度，用于检验压力驱动的径向运动。

**Integrate exterior kinetic energy.** Square the velocity in Eq. (C1.3-E02). Multiply by the spherical volume element and integrate. The inverse-square integral converges over the infinite exterior. Carrier liquid beyond the wall supplies the moving inertia.

**积分外域动能。** 将式（C1.3-E02）的速度平方，乘以球形体积微元并积分。平方反比积分在无限外域收敛。壁面之外的载液构成运动惯性。

**Derivation.**

**推导。**

(C1.4-E09) · Exact kinetic-energy integral in the spherical model / (C1.4-E09) · 球形模型内的精确动能积分

#### 1. Calculate the kinetic energy of the surrounding liquid

#### 计算周围载液的动能

We begin with the incompressible spherical velocity field from C1.3-E02:

首先利用 C1.3-E02 给出的不可压缩球对称流速场：



$$
u(r,t)=\frac{R^2\dot R}{r^2}.
$$



An infinitesimal spherical liquid shell has volume $dV=4\pi r^2\,dr$. Integrating the kinetic-energy density $\tfrac12\rho u^2$ over the entire exterior liquid gives:

半径为 $r$ 的球壳体积元为 $dV=4\pi r^2\,dr$。对外域液体的动能密度 $\tfrac12\rho u^2$ 积分：



$$
\begin{aligned}K_l&=\int_R^\infty \frac12\rho u(r,t)^2\,4\pi r^2\,dr\end{aligned}
$$



Substitute the inverse-square radial velocity into the kinetic-energy density.

将平方反比径向速度代入动能密度。



$$
\begin{aligned}K_l&=\int_R^\infty\frac12\rho\frac{R^4\dot R^2}{r^4}\,4\pi r^2\,dr\end{aligned}
$$



Collect factors independent of the shell radius outside the integral.

将与球壳径向坐标无关的因子提出积分号。



$$
\begin{aligned}K_l&=2\pi\rho R^4\dot R^2\int_R^\infty r^{-2}\,dr\end{aligned}
$$



Use the antiderivative of the inverse-square shell-radius factor.

使用球壳半径平方反比项的原函数。



$$
\begin{aligned}K_l&=2\pi\rho R^4\dot R^2\left[-\frac1r\right]_R^\infty\end{aligned}
$$



Evaluate the infinite and wall endpoints, then cancel one radius factor.

计算无穷远端点与壁面端点，再约去一个半径因子。



$$
\begin{aligned}K_l&=\boxed{2\pi\rho R^3\dot R^2}.\end{aligned}
$$



This is the kinetic energy of the *surrounding liquid*, not of the vapor inside the cavity.

这是**周围载液**的动能，而不是空腔内蒸气的动能。

**Symbols for Eq. (C1.4-E09).**

**式（C1.4-E09）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $K_l$ is exterior liquid kinetic energy (J)<br>$K_l$ 为外部液体动能（J） | $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） |
| $u$ is radial liquid speed (m s⁻¹)<br>$u$ 为径向液体速度（m s⁻¹） | $\dot R$ wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） |
| $t$ is time (s)<br>$t$ 为时间（s） | $R>0$ is cavity radius (m)<br>$R>0$ 为空腔半径（m） |
| $r$ the integration radius (m)<br>$r$ 为积分半径（m） | $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |
| $dV$ — spherical shell volume element (m³)<br>$dV$ — 球壳体积元（m³） | $\theta$ — polar angle, $0\le\theta\le\pi$ (1)<br>$\theta$ — 极角，$0\le\theta\le\pi$（1） |
| $\psi$ — azimuthal angle, $0\le\psi\le2\pi$ (1)<br>$\psi$ — 方位角，$0\le\psi\le2\pi$（1） | $b$ — finite outer cutoff radius, $b>R$ (m)<br>$b$ — 有限外截断半径，$b>R$（m） |

**Conventions and conditions.** $4\pi r^2dr$ is the spherical volume element (m³); endpoint brackets mean upper minus lower evaluation.

**约定与条件。** $4\pi r^2dr$ 为球形体积元（m³）；端点方括号表示上限取值减下限取值。

![Exterior shells contribute finite kinetic energy even in an infinite domain.](../assets/figures/c1-e09.svg)

Exterior shells contribute finite kinetic energy even in an infinite domain.

即使外域无限，外部液壳贡献的总动能仍有限。

**Check and interpretation.** Density × radius cubed × speed squared gives joules. Infinite volume causes no divergence because speed decays sufficiently fast. A finite outer wall changes the velocity boundary-value problem.

**检验与解释。** 密度乘半径三次方乘速度平方得到焦耳。速度衰减足够快，因此无限体积不造成发散。有限外壁会改变速度边值问题。

### Step 1.4.2 — Convert stored energies into rates

### 步骤 1.4.2——将储存能量转为变化率

**Purpose in this chapter.** Differentiate Eq. (C1.4-E09), the surface energy, and cavity volume. Their rates allow the momentum equation to be checked as a power balance.

**本章作用。** 对式（C1.4-E09）、表面能及空腔体积求导。这些变化率使动量方程能够通过功率平衡接受检验。

**Differentiate stored energy.** Apply the product rule to radius and squared speed. Differentiate cavity volume and interface energy separately. The surface-energy derivative assumes constant surface tension.

**对储存能量求导。** 对半径与速度平方应用乘积法则。分别对空腔体积和界面能求导。表面能导数假设表面张力恒定。

**Derivation.**

**推导。**

(C1.4-E10) · Exact product-rule derivatives / (C1.4-E10) · 乘积求导法则的精确应用

The left-hand side is exactly the time derivative of exterior-liquid kinetic energy:

左边恰好是外部载液动能的时间导数：



$$
\frac{d}{dt}\underbrace{(2\pi\rho R^3\dot R^2)}_{K_l}
=6\pi\rho R^2\dot R^3+4\pi\rho R^3\dot R\ddot R.
$$



The capillary term is exactly the time derivative of surface energy:

毛细项恰好是表面能的时间导数：



$$
\frac{d}{dt}\underbrace{(4\pi\sigma R^2)}_{E_\sigma}=8\pi\sigma R\dot R.
$$



**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Differentiate the kinetic-energy radius and squared-speed factors using the product rule.

用乘积法则对动能中的半径因子与速度平方因子求导。



$$
\begin{aligned}\frac{d(R^3\dot R^2)}{dt}&=\frac{dR^3}{dt}\dot R^2+R^3\frac{d\dot R^2}{dt},\end{aligned}
$$



Apply the chain rule to each factor separately. Both wall speed and wall acceleration appear.

分别对每个因子应用链式法则。壁面速度与加速度均会出现。



$$
\begin{aligned}\frac{dR^3}{dt}&=3R^2\dot R,\qquad\frac{d\dot R^2}{dt}=2\dot R\ddot R,\end{aligned}
$$



Insert those derivatives and factor out the cavity volume rate. The remaining bracket matches radial inertia.

代入上述导数，并提取空腔体积变化率。剩余括号与径向惯性项一致。



$$
\begin{aligned}2\pi\rho(3R^2\dot R^3+2R^3\dot R\ddot R)
      &=4\pi\rho R^2\dot R(\tfrac32\dot R^2+R\ddot R),\end{aligned}
$$



Differentiate surface energy at constant surface tension. The changing area supplies its time dependence.

在表面张力恒定时对表面能求导。其时间变化来自面积变化。



$$
\begin{aligned}\frac{d(4\pi\sigma R^2)}{dt}&=4\pi\sigma(2R\dot R).\end{aligned}
$$



Collect the differentiated kinetic energy in a form containing radial inertia.

将动能导数整理为包含径向惯性项的形式。



$$
\begin{aligned}\frac{dK_l}{dt}&=2\pi\rho\left(3R^2\dot R^3+2R^3\dot R\ddot R\right)=4\pi R^2\dot R\,\rho\left(R\ddot R+\frac32\dot R^2\right),\end{aligned}
$$



Record cavity volume and its rate for the pressure-work calculation.

写出空腔体积及其变化率，用于压力功计算。



$$
\begin{aligned}V_b&=\frac{4\pi R^3}{3},\qquad \dot V_b=4\pi R^2\dot R,\end{aligned}
$$



Record surface energy and its rate at constant surface tension.

写出常表面张力下的表面能及其变化率。



$$
\begin{aligned}E_\sigma&=4\pi\sigma R^2,\qquad \frac{dE_\sigma}{dt}=8\pi\sigma R\dot R.\end{aligned}
$$



**Symbols for Eq. (C1.4-E10).**

**式（C1.4-E10）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $K_l$ — Carrier kinetic energy (J)<br>$K_l$ — 载液动能（J） | $E_\sigma$ — Interfacial energy (J)<br>$E_\sigma$ — 界面能（J） |
| $t$ is time (s)<br>$t$ 为时间（s） | $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） |
| $R$ is radius (m)<br>$R$ 为半径（m） | $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） |
| $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） | $V_b$ is cavity volume (m³)<br>$V_b$ 为空腔体积（m³） |
| $\dot V_b$ its time derivative (m³ s⁻¹)<br>$\dot V_b$ 为其时间导数（m³ s⁻¹） | $\sigma$ is constant surface tension (N m⁻¹)<br>$\sigma$ 为常数表面张力（N m⁻¹） |
| $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |  |

**Conventions and conditions.** Energy derivatives are powers (W).

**约定与条件。** 能量的时间导数为功率（W）。

![Volume work couples kinetic storage, interface storage and dissipation.](../assets/figures/c1-e10.svg)

Volume work couples kinetic storage, interface storage and dissipation.

体积功耦合动能储存、界面能储存与耗散。

**Check and interpretation.** Energy rates have units watts. At a turning point both rates vanish instantaneously, even when acceleration is nonzero. Variable surface tension would add another product-rule term.

**检验与解释。** 能量变化率单位为瓦。转折点两种能量变化率瞬时为零，即使加速度非零。表面张力随时间变化时，需要增加乘积求导项。

### Step 1.4.3 — Check where pressure work goes

### 步骤 1.4.3——检验压力功的去向

**Purpose in this chapter.** Combine the motion law in Eq. (C1.3-E07) with Eq. (C1.4-E10). This separates kinetic-energy storage, surface-energy storage, and viscous loss.

**本章作用。** 将式（C1.3-E07）的运动规律与式（C1.4-E10）结合。由此区分动能储存、表面能储存与黏性损耗。

**Convert momentum balance into power balance.** Multiply by cavity volume rate. The inertial term becomes Eq. (C1.4-E10), first row. The capillary term equals minus the surface-energy derivative. Squared speed makes viscous power nonpositive in both motion directions.

**将动量平衡转为功率平衡。** 乘以空腔体积变化率。惯性项成为式（C1.4-E10）第一行。毛细项等于表面能导数的负值。速度平方使两种运动方向的黏性功率均不为正。

**Derivation.**

**推导。**

(C1.4-E11) · Derived mechanical-energy balance / (C1.4-E11) · 推导得到的机械能平衡

#### 2. Derivation without skipped steps

#### 不跳步推导

Start from the Rayleigh–Plesset equation under the chapter's spherical, incompressible, constant-property, no-slip assumptions:

从本章在球形、不可压缩、物性恒定、界面无滑移等假设下的 Rayleigh–Plesset 方程出发：



$$
\rho\left(R\ddot R+\frac32\dot R^2\right)=p_b-p_\infty-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}.
$$



Multiply every term by $\dot V_b=4\pi R^2\dot R$:

将每一项乘以 $\dot V_b=4\pi R^2\dot R$：



$$
4\pi\rho R^3\dot R\ddot R+6\pi\rho R^2\dot R^3
=(p_b-p_\infty)\dot V_b-8\pi\sigma R\dot R-16\pi\mu R\dot R^2.
$$



The left-hand side is exactly the time derivative of exterior-liquid kinetic energy:

左边恰好是外部载液动能的时间导数：



$$
\frac{d}{dt}\underbrace{(2\pi\rho R^3\dot R^2)}_{K_l}
=6\pi\rho R^2\dot R^3+4\pi\rho R^3\dot R\ddot R.
$$



The capillary term is exactly the time derivative of surface energy:

毛细项恰好是表面能的时间导数：



$$
\frac{d}{dt}\underbrace{(4\pi\sigma R^2)}_{E_\sigma}=8\pi\sigma R\dot R.
$$



Move the capillary term to the left, giving the required balance:

将毛细项移至左边，就得到所要求的收支关系：



$$
\boxed{\frac{dK_l}{dt}+\frac{dE_\sigma}{dt}=(p_b-p_\infty)\dot V_b-\mathcal D_\mu},\qquad
\mathcal D_\mu=16\pi\mu R\dot R^2\ge0.
$$



#### 3. Interpretation during expansion and collapse

#### 膨胀和塌缩时如何理解

**Expansion:** If $\dot R>0$ and $p_b>p_\infty$, pressure contributes positive power. This power can increase liquid kinetic energy and surface energy, with some lost to viscosity. **Collapse:** If $\dot R<0$ and $p_b<p_\infty$, their product is again positive: the ambient pressure is doing work that can accelerate the inward flow. The surface area shrinks, so stored interfacial energy can also be released. Viscosity always removes mechanical energy, regardless of whether $\dot R$ is positive or negative.

**膨胀：** 若 $\dot R>0$ 且 $p_b>p_\infty$，压差输入正功率；它可以转化成载液动能与增加的表面能，另有一部分由黏性耗散。**塌缩：** 若 $\dot R<0$ 且 $p_b<p_\infty$，两者乘积依然为正：环境压力对流体做功，可以加速向内流动。同时表面积缩小，界面储能也可释放。无论膨胀还是塌缩，黏性始终耗散机械能。

#### 4. Validity

#### 适用范围

This is the **mechanical** budget of the spherical cavity and exterior carrier. It does **not** already account for PFC internal energy, laser absorption, heat transfer, latent heat, noncondensable gas thermodynamics, acoustic radiation or an emitted directional jet. Those require additional balance equations. The equation also does not say that the pressure-work term is always positive.

该方程是球形空腔及外部载液的**机械能**收支关系，并未把 PFC 内能、激光吸收、热传导、潜热、非凝结气体热力学、声辐射或外部定向射流全部计入。这些过程需要额外的守恒方程。压差功率项也并非始终为正。

**Symbols for Eq. (C1.4-E11).**

**式（C1.4-E11）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $t$ is time (s)<br>$t$ 为时间（s） | $K_l$ — Carrier kinetic energy (J)<br>$K_l$ — 载液动能（J） |
| $E_\sigma$ — Interfacial energy (J)<br>$E_\sigma$ — 界面能（J） | $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） |
| $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） | $\dot V_b$ is cavity volume rate (m³ s⁻¹)<br>$\dot V_b$ 为空腔体积变化率（m³ s⁻¹） |
| $\mu\ge0$ is carrier viscosity (Pa s)<br>$\mu\ge0$ 为载液黏度（Pa s） | $R>0$ is cavity radius (m)<br>$R>0$ 为空腔半径（m） |
| $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** The nonnegative term is dissipated power (W).

**约定与条件。** 非负项是耗散功率（W）。

![The pressure source supplies mechanical work; focusing cannot create extra energy.](../assets/figures/c1-e11.svg)

The pressure source supplies mechanical work; focusing cannot create extra energy.

压力源提供机械功；聚焦不能产生额外能量。

**Check and interpretation.** Expansion against excess internal pressure and collapse under excess external pressure both allow positive work. Dissipation is nonnegative for either velocity sign. Missing: laser absorption, internal energy, latent heat and acoustic radiation in a complete energy budget.

**检验与解释。** 内压较高时膨胀与外压较高时塌缩都可得到正功。两种速度符号下耗散均非负。完整能量预算还缺少：激光吸收、内能、潜热与声辐射。

Confinement can redirect liquid and change its energy budget. It may store elastic energy or increase dissipation. Predicting carrier motion requires the thermodynamic source and mechanical receiver. Incident pulse energy alone leaves that budget unresolved.

约束可改变液体方向及能量分配，也可能储存弹性能或增加耗散。预测载液运动需同时计算热力学源与力学受载体系。仅知入射脉冲能量，能量分配仍未确定。

## 1.5 Ideal collapse time and coefficient

## 1.5 理想塌缩时间与系数

### Step 1.5.1 — Define a solvable ideal-collapse benchmark

### 步骤 1.5.1——规定可解的理想塌缩基准

**Purpose in this chapter.** Reduce Eq. (C1.3-E07) to collapse under a constant positive pressure difference. This restricted control problem supplies the trajectory and time benchmark below.

**本章作用。** 将式（C1.3-E07）约化为恒定正压差下的塌缩。这一受限对照问题为下文提供轨迹与时间基准。

**Specify the ideal collapse problem.** Start at maximum radius with zero wall speed. Far-field and vapor pressures are constant with positive collapse difference. Omit tension, viscosity, permanent gas and liquid compressibility. Thermal and phase dynamics are excluded assumptions. Their smallness for PFC remains unestablished. A hot vapor-rich cavity can still expand.

**规定理想塌缩问题。** 从最大半径及零壁面速度开始。远场压力与蒸气压恒定，塌缩压差为正。忽略张力、黏性、非凝结气体及液体可压缩性。热学与相变动力学被模型排除。它们对 PFC 是否足够小尚未确立。高温蒸气丰富的空腔仍可膨胀。

**Derivation.**

**推导。**

(C1.5-E12) · Idealized collapse initial-value problem / (C1.5-E12) · 理想化塌缩的初值问题

#### Complete derivation

#### 完整推导

Begin with the ideal Rayleigh collapse equation, for $\Delta p_c=p_\infty-p_v>0$, constant liquid density $\rho$, and cavity radius $R(t)>0$:

以理想 Rayleigh 塌缩方程为起点，其中 $\Delta p_c=p_\infty-p_v>0$，液体密度 $\rho$ 恒定，空腔半径 $R(t)>0$：



$$
R\ddot R+\frac32\dot R^2=-\frac{\Delta p_c}{\rho}.
\tag{1}
$$



**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Prescribe constant vapor pressure and omit surface tension and viscosity for this ideal control. Express the pressure difference with the collapse sign.

在这一理想对照中给定恒定蒸气压，并忽略表面张力与黏度。用塌缩符号约定表示压差。



$$
\begin{aligned}p_b&=p_v,\quad \mu=\sigma=0,\quad p_v-p_\infty=-\Delta p_c,\end{aligned}
$$



Insert these restrictions into Rayleigh–Plesset. The pressure forcing is negative.

将这些限制代入 Rayleigh–Plesset 方程。压力驱动力为负。



$$
\begin{aligned}\rho(R\ddot R+\tfrac32\dot R^2)&=-\Delta p_c,\end{aligned}
$$



Evaluate the initial state at maximum radius with zero wall speed. The squared-speed term vanishes.

在最大半径、壁面速度为零的初始状态求值。速度平方项消失。



$$
\begin{aligned}R_{\max}\ddot R(0)&=-\Delta p_c/\rho,\end{aligned}
$$



Divide by the positive maximum radius. Negative initial acceleration starts the inward collapse branch.

除以正的最大半径。负初始加速度使系统进入向内塌缩分支。



$$
\begin{aligned}\ddot R(0)&=-\frac{\Delta p_c}{\rho R_{\max}}<0.\end{aligned}
$$



Define a positive collapse-pressure difference.

定义正的塌缩压差。



$$
\Delta p_c=p_\infty-p_v>0
$$



Start from maximum radius with a stationary wall.

从最大半径、壁面静止状态开始。



$$
R(0)=R_{\max},\quad \dot R(0)=0
$$



The resulting ideal radial equation drives inward collapse.

所得理想径向方程驱动向内塌缩。



$$
R\ddot R+\frac32\dot R^2=-\frac{\Delta p_c}{\rho}
$$



**Symbols for Eq. (C1.5-E12).**

**式（C1.5-E12）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\Delta p_c>0$ is constant collapse-driving pressure (Pa)<br>$\Delta p_c>0$ 为常数塌缩驱动压差（Pa） | $p_\infty$ — Constant Far-field absolute pressure (Pa)<br>$p_\infty$ — 恒定的远场绝对压力（Pa） |
| $p_v$ — Stipulated constant vapor pressure (Pa)<br>$p_v$ — 假定恒定蒸气压（Pa） | $t=0$ is maximum-radius time (s)<br>$t=0$ 为最大半径时刻（s） |
| $R>0$ — Instantaneous cavity radius (m)<br>$R>0$ — 瞬时空腔半径（m） | $R_{\max}>0$ — Radius at the start of ideal collapse (m)<br>$R_{\max}>0$ — 理想塌缩开始时的半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |
| $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） | $\mu$ — viscosity, set to zero in this control (Pa s)<br>$\mu$ — 黏度，在此对照中置零（Pa s） |
| $\sigma$ — surface tension, set to zero in this control (N m⁻¹)<br>$\sigma$ — 表面张力，在此对照中置零（N m⁻¹） | $p_b$ — bubble pressure (Pa)<br>$p_b$ — 气泡压力（Pa） |![The ideal control begins at rest and excludes the mechanisms that arrest real collapse.](../assets/figures/c1-e12.svg)

The ideal control begins at rest and excludes the mechanisms that arrest real collapse.

理想对照从静止开始，并排除了阻止实际塌缩的机制。

**Check and interpretation.** Pressure deficit produces inward acceleration. This hypothetical control omits physical collapse arrest and evolving PFC vapor production.

**检验与解释。** 压差产生向内加速度。此假想对照省略了实际塌缩终止机制和随时间演化的 PFC 蒸气生成。

### Step 1.5.2 — Replace time by radius on the collapse branch

### 步骤 1.5.2——在塌缩分支以半径替代时间

**Purpose in this chapter.** Transform Eq. (C1.5-E12) into a first-order equation for squared speed. Its integrating factor prepares a trajectory satisfying the maximum-radius initial condition.

**本章作用。** 将式（C1.5-E12）转为速度平方的一阶方程。其积分因子用于构造满足最大半径初始条件的轨迹。

**Use radius on the collapse branch.** Negative initial acceleration starts decreasing radius. Define squared speed as a radius function. Away from the turning point, apply the chain rule. Cancel the nonzero speed there. Extend the relation continuously to the initial endpoint. Multiply by radius cubed to form an exact derivative.

**在塌缩分支上以半径为自变量。** 负初始加速度使半径开始减小。将速度平方定义为半径函数。在转折点之外应用链式法则，再约去非零速度。连续延拓关系至初始端点。乘以半径三次方，形成完整导数。

**Derivation.**

**推导。**

(C1.5-E13) · Exact chain rule and integrating factor / (C1.5-E13) · 精确的链式法则与积分因子

Define the squared wall velocity as a function of radius: $y(R)=\dot R^2$. By the chain rule, at times when $\dot R\ne0$,

将壁面速度的平方定义为半径的函数：$y(R)=\dot R^2$。在 $\dot R\ne0$ 的时刻，根据链式法则：



$$
\frac{dy}{dt}=2\dot R\ddot R,\qquad
\frac{dy}{dR}=\frac{dy/dt}{dR/dt}=2\ddot R,
\qquad\therefore\quad \ddot R=\frac12\frac{dy}{dR}.
\tag{2}
$$



The formula extends to the starting turning point by continuity. Substituting $y$ and $dy/dR$ into (1) yields

该关系可以通过连续性延拓到初始的速度零点。将 $y$ 和 $dy/dR$ 代入式 (1) 得到：



$$
\frac R2\frac{dy}{dR}+\frac32y=-\frac{\Delta p_c}{\rho},
\qquad\Longrightarrow\qquad
R\frac{dy}{dR}+3y=-\frac{2\Delta p_c}{\rho}.
\tag{3}
$$



Multiply by $R^2$ and recognize a product derivative:

两侧乘以 $R^2$，利用乘积求导公式：



$$
R^3\frac{dy}{dR}+3R^2y
=\frac{d}{dR}(R^3y)
=-\frac{2\Delta p_c}{\rho}R^2.
\tag{4}
$$



**Symbols for Eq. (C1.5-E13).**

**式（C1.5-E13）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $y(R)$ is squared wall speed (m² s⁻²)<br>$y(R)$ 为壁面速度平方（m² s⁻²） | $R\in(0,R_{\max})$ is decreasing radius (m)<br>$R\in(0,R_{\max})$ 为递减半径（m） |
| $t$ is time (s)<br>$t$ 为时间（s） | $\dot R\ne0$ — Wall radial velocity (m s⁻¹)<br>$\dot R\ne0$ — 壁面径向速度（m s⁻¹） |
| $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） | $\Delta p_c$ is positive pressure difference (Pa)<br>$\Delta p_c$ 为正压差（Pa） |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $y'$ — radius derivative $dy/dR$ (m s⁻²)<br>$y'$ — 半径导数 $dy/dR$（m s⁻²） |
| $I$ — positive integrating factor, $I(R_{\max})=1$ (1)<br>$I$ — 正积分因子，$I(R_{\max})=1$（1） | $I'$ — radius derivative $dI/dR$ (m⁻¹)<br>$I'$ — 半径导数 $dI/dR$（m⁻¹） |
| $s$ — positive dummy radius (m)<br>$s$ — 正积分哑半径（m） | $R_{\max}$ — maximum cavity radius (m)<br>$R_{\max}$ — 最大空腔半径（m） |
| $\ln$ — natural logarithm with positive dimensionless argument (1)<br>$\ln$ — 自变量为正无量纲数的自然对数（1） | $\exp$ — exponential with dimensionless argument (1)<br>$\exp$ — 自变量无量纲的指数函数（1） |

**Conventions and conditions.** $d/dR$ and $d/dt$ are ordinary derivatives on the monotonic branch; Radius powers are the integrating factor, not derivatives.

**约定与条件。** $d/dR$ 与 $d/dt$ 为单调分支上的普通导数；半径幂构成积分因子，并非导数。

![The monotonic collapse branch allows radius to replace time in the first integration.](../assets/figures/c1-e13.svg)

The monotonic collapse branch allows radius to replace time in the first integration.

单调塌缩分支允许在第一次积分中以半径取代时间。

**Check and interpretation.** Multiplying by the constant maximum-radius cube gives the equivalent integrating factor used below. Every momentum term retains acceleration-per-length-compatible units before integration.

**检验与解释。** 乘以常数最大半径三次方，即得到下文使用的等价积分因子。积分前各动量项保持一致量纲。

### Step 1.5.3 — Recover inward speed and its integration constant

### 步骤 1.5.3——求向内速度及积分常数

**Purpose in this chapter.** Integrate Eq. (C1.5-E13) from the stationary maximum-radius state. Select the inward branch before using its reciprocal to calculate collapse time.

**本章作用。** 从最大半径处的静止状态积分式（C1.5-E13）。先选取向内分支，再用速度倒数计算塌缩时间。

**Derivation.**

**推导。**

(C1.5-E14) · Integrated speed with initial constant and branch / (C1.5-E14) · 含初始积分常数与分支选择的速度积分解

Integrate from $R_{\max}$ (the initial maximum radius) to the current $R<R_{\max}$:

从初始最大半径 $R_{\max}$ 积分至当前半径 $R<R_{\max}$：



$$
R^3y(R)-R_{\max}^3 y(R_{\max})
=-\frac{2\Delta p_c}{\rho}\int_{R_{\max}}^R s^2\,ds
=-\frac{2\Delta p_c}{3\rho}(R^3-R_{\max}^3).
\tag{5}
$$



The cavity begins to collapse **from rest at its maximum radius**. Thus $\dot R=0$ and $y(R_{\max})=0$. Rearranging (5) and dividing by $R^3$ gives

空腔**从最大半径处静止开始塌缩**，所以 $\dot R=0$、$y(R_{\max})=0$。将式 (5) 整理并除以 $R^3$，得到：



$$
R^3y(R)=\frac{2\Delta p_c}{3\rho}(R_{\max}^3-R^3),
\qquad
\boxed{y(R)=\dot R^2=\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}R\right)^3-1\right]}.
\tag{6}
$$



Taking the square root produces **two mathematical branches**:

开平方后存在**两个数学分支**：



$$
\dot R=\pm\sqrt{\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}R\right)^3-1\right]}.
\tag{7}
$$



For collapse the radius decreases, so $\dot R=dR/dt<0$; choose the **negative** branch:

对于塌缩，半径随时间减小，因此 $\dot R=dR/dt<0$，应选取**负号**：



$$
\boxed{\dot R=-\sqrt{\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}R\right)^3-1\right]}}.
\tag{8}
$$



At the initial instant $\dot R=0$, but (1) gives $\ddot R(0)=-\Delta p_c/(\rho R_{\max})<0$, so the wall accelerates inward immediately. The expression is an **ideal-model** wall speed, not an experimentally established jet velocity; its divergence as $R\to0$ signals breakdown of the simplified model.

初始时刻虽然 $\dot R=0$，但根据式 (1)，$\ddot R(0)=-\Delta p_c/(\rho R_{\max})<0$，所以壁面立即向内加速。该表达式描述的是**理想模型**下的壁面速度，并不是经实验确立的射流速度；当 $R\to0$ 时发散，意味着简化模型在这一极限失效。

**Symbols for Eq. (C1.5-E14).**

**式（C1.5-E14）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $R\in(0,R_{\max}]$ — Instantaneous cavity radius (m)<br>$R\in(0,R_{\max}]$ — 瞬时空腔半径（m） | $R_{\max}$ — Radius at the start of ideal collapse (m)<br>$R_{\max}$ — 理想塌缩开始时的半径（m） |
| $y$ is squared speed (m² s⁻²)<br>$y$ 为速度平方（m² s⁻²） | $s$ is dummy radius (m)<br>$s$ 为积分哑半径（m） |
| $\Delta p_c>0$ is collapse pressure (Pa)<br>$\Delta p_c>0$ 为塌缩压差（Pa） | $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） |
| $\dot R\le0$ is inward wall velocity (m s⁻¹)<br>$\dot R\le0$ 为向内壁面速度（m s⁻¹） |  |

**Conventions and conditions.** The square root denotes the nonnegative root; its prefixed minus sign selects collapse.

**约定与条件。** 根号表示非负平方根；前置负号选择塌缩分支。

![The initial condition fixes the integration constant and the inward sign fixes the branch.](../assets/figures/c1-e14.svg)

The initial condition fixes the integration constant and the inward sign fixes the branch.

初值确定积分常数，向内的符号确定解分支。

**Check and interpretation.** At maximum radius the speed is zero. For smaller positive radius the squared speed is positive. The speed scale is the square root of pressure divided by density.

**检验与解释。** 最大半径处速度为零。半径减小且保持正值时，速度平方为正。速度尺度为压差除以密度的平方根。

### Step 1.5.4 — Separate collapse time from geometric scale

### 步骤 1.5.4——分离塌缩时间与几何尺度

**Purpose in this chapter.** Integrate the reciprocal speed from Eq. (C1.5-E14). Nondimensionalizing radius isolates the universal integral from radius, density, and pressure scales.

**本章作用。** 积分式（C1.5-E14）的速度倒数。将半径无量纲化，把通用积分与半径、密度及压力尺度分离。

**Separate scale from trajectory.** Integrate reciprocal inward speed from maximum radius to zero. Normalize radius by its maximum. Every case in this ideal family shares the resulting dimensionless integral. That common integral establishes the time proportionality.

**分离尺度与轨迹。** 从最大半径至零积分向内速度的倒数。用最大半径归一化半径。此理想模型族各情形共有所得无量纲积分。该共同积分确立时间的比例关系。

**Derivation.** For the inward branch, time increases while radius decreases. The negative reciprocal speed reverses the integration bounds. Normalize radius and include its differential. Factor the cubic ratio before taking the positive square root.

**推导。** 向内分支上，时间增加而半径减小。速度倒数的负号反转积分上下限。将半径无量纲化并包含微分变换。先整理三次方比值，再取正平方根。

(C1.5-E15) · Exact separation and nondimensionalization / (C1.5-E15) · 精确的变量分离与无量纲化

Separate time from radius along the inward trajectory. The reciprocal speed retains the negative collapse sign.

沿向内轨迹分离时间与半径。速度倒数保留塌缩负号。



$$
\begin{aligned}dt&=dR/\dot R,\qquad
    \frac1{\dot R}=-\sqrt{\frac{3\rho}{2\Delta p_c}}\frac1{\sqrt{(R_{\max}/R)^3-1}},\end{aligned}
$$



Introduce radius normalized by maximum radius. Rewrite the denominator using its cubed ratio.

引入以最大半径归一化的半径。用其三次方比值改写分母。



$$
\begin{aligned}(R_{\max}/R)^3-1&=x^{-3}-1=(1-x^3)/x^3,\end{aligned}
$$



Transform both the radius differential and denominator. The Jacobian contributes one maximum-radius factor.

同时变换半径微分与分母。雅可比因子提供一个最大半径因子。



$$
\begin{aligned}\frac{dR}{\sqrt{(R_{\max}/R)^3-1}}
      &=R_{\max}\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx,\end{aligned}
$$



Reverse the integration limits to cancel the collapse minus sign. The resulting time integral is positive.

反转积分上下限，消去塌缩负号。所得时间积分为正。



$$
\begin{aligned}-\int_1^0\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx
      &=\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx.\end{aligned}
$$



Integrate reciprocal inward speed and reverse the bounds to obtain positive elapsed time.

积分向内速度的倒数，并反转上下限以得到正的经过时间。



$$
\begin{aligned}t_c&=\int_{R_{\max}}^0\frac{dR}{\dot R}=\sqrt{\frac{3\rho}{2\Delta p_c}}\int_0^{R_{\max}}\frac{dR}{\sqrt{(R_{\max}/R)^3-1}},\end{aligned}
$$



Introduce the normalized radius and transform its differential.

引入无量纲半径，并变换其微分。



$$
\begin{aligned}x&=\frac{R}{R_{\max}},\qquad dR=R_{\max}dx,\end{aligned}
$$



Separate the dimensional time scale from its dimensionless coefficient.

将有量纲时间尺度与无量纲系数分离。



$$
\begin{aligned}t_c&=R_{\max}\sqrt{\frac{\rho}{\Delta p_c}}\ C_t,\qquad C_t=\sqrt{\frac32}\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx.\end{aligned}
$$



**Symbols for Eq. (C1.5-E15).**

**式（C1.5-E15）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $t_c$ is ideal collapse time (s)<br>$t_c$ 为理想塌缩时间（s） | $R$ is radius (m)<br>$R$ 为半径（m） |
| $R_{\max}$ its maximum (m)<br>$R_{\max}$ 为其最大值（m） | $\dot R<0$ is inward velocity (m s⁻¹)<br>$\dot R<0$ 为向内速度（m s⁻¹） |
| $\rho$ is density (kg m⁻³)<br>$\rho$ 为密度（kg m⁻³） | $\Delta p_c>0$ is pressure difference (Pa)<br>$\Delta p_c>0$ 为压差（Pa） |
| $x=R/R_{\max}\in[0,1]$ is dimensionless radius<br>$x=R/R_{\max}\in[0,1]$ 为无量纲半径 | $C_t$ is the dimensionless time coefficient<br>$C_t$ 为无量纲时间系数 |
| $dx$ — Dimensionless-radius integration measure (dimensionless)<br>$dx$ — 无量纲半径积分微元（无量纲） | $dR$ — Radius integration measure (m)<br>$dR$ — 半径积分微元（m） |

**Conventions and conditions.** definite integrals follow the collapse branch.

**约定与条件。** 定积分沿塌缩分支进行。

![The endpoint singularity is integrable, so the model has a finite collapse time.](../assets/figures/c1-e15.svg)

The endpoint singularity is integrable, so the model has a finite collapse time.

端点奇异性可积，因此该模型具有有限塌缩时间。

**Check and interpretation.** The scale Rmax × sqrt(density/pressure) has units seconds. The integral is improper at its endpoints; its finite value is the formal zero-radius model time.

**检验与解释。** 尺度 Rmax × sqrt(密度/压差) 的单位为秒。积分在端点为广义积分；其有限值是模型到零半径的形式时间。

### Step 1.5.5 — Evaluate the Rayleigh time coefficient

### 步骤 1.5.5——计算瑞利塌缩时间系数

**Purpose in this chapter.** Evaluate the dimensionless integral in Eq. (C1.5-E15). This establishes the coefficient used in the worked collapse-time calculation.

**本章作用。** 计算式（C1.5-E15）的无量纲积分。由此确定塌缩时间算例所用的系数。

**Evaluate the coefficient.** Substitute the cube of normalized radius, including its Jacobian. The exponents combine as one half minus two thirds. The result is minus one sixth. Both beta-function arguments are positive, so the integral converges. The coefficient agrees with the published Rayleigh factor. [[R1]](../reference/sources.html#r1) [[R3]](../reference/sources.html#r3)

**计算系数。** 用无量纲半径的三次方换元，并计入雅可比因子。指数由二分之一减去三分之二，得到负六分之一。贝塔函数两个参数均为正，积分收敛。系数与文献瑞利因子一致。 [[R1]](../reference/sources.html#r1) [[R3]](../reference/sources.html#r3)

**Derivation.** Cube the normalized radius. Carry both the numerator exponent and Jacobian into the transformed integral. Match each exponent to the beta-function definition. Inspect both endpoints before evaluating the coefficient.

**推导。** 对无量纲半径取三次方换元。将分子指数与雅可比因子一同代入积分。逐项将指数与贝塔函数定义匹配。计算系数前先检查两个端点。

(C1.5-E16) · Evaluated beta-function coefficient / (C1.5-E16) · 通过贝塔函数计算的系数

Use the cube substitution to rewrite the numerator power.

采用三次方换元，改写分子的幂次。



$$
\begin{aligned}x^{3/2}&=(q^{1/3})^{3/2}=q^{1/2},\end{aligned}
$$



Multiply by the substitution Jacobian. The exponents combine to negative one sixth.

乘以换元的雅可比因子。幂次合并为负六分之一。



$$
\begin{aligned}x^{3/2}\,dx&=q^{1/2}\tfrac13q^{-2/3}\,dq=\tfrac13q^{-1/6}\,dq,\end{aligned}
$$



Combine the numerical prefactors and identify the first beta-function exponent.

合并数值前因子，并识别贝塔函数的第一个指数参数。



$$
\begin{aligned}\sqrt{3/2}/3&=1/\sqrt6,\quad a-1=-1/6\Rightarrow a=5/6,\end{aligned}
$$



Identify the second beta-function exponent from the square-root denominator.

由平方根分母识别贝塔函数的第二个指数参数。



$$
\begin{aligned}b-1&=-1/2\Rightarrow b=1/2,\end{aligned}
$$



Both beta-function parameters are positive. Evaluate the convergent integral to obtain the Rayleigh coefficient.

贝塔函数的两个参数均为正。计算收敛积分，得到瑞利系数。



$$
\begin{aligned}C_t&=B(5/6,1/2)/\sqrt6=0.9146813565\ldots .\end{aligned}
$$



State the cube substitution and its Jacobian together.

一并写出三次方换元及其雅可比因子。



$$
\begin{aligned}q&=x^3,\quad x=q^{1/3},\quad dx=\frac13q^{-2/3}\,dq,\end{aligned}
$$



Identify the transformed integral with the beta function and evaluate its coefficient.

将变换后的积分识别为贝塔函数，并计算其系数。



$$
\begin{aligned}C_t&=\frac{1}{\sqrt6}\int_0^1q^{-1/6}(1-q)^{-1/2}\,dq=\frac{1}{\sqrt6}B\left(\frac56,\frac12\right)=0.9146813565\ldots,\end{aligned}
$$



Use the integral definition with positive beta-function arguments.

采用贝塔函数参数为正时的积分定义。



$$
\begin{aligned}B(a,b)&=\int_0^1q^{a-1}(1-q)^{b-1}\,dq\quad(a>0,b>0).\end{aligned}
$$



**Symbols for Eq. (C1.5-E16).**

**式（C1.5-E16）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $x$ — Dimensionless radius divided by the maximum radius (dimensionless)<br>$x$ — 半径除以最大半径所得无量纲量（无量纲） | $q=x^3$ — Dimensionless substitution variable equal to the cube of the radius fraction (dimensionless)<br>$q=x^3$ — 等于半径比例立方的无量纲换元变量（无量纲） |
| $C_t$ is the dimensionless collapse-time coefficient<br>$C_t$ 为无量纲塌缩时间系数 | $B(a,b)$ is the beta function, defined by the displayed convergent integral (dimensionless)<br>$B(a,b)$ 为贝塔函数，由公式中的收敛积分定义（无量纲） |
| $a$ — Positive first argument of the beta function (dimensionless)<br>$a$ — 贝塔函数的正第一参数（无量纲） | $b$ — Positive second argument of the beta function (dimensionless)<br>$b$ — 贝塔函数的正第二参数（无量纲） |
| $dx$ — Dimensionless-radius integration measure (dimensionless)<br>$dx$ — 无量纲半径积分微元（无量纲） | $dq$ — Dimensionless substitution integration measure (dimensionless)<br>$dq$ — 无量纲换元积分微元（无量纲） |

**Conventions and conditions.** The numeral 6 inside the root is a dimensionless constant; the ellipsis indicates decimal continuation; $x,q\in[0,1]$ and $q=x^3$ define the substitution domain..

**约定与条件。** 根号中的数字 6 为无量纲常数；省略号表示后续小数；$x,q\in[0,1]$ 且 $q=x^3$ 确定换元范围。。

![The change of variables exposes the beta integral that fixes the numerical coefficient.](../assets/figures/c1-e16.svg)

The change of variables exposes the beta integral that fixes the numerical coefficient.

换元揭示贝塔积分，从而确定数值系数。

**Check and interpretation.** Both endpoint powers exceed −1, ensuring integrability. This dimensionless coefficient follows from the trajectory integral. It is independent of material fitting.

**检验与解释。** 两个端点幂指数均大于 −1，因而可积。此无量纲系数来自轨迹积分，不依赖材料拟合。

### Step 1.5.6 — Cross-check the ideal trajectory with pressure work

### 步骤 1.5.6——用压力功交叉检验理想轨迹

**Purpose in this chapter.** Insert Eq. (C1.5-E14) into the kinetic energy from Eq. (C1.4-E09). Agreement with pressure work checks the collapse branch and integration constant.

**本章作用。** 将式（C1.5-E14）代入式（C1.4-E09）的动能。与压力功的一致性用于检验塌缩分支及积分常数。

**Check pressure work.** Insert Eq. (C1.5-E14) into the kinetic-energy integral. The result equals work from the lost cavity volume. Energy vanishes at maximum radius and becomes positive during collapse. This checks the integration constant and sign.

**检验压力功。** 将式（C1.5-E14）代入动能积分。结果等于空腔体积减少产生的压力功。最大半径处动能为零，塌缩过程中为正。这检验了积分常数与符号。

**Derivation.**

**推导。**

(C1.5-E17) · Independent pressure-work conservation check / (C1.5-E17) · 独立的压力功守恒检验

#### 2. Substitute the ideal-collapse wall velocity

#### 代入理想塌缩壁面速度

From the previous Rayleigh-collapse integration, with constant positive $\Delta p_c=p_\infty-p_v$ and a cavity starting from rest at $R_{\max}$:

前面已经由 Rayleigh 理想塌缩方程积分得到，假设 $\Delta p_c=p_\infty-p_v>0$ 为常数，空腔从 $R_{\max}$ 处静止开始塌缩：



$$
\dot R^2=\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}R\right)^3-1\right].
$$



Insert this into $K_l=2\pi\rho R^3\dot R^2$:

将它代入 $K_l=2\pi\rho R^3\dot R^2$：



$$
\begin{aligned}K_l(R)
&=2\pi\rho R^3\,\frac{2\Delta p_c}{3\rho}
\left[\left(\frac{R_{\max}}R\right)^3-1\right]\end{aligned}
$$



Cancel density and expand the cube of the radius ratio.

约去密度，并展开半径比例的三次方。



$$
\begin{aligned}K_l(R)&=\frac{4\pi\Delta p_c}{3}R^3
\left[\frac{R_{\max}^3}{R^3}-1\right]\end{aligned}
$$



Distribute the radius cubed to obtain the difference of cavity volumes.

将半径三次方乘入括号，得到空腔体积之差对应的表达式。



$$
\begin{aligned}K_l(R)&=\frac{4\pi\Delta p_c}{3}\left(R_{\max}^3-R^3\right).\end{aligned}
$$



Thus,

因此：

Identify each spherical volume as four thirds pi times its radius cubed.

将每个球体积识别为其半径三次方乘以三分之四圆周率。



$$
\boxed{K_l(R)=\frac{4\pi}{3}\Delta p_c\left(R_{\max}^3-R^3\right)}.
$$



The cancellation of $\rho$ is algebraic: liquid density still affects the wall velocity, even though the energy expression at a specified radius no longer explicitly contains it.

$\rho$ 的消去只是代数结果：液体密度仍然影响壁面速度，只是在给定半径下的动能表达式中不再显式出现。

#### 3. Independent check using pressure work

#### 利用压力功独立检验

During collapse, the far-field pressure exceeds cavity pressure by $\Delta p_c$. The decrease in cavity volume is $V_{\max}-V(R)$, so the net pressure work released equals

塌缩时远场压力比腔内压力大 $\Delta p_c$。空腔体积减小 $V_{\max}-V(R)$，净压力功为：



$$
W=\int_R^{R_{\max}}\Delta p_c\,4\pi s^2\,ds
=\Delta p_c\frac{4\pi}{3}\left(R_{\max}^3-R^3\right).
$$



Because the ideal Rayleigh-collapse model begins at rest and neglects viscosity, surface tension, compressibility, and other energy reservoirs, all of this net pressure work becomes surrounding-liquid kinetic energy: $W=K_l$.

由于理想 Rayleigh 塌缩模型从静止开始，并忽略黏性、表面张力、可压缩性以及其他能量储存途径，所以净压力功全部转化为周围载液动能，即 $W=K_l$。

**Symbols for Eq. (C1.5-E17).**

**式（C1.5-E17）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $K_l$ is carrier kinetic energy (J)<br>$K_l$ 为载液动能（J） | $E_B$ the maximum-volume pressure-work scale (J)<br>$E_B$ 为最大体积的压力功尺度（J） |
| $R\in(0,R_{\max}]$ — Instantaneous cavity radius (m)<br>$R\in(0,R_{\max}]$ — 瞬时空腔半径（m） | $R_{\max}$ — Radius at the start of ideal collapse (m)<br>$R_{\max}$ — 理想塌缩开始时的半径（m） |
| $\rho$ is density (kg m⁻³)<br>$\rho$ 为密度（kg m⁻³） | $\Delta p_c$ is constant positive pressure difference (Pa)<br>$\Delta p_c$ 为常数正压差（Pa） |
| $V_{\max}$ is maximum cavity volume (m³)<br>$V_{\max}$ 为最大空腔体积（m³） | $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |
| $K_l/E_B$ is dimensionless and this control has zero viscous and capillary losses<br>$K_l/E_B$ 无量纲，此对照模型的黏性与毛细损失为零 | $V_b$ — cavity volume, $4\pi R^3/3$ (m³)<br>$V_b$ — 空腔体积，$4\pi R^3/3$（m³） |
| $V$ — dummy volume variable (m³)<br>$V$ — 积分哑体积变量（m³） | $t$ — time (s)<br>$t$ — 时间（s） |
| $\dot R$ — wall speed (m s⁻¹)<br>$\dot R$ — 壁面速度（m s⁻¹） |  |![The Rayleigh speed solution and pressure-work balance agree exactly.](../assets/figures/c1-e17.svg)

The Rayleigh speed solution and pressure-work balance agree exactly.

瑞利速度解与压力功平衡严格一致。

**Check and interpretation.** Pressure times displaced volume has joule units. Zero initial energy and positive growth during collapse agree with the mechanical power balance. Radial liquid energy does not specify jet energy.

**检验与解释。** 压差乘置换体积具有焦耳单位。初始动能为零，塌缩时动能增加，与机械功率平衡一致。径向液体动能不能确定射流动能。

### Worked example: 30 μm cavity

### 计算示例：30 μm 空腔

Prescribe maximum radius 30 μm, density 1000 kg m⁻³, and collapse pressure 100 kPa. These teaching inputs are not measured PFC properties. Substitute SI values before converting units. At half radius, the cubic ratio is eight. Subtracting one leaves seven.

规定最大半径 30 μm、密度 1000 kg m⁻³、塌缩压差 100 kPa。这些教学输入并非 PFC 实测物性。先代入 SI 数值，再换算单位。一半半径处的三次方比值为八，减去一得到七。

#### Step 1.5.7 — Put the ideal benchmark on a numerical scale

#### 步骤 1.5.7——给出理想基准的数值尺度

**Purpose in this chapter.** Apply Eqs. (C1.5-E14)–(C1.5-E17) to the declared teaching inputs. This translates the benchmark into time, energy, and speed before testing its validity.

**本章作用。** 将式（C1.5-E14）至（C1.5-E17）用于已声明的教学输入。由此先得到时间、能量与速度尺度，再检验适用性。

**Derivation.** Convert every teaching input to SI units. Compute the common pressure–density factor and cubic radius before inserting them into time, energy and speed formulas. The half-radius energy fraction follows from the cube of one half.

**推导。** 将全部教学输入换为 SI 单位。先计算共同压差密度因子及半径三次方，再代入时间、能量和速度公式。半径减半时的能量比例来自二分之一的三次方。

(C1.5-E18) · Declared teaching calculation / (C1.5-E18) · 采用明确给定参数的教学计算

Convert the declared teaching radius and pressure difference to SI units before substitution.

代入之前，先将给定教学半径与压差换算为 SI 单位。



$$
\begin{aligned}R_{\max}&=30\ \mu\mathrm m=30\times10^{-6}\ \mathrm m,\quad
      \Delta p_c=100\ \mathrm{kPa}=10^5\ \mathrm{Pa},\end{aligned}
$$



Evaluate the density-to-pressure square root. Its units convert a radius into a time scale.

计算密度与压力比的平方根。其单位使半径能够转换为时间尺度。



$$
\begin{aligned}\sqrt{\rho/\Delta p_c}&=\sqrt{1000/10^5}=0.1\ \mathrm{s\,m^{-1}},\end{aligned}
$$



Cube the maximum radius with its SI conversion included.

将已换算为 SI 单位的最大半径取三次方。



$$
\begin{aligned}R_{\max}^3&=27\times10^{-15}\ \mathrm{m^3},\end{aligned}
$$



Multiply the radius scale, density-pressure factor, and Rayleigh coefficient to obtain collapse time.

将半径尺度、密度—压力因子与瑞利系数相乘，得到塌缩时间。



$$
\begin{aligned}t_c&=0.9146813565(30\times10^{-6})(0.1)\ \mathrm s
      =2.7440440695\times10^{-6}\ \mathrm s,\end{aligned}
$$



Multiply maximum cavity volume by collapse pressure. This is the available ideal pressure work.

将最大空腔体积乘以塌缩压力。所得为可用理想压力功。



$$
\begin{aligned}E_B&=(4\pi/3)(10^5)(27\times10^{-15})\ \mathrm J
      =1.1309733553\times10^{-8}\ \mathrm J,\end{aligned}
$$



At half radius, evaluate the cubic ratio and remaining energy fraction explicitly.

在一半半径处，显式计算三次方比值及剩余能量比例。



$$
\begin{aligned}(R_{\max}/R)^3-1&=2^3-1=7,\quad K_l/E_B=1-(1/2)^3=7/8.\end{aligned}
$$



Convert the calculated collapse time to microseconds.

将算得塌缩时间换算为微秒。



$$
\begin{aligned}t_c&=0.9146813565(30\times10^{-6})\sqrt{\frac{1000}{100\times10^3}}\ \mathrm s=2.74404\ \mu\mathrm s,\end{aligned}
$$



Convert the available ideal pressure work to nanojoules.

将可用理想压力功换算为纳焦耳。



$$
\begin{aligned}E_B&=\frac{4\pi}{3}(100\times10^3)(30\times10^{-6})^3\ \mathrm J=11.3097\ \mathrm{nJ},\end{aligned}
$$



Evaluate the negative wall speed at half maximum radius.

计算最大半径一半处的负壁面速度。



$$
\begin{aligned}\dot R\big|_{R=R_{\max}/2}&=-\sqrt{\frac{2(100\times10^3)}{3(1000)}(8-1)}\ \mathrm{m\,s^{-1}}=-21.6025\ \mathrm{m\,s^{-1}},\end{aligned}
$$



Multiply available work by the half-radius energy fraction.

将可用功乘以一半半径处的能量比例。



$$
\begin{aligned}K_l\big|_{R=R_{\max}/2}&=\frac78E_B=9.89602\ \mathrm{nJ}.\end{aligned}
$$



**Symbols for Eq. (C1.5-E18).**

**式（C1.5-E18）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $t_c$ is collapse time (s)<br>$t_c$ 为塌缩时间（s） | $E_B$ pressure-work scale (J)<br>$E_B$ 为压力功尺度（J） |
| $K_l$ carrier kinetic energy (J)<br>$K_l$ 为载液动能（J） | $R$ current radius (m)<br>$R$ 为当前半径（m） |
| $R_{\max}=30\times10^{-6}$ m maximum radius<br>$R_{\max}=30\times10^{-6}$ m 为最大半径 | $\dot R$ is signed wall speed (m s⁻¹)<br>$\dot R$ 为带符号壁面速度（m s⁻¹） |
| $\Delta p_c=100\times10^3$ — Positive ideal-collapse pressure difference (Pa)<br>$\Delta p_c=100\times10^3$ — 正的理想塌缩压差（Pa） | $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |
| $\rho=1000$ — Substituted carrier density (kg m⁻³)<br>$\rho=1000$ — 代入的载液密度（kg m⁻³） |  |

**Conventions and conditions.** s, J, μs and nJ mean seconds, joules, microseconds and nanojoules; the vertical bar specifies half-radius evaluation.

**约定与条件。** s、J、μs 与 nJ 分别为秒、焦耳、微秒与纳焦耳；竖线表示在一半半径处取值。

![The original numerical control is preserved with its energy and branch checks.](../assets/figures/c1-e18.svg)

The original numerical control is preserved with its energy and branch checks.

保留原始数值对照，并补充能量与解分支检验。

**Check and interpretation.** One microsecond is 10⁻⁶ seconds; one nanojoule is 10⁻⁹ joules. The final values below agree with independent quadrature and pressure-work checks. These inputs are illustrative.

**检验与解释。** 一微秒为 10⁻⁶ 秒；一纳焦为 10⁻⁹ 焦。下列结果与独立积分及压力功检验一致。这些输入是教学示例。

Length × √(density/pressure) has units of seconds. Doubling radius doubles collapse time and increases work eightfold. Quadrupling pressure halves time and doubles speed at fixed radius fraction. The dimensionless initial-value problem, and hence its coefficient, stays unchanged. Gas cushioning, varying vapor pressure or confinement can change that problem.

长度 × √（密度／压力）的单位为秒。半径加倍使塌缩时间加倍、压力功增至八倍。压差增至四倍使时间减半、固定半径比例处速率加倍。无量纲初值问题及其系数保持不变。气体缓冲、变化蒸气压或约束可改变该问题。

The zero-radius limit gives finite energy and divergent wall speed. Physical maximum speed: Not established. Missing: compressibility, internal pressure, heat and mass transfer, molecular scales and interface distortion. The next equation locates a chosen Mach threshold on the ideal trajectory. It supplies a diagnostic, not a collapse-arrest law.

零半径极限给出有限能量与发散壁面速率。实际最大速率尚未确立。缺失：可压缩性、内部压力、传热传质、分子尺度及界面变形。下一式定位理想轨迹上的所选马赫数阈值。它是诊断条件，并非塌缩终止规律。

#### Step 1.5.8 — Locate where the ideal speed needs further physics

#### 步骤 1.5.8——定位理想速度需要补充物理的位置

**Purpose in this chapter.** Compare the ideal wall speed with a chosen Mach threshold. This diagnoses the incompressible trajectory without establishing a physical maximum speed.

**本章作用。** 将理想壁面速度与选定的马赫数阈值比较。这用于诊断不可压缩轨迹，不确立实际最大速度。

**Derivation.**

**推导。**

(C1.5-E19) · Ideal-trajectory diagnostic, not a physical limit / (C1.5-E19) · 理想轨迹的诊断指标，而非物理极限

#### 1. Start from the Rayleigh collapse velocity

#### 从 Rayleigh 塌缩速度出发

We previously derived the bubble-wall velocity for ideal spherical collapse:

前面已经推导出理想球形塌缩的壁面速度：



$$
\dot R=-\sqrt{\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}{R}\right)^3-1\right]}.
\tag{1}
$$



Here, $\Delta p_c=p_\infty-p_v>0$ is the constant collapse-driving pressure difference, $\rho$ is the surrounding liquid density, and $R_{\max}$ is the initial maximum bubble radius.

其中，$\Delta p_c=p_\infty-p_v>0$ 是恒定的塌缩驱动压差，$\rho$ 为周围液体密度，$R_{\max}$ 为初始最大气泡半径。

Define the dimensionless radius ratio:

定义无量纲半径比例：



$$
x=\frac{R}{R_{\max}}.
$$



Therefore,

因此：

Substitute the normalized radius into the collapse speed and take its magnitude.

将归一化半径代入塌缩速度，并取速度大小。



$$
|\dot R|=\sqrt{\frac{2\Delta p_c}{3\rho}(x^{-3}-1)}.
\tag{2}
$$



#### 2. Introduce the wall Mach number

#### 引入壁面马赫数

The wall Mach number is defined as the magnitude of wall velocity divided by the liquid sound speed $c$:

壁面马赫数定义为壁面速度大小与液体声速 $c$ 之比：



$$
M_w=\frac{|\dot R|}{c}.
$$



Substituting equation (2) gives

将式 (2) 代入，得到：



$$
M_w=\frac{1}{c}\sqrt{\frac{2\Delta p_c}{3\rho}(x^{-3}-1)}.
$$



Squaring both sides:

两侧平方：



$$
M_w^2=\frac{2\Delta p_c}{3\rho c^2}(x^{-3}-1).
$$



Rearranging step by step:

逐步整理：

Divide by the positive pressure coefficient to isolate the radius-dependent factor.

除以正的压力系数，分离出随半径变化的因子。



$$
\frac{3\rho c^2M_w^2}{2\Delta p_c}=x^{-3}-1,
$$



Add one to both sides to isolate the inverse cube of the radius ratio.

两侧加一，分离出半径比例的负三次方。



$$
x^{-3}=1+\frac{3\rho c^2M_w^2}{2\Delta p_c},
$$



The radius ratio is positive; take the negative one-third power of both sides.

半径比例为正；对两侧取负三分之一次幂。



$$
\boxed{x=\left[1+\frac{3\rho c^2M_w^2}{2\Delta p_c}\right]^{-1/3}}.
\tag{3}
$$



Now choose a diagnostic Mach threshold $M_*$, and define $x_M$ as the radius ratio where the ideal trajectory first reaches that threshold:

现在选择一个诊断用马赫数阈值 $M_*$，并将 $x_M$ 定义为理想塌缩轨迹首次达到该阈值时的半径比例：



$$
\boxed{x_M=\frac{R_M}{R_{\max}}=\left[1+\frac{3\rho c^2M_*^2}{2\Delta p_c}\right]^{-1/3}}.
$$



This is exactly the formula in the screenshot.

这就是截图中公式的完整来源。

#### 3. What does the radius ratio mean?

#### 这个半径比例代表什么？

For example, the course uses $M_*=0.1$, $c=1500\ \mathrm{m/s}$, $\rho=1000\ \mathrm{kg/m^3}$, and $\Delta p_c=100\ \mathrm{kPa}$.

例如，课程采用 $M_*=0.1$、$c=1500\ \mathrm{m/s}$、$\rho=1000\ \mathrm{kg/m^3}$、$\Delta p_c=100\ \mathrm{kPa}$。

Substitution gives:

代入：



$$
x_M=\left[1+\frac{3(1000)(1500)^2(0.1)^2}{2(100000)}\right]^{-1/3}\approx\boxed{0.1435}.
$$



This means that **within the ideal Rayleigh model**, the wall speed reaches $0.1c=150\ \mathrm{m/s}$ when the bubble radius decreases to about 14.35% of its initial maximum value. The threshold radius is $R_M=0.1435R_{\max}$.

这意味着，**在理想 Rayleigh 模型内**，当气泡半径减小至初始最大半径的约 14.35% 时，壁面速度达到 $0.1c=150\ \mathrm{m/s}$。此时阈值半径为 $R_M=0.1435R_{\max}$。

#### 4. Why is this only a diagnostic?

#### 为什么它只是诊断指标？

The ideal Rayleigh model assumes incompressible liquid. As $R\to0$, equation (1) predicts $|\dot R|\to\infty$. This divergence is a mathematical consequence of the idealizations, not a physically attainable speed.

理想 Rayleigh 模型假设液体不可压缩。当 $R\to0$ 时，式 (1) 预测 $|\dot R|\to\infty$。这一发散是理想化假设的数学结果，并非物理上能够实现的速度。

Choosing $M_*=0.1$ is a conservative diagnostic convention for identifying when liquid compressibility may warrant closer examination. It is **not a universal threshold** at which incompressible theory suddenly becomes invalid.

选择 $M_*=0.1$，是一种保守的诊断约定，用于识别何时需要更加仔细地考虑液体可压缩性。它**不是不可压缩理论突然失效的普适临界值**。

Within the ideal trajectory, $R<R_M$ corresponds to $M_w>M_*$. However, a real cavity may be affected by vapor condensation, permanent gas, acoustic radiation, shocks, and other phenomena before reaching this radius.

在理想轨迹中，$R<R_M$ 对应 $M_w>M_*$。但真实空腔可能在达到该半径之前，就已经受到蒸气凝结、非凝结气体、声辐射、冲击波等因素的影响。

**Symbols for Eq. (C1.5-E19).**

**式（C1.5-E19）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $M_w$ is wall Mach number (dimensionless)<br>$M_w$ 为壁面马赫数（无量纲） | $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） |
| $c>0$ is stipulated carrier sound speed (m s⁻¹)<br>$c>0$ 为给定载液声速（m s⁻¹） | $M_*>0$ is a selected diagnostic Mach value (dimensionless)<br>$M_*>0$ 为选择的诊断马赫值（无量纲） |
| $x_M=R_M/R_{\max}$ is the radius fraction when $M_w=M_*$ (dimensionless)<br>$x_M=R_M/R_{\max}$ 为 $M_w=M_*$ 时的半径比例（无量纲） | $R_M$ — Cavity radius at the selected Mach value (m)<br>$R_M$ — 选定马赫数处的空腔半径（m） |
| $R_{\max}$ — Radius at the start of ideal collapse (m)<br>$R_{\max}$ — 理想塌缩开始时的半径（m） | $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） |
| $\Delta p_c$ is positive collapse pressure (Pa)<br>$\Delta p_c$ 为正塌缩压差（Pa） | $x$ — normalized radius, $R/R_{\max}$ (1)<br>$x$ — 无量纲半径，$R/R_{\max}$（1） |
| $R$ — current cavity radius (m)<br>$R$ — 当前空腔半径（m） |  |

**Conventions and conditions.** absolute bars denote magnitude; The number uses the previous teaching density and pressure; Teaching inputs use the preceding density and pressure, with $c=1500$ m s⁻¹ and chosen $M_*=0.1$.

**约定与条件。** 绝对值符号表示大小；数值使用前述教学密度与压差；教学输入采用前述密度和压差，并取 $c=1500$ m s⁻¹、选定 $M_*=0.1$。

![A Mach diagnostic exposes the shrinking validity range of incompressible collapse.](../assets/figures/c1-e19.svg)

A Mach diagnostic exposes the shrinking validity range of incompressible collapse.

马赫数诊断揭示不可压缩塌缩模型的适用范围不断缩小。

**Check and interpretation.** The bracket is dimensionless and exceeds one, so the diagnostic radius lies below maximum radius. As threshold tends to zero, its radius approaches the starting radius. Singular zero radius remains outside physical validity.

**检验与解释。** 括号无量纲且大于一，因此诊断半径小于最大半径。阈值趋于零时，诊断半径趋于初始最大半径。奇异零半径仍超出物理适用范围。

## 1.6 Pressure impulse and direction

## 1.6 压力冲量与方向

### Step 1.6.1 — Summarize a pressure history as pressure impulse

### 步骤 1.6.1——用压力冲量概括压力历程

**Purpose in this chapter.** Move from spherical radius dynamics to spatial liquid response. Define a local time-integrated pressure field whose gradient enters the next momentum calculation.

**本章作用。** 从球形半径动力学转向空间液体响应。定义局部压力时间积分场，其梯度将进入下一步动量计算。

**Define pressure impulse.** Integrate local pressure relative to a spatially uniform reference over time. Pressure impulse has units Pa s. Its spatial gradient drives liquid velocity change. Acoustic crossing time has units s. The cited short-event model motivates the following integration and approximation. [[R2]](../reference/sources.html#r2)

**定义压力冲量。** 对局部压力相对于空间均匀参考值作时间积分。压力冲量单位为 Pa s，其空间梯度驱动液体速度变化。声传播时间单位为 s。所引短事件模型提供以下积分与近似的依据。 [[R2]](../reference/sources.html#r2)

**Derivation.**

**推导。**

(C1.6-E20) · Definition of local pressure impulse / (C1.6-E20) · 局部压力冲量的定义

#### 1. What does C1.6-E20 integrate?

#### C1.6-E20 对什么积分？

At one fixed liquid position, integrate pressure excess over the stated event interval. This defines pressure impulse.

在固定液体位置，对给定事件区间内的超压作时间积分。由此定义压力冲量。



$$
\boxed{\Pi(\boldsymbol x)=\int_{t_0}^{t_1}[p(\boldsymbol x,t)-p_{\mathrm{ref}}(t)]\,dt}
$$



Here, $\boldsymbol x$ is a fixed Eulerian observation point, $t$ is the integration variable, and $[t_0,t_1]$ is the chosen pressure-event interval. $p_{\mathrm{ref}}$ is a spatially uniform reference pressure, possibly varying with time. The result $\Pi(\boldsymbol x)$ is a field over the liquid domain and has units Pa·s.

其中，$\boldsymbol x$ 是固定的欧拉空间观察点，$t$ 是积分变量，$[t_0,t_1]$ 是选定压力事件的持续时间。$p_{\mathrm{ref}}$ 是空间均匀、但可以随时间变化的参考压力。$\Pi(\boldsymbol x)$ 是定义在液体区域上的场，单位为 Pa·s。

Choose a fixed point A in the liquid. Plot the local excess-pressure history against time; the **signed area** under the curve over the selected interval is $\Pi(\boldsymbol x_A)$. Repeat at other points to reconstruct the spatial field. There is **no volume integral or surface integral in C1.6-E20**.

选择液体中的一个固定点 A，将该点的超压随时间绘图，曲线在指定时间区间内的**带符号面积**即为 $\Pi(\boldsymbol x_A)$。对其他位置重复即可重建空间冲量场。**C1.6-E20 不涉及体积分或面积分。**

A fixed Eulerian location is not an individual fluid parcel. The formula assumes that this location belongs to the liquid domain throughout the selected time interval. If the moving phase boundary crosses it, the integration domain or formulation must be reconsidered.

固定欧拉观察点并不是随液体质点运动的位置。该式要求该点在整个选定时间区间内属于液体域。如果运动界面穿过该点，则须重新界定积分区间或采用适合运动界面的形式。

#### 2. Why is the time integral useful?

#### 为什么时间积分重要？

For rectangular excess-pressure pulses, $\Pi=\Delta p\,\tau$. An illustrative 2 MPa pulse lasting 1 μs and a 1 MPa pulse lasting 2 μs both give 2 Pa·s. They have different peak pressures but equal time-integrated pressure at that location.

对于矩形超压脉冲，$\Pi=\Delta p\,\tau$。例如，2 MPa、持续 1 μs 的脉冲与 1 MPa、持续 2 μs 的脉冲，其压力冲量均为 2 Pa·s。两者峰值压力不同，但该位置的压力时间积分相等。

Equal impulse at a **single point** does not ensure equal velocity fields; the spatial impulse distribution, boundaries, compressibility, and the event regime also matter.

但在**单个点**具有相同压力冲量，并不保证获得相同的速度场；空间冲量分布、边界条件、可压缩性以及过程所处的物理机制同样重要。

#### 3. Derivation from momentum conservation

#### 从动量守恒推导

For an incompressible Newtonian liquid of constant density,

对于密度恒定的不可压缩牛顿流体：



$$
\rho\left[\frac{\partial\boldsymbol u}{\partial t}+(\boldsymbol u\cdot\nabla)\boldsymbol u\right]=-\nabla p+\mu\nabla^2\boldsymbol u.
$$



Time integration at a fixed position, with $\nu=\mu/\rho$, yields the equation appearing in C1.6-E21:

在固定空间位置对时间积分，并令 $\nu=\mu/\rho$，得到 C1.6-E21：



$$
\Delta\boldsymbol u=-\frac{\nabla\Pi}{\rho}-\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt+\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt.
$$



The spatially uniform reference pressure drops out when taking the gradient. If the integrated convective and viscous terms are negligible relative to pressure forcing, the reduced equation is

由于参考压力在空间中均匀，其梯度为零。如果积分后的对流项和黏性项相对于压力驱动可忽略，得到：



$$
\boxed{\Delta\boldsymbol u\simeq-\frac{1}{\rho}\nabla\Pi}.
$$



**Thus the spatial gradient of pressure impulse—not merely the local impulse magnitude—determines the leading-order velocity increment and direction.**

**因此，在该近似下，决定速度增量及其方向的是压力冲量的空间梯度，而非某一点的冲量大小本身。**

For the incompressible, fixed-domain reduced problem, taking the divergence of this relation yields $\nabla^2\Pi=0$. This Laplace equation needs boundary conditions on the cavity, walls, and outlets. A spatially uniform addition to $\Pi$ changes no velocity because its gradient is zero.

对于不可压缩、固定区域内的简化模型，对该式取散度得到 $\nabla^2\Pi=0$。这一拉普拉斯方程还需要空腔、壁面和出口的边界条件。对 $\Pi$ 增加空间均匀常数不会改变速度，因为其梯度为零。

#### 4. Pressure impulse versus force impulse

#### 压力冲量与力学冲量的区别

The local pressure impulse $\Pi(\boldsymbol x)$ has units **Pa·s = N·s/m²**. It is a time-integrated pressure *at a point*. To obtain a resultant **force impulse** on a fixed surface $S$, one must also integrate pressure traction over that surface:

局部压力冲量 $\Pi(\boldsymbol x)$ 的单位为 **Pa·s = N·s/m²**，表示某一点的压力时间积分。要得到固定表面 $S$ 上的合**力学冲量**，还需要对该表面上的压力牵引做面积分：



$$
\boxed{\boldsymbol J_p=-\int_{t_0}^{t_1}\int_S[p(\boldsymbol x,t)-p_{\rm ref}(t)]\boldsymbol n\,dA\,dt}
$$



where $\boldsymbol n$ is the chosen outward normal of the receiving fluid/control surface; the sign depends on the traction convention. For a fixed surface this can be written $\boldsymbol J_p=-\int_S\Pi(\boldsymbol x)\boldsymbol n\,dA$. Its units are N·s (kg·m/s). For a moving or deforming wall, the instantaneous area and normal change; viscous traction and momentum flux may also be needed.

其中 $\boldsymbol n$ 是按约定选取的表面外法向，符号取决于牵引方向约定。对于固定表面，可写为 $\boldsymbol J_p=-\int_S\Pi(\boldsymbol x)\boldsymbol n\,dA$。其单位为 N·s（kg·m/s）。若壁面运动或变形，瞬时表面积和法向会发生变化；还可能需要计入黏性牵引和动量通量。

In the special case of a planar fixed patch of area $A$ with uniform normal pressure impulse, $|\boldsymbol J_p|=A\Pi$ when $\Pi\ge0$. This special case must not be applied directly to a changing spherical cavity interface.

只有对于面积为 $A$ 的固定平面、且法向压力冲量均匀时，若 $\Pi\ge0$，才可写成 $|\boldsymbol J_p|=A\Pi$。不能将这一特例直接用于不断变化的球形空腔界面。

**Symbols for Eq. (C1.6-E20).**

**式（C1.6-E20）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\boldsymbol x$ is fixed liquid position (m)<br>$\boldsymbol x$ 为固定液体位置（m） | $\Pi$ is pressure impulse (Pa s)<br>$\Pi$ 为压力冲量（Pa s） |
| $p$ is local pressure (Pa)<br>$p$ 为局部压力（Pa） | $p_{\mathrm{ref}}$ a spatially uniform reference (Pa)<br>$p_{\mathrm{ref}}$ 为空间均匀参考压力（Pa） |
| $t$ is time (s)<br>$t$ 为时间（s） | $t_0$ — Event start time (s)<br>$t_0$ — 事件开始时刻（s） |
| $t_1$ — Event end time (s)<br>$t_1$ — 事件结束时刻（s） | $\tau$ is event duration (s)<br>$\tau$ 为持续时间（s） |
| $q$ — gauge pressure (Pa)<br>$q$ — 表压（Pa） | $N$ — positive integer subdivision count (1)<br>$N$ — 正整数分段数（1） |
| $k$ — time-sample index (1)<br>$k$ — 时间采样指标（1） | $t_k$ — sample time (s)<br>$t_k$ — 采样时刻（s） |
| $\Delta t$ — time-step width (s)<br>$\Delta t$ — 时间段宽度（s） | $\boldsymbol J_p$ — gauge-pressure mechanical impulse on the liquid control volume (N s)<br>$\boldsymbol J_p$ — 作用于液体控制体的表压机械冲量（N s） |
| $S(t)$ — liquid control-volume surface (m²)<br>$S(t)$ — 液体控制体表面（m²） | $\boldsymbol n$ — outward unit normal to the control surface (1)<br>$\boldsymbol n$ — 控制表面向外单位法向（1） |
| $dA$ — area element (m²)<br>$dA$ — 面积元（m²） | $\rho$ — constant liquid density (kg m⁻³)<br>$\rho$ — 恒定液体密度（kg m⁻³） |
| $\boldsymbol u$ — liquid velocity field (m s⁻¹)<br>$\boldsymbol u$ — 液体速度场（m s⁻¹） | $\mu$ — dynamic viscosity (Pa s)<br>$\mu$ — 动力黏度（Pa s） |
| $\nu$ — kinematic viscosity (m² s⁻¹)<br>$\nu$ — 运动黏度（m² s⁻¹） | $\Delta\boldsymbol u$ — fixed-position velocity increment (m s⁻¹)<br>$\Delta\boldsymbol u$ — 固定位置速度增量（m s⁻¹） |
| $S$ — fixed receiving surface (m²)<br>$S$ — 固定受载表面（m²） | $A$ — fixed planar patch area (m²)<br>$A$ — 固定平面面积（m²） |
| $\nabla$ — spatial gradient (m⁻¹)<br>$\nabla$ — 空间梯度（m⁻¹） | $\nabla^2$ — vector Laplacian (m⁻²)<br>$\nabla^2$ — 矢量拉普拉斯算子（m⁻²） |

**Conventions and conditions.** Square brackets on $\Pi$ denote units, not endpoint evaluation; The integral is at fixed position in a liquid domain whose displacement will be assessed below; Brackets denote units; fixed-surface reduction requires fixed orientation and all sampled points remaining liquid.

**约定与条件。** $\Pi$ 的方括号表示单位，而非端点取值；积分在固定位置进行，液体区域的位移将在下文评估；方括号表示单位；固定表面约化要求方向固定且全部采样点始终位于液体中。

![Impulse combines duration and amplitude at each liquid position.](../assets/figures/c1-e20.svg)

Impulse combines duration and amplitude at each liquid position.

压力冲量在每个液体位置组合压力幅值与持续时间。

**Check and interpretation.** A constant reference shifts the local pressure integral without changing its spatial gradient. Absolute contact loads require the actual exterior pressure and viscous traction. A point crossed by an interface needs a moving-domain formulation.

**检验与解释。** 常数参考压力可改变局部压力积分，但不改变其空间梯度。绝对接触载荷需要实际外部压力和黏性牵引。若界面穿过观察点，则需要运动域表述。

### Step 1.6.2 — Convert pressure history into liquid velocity change

### 步骤 1.6.2——将压力历程转为液体速度变化

**Purpose in this chapter.** Use the pressure impulse defined in Eq. (C1.6-E20). Integrating momentum separates pressure, convective, and viscous contributions to velocity change. This exact model identity is the starting point for Eq. (C1.6-E22).

**本章作用。** 采用式（C1.6-E20）定义的压力冲量。积分动量方程，分离压力、对流与黏性对速度变化的贡献。这一模型内精确恒等式是式（C1.6-E22）的起点。

**Derivation.**

**推导。**

(C1.6-E21) · Exact fixed-position integrated incompressible momentum / (C1.6-E21) · 固定位置处不可压缩动量方程的精确时间积分

#### 1. Start from the Navier–Stokes equation

#### 从 Navier–Stokes 方程出发

For an incompressible Newtonian liquid with constant density $\rho$, dynamic viscosity $\mu$, and no body forces, the momentum equation is

对于密度 $\rho$、动力黏度 $\mu$ 均为常数、且忽略体积力的不可压缩牛顿流体，动量方程为：



$$
\boxed{\rho\left[\frac{\partial\boldsymbol u}{\partial t}+(\boldsymbol u\cdot\nabla)\boldsymbol u\right]=-\nabla p+\mu\nabla^2\boldsymbol u}\tag{1}
$$



Here, $\boldsymbol u(\boldsymbol x,t)$ is the velocity field, $p(\boldsymbol x,t)$ is pressure, $\nabla p$ is the pressure gradient, and $\nabla^2\boldsymbol u$ is the vector Laplacian of velocity. The notation $(\boldsymbol u\cdot\nabla)\boldsymbol u$ denotes convective acceleration.

其中，$\boldsymbol u(\boldsymbol x,t)$ 是速度场，$p(\boldsymbol x,t)$ 是压力场，$\nabla p$ 是压力梯度，$\nabla^2\boldsymbol u$ 是速度的矢量拉普拉斯算子。$(\boldsymbol u\cdot\nabla)\boldsymbol u$ 表示对流加速度。

Divide both sides by $\rho$, and define the kinematic viscosity $\nu=\mu/\rho$:

两侧除以 $\rho$，并定义运动黏度 $\nu=\mu/\rho$：



$$
\boxed{\frac{\partial\boldsymbol u}{\partial t}=-\frac{\nabla p}{\rho}-(\boldsymbol u\cdot\nabla)\boldsymbol u+\nu\nabla^2\boldsymbol u}\tag{2}
$$



This equation states that the local velocity changes because of pressure gradients, convective transport, and viscous effects.

这个方程表示：局部速度的变化由压力梯度、对流输运以及黏性作用共同决定。

#### 2. Integrate every term over time

#### 对每一项分别进行时间积分

Fix a spatial point $\boldsymbol x$, and integrate equation (2) from $t_0$ to $t_1$:

固定空间位置 $\boldsymbol x$，对式 (2) 从 $t_0$ 到 $t_1$ 积分：



$$
\begin{aligned}
\int_{t_0}^{t_1}\frac{\partial\boldsymbol u}{\partial t}\,dt
={}&-\frac1\rho\int_{t_0}^{t_1}\nabla p\,dt\\
&-\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt\\
&+\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt.
\end{aligned}\tag{3}
$$



Notice that there are **four terms**. We have not discarded any of them.

注意，这里一共有**四项**，我们没有忽略其中任何一项。

#### Term 1: Local acceleration

#### 第一项：局部加速度

Because $\boldsymbol x$ is fixed, the fundamental theorem of calculus gives

因为 $\boldsymbol x$ 保持固定，根据微积分基本定理：



$$
\begin{aligned}\int_{t_0}^{t_1}\frac{\partial\boldsymbol u(\boldsymbol x,t)}{\partial t}\,dt
&=\boldsymbol u(\boldsymbol x,t_1)-\boldsymbol u(\boldsymbol x,t_0)\end{aligned}
$$



Define this endpoint difference as the fixed-position velocity increment.

将该端点差定义为固定位置的速度增量。



$$
\begin{aligned}\int_{t_0}^{t_1}\frac{\partial\boldsymbol u(\boldsymbol x,t)}{\partial t}\,dt&=\boxed{\Delta\boldsymbol u}.\end{aligned}\tag{4}
$$



This is the **velocity change at the same spatial location**, not the displacement of a liquid particle.

这是**同一空间位置上的速度变化**，而不是液体质点的位移。

#### Term 2: Pressure gradient

#### 第二项：压力梯度

For a sufficiently smooth pressure field, spatial differentiation and time integration commute:

对于足够光滑的压力场，空间求导与时间积分可以交换次序：



$$
\int_{t_0}^{t_1}\nabla p(\boldsymbol x,t)\,dt
=\nabla\left[\int_{t_0}^{t_1}p(\boldsymbol x,t)\,dt\right].\tag{5}
$$



Recall the definition of pressure impulse:

回忆压力冲量的定义：



$$
\Pi(\boldsymbol x)=\int_{t_0}^{t_1}[p(\boldsymbol x,t)-p_{\mathrm{ref}}(t)]\,dt.
$$



Because $p_{\mathrm{ref}}(t)$ is spatially uniform, its spatial gradient is zero. Therefore,

由于 $p_{\mathrm{ref}}(t)$ 在空间中均匀，其空间梯度为零，因此：



$$
\begin{aligned}\nabla\Pi&=\nabla\int_{t_0}^{t_1}p(\boldsymbol x,t)\,dt
-\underbrace{\nabla\int_{t_0}^{t_1}p_{\mathrm{ref}}(t)\,dt}_{=0}\end{aligned}
$$



The spatially uniform reference contributes zero gradient; commute the remaining gradient and integral.

空间均匀参考压强的梯度为零；交换剩余梯度与积分的次序。



$$
\begin{aligned}\nabla\Pi&=\int_{t_0}^{t_1}\nabla p\,dt.\end{aligned}\tag{6}
$$



Consequently, the pressure term in equation (3) becomes

因此，式 (3) 中的压力项就变成：



$$
\boxed{-\frac1\rho\int_{t_0}^{t_1}\nabla p\,dt=-\frac{\nabla\Pi}{\rho}}\tag{7}
$$



**This is the crucial mathematical step connecting pressure impulse to the momentum equation.**

**这就是将压力冲量与动量方程联系起来的关键数学步骤。**

#### Terms 3 and 4: Convection and viscosity

#### 第三、四项：对流与黏性

The remaining integrals are retained in their original forms:

剩余两项的积分保留原来的形式：



$$
-\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt
\qquad\text{and}\qquad
\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt.
$$



Unlike the local time derivative, these terms generally cannot be reduced to simple differences between their values at $t_0$ and $t_1$. Evaluating them requires the velocity field throughout the integration interval.

与局部时间导数不同，这两项通常不能直接化为在 $t_0$ 和 $t_1$ 时刻的函数值之差。计算它们需要知道整个积分时间段内的速度场。

#### 3. Assemble the equation

#### 合并各项

Substituting equations (4) and (7) into equation (3) yields

将式 (4)、(7) 代回式 (3)，就得到：



$$
\boxed{\begin{aligned}
\Delta\boldsymbol u
={}&-\frac{\nabla\Pi}{\rho}\\
&-\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt\\
&+\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt.
\end{aligned}}\tag{C1.6-E21}
$$



**This is exactly C1.6-E21. It is simply the time-integrated Navier–Stokes equation, with the pressure integral rewritten using the definition of pressure impulse.**

**这就是 C1.6-E21。它本质上只是对 Navier–Stokes 方程进行时间积分，并利用压力冲量的定义改写压力积分项。**

It is exact within the stated incompressible, constant-property model, provided the fixed observation point remains in the liquid domain over the integration interval. We have not yet made the short-event approximation.

在所述不可压缩、常物性模型内，只要固定观察点在整个积分时间段均属于液体区域，这个关系就是精确的。到目前为止，我们还没有使用短时事件近似。

**Symbols for Eq. (C1.6-E21).**

**式（C1.6-E21）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\Delta\boldsymbol u$ is fixed-position velocity change (m s⁻¹)<br>$\Delta\boldsymbol u$ 为固定位置速度变化（m s⁻¹） | $\boldsymbol u$ velocity (m s⁻¹)<br>$\boldsymbol u$ 为速度（m s⁻¹） |
| $\Pi$ is pressure impulse (Pa s)<br>$\Pi$ 为压力冲量（Pa s） | $\rho$ is constant density (kg m⁻³)<br>$\rho$ 为常数密度（kg m⁻³） |
| $\mu$ is viscosity (Pa s)<br>$\mu$ 为黏度（Pa s） | $\nu$ is kinematic viscosity (m² s⁻¹)<br>$\nu$ 为运动黏度（m² s⁻¹） |
| $t_0$ — Event start time (s)<br>$t_0$ — 事件开始时刻（s） | $t_1$ — Event end time (s)<br>$t_1$ — 事件结束时刻（s） |
| $t$ — Elapsed time (s)<br>$t$ — 经过时间（s） | $\boldsymbol x$ is fixed position (m)<br>$\boldsymbol x$ 为固定位置（m） |
| $p$ — local liquid pressure (Pa)<br>$p$ — 局部液体压力（Pa） | $p_{\mathrm{ref}}$ — spatially uniform reference pressure (Pa)<br>$p_{\mathrm{ref}}$ — 空间均匀参考压力（Pa） |
| $\nabla$ — spatial gradient operator (m⁻¹)<br>$\nabla$ — 空间梯度算子（m⁻¹） | $\nabla^2$ — vector Laplacian operator (m⁻²)<br>$\nabla^2$ — 矢量拉普拉斯算子（m⁻²） |
| $\partial_t$ — time derivative at fixed position (s⁻¹)<br>$\partial_t$ — 固定位置的时间导数（s⁻¹） |  |

**Conventions and conditions.** the dot is a true vector contraction in convective acceleration, not an equation separator.

**约定与条件。** 圆点是对流加速度中的真正矢量缩并，并非公式分隔符。

![The short-event approximation must justify removing convective and viscous impulses.](../assets/figures/c1-e21.svg)

The short-event approximation must justify removing convective and viscous impulses.

短事件近似必须说明为何可以删除对流与黏性冲量。

**Check and interpretation.** The convective and viscous terms remain integrals because their fields evolve. Each integrated term has units velocity. Time-dependent bounds that depend on position require additional gradient terms.

**检验与解释。** 对流和黏性场随时间变化，因此对应项仍为积分。每个积分项均具有速度单位。若时间上下限依赖位置，则梯度运算会产生额外项。

### Step 1.6.3 — Decide when pressure impulse dominates the event

### 步骤 1.6.3——判断事件何时由压力冲量主导

**Purpose in this chapter.** Estimate the convective and viscous terms retained in Eq. (C1.6-E21). Under the stated short-event conditions, the reduced model links incompressibility to a pressure-impulse boundary problem.

**本章作用。** 估计式（C1.6-E21）保留的对流与黏性项。在已声明的短事件条件下，约化模型将不可压缩条件连接至压力冲量边值问题。

**Bound the omitted scales.** Choose representative liquid speed and variation length. Convective impulse scales as speed × duration/length. Viscous impulse scales as kinematic viscosity × duration/length². Small interface displacement permits fixed boundary geometry. These scale diagnostics provide no guaranteed singular-boundary-layer error bound. Under these conditions, subtract incompressible velocities and take the divergence.

**估算被忽略项的尺度。** 选取代表性液体速率与变化长度。对流冲量尺度为速率 × 时间／长度。黏性冲量尺度为运动黏度 × 时间／长度²。小界面位移允许固定边界几何。这些尺度诊断不能保证奇异边界层的误差界限。在这些条件下，将不可压缩速度相减并取散度。

**Derivation.**

**推导。**

(C1.6-E22) · Short-event reduced pressure-impulse model / (C1.6-E22) · 短时事件的简化压力冲量模型

#### 4. Where does the next approximation come from?

#### 下一步的近似从哪里来？

C1.6-E22 is a separate approximation. If the event lasts $\tau=t_1-t_0$, the flow varies over a spatial scale $L$, and characteristic speed is $U$, then the convective and viscous terms are small relative to a characteristic velocity change when the corresponding ratios are small:

C1.6-E22 是另外一步近似。若事件持续 $\tau=t_1-t_0$，流场变化的特征长度为 $L$，特征速度为 $U$，那么当相应比值足够小时，对流和黏性项相对于特征速度变化较小：



$$
\frac{U\tau}{L}\ll1,\qquad\frac{\nu\tau}{L^2}\ll1.
$$



Provided the relevant velocity-change scaling and boundary conditions support these omissions, C1.6-E21 reduces to

在速度变化的尺度估计与边界条件也支持忽略这两项时，C1.6-E21 才简化为：



$$
\boxed{\Delta\boldsymbol u\simeq-\frac{\nabla\Pi}{\rho}}\tag{C1.6-E22}
$$



The two equations must not be conflated: C1.6-E21 retains all three acceleration mechanisms and is exact under the stated model; C1.6-E22 neglects two of them and requires additional assumptions.

不能将这两个方程混为一谈：C1.6-E21 保留全部三个加速机制，在所述模型内是精确的；C1.6-E22 则忽略其中两项，需要额外的近似条件。

**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Estimate convective acceleration by squared characteristic speed divided by variation length. Integrating over event duration gives its velocity-change scale.

用特征速度平方除以变化长度估计对流加速度。再乘以事件持续时间，得到其速度变化尺度。



$$
\begin{aligned}\left|\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt\right|
       &\sim U^2\tau/L,\qquad (U^2\tau/L)/U=U\tau/L,\end{aligned}
$$



Estimate the viscous Laplacian using inverse squared variation length. Compare the resulting viscous impulse with characteristic speed.

用变化长度平方的倒数估计黏性拉普拉斯项。将所得黏性冲量与特征速度比较。



$$
\begin{aligned}\left|\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt\right|
       &\sim\nu U\tau/L^2,\qquad(\nu U\tau/L^2)/U=\nu\tau/L^2,\end{aligned}
$$



Subtract the divergence-free velocities at the two fixed event endpoints. Their velocity increment remains divergence-free.

将两个固定事件端点的无散速度相减。所得速度增量仍无散。



$$
\begin{aligned}\nabla\cdot\Delta\boldsymbol u&=\nabla\cdot\boldsymbol u(t_1)-\nabla\cdot\boldsymbol u(t_0)=0-0=0,\end{aligned}
$$



Take the divergence of the reduced pressure-impulse relation. With constant density, incompressibility gives Laplace's equation.

对约化压力冲量关系取散度。密度恒定时，不可压缩条件给出拉普拉斯方程。



$$
\begin{aligned}0&=-\nabla\cdot\nabla\Pi/\rho=-\nabla^2\Pi/\rho.\end{aligned}
$$



Require small convective impulse on the chosen velocity scale.

要求在所选速度尺度下，对流冲量足够小。



$$
\frac{U\tau}{L}\ll1
$$



Require small viscous impulse on that same scale.

要求在同一尺度下，黏性冲量足够小。



$$
\frac{\nu\tau}{L^2}\ll1
$$



Under the stated additional assumptions, retain the pressure contribution as the leading velocity change.

在已声明的附加假设下，保留压力贡献作为主导速度变化。



$$
\Delta\boldsymbol u\simeq-\frac{\nabla\Pi}{\rho}
$$



Apply incompressibility to this reduced relation to obtain the pressure-impulse boundary equation.

对该约化关系应用不可压缩条件，得到压力冲量边值方程。



$$
0=\nabla\cdot\Delta\boldsymbol u\simeq-\frac{\nabla^2\Pi}{\rho}\ \Longrightarrow\ \nabla^2\Pi=0
$$



**Symbols for Eq. (C1.6-E22).**

**式（C1.6-E22）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $U>0$ is a characteristic liquid speed (m s⁻¹)<br>$U>0$ 为特征液体速度（m s⁻¹） | $\tau$ is impulse duration (s)<br>$\tau$ 为冲量持续时间（s） |
| $L>0$ is liquid variation length (m)<br>$L>0$ 为液体变化长度（m） | $\nu$ is kinematic viscosity (m² s⁻¹)<br>$\nu$ 为运动黏度（m² s⁻¹） |
| $\Delta\boldsymbol u$ is velocity change (m s⁻¹)<br>$\Delta\boldsymbol u$ 为速度变化（m s⁻¹） | $\Pi$ is pressure impulse (Pa s)<br>$\Pi$ 为压力冲量（Pa s） |
| $\rho$ is density (kg m⁻³)<br>$\rho$ 为密度（kg m⁻³） | $t_0$ — fixed event start time (s)<br>$t_0$ — 固定事件起始时刻（s） |
| $t_1$ — fixed event end time (s)<br>$t_1$ — 固定事件终止时刻（s） | $t$ — time (s)<br>$t$ — 时间（s） |
| $\boldsymbol u$ — liquid velocity (m s⁻¹)<br>$\boldsymbol u$ — 液体速度（m s⁻¹） | $\nabla$ — spatial gradient operator (m⁻¹)<br>$\nabla$ — 空间梯度算子（m⁻¹） |
| $\nabla\cdot$ — spatial divergence operator (m⁻¹)<br>$\nabla\cdot$ — 空间散度算子（m⁻¹） | $\nabla^2$ — spatial Laplacian operator (m⁻²)<br>$\nabla^2$ — 空间拉普拉斯算子（m⁻²） |

**Conventions and conditions.** $\nabla\cdot$ denotes divergence and $\nabla^2$ Laplacian; $\ll$ means asymptotically small, and $\simeq$ marks the reduced approximation; The last Laplace equation belongs to that reduced model; $\sim$ denotes a scale estimate, rather than an equality or rigorous error bound.

**约定与条件。** $\nabla\cdot$ 表示散度，$\nabla^2$ 表示拉普拉斯算子；$\ll$ 表示渐近很小，$\simeq$ 表示约化近似；最后的拉普拉斯方程属于该约化模型；$\sim$ 表示尺度估计，并非等式或严格误差界。

![The velocity depends on a spatial impulse gradient constrained by boundary geometry.](../assets/figures/c1-e22.svg)

The velocity depends on a spatial impulse gradient constrained by boundary geometry.

速度取决于受边界几何约束的空间压力冲量梯度。

**Check and interpretation.** If the actual increment is much smaller than the chosen speed, these ratios need not bound its relative error. A fixed wall gives zero normal impulse derivative when normal velocity is unchanged. Driven and outlet boundaries supply their impulse values.

**检验与解释。** 若实际增量远小于所选速度，这些比值不能约束增量的相对误差。固定壁面法向速度不变时，法向冲量导数为零。受驱边界与出口分别给出各自冲量值。

A fixed impermeable wall requires zero normal velocity change. Its normal impulse derivative therefore vanishes. A driven cavity prescribes impulse or pressure history. A communicating outlet supplies its pressure reference. A spatially uniform impulse addition has zero gradient and changes no velocity. Pulse duration and boundary geometry can change the response at fixed peak pressure.

固定不透壁要求法向速度变化为零，因而法向冲量导数为零。受驱空腔给定冲量或压力历程，连通出口给定压力参考值。空间均匀增加冲量的梯度为零，不改变速度。峰值压力固定时，脉冲时长与边界几何仍可改变响应。

### Step 1.6.4 — Show how a boundary selects the liquid-motion direction

### 步骤 1.6.4——说明边界如何选择液体运动方向

**Purpose in this chapter.** Solve the reduced model from Eq. (C1.6-E22) for a straight column. Inlet and outlet impulses select a gradient and therefore an axial velocity increment.

**本章作用。** 对直液柱求解式（C1.6-E22）的约化模型。入口与出口冲量确定梯度，进而确定轴向速度增量。

**Solve a straight-column benchmark.** Start with a stationary uniform column along the positive axis. Area is constant and side walls are fixed. Prescribe positive inlet impulse and zero outlet impulse. Integrate the one-dimensional Laplace equation twice. Apply both endpoint values to obtain its gradient.

**求解直液柱基准。** 初始均匀液柱沿正轴静止，面积恒定，侧壁固定。入口冲量给定为正，出口冲量为零。将一维拉普拉斯方程积分两次，再用两个端点值确定梯度。

**Derivation.**

**推导。**

(C1.6-E23) · Exact straight-column solution of the reduced model / (C1.6-E23) · 简化模型中直液柱的精确解

#### 5. Apply C1.6-E23 to a straight liquid column

#### 将 C1.6-E23 应用于直液柱

Let $z\in[0,L]$, with a driven inlet at $z=0$ and an outlet at $z=L$. Define $\Pi(0)=\Pi_0$ and $\Pi(L)=0$. The one-dimensional Laplace equation in the short-event reduced model is

令 $z\in[0,L]$，驱动端位于 $z=0$，出口位于 $z=L$。设 $\Pi(0)=\Pi_0$，$\Pi(L)=0$。在短时事件的简化模型中，一维拉普拉斯方程为：



$$
\frac{d^2\Pi}{dz^2}=0\quad\Longrightarrow\quad\Pi(z)=\Pi_0\left(1-\frac zL\right).
$$



Differentiating **in space** after the **time integration** gives

**先对时间积分，再对空间求导**，得到：



$$
\boxed{\Delta u_z=-\frac1\rho\frac{d\Pi}{dz}=\frac{\Pi_0}{\rho L}}.
$$



#### 5. Simple one-dimensional illustration

#### 简单的一维示例

If $z$ runs from the driven end $0$ to an outlet $L$, and the pressure excess has the spatial form $p(z,t)-p_{\mathrm{ref}}(t)=f(t)(1-z/L)$, then

如果 $z$ 从受驱端 $0$ 指向出口 $L$，并且超压具有如下空间形式 $p(z,t)-p_{\mathrm{ref}}(t)=f(t)(1-z/L)$，那么：



$$
\Pi(z)=\left(1-\frac zL\right)\int_{t_0}^{t_1}f(t)\,dt,
\qquad
\frac{d\Pi}{dz}=-\frac1L\int_{t_0}^{t_1}f(t)\,dt.
$$



When the short-event approximation applies, the resulting axial velocity increment is

当短时事件近似成立时，得到的轴向速度增量为：



$$
\boxed{\Delta u_z\simeq-\frac1\rho\frac{d\Pi}{dz}
=\frac1{\rho L}\int_{t_0}^{t_1}f(t)\,dt}.
$$



This makes the operations distinct: **integrate pressure over time to obtain $\Pi$; differentiate $\Pi$ in space to obtain the leading-order velocity change.**

这使两个操作的作用清晰区分：**先对压力进行时间积分得到 $\Pi$，再对 $\Pi$ 作空间求导得到一阶速度变化。**

**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Integrate the one-dimensional Laplace equation once. Its pressure-impulse gradient is constant.

对一维拉普拉斯方程积分一次。压力冲量梯度为常数。



$$
\begin{aligned}d^2\Pi/dz^2=0&\Rightarrow d\Pi/dz=A_1,\end{aligned}
$$



Integrate that constant gradient from the inlet to an arbitrary column position.

从入口至任意液柱位置积分该常梯度。



$$
\begin{aligned}\Pi(z)-\Pi(0)&=\int_0^z A_1\,ds=A_1z,\end{aligned}
$$



Apply the prescribed inlet pressure impulse to determine the additive constant.

应用给定入口压力冲量，确定加法积分常数。



$$
\begin{aligned}\Pi(0)=\Pi_0&\Rightarrow A_0=\Pi_0,\end{aligned}
$$



Apply zero outlet impulse. This determines the gradient and its negative sign.

应用出口冲量为零的条件。由此确定梯度及其负号。



$$
\begin{aligned}0=\Pi(L)&=A_1L+\Pi_0\Rightarrow A_1=-\Pi_0/L,\end{aligned}
$$



Insert the gradient into the reduced momentum relation. The resulting axial velocity increment is positive toward the outlet.

将该梯度代入约化动量关系。所得轴向速度增量为正，指向出口。



$$
\begin{aligned}\Delta u_z&=-(-\Pi_0/L)/\rho=\Pi_0/(\rho L).\end{aligned}
$$



The first integration makes pressure impulse linear in column position.

第一次积分使压力冲量成为液柱位置的线性函数。



$$
\begin{aligned}\frac{d^2\Pi}{dz^2}&=0\quad\Longrightarrow\quad\Pi=A_1z+A_0,\end{aligned}
$$



The two endpoint values determine its two integration constants.

两个端点值确定两个积分常数。



$$
\begin{aligned}\Pi(0)&=\Pi_0,\quad\Pi(L)=0\quad\Longrightarrow\quad A_0=\Pi_0,\quad A_1=-\frac{\Pi_0}{L},\end{aligned}
$$



Insert the resulting gradient into the axial velocity increment.

将所得梯度代入轴向速度增量。



$$
\begin{aligned}\Pi(z)&=\Pi_0\left(1-\frac zL\right),\qquad \Delta u_z=-\frac1\rho\frac{d\Pi}{dz}=\frac{\Pi_0}{\rho L}.\end{aligned}
$$



**Symbols for Eq. (C1.6-E23).**

**式（C1.6-E23）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $z\in[0,L]$ is axial position (m)<br>$z\in[0,L]$ 为轴向位置（m） | $L>0$ column length (m)<br>$L>0$ 为液柱长度（m） |
| $\Pi(z)$ — Local column pressure impulse (Pa s)<br>$\Pi(z)$ — 液柱局部压力冲量（Pa s） | $\Pi_0>0$ — Driven-end pressure impulse (Pa s)<br>$\Pi_0>0$ — 驱动端压力冲量（Pa s） |
| $A_0$ is an integration constant (Pa s)<br>$A_0$ 为积分常数（Pa s） | $A_1$ a gradient constant (Pa s m⁻¹)<br>$A_1$ 为梯度常数（Pa s m⁻¹） |
| $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） | $\Delta u_z$ is positive axial speed change (m s⁻¹)<br>$\Delta u_z$ 为正轴向速度变化（m s⁻¹） |
| $s$ — dummy axial integration coordinate (m)<br>$s$ — 轴向积分哑坐标（m） | $f(t)$ — prescribed pressure-excess waveform (Pa)<br>$f(t)$ — 给定超压波形（Pa） |
| $t_0$ — event start time (s)<br>$t_0$ — 事件开始时间（s） | $t_1$ — event end time (s)<br>$t_1$ — 事件结束时间（s） |

**Conventions and conditions.** $d/dz$ is an axial derivative; Subscript $z$ labels the component and 0 the driven endpoint; The uniform-speed column is an inviscid core benchmark; no-slip wall layers are omitted.

**约定与条件。** $d/dz$ 为轴向导数；下标 $z$ 表示分量，0 表示受驱动端点；匀速液柱是无黏核心流基准；省略无滑移壁面层。

![A linear spatial impulse drop accelerates liquid toward the outlet.](../assets/figures/c1-e23.svg)

A linear spatial impulse drop accelerates liquid toward the outlet.

线性的空间冲量下降使液体向出口加速。

**Check and interpretation.** At inlet and outlet the solution reproduces both prescribed values. Impulse divided by density and length has units m s⁻¹. Equal pressure peaks with different durations produce different speed increments.

**检验与解释。** 解在入口和出口恢复两个给定值。冲量除以密度及长度的单位为 m s⁻¹。相同压力峰值、不同持续时间会产生不同速度增量。

Prescribe 0.60 MPa for 0.50 μs across a 100 μm column. Use the earlier density, viscosity 0.001 Pa s, and sound speed 1500 m s⁻¹. The velocity change is 3.0 m s⁻¹. Crossing time is shorter than the pulse. Uniform pressure and final jet speed remain unestablished. The solved column has an end-to-end pressure gradient.

在 100 μm 液柱两端施加 0.60 MPa 压差，持续 0.50 μs。采用前述密度、黏度 0.001 Pa s 和声速 1500 m s⁻¹。速度变化为 3.0 m s⁻¹。传播时间短于脉冲时长。均匀压力及最终射流速率尚未确立。已解液柱具有端到端压力梯度。

### Step 1.6.5 — Check the scale and assumptions of the column result

### 步骤 1.6.5——检验液柱结果的尺度与假设

**Purpose in this chapter.** Apply Eq. (C1.6-E23) to a declared pressure pulse. Calculate velocity change and compare acoustic, convective, and viscous scales before interpreting that result.

**本章作用。** 将式（C1.6-E23）用于给定压力脉冲。计算速度变化，并比较声学、对流与黏性尺度，再解释该结果。

**Derivation.**

**推导。**

(C1.6-E24) · Declared impulse calculation and applicability diagnostics / (C1.6-E24) · 采用给定参数的冲量计算与适用性诊断

For the course's illustrative pressure difference $\Delta p=0.60\,\mathrm{MPa}$ lasting $\tau=0.50\,\mu\mathrm s$, $\Pi_0=\Delta p\tau=0.30\,\mathrm{Pa\,s}$. With $\rho=1000\,\mathrm{kg/m^3}$ and $L=100\,\mu\mathrm m$, the velocity increment is $\Delta u_z=3.0\,\mathrm{m/s}$.

课程示例中，压差 $\Delta p=0.60\,\mathrm{MPa}$，持续时间 $\tau=0.50\,\mu\mathrm s$，因此 $\Pi_0=\Delta p\tau=0.30\,\mathrm{Pa\,s}$。取 $\rho=1000\,\mathrm{kg/m^3}$、$L=100\,\mu\mathrm m$，可得速度增量 $\Delta u_z=3.0\,\mathrm{m/s}$。

This example distinguishes the two operations: the integral $\int dt$ produces $\Pi(z)$, while the spatial derivative $d\Pi/dz$ determines the direction and strength of acceleration. It is a straight-column benchmark, not a prediction of the ultimate cavitation jet velocity.

这个例子明确区分了两个操作：$\int dt$ 的时间积分给出 $\Pi(z)$，空间导数 $d\Pi/dz$ 则决定加速方向与强度。它只是直液柱基准模型，并不直接预测空化射流的最终速度。

#### 6. Validity and agreed revision

#### 适用范围与待修改事项

This reduced pressure-impulse model assumes small integrated convection and viscosity relative to the pressure forcing, sufficiently small interface displacement for fixed-geometry approximations, and a compatible incompressible pressure field. It does not automatically describe fast compressible shocks, strongly moving interfaces, or an actual jet without a spatially resolved geometry and boundary conditions. In the course example the acoustic crossing time $L/c$ is about 0.0667 μs, shorter than the 0.50 μs pulse; “short-event” here concerns the neglected inertial-advection and viscous effects, not a claim that the pulse is shorter than the acoustic time.

这一简化压力冲量模型要求积分后的对流和黏性效应相对于压力驱动较小、界面位移足够小以允许固定几何近似，并满足相应的不可压缩压力场假设。它不能自动描述高速可压缩冲击波、强烈运动的界面，或缺少空间几何与边界条件的真实射流。在课程例子中，声传播时间 $L/c$ 约为 0.0667 μs，小于 0.50 μs 的脉冲时长；这里“短时事件”指的是对流和黏性积分效应可以忽略，而不是声传播时间比脉冲更长。

**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Convert the teaching pressure, pulse duration, and column length to SI units.

将教学压力、脉冲持续时间及液柱长度换算为 SI 单位。



$$
\begin{aligned}\Delta p&=6.0\times10^5\ \mathrm{Pa},\quad\tau=5.0\times10^{-7}\ \mathrm s,
      \quad L=10^{-4}\ \mathrm m,\end{aligned}
$$



Integrate the constant pressure pulse by multiplying its amplitude and duration.

将恒压脉冲的幅值与持续时间相乘，得到其时间积分。



$$
\begin{aligned}\Pi_0&=(6.0\times10^5)(5.0\times10^{-7})=0.30\ \mathrm{Pa\,s},\end{aligned}
$$



Calculate density times column length, then divide pressure impulse by this factor to obtain velocity change.

计算密度与液柱长度的乘积，再用压力冲量除以该因子，得到速度变化。



$$
\begin{aligned}\rho L&=1000(10^{-4})=0.1\ \mathrm{kg\,m^{-2}},\quad U=0.30/0.1=3.0\ \mathrm{m\,s^{-1}},\end{aligned}
$$



Evaluate displacement relative to variation length using characteristic speed and event duration.

利用特征速度与事件持续时间，计算位移相对于变化长度的比例。



$$
\begin{aligned}U\tau/L&=3(5\times10^{-7})/10^{-4}=0.015,\end{aligned}
$$



Evaluate the viscous impulse ratio using kinematic viscosity and squared variation length.

利用运动黏度与变化长度平方，计算黏性冲量比值。



$$
\begin{aligned}\nu\tau/L^2&=(10^{-6})(5\times10^{-7})/10^{-8}=5\times10^{-5},\end{aligned}
$$



Calculate one-way acoustic travel time and compare it with the pressure-pulse duration.

计算单程声传播时间，并将其与压力脉冲持续时间比较。



$$
\begin{aligned}t_a&=10^{-4}/1500=6.66667\times10^{-8}\ \mathrm s,\quad \tau/t_a=7.5.\end{aligned}
$$



Collect the pressure-pulse time integral.

汇总压力脉冲的时间积分。



$$
\begin{aligned}\Pi_0&=\Delta p\tau=(0.60\times10^6)(0.50\times10^{-6})\ \mathrm{Pa\,s}=0.30\ \mathrm{Pa\,s},\end{aligned}
$$



Record the predicted column velocity change and acoustic travel time.

写出所预测的液柱速度变化与声传播时间。



$$
\begin{aligned}U&=\frac{\Pi_0}{\rho L}=3.0\ \mathrm{m\,s^{-1}},\qquad t_a=\frac Lc=0.066667\ \mu\mathrm s,\end{aligned}
$$



Compare the convective, viscous, and acoustic ratios before using the reduced model.

使用约化模型之前，比较对流、黏性与声学比值。



$$
\begin{aligned}\frac{U\tau}{L}&=0.015,\qquad\frac{\nu\tau}{L^2}=5.0\times10^{-5},\qquad\frac{\tau}{t_a}=7.5.\end{aligned}
$$



**Symbols for Eq. (C1.6-E24).**

**式（C1.6-E24）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\Pi_0$ is driven-end impulse (Pa s)<br>$\Pi_0$ 为受驱动端冲量（Pa s） | $\Delta p$ is constant applied column pressure difference (Pa)<br>$\Delta p$ 为施加的常数液柱压差（Pa） |
| $\tau$ is pulse duration (s)<br>$\tau$ 为脉冲持续时间（s） | $U$ is column speed increment (m s⁻¹)<br>$U$ 为液柱速度增量（m s⁻¹） |
| $\rho=1000$ kg m⁻³ is density<br>$\rho=1000$ kg m⁻³ 为密度 | $L=100\times10^{-6}$ m is length<br>$L=100\times10^{-6}$ m 为长度 |
| $c=1500$ m s⁻¹ is sound speed<br>$c=1500$ m s⁻¹ 为声速 | $t_a$ is acoustic crossing time (s)<br>$t_a$ 为声传播时间（s） |
| $\nu=\mu/\rho=10^{-6}$ m² s⁻¹ with $\mu=0.001$ Pa s<br>$\nu=\mu/\rho=10^{-6}$ m² s⁻¹，且 $\mu=0.001$ Pa s | $\mu$ — Carrier dynamic viscosity (Pa s)<br>$\mu$ — 载液动力黏度（Pa s） |

**Conventions and conditions.** The three ratios are dimensionless; μs means microseconds.

**约定与条件。** 三个比值均无量纲；μs 表示微秒。

![Pressure impulse and acoustic time have distinct definitions, dimensions and roles.](../assets/figures/c1-e24.svg)

Pressure impulse and acoustic time have distinct definitions, dimensions and roles.

压力冲量与声传播时间具有不同的定义、量纲与作用。

**Check and interpretation.** The rectangular discontinuity has zero ideal rise time, so its fronts require acoustic treatment. The integrated column result is a reduced impulse benchmark. A real pulse needs a measured or prescribed finite rise time and the separate communication test below.

**检验与解释。** 理想矩形跃变的上升时间为零，因此波前需要声学处理。液柱积分结果属于约化冲量基准。实际脉冲需要实测或给定的有限上升时间，并进行下文独立通信检验。

Directional motion requires asymmetry. A sphere in uniform infinite liquid has no preferred direction. Outlets, menisci, walls, neighbors or uneven heating break that symmetry. Stand-off is center-to-boundary distance divided by maximum radius. Equal stand-off still permits different curvature and material response. Collapse near a rigid plane commonly directs a jet toward it. Deformable boundaries can change or split that response. [[R3]](../reference/sources.html#r3) [[R12]](../reference/sources.html#r12)

定向运动需要非对称性。均匀无限液体中的球形空腔没有优选方向。出口、弯月面、壁面、邻近空腔或不均匀加热可破坏对称性。离壁参数为中心至边界距离除以最大半径。相同离壁参数仍可对应不同曲率和材料响应。刚性平面附近的塌缩射流通常朝向平面。可变形边界可改变或分裂该响应。 [[R3]](../reference/sources.html#r3) [[R12]](../reference/sources.html#r12)

### Step 1.6.6 — Explain why a spherical cavity cannot choose a jet direction

### 步骤 1.6.6——说明球形空腔为何不能选择射流方向

**Purpose in this chapter.** Contrast spherical symmetry with the directed column in Eq. (C1.6-E23). This identifies the geometric information missing from a radius-only model and motivates Section 1.7.

**本章作用。** 对比球形对称性与式（C1.6-E23）的定向液柱。由此明确纯半径模型缺失的几何信息，并引出第1.7节。

**Derivation.** Stand-off compares a center-to-boundary distance with maximum bubble radius. It is a geometric descriptor. To prove directional cancellation for the unbounded sphere, write each radial unit-vector component and integrate over all solid angles. The azimuthal sine and cosine integrate to zero; the axial component cancels between hemispheres.

**推导。** 离壁比将中心到边界距离与最大气泡半径比较，属于几何描述。为证明无界球形情况下方向相互抵消，写出径向单位矢量各分量并对全部立体角积分。方位正弦和余弦积分为零，轴向分量在两半球之间抵消。

(C1.6-E25) · Geometry definition and exact symmetry identity / (C1.6-E25) · 几何定义与精确的对称性恒等式

Write the radial unit vector in Cartesian components and the solid-angle integration measure.

用笛卡尔分量表示径向单位矢量，并写出立体角积分测度。



$$
\begin{aligned}\boldsymbol e_r&=(\sin\theta\cos\psi,\sin\theta\sin\psi,\cos\theta),\quad
      d\Omega=\sin\theta\,d\theta\,d\psi,\end{aligned}
$$



Integrate the azimuthal cosine factor. This cancels the first Cartesian component over a complete revolution.

积分方位角余弦因子。第一笛卡尔分量在完整一周内相互抵消。



$$
\begin{aligned}\int_0^{2\pi}\cos\psi\,d\psi&=[\sin\psi]_0^{2\pi}=0,\end{aligned}
$$



Integrate the azimuthal sine factor. This cancels the second Cartesian component.

积分方位角正弦因子。第二笛卡尔分量因此抵消。



$$
\begin{aligned}\int_0^{2\pi}\sin\psi\,d\psi&=[-\cos\psi]_0^{2\pi}=0,\end{aligned}
$$



Integrate the polar factor for the third component. Its two endpoint contributions are equal.

积分第三分量的极角因子。其两个端点的贡献相等。



$$
\begin{aligned}\int_0^\pi\cos\theta\sin\theta\,d\theta&=[\tfrac12\sin^2\theta]_0^\pi=0,\end{aligned}
$$



Collect the three zero components. An exactly spherical configuration has no preferred vector direction.

合并三个零分量。严格球形构型没有优先的矢量方向。



$$
\begin{aligned}\int_{S^2}\boldsymbol e_r\,d\Omega&=(0,0,0).\end{aligned}
$$



Define stand-off using center-to-boundary distance divided by maximum radius.

用中心至边界距离除以最大半径，定义相对壁距。



$$
\gamma=\frac h{R_{\max}}
$$



The zero angular vector integral records the absence of a preferred direction under exact spherical symmetry.

角向矢量积分为零，表明严格球对称时没有优先方向。



$$
\int_{S^2}\boldsymbol e_r\,d\Omega=\boldsymbol0
$$



**Symbols for Eq. (C1.6-E25).**

**式（C1.6-E25）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\gamma$ is dimensionless stand-off<br>$\gamma$ 为无量纲离壁比 | $h$ is bubble-center-to-boundary distance (m)<br>$h$ 为气泡中心到边界的距离（m） |
| $R_{\max}$ is maximum radius (m)<br>$R_{\max}$ 为最大半径（m） | $S^2$ denotes all directions on the unit sphere (—)<br>$S^2$ 表示单位球面上的全部方向（—） |
| $\boldsymbol e_r$ is the outward radial unit vector (dimensionless)<br>$\boldsymbol e_r$ 为向外径向单位矢量（无量纲） | $d\Omega$ is the dimensionless solid-angle measure<br>$d\Omega$ 为无量纲立体角测度 |
| $\boldsymbol0$ is the zero vector (dimensionless)<br>$\boldsymbol0$ 为零矢量（无量纲） | $\theta$ — polar angle, $0\le\theta\le\pi$ (1)<br>$\theta$ — 极角，$0\le\theta\le\pi$（1） |
| $\psi$ — azimuthal angle, $0\le\psi\le2\pi$ (1)<br>$\psi$ — 方位角，$0\le\psi\le2\pi$（1） |  |

**Conventions and conditions.** The angular identity expresses directional cancellation under perfect spherical symmetry; it is not a boundary-jet prediction; Angles are dimensionless radians; tuple entries are Cartesian vector components.

**约定与条件。** 角积分恒等式表示完全球对称下方向相互抵消，并非边界射流预测；角度以无量纲弧度计；有序三元组为笛卡尔矢量分量。

![Stand-off locates a boundary; perfect spherical symmetry selects no outgoing direction.](../assets/figures/c1-e25.svg)

Stand-off locates a boundary; perfect spherical symmetry selects no outgoing direction.

离壁比定位边界；完全球对称不能选出向外喷射方向。

**Check and interpretation.** The cancellation concerns perfect symmetry. Actual boundaries change the spatial pressure and velocity problem. Stand-off alone cannot determine the response of different boundary materials or curvatures.

**检验与解释。** 抵消结论针对完全球对称。实际边界改变空间压力和速度问题。离壁比本身不能确定不同边界材料或曲率下的响应。

## 1.7 Moving-interface model

## 1.7 运动界面模型

### Step 1.7.1 — Replace the radius model with spatial liquid equations

### 步骤 1.7.1——用空间液体方程替代纯半径模型

**Purpose in this chapter.** Retain the mass and momentum laws across the actual liquid domain. These equations provide the spatial dynamics needed when boundaries and interface shape determine the jet.

**本章作用。** 在实际液体区域保留质量与动量守恒规律。当边界及界面形状决定射流时，这些方程提供所需的空间动力学。

**Specify the spatial jet problem.** Prescribe initial interface shape and carrier velocity. Define solid boundaries, outlet, contact-line behavior and pressure closure. The following equations conserve mass and momentum for constant-property incompressible Newtonian liquid. Gravity is omitted. Solve them with the interface and boundary conditions below. A fitted radius history leaves these spatial conditions unresolved.

**规定空间射流问题。** 给定初始界面形状和载液速度，定义固体边界、出口、接触线规律及压力闭合。以下方程描述常物性不可压缩牛顿液体的质量与动量守恒，忽略重力。须结合下述界面和边界条件求解。拟合半径历程仍未确定这些空间条件。

**Derivation.**

**推导。**

(C1.7-E26) · Bulk conservation and Newtonian constitutive assumption / (C1.7-E26) · 体相守恒律与牛顿流体本构假设

#### 1. Start from the Navier–Stokes equation

#### 从 Navier–Stokes 方程出发

For an incompressible Newtonian liquid with constant density $\rho$, dynamic viscosity $\mu$, and no body forces, the momentum equation is

对于密度 $\rho$、动力黏度 $\mu$ 均为常数、且忽略体积力的不可压缩牛顿流体，动量方程为：



$$
\boxed{\rho\left[\frac{\partial\boldsymbol u}{\partial t}+(\boldsymbol u\cdot\nabla)\boldsymbol u\right]=-\nabla p+\mu\nabla^2\boldsymbol u}\tag{1}
$$



Here, $\boldsymbol u(\boldsymbol x,t)$ is the velocity field, $p(\boldsymbol x,t)$ is pressure, $\nabla p$ is the pressure gradient, and $\nabla^2\boldsymbol u$ is the vector Laplacian of velocity. The notation $(\boldsymbol u\cdot\nabla)\boldsymbol u$ denotes convective acceleration.

其中，$\boldsymbol u(\boldsymbol x,t)$ 是速度场，$p(\boldsymbol x,t)$ 是压力场，$\nabla p$ 是压力梯度，$\nabla^2\boldsymbol u$ 是速度的矢量拉普拉斯算子。$(\boldsymbol u\cdot\nabla)\boldsymbol u$ 表示对流加速度。

Divide both sides by $\rho$, and define the kinematic viscosity $\nu=\mu/\rho$:

两侧除以 $\rho$，并定义运动黏度 $\nu=\mu/\rho$：



$$
\boxed{\frac{\partial\boldsymbol u}{\partial t}=-\frac{\nabla p}{\rho}-(\boldsymbol u\cdot\nabla)\boldsymbol u+\nu\nabla^2\boldsymbol u}\tag{2}
$$



This equation states that the local velocity changes because of pressure gradients, convective transport, and viscous effects.

这个方程表示：局部速度的变化由压力梯度、对流输运以及黏性作用共同决定。

**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Begin with mass conservation before imposing constant density. Constant density reduces it to zero velocity divergence.

先写质量守恒，再施加常密度条件。常密度使其约化为速度散度为零。



$$
\begin{aligned}\partial_t\rho+\nabla\cdot(\rho\boldsymbol u)&=0
       \quad\xrightarrow{\rho\ \mathrm{constant}}\quad\nabla\cdot\boldsymbol u=0,\end{aligned}
$$



Adopt the Newtonian stress law with constant viscosity. It separates pressure and symmetric velocity-gradient stresses.

采用常黏度牛顿应力定律。该定律区分压力应力与对称速度梯度应力。



$$
\begin{aligned}\boldsymbol T&=-p\boldsymbol I+\mu[\nabla\boldsymbol u+(\nabla\boldsymbol u)^{\mathsf T}],\end{aligned}
$$



Apply momentum conservation without body force. Stress divergence produces material acceleration.

在无体积力时应用动量守恒。应力散度产生物质加速度。



$$
\begin{aligned}\rho D\boldsymbol u/Dt&=\nabla\cdot\boldsymbol T,\end{aligned}
$$



Take the divergence of Newtonian stress. Constant viscosity and incompressibility remove the gradient-of-divergence contribution.

对牛顿应力取散度。常黏度与不可压缩条件消去散度梯度项。



$$
\begin{aligned}\nabla\cdot\boldsymbol T&=-\nabla p+\mu[\nabla^2\boldsymbol u+\nabla(\nabla\cdot\boldsymbol u)]
      =-\nabla p+\mu\nabla^2\boldsymbol u,\end{aligned}
$$



Expand material acceleration into the local time derivative and convective acceleration.

将物质加速度展开为局部时间导数与对流加速度。



$$
\begin{aligned}D\boldsymbol u/Dt&=\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u.\end{aligned}
$$



State the constant-density mass-conservation condition.

写出常密度质量守恒条件。



$$
\nabla\cdot\boldsymbol u=0
$$



Combine material acceleration and Newtonian stress divergence to obtain the spatial liquid momentum equation.

结合物质加速度与牛顿应力散度，得到空间液体动量方程。



$$
\rho\left(\frac{\partial\boldsymbol u}{\partial t}+(\boldsymbol u\cdot\nabla)\boldsymbol u\right)=-\nabla p+\mu\nabla^2\boldsymbol u
$$



**Symbols for Eq. (C1.7-E26).**

**式（C1.7-E26）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\boldsymbol u(\boldsymbol x,t)$ is liquid velocity (m s⁻¹)<br>$\boldsymbol u(\boldsymbol x,t)$ 为液体速度（m s⁻¹） | $\boldsymbol x$ is spatial position (m)<br>$\boldsymbol x$ 为空间位置（m） |
| $t$ is time (s)<br>$t$ 为时间（s） | $\rho$ is constant carrier density (kg m⁻³)<br>$\rho$ 为常数载液密度（kg m⁻³） |
| $p$ is liquid pressure (Pa)<br>$p$ 为液体压力（Pa） | $\mu$ is constant viscosity (Pa s)<br>$\mu$ 为常数黏度（Pa s） |
| $\boldsymbol T$ — Cauchy stress tensor (Pa)<br>$\boldsymbol T$ — 柯西应力张量（Pa） | $\boldsymbol I$ — identity tensor (1)<br>$\boldsymbol I$ — 单位张量（1） |
| $D/Dt$ — material time derivative (s⁻¹)<br>$D/Dt$ — 物质时间导数（s⁻¹） | $\partial_t$ — time derivative at fixed position (s⁻¹)<br>$\partial_t$ — 固定位置的时间导数（s⁻¹） |
| $\nabla$ — spatial gradient operator (m⁻¹)<br>$\nabla$ — 空间梯度算子（m⁻¹） | $\nabla\cdot$ — spatial divergence operator (m⁻¹)<br>$\nabla\cdot$ — 空间散度算子（m⁻¹） |
| $\nabla^2$ — spatial Laplacian operator (m⁻²)<br>$\nabla^2$ — 空间拉普拉斯算子（m⁻²） |  |

**Conventions and conditions.** $\nabla\cdot,\nabla,\nabla^2$ denote divergence, gradient and vector Laplacian; $\partial_t$ is the fixed-position derivative; The dot in convection is vector contraction; The momentum equation has force-per-volume units (N m⁻³); Superscript $\mathsf T$ denotes transpose; body forces are omitted; the density derivative is displayed before imposing constant density.

**约定与条件。** $\nabla\cdot,\nabla,\nabla^2$ 分别为散度、梯度与矢量拉普拉斯；$\partial_t$ 为固定位置导数；对流中的圆点为矢量缩并；动量方程各项单位为单位体积力（N m⁻³）；上标 $\mathsf T$ 表示转置；忽略体力；密度导数写在施加常密度条件之前。

![Bulk momentum and volume conservation supply the spatial field needed for jet formation.](../assets/figures/c1-e26.svg)

Bulk momentum and volume conservation supply the spatial field needed for jet formation.

体内动量与体积守恒给出射流形成所需的空间场。

**Check and interpretation.** Stress divergence and inertia both have units N m⁻³. Supply a divergence-free initial velocity, compatible interface shape, wall velocities, outlet data and contact-line law. A radius history cannot replace these fields.

**检验与解释。** 应力散度和惯性项单位均为 N m⁻³。需要给定无散初始速度、相容初始界面、壁面速度、出口数据及接触线规律。半径历程不能代替这些空间场。

### Step 1.7.2 — Close the spatial model at its moving interface

### 步骤 1.7.2——在运动界面闭合空间模型

**Purpose in this chapter.** Add interface motion and traction conditions to Eq. (C1.7-E26). Their orientation and stress signs must recover the spherical jump in Eq. (C1.3-E06).

**本章作用。** 为式（C1.7-E26）补充界面运动与牵引条件。其方向与应力符号须恢复式（C1.3-E06）的球形跃变关系。

**Set interface orientation and stress.** The normal points from liquid into gas. An inner spherical cavity therefore has negative curvature. An outer liquid droplet has positive curvature. This reproduces Eq. (C1.3-E06). A clean interface with negligible gas viscosity has zero tangential viscous traction. At zero liquid viscosity, that condition adds no strain-rate constraint. Without phase transfer, interface and liquid normal velocities match.

**规定界面方向与应力。** 法向由液体指向气体，故内球形空腔曲率为负，外液滴曲率为正。这一约定恢复式（C1.3-E06）。清洁界面且气相黏性可忽略时，切向黏性牵引为零。液体黏度为零时，该条件不增加应变率约束。没有相变时，界面与液体法向速度相等。

**Derivation.**

**推导。**

(C1.7-E27) · Kinematic condition and clean-interface traction / (C1.7-E27) · 运动学条件与洁净界面牵引

#### 3. Kinematic condition: advance interface position

#### 运动学条件：推进界面位置

With zero mass transfer across the interface, the physically required statement is equality of normal velocities,

如果界面没有相变质量通量，物理上必须满足法向速度相等：



$$
\left(\frac{d\boldsymbol X}{dt}-\boldsymbol u\right)\cdot\boldsymbol n=0.
$$



If we deliberately follow material interface markers, we can choose the stronger parametrization used in C1.7-E28:

如果选择追踪界面上的物质标记点，就可以采用 C1.7-E28 的较强参数化形式：



$$
\boxed{\frac{d\boldsymbol X}{dt}=\boldsymbol u(\boldsymbol X,t)=\nabla\phi(\boldsymbol X,t).}
$$



The normal component determines the physical interface shape; tangential marker motion depends on parametrization. This equation tells us **where** the interface moves, not how its velocity potential evolves.

法向分量决定实际界面形状；切向标记点运动依赖参数化方式。这一方程告诉我们界面**移动到哪里**，但没有告诉我们界面速度势如何演化。

**Additional worked steps.** The following steps supply details beyond the preserved handoff passage.

**补充的完整步骤。** 以下步骤补充所保留交接材料之外的细节。

Represent the interface by a smooth level set increasing into gas. Its gradient defines the normal, and its time change defines normal interface speed.

用向气体侧增大的光滑水平集表示界面。其梯度确定法向，其时间变化确定界面法向速度。



$$
\begin{aligned}F(\boldsymbol x,t)=0,\quad\boldsymbol n&=\nabla F/|\nabla F|,\quad
      V_n=-\partial_tF/|\nabla F|,\end{aligned}
$$



For an interface transported by liquid without phase slip, impose zero material change of the level set.

对于由液体输运且没有相变滑移的界面，令水平集的物质变化为零。



$$
\begin{aligned}\partial_tF+\boldsymbol u\cdot\nabla F=0&\Rightarrow V_n=\boldsymbol u\cdot\boldsymbol n,\end{aligned}
$$



Apply the clean-interface traction jump using the liquid-to-gas normal and signed curvature.

采用液体指向气体的法向与带符号曲率，应用清洁界面牵引跃变关系。



$$
\begin{aligned}(\boldsymbol T_g-\boldsymbol T_l)\boldsymbol n&=\sigma\kappa\boldsymbol n,\end{aligned}
$$



Insert gas pressure stress and liquid Newtonian stress into the traction jump.

将气体压力应力与液体牛顿应力代入牵引跃变关系。



$$
\begin{aligned}(\boldsymbol T_g-\boldsymbol T_l)\boldsymbol n
       &=[(p_l-p_b)\boldsymbol I-2\mu\boldsymbol D]\boldsymbol n,\end{aligned}
$$



Use unit normal magnitude and orthogonality of normal and tangent before taking projections.

在作投影之前，使用单位法向的模长条件及法向与切向的正交性。



$$
\begin{aligned}\boldsymbol n\cdot\boldsymbol n&=1,\qquad\boldsymbol s\cdot\boldsymbol n=0,\end{aligned}
$$



Project the traction jump onto the normal. This gives the normal pressure and viscous-stress balance.

将牵引跃变投影至法向。由此得到法向压力与黏性应力平衡。



$$
\begin{aligned}p_l-p_b-2\mu\boldsymbol n\cdot\boldsymbol D\boldsymbol n&=\sigma\kappa,\end{aligned}
$$



Project onto a tangent. Constant surface tension and negligible gas viscous stress give zero tangential liquid traction.

投影至切向。常表面张力及可忽略的气相黏性应力给出零液体切向牵引。



$$
\begin{aligned}-2\mu\boldsymbol s\cdot\boldsymbol D\boldsymbol n&=0.\end{aligned}
$$



Define symmetric strain rate and signed curvature using the adopted normal orientation.

根据所采用的法向方向，定义对称应变率与带符号曲率。



$$
\begin{aligned}\boldsymbol D&=\frac12\left(\nabla\boldsymbol u+(\nabla\boldsymbol u)^\mathsf T\right),\qquad \kappa=\nabla_s\cdot\boldsymbol n,\end{aligned}
$$



Collect interface kinematics and normal pressure balance.

汇总界面运动学与法向压力平衡。



$$
\begin{aligned}V_n&=\boldsymbol u\cdot\boldsymbol n,\qquad p_l=p_b+\sigma\kappa+2\mu\boldsymbol n\cdot\boldsymbol D\boldsymbol n,\end{aligned}
$$



Collect tangential traction and the inner-sphere curvature sign.

汇总切向牵引条件及内球面曲率符号。



$$
\begin{aligned}2\mu\boldsymbol s\cdot\boldsymbol D\boldsymbol n&=0,\qquad \kappa_{\mathrm{sphere}}=-\frac2R.\end{aligned}
$$



**Symbols for Eq. (C1.7-E27).**

**式（C1.7-E27）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\boldsymbol D$ is symmetric liquid strain-rate tensor (s⁻¹)<br>$\boldsymbol D$ 为液体对称应变率张量（s⁻¹） | $\boldsymbol u$ is velocity (m s⁻¹)<br>$\boldsymbol u$ 为速度（m s⁻¹） |
| $\boldsymbol n$ is the unit normal from liquid into gas (dimensionless)<br>$\boldsymbol n$ 为从液体指向气体的单位法向（无量纲） | $\kappa$ is signed curvature (m⁻¹)<br>$\kappa$ 为带符号曲率（m⁻¹） |
| $V_n$ is interface normal speed (m s⁻¹)<br>$V_n$ 为界面法向速度（m s⁻¹） | $p_l$ — Adjacent-liquid absolute pressure (Pa)<br>$p_l$ — 邻近液体绝对压力（Pa） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $\sigma$ is surface tension (N m⁻¹)<br>$\sigma$ 为表面张力（N m⁻¹） |
| $\mu$ is viscosity (Pa s)<br>$\mu$ 为黏度（Pa s） | $\boldsymbol s$ is any unit tangent (dimensionless)<br>$\boldsymbol s$ 为任意单位切向（无量纲） |
| $R$ is spherical cavity radius (m)<br>$R$ 为球形空腔半径（m） | $F$ — smooth dimensionless level set increasing into gas (1)<br>$F$ — 向气体侧增加的光滑无量纲水平集（1） |
| $\boldsymbol x$ — position (m)<br>$\boldsymbol x$ — 位置（m） | $t$ — time (s)<br>$t$ — 时间（s） |
| $\boldsymbol T_g$ — gas stress, $-p_b\boldsymbol I$ (Pa)<br>$\boldsymbol T_g$ — 气体应力，$-p_b\boldsymbol I$（Pa） | $\boldsymbol T_l$ — liquid stress, $-p_l\boldsymbol I+2\mu\boldsymbol D$ (Pa)<br>$\boldsymbol T_l$ — 液体应力，$-p_l\boldsymbol I+2\mu\boldsymbol D$（Pa） |
| $\boldsymbol I$ — identity tensor (1)<br>$\boldsymbol I$ — 单位张量（1） | $\nabla$ — spatial gradient operator (m⁻¹)<br>$\nabla$ — 空间梯度算子（m⁻¹） |
| $\nabla_s\cdot$ — surface divergence operator (m⁻¹)<br>$\nabla_s\cdot$ — 表面散度算子（m⁻¹） | $\partial_t$ — time derivative at fixed position (s⁻¹)<br>$\partial_t$ — 固定位置的时间导数（s⁻¹） |
| $\boldsymbol X$ — material interface marker position (m)<br>$\boldsymbol X$ — 界面物质标记点位置（m） | $\phi$ — velocity potential (m² s⁻¹)<br>$\phi$ — 速度势（m² s⁻¹） |

**Conventions and conditions.** $\nabla\boldsymbol u$ is its spatial gradient, with superscript $\mathsf T$ denoting transpose; $\nabla_s\cdot$ is surface divergence; Dots denote tensor/vector contractions; The level-set gradient is nonzero on the interface.

**约定与条件。** $\nabla\boldsymbol u$ 为其空间梯度，上标 $\mathsf T$ 表示转置；$\nabla_s\cdot$ 为表面散度；圆点表示张量或矢量缩并；水平集在界面上的梯度非零。

![Interface normals, signed curvature and material motion must use one consistent convention.](../assets/figures/c1-e27.svg)

Interface normals, signed curvature and material motion must use one consistent convention.

界面法向、带符号曲率与物质运动必须采用一致约定。

**Check and interpretation.** The interface condition matches normal velocity; tangential node motion is a parametrization choice. It imposes no solid-wall no-slip condition on an inviscid free surface. Phase transfer needs a mass-flux condition instead.

**检验与解释。** 界面条件匹配法向速度；节点切向运动属于参数化选择。无黏自由表面不能施加固壁无滑移条件。发生相变传质时，应采用质量通量条件。

Set zero liquid velocity at a stationary viscous wall. Couple liquid velocity and stress to a moving film. Supply external pressure and stress at the outlet or meniscus. Close the contact line with a pinned or moving-angle law. Chapter 4 supplies payload and release mechanics. Appreciable phase transfer replaces equal normal velocities with Chapter 2’s mass-flux balance.

静止黏性壁面采用零液体速度。运动薄膜须与液体速度和应力耦合。出口或弯月面给定外部压力与应力。接触线采用固定或动态接触角规律闭合。第四章给出载荷与释放力学。相变显著时，用第二章质量通量平衡代替法向速度相等条件。

### Step 1.7.3 — Construct a conditional pre-impact interface solver

### 步骤 1.7.3——构造有条件的撞击前界面求解模型

**Purpose in this chapter.** Reduce Eqs. (C1.7-E26) and (C1.7-E27) under the stated inviscid potential-flow assumptions. The resulting system evolves interface shape and can resolve directional pre-impact motion.

**本章作用。** 在已声明的无黏势流假设下约化式（C1.7-E26）与（C1.7-E27）。所得系统演化界面形状，可解析撞击前的定向运动。

**Derive the potential-flow reduction.** Assume inviscid, initially irrotational flow away from shocks and unresolved wall layers. The potential satisfies Laplace’s equation. Without phase slip, interface nodes follow liquid velocity. Convert the Eulerian Bernoulli derivative to the material derivative. Add velocity dotted with the potential gradient. This closes a spatial pre-impact model under the stated assumptions. Boundary-integral microjet models use this reduction. [[R4]](../reference/sources.html#r4)

**推导势流约化。** 假设流动无黏且初始无旋，并避开激波及未解析壁面层。速度势满足拉普拉斯方程。无相变滑移时，界面节点随液体速度运动。将欧拉伯努利导数转为物质导数，加入速度与速度势梯度的点积。由此在已声明假设下闭合撞击前空间模型。边界积分微射流模型采用此约化。 [[R4]](../reference/sources.html#r4)

**Derivation.**

**推导。**

(C1.7-E28) · Inviscid pre-impact moving-interface closure / (C1.7-E28) · 冲击前无黏运动界面的闭合关系

**Core answer (English).** C1.7-E28 is a *conditional potential-flow closure* for a moving gas–liquid interface, not a complete laser-to-PFC-jet model. The bulk Laplace equation supplies the velocity field; the kinematic condition updates interface geometry; the dynamic condition updates interface potential. The material-derivative expression is a rewrite, not another independent equation. All initial data, non-interface boundary conditions and the bubble-pressure history must still be given or modeled.

**核心回答（中文）。** C1.7-E28 是运动气液界面的**条件性势流闭合**，不是完整的激光—PFC—射流模型。流体内部的 Laplace 方程给出速度场；运动学条件更新界面几何；动力学条件更新界面速度势。物质导数形式只是改写，不是额外独立方程。仍然需要初值、其他边界条件以及已知或另行计算的腔内压力历程。

#### 1. Identify the unknowns

#### 确认未知量

In the spherical Rayleigh–Plesset model, the unknown shape is only the radius `R(t)`. In the nonspherical jet problem, let `Ω(t)` be the liquid domain, `Γ(t)` its moving gas–liquid interface and `X(α,t)` the position of an interface marker (the parameter `α` labels that marker). We seek `φ(x,t)` in the liquid and `Γ(t)` over time. The velocity is then `u=∇φ`. Pressure at the interface is obtained from stress balance. Bubble pressure `p_b(t)` is an additional required source input or thermodynamic unknown.

球对称 Rayleigh–Plesset 模型的几何未知量只有半径 `R(t)`。在非球对称射流问题中，令 `Ω(t)` 为液体区域，`Γ(t)` 为运动气液界面，`X(α,t)` 为界面上某个标记点的位置（`α` 为标记参数）。我们需要求解液体中的 `φ(x,t)` 及随时间演化的 `Γ(t)`，速度再由 `u=∇φ` 得到。界面压力来自应力平衡。腔内压力 `p_b(t)` 则是另外必须给定或通过热力学求解的量。

#### 2. Bulk equation

#### 流体内部方程

Assume the carrier is incompressible, inviscid and irrotational, away from shocks and boundary layers. Irrotationality permits `u=∇φ`. Incompressibility requires `∇·u=0`. Substitution yields

假设载液不可压缩、无黏且无旋，并且不考虑冲击波及边界层。无旋条件允许写成 `u=∇φ`，不可压缩条件要求 `∇·u=0`。代入后：



$$
\boxed{\boldsymbol u=\nabla\phi,\qquad \nabla^2\phi=\nabla\cdot\nabla\phi=0\quad\text{in }\Omega(t).}
$$



At any fixed time, Laplace's equation determines the potential only after the domain and appropriate boundary data are specified. It cannot advance the interface by itself.

在任一固定时刻，只有给定区域和适当的边界条件，Laplace 方程才能确定速度势。它本身不能推进界面。

#### 3. Kinematic condition: advance interface position

#### 运动学条件：推进界面位置

With zero mass transfer across the interface, the physically required statement is equality of normal velocities,

如果界面没有相变质量通量，物理上必须满足法向速度相等：



$$
\left(\frac{d\boldsymbol X}{dt}-\boldsymbol u\right)\cdot\boldsymbol n=0.
$$



If we deliberately follow material interface markers, we can choose the stronger parametrization used in C1.7-E28:

如果选择追踪界面上的物质标记点，就可以采用 C1.7-E28 的较强参数化形式：



$$
\boxed{\frac{d\boldsymbol X}{dt}=\boldsymbol u(\boldsymbol X,t)=\nabla\phi(\boldsymbol X,t).}
$$



The normal component determines the physical interface shape; tangential marker motion depends on parametrization. This equation tells us **where** the interface moves, not how its velocity potential evolves.

法向分量决定实际界面形状；切向标记点运动依赖参数化方式。这一方程告诉我们界面**移动到哪里**，但没有告诉我们界面速度势如何演化。

#### 4. Dynamic condition: derive it instead of assuming it

#### 动力学条件：从基本方程推导

Begin with the inviscid Euler momentum equation with constant density and no body forces:

从密度恒定、无体积力的无黏 Euler 动量方程出发：



$$
\frac{\partial\boldsymbol u}{\partial t}+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\frac{\nabla p}{\rho}.
$$



For `u=∇φ`, the flow is irrotational. Consequently

对于 `u=∇φ` 的无旋流动，有：



$$
\frac{\partial\boldsymbol u}{\partial t}=\nabla\!\left(\frac{\partial\phi}{\partial t}\right),\qquad
(\boldsymbol u\cdot\nabla)\boldsymbol u=\nabla\!\left(\frac12|\boldsymbol u|^2\right).
$$



Substitute and factor the gradient:

将其代入并提取梯度：



$$
\nabla\left(\frac{\partial\phi}{\partial t}+\frac12|\boldsymbol u|^2+\frac{p}{\rho}\right)=\boldsymbol 0.
$$



The quantity in parentheses is constant in *space* but may depend on time, say `C(t)`. With the reference gauge `φ→0`, `u→0`, and `p→p∞(t)` at infinity, `C(t)=p∞(t)/ρ`. Thus unsteady Bernoulli is

括号内的量在**空间中**为常数，但可以随时间变化，记为 `C(t)`。若采用无穷远参考条件 `φ→0`、`u→0`、`p→p∞(t)`，则 `C(t)=p∞(t)/ρ`。于是非定常伯努利方程为：



$$
\boxed{\frac{\partial\phi}{\partial t}+\frac12|\boldsymbol u|^2+\frac{p}{\rho}=\frac{p_\infty}{\rho}.}
$$



At a clean inviscid gas–liquid interface, the normal-stress jump reduces to the signed Young–Laplace relation

在洁净、无黏的气液界面处，法向应力跳跃关系简化为带符号的 Young–Laplace 关系：



$$
\boxed{p_l=p_b+\sigma\kappa,\qquad \kappa=\nabla_s\cdot\boldsymbol n.}
$$



The course defines `n` from liquid to gas. For an *interior spherical cavity* this makes `κ=-2/R`, so `p_l=p_b-2σ/R`, consistent with the earlier spherical model. Evaluate Bernoulli on the liquid side of `Γ` and substitute `p=p_l`:

课程定义 `n` 从液体指向气体。对于**液体内部的球形空腔**，这使得 `κ=-2/R`，因此 `p_l=p_b-2σ/R`，与前面的球对称模型一致。在 `Γ` 的液体侧使用 Bernoulli 方程，再代入 `p=p_l`：



$$
\frac{\partial\phi}{\partial t}+\frac12|\boldsymbol u|^2+\frac{p_b+\sigma\kappa}{\rho}=\frac{p_\infty}{\rho}.
$$



Rearranging gives the displayed Eulerian dynamic boundary condition:

整理后就得到截图里的欧拉形式动力学边界条件：



$$
\boxed{\left.\frac{\partial\phi}{\partial t}\right|_{\Gamma}=\frac{p_\infty-p_b-\sigma\kappa}{\rho}-\frac12|\boldsymbol u|^2.}
$$



This is the missing derivation: **Euler momentum → unsteady Bernoulli → interface normal-stress balance → dynamic interface condition**.

这就是被省略的推导链：**Euler 动量方程 → 非定常伯努利方程 → 界面法向应力平衡 → 动力学界面条件**。

#### 5. Why does the last equation have plus one half?

#### 为什么最后一个方程变成正的二分之一？

The preceding `∂φ/∂t` is an Eulerian derivative at fixed spatial position, evaluated on the interface. The last line instead differentiates `φ(X(t),t)` **while following the moving material marker**. Apply the multivariable chain rule:

前面的 `∂φ/∂t` 是在固定空间位置取时间偏导，再在界面处取值。最后一行却是**沿运动界面物质点**对 `φ(X(t),t)` 求全导数，因此需要多变量链式法则：



$$
\frac{D\phi}{Dt}=\frac{d}{dt}\phi(\boldsymbol X(t),t)=\frac{\partial\phi}{\partial t}+\frac{d\boldsymbol X}{dt}\cdot\nabla\phi.
$$



For material interface markers, `dX/dt=u`, and since `∇φ=u`, their dot product is `|u|²`:

由于界面物质点满足 `dX/dt=u`，且 `∇φ=u`，点积等于 `|u|²`：



$$
\frac{D\phi}{Dt}=\frac{\partial\phi}{\partial t}+|\boldsymbol u|^2
=\frac{p_\infty-p_b-\sigma\kappa}{\rho}-\frac12|\boldsymbol u|^2+|\boldsymbol u|^2.
$$



Therefore,

因此：

Combine the negative half and positive whole squared-speed contributions.

合并负二分之一与正一倍的速度平方项。



$$
\boxed{\frac{D\phi}{Dt}=\frac{p_\infty-p_b-\sigma\kappa}{\rho}+\frac12|\boldsymbol u|^2\quad(\boldsymbol X\in\Gamma).}
$$



The sign changes only because of the additional advection term. **This is not an independent fifth physical law; it is the same dynamic boundary condition expressed on a moving marker.**

正负号变化只来自额外的对流项。**这并不是第五条独立物理定律，而是同一动力学界面条件在运动标记点上的表达。**

#### 6. In what sense is the model closed?

#### 模型究竟在哪个意义上闭合？

For *prescribed* `p_b(t)`, material parameters, complete initial interface shape and surface potential, and consistent boundary conditions at walls, outlets, far field and contact lines, the mathematical potential-flow problem can be advanced through a coupled loop:

在**给定** `p_b(t)`、物性参数、完整初始界面形状及表面速度势，并设置壁面、出口、远场和接触线等一致边界条件后，可以通过以下耦合步骤推进势流问题：

1. Given the current `Γ(t)` and surface potential `φ|Γ`, solve `∇²φ=0` in the current liquid geometry with all remaining boundary conditions.

   已知当前 `Γ(t)` 和界面速度势 `φ|Γ`，结合其余边界条件，在当前液体几何内求解 `∇²φ=0`。
2. Compute `u=∇φ` at the interface and curvature `κ` from its geometry.

   求得界面速度 `u=∇φ`，并从界面几何计算曲率 `κ`。
3. Use the kinematic condition to advance `X`.

   用运动学条件更新界面位置 `X`。
4. Use the material dynamic condition to advance the interface potential `φ|Γ`.

   用物质形式的动力学条件更新界面速度势 `φ|Γ`。
5. Update the geometry and repeat until the model's assumptions cease to apply.

   更新几何并重复，直到模型假设不再适用。

In this sense, there is one bulk elliptic problem and two evolving surface quantities (`X` and `φ|Γ`), with one kinematic and one dynamic evolution equation. The interior pressure can be reconstructed from Bernoulli; it is not an additional independent bulk evolution variable in this reduction.

从这个意义上说，模型包含一个流体内部的椭圆方程，以及界面上两个需要演化的量（`X` 与 `φ|Γ`），分别由运动学和动力学演化方程推进。流体内部压力可以由 Bernoulli 关系恢复，不再是此约化模型中的独立演化未知量。

**Not yet closed for a real PFC jet:** If `p_b(t)` is unknown, Chapter 2 must supply thermodynamics, heat transfer and finite phase inventory. If there is substantial evaporation/condensation, `dX/dt=u` is no longer the appropriate full interfacial kinematic law; a mass-flux jump condition is needed. If the geometry lacks outlet/contact-line conditions, the spatial problem is underdetermined. Strong compressibility, shocks, interface penetration and topology change also exceed the present potential-flow assumptions.

**对于真实 PFC 射流仍未完全闭合：** 若 `p_b(t)` 未知，则必须依靠第二章的热力学、热传递及有限相变物质量模型求解。若蒸发或凝结明显，`dX/dt=u` 不再是适用的完整运动学规律，而需要界面质量通量跳跃条件。若出口或接触线边界条件未给出，则空间问题仍欠定。强可压缩性、激波、界面穿透与拓扑变化也超出当前势流模型的适用范围。

**Symbols for Eq. (C1.7-E28).**

**式（C1.7-E28）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\boldsymbol u$ is liquid velocity (m s⁻¹)<br>$\boldsymbol u$ 为液体速度（m s⁻¹） | $\phi$ is velocity potential (m² s⁻¹)<br>$\phi$ 为速度势（m² s⁻¹） |
| $\boldsymbol X$ is a material interface position (m)<br>$\boldsymbol X$ 为物质界面点位置（m） | $t$ is time (s)<br>$t$ 为时间（s） |
| $\Gamma$ is the liquid–gas interface (—)<br>$\Gamma$ 为液—气界面（—） | $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $\sigma$ is surface tension (N m⁻¹)<br>$\sigma$ 为表面张力（N m⁻¹） |
| $\kappa$ is curvature for the liquid-to-gas normal (m⁻¹)<br>$\kappa$ 为液体指向气体法向下的曲率（m⁻¹） | $\rho$ is density (kg m⁻³)<br>$\rho$ 为密度（kg m⁻³） |
| $p_l$ — liquid-side interface pressure (Pa)<br>$p_l$ — 界面液体侧压力（Pa） | $\nabla$ — spatial gradient operator (m⁻¹)<br>$\nabla$ — 空间梯度算子（m⁻¹） |
| $\nabla^2$ — spatial Laplacian operator (m⁻²)<br>$\nabla^2$ — 空间拉普拉斯算子（m⁻²） | $D/Dt$ — material time derivative (s⁻¹)<br>$D/Dt$ — 物质时间导数（s⁻¹） |
| $\partial_t$ — time derivative at fixed position (s⁻¹)<br>$\partial_t$ — 固定位置的时间导数（s⁻¹） | $\Omega(t)$ — time-dependent liquid domain (—)<br>$\Omega(t)$ — 随时间变化的液体区域（—） |
| $\boldsymbol x$ — fixed spatial position (m)<br>$\boldsymbol x$ — 固定空间位置（m） | $\alpha$ — dimensionless interface marker label (1)<br>$\alpha$ — 无量纲界面标记参数（1） |
| $\boldsymbol n$ — unit normal directed from liquid to gas (1)<br>$\boldsymbol n$ — 液体指向气体的单位法向（1） | $\nabla_s\cdot$ — surface divergence operator (m⁻¹)<br>$\nabla_s\cdot$ — 表面散度算子（m⁻¹） |
| $p$ — local liquid pressure (Pa)<br>$p$ — 局部液体压强（Pa） | $C(t)$ — Bernoulli integration function (m² s⁻²)<br>$C(t)$ — 伯努利积分函数（m² s⁻²） |
| $R$ — radius in the spherical limit (m)<br>$R$ — 球形极限中的半径（m） |  |

**Conventions and conditions.** $\nabla$ and $\nabla^2$ are spatial gradient and Laplacian; $D/Dt$ is the material derivative; $|\boldsymbol u|$ is speed and the dot a vector contraction; The potential gauge is fixed at infinity; Interface markers $\boldsymbol X(t)$ follow liquid particles; $D\phi/Dt$ has units m² s⁻²; assume single-valued potential and a smooth pre-impact interface.

**约定与条件。** $\nabla$ 与 $\nabla^2$ 为空间梯度与拉普拉斯；$D/Dt$ 为物质导数；$|\boldsymbol u|$ 为速率，圆点为矢量缩并；速度势参考值固定在无穷远；界面标记点 $\boldsymbol X(t)$ 随液体质点运动；$D\phi/Dt$ 单位为 m² s⁻²；假设速度势单值且撞击前界面光滑。

![The interface shape evolves jointly with potential; changing geometry creates focusing.](../assets/figures/c1-e28.svg)

The interface shape evolves jointly with potential; changing geometry creates focusing.

界面形状与速度势共同演化，几何变化产生聚焦。

**Check and interpretation.** Solve-and-advance loop: prescribe initial interface and potential; evaluate pressure input and curvature; solve the harmonic field with interface potential and impermeable-wall normal data; recover velocity; advance interface positions and interface potential; repeat. An outlet supplies its pressure or compatible potential condition. Far-field gauge fixes the additive freedom. Material and Eulerian dynamic conditions are alternative forms. Missing: physical PFC pressure history, phase transfer, contact-line law where applicable, and treatment of topology changes.

**检验与解释。** 求解推进循环：给定初始界面与速度势；计算输入压力和曲率；用界面速度势及不透壁法向条件求解调和场；恢复速度；推进界面位置和界面速度势；重复计算。出口需给定压力或相容速度势条件。远场规范固定加法自由度。物质与欧拉动力学条件为等价表述。缺少：实际 PFC 压力历程、相变传质、适用处的接触线规律及拓扑变化处理。

Check the spherical limit of Eq. (C1.7-E28). Wall potential is minus radius × wall speed. Curvature is minus two/radius. Differentiate the wall potential and rearrange the squared-speed term. This recovers inviscid Rayleigh–Plesset. Interface penetration then changes topology. Post-penetration flow requires a new domain and pressure-transmission model.

检验式（C1.7-E28）的球形极限。壁面速度势为半径 × 壁面速度的负值，曲率为负二／半径。对壁面速度势求导并移项速度平方项，可恢复无黏 Rayleigh–Plesset 方程。界面穿透会改变拓扑，之后的流动需要新区域和压力传播模型。

### Step 1.7.4 — Recover the radial model as a consistency check

### 步骤 1.7.4——恢复径向模型以检验一致性

**Purpose in this chapter.** Apply Eq. (C1.7-E28) to a sphere. Recovering the inviscid form of Eq. (C1.3-E07) checks the moving-interface signs and derivative convention.

**本章作用。** 将式（C1.7-E28）用于球面。恢复无黏形式的式（C1.3-E07），用于检验运动界面的符号与导数约定。

**Derivation.**

**推导。**

(C1.7-E29) · Exact spherical recovery of the potential closure / (C1.7-E29) · 势流闭合关系对球形模型的精确恢复

#### 7. Spherical consistency check

#### 球对称极限校验

The interface potential from C1.3-E03 is `φΓ=-RṘ`. Along the moving boundary,

根据 C1.3-E03，球形界面速度势为 `φΓ=-RṘ`。沿运动界面求导：



$$
\frac{D\phi_\Gamma}{Dt}=\frac{d}{dt}(-R\dot R)=-\dot R^2-R\ddot R.
$$



Insert `κ=-2/R`, `|u|²=Ṙ²` into the dynamic condition:

代入 `κ=-2/R`、`|u|²=Ṙ²`：



$$
-\dot R^2-R\ddot R=\frac{p_\infty-p_b+2\sigma/R}{\rho}+\frac12\dot R^2.
$$



Rearranging gives the inviscid Rayleigh–Plesset equation:

整理后得到无黏 Rayleigh–Plesset 方程：



$$
\boxed{\rho\left(R\ddot R+\frac32\dot R^2\right)=p_b-p_\infty-\frac{2\sigma}{R}.}
$$



This shows the mathematical compatibility of C1.7-E28 with the earlier spherical equations, **not experimental validation of nonspherical PFC jetting**.

这表明 C1.7-E28 与前面的球对称方程在数学上相容，**并不构成非球对称 PFC 射流的实验验证**。

**Symbols for Eq. (C1.7-E29).**

**式（C1.7-E29）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\phi_\Gamma$ is the velocity potential evaluated on the spherical interface (m² s⁻¹), with subscript $\Gamma$ the interface label<br>$\phi_\Gamma$ 为球形界面处速度势（m² s⁻¹），下标 $\Gamma$ 标识界面 | $R>0$ is radius (m)<br>$R>0$ 为半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |
| $\kappa$ is signed liquid-to-gas curvature (m⁻¹)<br>$\kappa$ 为液体指向气体约定下的带符号曲率（m⁻¹） | $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $\sigma$ is surface tension (N m⁻¹)<br>$\sigma$ 为表面张力（N m⁻¹） |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $\Gamma$ — Moving liquid–gas interface (—)<br>$\Gamma$ — 运动液—气界面（—） |
| $t$ — time (s)<br>$t$ — 时间（s） |  |

**Conventions and conditions.** The potential is differentiated along the wall; viscosity is zero in this check; $d/dt$ follows the spherical interface.

**约定与条件。** 速度势沿壁面求导；此检验中黏度为零；$d/dt$ 跟随球形界面。

![The spatial potential formulation returns the spherical model under spherical geometry.](../assets/figures/c1-e29.svg)

The spatial potential formulation returns the spherical model under spherical geometry.

空间势流表述在球形几何下恢复球形模型。

**Check and interpretation.** This recovers the inviscid radial balance with the same capillary sign. The viscous term cannot emerge from an inviscid potential boundary condition. At static equilibrium the Laplace overpressure is recovered.

**检验与解释。** 该结果恢复相同毛细符号的无黏径向平衡。无黏势流边界条件不能产生黏性项。静态极限恢复拉普拉斯过压。

### Step 1.7.5 — Check whether incompressibility is adequate for the event

### 步骤 1.7.5——检验事件是否适用不可压缩近似

**Purpose in this chapter.** Compare wall speed and event duration with acoustic scales. These separate diagnostics delimit both the pressure-impulse reduction and the incompressible interface model.

**本章作用。** 将壁面速度与事件持续时间同声学尺度比较。这两个独立诊断分别限定压力冲量约化及不可压缩界面模型的适用范围。

**Derivation.**

**推导。**

(C1.7-E30) · Compressibility applicability diagnostics / (C1.7-E30) · 可压缩性适用性诊断

#### 1. Start with two physically different questions

#### 两个物理上不同的问题

**Question A — motion magnitude:** Is the cavity wall moving slowly compared with the speed of sound in the surrounding liquid? We define the wall Mach number from a measured or computed wall-speed history, not from the laser pulse intensity:

**问题 A——运动速度的大小：** 空腔壁面运动速度相对周围液体声速是否足够慢？壁面马赫数来自实测或计算的壁面速度历程，而不是来自激光脉冲强度：



$$
M_w(t)=\frac{|\dot R(t)|}{c},\qquad M_{w,\max}=\max_{t\in[t_0,t_1]}M_w(t).
$$



**Question B — pressure communication:** Can a change in pressure propagate across the relevant liquid region before the imposed loading changes appreciably? This comparison involves an acoustic travel time and a *load variation time*; it does not follow from the wall Mach number.

**问题 B——压力传播：** 压力扰动能否在外部载荷发生显著变化之前传播至相关液体区域的另一端？该问题需要比较声传播时间与*载荷变化时间*，不能仅从壁面马赫数推出。

#### 2. Derive the propagation time from compressible conservation

#### 从可压缩守恒方程解释传播时间

For a small acoustic disturbance in an initially resting, homogeneous, inviscid, barotropic liquid, write density $\rho=\rho_0+\rho'$, pressure $p=p_0+p'$, and velocity $\boldsymbol u'$. Linearized mass conservation is

对初始静止、均匀、无黏、压强仅与密度相关的液体，考虑小幅声学扰动：密度 $\rho=\rho_0+\rho'$、压力 $p=p_0+p'$、速度 $\boldsymbol u'$。线性化质量守恒为：



$$
\frac{\partial\rho'}{\partial t}+\rho_0\nabla\cdot\boldsymbol u'=0.\tag{1}
$$



Linearized momentum conservation gives

线性化动量守恒给出：



$$
\rho_0\frac{\partial\boldsymbol u'}{\partial t}=-\nabla p'.\tag{2}
$$



Define the small-disturbance sound speed by the barotropic relation $p'=c^2\rho'$. Differentiate equation (1) in time and take the divergence of equation (2):

用小扰动声速对应的本构关系 $p'=c^2\rho'$。对式 (1) 求时间导数，并对式 (2) 求散度：



$$
\frac{\partial^2\rho'}{\partial t^2}+\rho_0\nabla\cdot\frac{\partial\boldsymbol u'}{\partial t}=0,\qquad
\rho_0\nabla\cdot\frac{\partial\boldsymbol u'}{\partial t}=-\nabla^2p'.\tag{3}
$$



Substitution produces $\partial_t^2\rho'-\nabla^2p'=0$. For constant $c$, using $\rho'=p'/c^2$ gives the acoustic wave equation:

代入得到 $\partial_t^2\rho'-\nabla^2p'=0$。声速为常数时，使用 $\rho'=p'/c^2$，得到声波方程：



$$
\boxed{\frac{\partial^2p'}{\partial t^2}=c^2\nabla^2p'.}\tag{4}
$$



The disturbance propagates at speed $c$ under these assumptions. Over an appropriately selected communication distance $L_e$, the one-way acoustic crossing time is

在上述假设下，扰动以声速 $c$ 传播。对于选定的压力通信距离 $L_e$，单程声穿越时间为：



$$
\boxed{t_a=\frac{L_e}{c}.}\tag{5}
$$



This is a propagation *scale*, not a precise delay for every reflected or multidimensional wave pattern. Boundaries, geometry and variable sound speed may change the relevant communication path.

它是传播*时间尺度*，不是每个反射或多维波形的精确延迟。边界、几何与变声速可能改变真实的通信路径。

#### 3. Define the communication ratio and derive its meaning

#### 定义通信比并说明物理意义

Let $\tau_e$ be the characteristic time over which the **relevant load changes**, such as its rise time, pressure-reversal time or a specified high-gradient transient. Then

令 $\tau_e$ 为**相关载荷发生显著变化的特征时间**，例如压力上升时间、反向时间或指定的急剧变化瞬态，则：



$$
\boxed{\mathcal C_e=\frac{t_a}{\tau_e}=\frac{L_e}{c\tau_e}.}\tag{6}
$$



If $\mathcal C_e\ll1$, acoustic communication is fast compared with the imposed change, so the instantaneous-pressure-equilibration idea is more plausible. If $\mathcal C_e\gtrsim1$, the pressure changes before information can cross the region: propagation delay, wave reflection and compressibility may be essential. There is no universal sharp threshold or guaranteed numerical error bound at a particular value of $\mathcal C_e$.

若 $\mathcal C_e\ll1$，声学通信相对载荷变化很快，瞬时压力平衡近似更有可能成立。若 $\mathcal C_e\gtrsim1$，压力在信息传遍区域之前已经显著改变，传播延迟、波反射和可压缩性可能不可忽略。对于 $\mathcal C_e$ 不存在普适的突变阈值，也不能在某个指定比值上直接给出有保证的数值误差界限。

**Crucial distinction:** $M_w$ uses velocity; $\mathcal C_e$ uses geometry and forcing time. A small $M_w$ says nothing on its own about how suddenly pressure changes.

**关键区别：** $M_w$ 使用速度；$\mathcal C_e$ 使用几何尺度和载荷变化时间。$M_w$ 小，并不能单独说明压力变化是否很突然。

#### 4. Numerical test: same wall speed, different pressure rise

#### 数值检验：相同壁面速度，不同压力上升时间

Choose an **illustrative**, not experimentally calibrated, communication distance $L_e=100\ \mu\mathrm m=10^{-4}\ \mathrm m$, carrier sound speed $c=1500\ \mathrm{m/s}$, and a wall velocity magnitude $|\dot R|=15\ \mathrm{m/s}$. The speed criterion is

选择一组**教学示例**而非实验标定的参数：通信距离 $L_e=100\ \mu\mathrm m=10^{-4}\ \mathrm m$，载液声速 $c=1500\ \mathrm{m/s}$，壁面速度大小 $|\dot R|=15\ \mathrm{m/s}$。速度准则为：



$$
M_w=\frac{15}{1500}=0.010,\qquad
t_a=\frac{10^{-4}}{1500}=6.6667\times10^{-8}\ \mathrm s=66.667\ \mathrm{ns}.\tag{7}
$$



For a fast pressure rise $\tau_e=10\ \mathrm{ns}$:

对于快速上升的压力载荷 $\tau_e=10\ \mathrm{ns}$：



$$
\mathcal C_{e,\mathrm{fast}}=\frac{66.667\ \mathrm{ns}}{10\ \mathrm{ns}}=6.667.\tag{8}
$$



For a *different* slowly rising load $\tau_e=1\ \mu\mathrm s=1000\ \mathrm{ns}$:

对于**另一种**缓慢上升的载荷 $\tau_e=1\ \mu\mathrm s=1000\ \mathrm{ns}$：



$$
\mathcal C_{e,\mathrm{slow}}=\frac{66.667}{1000}=0.06667.\tag{9}
$$



Both scenarios have the same assumed $M_w=0.01$, but the first does **not** support an instantaneous-pressure-field approximation during the rise, whereas the second is more favorable. Neither number independently proves a quantitative solution-error bound.

两种情形都具有相同的假定 $M_w=0.01$，但第一种载荷在上升阶段**不支持**瞬时压力场近似；第二种则更有利于该近似。二者的指标都不能单独证明定量求解误差上界。

#### 5. Distinguish impulse duration from rise time

#### 区分冲量持续时间与载荷上升时间

Section 1.6 uses a nominal $0.50\ \mu\mathrm s$ pressure-impulse interval over a $100\ \mu\mathrm m$ column. Using that duration gives $t_a/\tau=66.667/500=0.1333$. **But this ratio is not necessarily the relevant $\mathcal C_e$:** if the actual pressure rise takes only $10\ \mathrm{ns}$, its communication ratio remains 6.667 during that rise. The lesson must state or measure the loading waveform before claiming a pressure-communication screen has passed.

第 1.6 节以 $100\ \mu\mathrm m$ 液柱和 $0.50\ \mu\mathrm s$ 压力冲量区间为例。若直接用脉宽计算，则 $t_a/\tau=66.667/500=0.1333$。**但这不一定是真正相关的 $\mathcal C_e$：** 如果真实压力上升仅用 $10\ \mathrm{ns}$，则上升期间的通信比仍为 6.667。因此，课程必须给定或测量载荷波形，才能宣称压力通信筛选是否通过。

The section's $U=3\ \mathrm{m/s}$ is a **liquid-column speed increment**, not necessarily the bubble-wall speed. It gives a different liquid-speed Mach scale $U/c=0.002$; it cannot silently be substituted for $M_w$ unless that velocity is genuinely the wall velocity.

该节的 $U=3\ \mathrm{m/s}$ 是**液柱速度增量**，不一定是气泡壁面速度。它对应另一个液体流速马赫数尺度 $U/c=0.002$；只有确实代表壁面速度时，才能代入 $M_w$。

#### 6. Can the short-impulse approximation and rapid communication coexist?

#### 短时冲量近似与快速通信能否同时满足？

The reduced impulse model neglects convection when $U\tau/L\ll1$, and needs fast pressure communication when $L/(c\tau_e)\ll1$. If the relevant event variation time is on the order of the pulse duration $\tau_e\sim\tau$, both can hold when the time hierarchy is

简化冲量模型在 $U\tau/L\ll1$ 时忽略对流，而快速压力通信要求 $L/(c\tau_e)\ll1$。如果载荷变化时间与脉宽同阶 $\tau_e\sim\tau$，则两者可以在如下尺度层级中同时成立：



$$
\boxed{\frac{L}{c}\ll\tau\ll\frac{L}{U}}.\tag{10}
$$



This requires $U\ll c$, but the latter alone does not guarantee that a particular selected $\tau$ lies between the two times. A separate viscous-diffusion check $\nu\tau/L^2\ll1$ is needed for the reduced bulk description, and does not substitute for wall-boundary-layer analysis.

这要求 $U\ll c$，但仅有后者并不能保证实际选定的 $\tau$ 位于两个时间尺度之间。对简化体相描述还须独立检验黏性扩散尺度 $\nu\tau/L^2\ll1$，且这不能代替壁面边界层的分析。

#### 7. Mandatory output table when applying C1.7-E30

#### 应用 C1.7-E30 时必须报告的结果表

| Required entry<br>必填项 | What to state<br>应报告内容 |
| --- | --- |
| Geometry<br>几何 | Actual liquid region and pressure-communication path $L_e$<br>真实液体区域与通信路径 $L_e$ |
| Material state<br>材料状态 | $c$, how obtained, pressure/temperature dependence<br>声速 $c$、其来源和压力/温度依赖 |
| Motion<br>运动 | $\dot R(t)$ and event-window $M_{w,\max}$<br>速度历程与事件内最大壁面马赫数 |
| Loading<br>载荷 | Actual rise/change time $\tau_e$, not merely pulse width<br>实际上升/变化时间，非仅脉宽 |
| Communication<br>通信 | $t_a=L_e/c$, $\mathcal C_e=t_a/\tau_e$<br>声穿越时间及通信比 |
| Conclusion<br>结论 | Supported approximation, uncertainties, missing geometry or waveform, compressible comparison if needed<br>支持的近似、不确定性、缺失波形及必要时的可压缩求解对照 |

**Defensible claim:** These are practical applicability diagnostics, not physical hard limits, proof of incompressibility, or independent validation of a cavitation jet.

**可辩护的结论：** 它们是实用的适用性诊断，不是物理硬极限，不构成不可压缩性的数学证明，也不是空化射流的独立验证。

**Symbols for Eq. (C1.7-E30).**

**式（C1.7-E30）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $M_w$ is wall Mach number (dimensionless)<br>$M_w$ 为壁面马赫数（无量纲） | $\mathcal C_e$ a pressure-communication ratio (both dimensionless)<br>$\mathcal C_e$ 为压力通信比（两者均无量纲） |
| $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $c>0$ is carrier sound speed (m s⁻¹)<br>$c>0$ 为载液声速（m s⁻¹） |
| $L_e>0$ is the distance across which loading must communicate (m)<br>$L_e>0$ 为载荷必须传播的距离（m） | $\tau_e>0$ is the event's relevant rise or change time (s)<br>$\tau_e>0$ 为事件相关的上升或变化时间（s） |
| $\rho_0$ — positive uniform background density (kg m⁻³)<br>$\rho_0$ — 均匀背景正密度（kg m⁻³） | $\rho'$ — small acoustic density perturbation (kg m⁻³)<br>$\rho'$ — 小幅声学密度扰动（kg m⁻³） |
| $p'$ — small acoustic pressure perturbation (Pa)<br>$p'$ — 小幅声学压力扰动（Pa） | $\boldsymbol u'$ — small acoustic velocity perturbation (m s⁻¹)<br>$\boldsymbol u'$ — 小幅声学速度扰动（m s⁻¹） |
| $\nabla\cdot$ — spatial divergence operator (m⁻¹)<br>$\nabla\cdot$ — 空间散度算子（m⁻¹） | $\nabla^2$ — spatial Laplacian operator (m⁻²)<br>$\nabla^2$ — 空间拉普拉斯算子（m⁻²） |
| $\partial_t$ — time derivative at fixed position (s⁻¹)<br>$\partial_t$ — 固定位置的时间导数（s⁻¹） | $t$ — time (s)<br>$t$ — 时间（s） |
| $t_a$ — one-way acoustic travel time (s)<br>$t_a$ — 单程声传播时间（s） | $\rho$ — total liquid density (kg m⁻³)<br>$\rho$ — 总液体密度（kg m⁻³） |
| $p$ — total liquid pressure (Pa)<br>$p$ — 总液体压强（Pa） | $p_0$ — uniform background pressure (Pa)<br>$p_0$ — 均匀背景压强（Pa） |
| $M_{w,\max}$ — maximum wall Mach number in the stated event window (1)<br>$M_{w,\max}$ — 给定事件区间内的最大壁面马赫数（1） | $t_0$ — event-window start (s)<br>$t_0$ — 事件区间起点（s） |
| $t_1$ — event-window end (s)<br>$t_1$ — 事件区间终点（s） | $U$ — characteristic liquid speed; distinct from wall speed (m s⁻¹)<br>$U$ — 特征液体速度；与壁速有区别（m s⁻¹） |
| $L$ — liquid-column length or chosen flow scale (m)<br>$L$ — 液柱长度或选定流动尺度（m） | $\tau$ — pressure-impulse integration duration (s)<br>$\tau$ — 压力冲量积分时长（s） |
| $\nu$ — kinematic viscosity (m² s⁻¹)<br>$\nu$ — 运动黏度（m² s⁻¹） |  |

**Conventions and conditions.** $|\ |$ denotes magnitude; subscript $e$ labels the selected event scale; Primes denote small acoustic perturbations; ns is 10⁻⁹ s; linearization assumes inviscid barotropic liquid and constant $c$.

**约定与条件。** $|\ |$ 表示大小；下标 $e$ 标识选定事件尺度；撇号标记小幅声学扰动；ns 为 10⁻⁹ s；线性化假设液体无黏、正压且声速恒定。

![A pressure pulse can require compressibility even while the bulk wall speed is modest.](../assets/figures/c1-e30.svg)

A pressure pulse can require compressibility even while the bulk wall speed is modest.

即使总体壁面速率不高，压力脉冲仍可能要求考虑可压缩性。

**Check and interpretation.** Operational test: record geometry, pressure observer, sound-speed source and uncertainty; identify the pressure variation time; sample wall speed with adequate temporal resolution; compute both ratios over the event. The rapid example fails pressure communication despite small Mach number. The slow example supports that approximation. These illustrative inputs are unmeasured. Thresholds are diagnostics, without certified error bounds. The impulse model also needs small displacement, advection and viscous corrections.

**检验与解释。** 实际检验：记录几何、压力观察位置、声速来源和不确定度；辨认压力变化时间；以足够时间分辨率采样壁面速度；在事件中计算两个比值。快速示例虽马赫数小，但压力通信不足。慢速示例支持该近似。这些示例输入未经实测。阈值属于诊断，不具有认证误差界。冲量模型还要求位移、对流和黏性修正较小。

Small wall Mach number and communication ratio test different incompressible assumptions. Jet survival, arriving mass, footprint and receiver response need further models. Chapter 3 defines finite-mass, finite-time jet observables. Chapter 4 connects those loads to release. Here, compressibility enters through rapid transmission and arrest.

小壁面马赫数与小通信比检验不同的不可压缩假设。射流存续、到达质量、作用面积及受载响应需要进一步模型。第三章定义有限质量、有限时间射流观测量，第四章将载荷连接至释放。这里通过快速传播与终止过程考虑可压缩性。

**Results and remaining inputs.** The radial momentum, energy, collapse-time and column-impulse calculations are derived above. The spatial jet model includes oriented interface conditions. PFC jet prediction still requires thermodynamic pressure history and actual geometry. It also requires the evolving spatial solution.

**结果与所需输入。** 上文已推导径向动量、能量、塌缩时间及液柱冲量。空间射流模型明确了界面方向条件。预测 PFC 射流仍需热力学压力历程、实际几何及演化空间解。

## 1.8 Oral questions

## 1.8 口头问题

Answer each question in your own words. Explain the governing equations and their assumptions. The reference answers support comparison after your attempt. Mastery requires a demonstrated explanation. Saving a response does not establish understanding.

请用自己的话回答各题，解释控制方程及其假设。作答后可与参考答案比较。掌握需要通过解释展示。保存回答并不代表理解。

### Question 1 — What connects cavity motion to an external transfer jet?

### 问题 1——哪些力学环节将空腔运动连接至外部转印射流？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

#### Step 1.8.1 — Connect bubble pressure to the transfer-jet explanation

#### 步骤 1.8.1——将气泡压力连接至转印射流解释

**Purpose in this chapter.** Combine the radial balance and pressure composition from Section 1.3. Use them to explain the source of liquid motion, then identify the boundary information required for an external jet.

**本章作用。** 结合第1.3节的径向平衡与压力组成。用它们解释液体运动的来源，再指出外部射流还需要的边界信息。

**Derivation.** Reconstruct the causal chain before answering. Subtract far-field pressure from the normal traction law, equate it to radial inertia, then solve for acceleration. The mixture statement identifies the missing source input. Follow the full Euler-to-Bernoulli derivation in C1.3-E05 and energy conversion in C1.4-E11. For a directional outlet, replace the scalar radial solution with C1.7-E26–C1.7-E28 and the actual boundaries.

**推导。** 作答前重建因果链。从法向牵引关系减去远场压力，将其与径向惯性相等，再求加速度。混合物关系指出缺失的源输入。完整欧拉至伯努利推导见 C1.3-E05，能量转换见 C1.4-E11。存在定向出口时，用 C1.7-E26–C1.7-E28 及实际边界替代标量径向解。

(C1.8-E31) · Original formulas quoted for defense 1 / (C1.8-E31) · 答辩问题 1 引用的原始公式

Use the spherical interface stress balance to express liquid-side pressure in terms of bubble pressure.

利用球形界面应力平衡，以气泡压力表示液体侧压力。



$$
\begin{aligned}p_l-p_\infty&=p_b-p_\infty-2\sigma/R-4\mu\dot R/R,\end{aligned}
$$



Use Bernoulli to express that same liquid pressure through wall inertia.

利用伯努利关系，通过壁面惯性表示同一液体压力。



$$
\begin{aligned}p_l-p_\infty&=\rho R\ddot R+\tfrac32\rho\dot R^2,\end{aligned}
$$



Equate these two pressure expressions and isolate the acceleration contribution.

令这两个压力表达式相等，并分离加速度贡献。



$$
\begin{aligned}\rho R\ddot R&=p_b-p_\infty-2\sigma/R-4\mu\dot R/R-\tfrac32\rho\dot R^2,\end{aligned}
$$



Divide by positive liquid density and cavity radius. This gives acceleration for the stated pressure input.

除以正的液体密度与空腔半径。由此得到给定压力输入下的加速度。



$$
\begin{aligned}\ddot R&=\frac{p_b-p_\infty-2\sigma/R-4\mu\dot R/R-\tfrac32\rho\dot R^2}{\rho R}.\end{aligned}
$$



Collect the radial motion law for the pressure-to-liquid-motion explanation.

为压力驱动液体运动的解释汇总径向运动规律。



$$
\rho\left(R\ddot R+\frac32\dot R^2\right)=p_b-p_\infty-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}
$$



Identify the vapor and permanent-gas inputs still needed to prescribe bubble pressure.

明确给定气泡压力仍需的蒸气与非凝结气体输入。



$$
p_b=p_{v,\mathrm{PFC}}+p_{v,w}+p_g
$$



**Symbols for Eq. (C1.8-E31).**

**式（C1.8-E31）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $R>0$ is cavity radius (m)<br>$R>0$ 为空腔半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） |
| $\sigma$ is surface tension (N m⁻¹)<br>$\sigma$ 为表面张力（N m⁻¹） | $\mu$ is viscosity (Pa s)<br>$\mu$ 为黏度（Pa s） |
| $p_{v,\mathrm{PFC}}$ — PFC-vapor partial pressure (Pa)<br>$p_{v,\mathrm{PFC}}$ — PFC 蒸气分压（Pa） | $p_{v,w}$ — Water-vapor partial pressure (Pa)<br>$p_{v,w}$ — 水蒸气分压（Pa） |
| $p_g$ — Noncondensable-gas partial pressure (Pa)<br>$p_g$ — 非凝结气体分压（Pa） | $p_l$ — liquid-side wall pressure (Pa)<br>$p_l$ — 壁面液体侧压力（Pa） |

**Conventions and conditions.** The equations are the spherical mechanical balance and the pressure-composition closure target.

**约定与条件。** 两式分别为球形力学平衡与需要闭合的压力组成。

![The source pressure moves carrier liquid; geometry determines whether that motion is a useful jet.](../assets/figures/c1-e31.svg)

The source pressure moves carrier liquid; geometry determines whether that motion is a useful jet.

源压力使载液运动；几何决定这种运动能否成为有用射流。

**Check and interpretation.** Falsification question: does the measured or prescribed pressure history satisfy the stated momentum balance within its regime? An emitted jet further needs direction, finite moving mass and an evolving interface. Transfer success needs a receiver load and fracture evidence.

**检验与解释。** 证伪问题：实测或给定压力历程能否在适用范围内满足所述动量平衡？喷出射流还需要方向、有限运动质量及演化界面。成功转印需要受载面载荷和断裂证据。

Identify PFC inventory, absorber, cavity and force path first. Absorption and phase change must supply the pressure history. Low boiling point leaves that history unresolved. The spherical balance gives acceleration of the surrounding carrier. Capillarity resists expansion and assists collapse. Viscosity dissipates energy in both directions. Keep the liquid inclusion distinct from the cavity.

先辨认 PFC 物质量、吸收体、空腔和传力路径。吸收与相变需提供压力历程。低沸点仍不能确定该历程。球形平衡给出周围载液加速度。毛细作用阻碍膨胀并促进塌缩，黏性在两种方向耗散能量。液态夹杂与空腔须分别描述。

An external jet needs directing geometry, coherent moving liquid and a receiver. Internal collapse jets, sealed inflation and stretched bridges have different event sequences. Track cavity shape, emitted liquid and film motion together. Chapter 2 supplies thermal closure. Chapters 3 and 4 address arrival, fracture and intact placement.

外部射流需要定向几何、相干运动液体及受载表面。内部塌缩射流、密闭膨胀及拉伸液桥有不同事件顺序。应同时追踪空腔形状、喷出液体及薄膜运动。第二章给出热学闭合，第三、四章处理到达、断裂与完整落位。

#### Review criteria

#### 审阅标准

* Distinguishes PFC liquid inventory, cavity contents and accelerated carrier, and states that the pressure history needs thermal/phase closure.

  区分 PFC 液体库存、空腔内容物与被加速载液，并说明压力历程需要热与相变闭合。
* Explains why a radial balance cannot select a jet direction; identifies a concrete asymmetric boundary or outlet.

  解释径向平衡为何不能选定射流方向，并指出具体非对称边界或出口。
* Distinguishes external ejection, re-entrant penetration, sealed inflation and liquid bridging using observable event order.

  利用可观测事件顺序区分外部喷射、再入穿透、密闭膨胀与液桥。
* Does not infer successful fracture or intact placement from cavity size or visible release alone.

  不单凭空腔尺寸或可见释放推断成功断裂或完整落位。

### Question 2 — Explain the Rayleigh coefficient and its speed singularity.

### 问题 2——解释瑞利系数及其速度奇异性的物理范围。

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

#### Step 1.8.2 — Reconstruct the collapse benchmark and its limits

#### 步骤 1.8.2——重建塌缩基准及其限制

**Purpose in this chapter.** Combine the trajectory, collapse-time coefficient, and energy check from Section 1.5. Explain their shared assumptions before discussing the ideal speed singularity.

**本章作用。** 结合第1.5节的轨迹、塌缩时间系数与能量检验。在讨论理想速度奇异性之前，说明这些结果共有的假设。

**Derivation.** Reproduce the collapse chain rather than memorize its coefficient. Use squared speed and the integrating factor from C1.5-E13. Apply the initial condition as in C1.5-E14. Integrate reciprocal inward speed as in C1.5-E15–C1.5-E16. Obtain energy independently from pressure work in C1.5-E17. Check the chosen Mach cutoff using C1.5-E19 before interpreting the singular trajectory.

**推导。** 重现塌缩推导链，不能背诵系数。采用 C1.5-E13 的速度平方和积分因子。按 C1.5-E14 施加初始条件。按 C1.5-E15–C1.5-E16 积分向内速度倒数。按 C1.5-E17 独立用压力功求能量。解释奇异轨迹前，先用 C1.5-E19 检查选定马赫截止条件。

(C1.8-E32) · Original formulas quoted for defense 2 / (C1.8-E32) · 答辩问题 2 引用的原始公式

Introduce squared speed and multiply the ideal radial equation by its integrating factor.

引入速度平方，并将理想径向方程乘以积分因子。



$$
\begin{aligned}y&=\dot R^2,\quad\frac{d(R^3y)}{dR}=-2\Delta p_cR^2/\rho,\end{aligned}
$$



Integrate from the stationary maximum-radius state. Its initial squared speed is zero.

从最大半径处的静止状态开始积分。其初始速度平方为零。



$$
\begin{aligned}R^3y-0&=-\frac{2\Delta p_c}{3\rho}(R^3-R_{\max}^3),\end{aligned}
$$



Choose inward speed, separate time and radius, and normalize the collapse-time integral.

选择向内速度，分离时间与半径，并将塌缩时间积分无量纲化。



$$
\begin{aligned}\dot R&=-\sqrt{y},\quad
    t_c=R_{\max}\sqrt{\frac{3\rho}{2\Delta p_c}}\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx,\end{aligned}
$$



Independently integrate pressure work over cavity volume. This checks the trajectory's energy and integration constant.

独立地对空腔体积积分压力功。这检验轨迹的能量与积分常数。



$$
\begin{aligned}K_l&=\int_{V_{\max}}^{V_b}-\Delta p_c\,dV=\Delta p_c(V_{\max}-V_b).\end{aligned}
$$



State the inward branch of the ideal collapse trajectory.

写出理想塌缩轨迹的向内分支。



$$
\dot R=-\sqrt{\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}R\right)^3-1\right]}
$$



State its collapse time with the evaluated beta-function coefficient.

用已求得的贝塔函数系数写出其塌缩时间。



$$
t_c=\frac{B(5/6,1/2)}{\sqrt6}R_{\max}\sqrt{\frac\rho{\Delta p_c}}
$$



State the independently checked exterior kinetic energy.

写出经独立压力功方法检验的外域动能。



$$
K_l=\frac{4\pi}{3}\Delta p_c(R_{\max}^3-R^3)
$$



**Symbols for Eq. (C1.8-E32).**

**式（C1.8-E32）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\dot R\le0$ is inward wall velocity (m s⁻¹)<br>$\dot R\le0$ 为向内壁面速度（m s⁻¹） | $R\in(0,R_{\max}]$ — Instantaneous cavity radius (m)<br>$R\in(0,R_{\max}]$ — 瞬时空腔半径（m） |
| $R_{\max}$ — Radius at the start of ideal collapse (m)<br>$R_{\max}$ — 理想塌缩开始时的半径（m） | $\Delta p_c>0$ is constant collapse pressure (Pa)<br>$\Delta p_c>0$ 为常数塌缩压差（Pa） |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $t_c$ is ideal collapse time (s)<br>$t_c$ 为理想塌缩时间（s） |
| $B$ is the dimensionless beta function defined in Eq<br>$B$ 为式（C1.5-E17）定义的无量纲贝塔函数 | $K_l$ is carrier kinetic energy (J)<br>$K_l$ 为载液动能（J） |
| $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） | $y$ — squared wall speed (m² s⁻²)<br>$y$ — 壁面速度平方（m² s⁻²） |
| $x$ — normalized radius, $R/R_{\max}$ (1)<br>$x$ — 无量纲半径，$R/R_{\max}$（1） | $V_b$ — cavity volume, $4\pi R^3/3$ (m³)<br>$V_b$ — 空腔体积，$4\pi R^3/3$（m³） |
| $V_{\max}$ — maximum volume, $4\pi R_{\max}^3/3$ (m³)<br>$V_{\max}$ — 最大体积，$4\pi R_{\max}^3/3$（m³） | $V$ — dummy volume variable (m³)<br>$V$ — 积分哑体积变量（m³） |

**Conventions and conditions.** (C1.5-E17); The initial cavity is at rest, with no gas, viscosity, capillarity or compressibility.

**约定与条件。** 初始空腔静止，并忽略非凝结气体、黏性、毛细及可压缩性。

![The singular velocity belongs to an ideal radial trajectory, not a validated physical maximum.](../assets/figures/c1-e32.svg)

The singular velocity belongs to an ideal radial trajectory, not a validated physical maximum.

奇异速度属于理想径向轨迹，而非经过验证的实际最大值。

**Check and interpretation.** Falsification question: do gas pressure, capillarity, viscosity, compressibility or deformation cease to be negligible before the radius of interest? Finite pressure work remains compatible with unbounded ideal speed because the effective radial inertia vanishes. Physical maximum: Not established.

**检验与解释。** 证伪问题：在目标半径之前，气体压力、毛细、黏性、可压缩性或变形是否已不可忽略？有效径向惯性趋于零，因此有限压力功与理想速度无界并不矛盾。实际最大值：尚未建立。

The coefficient integrates the common dimensionless collapse trajectory. Squared speed gives a first-order radial equation. Its integrating factor is radius cubed. Zero initial speed fixes the constant; the negative root selects collapse. Integrating reciprocal speed yields the beta function and 0.9146813565. Quadrupling pressure halves time under the same assumptions.

系数来自共同的无量纲塌缩轨迹积分。速度平方给出一阶径向方程，积分因子为半径三次方。初始零速度确定常数，负平方根选择塌缩分支。速度倒数积分给出贝塔函数及 0.9146813565。在相同假设下，压差增至四倍使时间减半。

The 30 μm control gives 2.744 μs and 11.31 nJ. Half-radius inward speed is 21.60 m s⁻¹. These are spherical pressure–inertia results. PFC activation and emitted jet speed remain unestablished. Finite work coexists with divergent speed because inertia scales with radius cubed. Gas, vapor pressure, compressibility, transport and distortion can arrest that ideal trajectory. A finite-mass maximum needs geometry and observation scales.

30 μm 对照给出 2.744 μs 和 11.31 nJ。一半半径处向内速率为 21.60 m s⁻¹。这些是球形压力—惯性结果。PFC 激活及外部射流速率尚未确立。惯性按半径三次方缩小，因此有限功可与发散速率共存。气体、蒸气压、可压缩性、输运及变形可终止理想轨迹。有限质量最大值需要几何与观测尺度。

#### Review criteria

#### 审阅标准

* Connects the coefficient to the nondimensional radius integral, including the initial condition and collapse branch.

  把系数联系到无量纲半径积分，并说明初始条件与塌缩分支。
* Explains the pressure and radius scaling and gives a consistent numerical or proportionality example.

  解释压差与半径的尺度关系，并给出一致的数值或比例例子。
* Reconciles finite pressure work with the shrinking inertia scale, then identifies concrete neglected arrest mechanisms.

  用不断缩小的惯性尺度解释有限压力功，再指出具体被忽略的终止机制。
* Distinguishes radial wall velocity from a directional jet and refuses a universal maximum without defined geometry, mass and observation scale.

  区分径向壁面速度与定向射流，且在几何、质量和观测尺度未定义时不声称通用最大值。

### Question 3 — Which spatial and temporal inputs determine a transfer jet?

### 问题 3——哪些空间及时间输入决定转印射流？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

#### Step 1.8.3 — Connect pressure history, geometry, and response time

#### 步骤 1.8.3——贯通压力历程、几何与响应时间

**Purpose in this chapter.** Combine Sections 1.6 and 1.7. Distinguish the exact momentum integral, its reduced column benchmark, and the additional spatial and acoustic inputs needed for a transfer-jet prediction.

**本章作用。** 结合第1.6节与第1.7节。区分精确动量积分、其约化液柱基准，以及预测转印射流还需要的空间与声学输入。

**Derivation.** Start with the exact time-integrated momentum in C1.6-E21. Apply C1.6-E22 conditions before discarding residual integrals. Use C1.6-E23 endpoint data to solve the spatial impulse field. C1.7-E30 separately tests communication using rise time. These steps determine an initial velocity increment; subsequent jet shape requires the moving-interface solve.

**推导。** 从 C1.6-E21 的精确时间积分动量出发。先检查 C1.6-E22 条件，再舍去残余积分。采用 C1.6-E23 的端点条件求空间冲量场。C1.7-E30 用上升时间单独检验通信。这些步骤确定初始速度增量；后续射流形状仍需运动界面求解。

(C1.8-E33) · Original formulas quoted for defense 3 / (C1.8-E33) · 答辩问题 3 引用的原始公式

Begin with the exact fixed-position integrated momentum relation. Retain convective and viscous impulses.

从精确的固定位置积分动量关系出发。保留对流与黏性冲量。



$$
\begin{aligned}\Delta\boldsymbol u&=-\nabla\Pi/\rho
       -\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt
       +\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt,\end{aligned}
$$



Under the stated scale and geometry conditions, neglect those two contributions relative to the leading velocity change.

在已声明的尺度与几何条件下，相对于主导速度变化忽略这两项贡献。



$$
\begin{aligned}U\tau/L\ll1,\quad\nu\tau/L^2\ll1
       &\Rightarrow\Delta\boldsymbol u\simeq-\nabla\Pi/\rho,\end{aligned}
$$



Apply incompressibility to the reduced velocity increment. Pressure impulse then satisfies Laplace's equation.

对约化速度增量应用不可压缩条件。压力冲量因此满足拉普拉斯方程。



$$
\begin{aligned}\nabla\cdot\Delta\boldsymbol u=0&\Rightarrow\nabla^2\Pi=0,\end{aligned}
$$



Apply the inlet and outlet impulse values to the straight-column solution.

将入口与出口冲量值应用于直液柱解。



$$
\begin{aligned}\Pi(0)=\Pi_0,\quad\Pi(L)=0&\Rightarrow\Pi(z)=\Pi_0(1-z/L),\end{aligned}
$$



Differentiate the resulting pressure-impulse profile and divide its negative gradient by density.

对所得压力冲量分布求导，再将其负梯度除以密度。



$$
\begin{aligned}\Delta u_z&=-\frac1\rho\frac{d\Pi}{dz}=\frac{\Pi_0}{\rho L}.\end{aligned}
$$



Begin with the fixed-position pressure-impulse definition.

从固定位置的压力冲量定义出发。



$$
\Pi(\boldsymbol x)=\int_{t_0}^{t_1}(p-p_{\mathrm{ref}})dt
$$



State the leading velocity-change relation and its incompressible boundary equation under the required approximations.

在所需近似下，写出主导速度变化关系及其不可压缩边值方程。



$$
\Delta\boldsymbol u\simeq-\frac{\nabla\Pi}{\rho},\quad\nabla^2\Pi=0
$$



Connect the column velocity scale to the pressure-impulse boundary values, and check the acoustic response time.

将液柱速度尺度连接至压力冲量边界值，并检验声学响应时间。



$$
U_{\mathrm{column}}=\frac{\Pi_0}{\rho L},\quad t_a=\frac Lc
$$



**Symbols for Eq. (C1.8-E33).**

**式（C1.8-E33）的符号定义。**

| First individual definition第一项单独定义 | Second individual definition第二项单独定义 |
| --- | --- |
| $\Pi$ is local pressure impulse (Pa s)<br>$\Pi$ 为局部压力冲量（Pa s） | $\boldsymbol x$ is fixed position (m)<br>$\boldsymbol x$ 为固定位置（m） |
| $t$ — Elapsed time (s)<br>$t$ — 经过时间（s） | $t_0$ — Event start time (s)<br>$t_0$ — 事件开始时刻（s） |
| $t_1$ — Event end time (s)<br>$t_1$ — 事件结束时刻（s） | $p$ — Liquid pressure field (Pa)<br>$p$ — 液体压力场（Pa） |
| $p_{\mathrm{ref}}$ — Spatially uniform reference pressure (Pa)<br>$p_{\mathrm{ref}}$ — 空间均匀参考压力（Pa） | $\Delta\boldsymbol u$ is liquid speed change (m s⁻¹)<br>$\Delta\boldsymbol u$ 为液体速度变化（m s⁻¹） |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $U_{\mathrm{column}}$ is the ideal straight-column speed increment (m s⁻¹)<br>$U_{\mathrm{column}}$ 为理想直液柱速度增量（m s⁻¹） |
| $\Pi_0$ is driven-end impulse (Pa s)<br>$\Pi_0$ 为受驱动端冲量（Pa s） | $L$ is column length (m)<br>$L$ 为液柱长度（m） |
| $t_a$ is crossing time (s)<br>$t_a$ 为传播时间（s） | $c$ is sound speed (m s⁻¹)<br>$c$ 为声速（m s⁻¹） |
| $\boldsymbol u$ — liquid velocity (m s⁻¹)<br>$\boldsymbol u$ — 液体速度（m s⁻¹） | $\nu$ — kinematic viscosity (m² s⁻¹)<br>$\nu$ — 运动黏度（m² s⁻¹） |
| $U$ — characteristic speed (m s⁻¹)<br>$U$ — 特征速度（m s⁻¹） | $\tau$ — event duration, $t_1-t_0$ (s)<br>$\tau$ — 事件时长，$t_1-t_0$（s） |
| $z$ — column coordinate, $0\le z\le L$ (m)<br>$z$ — 液柱坐标，$0\le z\le L$（m） | $\Delta u_z$ — axial speed increment (m s⁻¹)<br>$\Delta u_z$ — 轴向速度增量（m s⁻¹） |
| $\nabla$ — spatial gradient operator (m⁻¹)<br>$\nabla$ — 空间梯度算子（m⁻¹） | $\nabla^2$ — spatial Laplacian operator (m⁻²)<br>$\nabla^2$ — 空间拉普拉斯算子（m⁻²） |
| $\nabla\cdot$ — spatial divergence operator (m⁻¹)<br>$\nabla\cdot$ — 空间散度算子（m⁻¹） |  |

**Conventions and conditions.** $\nabla,\nabla^2$ denote spatial gradient and Laplacian; The reduced momentum formula needs a frozen geometry and small omitted impulses; $\ll$ denotes an asymptotic smallness condition.

**约定与条件。** $\nabla,\nabla^2$ 为空间梯度与拉普拉斯；约化动量公式要求冻结几何，且被忽略的冲量项较小；$\ll$ 表示渐近很小条件。

![The impulse benchmark gives an early velocity field, followed by a moving-interface problem.](../assets/figures/c1-e33.svg)

The impulse benchmark gives an early velocity field, followed by a moving-interface problem.

冲量基准给出早期速度场，之后还需解运动界面问题。

**Check and interpretation.** Falsification question: does the observer stay liquid, and are geometry motion, residual impulses and acoustic rise effects small? Report location, duration, geometry and reference pressure with every impulse. Equal scalar peaks cannot determine the spatial gradient.

**检验与解释。** 证伪问题：观察点是否始终位于液体内，几何运动、残余冲量和声学上升效应是否足够小？报告每个冲量时须给出位置、时长、几何及参考压力。相同标量峰值不能确定空间梯度。

Specify driven boundary, outlet, meniscus and receiver geometry. Integrate pressure over time at every location. Equal peaks can have different durations and impulses. Equal scalar impulses can produce different spatial gradients. The gradient sets early velocity. Boundary conditions determine that gradient. A uniform impulse addition causes no acceleration.

规定受驱边界、出口、弯月面及受载几何。在每个位置对压力作时间积分。相同峰值可对应不同时长和冲量，相同标量冲量可产生不同空间梯度。梯度决定早期速度，边界条件决定梯度。均匀增加冲量不产生加速度。

The column gives 0.30 Pa s and 3.0 m s⁻¹. Its separate crossing time is 0.0667 μs. The total duration spans 7.5 acoustic crossings. Its ideal rectangular fronts have zero rise time. Communication at those fronts requires an acoustic model. A finite physical rise time needs the separate C1.7-E30 test. Uniform pressure remains unestablished. Check displacement, convection and viscosity. Then evolve the interface with pressure, stress and contact-line conditions. Focusing follows from that spatial evolution and thermodynamic pressure history. Rapid changes or impact can require compressibility at low bulk speed.

液柱给出 0.30 Pa s 与 3.0 m s⁻¹，传播时间另为 0.0667 μs。总时长包含 7.5 次声穿越。理想矩形波前上升时间为零，波前通信需要声学模型。实际有限上升时间需单独应用 C1.7-E30 检验。均匀压力仍未确立。先检查位移、对流及黏性，再结合压力、应力和接触线条件演化界面。聚焦取决于空间演化及热力学压力历程。快速变化或撞击时，即使总体速率低也可能需要可压缩性。

#### Review criteria

#### 审阅标准

* Distinguishes pressure (Pa), pressure impulse (Pa s), momentum (N s) and crossing time (s), without equating their units.

  区分压力（Pa）、压力冲量（Pa s）、动量（N s）与传播时间（s），不混淆其单位。
* Uses the spatial impulse gradient and actual boundary conditions to explain the initial velocity; a scalar peak is insufficient.

  利用空间冲量梯度与实际边界条件解释初始速度，说明单一峰值不足。
* Explains what the ideal column predicts and what its small-displacement and residual-impulse diagnostics do not guarantee.

  解释理想液柱预测的内容，以及小位移与残余冲量诊断不能保证的内容。
* Identifies the subsequent moving-interface, pressure, phase-transfer and compressibility information needed for a physical jet.

  指出实际射流还需要后续运动界面、压力、相变传质与可压缩性信息。