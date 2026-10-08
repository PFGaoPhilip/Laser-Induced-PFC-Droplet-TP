# Appendix A: Hydrogel versus liquid platforms

# 附录 A：水凝胶与液体平台

## The question is whether gel improves complete transfer

## 问题在于凝胶是否改善完整转印过程

A hydrogel can preserve the position of PFC droplets, support a patterned liquid reservoir, and conform to a payload at small preload. It also adds a polymer network that stores energy, dissipates motion, changes heat and mass transport, and may tear. This appendix evaluates those changes through the same chain as the preceding chapters: absorbed energy → finite phase source → mechanical motion → intended interface release → intact placement and reset. A smaller cavity or a larger pressure peak alone does not establish improvement.

水凝胶可以保持 PFC 液滴的位置、支撑图案化液体储库，并在小预载下贴合被转印对象。它同时引入聚合物网络，该网络会储存能量、耗散运动、改变传热传质，并可能撕裂。本附录沿用前面各章的链条评估这些变化：吸收能量 → 有限相变源 → 力学运动 → 目标界面释放 → 完整定位与复位。仅凭腔体更小或压力峰值更大，不能证明性能改善。

| Architecture<br>结构方案 | Where displaced material can go<br>被排开材料的去向 | Benefit to test; new cost<br>待检验的收益与新增代价 |
| --- | --- | --- |
| Conventional liquid site containing PFC<br>含 PFC 的常规液体位点 | Toward an exposed meniscus or defined outlet; the carrier remains a liquid.<br>朝暴露液面或明确出口运动；载液保持液体状态。 | Direct liquid displacement; wetting drift, spreading and neighboring flows can vary.<br>直接排开液体；润湿漂移、铺展和邻近流动可能发生变化。 |
| Open liquid pocket supported by gel<br>凝胶支撑的开放液腔 | Liquid leaves an opening while the gel wall deforms.<br>液体经开口离开，同时凝胶壁发生变形。 | A located outlet and compliant support; moving walls consume, return or redirect energy.<br>定位出口与柔顺支撑；运动壁面会消耗、返还能量或改变其方向。 |
| PFC embedded directly in bulk gel<br>PFC 直接嵌入体相凝胶 | Initially into network deformation; an external liquid path must exist or be created.<br>起初转化为网络变形；必须已有或形成通往外部的液体路径。 | Stable inclusion locations; large strain, trapped vapor, network rupture and solid contamination.<br>稳定的夹杂位置；大应变、滞留蒸气、网络破裂及固体污染。 |
| Sealed cavity under a gel/composite stamp<br>凝胶／复合印章下的密封腔体 | Boundary bulging and pressure transmission rather than an open liquid outlet.<br>通过边界鼓起与压力传递，而不是开放液体出口。 | Distributed deformation and local peeling; this can be a blister actuator with a different release mechanism.<br>分布式变形与局部剥离；它可以是具有不同释放机制的鼓泡致动器。 |

