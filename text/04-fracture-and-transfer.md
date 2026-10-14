# Chapter 4: Fracture and transfer

# 第 4 章：断裂与转印

## 1. Intended-interface release

## 1. 目标界面释放

Connect the arriving jet to film deformation, crack growth and departure. Useful transfer ends with intact attachment at the intended receiver location. Chapter 3 supplies velocity, mass, momentum, energy, footprint and arrival history. Specify the exposed surface carrying that load. The output is opening and fracture at the release interface. These surfaces can lie at different stack positions.

本章将到达射流连接至薄膜变形、裂纹增长及离开。有效转印以完整对象附着于目标位置结束。第三章提供速度、质量、动量、能量、作用面积及到达历程。须注明承受该载荷的外露表面。输出是释放界面的张开与断裂，两表面可位于叠层不同位置。

Use Cartesian coordinates with the initial film horizontal. Positive vertical points along intended departure. Start the film at rest with specified adhesion and pre-existing delamination. Plate examples fix the donor reference face. A moving donor needs momentum and power balances. Pressure compresses the exposed face. Interface opening depends on relative face separation. Either prescribe fluid traction or resolve compatible fluid–solid velocities and opposite tractions. Count the interface load once.

采用笛卡尔坐标，初始薄膜水平。竖直正方向为预期离开方向。薄膜初始静止，给定粘附及已有脱层。板示例固定供体参考面。运动供体需动量与功率平衡。压力压缩外露面，界面张开取决于两面的相对分离。可给定流体牵引，或解析相容流固速度及相反牵引。界面载荷计入一次。

| Architecture<br>结构方案 | Force path<br>传力路径 | What must be solved<br>需要求解的内容 |
| --- | --- | --- |
| Direct liquid-to-film actuation<br>液体直接致动薄膜 | Liquid or jet → exposed film → release interface.<br>液体或射流 → 外露薄膜 → 释放界面。 | Fluid traction, film deformation and interface separation.<br>流体牵引、薄膜变形及界面分离。 |
| Intact PVC-mediated actuation<br>完整PVC层介导致动 | Liquid or jet → PVC → contact or bond → film → release interface.<br>液体或射流 → PVC → 接触或粘接层 → 薄膜 → 释放界面。 | PVC inertia, thickness, compliance, reflections, contact and the transmitted traction.<br>PVC的惯性、厚度、柔顺性、反射、接触及传递牵引。 |
| Sealed cavity<br>封闭腔体 | Finite vapor source → cavity wall or stamp → release interface.<br>有限蒸气源 → 腔壁或印章 → 释放界面。 | Coupled cavity thermodynamics, bulging and fracture; an outgoing jet need not exist.<br>耦合腔体热力学、鼓起与断裂；不一定存在出射射流。 |

Intact PVC blocks liquid passage. An incident jet first loads PVC. Direct film loading requires an actual opening or rupture. Sealed cavities and open pockets have different force paths. Appendix A compares these hydrogel architectures.

完整 PVC 阻挡液体穿透，入射射流首先加载 PVC。直接加载薄膜需要实际开口或破裂。密闭空腔与开放液腔具有不同传力路径。附录 A 比较这些水凝胶结构。

### Symbols and model limits

### 符号与模型范围

| Symbol<br>符号 | Physical meaning<br>物理意义 | SI units<br>SI 单位 | Role and convention<br>作用与约定 |
| --- | --- | --- | --- |
| $\boldsymbol n_f$ | Solid-to-liquid unit normal<br>固体指向液体的单位法向 | 1 | At a film with liquid below, it points downward; pressure traction can still push upward.<br>对于下方接触液体的薄膜，该法向向下；压力牵引仍可向上推动。 |
| $\boldsymbol t_l$ | Liquid traction on the solid<br>液体施加于固体的牵引 | Pa | Stress contracted with the specified normal at the exposed face.<br>外露面上应力与指定法向的收缩。 |
| $p$ | Liquid absolute pressure<br>液体绝对压力 | Pa | Acts compressively on the exposed face; release-interface opening depends on structural motion.<br>对外露面产生压缩作用；释放界面张开取决于结构运动。 |
| $q$ | Signed transverse applied load<br>带符号横向外加载荷 | Pa | Positive in the upward film-opening direction; distinguishes applied pressure from net reactions.<br>沿薄膜向上张开方向取正；区分外加压力与净反力。 |
| $w$ | Film transverse displacement<br>薄膜横向位移 | m | Positive upward; its spatial profile determines bending and interface opening.<br>向上取正；其空间分布决定弯曲与界面张开。 |
| $\dot w$ | Film transverse velocity<br>薄膜横向速度 | m s⁻¹ | First time derivative of displacement; enters kinetic energy and power.<br>位移的一阶时间导数；进入动能及功率计算。 |
| $\ddot w$ | Film transverse acceleration<br>薄膜横向加速度 | m s⁻² | Second time derivative of displacement; gives the areal inertial load.<br>位移的二阶时间导数；给出单位面积惯性载荷。 |
| $h_f$ | Film thickness<br>薄膜厚度 | m | Controls areal mass and the cubic thickness dependence of bending rigidity.<br>控制面质量及弯曲刚度对厚度的三次方依赖。 |
| $\rho_f$ | Film mass density<br>薄膜质量密度 | kg m⁻³ | Solid density used in areal mass; distinct from the incoming liquid density.<br>面质量采用的固体密度；与入射液体密度不同。 |
| $E_f$ | Film Young’s modulus<br>薄膜杨氏模量 | Pa | Elastic stiffness for the declared thin-plate constitutive control.<br>指定薄板本构对照的弹性刚度参数。 |
| $\nu_f$ | Film Poisson’s ratio<br>薄膜泊松比 | 1 | Relates transverse and longitudinal elastic strains within the adopted isotropic model.<br>在所采用各向同性模型中关联横向与纵向弹性应变。 |
| $D_f$ | Film bending rigidity<br>薄膜弯曲刚度 | N m | Combines modulus, thickness and Poisson’s ratio; not a diffusivity or strain-rate tensor.<br>结合模量、厚度与泊松比；不是扩散率或应变率张量。 |
| $\Gamma$ | Practical interfacial fracture energy<br>实际界面断裂能 | J m⁻² | Resistance per newly released area under the relevant mode and rate; not a geometric surface here.<br>相关模式与速率下单位新释放面积的阻力；此处不是几何曲面。 |
| $G$ | Mechanical energy-release rate<br>力学能量释放率 | J m⁻² | Energy available per incremental crack area; compared with fracture resistance.<br>单位增量裂纹面积可获得的能量；与断裂阻力比较。 |
| $T_{\max}$ | Peak tensile cohesive traction<br>峰值拉伸内聚牵引 | Pa | Local cohesive strength; not equivalent to interfacial fracture energy.<br>局部内聚强度；不等同于界面断裂能。 |
| $\delta$ | Relative opening of the release interface<br>释放界面相对张开量 | m | Relative displacement across the bonded interface; not the absolute displacement of one film.<br>粘接界面两侧的相对位移；不是某一薄膜的绝对位移。 |
| $a$ | Circular released/blister radius<br>圆形释放／鼓泡区域半径 | m | Defines the crack front and domain size in the clamped circular-plate control.<br>在固支圆板对照中定义裂纹前缘与区域尺度。 |
| $t$ | Time<br>时间 | s | Independent coordinate for pulse loading, inertia and fracture evolution.<br>脉冲受载、惯性及断裂演化的独立坐标。 |
| $\nabla_\parallel$ | Film-plane spatial gradient<br>薄膜平面空间梯度 | m⁻¹ | Differentiates within the plate plane; it is an operator rather than a material parameter.<br>在薄板平面内求导；是算子，而非材料参数。 |

## 2. Fluid stress and solid loading

## 2. 流体应力与固体加载

Step 1 — Adopt Newtonian liquid stress. Orient the normal from solid into liquid. Stress contracted with this normal gives liquid traction on solid. For liquid below a film, the normal points down. Positive pressure pushes the film up while compressing its exposed face. Opening another interface requires deformation and relative motion.

步骤 1——采用牛顿液体应力。法向由固体指向液体，应力与该法向收缩给出液体对固体的牵引。液体位于薄膜下方时，法向向下，正压力将薄膜向上推，同时压缩外露面。另一个界面的张开需要变形及相对运动。

**Symbols before Eq. (C4-E01).**

**式（C4-E01）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol u(\boldsymbol x,t)$ is liquid velocity (m s⁻¹)<br>$\boldsymbol u(\boldsymbol x,t)$为液体速度（m s⁻¹） | $\boldsymbol x$ position (m)<br>$\boldsymbol x$为位置（m） |
| $t$ time (s)<br>$t$为时间（s） | $\boldsymbol D_u$ is strain-rate tensor (s⁻¹)<br>$\boldsymbol D_u$为应变率张量（s⁻¹） |
| $\boldsymbol T_l$ liquid Cauchy stress (Pa)<br>$\boldsymbol T_l$为液体柯西应力（Pa） | $p$ liquid pressure (Pa)<br>$p$为液体压力（Pa） |
| $\mu\ge0$ dynamic viscosity (Pa s)<br>$\mu\ge0$为动力黏度（Pa s） | $\boldsymbol I$ the dimensionless identity tensor<br>$\boldsymbol I$为无量纲单位张量 |
| $\boldsymbol n_f$ is the unit solid-to-liquid normal (dimensionless)<br>$\boldsymbol n_f$为固体指向液体的单位法向（无量纲） | $\boldsymbol t_l$ is traction on the solid (Pa)<br>$\boldsymbol t_l$为固体上的牵引（Pa） |

**Conventions and conditions.** $\nabla$ is the spatial gradient (m⁻¹); superscript $\mathsf T$ transposes a tensor; Subscripts u, l and f label velocity strain, liquid and film surface.

**约定与条件。** $\nabla$为空间梯度（m⁻¹）；上标$\mathsf T$表示张量转置；下标u、l、f分别标识速度应变、液体及薄膜表面。

(C4-E01) · Constitutive assumption and traction identity / 本构假设与牵引恒等式


$$
\boldsymbol D_u=\frac{\nabla\boldsymbol u+(\nabla\boldsymbol u)^{\mathsf T}}{2},\qquad \boldsymbol T_l=-p\boldsymbol I+2\mu\boldsymbol D_u,\qquad \boldsymbol t_l=\boldsymbol T_l\boldsymbol n_f
$$


![Pressure and shear act at the exposed film face; the drawn normal fixes the traction sign.](../assets/figures/c4-e01.svg)

Pressure and shear act at the exposed film face; the drawn normal fixes the traction sign.

压力与剪切作用于薄膜外露面；所画法向决定牵引符号。

Step 2 — Integrate traction over area for force. Integrate force over time for impulse. Dot traction with surface velocity before integrating work. Pressure, impulse and work have units Pa, N s and J. A nearly rigid surface can receive high stress and impulse with little displacement work.

步骤 2——对面积积分牵引得到力，对时间积分力得到冲量。求功时先将牵引与表面速度点乘。压力、冲量与功单位分别为 Pa、N s 和 J。近刚性表面可承受大应力及冲量，同时位移功很小。

**Symbols before Eq. (C4-E02).**

**式（C4-E02）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $A_f(t)$ is the loaded solid surface (m²)<br>$A_f(t)$为固体受载表面（m²） | $dA$ its surface-area element (m²), and $\int$ denotes integration over the indicated surface or time<br>$dA$为表面积微元（m²），$\int$表示对所示表面或时间积分 |
| $\boldsymbol t_l$ is applied liquid traction (Pa)<br>$\boldsymbol t_l$为液体施加的牵引（Pa） | $\boldsymbol F_l$ its resultant (N)<br>$\boldsymbol F_l$为其合力（N） |
| $\boldsymbol I_l$ its impulse (N s)<br>$\boldsymbol I_l$为其冲量（N s） | $\mathcal W_l$ work delivered to the solid (J)<br>$\mathcal W_l$为传入固体的功（J） |
| $\boldsymbol v_f$ is local solid surface velocity (m s⁻¹)<br>$\boldsymbol v_f$为固体表面局部速度（m s⁻¹） | $t_a$ — Load-event start time (s)<br>$t_a$ — 载荷事件开始时刻（s） |
| $t_b$ — Load-event end time (s)<br>$t_b$ — 载荷事件结束时刻（s） | $t$ — Time (s)<br>$t$ — 时间（s） |
| $dt$ — Time integration element (s)<br>$dt$ — 时间积分微元（s） |  |

**Conventions and conditions.** The vector dot product projects force onto velocity; Subscripts l and f label liquid and film; $t_a<t_b$ fixes the integration interval..

**约定与条件。** 向量点乘将力投影到速度上；下标l和f表示液体与薄膜；$t_a<t_b$ 确定积分区间。。

(C4-E02) · Exact mechanical definitions / 精确的力学定义


$$
\begin{aligned}\boldsymbol F_l(t)&=\int_{A_f(t)}\boldsymbol t_l\,dA,\\ \boldsymbol I_l&=\int_{t_a}^{t_b}\boldsymbol F_l(t)\,dt,\\ \mathcal W_l&=\int_{t_a}^{t_b}\int_{A_f(t)}\boldsymbol t_l\cdot\boldsymbol v_f\,dA\,dt.\end{aligned}
$$


![The same footprint supplies force and impulse, but surface motion is additionally required for work.](../assets/figures/c4-e02.svg)

The same footprint supplies force and impulse, but surface motion is additionally required for work.

同一作用范围决定力与冲量，而求功还需要表面运动信息。

## 3. Transient film mechanics

## 3. 瞬态薄膜力学

Step 3 — Adopt a homogeneous isotropic Kirchhoff–Love plate. Assume elastic plane stress, small strain, small slope and thinness relative to deformation length. Through-thickness density integration gives areal mass. Bending stress integration gives stiffness with thickness moment thickness³/12. A bonded laminate needs a common neutral surface and laminate stiffness.

步骤 3——采用均匀各向同性 Kirchhoff–Love 板。假设弹性平面应力、小应变、小斜率，厚度远小于变形长度。沿厚度积分密度得到面质量。积分弯曲应力得到刚度，其中厚度矩为厚度³／12。粘接叠层需共同中性面及叠层刚度。

**Symbols before Eq. (C4-E03).**

**式（C4-E03）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_A>0$ is film areal mass (kg m⁻²)<br>$m_A>0$为薄膜面密度（kg m⁻²） | $D_f>0$ bending stiffness (N m)<br>$D_f>0$为弯曲刚度（N m） |
| $\rho_f>0$ constant density (kg m⁻³)<br>$\rho_f>0$为恒定密度（kg m⁻³） | $h_f>0$ film thickness (m)<br>$h_f>0$为薄膜厚度（m） |
| $E_f>0$ Young’s modulus (Pa)<br>$E_f>0$为杨氏模量（Pa） | $-1<\nu_f<1/2$ Poisson’s ratio (dimensionless)<br>$-1<\nu_f<1/2$为泊松比（无量纲） |
| $z$ is thickness coordinate (m), zero at the neutral midplane<br>$z$为厚度坐标（m），中性面处为零 | $dz$ is its integration element (m)<br>$dz$为其积分微元（m） |

**Conventions and conditions.** $\int$ is definite thickness integration; Subscripts A and f label areal quantity and film.

**约定与条件。** $\int$表示沿厚度定积分；下标A与f标识面量与薄膜。

(C4-E03) · Derived plate parameters under constitutive assumptions / 在本构假设下推导的板参数


$$
m_A=\int_{-h_f/2}^{h_f/2}\rho_f\,dz=\rho_fh_f,\qquad D_f=\frac{E_f}{1-\nu_f^2}\int_{-h_f/2}^{h_f/2}z^2\,dz=\frac{E_fh_f^3}{12(1-\nu_f^2)}
$$


![Areal inertia and bending stiffness come from different thickness integrals.](../assets/figures/c4-e03.svg)

Areal inertia and bending stiffness come from different thickness integrals.

面惯性与弯曲刚度来自不同的厚度积分。

Step 4 — Write kinetic, bending and pretension energies. Curvature is the displacement’s second spatial derivative. Poisson ratio couples the two curvature directions and twist. Hold pretension uniform; its energy penalizes slope. Shape stores elastic energy, while velocity carries kinetic energy.

