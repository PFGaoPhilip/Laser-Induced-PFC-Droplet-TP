"""Chapter 4: finite jet loading, fracture and intact transfer.

Owned chapter content only. All material values are declared teaching inputs.
"""
from coursekit import P, H, E, T, cite, defense, note
from symbol_tables import glossary


def eq(identifier, tex, en, zh, kind, diagram_type, labels, notes, caption_en, caption_zh):
    return E(identifier, tex, en, zh, kind,
             dict(type=diagram_type, labels=labels, notes=notes), caption_en, caption_zh)


body = []
add = body.append

add(H("1. Intended-interface release", "1. 目标界面释放", 'load-path'))
add(P(
    "Connect the arriving jet to film deformation, crack growth and departure. Useful transfer ends with intact attachment at the intended receiver location. Chapter 3 supplies velocity, mass, momentum, energy, footprint and arrival history. Specify the exposed surface carrying that load. The output is opening and fracture at the release interface. These surfaces can lie at different stack positions.",
    "本章将到达射流连接至薄膜变形、裂纹增长及离开。有效转印以完整对象附着于目标位置结束。第三章提供速度、质量、动量、能量、作用面积及到达历程。须注明承受该载荷的外露表面。输出是释放界面的张开与断裂，两表面可位于叠层不同位置。"))
add(P(
    "Use Cartesian coordinates with the initial film horizontal. Positive vertical points along intended departure. Start the film at rest with specified adhesion and pre-existing delamination. Plate examples fix the donor reference face. A moving donor needs momentum and power balances. Pressure compresses the exposed face. Interface opening depends on relative face separation. Either prescribe fluid traction or resolve compatible fluid–solid velocities and opposite tractions. Count the interface load once.",
    "采用笛卡尔坐标，初始薄膜水平。竖直正方向为预期离开方向。薄膜初始静止，给定粘附及已有脱层。板示例固定供体参考面。运动供体需动量与功率平衡。压力压缩外露面，界面张开取决于两面的相对分离。可给定流体牵引，或解析相容流固速度及相反牵引。界面载荷计入一次。"))
add(T(
    [('Architecture', '结构方案'), ('Force path', '传力路径'), ('What must be solved', '需要求解的内容')],
    [
        [('Direct liquid-to-film actuation', '液体直接致动薄膜'),
         ('Liquid or jet → exposed film → release interface.', '液体或射流 → 外露薄膜 → 释放界面。'),
         ('Fluid traction, film deformation and interface separation.', '流体牵引、薄膜变形及界面分离。')],
        [('Intact PVC-mediated actuation', '完整PVC层介导致动'),
         ('Liquid or jet → PVC → contact or bond → film → release interface.', '液体或射流 → PVC → 接触或粘接层 → 薄膜 → 释放界面。'),
         ('PVC inertia, thickness, compliance, reflections, contact and the transmitted traction.', 'PVC的惯性、厚度、柔顺性、反射、接触及传递牵引。')],
        [('Sealed cavity', '封闭腔体'),
         ('Finite vapor source → cavity wall or stamp → release interface.', '有限蒸气源 → 腔壁或印章 → 释放界面。'),
         ('Coupled cavity thermodynamics, bulging and fracture; an outgoing jet need not exist.', '耦合腔体热力学、鼓起与断裂；不一定存在出射射流。')],
    ]))
add(note(
    "Intact PVC blocks liquid passage. An incident jet first loads PVC. Direct film loading requires an actual opening or rupture. Sealed cavities and open pockets have different force paths. Appendix A compares these hydrogel architectures.",
    "完整 PVC 阻挡液体穿透，入射射流首先加载 PVC。直接加载薄膜需要实际开口或破裂。密闭空腔与开放液腔具有不同传力路径。附录 A 比较这些水凝胶结构。"))
add(H("Symbols and model limits", "符号与模型范围", 'glossary', 3))
add(glossary(4))

add(H("2. Fluid stress and solid loading", "2. 流体应力与固体加载", 'traction'))
add(P(
    "Step 1 — Adopt Newtonian liquid stress. Orient the normal from solid into liquid. Stress contracted with this normal gives liquid traction on solid. For liquid below a film, the normal points down. Positive pressure pushes the film up while compressing its exposed face. Opening another interface requires deformation and relative motion.",
    "步骤 1——采用牛顿液体应力。法向由固体指向液体，应力与该法向收缩给出液体对固体的牵引。液体位于薄膜下方时，法向向下，正压力将薄膜向上推，同时压缩外露面。另一个界面的张开需要变形及相对运动。"))
add(eq('C4-E01', r'\boldsymbol D_u=\frac{\nabla\boldsymbol u+(\nabla\boldsymbol u)^{\mathsf T}}{2},\qquad \boldsymbol T_l=-p\boldsymbol I+2\mu\boldsymbol D_u,\qquad \boldsymbol t_l=\boldsymbol T_l\boldsymbol n_f',
    r'$\boldsymbol u(\boldsymbol x,t)$ is liquid velocity (m s⁻¹), $\boldsymbol x$ position (m), and $t$ time (s). $\nabla$ is the spatial gradient (m⁻¹); superscript $\mathsf T$ transposes a tensor. $\boldsymbol D_u$ is strain-rate tensor (s⁻¹), $\boldsymbol T_l$ liquid Cauchy stress (Pa), $p$ liquid pressure (Pa), $\mu\ge0$ dynamic viscosity (Pa s), and $\boldsymbol I$ the dimensionless identity tensor. $\boldsymbol n_f$ is the unit solid-to-liquid normal; $\boldsymbol t_l$ is traction on the solid (Pa). Subscripts u, l and f label velocity strain, liquid and film surface.',
    r'$\boldsymbol u(\boldsymbol x,t)$为液体速度（m s⁻¹），$\boldsymbol x$为位置（m），$t$为时间（s）。$\nabla$为空间梯度（m⁻¹）；上标$\mathsf T$表示张量转置。$\boldsymbol D_u$为应变率张量（s⁻¹），$\boldsymbol T_l$为液体柯西应力（Pa），$p$为液体压力（Pa），$\mu\ge0$为动力黏度（Pa s），$\boldsymbol I$为无量纲单位张量。$\boldsymbol n_f$为固体指向液体的单位法向；$\boldsymbol t_l$为固体上的牵引（Pa）。下标u、l、f分别标识速度应变、液体及薄膜表面。',
    'Constitutive assumption and traction identity', 'film',
    ['film surface', 'n_f ↓ solid → liquid', 'p → compressive load', 'u, x, t in liquid', 'μ, D_u — shear', 'T_l, t_l at exposed face', 'I — identity tensor'],
    ['Positive opening direction ↑', 'The release interface is a separate surface.'],
    'Pressure and shear act at the exposed film face; the drawn normal fixes the traction sign.',
    '压力与剪切作用于薄膜外露面；所画法向决定牵引符号。'))
add(P(
    "Step 2 — Integrate traction over area for force. Integrate force over time for impulse. Dot traction with surface velocity before integrating work. Pressure, impulse and work have units Pa, N s and J. A nearly rigid surface can receive high stress and impulse with little displacement work.",
    "步骤 2——对面积积分牵引得到力，对时间积分力得到冲量。求功时先将牵引与表面速度点乘。压力、冲量与功单位分别为 Pa、N s 和 J。近刚性表面可承受大应力及冲量，同时位移功很小。"))
add(eq('C4-E02', r'\begin{aligned}\boldsymbol F_l(t)&=\int_{A_f(t)}\boldsymbol t_l\,dA,\\ \boldsymbol I_l&=\int_{t_a}^{t_b}\boldsymbol F_l(t)\,dt,\\ \mathcal W_l&=\int_{t_a}^{t_b}\int_{A_f(t)}\boldsymbol t_l\cdot\boldsymbol v_f\,dA\,dt.\end{aligned}',
    r'$A_f(t)$ is the loaded solid surface (m²), $dA$ its surface-area element (m²), and $\int$ denotes integration over the indicated surface or time. $\boldsymbol t_l$ is applied liquid traction (Pa), $\boldsymbol F_l$ its resultant (N), $\boldsymbol I_l$ its impulse (N s), and $\mathcal W_l$ work delivered to the solid (J). $\boldsymbol v_f$ is local solid surface velocity (m s⁻¹). $t_a<t_b$ are event start and end times (s); $t$ and $dt$ are time and its integration element (s). The vector dot product projects force onto velocity. Subscripts l and f label liquid and film.',
    r'$A_f(t)$为固体受载表面（m²），$dA$为表面积微元（m²），$\int$表示对所示表面或时间积分。$\boldsymbol t_l$为液体施加的牵引（Pa），$\boldsymbol F_l$为其合力（N），$\boldsymbol I_l$为其冲量（N s），$\mathcal W_l$为传入固体的功（J）。$\boldsymbol v_f$为固体表面局部速度（m s⁻¹）。$t_a<t_b$为事件起止时间（s）；$t$与$dt$分别为时间及其积分微元（s）。向量点乘将力投影到速度上。下标l和f表示液体与薄膜。',
    'Exact mechanical definitions', 'impact',
    ['A_f(t) — loaded footprint', 't_l → applied traction', 'v_f ↑ moving film', 'F_l — surface resultant', 'I_l — force-time area', 'W_l — traction × displacement', 't_a → t_b — event interval'],
    ['A high pressure maximum does not specify work.'],
    'The same footprint supplies force and impulse, but surface motion is additionally required for work.',
    '同一作用范围决定力与冲量，而求功还需要表面运动信息。'))

add(H("3. Transient film mechanics", "3. 瞬态薄膜力学", 'film-dynamics'))
add(P(
    "Step 3 — Adopt a homogeneous isotropic Kirchhoff–Love plate. Assume elastic plane stress, small strain, small slope and thinness relative to deformation length. Through-thickness density integration gives areal mass. Bending stress integration gives stiffness with thickness moment thickness³/12. A bonded laminate needs a common neutral surface and laminate stiffness.",
    "步骤 3——采用均匀各向同性 Kirchhoff–Love 板。假设弹性平面应力、小应变、小斜率，厚度远小于变形长度。沿厚度积分密度得到面质量。积分弯曲应力得到刚度，其中厚度矩为厚度³／12。粘接叠层需共同中性面及叠层刚度。"))
add(eq('C4-E03', r'm_A=\int_{-h_f/2}^{h_f/2}\rho_f\,dz=\rho_fh_f,\qquad D_f=\frac{E_f}{1-\nu_f^2}\int_{-h_f/2}^{h_f/2}z^2\,dz=\frac{E_fh_f^3}{12(1-\nu_f^2)}',
    r'$m_A>0$ is film areal mass (kg m⁻²), $D_f>0$ bending stiffness (N m), $\rho_f>0$ constant density (kg m⁻³), $h_f>0$ film thickness (m), $E_f>0$ Young’s modulus (Pa), and $-1<\nu_f<1/2$ Poisson’s ratio (dimensionless). $z$ is thickness coordinate (m), zero at the neutral midplane; $dz$ is its integration element (m). $\int$ is definite thickness integration. Subscripts A and f label areal quantity and film.',
    r'$m_A>0$为薄膜面密度（kg m⁻²），$D_f>0$为弯曲刚度（N m），$\rho_f>0$为恒定密度（kg m⁻³），$h_f>0$为薄膜厚度（m），$E_f>0$为杨氏模量（Pa），$-1<\nu_f<1/2$为泊松比（无量纲）。$z$为厚度坐标（m），中性面处为零；$dz$为其积分微元（m）。$\int$表示沿厚度定积分。下标A与f标识面量与薄膜。',
    'Derived plate parameters under constitutive assumptions', 'film',
    ['h_f — thickness', 'z = 0 — neutral midplane', 'ρ_f → m_A', 'E_f, ν_f → D_f', 'z² dz — bending moment weight'],
    ['Density integrates once; bending weights distance squared.'],
    'Areal inertia and bending stiffness come from different thickness integrals.',
    '面惯性与弯曲刚度来自不同的厚度积分。'))
add(P(
    "Step 4 — Write kinetic, bending and pretension energies. Curvature is the displacement’s second spatial derivative. Poisson ratio couples the two curvature directions and twist. Hold pretension uniform; its energy penalizes slope. Shape stores elastic energy, while velocity carries kinetic energy.",
    "步骤 4——写出动能、弯曲能及预张力能。曲率为位移空间二阶导数。泊松比耦合两方向曲率与扭曲。预张力保持均匀，其能量随斜率增加。形状储存弹性能，速度携带动能。"))
add(eq('C4-E04', r'\begin{aligned}K_f&=\frac{m_A}{2}\int_{\Omega_f}\dot w^2\,dA,\\U_b&=\frac{D_f}{2}\int_{\Omega_f}\left[w_{xx}^2+w_{yy}^2+2\nu_fw_{xx}w_{yy}+2(1-\nu_f)w_{xy}^2\right]dA,\\U_T&=\frac{T_0}{2}\int_{\Omega_f}|\nabla_\parallel w|^2\,dA.\end{aligned}',
    r'$\Omega_f$ is the reference film plane (m²), $dA$ its area element (m²), $w(x,y,t)$ vertical displacement (m), $x,y$ in-plane coordinates (m), and $t$ time (s). A dot differentiates in time; subscripts $xx,yy,xy$ differentiate twice in the indicated coordinates, giving curvatures (m⁻¹). $\nabla_\parallel$ is the in-plane gradient; $|\ |$ denotes Euclidean magnitude. $m_A$ is areal mass (kg m⁻²), $D_f$ bending stiffness (N m), $\nu_f$ Poisson’s ratio, and $T_0\ge0$ prescribed isotropic tensile force per edge length (N m⁻¹). $K_f,U_b,U_T$ are kinetic, bending and pretension energies (J); $\int$ denotes area integration. Labels f, b, T identify film, bending and tension.',
    r'$\Omega_f$为薄膜参考平面（m²），$dA$为面积微元（m²），$w(x,y,t)$为竖直位移（m），$x,y$为面内坐标（m），$t$为时间（s）。上点表示时间导数；下标$xx,yy,xy$表示对所示坐标求二阶导数，得到曲率（m⁻¹）。$\nabla_\parallel$为面内梯度；$|\ |$为欧氏模长。$m_A$为面密度（kg m⁻²），$D_f$为弯曲刚度（N m），$\nu_f$为泊松比，$T_0\ge0$为给定各向同性单位边长拉力（N m⁻¹）。$K_f,U_b,U_T$分别为动能、弯曲能及预张力能（J）；$\int$表示面积积分。标签f、b、T分别指薄膜、弯曲与张力。',
    'Linear-plate energy model', 'film',
    ['Ω_f, dA — film plane', 'x, y — in-plane directions', 'w, ẇ, t — film motion', 'w_xx, w_yy, w_xy — curvature', 'D_f, ν_f — bending', 'm_A → K_f', 'T₀ → U_T', 'U_b — shape energy'],
    ['Clamped edge: displacement and normal slope fixed.'],
    'Bending energy is stored by curvature; inertia depends on velocity.',
    '曲率储存弯曲能，速度决定惯性动能。'))
add(P(
    "Step 5 — Vary displacement at a fixed clamped boundary. Integrate bending terms by parts twice. Displacement variation and its normal slope vanish at the clamp, eliminating boundary terms. Integrate tension once to obtain minus the Laplacian. Every transverse-balance term has pressure units.",
    "步骤 5——在固定夹持边界下变分位移。弯曲项分部积分两次。夹持处位移变分及其法向斜率为零，消去边界项。张力项分部积分一次，得到负拉普拉斯。横向平衡各项均为压力单位。"))
