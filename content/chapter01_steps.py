"""Bilingual, multiline derivation expansions for every Chapter 1 equation.

Keys use the final, post-deletion numbering. Each entry supplies premises,
additional locally defined symbols, intermediate mathematics and interpretation.
The chapter's original final result follows these intermediate lines.
"""

STEPS = {}


def step(n, en, zh, tex, symbols_en='', symbols_zh='', check_en='', check_zh=''):
    STEPS[f'C1-E{n:02d}'] = dict(en=en, zh=zh, tex=tex,
        symbols_en=symbols_en, symbols_zh=symbols_zh,
        check_en=check_en, check_zh=check_zh)


step(1,
    'Initial data are prescribed, rather than derived. The radial equation is second order, so radius and signed velocity are separate data. Choose time zero before activation, during growth, or at maximum radius. A stationary initial wall can accelerate. Evaluate the later momentum law at time zero to see why.',
    '初始数据是给定条件，不能作为推导结果。径向方程是二阶方程，半径和带符号速度是独立初值。时间原点可选在激活前、增长中或最大半径处。初始静止的壁面仍能加速。将下文动量方程在零时刻取值即可说明原因。',
    r'''\begin{aligned}
    \dot R&=dR/dt,\qquad \ddot R=d\dot R/dt,\\
    \rho R_0\ddot R(0)&=p_b(0)-p_\infty(0)-2\sigma/R_0-4\mu U_0/R_0-\tfrac32\rho U_0^2,\\
    U_0=0\quad&\Longrightarrow\quad
    \ddot R(0)=\frac{p_b(0)-p_\infty(0)-2\sigma/R_0}{\rho R_0}.
    \end{aligned}''',
    r'$\rho>0$ is carrier density (kg m⁻³); $p_b$ is bubble pressure (Pa); $\sigma$ is constant surface tension (N m⁻¹); $\mu$ is viscosity (Pa s); $\ddot R$ is acceleration (m s⁻²). All pressures share an absolute reference.',
    r'$\rho>0$ 为载液密度（kg m⁻³）；$p_b$ 为气泡压力（Pa）；$\sigma$ 为常数表面张力（N m⁻¹）；$\mu$ 为黏度（Pa s）；$\ddot R$ 为加速度（m s⁻²）。全部压力采用同一绝对参考值。',
    'Positive initial pressure excess over capillarity gives outward acceleration. Initial zero speed therefore does not imply equilibrium. The acceleration expression has units Pa/(kg m⁻²) = m s⁻².',
    '初始内外压差超过毛细压差时产生向外加速度。因此初速为零不代表平衡。加速度表达式单位为 Pa/(kg m⁻²) = m s⁻²。')

step(2,
    'Apply mass conservation to a spherical shell. Constant density reduces it to zero divergence. Integrate in radius at fixed time. The integration function can depend on time. A material cavity wall supplies the final boundary value. Appreciable phase transfer changes that boundary value.',
    '对球壳应用质量守恒。密度为常数时，散度为零。在固定时间对半径积分，积分函数仍可随时间变化。物质空腔壁面提供最终边界值。相变传质显著时，该边界值需要修改。',
    r'''\begin{aligned}
    \frac{d}{dt}\left[\rho\frac{4\pi}{3}((r+\delta r)^3-r^3)\right]&=0,\\
    4\pi\rho r^2u(r,t)-4\pi\rho(r+\delta r)^2u(r+\delta r,t)&=0,\\
    \lim_{\delta r\to0}\frac{(r+\delta r)^2u(r+\delta r,t)-r^2u(r,t)}{\delta r}&=\partial_r(r^2u)=0,\\
    0&=\frac{1}{r^2}\frac{\partial(r^2u)}{\partial r},\\
    \frac{\partial(r^2u)}{\partial r}&=0
      \quad\Longrightarrow\quad r^2u=C(t),\\
    u(R,t)&=\dot R\quad\Longrightarrow\quad C(t)=R^2\dot R,\\
    \frac{u(2R,t)}{\dot R}&=\frac{R^2}{(2R)^2}=\frac14\quad(\dot R\ne0).
    \end{aligned}''',
    r'$C(t)$ is the radial volume-flux factor (m³ s⁻¹); $\rho>0$ is constant liquid density (kg m⁻³); $\delta r>0$ is fixed shell thickness (m); $\pi$ is the circle constant; $\partial_r$ holds time fixed; the fixed shell stays liquid; the liquid domain is $r\ge R(t)>0$.',
    r'$C(t)$ 为径向体积通量因子（m³ s⁻¹）；$\rho>0$ 为常数液体密度（kg m⁻³）；$\delta r>0$ 为固定球壳厚度（m）；$\pi$ 为圆周率；$\partial_r$ 保持时间固定；固定球壳始终属于液体；液体区域为 $r\ge R(t)>0$。',
    'The flux factor divided by radius squared has velocity units. Setting wall speed to zero gives a stationary liquid everywhere.',
    '通量因子除以半径平方具有速度单位。壁面速度为零时，全部液体静止。')

step(3,
    'Purely radial, angle-independent flow has zero curl outside the cavity. The exterior of a sphere is simply connected, so a single-valued potential exists. Integrating velocity introduces an arbitrary time function. Fix that gauge at infinity. The potential packages the velocity field for the momentum integration; it supplies no extra physical degree of freedom.',
    '纯径向且与角度无关的流动在空腔外旋度为零。球外域单连通，因此存在单值速度势。积分速度会引入任意时间函数。用无穷远处的参考值固定该规范。速度势便于积分动量方程，并不增加物理自由度。',
    r'''\begin{aligned}
    \boldsymbol u&=u(r,t)\boldsymbol e_r,\qquad\nabla\times\boldsymbol u=\boldsymbol0,\\
    \partial_r\phi&=u=R^2\dot R/r^2,\\
    \phi(r,t)&=-R^2\dot R/r+g(t),\\
    \phi(\infty,t)&=0\quad\Longrightarrow\quad g(t)=0,\\
    \int_\infty^r s^{-2}\,ds&=[-s^{-1}]_\infty^r=-1/r-0.
    \end{aligned}''',
    r'$\boldsymbol u$ is velocity (m s⁻¹), $\boldsymbol e_r$ the outward radial unit vector, $\nabla\times$ the curl (inverse-length differentiation), $\boldsymbol0$ the zero vector; $g(t)$ is a potential gauge (m² s⁻¹).',
    r'$\boldsymbol u$ 为速度（m s⁻¹），$\boldsymbol e_r$ 为向外径向单位矢量，$\nabla\times$ 为旋度算子（逆长度微分），$\boldsymbol0$ 为零矢量；$g(t)$ 为速度势规范函数（m² s⁻¹）。',
    'Spatial differentiation recovers positive outward velocity during expansion. Potential has units length × speed. The construction excludes rotational flow and unresolved vortex sheets.',
    '空间求导恢复膨胀时向外的正速度。速度势单位为长度乘速度。该构造排除了旋转流动和未解析涡片。')

step(4,
    'Differentiate the product in the numerator before evaluating at the wall. For a moving wall value, add the chain-rule displacement term. These operations differ because the observation points differ.',
    '先对分子乘积求导，再在壁面取值。对运动壁面处的取值求导时，需要加入链式法则的位移项。两种操作的观察点不同。',
    r'''\begin{aligned}
    \frac{d(R^2\dot R)}{dt}&=2R\dot R\dot R+R^2\ddot R,\\
    \frac{d\phi(R(t),t)}{dt}&=\left.\partial_t\phi\right|_{r=R}
       +\dot R\left.\partial_r\phi\right|_{r=R},\\
    &=-(2\dot R^2+R\ddot R)+\dot R\dot R\\
    &=-\dot R^2-R\ddot R.
    \end{aligned}''', check_en='The moving derivative exceeds the Eulerian wall evaluation by wall speed squared. Both derivatives have energy-per-mass units.',
    check_zh='运动导数比欧拉导数的壁面取值大一个壁面速度平方。两者均具有单位质量能量的单位。')