Li and colleagues demonstrated a sealed hydrogel-composite stamp in which laser heating creates a water-vapor cavity, deforms covering layers, and releases a platelet. It supports the pressure–deformation–fracture route; it does not verify a coherent jet from PFC embedded in bulk gel. Its millisecond heating event must not supply a microsecond PFC constitutive law by analogy. [[R11]](../reference/sources.html#r11)

Li 等人展示了密封水凝胶复合印章：激光加热产生水蒸气腔体，使覆盖层变形并释放片状对象。该研究支持压力—变形—断裂路径，却没有验证体相凝胶中嵌入 PFC 后产生相干射流。不能仅凭类比，用其毫秒级加热事件提供微秒级 PFC 过程的本构规律。[[R11]](../reference/sources.html#r11)

## 1. Declare the intact spherical control

## 1. 明确完整球形控制模型

The analytical control is an infinite, homogeneous, isotropic, incompressible medium with a continuous unbroken neo-Hookean network. An existing spherical cavity has stress-free reference radius $R_{\mathrm{ref}}>0$ and current radius $R(t)>0$. Material occupies the exterior of the cavity. Far-field total radial stress is $-p_\infty(t)$, the gas/liquid cavity pressure is spatially uniform $p_b(t)$, and the interfacial tension is constant $\sigma$. Tensile Cauchy stress is positive. The radial coordinate points from the cavity center outward; positive wall speed means expansion. No gravity, nearby boundary, outlet, solvent drainage, damage, shell stress or material phase slip is resolved.

解析控制模型采用无限、均匀、各向同性、不可压缩介质，包含连续且未破坏的 neo-Hookean 网络。已有球形空腔的无应力参考半径为 $R_{\mathrm{ref}}>0$，当前半径为 $R(t)>0$。材料位于空腔外部。远场总径向应力为 $-p_\infty(t)$，腔内气体／液体压力 $p_b(t)$ 在空间上均匀，界面张力 $\sigma$ 为常数。拉伸 Cauchy 应力取正。径向坐标从空腔中心向外，泡壁速度为正表示膨胀。模型不解析重力、附近边界、出口、溶剂排水、损伤、壳层应力或材料相间滑移。

At initial time $t=0$, take $R=R_{\mathrm{ref}}$, $\dot R=0$ and an unstretched network. A constant-tension interface requires $p_b(0)-p_\infty(0)=2\sigma/R_{\mathrm{ref}}$ for this initial mechanical equilibrium. A subsequent laser/phase calculation supplies $p_b(t)$; the elastic calculation does not derive it. If the network was polymerized around a loaded inclusion, the stress-free configuration may differ from its observed initial shape. The initial liquid-PFC core radius $a_0$ is an inventory variable and is not silently identified with $R_{\mathrm{ref}}$ or with the evolving vapor-cavity radius.

初始时刻 $t=0$ 取 $R=R_{\mathrm{ref}}$、$\dot R=0$，网络没有伸长。若界面张力为常数，该初始力学平衡要求 $p_b(0)-p_\infty(0)=2\sigma/R_{\mathrm{ref}}$。后续激光／相变计算提供 $p_b(t)$；弹性计算不会推导这个压力。若网络围绕受载夹杂进行聚合，其无应力构形可能不同于观测到的初始形状。初始液态 PFC 核半径 $a_0$ 是描述物质量的变量，不能默默将其等同于 $R_{\mathrm{ref}}$ 或不断演化的蒸气空腔半径。

| Symbol<br>符号 | Physical meaning<br>物理意义 | SI units<br>SI 单位 | Role and convention<br>作用与约定 |
| --- | --- | --- | --- |
| $t$ | Time<br>时间 | s | Independent coordinate of the transient cavity event; the reference state is specified at zero.<br>瞬态腔体事件的独立坐标；参考状态规定在零时刻。 |
| $r_0$ | Reference material radial coordinate<br>参考材料径向坐标 | m | Labels a material shell in the stress-free configuration; held fixed for material motion.<br>标识无应力构形中的材料壳层；追踪材料运动时保持不变。 |
| $r$ | Current material radial coordinate<br>当前材料径向坐标 | m | Current position of the shell labeled by r₀; distinct from current wall radius R.<br>由 r₀ 标识的壳层当前所在位置；不同于当前壁面半径 R。 |
| $R_{\mathrm{ref}}$ | Stress-free reference cavity radius<br>无应力参考腔体半径 | m | Reference geometry for network stretch; not automatically an observed loaded cavity radius.<br>网络伸长的参考几何；不能自动等同于观测到的受载腔体半径。 |
| $R$ | Current cavity radius<br>当前腔体半径 | m | Locates the moving cavity boundary in the current configuration.<br>定位当前构形中的运动腔体边界。 |
| $\dot R$ | Cavity wall radial velocity<br>腔体壁面径向速度 | m s⁻¹ | First time derivative of R; positive expansion and negative inward motion.<br>R 的一阶时间导数；正值表示膨胀，负值表示向内运动。 |
| $\ddot R$ | Cavity wall radial acceleration<br>腔体壁面径向加速度 | m s⁻² | Second time derivative of R in the inertial radial balance.<br>惯性径向平衡中的 R 的二阶时间导数。 |
| $a_0$ | Initial liquid-PFC core radius<br>初始液态 PFC 核半径 | m | Inventory geometry; neither R nor the network reference radius is silently substituted for it.<br>存量几何；不能默默用 R 或网络参考半径替代它。 |
| $\lambda_r$ | Radial principal stretch<br>径向主伸长 | 1 | Ratio of current to reference radial line elements at a material shell.<br>材料壳层处当前与参考径向线元的比值。 |
| $\lambda_\theta$ | First tangential principal stretch<br>第一切向主伸长 | 1 | Circumferential line-element ratio in the θ direction.<br>θ 方向周向线元的比值。 |
| $\lambda_\phi$ | Second tangential principal stretch<br>第二切向主伸长 | 1 | Circumferential line-element ratio in the φ direction; equals the other tangential stretch under spherical symmetry.<br>φ 方向周向线元的比值；在球对称下等于另一切向伸长。 |
| $\mathbf F$ | Deformation-gradient tensor<br>变形梯度张量 | 1 | Maps reference line elements into the current configuration.<br>将参考线元映射到当前构形。 |
| $\mathbf B$ | Left Cauchy–Green tensor<br>左 Cauchy—Green 张量 | 1 | Product of deformation gradient and its transpose; enters the neo-Hookean stress.<br>变形梯度与其转置的乘积；进入 neo-Hookean 应力。 |
| $G_g$ | Gel-network shear modulus<br>凝胶网络剪切模量 | Pa | Elastic material parameter controlling stored network resistance; relevant strain/rate dependence must be validated.<br>控制所储存网络阻力的弹性材料参数；相关应变／速率依赖需验证。 |
| $\eta_g$ | Represented Kelvin–Voigt viscosity<br>所描述的 Kelvin—Voigt 黏度 | Pa s | Coefficient of the adopted viscous stress; avoid counting the same solvent dissipation twice.<br>所采用黏性应力的系数；避免对同一溶剂耗散重复计数。 |
| $\rho_g$ | Effective medium mass density<br>有效介质质量密度 | kg m⁻³ | Density of the moving surrounding medium, not the PFC core or vapor alone.<br>周围运动介质的密度，不是单独的 PFC 核或蒸气密度。 |
| $\sigma$ | Cavity-interface tension<br>腔体界面张力 | N m⁻¹ | Constant coefficient for the declared interface; separate from network elastic stress.<br>指定界面的恒定系数；与网络弹性应力不同。 |
| $\mathbf T^e$ | Elastic Cauchy-stress tensor<br>弹性 Cauchy 应力张量 | Pa | Tensile-positive stress contributed by the network constitutive law; e denotes elasticity.<br>网络本构规律产生的应力，拉伸为正；e 表示弹性。 |
| $\mathbf T$ | Total Cauchy-stress tensor<br>总 Cauchy 应力张量 | Pa | Includes elastic and represented viscous contributions in the radial momentum balance.<br>包含径向动量平衡中的弹性及所描述黏性贡献。 |
| $\chi$ | Incompressibility multiplier<br>不可压缩约束乘子 | Pa | Unknown isotropic stress multiplier; unlike Chapter 3’s interaction parameter, it has pressure units here.<br>未知各向同性应力乘子；与第三章的相互作用参数不同，此处具有压力单位。 |
| $p_b$ | Uniform cavity absolute pressure<br>均匀腔内绝对压力 | Pa | Supplied by the laser/phase source calculation, not derived from the elastic resistance.<br>由激光／相变源计算提供，不由弹性阻力推导。 |
| $p_\infty$ | Far-field absolute pressure<br>远场绝对压力 | Pa | Sets the exterior radial-traction condition under the stated stress convention.<br>在指定应力约定下确定外部径向牵引条件。 |
| $p_{\mathrm{el}}$ | Signed elastic cavity resistance<br>带符号弹性腔体阻力 | Pa | Stress-difference integral resisting expansion; its intact-network formula is not a fracture threshold.<br>抵抗膨胀的应力差积分；其完整网络公式不是断裂阈值。 |
| $u_r$ | Radial material velocity<br>材料径向速度 | m s⁻¹ | Velocity of the surrounding material, consistent with the stated no-phase-slip control.<br>周围材料的速度，与所声明无相间滑移对照一致。 |
| $\mathbf D$ | Symmetric velocity-gradient tensor<br>对称速度梯度张量 | s⁻¹ | Strain-rate tensor used by the represented viscous constitutive law.<br>所描述黏性本构规律使用的应变率张量。 |
| $W_g$ | Stored network elastic work<br>储存的网络弹性功 | J | Integrated recoverable network work measured from the stress-free reference cavity.<br>从无应力参考腔体起算的可恢复网络功积分。 |
| $K_g$ | Surrounding-medium kinetic energy<br>周围介质动能 | J | Integrated energy of the radial exterior motion.<br>外部径向运动能量的积分。 |
| $E_\sigma$ | Cavity surface energy<br>腔体表面能 | J | Interface-area energy under the declared constant-tension assumption.<br>指定恒张力假设下的界面面积能量。 |
| $P_{\mathrm{dis}}$ | Nonnegative viscous dissipation power<br>非负黏性耗散功率 | W | Rate of irreversible mechanical-energy loss; differs from recoverable storage.<br>不可逆力学能损失速率；不同于可恢复储能。 |
| $\tau_e$ | Event duration<br>事件持续时间 | s | Specified loading/evolution time used to test material-response assumptions.<br>检验材料响应假设采用的指定受载／演化时间。 |
| $\tau_{\mathrm{rel}}$ | Measured stress-relaxation time<br>测量的应力松弛时间 | s | Independently identified memory time; not Kelvin–Voigt retardation time.<br>独立确定的记忆时间；不是 Kelvin—Voigt 延迟时间。 |
| $L_g$ | Specified gel communication length<br>指定凝胶传播长度 | m | Distance over which shear support or solvent drainage must communicate.<br>剪切支撑或溶剂排水需要传播的距离。 |
| $\mathrm{De}$ | Deborah number<br>Deborah 数 | 1 | Stress-relaxation time divided by event duration in the declared memory test.<br>在指定记忆检验中为应力松弛时间除以事件持续时间。 |
| $t_s$ | Shear communication time<br>剪切传播时间 | s | Small-disturbance elastic communication scale over Lg; not a universal cavity-collapse time.<br>跨越 Lg 的小扰动弹性传播尺度；不是通用腔体塌缩时间。 |
| $t_{\mathrm{poro}}$ | Poroelastic drainage time scale<br>孔弹性排水时间尺度 | s | Diffusion-scale solvent/network pressure equilibration under the stated linear approximation.<br>在指定线性近似下溶剂／网络压力平衡的扩散时间尺度。 |

Ordinary powers, scalar products and comparisons use their usual meanings; subscripts name directions, materials or states. $d/dr$ is a derivative in current radius, $\partial/\partial$ holds other independent coordinates fixed, $\int$ is a definite integral with its written limits, $\lim$ is a limit, and $\pi$ is the dimensionless circle constant. All local symbol declarations below repeat the quantities actually displayed. Gaudron, Warnez and Johnsen provide the nonlinear-elastic cavity framework; the intermediate transformations and work evaluation here are derived explicitly for this stated control. [[R13]](../reference/sources.html#r13)

普通幂、标量乘积和比较沿用通常意义；下标表示方向、材料或状态。$d/dr$ 表示对当前径向位置求导，$\partial/\partial$ 表示保持其他独立坐标不变的偏导，$\int$ 表示采用所写上下限的定积分，$\lim$ 表示极限，$\pi$ 为无量纲圆周率。下文每处局部符号声明都重复定义实际显示的量。Gaudron、Warnez 和 Johnsen 提供了非线性弹性空腔的理论框架；这里针对已声明的控制模型，显式推导中间变换及功的计算。[[R13]](../reference/sources.html#r13)

## 2. Derive the elastic pressure rather than inserting it

## 2. 推导弹性压力，而不是直接代入

Step 1 — exact volume conservation. Follow one material shell from its reference radius to its present radius. Incompressibility equates the material volume between the cavity and that shell. Differentiate at fixed time to obtain the radial stretch; divide only by strictly positive radii.

步骤 1——精确的体积守恒。跟踪一个材料球壳从参考位置到当前位置。不可压缩性要求腔体与球壳之间的材料体积相等。在固定时刻求导即可得到径向伸长；只有严格为正的半径才进行除法。

**Symbols before Eq. (A-E01).**

**式（A-E01）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $r_0\geq R_{\mathrm{ref}}>0$ — Reference material radius (m)<br>$r_0\geq R_{\mathrm{ref}}>0$ — 参考物质半径（m） | $r\geq R>0$ — Current material radius (m)<br>$r\geq R>0$ — 当前物质半径（m） |
| $R_{\mathrm{ref}}$ — Stress-free reference cavity radius (m)<br>$R_{\mathrm{ref}}$ — 无应力参考腔体半径（m） | $R$ — Current cavity radius (m)<br>$R$ — 当前腔体半径（m） |
| $\lambda_r$ — Radial principal stretch (dimensionless)<br>$\lambda_r$ — 径向主伸长比（无量纲） | $\lambda_\theta$ — Polar tangential principal stretch (dimensionless)<br>$\lambda_\theta$ — 极角切向主伸长比（无量纲） |
| $\lambda_\phi$ — Azimuthal tangential principal stretch (dimensionless)<br>$\lambda_\phi$ — 方位角切向主伸长比（无量纲） | $\theta$ — Polar tangential coordinate label (—)<br>$\theta$ — 极角切向坐标标记（—） |
| $\phi$ — Azimuthal tangential coordinate label (—)<br>$\phi$ — 方位角切向坐标标记（—） |  |

**Conventions and conditions.** $\partial r/\partial r_0$ is the derivative with respect to the reference material coordinate at fixed time.

**约定与条件。** $\partial r/\partial r_0$ 表示构形映射中固定时刻的材料坐标导数。

(A-E01) · Exact kinematics under incompressibility

$$
\begin{aligned}r^3-R^3&=r_0^3-R_{\mathrm{ref}}^3,\\3r^2\frac{\partial r}{\partial r_0}&=3r_0^2,\\\lambda_r:=\frac{\partial r}{\partial r_0}&=\frac{r_0^2}{r^2},\qquad\lambda_\theta=\lambda_\phi=\frac{r}{r_0},\\\lambda_r\lambda_\theta\lambda_\phi&=1.\end{aligned}
$$


![The same network shell moves outward while thinning radially and stretching tangentially.](../assets/figures/a-e01.svg)

The same network shell moves outward while thinning radially and stretching tangentially.

同一网络球壳向外移动，同时径向变薄、切向伸长。

Step 2 — declared constitutive law. In principal directions the neo-Hookean Cauchy stress is a common incompressibility multiplier plus a stretch-dependent part. Subtract radial from tangential stress to eliminate that unknown multiplier. This is a material model, not a universal hydrogel law.

步骤 2——明确采用的本构规律。在主方向上，neo-Hookean Cauchy 应力由共同的不可压缩约束乘子及依赖伸长的部分组成。用切向应力减去径向应力，消除未知约束乘子。这是材料模型，不是普适的水凝胶定律。

**Symbols before Eq. (A-E02).**

**式（A-E02）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\mathbf T^e$ — Elastic Cauchy stress tensor, tension positive (Pa)<br>$\mathbf T^e$ — 拉伸取正的弹性柯西应力张量（Pa） | $\chi$ is the incompressibility multiplier (Pa)<br>$\chi$ 为不可压缩约束乘子（Pa） |
| $\mathbf I$ is the dimensionless identity tensor<br>$\mathbf I$ 为无量纲单位张量 | $G_g>0$ is network shear modulus (Pa)<br>$G_g>0$ 为网络剪切模量（Pa） |
| $\mathbf F$ is the dimensionless deformation gradient<br>$\mathbf F$ 为无量纲变形梯度 | $\mathbf B$ its left Cauchy–Green tensor (dimensionless)<br>$\mathbf B$ 为左 Cauchy–Green 张量（无量纲） |
| $\lambda_r$ — Radial principal stretch (dimensionless)<br>$\lambda_r$ — 径向主伸长比（无量纲） | $\lambda_\theta$ — Polar tangential principal stretch (dimensionless)<br>$\lambda_\theta$ — 极角切向主伸长比（无量纲） |
| $r$ — Current material radius (m)<br>$r$ — 当前物质半径（m） | $r_0>0$ — Reference material radius (m)<br>$r_0>0$ — 参考物质半径（m） |
| $T^e_{rr}$ — Radial elastic Cauchy stress (Pa)<br>$T^e_{rr}$ — 径向弹性柯西应力（Pa） | $T^e_{\theta\theta}$ — Polar tangential elastic Cauchy stress (Pa)<br>$T^e_{\theta\theta}$ — 极角切向弹性柯西应力（Pa） |
| $T^e_{\phi\phi}$ — Azimuthal tangential elastic Cauchy stress (Pa)<br>$T^e_{\phi\phi}$ — 方位角切向弹性柯西应力（Pa） |  |

**Conventions and conditions.** $\mathsf T$ denotes transpose; Elastic stress is positive in tension..

**约定与条件。** $\mathsf T$ 表示转置；弹性应力以拉伸为正。。

(A-E02) · Constitutive assumption and exact subtraction

$$
\begin{aligned}\mathbf T^e&=-\chi\mathbf I+G_g\mathbf B,\qquad\mathbf B=\mathbf F\mathbf F^{\mathsf T},\\T^e_{rr}&=-\chi+G_g\lambda_r^2,\qquad T^e_{\theta\theta}=T^e_{\phi\phi}=-\chi+G_g\lambda_\theta^2,\\T^e_{\theta\theta}-T^e_{rr}&=G_g\left[\left(\frac r{r_0}\right)^2-\left(\frac{r_0}r\right)^4\right].\end{aligned}
$$


![Radial and tangential stretches produce different network stresses around the cavity.](../assets/figures/a-e02.svg)

Radial and tangential stretches produce different network stresses around the cavity.

空腔周围的径向与切向伸长产生不同的网络应力。

Step 3 — integrate the elastic contribution. For a static spherical field, radial equilibrium places twice the tangential–radial stress difference over radius in the radial stress derivative. The wall traction and the far-field traction then identify the pressure needed to support the elastic deformation. The same stress-difference integral will reappear as a resistance in the dynamic balance; setting the whole dynamic field quasistatic is not required there.

步骤 3——积分弹性贡献。对静态球形应力场，径向平衡使径向应力导数等于切向—径向应力差的两倍除以半径。壁面牵引与远场牵引由此确定维持弹性变形所需的压力。同一应力差积分还会作为阻力出现在动力学平衡中；后者并不要求整个动态场处于准静态。

**Symbols before Eq. (A-E03).**

**式（A-E03）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $T^e_{rr}$ — Radial elastic Cauchy stress (Pa)<br>$T^e_{rr}$ — 径向弹性柯西应力（Pa） | $T^e_{\theta\theta}$ — Polar tangential elastic Cauchy stress (Pa)<br>$T^e_{\theta\theta}$ — 极角切向弹性柯西应力（Pa） |
| $r$ is current radius (m)<br>$r$ 为当前半径（m） | $r_0=r_0(r)$ the reference coordinate (m)<br>$r_0=r_0(r)$ 为参考坐标（m） |
| $R>0$ the cavity radius (m)<br>$R>0$ 为腔体半径（m） | $p_b$ — Cavity pressure (Pa)<br>$p_b$ — 空腔压力（Pa） |
| $p_\infty$ — Far-field pressure (Pa)<br>$p_\infty$ — 远场压力（Pa） | $\sigma\geq0$ is constant tension (N m⁻¹)<br>$\sigma\geq0$ 为恒定张力（N m⁻¹） |
| $G_g>0$ is shear modulus (Pa)<br>$G_g>0$ 为剪切模量（Pa） | $p_{\mathrm{el}}$ is the signed elastic resistance (Pa)<br>$p_{\mathrm{el}}$ 为带符号的弹性阻力（Pa） |

**Conventions and conditions.** $d/dr$ differentiates in $r$, $\int_R^\infty$ integrates over exterior material, and $\infty$ labels the infinite far field.

**约定与条件。** $d/dr$ 表示对 $r$ 求导，$\int_R^\infty$ 对外部材料积分，$\infty$ 标记无限远场。

(A-E03) · Static balance defining the elastic resistance

$$
\begin{aligned}\frac{dT^e_{rr}}{dr}&=\frac{2}{r}(T^e_{\theta\theta}-T^e_{rr}),\\T^e_{rr}(\infty)&=-p_\infty,\qquad T^e_{rr}(R)=-p_b+\frac{2\sigma}{R},\\p_{\mathrm{el}}(R):=p_b-p_\infty-\frac{2\sigma}{R}&=2G_g\int_R^\infty\left[\left(\frac r{r_0}\right)^2-\left(\frac{r_0}r\right)^4\right]\frac{dr}{r}.\end{aligned}
$$


![The wall pressure supports capillary traction and the accumulated elastic resistance.](../assets/figures/a-e03.svg)

The wall pressure supports capillary traction and the accumulated elastic resistance.

壁面压力同时支撑毛细牵引与积分后的弹性阻力。

Step 4 — change variables with its Jacobian. During expansion $R>R_{\mathrm{ref}}$, set the dimensionless ratio $q=r_0/r$. The mapping makes it increase from $R_{\mathrm{ref}}/R$ at the wall to one at infinity. Differentiate its cube, cancel its positive square, and use the positive factor $1-q^3$ for finite exterior positions. Exactly at the undeformed state the transformation is degenerate; evaluate zero resistance directly instead of dividing by zero.

步骤 4——带雅可比地变换变量。膨胀时 $R>R_{\mathrm{ref}}$，定义无量纲比值 $q=r_0/r$。由构形映射，它从壁面处的 $R_{\mathrm{ref}}/R$ 增大到无穷远处的 1。对其三次方求导，约去正的平方，并对有限外部位置使用正因子 $1-q^3$。在恰好未变形的状态，这个变换退化；此时直接求得零阻力，而不是除以零。

**Symbols before Eq. (A-E04).**

**式（A-E04）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $q=r_0/r$ is a positive dimensionless coordinate ratio<br>$q=r_0/r$ 为正的无量纲坐标比 | $r_0$ — Reference material radius (m)<br>$r_0$ — 参考物质半径（m） |
| $r$ — Current material radius (m)<br>$r$ — 当前物质半径（m） | $R>R_{\mathrm{ref}}>0$ — Current cavity radius (m)<br>$R>R_{\mathrm{ref}}>0$ — 当前腔体半径（m） |
| $R_{\mathrm{ref}}$ — Stress-free reference cavity radius (m)<br>$R_{\mathrm{ref}}$ — 无应力参考腔体半径（m） | $q(R)$ — Coordinate-ratio value at the cavity wall (dimensionless)<br>$q(R)$ — 空腔壁面处的坐标比值（无量纲） |
| $q(\infty)$ denote endpoint values (dimensionless)<br>$q(\infty)$ 表示端点值（无量纲） | $dq$ — Dimensionless coordinate-ratio integration element (dimensionless)<br>$dq$ — 无量纲坐标比积分微元（无量纲） |
| $dr$ — Current-radius integration element (m)<br>$dr$ — 当前半径积分微元（m） |  |

**Conventions and conditions.** $\infty$ denotes the far-field limit; The factorization $1-q^6=(1-q^3)(1+q^3)$ applies for $q<1$ before taking the endpoint limit.

**约定与条件。** $\infty$ 表示远场极限；因式分解 $1-q^6=(1-q^3)(1+q^3)$ 先在 $q<1$ 时使用，再取端点极限。

(A-E04) · Exact change of variable for expansion

$$
\begin{aligned}q^3&=1-\frac{R^3-R_{\mathrm{ref}}^3}{r^3},\qquad q(R)=\frac{R_{\mathrm{ref}}}{R},\qquad q(\infty)=1,\\3q^2\,dq&=3(1-q^3)\frac{dr}{r},\qquad \frac{dr}{r}=\frac{q^2\,dq}{1-q^3},\\\left(q^{-2}-q^4\right)\frac{dr}{r}&=\frac{1-q^6}{1-q^3}\,dq=(1+q^3)\,dq.\end{aligned}
$$


![The material coordinate ratio converts a spatial stress integral into a regular polynomial integral.](../assets/figures/a-e04.svg)

The material coordinate ratio converts a spatial stress integral into a regular polynomial integral.

材料坐标比将空间应力积分转化为正则的多项式积分。

**Symbols before Eq. (A-E05).**

**式（A-E05）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{el}}$ is elastic cavity resistance (Pa)<br>$p_{\mathrm{el}}$ 为弹性腔体阻力（Pa） | $G_g>0$ is network shear modulus (Pa)<br>$G_g>0$ 为网络剪切模量（Pa） |
| $R\geq R_{\mathrm{ref}}>0$ — Current cavity radius (m)<br>$R\geq R_{\mathrm{ref}}>0$ — 当前腔体半径（m） | $R_{\mathrm{ref}}$ — Stress-free reference cavity radius (m)<br>$R_{\mathrm{ref}}$ — 无应力参考腔体半径（m） |
| $q$ is the dimensionless integration variable<br>$q$ 为无量纲积分变量 |  |

**Conventions and conditions.** $\int$ is a definite integral; $[f(q)]_a^b$ means upper-endpoint minus lower-endpoint evaluation of the bracketed function.

**约定与条件。** $\int$ 为定积分；$[f(q)]_a^b$ 表示括号中函数的上端点值减去下端点值。

(A-E05) · Derived neo-Hookean elastic resistance

$$
\begin{aligned}p_{\mathrm{el}}(R)&=2G_g\int_{R_{\mathrm{ref}}/R}^{1}(1+q^3)\,dq\\&=2G_g\left[q+\frac{q^4}{4}\right]_{R_{\mathrm{ref}}/R}^{1}\\&=2G_g\left[\frac54-\frac{R_{\mathrm{ref}}}{R}-\frac14\left(\frac{R_{\mathrm{ref}}}{R}\right)^4\right]\\&=\frac{G_g}{2}\left[5-4\frac{R_{\mathrm{ref}}}{R}-\left(\frac{R_{\mathrm{ref}}}{R}\right)^4\right].\end{aligned}
$$


![Elastic resistance follows from the full stretch field, not from a guessed constant pressure.](../assets/figures/a-e05.svg)

Elastic resistance follows from the full stretch field, not from a guessed constant pressure.

弹性阻力来自完整伸长场，而不是猜测的恒定压力。

Each row uses, in order, Eq. (A-E04), the antiderivative of $1+q^3$, upper-minus-lower endpoint evaluation, and scalar multiplication. The result matches the neo-Hookean elastic term reported in Gaudron et al., Eq. (2.18). The constitutive large-expansion limit is a plateau in pressure resistance, not a material fracture threshold. A fractured, finite, prestressed or strain-stiffening gel can depart from this result. [[R13]](../reference/sources.html#r13)

各行依次使用式（A-E04）、$1+q^3$ 的原函数、上端点减下端点，以及标量乘法。该结果与 Gaudron 等人式（2.18）报告的 neo-Hookean 弹性项一致。本构模型的大膨胀极限是压力阻力的平台值，不是材料断裂阈值。已破裂、有限尺寸、预应力或具有应变硬化的凝胶都可能偏离这一结果。[[R13]](../reference/sources.html#r13)

**Symbols before Eq. (A-E06).**

**式（A-E06）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{el}}$ is pressure resistance (Pa)<br>$p_{\mathrm{el}}$ 为压力阻力（Pa） | $G_g>0$ is shear modulus (Pa)<br>$G_g>0$ 为剪切模量（Pa） |
| $R\geq R_{\mathrm{ref}}>0$ — Current cavity radius (m)<br>$R\geq R_{\mathrm{ref}}>0$ — 当前腔体半径（m） | $R_{\mathrm{ref}}$ — Stress-free reference cavity radius (m)<br>$R_{\mathrm{ref}}$ — 无应力参考腔体半径（m） |

**Conventions and conditions.** $d/dR$ is the radius derivative (giving Pa m⁻¹ here); $\lim$ takes the positive large-radius-ratio limit; $\infty$ denotes an unbounded ratio.

**约定与条件。** $d/dR$ 表示半径导数（此处单位为 Pa m⁻¹）；$\lim$ 取正的大半径比极限；$\infty$ 表示比值无界。

(A-E06) · Limiting-state and sign checks

$$
\begin{aligned}p_{\mathrm{el}}(R_{\mathrm{ref}})&=\frac{G_g}{2}(5-4-1)=0,\\\frac{dp_{\mathrm{el}}}{dR}&=2G_g\left(\frac{R_{\mathrm{ref}}}{R^2}+\frac{R_{\mathrm{ref}}^4}{R^5}\right)>0,\\\lim_{R/R_{\mathrm{ref}}\to\infty}p_{\mathrm{el}}(R)&=\frac52G_g.\end{aligned}
$$


![Zero deformation gives zero elastic resistance, and positive expansion raises it monotonically.](../assets/figures/a-e06.svg)

Zero deformation gives zero elastic resistance, and positive expansion raises it monotonically.

零变形给出零弹性阻力，正向膨胀使阻力单调增大。

## 3. Close the elastic work calculation

## 3. 完整计算弹性功

Step 5 — integrate work against cavity volume. Pressure is conjugate to volume change, not to radius change alone. Multiply by the spherical area, insert Eq. (A-E05), and integrate each power of the dummy radius. The last term uses the antiderivative $-1/\xi$ of $\xi^{-2}$; retain both endpoints so that the reference work is zero.

步骤 5——对腔体体积积分功。压力与体积变化共轭，而不是单独与半径变化共轭。乘以球面面积，代入式（A-E05），再逐项积分虚拟半径的各次幂。最后一项使用 $\xi^{-2}$ 的原函数 $-1/\xi$；保留两个端点，保证参考状态的功为零。

**Symbols before Eq. (A-E07).**

**式（A-E07）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $W_g$ is stored elastic work relative to the unstretched state (J)<br>$W_g$ 为相对未伸长状态的储存弹性功（J） | $p_{\mathrm{el}}(\xi)$ is signed elastic resistance (Pa)<br>$p_{\mathrm{el}}(\xi)$ 为带符号弹性阻力（Pa） |
| $G_g>0$ is modulus (Pa)<br>$G_g>0$ 为模量（Pa） | $R\geq R_{\mathrm{ref}}>0$ — Current cavity radius (m)<br>$R\geq R_{\mathrm{ref}}>0$ — 当前腔体半径（m） |
| $R_{\mathrm{ref}}$ — Stress-free reference cavity radius (m)<br>$R_{\mathrm{ref}}$ — 无应力参考腔体半径（m） | $d\xi$ is its differential (m)<br>$d\xi$ 为其微分（m） |
| $\pi$ is the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） | $\xi$ — Dummy cavity-radius integration coordinate (m)<br>$\xi$ — 空腔半径积分哑坐标（m） |

**Conventions and conditions.** $[\ ]_{R_{\mathrm{ref}}}^{R}$ denotes endpoint subtraction.

**约定与条件。** $[\ ]_{R_{\mathrm{ref}}}^{R}$ 表示端点相减。

(A-E07) · Exact work integral within the elastic model

$$
\begin{aligned}W_g(R)&=4\pi\int_{R_{\mathrm{ref}}}^{R}p_{\mathrm{el}}(\xi)\xi^2\,d\xi\\&=2\pi G_g\int_{R_{\mathrm{ref}}}^{R}\left(5\xi^2-4R_{\mathrm{ref}}\xi-R_{\mathrm{ref}}^4\xi^{-2}\right)d\xi\\&=2\pi G_g\left[\frac{5\xi^3}{3}-2R_{\mathrm{ref}}\xi^2+\frac{R_{\mathrm{ref}}^4}{\xi}\right]_{R_{\mathrm{ref}}}^{R}\\&=2\pi G_g\left[\frac{5R^3}{3}-2R_{\mathrm{ref}}R^2+\frac{R_{\mathrm{ref}}^4}{R}-\frac{2R_{\mathrm{ref}}^3}{3}\right].\end{aligned}
$$


![The area factor converts radius increments into cavity volume increments before integrating work.](../assets/figures/a-e07.svg)

The area factor converts radius increments into cavity volume increments before integrating work.

先用面积因子将半径增量转化为腔体体积增量，再积分功。

In the final row the lower endpoint contributes $(5/3-2+1)R_{\mathrm{ref}}^3=2R_{\mathrm{ref}}^3/3$, which is subtracted. A pressure plateau therefore still allows work to grow approximately in proportion to cavity volume. The units are Pa m³ = J. Differentiating the closed form gives exactly pressure times area; this is a stronger check than comparing pressure magnitudes alone.

最后一行中，下端点贡献为 $(5/3-2+1)R_{\mathrm{ref}}^3=2R_{\mathrm{ref}}^3/3$，需将其减去。因此，即使压力出现平台，功仍可近似随腔体体积增长。单位为 Pa m³ = J。对闭式结果求导恰好得到压力乘面积；这个核查比单独比较压力大小更有力。

**Symbols before Eq. (A-E08).**

**式（A-E08）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $W_g$ is elastic work (J)<br>$W_g$ 为弹性功（J） | $p_{\mathrm{el}}$ resistance (Pa)<br>$p_{\mathrm{el}}$ 为阻力（Pa） |
| $G_g>0$ shear modulus (Pa)<br>$G_g>0$ 为剪切模量（Pa） | $R$ — Current cavity radius (m)<br>$R$ — 当前腔体半径（m） |
| $R_{\mathrm{ref}}>0$ — Stress-free reference cavity radius (m)<br>$R_{\mathrm{ref}}>0$ — 无应力参考腔体半径（m） | $\delta R=R-R_{\mathrm{ref}}$ a small radius change (m), with $\|\delta R\|/R_{\mathrm{ref}}\ll1$<br>$\delta R=R-R_{\mathrm{ref}}$ 为小半径变化（m），满足 $\|\delta R\|/R_{\mathrm{ref}}\ll1$ |
| $\pi$ is dimensionless<br>$\pi$ 为无量纲量 |  |

**Conventions and conditions.** $d/dR$ is differentiation in radius; $O$ denotes terms bounded by a constant times the indicated scale as that ratio tends to zero.

**约定与条件。** $d/dR$ 表示对半径求导；$O$ 表示当该比值趋于零时，被某常数乘所示尺度界定的项。

(A-E08) · Work-conjugacy and small-deformation checks

$$
\begin{aligned}\frac{dW_g}{dR}&=2\pi G_g\left(5R^2-4R_{\mathrm{ref}}R-\frac{R_{\mathrm{ref}}^4}{R^2}\right)=4\pi R^2p_{\mathrm{el}}(R),\\R=R_{\mathrm{ref}}+\delta R\colon\qquad p_{\mathrm{el}}&=\frac{4G_g\delta R}{R_{\mathrm{ref}}}+O\!\left(G_g\frac{\delta R^2}{R_{\mathrm{ref}}^2}\right),\\W_g&=8\pi G_gR_{\mathrm{ref}}\delta R^2+O(G_g\delta R^3).\end{aligned}
$$


![Near the reference cavity, pressure is linear in radius change and stored work is quadratic.](../assets/figures/a-e08.svg)

Near the reference cavity, pressure is linear in radius change and stored work is quadratic.

在参考腔体附近，压力与半径变化呈线性关系，储存功则呈二次关系。

The linear term follows by differentiating Eq. (A-E05) at the reference radius; integrate $4\pi R_{\mathrm{ref}}^2$ times that term to obtain the quadratic work. An independent volume-integral check sums the neo-Hookean strain-energy density throughout the reference material and reproduces Eq. (A-E07). Energy storage is reversible in this intact hyperelastic law. Returning that energy to useful jet motion is conditional on timing and geometry; it is not guaranteed, and stored work should not automatically be counted as irreversible heat loss.

线性项来自在参考半径处对式（A-E05）求导；将其乘以 $4\pi R_{\mathrm{ref}}^2$ 后积分，得到二次功项。独立的体积积分核查对参考材料中的 neo-Hookean 应变能密度求和，重现式（A-E07）。该完整超弹性规律中的能量储存可逆。能量能否返还给有效射流运动，取决于时序和几何，并不保证发生；储存功也不应自动计作不可逆热损失。

## 4. Add inertia and loss without double counting

## 4. 加入惯性与损耗，避免重复计算

Step 6 — choose a Kelvin–Voigt viscous contribution. Let the total stress add $2\eta_g\mathbf D$ to the elastic stress, where $\mathbf D$ is the symmetric velocity gradient. Incompressibility and no wall/material slip supply the radial speed field. Its radial gradient is negative during outward motion, while tangential extension is positive.

步骤 6——选择 Kelvin–Voigt 黏性贡献。令总应力在弹性应力上加入 $2\eta_g\mathbf D$，其中 $\mathbf D$ 为对称速度梯度。不可压缩性及壁面／材料无滑移给出径向速度场。向外运动时，其径向梯度为负，切向拉伸为正。

**Symbols before Eq. (A-E09).**

**式（A-E09）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\mathbf T$ — Total Cauchy stress tensor (Pa)<br>$\mathbf T$ — 总柯西应力张量（Pa） | $\mathbf T^e$ — Elastic Cauchy stress tensor, tension positive (Pa)<br>$\mathbf T^e$ — 拉伸取正的弹性柯西应力张量（Pa） |
| $\eta_g\geq0$ is the chosen medium viscosity (Pa s)<br>$\eta_g\geq0$ 为所选介质黏度（Pa s） | $\mathbf D$ — Material strain-rate tensor (s⁻¹)<br>$\mathbf D$ — 物质应变率张量（s⁻¹） |
| $u_r$ is radial material speed (m s⁻¹)<br>$u_r$ 为径向材料速度（m s⁻¹） | $r\geq R(t)>0$ is current position (m)<br>$r\geq R(t)>0$ 为当前位置（m） |
| $R$ wall radius (m)<br>$R$ 为壁面半径（m） | $t$ time (s)<br>$t$ 为时间（s） |
| $\dot R$ wall speed (m s⁻¹)<br>$\dot R$ 为泡壁速度（m s⁻¹） | $T_{rr}$ — Total radial Cauchy stress (Pa)<br>$T_{rr}$ — 总径向柯西应力（Pa） |
| $T_{\theta\theta}$ — Total polar tangential Cauchy stress (Pa)<br>$T_{\theta\theta}$ — 总极角切向柯西应力（Pa） | $T^e_{rr}$ — Radial elastic Cauchy stress (Pa)<br>$T^e_{rr}$ — 径向弹性柯西应力（Pa） |
| $T^e_{\theta\theta}$ — Polar tangential elastic Cauchy stress (Pa)<br>$T^e_{\theta\theta}$ — 极角切向弹性柯西应力（Pa） | $D_{rr}$ — Radial strain-rate component (s⁻¹)<br>$D_{rr}$ — 径向应变率分量（s⁻¹） |
| $D_{\theta\theta}$ — Polar tangential strain-rate component (s⁻¹)<br>$D_{\theta\theta}$ — 极角切向应变率分量（s⁻¹） | $D_{\phi\phi}$ — Azimuthal tangential strain-rate component (s⁻¹)<br>$D_{\phi\phi}$ — 方位角切向应变率分量（s⁻¹） |

**Conventions and conditions.** $\partial/\partial r$ is the fixed-time spatial derivative.

**约定与条件。** $\partial/\partial r$ 为固定时刻的空间导数。

(A-E09) · Kelvin–Voigt closure and exact radial kinematics

$$
\begin{aligned}\mathbf T&=\mathbf T^e+2\eta_g\mathbf D,\qquad u_r(r,t)=\frac{R^2\dot R}{r^2},\\D_{rr}&=\frac{\partial u_r}{\partial r}=-\frac{2R^2\dot R}{r^3},\qquad D_{\theta\theta}=D_{\phi\phi}=\frac{u_r}{r}=\frac{R^2\dot R}{r^3},\\T_{\theta\theta}-T_{rr}&=T^e_{\theta\theta}-T^e_{rr}+\frac{6\eta_gR^2\dot R}{r^3}.\end{aligned}
$$


![The viscous term derives from the surrounding-medium strain rate, not from bubble mass.](../assets/figures/a-e09.svg)

The viscous term derives from the surrounding-medium strain rate, not from bubble mass.

黏性项来自周围介质的应变率，而不是气泡质量。

Step 7 — integrate the radial momentum equation. The fixed-position time derivative and the convective derivative must both be retained. Substitution of Eq. (A-E09) leaves an integrable acceleration field. The total wall stress is $-p_b+2\sigma/R$, and total far-field stress is $-p_\infty$; integrate the stress difference instead of guessing its sign.

步骤 7——积分径向动量方程。必须同时保留固定位置的时间偏导和对流导数。代入式（A-E09）后得到可积的加速度场。总壁面应力为 $-p_b+2\sigma/R$，总远场应力为 $-p_\infty$；应积分应力差，而不是猜测其符号。

**Symbols before Eq. (A-E10).**

**式（A-E10）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $a_r$ is material radial acceleration (m s⁻²)<br>$a_r$ 为材料径向加速度（m s⁻²） | $u_r$ radial speed (m s⁻¹)<br>$u_r$ 为径向速度（m s⁻¹） |
| $r\geq R>0$ — Current material radial position outside the cavity (m)<br>$r\geq R>0$ — 空腔外部的当前物质径向位置（m） | $t$ time (s)<br>$t$ 为时间（s） |
| $\dot R$ — Cavity-wall radial velocity (m s⁻¹)<br>$\dot R$ — 空腔壁面径向速度（m s⁻¹） | $\ddot R$ wall speed/acceleration (m s⁻¹, m s⁻²)<br>$\ddot R$ 为泡壁速度／加速度（m s⁻¹、m s⁻²） |
| $\rho_g>0$ is density (kg m⁻³)<br>$\rho_g>0$ 为密度（kg m⁻³） | $\eta_g\geq0$ viscosity (Pa s)<br>$\eta_g\geq0$ 为黏度（Pa s） |
| $T_{rr}$ — Total radial Cauchy stress (Pa)<br>$T_{rr}$ — 总径向柯西应力（Pa） | $T_{\theta\theta}$ — Total polar tangential Cauchy stress (Pa)<br>$T_{\theta\theta}$ — 总极角切向柯西应力（Pa） |
| $R$ — Current cavity radius (m)<br>$R$ — 当前腔体半径（m） |  |

**Conventions and conditions.** $\partial$ denotes fixed-other-coordinate derivatives and the integrals run through the exterior to infinity; Integrated acceleration times density has units Pa.

**约定与条件。** $\partial$ 表示保持其他坐标不变的偏导，积分经外部材料到无穷远；积分后的加速度乘以密度的单位为 Pa。

(A-E10) · Momentum law and explicitly evaluated integrals

$$
\begin{aligned}a_r&:=\frac{\partial u_r}{\partial t}+u_r\frac{\partial u_r}{\partial r}=\frac{2R\dot R^2+R^2\ddot R}{r^2}-\frac{2R^4\dot R^2}{r^5},\\\rho_g a_r&=\frac{\partial T_{rr}}{\partial r}+\frac{2}{r}(T_{rr}-T_{\theta\theta}),\\\rho_g\int_R^\infty a_r\,dr&=\rho_g\left[R\ddot R+2\dot R^2-\frac{\dot R^2}{2}\right]=\rho_g\left(R\ddot R+\frac32\dot R^2\right),\\2\int_R^\infty\frac{6\eta_gR^2\dot R}{r^4}\,dr&=12\eta_gR^2\dot R\left(\frac{1}{3R^3}\right)=\frac{4\eta_g\dot R}{R}.\end{aligned}
$$


![Integrating the material acceleration and the viscous stress difference gives their distinct radial contributions.](../assets/figures/a-e10.svg)

Integrating the material acceleration and the viscous stress difference gives their distinct radial contributions.

对材料加速度与黏性应力差积分，得到各自不同的径向贡献。

**Symbols before Eq. (A-E11).**

**式（A-E11）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\rho_g$ is effective medium density (kg m⁻³)<br>$\rho_g$ 为有效介质密度（kg m⁻³） | $R>0$ is the cavity radius (m)<br>$R>0$ 为腔体半径（m） |
| $\dot R$ — Cavity-wall radial velocity (m s⁻¹)<br>$\dot R$ — 空腔壁面径向速度（m s⁻¹） | $\ddot R$ — Cavity-wall radial acceleration (m s⁻²)<br>$\ddot R$ — 空腔壁面径向加速度（m s⁻²） |
| $p_b$ — Cavity pressure (Pa)<br>$p_b$ — 空腔压力（Pa） | $p_\infty$ — Far-field pressure (Pa)<br>$p_\infty$ — 远场压力（Pa） |
| $p_{\mathrm{el}}(R)$ — Signed elastic cavity-pressure resistance (Pa)<br>$p_{\mathrm{el}}(R)$ — 带符号弹性空腔压力阻力（Pa） | $\sigma$ is tension (N m⁻¹)<br>$\sigma$ 为张力（N m⁻¹） |
| $\eta_g$ is the represented medium viscosity (Pa s)<br>$\eta_g$ 为所描述介质的黏度（Pa s） |  |

**Conventions and conditions.** Each term has units Pa.

**约定与条件。** 每一项的单位均为 Pa。

(A-E11) · Derived intact-medium radial control

$$
\rho_g\left(R\ddot R+\frac32\dot R^2\right)=p_b-p_\infty-\frac{2\sigma}{R}-p_{\mathrm{el}}(R)-\frac{4\eta_g\dot R}{R}.
$$


![The spherical control quantifies cavity work and wall motion before any directional-flow calculation.](../assets/figures/a-e11.svg)

The spherical control quantifies cavity work and wall motion before any directional-flow calculation.

球形控制模型先量化腔体功与泡壁运动，再进行定向流动计算。

The stress derivative integrates to far-field minus wall stress; subtracting the two stress-difference integrals yields Eq. (A-E11). Setting $G_g=0$ recovers the corresponding liquid radial model. For expansion the viscous term is negative; during inward motion it is positive and opposes collapse. Do not add a separate solvent viscosity if the fitted $\eta_g$ already represents the same dissipation. A separate solvent/network model needs its own relative motion and constitutive partition. Phase transfer that gives appreciable material/wall velocity slip also changes the kinematic premise.

应力导数积分得到远场应力减去壁面应力；再减去两个应力差积分，便得到式（A-E11）。取 $G_g=0$ 可恢复相应的液体径向模型。膨胀时黏性项为负；向内运动时为正，抵抗塌缩。若拟合的 $\eta_g$ 已描述同一耗散，不应再另加溶剂黏度。独立的溶剂／网络模型需要各自的相对运动及本构分配。若相变传递造成明显的材料／壁面速度滑移，也会改变运动学前提。

Step 8 — multiply by the volume-change rate to check conservation. The medium kinetic energy follows the radial field, and the elastic work derivative was already checked. The viscous pressure has signed effects on acceleration but always removes mechanical energy because the dissipation contains the square of speed.

步骤 8——乘以体积变化率，核查能量守恒。介质动能由径向速度场确定，弹性功导数已完成核查。黏性压力对加速度的作用具有符号，但它总会移除机械能，因为耗散包含速度平方。

**Symbols before Eq. (A-E12).**

**式（A-E12）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $K_g$ — Surrounding-medium kinetic energy (J)<br>$K_g$ — 周围介质动能（J） | $W_g$ — Stored network elastic work (J)<br>$W_g$ — 储存的网络弹性功（J） |
| $E_\sigma$ — Interface energy (J)<br>$E_\sigma$ — 界面能（J） | $\rho_g$ density (kg m⁻³)<br>$\rho_g$ 为密度（kg m⁻³） |
| $R>0$ radius (m)<br>$R>0$ 为半径（m） | $\dot R$ wall speed (m s⁻¹)<br>$\dot R$ 为泡壁速度（m s⁻¹） |
| $\sigma$ tension (N m⁻¹)<br>$\sigma$ 为张力（N m⁻¹） | $\dot V$ is cavity volume-change rate (m³ s⁻¹)<br>$\dot V$ 为腔体体积变化率（m³ s⁻¹） |
| $p_b$ — Cavity pressure (Pa)<br>$p_b$ — 空腔压力（Pa） | $p_\infty$ — Far-field pressure (Pa)<br>$p_\infty$ — 远场压力（Pa） |
| $P_{\mathrm{dis}}$ nonnegative viscous power (W)<br>$P_{\mathrm{dis}}$ 为非负黏性功率（W） | $\eta_g\geq0$ viscosity (Pa s)<br>$\eta_g\geq0$ 为黏度（Pa s） |
| $t$ time (s)<br>$t$ 为时间（s） | $\pi$ the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** $d/dt$ is the full time derivative.

**约定与条件。** $d/dt$ 为全时间导数。

(A-E12) · Derived mechanical energy balance

$$
\begin{aligned}K_g&=2\pi\rho_gR^3\dot R^2,\qquad E_\sigma=4\pi\sigma R^2,\qquad \dot V=4\pi R^2\dot R,\\\frac{d}{dt}(K_g+W_g+E_\sigma)&=(p_b-p_\infty)\dot V-P_{\mathrm{dis}},\\P_{\mathrm{dis}}&=16\pi\eta_gR\dot R^2\geq0.\end{aligned}
$$


![Pressure work divides into inertia, recoverable network energy, surface energy and viscous loss.](../assets/figures/a-e12.svg)

Pressure work divides into inertia, recoverable network energy, surface energy and viscous loss.

压力功分配到惯性、可恢复的网络能、表面能和黏性损耗。

## 5. Worked benchmark: pressure is not the work budget

## 5. 计算示例：压力并不等于功预算

All following numbers are declared teaching inputs, not measurements of a proposed PFC gel. Choose network shear modulus 20 kPa, stress-free radius 5 µm, current radius 30 µm and density 1000 kg m⁻³. First calculate the wall resistance and stored work. The sixfold wall stretch is large; assuming an intact neo-Hookean network there is an explicit hypothesis that needs material validation.

以下数值均为明确设定的教学输入，并非所提出 PFC 凝胶的实测值。取网络剪切模量 20 kPa、无应力半径 5 µm、当前半径 30 µm，以及密度 1000 kg m⁻³。先计算壁面阻力和储存功。壁面伸长六倍属于大变形；此时假设 neo-Hookean 网络保持完整，是需要材料验证的明确假设。

**Symbols before Eq. (A-E13).**

**式（A-E13）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{el}}$ is elastic resistance (Pa)<br>$p_{\mathrm{el}}$ 为弹性阻力（Pa） | $W_g$ is stored elastic work (J)<br>$W_g$ 为储存弹性功（J） |
| $\pi$ is dimensionless<br>$\pi$ 为无量纲量 | $G_g=20000$ — Substituted network shear modulus (Pa)<br>$G_g=20000$ — 代入的网络剪切模量（Pa） |
| $R_{\mathrm{ref}}=5\times10^{-6}$ — Substituted reference cavity radius (m)<br>$R_{\mathrm{ref}}=5\times10^{-6}$ — 代入的参考空腔半径（m） | $R=30\times10^{-6}$ — Substituted current cavity radius (m)<br>$R=30\times10^{-6}$ — 代入的当前空腔半径（m） |

**Conventions and conditions.** The numbers 5 and 30 in radius ratios both use µm. Powers denote numerical exponents; Pa means pascal, J joule, and the cross denotes multiplication..

**约定与条件。** 半径比值中的数值 5 与 30 均采用 µm。幂表示数值指数；Pa 为帕斯卡，J 为焦耳，叉号表示乘法。。

(A-E13) · Teaching-input substitution

$$
\begin{aligned}p_{\mathrm{el}}&=\frac{20000}{2}\left[5-4\left(\frac5{30}\right)-\left(\frac5{30}\right)^4\right]=43325.6173\ \mathrm{Pa},\\W_g&=2\pi(20000)\left[\frac53(30\times10^{-6})^3-2(5\times10^{-6})(30\times10^{-6})^2\right.\\&\hspace{30mm}\left.+\frac{(5\times10^{-6})^4}{30\times10^{-6}}-\frac23(5\times10^{-6})^3\right]\\&=4.51603944\times10^{-9}\ \mathrm J.\end{aligned}
$$


![This soft network still stores several nanojoules when the cavity radius expands sixfold.](../assets/figures/a-e13.svg)

This soft network still stores several nanojoules when the cavity radius expands sixfold.

腔体半径膨胀六倍时，即使这个柔软网络也会储存数纳焦耳能量。

For comparison, prescribe a constant net pressure-work scale of 100 kPa over exactly the same displaced volume. This is a work scale, not a solved gas-pressure history. It gives 11.2574 nJ, of which the calculated network storage is 40.1163%. The remaining 6.74133 nJ is an upper residual for kinetic and surface increments plus losses in this artificial expansion ledger; it is not a predicted external jet energy. Initial surface energy cancels only after its increment is treated consistently.

作为比较，对完全相同的排开体积指定恒定净压力功尺度 100 kPa。这是功的尺度，而不是求解得到的气体压力历程。它给出 11.2574 nJ，其中计算出的网络储存占 40.1163%。余下 6.74133 nJ 是这个人为膨胀账本中，动能与表面能增量加损耗的剩余上限；它不是外部射流能量的预测值。只有一致地处理表面能增量后，初始表面能才能消去。

**Symbols before Eq. (A-E14).**

**式（A-E14）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Delta V$ is expanded cavity volume (m³)<br>$\Delta V$ 为腔体膨胀体积（m³） | $R=30$ µm (m)<br>$R=30$ µm（m） |
| $R_{\mathrm{ref}}=5$ — Stress-free reference cavity radius (m)<br>$R_{\mathrm{ref}}=5$ — 无应力参考腔体半径（m） | $\Delta p_w=100000$ Pa is a constant illustrative net pressure-work input<br>$\Delta p_w=100000$ Pa 为恒定的示例净压力功输入 |
| $W_{100}$ is the resulting work scale (J), with subscript 100 labeling its 100 kPa input<br>$W_{100}$ 为由此得到的功尺度（J），下标 100 标记其 100 kPa 输入 | $W_g=4.51603944$ nJ is stored network work (J)<br>$W_g=4.51603944$ nJ 为储存网络功（J） |
| $\pi$ is dimensionless<br>$\pi$ 为无量纲量 |  |

**Conventions and conditions.** nJ means $10^{-9}$ J.

**约定与条件。** nJ 表示 $10^{-9}$ J。

(A-E14) · Finite work-budget comparison

$$
\begin{aligned}\Delta V&=\frac{4\pi}{3}(R^3-R_{\mathrm{ref}}^3)=1.12573737\times10^{-13}\ \mathrm{m^3},\\W_{100}&:=\Delta p_w\Delta V=11.2573737\ \mathrm{nJ},\\\frac{W_g}{W_{100}}&=0.401162791,\qquad W_{100}-W_g=6.74133424\ \mathrm{nJ}.\end{aligned}
$$


![The elastic cost occupies a finite fraction of the work budget even though its pressure is below 100 kPa.](../assets/figures/a-e14.svg)

The elastic cost occupies a finite fraction of the work budget even though its pressure is below 100 kPa.

即使弹性压力低于 100 kPa，其能量代价也占据功预算的有限份额。

A separate sign calculation uses an illustrative viscosity 0.010 Pa s, current radius 30 µm and inward wall speed −10 m s⁻¹. Its signed right-hand-side pressure contribution is +13.3333 kPa, but its irreversible power remains +1.50796 mW. A positive resistance during collapse is not energy generation. These instantaneous values require a time history before integrating total dissipation.

另一个符号计算采用示例黏度 0.010 Pa s、当前半径 30 µm，以及向内泡壁速度 −10 m s⁻¹。其方程右侧带符号压力贡献为 +13.3333 kPa，但不可逆功率仍为 +1.50796 mW。塌缩时阻力为正不代表产生能量。这些瞬时值需要结合时间历程，才能积分总耗散。

**Symbols before Eq. (A-E15).**

**式（A-E15）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{visc,RHS}}$ is the signed viscous pressure term on the radial equation's right-hand side (Pa)<br>$p_{\mathrm{visc,RHS}}$ 为径向方程右侧的带符号黏性压力项（Pa） | $P_{\mathrm{dis}}$ is dissipated power (W)<br>$P_{\mathrm{dis}}$ 为耗散功率（W） |
| $\eta_g=0.010$ Pa s is illustrative viscosity<br>$\eta_g=0.010$ Pa s 为示例黏度 | $R=30\times10^{-6}$ m radius<br>$R=30\times10^{-6}$ m 为半径 |
| $\dot R=-10$ m s⁻¹ wall speed<br>$\dot R=-10$ m s⁻¹ 为泡壁速度 | $\pi$ the circle constant (dimensionless)<br>$\pi$ 为圆周率（无量纲） |

**Conventions and conditions.** RHS labels that side; The number 100 is the squared speed in m² s⁻².

**约定与条件。** RHS 标记右侧；数值 100 为以 m² s⁻² 表示的速度平方。

(A-E15) · Signed-pressure and positive-loss check

$$
\begin{aligned}p_{\mathrm{visc,RHS}}&=-\frac{4\eta_g\dot R}{R}=-\frac{4(0.010)(-10)}{30\times10^{-6}}=13333.3333\ \mathrm{Pa},\\P_{\mathrm{dis}}&=16\pi\eta_gR\dot R^2=16\pi(0.010)(30\times10^{-6})(100)=1.50796447\times10^{-3}\ \mathrm W.\end{aligned}
$$


![Inward motion changes the pressure sign but leaves dissipated power positive.](../assets/figures/a-e15.svg)

Inward motion changes the pressure sign but leaves dissipated power positive.

向内运动改变压力项符号，但耗散功率仍为正。

## 6. Use event times, not a separate vibration curriculum

## 6. 使用事件时间尺度，不另设振荡课程

Step 9 — compare network memory to event duration. The Deborah number uses an independently identified stress-relaxation time. A large value means stress memory persists during the event; it does not mean an infinitely stiff wall. A small value allows relaxation but does not remove geometric confinement or prove rapid solvent drainage. A relaxation spectrum may require several times rather than one.

步骤 9——比较网络记忆与事件持续时间。Deborah 数使用独立确定的应力松弛时间。数值大表示应力记忆在事件期间持续存在，并不表示壁面无限刚硬。数值小允许发生松弛，但不会消除几何约束，也不能证明溶剂迅速排出。若存在松弛谱，可能需要多个时间而不是一个。

**Symbols before Eq. (A-E16).**

**式（A-E16）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\mathrm{De}$ is the dimensionless event Deborah number<br>$\mathrm{De}$ 为无量纲事件 Deborah 数 | $\tau_{\mathrm{rel}}>0$ is an independently identified network stress-relaxation time (s)<br>$\tau_{\mathrm{rel}}>0$ 为独立确定的网络应力松弛时间（s） |
| $\tau_e>0$ is the specified cavity/jet event duration (s)<br>$\tau_e>0$ 为指定的腔体／射流事件持续时间（s） |  |

**Conventions and conditions.** Subscripts rel and e label relaxation and event respectively.

**约定与条件。** 下标 rel、e 分别表示松弛与事件。

(A-E16) · Response-time definition

$$
\mathrm{De}:=\frac{\tau_{\mathrm{rel}}}{\tau_e}.
$$


![The event duration determines which part of the network response can act before the jet or load arrives.](../assets/figures/a-e16.svg)

The event duration determines which part of the network response can act before the jet or load arrives.

事件持续时间决定网络响应的哪一部分能在射流或载荷到达前发挥作用。

Do not silently call $\eta_g/G_g$ a Kelvin–Voigt stress-relaxation time. In the linear shear version, held strain gives constant elastic stress after the rate term vanishes. Releasing the imposed stress instead gives exponential strain recovery with a retardation time. This distinction prevents fitting an invented relaxation mechanism to the spherical dashpot model.

不要默默把 $\eta_g/G_g$ 称作 Kelvin–Voigt 应力松弛时间。在其线性剪切版本中，保持应变不变时，速率项消失后弹性应力保持恒定。若解除外加应力，才会产生指数式应变恢复，其时间为迟滞时间。这一区分可避免给球形黏壶模型拟合一个凭空假设的松弛机制。

**Symbols before Eq. (A-E17).**

**式（A-E17）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $T_{\mathrm{sh}}$ is shear stress (Pa)<br>$T_{\mathrm{sh}}$ 为剪切应力（Pa） | $\gamma$ is dimensionless small shear strain<br>$\gamma$ 为无量纲小剪切应变 |
| $\dot\gamma$ its rate (s⁻¹)<br>$\dot\gamma$ 为其速率（s⁻¹） | $G_g>0$ shear modulus (Pa)<br>$G_g>0$ 为剪切模量（Pa） |
| $\eta_g>0$ viscosity (Pa s)<br>$\eta_g>0$ 为黏度（Pa s） | $t\geq0$ is time after release (s)<br>$t\geq0$ 为卸载后的时间（s） |
| $\gamma_0$ initial strain (dimensionless)<br>$\gamma_0$ 为初始应变（无量纲） | $\tau_{\mathrm{KV}}$ the Kelvin–Voigt zero-stress recovery/retardation time (s), and $\exp$ the exponential of a dimensionless argument<br>$\tau_{\mathrm{KV}}$ 为 Kelvin–Voigt 零应力恢复／迟滞时间（s），$\exp$ 表示对无量纲参数取指数 |

**Conventions and conditions.** sh and KV are labels, not multiplication.

**约定与条件。** sh 与 KV 是标签，不是乘法。

(A-E17) · Linear constitutive check for the chosen dashpot

$$
\begin{aligned}T_{\mathrm{sh}}&=G_g\gamma+\eta_g\dot\gamma,\\T_{\mathrm{sh}}=0:\quad\dot\gamma&=-\frac{G_g}{\eta_g}\gamma,\qquad\gamma(t)=\gamma_0\exp(-t/\tau_{\mathrm{KV}}),\qquad\tau_{\mathrm{KV}}:=\frac{\eta_g}{G_g}.\end{aligned}
$$


![Kelvin–Voigt strain recovery illustrates what its parameter ratio means and what it does not mean.](../assets/figures/a-e17.svg)

Kelvin–Voigt strain recovery illustrates what its parameter ratio means and what it does not mean.

Kelvin–Voigt 应变恢复说明其参数比值的意义及不能代表的意义。

Step 10 — test spatial communication. A small-strain shear speed estimate concerns network/shear deformation over a stated length. The ideal liquid-collapse reference concerns radial liquid inertia over a stated maximum radius. Use the same 30 µm comparison length but keep the two physical models distinct. The resulting ratio is 2.44464: global support shear equilibration is not automatically rapid on that liquid-collapse timescale. This is a flag for nonradial support motion, not a proof that the derived spherical model has omitted all inertia.

步骤 10——检验空间传播。小应变剪切波速估计涉及指定长度上的网络／剪切变形；理想液体塌缩参考则涉及指定最大半径上的液体径向惯性。比较时采用相同的 30 µm 长度，但保持两个物理模型的区别。所得比值为 2.44464：整个支撑体的剪切平衡并不自动比该液体塌缩过程快。这提示需关注非径向支撑运动，而不是证明所推导球形模型完全忽略了惯性。

**Symbols before Eq. (A-E18).**

**式（A-E18）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $c_s$ is a small-strain shear speed estimate (m s⁻¹)<br>$c_s$ 为小应变剪切波速估计（m s⁻¹） | $G_g=20000$ Pa modulus<br>$G_g=20000$ Pa 为模量 |
| $\rho_g=1000$ kg m⁻³ medium density<br>$\rho_g=1000$ kg m⁻³ 为介质密度 | $L_g=30$ µm comparison length<br>$L_g=30$ µm 为比较长度 |
| $t_s$ its shear crossing time (s)<br>$t_s$ 为该长度上的剪切传播时间（s） | $t_{c,\mathrm{liq}}$ is ideal empty-liquid-cavity collapse time (s)<br>$t_{c,\mathrm{liq}}$ 为理想空液体腔的塌缩时间（s） |
| $R_{\max}=30$ µm maximum radius<br>$R_{\max}=30$ µm 为最大半径 | $\rho_l=1000$ kg m⁻³ liquid density<br>$\rho_l=1000$ kg m⁻³ 为液体密度 |
| $\Delta p_c=100000$ Pa collapse pressure gap<br>$\Delta p_c=100000$ Pa 为塌缩压力差 |  |

**Conventions and conditions.** The coefficient is the Rayleigh integral; liq labels the liquid control, $\simeq$ is an estimate, and µs means $10^{-6}$ s.

**约定与条件。** 系数来自 Rayleigh 积分；liq 标记液体控制模型，$\simeq$ 表示估计，µs 表示 $10^{-6}$ s。

(A-E18) · Teaching response-time comparison

$$
\begin{aligned}c_s&\simeq\sqrt{G_g/\rho_g}=4.47213595\ \mathrm{m\,s^{-1}},\qquad t_s:=L_g/c_s=6.70820393\ \mathrm{\mu s},\\t_{c,\mathrm{liq}}&=0.9146813565\,R_{\max}\sqrt{\rho_l/\Delta p_c}=2.74404407\ \mathrm{\mu s},\qquad\frac{t_s}{t_{c,\mathrm{liq}}}=2.44464147.\end{aligned}
$$


![The gel communication estimate exceeds the ideal liquid-collapse reference for the declared inputs.](../assets/figures/a-e18.svg)

The gel communication estimate exceeds the ideal liquid-collapse reference for the declared inputs.

对已声明输入，凝胶传播时间估计大于理想液体塌缩参考时间。

Low shear modulus does not imply low rapid-compression resistance. In a small-strain compressible extension, longitudinal motion also samples the bulk modulus. Compressibility must be restored when acoustic travel or high wall speed becomes central. The incompressible spherical control takes that longitudinal propagation idealization to its limit; it cannot predict shock peaks or finite arrival times by itself.

低剪切模量不意味着快速压缩阻力小。在小应变可压缩扩展中，纵向运动还涉及体积模量。当声传播时间或较高泡壁速度变得关键时，必须恢复可压缩性。不可压缩球形控制模型采用了纵向传播的极限理想化；它自身不能预测冲击波峰值或有限传播到达时间。

**Symbols before Eq. (A-E19).**

**式（A-E19）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $c_L$ is longitudinal wave speed estimate (m s⁻¹) in a separate small-strain compressible extension<br>$c_L$ 为独立小应变可压缩扩展中的纵波波速估计（m s⁻¹） | $K_g^{\mathrm{bulk}}>0$ is bulk modulus (Pa), distinctly labeled from kinetic energy $K_g$<br>$K_g^{\mathrm{bulk}}>0$ 为体积模量（Pa），其明确标签使之区别于动能 $K_g$ |
| $G_g$ shear modulus (Pa)<br>$G_g$ 为剪切模量（Pa） | $\rho_g$ density (kg m⁻³)<br>$\rho_g$ 为密度（kg m⁻³） |
| $L_g$ length (m)<br>$L_g$ 为长度（m） | $t_L$ longitudinal crossing time (s)<br>$t_L$ 为纵波传播时间（s） |
| $M_w$ dimensionless wall Mach number<br>$M_w$ 为无量纲泡壁 Mach 数 | $\dot R$ wall speed (m s⁻¹)<br>$\dot R$ 为泡壁速度（m s⁻¹） |
| $K_g$ — Surrounding-medium kinetic energy (J)<br>$K_g$ — 周围介质动能（J） |  |

**Conventions and conditions.** $|\ |$ takes absolute value; $\simeq$ denotes an estimate.

**约定与条件。** $|\ |$ 表示绝对值；$\simeq$ 表示估计。

(A-E19) · Separate compressibility diagnostic

$$
c_L\simeq\sqrt{\frac{K_g^{\mathrm{bulk}}+4G_g/3}{\rho_g}},\qquad t_L:=\frac{L_g}{c_L},\qquad M_w:=\frac{|\dot R|}{c_L}.
$$


![Shear and longitudinal propagation test different aspects of a water-rich gel's transient response.](../assets/figures/a-e19.svg)

Shear and longitudinal propagation test different aspects of a water-rich gel's transient response.

剪切与纵向传播检验富水凝胶瞬态响应的不同方面。

Step 11 — derive the drainage estimate from a separate two-phase approximation. For small perturbations in a uniform gel, adopt Darcy relative solvent flux and a constant storage modulus. Solvent conservation then produces a diffusion equation. This does not extend the large-strain intact-cavity law automatically to porous flow near the vapor interface.

步骤 11——从独立的两相近似推导排水估计。对均匀凝胶中的小扰动，采用 Darcy 相对溶剂通量和恒定储存模量。溶剂守恒随后给出扩散方程。这并不会自动将大应变完整腔体规律扩展到蒸气界面附近的多孔流动。

**Symbols before Eq. (A-E20).**

**式（A-E20）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\mathbf j_l$ is relative solvent volume flux (m s⁻¹)<br>$\mathbf j_l$ 为相对溶剂体积通量（m s⁻¹） | $k_{\mathrm{perm}}>0$ permeability (m²)<br>$k_{\mathrm{perm}}>0$ 为渗透率（m²） |
| $\mu_l>0$ solvent viscosity (Pa s)<br>$\mu_l>0$ 为溶剂黏度（Pa s） | $p_{\mathrm{pore}}$ incremental pore pressure (Pa)<br>$p_{\mathrm{pore}}$ 为增量孔隙压力（Pa） |
| $M_d>0$ storage/constrained drained modulus adopted for this scalar approximation (Pa)<br>$M_d>0$ 为该标量近似采用的储存／受约束排水模量（Pa） | $t$ time (s)<br>$t$ 为时间（s） |
| $D_{\mathrm{poro}}$ diffusion coefficient (m² s⁻¹)<br>$D_{\mathrm{poro}}$ 为扩散系数（m² s⁻¹） | $L_g$ drainage length (m)<br>$L_g$ 为排水长度（m） |
| $t_{\mathrm{poro}}$ drainage time estimate (s)<br>$t_{\mathrm{poro}}$ 为排水时间估计（s） |  |

**Conventions and conditions.** $\nabla$, $\nabla\cdot$, $\nabla^2$ are gradient, divergence and Laplacian in space; the dot here is the vector divergence operator, not an equation separator; $\sim$ means scaling estimate.

**约定与条件。** $\nabla$、$\nabla\cdot$、$\nabla^2$ 为空间梯度、散度和 Laplace 算子；此处点号属于向量散度算子，不是方程分隔符；$\sim$ 表示尺度估计。

(A-E20) · Darcy/storage approximation and derived diffusion

$$
\begin{aligned}\mathbf j_l&=-\frac{k_{\mathrm{perm}}}{\mu_l}\nabla p_{\mathrm{pore}},\qquad\frac{1}{M_d}\frac{\partial p_{\mathrm{pore}}}{\partial t}+\nabla\cdot\mathbf j_l=0,\\\frac{\partial p_{\mathrm{pore}}}{\partial t}&=D_{\mathrm{poro}}\nabla^2p_{\mathrm{pore}},\qquad D_{\mathrm{poro}}:=\frac{k_{\mathrm{perm}}M_d}{\mu_l},\\t_{\mathrm{poro}}&\sim\frac{L_g^2}{D_{\mathrm{poro}}}=\frac{\mu_lL_g^2}{k_{\mathrm{perm}}M_d}.\end{aligned}
$$


![Pressure gradients drive solvent through the network, producing a length-dependent drainage time.](../assets/figures/a-e20.svg)

Pressure gradients drive solvent through the network, producing a length-dependent drainage time.

压力梯度驱动溶剂通过网络，产生依赖长度的排水时间。

Substitute the first row's Darcy flux into conservation to obtain the second row; constant coefficients allow them outside the derivatives. Balance a time derivative against a spatial second derivative over $L_g$ for the third row. This scaling agrees with primary poroelastic gel measurements; the actual permeability and storage modulus still need characterization. For a deliberately illustrative permeability $10^{-17}$ m², modulus 60 kPa, solvent viscosity 0.001 Pa s and length 30 µm, the estimate is 1.5 s. A 3 µs event is then approximately undrained at that length, not proof that no local solvent movement occurs. [Primary drainage study](https://pubs.rsc.org/en/content/articlehtml/2021/sm/d0sm02243h).

将第一行的 Darcy 通量代入守恒式即可得到第二行；常系数可移到导数外。用 $L_g$ 尺度上的空间二阶导数与时间导数平衡，得到第三行。该尺度关系与原始研究中的凝胶孔弹性测量一致；实际渗透率与储存模量仍需表征。若明确采用示例渗透率 $10^{-17}$ m²、模量 60 kPa、溶剂黏度 0.001 Pa s、长度 30 µm，估计时间为 1.5 s。此时 3 µs 事件在该长度上近似不排水，但这不证明完全不存在局部溶剂运动。[原始排水研究](https://pubs.rsc.org/en/content/articlehtml/2021/sm/d0sm02243h)。

## 7. Test mechanisms and compare complete operating windows

## 7. 检验机制，并比较完整工作窗口

The hypothesis that compliant confinement stabilizes a PFC-driven jet remains unresolved. Elastic-boundary experiments by Brujan and colleagues show that deformation and recoil can accompany jets in either direction and ejection of boundary material; their reported maximum liquid-jet speed was 960 m s⁻¹ in a particular laser-bubble/gel geometry. That observation defeats a universal stabilization claim and is not a performance limit or calibration for PFC transfer. [[R12]](../reference/sources.html#r12)

柔顺约束能够稳定 PFC 驱动射流这一假设仍未解决。Brujan 等人的弹性边界实验表明，变形与回弹可伴随向两个方向的射流，以及边界材料喷出；他们在特定激光气泡／凝胶几何中报告的最高液体射流速度为 960 m s⁻¹。该观察否定普适的稳定化主张，却不是 PFC 转印的性能极限或标定。[[R12]](../reference/sources.html#r12)

Keep all four architectures available for experiments. In a liquid pocket, resolve liquid momentum, moving-wall traction and outlet shape together. In bulk embedding, successful vaporization is only the source step: identify the route through which a finite carrier-liquid mass exits, or show that the actuator works by solid deformation instead. In a sealed cavity, use pressure–layer-motion–fracture coupling directly. For the film/PVC concept, retain both direct liquid/film loading and loading transmitted through an intact PVC layer. The intended release interface and payload stress must be identified in either route.

保留全部四种结构方案供实验使用。在液腔中，需要联合解析液体动量、运动壁面牵引与出口形状。对体相嵌入，成功汽化只是源环节：应明确有限载液质量离开的路径，或证明致动器其实通过固体变形工作。对密封腔体，直接采用压力—层运动—断裂耦合。对薄膜／PVC 概念，保留液体直接加载薄膜，以及载荷经完整 PVC 层传递这两条路径。两条路径都必须确定目标释放界面及被转印对象的应力。

| Control or observation<br>控制或观测 | What it discriminates<br>可区分的机制 |
| --- | --- |
| Match PFC inventory, distribution, shell survival, absorber position, initial temperature and measured absorbed energy.<br>匹配 PFC 物质量、分布、壳层存活、吸收体位置、初始温度及实测吸收能量。 | Separates optical/activation changes from mechanical support changes; equal incident energy alone does not do this.<br>将光学／激活变化与力学支撑变化区分开；仅使入射能量相等做不到这一点。 |
| Synchronize cavity contour, gel/film motion, emitted liquid composition, finite jet mass, speed, angle and arrival.<br>同步记录腔体轮廓、凝胶／薄膜运动、喷出液体成分、有限射流质量、速度、角度及到达时间。 | Distinguishes a liquid jet, a recoil-driven second jet, solid fragments and a membrane/blister actuator.<br>区分液体射流、回弹驱动的第二股射流、固体碎片及膜片／鼓泡致动器。 |
| Specify pressure location, area, bandwidth and time window; record displacement and crack progression.<br>明确压力位置、面积、带宽及时间窗口；记录位移和裂纹进展。 | Connects fluid output to interface work and selective release rather than an isolated peak.<br>将流体输出连接到界面功和选择性释放，而不是孤立峰值。 |
| Across independent events, compare angular spread, mass/speed variation, breakup, release success, damage and placement error.<br>在独立事件间比较角度分散、质量／速度变异、破碎、释放成功率、损伤及定位误差。 | Tests repeatability at a useful delivered load; a lower speed variation with insufficient release is not an improved process.<br>在有用的实际传递载荷下检验重复性；若载荷不足以释放，仅速度变异降低不代表工艺改善。 |
| Measure cooling, retained vapor, swelling, residue, network damage and reset before repeated pulses.<br>重复脉冲前测量冷却、滞留蒸气、溶胀、残留物、网络损伤及复位。 | Tests whether positional benefits survive reuse and whether activation/geometry drift accumulates.<br>检验定位优势能否在复用中持续，以及激活／几何漂移是否累积。 |

Report two different outcomes separately: the largest verified single-event pressure or finite-mass jet speed under stated conditions, and the repeatable intact-transfer window. A favorable gel may trade peak speed for controlled peeling and lower placement scatter, or may improve alignment while reducing useful impulse. Neither trade is decidable from the radial resistance formula. The unresolved inputs are event-rate material laws, actual inclusion/reference geometry, damage and phase kinetics, outlet evolution, and the measured release/landing interface laws.

分别报告两个不同结果：指定条件下经验证的最大单次压力或有限质量射流速度，以及可重复的完整转印窗口。有利的凝胶可能以降低峰值速度换取可控剥离和较小定位离散，也可能改善对准却降低有效冲量。这两类取舍都不能由径向阻力公式决定。尚未解决的输入包括事件速率下的材料规律、实际夹杂／参考几何、损伤及相变动力学、出口演化，以及实测释放／落点界面规律。

## 8. Three defense questions: explain the chain in your own words

## 8. 三道答辩题：用自己的话解释物理链条

### Why are an open pocket, bulk-embedded PFC and a sealed hydrogel stamp different actuators?

### 为什么开放液腔、体相嵌入 PFC 和密封水凝胶印章是不同致动器？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (A-E21).**

**式（A-E21）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\rho_g$ is effective exterior density (kg m⁻³)<br>$\rho_g$ 为外部有效密度（kg m⁻³） | $R>0$ cavity radius (m)<br>$R>0$ 为腔体半径（m） |
| $\dot R$ — Cavity-wall radial velocity (m s⁻¹)<br>$\dot R$ — 空腔壁面径向速度（m s⁻¹） | $\ddot R$ — Cavity-wall radial acceleration (m s⁻²)<br>$\ddot R$ — 空腔壁面径向加速度（m s⁻²） |
| $p_b$ — Cavity pressure (Pa)<br>$p_b$ — 空腔压力（Pa） | $p_\infty$ — Far-field pressure (Pa)<br>$p_\infty$ — 远场压力（Pa） |
| $p_{\mathrm{el}}$ — Signed elastic cavity resistance (Pa)<br>$p_{\mathrm{el}}$ — 带符号弹性腔体阻力（Pa） | $\sigma$ tension (N m⁻¹)<br>$\sigma$ 为张力（N m⁻¹） |
| $\eta_g$ represented medium viscosity (Pa s)<br>$\eta_g$ 为所描述介质的黏度（Pa s） |  |

**Conventions and conditions.** This quoted original formula has the intact spherical, no-slip assumptions of Eq; (A-E11).

**约定与条件。** 这一引用的原始公式采用式（A-E11）的完整球形、无滑移假设。

(A-E21) · Original radial control recalled

$$
\rho_g\left(R\ddot R+\frac32\dot R^2\right)=p_b-p_\infty-\frac{2\sigma}{R}-p_{\mathrm{el}}(R)-\frac{4\eta_g\dot R}{R}.
$$


![A radial model describes expansion and resistance; it does not manufacture an outlet.](../assets/figures/a-e21.svg)

A radial model describes expansion and resistance; it does not manufacture an outlet.

径向模型描述膨胀及阻力，不会凭空产生出口。

A defensible explanation begins with where matter can move. A liquid site or open gel-supported pocket can emit carrier liquid through a meniscus/outlet if asymmetric pressure-driven flow develops. A buried inclusion can expand a cavity yet produce no external liquid jet; network rupture or a channel is an additional mechanism with contamination and damage consequences. A sealed composite cavity can instead bend a cover and drive an interfacial crack without any liquid jet leaving the stamp. The hydrogel paper demonstrates this pressure–deformation–release mechanism, not all four architectures.

可成立的解释应从材料能向哪里运动开始。液体位点或开放的凝胶支撑液腔，如果形成非对称的压力驱动流动，就可以通过液面／出口喷出载液。埋入的夹杂可以使腔体膨胀，却不产生外部液体射流；网络破裂或通道属于额外机制，会带来污染与损伤后果。密封复合腔体则可使覆盖层弯曲并驱动界面裂纹，而无需任何液体射流离开印章。水凝胶论文展示的是这种压力—变形—释放机制，并非全部四种结构。

The spherical equation supplies an intact-medium pressure/work control but cannot determine jet direction or release on its own. Use a spatial moving-interface calculation for an outlet, and a solid/interface calculation for a blister or intact PVC force path. A correct answer may retain all candidates while specifying their different missing closure. Successful PFC activation does not prove a carrier jet or selective transfer.

球形方程提供完整介质的压力／功控制关系，但自身不能确定射流方向或释放。对出口需要空间运动界面计算；对鼓泡或完整 PVC 载荷路径，需要固体／界面计算。正确回答可以保留所有候选方案，同时指出各自缺少的不同闭合关系。PFC 成功激活不证明载液射流或选择性转印。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Identifies the displaced-material path and distinguishes external liquid flow from solid deformation or damage.

  明确被排开材料的路径，区分外部液体流动、固体变形与损伤。
* Connects pressure to an explicit outlet or solid/interface load path and states what the spherical equation cannot calculate.

  将压力连接到明确出口或固体／界面载荷路径，并说明球形方程不能计算什么。
* Uses the hydrogel paper as architecture-specific evidence and keeps the other possibilities conditional rather than discarded.

  将水凝胶论文作为特定结构的证据，保留其他条件性可能，而不是排除它们。

### Why does the 5Gg/2 pressure plateau neither prove stabilization nor replace an energy calculation?

### 为什么 5Gg/2 压力平台既不能证明稳定化，也不能代替能量计算？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (A-E22).**

**式（A-E22）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{\mathrm{el}}$ is elastic resistance (Pa)<br>$p_{\mathrm{el}}$ 为弹性阻力（Pa） | $W_g$ stored work (J)<br>$W_g$ 为储存功（J） |
| $G_g>0$ shear modulus (Pa)<br>$G_g>0$ 为剪切模量（Pa） | $R\geq R_{\mathrm{ref}}>0$ — Current cavity radius (m)<br>$R\geq R_{\mathrm{ref}}>0$ — 当前腔体半径（m） |
| $R_{\mathrm{ref}}$ — Stress-free reference cavity radius (m)<br>$R_{\mathrm{ref}}$ — 无应力参考腔体半径（m） | $\pi$ is dimensionless<br>$\pi$ 为无量纲量 |

**Conventions and conditions.** These quote Eqs; (A-E05) and (A-E07) for the intact infinite incompressible neo-Hookean medium.

**约定与条件。** 这些公式引用式（A-E05）与（A-E07），适用于完整、无限、不可压缩 neo-Hookean 介质。

(A-E22) · Original pressure and work formulas recalled

$$
\begin{aligned}p_{\mathrm{el}}(R)&=\frac{G_g}{2}\left[5-4\frac{R_{\mathrm{ref}}}{R}-\left(\frac{R_{\mathrm{ref}}}{R}\right)^4\right],\\W_g(R)&=2\pi G_g\left[\frac{5R^3}{3}-2R_{\mathrm{ref}}R^2+\frac{R_{\mathrm{ref}}^4}{R}-\frac{2R_{\mathrm{ref}}^3}{3}\right].\end{aligned}
$$


![Pressure resistance and elastic work answer different parts of the feasibility calculation.](../assets/figures/a-e22.svg)

Pressure resistance and elastic work answer different parts of the feasibility calculation.

压力阻力与弹性功回答可行性计算中的不同部分。

At the declared 20 kPa modulus and 5 → 30 µm expansion, resistance is 43.3256 kPa and network work is 4.51604 nJ. A constant 100 kPa net-pressure scale supplies 11.2574 nJ over the same displaced volume, so 40.1163% is stored in the model network. Comparing only 43.3 kPa with 100 kPa misses this integral and the remaining surface, viscous and kinetic demands. The 5 µm reference is a cavity/network reference, not an automatically inherited PFC liquid core size.

对设定的 20 kPa 模量和 5 → 30 µm 膨胀，阻力为 43.3256 kPa，网络功为 4.51604 nJ。恒定 100 kPa 净压力尺度在同一排开体积上提供 11.2574 nJ，因此模型网络储存 40.1163%。仅比较 43.3 kPa 与 100 kPa，会漏掉这个积分及剩余的表面、黏性和动能需求。5 µm 参考值属于腔体／网络参考，不是自动沿用的 PFC 液态核尺寸。

The plateau $5G_g/2$ belongs to a selected intact constitutive model. It neither limits fracture nor proves jet stability. Work continues to grow with volume, real material can stiffen or tear, and directional flow is absent from this radial model. Stored elastic energy can return on recoil but may return too late, in another direction, or into damage. Viscous loss, by contrast, is nonnegative in both expansion and collapse. The useful conversion needs the actual phase-pressure history, moving geometry and energy partition, not an assumed efficiency pasted onto the pressure formula.

平台值 $5G_g/2$ 属于选定的完整本构模型。它既不限定断裂，也不证明射流稳定。功仍随体积增长，真实材料可能硬化或撕裂，而且该径向模型没有定向流动。储存弹性能可在回弹时返还，但返还可能太晚、朝另一个方向，或进入损伤。相反，黏性损耗在膨胀与塌缩时都非负。有效转换需要实际相变压力历程、运动几何和能量分配，不能把假定效率直接贴到压力公式上。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Explains the stretch-based elastic origin, zero reference resistance, and constitutive rather than fracture meaning of the plateau.

  说明基于伸长的弹性来源、参考状态零阻力，以及平台属于本构而非断裂意义。
* Uses pressure times volume change to interpret the 4.51604 nJ storage and its 40.1163% benchmark fraction without calling it a predicted jet energy.

  用压力乘体积变化解释 4.51604 nJ 储存及其 40.1163% 示例比例，不将其称为预测射流能量。
* Separates recoverable storage from irreversible viscosity and identifies damage, timing and nonspherical flow as unresolved links.

  区分可恢复储存与不可逆黏性，指出损伤、时序和非球形流动仍是未闭合环节。

### What evidence would establish that a hydrogel improves this PFC transfer process, rather than merely changing its mechanism?

### 什么证据能证明水凝胶改善了该 PFC 转印过程，而不只是改变其机制？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (A-E23).**

**式（A-E23）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\mathrm{De}$ is dimensionless event Deborah number<br>$\mathrm{De}$ 为无量纲事件 Deborah 数 | $\tau_{\mathrm{rel}}$ measured stress-memory time (s)<br>$\tau_{\mathrm{rel}}$ 为实测应力记忆时间（s） |
| $\tau_e$ event duration (s)<br>$\tau_e$ 为事件持续时间（s） | $t_s$ — Shear crossing-time estimate (s)<br>$t_s$ — 剪切跨越时间估计（s） |
| $t_{\mathrm{poro}}$ — Drainage-time estimate (s)<br>$t_{\mathrm{poro}}$ — 排水时间估计（s） | $L_g$ is a specified length (m)<br>$L_g$ 为指定长度（m） |
| $G_g$ shear modulus (Pa)<br>$G_g$ 为剪切模量（Pa） | $\rho_g$ density (kg m⁻³)<br>$\rho_g$ 为密度（kg m⁻³） |
| $\mu_l$ solvent viscosity (Pa s)<br>$\mu_l$ 为溶剂黏度（Pa s） | $k_{\mathrm{perm}}$ permeability (m²)<br>$k_{\mathrm{perm}}$ 为渗透率（m²） |
| $M_d$ adopted drained storage modulus (Pa)<br>$M_d$ 为所采用的排水储存模量（Pa） |  |

**Conventions and conditions.** $\sim$ denotes scaling and the square root is the small-strain shear-speed estimate; These recall Eqs; (A-E16), (A-E18) and (A-E20).

**约定与条件。** $\sim$ 表示尺度关系，平方根为小应变剪切波速估计；这些公式引用式（A-E16）、（A-E18）、（A-E20）。

(A-E23) · Original event-response formulas recalled

$$
\mathrm{De}=\frac{\tau_{\mathrm{rel}}}{\tau_e},\qquad t_s=\frac{L_g}{\sqrt{G_g/\rho_g}},\qquad t_{\mathrm{poro}}\sim\frac{\mu_lL_g^2}{k_{\mathrm{perm}}M_d}.
$$


![Three timescale comparisons constrain three different physical assumptions.](../assets/figures/a-e23.svg)

Three timescale comparisons constrain three different physical assumptions.

三个时间尺度比较分别约束三个不同的物理假设。

**Symbols before Eq. (A-E24).**

**式（A-E24）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\mathbf J_{\mathrm{target}}$ is vector impulse delivered to the specified target (N s)<br>$\mathbf J_{\mathrm{target}}$ 为传递到指定目标的向量冲量（N s） | $\mathbf t_{\mathrm{load}}$ is external load traction (Pa)<br>$\mathbf t_{\mathrm{load}}$ 为外加载荷牵引（Pa） |
| $A_t$ target loading area (m²)<br>$A_t$ 为目标受载面积（m²） | $t_0$ — Specified event start time (s)<br>$t_0$ — 指定事件开始时刻（s） |
| $t_1$ — Specified event end time (s)<br>$t_1$ — 指定事件结束时刻（s） | $W_{\mathrm{sep,min}}$ is necessary fracture-work budget (J)<br>$W_{\mathrm{sep,min}}$ 为必要断裂功预算（J） |
| $A_{\mathrm{rel}}$ intended released interface area (m²)<br>$A_{\mathrm{rel}}$ 为目标释放界面面积（m²） | $\Gamma_c$ relevant interface fracture energy (J m⁻²), conditional on mode and rate<br>$\Gamma_c$ 为相关界面断裂能（J m⁻²），取决于模态与速率 |
| $dA$ — Area integration element (m²)<br>$dA$ — 面积积分微元（m²） | $dt$ — Time integration element (s)<br>$dt$ — 时间积分微元（s） |

**Conventions and conditions.** Neither integral alone proves crack onset or intact landing.

**约定与条件。** 这两个积分都不能独自证明裂纹起始或完整落点。

(A-E24) · Original load and interface-work accounting

$$
\mathbf J_{\mathrm{target}}=\int_{t_0}^{t_1}\int_{A_t}\mathbf t_{\mathrm{load}}\,dA\,dt,\qquad W_{\mathrm{sep,min}}=\int_{A_{\mathrm{rel}}}\Gamma_c\,dA.
$$


![A fair comparison follows the delivered load into the intended interface and the final placement.](../assets/figures/a-e24.svg)

A fair comparison follows the delivered load into the intended interface and the final placement.

公平比较要跟踪实际载荷进入目标界面及最终定位。

I would preserve all architectures and match the PFC batch/inventory, absorber location, absorbed energy, initial temperature, outlet definition and release interface where physically possible. When an architecture changes a matched condition, I would measure that change and report the comparison as conditional. I would characterize network behavior at the event strain, rate and temperature, test shell survival and heat deposition, and distinguish the 6.7082 µs shear estimate from the 2.7440 µs empty-liquid reference. Those times do not predict the actual gel-cavity event or longitudinal shock load.

我会保留所有结构方案，并在物理允许范围内匹配 PFC 批次／物质量、吸收体位置、吸收能量、初始温度、出口定义及释放界面。若某一结构改变了匹配条件，就测量该变化，并将比较报告为有条件的比较。我会在事件的应变、速率和温度下表征网络行为，检验壳层存活及热沉积，并区分 6.7082 µs 剪切时间估计与 2.7440 µs 空液体参考。这两个时间不能预测实际凝胶腔体事件或纵向冲击载荷。

Then I would synchronize cavity, jet/composition, solid motion, calibrated load and crack images; compare independent-shot distributions and intact placement, contamination and reset. Stabilization means lower relevant angle/speed/mass/footprint variability at sufficient useful load, not one slower or smaller bubble. I would report the largest verified single-event output separately from the repeatable intact-transfer envelope. Missing rate-dependent mechanics, permeability, phase kinetics or fracture data leave a stated uncertainty instead of being replaced by the published hydrogel stamp's parameters.

随后，我会同步记录腔体、射流／成分、固体运动、标定载荷和裂纹影像；比较独立事件的分布，以及完整定位、污染和复位。稳定化意味着在足够的有效载荷下，相关角度／速度／质量／载荷范围变异降低，而不是一次更慢或更小的气泡。我会分别报告经验证的最大单次输出与可重复的完整转印范围。若缺少速率相关力学、渗透率、相变动力学或断裂数据，就明确保留不确定性，而不是用已发表水凝胶印章的参数代替。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Defines a fair absorbed-energy/material/geometry comparison while retaining each architecture and both film/PVC load paths.

  定义公平的吸收能量／材料／几何比较，同时保留每种结构及两条薄膜／PVC 载荷路径。
* Distinguishes stress memory, shear communication, solvent drainage and longitudinal compression, with the assumptions of each estimate.

  区分应力记忆、剪切传播、溶剂排水与纵向压缩，并说明各估计的假设。
* Links synchronized mechanism measurements to useful impulse, selective fracture, intact placement, variability and reset; separates extreme output from repeatable transfer.

  将同步机制测量连接到有效冲量、选择性断裂、完整定位、变异与复位；区分极端输出与可重复转印。