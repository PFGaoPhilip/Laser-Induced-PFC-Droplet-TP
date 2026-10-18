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

除非另行说明，上标表示幂，粗体表示矢量或张量。π 是无量纲圆周率。梯度、散度与拉普拉斯算子采用笛卡尔定义。时间偏导保持位置固定。每个公式前给出局部符号定义。初始半径为正，允许除以半径。零半径属于模型排除的极限。

**Derivation.** Initial data are prescribed, rather than derived. The radial equation is second order, so radius and signed velocity are separate data. Choose time zero before activation, during growth, or at maximum radius. A stationary initial wall can accelerate. Evaluate the later momentum law at time zero to see why.

**推导。** 初始数据是给定条件，不能作为推导结果。径向方程是二阶方程，半径和带符号速度是独立初值。时间原点可选在激活前、增长中或最大半径处。初始静止的壁面仍能加速。将下文动量方程在零时刻取值即可说明原因。

**Symbols before Eq. (C1-E01).**

**式（C1-E01）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $R$ is the cavity radius (m)<br>$R$ 为空腔半径（m） | $t$ is time (s), with 0 the chosen initial instant<br>$t$ 为时间（s），0 为选定的初始时刻 |
| $R_0$ is its prescribed positive initial value (m)<br>$R_0$ 为给定的正初始半径（m） | $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） |
| $U_0$ its initial value (m s⁻¹)<br>$U_0$ 为其初值（m s⁻¹） | $r$ is radial position (m)<br>$r$ 为径向位置（m） |
| $u$ is radial liquid speed (m s⁻¹)<br>$u$ 为液体径向速度（m s⁻¹） | $p$ is liquid pressure (Pa)<br>$p$ 为液体压力（Pa） |
| $p_\infty$ is prescribed far-field pressure (Pa)<br>$p_\infty$ 为给定远场压力（Pa） |  |

**Conventions and conditions.** The arrow denotes the far-field limit.

**约定与条件。** 箭头表示远场极限。

(C1-E01) · Prescribed initial and boundary conditions / 给定的初始条件与边界条件

$R$ is the cavity radius (m); $t$ is time (s), with 0 the chosen initial instant; $R_0$ is its prescribed positive initial value (m); $\dot R$ is wall speed and $U_0$ its initial value (m s⁻¹); $r$ is radial position (m); $u$ is radial liquid speed (m s⁻¹); $p$ is liquid pressure (Pa); $p_\infty$ is prescribed far-field pressure (Pa). The arrow denotes the far-field limit. $\rho>0$ is carrier density (kg m⁻³); $p_b$ is bubble pressure (Pa); $\sigma$ is constant surface tension (N m⁻¹); $\mu$ is viscosity (Pa s); $\ddot R$ is acceleration (m s⁻²). All pressures share an absolute reference.

$R$ 为空腔半径（m）；$t$ 为时间（s），0 为选定的初始时刻；$R_0$ 为给定的正初始半径（m）；$\dot R$ 为壁面速度，$U_0$ 为其初值（m s⁻¹）；$r$ 为径向位置（m）；$u$ 为液体径向速度（m s⁻¹）；$p$ 为液体压力（Pa）；$p_\infty$ 为给定远场压力（Pa）。箭头表示远场极限。 $\rho>0$ 为载液密度（kg m⁻³）；$p_b$ 为气泡压力（Pa）；$\sigma$ 为常数表面张力（N m⁻¹）；$\mu$ 为黏度（Pa s）；$\ddot R$ 为加速度（m s⁻²）。全部压力采用同一绝对参考值。



$$
\begin{gathered}\begin{aligned}
    \dot R&=dR/dt,\qquad \ddot R=d\dot R/dt,\\
    \rho R_0\ddot R(0)&=p_b(0)-p_\infty(0)-2\sigma/R_0-4\mu U_0/R_0-\tfrac32\rho U_0^2,\\
    U_0=0\quad&\Longrightarrow\quad
    \ddot R(0)=\frac{p_b(0)-p_\infty(0)-2\sigma/R_0}{\rho R_0}.
    \end{aligned}\\[6pt]\begin{gathered}R(0)=R_0>0\\ \dot R(0)=U_0\\ u(r,t)\to0,\quad p(r,t)\to p_\infty(t)\quad(r\to\infty)\end{gathered}\end{gathered}
$$


![The evolving spherical boundary and the prescribed far-field state.](../assets/figures/c1-e01.svg)

The evolving spherical boundary and the prescribed far-field state.

运动球形边界与给定的远场状态。

**Check and interpretation.** Positive initial pressure excess over capillarity gives outward acceleration. Initial zero speed therefore does not imply equilibrium. The acceleration expression has units Pa/(kg m⁻²) = m s⁻².

**检验与解释。** 初始内外压差超过毛细压差时产生向外加速度。因此初速为零不代表平衡。加速度表达式单位为 Pa/(kg m⁻²) = m s⁻²。

## 1.3 Rayleigh–Plesset derivation

## 1.3 Rayleigh–Plesset 方程推导

**Step 1 — Conserve carrier volume.** Radial incompressibility makes volume flux independent of radius. Integrate its radial derivative. Apply equal normal liquid and interface velocities at the wall. Vapor density does not enter this carrier-flow calculation.

**步骤 1——载液体积守恒。** 径向不可压缩流的体积流量与半径无关。积分径向导数，再令壁面处液体法向速度等于界面速度。这一载液流动计算不需要蒸气密度。

**Derivation.** Apply mass conservation to a spherical shell. Constant density reduces it to zero divergence. Integrate in radius at fixed time. The integration function can depend on time. A material cavity wall supplies the final boundary value. Appreciable phase transfer changes that boundary value.

**推导。** 对球壳应用质量守恒。密度为常数时，散度为零。在固定时间对半径积分，积分函数仍可随时间变化。物质空腔壁面提供最终边界值。相变传质显著时，该边界值需要修改。

**Symbols before Eq. (C1-E02).**

**式（C1-E02）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $r\ge R(t)>0$ is radial position (m)<br>$r\ge R(t)>0$ 为径向位置（m） | $R$ is cavity radius (m)<br>$R$ 为空腔半径（m） |
| $t$ is time (s)<br>$t$ 为时间（s） | $u$ is radial carrier velocity (m s⁻¹)<br>$u$ 为载液径向速度（m s⁻¹） |
| $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $C(t)$ is the radius-independent flux factor (m³ s⁻¹), not a material constant<br>$C(t)$ 为与径向位置无关的流量因子（m³ s⁻¹），并非材料常数 |

**Conventions and conditions.** $\partial/\partial r$ differentiates at fixed time; The implication arrows indicate integration and use of the interface condition.

**约定与条件。** $\partial/\partial r$ 表示固定时间下的径向求导；箭头表示积分及应用界面条件。

(C1-E02) · Exact continuity within the spherical model / 球形模型内的精确连续性关系

$r\ge R(t)>0$ is radial position (m); $R$ is cavity radius (m); $t$ is time (s); $u$ is radial carrier velocity (m s⁻¹); $\dot R$ is wall speed (m s⁻¹); $C(t)$ is the radius-independent flux factor (m³ s⁻¹), not a material constant; $\partial/\partial r$ differentiates at fixed time. The implication arrows indicate integration and use of the interface condition. $C(t)$ is the radial volume-flux factor (m³ s⁻¹); $\rho>0$ is constant liquid density (kg m⁻³); $\delta r>0$ is fixed shell thickness (m); $\pi$ is the circle constant; $\partial_r$ holds time fixed; the fixed shell stays liquid; the liquid domain is $r\ge R(t)>0$.

$r\ge R(t)>0$ 为径向位置（m）；$R$ 为空腔半径（m）；$t$ 为时间（s）；$u$ 为载液径向速度（m s⁻¹）；$\dot R$ 为壁面速度（m s⁻¹）；$C(t)$ 为与径向位置无关的流量因子（m³ s⁻¹），并非材料常数；$\partial/\partial r$ 表示固定时间下的径向求导。箭头表示积分及应用界面条件。 $C(t)$ 为径向体积通量因子（m³ s⁻¹）；$\rho>0$ 为常数液体密度（kg m⁻³）；$\delta r>0$ 为固定球壳厚度（m）；$\pi$ 为圆周率；$\partial_r$ 保持时间固定；固定球壳始终属于液体；液体区域为 $r\ge R(t)>0$。



$$
\begin{gathered}\begin{aligned}
    \frac{d}{dt}\left[\rho\frac{4\pi}{3}((r+\delta r)^3-r^3)\right]&=0,\\
    4\pi\rho r^2u(r,t)-4\pi\rho(r+\delta r)^2u(r+\delta r,t)&=0,\\
    \lim_{\delta r\to0}\frac{(r+\delta r)^2u(r+\delta r,t)-r^2u(r,t)}{\delta r}&=\partial_r(r^2u)=0,\\
    0&=\frac{1}{r^2}\frac{\partial(r^2u)}{\partial r},\\
    \frac{\partial(r^2u)}{\partial r}&=0
      \quad\Longrightarrow\quad r^2u=C(t),\\
    u(R,t)&=\dot R\quad\Longrightarrow\quad C(t)=R^2\dot R,\\
    \frac{u(2R,t)}{\dot R}&=\frac{R^2}{(2R)^2}=\frac14\quad(\dot R\ne0).
    \end{aligned}\\[6pt]\begin{gathered}\frac{1}{r^2}\frac{\partial(r^2u)}{\partial r}=0\ \Longrightarrow\ r^2u=C(t)\\ u(R,t)=\dot R\ \Longrightarrow\ C(t)=R^2\dot R\\ u(r,t)=\frac{R^2\dot R}{r^2}\end{gathered}\end{gathered}
$$


![Inverse-square velocity decay places the inertia in the surrounding carrier.](../assets/figures/c1-e02.svg)

Inverse-square velocity decay places the inertia in the surrounding carrier.

速度按距离平方反比衰减，惯性来自周围载液。

**Check and interpretation.** The flux factor divided by radius squared has velocity units. Setting wall speed to zero gives a stationary liquid everywhere.

**检验与解释。** 通量因子除以半径平方具有速度单位。壁面速度为零时，全部液体静止。

**Step 2 — Fix the potential reference.** Integrate velocity from infinity to the observation point. The potential applies outside the cavity. Zero potential at infinity fixes the time-dependent integration constant.

**步骤 2——固定速度势参考值。** 从无穷远积分速度至观察点。速度势适用于空腔外域。令无穷远速度势为零，确定随时间变化的积分常数。

**Derivation.** Purely radial, angle-independent flow has zero curl outside the cavity. The exterior of a sphere is simply connected, so a single-valued potential exists. Integrating velocity introduces an arbitrary time function. Fix that gauge at infinity. The potential packages the velocity field for the momentum integration; it supplies no extra physical degree of freedom.

**推导。** 纯径向且与角度无关的流动在空腔外旋度为零。球外域单连通，因此存在单值速度势。积分速度会引入任意时间函数。用无穷远处的参考值固定该规范。速度势便于积分动量方程，并不增加物理自由度。

**Symbols before Eq. (C1-E03).**

**式（C1-E03）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\phi$ is velocity potential (m² s⁻¹)<br>$\phi$ 为速度势（m² s⁻¹） | $r$ is liquid radial position (m)<br>$r$ 为液体径向位置（m） |
| $R$ cavity radius (m)<br>$R$ 为空腔半径（m） | $t$ is time (s)<br>$t$ 为时间（s） |
| $s$ is a dummy radial integration coordinate (m)<br>$s$ 为径向积分哑变量（m） | $u$ is radial velocity (m s⁻¹)<br>$u$ 为径向速度（m s⁻¹） |
| $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） |  |

**Conventions and conditions.** the integral is an improper integral convergent for $r\ge R>0$; $\partial/\partial r$ is the fixed-time spatial derivative.

**约定与条件。** 该广义积分在 $r\ge R>0$ 时收敛；$\partial/\partial r$ 为固定时间的空间导数。

(C1-E03) · Derived velocity potential / 推导得到的速度势

$\phi$ is velocity potential (m² s⁻¹); $r$ is liquid radial position and $R$ cavity radius (m); $t$ is time (s); $s$ is a dummy radial integration coordinate (m); $u$ is radial velocity (m s⁻¹); $\dot R$ is wall speed (m s⁻¹); the integral is an improper integral convergent for $r\ge R>0$; $\partial/\partial r$ is the fixed-time spatial derivative. $\boldsymbol u$ is velocity (m s⁻¹), $\boldsymbol e_r$ the outward radial unit vector, $\nabla\times$ the curl (inverse-length differentiation), $\boldsymbol0$ the zero vector; $g(t)$ is a potential gauge (m² s⁻¹).

$\phi$ 为速度势（m² s⁻¹）；$r$ 为液体径向位置，$R$ 为空腔半径（m）；$t$ 为时间（s）；$s$ 为径向积分哑变量（m）；$u$ 为径向速度（m s⁻¹）；$\dot R$ 为壁面速度（m s⁻¹）；该广义积分在 $r\ge R>0$ 时收敛；$\partial/\partial r$ 为固定时间的空间导数。 $\boldsymbol u$ 为速度（m s⁻¹），$\boldsymbol e_r$ 为向外径向单位矢量，$\nabla\times$ 为旋度算子（逆长度微分），$\boldsymbol0$ 为零矢量；$g(t)$ 为速度势规范函数（m² s⁻¹）。



$$
\begin{gathered}\begin{aligned}
    \boldsymbol u&=u(r,t)\boldsymbol e_r,\qquad\nabla\times\boldsymbol u=\boldsymbol0,\\
    \partial_r\phi&=u=R^2\dot R/r^2,\\
    \phi(r,t)&=-R^2\dot R/r+g(t),\\
    \phi(\infty,t)&=0\quad\Longrightarrow\quad g(t)=0,\\
    \int_\infty^r s^{-2}\,ds&=[-s^{-1}]_\infty^r=-1/r-0.
    \end{aligned}\\[6pt]\begin{gathered}\phi(r,t)=\int_\infty^r u(s,t)\,ds=R^2\dot R\int_\infty^r s^{-2}\,ds=-\frac{R^2\dot R}{r}\\ \frac{\partial\phi}{\partial r}=u\end{gathered}\end{gathered}
$$


![The potential reference is fixed at infinity before differentiation.](../assets/figures/c1-e03.svg)

The potential reference is fixed at infinity before differentiation.

在求导之前，先固定无穷远处的速度势参考值。

**Check and interpretation.** Spatial differentiation recovers positive outward velocity during expansion. Potential has units length × speed. The construction excludes rotational flow and unresolved vortex sheets.

**检验与解释。** 空间求导恢复膨胀时向外的正速度。速度势单位为长度乘速度。该构造排除了旋转流动和未解析涡片。

**Step 3 — Differentiate at fixed position.** Hold the denominator fixed while differentiating the potential numerator. Then evaluate the result at the moving wall. Differentiating the wall value instead includes a convective contribution.

**步骤 3——在固定位置求导。** 保持速度势分母不变，对分子求时间导数。随后在运动壁面处取值。直接对壁面取值求导会包含对流贡献。

**Derivation.** Differentiate the product in the numerator before evaluating at the wall. For a moving wall value, add the chain-rule displacement term. These operations differ because the observation points differ.

**推导。** 先对分子乘积求导，再在壁面取值。对运动壁面处的取值求导时，需要加入链式法则的位移项。两种操作的观察点不同。

**Symbols before Eq. (C1-E04).**

**式（C1-E04）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\phi$ is velocity potential (m² s⁻¹)<br>$\phi$ 为速度势（m² s⁻¹） | $t$ is time (s)<br>$t$ 为时间（s） |
| $r$ is fixed radial position (m)<br>$r$ 为固定径向位置（m） | $R(t)>0$ is moving cavity radius (m)<br>$R(t)>0$ 为运动空腔半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |

**Conventions and conditions.** vertical bars specify where the derivative is taken or evaluated; $d/dt$ follows the moving wall value; Each derivative has units m² s⁻².

**约定与条件。** 竖线表示求导或取值条件；$d/dt$ 跟随运动壁面的取值；各导数的单位均为 m² s⁻²。

(C1-E04) · Exact Eulerian and moving-point derivatives / 精确的欧拉导数与运动点导数

$\phi$ is velocity potential (m² s⁻¹); $t$ is time (s); $r$ is fixed radial position, $R(t)>0$ is moving cavity radius (m); $\dot R$ and $\ddot R$ are wall speed (m s⁻¹) and acceleration (m s⁻²); vertical bars specify where the derivative is taken or evaluated; $d/dt$ follows the moving wall value. Each derivative has units m² s⁻².

$\phi$ 为速度势（m² s⁻¹）；$t$ 为时间（s）；$r$ 为固定径向位置，$R(t)>0$ 为运动空腔半径（m）；$\dot R$ 与 $\ddot R$ 分别为壁面速度（m s⁻¹）和加速度（m s⁻²）；竖线表示求导或取值条件；$d/dt$ 跟随运动壁面的取值。各导数的单位均为 m² s⁻²。



$$
\begin{gathered}\begin{aligned}
    \frac{d(R^2\dot R)}{dt}&=2R\dot R\dot R+R^2\ddot R,\\
    \frac{d\phi(R(t),t)}{dt}&=\left.\partial_t\phi\right|_{r=R}
       +\dot R\left.\partial_r\phi\right|_{r=R},\\
    &=-(2\dot R^2+R\ddot R)+\dot R\dot R\\
    &=-\dot R^2-R\ddot R.
    \end{aligned}\\[6pt]\begin{gathered}\left.\frac{\partial\phi}{\partial t}\right|_r=-\frac{2R\dot R^2+R^2\ddot R}{r}\\ \left.\frac{\partial\phi}{\partial t}\right|_{r=R}=-(2\dot R^2+R\ddot R)\\ \frac{d\phi(R(t),t)}{dt}=-\dot R^2-R\ddot R\end{gathered}\end{gathered}
$$


![A fixed liquid observation point and a moving interface point have different time derivatives.](../assets/figures/c1-e04.svg)

A fixed liquid observation point and a moving interface point have different time derivatives.

固定液体观察点与运动界面点对应不同的时间导数。

**Check and interpretation.** The moving derivative exceeds the Eulerian wall evaluation by wall speed squared. Both derivatives have energy-per-mass units.

**检验与解释。** 运动导数比欧拉导数的壁面取值大一个壁面速度平方。两者均具有单位质量能量的单位。

**Step 4 — Integrate radial momentum.** The exterior field is irrotational with zero vector Laplacian. Bulk viscous force therefore vanishes. Viscous wall stress and dissipation remain. Reference unsteady Bernoulli to infinity. Insert the fixed-position derivative and wall velocity. Subtracting one half from two gives the inertial coefficient.

**步骤 4——积分径向动量。** 外域流场无旋，矢量拉普拉斯为零，因而体内黏性力为零。壁面黏性应力和耗散仍存在。以无穷远为参考应用非定常伯努利方程。代入固定位置导数与壁面速度。二减去二分之一得到惯性项系数。

**Derivation.** Start from exterior Euler momentum. In this radial field the bulk viscous term vanishes, so this momentum form also applies outside the viscous traction boundary. Irrotationality turns convection into a kinetic-energy gradient. Integrate the resulting zero gradient over the connected liquid domain. The spatial integration function depends on time. The gauge and far-field condition determine it. Then evaluate at the wall.

**推导。** 从外域欧拉动量方程出发。此径向流场的体黏性项为零，因此在黏性牵引边界之外仍可采用该动量形式。无旋条件将对流项写成动能梯度。在连通液体域中积分零梯度，得到随时间变化的空间积分函数。规范与远场条件确定该函数，随后在壁面取值。

**Symbols before Eq. (C1-E05).**

**式（C1-E05）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_l$ is liquid pressure at the wall (Pa)<br>$p_l$ 为壁面液体压力（Pa） | $p_\infty$ far-field pressure (Pa)<br>$p_\infty$ 为远场压力（Pa） |
| $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） | $\phi$ is velocity potential (m² s⁻¹)<br>$\phi$ 为速度势（m² s⁻¹） |
| $t$ is time (s)<br>$t$ 为时间（s） | $r$ is radial position (m)<br>$r$ 为径向位置（m） |
| $R>0$ cavity radius (m)<br>$R>0$ 为空腔半径（m） | $u$ is radial velocity (m s⁻¹)<br>$u$ 为径向速度（m s⁻¹） |
| $\dot R$ wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $\ddot R$ is wall acceleration (m s⁻²)<br>$\ddot R$ 为壁面加速度（m s⁻²） |

**Conventions and conditions.** $\partial_t$ is taken at fixed position before wall evaluation.

**约定与条件。** $\partial_t$ 必须先在固定位置求导，再于壁面取值。

(C1-E05) · Derived inertial pressure / 推导得到的惯性压力

$p_l$ is liquid pressure at the wall and $p_\infty$ far-field pressure (Pa); $\rho>0$ is carrier density (kg m⁻³); $\phi$ is velocity potential (m² s⁻¹); $t$ is time (s); $r$ is radial position and $R>0$ cavity radius (m); $u$ is radial velocity and $\dot R$ wall speed (m s⁻¹); $\ddot R$ is wall acceleration (m s⁻²); $\partial_t$ is taken at fixed position before wall evaluation. $\boldsymbol u=\nabla\phi$ is liquid velocity (m s⁻¹); $\nabla$, $\nabla\cdot$, $\nabla\times$, $\nabla^2$ denote gradient, divergence, curl and vector Laplacian; $u_i,u_j$ are Cartesian velocity components (m s⁻¹), $i,j\in\{1,2,3\}$; $\partial_i,\partial_j$ are coordinate derivatives (m⁻¹); $\sum$ adds over the indicated index; zero vorticity implies $\partial_j u_i=\partial_i u_j$. $|\ |$ is Euclidean magnitude; $B_0(t)$ is the Bernoulli integration function (m² s⁻²); subscript $\infty$ denotes the far-field limit; $p$ is local liquid pressure (Pa). Smooth fields permit exchanging derivatives.