step(5,
    'Start from exterior Euler momentum. In this radial field the bulk viscous term vanishes, so this momentum form also applies outside the viscous traction boundary. Irrotationality turns convection into a kinetic-energy gradient. Integrate the resulting zero gradient over the connected liquid domain. The spatial integration function depends on time. The gauge and far-field condition determine it. Then evaluate at the wall.',
    '从外域欧拉动量方程出发。此径向流场的体黏性项为零，因此在黏性牵引边界之外仍可采用该动量形式。无旋条件将对流项写成动能梯度。在连通液体域中积分零梯度，得到随时间变化的空间积分函数。规范与远场条件确定该函数，随后在壁面取值。',
    r'''\begin{aligned}
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
    \end{aligned}''',
    r'$\boldsymbol u=\nabla\phi$ is liquid velocity (m s⁻¹); $\nabla$, $\nabla\cdot$, $\nabla\times$, $\nabla^2$ denote gradient, divergence, curl and vector Laplacian; $u_i,u_j$ are Cartesian velocity components (m s⁻¹), $i,j\in\{1,2,3\}$; $\partial_i,\partial_j$ are coordinate derivatives (m⁻¹); $\sum$ adds over the indicated index; zero vorticity implies $\partial_j u_i=\partial_i u_j$. $|\ |$ is Euclidean magnitude; $B_0(t)$ is the Bernoulli integration function (m² s⁻²); subscript $\infty$ denotes the far-field limit; $p$ is local liquid pressure (Pa). Smooth fields permit exchanging derivatives.',
    r'$\boldsymbol u=\nabla\phi$ 为液体速度（m s⁻¹）；$\nabla$、$\nabla\cdot$、$\nabla\times$、$\nabla^2$ 分别表示梯度、散度、旋度及矢量拉普拉斯；$u_i,u_j$ 为笛卡尔速度分量（m s⁻¹），$i,j\in\{1,2,3\}$；$\partial_i,\partial_j$ 为坐标导数（m⁻¹）；$\sum$ 对指定指标求和；无旋条件给出 $\partial_j u_i=\partial_i u_j$。$|\ |$ 为欧氏模长；$B_0(t)$ 为伯努利积分函数（m² s⁻²）；下标 $\infty$ 表示远场极限；$p$ 为局部液体压力（Pa）。场足够光滑时允许交换导数。',
    'The coefficient is 2 − 1/2 = 3/2. Constant potential gauge has been fixed; an arbitrary time gauge would change the integration function together with the potential derivative.',
    '系数为 2 − 1/2 = 3/2。速度势规范已经固定；若使用任意时间规范，积分函数会与速度势导数一同改变。')

step(6,
    'Use a normal pointing from liquid into gas. At an inner spherical cavity this normal points inward and curvature is negative. The normal stress jump gives the liquid pressure. Differentiate the radial speed to evaluate the normal viscous traction.',
    '法向从液体指向气体。内球形空腔的该法向向内，曲率为负。法向应力跳跃给出液体压力。对径向速度求导，计算法向黏性牵引。',
    r'''\begin{aligned}
    \boldsymbol n&=-\boldsymbol e_r,\qquad
    \nabla_s\cdot\boldsymbol n=\nabla\cdot\boldsymbol n
      =\frac1{r^2}\partial_r(-r^2)=-2/r,\\
    \kappa&=(\nabla_s\cdot\boldsymbol n)|_{r=R}=-2/R,\\
    p_l-p_b&=\sigma\kappa+2\mu\partial_r u|_{r=R},\\
    \partial_r(R^2\dot R r^{-2})&=-2R^2\dot R r^{-3},\\
    2\mu\partial_r u|_{r=R}&=2\mu(-2\dot R/R)=-4\mu\dot R/R.
    \end{aligned}''',
    r'$\boldsymbol n$ is the liquid-to-gas unit normal; $\boldsymbol e_r$ is the outward radial unit vector; $\kappa$ is signed curvature (m⁻¹); $\nabla_s\cdot$ is surface divergence and $\nabla\cdot$ volume divergence. Extend the unit normal radially without radial variation, so its normal derivative is zero and both divergences agree at the sphere.',
    r'$\boldsymbol n$ 为液体指向气体的单位法向；$\boldsymbol e_r$ 为向外径向单位矢量；$\kappa$ 为带符号曲率（m⁻¹）；$\nabla_s\cdot$ 为表面散度，$\nabla\cdot$ 为体散度。将单位法向沿径向作不变延拓，其法向导数为零，因此两种散度在球面一致。',
    'For a static sphere the gas pressure exceeds liquid pressure by 2σ/R. The viscous pressure reverses with velocity. This local traction calculation remains necessary after deleting the separate tensor-dissipation check.',
    '静止球面气压比液压高 2σ/R。黏性压力随速度反向。删除独立张量耗散检验后，仍需保留此局部牵引计算。')

step(7,
    'Multiply the inertial-pressure relation by density. Replace liquid wall pressure with the traction balance. Collect all pressures with their signs. Divide by positive density and radius when acceleration is required.',
    '将惯性压力关系乘以密度。以牵引平衡替换壁面液压，按符号整理各项压力。需要加速度时，再除以正密度与正半径。',
    r'''\begin{aligned}
    \rho(R\ddot R+\tfrac32\dot R^2)&=p_l-p_\infty,\\
    p_l-p_\infty&=(p_b-2\sigma/R-4\mu\dot R/R)-p_\infty,\\
    \ddot R&=\frac{p_b-p_\infty-2\sigma/R-4\mu\dot R/R}{\rho R}
       -\frac{3\dot R^2}{2R},\\
    \dot R=\ddot R=0&\quad\Longrightarrow\quad p_b-p_\infty=2\sigma/R.
    \end{aligned}''', check_en='The inviscid limit removes the viscous term continuously. At rest capillarity requires positive bubble overpressure. Each original balance term has units Pa.',
    check_zh='无黏极限连续消去黏性项。静止时毛细作用要求气泡内过压为正。原平衡各项单位均为 Pa。')

step(8,
    'This is an adopted ideal-mixture closure. For components sharing temperature and volume, each ideal-gas partial pressure is proportional to its amount. Add component amounts to obtain total pressure. These algebraic steps do not determine evaporation, temperature, or saturation. Real mixtures can require a different equation of state.',
    '这里采用理想混合物闭合。共享温度和体积的各理想气体分压正比于物质的量。将各组分物质的量相加，得到总压力。该代数过程不能确定蒸发、温度或饱和状态。实际混合物可能需要不同状态方程。',
    r'''\begin{aligned}
    p_iV_b&=n_i\mathcal R T_b\quad (i\in\{v,\mathrm{PFC};v,w;g\}),\\
    p_bV_b&=\left(n_{v,\mathrm{PFC}}+n_{v,w}+n_g\right)\mathcal R T_b,\\
    p_b&=\frac{n_{v,\mathrm{PFC}}\mathcal R T_b}{V_b}
      +\frac{n_{v,w}\mathcal R T_b}{V_b}+\frac{n_g\mathcal R T_b}{V_b}.
    \end{aligned}''',
    r'$i$ labels PFC vapor, water vapor or permanent gas; $p_i$ is component partial pressure (Pa); $n_i$ is component amount (mol); $V_b>0$ is bubble volume (m³); $\mathcal R$ is the universal gas constant (J mol⁻¹ K⁻¹); $T_b>0$ is common gas temperature (K).',
    r'$i$ 标记 PFC 蒸气、水蒸气或非凝结气体；$p_i$ 为组分分压（Pa）；$n_i$ 为组分物质的量（mol）；$V_b>0$ 为气泡体积（m³）；$\mathcal R$ 为通用气体常数（J mol⁻¹ K⁻¹）；$T_b>0$ 为共同气体温度（K）。',
    'Pressure × volume has energy units. A vanishing component amount removes its partial pressure. Missing: component mass-transfer rates, energy balance and appropriate phase equilibrium or kinetics.',
    '压力乘体积具有能量单位。某组分物质的量为零时，其分压为零。缺少：组分传质率、能量平衡以及适用的相平衡或相变动力学。')