add(eq('C4-E40', r'\begin{aligned}B_{\alpha\beta}&=D_f[(1-\nu_f)w_{\alpha\beta}+\nu_f\delta_{\alpha\beta}\nabla_\parallel^2w],\\\delta U_b&=\sum_{\alpha,\beta=1}^{2}\int_{\Omega_f}B_{\alpha\beta}\partial_\alpha\partial_\beta(\delta w)\,dA\\&=\sum_{\alpha,\beta=1}^{2}\oint_{\partial\Omega_f}n_\alpha B_{\alpha\beta}\partial_\beta(\delta w)\,d\ell-\sum_{\alpha,\beta=1}^{2}\int_{\Omega_f}(\partial_\alpha B_{\alpha\beta})\partial_\beta(\delta w)\,dA\\&=\sum_{\alpha,\beta=1}^{2}\oint_{\partial\Omega_f}[n_\alpha B_{\alpha\beta}\partial_\beta(\delta w)-n_\beta(\partial_\alpha B_{\alpha\beta})\delta w]\,d\ell+\sum_{\alpha,\beta=1}^{2}\int_{\Omega_f}(\partial_\beta\partial_\alpha B_{\alpha\beta})\delta w\,dA,\\\delta U_T&=T_0\oint_{\partial\Omega_f}\delta w\,\partial_nw\,d\ell-T_0\int_{\Omega_f}\delta w\nabla_\parallel^2w\,dA,\\\delta w=0,\quad\partial_n\delta w=0&\ \Longrightarrow\ \nabla_\parallel\delta w=\boldsymbol0\quad\text{on the fixed clamp}.\end{aligned}',
    r'$\Omega_f$ is the smooth reference film plane (m²), $\partial\Omega_f$ its boundary, $dA$ area element (m²), and $d\ell$ boundary arc-length element (m). $w$ is displacement (m); $\delta w$ an admissible infinitesimal variation (m); $\delta U_b,\delta U_T$ the corresponding bending/pretension energy variations (J). $\alpha,\beta=1,2$ index the two Cartesian in-plane directions, with $\sum$ summing all four index pairs. $\partial_\alpha$ is coordinate differentiation (m⁻¹); $w_{\alpha\beta}=\partial_\alpha\partial_\beta w$ is curvature (m⁻¹). $D_f$ is bending stiffness (N m), $\nu_f$ Poisson’s ratio, $T_0$ pretension (N m⁻¹), and $B_{\alpha\beta}$ the bending-energy tensor conjugate to curvature (N). $\delta_{\alpha\beta}$ is the dimensionless Kronecker identity, distinct from variation notation. $n_\alpha,n_\beta$ are components of the outward in-plane unit boundary normal; $\partial_n$ its derivative. $\nabla_\parallel$ and $\nabla_\parallel^2$ are in-plane gradient and Laplacian; $\boldsymbol0$ is zero gradient. $\int,\oint$ denote area and closed-boundary integrals. $\Rightarrow$ uses zero tangential derivative of an identically zero boundary variation plus the prescribed zero normal derivative.',
    r'$\Omega_f$为光滑薄膜参考平面（m²），$\partial\Omega_f$为其边界，$dA$为面积微元（m²），$d\ell$为边界弧长微元（m）。$w$为位移（m）；$\delta w$为容许无穷小变分（m）；$\delta U_b,\delta U_T$为相应弯曲／预张力能变分（J）。$\alpha,\beta=1,2$标识两个笛卡尔面内方向，$\sum$对四种指标组合求和。$\partial_\alpha$为坐标求导（m⁻¹）；$w_{\alpha\beta}=\partial_\alpha\partial_\beta w$为曲率（m⁻¹）。$D_f$为弯曲刚度（N m），$\nu_f$为泊松比，$T_0$为预张力（N m⁻¹），$B_{\alpha\beta}$为与曲率共轭的弯曲能张量（N）。$\delta_{\alpha\beta}$为无量纲Kronecker单位张量，与变分记号不同。$n_\alpha,n_\beta$为面内边界外单位法向分量；$\partial_n$为沿该法向求导。$\nabla_\parallel$及$\nabla_\parallel^2$为面内梯度及拉普拉斯算子；$\boldsymbol0$为零梯度。$\int,\oint$分别表示面积积分与闭合边界积分。$\Rightarrow$使用恒为零的边界变分具有零切向导数，并结合给定零法向导数。',
    'Explicit integration-by-parts boundary terms', 'film',
    ['Ω_f — plate interior', '∂Ω_f, dℓ — fixed clamped edge', 'w, δw — displacement and variation', 'B_αβ, D_f, ν_f — curvature moments', 'n_α, n_β — in-plane boundary normal', 'δU_b, δU_T — virtual energy', 'T₀ — pretension', 'boundary: δw = 0, ∂ₙδw = 0'],
    ['The first bending boundary term contains the slope variation.', 'The second contains the displacement variation; both vanish at the clamp.'],
    'Two integrations by parts expose the boundary moment and shear terms before they are removed.',
    '两次分部积分先明确显示边界弯矩与剪力项，再依据条件将其消去。'))
add(eq('C4-E05', r'\begin{aligned}\delta U_b&=D_f\int_{\Omega_f}\left[w_{xxxx}+\{2\nu_f+2(1-\nu_f)\}w_{xxyy}+w_{yyyy}\right]\delta w\,dA\\&=D_f\int_{\Omega_f}(w_{xxxx}+2w_{xxyy}+w_{yyyy})\delta w\,dA=D_f\int_{\Omega_f}\nabla_\parallel^4w\,\delta w\,dA,\\\delta U_T&=-T_0\int_{\Omega_f}\nabla_\parallel^2w\,\delta w\,dA.\end{aligned}',
    r'$\delta$ denotes an infinitesimal admissible variation, not physical crack opening here; $\delta w$ is a displacement variation (m). $U_b,U_T$ are bending and pretension energy (J); $D_f$ is bending stiffness (N m); $\nu_f$ is dimensionless Poisson’s ratio; $T_0$ is uniform pretension (N m⁻¹). $w$ is transverse displacement (m); $x,y$ are in-plane coordinates (m). Subscripts $xxxx,xxyy,yyyy$ denote the indicated fourth derivatives (m⁻³). $\nabla_\parallel^2=\partial_x^2+\partial_y^2$ is the in-plane Laplacian; $\nabla_\parallel^4$ is that Laplacian applied twice. $\Omega_f$ is film area (m²); $dA$ is its element (m²); $\int$ is area integration. The variations and their normal slopes vanish at a clamped boundary.',
    r'$\delta$在此表示无穷小容许变分，而非物理裂纹张开；$\delta w$为位移变分（m）。$U_b,U_T$为弯曲能及预张力能（J）；$D_f$为弯曲刚度（N m）；$\nu_f$为无量纲泊松比；$T_0$为均匀预张力（N m⁻¹）。$w$为横向位移（m）；$x,y$为面内坐标（m）。下标$xxxx,xxyy,yyyy$表示所示四阶导数（m⁻³）。$\nabla_\parallel^2=\partial_x^2+\partial_y^2$为面内拉普拉斯算子；$\nabla_\parallel^4$为将该算子作用两次。$\Omega_f$为薄膜面积（m²）；$dA$为面积微元（m²）；$\int$表示面积积分。夹持边界处变分及其法向斜率均为零。',
    'Derived variational identity for fixed clamps', 'film',
    ['Ω_f, x, y — film plane', 'w, δw — displacement and variation', 'D_f, ν_f → ∇⁴w restoring load', 'T₀ → −∇²w restoring load', 'U_b, U_T — stored energy', 'clamp: δw = 0, slope variation = 0'],
    ['Four spatial derivatives arise from two integrations by parts.'],
    'A fixed clamp removes the boundary virtual-work terms.',
    '固定夹持边界使边界虚功项消失。'))
add(eq('C4-E06', r'\begin{aligned}m_A\ddot w+D_f\nabla_\parallel^4w-T_0\nabla_\parallel^2w&=p_{\rm load}-t_{\rm coh},\\w(\boldsymbol x,0)=0,\quad\dot w(\boldsymbol x,0)&=0,\\w=0,\quad\partial_n w&=0\quad\text{on a clamped edge}.\end{aligned}',
    r'$w(\boldsymbol x,t)$ is film displacement in the positive departure direction (m); $\boldsymbol x=(x,y)$ is in-plane position (m), and $t$ time (s). $\dot w,\ddot w$ are time derivatives (m s⁻¹, m s⁻²). $m_A$ is areal mass (kg m⁻²), $D_f$ bending stiffness (N m), and $T_0\ge0$ pretension (N m⁻¹). $\nabla_\parallel^2$ is in-plane Laplacian (m⁻²), and $\nabla_\parallel^4$ its square. $p_{\rm load}$ is net applied transverse traction projected positively (Pa), whereas $t_{\rm coh}\ge0$ is an opening-resisting cohesive traction magnitude (Pa). $\partial_n$ differentiates along the outward in-plane boundary normal. Initial zero is displacement or velocity according to its row. Labels load and coh identify applied and cohesive forces.',
    r'$w(\boldsymbol x,t)$为沿正离开方向的薄膜位移（m）；$\boldsymbol x=(x,y)$为面内位置（m），$t$为时间（s）。$\dot w,\ddot w$为时间导数（m s⁻¹、m s⁻²）。$m_A$为面密度（kg m⁻²），$D_f$为弯曲刚度（N m），$T_0\ge0$为预张力（N m⁻¹）。$\nabla_\parallel^2$为面内拉普拉斯算子（m⁻²），$\nabla_\parallel^4$为其平方。$p_{\rm load}$为沿正方向投影的净外加横向牵引（Pa），$t_{\rm coh}\ge0$为抵抗张开的内聚牵引幅值（Pa）。$\partial_n$表示沿面内边界外法向求导。初始零值按对应行分别表示位移或速度。标签load和coh表示外载与内聚力。',
    'Reduced transient momentum balance with explicit initial/boundary data', 'film',
    ['w, ẇ, ẅ ↑ positive departure', 'x, t — location and time', 'm_A — film inertia', 'D_f — bending stiffness', 'T₀ — pretension', 'p_load ↑ exposed load', 't_coh ↓ opening resistance', 'clamp: w = 0, ∂ₙw = 0'],
    ['The film starts at rest.', 'The release interface supplies resistance.'],
    'Film acceleration balances applied traction, elastic restoring forces and cohesive resistance.',
    '薄膜加速度由外加牵引、弹性恢复力与内聚阻力的平衡决定。'))
add(P(
    "The fixed clamp also has zero velocity and normal velocity slope. Multiply the plate equation by velocity and integrate. Inertia differentiates kinetic energy. Two bending integrations by parts differentiate bending energy. One tension integration differentiates pretension energy. Cohesive power removes energy from plate motion. The interface law partitions recoverable and irreversible parts.",
    "固定夹持处速度及法向速度斜率也为零。将板方程乘速度并积分。惯性项给出动能导数。弯曲项两次分部积分给出弯曲能导数，张力项一次积分给出预张力能导数。内聚功率从板运动取走能量。界面规律区分可恢复与不可逆部分。"))
add(eq('C4-E41', r'\begin{aligned}\int_{\Omega_f}m_A\ddot w\dot w\,dA&=\frac{dK_f}{dt},\qquad \int_{\Omega_f}D_f\nabla_\parallel^4w\dot w\,dA=\frac{dU_b}{dt},\\-\int_{\Omega_f}T_0\nabla_\parallel^2w\dot w\,dA&=\frac{dU_T}{dt},\\\frac{d}{dt}(K_f+U_b+U_T)&=\int_{\Omega_f}p_{\rm load}\dot w\,dA-\int_{\Omega_f}t_{\rm coh}\dot w\,dA.\end{aligned}',
    r'$\Omega_f$ is reference film area (m²), $dA$ its area element (m²), $w$ displacement (m), and $\dot w,\ddot w$ velocity and acceleration (m s⁻¹, m s⁻²). $m_A$ is areal mass (kg m⁻²), $D_f$ bending stiffness (N m), $T_0$ constant pretension (N m⁻¹), $p_{\rm load}$ applied transverse traction (Pa), and $t_{\rm coh}$ resisting cohesive traction (Pa). $K_f,U_b,U_T$ are kinetic, bending and pretension energies (J); $t$ is time (s); $d/dt$ is its derivative. $\nabla_\parallel^2$ is planar Laplacian and $\nabla_\parallel^4$ its square; $\int$ is area integration. The derivatives are valid for the stated constant parameters and sufficiently regular fields at a fixed clamp with zero velocity and normal velocity slope. Every row has power units W; f, b, T, load and coh label film, bending, tension, applied and cohesive.',
    r'$\Omega_f$为薄膜参考面积（m²），$dA$为面积微元（m²），$w$为位移（m），$\dot w,\ddot w$为速度及加速度（m s⁻¹、m s⁻²）。$m_A$为面密度（kg m⁻²），$D_f$为弯曲刚度（N m），$T_0$为恒定预张力（N m⁻¹），$p_{\rm load}$为外加横向牵引（Pa），$t_{\rm coh}$为抵抗内聚牵引（Pa）。$K_f,U_b,U_T$为动能、弯曲能及预张力能（J）；$t$为时间（s）；$d/dt$为时间导数。$\nabla_\parallel^2$为平面拉普拉斯算子，$\nabla_\parallel^4$为其平方；$\int$表示面积积分。导数适用于所述恒定参数、足够正则的场，以及速度和法向速度斜率均为零的固定夹持边界。各行单位均为功率W；f、b、T、load、coh分别表示薄膜、弯曲、张力、外加及内聚。',
    'Transient plate power identity under fixed clamps', 'energy',
    ['p_load ẇ → incoming solid power', 't_coh ẇ → interface power', 'm_A, ẇ, ẅ → K_f storage', 'D_f, ∇⁴w → U_b storage', 'T₀, ∇²w → U_T storage', 'Ω_f, dA — reference plane', 't — event time'],
    ['Fixed clamps perform no boundary work.', 'Recoverable cohesion and fracture loss must be counted once.'],
    'The transient plate equation conserves power between applied work, motion, shape and interface response.',
    '瞬态薄板方程在外加功、运动、形状与界面响应之间保持功率守恒。'))
add(P(
    "This is an exact balance within the reduced plate assumptions. Bending units are N m × m⁻³ = Pa. Tension units are N m⁻¹ × m⁻¹ = Pa. Zero mass gives quasistatic balance. Zero stiffness, tension and cohesion gives free areal acceleration. Large slope, stretching, plasticity, anisotropy, finite thickness or contact needs refinement. The cited static benchmark agrees with the stiffness formulation. This derivation retains inertia. <a href=\"https://ocw.mit.edu/courses/2-080j-structural-mechanics-fall-2013/resources/mit2_080jf13_lecture7/\" class=\"citation\">MIT plate benchmark</a>",
    "这是约化板假设内的精确平衡。弯曲单位为 N m × m⁻³ = Pa，张力单位为 N m⁻¹ × m⁻¹ = Pa。质量取零得到准静态平衡，刚度、张力及内聚力取零得到自由面加速度。大斜率、拉伸、塑性、各向异性、有限厚度或接触需细化。所引静态基准与刚度形式一致，本推导保留惯性。<a href=\"https://ocw.mit.edu/courses/2-080j-structural-mechanics-fall-2013/resources/mit2_080jf13_lecture7/\" class=\"citation\">MIT 板基准</a>"))
add(P(
    "Step 6 — Include PVC mechanics. Give each sheet its own areal mass, stiffness and support. Transmitted traction acts oppositely on the sheets by Newton’s third law. Determine it through contact or bond closure. A fully bonded laminate additionally requires in-plane compatibility and composite stiffness.",
    "步骤 6——计入 PVC 力学。各片层具有独立面质量、刚度和支撑。根据牛顿第三定律，传递牵引在两片层上方向相反。须通过接触或粘接规律确定牵引。完全粘接叠层还需要面内相容性及复合刚度。"))