步骤 4——写出动能、弯曲能及预张力能。曲率为位移空间二阶导数。泊松比耦合两方向曲率与扭曲。预张力保持均匀，其能量随斜率增加。形状储存弹性能，速度携带动能。

**Symbols before Eq. (C4-E04).**

**式（C4-E04）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Omega_f$ is the reference film plane (m²)<br>$\Omega_f$为薄膜参考平面（m²） | $dA$ its area element (m²)<br>$dA$为面积微元（m²） |
| $w(x,y,t)$ vertical displacement (m)<br>$w(x,y,t)$为竖直位移（m） | $x$ — First Cartesian in-plane coordinate (m)<br>$x$ — 第一笛卡尔面内坐标（m） |
| $y$ — Second Cartesian in-plane coordinate (m)<br>$y$ — 第二笛卡尔面内坐标（m） | $t$ time (s)<br>$t$为时间（s） |
| $m_A$ is areal mass (kg m⁻²)<br>$m_A$为面密度（kg m⁻²） | $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） |
| $\nu_f$ Poisson’s ratio<br>$\nu_f$为泊松比 | $T_0\ge0$ prescribed isotropic tensile force per edge length (N m⁻¹)<br>$T_0\ge0$为给定各向同性单位边长拉力（N m⁻¹） |
| $K_f$ — Film kinetic energy (J)<br>$K_f$ — 薄膜动能（J） | $U_b$ — Plate bending energy, not bubble internal energy in this unit (J)<br>$U_b$ — 板弯曲能，本单元不表示气泡内能（J） |
| $U_T$ — Stored pretension energy (J)<br>$U_T$ — 预张力储能（J） |  |

**Conventions and conditions.** A dot differentiates in time; subscripts $xx,yy,xy$ differentiate twice in the indicated coordinates, giving curvatures (m⁻¹); $\nabla_\parallel$ is the in-plane gradient; $|\ |$ denotes Euclidean magnitude; $\int$ denotes area integration; Labels f, b, T identify film, bending and tension.

**约定与条件。** 上点表示时间导数；下标$xx,yy,xy$表示对所示坐标求二阶导数，得到曲率（m⁻¹）；$\nabla_\parallel$为面内梯度；$|\ |$为欧氏模长；$\int$表示面积积分；标签f、b、T分别指薄膜、弯曲与张力。

(C4-E04) · Linear-plate energy model / 线性板的能量模型


$$
\begin{aligned}K_f&=\frac{m_A}{2}\int_{\Omega_f}\dot w^2\,dA,\\U_b&=\frac{D_f}{2}\int_{\Omega_f}\left[w_{xx}^2+w_{yy}^2+2\nu_fw_{xx}w_{yy}+2(1-\nu_f)w_{xy}^2\right]dA,\\U_T&=\frac{T_0}{2}\int_{\Omega_f}|\nabla_\parallel w|^2\,dA.\end{aligned}
$$


![Bending energy is stored by curvature; inertia depends on velocity.](../assets/figures/c4-e04.svg)

Bending energy is stored by curvature; inertia depends on velocity.

曲率储存弯曲能，速度决定惯性动能。

Step 5 — Vary displacement at a fixed clamped boundary. Integrate bending terms by parts twice. Displacement variation and its normal slope vanish at the clamp, eliminating boundary terms. Integrate tension once to obtain minus the Laplacian. Every transverse-balance term has pressure units.

步骤 5——在固定夹持边界下变分位移。弯曲项分部积分两次。夹持处位移变分及其法向斜率为零，消去边界项。张力项分部积分一次，得到负拉普拉斯。横向平衡各项均为压力单位。

**Symbols before Eq. (C4-E40).**

**式（C4-E40）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Omega_f$ is the smooth reference film plane (m²), $\partial\Omega_f$ its boundary<br>$\Omega_f$为光滑薄膜参考平面（m²），$\partial\Omega_f$为其边界 | $dA$ area element (m²)<br>$dA$为面积微元（m²） |
| $d\ell$ boundary arc-length element (m)<br>$d\ell$为边界弧长微元（m） | $w$ is displacement (m)<br>$w$为位移（m） |
| $\delta w$ an admissible infinitesimal variation (m)<br>$\delta w$为容许无穷小变分（m） | $\delta U_b$ — Bending-energy variation (J)<br>$\delta U_b$ — 弯曲能变分（J） |
| $\delta U_T$ — Pretension-energy variation (J)<br>$\delta U_T$ — 预张力能变分（J） | $\alpha$ — Cartesian in-plane direction index, taking 1 or 2 (dimensionless)<br>$\alpha$ — 取 1 或 2 的笛卡尔面内方向指标（无量纲） |
| $\beta$ — Cartesian in-plane direction index, taking 1 or 2 (dimensionless)<br>$\beta$ — 取 1 或 2 的笛卡尔面内方向指标（无量纲） | $w_{\alpha\beta}=\partial_\alpha\partial_\beta w$ is curvature (m⁻¹)<br>$w_{\alpha\beta}=\partial_\alpha\partial_\beta w$为曲率（m⁻¹） |
| $D_f$ is bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） | $\nu_f$ Poisson’s ratio<br>$\nu_f$为泊松比 |
| $T_0$ pretension (N m⁻¹)<br>$T_0$为预张力（N m⁻¹） | $B_{\alpha\beta}$ the bending-energy tensor conjugate to curvature (N)<br>$B_{\alpha\beta}$为与曲率共轭的弯曲能张量（N） |
| $\delta_{\alpha\beta}$ is the dimensionless Kronecker identity, distinct from variation notation<br>$\delta_{\alpha\beta}$为无量纲Kronecker单位张量，与变分记号不同 | $n_\alpha$ — Component of the outward in-plane unit normal (dimensionless)<br>$n_\alpha$ — 面内外单位法向的分量（无量纲） |
| $n_\beta$ — Component of the outward in-plane unit normal (dimensionless)<br>$n_\beta$ — 面内外单位法向的分量（无量纲） | $\boldsymbol0$ is zero gradient (dimensionless)<br>$\boldsymbol0$为零梯度（无量纲） |

**Conventions and conditions.** $\partial_\alpha$ is coordinate differentiation (m⁻¹); $\partial_n$ its derivative; $\nabla_\parallel$ and $\nabla_\parallel^2$ are in-plane gradient and Laplacian; $\int,\oint$ denote area and closed-boundary integrals; $\Rightarrow$ uses zero tangential derivative of an identically zero boundary variation plus the prescribed zero normal derivative; $\sum_{\alpha,\beta=1}^{2}$ sums all four index pairs..

**约定与条件。** $\partial_\alpha$为坐标求导（m⁻¹）；$\partial_n$为沿该法向求导；$\nabla_\parallel$及$\nabla_\parallel^2$为面内梯度及拉普拉斯算子；$\int,\oint$分别表示面积积分与闭合边界积分；$\Rightarrow$使用恒为零的边界变分具有零切向导数，并结合给定零法向导数；$\sum_{\alpha,\beta=1}^{2}$ 对四种指标组合求和。。

(C4-E40) · Explicit integration-by-parts boundary terms / 明确写出的分部积分边界项


$$
\begin{aligned}B_{\alpha\beta}&=D_f[(1-\nu_f)w_{\alpha\beta}+\nu_f\delta_{\alpha\beta}\nabla_\parallel^2w],\\\delta U_b&=\sum_{\alpha,\beta=1}^{2}\int_{\Omega_f}B_{\alpha\beta}\partial_\alpha\partial_\beta(\delta w)\,dA\\&=\sum_{\alpha,\beta=1}^{2}\oint_{\partial\Omega_f}n_\alpha B_{\alpha\beta}\partial_\beta(\delta w)\,d\ell-\sum_{\alpha,\beta=1}^{2}\int_{\Omega_f}(\partial_\alpha B_{\alpha\beta})\partial_\beta(\delta w)\,dA\\&=\sum_{\alpha,\beta=1}^{2}\oint_{\partial\Omega_f}[n_\alpha B_{\alpha\beta}\partial_\beta(\delta w)-n_\beta(\partial_\alpha B_{\alpha\beta})\delta w]\,d\ell+\sum_{\alpha,\beta=1}^{2}\int_{\Omega_f}(\partial_\beta\partial_\alpha B_{\alpha\beta})\delta w\,dA,\\\delta U_T&=T_0\oint_{\partial\Omega_f}\delta w\,\partial_nw\,d\ell-T_0\int_{\Omega_f}\delta w\nabla_\parallel^2w\,dA,\\\delta w=0,\quad\partial_n\delta w=0&\ \Longrightarrow\ \nabla_\parallel\delta w=\boldsymbol0\quad\text{on the fixed clamp}.\end{aligned}
$$


![Two integrations by parts expose the boundary moment and shear terms before they are removed.](../assets/figures/c4-e40.svg)

Two integrations by parts expose the boundary moment and shear terms before they are removed.

两次分部积分先明确显示边界弯矩与剪力项，再依据条件将其消去。

**Symbols before Eq. (C4-E05).**

**式（C4-E05）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\delta w$ is a displacement variation (m)<br>$\delta w$为位移变分（m） | $U_b$ — Plate bending energy, not bubble internal energy in this unit (J)<br>$U_b$ — 板弯曲能，本单元不表示气泡内能（J） |
| $U_T$ — Stored pretension energy (J)<br>$U_T$ — 预张力储能（J） | $D_f$ is bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） |
| $\nu_f$ is dimensionless Poisson’s ratio<br>$\nu_f$为无量纲泊松比 | $T_0$ is uniform pretension (N m⁻¹)<br>$T_0$为均匀预张力（N m⁻¹） |
| $w$ is transverse displacement (m)<br>$w$为横向位移（m） | $x$ — First Cartesian in-plane coordinate (m)<br>$x$ — 第一笛卡尔面内坐标（m） |
| $y$ — Second Cartesian in-plane coordinate (m)<br>$y$ — 第二笛卡尔面内坐标（m） | $\Omega_f$ is film area (m²)<br>$\Omega_f$为薄膜面积（m²） |
| $dA$ is its element (m²)<br>$dA$为面积微元（m²） |  |

**Conventions and conditions.** Subscripts $xxxx,xxyy,yyyy$ denote the indicated fourth derivatives (m⁻³); $\nabla_\parallel^2=\partial_x^2+\partial_y^2$ is the in-plane Laplacian; $\nabla_\parallel^4$ is that Laplacian applied twice; $\int$ is area integration; The variations and their normal slopes vanish at a clamped boundary; $\delta$ denotes an infinitesimal admissible variation, not physical crack opening here.

**约定与条件。** 下标$xxxx,xxyy,yyyy$表示所示四阶导数（m⁻³）；$\nabla_\parallel^2=\partial_x^2+\partial_y^2$为面内拉普拉斯算子；$\nabla_\parallel^4$为将该算子作用两次；$\int$表示面积积分；夹持边界处变分及其法向斜率均为零；$\delta$在此表示无穷小容许变分，而非物理裂纹张开。

(C4-E05) · Derived variational identity for fixed clamps / 固定夹持条件下推导的变分恒等式


$$
\begin{aligned}\delta U_b&=D_f\int_{\Omega_f}\left[w_{xxxx}+\{2\nu_f+2(1-\nu_f)\}w_{xxyy}+w_{yyyy}\right]\delta w\,dA\\&=D_f\int_{\Omega_f}(w_{xxxx}+2w_{xxyy}+w_{yyyy})\delta w\,dA=D_f\int_{\Omega_f}\nabla_\parallel^4w\,\delta w\,dA,\\\delta U_T&=-T_0\int_{\Omega_f}\nabla_\parallel^2w\,\delta w\,dA.\end{aligned}
$$


![A fixed clamp removes the boundary virtual-work terms.](../assets/figures/c4-e05.svg)

A fixed clamp removes the boundary virtual-work terms.

固定夹持边界使边界虚功项消失。

**Symbols before Eq. (C4-E06).**

**式（C4-E06）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $w(\boldsymbol x,t)$ is film displacement in the positive departure direction (m)<br>$w(\boldsymbol x,t)$为沿正离开方向的薄膜位移（m） | $\boldsymbol x=(x,y)$ is in-plane position (m)<br>$\boldsymbol x=(x,y)$为面内位置（m） |
| $t$ time (s)<br>$t$为时间（s） | $\dot w$ — Film transverse velocity (m s⁻¹)<br>$\dot w$ — 薄膜横向速度（m s⁻¹） |
| $\ddot w$ — Film transverse acceleration (m s⁻²)<br>$\ddot w$ — 薄膜横向加速度（m s⁻²） | $m_A$ is areal mass (kg m⁻²)<br>$m_A$为面密度（kg m⁻²） |
| $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） | $T_0\ge0$ pretension (N m⁻¹)<br>$T_0\ge0$为预张力（N m⁻¹） |
| $p_{\rm load}$ is net applied transverse traction projected positively (Pa)<br>$p_{\rm load}$为沿正方向投影的净外加横向牵引（Pa） | $t_{\rm coh}\ge0$ is an opening-resisting cohesive traction magnitude (Pa)<br>$t_{\rm coh}\ge0$为抵抗张开的内聚牵引幅值（Pa） |

**Conventions and conditions.** $\nabla_\parallel^2$ is in-plane Laplacian (m⁻²), and $\nabla_\parallel^4$ its square; $\partial_n$ differentiates along the outward in-plane boundary normal; Initial zero is displacement or velocity according to its row; Labels load and coh identify applied and cohesive forces.

**约定与条件。** $\nabla_\parallel^2$为面内拉普拉斯算子（m⁻²），$\nabla_\parallel^4$为其平方；$\partial_n$表示沿面内边界外法向求导；初始零值按对应行分别表示位移或速度；标签load和coh表示外载与内聚力。

(C4-E06) · Reduced transient momentum balance with explicit initial/boundary data / 含明确初始与边界数据的简化瞬态动量平衡


$$
\begin{aligned}m_A\ddot w+D_f\nabla_\parallel^4w-T_0\nabla_\parallel^2w&=p_{\rm load}-t_{\rm coh},\\w(\boldsymbol x,0)=0,\quad\dot w(\boldsymbol x,0)&=0,\\w=0,\quad\partial_n w&=0\quad\text{on a clamped edge}.\end{aligned}
$$


![Film acceleration balances applied traction, elastic restoring forces and cohesive resistance.](../assets/figures/c4-e06.svg)

Film acceleration balances applied traction, elastic restoring forces and cohesive resistance.

薄膜加速度由外加牵引、弹性恢复力与内聚阻力的平衡决定。

The fixed clamp also has zero velocity and normal velocity slope. Multiply the plate equation by velocity and integrate. Inertia differentiates kinetic energy. Two bending integrations by parts differentiate bending energy. One tension integration differentiates pretension energy. Cohesive power removes energy from plate motion. The interface law partitions recoverable and irreversible parts.

固定夹持处速度及法向速度斜率也为零。将板方程乘速度并积分。惯性项给出动能导数。弯曲项两次分部积分给出弯曲能导数，张力项一次积分给出预张力能导数。内聚功率从板运动取走能量。界面规律区分可恢复与不可逆部分。

**Symbols before Eq. (C4-E41).**

**式（C4-E41）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Omega_f$ is reference film area (m²)<br>$\Omega_f$为薄膜参考面积（m²） | $dA$ its area element (m²)<br>$dA$为面积微元（m²） |
| $w$ displacement (m)<br>$w$为位移（m） | $\dot w$ — Film transverse velocity (m s⁻¹)<br>$\dot w$ — 薄膜横向速度（m s⁻¹） |
| $\ddot w$ — Film transverse acceleration (m s⁻²)<br>$\ddot w$ — 薄膜横向加速度（m s⁻²） | $m_A$ is areal mass (kg m⁻²)<br>$m_A$为面密度（kg m⁻²） |
| $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） | $T_0$ constant pretension (N m⁻¹)<br>$T_0$为恒定预张力（N m⁻¹） |
| $p_{\rm load}$ applied transverse traction (Pa)<br>$p_{\rm load}$为外加横向牵引（Pa） | $t_{\rm coh}$ resisting cohesive traction (Pa)<br>$t_{\rm coh}$为抵抗内聚牵引（Pa） |
| $K_f$ — Film kinetic energy (J)<br>$K_f$ — 薄膜动能（J） | $U_b$ — Plate bending energy, not bubble internal energy in this unit (J)<br>$U_b$ — 板弯曲能，本单元不表示气泡内能（J） |
| $U_T$ — Stored pretension energy (J)<br>$U_T$ — 预张力储能（J） | $t$ is time (s)<br>$t$为时间（s） |