step(9,
    'At a fixed instant, integrate energy over the whole exterior. Angular integration supplies the shell area. The lower bound is the current interface. Replace speed by the continuity solution, cancel radial powers and evaluate the improper integral before differentiating the result.',
    '在固定时刻，对整个外域积分能量。角向积分给出球壳面积。下限为当前界面。用连续性解替换速度，约去径向幂，再计算广义积分，最后才对结果求导。',
    r'''\begin{aligned}
    dV&=r^2\sin\theta\,d\theta\,d\psi\,dr,\\
    \int_0^{2\pi}\!d\psi\int_0^\pi\!\sin\theta\,d\theta&=2\pi[-\cos\theta]_0^\pi=4\pi,\\
    u^2&=R^4\dot R^2/r^4,\qquad r^2/r^4=r^{-2},\\
    \int_R^b r^{-2}\,dr&=-1/b+1/R\ \longrightarrow\ 1/R\quad(b\to\infty),\\
    2\pi\rho R^4\dot R^2/R&=2\pi\rho R^3\dot R^2.
    \end{aligned}''',
    r'$dV$ is shell volume (m³); $\theta\in[0,\pi]$ and $\psi\in[0,2\pi]$ are polar and azimuthal angles (dimensionless radians); $b>R$ is a finite outer cutoff (m).',
    r'$dV$ 为体积元（m³）；$\theta\in[0,\pi]$ 与 $\psi\in[0,2\pi]$ 为极角与方位角（无量纲弧度）；$b>R$ 为有限外截断半径（m）。',
    'Density × radius cubed × speed squared gives joules. Infinite volume causes no divergence because speed decays sufficiently fast. A finite outer wall changes the velocity boundary-value problem.',
    '密度乘半径三次方乘速度平方得到焦耳。速度衰减足够快，因此无限体积不造成发散。有限外壁会改变速度边值问题。')

step(10,
    'The integrated kinetic energy already contains the moving lower boundary through radius. Apply the product rule to that expression. Differentiating a fixed-limit integral while ignoring the moving boundary would miss part of this rate.',
    '积分后的动能已通过半径包含运动下边界。对该表达式应用乘积法则。若将其作为固定积分限求导并忽略运动边界，就会遗漏部分变化率。',
    r'''\begin{aligned}
    \frac{d(R^3\dot R^2)}{dt}&=\frac{dR^3}{dt}\dot R^2+R^3\frac{d\dot R^2}{dt},\\
    \frac{dR^3}{dt}&=3R^2\dot R,\qquad\frac{d\dot R^2}{dt}=2\dot R\ddot R,\\
    2\pi\rho(3R^2\dot R^3+2R^3\dot R\ddot R)
      &=4\pi\rho R^2\dot R(\tfrac32\dot R^2+R\ddot R),\\
    \frac{d(4\pi\sigma R^2)}{dt}&=4\pi\sigma(2R\dot R).
    \end{aligned}''', check_en='Energy rates have units watts. At a turning point both rates vanish instantaneously, even when acceleration is nonzero. Variable surface tension would add another product-rule term.',
    check_zh='能量变化率单位为瓦。转折点两种能量变化率瞬时为零，即使加速度非零。表面张力随时间变化时，需要增加乘积求导项。')

step(11,
    'Multiply the radial pressure balance by signed cavity volume rate. Identify the inertial term using the preceding product rule. Expand the capillary and viscous products separately. Move surface-energy storage to the left. This derives mechanical power accounting without restoring the deleted strain-tensor calculation.',
    '将径向压力平衡乘以带符号空腔体积变化率。用前式乘积法则识别惯性项。分别展开毛细项和黏性项，再将表面能储存移至左侧。由此推导机械功率平衡，无须恢复已删除的应变张量计算。',
    r'''\begin{aligned}
    \frac{dK_l}{dt}&=(p_b-p_\infty-2\sigma/R-4\mu\dot R/R)(4\pi R^2\dot R),\\
    (-2\sigma/R)(4\pi R^2\dot R)&=-8\pi\sigma R\dot R=-dE_\sigma/dt,\\
    (-4\mu\dot R/R)(4\pi R^2\dot R)&=-16\pi\mu R\dot R^2,\\
    \frac{dK_l}{dt}+\frac{dE_\sigma}{dt}
      &=(p_b-p_\infty)\dot V_b-16\pi\mu R\dot R^2.
    \end{aligned}''', check_en='Expansion against excess internal pressure and collapse under excess external pressure both allow positive work. Dissipation is nonnegative for either velocity sign. Missing: laser absorption, internal energy, latent heat and acoustic radiation in a complete energy budget.',
    check_zh='内压较高时膨胀与外压较高时塌缩都可得到正功。两种速度符号下耗散均非负。完整能量预算还缺少：激光吸收、内能、潜热与声辐射。')

step(12,
    'Define an ideal control: constant vapor pressure, constant exterior pressure, zero gas, zero viscosity and zero surface tension. These assumptions reduce the previously derived momentum law. Start at maximum radius with zero speed. Evaluate acceleration there to select the inward trajectory.',
    '定义理想对照：蒸气压和外压恒定，忽略气体、黏度及表面张力。用这些假设约化前述动量方程。初始位于最大半径且速度为零。在此处计算加速度，选择向内轨迹。',
    r'''\begin{aligned}
    p_b&=p_v,\quad \mu=\sigma=0,\quad p_v-p_\infty=-\Delta p_c,\\
    \rho(R\ddot R+\tfrac32\dot R^2)&=-\Delta p_c,\\
    R_{\max}\ddot R(0)&=-\Delta p_c/\rho,\\
    \ddot R(0)&=-\frac{\Delta p_c}{\rho R_{\max}}<0.
    \end{aligned}''',
    r'$\mu$ is viscosity (Pa s) and $\sigma$ surface tension (N m⁻¹), both set to zero in this control; $p_b$ is bubble pressure (Pa).',
    r'$\mu$ 为黏度（Pa s），$\sigma$ 为表面张力（N m⁻¹），在此对照中均置零；$p_b$ 为气泡压力（Pa）。',
    'Pressure deficit produces inward acceleration. This hypothetical control omits physical collapse arrest and evolving PFC vapor production.',
    '压差产生向内加速度。此假想对照省略了实际塌缩终止机制和随时间演化的 PFC 蒸气生成。')

step(13,
    'On the open inward branch speed is nonzero, so divide the chain rule by speed. Divide the reduced momentum equation by positive radius. Solve the integrating-factor equation explicitly. The initial turning point is handled by continuity rather than division by zero.',
    '向内分支内部速度非零，因此链式法则可除以速度。将约化动量方程除以正半径。显式求解积分因子方程。初始转折点通过连续延拓处理，不能除以零。',
    r'''\begin{aligned}
    R(\tfrac12 y')+\tfrac32 y&=-\Delta p_c/\rho,\\
    y'+3y/R&=-2\Delta p_c/(\rho R),\\
    I'/I&=3/R,\quad I(R_{\max})=1,\\
    \ln I(R)-\ln I(R_{\max})&=\int_{R_{\max}}^R\frac{3}{s}\,ds
       =3[\ln(s/R_{\max})]_{R_{\max}}^R=3\ln(R/R_{\max}),\\
    \ln I(R)&=3\ln(R/R_{\max}),\quad
       I(R)=\exp(3\ln(R/R_{\max}))=(R/R_{\max})^3,\\
    (R^3y)'&=R^3y'+3R^2y.
    \end{aligned}''',
    r"$y'=dy/dR$ has units m s⁻²; $I>0$ is a dimensionless integrating factor normalized by $I(R_{\max})=1$, $I'=dI/dR$ (m⁻¹); $s>0$ is a dummy radius (m); $\ln$ and $\exp$ are natural logarithm and exponential with dimensionless arguments.",
    r"$y'=dy/dR$ 的单位为 m s⁻²；$I>0$ 为无量纲积分因子，采用 $I(R_{\max})=1$ 归一化，$I'=dI/dR$（m⁻¹）；$s>0$ 为积分哑半径（m）；$\ln$ 与 $\exp$ 为自然对数和指数，自变量无量纲。",
    'Multiplying by the constant maximum-radius cube gives the equivalent integrating factor used below. Every momentum term retains acceleration-per-length-compatible units before integration.',
    '乘以常数最大半径三次方，即得到下文使用的等价积分因子。积分前各动量项保持一致量纲。')