add(eq('C4-E07', r'\begin{aligned}m_{A,P}\ddot w_P+D_P\nabla_\parallel^4w_P-T_P\nabla_\parallel^2w_P&=p_{\rm liq}-t_{P\to f},\\m_A\ddot w+D_f\nabla_\parallel^4w-T_0\nabla_\parallel^2w&=t_{P\to f}-t_{\rm coh}.\end{aligned}',
    r'$w_P,w$ are PVC and film displacements in the same positive direction (m); double dots are accelerations (m s⁻²). $m_{A,P},m_A$ are their areal masses (kg m⁻²); $D_P,D_f$ their bending stiffnesses (N m); $T_P,T_0$ their prescribed pretensions (N m⁻¹). $\nabla_\parallel^2$ is the in-plane Laplacian and $\nabla_\parallel^4$ its square. $p_{\rm liq}$ is net liquid traction on PVC (Pa), $t_{P\to f}$ transmitted PVC-to-film traction projected positively (Pa), and $t_{\rm coh}$ film-release resistance (Pa). P labels PVC, f film, A areal, liq liquid and coh cohesion; the arrow labels the transmission direction. Each sheet has its actual initial and support conditions. No value of transmitted traction is supplied without an additional contact/bond closure.',
    r'$w_P,w$为PVC与薄膜沿同一正方向的位移（m）；双上点为加速度（m s⁻²）。$m_{A,P},m_A$为两者面密度（kg m⁻²）；$D_P,D_f$为弯曲刚度（N m）；$T_P,T_0$为给定预张力（N m⁻¹）。$\nabla_\parallel^2$为面内拉普拉斯算子，$\nabla_\parallel^4$为其平方。$p_{\rm liq}$为液体作用于PVC的净牵引（Pa），$t_{P\to f}$为沿正方向投影的PVC传向薄膜牵引（Pa），$t_{\rm coh}$为薄膜释放阻力（Pa）。P表示PVC，f表示薄膜，A表示面量，liq表示液体，coh表示内聚；箭头标识传递方向。每层均具有自身实际初始及支承条件。若无附加接触／粘接闭合关系，传递牵引就尚未确定。',
    'Conditional coupled-sheet model', 'film',
    ['p_liq → PVC', 'w_P, m_A,P, D_P, T_P — PVC response', 't_P→f → contact or bond', 'w, m_A, D_f, T₀ — film response', 't_coh → release interface'],
    ['No liquid passes through intact PVC.', 'Transmitted traction is an unknown, not a copied pressure.'],
    'The PVC-to-film load follows intermediate-sheet motion and contact.',
    'PVC传向薄膜的载荷由中间片层运动与接触决定。'))
add(P(
    "Step 7 — Integrate the film equation over the pulse. Retain restoring and cohesive impulses. A free velocity jump requires both small relative to applied impulse. A film bonded to rigid donor across the footprint fails that condition. Count resolved fluid inertia once.",
    "步骤 7——在脉冲期间积分薄膜方程，保留恢复力与内聚力冲量。自由速度跃变要求两者相对外加冲量较小。整个作用区粘接于刚性供体的薄膜不满足该条件。解析流体惯性计入一次。"))
add(eq('C4-E08', r'm_A[\dot w(\boldsymbol x,t_b)-\dot w(\boldsymbol x,t_a)]=J_A-\int_{t_a}^{t_b}[D_f\nabla_\parallel^4w-T_0\nabla_\parallel^2w+t_{\rm coh}]\,dt,\qquad J_A=\int_{t_a}^{t_b}p_{\rm load}\,dt',
    r'$m_A$ is film areal mass (kg m⁻²), $w(\boldsymbol x,t)$ vertical displacement (m), $\boldsymbol x$ in-plane position (m), and $\dot w$ velocity (m s⁻¹). $t_a,t_b,t,dt$ are pulse endpoints, integration time and time element (s). $J_A$ is local applied impulse per area (Pa s), $p_{\rm load}$ net applied traction (Pa), $t_{\rm coh}$ cohesive resistance (Pa), $D_f$ bending stiffness (N m), and $T_0$ pretension (N m⁻¹). $\nabla_\parallel^2$ and $\nabla_\parallel^4$ are the in-plane Laplacian and its square. $\int$ integrates the actual local load/response during the pulse. Labels A, f, load and coh mean areal, film, applied and cohesive.',
    r'$m_A$为薄膜面密度（kg m⁻²），$w(\boldsymbol x,t)$为竖直位移（m），$\boldsymbol x$为面内位置（m），$\dot w$为速度（m s⁻¹）。$t_a,t_b,t,dt$分别为脉冲起止时刻、积分时间及时间微元（s）。$J_A$为局部单位面积外加冲量（Pa s），$p_{\rm load}$为净外加牵引（Pa），$t_{\rm coh}$为内聚阻力（Pa），$D_f$为弯曲刚度（N m），$T_0$为预张力（N m⁻¹）。$\nabla_\parallel^2$与$\nabla_\parallel^4$为面内拉普拉斯算子及其平方。$\int$表示对脉冲期间实际局部载荷／响应积分。标签A、f、load、coh分别表示面量、薄膜、外加及内聚。',
    'Exact time integral within the reduced plate model', 'impulse',
    ['t_a → t_b — pulse interval', 'p_load(t) → J_A', 'm_A → velocity change', 'ẇ(x,t_a), ẇ(x,t_b)', 'D_f∇⁴w, −T₀∇²w, t_coh — reaction impulses'],
    ['Applied impulse and reaction impulse both enter.'],
    'Pulse integration exposes the reactions that can invalidate a free velocity jump.',
    '脉冲积分明确显示哪些反作用冲量会使自由速度跃变失效。'))
add(eq('C4-E09', r'\Delta\dot w\simeq\frac{J_A}{m_A},\qquad \mathcal E_A\simeq\frac12m_A(\Delta\dot w)^2=\frac{J_A^2}{2m_A}',
    r'$\Delta\dot w$ is the film velocity change from rest (m s⁻¹); $\Delta$ denotes final-minus-initial difference, and a dot is a time derivative. $J_A$ is local applied impulse per area (Pa s), $m_A>0$ film areal mass (kg m⁻²), and $\mathcal E_A$ resulting kinetic energy per area (J m⁻²). $\simeq$ marks negligible restoring/cohesive impulse during the pulse, not guaranteed transmission through an adhered stack. Subscript A labels quantities per area.',
    r'$\Delta\dot w$为薄膜从静止开始的速度变化（m s⁻¹）；$\Delta$表示终值减初值，上点为时间导数。$J_A$为局部单位面积外加冲量（Pa s），$m_A>0$为薄膜面密度（kg m⁻²），$\mathcal E_A$为所得单位面积动能（J m⁻²）。$\simeq$表示脉冲期间恢复力／内聚力冲量可忽略，而非保证粘接叠层中的载荷传递。下标A表示单位面积量。',
    'Short-pulse free-response approximation', 'film',
    ['J_A ↑ pulse impulse', 'm_A — areal mass', 'Δẇ ↑ initial response', 'E_A — motion energy per area'],
    ['Reaction impulses must be negligible.'],
    'Impulse creates film kinetic energy that may subsequently feed deformation and fracture.',
    '冲量产生薄膜动能，之后才可能转入变形与断裂。'))
add(P(
    "Balance inertia with bending and tension over the deformation length. Compare the resulting response times with pulse duration. Small-opening cohesive stiffness gives a third time. Slow duration alone leaves equilibrium unresolved when pulse edges or crack growth are rapid.",
    "在变形长度上分别平衡惯性与弯曲、张力。比较所得响应时间与脉冲时长。小张开内聚刚度给出第三种时间。脉冲边缘或裂纹增长快速时，单凭长时长仍未确立平衡。"))
add(eq('C4-E10', r't_b^{\rm scale}=a_f^2\sqrt{\frac{m_A}{D_f}},\qquad t_T^{\rm scale}=a_f\sqrt{\frac{m_A}{T_0}},\qquad t_n^{\rm scale}=\sqrt{\frac{m_A}{K_n}}',
    r'$t_b^{\rm scale},t_T^{\rm scale},t_n^{\rm scale}$ are bending, pretension and normal-cohesion response scales (s), not exact modal periods; superscript scale labels estimates and subscripts b, T, n identify the restoring mechanisms. $a_f>0$ is lateral deformation length (m), $m_A>0$ areal mass (kg m⁻²), $D_f>0$ bending stiffness (N m), $T_0>0$ pretension (N m⁻¹), and $K_n>0$ small-opening normal cohesive stiffness (Pa m⁻¹). $\sqrt{\ }$ is the positive root. If pretension or cohesion is absent, its corresponding timescale is omitted rather than divided by zero.',
    r'$t_b^{\rm scale},t_T^{\rm scale},t_n^{\rm scale}$分别为弯曲、预张力及法向内聚响应尺度（s），而非精确模态周期；上标scale表示估计，下标b、T、n标识恢复机制。$a_f>0$为横向变形长度（m），$m_A>0$为面密度（kg m⁻²），$D_f>0$为弯曲刚度（N m），$T_0>0$为预张力（N m⁻¹），$K_n>0$为小张开法向内聚刚度（Pa m⁻¹）。$\sqrt{\ }$取正根。若预张力或内聚机制不存在，则不使用对应时间尺度，不能除以零。',
    'Derived term-balance estimates', 'timescale',
    ['a_f — lateral deformation length', 'm_A — inertia', 'D_f → t_b,scale', 'T₀ → t_T,scale', 'K_n → t_n,scale', 'pulse duration → compare response times'],
    ['PVC also has a finite through-thickness wave time.'],
    'Pulse duration must be compared with the response scales of the actual load path.',
    '脉冲持续时间须与实际传力路径的响应尺度比较。'))

add(H("4. Interface strength and fracture work", "4. 界面强度与断裂功", 'fracture'))
add(P(
    "Step 8 — Specify loading control before crack driving force. Peak tensile traction is local strength in Pa. Reversible adhesion work is a surface-energy difference. Practical fracture energy includes dissipation and has units J m⁻². For quasistatic conservative mechanics, differentiate potential by crack area at fixed source control. Mode mixture, temperature and crack speed can change resistance.",
    "步骤 8——计算裂纹驱动力前规定加载控制。峰值拉伸牵引是 Pa 单位局部强度。可逆粘附功是表面能差。实际断裂能包含耗散，单位为 J m⁻²。准静态保守力学中，在固定源控制下对裂纹面积求势能导数。模态混合、温度及裂纹速度可改变阻力。"))
add(eq('C4-E11', r'G=-\left.\frac{\partial\mathcal P}{\partial A_c}\right|_{\mathcal C},\qquad G\ge\Gamma(\psi,T_i,v_c)',
    r'$G$ is quasistatic energy-release rate (J m⁻²), $\mathcal P$ total mechanical potential including the external loading system (J), $A_c$ crack area (m²), and $\partial/\partial A_c$ a partial derivative. $\mathcal C$ labels the held loading control, such as pressure or displacement; it is not a material coefficient. $\Gamma$ is fracture resistance (J m⁻²), $\psi$ mode-mixture parameter (dimensionless), $T_i$ interface temperature (K), and $v_c$ crack-front speed (m s⁻¹). Subscripts c and i label crack and interface. The inequality is an energetic propagation criterion for the specified fracture model, not a sufficient transfer criterion.',
    r'$G$为准静态能量释放率（J m⁻²），$\mathcal P$为包含外部加载系统的总力学势能（J），$A_c$为裂纹面积（m²），$\partial/\partial A_c$为偏导数。$\mathcal C$标识保持不变的加载控制量，例如压力或位移，而非材料系数。$\Gamma$为断裂阻力（J m⁻²），$\psi$为模态混合参数（无量纲），$T_i$为界面温度（K），$v_c$为裂纹前沿速度（m s⁻¹）。下标c与i表示裂纹及界面。此不等式是指定断裂模型的能量扩展判据，而非充分转印判据。',
    'Definition with quasistatic fracture criterion', 'film',
    ['A_c → advancing release area', 'G → available energy per new area', 'Γ(ψ,T_i,v_c) → resistance', 'P — system potential', 'C — held source control'],
    ['Strength has units Pa; fracture resistance has units J/m².'],
    'A crack is driven by energy per newly separated area, under a specified load control.',
    '裂纹由每单位新分离面积的可用能量驱动，且加载控制必须明确。'))
add(P(
    "Comparing pressure with fracture energy requires a deformation length and mechanical law. Competing paths include intended release, another bond’s failure and payload tearing. Feng et al. show how interface kinetics alter path competition. Measure rate and temperature dependence for the actual PFC stack. Their PDMS values require separate justification before reuse. "+cite('r10'),
    "压力与断裂能比较需要变形长度及力学规律。竞争路径包括目标释放、其他粘接失效及载荷撕裂。Feng 等说明界面动力学如何改变路径竞争。实际 PFC 叠层须测量速率及温度依赖性。复用其 PDMS 数值需要独立依据。 "+cite('r10')))
add(P(
    "Retain kinetic energy during rapid fracture. The chosen crack-front balance includes elastic storage, inertia, fracture consumption and other loss. Count cohesive dissipation once through the selected fracture energy. Crack path still requires structural and interface equations.",
    "快速断裂时保留动能。所选裂纹前沿平衡包括弹性储存、惯性、断裂消耗及其他损失。所选断裂能中的内聚耗散计入一次。裂纹路径仍需结构与界面方程。"))
add(eq('C4-E12', r'P_{\rm load}=\frac{d}{dt}(K_f+U_f)+\int_{\mathcal L_c}\Gamma(\psi,T_i,v_c)v_c\,d\ell+P_{\rm other}',
    r'$P_{\rm load}$ is mechanical power delivered to the solid (W), $K_f$ its kinetic energy (J), $U_f$ its recoverable elastic energy including any recoverable interface energy (J), and $d/dt$ the time derivative with $t$ in s. $\mathcal L_c$ is the active crack-front line; $d\ell$ is its arc-length element (m). $v_c\ge0$ is front speed (m s⁻¹), $\Gamma$ fracture energy (J m⁻²), $\psi$ dimensionless mode mixture, and $T_i$ interface temperature (K). $P_{\rm other}\ge0$ is additional nonfracture dissipation (W). $\int$ integrates along the front. Labels load, f, c, i and other denote applied, solid film, crack, interface and remaining dissipative processes.',
    r'$P_{\rm load}$为传入固体的力学功率（W），$K_f$为固体动能（J），$U_f$为可恢复弹性能，含任何可恢复界面能（J），$d/dt$为时间导数，$t$单位s。$\mathcal L_c$为活跃裂纹前沿曲线；$d\ell$为弧长微元（m）。$v_c\ge0$为前沿速度（m s⁻¹），$\Gamma$为断裂能（J m⁻²），$\psi$为无量纲模态混合参数，$T_i$为界面温度（K）。$P_{\rm other}\ge0$为其他非断裂耗散（W）。$\int$表示沿前沿积分。标签load、f、c、i、other分别表示外加、固体薄膜、裂纹、界面及其余耗散过程。',
    'Conditional dynamic energy balance', 'energy',
    ['P_load → solid power', 'K_f — motion storage', 'U_f — elastic storage', 'L_c, dℓ, v_c → new crack area/time', 'Γ(ψ,T_i,v_c) → fracture consumption', 'P_other → other losses'],
    ['Crack dissipation is counted once.'],
    'Dynamic loading can store kinetic energy before or during crack advance.',
    '动态载荷可在裂纹扩展前或扩展中储存动能。'))