**Conventions and conditions.** $d/dt$ is its derivative; $\nabla_\parallel^2$ is planar Laplacian and $\nabla_\parallel^4$ its square; $\int$ is area integration; The derivatives are valid for the stated constant parameters and sufficiently regular fields at a fixed clamp with zero velocity and normal velocity slope; Every row has power units W; f, b, T, load and coh label film, bending, tension, applied and cohesive.

**约定与条件。** $d/dt$为时间导数；$\nabla_\parallel^2$为平面拉普拉斯算子，$\nabla_\parallel^4$为其平方；$\int$表示面积积分；导数适用于所述恒定参数、足够正则的场，以及速度和法向速度斜率均为零的固定夹持边界；各行单位均为功率W；f、b、T、load、coh分别表示薄膜、弯曲、张力、外加及内聚。

(C4-E41) · Transient plate power identity under fixed clamps / 固定夹持条件下瞬态板的功率恒等式


$$
\begin{aligned}\int_{\Omega_f}m_A\ddot w\dot w\,dA&=\frac{dK_f}{dt},\qquad \int_{\Omega_f}D_f\nabla_\parallel^4w\dot w\,dA=\frac{dU_b}{dt},\\-\int_{\Omega_f}T_0\nabla_\parallel^2w\dot w\,dA&=\frac{dU_T}{dt},\\\frac{d}{dt}(K_f+U_b+U_T)&=\int_{\Omega_f}p_{\rm load}\dot w\,dA-\int_{\Omega_f}t_{\rm coh}\dot w\,dA.\end{aligned}
$$


![The transient plate equation conserves power between applied work, motion, shape and interface response.](../assets/figures/c4-e41.svg)

The transient plate equation conserves power between applied work, motion, shape and interface response.

瞬态薄板方程在外加功、运动、形状与界面响应之间保持功率守恒。