step(14,
    'Integrate the exact radial derivative from the initial maximum to the present radius. Apply zero initial squared speed. Evaluate the cubic antiderivative. Divide by positive radius cubed. Taking a square root gives two mathematical signs; inward motion selects the negative one.',
    '从初始最大半径积分完整径向导数至当前半径。代入初始速度平方为零，计算三次方原函数，再除以正半径三次方。开平方得到两个数学符号，向内运动选择负号。',
    r'''\begin{aligned}
    \int_{R_{\max}}^R\frac{d(s^3y)}{ds}\,ds
      &=-\frac{2\Delta p_c}{\rho}\left[\frac{s^3}{3}\right]_{R_{\max}}^R,\\
    R^3y(R)&=\frac{2\Delta p_c}{3\rho}(R_{\max}^3-R^3),\\
    y(R)&=\frac{2\Delta p_c}{3\rho}\left(\frac{R_{\max}^3}{R^3}-1\right)\ge0,\\
    \dot R&=\pm\sqrt{y(R)},\qquad\dot R<0\ \text{during collapse}.
    \end{aligned}''', check_en='At maximum radius the speed is zero. For smaller positive radius the squared speed is positive. The speed scale is the square root of pressure divided by density.',
    check_zh='最大半径处速度为零。半径减小且保持正值时，速度平方为正。速度尺度为压差除以密度的平方根。')

step(15,
    'For the inward branch, time increases while radius decreases. The negative reciprocal speed reverses the integration bounds. Normalize radius and include its differential. Factor the cubic ratio before taking the positive square root.',
    '向内分支上，时间增加而半径减小。速度倒数的负号反转积分上下限。将半径无量纲化并包含微分变换。先整理三次方比值，再取正平方根。',
    r'''\begin{aligned}
    dt&=dR/\dot R,\qquad
    \frac1{\dot R}=-\sqrt{\frac{3\rho}{2\Delta p_c}}\frac1{\sqrt{(R_{\max}/R)^3-1}},\\
    (R_{\max}/R)^3-1&=x^{-3}-1=(1-x^3)/x^3,\\
    \frac{dR}{\sqrt{(R_{\max}/R)^3-1}}
      &=R_{\max}\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx,\\
    -\int_1^0\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx
      &=\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx.
    \end{aligned}''', check_en='The scale Rmax × sqrt(density/pressure) has units seconds. The integral is improper at its endpoints; its finite value is the formal zero-radius model time.',
    check_zh='尺度 Rmax × sqrt(密度/压差) 的单位为秒。积分在端点为广义积分；其有限值是模型到零半径的形式时间。')

step(16,
    'Cube the normalized radius. Carry both the numerator exponent and Jacobian into the transformed integral. Match each exponent to the beta-function definition. Inspect both endpoints before evaluating the coefficient.',
    '对无量纲半径取三次方换元。将分子指数与雅可比因子一同代入积分。逐项将指数与贝塔函数定义匹配。计算系数前先检查两个端点。',
    r'''\begin{aligned}
    x^{3/2}&=(q^{1/3})^{3/2}=q^{1/2},\\
    x^{3/2}\,dx&=q^{1/2}\tfrac13q^{-2/3}\,dq=\tfrac13q^{-1/6}\,dq,\\
    \sqrt{3/2}/3&=1/\sqrt6,\quad a-1=-1/6\Rightarrow a=5/6,\\
    b-1&=-1/2\Rightarrow b=1/2,\\
    C_t&=B(5/6,1/2)/\sqrt6=0.9146813565\ldots .
    \end{aligned}''', check_en='Both endpoint powers exceed −1, ensuring integrability. This dimensionless coefficient follows from the trajectory integral. It is independent of material fitting.',
    check_zh='两个端点幂指数均大于 −1，因而可积。此无量纲系数来自轨迹积分，不依赖材料拟合。')

step(17,
    'Insert squared speed into the exterior kinetic-energy result. Cancel density, distribute radius cubed and remove its denominator. Independently integrate pressure work over decreasing cavity volume. Differentiate the result to check its power and sign.',
    '将速度平方代入外域动能结果。约去密度，将半径三次方分配至括号内并约去分母。独立对减小的空腔体积积分压力功。再对结果求导，检验功率和符号。',
    r'''\begin{aligned}
    (2\pi\rho)\frac{2\Delta p_c}{3\rho}&=4\pi\Delta p_c/3,\\
    R^3\left(\frac{R_{\max}^3}{R^3}-1\right)&=R_{\max}^3-R^3,\\
    K_l&=\int_{V_{\max}}^{V_b}(-\Delta p_c)\,dV
      =\Delta p_c(V_{\max}-V_b),\\
    \frac{dK_l}{dt}&=-\Delta p_c\,4\pi R^2\dot R>0\quad(\dot R<0),\\
    K_l/E_B&=(R_{\max}^3-R^3)/R_{\max}^3=1-(R/R_{\max})^3.
    \end{aligned}''',
    r'$V_b=4\pi R^3/3$ is cavity volume (m³); $V$ is the dummy volume variable (m³); $t$ is time (s), $\dot R$ wall speed (m s⁻¹).',
    r'$V_b=4\pi R^3/3$ 为空腔体积（m³）；$V$ 为积分哑体积（m³）；$t$ 为时间（s），$\dot R$ 为壁面速度（m s⁻¹）。',
    'Pressure times displaced volume has joule units. Zero initial energy and positive growth during collapse agree with the mechanical power balance. Radial liquid energy does not specify jet energy.',
    '压差乘置换体积具有焦耳单位。初始动能为零，塌缩时动能增加，与机械功率平衡一致。径向液体动能不能确定射流动能。')

step(18,
    'Convert every teaching input to SI units. Compute the common pressure–density factor and cubic radius before inserting them into time, energy and speed formulas. The half-radius energy fraction follows from the cube of one half.',
    '将全部教学输入换为 SI 单位。先计算共同压差密度因子及半径三次方，再代入时间、能量和速度公式。半径减半时的能量比例来自二分之一的三次方。',
    r'''\begin{aligned}
    R_{\max}&=30\ \mu\mathrm m=30\times10^{-6}\ \mathrm m,\quad
      \Delta p_c=100\ \mathrm{kPa}=10^5\ \mathrm{Pa},\\
    \sqrt{\rho/\Delta p_c}&=\sqrt{1000/10^5}=0.1\ \mathrm{s\,m^{-1}},\\
    R_{\max}^3&=27\times10^{-15}\ \mathrm{m^3},\\
    t_c&=0.9146813565(30\times10^{-6})(0.1)\ \mathrm s
      =2.7440440695\times10^{-6}\ \mathrm s,\\
    E_B&=(4\pi/3)(10^5)(27\times10^{-15})\ \mathrm J
      =1.1309733553\times10^{-8}\ \mathrm J,\\
    (R_{\max}/R)^3-1&=2^3-1=7,\quad K_l/E_B=1-(1/2)^3=7/8.
    \end{aligned}''',
    check_en='One microsecond is 10⁻⁶ seconds; one nanojoule is 10⁻⁹ joules. The final values below agree with independent quadrature and pressure-work checks. These inputs are illustrative.',
    check_zh='一微秒为 10⁻⁶ 秒；一纳焦为 10⁻⁹ 焦。下列结果与独立积分及压力功检验一致。这些输入是教学示例。')