add(H("5. Circular blister benchmark", "5. 圆形鼓泡基准", 'blister'))
add(P(
    "Step 9 — Define pressure-controlled delamination. A pre-existing circular crack lies beneath a thin isotropic plate. The bonded region clamps its edge. A reservoir maintains uniform positive pressure as radius varies. Omit inertia, pretension and stretching. Center displacement and curvature are regular without point force or singular moment. This benchmark has different loading from the transient jet array.",
    "步骤 9——定义压力控制脱层。薄各向同性板下已有圆形裂纹，粘接外区夹持其边缘。半径变化时，储库维持均匀正压差。忽略惯性、预张力及拉伸。中心无点力或奇异弯矩，位移和曲率正则。该基准加载不同于瞬态射流阵列。"))
add(eq('C4-E13', r'\mathscr L_rg=\frac{p_0}{D_f},\qquad g=\mathscr L_rw,\qquad \mathscr L_r f=\frac1r\frac{d}{dr}\left(r\frac{df}{dr}\right),\qquad w(b)=0,\quad w^{\prime}(b)=0',
    r'$r\in[0,b]$ is radius in the plate plane (m), $b>0$ delamination radius (m), $w(r)$ opening displacement (m), $p_0>0$ externally maintained pressure difference (Pa), and $D_f>0$ bending stiffness (N m). $\mathscr L_r$ is the axisymmetric planar Laplacian (m⁻²); $f$ is an arbitrary smooth radial function, and $g=\mathscr L_rw$ has units m⁻¹. $d/dr$ and a prime denote radial differentiation; the operator at $r=0$ is its regular limit. Labels r, f and 0 denote radial operator, film/arbitrary function according to context, and maintained load. The two zero values prescribe edge displacement and slope.',
    r'$r\in[0,b]$为板平面内半径（m），$b>0$为脱层半径（m），$w(r)$为张开位移（m），$p_0>0$为外部保持的压差（Pa），$D_f>0$为弯曲刚度（N m）。$\mathscr L_r$为轴对称平面拉普拉斯算子（m⁻²）；$f$为任意光滑径向函数，$g=\mathscr L_rw$的单位为m⁻¹。$d/dr$及撇号表示径向求导；$r=0$处算子取正则极限。标签r、f、0分别表示径向算子、薄膜／任意函数（依语境）及恒定载荷。两个零值指定边缘位移与斜率。',
    'Quasistatic plate boundary-value model', 'film',
    ['r = 0 — regular centre', 'r = b — clamped crack front', 'p₀ ↑ uniform maintained pressure', 'D_f — plate stiffness', 'w(r) ↑ opening', 'g = L_r w — curvature sum', 'f — radial test function'],
    ['No point force at the centre.', 'External pressure remains fixed as b changes.'],
    'Uniform pressure loads a clamped circular delamination with regular central fields.',
    '均匀压力作用于边缘夹持的圆形脱层，中心场必须正则。'))
add(P(
    "Step 10 — Solve the curvature sum. Multiply its radial Laplacian equation by radius and integrate. Divide by radius away from the center. Regular curvature gradient excludes the inverse-radius term. Integrate again for the constant curvature offset. The edge slope will determine it.",
    "步骤 10——求曲率和。将径向拉普拉斯方程乘半径并积分。中心之外除以半径。曲率梯度正则性排除半径反比项。再次积分得到常曲率偏置，随后由边缘斜率确定。"))
add(eq('C4-E14', r'\begin{aligned}\frac{d}{dr}(rg^{\prime})&=\frac{p_0r}{D_f},\\rg^{\prime}&=\frac{p_0r^2}{2D_f}+C_1,\\g^{\prime}&=\frac{p_0r}{2D_f}+\frac{C_1}{r},\quad C_1=0,\\g(r)&=\frac{p_0r^2}{4D_f}+C_2.\end{aligned}',
    r'$r\in(0,b]$ is radial coordinate (m); $b$ is delamination radius (m). $g(r)=\mathscr L_rw$ is the curvature sum (m⁻¹), with a prime and $d/dr$ denoting radial differentiation. $p_0$ is maintained pressure difference (Pa); $D_f$ bending stiffness (N m). $C_1,C_2$ are integration constants with units m⁻¹. $C_1=0$ follows from regular central curvature gradient and absence of a point load. $\mathscr L_r$ is the radial Laplacian, $w$ displacement (m); the subscript 0 labels the maintained pressure, not the initial liquid pressure.',
    r'$r\in(0,b]$为径向坐标（m）；$b$为脱层半径（m）。$g(r)=\mathscr L_rw$为曲率和（m⁻¹），撇号及$d/dr$表示径向求导。$p_0$为恒定压差（Pa）；$D_f$为弯曲刚度（N m）。$C_1,C_2$为单位m⁻¹的积分常数。$C_1=0$来自中心曲率梯度正则及无点载荷条件。$\mathscr L_r$为径向拉普拉斯算子，$w$为位移（m）；下标0标识恒定压力，而非液体初始压力。',
    'Derived first two radial integrations', 'film',
    ['p₀ → curvature forcing', 'D_f — resistance', 'r, b — radial domain', 'g(r), g′ — curvature fields', 'C₁ = 0 — centre regularity', 'C₂ — remaining curvature offset'],
    ['An inverse-radius curvature gradient is rejected at the centre.'],
    'Regularity removes the singular integration constant before edge conditions are used.',
    '在使用边缘条件之前，正则性先排除奇异积分常数。'))
add(P(
    "Step 11 — Integrate curvature to displacement. Center regularity removes the inverse-radius slope. Integration leaves quartic, quadratic and constant terms. Zero edge slope fixes curvature offset. Zero edge displacement fixes the remaining constant.",
    "步骤 11——由曲率积分至位移。中心正则性消去半径反比斜率。积分留下四次、二次及常数项。边缘零斜率确定曲率偏置，边缘零位移确定剩余常数。"))
add(eq('C4-E15', r'\begin{aligned}\frac{d}{dr}(rw^{\prime})&=rg=\frac{p_0r^3}{4D_f}+C_2r,\\rw^{\prime}&=\frac{p_0r^4}{16D_f}+\frac{C_2r^2}{2}+C_3,\quad C_3=0,\\w^{\prime}&=\frac{p_0r^3}{16D_f}+\frac{C_2r}{2},\\w(r)&=\frac{p_0r^4}{64D_f}+\frac{C_2r^2}{4}+C_4.\end{aligned}',
    r'$r\in(0,b]$ is radial position (m), $b$ delamination radius (m), $w$ displacement (m), and $g$ curvature sum (m⁻¹). A prime and $d/dr$ are radial derivatives; $w^{\prime}$ is dimensionless slope. $p_0$ is maintained pressure (Pa), $D_f$ bending stiffness (N m), $C_2$ curvature integration constant (m⁻¹), and $C_3,C_4$ displacement integration constants (m). $C_3=0$ excludes a central inverse-radius slope. All rows are regular-limit solutions at the centre. Subscripts 2,3,4 index distinct constants, not derivative orders.',
    r'$r\in(0,b]$为径向位置（m），$b$为脱层半径（m），$w$为位移（m），$g$为曲率和（m⁻¹）。撇号及$d/dr$为径向导数；$w^{\prime}$为无量纲斜率。$p_0$为恒定压力（Pa），$D_f$为弯曲刚度（N m），$C_2$为曲率积分常数（m⁻¹），$C_3,C_4$为位移积分常数（m）。$C_3=0$排除中心反比于半径的斜率。各行在中心均取正则极限。下标2、3、4标识不同常数，而非导数阶数。',
    'Derived second pair of radial integrations', 'film',
    ['r, b — radial geometry', 'w(r), w′ — displacement and slope', 'g — curvature sum', 'p₀, D_f — forcing and stiffness', 'C₂ — curvature offset', 'C₃ = 0 — regular slope', 'C₄ — height offset'],
    ['The centre carries no singular force.'],
    'The regular displacement contains quartic, quadratic and constant contributions.',
    '正则位移含四次项、二次项与常数项。'))
add(eq('C4-E16', r'\begin{aligned}0=w^{\prime}(b)&=\frac{p_0b^3}{16D_f}+\frac{C_2b}{2}\quad\Rightarrow\quad C_2=-\frac{p_0b^2}{8D_f},\\0=w(b)&=\frac{p_0b^4}{64D_f}-\frac{p_0b^4}{32D_f}+C_4\quad\Rightarrow\quad C_4=\frac{p_0b^4}{64D_f},\\w(r)&=\frac{p_0}{64D_f}(r^4-2b^2r^2+b^4)=\frac{p_0}{64D_f}(b^2-r^2)^2.\end{aligned}',
    r'$w(r)$ is displacement (m), $w^{\prime}$ radial slope, $r\in[0,b]$ radial position (m), and $b>0$ delamination radius (m), allowing division by $b$. $p_0>0$ is maintained pressure (Pa), $D_f>0$ bending stiffness (N m), $C_2$ curvature constant (m⁻¹), and $C_4$ displacement constant (m). The prime denotes $d/dr$; $\Rightarrow$ denotes the algebraic consequence of each clamped boundary condition. Subscripts 2 and 4 label constants, and f labels film.',
    r'$w(r)$为位移（m），$w^{\prime}$为径向斜率，$r\in[0,b]$为径向位置（m），$b>0$为脱层半径（m），因此可以除以$b$。$p_0>0$为恒定压力（Pa），$D_f>0$为弯曲刚度（N m），$C_2$为曲率常数（m⁻¹），$C_4$为位移常数（m）。撇号表示$d/dr$；$\Rightarrow$表示各夹持边界条件的代数结果。下标2与4标识常数，f表示薄膜。',
    'Exact solution of the stated linear-plate benchmark', 'film',
    ['r = 0 → w_max', 'r = b → w = 0, slope = 0', 'p₀ ↑ held pressure', 'D_f — bending resistance', 'C₂, C₄ — boundary-fixed constants', 'w(r) — quartic profile'],
    ['The bonded outside region supplies the clamp.'],
    'Applying both edge conditions fixes the unique regular blister profile.',
    '同时应用两个边缘条件，确定唯一正则鼓泡轮廓。'))
add(P(
    "Step 12 — Substitute the solution to check it. Radial Laplacian of radius² is four. That of radius⁴ is sixteen × radius². Applying twice gives sixty-four. Edge displacement and slope vanish. Positive pressure opens the center; larger stiffness reduces opening. Units are Pa × m⁴/(N m) = m. MIT Lecture 7, Eq. 7.24 gives the same clamped-circle solution.",
    "步骤 12——代回解进行检验。半径²的径向拉普拉斯为四，半径⁴的结果为十六 × 半径²，作用两次得六十四。边缘位移和斜率为零。正压使中心张开，刚度增大使张开减小。单位为 Pa × m⁴／（N m）= m。MIT 第 7 讲式 7.24 给出相同夹持圆板解。"))
add(eq('C4-E17', r'\mathscr L_r(r^2)=4,\qquad \mathscr L_r(r^4)=16r^2,\qquad D_f\mathscr L_r^2w=p_0,\qquad w^{\prime}(r)=\frac{p_0r(r^2-b^2)}{16D_f}',
    r'$\mathscr L_r$ is the radial planar Laplacian (m⁻²), and superscript 2 on the operator means composition twice; superscripts on $r$ are powers. $r$ is radial position (m), $b$ delamination radius (m), $w$ blister displacement (m), and its prime is radial slope. $D_f$ is bending stiffness (N m); $p_0$ maintained pressure (Pa). Literal 4 and 16 are numerical coefficients; $\mathscr L_r(r^2)$ is dimensionless and $\mathscr L_r(r^4)$ has units m². The slope expression vanishes at $r=0$ and $r=b$.',
    r'$\mathscr L_r$为径向平面拉普拉斯算子（m⁻²），算子上的上标2表示连续作用两次；$r$上的上标表示幂。$r$为径向位置（m），$b$为脱层半径（m），$w$为鼓泡位移（m），其撇号为径向斜率。$D_f$为弯曲刚度（N m）；$p_0$为恒定压力（Pa）。数字4与16是数值系数；$\mathscr L_r(r^2)$无量纲，$\mathscr L_r(r^4)$单位为m²。斜率式在$r=0$及$r=b$均为零。',
    'Governing-equation and boundary verification', 'film',
    ['r — radial coordinate', 'b — crack edge', 'w, w′ — opening and slope', 'D_f L_r²w = p₀ — equation residual', 'r = 0 and b → zero slope'],
    ['L_r r² = 4', 'L_r r⁴ = 16r²'],
    'Direct radial differentiation verifies the pressure balance and regular clamped profile.',
    '直接径向求导可检验压力平衡及正则夹持轮廓。'))
add(P(
    "Step 13 — Integrate opening for cavity volume. The axisymmetric area element includes radius × radial increment. Expand the profile square and integrate each power. Evaluate both limits. The first two endpoint terms cancel, leaving the sixth-power term.",
    "步骤 13——积分张开位移求空腔体积。轴对称面积微元包含半径 × 径向增量。展开轮廓平方并积分各幂。计算上下限，前两端点项相消，留下六次幂项。"))
add(eq('C4-E18', r'\begin{aligned}V_{\rm bl}&=2\pi\int_0^b w(r)r\,dr=\frac{\pi p_0}{32D_f}\int_0^b(b^4r-2b^2r^3+r^5)\,dr,\\&=\frac{\pi p_0}{32D_f}\left[\frac{b^4r^2}{2}-\frac{b^2r^4}{2}+\frac{r^6}{6}\right]_0^b=\frac{\pi p_0b^6}{192D_f}.\end{aligned}',
    r'$V_{\rm bl}$ is added blister volume (m³), $w(r)$ displacement (m), $r\in[0,b]$ radial integration coordinate (m), $dr$ its integration element (m), and $b$ delamination radius (m). $p_0$ is maintained pressure (Pa); $D_f$ bending stiffness (N m); $\pi$ the dimensionless circle constant. $\int$ is radial integration, and $[\ ]_0^b$ denotes antiderivative at the upper endpoint minus its value at zero. Subscript bl labels the blister; superscripts on lengths are powers.',
    r'$V_{\rm bl}$为新增鼓泡体积（m³），$w(r)$为位移（m），$r\in[0,b]$为径向积分坐标（m），$dr$为积分微元（m），$b$为脱层半径（m）。$p_0$为恒定压力（Pa）；$D_f$为弯曲刚度（N m）；$\pi$为无量纲圆周率。$\int$表示径向积分，$[\ ]_0^b$表示原函数在上端点的值减去其零端点值。下标bl表示鼓泡；长度上的上标均表示幂。',
    'Exact geometric volume integral for the benchmark', 'film',
    ['V_bl — volume below lifted plate', 'w(r) ↑ local opening', 'r dr → annular area weight', 'b — circular crack edge', 'p₀, D_f — compliance inputs'],
    ['Every annulus contributes its own displacement.'],
    'Blister volume sums the opening of all concentric annuli.',
    '鼓泡体积等于各同心圆环张开贡献之和。'))
add(P(
    "Step 14 — Include reservoir work in potential. At fixed crack radius, volume is linear in pressure. Elastic storage is half pressure × volume. Reservoir potential is minus pressure × volume. Their sum is minus the half-product. Omitting reservoir work reverses the pressure-controlled driving-force sign.",
    "步骤 14——在势能中计入储库功。裂纹半径固定时，体积随压力线性变化。弹性储存为压力 × 体积的一半，储库势能为压力 × 体积的负值。总和为负半积。省略储库功会反转压力控制驱动力符号。"))