This is an exact balance within the reduced plate assumptions. Bending units are N m × m⁻³ = Pa. Tension units are N m⁻¹ × m⁻¹ = Pa. Zero mass gives quasistatic balance. Zero stiffness, tension and cohesion gives free areal acceleration. Large slope, stretching, plasticity, anisotropy, finite thickness or contact needs refinement. The cited static benchmark agrees with the stiffness formulation. This derivation retains inertia. [MIT plate benchmark](https://ocw.mit.edu/courses/2-080j-structural-mechanics-fall-2013/resources/mit2_080jf13_lecture7/)

这是约化板假设内的精确平衡。弯曲单位为 N m × m⁻³ = Pa，张力单位为 N m⁻¹ × m⁻¹ = Pa。质量取零得到准静态平衡，刚度、张力及内聚力取零得到自由面加速度。大斜率、拉伸、塑性、各向异性、有限厚度或接触需细化。所引静态基准与刚度形式一致，本推导保留惯性。[MIT 板基准](https://ocw.mit.edu/courses/2-080j-structural-mechanics-fall-2013/resources/mit2_080jf13_lecture7/)

Step 6 — Include PVC mechanics. Give each sheet its own areal mass, stiffness and support. Transmitted traction acts oppositely on the sheets by Newton’s third law. Determine it through contact or bond closure. A fully bonded laminate additionally requires in-plane compatibility and composite stiffness.

步骤 6——计入 PVC 力学。各片层具有独立面质量、刚度和支撑。根据牛顿第三定律，传递牵引在两片层上方向相反。须通过接触或粘接规律确定牵引。完全粘接叠层还需要面内相容性及复合刚度。

**Symbols before Eq. (C4-E07).**

**式（C4-E07）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $w_P$ — PVC displacement along the common positive direction (m)<br>$w_P$ — 沿共同正方向的 PVC 位移（m） | $w$ — Film displacement along the same positive direction as PVC displacement (m)<br>$w$ — 与 PVC 位移采用相同正方向的薄膜位移（m） |
| $m_{A,P}$ — PVC areal mass (kg m⁻²)<br>$m_{A,P}$ — PVC 面密度（kg m⁻²） | $m_A$ — Film areal mass (kg m⁻²)<br>$m_A$ — 薄膜面密度（kg m⁻²） |
| $D_P$ — PVC bending stiffness (N m)<br>$D_P$ — PVC 弯曲刚度（N m） | $D_f$ — Film bending rigidity (N m)<br>$D_f$ — 薄膜弯曲刚度（N m） |
| $T_P$ — Prescribed PVC pretension (N m⁻¹)<br>$T_P$ — 给定 PVC 预张力（N m⁻¹） | $T_0$ — Prescribed isotropic tensile force per edge length (N m⁻¹)<br>$T_0$ — 给定的单位边长各向同性拉力（N m⁻¹） |
| $p_{\rm liq}$ is net liquid traction on PVC (Pa)<br>$p_{\rm liq}$为液体作用于PVC的净牵引（Pa） | $t_{P\to f}$ transmitted PVC-to-film traction projected positively (Pa)<br>$t_{P\to f}$为沿正方向投影的PVC传向薄膜牵引（Pa） |
| $t_{\rm coh}$ film-release resistance (Pa)<br>$t_{\rm coh}$为薄膜释放阻力（Pa） |  |

**Conventions and conditions.** double dots are accelerations (m s⁻²); $\nabla_\parallel^2$ is the in-plane Laplacian and $\nabla_\parallel^4$ its square; P labels PVC, f film, A areal, liq liquid and coh cohesion; the arrow labels the transmission direction; Each sheet has its actual initial and support conditions; No value of transmitted traction is supplied without an additional contact/bond closure.

**约定与条件。** 双上点为加速度（m s⁻²）；$\nabla_\parallel^2$为面内拉普拉斯算子，$\nabla_\parallel^4$为其平方；P表示PVC，f表示薄膜，A表示面量，liq表示液体，coh表示内聚；箭头标识传递方向；每层均具有自身实际初始及支承条件；若无附加接触／粘接闭合关系，传递牵引就尚未确定。

(C4-E07) · Conditional coupled-sheet model / 有条件的耦合薄片模型


$$
\begin{aligned}m_{A,P}\ddot w_P+D_P\nabla_\parallel^4w_P-T_P\nabla_\parallel^2w_P&=p_{\rm liq}-t_{P\to f},\\m_A\ddot w+D_f\nabla_\parallel^4w-T_0\nabla_\parallel^2w&=t_{P\to f}-t_{\rm coh}.\end{aligned}
$$


![The PVC-to-film load follows intermediate-sheet motion and contact.](../assets/figures/c4-e07.svg)

The PVC-to-film load follows intermediate-sheet motion and contact.

PVC传向薄膜的载荷由中间片层运动与接触决定。

Step 7 — Integrate the film equation over the pulse. Retain restoring and cohesive impulses. A free velocity jump requires both small relative to applied impulse. A film bonded to rigid donor across the footprint fails that condition. Count resolved fluid inertia once.

步骤 7——在脉冲期间积分薄膜方程，保留恢复力与内聚力冲量。自由速度跃变要求两者相对外加冲量较小。整个作用区粘接于刚性供体的薄膜不满足该条件。解析流体惯性计入一次。

**Symbols before Eq. (C4-E08).**

**式（C4-E08）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_A$ is film areal mass (kg m⁻²)<br>$m_A$为薄膜面密度（kg m⁻²） | $w(\boldsymbol x,t)$ vertical displacement (m)<br>$w(\boldsymbol x,t)$为竖直位移（m） |
| $\boldsymbol x$ in-plane position (m)<br>$\boldsymbol x$为面内位置（m） | $\dot w$ velocity (m s⁻¹)<br>$\dot w$为速度（m s⁻¹） |
| $t_a$ — Load-event start time (s)<br>$t_a$ — 载荷事件开始时刻（s） | $t_b$ — Load-event end time (s)<br>$t_b$ — 载荷事件结束时刻（s） |
| $t$ — Time (s)<br>$t$ — 时间（s） | $dt$ — Time integration element (s)<br>$dt$ — 时间积分微元（s） |
| $J_A$ is local applied impulse per area (Pa s)<br>$J_A$为局部单位面积外加冲量（Pa s） | $p_{\rm load}$ net applied traction (Pa)<br>$p_{\rm load}$为净外加牵引（Pa） |
| $t_{\rm coh}$ cohesive resistance (Pa)<br>$t_{\rm coh}$为内聚阻力（Pa） | $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） |
| $T_0$ pretension (N m⁻¹)<br>$T_0$为预张力（N m⁻¹） |  |

**Conventions and conditions.** $\nabla_\parallel^2$ and $\nabla_\parallel^4$ are the in-plane Laplacian and its square; $\int$ integrates the actual local load/response during the pulse; Labels A, f, load and coh mean areal, film, applied and cohesive.

**约定与条件。** $\nabla_\parallel^2$与$\nabla_\parallel^4$为面内拉普拉斯算子及其平方；$\int$表示对脉冲期间实际局部载荷／响应积分；标签A、f、load、coh分别表示面量、薄膜、外加及内聚。

(C4-E08) · Exact time integral within the reduced plate model / 简化板模型内的精确时间积分


$$
m_A[\dot w(\boldsymbol x,t_b)-\dot w(\boldsymbol x,t_a)]=J_A-\int_{t_a}^{t_b}[D_f\nabla_\parallel^4w-T_0\nabla_\parallel^2w+t_{\rm coh}]\,dt,\qquad J_A=\int_{t_a}^{t_b}p_{\rm load}\,dt
$$


![Pulse integration exposes the reactions that can invalidate a free velocity jump.](../assets/figures/c4-e08.svg)

Pulse integration exposes the reactions that can invalidate a free velocity jump.

脉冲积分明确显示哪些反作用冲量会使自由速度跃变失效。

**Symbols before Eq. (C4-E09).**

**式（C4-E09）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Delta\dot w$ is the film velocity change from rest (m s⁻¹)<br>$\Delta\dot w$为薄膜从静止开始的速度变化（m s⁻¹） | $J_A$ is local applied impulse per area (Pa s)<br>$J_A$为局部单位面积外加冲量（Pa s） |
| $m_A>0$ film areal mass (kg m⁻²)<br>$m_A>0$为薄膜面密度（kg m⁻²） | $\mathcal E_A$ resulting kinetic energy per area (J m⁻²)<br>$\mathcal E_A$为所得单位面积动能（J m⁻²） |

**Conventions and conditions.** $\simeq$ marks negligible restoring/cohesive impulse during the pulse, not guaranteed transmission through an adhered stack; Subscript A labels quantities per area; $\Delta$ denotes final-minus-initial difference, and a dot is a time derivative.

**约定与条件。** $\simeq$表示脉冲期间恢复力／内聚力冲量可忽略，而非保证粘接叠层中的载荷传递；下标A表示单位面积量；$\Delta$表示终值减初值，上点为时间导数。

(C4-E09) · Short-pulse free-response approximation / 短脉冲后的自由响应近似


$$
\Delta\dot w\simeq\frac{J_A}{m_A},\qquad \mathcal E_A\simeq\frac12m_A(\Delta\dot w)^2=\frac{J_A^2}{2m_A}
$$


![Impulse creates film kinetic energy that may subsequently feed deformation and fracture.](../assets/figures/c4-e09.svg)

Impulse creates film kinetic energy that may subsequently feed deformation and fracture.

冲量产生薄膜动能，之后才可能转入变形与断裂。

Balance inertia with bending and tension over the deformation length. Compare the resulting response times with pulse duration. Small-opening cohesive stiffness gives a third time. Slow duration alone leaves equilibrium unresolved when pulse edges or crack growth are rapid.

在变形长度上分别平衡惯性与弯曲、张力。比较所得响应时间与脉冲时长。小张开内聚刚度给出第三种时间。脉冲边缘或裂纹增长快速时，单凭长时长仍未确立平衡。

**Symbols before Eq. (C4-E10).**

**式（C4-E10）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $t_b^{\rm scale}$ — Bending response-time estimate (s)<br>$t_b^{\rm scale}$ — 弯曲响应时间估计（s） | $t_T^{\rm scale}$ — Pretension response-time estimate (s)<br>$t_T^{\rm scale}$ — 预张力响应时间估计（s） |
| $t_n^{\rm scale}$ — Normal-cohesion response-time estimate (s)<br>$t_n^{\rm scale}$ — 法向内聚响应时间估计（s） | $a_f>0$ is lateral deformation length (m)<br>$a_f>0$为横向变形长度（m） |
| $m_A>0$ areal mass (kg m⁻²)<br>$m_A>0$为面密度（kg m⁻²） | $D_f>0$ bending stiffness (N m)<br>$D_f>0$为弯曲刚度（N m） |
| $T_0>0$ pretension (N m⁻¹)<br>$T_0>0$为预张力（N m⁻¹） | $K_n>0$ small-opening normal cohesive stiffness (Pa m⁻¹)<br>$K_n>0$为小张开法向内聚刚度（Pa m⁻¹） |

**Conventions and conditions.** superscript scale labels estimates and subscripts b, T, n identify the restoring mechanisms; $\sqrt{\ }$ is the positive root; If pretension or cohesion is absent, its corresponding timescale is omitted rather than divided by zero.

**约定与条件。** 上标scale表示估计，下标b、T、n标识恢复机制；$\sqrt{\ }$取正根；若预张力或内聚机制不存在，则不使用对应时间尺度，不能除以零。

(C4-E10) · Derived term-balance estimates / 通过各项平衡推导的估算


$$
t_b^{\rm scale}=a_f^2\sqrt{\frac{m_A}{D_f}},\qquad t_T^{\rm scale}=a_f\sqrt{\frac{m_A}{T_0}},\qquad t_n^{\rm scale}=\sqrt{\frac{m_A}{K_n}}
$$


![Pulse duration must be compared with the response scales of the actual load path.](../assets/figures/c4-e10.svg)

Pulse duration must be compared with the response scales of the actual load path.

脉冲持续时间须与实际传力路径的响应尺度比较。

## 4. Interface strength and fracture work

## 4. 界面强度与断裂功

Step 8 — Specify loading control before crack driving force. Peak tensile traction is local strength in Pa. Reversible adhesion work is a surface-energy difference. Practical fracture energy includes dissipation and has units J m⁻². For quasistatic conservative mechanics, differentiate potential by crack area at fixed source control. Mode mixture, temperature and crack speed can change resistance.

步骤 8——计算裂纹驱动力前规定加载控制。峰值拉伸牵引是 Pa 单位局部强度。可逆粘附功是表面能差。实际断裂能包含耗散，单位为 J m⁻²。准静态保守力学中，在固定源控制下对裂纹面积求势能导数。模态混合、温度及裂纹速度可改变阻力。

**Symbols before Eq. (C4-E11).**

**式（C4-E11）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $G$ is quasistatic energy-release rate (J m⁻²)<br>$G$为准静态能量释放率（J m⁻²） | $\mathcal P$ total mechanical potential including the external loading system (J)<br>$\mathcal P$为包含外部加载系统的总力学势能（J） |
| $A_c$ crack area (m²), and $\partial/\partial A_c$ a partial derivative<br>$A_c$为裂纹面积（m²），$\partial/\partial A_c$为偏导数 | $\mathcal C$ labels the held loading control, such as pressure or displacement (—)<br>$\mathcal C$标识保持不变的加载控制量，例如压力或位移，而非材料系数（—） |
| $\Gamma$ is fracture resistance (J m⁻²)<br>$\Gamma$为断裂阻力（J m⁻²） | $\psi$ mode-mixture parameter (dimensionless)<br>$\psi$为模态混合参数（无量纲） |
| $T_i$ interface temperature (K)<br>$T_i$为界面温度（K） | $v_c$ crack-front speed (m s⁻¹)<br>$v_c$为裂纹前沿速度（m s⁻¹） |

**Conventions and conditions.** it is not a material coefficient; Subscripts c and i label crack and interface; The inequality is an energetic propagation criterion for the specified fracture model, not a sufficient transfer criterion.

**约定与条件。** 下标c与i表示裂纹及界面；此不等式是指定断裂模型的能量扩展判据，而非充分转印判据。

(C4-E11) · Definition with quasistatic fracture criterion / 定义与准静态断裂判据


$$
G=-\left.\frac{\partial\mathcal P}{\partial A_c}\right|_{\mathcal C},\qquad G\ge\Gamma(\psi,T_i,v_c)
$$


![A crack is driven by energy per newly separated area, under a specified load control.](../assets/figures/c4-e11.svg)

A crack is driven by energy per newly separated area, under a specified load control.

裂纹由每单位新分离面积的可用能量驱动，且加载控制必须明确。

Comparing pressure with fracture energy requires a deformation length and mechanical law. Competing paths include intended release, another bond’s failure and payload tearing. Feng et al. show how interface kinetics alter path competition. Measure rate and temperature dependence for the actual PFC stack. Their PDMS values require separate justification before reuse. [[R10]](../reference/sources.html#r10)

压力与断裂能比较需要变形长度及力学规律。竞争路径包括目标释放、其他粘接失效及载荷撕裂。Feng 等说明界面动力学如何改变路径竞争。实际 PFC 叠层须测量速率及温度依赖性。复用其 PDMS 数值需要独立依据。 [[R10]](../reference/sources.html#r10)

Retain kinetic energy during rapid fracture. The chosen crack-front balance includes elastic storage, inertia, fracture consumption and other loss. Count cohesive dissipation once through the selected fracture energy. Crack path still requires structural and interface equations.

快速断裂时保留动能。所选裂纹前沿平衡包括弹性储存、惯性、断裂消耗及其他损失。所选断裂能中的内聚耗散计入一次。裂纹路径仍需结构与界面方程。

**Symbols before Eq. (C4-E12).**

**式（C4-E12）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $P_{\rm load}$ is mechanical power delivered to the solid (W)<br>$P_{\rm load}$为传入固体的力学功率（W） | $K_f$ its kinetic energy (J)<br>$K_f$为固体动能（J） |
| $U_f$ its recoverable elastic energy including any recoverable interface energy (J), and $d/dt$ the time derivative with $t$ in s<br>$U_f$为可恢复弹性能，含任何可恢复界面能（J），$d/dt$为时间导数 | $\mathcal L_c$ is the active crack-front line (—)<br>$\mathcal L_c$为活跃裂纹前沿曲线（—） |
| $d\ell$ is its arc-length element (m)<br>$d\ell$为弧长微元（m） | $v_c\ge0$ is front speed (m s⁻¹)<br>$v_c\ge0$为前沿速度（m s⁻¹） |
| $\Gamma$ fracture energy (J m⁻²)<br>$\Gamma$为断裂能（J m⁻²） | $\psi$ dimensionless mode mixture<br>$\psi$为无量纲模态混合参数 |
| $T_i$ interface temperature (K)<br>$T_i$为界面温度（K） | $P_{\rm other}\ge0$ is additional nonfracture dissipation (W)<br>$P_{\rm other}\ge0$为其他非断裂耗散（W） |
| $t$ — Time (s)<br>$t$ — 时间（s） |  |

**Conventions and conditions.** $\int$ integrates along the front; Labels load, f, c, i and other denote applied, solid film, crack, interface and remaining dissipative processes.

**约定与条件。** $\int$表示沿前沿积分；标签load、f、c、i、other分别表示外加、固体薄膜、裂纹、界面及其余耗散过程。

(C4-E12) · Conditional dynamic energy balance / 有条件的动态能量平衡


$$
P_{\rm load}=\frac{d}{dt}(K_f+U_f)+\int_{\mathcal L_c}\Gamma(\psi,T_i,v_c)v_c\,d\ell+P_{\rm other}
$$


![Dynamic loading can store kinetic energy before or during crack advance.](../assets/figures/c4-e12.svg)

Dynamic loading can store kinetic energy before or during crack advance.

动态载荷可在裂纹扩展前或扩展中储存动能。

## 5. Circular blister benchmark

## 5. 圆形鼓泡基准

Step 9 — Define pressure-controlled delamination. A pre-existing circular crack lies beneath a thin isotropic plate. The bonded region clamps its edge. A reservoir maintains uniform positive pressure as radius varies. Omit inertia, pretension and stretching. Center displacement and curvature are regular without point force or singular moment. This benchmark has different loading from the transient jet array.

步骤 9——定义压力控制脱层。薄各向同性板下已有圆形裂纹，粘接外区夹持其边缘。半径变化时，储库维持均匀正压差。忽略惯性、预张力及拉伸。中心无点力或奇异弯矩，位移和曲率正则。该基准加载不同于瞬态射流阵列。

**Symbols before Eq. (C4-E13).**

**式（C4-E13）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $r\in[0,b]$ is radius in the plate plane (m)<br>$r\in[0,b]$为板平面内半径（m） | $b>0$ delamination radius (m)<br>$b>0$为脱层半径（m） |
| $w(r)$ opening displacement (m)<br>$w(r)$为张开位移（m） | $p_0>0$ externally maintained pressure difference (Pa)<br>$p_0>0$为外部保持的压差（Pa） |
| $D_f>0$ bending stiffness (N m)<br>$D_f>0$为弯曲刚度（N m） | $\mathscr L_r$ is the axisymmetric planar Laplacian (m⁻²)<br>$\mathscr L_r$为轴对称平面拉普拉斯算子（m⁻²） |
| $f$ is an arbitrary smooth radial function (—)<br>$f$为任意光滑径向函数（—） | $g=\mathscr L_rw$ has units m⁻¹<br>$g=\mathscr L_rw$的单位为m⁻¹ |

**Conventions and conditions.** $d/dr$ and a prime denote radial differentiation; the operator at $r=0$ is its regular limit; Labels r, f and 0 denote radial operator, film/arbitrary function according to context, and maintained load; The two zero values prescribe edge displacement and slope.

**约定与条件。** $d/dr$及撇号表示径向求导；$r=0$处算子取正则极限；标签r、f、0分别表示径向算子、薄膜／任意函数（依语境）及恒定载荷；两个零值指定边缘位移与斜率。

(C4-E13) · Quasistatic plate boundary-value model / 准静态板的边值模型


$$
\mathscr L_rg=\frac{p_0}{D_f},\qquad g=\mathscr L_rw,\qquad \mathscr L_r f=\frac1r\frac{d}{dr}\left(r\frac{df}{dr}\right),\qquad w(b)=0,\quad w^{\prime}(b)=0
$$


![Uniform pressure loads a clamped circular delamination with regular central fields.](../assets/figures/c4-e13.svg)

Uniform pressure loads a clamped circular delamination with regular central fields.

均匀压力作用于边缘夹持的圆形脱层，中心场必须正则。

Step 10 — Solve the curvature sum. Multiply its radial Laplacian equation by radius and integrate. Divide by radius away from the center. Regular curvature gradient excludes the inverse-radius term. Integrate again for the constant curvature offset. The edge slope will determine it.

步骤 10——求曲率和。将径向拉普拉斯方程乘半径并积分。中心之外除以半径。曲率梯度正则性排除半径反比项。再次积分得到常曲率偏置，随后由边缘斜率确定。

**Symbols before Eq. (C4-E14).**

**式（C4-E14）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $r\in(0,b]$ is radial coordinate (m)<br>$r\in(0,b]$为径向坐标（m） | $b$ is delamination radius (m)<br>$b$为脱层半径（m） |
| $g(r)=\mathscr L_rw$ is the curvature sum (m⁻¹), with a prime and $d/dr$ denoting radial differentiation<br>$g(r)=\mathscr L_rw$为曲率和（m⁻¹），撇号及$d/dr$表示径向求导 | $p_0$ is maintained pressure difference (Pa)<br>$p_0$为恒定压差（Pa） |
| $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） | $C_1$ — Curvature integration constant (m⁻¹)<br>$C_1$ — 曲率积分常数（m⁻¹） |
| $C_2$ — Curvature integration constant (m⁻¹)<br>$C_2$ — 曲率积分常数（m⁻¹） | $\mathscr L_r$ is the radial Laplacian (m⁻²)<br>$\mathscr L_r$为径向拉普拉斯算子（m⁻²） |
| $w$ displacement (m)<br>$w$为位移（m） |  |

**Conventions and conditions.** $C_1=0$ follows from regular central curvature gradient and absence of a point load; the subscript 0 labels the maintained pressure, not the initial liquid pressure.

**约定与条件。** $C_1=0$来自中心曲率梯度正则及无点载荷条件；下标0标识恒定压力，而非液体初始压力。

(C4-E14) · Derived first two radial integrations / 推导中的前两次径向积分


$$
\begin{aligned}\frac{d}{dr}(rg^{\prime})&=\frac{p_0r}{D_f},\\rg^{\prime}&=\frac{p_0r^2}{2D_f}+C_1,\\g^{\prime}&=\frac{p_0r}{2D_f}+\frac{C_1}{r},\quad C_1=0,\\g(r)&=\frac{p_0r^2}{4D_f}+C_2.\end{aligned}
$$


![Regularity removes the singular integration constant before edge conditions are used.](../assets/figures/c4-e14.svg)

Regularity removes the singular integration constant before edge conditions are used.

在使用边缘条件之前，正则性先排除奇异积分常数。

Step 11 — Integrate curvature to displacement. Center regularity removes the inverse-radius slope. Integration leaves quartic, quadratic and constant terms. Zero edge slope fixes curvature offset. Zero edge displacement fixes the remaining constant.

步骤 11——由曲率积分至位移。中心正则性消去半径反比斜率。积分留下四次、二次及常数项。边缘零斜率确定曲率偏置，边缘零位移确定剩余常数。

**Symbols before Eq. (C4-E15).**

**式（C4-E15）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $r\in(0,b]$ is radial position (m)<br>$r\in(0,b]$为径向位置（m） | $b$ delamination radius (m)<br>$b$为脱层半径（m） |
| $w$ displacement (m)<br>$w$为位移（m） | $g$ curvature sum (m⁻¹)<br>$g$为曲率和（m⁻¹） |
| $w^{\prime}$ is dimensionless slope<br>$w^{\prime}$为无量纲斜率 | $p_0$ is maintained pressure (Pa)<br>$p_0$为恒定压力（Pa） |
| $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） | $C_2$ curvature integration constant (m⁻¹)<br>$C_2$为曲率积分常数（m⁻¹） |
| $C_3$ — Displacement integration constant (m)<br>$C_3$ — 位移积分常数（m） | $C_4$ — Displacement integration constant (m)<br>$C_4$ — 位移积分常数（m） |

**Conventions and conditions.** A prime and $d/dr$ are radial derivatives; $C_3=0$ excludes a central inverse-radius slope; All rows are regular-limit solutions at the centre; Subscripts 2,3,4 index distinct constants, not derivative orders.

**约定与条件。** 撇号及$d/dr$为径向导数；$C_3=0$排除中心反比于半径的斜率；各行在中心均取正则极限；下标2、3、4标识不同常数，而非导数阶数。

(C4-E15) · Derived second pair of radial integrations / 推导中的后两次径向积分


$$
\begin{aligned}\frac{d}{dr}(rw^{\prime})&=rg=\frac{p_0r^3}{4D_f}+C_2r,\\rw^{\prime}&=\frac{p_0r^4}{16D_f}+\frac{C_2r^2}{2}+C_3,\quad C_3=0,\\w^{\prime}&=\frac{p_0r^3}{16D_f}+\frac{C_2r}{2},\\w(r)&=\frac{p_0r^4}{64D_f}+\frac{C_2r^2}{4}+C_4.\end{aligned}
$$


![The regular displacement contains quartic, quadratic and constant contributions.](../assets/figures/c4-e15.svg)

The regular displacement contains quartic, quadratic and constant contributions.

正则位移含四次项、二次项与常数项。

**Symbols before Eq. (C4-E16).**

**式（C4-E16）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $w(r)$ is displacement (m)<br>$w(r)$为位移（m） | $w^{\prime}$ radial slope (dimensionless)<br>$w^{\prime}$为径向斜率（无量纲） |
| $r\in[0,b]$ radial position (m)<br>$r\in[0,b]$为径向位置（m） | $b>0$ delamination radius (m), allowing division by $b$<br>$b>0$为脱层半径（m），因此可以除以$b$ |
| $p_0>0$ is maintained pressure (Pa)<br>$p_0>0$为恒定压力（Pa） | $D_f>0$ bending stiffness (N m)<br>$D_f>0$为弯曲刚度（N m） |
| $C_2$ curvature constant (m⁻¹)<br>$C_2$为曲率常数（m⁻¹） | $C_4$ displacement constant (m)<br>$C_4$为位移常数（m） |

**Conventions and conditions.** The prime denotes $d/dr$; $\Rightarrow$ denotes the algebraic consequence of each clamped boundary condition; Subscripts 2 and 4 label constants, and f labels film.

**约定与条件。** 撇号表示$d/dr$；$\Rightarrow$表示各夹持边界条件的代数结果；下标2与4标识常数，f表示薄膜。

(C4-E16) · Exact solution of the stated linear-plate benchmark / 所述线性板基准问题的精确解


$$
\begin{aligned}0=w^{\prime}(b)&=\frac{p_0b^3}{16D_f}+\frac{C_2b}{2}\quad\Rightarrow\quad C_2=-\frac{p_0b^2}{8D_f},\\0=w(b)&=\frac{p_0b^4}{64D_f}-\frac{p_0b^4}{32D_f}+C_4\quad\Rightarrow\quad C_4=\frac{p_0b^4}{64D_f},\\w(r)&=\frac{p_0}{64D_f}(r^4-2b^2r^2+b^4)=\frac{p_0}{64D_f}(b^2-r^2)^2.\end{aligned}
$$


![Applying both edge conditions fixes the unique regular blister profile.](../assets/figures/c4-e16.svg)

Applying both edge conditions fixes the unique regular blister profile.

同时应用两个边缘条件，确定唯一正则鼓泡轮廓。

Step 12 — Substitute the solution to check it. Radial Laplacian of radius² is four. That of radius⁴ is sixteen × radius². Applying twice gives sixty-four. Edge displacement and slope vanish. Positive pressure opens the center; larger stiffness reduces opening. Units are Pa × m⁴/(N m) = m. MIT Lecture 7, Eq. 7.24 gives the same clamped-circle solution.

步骤 12——代回解进行检验。半径²的径向拉普拉斯为四，半径⁴的结果为十六 × 半径²，作用两次得六十四。边缘位移和斜率为零。正压使中心张开，刚度增大使张开减小。单位为 Pa × m⁴／（N m）= m。MIT 第 7 讲式 7.24 给出相同夹持圆板解。

**Symbols before Eq. (C4-E17).**

**式（C4-E17）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\mathscr L_r$ is the radial planar Laplacian (m⁻²), and superscript 2 on the operator means composition twice<br>$\mathscr L_r$为径向平面拉普拉斯算子（m⁻²），算子上的上标2表示连续作用两次 | $r$ is radial position (m)<br>$r$为径向位置（m） |
| $b$ delamination radius (m)<br>$b$为脱层半径（m） | $w$ blister displacement (m), and its prime is radial slope<br>$w$为鼓泡位移（m），其撇号为径向斜率 |
| $D_f$ is bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） | $p_0$ maintained pressure (Pa)<br>$p_0$为恒定压力（Pa） |
| $\mathscr L_r(r^2)$ is dimensionless<br>$\mathscr L_r(r^2)$无量纲 | $\mathscr L_r(r^4)$ has units m²<br>$\mathscr L_r(r^4)$单位为m² |

**Conventions and conditions.** superscripts on $r$ are powers; Literal 4 and 16 are numerical coefficients; The slope expression vanishes at $r=0$; $r=b$.

**约定与条件。** $r$上的上标表示幂；数字4与16是数值系数；斜率式在$r=0$及$r=b$均为零。

(C4-E17) · Governing-equation and boundary verification / 控制方程与边界条件核验


$$
\mathscr L_r(r^2)=4,\qquad \mathscr L_r(r^4)=16r^2,\qquad D_f\mathscr L_r^2w=p_0,\qquad w^{\prime}(r)=\frac{p_0r(r^2-b^2)}{16D_f}
$$


![Direct radial differentiation verifies the pressure balance and regular clamped profile.](../assets/figures/c4-e17.svg)

Direct radial differentiation verifies the pressure balance and regular clamped profile.

直接径向求导可检验压力平衡及正则夹持轮廓。

Step 13 — Integrate opening for cavity volume. The axisymmetric area element includes radius × radial increment. Expand the profile square and integrate each power. Evaluate both limits. The first two endpoint terms cancel, leaving the sixth-power term.

步骤 13——积分张开位移求空腔体积。轴对称面积微元包含半径 × 径向增量。展开轮廓平方并积分各幂。计算上下限，前两端点项相消，留下六次幂项。

**Symbols before Eq. (C4-E18).**

**式（C4-E18）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $V_{\rm bl}$ is added blister volume (m³)<br>$V_{\rm bl}$为新增鼓泡体积（m³） | $w(r)$ displacement (m)<br>$w(r)$为位移（m） |
| $r\in[0,b]$ radial integration coordinate (m)<br>$r\in[0,b]$为径向积分坐标（m） | $dr$ its integration element (m)<br>$dr$为积分微元（m） |
| $b$ delamination radius (m)<br>$b$为脱层半径（m） | $p_0$ is maintained pressure (Pa)<br>$p_0$为恒定压力（Pa） |
| $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） | $\pi$ the dimensionless circle constant<br>$\pi$为无量纲圆周率 |

**Conventions and conditions.** $\int$ is radial integration; Subscript bl labels the blister; superscripts on lengths are powers; $[\ ]_0^b$ denotes antiderivative at the upper endpoint minus its value at zero.

**约定与条件。** $\int$表示径向积分；下标bl表示鼓泡；长度上的上标均表示幂；$[\ ]_0^b$表示原函数在上端点的值减去其零端点值。

(C4-E18) · Exact geometric volume integral for the benchmark / 基准模型的精确几何体积积分


$$
\begin{aligned}V_{\rm bl}&=2\pi\int_0^b w(r)r\,dr=\frac{\pi p_0}{32D_f}\int_0^b(b^4r-2b^2r^3+r^5)\,dr,\\&=\frac{\pi p_0}{32D_f}\left[\frac{b^4r^2}{2}-\frac{b^2r^4}{2}+\frac{r^6}{6}\right]_0^b=\frac{\pi p_0b^6}{192D_f}.\end{aligned}
$$


![Blister volume sums the opening of all concentric annuli.](../assets/figures/c4-e18.svg)

Blister volume sums the opening of all concentric annuli.

鼓泡体积等于各同心圆环张开贡献之和。

Step 14 — Include reservoir work in potential. At fixed crack radius, volume is linear in pressure. Elastic storage is half pressure × volume. Reservoir potential is minus pressure × volume. Their sum is minus the half-product. Omitting reservoir work reverses the pressure-controlled driving-force sign.

步骤 14——在势能中计入储库功。裂纹半径固定时，体积随压力线性变化。弹性储存为压力 × 体积的一半，储库势能为压力 × 体积的负值。总和为负半积。省略储库功会反转压力控制驱动力符号。

**Symbols before Eq. (C4-E19).**

**式（C4-E19）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $C_b>0$ is blister volume compliance (m³ Pa⁻¹), defined by the pressure derivative at fixed radius, including the regular zero-load value<br>$C_b>0$为鼓泡体积柔度（m³ Pa⁻¹），由固定半径下的压力导数定义，包含正则零载荷值 | $V_{\rm bl}\ge0$ is added volume (m³)<br>$V_{\rm bl}\ge0$为新增体积（m³） |
| $p_0\ge0$ maintained pressure (Pa)<br>$p_0\ge0$为恒定压力（Pa） | $b>0$ crack radius (m)<br>$b>0$为裂纹半径（m） |
| $D_f>0$ bending stiffness (N m)<br>$D_f>0$为弯曲刚度（N m） | $U_b$ is stored plate bending energy (J)<br>$U_b$为板弯曲储能（J） |
| $\mathcal P$ plate-plus-pressure-reservoir potential (J)<br>$\mathcal P$为板与恒压储库的总势能（J） | $v$ a dummy volume along the fixed-radius elastic loading curve (m³), with $dv$ its element (m³)<br>$v$为固定半径弹性加载曲线上的虚拟体积变量（m³） |
| $dv$ — Dummy-volume integration element (m³)<br>$dv$ — 体积哑变量积分微元（m³） |  |

**Conventions and conditions.** $\partial/\partial p_0$ is the pressure derivative; the vertical bar holds radius fixed; $\int$ integrates that loading curve; Subscripts b and bl label blister compliance/bending and blister volume, respectively; the meanings are explicitly fixed here; No crack-area variation is taken during the loading-curve integral; For positive pressure, compliance also equals volume divided by pressure; at zero pressure the derivative avoids division by zero.

**约定与条件。** $\partial/\partial p_0$为压力导数；竖线表示保持半径不变；$\int$表示该加载曲线积分；下标b与bl分别表示鼓泡柔度／弯曲及鼓泡体积，此处已明确其含义；在加载曲线积分过程中不改变裂纹面积；正压力时，柔度也等于体积除以压力；零压力时采用导数避免除以零。

(C4-E19) · Derived potential under maintained-pressure control / 维持压力控制条件下推导的势能


$$
C_b=\left.\frac{\partial V_{\rm bl}}{\partial p_0}\right|_b=\frac{\pi b^6}{192D_f},\qquad V_{\rm bl}=C_bp_0,\qquad U_b=\int_0^{V_{\rm bl}}\frac{v}{C_b}\,dv=\frac{V_{\rm bl}^2}{2C_b}=\frac{p_0V_{\rm bl}}2,\qquad \mathcal P=U_b-p_0V_{\rm bl}=-\frac{\pi p_0^2b^6}{384D_f}
$$


![Source work changes the sign of the relevant total potential.](../assets/figures/c4-e19.svg)

Source work changes the sign of the relevant total potential.

压力源做功改变相关总势能的符号。

Step 15 — Differentiate potential by crack radius. Divide by the area derivative, retaining numerical factors. Positive pressure gives positive release rate. Growing compliance lowers plate-plus-reservoir potential. Doubling radius at fixed pressure multiplies driving force by sixteen.

步骤 15——对裂纹半径求势能导数，再除以面积导数，并保留数值系数。正压给出正能量释放率。柔顺性增加降低板与储库总势能。压力固定时，半径加倍使驱动力增至十六倍。

**Symbols before Eq. (C4-E20).**

**式（C4-E20）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $A_c$ is delaminated area (m²)<br>$A_c$为脱层面积（m²） | $b>0$ its radius (m)<br>$b>0$为其半径（m） |
| $\pi$ the circle constant (dimensionless)<br>$\pi$为圆周率（无量纲） | $\mathcal P$ total potential including maintained pressure (J)<br>$\mathcal P$为包含恒压源的总势能（J） |
| $p_0$ fixed pressure difference (Pa)<br>$p_0$为固定压差（Pa） | $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） |
| $G_{p_0}$ is energy-release rate under that control (J m⁻²)<br>$G_{p_0}$为该控制方式下的能量释放率（J m⁻²） |  |

**Conventions and conditions.** $d/db$ differentiates in radius; the vertical bar and subscript $p_0$ indicate held pressure; Subscript c labels crack area; all length superscripts are powers; Positive $b$ makes the area derivative nonzero.

**约定与条件。** $d/db$表示按半径求导；竖线及下标$p_0$表示保持压力不变；下标c表示裂纹面积；长度上的上标均为幂；$b$为正保证面积导数非零。

(C4-E20) · Derived quasistatic energy-release rate / 推导得到的准静态能量释放率


$$
\begin{aligned}A_c&=\pi b^2,\qquad \left.\frac{d\mathcal P}{db}\right|_{p_0}=-\frac{6\pi p_0^2b^5}{384D_f},\qquad\frac{dA_c}{db}=2\pi b,\\G_{p_0}&=-\frac{(d\mathcal P/db)_{p_0}}{dA_c/db}=\frac{p_0^2b^4}{128D_f}.\end{aligned}
$$


![Geometry and compliance convert pressure into fracture energy per area.](../assets/figures/c4-e20.svg)

Geometry and compliance convert pressure into fracture energy per area.

几何与柔度将压力转换为单位面积断裂能。

**Symbols before Eq. (C4-E21).**

**式（C4-E21）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $p_{0,\rm crit}>0$ is critical maintained pressure (Pa) for constant fracture resistance $\Gamma>0$ (J m⁻²)<br>$p_{0,\rm crit}>0$为恒定断裂阻力$\Gamma>0$（J m⁻²）对应的临界恒压（Pa） | $D_f>0$ is bending stiffness (N m)<br>$D_f>0$为弯曲刚度（N m） |
| $b>0$ delamination radius (m)<br>$b>0$为脱层半径（m） | $p_0\ge0$ applied maintained pressure (Pa)<br>$p_0\ge0$为外加恒压（Pa） |
| $G_{p_0}$ the corresponding energy-release rate (J m⁻²)<br>$G_{p_0}$为相应能量释放率（J m⁻²） | $\Gamma$ — Practical interfacial fracture energy (J m⁻²)<br>$\Gamma$ — 实际界面断裂能（J m⁻²） |

**Conventions and conditions.** $\sqrt{\ }$ is the positive root; subscript crit labels the onset threshold; The quotient $G_{p_0}/\Gamma$ is dimensionless; This onset criterion assumes an existing crack and the quasistatic bending model.

**约定与条件。** $\sqrt{\ }$取正根；下标crit表示起始阈值；比值$G_{p_0}/\Gamma$无量纲；此起始判据假设存在预裂纹，并采用准静态弯曲模型。

(C4-E21) · Derived onset threshold within the benchmark / 基准模型内推导的起始阈值


$$
p_{0,\rm crit}=\frac{\sqrt{128D_f\Gamma}}{b^2},\qquad \frac{G_{p_0}}{\Gamma}=\left(\frac{p_0}{p_{0,\rm crit}}\right)^2
$$


![The pressure threshold depends on crack geometry and fracture resistance, not pressure alone.](../assets/figures/c4-e21.svg)

The pressure threshold depends on crack geometry and fracture resistance, not pressure alone.

压力阈值取决于裂纹几何及断裂阻力，而非压力本身。

Step 16 — Change to fixed volume. Remove continuing reservoir work and eliminate pressure through compliance. Differentiate plate storage at fixed volume. Reinsert instantaneous pressure for comparison. The same state gives the same instantaneous expression. Radius growth increases fixed-pressure driving and decreases fixed-volume driving. Constant resistance therefore gives different stability under these controls. A sealed PFC cavity has evolving mass and temperature. Its trajectory needs a thermodynamic closure.

步骤 16——改为固定体积。取消持续储库功，通过柔顺性消去压力。在固定体积下对板储能求导，再代回瞬时压力进行比较。同一状态给出相同瞬时形式。半径增长使定压驱动增加、定容驱动减小。阻力恒定时，两类控制具有不同稳定性。密闭 PFC 空腔质量和温度会演化，其轨迹需要热力学闭合。

**Symbols before Eq. (C4-E22).**

**式（C4-E22）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\bar V>0$ is imposed fixed added volume (m³)<br>$\bar V>0$为强制固定的新增体积（m³） | $U_b$ plate bending energy (J)<br>$U_b$为板弯曲能（J） |
| $C_b$ volume compliance (m³ Pa⁻¹)<br>$C_b$为体积柔度（m³ Pa⁻¹） | $D_f$ bending stiffness (N m)<br>$D_f$为弯曲刚度（N m） |
| $b>0$ crack radius (m)<br>$b>0$为裂纹半径（m） | $p(b)$ the pressure required at that radius (Pa)<br>$p(b)$为该半径处所需压力（Pa） |
| $G_{\bar V}$ — Energy-release rate at fixed added volume (J m⁻²)<br>$G_{\bar V}$ — 固定新增体积下的能量释放率（J m⁻²） | $G_{p_0}$ — Energy-release rate at fixed maintained pressure (J m⁻²)<br>$G_{p_0}$ — 固定恒定压力下的能量释放率（J m⁻²） |
| $p_0$ is maintained pressure (Pa)<br>$p_0$为恒定压力（Pa） | $\pi$ the circle constant, and $\propto$ means proportional at fixed other parameters (dimensionless)<br>$\pi$为圆周率，$\propto$表示其他参数固定时成正比（无量纲） |

**Conventions and conditions.** $d/db$ is radius differentiation holding $\bar V$ fixed; The bar labels controlled volume, not averaging; The fixed-volume system here supplies no additional pressure-source work.

**约定与条件。** $d/db$表示保持$\bar V$不变的半径求导；横线标识受控体积，而非平均；此恒容系统不再提供额外压力源功。

(C4-E22) · Derived loading-control comparison / 推导得到的加载控制方式比较


$$
\begin{aligned}U_b\big|_{\bar V}&=\frac{\bar V^2}{2C_b}=\frac{96D_f\bar V^2}{\pi b^6},\qquad p(b)=\frac{192D_f\bar V}{\pi b^6},\\G_{\bar V}&=-\frac{dU_b/db}{2\pi b}=\frac{288D_f\bar V^2}{\pi^2b^8}=\frac{p(b)^2b^4}{128D_f},\\G_{p_0}&\propto b^4\ \text{at fixed }p_0,\qquad G_{\bar V}\propto b^{-8}\ \text{at fixed }\bar V.\end{aligned}
$$


![Fixed pressure and fixed volume lead to opposite changes in driving force as the crack grows.](../assets/figures/c4-e22.svg)

Fixed pressure and fixed volume lead to opposite changes in driving force as the crack grows.

裂纹扩展时，恒压与恒容控制使驱动力发生相反变化。

### Blister calculation

### 鼓泡计算

Prescribe modulus 2 GPa, thickness 10 μm, Poisson ratio 0.35, crack radius 100 μm and fracture energy 0.10 J m⁻². These source-course inputs describe the illustrative plate. They do not specify the later 1 μm payload or PVC formulation. Convert thickness to meters before cubing. Evaluate stiffness and the positive onset root.

规定模量 2 GPa、厚度 10 μm、泊松比 0.35、裂纹半径 100 μm、断裂能 0.10 J m⁻²。这些源课程输入描述示例板，未指定后续 1 μm 载荷或 PVC 配方。厚度先换算为米再取三次方。计算刚度及正起始根。

**Symbols before Eq. (C4-E23).**

**式（C4-E23）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $D_f$ is film bending stiffness (N m)<br>$D_f$为薄膜弯曲刚度（N m） | $p_{0,\rm crit}$ the positive critical maintained pressure (Pa)<br>$p_{0,\rm crit}$为正临界恒压（Pa） |

**Conventions and conditions.** The substituted teaching Young’s modulus is 2.00×10⁹ Pa, thickness 10.0×10⁻⁶ m, Poisson’s ratio 0.35, crack radius 100×10⁻⁶ m, and fracture resistance 0.10 J m⁻²; Pa, N, m, J and kPa denote pascal, newton, metre, joule and kilopascal; $\sqrt{\ }$ is the positive root; superscripts are powers; Subscript f labels the film and crit the onset threshold.

**约定与条件。** 代入的教学杨氏模量为2.00×10⁹ Pa，厚度10.0×10⁻⁶ m，泊松比0.35，裂纹半径100×10⁻⁶ m，断裂阻力0.10 J m⁻²；Pa、N、m、J及kPa分别为帕、牛顿、米、焦耳及千帕；$\sqrt{\ }$取正根；上标表示幂；下标f表示薄膜，crit表示起始阈值。

(C4-E23) · Checked teaching substitution / 已核验的教学参数代入


$$
\begin{aligned}D_f&=\frac{(2.00\times10^9\ {\rm Pa})(10.0\times10^{-6}\ {\rm m})^3}{12(1-0.35^2)}=1.899335\times10^{-7}\ {\rm N\,m},\\p_{0,\rm crit}&=\frac{\sqrt{128(1.899335\times10^{-7}\ {\rm N\,m})(0.10\ {\rm J\,m^{-2}})}}{(100\times10^{-6}\ {\rm m})^2}=155.921\ {\rm kPa}.\end{aligned}
$$


![The stated plate and interface yield a conditional 156 kPa maintained-pressure threshold.](../assets/figures/c4-e23.svg)

The stated plate and interface yield a conditional 156 kPa maintained-pressure threshold.

所给薄板与界面产生约156 kPa的条件性恒压阈值。

Check opening, volume and stress at onset. Edge moment magnitude is pressure × radius²/8. Outer-surface bending stress is six × moment/thickness². The hypothetical plate reaches about 11.7 MPa edge stress. Allowable strength is missing. Thickness/radius is 0.10. Finite-thickness error requires assessment before claiming accuracy.

在起始点检查张开、体积及应力。边缘弯矩大小为压力 × 半径²／8，外表面弯曲应力为六 × 弯矩／厚度²。假想板边缘应力约 11.7 MPa。缺失允许强度。厚度／半径为 0.10，声称精度前须评估有限厚度误差。

**Symbols before Eq. (C4-E24).**

**式（C4-E24）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $w(0)$ is centre displacement (m)<br>$w(0)$为中心位移（m） | $h_f=10$ μm thickness (m)<br>$h_f=10$ μm为厚度（m） |
| $b=100$ μm crack radius (m)<br>$b=100$ μm为裂纹半径（m） | $D_f=1.899335$×10⁻⁷ N m bending stiffness<br>$D_f=1.899335$×10⁻⁷ N m为弯曲刚度 |
| $p_{0,\rm crit}=155.921$ kPa maintained threshold (Pa)<br>$p_{0,\rm crit}=155.921$ kPa为恒压阈值（Pa） | $V_{\rm bl}$ is blister volume (m³)<br>$V_{\rm bl}$为鼓泡体积（m³） |
| $M_r(b)$ radial bending moment per edge length (N)<br>$M_r(b)$为单位边长径向弯矩（N） | $\sigma_{rr}$ radial normal bending stress (Pa)<br>$\sigma_{rr}$为径向法向弯曲应力（Pa） |
| $\pi$ the circle constant (dimensionless)<br>$\pi$为圆周率（无量纲） |  |

**Conventions and conditions.** Subscript edge labels its outer-surface value at the clamped edge; r labels radial direction; $|\ |$ denotes magnitude; μm and MPa are micrometre and megapascal; This stress result uses the same linear isotropic plate assumptions.

**约定与条件。** 下标edge表示夹持边缘厚度外表面的值；r表示径向；$|\ |$表示幅值；μm与MPa分别为微米及兆帕；应力结果采用相同线性各向同性薄板假设。

(C4-E24) · Magnitude, geometric-validity and competing-failure checks / 数量级、几何适用性与竞争失效模式检验


$$
\begin{aligned}w(0)&=\frac{p_{0,\rm crit}b^4}{64D_f}=1.28270\ \mu{\rm m},\qquad \frac{w(0)}{h_f}=0.12827,\\V_{\rm bl}&=\frac{\pi p_{0,\rm crit}b^6}{192D_f}=1.34324\times10^{-14}\ {\rm m^3},\\|M_r(b)|&=\frac{p_{0,\rm crit}b^2}{8},\qquad |\sigma_{rr}|_{\rm edge}=\frac{6|M_r(b)|}{h_f^2}=11.6941\ {\rm MPa}.\end{aligned}
$$


![A fracture threshold must be checked against deflection validity and payload bending stress.](../assets/figures/c4-e24.svg)

A fracture threshold must be checked against deflection validity and payload bending stress.

断裂阈值必须同时检验挠度适用性与对象弯曲应力。

## 6. Cohesive strength and separation work

## 6. 内聚强度与分离功

Step 17 — Adopt triangular tensile traction–separation behavior. Initial slope sets opening stiffness, peak sets initiation strength, and final opening completes separation. This is a declared interface model. Compression needs contact closure. Unloading needs elastic recovery and damage history. Mixed modes need a coupling law.

步骤 17——采用三角形拉伸牵引—分离规律。初始斜率规定张开刚度，峰值规定起始强度，最终张开完成分离。这是给定界面模型。压缩需要接触闭合，卸载需要弹性恢复和损伤历程，混合模态需要耦合规律。

**Symbols before Eq. (C4-E25).**

**式（C4-E25）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\delta\ge0$ now denotes physical relative tensile opening (m), not variational notation<br>$\delta\ge0$此处表示物理相对拉伸张开（m），不再是变分符号 | $t_n(\delta)$ is tensile cohesive traction magnitude (Pa)<br>$t_n(\delta)$为拉伸内聚牵引幅值（Pa） |
| $K_n>0$ initial normal stiffness (Pa m⁻¹)<br>$K_n>0$为初始法向刚度（Pa m⁻¹） | $T_{\max}>0$ peak tensile traction (Pa)<br>$T_{\max}>0$为峰值拉伸牵引（Pa） |
| $\delta_0=T_{\max}/K_n$ peak-traction opening (m)<br>$\delta_0=T_{\max}/K_n$为峰值牵引处张开（m） | $\delta_c>\delta_0$ complete-separation opening (m)<br>$\delta_c>\delta_0$为完全分离张开（m） |

**Conventions and conditions.** Subscripts n, 0 and c label normal, peak onset and final separation; max labels the maximum; The law assumes monotonically increasing opening and a strictly positive softening interval; Compression and unloading are not specified by this formula.

**约定与条件。** 下标n、0、c分别表示法向、峰值起始及最终分离；max表示最大值；关系假设张开单调增大，且软化区间严格为正；此式未指定压缩与卸载行为。

(C4-E25) · Adopted monotonic tensile cohesive law / 采用的单调拉伸内聚定律


$$
\delta_0=\frac{T_{\max}}{K_n},\qquad t_n(\delta)=\begin{cases}K_n\delta,&0\le\delta\le\delta_0,\\T_{\max}\dfrac{\delta_c-\delta}{\delta_c-\delta_0},&\delta_0<\delta<\delta_c,\\0,&\delta\ge\delta_c.\end{cases}
$$


![The traction–separation curve contains strength, stiffness and a finite separation distance.](../assets/figures/c4-e25.svg)

The traction–separation curve contains strength, stiffness and a finite separation distance.

牵引—分离曲线包含强度、刚度及有限分离距离。

Step 18 — Integrate ascending and descending branches. Each contributes one triangle area. With admissible opening order, their sum depends on peak traction and final opening. Units are Pa m = J m⁻². Peak location still affects stiffness and initiation dynamics.

步骤 18——积分上升与下降分支。每段贡献一个三角形面积。张开顺序允许时，总面积取决于峰值牵引及最终张开。单位为 Pa m = J m⁻²。峰值位置仍影响刚度及起始动力学。

**Symbols before Eq. (C4-E26).**

**式（C4-E26）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Gamma>0$ is the fracture energy of the adopted monotonic law (J m⁻²)<br>$\Gamma>0$为所采用单调关系的断裂能（J m⁻²） | $\delta$ tensile opening integration variable (m)<br>$\delta$为拉伸张开积分变量（m） |
| $d\delta$ its element (m)<br>$d\delta$为其微元（m） | $t_n$ is tensile cohesive traction (Pa)<br>$t_n$为拉伸内聚牵引（Pa） |
| $K_n>0$ initial stiffness (Pa m⁻¹)<br>$K_n>0$为初始刚度（Pa m⁻¹） | $T_{\max}>0$ peak traction (Pa)<br>$T_{\max}>0$为峰值牵引（Pa） |
| $\delta_0$ opening at the peak (m)<br>$\delta_0$为峰值处张开（m） | $\delta_c>\delta_0$ final separation opening (m)<br>$\delta_c>\delta_0$为最终分离张开（m） |

**Conventions and conditions.** $\int$ integrates traction against opening; endpoint brackets mean upper minus lower value; Subscripts n, 0, c and max label normal, peak onset, final separation and maximum; The last inequality enforces a nonzero softening branch; it is a model-admissibility condition.

**约定与条件。** $\int$表示牵引对张开的积分；端点方括号表示上端值减下端值；下标n、0、c、max分别表示法向、峰值起始、最终分离与最大值；末行不等式保证非零软化分支，是模型的可接受条件。

(C4-E26) · Exact work integral of the adopted cohesive law / 所采用内聚定律的精确功积分


$$
\begin{aligned}\Gamma&=\int_0^{\delta_c}t_n(\delta)\,d\delta\\&=\frac{K_n\delta_0^2}{2}+\frac{T_{\max}}{\delta_c-\delta_0}\left[\delta_c\delta-\frac{\delta^2}{2}\right]_{\delta_0}^{\delta_c}\\&=\frac{T_{\max}\delta_0}{2}+\frac{T_{\max}(\delta_c-\delta_0)}{2}=\frac{T_{\max}\delta_c}{2},\\\delta_c&=\frac{2\Gamma}{T_{\max}},\qquad K_n>\frac{T_{\max}^2}{2\Gamma}\quad\text{for }\delta_0<\delta_c.\end{aligned}
$$


![Complete separation needs the entire traction–opening area, not merely the peak value.](../assets/figures/c4-e26.svg)

Complete separation needs the entire traction–opening area, not merely the peak value.

完全分离需要完整牵引—张开曲线面积，而不仅仅达到峰值。

**Symbols before Eq. (C4-E27).**

**式（C4-E27）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Gamma$ is assumed fracture energy (J m⁻²)<br>$\Gamma$为假设断裂能（J m⁻²） | $T_{\max}$ assumed peak tensile traction (Pa)<br>$T_{\max}$为假设峰值拉伸牵引（Pa） |
| $K_n$ assumed initial normal stiffness (Pa m⁻¹)<br>$K_n$为假设初始法向刚度（Pa m⁻¹） | $\delta_0$ peak-traction opening (m)<br>$\delta_0$为峰值牵引处张开（m） |
| $\delta_c$ final tensile separation (m)<br>$\delta_c$为最终拉伸分离（m） |  |

**Conventions and conditions.** MPa and nm denote megapascal and nanometre; $\Rightarrow$ denotes substitution into the triangular law; These are separate illustrative cohesive parameters, not measurements of the film release interface; Subscripts max, n, 0 and c identify peak, normal, peak opening and complete opening.

**约定与条件。** MPa与nm表示兆帕与纳米；$\Rightarrow$表示代入三角形关系；这些是独立内聚教学参数，而非薄膜释放界面的测量；下标max、n、0、c分别标识峰值、法向、峰值张开与完全张开。

(C4-E27) · Cohesive admissibility teaching calculation / 内聚模型容许条件的教学计算


$$
\Gamma=0.005\ {\rm J\,m^{-2}},\quad T_{\max}=0.10\ {\rm MPa},\quad K_n=10^{13}\ {\rm Pa\,m^{-1}}\quad\Rightarrow\quad\delta_0=10\ {\rm nm},\quad\delta_c=100\ {\rm nm}
$$


![The example has distinct peak and final separation openings.](../assets/figures/c4-e27.svg)

The example has distinct peak and final separation openings.

本例具有不同的峰值张开与最终分离张开。

## 7. Array-to-film calculation

## 7. 阵列至薄膜计算

Step 19 — Carry forward the finite source. Chapter 2’s inventory feeds 25 independent Chapter 3 cells. Patterned/addressed illumination gives equal prescribed allocation. Total absorbed energy is 10 μJ. Declared jet conversion 0.005 gives 50 nJ kinetic energy. Each jet has density 1000 kg m⁻³, diameter 10 μm and length 50 μm. Recompute mass and momentum without rounded speed. Separate cells carry no interacting-bubble multiplier.

步骤 19——继续使用有限源。第二章物质量供给第三章二十五个独立单元。图案／寻址照明给定相等分配。总吸收能量为 10 μJ，给定射流转换率 0.005 得到 50 nJ 动能。各射流密度 1000 kg m⁻³、直径 10 μm、长度 50 μm。用未舍入速率重算质量和动量。独立单元不采用相互作用倍数。

**Symbols before Eq. (C4-E28).**

**式（C4-E28）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_j$ is carrier mass in one uniform cylindrical jet (kg)<br>$m_j$为单股均匀圆柱射流的载液质量（kg） | $\rho=1000$ kg m⁻³ carrier density<br>$\rho=1000$ kg m⁻³为载液密度 |
| $d_j=10$ μm jet diameter<br>$d_j=10$ μm为射流直径 | $L_j=50$ μm jet length<br>$L_j=50$ μm为长度 |
| $\pi$ the circle constant (dimensionless)<br>$\pi$为圆周率（无量纲） | $E_j=2.00$ nJ is assigned kinetic energy per jet (J)<br>$E_j=2.00$ nJ为指定单射流动能（J） |
| $U_j$ its uniform speed (m s⁻¹)<br>$U_j$为其均匀速度（m s⁻¹） | $N=25$ independent identically supplied jets (dimensionless)<br>$N=25$为独立且供给相同的射流数（无量纲） |
| $E_{\rm in}$ total incoming kinetic energy (J)<br>$E_{\rm in}$为总入射动能（J） | $I_{\rm in}$ aligned incoming momentum (N s)<br>$I_{\rm in}$为同向入射动量（N s） |

**Conventions and conditions.** $\sqrt{\ }$ is the positive root; Subscripts j and in label single jet and incoming array; nJ is nanojoule; Simultaneous aligned arrival is assumed for the directional sum, but pressure fields are not added as N times a peak.

**约定与条件。** $\sqrt{\ }$取正根；下标j、in分别标识单射流与入射阵列；nJ为纳焦耳；方向求和假设同时同向到达，但不将压力场按N倍峰值相加。

(C4-E28) · Finite incoming state inherited from the teaching source / 沿用教学源模型的有限入射状态


$$
\begin{aligned}m_j&=\frac{\rho\pi d_j^2L_j}{4}=3.926990817\times10^{-12}\ {\rm kg},\\U_j&=\sqrt{\frac{2E_j}{m_j}}=31.9153824\ {\rm m\,s^{-1}},\\E_{\rm in}&=NE_j=50.0\ {\rm nJ},\qquad I_{\rm in}=Nm_jU_j=3.133285343\times10^{-9}\ {\rm N\,s}.\end{aligned}
$$


![Finite jet energy and aligned momentum provide the input to solid coupling.](../assets/figures/c4-e28.svg)

Finite jet energy and aligned momentum provide the input to solid coupling.

有限射流能量与同向动量提供固体耦合输入。

Step 20 — Declare solid coupling. Payload area is 1 mm², thickness 1 μm and density 2330 kg m⁻³. It starts at rest without stored recoverable energy. Assign 20% jet energy to deformation, release and departure. Assign 50% aligned momentum as net opening-direction payload impulse after reactions. Both fractions require measurement or coupled calculation. Boiling point and rigid-contact pressure leave them unresolved.

步骤 20——规定固体耦合。载荷面积为 1 mm²、厚度 1 μm、密度 2330 kg m⁻³，初始静止且无可恢复储能。分配 20% 射流能量用于变形、释放及离开。传力反作用之后，将 50% 同向动量分配为净张开方向载荷冲量。两比例均需测量或耦合计算。沸点与刚性接触压力不能确定它们。

**Symbols before Eq. (C4-E29).**

**式（C4-E29）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $m_f$ is payload mass (kg)<br>$m_f$为对象质量（kg） | $\rho_f=2330$ kg m⁻³ density<br>$\rho_f=2330$ kg m⁻³为密度 |
| $A_f=1.00$ mm² = 1.00×10⁻⁶ m² release area (m²)<br>$A_f=1.00$ mm² = 1.00×10⁻⁶ m²为释放面积（m²） | $h_f=1.00$ μm = 1.00×10⁻⁶ m thickness<br>$h_f=1.00$ μm = 1.00×10⁻⁶ m为厚度 |
| $E_{\rm solid}$ is assigned useful solid energy (J)<br>$E_{\rm solid}$为指定有效固体能量（J） | $E_{\rm in}$ incoming jet kinetic energy (J)<br>$E_{\rm in}$为入射射流动能（J） |
| $\eta_E=0.20$ a dimensionless energy-allocation assumption<br>$\eta_E=0.20$为无量纲能量分配假设 | $I_{\rm net}$ is assigned net opening-direction payload impulse after all load-path reactions (N s)<br>$I_{\rm net}$为考虑全部传力路径反作用后的净张开方向对象冲量（N s） |
| $I_{\rm in}$ aligned incoming momentum (N s)<br>$I_{\rm in}$为同向入射动量（N s） | $\eta_I=0.50$ a dimensionless impulse assumption<br>$\eta_I=0.50$为无量纲冲量假设 |

**Conventions and conditions.** Labels f, in, solid, net, E and I identify film, incoming, useful solid allocation, net, energy and impulse; The numerical first-row factors represent density, area and thickness in SI units.

**约定与条件。** 标签f、in、solid、net、E、I分别标识薄膜、入射、有效固体分配、净量、能量与冲量；第一行数值因子分别是SI制密度、面积及厚度。

(C4-E29) · Explicit conditional solid-coupling allocation / 明确给定且有条件的固体耦合分配


$$
\begin{aligned}m_f&=\rho_fA_fh_f=(2330)(1.00\times10^{-6})(1.00\times10^{-6})\ {\rm kg}=2.33\times10^{-9}\ {\rm kg},\\E_{\rm solid}&=\eta_EE_{\rm in}=0.20(50.0\ {\rm nJ})=10.0\ {\rm nJ},\\I_{\rm net}&=\eta_II_{\rm in}=0.50(3.133285343\times10^{-9}\ {\rm N\,s})=1.566642672\times10^{-9}\ {\rm N\,s}.\end{aligned}
$$


![Declared coupling converts incoming jet budgets into conditional payload budgets.](../assets/figures/c4-e29.svg)

Declared coupling converts incoming jet budgets into conditional payload budgets.

明确声明的耦合将入射射流预算转换为条件性对象预算。

Step 21 — Apply global necessary conditions. Separation costs fracture energy × intended area. Minimum translation costs half mass × minimum speed². Net impulse must reach mass × minimum speed. Residual bending, rotation, loss and competing fracture add demands. Failure excludes this assumed case. Passing leaves full transfer unresolved. Exact complete impulse from rest fixes final center-of-mass speed.

步骤 21——应用整体必要条件。分离消耗断裂能 × 目标面积。最低平动消耗质量 × 最低速率²的一半。净冲量须达到质量 × 最低速率。残余弯曲、旋转、损失及竞争断裂会增加需求。失败可排除该假设情形，通过仍未确立完整转印。静止开始的精确总冲量决定最终质心速率。

**Symbols before Eq. (C4-E30).**

**式（C4-E30）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $E_{\rm req}(v_f)$ is minimum fracture-plus-translation energy (J)<br>$E_{\rm req}(v_f)$为最低断裂加平动能量（J） | $I_{\rm req}(v_f)$ required net impulse for the minimum departure speed (N s)<br>$I_{\rm req}(v_f)$为达到最低离开速度所需净冲量（N s） |
| $v_f\ge0$ that required speed (m s⁻¹)<br>$v_f\ge0$为所需速度（m s⁻¹） | $m_f>0$ payload mass (kg)<br>$m_f>0$为对象质量（kg） |
| $A_f$ full intended release area (m²)<br>$A_f$为全部目标释放面积（m²） | $\Gamma\ge0$ assumed uniform fracture energy (J m⁻²)<br>$\Gamma\ge0$为假设均匀断裂能（J m⁻²） |
| $E_{\rm solid}$ is assigned available solid energy (J)<br>$E_{\rm solid}$为指定可用固体能量（J） | $I_{\rm net}$ is net opening-direction impulse after interface/support reactions (N s)<br>$I_{\rm net}$为考虑界面／支承反作用后的净张开方向冲量（N s） |

**Conventions and conditions.** Subscripts req, f, solid and net identify required, payload, useful solid and net quantities; The inequalities are necessary under the stated zero-initial-energy/no-additional-source assumptions; they are not spatial fracture solutions.

**约定与条件。** 下标req、f、solid、net分别标识所需、对象、有效固体及净量；在所述零初始能量／无额外源假设下，不等式是必要条件，而非空间断裂解。

(C4-E30) · Necessary global energy and momentum screens / 全局能量与动量的必要条件筛查


$$
E_{\rm req}(v_f)=\Gamma A_f+\frac12m_fv_f^2,\qquad I_{\rm req}(v_f)=m_fv_f,\qquad E_{\rm solid}\ge E_{\rm req}(v_f),\qquad I_{\rm net}\ge I_{\rm req}(v_f)
$$


![The full intended release area, not a pressure peak, determines the fracture-energy cost.](../assets/figures/c4-e30.svg)

The full intended release area, not a pressure peak, determines the fracture-energy cost.

决定断裂能消耗的是全部目标释放面积，而非压力峰值。

**Symbols before Eq. (C4-E31).**

**式（C4-E31）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Gamma$ is assumed uniform release fracture energy (J m⁻²)<br>$\Gamma$为假设均匀释放断裂能（J m⁻²） | $A_f=1.00$×10⁻⁶ m² intended full release area (m²)<br>$A_f=1.00$×10⁻⁶ m²为全部目标释放面积（m²） |
| $E_{\rm solid}=10.0$ nJ assigned available solid energy (J)<br>$E_{\rm solid}=10.0$ nJ为指定可用固体能量（J） |  |

**Conventions and conditions.** nJ is nanojoule; $\Rightarrow$ denotes numerical substitution; The comparison assumes no initially stored recoverable energy and no additional post-impact source; Subscript f labels film area, and solid labels the assigned useful energy.

**约定与条件。** nJ为纳焦耳；$\Rightarrow$表示数值代入；比较假设没有初始储存的可恢复能量，也没有额外冲击后源；下标f表示薄膜面积，solid表示指定有效能量。

(C4-E31) · Failed release-energy screen / 未通过的释放能量筛查


$$
\Gamma=0.020\ {\rm J\,m^{-2}}\quad\Rightarrow\quad \Gamma A_f=(0.020)(1.00\times10^{-6})\ {\rm J}=20.0\ {\rm nJ}>E_{\rm solid}=10.0\ {\rm nJ}
$$


![The assigned source cannot release the whole interface even before departure energy is added.](../assets/figures/c4-e31.svg)

The assigned source cannot release the whole interface even before departure energy is added.

即使尚未计入离开动能，所指定源也无法释放整个界面。

The stated energy failure excludes that case. The 47.23 MPa local transient creates no extra energy. Its footprint cannot automatically cover 1 mm² or sustain full-duration loading. Local damage is possible. Now change fracture energy to 0.005 J m⁻². Require minimum departure speed 0.50 m s⁻¹. Keep incoming jets and coupling fixed, then repeat both screens.

给定能量条件失败，排除该情形。47.23 MPa 局部瞬态不会产生额外能量，其作用区不会自动覆盖 1 mm² 或维持整个加载时长，并可能造成局部损伤。现将断裂能改为 0.005 J m⁻²，要求最低离开速率 0.50 m s⁻¹。保持入射射流及耦合不变，重算两类筛选。

**Symbols before Eq. (C4-E32).**

**式（C4-E32）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Gamma=0.005$ J m⁻² is the changed teaching fracture energy<br>$\Gamma=0.005$ J m⁻²为改变后的教学断裂能 | $A_f=1.00$×10⁻⁶ m² is release area (m²)<br>$A_f=1.00$×10⁻⁶ m²为释放面积（m²） |
| $m_f=2.33$×10⁻⁹ kg is payload mass (kg)<br>$m_f=2.33$×10⁻⁹ kg为对象质量（kg） | $v_f=0.50$ m s⁻¹ is minimum required departure speed<br>$v_f=0.50$ m s⁻¹为最低所需离开速度 |
| $E_{\rm req}$ is minimum fracture-plus-translation energy (J)<br>$E_{\rm req}$为最低断裂加平动能（J） | $I_{\rm req}$ required net impulse (N s)<br>$I_{\rm req}$为所需净冲量（N s） |
| $I_{\rm net}=1.566642672$×10⁻⁹ N s the assigned actual net impulse<br>$I_{\rm net}=1.566642672$×10⁻⁹ N s为指定实际净冲量 |  |

**Conventions and conditions.** nJ is nanojoule; Subscripts req, f and net label required, payload and net; The 10.0 nJ comparator is assigned solid energy; The first-row numbers are SI mass and speed.

**约定与条件。** nJ为纳焦耳；下标req、f、net分别标识所需、对象及净量；10.0 nJ比较值是指定固体能量；第一行数值为SI制质量与速度。

(C4-E32) · Passed necessary release and minimum-speed screens / 通过的释放与最低速度必要条件筛查


$$
\begin{aligned}\Gamma A_f&=5.00\ {\rm nJ},\qquad \frac12m_fv_f^2=\frac12(2.33\times10^{-9})(0.50)^2\ {\rm J}=0.29125\ {\rm nJ},\\E_{\rm req}(0.50\ {\rm m\,s^{-1}})&=5.29125\ {\rm nJ}<10.0\ {\rm nJ},\\I_{\rm req}(0.50\ {\rm m\,s^{-1}})&=(2.33\times10^{-9})(0.50)\ {\rm N\,s}=1.165\times10^{-9}\ {\rm N\,s}<I_{\rm net}.\end{aligned}
$$


![Reducing the assumed fracture cost allows the necessary budgets to pass.](../assets/figures/c4-e32.svg)

Reducing the assumed fracture cost allows the necessary budgets to pass.

降低假设断裂消耗后，必要预算可以通过。

Step 22 — Match energy to exact impulse. Complete assigned impulse gives final speed 0.67238 m s⁻¹. This exceeds the 0.50 m s⁻¹ minimum. Its kinetic energy is 0.52669 nJ; minimum-speed energy is 0.29125 nJ. Adding actual kinetic energy still fits the 10 nJ low-fracture budget. Exact 0.50 m s⁻¹ would require counter-impulse or different coupling. Energy and momentum must share a physical force path.

步骤 22——使能量与精确冲量一致。完整分配冲量给出最终速率 0.67238 m s⁻¹，高于 0.50 m s⁻¹ 最低要求。对应动能为 0.52669 nJ，最低速率动能为 0.29125 nJ。计入实际动能后仍满足 10 nJ 低断裂能预算。精确 0.50 m s⁻¹ 需反向冲量或不同耦合。能量和动量须对应同一实际传力路径。

**Symbols before Eq. (C4-E33).**

**式（C4-E33）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $v_{\rm CM}$ is actual final centre-of-mass speed (m s⁻¹) if the specified $I_{\rm net}$ is the complete net impulse from rest (N s)<br>$v_{\rm CM}$为实际最终质心速度（m s⁻¹），条件是所给$I_{\rm net}$为从静止开始受到的全部净冲量（N s） | $m_f=2.33$×10⁻⁹ kg is payload mass (kg)<br>$m_f=2.33$×10⁻⁹ kg为对象质量（kg） |
| $K_{\rm CM}$ centre-of-mass kinetic energy (J)<br>$K_{\rm CM}$为质心动能（J） | $\Gamma=0.005$ J m⁻² fracture energy<br>$\Gamma=0.005$ J m⁻²为断裂能 |
| $A_f=1.00$×10⁻⁶ m² release area (m²)<br>$A_f=1.00$×10⁻⁶ m²为释放面积（m²） | $E_{\rm solid}=10.0$ nJ assigned available energy (J)<br>$E_{\rm solid}=10.0$ nJ为指定可用能量（J） |
| $I_{\rm net}$ — Net opening-direction impulse after all load-path reactions (N s)<br>$I_{\rm net}$ — 考虑全部载荷路径反作用后的净张开方向冲量（N s） |  |

**Conventions and conditions.** CM labels centre of mass and net labels impulse after all reactions; nJ denotes nanojoule; Rotation, shape motion and dissipation still require additional positive energy beyond the terms shown.

**约定与条件。** CM标识质心，net表示考虑全部反作用后的冲量；nJ为纳焦耳；转动、形状运动及耗散仍需在所示项之外增加正能量。

(C4-E33) · Energy–momentum compatibility check / 能量–动量相容性检验


$$
v_{\rm CM}=\frac{I_{\rm net}}{m_f}=0.672378829\ {\rm m\,s^{-1}},\qquad K_{\rm CM}=\frac{I_{\rm net}^2}{2m_f}=0.526688683\ {\rm nJ},\qquad \Gamma A_f+K_{\rm CM}=5.526688683\ {\rm nJ}<E_{\rm solid}
$$


![The stated impulse and low-fracture-energy budget are mutually consistent at the implied speed.](../assets/figures/c4-e33.svg)

The stated impulse and low-fracture-energy budget are mutually consistent at the implied speed.

所给冲量与低断裂能预算在其决定的速度处相互相容。

**Missing stack calibration.** Coupling fractions, fracture energy, cohesive strength and PVC transmission remain unmeasured. The screens give conditional feasibility or exclusion. Resolve crack coverage, puncture, bending, torque, competing release and intact arrival.

**缺失叠层标定。** 耦合比例、断裂能、内聚强度及 PVC 传递尚未测量。筛选给出有条件可行性或排除。须解析裂纹覆盖、穿刺、弯曲、扭矩、竞争释放及完整到达。

## 8. Placement and reset

## 8. 落位与复位

Step 23 — Track payload flight after release. With negligible drag and gravity, lateral offset equals normal gap × tangent of departure angle. Use payload gap rather than liquid-jet gap. Array nonuniformity can add torque despite sufficient net impulse. The receiver must arrest motion, avoid damage and rebound, and provide final adhesion.

步骤 23——追踪释放后的载荷飞行。阻力与重力可忽略时，横向偏移等于法向间隙 × 离开角正切。采用载荷间隙而非液体射流间隙。阵列不均匀可在净冲量足够时增加扭矩。受载体须停止运动、避免损伤及反弹，并提供最终粘附。

**Symbols before Eq. (C4-E34).**

**式（C4-E34）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Delta x$ is lateral payload offset (m)<br>$\Delta x$为对象横向偏移（m） | $H_f>0$ normal payload flight gap (m)<br>$H_f>0$为对象法向飞行间隙（m） |
| $\theta\in(-\pi/2,\pi/2)$ departure angle relative to the target normal (rad)<br>$\theta\in(-\pi/2,\pi/2)$为相对目标法向的离开角（rad） |  |

**Conventions and conditions.** $\tan$ is tangent; the numerical angle is converted from degrees to radians for evaluation; μm is micrometre and $\Rightarrow$ denotes substitution; Subscript f labels film/payload flight, not liquid-jet travel; The relation assumes straight flight without significant drag, gravity or rotation-dependent aerodynamic force; $\Delta$ marks position difference.

**约定与条件。** $\tan$为正切；数值角度由度转换为弧度计算；μm为微米，$\Rightarrow$表示代入；下标f标识薄膜／对象飞行，而非液体射流运动；关系假设直线飞行，且无显著阻力、重力或随转动变化的气动力；$\Delta$表示位置差。

(C4-E34) · Ballistic placement estimate / 弹道式定位估算


$$
\Delta x=H_f\tan\theta,\qquad H_f=100\ \mu{\rm m},\quad\theta=1^{\circ}\quad\Rightarrow\quad\Delta x=1.74551\ \mu{\rm m}
$$


![A finite receiving gap converts angular error into placement error.](../assets/figures/c4-e34.svg)

A finite receiving gap converts angular error into placement error.

有限接收间隙将角度误差转换为落位误差。

Cooling, condensation, remaining inventory, shell integrity and trapped gas set the next shot. Persistent cavities can change absorption, wetting and transmission. Repeatable transfer requires activation, useful output, selective release, survival, landing and reset. Report single-shot pressure records separately from the repeatable transfer window.

冷却、凝结、剩余物质量、壳层完整性及滞留气体决定下一次发射。残留空腔可改变吸收、润湿和传递。可重复转印需要激活、有用输出、选择性释放、完整存续、落位及复位。单发压力纪录与可重复转印窗口分别报告。

Measure deposited energy and activation statistics. Track cavity shape, lifetime and arriving jet mass, speed and direction. Record exposed and buried load histories, PVC/film motion and crack growth. Verify final integrity, position and next-shot state. Each missing link needs its corresponding measurement or model.

测量沉积能量及激活统计。追踪空腔形状、寿命及到达射流质量、速率、方向。记录外露与埋藏载荷历程、PVC／薄膜运动及裂纹增长。核验最终完整性、位置与下一发状态。每个缺失环节需对应测量或模型。

## Oral questions

## 口头问题

### Trace a 47 MPa impact through the film/PVC stack. What limits release?

### 追踪 47 MPa 撞击在薄膜／PVC 叠层中的传递。什么限制释放？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C4-E35).**

**式（C4-E35）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\boldsymbol t_l$ — Liquid traction on the solid (Pa)<br>$\boldsymbol t_l$ — 液体作用于固体的牵引（Pa） | $\boldsymbol T_l$ liquid stress tensor (Pa)<br>$\boldsymbol T_l$为液体应力张量（Pa） |
| $\boldsymbol n_f$ solid-to-liquid unit normal (dimensionless)<br>$\boldsymbol n_f$为固体指向液体的单位法向（无量纲） | $\boldsymbol I_l$ applied liquid impulse (N s)<br>$\boldsymbol I_l$为液体外加冲量（N s） |
| $\mathcal W_l$ delivered work (J)<br>$\mathcal W_l$为传递功（J） | $A_f(t)$ is loaded surface (m²)<br>$A_f(t)$为受载表面（m²） |
| $dA$ its element (m²)<br>$dA$为其微元（m²） | $\boldsymbol v_f$ surface velocity (m s⁻¹)<br>$\boldsymbol v_f$为表面速度（m s⁻¹） |
| $t_a$ — Load-event start time (s)<br>$t_a$ — 载荷事件开始时刻（s） | $t_b$ — Load-event end time (s)<br>$t_b$ — 载荷事件结束时刻（s） |
| $t$ — Time (s)<br>$t$ — 时间（s） | $dt$ — Time integration element (s)<br>$dt$ — 时间积分微元（s） |

**Conventions and conditions.** $\int$ means surface/time integration; the dot denotes a vector projection; Subscripts l and f label liquid and film; The same identities first load PVC if it is the exposed layer; $t_a<t_b$ fixes the integration interval..

**约定与条件。** 原公式：$\boldsymbol t_l$为流体施加于固体的牵引（Pa）；$\int$表示表面／时间积分；点乘表示向量投影；下标l、f表示液体与薄膜；若PVC为外露层，同一恒等式首先加载PVC；$t_a<t_b$ 确定积分区间。。

(C4-E35) · Original load, impulse and work formulas / 原始载荷、冲量与功公式


$$
\boldsymbol t_l=\boldsymbol T_l\boldsymbol n_f,\qquad \boldsymbol I_l=\int_{t_a}^{t_b}\int_{A_f(t)}\boldsymbol t_l\,dA\,dt,\qquad \mathcal W_l=\int_{t_a}^{t_b}\int_{A_f(t)}\boldsymbol t_l\cdot\boldsymbol v_f\,dA\,dt
$$


![Reference answer: pressure, impulse and work describe different parts of the transmission path.](../assets/figures/c4-e35.svg)

Reference answer: pressure, impulse and work describe different parts of the transmission path.

参考答案：压力、冲量与功描述传递路径中的不同部分。

**Symbols before Eq. (C4-E36).**

**式（C4-E36）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $E_{\rm solid}$ — Assigned useful solid-energy budget (J)<br>$E_{\rm solid}$ — 指定的有效固体能量预算（J） | $\Gamma$ uniform release fracture energy (J m⁻²)<br>$\Gamma$为均匀释放断裂能（J m⁻²） |
| $A_f$ intended full release area (m²)<br>$A_f$为全部目标释放面积（m²） | $m_f$ payload mass (kg)<br>$m_f$为对象质量（kg） |
| $v_f$ minimum required departure speed (m s⁻¹)<br>$v_f$为最低所需离开速度（m s⁻¹） | $I_{\rm net}$ net opening impulse after all reactions (N s)<br>$I_{\rm net}$为考虑全部反作用后的净张开冲量（N s） |

**Conventions and conditions.** The payload initially rests and has no additional recoverable source; Subscripts solid, f and net label useful solid allocation, payload and net impulse.

**约定与条件。** 原必要筛选：$E_{\rm solid}$为指定可用固体能量（J）；对象初始静止，且无额外可恢复源；下标solid、f、net标识有效固体分配、对象及净冲量。

(C4-E36) · Original global screens / 原始全局筛查公式


$$
E_{\rm solid}\ge\Gamma A_f+\frac12m_fv_f^2,\qquad I_{\rm net}\ge m_fv_f
$$


![Reference answer: finite energy and net impulse must reach the intended interface.](../assets/figures/c4-e36.svg)

Reference answer: finite energy and net impulse must reach the intended interface.

参考答案：有限能量与净冲量必须到达目标界面。

The 47.23 MPa scale describes initial local compression at a rigid receiver. Footprint, duration and transmission still require calculation. Twenty-five jets carry 50 nJ; assigned useful solid energy is 10 nJ. Releasing 1 mm² at 0.020 J m⁻² costs 20 nJ before translation. This case fails its energy condition. Direct impact first loads film; intact PVC first carries the load. Film loading follows PVC motion and contact. A lower-fracture case still needs crack coverage and payload integrity.

47.23 MPa 尺度描述刚性受载体初始局部压缩。作用面积、时长及传递仍需计算。二十五束射流携带 50 nJ，分配有用固体能量为 10 nJ。以 0.020 J m⁻² 释放 1 mm²，在平动之前已需 20 nJ。该情形能量条件失败。直接撞击先加载薄膜，完整 PVC 则先承载。薄膜载荷取决于 PVC 运动与接触。低断裂能情形仍需裂纹覆盖及载荷完整性。

#### Review criteria

#### 审阅标准

* Distinguish local compressive pressure from opening traction, impulse and delivered work.

  区分局部压缩压力、张开牵引、冲量与传递功。
* Explain why the stated 10 nJ budget cannot pay the 20 nJ full-area release cost.

  解释为什么所给10 nJ预算无法支付20 nJ整面积释放消耗。
* Trace direct and PVC-mediated force paths, identify unknown transmission, and retain spatial/competing-failure checks.

  追踪直接及PVC介导传力路径，指出未知传递关系，并保留空间／竞争失效检验。

### When does the 156 kPa blister threshold apply?

### 156 kPa 鼓泡阈值适用于哪些条件？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C4-E37).**

**式（C4-E37）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $w(r)$ — Blister opening displacement (m)<br>$w(r)$ — 鼓泡张开位移（m） | $r\in[0,b]$ radial position (m)<br>$r\in[0,b]$为径向位置（m） |
| $b>0$ existing circular crack radius (m)<br>$b>0$为预存圆裂纹半径（m） | $p_0\ge0$ uniform maintained pressure difference (Pa)<br>$p_0\ge0$为均匀恒定压差（Pa） |
| $D_f>0$ linear plate bending stiffness (N m)<br>$D_f>0$为线性薄板弯曲刚度（N m） | $G_{p_0}$ fixed-pressure energy-release rate (J m⁻²)<br>$G_{p_0}$为恒压能量释放率（J m⁻²） |
| $\Gamma>0$ constant fracture resistance (J m⁻²)<br>$\Gamma>0$为恒定断裂阻力（J m⁻²） | $p_{0,\rm crit}$ positive onset pressure (Pa)<br>$p_{0,\rm crit}$为正起始压力（Pa） |

**Conventions and conditions.** $\sqrt{\ }$ is the positive root; Subscripts f, 0 and crit denote film, maintained load and threshold; These expressions require regular centre and a clamped crack edge, quasistatic bending, and negligible stretching/pretension.

**约定与条件。** 原鼓泡公式：$w(r)$为张开位移（m）；$\sqrt{\ }$取正根；下标f、0、crit分别表示薄膜、恒定载荷与阈值；表达式要求中心正则、裂纹边缘夹持、准静态弯曲，且拉伸／预张力可忽略。

(C4-E37) · Original pressure-controlled benchmark formulas / 原始压力控制基准模型公式


$$
w(r)=\frac{p_0}{64D_f}(b^2-r^2)^2,\qquad G_{p_0}=\frac{p_0^2b^4}{128D_f},\qquad p_{0,\rm crit}=\frac{\sqrt{128D_f\Gamma}}{b^2}
$$


![Reference answer: this pressure threshold follows a particular geometry and loading control.](../assets/figures/c4-e37.svg)

Reference answer: this pressure threshold follows a particular geometry and loading control.

参考答案：此压力阈值源于特定几何及加载控制。

The blister threshold follows from the clamped-plate solution, volume integration and reservoir work. Differentiate total potential by crack area. Assume an existing circular crack, slow uniform bending, negligible stretching, pretension and inertia. A brief local jet needs a different loading history. Intact PVC also changes the loaded structure. Fixed pressure increases driving with crack radius. Fixed volume lowers pressure and driving during growth. A sealed PFC cavity needs evolving pressure, volume and temperature. Rapid release needs transmitted traction, inertia, crack kinetics and energy balance. Check payload stress alongside interface release.

鼓泡阈值来自夹持板解、体积积分及储库功，再对裂纹面积求总势能导数。假设已有圆裂纹、缓慢均匀弯曲、拉伸、预张力及惯性可忽略。短局部射流需要不同加载历程。完整 PVC 也会改变受载结构。固定压力时，驱动随裂纹半径增加；固定体积时，增长使压力与驱动降低。密闭 PFC 空腔需演化压力、体积和温度。快速释放需传递牵引、惯性、裂纹动力学及能量平衡。界面释放同时须检查载荷应力。

#### Review criteria

#### 审阅标准

* Reconstruct pressure → plate opening → volume → source-inclusive potential → energy-release rate.

  重构压力 → 薄板张开 → 体积 → 含源势能 → 能量释放率。
* Identify the clamped existing crack, uniform maintained pressure and quasistatic small-deflection assumptions.

  指出夹持预裂纹、均匀恒压及准静态小挠度假设。
* Explain why short/localized loads, fixed volume, sealed thermodynamics or PVC transmission require another calculation.

  解释短时／局部载荷、恒容、封闭热力学或PVC传递为什么需要另一计算。

### Both global screens pass. What measurements establish repeatable intact transfer?

### 两项整体筛选均通过。哪些测量能确立可重复完整转印？

Explain the mechanism, assumptions, and limits in your own words.

用自己的话解释机制、假设与限制。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C4-E38).**

**式（C4-E38）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $\Gamma$ — Practical interfacial fracture energy (J m⁻²)<br>$\Gamma$ — 实际界面断裂能（J m⁻²） | $\delta$ physical opening integration variable (m)<br>$\delta$为物理张开积分变量（m） |
| $d\delta$ its element (m)<br>$d\delta$为其微元（m） | $\delta_c$ complete opening (m)<br>$\delta_c$为完全张开（m） |
| $t_n$ tensile cohesive traction (Pa)<br>$t_n$为拉伸内聚牵引（Pa） | $T_{\max}$ peak tensile traction (Pa)<br>$T_{\max}$为峰值拉伸牵引（Pa） |
| $G$ is energy available per new crack area (J m⁻²)<br>$G$为单位新增裂纹面积可用能量（J m⁻²） | $\psi$ dimensionless mode mixture<br>$\psi$为无量纲模态混合参数 |
| $T_i$ interface temperature (K)<br>$T_i$为界面温度（K） | $v_c$ crack speed (m s⁻¹)<br>$v_c$为裂纹速度（m s⁻¹） |

**Conventions and conditions.** The half-product applies to the adopted triangular monotonic law; $\int$ denotes opening integration; Subscripts n, c, i and max identify normal, crack/final opening, interface and maximum.

**约定与条件。** 原界面公式：$\Gamma$为单位面积拉伸内聚断裂功（J m⁻²）；一半乘积适用于所采用的三角形单调关系；$\int$表示张开积分；下标n、c、i、max分别表示法向、裂纹／最终张开、界面与最大值。

(C4-E38) · Original cohesive work and fracture criteria / 原始内聚功与断裂判据


$$
\Gamma=\int_0^{\delta_c}t_n(\delta)\,d\delta=\frac12T_{\max}\delta_c,\qquad G\ge\Gamma(\psi,T_i,v_c)
$$


![Reference answer: successful release requires both initiation and separation work at the correct interface.](../assets/figures/c4-e38.svg)

Reference answer: successful release requires both initiation and separation work at the correct interface.

参考答案：成功释放需要在正确界面上同时满足起始与分离功要求。

**Symbols before Eq. (C4-E39).**

**式（C4-E39）前的符号定义。**

| First individual definition / 第一项单独定义 | Second individual definition / 第二项单独定义 |
| --- | --- |
| $E_{\rm solid}$ — Assigned useful solid-energy budget (J)<br>$E_{\rm solid}$ — 指定的有效固体能量预算（J） | $\Gamma$ fracture energy (J m⁻²)<br>$\Gamma$为断裂能（J m⁻²） |
| $A_f$ full release area (m²)<br>$A_f$为全部释放面积（m²） | $m_f$ payload mass (kg)<br>$m_f$为对象质量（kg） |
| $v_f$ minimum departure speed (m s⁻¹)<br>$v_f$为最低离开速度（m s⁻¹） | $I_{\rm net}$ net opening impulse (N s)<br>$I_{\rm net}$为净张开冲量（N s） |
| $\Delta x$ is lateral payload offset (m)<br>$\Delta x$为对象横向偏移（m） | $H_f$ normal payload flight gap (m)<br>$H_f$为对象法向飞行间隙（m） |
| $\theta$ departure angle relative to receiver normal, and $\tan$ tangent (rad)<br>$\theta$为相对接收面法向的离开角，$\tan$为正切（rad） |  |

**Conventions and conditions.** The screens assume initial rest without another energy source; the placement relation assumes straight short flight; Subscripts solid, f and net label useful solid energy, payload and net impulse.

**约定与条件。** 原筛选与落位关系：$E_{\rm solid}$为可用有效固体能量（J）；筛选假设初始静止且无其他能量源；落位关系假设短时直线飞行；下标solid、f、net标识有效固体能量、对象及净冲量。

(C4-E39) · Original necessary operating-window checks / 原始工作窗口的必要条件检验


$$
E_{\rm solid}\ge\Gamma A_f+\frac12m_fv_f^2,\qquad I_{\rm net}\ge m_fv_f,\qquad \Delta x=H_f\tan\theta
$$


![Reference answer: passing global budgets starts, rather than completes, the transfer argument.](../assets/figures/c4-e39.svg)

Reference answer: passing global budgets starts, rather than completes, the transfer argument.

参考答案：通过整体预算是转印论证的起点，而非终点。

The low-fracture case passes assigned energy and minimum-impulse conditions. Complete transfer: Not established. Missing: local initiation, full crack coverage and payload survival. Compression needs conversion into relative interface opening. Exclude unintended release, puncture, tearing and excessive bending. Keep exact impulse consistent with final translation. Then check tilt, flight, landing adhesion and rebound. Synchronize solid motion, crack growth and integrity measurements. Repeated shots require cooling, condensation and remaining-inventory checks. Report single-shot output separately from repeatable intact transfer.

低断裂能情形通过分配能量及最低冲量条件。完整转印尚未确立。缺失：局部起始、完整裂纹覆盖及载荷存续。压缩载荷须转化为界面相对张开。须排除意外释放、穿刺、撕裂及过度弯曲。精确冲量与最终平动保持一致。再检查倾斜、飞行、落位粘附及反弹。同步测量固体运动、裂纹增长和完整性。重复发射需检查冷却、凝结及剩余物质量。单发输出与可重复完整转印分别报告。

#### Review criteria

#### 审阅标准

* Distinguish local strength initiation, full separation work and competing fracture paths.

  区分局部强度起始、完整分离功及竞争断裂路径。
* Keep energy and actual net impulse consistent and explain why spatial crack coverage and payload damage remain unresolved.

  保持能量与实际净冲量相容，并解释为什么空间裂纹覆盖和对象损伤仍未确定。
* Connect correct release to placement, landing and repeatable thermal/phase reset, proposing observations for the missing links.

  将正确释放连接至落位、着陆及可重复热／相变复位，并为缺失环节提出观测。