step(19,
    'Use the ideal inward speed as a diagnostic trajectory. Square the nonnegative Mach magnitude, set a selected positive threshold, and solve for the positive radius fraction. The threshold marks a chosen modeling cutoff. It does not predict the physical collapse endpoint.',
    '将理想向内速度用作诊断轨迹。对非负马赫数取平方，令其等于选定的正阈值，再解出正半径比例。阈值标记选定的模型截止条件，并不预测实际塌缩终点。',
    r'''\begin{aligned}
    x&=R/R_{\max},\qquad M_w^2=\frac{2\Delta p_c}{3\rho c^2}(x^{-3}-1),\\
    M_w=M_*&\quad\Longrightarrow\quad
      \frac{3\rho c^2M_*^2}{2\Delta p_c}=x_M^{-3}-1,\\
    x_M^{-3}&=1+\frac{3\rho c^2M_*^2}{2\Delta p_c},\\
    x_M&=\left[1+\frac{3(1000)(1500)^2(0.1)^2}{2(10^5)}\right]^{-1/3}\\
       &=338.5^{-1/3}=0.1434874,\\
    R_M&=(30\ \mu\mathrm m)(0.1434874)=4.30462\ \mu\mathrm m.
    \end{aligned}''',
    r'$x$ is normalized radius (dimensionless); $R_M=x_MR_{\max}$ is diagnostic radius (m); numerical inputs are the previous teaching density and pressure, with $c=1500$ m s⁻¹ and chosen $M_*=0.1$.',
    r'$x$ 为无量纲半径；$R_M=x_MR_{\max}$ 为诊断半径（m）；数值输入采用前述教学密度和压差，并取 $c=1500$ m s⁻¹、选定 $M_*=0.1$。',
    'The bracket is dimensionless and exceeds one, so the diagnostic radius lies below maximum radius. As threshold tends to zero, its radius approaches the starting radius. Singular zero radius remains outside physical validity.',
    '括号无量纲且大于一，因此诊断半径小于最大半径。阈值趋于零时，诊断半径趋于初始最大半径。奇异零半径仍超出物理适用范围。')

step(20,
    'Place a pressure observer at a fixed liquid point throughout the event. Integrate over time there. Subtract a spatially uniform reference pressure. A separate area integral converts pressure impulse into mechanical impulse when the surface is fixed. For moving surfaces, pressure, normal and area must remain inside the time integral.',
    '在整个事件中始终属于液体的固定点放置压力观察者。在该处对时间积分，并减去空间均匀的参考压力。表面固定时，另作面积积分可将压力冲量转为机械冲量。表面运动时，压力、法向和面积均须保留在时间积分内。',
    r'''\begin{aligned}
    q(\boldsymbol x,t)&=p(\boldsymbol x,t)-p_{\mathrm{ref}}(t),\\
    \Pi(\boldsymbol x)&=\lim_{N\to\infty}\sum_{k=1}^Nq(\boldsymbol x,t_k)\Delta t,
       \quad\Delta t=(t_1-t_0)/N,\\
    \boldsymbol J_p&=-\int_{t_0}^{t_1}\int_{S(t)}q\boldsymbol n\,dA\,dt,\\
    S(t)=S\quad&\Longrightarrow\quad\boldsymbol J_p=-\int_S\Pi\boldsymbol n\,dA,\\
    [\boldsymbol J_p]&=\mathrm{Pa\,s\,m^2}=\mathrm{N\,s},\qquad[\Pi]=\mathrm{Pa\,s}.
    \end{aligned}''',
    r'$q$ is gauge pressure (Pa); $N$ is a positive integer subdivision count; $k$ labels a time sample $t_k$ (s); $\Delta t$ is time-step width (s); $\boldsymbol J_p$ is gauge-pressure mechanical impulse on a liquid control volume (N s); $S(t)$ is its surface, $\boldsymbol n$ its outward unit normal, and $dA$ an area element (m²); brackets denote units. Fixed-surface reduction requires fixed orientation and all sampled points remaining liquid.',
    r'$q$ 为表压（Pa）；$N$ 为正整数分段数；$k$ 标记采样时间 $t_k$（s）；$\Delta t$ 为时间段宽度（s）；$\boldsymbol J_p$ 为作用于液体控制体的表压机械冲量（N s）；$S(t)$ 为其表面，$\boldsymbol n$ 为向外单位法向，$dA$ 为面积元（m²）；方括号表示单位。固定表面约化要求方向固定且全部采样点始终位于液体中。',
    'A constant reference shifts the local pressure integral without changing its spatial gradient. Absolute contact loads require the actual exterior pressure and viscous traction. A point crossed by an interface needs a moving-domain formulation.',
    '常数参考压力可改变局部压力积分，但不改变其空间梯度。绝对接触载荷需要实际外部压力和黏性牵引。若界面穿过观察点，则需要运动域表述。')

step(21,
    'Divide constant-density Navier–Stokes by density. Integrate every term between the same fixed times at the same fixed position. The fundamental theorem gives the velocity difference. Smoothness and a common liquid domain permit gradient–integral exchange. The spatially uniform reference has zero gradient.',
    '将常密度 Navier–Stokes 方程除以密度。在相同固定位置、相同时间上下限内逐项积分。微积分基本定理给出速度差。场足够光滑且积分期间均属于液体域时，允许交换梯度与积分。空间均匀的参考压力梯度为零。',
    r'''\begin{aligned}
    \partial_t\boldsymbol u&=-\nabla p/\rho-(\boldsymbol u\cdot\nabla)\boldsymbol u+\nu\nabla^2\boldsymbol u,\\
    \int_{t_0}^{t_1}\partial_t\boldsymbol u\,dt
       &=\boldsymbol u(\boldsymbol x,t_1)-\boldsymbol u(\boldsymbol x,t_0)=\Delta\boldsymbol u,\\
    \int_{t_0}^{t_1}\nabla p\,dt
       &=\nabla\int_{t_0}^{t_1}(p-p_{\mathrm{ref}})\,dt
         +\int_{t_0}^{t_1}\underbrace{\nabla p_{\mathrm{ref}}}_{=0}\,dt=\nabla\Pi,\\
    \int_{t_0}^{t_1}\nu\nabla^2\boldsymbol u\,dt
       &=\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt.
    \end{aligned}''', check_en='The convective and viscous terms remain integrals because their fields evolve. Each integrated term has units velocity. Time-dependent bounds that depend on position require additional gradient terms.',
    check_zh='对流和黏性场随时间变化，因此对应项仍为积分。每个积分项均具有速度单位。若时间上下限依赖位置，则梯度运算会产生额外项。')

step(22,
    'Scale the omitted acceleration terms over the pulse duration. Compare them with a velocity increment of order the chosen speed. Apply incompressibility to both endpoint fields. Taking divergence of reduced impulse momentum gives a Laplace problem. Boundary data select its solution.',
    '用脉冲持续时间估算被忽略加速度项。将其与所选速度同阶的速度增量比较。对两个端点速度场分别应用不可压缩条件。对约化冲量动量关系取散度，得到拉普拉斯问题。边界数据决定其解。',
    r'''\begin{aligned}
    \left|\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt\right|
       &\sim U^2\tau/L,\qquad (U^2\tau/L)/U=U\tau/L,\\
    \left|\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt\right|
       &\sim\nu U\tau/L^2,\qquad(\nu U\tau/L^2)/U=\nu\tau/L^2,\\
    \nabla\cdot\Delta\boldsymbol u&=\nabla\cdot\boldsymbol u(t_1)-\nabla\cdot\boldsymbol u(t_0)=0-0=0,\\
    0&=-\nabla\cdot\nabla\Pi/\rho=-\nabla^2\Pi/\rho.
    \end{aligned}''',
    r'$\sim$ denotes a scale estimate rather than an equality or rigorous error bound; $t_0,t_1$ are fixed event endpoints (s); $\boldsymbol u$ is velocity (m s⁻¹).',
    r'$\sim$ 表示尺度估计，并非等式或严格误差界；$t_0,t_1$ 为固定事件端点（s）；$\boldsymbol u$ 为速度（m s⁻¹）。',
    'If the actual increment is much smaller than the chosen speed, these ratios need not bound its relative error. A fixed wall gives zero normal impulse derivative when normal velocity is unchanged. Driven and outlet boundaries supply their impulse values.',
    '若实际增量远小于所选速度，这些比值不能约束增量的相对误差。固定壁面法向速度不变时，法向冲量导数为零。受驱边界与出口分别给出各自冲量值。')