add(eq('C4-E19', r'C_b=\left.\frac{\partial V_{\rm bl}}{\partial p_0}\right|_b=\frac{\pi b^6}{192D_f},\qquad V_{\rm bl}=C_bp_0,\qquad U_b=\int_0^{V_{\rm bl}}\frac{v}{C_b}\,dv=\frac{V_{\rm bl}^2}{2C_b}=\frac{p_0V_{\rm bl}}2,\qquad \mathcal P=U_b-p_0V_{\rm bl}=-\frac{\pi p_0^2b^6}{384D_f}',
    r'$C_b>0$ is blister volume compliance (m³ Pa⁻¹), defined by the pressure derivative at fixed radius, including the regular zero-load value. $V_{\rm bl}\ge0$ is added volume (m³), $p_0\ge0$ maintained pressure (Pa), $b>0$ crack radius (m), and $D_f>0$ bending stiffness (N m). $\partial/\partial p_0$ is the pressure derivative; the vertical bar holds radius fixed. $U_b$ is stored plate bending energy (J), $\mathcal P$ plate-plus-pressure-reservoir potential (J), and $v$ a dummy volume along the fixed-radius elastic loading curve (m³), with $dv$ its element (m³). $\int$ integrates that loading curve. Subscripts b and bl label blister compliance/bending and blister volume, respectively; the meanings are explicitly fixed here. No crack-area variation is taken during the loading-curve integral. For positive pressure, compliance also equals volume divided by pressure; at zero pressure the derivative avoids division by zero.',
    r'$C_b>0$为鼓泡体积柔度（m³ Pa⁻¹），由固定半径下的压力导数定义，包含正则零载荷值。$V_{\rm bl}\ge0$为新增体积（m³），$p_0\ge0$为恒定压力（Pa），$b>0$为裂纹半径（m），$D_f>0$为弯曲刚度（N m）。$\partial/\partial p_0$为压力导数；竖线表示保持半径不变。$U_b$为板弯曲储能（J），$\mathcal P$为板与恒压储库的总势能（J），$v$为固定半径弹性加载曲线上的虚拟体积变量（m³），$dv$为其微元（m³）。$\int$表示该加载曲线积分。下标b与bl分别表示鼓泡柔度／弯曲及鼓泡体积，此处已明确其含义。在加载曲线积分过程中不改变裂纹面积。正压力时，柔度也等于体积除以压力；零压力时采用导数避免除以零。',
    'Derived potential under maintained-pressure control', 'energy',
    ['p₀ — maintained source pressure', 'V_bl, v — cavity volume', 'C_b — volume compliance', 'U_b = ½p₀V_bl — plate storage', '−p₀V_bl — source potential', 'P = U_b − p₀V_bl', 'b, D_f — geometry and stiffness'],
    ['The external pressure reservoir supplies work as the crack grows.'],
    'Source work changes the sign of the relevant total potential.',
    '压力源做功改变相关总势能的符号。'))
add(P(
    "Step 15 — Differentiate potential by crack radius. Divide by the area derivative, retaining numerical factors. Positive pressure gives positive release rate. Growing compliance lowers plate-plus-reservoir potential. Doubling radius at fixed pressure multiplies driving force by sixteen.",
    "步骤 15——对裂纹半径求势能导数，再除以面积导数，并保留数值系数。正压给出正能量释放率。柔顺性增加降低板与储库总势能。压力固定时，半径加倍使驱动力增至十六倍。"))
add(eq('C4-E20', r'\begin{aligned}A_c&=\pi b^2,\qquad \left.\frac{d\mathcal P}{db}\right|_{p_0}=-\frac{6\pi p_0^2b^5}{384D_f},\qquad\frac{dA_c}{db}=2\pi b,\\G_{p_0}&=-\frac{(d\mathcal P/db)_{p_0}}{dA_c/db}=\frac{p_0^2b^4}{128D_f}.\end{aligned}',
    r'$A_c$ is delaminated area (m²), $b>0$ its radius (m), $\pi$ the circle constant, $\mathcal P$ total potential including maintained pressure (J), $p_0$ fixed pressure difference (Pa), and $D_f$ bending stiffness (N m). $d/db$ differentiates in radius; the vertical bar and subscript $p_0$ indicate held pressure. $G_{p_0}$ is energy-release rate under that control (J m⁻²). Subscript c labels crack area; all length superscripts are powers. Positive $b$ makes the area derivative nonzero.',
    r'$A_c$为脱层面积（m²），$b>0$为其半径（m），$\pi$为圆周率，$\mathcal P$为包含恒压源的总势能（J），$p_0$为固定压差（Pa），$D_f$为弯曲刚度（N m）。$d/db$表示按半径求导；竖线及下标$p_0$表示保持压力不变。$G_{p_0}$为该控制方式下的能量释放率（J m⁻²）。下标c表示裂纹面积；长度上的上标均为幂。$b$为正保证面积导数非零。',
    'Derived quasistatic energy-release rate', 'film',
    ['b → moving circular crack edge', 'A_c = πb² → released area', 'p₀ — fixed load', 'D_f — plate stiffness', 'P → differentiable system potential', 'G_p₀ → energy per new area'],
    ['The derivative is taken at fixed pressure.'],
    'Geometry and compliance convert pressure into fracture energy per area.',
    '几何与柔度将压力转换为单位面积断裂能。'))
add(eq('C4-E21', r'p_{0,\rm crit}=\frac{\sqrt{128D_f\Gamma}}{b^2},\qquad \frac{G_{p_0}}{\Gamma}=\left(\frac{p_0}{p_{0,\rm crit}}\right)^2',
    r'$p_{0,\rm crit}>0$ is critical maintained pressure (Pa) for constant fracture resistance $\Gamma>0$ (J m⁻²); $D_f>0$ is bending stiffness (N m), $b>0$ delamination radius (m), $p_0\ge0$ applied maintained pressure (Pa), and $G_{p_0}$ the corresponding energy-release rate (J m⁻²). $\sqrt{\ }$ is the positive root; subscript crit labels the onset threshold. The quotient $G_{p_0}/\Gamma$ is dimensionless. This onset criterion assumes an existing crack and the quasistatic bending model.',
    r'$p_{0,\rm crit}>0$为恒定断裂阻力$\Gamma>0$（J m⁻²）对应的临界恒压（Pa）；$D_f>0$为弯曲刚度（N m），$b>0$为脱层半径（m），$p_0\ge0$为外加恒压（Pa），$G_{p_0}$为相应能量释放率（J m⁻²）。$\sqrt{\ }$取正根；下标crit表示起始阈值。比值$G_{p_0}/\Gamma$无量纲。此起始判据假设存在预裂纹，并采用准静态弯曲模型。',
    'Derived onset threshold within the benchmark', 'film',
    ['p₀ → pressure loading', 'p₀,crit → onset threshold', 'D_f, Γ → stiffness and fracture resistance', 'b → pre-existing crack size', 'G_p₀/Γ → propagation screen'],
    ['Larger existing delamination lowers critical pressure.'],
    'The pressure threshold depends on crack geometry and fracture resistance, not pressure alone.',
    '压力阈值取决于裂纹几何及断裂阻力，而非压力本身。'))
add(P(
    "Step 16 — Change to fixed volume. Remove continuing reservoir work and eliminate pressure through compliance. Differentiate plate storage at fixed volume. Reinsert instantaneous pressure for comparison. The same state gives the same instantaneous expression. Radius growth increases fixed-pressure driving and decreases fixed-volume driving. Constant resistance therefore gives different stability under these controls. A sealed PFC cavity has evolving mass and temperature. Its trajectory needs a thermodynamic closure.",
    "步骤 16——改为固定体积。取消持续储库功，通过柔顺性消去压力。在固定体积下对板储能求导，再代回瞬时压力进行比较。同一状态给出相同瞬时形式。半径增长使定压驱动增加、定容驱动减小。阻力恒定时，两类控制具有不同稳定性。密闭 PFC 空腔质量和温度会演化，其轨迹需要热力学闭合。"))
add(eq('C4-E22', r'\begin{aligned}U_b\big|_{\bar V}&=\frac{\bar V^2}{2C_b}=\frac{96D_f\bar V^2}{\pi b^6},\qquad p(b)=\frac{192D_f\bar V}{\pi b^6},\\G_{\bar V}&=-\frac{dU_b/db}{2\pi b}=\frac{288D_f\bar V^2}{\pi^2b^8}=\frac{p(b)^2b^4}{128D_f},\\G_{p_0}&\propto b^4\ \text{at fixed }p_0,\qquad G_{\bar V}\propto b^{-8}\ \text{at fixed }\bar V.\end{aligned}',
    r'$\bar V>0$ is imposed fixed added volume (m³), $U_b$ plate bending energy (J), $C_b$ volume compliance (m³ Pa⁻¹), $D_f$ bending stiffness (N m), $b>0$ crack radius (m), and $p(b)$ the pressure required at that radius (Pa). $G_{\bar V}$ and $G_{p_0}$ are energy-release rates under fixed volume and fixed pressure, respectively (J m⁻²); $p_0$ is maintained pressure (Pa). $d/db$ is radius differentiation holding $\bar V$ fixed, $\pi$ the circle constant, and $\propto$ means proportional at fixed other parameters. The bar labels controlled volume, not averaging. The fixed-volume system here supplies no additional pressure-source work.',
    r'$\bar V>0$为强制固定的新增体积（m³），$U_b$为板弯曲能（J），$C_b$为体积柔度（m³ Pa⁻¹），$D_f$为弯曲刚度（N m），$b>0$为裂纹半径（m），$p(b)$为该半径处所需压力（Pa）。$G_{\bar V}$与$G_{p_0}$分别为恒容及恒压控制下的能量释放率（J m⁻²）；$p_0$为恒定压力（Pa）。$d/db$表示保持$\bar V$不变的半径求导，$\pi$为圆周率，$\propto$表示其他参数固定时成正比。横线标识受控体积，而非平均。此恒容系统不再提供额外压力源功。',
    'Derived loading-control comparison', 'energy',
    ['V̄ — fixed added volume', 'b ↑ advancing crack', 'p(b) ↓ as compliance grows', 'C_b, D_f — elastic compliance', 'U_b — plate storage', 'G_V̄ ∝ b⁻⁸', 'G_p₀ ∝ b⁴ under fixed p₀'],
    ['Same instantaneous state does not imply the same crack trajectory.'],
    'Fixed pressure and fixed volume lead to opposite changes in driving force as the crack grows.',
    '裂纹扩展时，恒压与恒容控制使驱动力发生相反变化。'))
add(H("Blister calculation", "鼓泡计算", 'blister-calculation', 3))
add(P(
    "Prescribe modulus 2 GPa, thickness 10 μm, Poisson ratio 0.35, crack radius 100 μm and fracture energy 0.10 J m⁻². These source-course inputs describe the illustrative plate. They do not specify the later 1 μm payload or PVC formulation. Convert thickness to meters before cubing. Evaluate stiffness and the positive onset root.",
    "规定模量 2 GPa、厚度 10 μm、泊松比 0.35、裂纹半径 100 μm、断裂能 0.10 J m⁻²。这些源课程输入描述示例板，未指定后续 1 μm 载荷或 PVC 配方。厚度先换算为米再取三次方。计算刚度及正起始根。"))
add(eq('C4-E23', r'\begin{aligned}D_f&=\frac{(2.00\times10^9\ {\rm Pa})(10.0\times10^{-6}\ {\rm m})^3}{12(1-0.35^2)}=1.899335\times10^{-7}\ {\rm N\,m},\\p_{0,\rm crit}&=\frac{\sqrt{128(1.899335\times10^{-7}\ {\rm N\,m})(0.10\ {\rm J\,m^{-2}})}}{(100\times10^{-6}\ {\rm m})^2}=155.921\ {\rm kPa}.\end{aligned}',
    r'$D_f$ is film bending stiffness (N m) and $p_{0,\rm crit}$ the positive critical maintained pressure (Pa). The substituted teaching Young’s modulus is 2.00×10⁹ Pa, thickness 10.0×10⁻⁶ m, Poisson’s ratio 0.35, crack radius 100×10⁻⁶ m, and fracture resistance 0.10 J m⁻². Pa, N, m, J and kPa denote pascal, newton, metre, joule and kilopascal. $\sqrt{\ }$ is the positive root; superscripts are powers. Subscript f labels the film and crit the onset threshold.',
    r'$D_f$为薄膜弯曲刚度（N m），$p_{0,\rm crit}$为正临界恒压（Pa）。代入的教学杨氏模量为2.00×10⁹ Pa，厚度10.0×10⁻⁶ m，泊松比0.35，裂纹半径100×10⁻⁶ m，断裂阻力0.10 J m⁻²。Pa、N、m、J及kPa分别为帕、牛顿、米、焦耳及千帕。$\sqrt{\ }$取正根；上标表示幂。下标f表示薄膜，crit表示起始阈值。',
    'Checked teaching substitution', 'film',
    ['h_f = 10 μm — plate thickness', 'b = 100 μm — existing crack', 'E_f = 2 GPa, ν_f = 0.35', 'D_f = 1.8993×10⁻⁷ N m', 'Γ = 0.10 J/m²', 'p₀,crit = 155.921 kPa'],
    ['This is not the 1 μm array-loaded payload.'],
    'The stated plate and interface yield a conditional 156 kPa maintained-pressure threshold.',
    '所给薄板与界面产生约156 kPa的条件性恒压阈值。'))
add(P(
    "Check opening, volume and stress at onset. Edge moment magnitude is pressure × radius²/8. Outer-surface bending stress is six × moment/thickness². The hypothetical plate reaches about 11.7 MPa edge stress. Allowable strength is missing. Thickness/radius is 0.10. Finite-thickness error requires assessment before claiming accuracy.",
    "在起始点检查张开、体积及应力。边缘弯矩大小为压力 × 半径²／8，外表面弯曲应力为六 × 弯矩／厚度²。假想板边缘应力约 11.7 MPa。缺失允许强度。厚度／半径为 0.10，声称精度前须评估有限厚度误差。"))
add(eq('C4-E24', r'\begin{aligned}w(0)&=\frac{p_{0,\rm crit}b^4}{64D_f}=1.28270\ \mu{\rm m},\qquad \frac{w(0)}{h_f}=0.12827,\\V_{\rm bl}&=\frac{\pi p_{0,\rm crit}b^6}{192D_f}=1.34324\times10^{-14}\ {\rm m^3},\\|M_r(b)|&=\frac{p_{0,\rm crit}b^2}{8},\qquad |\sigma_{rr}|_{\rm edge}=\frac{6|M_r(b)|}{h_f^2}=11.6941\ {\rm MPa}.\end{aligned}',
    r'$w(0)$ is centre displacement (m), $h_f=10$ μm thickness (m), $b=100$ μm crack radius (m), $D_f=1.899335$×10⁻⁷ N m bending stiffness, and $p_{0,\rm crit}=155.921$ kPa maintained threshold. $V_{\rm bl}$ is blister volume (m³), $M_r(b)$ radial bending moment per edge length (N), and $\sigma_{rr}$ radial normal bending stress (Pa). Subscript edge labels its outer-surface value at the clamped edge; r labels radial direction. $|\ |$ denotes magnitude, $\pi$ the circle constant; μm and MPa are micrometre and megapascal. This stress result uses the same linear isotropic plate assumptions.',
    r'$w(0)$为中心位移（m），$h_f=10$ μm为厚度（m），$b=100$ μm为裂纹半径（m），$D_f=1.899335$×10⁻⁷ N m为弯曲刚度，$p_{0,\rm crit}=155.921$ kPa为恒压阈值。$V_{\rm bl}$为鼓泡体积（m³），$M_r(b)$为单位边长径向弯矩（N），$\sigma_{rr}$为径向法向弯曲应力（Pa）。下标edge表示夹持边缘厚度外表面的值；r表示径向。$|\ |$表示幅值，$\pi$为圆周率；μm与MPa分别为微米及兆帕。应力结果采用相同线性各向同性薄板假设。',
    'Magnitude, geometric-validity and competing-failure checks', 'film',
    ['w(0) = 1.283 μm — centre lift', 'h_f = 10 μm — thickness', 'b = 100 μm — clamp', 'V_bl = 13.4324 pL', 'p₀,crit, D_f — input state', 'M_r, σ_rr — edge bending', '|σ_rr| = 11.694 MPa'],
    ['Small deflection relative to thickness is checked.', 'Payload allowable strength is still missing.'],
    'A fracture threshold must be checked against deflection validity and payload bending stress.',
    '断裂阈值必须同时检验挠度适用性与对象弯曲应力。'))