$p_l$ 为壁面液体压力，$p_\infty$ 为远场压力（Pa）；$\rho>0$ 为载液密度（kg m⁻³）；$\phi$ 为速度势（m² s⁻¹）；$t$ 为时间（s）；$r$ 为径向位置，$R>0$ 为空腔半径（m）；$u$ 为径向速度，$\dot R$ 为壁面速度（m s⁻¹）；$\ddot R$ 为壁面加速度（m s⁻²）；$\partial_t$ 必须先在固定位置求导，再于壁面取值。 $\boldsymbol u=\nabla\phi$ 为液体速度（m s⁻¹）；$\nabla$、$\nabla\cdot$、$\nabla\times$、$\nabla^2$ 分别表示梯度、散度、旋度及矢量拉普拉斯；$u_i,u_j$ 为笛卡尔速度分量（m s⁻¹），$i,j\in\{1,2,3\}$；$\partial_i,\partial_j$ 为坐标导数（m⁻¹）；$\sum$ 对指定指标求和；无旋条件给出 $\partial_j u_i=\partial_i u_j$。$|\ |$ 为欧氏模长；$B_0(t)$ 为伯努利积分函数（m² s⁻²）；下标 $\infty$ 表示远场极限；$p$ 为局部液体压力（Pa）。场足够光滑时允许交换导数。



$$
\begin{gathered}\begin{aligned}
    \nabla^2\boldsymbol u&=\nabla(\nabla\cdot\boldsymbol u)-\nabla\times(\nabla\times\boldsymbol u)=\boldsymbol0,\\
    \partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u&=-\nabla p/\rho,\\
    \sum_{j=1}^3u_j\partial_j u_i&=\sum_{j=1}^3u_j\partial_i u_j
       =\partial_i\left(\tfrac12\sum_{j=1}^3u_j^2\right)\quad(i=1,2,3),\\
    \boldsymbol u=\nabla\phi,\quad(\boldsymbol u\cdot\nabla)\boldsymbol u
      &=\nabla(|\boldsymbol u|^2/2),\\
    \nabla\left(\partial_t\phi+|\nabla\phi|^2/2+p/\rho\right)&=\boldsymbol0,\\
    \partial_t\phi+|\nabla\phi|^2/2+p/\rho&=B_0(t),\\
    \phi_\infty=0,\quad\boldsymbol u_\infty=\boldsymbol0
      &\quad\Longrightarrow\quad B_0(t)=p_\infty(t)/\rho,\\
    \partial_t\phi+\tfrac12|\nabla\phi|^2+p/\rho&=p_\infty/\rho,\\
    (p_l-p_\infty)/\rho&=-\partial_t\phi|_{r=R}-\tfrac12\dot R^2.
    \end{aligned}\\[6pt]\begin{aligned}
        (p_l-p_\infty)/\rho&=-\partial_t\phi|_{r=R}-u(R,t)^2/2\\
          &=2\dot R^2+R\ddot R-\dot R^2/2\\
          &=R\ddot R+\tfrac32\dot R^2.
        \end{aligned}\end{gathered}
$$


![Liquid inertia relates the interface pressure to wall acceleration and squared speed.](../assets/figures/c1-e05.svg)

Liquid inertia relates the interface pressure to wall acceleration and squared speed.

液体惯性把界面压力与壁面加速度及速度平方联系起来。

**Check and interpretation.** The coefficient is 2 − 1/2 = 3/2. Constant potential gauge has been fixed; an arbitrary time gauge would change the integration function together with the potential derivative.

**检验与解释。** 系数为 2 − 1/2 = 3/2。速度势规范已经固定；若使用任意时间规范，积分函数会与速度势导数一同改变。

**Step 5 — Balance normal stress.** Expansion gives a negative radial strain rate at the wall. The capillary jump lowers liquid pressure relative to cavity pressure. Balance normal traction with Newtonian viscous stress included.

**步骤 5——平衡法向应力。** 膨胀时壁面径向应变率为负。毛细压差使液体侧压力低于腔内压力。将牛顿黏性应力计入法向牵引平衡。

**Derivation.** Use a normal pointing from liquid into gas. At an inner spherical cavity this normal points inward and curvature is negative. The normal stress jump gives the liquid pressure. Differentiate the radial speed to evaluate the normal viscous traction.

**推导。** 法向从液体指向气体。内球形空腔的该法向向内，曲率为负。法向应力跳跃给出液体压力。对径向速度求导，计算法向黏性牵引。

**Symbols before Eq. (C1-E06).**

**式（C1-E06）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $u$ — Radial liquid velocity (m s⁻¹)<br>$u$ — 液体径向速度（m s⁻¹） | $\dot R$ — Bubble-wall radial velocity (m s⁻¹)<br>$\dot R$ — 气泡壁面径向速度（m s⁻¹） |
| $r$ — Radial liquid position (m)<br>$r$ — 液体径向位置（m） | $R>0$ — Positive cavity radius (m)<br>$R>0$ — 正的空腔半径（m） |
| $p_l$ — Liquid-side pressure at the cavity wall (Pa)<br>$p_l$ — 空腔壁面处的液体侧压力（Pa） | $p_b$ — Spatially uniform bubble pressure (Pa)<br>$p_b$ — 空间均匀的气泡压力（Pa） |
| $\sigma\ge0$ — Nonnegative surface tension (N m⁻¹)<br>$\sigma\ge0$ — 非负表面张力（N m⁻¹） | $\mu\ge0$ — Nonnegative carrier dynamic viscosity (Pa s)<br>$\mu\ge0$ — 非负载液动力黏度（Pa s） |
| $\partial_r u$ — Radial strain rate, evaluated at the wall (s⁻¹)<br>$\partial_r u$ — 在壁面取值的径向应变率（s⁻¹） |  |

**Conventions and conditions.** wall evaluation is performed at $r=R$.

**约定与条件。** 壁面取值在 $r=R$ 处进行。

(C1-E06) · Newtonian stress and capillary boundary condition / 牛顿流体应力与毛细边界条件

$u$ is radial velocity and $\dot R$ wall speed (m s⁻¹); $r$ is radial position and $R>0$ cavity radius (m); $p_l,p_b$ are liquid-side and uniform bubble pressures (Pa); $\sigma\ge0$ is surface tension (N m⁻¹); $\mu\ge0$ is carrier viscosity (Pa s); $\partial_r u$ is radial strain rate (s⁻¹); wall evaluation is performed at $r=R$. $\boldsymbol n$ is the liquid-to-gas unit normal; $\boldsymbol e_r$ is the outward radial unit vector; $\kappa$ is signed curvature (m⁻¹); $\nabla_s\cdot$ is surface divergence and $\nabla\cdot$ volume divergence. Extend the unit normal radially without radial variation, so its normal derivative is zero and both divergences agree at the sphere.

$u$ 为径向速度，$\dot R$ 为壁面速度（m s⁻¹）；$r$ 为径向位置，$R>0$ 为空腔半径（m）；$p_l,p_b$ 分别为液体侧与空间均匀的气泡压力（Pa）；$\sigma\ge0$ 为表面张力（N m⁻¹）；$\mu\ge0$ 为载液黏度（Pa s）；$\partial_r u$ 为径向应变率（s⁻¹）；壁面取值在 $r=R$ 处进行。 $\boldsymbol n$ 为液体指向气体的单位法向；$\boldsymbol e_r$ 为向外径向单位矢量；$\kappa$ 为带符号曲率（m⁻¹）；$\nabla_s\cdot$ 为表面散度，$\nabla\cdot$ 为体散度。将单位法向沿径向作不变延拓，其法向导数为零，因此两种散度在球面一致。



$$
\begin{gathered}\begin{aligned}
    \boldsymbol n&=-\boldsymbol e_r,\qquad
    \nabla_s\cdot\boldsymbol n=\nabla\cdot\boldsymbol n
      =\frac1{r^2}\partial_r(-r^2)=-2/r,\\
    \kappa&=(\nabla_s\cdot\boldsymbol n)|_{r=R}=-2/R,\\
    p_l-p_b&=\sigma\kappa+2\mu\partial_r u|_{r=R},\\
    \partial_r(R^2\dot R r^{-2})&=-2R^2\dot R r^{-3},\\
    2\mu\partial_r u|_{r=R}&=2\mu(-2\dot R/R)=-4\mu\dot R/R.
    \end{aligned}\\[6pt]\begin{gathered}\left.\frac{\partial u}{\partial r}\right|_{r=R}=\left.-\frac{2R^2\dot R}{r^3}\right|_{r=R}=-\frac{2\dot R}{R}\\ p_l=p_b-\frac{2\sigma}{R}+2\mu\left.\frac{\partial u}{\partial r}\right|_{r=R}=p_b-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}\end{gathered}\end{gathered}
$$


![Capillary and viscous stresses act at the interface even when the radial bulk viscous force is zero.](../assets/figures/c1-e06.svg)

Capillary and viscous stresses act at the interface even when the radial bulk viscous force is zero.

即使径向体内黏性力为零，毛细与黏性应力仍作用于界面。

**Check and interpretation.** For a static sphere the gas pressure exceeds liquid pressure by 2σ/R. The viscous pressure reverses with velocity. This local traction calculation remains necessary after deleting the separate tensor-dissipation check.

**检验与解释。** 静止球面气压比液压高 2σ/R。黏性压力随速度反向。删除独立张量耗散检验后，仍需保留此局部牵引计算。

**Step 6 — Combine inertia and traction.** Insert Eq. (C1-E06) into Eq. (C1-E05). Multiply by carrier density to obtain radial momentum balance. Internal pressure still requires a source model. Use aqueous carrier density for the exterior inertia. PFC density describes a different material domain.

**步骤 6——合并惯性与牵引。** 将式（C1-E06）代入式（C1-E05），再乘以载液密度，得到径向动量平衡。内部压力仍需源模型。外域惯性采用水相载液密度。PFC 密度对应另一材料区域。

**Derivation.** Multiply the inertial-pressure relation by density. Replace liquid wall pressure with the traction balance. Collect all pressures with their signs. Divide by positive density and radius when acceleration is required.

**推导。** 将惯性压力关系乘以密度。以牵引平衡替换壁面液压，按符号整理各项压力。需要加速度时，再除以正密度与正半径。

**Symbols before Eq. (C1-E07).**

**式（C1-E07）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） | $R>0$ is cavity radius (m)<br>$R>0$ 为空腔半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） |
| $\sigma$ is constant surface tension (N m⁻¹)<br>$\sigma$ 为常数表面张力（N m⁻¹） | $\mu$ is constant carrier viscosity (Pa s)<br>$\mu$ 为常数载液黏度（Pa s） |

**Conventions and conditions.** Every term is a pressure.

**约定与条件。** 各项均具有压力单位。

(C1-E07) · Rayleigh–Plesset under the declared assumptions / 所述假设下的 Rayleigh–Plesset 方程

$\rho>0$ is carrier density (kg m⁻³); $R>0$ is cavity radius (m); $\dot R,\ddot R$ are wall speed (m s⁻¹) and acceleration (m s⁻²); $p_b,p_\infty$ are bubble and far-field pressures (Pa); $\sigma$ is constant surface tension (N m⁻¹); $\mu$ is constant carrier viscosity (Pa s). Every term is a pressure.

$\rho>0$ 为载液密度（kg m⁻³）；$R>0$ 为空腔半径（m）；$\dot R,\ddot R$ 分别为壁面速度（m s⁻¹）和加速度（m s⁻²）；$p_b,p_\infty$ 为气泡与远场压力（Pa）；$\sigma$ 为常数表面张力（N m⁻¹）；$\mu$ 为常数载液黏度（Pa s）。各项均具有压力单位。



$$
\begin{gathered}\begin{aligned}
    \rho(R\ddot R+\tfrac32\dot R^2)&=p_l-p_\infty,\\
    p_l-p_\infty&=(p_b-2\sigma/R-4\mu\dot R/R)-p_\infty,\\
    \ddot R&=\frac{p_b-p_\infty-2\sigma/R-4\mu\dot R/R}{\rho R}
       -\frac{3\dot R^2}{2R},\\
    \dot R=\ddot R=0&\quad\Longrightarrow\quad p_b-p_\infty=2\sigma/R.
    \end{aligned}\\[6pt]\rho\left(R\ddot R+\frac32\dot R^2\right)=p_b-p_\infty-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}\end{gathered}
$$


![The spherical pressure–inertia balance has a scalar radial state.](../assets/figures/c1-e07.svg)

The spherical pressure–inertia balance has a scalar radial state.

球形压力—惯性平衡只具有标量径向状态。

**Check and interpretation.** The inviscid limit removes the viscous term continuously. At rest capillarity requires positive bubble overpressure. Each original balance term has units Pa.

**检验与解释。** 无黏极限连续消去黏性项。静止时毛细作用要求气泡内过压为正。原平衡各项单位均为 Pa。