step(23,
    'For the straight column, integrate the zero second derivative once to obtain a constant slope. Integrate again. Apply inlet data to the intercept and outlet data to the slope. The negative pressure-impulse slope accelerates liquid in the positive axial direction.',
    '对直液柱，将二阶导数为零积分一次，得到常斜率，再积分一次。入口条件确定截距，出口条件确定斜率。负压力冲量斜率使液体沿正轴向加速。',
    r'''\begin{aligned}
    d^2\Pi/dz^2=0&\Rightarrow d\Pi/dz=A_1,\\
    \Pi(z)-\Pi(0)&=\int_0^z A_1\,ds=A_1z,\\
    \Pi(0)=\Pi_0&\Rightarrow A_0=\Pi_0,\\
    0=\Pi(L)&=A_1L+\Pi_0\Rightarrow A_1=-\Pi_0/L,\\
    \Delta u_z&=-(-\Pi_0/L)/\rho=\Pi_0/(\rho L).
    \end{aligned}''',
    r'$s$ is a dummy axial integration coordinate (m). The uniform-speed column is an inviscid core benchmark; no-slip wall layers are omitted.',
    r'$s$ 为轴向积分哑坐标（m）。匀速液柱是无黏核心流基准，省略无滑移壁面层。',
    'At inlet and outlet the solution reproduces both prescribed values. Impulse divided by density and length has units m s⁻¹. Equal pressure peaks with different durations produce different speed increments.',
    '解在入口和出口恢复两个给定值。冲量除以密度及长度的单位为 m s⁻¹。相同压力峰值、不同持续时间会产生不同速度增量。')

step(24,
    'The rectangular pulse is a stipulated ideal benchmark. Convert its pressure, duration and column length. Compute the impulse, velocity, displacement ratio, viscous ratio and crossing time separately. The total pulse duration does not specify its physical rise time.',
    '矩形脉冲是规定的理想基准。换算压力、持续时间和液柱长度。分别计算冲量、速度、位移比、黏性比及声穿越时间。脉冲总时长不能确定实际上升时间。',
    r'''\begin{aligned}
    \Delta p&=6.0\times10^5\ \mathrm{Pa},\quad\tau=5.0\times10^{-7}\ \mathrm s,
      \quad L=10^{-4}\ \mathrm m,\\
    \Pi_0&=(6.0\times10^5)(5.0\times10^{-7})=0.30\ \mathrm{Pa\,s},\\
    \rho L&=1000(10^{-4})=0.1\ \mathrm{kg\,m^{-2}},\quad U=0.30/0.1=3.0\ \mathrm{m\,s^{-1}},\\
    U\tau/L&=3(5\times10^{-7})/10^{-4}=0.015,\\
    \nu\tau/L^2&=(10^{-6})(5\times10^{-7})/10^{-8}=5\times10^{-5},\\
    t_a&=10^{-4}/1500=6.66667\times10^{-8}\ \mathrm s,\quad \tau/t_a=7.5.
    \end{aligned}''', check_en='The rectangular discontinuity has zero ideal rise time, so its fronts require acoustic treatment. The integrated column result is a reduced impulse benchmark. A real pulse needs a measured or prescribed finite rise time and the separate communication test below.',
    check_zh='理想矩形跃变的上升时间为零，因此波前需要声学处理。液柱积分结果属于约化冲量基准。实际脉冲需要实测或给定的有限上升时间，并进行下文独立通信检验。')

step(25,
    'Stand-off compares a center-to-boundary distance with maximum bubble radius. It is a geometric descriptor. To prove directional cancellation for the unbounded sphere, write each radial unit-vector component and integrate over all solid angles. The azimuthal sine and cosine integrate to zero; the axial component cancels between hemispheres.',
    '离壁比将中心到边界距离与最大气泡半径比较，属于几何描述。为证明无界球形情况下方向相互抵消，写出径向单位矢量各分量并对全部立体角积分。方位正弦和余弦积分为零，轴向分量在两半球之间抵消。',
    r'''\begin{aligned}
    \boldsymbol e_r&=(\sin\theta\cos\psi,\sin\theta\sin\psi,\cos\theta),\quad
      d\Omega=\sin\theta\,d\theta\,d\psi,\\
    \int_0^{2\pi}\cos\psi\,d\psi&=[\sin\psi]_0^{2\pi}=0,\\
    \int_0^{2\pi}\sin\psi\,d\psi&=[-\cos\psi]_0^{2\pi}=0,\\
    \int_0^\pi\cos\theta\sin\theta\,d\theta&=[\tfrac12\sin^2\theta]_0^\pi=0,\\
    \int_{S^2}\boldsymbol e_r\,d\Omega&=(0,0,0).
    \end{aligned}''',
    r'$\theta\in[0,\pi]$ and $\psi\in[0,2\pi]$ are dimensionless polar and azimuthal angles; tuple entries are Cartesian vector components.',
    r'$\theta\in[0,\pi]$ 与 $\psi\in[0,2\pi]$ 为无量纲极角和方位角；有序三元组为笛卡尔矢量分量。',
    'The cancellation concerns perfect symmetry. Actual boundaries change the spatial pressure and velocity problem. Stand-off alone cannot determine the response of different boundary materials or curvatures.',
    '抵消结论针对完全球对称。实际边界改变空间压力和速度问题。离壁比本身不能确定不同边界材料或曲率下的响应。')

step(26,
    'Start with local mass and Cauchy momentum conservation. Adopt constant-density Newtonian stress. Its divergence reduces to the vector Laplacian because incompressibility removes the divergence-gradient term. The spatial problem has three velocity components, pressure and unknown interface shape, together with initial and boundary data.',
    '从局部质量守恒与柯西动量守恒出发，采用常密度牛顿应力。不可压缩条件消去散度梯度项，使黏性应力散度约化为矢量拉普拉斯。空间问题包含三个速度分量、压力及未知界面形状，还需初始和边界数据。',
    r'''\begin{aligned}
    \partial_t\rho+\nabla\cdot(\rho\boldsymbol u)&=0
       \quad\xrightarrow{\rho\ \mathrm{constant}}\quad\nabla\cdot\boldsymbol u=0,\\
    \boldsymbol T&=-p\boldsymbol I+\mu[\nabla\boldsymbol u+(\nabla\boldsymbol u)^{\mathsf T}],\\
    \rho D\boldsymbol u/Dt&=\nabla\cdot\boldsymbol T,\\
    \nabla\cdot\boldsymbol T&=-\nabla p+\mu[\nabla^2\boldsymbol u+\nabla(\nabla\cdot\boldsymbol u)]
      =-\nabla p+\mu\nabla^2\boldsymbol u,\\
    D\boldsymbol u/Dt&=\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u.
    \end{aligned}''',
    r'$\boldsymbol T$ is Cauchy stress (Pa), $\boldsymbol I$ the dimensionless identity tensor, superscript $\mathsf T$ transpose, $D/Dt$ the material derivative; body forces are omitted. The density derivative is displayed before imposing constant density.',
    r'$\boldsymbol T$ 为柯西应力（Pa），$\boldsymbol I$ 为无量纲单位张量，上标 $\mathsf T$ 表示转置，$D/Dt$ 为物质导数；忽略体力。密度导数写在施加常密度条件之前。',
    'Stress divergence and inertia both have units N m⁻³. Supply a divergence-free initial velocity, compatible interface shape, wall velocities, outlet data and contact-line law. A radius history cannot replace these fields.',
    '应力散度和惯性项单位均为 N m⁻³。需要给定无散初始速度、相容初始界面、壁面速度、出口数据及接触线规律。半径历程不能代替这些空间场。')