add(H("6. Cohesive strength and separation work", "6. 内聚强度与分离功", 'cohesion'))
add(P(
    "Step 17 — Adopt triangular tensile traction–separation behavior. Initial slope sets opening stiffness, peak sets initiation strength, and final opening completes separation. This is a declared interface model. Compression needs contact closure. Unloading needs elastic recovery and damage history. Mixed modes need a coupling law.",
    "步骤 17——采用三角形拉伸牵引—分离规律。初始斜率规定张开刚度，峰值规定起始强度，最终张开完成分离。这是给定界面模型。压缩需要接触闭合，卸载需要弹性恢复和损伤历程，混合模态需要耦合规律。"))
add(eq('C4-E25', r'\delta_0=\frac{T_{\max}}{K_n},\qquad t_n(\delta)=\begin{cases}K_n\delta,&0\le\delta\le\delta_0,\\T_{\max}\dfrac{\delta_c-\delta}{\delta_c-\delta_0},&\delta_0<\delta<\delta_c,\\0,&\delta\ge\delta_c.\end{cases}',
    r'$\delta\ge0$ now denotes physical relative tensile opening (m), not variational notation. $t_n(\delta)$ is tensile cohesive traction magnitude (Pa), $K_n>0$ initial normal stiffness (Pa m⁻¹), $T_{\max}>0$ peak tensile traction (Pa), $\delta_0=T_{\max}/K_n$ peak-traction opening (m), and $\delta_c>\delta_0$ complete-separation opening (m). Subscripts n, 0 and c label normal, peak onset and final separation; max labels the maximum. The law assumes monotonically increasing opening and a strictly positive softening interval. Compression and unloading are not specified by this formula.',
    r'$\delta\ge0$此处表示物理相对拉伸张开（m），不再是变分符号。$t_n(\delta)$为拉伸内聚牵引幅值（Pa），$K_n>0$为初始法向刚度（Pa m⁻¹），$T_{\max}>0$为峰值拉伸牵引（Pa），$\delta_0=T_{\max}/K_n$为峰值牵引处张开（m），$\delta_c>\delta_0$为完全分离张开（m）。下标n、0、c分别表示法向、峰值起始及最终分离；max表示最大值。关系假设张开单调增大，且软化区间严格为正。此式未指定压缩与卸载行为。',
    'Adopted monotonic tensile cohesive law', 'cohesive',
    ['δ → interface opening', 't_n(δ) ↑ tensile resistance', 'K_n — initial curve slope', 'δ₀ → peak opening', 'T_max → peak traction', 'δ_c → complete separation'],
    ['Compression is a different branch.', 'Tensile damage must not be inferred from pressure magnitude.'],
    'The traction–separation curve contains strength, stiffness and a finite separation distance.',
    '牵引—分离曲线包含强度、刚度及有限分离距离。'))
add(P(
    "Step 18 — Integrate ascending and descending branches. Each contributes one triangle area. With admissible opening order, their sum depends on peak traction and final opening. Units are Pa m = J m⁻². Peak location still affects stiffness and initiation dynamics.",
    "步骤 18——积分上升与下降分支。每段贡献一个三角形面积。张开顺序允许时，总面积取决于峰值牵引及最终张开。单位为 Pa m = J m⁻²。峰值位置仍影响刚度及起始动力学。"))
add(eq('C4-E26', r'\begin{aligned}\Gamma&=\int_0^{\delta_c}t_n(\delta)\,d\delta\\&=\frac{K_n\delta_0^2}{2}+\frac{T_{\max}}{\delta_c-\delta_0}\left[\delta_c\delta-\frac{\delta^2}{2}\right]_{\delta_0}^{\delta_c}\\&=\frac{T_{\max}\delta_0}{2}+\frac{T_{\max}(\delta_c-\delta_0)}{2}=\frac{T_{\max}\delta_c}{2},\\\delta_c&=\frac{2\Gamma}{T_{\max}},\qquad K_n>\frac{T_{\max}^2}{2\Gamma}\quad\text{for }\delta_0<\delta_c.\end{aligned}',
    r'$\Gamma>0$ is the fracture energy of the adopted monotonic law (J m⁻²), $\delta$ tensile opening integration variable (m), and $d\delta$ its element (m). $t_n$ is tensile cohesive traction (Pa), $K_n>0$ initial stiffness (Pa m⁻¹), $T_{\max}>0$ peak traction (Pa), $\delta_0$ opening at the peak (m), and $\delta_c>\delta_0$ final separation opening (m). $\int$ integrates traction against opening; endpoint brackets mean upper minus lower value. Subscripts n, 0, c and max label normal, peak onset, final separation and maximum. The last inequality enforces a nonzero softening branch; it is a model-admissibility condition.',
    r'$\Gamma>0$为所采用单调关系的断裂能（J m⁻²），$\delta$为拉伸张开积分变量（m），$d\delta$为其微元（m）。$t_n$为拉伸内聚牵引（Pa），$K_n>0$为初始刚度（Pa m⁻¹），$T_{\max}>0$为峰值牵引（Pa），$\delta_0$为峰值处张开（m），$\delta_c>\delta_0$为最终分离张开（m）。$\int$表示牵引对张开的积分；端点方括号表示上端值减下端值。下标n、0、c、max分别表示法向、峰值起始、最终分离与最大值。末行不等式保证非零软化分支，是模型的可接受条件。',
    'Exact work integral of the adopted cohesive law', 'cohesive',
    ['t_n(δ) — tensile traction curve', 'δ, dδ — separation distance', 'δ₀, δ_c — branch endpoints', 'T_max — curve peak', 'K_n — ascending slope', 'Γ — full curve area'],
    ['Reaching the peak does not pay the entire curve area.'],
    'Complete separation needs the entire traction–opening area, not merely the peak value.',
    '完全分离需要完整牵引—张开曲线面积，而不仅仅达到峰值。'))
add(eq('C4-E27', r'\Gamma=0.005\ {\rm J\,m^{-2}},\quad T_{\max}=0.10\ {\rm MPa},\quad K_n=10^{13}\ {\rm Pa\,m^{-1}}\quad\Rightarrow\quad\delta_0=10\ {\rm nm},\quad\delta_c=100\ {\rm nm}',
    r'$\Gamma$ is assumed fracture energy (J m⁻²), $T_{\max}$ assumed peak tensile traction (Pa), $K_n$ assumed initial normal stiffness (Pa m⁻¹), $\delta_0$ peak-traction opening (m), and $\delta_c$ final tensile separation (m). MPa and nm denote megapascal and nanometre. $\Rightarrow$ denotes substitution into the triangular law. These are separate illustrative cohesive parameters, not measurements of the film release interface. Subscripts max, n, 0 and c identify peak, normal, peak opening and complete opening.',
    r'$\Gamma$为假设断裂能（J m⁻²），$T_{\max}$为假设峰值拉伸牵引（Pa），$K_n$为假设初始法向刚度（Pa m⁻¹），$\delta_0$为峰值牵引处张开（m），$\delta_c$为最终拉伸分离（m）。MPa与nm表示兆帕与纳米。$\Rightarrow$表示代入三角形关系。这些是独立内聚教学参数，而非薄膜释放界面的测量。下标max、n、0、c分别标识峰值、法向、峰值张开与完全张开。',
    'Cohesive admissibility teaching calculation', 'cohesive',
    ['T_max = 0.10 MPa — curve peak', 'K_n = 10¹³ Pa/m — initial slope', 'δ₀ = 10 nm', 'δ_c = 100 nm', 'Γ = 0.005 J/m² — curve area'],
    ['10 nm < 100 nm: the softening interval is admissible.'],
    'The example has distinct peak and final separation openings.',
    '本例具有不同的峰值张开与最终分离张开。'))

add(H("7. Array-to-film calculation", "7. 阵列至薄膜计算", 'array-release'))
add(P(
    "Step 19 — Carry forward the finite source. Chapter 2’s inventory feeds 25 independent Chapter 3 cells. Patterned/addressed illumination gives equal prescribed allocation. Total absorbed energy is 10 μJ. Declared jet conversion 0.005 gives 50 nJ kinetic energy. Each jet has density 1000 kg m⁻³, diameter 10 μm and length 50 μm. Recompute mass and momentum without rounded speed. Separate cells carry no interacting-bubble multiplier.",
    "步骤 19——继续使用有限源。第二章物质量供给第三章二十五个独立单元。图案／寻址照明给定相等分配。总吸收能量为 10 μJ，给定射流转换率 0.005 得到 50 nJ 动能。各射流密度 1000 kg m⁻³、直径 10 μm、长度 50 μm。用未舍入速率重算质量和动量。独立单元不采用相互作用倍数。"))
add(eq('C4-E28', r'\begin{aligned}m_j&=\frac{\rho\pi d_j^2L_j}{4}=3.926990817\times10^{-12}\ {\rm kg},\\U_j&=\sqrt{\frac{2E_j}{m_j}}=31.9153824\ {\rm m\,s^{-1}},\\E_{\rm in}&=NE_j=50.0\ {\rm nJ},\qquad I_{\rm in}=Nm_jU_j=3.133285343\times10^{-9}\ {\rm N\,s}.\end{aligned}',
    r'$m_j$ is carrier mass in one uniform cylindrical jet (kg), $\rho=1000$ kg m⁻³ carrier density, $d_j=10$ μm jet diameter, $L_j=50$ μm jet length, and $\pi$ the circle constant. $E_j=2.00$ nJ is assigned kinetic energy per jet, $U_j$ its uniform speed (m s⁻¹), $N=25$ independent identically supplied jets, $E_{\rm in}$ total incoming kinetic energy (J), and $I_{\rm in}$ aligned incoming momentum (N s). $\sqrt{\ }$ is the positive root. Subscripts j and in label single jet and incoming array; nJ is nanojoule. Simultaneous aligned arrival is assumed for the directional sum, but pressure fields are not added as N times a peak.',
    r'$m_j$为单股均匀圆柱射流的载液质量（kg），$\rho=1000$ kg m⁻³为载液密度，$d_j=10$ μm为射流直径，$L_j=50$ μm为长度，$\pi$为圆周率。$E_j=2.00$ nJ为指定单射流动能，$U_j$为其均匀速度（m s⁻¹），$N=25$为独立且供给相同的射流数，$E_{\rm in}$为总入射动能（J），$I_{\rm in}$为同向入射动量（N s）。$\sqrt{\ }$取正根。下标j、in分别标识单射流与入射阵列；nJ为纳焦耳。方向求和假设同时同向到达，但不将压力场按N倍峰值相加。',
    'Finite incoming state inherited from the teaching source', 'jet',
    ['N = 25 — independent cells', 'd_j = 10 μm', 'L_j = 50 μm', 'ρ = 1000 kg/m³ → m_j', 'E_j = 2 nJ → U_j = 31.915 m/s', 'E_in = 50 nJ', 'I_in = 3.1333×10⁻⁹ N s'],
    ['Finite carrier mass, not PFC vapor mass.', 'No additional cluster amplification factor.'],
    'Finite jet energy and aligned momentum provide the input to solid coupling.',
    '有限射流能量与同向动量提供固体耦合输入。'))
add(P(
    "Step 20 — Declare solid coupling. Payload area is 1 mm², thickness 1 μm and density 2330 kg m⁻³. It starts at rest without stored recoverable energy. Assign 20% jet energy to deformation, release and departure. Assign 50% aligned momentum as net opening-direction payload impulse after reactions. Both fractions require measurement or coupled calculation. Boiling point and rigid-contact pressure leave them unresolved.",
    "步骤 20——规定固体耦合。载荷面积为 1 mm²、厚度 1 μm、密度 2330 kg m⁻³，初始静止且无可恢复储能。分配 20% 射流能量用于变形、释放及离开。传力反作用之后，将 50% 同向动量分配为净张开方向载荷冲量。两比例均需测量或耦合计算。沸点与刚性接触压力不能确定它们。"))
add(eq('C4-E29', r'\begin{aligned}m_f&=\rho_fA_fh_f=(2330)(1.00\times10^{-6})(1.00\times10^{-6})\ {\rm kg}=2.33\times10^{-9}\ {\rm kg},\\E_{\rm solid}&=\eta_EE_{\rm in}=0.20(50.0\ {\rm nJ})=10.0\ {\rm nJ},\\I_{\rm net}&=\eta_II_{\rm in}=0.50(3.133285343\times10^{-9}\ {\rm N\,s})=1.566642672\times10^{-9}\ {\rm N\,s}.\end{aligned}',
    r'$m_f$ is payload mass (kg), $\rho_f=2330$ kg m⁻³ density, $A_f=1.00$ mm² = 1.00×10⁻⁶ m² release area, and $h_f=1.00$ μm = 1.00×10⁻⁶ m thickness. $E_{\rm solid}$ is assigned useful solid energy (J), $E_{\rm in}$ incoming jet kinetic energy (J), and $\eta_E=0.20$ a dimensionless energy-allocation assumption. $I_{\rm net}$ is assigned net opening-direction payload impulse after all load-path reactions (N s), $I_{\rm in}$ aligned incoming momentum (N s), and $\eta_I=0.50$ a dimensionless impulse assumption. Labels f, in, solid, net, E and I identify film, incoming, useful solid allocation, net, energy and impulse. The numerical first-row factors represent density, area and thickness in SI units.',
    r'$m_f$为对象质量（kg），$\rho_f=2330$ kg m⁻³为密度，$A_f=1.00$ mm² = 1.00×10⁻⁶ m²为释放面积，$h_f=1.00$ μm = 1.00×10⁻⁶ m为厚度。$E_{\rm solid}$为指定有效固体能量（J），$E_{\rm in}$为入射射流动能（J），$\eta_E=0.20$为无量纲能量分配假设。$I_{\rm net}$为考虑全部传力路径反作用后的净张开方向对象冲量（N s），$I_{\rm in}$为同向入射动量（N s），$\eta_I=0.50$为无量纲冲量假设。标签f、in、solid、net、E、I分别标识薄膜、入射、有效固体分配、净量、能量与冲量。第一行数值因子分别是SI制密度、面积及厚度。',
    'Explicit conditional solid-coupling allocation', 'film',
    ['A_f = 1 mm² — intended release', 'h_f = 1 μm — payload thickness', 'ρ_f = 2330 kg/m³ → m_f = 2.33 μg', 'η_E = 0.20 → E_solid = 10 nJ', 'η_I = 0.50 → I_net = 1.5666×10⁻⁹ N s', 'E_in, I_in — incoming array'],
    ['Load-path coupling fractions are assumptions.', 'This payload differs from the blister benchmark.'],
    'Declared coupling converts incoming jet budgets into conditional payload budgets.',
    '明确声明的耦合将入射射流预算转换为条件性对象预算。'))