Every term has pressure units: density × length × acceleration, tension/radius, and viscosity × speed/radius. At rest, internal overpressure equals the capillary jump. During collapse, the viscous term resists inward motion. To obtain acceleration, also subtract the squared-speed term. This matches the classical spherical model. [[R1]](../reference/sources.html#r1) [[Brennen, Ch. 2]](https://media.library.caltech.edu/CaltechBOOK%3A1995.001/chap2.htm)

各项均为压力：密度 × 长度 × 加速度、张力／半径，以及黏度 × 速度／半径。静止时，内部过压等于毛细压差。塌缩时，黏性项阻碍向内运动。求加速度时还须减去速度平方项。结果与经典球形模型一致。 [[R1]](../reference/sources.html#r1) [[Brennen，第 2 章]](https://media.library.caltech.edu/CaltechBOOK%3A1995.001/chap2.htm)

**Derivation.** This is an adopted ideal-mixture closure. For components sharing temperature and volume, each ideal-gas partial pressure is proportional to its amount. Add component amounts to obtain total pressure. These algebraic steps do not determine evaporation, temperature, or saturation. Real mixtures can require a different equation of state.

**推导。** 这里采用理想混合物闭合。共享温度和体积的各理想气体分压正比于物质的量。将各组分物质的量相加，得到总压力。该代数过程不能确定蒸发、温度或饱和状态。实际混合物可能需要不同状态方程。

**Symbols before Eq. (C1-E08).**

**式（C1-E08）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_b$ is uniform total bubble pressure (Pa)<br>$p_b$ 为空间均匀的气泡总压力（Pa） | $p_{v,\mathrm{PFC}}$ is the PFC-vapor partial pressure (Pa)<br>$p_{v,\mathrm{PFC}}$ 为 PFC 蒸气分压（Pa） |
| $p_{v,w}$ water-vapor partial pressure (Pa)<br>$p_{v,w}$ 为水蒸气分压（Pa） | $p_g$ permanent-gas partial pressure (all Pa)<br>$p_g$ 为非凝结气体分压（均为 Pa） |

**Conventions and conditions.** Subscript $v$ labels vapor, PFC its chemical family; Additivity assumes a gas-mixture pressure description with the stated partial pressures; $w$ water; $g$ noncondensable gas.

**约定与条件。** 下标 $v$ 表示蒸气，PFC 表示该化学物质族；相加关系采用具有上述分压定义的气体混合物压力描述；$w$ 表示水；$g$ 表示非凝结气体。

(C1-E08) · Pressure composition requiring thermodynamic closure / 需要热力学闭合的压力组成关系

$p_b$ is uniform total bubble pressure (Pa); $p_{v,\mathrm{PFC}}$ is the PFC-vapor partial pressure, $p_{v,w}$ water-vapor partial pressure, and $p_g$ permanent-gas partial pressure (all Pa). Subscript $v$ labels vapor, PFC its chemical family, $w$ water, and $g$ noncondensable gas. Additivity assumes a gas-mixture pressure description with the stated partial pressures. $i$ labels PFC vapor, water vapor or permanent gas; $p_i$ is component partial pressure (Pa); $n_i$ is component amount (mol); $V_b>0$ is bubble volume (m³); $\mathcal R$ is the universal gas constant (J mol⁻¹ K⁻¹); $T_b>0$ is common gas temperature (K).

$p_b$ 为空间均匀的气泡总压力（Pa）；$p_{v,\mathrm{PFC}}$ 为 PFC 蒸气分压，$p_{v,w}$ 为水蒸气分压，$p_g$ 为非凝结气体分压（均为 Pa）。下标 $v$ 表示蒸气，PFC 表示该化学物质族，$w$ 表示水，$g$ 表示非凝结气体。相加关系采用具有上述分压定义的气体混合物压力描述。 $i$ 标记 PFC 蒸气、水蒸气或非凝结气体；$p_i$ 为组分分压（Pa）；$n_i$ 为组分物质的量（mol）；$V_b>0$ 为气泡体积（m³）；$\mathcal R$ 为通用气体常数（J mol⁻¹ K⁻¹）；$T_b>0$ 为共同气体温度（K）。



$$
\begin{gathered}\begin{aligned}
    p_iV_b&=n_i\mathcal R T_b\quad (i\in\{v,\mathrm{PFC};v,w;g\}),\\
    p_bV_b&=\left(n_{v,\mathrm{PFC}}+n_{v,w}+n_g\right)\mathcal R T_b,\\
    p_b&=\frac{n_{v,\mathrm{PFC}}\mathcal R T_b}{V_b}
      +\frac{n_{v,w}\mathcal R T_b}{V_b}+\frac{n_g\mathcal R T_b}{V_b}.
    \end{aligned}\\[6pt]p_b=p_{v,\mathrm{PFC}}+p_{v,w}+p_g\end{gathered}
$$


![The mechanical input comes from the evolving contents, not from radius alone.](../assets/figures/c1-e08.svg)

The mechanical input comes from the evolving contents, not from radius alone.

力学输入来自不断变化的气泡内容物，不能仅由半径决定。

**Check and interpretation.** Pressure × volume has energy units. A vanishing component amount removes its partial pressure. Missing: component mass-transfer rates, energy balance and appropriate phase equilibrium or kinetics.

**检验与解释。** 压力乘体积具有能量单位。某组分物质的量为零时，其分压为零。缺少：组分传质率、能量平衡以及适用的相平衡或相变动力学。

A fixed-mass polytropic gas control requires its stated thermal assumptions. Evaporation and condensation exchange mass and latent heat. A permanent-gas closure omits those exchanges. Uniform internal pressure requires communication faster than state evolution. Chapter 2 supplies a finite-inventory closure. [[R5]](../reference/sources.html#r5)

固定质量多方气体对照要求满足其热学假设。蒸发和凝结交换质量与潜热，非凝结气体闭合省略了这些交换。均匀内压要求内部通信快于状态演化。第二章给出有限物质量闭合。 [[R5]](../reference/sources.html#r5)

## 1.4 Carrier energy balance

## 1.4 载液能量平衡

**Step 7 — Integrate exterior kinetic energy.** Square the velocity in Eq. (C1-E02). Multiply by the spherical volume element and integrate. The inverse-square integral converges over the infinite exterior. Carrier liquid beyond the wall supplies the moving inertia.

**步骤 7——积分外域动能。** 将式（C1-E02）的速度平方，乘以球形体积微元并积分。平方反比积分在无限外域收敛。壁面之外的载液构成运动惯性。

**Derivation.** At a fixed instant, integrate energy over the whole exterior. Angular integration supplies the shell area. The lower bound is the current interface. Replace speed by the continuity solution, cancel radial powers and evaluate the improper integral before differentiating the result.

**推导。** 在固定时刻，对整个外域积分能量。角向积分给出球壳面积。下限为当前界面。用连续性解替换速度，约去径向幂，再计算广义积分，最后才对结果求导。

**Symbols before Eq. (C1-E09).**

**式（C1-E09）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $K_l$ is exterior liquid kinetic energy (J)<br>$K_l$ 为外部液体动能（J） | $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） |
| $u$ is radial liquid speed (m s⁻¹)<br>$u$ 为径向液体速度（m s⁻¹） | $\dot R$ wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） |
| $t$ is time (s)<br>$t$ 为时间（s） | $R>0$ is cavity radius (m)<br>$R>0$ 为空腔半径（m） |
| $r$ the integration radius (m)<br>$r$ 为积分半径（m） | $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** $4\pi r^2dr$ is the spherical volume element (m³); endpoint brackets mean upper minus lower evaluation.

**约定与条件。** $4\pi r^2dr$ 为球形体积元（m³）；端点方括号表示上限取值减下限取值。

(C1-E09) · Exact kinetic-energy integral in the spherical model / 球形模型内的精确动能积分

$K_l$ is exterior liquid kinetic energy (J); $\rho$ is carrier density (kg m⁻³); $u$ is radial liquid speed and $\dot R$ wall speed (m s⁻¹); $t$ is time (s); $R>0$ is cavity radius, $r$ the integration radius (m); $\pi$ is the circle constant; $4\pi r^2dr$ is the spherical volume element (m³); endpoint brackets mean upper minus lower evaluation. $dV$ is shell volume (m³); $\theta\in[0,\pi]$ and $\psi\in[0,2\pi]$ are polar and azimuthal angles (dimensionless radians); $b>R$ is a finite outer cutoff (m).

$K_l$ 为外部液体动能（J）；$\rho$ 为载液密度（kg m⁻³）；$u$ 为径向液体速度，$\dot R$ 为壁面速度（m s⁻¹）；$t$ 为时间（s）；$R>0$ 为空腔半径，$r$ 为积分半径（m）；$\pi$ 为圆周率；$4\pi r^2dr$ 为球形体积元（m³）；端点方括号表示上限取值减下限取值。 $dV$ 为体积元（m³）；$\theta\in[0,\pi]$ 与 $\psi\in[0,2\pi]$ 为极角与方位角（无量纲弧度）；$b>R$ 为有限外截断半径（m）。



$$
\begin{gathered}\begin{aligned}
    dV&=r^2\sin\theta\,d\theta\,d\psi\,dr,\\
    \int_0^{2\pi}\!d\psi\int_0^\pi\!\sin\theta\,d\theta&=2\pi[-\cos\theta]_0^\pi=4\pi,\\
    u^2&=R^4\dot R^2/r^4,\qquad r^2/r^4=r^{-2},\\
    \int_R^b r^{-2}\,dr&=-1/b+1/R\ \longrightarrow\ 1/R\quad(b\to\infty),\\
    2\pi\rho R^4\dot R^2/R&=2\pi\rho R^3\dot R^2.
    \end{aligned}\\[6pt]\begin{aligned}K_l&=\int_R^\infty\frac12\rho u(r,t)^2\,4\pi r^2\,dr\\&=2\pi\rho R^4\dot R^2\int_R^\infty r^{-2}\,dr\\&=2\pi\rho R^4\dot R^2\left[-\frac1r\right]_R^\infty=2\pi\rho R^3\dot R^2.\end{aligned}\end{gathered}
$$


![Exterior shells contribute finite kinetic energy even in an infinite domain.](../assets/figures/c1-e09.svg)

Exterior shells contribute finite kinetic energy even in an infinite domain.

即使外域无限，外部液壳贡献的总动能仍有限。

**Check and interpretation.** Density × radius cubed × speed squared gives joules. Infinite volume causes no divergence because speed decays sufficiently fast. A finite outer wall changes the velocity boundary-value problem.

**检验与解释。** 密度乘半径三次方乘速度平方得到焦耳。速度衰减足够快，因此无限体积不造成发散。有限外壁会改变速度边值问题。

**Step 8 — Differentiate stored energy.** Apply the product rule to radius and squared speed. Differentiate cavity volume and interface energy separately. The surface-energy derivative assumes constant surface tension.

**步骤 8——对储存能量求导。** 对半径与速度平方应用乘积法则。分别对空腔体积和界面能求导。表面能导数假设表面张力恒定。

**Derivation.** The integrated kinetic energy already contains the moving lower boundary through radius. Apply the product rule to that expression. Differentiating a fixed-limit integral while ignoring the moving boundary would miss part of this rate.

**推导。** 积分后的动能已通过半径包含运动下边界。对该表达式应用乘积法则。若将其作为固定积分限求导并忽略运动边界，就会遗漏部分变化率。

**Symbols before Eq. (C1-E10).**

**式（C1-E10）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $K_l$ — Carrier kinetic energy (J)<br>$K_l$ — 载液动能（J） | $E_\sigma$ — Interfacial energy (J)<br>$E_\sigma$ — 界面能（J） |
| $t$ is time (s)<br>$t$ 为时间（s） | $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） |
| $R$ is radius (m)<br>$R$ 为半径（m） | $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） |
| $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） | $V_b$ is cavity volume (m³)<br>$V_b$ 为空腔体积（m³） |
| $\dot V_b$ its time derivative (m³ s⁻¹)<br>$\dot V_b$ 为其时间导数（m³ s⁻¹） | $\sigma$ is constant surface tension (N m⁻¹)<br>$\sigma$ 为常数表面张力（N m⁻¹） |
| $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |  |

**Conventions and conditions.** Energy derivatives are powers (W).

**约定与条件。** 能量的时间导数为功率（W）。

(C1-E10) · Exact product-rule derivatives / 乘积求导法则的精确应用

$K_l,E_\sigma$ are liquid kinetic and interface energies (J); $t$ is time (s); $\rho$ is carrier density (kg m⁻³); $R$ is radius (m); $\dot R,\ddot R$ are speed (m s⁻¹) and acceleration (m s⁻²); $V_b$ is cavity volume (m³), $\dot V_b$ its time derivative (m³ s⁻¹); $\sigma$ is constant surface tension (N m⁻¹); $\pi$ is the circle constant. Energy derivatives are powers (W).

$K_l,E_\sigma$ 分别为液体动能与界面能（J）；$t$ 为时间（s）；$\rho$ 为载液密度（kg m⁻³）；$R$ 为半径（m）；$\dot R,\ddot R$ 分别为速度（m s⁻¹）与加速度（m s⁻²）；$V_b$ 为空腔体积（m³），$\dot V_b$ 为其时间导数（m³ s⁻¹）；$\sigma$ 为常数表面张力（N m⁻¹）；$\pi$ 为圆周率。能量的时间导数为功率（W）。



$$
\begin{gathered}\begin{aligned}
    \frac{d(R^3\dot R^2)}{dt}&=\frac{dR^3}{dt}\dot R^2+R^3\frac{d\dot R^2}{dt},\\
    \frac{dR^3}{dt}&=3R^2\dot R,\qquad\frac{d\dot R^2}{dt}=2\dot R\ddot R,\\
    2\pi\rho(3R^2\dot R^3+2R^3\dot R\ddot R)
      &=4\pi\rho R^2\dot R(\tfrac32\dot R^2+R\ddot R),\\
    \frac{d(4\pi\sigma R^2)}{dt}&=4\pi\sigma(2R\dot R).
    \end{aligned}\\[6pt]\begin{aligned}\frac{dK_l}{dt}&=2\pi\rho\left(3R^2\dot R^3+2R^3\dot R\ddot R\right)=4\pi R^2\dot R\,\rho\left(R\ddot R+\frac32\dot R^2\right),\\V_b&=\frac{4\pi R^3}{3},\qquad \dot V_b=4\pi R^2\dot R,\\E_\sigma&=4\pi\sigma R^2,\qquad \frac{dE_\sigma}{dt}=8\pi\sigma R\dot R.\end{aligned}\end{gathered}
$$


![Volume work couples kinetic storage, interface storage and dissipation.](../assets/figures/c1-e10.svg)

Volume work couples kinetic storage, interface storage and dissipation.

体积功耦合动能储存、界面能储存与耗散。

**Check and interpretation.** Energy rates have units watts. At a turning point both rates vanish instantaneously, even when acceleration is nonzero. Variable surface tension would add another product-rule term.

**检验与解释。** 能量变化率单位为瓦。转折点两种能量变化率瞬时为零，即使加速度非零。表面张力随时间变化时，需要增加乘积求导项。

**Step 9 — Convert momentum balance into power balance.** Multiply by cavity volume rate. The inertial term becomes Eq. (C1-E10), first row. The capillary term equals minus the surface-energy derivative. Squared speed makes viscous power nonpositive in both motion directions.

**步骤 9——将动量平衡转为功率平衡。** 乘以空腔体积变化率。惯性项成为式（C1-E10）第一行。毛细项等于表面能导数的负值。速度平方使两种运动方向的黏性功率均不为正。

**Derivation.** Multiply the radial pressure balance by signed cavity volume rate. Identify the inertial term using the preceding product rule. Expand the capillary and viscous products separately. Move surface-energy storage to the left. This derives mechanical power accounting without restoring the deleted strain-tensor calculation.

**推导。** 将径向压力平衡乘以带符号空腔体积变化率。用前式乘积法则识别惯性项。分别展开毛细项和黏性项，再将表面能储存移至左侧。由此推导机械功率平衡，无须恢复已删除的应变张量计算。

**Symbols before Eq. (C1-E11).**

**式（C1-E11）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $t$ is time (s)<br>$t$ 为时间（s） | $K_l$ — Carrier kinetic energy (J)<br>$K_l$ — 载液动能（J） |
| $E_\sigma$ — Interfacial energy (J)<br>$E_\sigma$ — 界面能（J） | $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） |
| $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） | $\dot V_b$ is cavity volume rate (m³ s⁻¹)<br>$\dot V_b$ 为空腔体积变化率（m³ s⁻¹） |
| $\mu\ge0$ is carrier viscosity (Pa s)<br>$\mu\ge0$ 为载液黏度（Pa s） | $R>0$ is cavity radius (m)<br>$R>0$ 为空腔半径（m） |
| $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** The nonnegative term is dissipated power (W).

**约定与条件。** 非负项是耗散功率（W）。

(C1-E11) · Derived mechanical-energy balance / 推导得到的机械能平衡

$t$ is time (s); $K_l,E_\sigma$ are kinetic and interface energies (J); $p_b,p_\infty$ are bubble and far-field pressures (Pa); $\dot V_b$ is cavity volume rate (m³ s⁻¹); $\mu\ge0$ is carrier viscosity (Pa s); $R>0$ is cavity radius (m); $\dot R$ is wall speed (m s⁻¹); $\pi$ is the circle constant. The nonnegative term is dissipated power (W).

$t$ 为时间（s）；$K_l,E_\sigma$ 为动能与界面能（J）；$p_b,p_\infty$ 为气泡与远场压力（Pa）；$\dot V_b$ 为空腔体积变化率（m³ s⁻¹）；$\mu\ge0$ 为载液黏度（Pa s）；$R>0$ 为空腔半径（m）；$\dot R$ 为壁面速度（m s⁻¹）；$\pi$ 为圆周率。非负项是耗散功率（W）。



$$
\begin{gathered}\begin{aligned}
    \frac{dK_l}{dt}&=(p_b-p_\infty-2\sigma/R-4\mu\dot R/R)(4\pi R^2\dot R),\\
    (-2\sigma/R)(4\pi R^2\dot R)&=-8\pi\sigma R\dot R=-dE_\sigma/dt,\\
    (-4\mu\dot R/R)(4\pi R^2\dot R)&=-16\pi\mu R\dot R^2,\\
    \frac{dK_l}{dt}+\frac{dE_\sigma}{dt}
      &=(p_b-p_\infty)\dot V_b-16\pi\mu R\dot R^2.
    \end{aligned}\\[6pt]\begin{gathered}\frac{d}{dt}(K_l+E_\sigma)=(p_b-p_\infty)\dot V_b-16\pi\mu R\dot R^2\\ 16\pi\mu R\dot R^2\ge0\end{gathered}\end{gathered}
$$


![The pressure source supplies mechanical work; focusing cannot create extra energy.](../assets/figures/c1-e11.svg)

The pressure source supplies mechanical work; focusing cannot create extra energy.

压力源提供机械功；聚焦不能产生额外能量。

**Check and interpretation.** Expansion against excess internal pressure and collapse under excess external pressure both allow positive work. Dissipation is nonnegative for either velocity sign. Missing: laser absorption, internal energy, latent heat and acoustic radiation in a complete energy budget.

**检验与解释。** 内压较高时膨胀与外压较高时塌缩都可得到正功。两种速度符号下耗散均非负。完整能量预算还缺少：激光吸收、内能、潜热与声辐射。

Confinement can redirect liquid and change its energy budget. It may store elastic energy or increase dissipation. Predicting carrier motion requires the thermodynamic source and mechanical receiver. Incident pulse energy alone leaves that budget unresolved.

约束可改变液体方向及能量分配，也可能储存弹性能或增加耗散。预测载液运动需同时计算热力学源与力学受载体系。仅知入射脉冲能量，能量分配仍未确定。

## 1.5 Ideal collapse time and coefficient

## 1.5 理想塌缩时间与系数

**Step 10 — Specify the ideal collapse problem.** Start at maximum radius with zero wall speed. Far-field and vapor pressures are constant with positive collapse difference. Omit tension, viscosity, permanent gas and liquid compressibility. Thermal and phase dynamics are excluded assumptions. Their smallness for PFC remains unestablished. A hot vapor-rich cavity can still expand.

**步骤 10——规定理想塌缩问题。** 从最大半径及零壁面速度开始。远场压力与蒸气压恒定，塌缩压差为正。忽略张力、黏性、非凝结气体及液体可压缩性。热学与相变动力学被模型排除。它们对 PFC 是否足够小尚未确立。高温蒸气丰富的空腔仍可膨胀。

**Derivation.** Define an ideal control: constant vapor pressure, constant exterior pressure, zero gas, zero viscosity and zero surface tension. These assumptions reduce the previously derived momentum law. Start at maximum radius with zero speed. Evaluate acceleration there to select the inward trajectory.

**推导。** 定义理想对照：蒸气压和外压恒定，忽略气体、黏度及表面张力。用这些假设约化前述动量方程。初始位于最大半径且速度为零。在此处计算加速度，选择向内轨迹。

**Symbols before Eq. (C1-E12).**

**式（C1-E12）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Delta p_c>0$ is constant collapse-driving pressure (Pa)<br>$\Delta p_c>0$ 为常数塌缩驱动压差（Pa） | $p_\infty$ — Constant Far-field absolute pressure (Pa)<br>$p_\infty$ — 恒定的远场绝对压力（Pa） |
| $p_v$ — Stipulated constant vapor pressure (Pa)<br>$p_v$ — 假定恒定蒸气压（Pa） | $t=0$ is maximum-radius time (s)<br>$t=0$ 为最大半径时刻（s） |
| $R>0$ — Instantaneous cavity radius (m)<br>$R>0$ — 瞬时空腔半径（m） | $R_{\max}>0$ — Radius at the start of ideal collapse (m)<br>$R_{\max}>0$ — 理想塌缩开始时的半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |
| $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） |  |(C1-E12) · Idealized collapse initial-value problem / 理想化塌缩的初值问题

$\Delta p_c>0$ is constant collapse-driving pressure (Pa); $p_\infty,p_v$ are constant far-field and vapor pressures (Pa); $t=0$ is maximum-radius time (s); $R>0$ and $R_{\max}>0$ are instantaneous and maximum radii (m); $\dot R,\ddot R$ are speed (m s⁻¹) and acceleration (m s⁻²); $\rho>0$ is carrier density (kg m⁻³). $\mu$ is viscosity (Pa s) and $\sigma$ surface tension (N m⁻¹), both set to zero in this control; $p_b$ is bubble pressure (Pa).

$\Delta p_c>0$ 为常数塌缩驱动压差（Pa）；$p_\infty,p_v$ 为常数远场压力与蒸气压（Pa）；$t=0$ 为最大半径时刻（s）；$R>0$ 与 $R_{\max}>0$ 分别为当前与最大半径（m）；$\dot R,\ddot R$ 为速度（m s⁻¹）与加速度（m s⁻²）；$\rho>0$ 为载液密度（kg m⁻³）。 $\mu$ 为黏度（Pa s），$\sigma$ 为表面张力（N m⁻¹），在此对照中均置零；$p_b$ 为气泡压力（Pa）。



$$
\begin{gathered}\begin{aligned}
    p_b&=p_v,\quad \mu=\sigma=0,\quad p_v-p_\infty=-\Delta p_c,\\
    \rho(R\ddot R+\tfrac32\dot R^2)&=-\Delta p_c,\\
    R_{\max}\ddot R(0)&=-\Delta p_c/\rho,\\
    \ddot R(0)&=-\frac{\Delta p_c}{\rho R_{\max}}<0.
    \end{aligned}\\[6pt]\begin{gathered}\Delta p_c=p_\infty-p_v>0\\ R(0)=R_{\max},\quad \dot R(0)=0\\ R\ddot R+\frac32\dot R^2=-\frac{\Delta p_c}{\rho}\end{gathered}\end{gathered}
$$


![The ideal control begins at rest and excludes the mechanisms that arrest real collapse.](../assets/figures/c1-e12.svg)

The ideal control begins at rest and excludes the mechanisms that arrest real collapse.

理想对照从静止开始，并排除了阻止实际塌缩的机制。

**Check and interpretation.** Pressure deficit produces inward acceleration. This hypothetical control omits physical collapse arrest and evolving PFC vapor production.

**检验与解释。** 压差产生向内加速度。此假想对照省略了实际塌缩终止机制和随时间演化的 PFC 蒸气生成。

**Step 11 — Use radius on the collapse branch.** Negative initial acceleration starts decreasing radius. Define squared speed as a radius function. Away from the turning point, apply the chain rule. Cancel the nonzero speed there. Extend the relation continuously to the initial endpoint. Multiply by radius cubed to form an exact derivative.

**步骤 11——在塌缩分支上以半径为自变量。** 负初始加速度使半径开始减小。将速度平方定义为半径函数。在转折点之外应用链式法则，再约去非零速度。连续延拓关系至初始端点。乘以半径三次方，形成完整导数。

**Derivation.** On the open inward branch speed is nonzero, so divide the chain rule by speed. Divide the reduced momentum equation by positive radius. Solve the integrating-factor equation explicitly. The initial turning point is handled by continuity rather than division by zero.

**推导。** 向内分支内部速度非零，因此链式法则可除以速度。将约化动量方程除以正半径。显式求解积分因子方程。初始转折点通过连续延拓处理，不能除以零。

**Symbols before Eq. (C1-E13).**

**式（C1-E13）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $y(R)$ is squared wall speed (m² s⁻²)<br>$y(R)$ 为壁面速度平方（m² s⁻²） | $R\in(0,R_{\max})$ is decreasing radius (m)<br>$R\in(0,R_{\max})$ 为递减半径（m） |
| $t$ is time (s)<br>$t$ 为时间（s） | $\dot R\ne0$ — Wall radial velocity (m s⁻¹)<br>$\dot R\ne0$ — 壁面径向速度（m s⁻¹） |
| $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） | $\Delta p_c$ is positive pressure difference (Pa)<br>$\Delta p_c$ 为正压差（Pa） |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） |  |

**Conventions and conditions.** $d/dR$ and $d/dt$ are ordinary derivatives on the monotonic branch; Radius powers are the integrating factor, not derivatives.

**约定与条件。** $d/dR$ 与 $d/dt$ 为单调分支上的普通导数；半径幂构成积分因子，并非导数。

(C1-E13) · Exact chain rule and integrating factor / 精确的链式法则与积分因子

$y(R)$ is squared wall speed (m² s⁻²); $R\in(0,R_{\max})$ is decreasing radius (m); $t$ is time (s); $\dot R\ne0$ and $\ddot R$ are speed (m s⁻¹) and acceleration (m s⁻²); $\Delta p_c$ is positive pressure difference (Pa); $\rho$ is carrier density (kg m⁻³); $d/dR$ and $d/dt$ are ordinary derivatives on the monotonic branch. Radius powers are the integrating factor, not derivatives. $y'=dy/dR$ has units m s⁻²; $I>0$ is a dimensionless integrating factor normalized by $I(R_{\max})=1$, $I'=dI/dR$ (m⁻¹); $s>0$ is a dummy radius (m); $\ln$ and $\exp$ are natural logarithm and exponential with dimensionless arguments.

$y(R)$ 为壁面速度平方（m² s⁻²）；$R\in(0,R_{\max})$ 为递减半径（m）；$t$ 为时间（s）；$\dot R\ne0$ 与 $\ddot R$ 为速度（m s⁻¹）与加速度（m s⁻²）；$\Delta p_c$ 为正压差（Pa）；$\rho$ 为载液密度（kg m⁻³）；$d/dR$ 与 $d/dt$ 为单调分支上的普通导数。半径幂构成积分因子，并非导数。 $y'=dy/dR$ 的单位为 m s⁻²；$I>0$ 为无量纲积分因子，采用 $I(R_{\max})=1$ 归一化，$I'=dI/dR$（m⁻¹）；$s>0$ 为积分哑半径（m）；$\ln$ 与 $\exp$ 为自然对数和指数，自变量无量纲。



$$
\begin{gathered}\begin{aligned}
    R(\tfrac12 y')+\tfrac32 y&=-\Delta p_c/\rho,\\
    y'+3y/R&=-2\Delta p_c/(\rho R),\\
    I'/I&=3/R,\quad I(R_{\max})=1,\\
    \ln I(R)-\ln I(R_{\max})&=\int_{R_{\max}}^R\frac{3}{s}\,ds
       =3[\ln(s/R_{\max})]_{R_{\max}}^R=3\ln(R/R_{\max}),\\
    \ln I(R)&=3\ln(R/R_{\max}),\quad
       I(R)=\exp(3\ln(R/R_{\max}))=(R/R_{\max})^3,\\
    (R^3y)'&=R^3y'+3R^2y.
    \end{aligned}\\[6pt]\begin{aligned}y(R)&=\dot R^2,\qquad \frac{dy}{dt}=\frac{dy}{dR}\dot R=2\dot R\ddot R\quad\Longrightarrow\quad\ddot R=\frac12\frac{dy}{dR},\\\frac{dy}{dR}+\frac{3y}{R}&=-\frac{2\Delta p_c}{\rho R},\\\frac{d(R^3y)}{dR}&=R^3\frac{dy}{dR}+3R^2y=-\frac{2\Delta p_c}{\rho}R^2.\end{aligned}\end{gathered}
$$


![The monotonic collapse branch allows radius to replace time in the first integration.](../assets/figures/c1-e13.svg)

The monotonic collapse branch allows radius to replace time in the first integration.

单调塌缩分支允许在第一次积分中以半径取代时间。

**Check and interpretation.** Multiplying by the constant maximum-radius cube gives the equivalent integrating factor used below. Every momentum term retains acceleration-per-length-compatible units before integration.

**检验与解释。** 乘以常数最大半径三次方，即得到下文使用的等价积分因子。积分前各动量项保持一致量纲。

**Derivation.** Integrate the exact radial derivative from the initial maximum to the present radius. Apply zero initial squared speed. Evaluate the cubic antiderivative. Divide by positive radius cubed. Taking a square root gives two mathematical signs; inward motion selects the negative one.

**推导。** 从初始最大半径积分完整径向导数至当前半径。代入初始速度平方为零，计算三次方原函数，再除以正半径三次方。开平方得到两个数学符号，向内运动选择负号。

**Symbols before Eq. (C1-E14).**

**式（C1-E14）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $R\in(0,R_{\max}]$ — Instantaneous cavity radius (m)<br>$R\in(0,R_{\max}]$ — 瞬时空腔半径（m） | $R_{\max}$ — Radius at the start of ideal collapse (m)<br>$R_{\max}$ — 理想塌缩开始时的半径（m） |
| $y$ is squared speed (m² s⁻²)<br>$y$ 为速度平方（m² s⁻²） | $s$ is dummy radius (m)<br>$s$ 为积分哑半径（m） |
| $\Delta p_c>0$ is collapse pressure (Pa)<br>$\Delta p_c>0$ 为塌缩压差（Pa） | $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） |
| $\dot R\le0$ is inward wall velocity (m s⁻¹)<br>$\dot R\le0$ 为向内壁面速度（m s⁻¹） |  |

**Conventions and conditions.** The square root denotes the nonnegative root; its prefixed minus sign selects collapse.

**约定与条件。** 根号表示非负平方根；前置负号选择塌缩分支。

(C1-E14) · Integrated speed with initial constant and branch / 含初始积分常数与分支选择的速度积分解

$R\in(0,R_{\max}]$ and $R_{\max}$ are current and maximum radii (m); $y$ is squared speed (m² s⁻²); $s$ is dummy radius (m); $\Delta p_c>0$ is collapse pressure (Pa); $\rho>0$ is carrier density (kg m⁻³); $\dot R\le0$ is inward wall velocity (m s⁻¹). The square root denotes the nonnegative root; its prefixed minus sign selects collapse.

$R\in(0,R_{\max}]$ 与 $R_{\max}$ 分别为当前与最大半径（m）；$y$ 为速度平方（m² s⁻²）；$s$ 为积分哑半径（m）；$\Delta p_c>0$ 为塌缩压差（Pa）；$\rho>0$ 为载液密度（kg m⁻³）；$\dot R\le0$ 为向内壁面速度（m s⁻¹）。根号表示非负平方根；前置负号选择塌缩分支。



$$
\begin{gathered}\begin{aligned}
    \int_{R_{\max}}^R\frac{d(s^3y)}{ds}\,ds
      &=-\frac{2\Delta p_c}{\rho}\left[\frac{s^3}{3}\right]_{R_{\max}}^R,\\
    R^3y(R)&=\frac{2\Delta p_c}{3\rho}(R_{\max}^3-R^3),\\
    y(R)&=\frac{2\Delta p_c}{3\rho}\left(\frac{R_{\max}^3}{R^3}-1\right)\ge0,\\
    \dot R&=\pm\sqrt{y(R)},\qquad\dot R<0\ \text{during collapse}.
    \end{aligned}\\[6pt]\begin{aligned}R^3y(R)-R_{\max}^3y(R_{\max})&=-\frac{2\Delta p_c}{\rho}\int_{R_{\max}}^R s^2\,ds=-\frac{2\Delta p_c}{3\rho}(R^3-R_{\max}^3),\\y(R_{\max})&=0,\qquad \dot R=-\sqrt{\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}{R}\right)^3-1\right]}.\end{aligned}\end{gathered}
$$


![The initial condition fixes the integration constant and the inward sign fixes the branch.](../assets/figures/c1-e14.svg)

The initial condition fixes the integration constant and the inward sign fixes the branch.

初值确定积分常数，向内的符号确定解分支。

**Check and interpretation.** At maximum radius the speed is zero. For smaller positive radius the squared speed is positive. The speed scale is the square root of pressure divided by density.

**检验与解释。** 最大半径处速度为零。半径减小且保持正值时，速度平方为正。速度尺度为压差除以密度的平方根。

**Step 12 — Separate scale from trajectory.** Integrate reciprocal inward speed from maximum radius to zero. Normalize radius by its maximum. Every case in this ideal family shares the resulting dimensionless integral. That common integral establishes the time proportionality.

**步骤 12——分离尺度与轨迹。** 从最大半径至零积分向内速度的倒数。用最大半径归一化半径。此理想模型族各情形共有所得无量纲积分。该共同积分确立时间的比例关系。

**Derivation.** For the inward branch, time increases while radius decreases. The negative reciprocal speed reverses the integration bounds. Normalize radius and include its differential. Factor the cubic ratio before taking the positive square root.

**推导。** 向内分支上，时间增加而半径减小。速度倒数的负号反转积分上下限。将半径无量纲化并包含微分变换。先整理三次方比值，再取正平方根。

**Symbols before Eq. (C1-E15).**

**式（C1-E15）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $t_c$ is ideal collapse time (s)<br>$t_c$ 为理想塌缩时间（s） | $R$ is radius (m)<br>$R$ 为半径（m） |
| $R_{\max}$ its maximum (m)<br>$R_{\max}$ 为其最大值（m） | $\dot R<0$ is inward velocity (m s⁻¹)<br>$\dot R<0$ 为向内速度（m s⁻¹） |
| $\rho$ is density (kg m⁻³)<br>$\rho$ 为密度（kg m⁻³） | $\Delta p_c>0$ is pressure difference (Pa)<br>$\Delta p_c>0$ 为压差（Pa） |
| $x=R/R_{\max}\in[0,1]$ is dimensionless radius<br>$x=R/R_{\max}\in[0,1]$ 为无量纲半径 | $C_t$ is the dimensionless time coefficient<br>$C_t$ 为无量纲时间系数 |
| $dx$ — Dimensionless-radius integration measure (dimensionless)<br>$dx$ — 无量纲半径积分微元（无量纲） | $dR$ — Radius integration measure (m)<br>$dR$ — 半径积分微元（m） |

**Conventions and conditions.** definite integrals follow the collapse branch.

**约定与条件。** 定积分沿塌缩分支进行。

(C1-E15) · Exact separation and nondimensionalization / 精确的变量分离与无量纲化

$t_c$ is ideal collapse time (s); $R$ is radius and $R_{\max}$ its maximum (m); $\dot R<0$ is inward velocity (m s⁻¹); $\rho$ is density (kg m⁻³); $\Delta p_c>0$ is pressure difference (Pa); $x=R/R_{\max}\in[0,1]$ is dimensionless radius; $C_t$ is the dimensionless time coefficient; definite integrals follow the collapse branch. $dx$ and $dR$ denote integration measures.

$t_c$ 为理想塌缩时间（s）；$R$ 为半径，$R_{\max}$ 为其最大值（m）；$\dot R<0$ 为向内速度（m s⁻¹）；$\rho$ 为密度（kg m⁻³）；$\Delta p_c>0$ 为压差（Pa）；$x=R/R_{\max}\in[0,1]$ 为无量纲半径；$C_t$ 为无量纲时间系数；定积分沿塌缩分支进行。$dx$ 与 $dR$ 表示积分测度。



$$
\begin{gathered}\begin{aligned}
    dt&=dR/\dot R,\qquad
    \frac1{\dot R}=-\sqrt{\frac{3\rho}{2\Delta p_c}}\frac1{\sqrt{(R_{\max}/R)^3-1}},\\
    (R_{\max}/R)^3-1&=x^{-3}-1=(1-x^3)/x^3,\\
    \frac{dR}{\sqrt{(R_{\max}/R)^3-1}}
      &=R_{\max}\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx,\\
    -\int_1^0\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx
      &=\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx.
    \end{aligned}\\[6pt]\begin{aligned}t_c&=\int_{R_{\max}}^0\frac{dR}{\dot R}=\sqrt{\frac{3\rho}{2\Delta p_c}}\int_0^{R_{\max}}\frac{dR}{\sqrt{(R_{\max}/R)^3-1}},\\x&=\frac{R}{R_{\max}},\qquad dR=R_{\max}dx,\\t_c&=R_{\max}\sqrt{\frac{\rho}{\Delta p_c}}\ C_t,\qquad C_t=\sqrt{\frac32}\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx.\end{aligned}\end{gathered}
$$


![The endpoint singularity is integrable, so the model has a finite collapse time.](../assets/figures/c1-e15.svg)

The endpoint singularity is integrable, so the model has a finite collapse time.

端点奇异性可积，因此该模型具有有限塌缩时间。

**Check and interpretation.** The scale Rmax × sqrt(density/pressure) has units seconds. The integral is improper at its endpoints; its finite value is the formal zero-radius model time.

**检验与解释。** 尺度 Rmax × sqrt(密度/压差) 的单位为秒。积分在端点为广义积分；其有限值是模型到零半径的形式时间。

**Step 13 — Evaluate the coefficient.** Substitute the cube of normalized radius, including its Jacobian. The exponents combine as one half minus two thirds. The result is minus one sixth. Both beta-function arguments are positive, so the integral converges. The coefficient agrees with the published Rayleigh factor. [[R1]](../reference/sources.html#r1) [[R3]](../reference/sources.html#r3)

**步骤 13——计算系数。** 用无量纲半径的三次方换元，并计入雅可比因子。指数由二分之一减去三分之二，得到负六分之一。贝塔函数两个参数均为正，积分收敛。系数与文献瑞利因子一致。 [[R1]](../reference/sources.html#r1) [[R3]](../reference/sources.html#r3)

**Derivation.** Cube the normalized radius. Carry both the numerator exponent and Jacobian into the transformed integral. Match each exponent to the beta-function definition. Inspect both endpoints before evaluating the coefficient.

**推导。** 对无量纲半径取三次方换元。将分子指数与雅可比因子一同代入积分。逐项将指数与贝塔函数定义匹配。计算系数前先检查两个端点。

**Symbols before Eq. (C1-E16).**

**式（C1-E16）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $x$ — Dimensionless radius divided by the maximum radius (dimensionless)<br>$x$ — 半径除以最大半径所得无量纲量（无量纲） | $q=x^3$ — Dimensionless substitution variable equal to the cube of the radius fraction (dimensionless)<br>$q=x^3$ — 等于半径比例立方的无量纲换元变量（无量纲） |
| $C_t$ is the dimensionless collapse-time coefficient<br>$C_t$ 为无量纲塌缩时间系数 | $B(a,b)$ is the beta function, defined by the displayed convergent integral (dimensionless)<br>$B(a,b)$ 为贝塔函数，由公式中的收敛积分定义（无量纲） |
| $a$ — Positive first argument of the beta function (dimensionless)<br>$a$ — 贝塔函数的正第一参数（无量纲） | $b$ — Positive second argument of the beta function (dimensionless)<br>$b$ — 贝塔函数的正第二参数（无量纲） |
| $dx$ — Dimensionless-radius integration measure (dimensionless)<br>$dx$ — 无量纲半径积分微元（无量纲） | $dq$ — Dimensionless substitution integration measure (dimensionless)<br>$dq$ — 无量纲换元积分微元（无量纲） |

**Conventions and conditions.** The numeral 6 inside the root is a dimensionless constant; the ellipsis indicates decimal continuation; $x,q\in[0,1]$ and $q=x^3$ define the substitution domain..

**约定与条件。** 根号中的数字 6 为无量纲常数；省略号表示后续小数；$x,q\in[0,1]$ 且 $q=x^3$ 确定换元范围。。

(C1-E16) · Evaluated beta-function coefficient / 通过贝塔函数计算的系数

$x$ and $q=x^3$ are dimensionless radius and substitution variables on [0,1]; $C_t$ is the dimensionless collapse-time coefficient; $B(a,b)$ is the beta function, defined by the displayed convergent integral; $a,b$ are positive dimensionless arguments; $dx,dq$ are integration measures. The numeral 6 inside the root is a dimensionless constant; the ellipsis indicates decimal continuation.

$x$ 与 $q=x^3$ 分别为区间 [0,1] 上的无量纲半径与换元变量；$C_t$ 为无量纲塌缩时间系数；$B(a,b)$ 为贝塔函数，由公式中的收敛积分定义；$a,b$ 为正的无量纲参数；$dx,dq$ 为积分测度。根号中的数字 6 为无量纲常数；省略号表示后续小数。



$$
\begin{gathered}\begin{aligned}
    x^{3/2}&=(q^{1/3})^{3/2}=q^{1/2},\\
    x^{3/2}\,dx&=q^{1/2}\tfrac13q^{-2/3}\,dq=\tfrac13q^{-1/6}\,dq,\\
    \sqrt{3/2}/3&=1/\sqrt6,\quad a-1=-1/6\Rightarrow a=5/6,\\
    b-1&=-1/2\Rightarrow b=1/2,\\
    C_t&=B(5/6,1/2)/\sqrt6=0.9146813565\ldots .
    \end{aligned}\\[6pt]\begin{aligned}q&=x^3,\quad x=q^{1/3},\quad dx=\frac13q^{-2/3}\,dq,\\C_t&=\frac{1}{\sqrt6}\int_0^1q^{-1/6}(1-q)^{-1/2}\,dq=\frac{1}{\sqrt6}B\left(\frac56,\frac12\right)=0.9146813565\ldots,\\B(a,b)&=\int_0^1q^{a-1}(1-q)^{b-1}\,dq\quad(a>0,b>0).\end{aligned}\end{gathered}
$$


![The change of variables exposes the beta integral that fixes the numerical coefficient.](../assets/figures/c1-e16.svg)

The change of variables exposes the beta integral that fixes the numerical coefficient.

换元揭示贝塔积分，从而确定数值系数。

**Check and interpretation.** Both endpoint powers exceed −1, ensuring integrability. This dimensionless coefficient follows from the trajectory integral. It is independent of material fitting.

**检验与解释。** 两个端点幂指数均大于 −1，因而可积。此无量纲系数来自轨迹积分，不依赖材料拟合。

**Step 14 — Check pressure work.** Insert Eq. (C1-E14) into the kinetic-energy integral. The result equals work from the lost cavity volume. Energy vanishes at maximum radius and becomes positive during collapse. This checks the integration constant and sign.

**步骤 14——检验压力功。** 将式（C1-E14）代入动能积分。结果等于空腔体积减少产生的压力功。最大半径处动能为零，塌缩过程中为正。这检验了积分常数与符号。

**Derivation.** Insert squared speed into the exterior kinetic-energy result. Cancel density, distribute radius cubed and remove its denominator. Independently integrate pressure work over decreasing cavity volume. Differentiate the result to check its power and sign.

**推导。** 将速度平方代入外域动能结果。约去密度，将半径三次方分配至括号内并约去分母。独立对减小的空腔体积积分压力功。再对结果求导，检验功率和符号。

**Symbols before Eq. (C1-E17).**

**式（C1-E17）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $K_l$ is carrier kinetic energy (J)<br>$K_l$ 为载液动能（J） | $E_B$ the maximum-volume pressure-work scale (J)<br>$E_B$ 为最大体积的压力功尺度（J） |
| $R\in(0,R_{\max}]$ — Instantaneous cavity radius (m)<br>$R\in(0,R_{\max}]$ — 瞬时空腔半径（m） | $R_{\max}$ — Radius at the start of ideal collapse (m)<br>$R_{\max}$ — 理想塌缩开始时的半径（m） |
| $\rho$ is density (kg m⁻³)<br>$\rho$ 为密度（kg m⁻³） | $\Delta p_c$ is constant positive pressure difference (Pa)<br>$\Delta p_c$ 为常数正压差（Pa） |
| $V_{\max}$ is maximum cavity volume (m³)<br>$V_{\max}$ 为最大空腔体积（m³） | $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |
| $K_l/E_B$ is dimensionless and this control has zero viscous and capillary losses<br>$K_l/E_B$ 无量纲，此对照模型的黏性与毛细损失为零 |  |(C1-E17) · Independent pressure-work conservation check / 独立的压力功守恒检验

$K_l$ is carrier kinetic energy, $E_B$ the maximum-volume pressure-work scale (J); $R\in(0,R_{\max}]$ and $R_{\max}$ are radii (m); $\rho$ is density (kg m⁻³); $\Delta p_c$ is constant positive pressure difference (Pa); $V_{\max}$ is maximum cavity volume (m³); $\pi$ is the circle constant. $K_l/E_B$ is dimensionless and this control has zero viscous and capillary losses. $V_b=4\pi R^3/3$ is cavity volume (m³); $V$ is the dummy volume variable (m³); $t$ is time (s), $\dot R$ wall speed (m s⁻¹).

$K_l$ 为载液动能，$E_B$ 为最大体积的压力功尺度（J）；$R\in(0,R_{\max}]$ 与 $R_{\max}$ 为半径（m）；$\rho$ 为密度（kg m⁻³）；$\Delta p_c$ 为常数正压差（Pa）；$V_{\max}$ 为最大空腔体积（m³）；$\pi$ 为圆周率。$K_l/E_B$ 无量纲，此对照模型的黏性与毛细损失为零。 $V_b=4\pi R^3/3$ 为空腔体积（m³）；$V$ 为积分哑体积（m³）；$t$ 为时间（s），$\dot R$ 为壁面速度（m s⁻¹）。



$$
\begin{gathered}\begin{aligned}
    (2\pi\rho)\frac{2\Delta p_c}{3\rho}&=4\pi\Delta p_c/3,\\
    R^3\left(\frac{R_{\max}^3}{R^3}-1\right)&=R_{\max}^3-R^3,\\
    K_l&=\int_{V_{\max}}^{V_b}(-\Delta p_c)\,dV
      =\Delta p_c(V_{\max}-V_b),\\
    \frac{dK_l}{dt}&=-\Delta p_c\,4\pi R^2\dot R>0\quad(\dot R<0),\\
    K_l/E_B&=(R_{\max}^3-R^3)/R_{\max}^3=1-(R/R_{\max})^3.
    \end{aligned}\\[6pt]\begin{aligned}K_l(R)&=2\pi\rho R^3\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}R\right)^3-1\right]=\frac{4\pi}{3}\Delta p_c(R_{\max}^3-R^3),\\E_B&=\Delta p_cV_{\max}=\frac{4\pi}{3}\Delta p_cR_{\max}^3,\qquad \frac{K_l}{E_B}=1-\left(\frac R{R_{\max}}\right)^3.\end{aligned}\end{gathered}
$$


![The Rayleigh speed solution and pressure-work balance agree exactly.](../assets/figures/c1-e17.svg)

The Rayleigh speed solution and pressure-work balance agree exactly.

瑞利速度解与压力功平衡严格一致。

**Check and interpretation.** Pressure times displaced volume has joule units. Zero initial energy and positive growth during collapse agree with the mechanical power balance. Radial liquid energy does not specify jet energy.

**检验与解释。** 压差乘置换体积具有焦耳单位。初始动能为零，塌缩时动能增加，与机械功率平衡一致。径向液体动能不能确定射流动能。

### Worked example: 30 μm cavity

### 计算示例：30 μm 空腔

Prescribe maximum radius 30 μm, density 1000 kg m⁻³, and collapse pressure 100 kPa. These teaching inputs are not measured PFC properties. Substitute SI values before converting units. At half radius, the cubic ratio is eight. Subtracting one leaves seven.

规定最大半径 30 μm、密度 1000 kg m⁻³、塌缩压差 100 kPa。这些教学输入并非 PFC 实测物性。先代入 SI 数值，再换算单位。一半半径处的三次方比值为八，减去一得到七。

**Derivation.** Convert every teaching input to SI units. Compute the common pressure–density factor and cubic radius before inserting them into time, energy and speed formulas. The half-radius energy fraction follows from the cube of one half.

**推导。** 将全部教学输入换为 SI 单位。先计算共同压差密度因子及半径三次方，再代入时间、能量和速度公式。半径减半时的能量比例来自二分之一的三次方。

**Symbols before Eq. (C1-E18).**

**式（C1-E18）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $t_c$ is collapse time (s)<br>$t_c$ 为塌缩时间（s） | $E_B$ pressure-work scale (J)<br>$E_B$ 为压力功尺度（J） |
| $K_l$ carrier kinetic energy (J)<br>$K_l$ 为载液动能（J） | $R$ current radius (m)<br>$R$ 为当前半径（m） |
| $R_{\max}=30\times10^{-6}$ m maximum radius<br>$R_{\max}=30\times10^{-6}$ m 为最大半径 | $\dot R$ is signed wall speed (m s⁻¹)<br>$\dot R$ 为带符号壁面速度（m s⁻¹） |
| $\Delta p_c=100\times10^3$ — Positive ideal-collapse pressure difference (Pa)<br>$\Delta p_c=100\times10^3$ — 正的理想塌缩压差（Pa） | $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |
| $\rho=1000$ — Substituted carrier density (kg m⁻³)<br>$\rho=1000$ — 代入的载液密度（kg m⁻³） |  |

**Conventions and conditions.** s, J, μs and nJ mean seconds, joules, microseconds and nanojoules; the vertical bar specifies half-radius evaluation.

**约定与条件。** s、J、μs 与 nJ 分别为秒、焦耳、微秒与纳焦耳；竖线表示在一半半径处取值。

(C1-E18) · Declared teaching calculation / 采用明确给定参数的教学计算

$t_c$ is collapse time (s), $E_B$ pressure-work scale (J), $K_l$ carrier kinetic energy (J), $R$ current radius and $R_{\max}=30\times10^{-6}$ m maximum radius; $\dot R$ is signed wall speed (m s⁻¹). Substituted inputs are $\rho=1000$ kg m⁻³ and $\Delta p_c=100\times10^3$ Pa. $\pi$ is the circle constant; s, J, μs and nJ mean seconds, joules, microseconds and nanojoules; the vertical bar specifies half-radius evaluation.

$t_c$ 为塌缩时间（s），$E_B$ 为压力功尺度（J），$K_l$ 为载液动能（J），$R$ 为当前半径，$R_{\max}=30\times10^{-6}$ m 为最大半径；$\dot R$ 为带符号壁面速度（m s⁻¹）。代入输入为 $\rho=1000$ kg m⁻³ 与 $\Delta p_c=100\times10^3$ Pa。$\pi$ 为圆周率；s、J、μs 与 nJ 分别为秒、焦耳、微秒与纳焦耳；竖线表示在一半半径处取值。



$$
\begin{gathered}\begin{aligned}
    R_{\max}&=30\ \mu\mathrm m=30\times10^{-6}\ \mathrm m,\quad
      \Delta p_c=100\ \mathrm{kPa}=10^5\ \mathrm{Pa},\\
    \sqrt{\rho/\Delta p_c}&=\sqrt{1000/10^5}=0.1\ \mathrm{s\,m^{-1}},\\
    R_{\max}^3&=27\times10^{-15}\ \mathrm{m^3},\\
    t_c&=0.9146813565(30\times10^{-6})(0.1)\ \mathrm s
      =2.7440440695\times10^{-6}\ \mathrm s,\\
    E_B&=(4\pi/3)(10^5)(27\times10^{-15})\ \mathrm J
      =1.1309733553\times10^{-8}\ \mathrm J,\\
    (R_{\max}/R)^3-1&=2^3-1=7,\quad K_l/E_B=1-(1/2)^3=7/8.
    \end{aligned}\\[6pt]\begin{aligned}t_c&=0.9146813565(30\times10^{-6})\sqrt{\frac{1000}{100\times10^3}}\ \mathrm s=2.74404\ \mu\mathrm s,\\E_B&=\frac{4\pi}{3}(100\times10^3)(30\times10^{-6})^3\ \mathrm J=11.3097\ \mathrm{nJ},\\\dot R\big|_{R=R_{\max}/2}&=-\sqrt{\frac{2(100\times10^3)}{3(1000)}(8-1)}\ \mathrm{m\,s^{-1}}=-21.6025\ \mathrm{m\,s^{-1}},\\K_l\big|_{R=R_{\max}/2}&=\frac78E_B=9.89602\ \mathrm{nJ}.\end{aligned}\end{gathered}
$$


![The original numerical control is preserved with its energy and branch checks.](../assets/figures/c1-e18.svg)

The original numerical control is preserved with its energy and branch checks.

保留原始数值对照，并补充能量与解分支检验。

**Check and interpretation.** One microsecond is 10⁻⁶ seconds; one nanojoule is 10⁻⁹ joules. The final values below agree with independent quadrature and pressure-work checks. These inputs are illustrative.

**检验与解释。** 一微秒为 10⁻⁶ 秒；一纳焦为 10⁻⁹ 焦。下列结果与独立积分及压力功检验一致。这些输入是教学示例。

Length × √(density/pressure) has units of seconds. Doubling radius doubles collapse time and increases work eightfold. Quadrupling pressure halves time and doubles speed at fixed radius fraction. The dimensionless initial-value problem, and hence its coefficient, stays unchanged. Gas cushioning, varying vapor pressure or confinement can change that problem.

长度 × √（密度／压力）的单位为秒。半径加倍使塌缩时间加倍、压力功增至八倍。压差增至四倍使时间减半、固定半径比例处速率加倍。无量纲初值问题及其系数保持不变。气体缓冲、变化蒸气压或约束可改变该问题。

The zero-radius limit gives finite energy and divergent wall speed. Physical maximum speed: Not established. Missing: compressibility, internal pressure, heat and mass transfer, molecular scales and interface distortion. The next equation locates a chosen Mach threshold on the ideal trajectory. It supplies a diagnostic, not a collapse-arrest law.

零半径极限给出有限能量与发散壁面速率。实际最大速率尚未确立。缺失：可压缩性、内部压力、传热传质、分子尺度及界面变形。下一式定位理想轨迹上的所选马赫数阈值。它是诊断条件，并非塌缩终止规律。

**Derivation.** Use the ideal inward speed as a diagnostic trajectory. Square the nonnegative Mach magnitude, set a selected positive threshold, and solve for the positive radius fraction. The threshold marks a chosen modeling cutoff. It does not predict the physical collapse endpoint.

**推导。** 将理想向内速度用作诊断轨迹。对非负马赫数取平方，令其等于选定的正阈值，再解出正半径比例。阈值标记选定的模型截止条件，并不预测实际塌缩终点。

**Symbols before Eq. (C1-E19).**

**式（C1-E19）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $M_w$ is wall Mach number (dimensionless)<br>$M_w$ 为壁面马赫数（无量纲） | $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） |
| $c>0$ is stipulated carrier sound speed (m s⁻¹)<br>$c>0$ 为给定载液声速（m s⁻¹） | $M_*>0$ is a selected diagnostic Mach value (dimensionless)<br>$M_*>0$ 为选择的诊断马赫值（无量纲） |
| $x_M=R_M/R_{\max}$ is the radius fraction when $M_w=M_*$ (dimensionless)<br>$x_M=R_M/R_{\max}$ 为 $M_w=M_*$ 时的半径比例（无量纲） | $R_M$ — Cavity radius at the selected Mach value (m)<br>$R_M$ — 选定马赫数处的空腔半径（m） |
| $R_{\max}$ — Radius at the start of ideal collapse (m)<br>$R_{\max}$ — 理想塌缩开始时的半径（m） | $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） |
| $\Delta p_c$ is positive collapse pressure (Pa)<br>$\Delta p_c$ 为正塌缩压差（Pa） |  |

**Conventions and conditions.** absolute bars denote magnitude; The number uses the previous teaching density and pressure.

**约定与条件。** 绝对值符号表示大小；数值使用前述教学密度与压差。

(C1-E19) · Ideal-trajectory diagnostic, not a physical limit / 理想轨迹的诊断指标，而非物理极限

$M_w$ is wall Mach number (dimensionless); $\dot R$ is wall speed (m s⁻¹); absolute bars denote magnitude; $c>0$ is stipulated carrier sound speed (m s⁻¹); $M_*>0$ is a selected diagnostic Mach value; $x_M=R_M/R_{\max}$ is the radius fraction when $M_w=M_*$; $R_M,R_{\max}$ are radii (m); $\rho$ is carrier density (kg m⁻³); $\Delta p_c$ is positive collapse pressure (Pa). The number uses the previous teaching density and pressure. $x$ is normalized radius (dimensionless); $R_M=x_MR_{\max}$ is diagnostic radius (m); numerical inputs are the previous teaching density and pressure, with $c=1500$ m s⁻¹ and chosen $M_*=0.1$.

$M_w$ 为壁面马赫数（无量纲）；$\dot R$ 为壁面速度（m s⁻¹）；绝对值符号表示大小；$c>0$ 为给定载液声速（m s⁻¹）；$M_*>0$ 为选择的诊断马赫值；$x_M=R_M/R_{\max}$ 为 $M_w=M_*$ 时的半径比例；$R_M,R_{\max}$ 为半径（m）；$\rho$ 为载液密度（kg m⁻³）；$\Delta p_c$ 为正塌缩压差（Pa）。数值使用前述教学密度与压差。 $x$ 为无量纲半径；$R_M=x_MR_{\max}$ 为诊断半径（m）；数值输入采用前述教学密度和压差，并取 $c=1500$ m s⁻¹、选定 $M_*=0.1$。



$$
\begin{gathered}\begin{aligned}
    x&=R/R_{\max},\qquad M_w^2=\frac{2\Delta p_c}{3\rho c^2}(x^{-3}-1),\\
    M_w=M_*&\quad\Longrightarrow\quad
      \frac{3\rho c^2M_*^2}{2\Delta p_c}=x_M^{-3}-1,\\
    x_M^{-3}&=1+\frac{3\rho c^2M_*^2}{2\Delta p_c},\\
    x_M&=\left[1+\frac{3(1000)(1500)^2(0.1)^2}{2(10^5)}\right]^{-1/3}\\
       &=338.5^{-1/3}=0.1434874,\\
    R_M&=(30\ \mu\mathrm m)(0.1434874)=4.30462\ \mu\mathrm m.
    \end{aligned}\\[6pt]\begin{gathered}M_w=\frac{|\dot R|}{c}\\ x_M=\left[1+\frac{3\rho c^2M_*^2}{2\Delta p_c}\right]^{-1/3}\\ M_*=0.1,\ c=1500\ \mathrm{m\,s^{-1}}\ \Longrightarrow\ x_M=0.143487\end{gathered}\end{gathered}
$$


![A Mach diagnostic exposes the shrinking validity range of incompressible collapse.](../assets/figures/c1-e19.svg)

A Mach diagnostic exposes the shrinking validity range of incompressible collapse.

马赫数诊断揭示不可压缩塌缩模型的适用范围不断缩小。

**Check and interpretation.** The bracket is dimensionless and exceeds one, so the diagnostic radius lies below maximum radius. As threshold tends to zero, its radius approaches the starting radius. Singular zero radius remains outside physical validity.

**检验与解释。** 括号无量纲且大于一，因此诊断半径小于最大半径。阈值趋于零时，诊断半径趋于初始最大半径。奇异零半径仍超出物理适用范围。

## 1.6 Pressure impulse and direction

## 1.6 压力冲量与方向

**Step 15 — Define pressure impulse.** Integrate local pressure relative to a spatially uniform reference over time. Pressure impulse has units Pa s. Its spatial gradient drives liquid velocity change. Acoustic crossing time has units s. The cited short-event model motivates the following integration and approximation. [[R2]](../reference/sources.html#r2)

**步骤 15——定义压力冲量。** 对局部压力相对于空间均匀参考值作时间积分。压力冲量单位为 Pa s，其空间梯度驱动液体速度变化。声传播时间单位为 s。所引短事件模型提供以下积分与近似的依据。 [[R2]](../reference/sources.html#r2)

**Derivation.** Place a pressure observer at a fixed liquid point throughout the event. Integrate over time there. Subtract a spatially uniform reference pressure. A separate area integral converts pressure impulse into mechanical impulse when the surface is fixed. For moving surfaces, pressure, normal and area must remain inside the time integral.

**推导。** 在整个事件中始终属于液体的固定点放置压力观察者。在该处对时间积分，并减去空间均匀的参考压力。表面固定时，另作面积积分可将压力冲量转为机械冲量。表面运动时，压力、法向和面积均须保留在时间积分内。

**Symbols before Eq. (C1-E20).**

**式（C1-E20）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol x$ is fixed liquid position (m)<br>$\boldsymbol x$ 为固定液体位置（m） | $\Pi$ is pressure impulse (Pa s)<br>$\Pi$ 为压力冲量（Pa s） |
| $p$ is local pressure (Pa)<br>$p$ 为局部压力（Pa） | $p_{\mathrm{ref}}$ a spatially uniform reference (Pa)<br>$p_{\mathrm{ref}}$ 为空间均匀参考压力（Pa） |
| $t$ is time (s)<br>$t$ 为时间（s） | $t_0$ — Event start time (s)<br>$t_0$ — 事件开始时刻（s） |
| $t_1$ — Event end time (s)<br>$t_1$ — 事件结束时刻（s） | $\tau$ is event duration (s)<br>$\tau$ 为持续时间（s） |

**Conventions and conditions.** Square brackets on $\Pi$ denote units, not endpoint evaluation; The integral is at fixed position in a liquid domain whose displacement will be assessed below.

**约定与条件。** $\Pi$ 的方括号表示单位，而非端点取值；积分在固定位置进行，液体区域的位移将在下文评估。

(C1-E20) · Definition of local pressure impulse / 局部压力冲量的定义

$\boldsymbol x$ is fixed liquid position (m); $\Pi$ is pressure impulse (Pa s); $p$ is local pressure and $p_{\mathrm{ref}}$ a spatially uniform reference (Pa); $t$ is time and $t_0,t_1$ event endpoints (s); $\tau$ is event duration (s). Square brackets on $\Pi$ denote units, not endpoint evaluation. The integral is at fixed position in a liquid domain whose displacement will be assessed below. $q$ is gauge pressure (Pa); $N$ is a positive integer subdivision count; $k$ labels a time sample $t_k$ (s); $\Delta t$ is time-step width (s); $\boldsymbol J_p$ is gauge-pressure mechanical impulse on a liquid control volume (N s); $S(t)$ is its surface, $\boldsymbol n$ its outward unit normal, and $dA$ an area element (m²); brackets denote units. Fixed-surface reduction requires fixed orientation and all sampled points remaining liquid.

$\boldsymbol x$ 为固定液体位置（m）；$\Pi$ 为压力冲量（Pa s）；$p$ 为局部压力，$p_{\mathrm{ref}}$ 为空间均匀参考压力（Pa）；$t$ 为时间，$t_0,t_1$ 为事件端点（s）；$\tau$ 为持续时间（s）。$\Pi$ 的方括号表示单位，而非端点取值。积分在固定位置进行，液体区域的位移将在下文评估。 $q$ 为表压（Pa）；$N$ 为正整数分段数；$k$ 标记采样时间 $t_k$（s）；$\Delta t$ 为时间段宽度（s）；$\boldsymbol J_p$ 为作用于液体控制体的表压机械冲量（N s）；$S(t)$ 为其表面，$\boldsymbol n$ 为向外单位法向，$dA$ 为面积元（m²）；方括号表示单位。固定表面约化要求方向固定且全部采样点始终位于液体中。



$$
\begin{gathered}\begin{aligned}
    q(\boldsymbol x,t)&=p(\boldsymbol x,t)-p_{\mathrm{ref}}(t),\\
    \Pi(\boldsymbol x)&=\lim_{N\to\infty}\sum_{k=1}^Nq(\boldsymbol x,t_k)\Delta t,
       \quad\Delta t=(t_1-t_0)/N,\\
    \boldsymbol J_p&=-\int_{t_0}^{t_1}\int_{S(t)}q\boldsymbol n\,dA\,dt,\\
    S(t)=S\quad&\Longrightarrow\quad\boldsymbol J_p=-\int_S\Pi\boldsymbol n\,dA,\\
    [\boldsymbol J_p]&=\mathrm{Pa\,s\,m^2}=\mathrm{N\,s},\qquad[\Pi]=\mathrm{Pa\,s}.
    \end{aligned}\\[6pt]\begin{gathered}\Pi(\boldsymbol x)=\int_{t_0}^{t_1}\left[p(\boldsymbol x,t)-p_{\mathrm{ref}}(t)\right]dt\\ \tau=t_1-t_0>0\\ [\Pi]=\mathrm{Pa\,s}\end{gathered}\end{gathered}
$$


![Impulse combines duration and amplitude at each liquid position.](../assets/figures/c1-e20.svg)

Impulse combines duration and amplitude at each liquid position.

压力冲量在每个液体位置组合压力幅值与持续时间。

**Check and interpretation.** A constant reference shifts the local pressure integral without changing its spatial gradient. Absolute contact loads require the actual exterior pressure and viscous traction. A point crossed by an interface needs a moving-domain formulation.

**检验与解释。** 常数参考压力可改变局部压力积分，但不改变其空间梯度。绝对接触载荷需要实际外部压力和黏性牵引。若界面穿过观察点，则需要运动域表述。

**Derivation.** Divide constant-density Navier–Stokes by density. Integrate every term between the same fixed times at the same fixed position. The fundamental theorem gives the velocity difference. Smoothness and a common liquid domain permit gradient–integral exchange. The spatially uniform reference has zero gradient.

**推导。** 将常密度 Navier–Stokes 方程除以密度。在相同固定位置、相同时间上下限内逐项积分。微积分基本定理给出速度差。场足够光滑且积分期间均属于液体域时，允许交换梯度与积分。空间均匀的参考压力梯度为零。

**Symbols before Eq. (C1-E21).**

**式（C1-E21）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Delta\boldsymbol u$ is fixed-position velocity change (m s⁻¹)<br>$\Delta\boldsymbol u$ 为固定位置速度变化（m s⁻¹） | $\boldsymbol u$ velocity (m s⁻¹)<br>$\boldsymbol u$ 为速度（m s⁻¹） |
| $\Pi$ is pressure impulse (Pa s)<br>$\Pi$ 为压力冲量（Pa s） | $\rho$ is constant density (kg m⁻³)<br>$\rho$ 为常数密度（kg m⁻³） |
| $\mu$ is viscosity (Pa s)<br>$\mu$ 为黏度（Pa s） | $\nu$ is kinematic viscosity (m² s⁻¹)<br>$\nu$ 为运动黏度（m² s⁻¹） |
| $t_0$ — Event start time (s)<br>$t_0$ — 事件开始时刻（s） | $t_1$ — Event end time (s)<br>$t_1$ — 事件结束时刻（s） |
| $t$ — Elapsed time (s)<br>$t$ — 经过时间（s） | $\boldsymbol x$ is fixed position (m)<br>$\boldsymbol x$ 为固定位置（m） |

**Conventions and conditions.** $\nabla$ is spatial gradient (m⁻¹), $\nabla^2$ the vector Laplacian (m⁻²); the dot is a true vector contraction in convective acceleration, not an equation separator.

**约定与条件。** $\nabla$ 为空间梯度（m⁻¹），$\nabla^2$ 为矢量拉普拉斯（m⁻²）；圆点是对流加速度中的真正矢量缩并，并非公式分隔符。

(C1-E21) · Exact fixed-position integrated incompressible momentum / 固定位置处不可压缩动量方程的精确时间积分

$\Delta\boldsymbol u$ is fixed-position velocity change and $\boldsymbol u$ velocity (m s⁻¹); $\Pi$ is pressure impulse (Pa s); $\rho$ is constant density (kg m⁻³); $\mu$ is viscosity (Pa s); $\nu$ is kinematic viscosity (m² s⁻¹); $t_0,t_1,t$ are times (s); $\boldsymbol x$ is fixed position (m); $\nabla$ is spatial gradient (m⁻¹), $\nabla^2$ the vector Laplacian (m⁻²); the dot is a true vector contraction in convective acceleration, not an equation separator.

$\Delta\boldsymbol u$ 为固定位置速度变化，$\boldsymbol u$ 为速度（m s⁻¹）；$\Pi$ 为压力冲量（Pa s）；$\rho$ 为常数密度（kg m⁻³）；$\mu$ 为黏度（Pa s）；$\nu$ 为运动黏度（m² s⁻¹）；$t_0,t_1,t$ 为时间（s）；$\boldsymbol x$ 为固定位置（m）；$\nabla$ 为空间梯度（m⁻¹），$\nabla^2$ 为矢量拉普拉斯（m⁻²）；圆点是对流加速度中的真正矢量缩并，并非公式分隔符。



$$
\begin{gathered}\begin{aligned}
    \partial_t\boldsymbol u&=-\nabla p/\rho-(\boldsymbol u\cdot\nabla)\boldsymbol u+\nu\nabla^2\boldsymbol u,\\
    \int_{t_0}^{t_1}\partial_t\boldsymbol u\,dt
       &=\boldsymbol u(\boldsymbol x,t_1)-\boldsymbol u(\boldsymbol x,t_0)=\Delta\boldsymbol u,\\
    \int_{t_0}^{t_1}\nabla p\,dt
       &=\nabla\int_{t_0}^{t_1}(p-p_{\mathrm{ref}})\,dt
         +\int_{t_0}^{t_1}\underbrace{\nabla p_{\mathrm{ref}}}_{=0}\,dt=\nabla\Pi,\\
    \int_{t_0}^{t_1}\nu\nabla^2\boldsymbol u\,dt
       &=\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt.
    \end{aligned}\\[6pt]\begin{aligned}
        \Delta\boldsymbol u&=-\nabla\Pi/\rho
          -\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt\\
          &\quad+\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt,\\
        \Delta\boldsymbol u&=\boldsymbol u(\boldsymbol x,t_1)-\boldsymbol u(\boldsymbol x,t_0),\\
        \nu&=\mu/\rho.
        \end{aligned}\end{gathered}
$$


![The short-event approximation must justify removing convective and viscous impulses.](../assets/figures/c1-e21.svg)

The short-event approximation must justify removing convective and viscous impulses.

短事件近似必须说明为何可以删除对流与黏性冲量。

**Check and interpretation.** The convective and viscous terms remain integrals because their fields evolve. Each integrated term has units velocity. Time-dependent bounds that depend on position require additional gradient terms.

**检验与解释。** 对流和黏性场随时间变化，因此对应项仍为积分。每个积分项均具有速度单位。若时间上下限依赖位置，则梯度运算会产生额外项。

**Step 16 — Bound the omitted scales.** Choose representative liquid speed and variation length. Convective impulse scales as speed × duration/length. Viscous impulse scales as kinematic viscosity × duration/length². Small interface displacement permits fixed boundary geometry. These scale diagnostics provide no guaranteed singular-boundary-layer error bound. Under these conditions, subtract incompressible velocities and take the divergence.

**步骤 16——估算被忽略项的尺度。** 选取代表性液体速率与变化长度。对流冲量尺度为速率 × 时间／长度。黏性冲量尺度为运动黏度 × 时间／长度²。小界面位移允许固定边界几何。这些尺度诊断不能保证奇异边界层的误差界限。在这些条件下，将不可压缩速度相减并取散度。

**Derivation.** Scale the omitted acceleration terms over the pulse duration. Compare them with a velocity increment of order the chosen speed. Apply incompressibility to both endpoint fields. Taking divergence of reduced impulse momentum gives a Laplace problem. Boundary data select its solution.

**推导。** 用脉冲持续时间估算被忽略加速度项。将其与所选速度同阶的速度增量比较。对两个端点速度场分别应用不可压缩条件。对约化冲量动量关系取散度，得到拉普拉斯问题。边界数据决定其解。

**Symbols before Eq. (C1-E22).**

**式（C1-E22）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $U>0$ is a characteristic liquid speed (m s⁻¹)<br>$U>0$ 为特征液体速度（m s⁻¹） | $\tau$ is impulse duration (s)<br>$\tau$ 为冲量持续时间（s） |
| $L>0$ is liquid variation length (m)<br>$L>0$ 为液体变化长度（m） | $\nu$ is kinematic viscosity (m² s⁻¹)<br>$\nu$ 为运动黏度（m² s⁻¹） |
| $\Delta\boldsymbol u$ is velocity change (m s⁻¹)<br>$\Delta\boldsymbol u$ 为速度变化（m s⁻¹） | $\Pi$ is pressure impulse (Pa s)<br>$\Pi$ 为压力冲量（Pa s） |
| $\rho$ is density (kg m⁻³)<br>$\rho$ 为密度（kg m⁻³） |  |

**Conventions and conditions.** $\nabla\cdot$ denotes divergence and $\nabla^2$ Laplacian; $\ll$ means asymptotically small, and $\simeq$ marks the reduced approximation; The last Laplace equation belongs to that reduced model.

**约定与条件。** $\nabla\cdot$ 表示散度，$\nabla^2$ 表示拉普拉斯算子；$\ll$ 表示渐近很小，$\simeq$ 表示约化近似；最后的拉普拉斯方程属于该约化模型。

(C1-E22) · Short-event reduced pressure-impulse model / 短时事件的简化压力冲量模型

$U>0$ is a characteristic liquid speed (m s⁻¹); $\tau$ is impulse duration (s); $L>0$ is liquid variation length (m); $\nu$ is kinematic viscosity (m² s⁻¹); $\Delta\boldsymbol u$ is velocity change (m s⁻¹); $\Pi$ is pressure impulse (Pa s); $\rho$ is density (kg m⁻³); $\nabla\cdot$ denotes divergence and $\nabla^2$ Laplacian; $\ll$ means asymptotically small, and $\simeq$ marks the reduced approximation. The last Laplace equation belongs to that reduced model. $\sim$ denotes a scale estimate rather than an equality or rigorous error bound; $t_0,t_1$ are fixed event endpoints (s); $\boldsymbol u$ is velocity (m s⁻¹).

$U>0$ 为特征液体速度（m s⁻¹）；$\tau$ 为冲量持续时间（s）；$L>0$ 为液体变化长度（m）；$\nu$ 为运动黏度（m² s⁻¹）；$\Delta\boldsymbol u$ 为速度变化（m s⁻¹）；$\Pi$ 为压力冲量（Pa s）；$\rho$ 为密度（kg m⁻³）；$\nabla\cdot$ 表示散度，$\nabla^2$ 表示拉普拉斯算子；$\ll$ 表示渐近很小，$\simeq$ 表示约化近似。最后的拉普拉斯方程属于该约化模型。 $\sim$ 表示尺度估计，并非等式或严格误差界；$t_0,t_1$ 为固定事件端点（s）；$\boldsymbol u$ 为速度（m s⁻¹）。



$$
\begin{gathered}\begin{aligned}
    \left|\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt\right|
       &\sim U^2\tau/L,\qquad (U^2\tau/L)/U=U\tau/L,\\
    \left|\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt\right|
       &\sim\nu U\tau/L^2,\qquad(\nu U\tau/L^2)/U=\nu\tau/L^2,\\
    \nabla\cdot\Delta\boldsymbol u&=\nabla\cdot\boldsymbol u(t_1)-\nabla\cdot\boldsymbol u(t_0)=0-0=0,\\
    0&=-\nabla\cdot\nabla\Pi/\rho=-\nabla^2\Pi/\rho.
    \end{aligned}\\[6pt]\begin{gathered}\frac{U\tau}{L}\ll1\\ \frac{\nu\tau}{L^2}\ll1\\ \Delta\boldsymbol u\simeq-\frac{\nabla\Pi}{\rho}\\ 0=\nabla\cdot\Delta\boldsymbol u\simeq-\frac{\nabla^2\Pi}{\rho}\ \Longrightarrow\ \nabla^2\Pi=0\end{gathered}\end{gathered}
$$


![The velocity depends on a spatial impulse gradient constrained by boundary geometry.](../assets/figures/c1-e22.svg)

The velocity depends on a spatial impulse gradient constrained by boundary geometry.

速度取决于受边界几何约束的空间压力冲量梯度。

**Check and interpretation.** If the actual increment is much smaller than the chosen speed, these ratios need not bound its relative error. A fixed wall gives zero normal impulse derivative when normal velocity is unchanged. Driven and outlet boundaries supply their impulse values.

**检验与解释。** 若实际增量远小于所选速度，这些比值不能约束增量的相对误差。固定壁面法向速度不变时，法向冲量导数为零。受驱边界与出口分别给出各自冲量值。

A fixed impermeable wall requires zero normal velocity change. Its normal impulse derivative therefore vanishes. A driven cavity prescribes impulse or pressure history. A communicating outlet supplies its pressure reference. A spatially uniform impulse addition has zero gradient and changes no velocity. Pulse duration and boundary geometry can change the response at fixed peak pressure.

固定不透壁要求法向速度变化为零，因而法向冲量导数为零。受驱空腔给定冲量或压力历程，连通出口给定压力参考值。空间均匀增加冲量的梯度为零，不改变速度。峰值压力固定时，脉冲时长与边界几何仍可改变响应。

**Step 17 — Solve a straight-column benchmark.** Start with a stationary uniform column along the positive axis. Area is constant and side walls are fixed. Prescribe positive inlet impulse and zero outlet impulse. Integrate the one-dimensional Laplace equation twice. Apply both endpoint values to obtain its gradient.

**步骤 17——求解直液柱基准。** 初始均匀液柱沿正轴静止，面积恒定，侧壁固定。入口冲量给定为正，出口冲量为零。将一维拉普拉斯方程积分两次，再用两个端点值确定梯度。

**Derivation.** For the straight column, integrate the zero second derivative once to obtain a constant slope. Integrate again. Apply inlet data to the intercept and outlet data to the slope. The negative pressure-impulse slope accelerates liquid in the positive axial direction.

**推导。** 对直液柱，将二阶导数为零积分一次，得到常斜率，再积分一次。入口条件确定截距，出口条件确定斜率。负压力冲量斜率使液体沿正轴向加速。

**Symbols before Eq. (C1-E23).**

**式（C1-E23）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $z\in[0,L]$ is axial position (m)<br>$z\in[0,L]$ 为轴向位置（m） | $L>0$ column length (m)<br>$L>0$ 为液柱长度（m） |
| $\Pi(z)$ — Local column pressure impulse (Pa s)<br>$\Pi(z)$ — 液柱局部压力冲量（Pa s） | $\Pi_0>0$ — Driven-end pressure impulse (Pa s)<br>$\Pi_0>0$ — 驱动端压力冲量（Pa s） |
| $A_0$ is an integration constant (Pa s)<br>$A_0$ 为积分常数（Pa s） | $A_1$ a gradient constant (Pa s m⁻¹)<br>$A_1$ 为梯度常数（Pa s m⁻¹） |
| $\rho>0$ is carrier density (kg m⁻³)<br>$\rho>0$ 为载液密度（kg m⁻³） | $\Delta u_z$ is positive axial speed change (m s⁻¹)<br>$\Delta u_z$ 为正轴向速度变化（m s⁻¹） |

**Conventions and conditions.** $d/dz$ is an axial derivative; Subscript $z$ labels the component and 0 the driven endpoint.

**约定与条件。** $d/dz$ 为轴向导数；下标 $z$ 表示分量，0 表示受驱动端点。

(C1-E23) · Exact straight-column solution of the reduced model / 简化模型中直液柱的精确解

$z\in[0,L]$ is axial position and $L>0$ column length (m); $\Pi(z)$ and $\Pi_0>0$ are local and driven-end impulses (Pa s); $A_0$ is an integration constant (Pa s), $A_1$ a gradient constant (Pa s m⁻¹); $\rho>0$ is carrier density (kg m⁻³); $\Delta u_z$ is positive axial speed change (m s⁻¹); $d/dz$ is an axial derivative. Subscript $z$ labels the component and 0 the driven endpoint. $s$ is a dummy axial integration coordinate (m). The uniform-speed column is an inviscid core benchmark; no-slip wall layers are omitted.

$z\in[0,L]$ 为轴向位置，$L>0$ 为液柱长度（m）；$\Pi(z)$ 与 $\Pi_0>0$ 为局部与受驱动端冲量（Pa s）；$A_0$ 为积分常数（Pa s），$A_1$ 为梯度常数（Pa s m⁻¹）；$\rho>0$ 为载液密度（kg m⁻³）；$\Delta u_z$ 为正轴向速度变化（m s⁻¹）；$d/dz$ 为轴向导数。下标 $z$ 表示分量，0 表示受驱动端点。 $s$ 为轴向积分哑坐标（m）。匀速液柱是无黏核心流基准，省略无滑移壁面层。



$$
\begin{gathered}\begin{aligned}
    d^2\Pi/dz^2=0&\Rightarrow d\Pi/dz=A_1,\\
    \Pi(z)-\Pi(0)&=\int_0^z A_1\,ds=A_1z,\\
    \Pi(0)=\Pi_0&\Rightarrow A_0=\Pi_0,\\
    0=\Pi(L)&=A_1L+\Pi_0\Rightarrow A_1=-\Pi_0/L,\\
    \Delta u_z&=-(-\Pi_0/L)/\rho=\Pi_0/(\rho L).
    \end{aligned}\\[6pt]\begin{aligned}\frac{d^2\Pi}{dz^2}&=0\quad\Longrightarrow\quad\Pi=A_1z+A_0,\\\Pi(0)&=\Pi_0,\quad\Pi(L)=0\quad\Longrightarrow\quad A_0=\Pi_0,\quad A_1=-\frac{\Pi_0}{L},\\\Pi(z)&=\Pi_0\left(1-\frac zL\right),\qquad \Delta u_z=-\frac1\rho\frac{d\Pi}{dz}=\frac{\Pi_0}{\rho L}.\end{aligned}\end{gathered}
$$


![A linear spatial impulse drop accelerates liquid toward the outlet.](../assets/figures/c1-e23.svg)

A linear spatial impulse drop accelerates liquid toward the outlet.

线性的空间冲量下降使液体向出口加速。

**Check and interpretation.** At inlet and outlet the solution reproduces both prescribed values. Impulse divided by density and length has units m s⁻¹. Equal pressure peaks with different durations produce different speed increments.

**检验与解释。** 解在入口和出口恢复两个给定值。冲量除以密度及长度的单位为 m s⁻¹。相同压力峰值、不同持续时间会产生不同速度增量。

Prescribe 0.60 MPa for 0.50 μs across a 100 μm column. Use the earlier density, viscosity 0.001 Pa s, and sound speed 1500 m s⁻¹. The velocity change is 3.0 m s⁻¹. Crossing time is shorter than the pulse. Uniform pressure and final jet speed remain unestablished. The solved column has an end-to-end pressure gradient.

在 100 μm 液柱两端施加 0.60 MPa 压差，持续 0.50 μs。采用前述密度、黏度 0.001 Pa s 和声速 1500 m s⁻¹。速度变化为 3.0 m s⁻¹。传播时间短于脉冲时长。均匀压力及最终射流速率尚未确立。已解液柱具有端到端压力梯度。

**Derivation.** The rectangular pulse is a stipulated ideal benchmark. Convert its pressure, duration and column length. Compute the impulse, velocity, displacement ratio, viscous ratio and crossing time separately. The total pulse duration does not specify its physical rise time.

**推导。** 矩形脉冲是规定的理想基准。换算压力、持续时间和液柱长度。分别计算冲量、速度、位移比、黏性比及声穿越时间。脉冲总时长不能确定实际上升时间。

**Symbols before Eq. (C1-E24).**

**式（C1-E24）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Pi_0$ is driven-end impulse (Pa s)<br>$\Pi_0$ 为受驱动端冲量（Pa s） | $\Delta p$ is constant applied column pressure difference (Pa)<br>$\Delta p$ 为施加的常数液柱压差（Pa） |
| $\tau$ is pulse duration (s)<br>$\tau$ 为脉冲持续时间（s） | $U$ is column speed increment (m s⁻¹)<br>$U$ 为液柱速度增量（m s⁻¹） |
| $\rho=1000$ kg m⁻³ is density<br>$\rho=1000$ kg m⁻³ 为密度 | $L=100\times10^{-6}$ m is length<br>$L=100\times10^{-6}$ m 为长度 |
| $c=1500$ m s⁻¹ is sound speed<br>$c=1500$ m s⁻¹ 为声速 | $t_a$ is acoustic crossing time (s)<br>$t_a$ 为声传播时间（s） |
| $\nu=\mu/\rho=10^{-6}$ m² s⁻¹ with $\mu=0.001$ Pa s<br>$\nu=\mu/\rho=10^{-6}$ m² s⁻¹，且 $\mu=0.001$ Pa s | $\mu$ — Carrier dynamic viscosity (Pa s)<br>$\mu$ — 载液动力黏度（Pa s） |

**Conventions and conditions.** The three ratios are dimensionless; μs means microseconds.

**约定与条件。** 三个比值均无量纲；μs 表示微秒。

(C1-E24) · Declared impulse calculation and applicability diagnostics / 采用给定参数的冲量计算与适用性诊断

$\Pi_0$ is driven-end impulse (Pa s); $\Delta p$ is constant applied column pressure difference (Pa); $\tau$ is pulse duration (s); $U$ is column speed increment (m s⁻¹); $\rho=1000$ kg m⁻³ is density; $L=100\times10^{-6}$ m is length; $c=1500$ m s⁻¹ is sound speed; $t_a$ is acoustic crossing time (s); $\nu=\mu/\rho=10^{-6}$ m² s⁻¹ with $\mu=0.001$ Pa s. The three ratios are dimensionless; μs means microseconds.

$\Pi_0$ 为受驱动端冲量（Pa s）；$\Delta p$ 为施加的常数液柱压差（Pa）；$\tau$ 为脉冲持续时间（s）；$U$ 为液柱速度增量（m s⁻¹）；$\rho=1000$ kg m⁻³ 为密度；$L=100\times10^{-6}$ m 为长度；$c=1500$ m s⁻¹ 为声速；$t_a$ 为声传播时间（s）；$\nu=\mu/\rho=10^{-6}$ m² s⁻¹，且 $\mu=0.001$ Pa s。三个比值均无量纲；μs 表示微秒。



$$
\begin{gathered}\begin{aligned}
    \Delta p&=6.0\times10^5\ \mathrm{Pa},\quad\tau=5.0\times10^{-7}\ \mathrm s,
      \quad L=10^{-4}\ \mathrm m,\\
    \Pi_0&=(6.0\times10^5)(5.0\times10^{-7})=0.30\ \mathrm{Pa\,s},\\
    \rho L&=1000(10^{-4})=0.1\ \mathrm{kg\,m^{-2}},\quad U=0.30/0.1=3.0\ \mathrm{m\,s^{-1}},\\
    U\tau/L&=3(5\times10^{-7})/10^{-4}=0.015,\\
    \nu\tau/L^2&=(10^{-6})(5\times10^{-7})/10^{-8}=5\times10^{-5},\\
    t_a&=10^{-4}/1500=6.66667\times10^{-8}\ \mathrm s,\quad \tau/t_a=7.5.
    \end{aligned}\\[6pt]\begin{aligned}\Pi_0&=\Delta p\tau=(0.60\times10^6)(0.50\times10^{-6})\ \mathrm{Pa\,s}=0.30\ \mathrm{Pa\,s},\\U&=\frac{\Pi_0}{\rho L}=3.0\ \mathrm{m\,s^{-1}},\qquad t_a=\frac Lc=0.066667\ \mu\mathrm s,\\\frac{U\tau}{L}&=0.015,\qquad\frac{\nu\tau}{L^2}=5.0\times10^{-5},\qquad\frac{\tau}{t_a}=7.5.\end{aligned}\end{gathered}
$$


![Pressure impulse and acoustic time have distinct definitions, dimensions and roles.](../assets/figures/c1-e24.svg)

Pressure impulse and acoustic time have distinct definitions, dimensions and roles.

压力冲量与声传播时间具有不同的定义、量纲与作用。

**Check and interpretation.** The rectangular discontinuity has zero ideal rise time, so its fronts require acoustic treatment. The integrated column result is a reduced impulse benchmark. A real pulse needs a measured or prescribed finite rise time and the separate communication test below.

**检验与解释。** 理想矩形跃变的上升时间为零，因此波前需要声学处理。液柱积分结果属于约化冲量基准。实际脉冲需要实测或给定的有限上升时间，并进行下文独立通信检验。

Directional motion requires asymmetry. A sphere in uniform infinite liquid has no preferred direction. Outlets, menisci, walls, neighbors or uneven heating break that symmetry. Stand-off is center-to-boundary distance divided by maximum radius. Equal stand-off still permits different curvature and material response. Collapse near a rigid plane commonly directs a jet toward it. Deformable boundaries can change or split that response. [[R3]](../reference/sources.html#r3) [[R12]](../reference/sources.html#r12)

定向运动需要非对称性。均匀无限液体中的球形空腔没有优选方向。出口、弯月面、壁面、邻近空腔或不均匀加热可破坏对称性。离壁参数为中心至边界距离除以最大半径。相同离壁参数仍可对应不同曲率和材料响应。刚性平面附近的塌缩射流通常朝向平面。可变形边界可改变或分裂该响应。 [[R3]](../reference/sources.html#r3) [[R12]](../reference/sources.html#r12)

**Derivation.** Stand-off compares a center-to-boundary distance with maximum bubble radius. It is a geometric descriptor. To prove directional cancellation for the unbounded sphere, write each radial unit-vector component and integrate over all solid angles. The azimuthal sine and cosine integrate to zero; the axial component cancels between hemispheres.

**推导。** 离壁比将中心到边界距离与最大气泡半径比较，属于几何描述。为证明无界球形情况下方向相互抵消，写出径向单位矢量各分量并对全部立体角积分。方位正弦和余弦积分为零，轴向分量在两半球之间抵消。

**Symbols before Eq. (C1-E25).**

**式（C1-E25）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\gamma$ is dimensionless stand-off<br>$\gamma$ 为无量纲离壁比 | $h$ is bubble-center-to-boundary distance (m)<br>$h$ 为气泡中心到边界的距离（m） |
| $R_{\max}$ is maximum radius (m)<br>$R_{\max}$ 为最大半径（m） | $S^2$ denotes all directions on the unit sphere (—)<br>$S^2$ 表示单位球面上的全部方向（—） |
| $\boldsymbol e_r$ is the outward radial unit vector (dimensionless)<br>$\boldsymbol e_r$ 为向外径向单位矢量（无量纲） | $d\Omega$ is the dimensionless solid-angle measure<br>$d\Omega$ 为无量纲立体角测度 |
| $\boldsymbol0$ is the zero vector (dimensionless)<br>$\boldsymbol0$ 为零矢量（无量纲） |  |

**Conventions and conditions.** The angular identity expresses directional cancellation under perfect spherical symmetry; it is not a boundary-jet prediction.

**约定与条件。** 角积分恒等式表示完全球对称下方向相互抵消，并非边界射流预测。

(C1-E25) · Geometry definition and exact symmetry identity / 几何定义与精确的对称性恒等式

$\gamma$ is dimensionless stand-off; $h$ is bubble-center-to-boundary distance (m); $R_{\max}$ is maximum radius (m); $S^2$ denotes all directions on the unit sphere; $\boldsymbol e_r$ is the outward radial unit vector; $d\Omega$ is the dimensionless solid-angle measure; $\boldsymbol0$ is the zero vector. The angular identity expresses directional cancellation under perfect spherical symmetry; it is not a boundary-jet prediction. $\theta\in[0,\pi]$ and $\psi\in[0,2\pi]$ are dimensionless polar and azimuthal angles; tuple entries are Cartesian vector components.

$\gamma$ 为无量纲离壁比；$h$ 为气泡中心到边界的距离（m）；$R_{\max}$ 为最大半径（m）；$S^2$ 表示单位球面上的全部方向；$\boldsymbol e_r$ 为向外径向单位矢量；$d\Omega$ 为无量纲立体角测度；$\boldsymbol0$ 为零矢量。角积分恒等式表示完全球对称下方向相互抵消，并非边界射流预测。 $\theta\in[0,\pi]$ 与 $\psi\in[0,2\pi]$ 为无量纲极角和方位角；有序三元组为笛卡尔矢量分量。



$$
\begin{gathered}\begin{aligned}
    \boldsymbol e_r&=(\sin\theta\cos\psi,\sin\theta\sin\psi,\cos\theta),\quad
      d\Omega=\sin\theta\,d\theta\,d\psi,\\
    \int_0^{2\pi}\cos\psi\,d\psi&=[\sin\psi]_0^{2\pi}=0,\\
    \int_0^{2\pi}\sin\psi\,d\psi&=[-\cos\psi]_0^{2\pi}=0,\\
    \int_0^\pi\cos\theta\sin\theta\,d\theta&=[\tfrac12\sin^2\theta]_0^\pi=0,\\
    \int_{S^2}\boldsymbol e_r\,d\Omega&=(0,0,0).
    \end{aligned}\\[6pt]\begin{gathered}\gamma=\frac h{R_{\max}}\\ \int_{S^2}\boldsymbol e_r\,d\Omega=\boldsymbol0\end{gathered}\end{gathered}
$$


![Stand-off locates a boundary; perfect spherical symmetry selects no outgoing direction.](../assets/figures/c1-e25.svg)

Stand-off locates a boundary; perfect spherical symmetry selects no outgoing direction.

离壁比定位边界；完全球对称不能选出向外喷射方向。

**Check and interpretation.** The cancellation concerns perfect symmetry. Actual boundaries change the spatial pressure and velocity problem. Stand-off alone cannot determine the response of different boundary materials or curvatures.

**检验与解释。** 抵消结论针对完全球对称。实际边界改变空间压力和速度问题。离壁比本身不能确定不同边界材料或曲率下的响应。

## 1.7 Moving-interface model

## 1.7 运动界面模型

**Step 18 — Specify the spatial jet problem.** Prescribe initial interface shape and carrier velocity. Define solid boundaries, outlet, contact-line behavior and pressure closure. The following equations conserve mass and momentum for constant-property incompressible Newtonian liquid. Gravity is omitted. Solve them with the interface and boundary conditions below. A fitted radius history leaves these spatial conditions unresolved.

**步骤 18——规定空间射流问题。** 给定初始界面形状和载液速度，定义固体边界、出口、接触线规律及压力闭合。以下方程描述常物性不可压缩牛顿液体的质量与动量守恒，忽略重力。须结合下述界面和边界条件求解。拟合半径历程仍未确定这些空间条件。

**Derivation.** Start with local mass and Cauchy momentum conservation. Adopt constant-density Newtonian stress. Its divergence reduces to the vector Laplacian because incompressibility removes the divergence-gradient term. The spatial problem has three velocity components, pressure and unknown interface shape, together with initial and boundary data.

**推导。** 从局部质量守恒与柯西动量守恒出发，采用常密度牛顿应力。不可压缩条件消去散度梯度项，使黏性应力散度约化为矢量拉普拉斯。空间问题包含三个速度分量、压力及未知界面形状，还需初始和边界数据。

**Symbols before Eq. (C1-E26).**

**式（C1-E26）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol u(\boldsymbol x,t)$ is liquid velocity (m s⁻¹)<br>$\boldsymbol u(\boldsymbol x,t)$ 为液体速度（m s⁻¹） | $\boldsymbol x$ is spatial position (m)<br>$\boldsymbol x$ 为空间位置（m） |
| $t$ is time (s)<br>$t$ 为时间（s） | $\rho$ is constant carrier density (kg m⁻³)<br>$\rho$ 为常数载液密度（kg m⁻³） |
| $p$ is liquid pressure (Pa)<br>$p$ 为液体压力（Pa） | $\mu$ is constant viscosity (Pa s)<br>$\mu$ 为常数黏度（Pa s） |

**Conventions and conditions.** $\nabla\cdot,\nabla,\nabla^2$ denote divergence, gradient and vector Laplacian; $\partial_t$ is the fixed-position derivative; The dot in convection is vector contraction; The momentum equation has force-per-volume units (N m⁻³).

**约定与条件。** $\nabla\cdot,\nabla,\nabla^2$ 分别为散度、梯度与矢量拉普拉斯；$\partial_t$ 为固定位置导数；对流中的圆点为矢量缩并；动量方程各项单位为单位体积力（N m⁻³）。

(C1-E26) · Bulk conservation and Newtonian constitutive assumption / 体相守恒律与牛顿流体本构假设

$\boldsymbol u(\boldsymbol x,t)$ is liquid velocity (m s⁻¹); $\boldsymbol x$ is spatial position (m); $t$ is time (s); $\rho$ is constant carrier density (kg m⁻³); $p$ is liquid pressure (Pa); $\mu$ is constant viscosity (Pa s); $\nabla\cdot,\nabla,\nabla^2$ denote divergence, gradient and vector Laplacian; $\partial_t$ is the fixed-position derivative. The dot in convection is vector contraction. The momentum equation has force-per-volume units (N m⁻³). $\boldsymbol T$ is Cauchy stress (Pa), $\boldsymbol I$ the dimensionless identity tensor, superscript $\mathsf T$ transpose, $D/Dt$ the material derivative; body forces are omitted. The density derivative is displayed before imposing constant density.

$\boldsymbol u(\boldsymbol x,t)$ 为液体速度（m s⁻¹）；$\boldsymbol x$ 为空间位置（m）；$t$ 为时间（s）；$\rho$ 为常数载液密度（kg m⁻³）；$p$ 为液体压力（Pa）；$\mu$ 为常数黏度（Pa s）；$\nabla\cdot,\nabla,\nabla^2$ 分别为散度、梯度与矢量拉普拉斯；$\partial_t$ 为固定位置导数。对流中的圆点为矢量缩并。动量方程各项单位为单位体积力（N m⁻³）。 $\boldsymbol T$ 为柯西应力（Pa），$\boldsymbol I$ 为无量纲单位张量，上标 $\mathsf T$ 表示转置，$D/Dt$ 为物质导数；忽略体力。密度导数写在施加常密度条件之前。



$$
\begin{gathered}\begin{aligned}
    \partial_t\rho+\nabla\cdot(\rho\boldsymbol u)&=0
       \quad\xrightarrow{\rho\ \mathrm{constant}}\quad\nabla\cdot\boldsymbol u=0,\\
    \boldsymbol T&=-p\boldsymbol I+\mu[\nabla\boldsymbol u+(\nabla\boldsymbol u)^{\mathsf T}],\\
    \rho D\boldsymbol u/Dt&=\nabla\cdot\boldsymbol T,\\
    \nabla\cdot\boldsymbol T&=-\nabla p+\mu[\nabla^2\boldsymbol u+\nabla(\nabla\cdot\boldsymbol u)]
      =-\nabla p+\mu\nabla^2\boldsymbol u,\\
    D\boldsymbol u/Dt&=\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u.
    \end{aligned}\\[6pt]\begin{gathered}\nabla\cdot\boldsymbol u=0\\ \rho\left(\frac{\partial\boldsymbol u}{\partial t}+(\boldsymbol u\cdot\nabla)\boldsymbol u\right)=-\nabla p+\mu\nabla^2\boldsymbol u\end{gathered}\end{gathered}
$$


![Bulk momentum and volume conservation supply the spatial field needed for jet formation.](../assets/figures/c1-e26.svg)

Bulk momentum and volume conservation supply the spatial field needed for jet formation.

体内动量与体积守恒给出射流形成所需的空间场。

**Check and interpretation.** Stress divergence and inertia both have units N m⁻³. Supply a divergence-free initial velocity, compatible interface shape, wall velocities, outlet data and contact-line law. A radius history cannot replace these fields.

**检验与解释。** 应力散度和惯性项单位均为 N m⁻³。需要给定无散初始速度、相容初始界面、壁面速度、出口数据及接触线规律。半径历程不能代替这些空间场。

**Step 19 — Set interface orientation and stress.** The normal points from liquid into gas. An inner spherical cavity therefore has negative curvature. An outer liquid droplet has positive curvature. This reproduces Eq. (C1-E06). A clean interface with negligible gas viscosity has zero tangential viscous traction. At zero liquid viscosity, that condition adds no strain-rate constraint. Without phase transfer, interface and liquid normal velocities match.

**步骤 19——规定界面方向与应力。** 法向由液体指向气体，故内球形空腔曲率为负，外液滴曲率为正。这一约定恢复式（C1-E06）。清洁界面且气相黏性可忽略时，切向黏性牵引为零。液体黏度为零时，该条件不增加应变率约束。没有相变时，界面与液体法向速度相等。

**Derivation.** Represent a material interface by a level set. Its material derivative vanishes, yielding equal normal speeds. The level-set normal points from liquid to gas. Project the clean-interface stress jump onto its normal and tangent. Constant surface tension and negligible gas viscous stress give the pressure and tangential conditions.

**推导。** 用水平集表示物质界面。其物质导数为零，从而得到法向速度相等。水平集法向从液体指向气体。将清洁界面应力跳跃分别投影至法向和切向。表面张力恒定且气体黏性应力可忽略时，得到压力和切向条件。

**Symbols before Eq. (C1-E27).**

**式（C1-E27）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol D$ is symmetric liquid strain-rate tensor (s⁻¹)<br>$\boldsymbol D$ 为液体对称应变率张量（s⁻¹） | $\boldsymbol u$ is velocity (m s⁻¹)<br>$\boldsymbol u$ 为速度（m s⁻¹） |
| $\boldsymbol n$ is the unit normal from liquid into gas (dimensionless)<br>$\boldsymbol n$ 为从液体指向气体的单位法向（无量纲） | $\kappa$ is signed curvature (m⁻¹)<br>$\kappa$ 为带符号曲率（m⁻¹） |
| $V_n$ is interface normal speed (m s⁻¹)<br>$V_n$ 为界面法向速度（m s⁻¹） | $p_l$ — Adjacent-liquid absolute pressure (Pa)<br>$p_l$ — 邻近液体绝对压力（Pa） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $\sigma$ is surface tension (N m⁻¹)<br>$\sigma$ 为表面张力（N m⁻¹） |
| $\mu$ is viscosity (Pa s)<br>$\mu$ 为黏度（Pa s） | $\boldsymbol s$ is any unit tangent (dimensionless)<br>$\boldsymbol s$ 为任意单位切向（无量纲） |
| $R$ is spherical cavity radius (m)<br>$R$ 为球形空腔半径（m） |  |

**Conventions and conditions.** $\nabla\boldsymbol u$ is its spatial gradient, with superscript $\mathsf T$ denoting transpose; $\nabla_s\cdot$ is surface divergence; Dots denote tensor/vector contractions.

**约定与条件。** $\nabla\boldsymbol u$ 为其空间梯度，上标 $\mathsf T$ 表示转置；$\nabla_s\cdot$ 为表面散度；圆点表示张量或矢量缩并。

(C1-E27) · Kinematic condition and clean-interface traction / 运动学条件与洁净界面牵引

$\boldsymbol D$ is symmetric liquid strain-rate tensor (s⁻¹); $\boldsymbol u$ is velocity (m s⁻¹); $\nabla\boldsymbol u$ is its spatial gradient, with superscript $\mathsf T$ denoting transpose; $\boldsymbol n$ is the unit normal from liquid into gas; $\nabla_s\cdot$ is surface divergence; $\kappa$ is signed curvature (m⁻¹); $V_n$ is interface normal speed (m s⁻¹); $p_l,p_b$ are interface liquid and gas pressures (Pa); $\sigma$ is surface tension (N m⁻¹); $\mu$ is viscosity (Pa s); $\boldsymbol s$ is any unit tangent; $R$ is spherical cavity radius (m). Dots denote tensor/vector contractions. $F$ is a smooth dimensionless level-set function increasing into gas, with nonzero gradient on the interface; $\boldsymbol x$ is position (m), $t$ time (s); $\boldsymbol T_g=-p_b\boldsymbol I$ and $\boldsymbol T_l=-p_l\boldsymbol I+2\mu\boldsymbol D$ are gas and liquid stresses (Pa); $\boldsymbol I$ is the identity tensor.

$\boldsymbol D$ 为液体对称应变率张量（s⁻¹）；$\boldsymbol u$ 为速度（m s⁻¹）；$\nabla\boldsymbol u$ 为其空间梯度，上标 $\mathsf T$ 表示转置；$\boldsymbol n$ 为从液体指向气体的单位法向；$\nabla_s\cdot$ 为表面散度；$\kappa$ 为带符号曲率（m⁻¹）；$V_n$ 为界面法向速度（m s⁻¹）；$p_l,p_b$ 为界面液体与气体压力（Pa）；$\sigma$ 为表面张力（N m⁻¹）；$\mu$ 为黏度（Pa s）；$\boldsymbol s$ 为任意单位切向；$R$ 为球形空腔半径（m）。圆点表示张量或矢量缩并。 $F$ 为向气体侧增加的光滑无量纲水平集，界面上梯度非零；$\boldsymbol x$ 为位置（m），$t$ 为时间（s）；$\boldsymbol T_g=-p_b\boldsymbol I$ 与 $\boldsymbol T_l=-p_l\boldsymbol I+2\mu\boldsymbol D$ 为气液应力（Pa）；$\boldsymbol I$ 为单位张量。



$$
\begin{gathered}\begin{aligned}
    F(\boldsymbol x,t)=0,\quad\boldsymbol n&=\nabla F/|\nabla F|,\quad
      V_n=-\partial_tF/|\nabla F|,\\
    \partial_tF+\boldsymbol u\cdot\nabla F=0&\Rightarrow V_n=\boldsymbol u\cdot\boldsymbol n,\\
    (\boldsymbol T_g-\boldsymbol T_l)\boldsymbol n&=\sigma\kappa\boldsymbol n,\\
    (\boldsymbol T_g-\boldsymbol T_l)\boldsymbol n
       &=[(p_l-p_b)\boldsymbol I-2\mu\boldsymbol D]\boldsymbol n,\\
    \boldsymbol n\cdot\boldsymbol n&=1,\qquad\boldsymbol s\cdot\boldsymbol n=0,\\
    p_l-p_b-2\mu\boldsymbol n\cdot\boldsymbol D\boldsymbol n&=\sigma\kappa,\\
    -2\mu\boldsymbol s\cdot\boldsymbol D\boldsymbol n&=0.
    \end{aligned}\\[6pt]\begin{aligned}\boldsymbol D&=\frac12\left(\nabla\boldsymbol u+(\nabla\boldsymbol u)^\mathsf T\right),\qquad \kappa=\nabla_s\cdot\boldsymbol n,\\V_n&=\boldsymbol u\cdot\boldsymbol n,\qquad p_l=p_b+\sigma\kappa+2\mu\boldsymbol n\cdot\boldsymbol D\boldsymbol n,\\2\mu\boldsymbol s\cdot\boldsymbol D\boldsymbol n&=0,\qquad \kappa_{\mathrm{sphere}}=-\frac2R.\end{aligned}\end{gathered}
$$


![Interface normals, signed curvature and material motion must use one consistent convention.](../assets/figures/c1-e27.svg)

Interface normals, signed curvature and material motion must use one consistent convention.

界面法向、带符号曲率与物质运动必须采用一致约定。

**Check and interpretation.** The interface condition matches normal velocity; tangential node motion is a parametrization choice. It imposes no solid-wall no-slip condition on an inviscid free surface. Phase transfer needs a mass-flux condition instead.

**检验与解释。** 界面条件匹配法向速度；节点切向运动属于参数化选择。无黏自由表面不能施加固壁无滑移条件。发生相变传质时，应采用质量通量条件。

Set zero liquid velocity at a stationary viscous wall. Couple liquid velocity and stress to a moving film. Supply external pressure and stress at the outlet or meniscus. Close the contact line with a pinned or moving-angle law. Chapter 4 supplies payload and release mechanics. Appreciable phase transfer replaces equal normal velocities with Chapter 2’s mass-flux balance.

静止黏性壁面采用零液体速度。运动薄膜须与液体速度和应力耦合。出口或弯月面给定外部压力与应力。接触线采用固定或动态接触角规律闭合。第四章给出载荷与释放力学。相变显著时，用第二章质量通量平衡代替法向速度相等条件。

**Step 20 — Derive the potential-flow reduction.** Assume inviscid, initially irrotational flow away from shocks and unresolved wall layers. The potential satisfies Laplace’s equation. Without phase slip, interface nodes follow liquid velocity. Convert the Eulerian Bernoulli derivative to the material derivative. Add velocity dotted with the potential gradient. This closes a spatial pre-impact model under the stated assumptions. Boundary-integral microjet models use this reduction. [[R4]](../reference/sources.html#r4)

**步骤 20——推导势流约化。** 假设流动无黏且初始无旋，并避开激波及未解析壁面层。速度势满足拉普拉斯方程。无相变滑移时，界面节点随液体速度运动。将欧拉伯努利导数转为物质导数，加入速度与速度势梯度的点积。由此在已声明假设下闭合撞击前空间模型。边界积分微射流模型采用此约化。 [[R4]](../reference/sources.html#r4)

**Derivation.** For inviscid irrotational liquid, choose potential and interface position as unknowns. Incompressibility gives Laplace’s equation. On the interface, combine Bernoulli with the inviscid traction jump. Then convert the fixed-position derivative into the derivative following a liquid marker. This conversion changes the kinetic-term sign.

**推导。** 对无黏无旋液体，选取速度势和界面位置为未知量。不可压缩条件给出拉普拉斯方程。在界面结合伯努利方程与无黏牵引跳跃，再将固定位置导数转为随液体标记点运动的导数。该转换改变动能项符号。

**Symbols before Eq. (C1-E28).**

**式（C1-E28）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol u$ is liquid velocity (m s⁻¹)<br>$\boldsymbol u$ 为液体速度（m s⁻¹） | $\phi$ is velocity potential (m² s⁻¹)<br>$\phi$ 为速度势（m² s⁻¹） |
| $\boldsymbol X$ is a material interface position (m)<br>$\boldsymbol X$ 为物质界面点位置（m） | $t$ is time (s)<br>$t$ 为时间（s） |
| $\Gamma$ is the liquid–gas interface (—)<br>$\Gamma$ 为液—气界面（—） | $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $\sigma$ is surface tension (N m⁻¹)<br>$\sigma$ 为表面张力（N m⁻¹） |
| $\kappa$ is curvature for the liquid-to-gas normal (m⁻¹)<br>$\kappa$ 为液体指向气体法向下的曲率（m⁻¹） | $\rho$ is density (kg m⁻³)<br>$\rho$ 为密度（kg m⁻³） |

**Conventions and conditions.** $\nabla$ and $\nabla^2$ are spatial gradient and Laplacian; $D/Dt$ is the material derivative; $|\boldsymbol u|$ is speed and the dot a vector contraction; The potential gauge is fixed at infinity.

**约定与条件。** $\nabla$ 与 $\nabla^2$ 为空间梯度与拉普拉斯；$D/Dt$ 为物质导数；$|\boldsymbol u|$ 为速率，圆点为矢量缩并；速度势参考值固定在无穷远。

(C1-E28) · Inviscid pre-impact moving-interface closure / 冲击前无黏运动界面的闭合关系

$\boldsymbol u$ is liquid velocity (m s⁻¹); $\phi$ is velocity potential (m² s⁻¹); $\nabla$ and $\nabla^2$ are spatial gradient and Laplacian; $\boldsymbol X$ is a material interface position (m); $t$ is time (s); $\Gamma$ is the liquid–gas interface; $p_\infty,p_b$ are far-field and bubble pressures (Pa); $\sigma$ is surface tension (N m⁻¹); $\kappa$ is curvature for the liquid-to-gas normal (m⁻¹); $\rho$ is density (kg m⁻³); $D/Dt$ is the material derivative; $|\boldsymbol u|$ is speed and the dot a vector contraction. The potential gauge is fixed at infinity. $p_l$ is liquid-side interface pressure (Pa). Interface markers $\boldsymbol X(t)$ follow liquid particles; the material potential derivative has units m² s⁻². The construction assumes single-valued potential and a smooth pre-impact interface.

$\boldsymbol u$ 为液体速度（m s⁻¹）；$\phi$ 为速度势（m² s⁻¹）；$\nabla$ 与 $\nabla^2$ 为空间梯度与拉普拉斯；$\boldsymbol X$ 为物质界面点位置（m）；$t$ 为时间（s）；$\Gamma$ 为液—气界面；$p_\infty,p_b$ 为远场与气泡压力（Pa）；$\sigma$ 为表面张力（N m⁻¹）；$\kappa$ 为液体指向气体法向下的曲率（m⁻¹）；$\rho$ 为密度（kg m⁻³）；$D/Dt$ 为物质导数；$|\boldsymbol u|$ 为速率，圆点为矢量缩并。速度势参考值固定在无穷远。 $p_l$ 为界面液体侧压力（Pa）。界面标记点 $\boldsymbol X(t)$ 随液体质点运动；速度势物质导数单位为 m² s⁻²。该构造假设速度势单值，且撞击前界面光滑。



$$
\begin{gathered}\begin{aligned}
    \nabla\cdot\boldsymbol u=0,\quad\boldsymbol u=\nabla\phi
       &\Rightarrow\nabla\cdot\nabla\phi=\nabla^2\phi=0,\\
    p_l&=p_b+\sigma\kappa,\\
    \partial_t\phi&=p_\infty/\rho-p_l/\rho-|\boldsymbol u|^2/2\\
       &=(p_\infty-p_b-\sigma\kappa)/\rho-|\boldsymbol u|^2/2,\\
    \frac{d\phi(\boldsymbol X(t),t)}{dt}
       &=\partial_t\phi+\frac{d\boldsymbol X}{dt}\cdot\nabla\phi,\\
    \frac{d\boldsymbol X}{dt}=\boldsymbol u&\Rightarrow
       \boldsymbol u\cdot\nabla\phi=|\boldsymbol u|^2,\\
    -|\boldsymbol u|^2/2+|\boldsymbol u|^2&=+|\boldsymbol u|^2/2.
    \end{aligned}\\[6pt]\begin{aligned}
        \boldsymbol u&=\nabla\phi,\qquad\nabla^2\phi=0,\\
        \frac{d\boldsymbol X}{dt}&=\boldsymbol u(\boldsymbol X,t),\\
        \partial_t\phi&=(p_\infty-p_b-\sigma\kappa)/\rho-\tfrac12|\boldsymbol u|^2,\\
        \frac{D\phi}{Dt}&=\partial_t\phi+\boldsymbol u\cdot\nabla\phi\\
          &=(p_\infty-p_b-\sigma\kappa)/\rho+\tfrac12|\boldsymbol u|^2
             \quad(\boldsymbol X\in\Gamma).
        \end{aligned}\end{gathered}
$$


![The interface shape evolves jointly with potential; changing geometry creates focusing.](../assets/figures/c1-e28.svg)

The interface shape evolves jointly with potential; changing geometry creates focusing.

界面形状与速度势共同演化，几何变化产生聚焦。

**Check and interpretation.** Solve-and-advance loop: prescribe initial interface and potential; evaluate pressure input and curvature; solve the harmonic field with interface potential and impermeable-wall normal data; recover velocity; advance interface positions and interface potential; repeat. An outlet supplies its pressure or compatible potential condition. Far-field gauge fixes the additive freedom. Material and Eulerian dynamic conditions are alternative forms. Missing: physical PFC pressure history, phase transfer, contact-line law where applicable, and treatment of topology changes.

**检验与解释。** 求解推进循环：给定初始界面与速度势；计算输入压力和曲率；用界面速度势及不透壁法向条件求解调和场；恢复速度；推进界面位置和界面速度势；重复计算。出口需给定压力或相容速度势条件。远场规范固定加法自由度。物质与欧拉动力学条件为等价表述。缺少：实际 PFC 压力历程、相变传质、适用处的接触线规律及拓扑变化处理。

Check the spherical limit of Eq. (C1-E28). Wall potential is minus radius × wall speed. Curvature is minus two/radius. Differentiate the wall potential and rearrange the squared-speed term. This recovers inviscid Rayleigh–Plesset. Interface penetration then changes topology. Post-penetration flow requires a new domain and pressure-transmission model.

检验式（C1-E28）的球形极限。壁面速度势为半径 × 壁面速度的负值，曲率为负二／半径。对壁面速度势求导并移项速度平方项，可恢复无黏 Rayleigh–Plesset 方程。界面穿透会改变拓扑，之后的流动需要新区域和压力传播模型。

**Derivation.** Test the spatial model against a sphere. Evaluate the potential at its moving wall and differentiate by the product rule. Insert negative cavity curvature into the material dynamic condition. Move squared-speed terms to the same side, reverse signs, then multiply by density.

**推导。** 用球形极限检验空间模型。在运动壁面取速度势，并按乘积法则求导。将负的空腔曲率代入物质动力学条件。把速度平方项移至同侧，变号后再乘密度。

**Symbols before Eq. (C1-E29).**

**式（C1-E29）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\phi_\Gamma$ is the velocity potential evaluated on the spherical interface (m² s⁻¹), with subscript $\Gamma$ the interface label<br>$\phi_\Gamma$ 为球形界面处速度势（m² s⁻¹），下标 $\Gamma$ 标识界面 | $R>0$ is radius (m)<br>$R>0$ 为半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |
| $\kappa$ is signed liquid-to-gas curvature (m⁻¹)<br>$\kappa$ 为液体指向气体约定下的带符号曲率（m⁻¹） | $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $\sigma$ is surface tension (N m⁻¹)<br>$\sigma$ 为表面张力（N m⁻¹） |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $\Gamma$ — Moving liquid–gas interface (—)<br>$\Gamma$ — 运动液—气界面（—） |

**Conventions and conditions.** The potential is differentiated along the wall; viscosity is zero in this check.

**约定与条件。** 速度势沿壁面求导；此检验中黏度为零。

(C1-E29) · Exact spherical recovery of the potential closure / 势流闭合关系对球形模型的精确恢复

$\phi_\Gamma$ is the velocity potential evaluated on the spherical interface (m² s⁻¹), with subscript $\Gamma$ the interface label; $R>0$ is radius (m); $\dot R,\ddot R$ are speed (m s⁻¹) and acceleration (m s⁻²); $\kappa$ is signed liquid-to-gas curvature (m⁻¹); $p_\infty,p_b$ are pressures (Pa); $\sigma$ is surface tension (N m⁻¹); $\rho$ is carrier density (kg m⁻³). The potential is differentiated along the wall; viscosity is zero in this check. $t$ is time (s); $d/dt$ follows the spherical interface.

$\phi_\Gamma$ 为球形界面处速度势（m² s⁻¹），下标 $\Gamma$ 标识界面；$R>0$ 为半径（m）；$\dot R,\ddot R$ 为速度（m s⁻¹）与加速度（m s⁻²）；$\kappa$ 为液体指向气体约定下的带符号曲率（m⁻¹）；$p_\infty,p_b$ 为压力（Pa）；$\sigma$ 为表面张力（N m⁻¹）；$\rho$ 为载液密度（kg m⁻³）。速度势沿壁面求导；此检验中黏度为零。 $t$ 为时间（s）；$d/dt$ 跟随球形界面。



$$
\begin{gathered}\begin{aligned}
    \phi_\Gamma&=-R^2\dot R/R=-R\dot R,\\
    d\phi_\Gamma/dt&=-(\dot R\dot R+R\ddot R),\\
    -R\ddot R-\tfrac32\dot R^2&=(p_\infty-p_b+2\sigma/R)/\rho,\\
    R\ddot R+\tfrac32\dot R^2&=(p_b-p_\infty-2\sigma/R)/\rho.
    \end{aligned}\\[6pt]\begin{aligned}\phi_\Gamma&=-R\dot R,\qquad\kappa=-\frac2R,\\-\dot R^2-R\ddot R&=\frac{p_\infty-p_b+2\sigma/R}{\rho}+\frac12\dot R^2,\\\rho\left(R\ddot R+\frac32\dot R^2\right)&=p_b-p_\infty-\frac{2\sigma}{R}.\end{aligned}\end{gathered}
$$


![The spatial potential formulation returns the spherical model under spherical geometry.](../assets/figures/c1-e29.svg)

The spatial potential formulation returns the spherical model under spherical geometry.

空间势流表述在球形几何下恢复球形模型。

**Check and interpretation.** This recovers the inviscid radial balance with the same capillary sign. The viscous term cannot emerge from an inviscid potential boundary condition. At static equilibrium the Laplace overpressure is recovered.

**检验与解释。** 该结果恢复相同毛细符号的无黏径向平衡。无黏势流边界条件不能产生黏性项。静态极限恢复拉普拉斯过压。

**Derivation.** Derive the communication time from linear acoustics about uniform resting liquid. Linear mass conservation and momentum combine into a wave equation. A disturbance travels the selected path at sound speed. Choose the path from the driven region to the relevant observer. Use the shortest important pressure-rise or change time, rather than automatically using pulse duration. Separately evaluate the wall-speed history.

**推导。** 从均匀静止液体附近的线性声学推导通信时间。将线性质量守恒和动量方程结合，得到波动方程。扰动以声速沿所选路径传播。路径应从驱动区通向相关观察位置。采用最短的重要压力上升或变化时间，不能自动用脉冲总时长代替。另行检验壁面速度历程。

**Symbols before Eq. (C1-E30).**

**式（C1-E30）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $M_w$ is wall Mach number (dimensionless)<br>$M_w$ 为壁面马赫数（无量纲） | $\mathcal C_e$ a pressure-communication ratio (both dimensionless)<br>$\mathcal C_e$ 为压力通信比（两者均无量纲） |
| $\dot R$ is wall speed (m s⁻¹)<br>$\dot R$ 为壁面速度（m s⁻¹） | $c>0$ is carrier sound speed (m s⁻¹)<br>$c>0$ 为载液声速（m s⁻¹） |
| $L_e>0$ is the distance across which loading must communicate (m)<br>$L_e>0$ 为载荷必须传播的距离（m） | $\tau_e>0$ is the event's relevant rise or change time (s)<br>$\tau_e>0$ 为事件相关的上升或变化时间（s） |

**Conventions and conditions.** $|\ |$ denotes magnitude; subscript $e$ labels the selected event scale.

**约定与条件。** $|\ |$ 表示大小；下标 $e$ 标识选定事件尺度。

(C1-E30) · Compressibility applicability diagnostics / 可压缩性适用性诊断

$M_w$ is wall Mach number and $\mathcal C_e$ a pressure-communication ratio (both dimensionless); $\dot R$ is wall speed (m s⁻¹); $c>0$ is carrier sound speed (m s⁻¹); $L_e>0$ is the distance across which loading must communicate (m); $\tau_e>0$ is the event's relevant rise or change time (s); $|\ |$ denotes magnitude; subscript $e$ labels the selected event scale. $\rho_0>0$ is uniform background density (kg m⁻³); primes label small acoustic perturbations, with $\rho'$ density (kg m⁻³), $p'$ pressure (Pa), $\boldsymbol u'$ velocity (m s⁻¹); $\nabla\cdot$ and $\nabla^2$ are spatial divergence and Laplacian; $\partial_t$ is the fixed-position derivative; $t_a$ is one-way travel time (s); ns is 10⁻⁹ s. Linearization assumes inviscid barotropic liquid and constant $c$.

$M_w$ 为壁面马赫数，$\mathcal C_e$ 为压力通信比（两者均无量纲）；$\dot R$ 为壁面速度（m s⁻¹）；$c>0$ 为载液声速（m s⁻¹）；$L_e>0$ 为载荷必须传播的距离（m）；$\tau_e>0$ 为事件相关的上升或变化时间（s）；$|\ |$ 表示大小；下标 $e$ 标识选定事件尺度。 $\rho_0>0$ 为均匀背景密度（kg m⁻³）；撇号标记小幅声学扰动，$\rho'$ 为密度（kg m⁻³），$p'$ 为压力（Pa），$\boldsymbol u'$ 为速度（m s⁻¹）；$\nabla\cdot$ 和 $\nabla^2$ 为空间散度与拉普拉斯；$\partial_t$ 为固定位置导数；$t_a$ 为单程传播时间（s）；ns 为 10⁻⁹ s。线性化假设液体无黏、正压且声速恒定。



$$
\begin{gathered}\begin{aligned}
    \partial_t\rho'+\rho_0\nabla\cdot\boldsymbol u'&=0,\quad
      \rho_0\partial_t\boldsymbol u'=-\nabla p',\quad p'=c^2\rho',\\
    \partial_t^2\rho'+\rho_0\nabla\cdot\partial_t\boldsymbol u'&=0,\quad
      \rho_0\nabla\cdot\partial_t\boldsymbol u'=-\nabla^2p',\\
    \partial_t^2\rho'-\nabla^2p'&=0\Rightarrow\partial_t^2p'=c^2\nabla^2p',\\
    L_e=ct_a&\Rightarrow t_a=L_e/c,\quad\mathcal C_e=t_a/\tau_e,\\
    t_a&=\frac{100\times10^{-6}}{1500}\ \mathrm s=66.6667\ \mathrm{ns},\\
    \tau_e=10\ \mathrm{ns}&\Rightarrow\mathcal C_e=66.6667/10=6.66667,\\
    \tau_e=1\ \mu\mathrm s=1000\ \mathrm{ns}&\Rightarrow\mathcal C_e=66.6667/1000=0.0666667,\\
    |\dot R|=15\ \mathrm{m\,s^{-1}}&\Rightarrow M_w=15/1500=0.01\quad\text{in both cases}.
    \end{aligned}\\[6pt]\begin{gathered}M_w=\frac{|\dot R|}{c}\\ \mathcal C_e=\frac{L_e}{c\tau_e}\end{gathered}\end{gathered}
$$


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

**Derivation.** Reconstruct the causal chain before answering. Subtract far-field pressure from the normal traction law, equate it to radial inertia, then solve for acceleration. The mixture statement identifies the missing source input. Follow the full Euler-to-Bernoulli derivation in C1-E05 and energy conversion in C1-E11. For a directional outlet, replace the scalar radial solution with C1-E26–C1-E28 and the actual boundaries.

**推导。** 作答前重建因果链。从法向牵引关系减去远场压力，将其与径向惯性相等，再求加速度。混合物关系指出缺失的源输入。完整欧拉至伯努利推导见 C1-E05，能量转换见 C1-E11。存在定向出口时，用 C1-E26–C1-E28 及实际边界替代标量径向解。

**Symbols before Eq. (C1-E31).**

**式（C1-E31）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $R>0$ is cavity radius (m)<br>$R>0$ 为空腔半径（m） |
| $\dot R$ — Wall radial velocity (m s⁻¹)<br>$\dot R$ — 壁面径向速度（m s⁻¹） | $\ddot R$ — Wall radial acceleration (m s⁻²)<br>$\ddot R$ — 壁面径向加速度（m s⁻²） |
| $p_b$ — Uniform bubble absolute pressure (Pa)<br>$p_b$ — 均匀气泡绝对压力（Pa） | $p_\infty$ — Far-field absolute pressure (Pa)<br>$p_\infty$ — 远场绝对压力（Pa） |
| $\sigma$ is surface tension (N m⁻¹)<br>$\sigma$ 为表面张力（N m⁻¹） | $\mu$ is viscosity (Pa s)<br>$\mu$ 为黏度（Pa s） |
| $p_{v,\mathrm{PFC}}$ — PFC-vapor partial pressure (Pa)<br>$p_{v,\mathrm{PFC}}$ — PFC 蒸气分压（Pa） | $p_{v,w}$ — Water-vapor partial pressure (Pa)<br>$p_{v,w}$ — 水蒸气分压（Pa） |
| $p_g$ — Noncondensable-gas partial pressure (Pa)<br>$p_g$ — 非凝结气体分压（Pa） |  |

**Conventions and conditions.** The equations are the spherical mechanical balance and the pressure-composition closure target.

**约定与条件。** 两式分别为球形力学平衡与需要闭合的压力组成。

(C1-E31) · Original formulas quoted for defense 1 / 答辩问题 1 引用的原始公式

$\rho$ is carrier density (kg m⁻³); $R>0$ is cavity radius (m); $\dot R,\ddot R$ are wall speed (m s⁻¹) and acceleration (m s⁻²); $p_b,p_\infty$ are total bubble and far-field pressures (Pa); $\sigma$ is surface tension (N m⁻¹); $\mu$ is viscosity (Pa s); $p_{v,\mathrm{PFC}},p_{v,w},p_g$ are PFC-vapor, water-vapor and permanent-gas partial pressures (Pa). The equations are the spherical mechanical balance and the pressure-composition closure target. $p_l$ is liquid-side wall pressure (Pa).

$\rho$ 为载液密度（kg m⁻³）；$R>0$ 为空腔半径（m）；$\dot R,\ddot R$ 为壁面速度（m s⁻¹）与加速度（m s⁻²）；$p_b,p_\infty$ 为气泡总压力与远场压力（Pa）；$\sigma$ 为表面张力（N m⁻¹）；$\mu$ 为黏度（Pa s）；$p_{v,\mathrm{PFC}},p_{v,w},p_g$ 为 PFC 蒸气、水蒸气与非凝结气体分压（Pa）。两式分别为球形力学平衡与需要闭合的压力组成。 $p_l$ 为壁面液体侧压力（Pa）。



$$
\begin{gathered}\begin{aligned}
    p_l-p_\infty&=p_b-p_\infty-2\sigma/R-4\mu\dot R/R,\\
    p_l-p_\infty&=\rho R\ddot R+\tfrac32\rho\dot R^2,\\
    \rho R\ddot R&=p_b-p_\infty-2\sigma/R-4\mu\dot R/R-\tfrac32\rho\dot R^2,\\
    \ddot R&=\frac{p_b-p_\infty-2\sigma/R-4\mu\dot R/R-\tfrac32\rho\dot R^2}{\rho R}.
    \end{aligned}\\[6pt]\begin{gathered}\rho\left(R\ddot R+\frac32\dot R^2\right)=p_b-p_\infty-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}\\ p_b=p_{v,\mathrm{PFC}}+p_{v,w}+p_g\end{gathered}\end{gathered}
$$


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

**Derivation.** Reproduce the collapse chain rather than memorize its coefficient. Use squared speed and the integrating factor from C1-E13. Apply the initial condition as in C1-E14. Integrate reciprocal inward speed as in C1-E15–C1-E16. Obtain energy independently from pressure work in C1-E17. Check the chosen Mach cutoff using C1-E19 before interpreting the singular trajectory.

**推导。** 重现塌缩推导链，不能背诵系数。采用 C1-E13 的速度平方和积分因子。按 C1-E14 施加初始条件。按 C1-E15–C1-E16 积分向内速度倒数。按 C1-E17 独立用压力功求能量。解释奇异轨迹前，先用 C1-E19 检查选定马赫截止条件。

**Symbols before Eq. (C1-E32).**

**式（C1-E32）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\dot R\le0$ is inward wall velocity (m s⁻¹)<br>$\dot R\le0$ 为向内壁面速度（m s⁻¹） | $R\in(0,R_{\max}]$ — Instantaneous cavity radius (m)<br>$R\in(0,R_{\max}]$ — 瞬时空腔半径（m） |
| $R_{\max}$ — Radius at the start of ideal collapse (m)<br>$R_{\max}$ — 理想塌缩开始时的半径（m） | $\Delta p_c>0$ is constant collapse pressure (Pa)<br>$\Delta p_c>0$ 为常数塌缩压差（Pa） |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $t_c$ is ideal collapse time (s)<br>$t_c$ 为理想塌缩时间（s） |
| $B$ is the dimensionless beta function defined in Eq<br>$B$ 为式（C1-E17）定义的无量纲贝塔函数 | $K_l$ is carrier kinetic energy (J)<br>$K_l$ 为载液动能（J） |
| $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |  |

**Conventions and conditions.** (C1-E17); The initial cavity is at rest, with no gas, viscosity, capillarity or compressibility.

**约定与条件。** 初始空腔静止，并忽略非凝结气体、黏性、毛细及可压缩性。

(C1-E32) · Original formulas quoted for defense 2 / 答辩问题 2 引用的原始公式

$\dot R\le0$ is inward wall velocity (m s⁻¹); $R\in(0,R_{\max}]$ and $R_{\max}$ are current and maximum radii (m); $\Delta p_c>0$ is constant collapse pressure (Pa); $\rho$ is carrier density (kg m⁻³); $t_c$ is ideal collapse time (s); $B$ is the dimensionless beta function defined in Eq. (C1-E16); $K_l$ is carrier kinetic energy (J); $\pi$ is the circle constant. The initial cavity is at rest, with no gas, viscosity, capillarity or compressibility. $y$ is squared speed (m² s⁻²); $x=R/R_{\max}$ is dimensionless radius; $V_b=4\pi R^3/3$ and $V_{\max}=4\pi R_{\max}^3/3$ are volumes (m³); $V$ is dummy volume (m³).

$\dot R\le0$ 为向内壁面速度（m s⁻¹）；$R\in(0,R_{\max}]$ 与 $R_{\max}$ 为当前与最大半径（m）；$\Delta p_c>0$ 为常数塌缩压差（Pa）；$\rho$ 为载液密度（kg m⁻³）；$t_c$ 为理想塌缩时间（s）；$B$ 为式（C1-E16）定义的无量纲贝塔函数；$K_l$ 为载液动能（J）；$\pi$ 为圆周率。初始空腔静止，并忽略非凝结气体、黏性、毛细及可压缩性。 $y$ 为速度平方（m² s⁻²）；$x=R/R_{\max}$ 为无量纲半径；$V_b=4\pi R^3/3$ 与 $V_{\max}=4\pi R_{\max}^3/3$ 为体积（m³）；$V$ 为积分哑体积（m³）。



$$
\begin{gathered}\begin{aligned}
    y&=\dot R^2,\quad\frac{d(R^3y)}{dR}=-2\Delta p_cR^2/\rho,\\
    R^3y-0&=-\frac{2\Delta p_c}{3\rho}(R^3-R_{\max}^3),\\
    \dot R&=-\sqrt{y},\quad
    t_c=R_{\max}\sqrt{\frac{3\rho}{2\Delta p_c}}\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx,\\
    K_l&=\int_{V_{\max}}^{V_b}-\Delta p_c\,dV=\Delta p_c(V_{\max}-V_b).
    \end{aligned}\\[6pt]\begin{gathered}\dot R=-\sqrt{\frac{2\Delta p_c}{3\rho}\left[\left(\frac{R_{\max}}R\right)^3-1\right]}\\ t_c=\frac{B(5/6,1/2)}{\sqrt6}R_{\max}\sqrt{\frac\rho{\Delta p_c}}\\ K_l=\frac{4\pi}{3}\Delta p_c(R_{\max}^3-R^3)\end{gathered}\end{gathered}
$$


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

**Derivation.** Start with the exact time-integrated momentum in C1-E21. Apply C1-E22 conditions before discarding residual integrals. Use C1-E23 endpoint data to solve the spatial impulse field. C1-E30 separately tests communication using rise time. These steps determine an initial velocity increment; subsequent jet shape requires the moving-interface solve.

**推导。** 从 C1-E21 的精确时间积分动量出发。先检查 C1-E22 条件，再舍去残余积分。采用 C1-E23 的端点条件求空间冲量场。C1-E30 用上升时间单独检验通信。这些步骤确定初始速度增量；后续射流形状仍需运动界面求解。

**Symbols before Eq. (C1-E33).**

**式（C1-E33）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Pi$ is local pressure impulse (Pa s)<br>$\Pi$ 为局部压力冲量（Pa s） | $\boldsymbol x$ is fixed position (m)<br>$\boldsymbol x$ 为固定位置（m） |
| $t$ — Elapsed time (s)<br>$t$ — 经过时间（s） | $t_0$ — Event start time (s)<br>$t_0$ — 事件开始时刻（s） |
| $t_1$ — Event end time (s)<br>$t_1$ — 事件结束时刻（s） | $p$ — Liquid pressure field (Pa)<br>$p$ — 液体压力场（Pa） |
| $p_{\mathrm{ref}}$ — Spatially uniform reference pressure (Pa)<br>$p_{\mathrm{ref}}$ — 空间均匀参考压力（Pa） | $\Delta\boldsymbol u$ is liquid speed change (m s⁻¹)<br>$\Delta\boldsymbol u$ 为液体速度变化（m s⁻¹） |
| $\rho$ is carrier density (kg m⁻³)<br>$\rho$ 为载液密度（kg m⁻³） | $U_{\mathrm{column}}$ is the ideal straight-column speed increment (m s⁻¹)<br>$U_{\mathrm{column}}$ 为理想直液柱速度增量（m s⁻¹） |
| $\Pi_0$ is driven-end impulse (Pa s)<br>$\Pi_0$ 为受驱动端冲量（Pa s） | $L$ is column length (m)<br>$L$ 为液柱长度（m） |
| $t_a$ is crossing time (s)<br>$t_a$ 为传播时间（s） | $c$ is sound speed (m s⁻¹)<br>$c$ 为声速（m s⁻¹） |

**Conventions and conditions.** $\nabla,\nabla^2$ denote spatial gradient and Laplacian; The reduced momentum formula needs a frozen geometry and small omitted impulses.

**约定与条件。** $\nabla,\nabla^2$ 为空间梯度与拉普拉斯；约化动量公式要求冻结几何，且被忽略的冲量项较小。

(C1-E33) · Original formulas quoted for defense 3 / 答辩问题 3 引用的原始公式

$\Pi$ is local pressure impulse (Pa s); $\boldsymbol x$ is fixed position (m); $t,t_0,t_1$ are time and interval endpoints (s); $p,p_{\mathrm{ref}}$ are local and spatially uniform reference pressures (Pa); $\Delta\boldsymbol u$ is liquid speed change (m s⁻¹); $\nabla,\nabla^2$ denote spatial gradient and Laplacian; $\rho$ is carrier density (kg m⁻³); $U_{\mathrm{column}}$ is the ideal straight-column speed increment (m s⁻¹); $\Pi_0$ is driven-end impulse (Pa s); $L$ is column length (m); $t_a$ is crossing time (s); $c$ is sound speed (m s⁻¹). The reduced momentum formula needs a frozen geometry and small omitted impulses. $\boldsymbol u$ is velocity (m s⁻¹); $\nu$ is kinematic viscosity (m² s⁻¹); $U$ is a characteristic speed (m s⁻¹); $\tau=t_1-t_0$ is event duration (s); $z\in[0,L]$ is column coordinate (m); $\Delta u_z$ is axial speed increment (m s⁻¹); $\ll$ is an asymptotic smallness condition.

$\Pi$ 为局部压力冲量（Pa s）；$\boldsymbol x$ 为固定位置（m）；$t,t_0,t_1$ 为时间与区间端点（s）；$p,p_{\mathrm{ref}}$ 为局部压力与空间均匀参考压力（Pa）；$\Delta\boldsymbol u$ 为液体速度变化（m s⁻¹）；$\nabla,\nabla^2$ 为空间梯度与拉普拉斯；$\rho$ 为载液密度（kg m⁻³）；$U_{\mathrm{column}}$ 为理想直液柱速度增量（m s⁻¹）；$\Pi_0$ 为受驱动端冲量（Pa s）；$L$ 为液柱长度（m）；$t_a$ 为传播时间（s）；$c$ 为声速（m s⁻¹）。约化动量公式要求冻结几何，且被忽略的冲量项较小。 $\boldsymbol u$ 为速度（m s⁻¹）；$\nu$ 为运动黏度（m² s⁻¹）；$U$ 为特征速度（m s⁻¹）；$\tau=t_1-t_0$ 为事件时长（s）；$z\in[0,L]$ 为液柱坐标（m）；$\Delta u_z$ 为轴向速度增量（m s⁻¹）；$\ll$ 表示渐近很小条件。



$$
\begin{gathered}\begin{aligned}
    \Delta\boldsymbol u&=-\nabla\Pi/\rho
       -\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt
       +\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt,\\
    U\tau/L\ll1,\quad\nu\tau/L^2\ll1
       &\Rightarrow\Delta\boldsymbol u\simeq-\nabla\Pi/\rho,\\
    \nabla\cdot\Delta\boldsymbol u=0&\Rightarrow\nabla^2\Pi=0,\\
    \Pi(0)=\Pi_0,\quad\Pi(L)=0&\Rightarrow\Pi(z)=\Pi_0(1-z/L),\\
    \Delta u_z&=-\frac1\rho\frac{d\Pi}{dz}=\frac{\Pi_0}{\rho L}.
    \end{aligned}\\[6pt]\begin{gathered}\Pi(\boldsymbol x)=\int_{t_0}^{t_1}(p-p_{\mathrm{ref}})dt\\\Delta\boldsymbol u\simeq-\frac{\nabla\Pi}{\rho},\quad\nabla^2\Pi=0\\ U_{\mathrm{column}}=\frac{\Pi_0}{\rho L},\quad t_a=\frac Lc\end{gathered}\end{gathered}
$$


![The impulse benchmark gives an early velocity field, followed by a moving-interface problem.](../assets/figures/c1-e33.svg)

The impulse benchmark gives an early velocity field, followed by a moving-interface problem.

冲量基准给出早期速度场，之后还需解运动界面问题。

**Check and interpretation.** Falsification question: does the observer stay liquid, and are geometry motion, residual impulses and acoustic rise effects small? Report location, duration, geometry and reference pressure with every impulse. Equal scalar peaks cannot determine the spatial gradient.

**检验与解释。** 证伪问题：观察点是否始终位于液体内，几何运动、残余冲量和声学上升效应是否足够小？报告每个冲量时须给出位置、时长、几何及参考压力。相同标量峰值不能确定空间梯度。

Specify driven boundary, outlet, meniscus and receiver geometry. Integrate pressure over time at every location. Equal peaks can have different durations and impulses. Equal scalar impulses can produce different spatial gradients. The gradient sets early velocity. Boundary conditions determine that gradient. A uniform impulse addition causes no acceleration.

规定受驱边界、出口、弯月面及受载几何。在每个位置对压力作时间积分。相同峰值可对应不同时长和冲量，相同标量冲量可产生不同空间梯度。梯度决定早期速度，边界条件决定梯度。均匀增加冲量不产生加速度。

The column gives 0.30 Pa s and 3.0 m s⁻¹. Its separate crossing time is 0.0667 μs. The total duration spans 7.5 acoustic crossings. Its ideal rectangular fronts have zero rise time. Communication at those fronts requires an acoustic model. A finite physical rise time needs the separate C1-E30 test. Uniform pressure remains unestablished. Check displacement, convection and viscosity. Then evolve the interface with pressure, stress and contact-line conditions. Focusing follows from that spatial evolution and thermodynamic pressure history. Rapid changes or impact can require compressibility at low bulk speed.

液柱给出 0.30 Pa s 与 3.0 m s⁻¹，传播时间另为 0.0667 μs。总时长包含 7.5 次声穿越。理想矩形波前上升时间为零，波前通信需要声学模型。实际有限上升时间需单独应用 C1-E30 检验。均匀压力仍未确立。先检查位移、对流及黏性，再结合压力、应力和接触线条件演化界面。聚焦取决于空间演化及热力学压力历程。快速变化或撞击时，即使总体速率低也可能需要可压缩性。

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