step(27,
    'Represent a material interface by a level set. Its material derivative vanishes, yielding equal normal speeds. The level-set normal points from liquid to gas. Project the clean-interface stress jump onto its normal and tangent. Constant surface tension and negligible gas viscous stress give the pressure and tangential conditions.',
    '用水平集表示物质界面。其物质导数为零，从而得到法向速度相等。水平集法向从液体指向气体。将清洁界面应力跳跃分别投影至法向和切向。表面张力恒定且气体黏性应力可忽略时，得到压力和切向条件。',
    r'''\begin{aligned}
    F(\boldsymbol x,t)=0,\quad\boldsymbol n&=\nabla F/|\nabla F|,\quad
      V_n=-\partial_tF/|\nabla F|,\\
    \partial_tF+\boldsymbol u\cdot\nabla F=0&\Rightarrow V_n=\boldsymbol u\cdot\boldsymbol n,\\
    (\boldsymbol T_g-\boldsymbol T_l)\boldsymbol n&=\sigma\kappa\boldsymbol n,\\
    (\boldsymbol T_g-\boldsymbol T_l)\boldsymbol n
       &=[(p_l-p_b)\boldsymbol I-2\mu\boldsymbol D]\boldsymbol n,\\
    \boldsymbol n\cdot\boldsymbol n&=1,\qquad\boldsymbol s\cdot\boldsymbol n=0,\\
    p_l-p_b-2\mu\boldsymbol n\cdot\boldsymbol D\boldsymbol n&=\sigma\kappa,\\
    -2\mu\boldsymbol s\cdot\boldsymbol D\boldsymbol n&=0.
    \end{aligned}''',
    r'$F$ is a smooth dimensionless level-set function increasing into gas, with nonzero gradient on the interface; $\boldsymbol x$ is position (m), $t$ time (s); $\boldsymbol T_g=-p_b\boldsymbol I$ and $\boldsymbol T_l=-p_l\boldsymbol I+2\mu\boldsymbol D$ are gas and liquid stresses (Pa); $\boldsymbol I$ is the identity tensor.',
    r'$F$ 为向气体侧增加的光滑无量纲水平集，界面上梯度非零；$\boldsymbol x$ 为位置（m），$t$ 为时间（s）；$\boldsymbol T_g=-p_b\boldsymbol I$ 与 $\boldsymbol T_l=-p_l\boldsymbol I+2\mu\boldsymbol D$ 为气液应力（Pa）；$\boldsymbol I$ 为单位张量。',
    'The interface condition matches normal velocity; tangential node motion is a parametrization choice. It imposes no solid-wall no-slip condition on an inviscid free surface. Phase transfer needs a mass-flux condition instead.',
    '界面条件匹配法向速度；节点切向运动属于参数化选择。无黏自由表面不能施加固壁无滑移条件。发生相变传质时，应采用质量通量条件。')

step(28,
    'For inviscid irrotational liquid, choose potential and interface position as unknowns. Incompressibility gives Laplace’s equation. On the interface, combine Bernoulli with the inviscid traction jump. Then convert the fixed-position derivative into the derivative following a liquid marker. This conversion changes the kinetic-term sign.',
    '对无黏无旋液体，选取速度势和界面位置为未知量。不可压缩条件给出拉普拉斯方程。在界面结合伯努利方程与无黏牵引跳跃，再将固定位置导数转为随液体标记点运动的导数。该转换改变动能项符号。',
    r'''\begin{aligned}
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
    \end{aligned}''',
    r'$p_l$ is liquid-side interface pressure (Pa). Interface markers $\boldsymbol X(t)$ follow liquid particles; the material potential derivative has units m² s⁻². The construction assumes single-valued potential and a smooth pre-impact interface.',
    r'$p_l$ 为界面液体侧压力（Pa）。界面标记点 $\boldsymbol X(t)$ 随液体质点运动；速度势物质导数单位为 m² s⁻²。该构造假设速度势单值，且撞击前界面光滑。',
    'Solve-and-advance loop: prescribe initial interface and potential; evaluate pressure input and curvature; solve the harmonic field with interface potential and impermeable-wall normal data; recover velocity; advance interface positions and interface potential; repeat. An outlet supplies its pressure or compatible potential condition. Far-field gauge fixes the additive freedom. Material and Eulerian dynamic conditions are alternative forms. Missing: physical PFC pressure history, phase transfer, contact-line law where applicable, and treatment of topology changes.',
    '求解推进循环：给定初始界面与速度势；计算输入压力和曲率；用界面速度势及不透壁法向条件求解调和场；恢复速度；推进界面位置和界面速度势；重复计算。出口需给定压力或相容速度势条件。远场规范固定加法自由度。物质与欧拉动力学条件为等价表述。缺少：实际 PFC 压力历程、相变传质、适用处的接触线规律及拓扑变化处理。')

step(29,
    'Test the spatial model against a sphere. Evaluate the potential at its moving wall and differentiate by the product rule. Insert negative cavity curvature into the material dynamic condition. Move squared-speed terms to the same side, reverse signs, then multiply by density.',
    '用球形极限检验空间模型。在运动壁面取速度势，并按乘积法则求导。将负的空腔曲率代入物质动力学条件。把速度平方项移至同侧，变号后再乘密度。',
    r'''\begin{aligned}
    \phi_\Gamma&=-R^2\dot R/R=-R\dot R,\\
    d\phi_\Gamma/dt&=-(\dot R\dot R+R\ddot R),\\
    -R\ddot R-\tfrac32\dot R^2&=(p_\infty-p_b+2\sigma/R)/\rho,\\
    R\ddot R+\tfrac32\dot R^2&=(p_b-p_\infty-2\sigma/R)/\rho.
    \end{aligned}''',
    r'$t$ is time (s); $d/dt$ follows the spherical interface.',
    r'$t$ 为时间（s）；$d/dt$ 跟随球形界面。',
    'This recovers the inviscid radial balance with the same capillary sign. The viscous term cannot emerge from an inviscid potential boundary condition. At static equilibrium the Laplace overpressure is recovered.',
    '该结果恢复相同毛细符号的无黏径向平衡。无黏势流边界条件不能产生黏性项。静态极限恢复拉普拉斯过压。')

step(30,
    'Derive the communication time from linear acoustics about uniform resting liquid. Linear mass conservation and momentum combine into a wave equation. A disturbance travels the selected path at sound speed. Choose the path from the driven region to the relevant observer. Use the shortest important pressure-rise or change time, rather than automatically using pulse duration. Separately evaluate the wall-speed history.',
    '从均匀静止液体附近的线性声学推导通信时间。将线性质量守恒和动量方程结合，得到波动方程。扰动以声速沿所选路径传播。路径应从驱动区通向相关观察位置。采用最短的重要压力上升或变化时间，不能自动用脉冲总时长代替。另行检验壁面速度历程。',
    r'''\begin{aligned}
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
    \end{aligned}''',
    r"$\rho_0>0$ is uniform background density (kg m⁻³); primes label small acoustic perturbations, with $\rho'$ density (kg m⁻³), $p'$ pressure (Pa), $\boldsymbol u'$ velocity (m s⁻¹); $\nabla\cdot$ and $\nabla^2$ are spatial divergence and Laplacian; $\partial_t$ is the fixed-position derivative; $t_a$ is one-way travel time (s); ns is 10⁻⁹ s. Linearization assumes inviscid barotropic liquid and constant $c$.",
    r"$\rho_0>0$ 为均匀背景密度（kg m⁻³）；撇号标记小幅声学扰动，$\rho'$ 为密度（kg m⁻³），$p'$ 为压力（Pa），$\boldsymbol u'$ 为速度（m s⁻¹）；$\nabla\cdot$ 和 $\nabla^2$ 为空间散度与拉普拉斯；$\partial_t$ 为固定位置导数；$t_a$ 为单程传播时间（s）；ns 为 10⁻⁹ s。线性化假设液体无黏、正压且声速恒定。",
    'Operational test: record geometry, pressure observer, sound-speed source and uncertainty; identify the pressure variation time; sample wall speed with adequate temporal resolution; compute both ratios over the event. The rapid example fails pressure communication despite small Mach number. The slow example supports that approximation. These illustrative inputs are unmeasured. Thresholds are diagnostics, without certified error bounds. The impulse model also needs small displacement, advection and viscous corrections.',
    '实际检验：记录几何、压力观察位置、声速来源和不确定度；辨认压力变化时间；以足够时间分辨率采样壁面速度；在事件中计算两个比值。快速示例虽马赫数小，但压力通信不足。慢速示例支持该近似。这些示例输入未经实测。阈值属于诊断，不具有认证误差界。冲量模型还要求位移、对流和黏性修正较小。')