add(P(
    "Step 21 — Apply global necessary conditions. Separation costs fracture energy × intended area. Minimum translation costs half mass × minimum speed². Net impulse must reach mass × minimum speed. Residual bending, rotation, loss and competing fracture add demands. Failure excludes this assumed case. Passing leaves full transfer unresolved. Exact complete impulse from rest fixes final center-of-mass speed.",
    "步骤 21——应用整体必要条件。分离消耗断裂能 × 目标面积。最低平动消耗质量 × 最低速率²的一半。净冲量须达到质量 × 最低速率。残余弯曲、旋转、损失及竞争断裂会增加需求。失败可排除该假设情形，通过仍未确立完整转印。静止开始的精确总冲量决定最终质心速率。"))
add(eq('C4-E30', r'E_{\rm req}(v_f)=\Gamma A_f+\frac12m_fv_f^2,\qquad I_{\rm req}(v_f)=m_fv_f,\qquad E_{\rm solid}\ge E_{\rm req}(v_f),\qquad I_{\rm net}\ge I_{\rm req}(v_f)',
    r'$E_{\rm req}(v_f)$ is minimum fracture-plus-translation energy (J), $I_{\rm req}(v_f)$ required net impulse for the minimum departure speed (N s), $v_f\ge0$ that required speed (m s⁻¹), $m_f>0$ payload mass (kg), $A_f$ full intended release area (m²), and $\Gamma\ge0$ assumed uniform fracture energy (J m⁻²). $E_{\rm solid}$ is assigned available solid energy (J); $I_{\rm net}$ is net opening-direction impulse after interface/support reactions (N s). Subscripts req, f, solid and net identify required, payload, useful solid and net quantities. The inequalities are necessary under the stated zero-initial-energy/no-additional-source assumptions; they are not spatial fracture solutions.',
    r'$E_{\rm req}(v_f)$为最低断裂加平动能量（J），$I_{\rm req}(v_f)$为达到最低离开速度所需净冲量（N s），$v_f\ge0$为所需速度（m s⁻¹），$m_f>0$为对象质量（kg），$A_f$为全部目标释放面积（m²），$\Gamma\ge0$为假设均匀断裂能（J m⁻²）。$E_{\rm solid}$为指定可用固体能量（J）；$I_{\rm net}$为考虑界面／支承反作用后的净张开方向冲量（N s）。下标req、f、solid、net分别标识所需、对象、有效固体及净量。在所述零初始能量／无额外源假设下，不等式是必要条件，而非空间断裂解。',
    'Necessary global energy and momentum screens', 'energy',
    ['E_solid → available budget', 'ΓA_f → full release cost', '½m_f v_f² → departure kinetic energy', 'I_net → net opening impulse', 'm_f v_f → required momentum', 'E_req, I_req — minimum screens'],
    ['Passing is necessary, not sufficient.', 'Support reactions are already included in net impulse.'],
    'The full intended release area, not a pressure peak, determines the fracture-energy cost.',
    '决定断裂能消耗的是全部目标释放面积，而非压力峰值。'))
add(eq('C4-E31', r'\Gamma=0.020\ {\rm J\,m^{-2}}\quad\Rightarrow\quad \Gamma A_f=(0.020)(1.00\times10^{-6})\ {\rm J}=20.0\ {\rm nJ}>E_{\rm solid}=10.0\ {\rm nJ}',
    r'$\Gamma$ is assumed uniform release fracture energy (J m⁻²), $A_f=1.00$×10⁻⁶ m² intended full release area, and $E_{\rm solid}=10.0$ nJ assigned available solid energy. nJ is nanojoule; $\Rightarrow$ denotes numerical substitution. The comparison assumes no initially stored recoverable energy and no additional post-impact source. Subscript f labels film area, and solid labels the assigned useful energy.',
    r'$\Gamma$为假设均匀释放断裂能（J m⁻²），$A_f=1.00$×10⁻⁶ m²为全部目标释放面积，$E_{\rm solid}=10.0$ nJ为指定可用固体能量。nJ为纳焦耳；$\Rightarrow$表示数值代入。比较假设没有初始储存的可恢复能量，也没有额外冲击后源。下标f表示薄膜面积，solid表示指定有效能量。',
    'Failed release-energy screen', 'energy',
    ['Γ = 0.020 J/m²', 'A_f = 1 mm²', 'ΓA_f = 20 nJ — required release', 'E_solid = 10 nJ — available', 'early rigid impact ≈ 47.23 MPa'],
    ['High local pressure coexists with insufficient total release work.'],
    'The assigned source cannot release the whole interface even before departure energy is added.',
    '即使尚未计入离开动能，所指定源也无法释放整个界面。'))
add(P(
    "The stated energy failure excludes that case. The 47.23 MPa local transient creates no extra energy. Its footprint cannot automatically cover 1 mm² or sustain full-duration loading. Local damage is possible. Now change fracture energy to 0.005 J m⁻². Require minimum departure speed 0.50 m s⁻¹. Keep incoming jets and coupling fixed, then repeat both screens.",
    "给定能量条件失败，排除该情形。47.23 MPa 局部瞬态不会产生额外能量，其作用区不会自动覆盖 1 mm² 或维持整个加载时长，并可能造成局部损伤。现将断裂能改为 0.005 J m⁻²，要求最低离开速率 0.50 m s⁻¹。保持入射射流及耦合不变，重算两类筛选。"))
add(eq('C4-E32', r'\begin{aligned}\Gamma A_f&=5.00\ {\rm nJ},\qquad \frac12m_fv_f^2=\frac12(2.33\times10^{-9})(0.50)^2\ {\rm J}=0.29125\ {\rm nJ},\\E_{\rm req}(0.50\ {\rm m\,s^{-1}})&=5.29125\ {\rm nJ}<10.0\ {\rm nJ},\\I_{\rm req}(0.50\ {\rm m\,s^{-1}})&=(2.33\times10^{-9})(0.50)\ {\rm N\,s}=1.165\times10^{-9}\ {\rm N\,s}<I_{\rm net}.\end{aligned}',
    r'$\Gamma=0.005$ J m⁻² is the changed teaching fracture energy; $A_f=1.00$×10⁻⁶ m² is release area; $m_f=2.33$×10⁻⁹ kg is payload mass; and $v_f=0.50$ m s⁻¹ is minimum required departure speed. $E_{\rm req}$ is minimum fracture-plus-translation energy (J), $I_{\rm req}$ required net impulse (N s), and $I_{\rm net}=1.566642672$×10⁻⁹ N s the assigned actual net impulse. nJ is nanojoule. Subscripts req, f and net label required, payload and net. The 10.0 nJ comparator is assigned solid energy. The first-row numbers are SI mass and speed.',
    r'$\Gamma=0.005$ J m⁻²为改变后的教学断裂能；$A_f=1.00$×10⁻⁶ m²为释放面积；$m_f=2.33$×10⁻⁹ kg为对象质量；$v_f=0.50$ m s⁻¹为最低所需离开速度。$E_{\rm req}$为最低断裂加平动能（J），$I_{\rm req}$为所需净冲量（N s），$I_{\rm net}=1.566642672$×10⁻⁹ N s为指定实际净冲量。nJ为纳焦耳。下标req、f、net分别标识所需、对象及净量。10.0 nJ比较值是指定固体能量。第一行数值为SI制质量与速度。',
    'Passed necessary release and minimum-speed screens', 'energy',
    ['ΓA_f = 5 nJ — release', '½m_f v_f² = 0.29125 nJ — minimum translation', 'E_req = 5.29125 nJ < E_solid', 'I_req = 1.165×10⁻⁹ N s < I_net', 'v_f = 0.50 m/s — required minimum'],
    ['Spatial crack completion and intactness remain unproved.'],
    'Reducing the assumed fracture cost allows the necessary budgets to pass.',
    '降低假设断裂消耗后，必要预算可以通过。'))
add(P(
    "Step 22 — Match energy to exact impulse. Complete assigned impulse gives final speed 0.67238 m s⁻¹. This exceeds the 0.50 m s⁻¹ minimum. Its kinetic energy is 0.52669 nJ; minimum-speed energy is 0.29125 nJ. Adding actual kinetic energy still fits the 10 nJ low-fracture budget. Exact 0.50 m s⁻¹ would require counter-impulse or different coupling. Energy and momentum must share a physical force path.",
    "步骤 22——使能量与精确冲量一致。完整分配冲量给出最终速率 0.67238 m s⁻¹，高于 0.50 m s⁻¹ 最低要求。对应动能为 0.52669 nJ，最低速率动能为 0.29125 nJ。计入实际动能后仍满足 10 nJ 低断裂能预算。精确 0.50 m s⁻¹ 需反向冲量或不同耦合。能量和动量须对应同一实际传力路径。"))
add(eq('C4-E33', r'v_{\rm CM}=\frac{I_{\rm net}}{m_f}=0.672378829\ {\rm m\,s^{-1}},\qquad K_{\rm CM}=\frac{I_{\rm net}^2}{2m_f}=0.526688683\ {\rm nJ},\qquad \Gamma A_f+K_{\rm CM}=5.526688683\ {\rm nJ}<E_{\rm solid}',
    r'$v_{\rm CM}$ is actual final centre-of-mass speed (m s⁻¹) if the specified $I_{\rm net}$ is the complete net impulse from rest (N s). $m_f=2.33$×10⁻⁹ kg is payload mass; $K_{\rm CM}$ centre-of-mass kinetic energy (J); $\Gamma=0.005$ J m⁻² fracture energy; $A_f=1.00$×10⁻⁶ m² release area; and $E_{\rm solid}=10.0$ nJ assigned available energy. CM labels centre of mass and net labels impulse after all reactions. nJ denotes nanojoule. Rotation, shape motion and dissipation still require additional positive energy beyond the terms shown.',
    r'$v_{\rm CM}$为实际最终质心速度（m s⁻¹），条件是所给$I_{\rm net}$为从静止开始受到的全部净冲量（N s）。$m_f=2.33$×10⁻⁹ kg为对象质量；$K_{\rm CM}$为质心动能（J）；$\Gamma=0.005$ J m⁻²为断裂能；$A_f=1.00$×10⁻⁶ m²为释放面积；$E_{\rm solid}=10.0$ nJ为指定可用能量。CM标识质心，net表示考虑全部反作用后的冲量。nJ为纳焦耳。转动、形状运动及耗散仍需在所示项之外增加正能量。',
    'Energy–momentum compatibility check', 'energy',
    ['I_net → final payload momentum', 'm_f → v_CM = 0.67238 m/s', 'K_CM = 0.52669 nJ', 'ΓA_f = 5 nJ', 'total minimum = 5.52669 nJ', 'E_solid = 10 nJ'],
    ['An exact actual impulse fixes the centre-of-mass speed.'],
    'The stated impulse and low-fracture-energy budget are mutually consistent at the implied speed.',
    '所给冲量与低断裂能预算在其决定的速度处相互相容。'))
add(note(
    "<strong>Missing stack calibration.</strong> Coupling fractions, fracture energy, cohesive strength and PVC transmission remain unmeasured. The screens give conditional feasibility or exclusion. Resolve crack coverage, puncture, bending, torque, competing release and intact arrival.",
    "<strong>缺失叠层标定。</strong> 耦合比例、断裂能、内聚强度及 PVC 传递尚未测量。筛选给出有条件可行性或排除。须解析裂纹覆盖、穿刺、弯曲、扭矩、竞争释放及完整到达。"))

add(H("8. Placement and reset", "8. 落位与复位", 'operating-window'))
add(P(
    "Step 23 — Track payload flight after release. With negligible drag and gravity, lateral offset equals normal gap × tangent of departure angle. Use payload gap rather than liquid-jet gap. Array nonuniformity can add torque despite sufficient net impulse. The receiver must arrest motion, avoid damage and rebound, and provide final adhesion.",
    "步骤 23——追踪释放后的载荷飞行。阻力与重力可忽略时，横向偏移等于法向间隙 × 离开角正切。采用载荷间隙而非液体射流间隙。阵列不均匀可在净冲量足够时增加扭矩。受载体须停止运动、避免损伤及反弹，并提供最终粘附。"))
add(eq('C4-E34', r'\Delta x=H_f\tan\theta,\qquad H_f=100\ \mu{\rm m},\quad\theta=1^{\circ}\quad\Rightarrow\quad\Delta x=1.74551\ \mu{\rm m}',
    r'$\Delta x$ is lateral payload offset (m), $H_f>0$ normal payload flight gap (m), and $\theta\in(-\pi/2,\pi/2)$ departure angle relative to the target normal. $\tan$ is tangent; the numerical angle is converted from degrees to radians for evaluation. μm is micrometre and $\Rightarrow$ denotes substitution. Subscript f labels film/payload flight, not liquid-jet travel; $\Delta$ marks position difference. The relation assumes straight flight without significant drag, gravity or rotation-dependent aerodynamic force.',
    r'$\Delta x$为对象横向偏移（m），$H_f>0$为对象法向飞行间隙（m），$\theta\in(-\pi/2,\pi/2)$为相对目标法向的离开角。$\tan$为正切；数值角度由度转换为弧度计算。μm为微米，$\Rightarrow$表示代入。下标f标识薄膜／对象飞行，而非液体射流运动；$\Delta$表示位置差。关系假设直线飞行，且无显著阻力、重力或随转动变化的气动力。',
    'Ballistic placement estimate', 'film',
    ['H_f — payload normal flight gap', 'θ — departure angle', 'Δx — lateral placement error', 'target normal ↓ receiver', 'H_f = 100 μm, θ = 1°'],
    ['A 1° departure error gives about 1.75 μm offset in this example.'],
    'A finite receiving gap converts angular error into placement error.',
    '有限接收间隙将角度误差转换为落位误差。'))
add(P(
    "Cooling, condensation, remaining inventory, shell integrity and trapped gas set the next shot. Persistent cavities can change absorption, wetting and transmission. Repeatable transfer requires activation, useful output, selective release, survival, landing and reset. Report single-shot pressure records separately from the repeatable transfer window.",
    "冷却、凝结、剩余物质量、壳层完整性及滞留气体决定下一次发射。残留空腔可改变吸收、润湿和传递。可重复转印需要激活、有用输出、选择性释放、完整存续、落位及复位。单发压力纪录与可重复转印窗口分别报告。"))
add(P(
    "Measure deposited energy and activation statistics. Track cavity shape, lifetime and arriving jet mass, speed and direction. Record exposed and buried load histories, PVC/film motion and crack growth. Verify final integrity, position and next-shot state. Each missing link needs its corresponding measurement or model.",
    "测量沉积能量及激活统计。追踪空腔形状、寿命及到达射流质量、速率、方向。记录外露与埋藏载荷历程、PVC／薄膜运动及裂纹增长。核验最终完整性、位置与下一发状态。每个缺失环节需对应测量或模型。"))

add(H("Oral questions", "口头问题", 'defenses'))