step(31,
    'Reconstruct the causal chain before answering. Subtract far-field pressure from the normal traction law, equate it to radial inertia, then solve for acceleration. The mixture statement identifies the missing source input. Follow the full Euler-to-Bernoulli derivation in C1-E05 and energy conversion in C1-E11. For a directional outlet, replace the scalar radial solution with C1-E26–C1-E28 and the actual boundaries.',
    '作答前重建因果链。从法向牵引关系减去远场压力，将其与径向惯性相等，再求加速度。混合物关系指出缺失的源输入。完整欧拉至伯努利推导见 C1-E05，能量转换见 C1-E11。存在定向出口时，用 C1-E26–C1-E28 及实际边界替代标量径向解。',
    r'''\begin{aligned}
    p_l-p_\infty&=p_b-p_\infty-2\sigma/R-4\mu\dot R/R,\\
    p_l-p_\infty&=\rho R\ddot R+\tfrac32\rho\dot R^2,\\
    \rho R\ddot R&=p_b-p_\infty-2\sigma/R-4\mu\dot R/R-\tfrac32\rho\dot R^2,\\
    \ddot R&=\frac{p_b-p_\infty-2\sigma/R-4\mu\dot R/R-\tfrac32\rho\dot R^2}{\rho R}.
    \end{aligned}''',
    r'$p_l$ is liquid-side wall pressure (Pa).',
    r'$p_l$ 为壁面液体侧压力（Pa）。',
    'Falsification question: does the measured or prescribed pressure history satisfy the stated momentum balance within its regime? An emitted jet further needs direction, finite moving mass and an evolving interface. Transfer success needs a receiver load and fracture evidence.',
    '证伪问题：实测或给定压力历程能否在适用范围内满足所述动量平衡？喷出射流还需要方向、有限运动质量及演化界面。成功转印需要受载面载荷和断裂证据。')

step(32,
    'Reproduce the collapse chain rather than memorize its coefficient. Use squared speed and the integrating factor from C1-E13. Apply the initial condition as in C1-E14. Integrate reciprocal inward speed as in C1-E15–C1-E16. Obtain energy independently from pressure work in C1-E17. Check the chosen Mach cutoff using C1-E19 before interpreting the singular trajectory.',
    '重现塌缩推导链，不能背诵系数。采用 C1-E13 的速度平方和积分因子。按 C1-E14 施加初始条件。按 C1-E15–C1-E16 积分向内速度倒数。按 C1-E17 独立用压力功求能量。解释奇异轨迹前，先用 C1-E19 检查选定马赫截止条件。',
    r'''\begin{aligned}
    y&=\dot R^2,\quad\frac{d(R^3y)}{dR}=-2\Delta p_cR^2/\rho,\\
    R^3y-0&=-\frac{2\Delta p_c}{3\rho}(R^3-R_{\max}^3),\\
    \dot R&=-\sqrt{y},\quad
    t_c=R_{\max}\sqrt{\frac{3\rho}{2\Delta p_c}}\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,dx,\\
    K_l&=\int_{V_{\max}}^{V_b}-\Delta p_c\,dV=\Delta p_c(V_{\max}-V_b).
    \end{aligned}''',
    r'$y$ is squared speed (m² s⁻²); $x=R/R_{\max}$ is dimensionless radius; $V_b=4\pi R^3/3$ and $V_{\max}=4\pi R_{\max}^3/3$ are volumes (m³); $V$ is dummy volume (m³).',
    r'$y$ 为速度平方（m² s⁻²）；$x=R/R_{\max}$ 为无量纲半径；$V_b=4\pi R^3/3$ 与 $V_{\max}=4\pi R_{\max}^3/3$ 为体积（m³）；$V$ 为积分哑体积（m³）。',
    'Falsification question: do gas pressure, capillarity, viscosity, compressibility or deformation cease to be negligible before the radius of interest? Finite pressure work remains compatible with unbounded ideal speed because the effective radial inertia vanishes. Physical maximum: Not established.',
    '证伪问题：在目标半径之前，气体压力、毛细、黏性、可压缩性或变形是否已不可忽略？有效径向惯性趋于零，因此有限压力功与理想速度无界并不矛盾。实际最大值：尚未建立。')

step(33,
    'Start with the exact time-integrated momentum in C1-E21. Apply C1-E22 conditions before discarding residual integrals. Use C1-E23 endpoint data to solve the spatial impulse field. C1-E30 separately tests communication using rise time. These steps determine an initial velocity increment; subsequent jet shape requires the moving-interface solve.',
    '从 C1-E21 的精确时间积分动量出发。先检查 C1-E22 条件，再舍去残余积分。采用 C1-E23 的端点条件求空间冲量场。C1-E30 用上升时间单独检验通信。这些步骤确定初始速度增量；后续射流形状仍需运动界面求解。',
    r'''\begin{aligned}
    \Delta\boldsymbol u&=-\nabla\Pi/\rho
       -\int_{t_0}^{t_1}(\boldsymbol u\cdot\nabla)\boldsymbol u\,dt
       +\nu\int_{t_0}^{t_1}\nabla^2\boldsymbol u\,dt,\\
    U\tau/L\ll1,\quad\nu\tau/L^2\ll1
       &\Rightarrow\Delta\boldsymbol u\simeq-\nabla\Pi/\rho,\\
    \nabla\cdot\Delta\boldsymbol u=0&\Rightarrow\nabla^2\Pi=0,\\
    \Pi(0)=\Pi_0,\quad\Pi(L)=0&\Rightarrow\Pi(z)=\Pi_0(1-z/L),\\
    \Delta u_z&=-\frac1\rho\frac{d\Pi}{dz}=\frac{\Pi_0}{\rho L}.
    \end{aligned}''',
    r'$\boldsymbol u$ is velocity (m s⁻¹); $\nu$ is kinematic viscosity (m² s⁻¹); $U$ is a characteristic speed (m s⁻¹); $\tau=t_1-t_0$ is event duration (s); $z\in[0,L]$ is column coordinate (m); $\Delta u_z$ is axial speed increment (m s⁻¹); $\ll$ is an asymptotic smallness condition.',
    r'$\boldsymbol u$ 为速度（m s⁻¹）；$\nu$ 为运动黏度（m² s⁻¹）；$U$ 为特征速度（m s⁻¹）；$\tau=t_1-t_0$ 为事件时长（s）；$z\in[0,L]$ 为液柱坐标（m）；$\Delta u_z$ 为轴向速度增量（m s⁻¹）；$\ll$ 表示渐近很小条件。',
    'Falsification question: does the observer stay liquid, and are geometry motion, residual impulses and acoustic rise effects small? Report location, duration, geometry and reference pressure with every impulse. Equal scalar peaks cannot determine the spatial gradient.',
    '证伪问题：观察点是否始终位于液体内，几何运动、残余冲量和声学上升效应是否足够小？报告每个冲量时须给出位置、时长、几何及参考压力。相同标量峰值不能确定空间梯度。')

assert set(STEPS) == {f'C1-E{n:02d}' for n in range(1,34)}