answer1 = eq('C4-E35', r'\boldsymbol t_l=\boldsymbol T_l\boldsymbol n_f,\qquad \boldsymbol I_l=\int_{t_a}^{t_b}\int_{A_f(t)}\boldsymbol t_l\,dA\,dt,\qquad \mathcal W_l=\int_{t_a}^{t_b}\int_{A_f(t)}\boldsymbol t_l\cdot\boldsymbol v_f\,dA\,dt',
    r'Original formulas: $\boldsymbol t_l$ is fluid traction on the solid (Pa), $\boldsymbol T_l$ liquid stress tensor (Pa), $\boldsymbol n_f$ solid-to-liquid unit normal, $\boldsymbol I_l$ applied liquid impulse (N s), and $\mathcal W_l$ delivered work (J). $A_f(t)$ is loaded surface (m²), $dA$ its element (m²), $\boldsymbol v_f$ surface velocity (m s⁻¹), and $t_a,t_b,t,dt$ event endpoints, integration time and time element (s). $\int$ means surface/time integration; the dot denotes a vector projection. Subscripts l and f label liquid and film. The same identities first load PVC if it is the exposed layer.',
    r'原公式：$\boldsymbol t_l$为流体施加于固体的牵引（Pa），$\boldsymbol T_l$为液体应力张量（Pa），$\boldsymbol n_f$为固体指向液体的单位法向，$\boldsymbol I_l$为液体外加冲量（N s），$\mathcal W_l$为传递功（J）。$A_f(t)$为受载表面（m²），$dA$为其微元（m²），$\boldsymbol v_f$为表面速度（m s⁻¹），$t_a,t_b,t,dt$分别为事件起止时间、积分时间及时间微元（s）。$\int$表示表面／时间积分；点乘表示向量投影。下标l、f表示液体与薄膜。若PVC为外露层，同一恒等式首先加载PVC。',
    'Original load, impulse and work formulas', 'impact',
    ['T_l, n_f → t_l at exposed face', 'A_f(t), t_a → t_b — footprint and event', 'I_l — force-time integral', 'v_f → W_l requires motion'],
    ['Exposed PVC and buried film are different surfaces.'],
    'Reference answer: pressure, impulse and work describe different parts of the transmission path.',
    '参考答案：压力、冲量与功描述传递路径中的不同部分。')
answer1 += eq('C4-E36', r'E_{\rm solid}\ge\Gamma A_f+\frac12m_fv_f^2,\qquad I_{\rm net}\ge m_fv_f',
    r'Original necessary screens: $E_{\rm solid}$ is assigned available solid energy (J), $\Gamma$ uniform release fracture energy (J m⁻²), $A_f$ intended full release area (m²), $m_f$ payload mass (kg), $v_f$ minimum required departure speed (m s⁻¹), and $I_{\rm net}$ net opening impulse after all reactions (N s). The payload initially rests and has no additional recoverable source. Subscripts solid, f and net label useful solid allocation, payload and net impulse.',
    r'原必要筛选：$E_{\rm solid}$为指定可用固体能量（J），$\Gamma$为均匀释放断裂能（J m⁻²），$A_f$为全部目标释放面积（m²），$m_f$为对象质量（kg），$v_f$为最低所需离开速度（m s⁻¹），$I_{\rm net}$为考虑全部反作用后的净张开冲量（N s）。对象初始静止，且无额外可恢复源。下标solid、f、net标识有效固体分配、对象及净冲量。',
    'Original global screens', 'energy',
    ['E_solid — available work budget', 'ΓA_f — release cost', 'm_f, v_f — finite payload translation', 'I_net — actual net impulse'],
    ['Peak pressure supplies neither the area nor the energy budget.'],
    'Reference answer: finite energy and net impulse must reach the intended interface.',
    '参考答案：有限能量与净冲量必须到达目标界面。')
answer1 += P(
    "The 47.23 MPa scale describes initial local compression at a rigid receiver. Footprint, duration and transmission still require calculation. Twenty-five jets carry 50 nJ; assigned useful solid energy is 10 nJ. Releasing 1 mm² at 0.020 J m⁻² costs 20 nJ before translation. This case fails its energy condition. Direct impact first loads film; intact PVC first carries the load. Film loading follows PVC motion and contact. A lower-fracture case still needs crack coverage and payload integrity.",
    "47.23 MPa 尺度描述刚性受载体初始局部压缩。作用面积、时长及传递仍需计算。二十五束射流携带 50 nJ，分配有用固体能量为 10 nJ。以 0.020 J m⁻² 释放 1 mm²，在平动之前已需 20 nJ。该情形能量条件失败。直接撞击先加载薄膜，完整 PVC 则先承载。薄膜载荷取决于 PVC 运动与接触。低断裂能情形仍需裂纹覆盖及载荷完整性。")
add(defense('C4-Q1',
    "Trace a 47 MPa impact through the film/PVC stack. What limits release?",
    "追踪 47 MPa 撞击在薄膜／PVC 叠层中的传递。什么限制释放？",
    answer1,
    [('Distinguish local compressive pressure from opening traction, impulse and delivered work.', '区分局部压缩压力、张开牵引、冲量与传递功。'),
     ('Explain why the stated 10 nJ budget cannot pay the 20 nJ full-area release cost.', '解释为什么所给10 nJ预算无法支付20 nJ整面积释放消耗。'),
     ('Trace direct and PVC-mediated force paths, identify unknown transmission, and retain spatial/competing-failure checks.', '追踪直接及PVC介导传力路径，指出未知传递关系，并保留空间／竞争失效检验。')]))

answer2 = eq('C4-E37', r'w(r)=\frac{p_0}{64D_f}(b^2-r^2)^2,\qquad G_{p_0}=\frac{p_0^2b^4}{128D_f},\qquad p_{0,\rm crit}=\frac{\sqrt{128D_f\Gamma}}{b^2}',
    r'Original blister formulas: $w(r)$ is opening displacement (m), $r\in[0,b]$ radial position (m), $b>0$ existing circular crack radius (m), $p_0\ge0$ uniform maintained pressure difference (Pa), $D_f>0$ linear plate bending stiffness (N m), $G_{p_0}$ fixed-pressure energy-release rate (J m⁻²), $\Gamma>0$ constant fracture resistance (J m⁻²), and $p_{0,\rm crit}$ positive onset pressure (Pa). $\sqrt{\ }$ is the positive root. Subscripts f, 0 and crit denote film, maintained load and threshold. These expressions require regular centre and a clamped crack edge, quasistatic bending, and negligible stretching/pretension.',
    r'原鼓泡公式：$w(r)$为张开位移（m），$r\in[0,b]$为径向位置（m），$b>0$为预存圆裂纹半径（m），$p_0\ge0$为均匀恒定压差（Pa），$D_f>0$为线性薄板弯曲刚度（N m），$G_{p_0}$为恒压能量释放率（J m⁻²），$\Gamma>0$为恒定断裂阻力（J m⁻²），$p_{0,\rm crit}$为正起始压力（Pa）。$\sqrt{\ }$取正根。下标f、0、crit分别表示薄膜、恒定载荷与阈值。表达式要求中心正则、裂纹边缘夹持、准静态弯曲，且拉伸／预张力可忽略。',
    'Original pressure-controlled benchmark formulas', 'film',
    ['r, b — circular crack geometry', 'w(r) ↑ clamped profile', 'p₀ — uniform maintained pressure', 'D_f — bending stiffness', 'Γ — fracture resistance', 'G_p₀, p₀,crit — onset quantities'],
    ['A finite short jet is not a maintained pressure reservoir.'],
    'Reference answer: this pressure threshold follows a particular geometry and loading control.',
    '参考答案：此压力阈值源于特定几何及加载控制。')
answer2 += P(
    "The blister threshold follows from the clamped-plate solution, volume integration and reservoir work. Differentiate total potential by crack area. Assume an existing circular crack, slow uniform bending, negligible stretching, pretension and inertia. A brief local jet needs a different loading history. Intact PVC also changes the loaded structure. Fixed pressure increases driving with crack radius. Fixed volume lowers pressure and driving during growth. A sealed PFC cavity needs evolving pressure, volume and temperature. Rapid release needs transmitted traction, inertia, crack kinetics and energy balance. Check payload stress alongside interface release.",
    "鼓泡阈值来自夹持板解、体积积分及储库功，再对裂纹面积求总势能导数。假设已有圆裂纹、缓慢均匀弯曲、拉伸、预张力及惯性可忽略。短局部射流需要不同加载历程。完整 PVC 也会改变受载结构。固定压力时，驱动随裂纹半径增加；固定体积时，增长使压力与驱动降低。密闭 PFC 空腔需演化压力、体积和温度。快速释放需传递牵引、惯性、裂纹动力学及能量平衡。界面释放同时须检查载荷应力。")
add(defense('C4-Q2',
    "When does the 156 kPa blister threshold apply?",
    "156 kPa 鼓泡阈值适用于哪些条件？",
    answer2,
    [('Reconstruct pressure → plate opening → volume → source-inclusive potential → energy-release rate.', '重构压力 → 薄板张开 → 体积 → 含源势能 → 能量释放率。'),
     ('Identify the clamped existing crack, uniform maintained pressure and quasistatic small-deflection assumptions.', '指出夹持预裂纹、均匀恒压及准静态小挠度假设。'),
     ('Explain why short/localized loads, fixed volume, sealed thermodynamics or PVC transmission require another calculation.', '解释短时／局部载荷、恒容、封闭热力学或PVC传递为什么需要另一计算。')]))

answer3 = eq('C4-E38', r'\Gamma=\int_0^{\delta_c}t_n(\delta)\,d\delta=\frac12T_{\max}\delta_c,\qquad G\ge\Gamma(\psi,T_i,v_c)',
    r'Original interface formulas: $\Gamma$ is tensile cohesive fracture work per area (J m⁻²), $\delta$ physical opening integration variable (m), $d\delta$ its element (m), $\delta_c$ complete opening (m), $t_n$ tensile cohesive traction (Pa), and $T_{\max}$ peak tensile traction (Pa). The half-product applies to the adopted triangular monotonic law. $G$ is energy available per new crack area (J m⁻²), $\psi$ dimensionless mode mixture, $T_i$ interface temperature (K), and $v_c$ crack speed (m s⁻¹). $\int$ denotes opening integration. Subscripts n, c, i and max identify normal, crack/final opening, interface and maximum.',
    r'原界面公式：$\Gamma$为单位面积拉伸内聚断裂功（J m⁻²），$\delta$为物理张开积分变量（m），$d\delta$为其微元（m），$\delta_c$为完全张开（m），$t_n$为拉伸内聚牵引（Pa），$T_{\max}$为峰值拉伸牵引（Pa）。一半乘积适用于所采用的三角形单调关系。$G$为单位新增裂纹面积可用能量（J m⁻²），$\psi$为无量纲模态混合参数，$T_i$为界面温度（K），$v_c$为裂纹速度（m s⁻¹）。$\int$表示张开积分。下标n、c、i、max分别表示法向、裂纹／最终张开、界面与最大值。',
    'Original cohesive work and fracture criteria', 'cohesive',
    ['δ → tensile opening', 't_n, T_max — strength curve', 'δ_c — final separation', 'Γ — full curve area', 'G — crack energy supply', 'ψ, T_i, v_c — actual resistance conditions'],
    ['Reaching strength does not establish complete separation.'],
    'Reference answer: successful release requires both initiation and separation work at the correct interface.',
    '参考答案：成功释放需要在正确界面上同时满足起始与分离功要求。')
answer3 += eq('C4-E39', r'E_{\rm solid}\ge\Gamma A_f+\frac12m_fv_f^2,\qquad I_{\rm net}\ge m_fv_f,\qquad \Delta x=H_f\tan\theta',
    r'Original screens and placement relation: $E_{\rm solid}$ is available useful solid energy (J), $\Gamma$ fracture energy (J m⁻²), $A_f$ full release area (m²), $m_f$ payload mass (kg), $v_f$ minimum departure speed (m s⁻¹), and $I_{\rm net}$ net opening impulse (N s). $\Delta x$ is lateral payload offset (m), $H_f$ normal payload flight gap (m), $\theta$ departure angle relative to receiver normal, and $\tan$ tangent. The screens assume initial rest without another energy source; the placement relation assumes straight short flight. Subscripts solid, f and net label useful solid energy, payload and net impulse.',
    r'原筛选与落位关系：$E_{\rm solid}$为可用有效固体能量（J），$\Gamma$为断裂能（J m⁻²），$A_f$为全部释放面积（m²），$m_f$为对象质量（kg），$v_f$为最低离开速度（m s⁻¹），$I_{\rm net}$为净张开冲量（N s）。$\Delta x$为对象横向偏移（m），$H_f$为对象法向飞行间隙（m），$\theta$为相对接收面法向的离开角，$\tan$为正切。筛选假设初始静止且无其他能量源；落位关系假设短时直线飞行。下标solid、f、net标识有效固体能量、对象及净冲量。',
    'Original necessary operating-window checks', 'film',
    ['ΓA_f — intended release', 'm_f, v_f — outgoing intact object', 'E_solid, I_net — transmitted budgets', 'H_f, θ → Δx at receiver'],
    ['Full release, intact flight and repeatable reset are separate requirements.'],
    'Reference answer: passing global budgets starts, rather than completes, the transfer argument.',
    '参考答案：通过整体预算是转印论证的起点，而非终点。')
answer3 += P(
    "The low-fracture case passes assigned energy and minimum-impulse conditions. Complete transfer: Not established. Missing: local initiation, full crack coverage and payload survival. Compression needs conversion into relative interface opening. Exclude unintended release, puncture, tearing and excessive bending. Keep exact impulse consistent with final translation. Then check tilt, flight, landing adhesion and rebound. Synchronize solid motion, crack growth and integrity measurements. Repeated shots require cooling, condensation and remaining-inventory checks. Report single-shot output separately from repeatable intact transfer.",
    "低断裂能情形通过分配能量及最低冲量条件。完整转印尚未确立。缺失：局部起始、完整裂纹覆盖及载荷存续。压缩载荷须转化为界面相对张开。须排除意外释放、穿刺、撕裂及过度弯曲。精确冲量与最终平动保持一致。再检查倾斜、飞行、落位粘附及反弹。同步测量固体运动、裂纹增长和完整性。重复发射需检查冷却、凝结及剩余物质量。单发输出与可重复完整转印分别报告。")
add(defense('C4-Q3',
    "Both global screens pass. What measurements establish repeatable intact transfer?",
    "两项整体筛选均通过。哪些测量能确立可重复完整转印？",
    answer3,
    [('Distinguish local strength initiation, full separation work and competing fracture paths.', '区分局部强度起始、完整分离功及竞争断裂路径。'),
     ('Keep energy and actual net impulse consistent and explain why spatial crack coverage and payload damage remain unresolved.', '保持能量与实际净冲量相容，并解释为什么空间裂纹覆盖和对象损伤仍未确定。'),
     ('Connect correct release to placement, landing and repeatable thermal/phase reset, proposing observations for the missing links.', '将正确释放连接至落位、着陆及可重复热／相变复位，并为缺失环节提出观测。')]))


CHAPTER = dict(
    number=4,
    slug='04-fracture-and-transfer',
    title_en='Fracture and transfer',
    title_zh='断裂与转印',
    summary_en="Calculate transmitted load, film deformation and fracture work. Check release, landing and reset.",
    summary_zh="计算传递载荷、薄膜变形及断裂功。检验释放、落位及复位。",
    body=''.join(body),
    question_ids=['C4-Q1', 'C4-Q2', 'C4-Q3'],
    objectives=[
        ('Trace direct and intact-PVC load paths without equating exposed pressure to buried opening traction.', '追踪直接及完整PVC传力路径，不把外露压力等同于埋藏张开牵引。'),
        ('Derive transient areal inertia and the pressure-controlled circular blister fracture relation with explicit source work.', '推导瞬态面惯性及恒压圆鼓泡断裂关系，明确压力源做功。'),
        ('Connect cohesive strength, fracture work, finite energy/momentum, correct release, placement and reset.', '连接内聚强度、断裂功、有限能量／动量、正确释放、落位及复位。'),
    ],
    prerequisite_en="Prerequisites: Chapter 3’s arriving mass, energy, momentum, footprint and impact history.",
    prerequisite_zh="前提：第三章的到达质量、能量、动量、作用面积及撞击历程。",
)
