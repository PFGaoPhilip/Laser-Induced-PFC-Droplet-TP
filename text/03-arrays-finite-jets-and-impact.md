# Arrays, finite jets and measurable impact

# 阵列、有限射流与可测冲击

## 1. Define the array, its energy constraint, and the desired output

## 1. 定义阵列、能量约束及所需输出

Our objective is to follow a finite laser-activated array from individual cavity histories to an emitted liquid jet, coherent arrival, and pressure measured at a stated receiver. Chapter 2 supplies each site's heat input, finite PFC inventory, and internal-pressure history. Here we solve mechanical controls with declared source histories; we do not claim to have calculated a target PFC jet maximum. The carrier liquid supplies most of the moving mass. Internal bubble pressure, external jet speed, exposed-surface pressure, and buried-interface traction remain distinct outputs.

本章目标是沿有限激光激活阵列，追踪各腔体历程、喷出液体射流、相干到达，以及规定接收位置的实测压力。第二章提供各位点热输入、有限 PFC 储量及内部压力历程。本章在声明源历程的条件下求解力学对照，并不声称已算出目标 PFC 射流的最大值。运动质量主要来自载液。气泡内部压力、外部射流速度、暴露表面压力及埋藏界面牵引仍是不同输出。

Use fixed Cartesian bubble centers for the first interaction model; neglect center translation, gravity, walls, coalescence and shape modes. Require nearly spherical bubbles, radius much smaller than separation, low wall Mach number, and pressure communication faster than the radial event. At time zero the ideal-collapse controls start at their maximum radius with zero wall velocity, with constant positive ambient-minus-bubble pressure. Real PFC pressures must instead be coupled to Chapter 2. The spatial launch problem later uses the actual walls, outlets and moving interfaces. Its liquid-to-gas normal defines positive curvature for an exterior cylindrical jet and negative curvature for an interior spherical cavity.

第一种相互作用模型采用固定 Cartesian 气泡中心，忽略中心平移、重力、壁面、合并及形状模态。要求气泡接近球形、半径远小于间距、壁面 Mach 数小，且压力传播快于径向事件。理想塌缩对照在零时刻从最大半径及零壁速开始，环境压力减去泡内压力为恒定正值。实际 PFC 压力则必须与第二章耦合。后续空间发射问题采用实际壁面、出口及运动界面。液体指向气体的法向，使外部圆柱射流曲率为正、内部球腔曲率为负。

| Symbol family  符号组 | Meaning and units  含义与单位 |
| --- | --- |
| $i,j=1,\ldots,N\_b$; $N\_d,N\_b$  $i,j=1,\ldots,N\_b$；$N\_d,N\_b$ | Bubble indices; fabricated-site count and activated-bubble count (dimensionless).  气泡编号；制造位点数及已激活气泡数（无量纲）。 |
| $R\_i,d\_{ij},s,R\_{\max}$  $R\_i,d\_{ij},s,R\_{\max}$ | Radius, center distance, nearest-vertex pitch and maximum radius (m). Newton dots denote time derivatives.  半径、中心距离、相邻顶点间距及最大半径（m）；Newton 点表示时间导数。 |
| $\rho,\mu,\sigma\_b,\sigma\_j,c$  $\rho,\mu,\sigma\_b,\sigma\_j,c$ | Carrier density (kg m⁻³), viscosity (Pa s), bubble and jet surface tensions (N m⁻¹), sound speed (m s⁻¹).  载液密度（kg m⁻³）、黏度（Pa s）、气泡及射流表面张力（N m⁻¹）、声速（m s⁻¹）。 |
| $\phi,\Pi,\boldsymbol u$  $\phi,\Pi,\boldsymbol u$ | Velocity potential (m² s⁻¹), pressure impulse per area (Pa s), velocity field (m s⁻¹).  速度势（m² s⁻¹）、单位面积压力冲量（Pa s）、速度场（m s⁻¹）。 |
| $E,m,P,\mathcal J$  $E,m,P,\mathcal J$ | Energy (J), liquid mass (kg), directional momentum (N s), delivered force impulse (N s). Labels identify the particular system.  能量（J）、液体质量（kg）、方向动量（N s）、传递的力冲量（N s）；下标区分具体系统。 |
| $a\_j,d\_j,L\_j,H,z$  $a\_j,d\_j,L\_j,H,z$ | Jet radius, diameter, emitted length, flight gap and axial coordinate (m).  射流半径、直径、喷出长度、飞行间隙及轴向坐标（m）。 |
| $S,\chi,C(\chi),b\_i$  $S,\chi,C(\chi),b\_i$ | Neighbor reciprocal-distance sum (m⁻¹), interaction parameter, collapse-time coefficient (dimensionless), and source strength (m³ s⁻¹).  邻距倒数和（m⁻¹）、相互作用参数、塌缩时间系数（无量纲）及源强度（m³ s⁻¹）。 |
| $\Gamma,\Omega,\boldsymbol n,\kappa$  $\Gamma,\Omega,\boldsymbol n,\kappa$ | Moving interface, liquid domain, unit normal pointing out of liquid, and signed curvature (m⁻¹).  运动界面、液体域、指向液体外部的单位法向及带符号曲率（m⁻¹）。 |
| $g,\delta,k,q,I\_0,I\_1$  $g,\delta,k,q,I\_0,I\_1$ | Disturbance growth rate (s⁻¹; not gravity), amplitude (m), wavenumber (m⁻¹), dimensionless wavenumber and modified Bessel functions. The pitch remains the distinct symbol s.  扰动增长率（s⁻¹；并非重力）、振幅（m）、波数（m⁻¹）、无量纲波数及修正 Bessel 函数；间距保留为另一符号 s。 |
| $Z\_l,Z\_r,A\_o,\tau\_o,p\_{\mathrm{obs}}$  $Z\_l,Z\_r,A\_o,\tau\_o,p\_{\mathrm{obs}}$ | Liquid/receiver impedance (Pa s m⁻¹), observer area (m²), averaging time (s) and observed mean excess pressure (Pa).  液体／接收体阻抗（Pa s m⁻¹）、观察面积（m²）、平均时间（s）及观察平均超压（Pa）。 |
| $\partial\_t,\nabla,\nabla^2,\int,\sum$  $\partial\_t,\nabla,\nabla^2,\int,\sum$ | Fixed-position time derivative, spatial gradient/Laplacian, integral and finite sum. Powers are arithmetic powers; subscripts label sites or physical roles.  固定位置时间导数、空间梯度／Laplace 算子、积分及有限求和。上标幂为算术幂；下标表示位点或物理作用。 |

Step 1 — distinguish five uniformities: core inventory, carrier volume, pitch, optical fluence and activation time. Separate liquid cells can be summed only after their finite outputs and arrival times are known. Bubbles sharing a liquid domain move common liquid and modify one another's ambient pressure. A regular pattern therefore supplies geometry, not a count-proportional pressure law.

步骤 1——区分五种均匀性：芯部储量、载液体积、间距、光学通量及激活时间。分隔液体单元只能在有限输出及到达时间已知后求和。共享液体域的气泡推动共同液体，并改变彼此的周围压力。因此规则排列只提供几何，并不提供压力正比于数量的定律。

**Symbols before Eq. (C3-E01).** $N\_d$ is positive integer site count; $N\_b$ is the random activated count; $p\_a\in(0,1]$ is identical independent activation probability. $\mathbb E$, $\operatorname{Var}$ and $\Pr$ denote expectation, variance and probability; $\mathrm{CV}$ is standard deviation divided by nonzero mean. All are dimensionless.

**式（C3-E01）前的符号定义。** $N\_d$ 是正整数位点数；$N\_b$ 为随机已激活数量；$p\_a\in(0,1]$ 为相同且相互独立的激活概率。$\mathbb E$、$\operatorname{Var}$、$\Pr$ 分别表示期望、方差、概率；$\mathrm{CV}$ 是标准差除以非零均值。所有量均无量纲。

(C3-E01) · Independent-event statistical model$$
\begin{aligned}\mathbb E[N\_b]&=N\_dp\_a,\quad \operatorname{Var}(N\_b)=N\_dp\_a(1-p\_a),\\ \mathrm{CV}(N\_b)&=\frac{\sqrt{N\_dp\_a(1-p\_a)}}{N\_dp\_a}=\sqrt{\frac{1-p\_a}{N\_dp\_a}},\quad \Pr(N\_b=N\_d)=p\_a^{N\_d}.\end{aligned}
$$
![Count reproducibility and complete activation are different tests.](../assets/figures/c3-e01.svg)

Count reproducibility and complete activation are different tests.

数量重复性与全部激活是不同检验。

For 25 sites and activation probability 0.95, the mean count is 23.75 and relative standard deviation is 4.588%. Nevertheless, complete activation occurs with probability 0.27739. This calculation assumes independent Bernoulli trials; common heating and mechanical feedback can invalidate it. Counting bubbles alone does not verify a fully actuated, symmetric load.

25 个位点、激活概率 0.95 时，平均数量为 23.75，相对标准差为 4.588%。然而全部激活概率仅为 0.27739。该计算假设独立 Bernoulli 试验；共同加热及力学反馈可破坏这一假设。仅统计气泡数量不能核验完全激活的对称载荷。

**Symbols before Eq. (C3-E02).** $F(r)$ is Gaussian pulse fluence at radial distance $r$ (J m⁻²); $F\_0>0$ is central fluence. $R\_A>0$ encloses the array and $w>0$ is the Gaussian 1/e² radius (m). $\epsilon\in(0,1)$ is allowed fractional edge decrease. $\exp$ and $\ln$ are exponential and natural logarithm of dimensionless arguments.

**式（C3-E02）前的符号定义。** $F(r)$ 是径向距离 $r$ 处的 Gaussian 脉冲通量（J m⁻²）；$F\_0>0$ 为中心通量。$R\_A>0$ 包围阵列，$w>0$ 为 Gaussian 的 1/e² 半径（m）。$\epsilon\in(0,1)$ 是允许的边缘相对降低量。$\exp$、$\ln$ 分别为无量纲自变量的指数及自然对数。

(C3-E02) · Derived optical-uniformity condition$$
\frac{F(R\_A)}{F\_0}=\exp(-2R\_A^2/w^2)\ge1-\epsilon\ \Longrightarrow\ w^2\ge\frac{2R\_A^2}{-\ln(1-\epsilon)}\ \Longrightarrow\ w\ge R\_A\sqrt{\frac{2}{-\ln(1-\epsilon)}}.
$$
![An optical condition can be checked before solving cavity mechanics.](../assets/figures/c3-e02.svg)

An optical condition can be checked before solving cavity mechanics.

求解腔体力学前即可检验光学条件。

Taking logarithms preserves order because the logarithm is increasing. Multiplying by minus one reverses the inequality; the denominator is positive because the allowed decrease lies between zero and one. A 10% decrease requires a beam radius at least 4.35688 times the enclosing array radius. Increasing beam width can improve uniformity while increasing energy deposited outside the array. This does not determine the absorbed energy at individual cores.

对数单调递增，因此取对数保持不等号方向；乘以负一使不等号反向。允许降低量位于零与一之间，故分母为正。允许降低 10% 时，束半径至少为包围阵列半径的 4.35688 倍。增大束宽可以改善均匀性，同时增加阵列外能量沉积。该条件并不确定各芯部吸收的能量。

## 2. Derive the first bubble–bubble interaction from the velocity potential

## 2. 从速度势推导首阶气泡相互作用

Step 2 — use incompressibility to obtain one source. At a distance from a fixed spherical center, radial volume flux is constant over concentric spheres. Integrate the velocity radially and choose zero potential at infinity. For another well-separated center the source potential is almost spatially uniform over that bubble. Its fixed-position time derivative supplies the leading surrounding-pressure correction through unsteady Bernoulli.

步骤 2——利用不可压缩性得到单个源。在距固定球形中心的不同位置，同心球面上的径向体积流率相同。对速度作径向积分，并取无穷远速度势为零。对另一个充分分离的中心，该源势在目标气泡表面近乎空间均匀。通过非定常 Bernoulli，其固定位置时间导数提供首阶周围压力修正。

**Symbols before Eq. (C3-E03).** $j$ labels the emitting bubble and $i\ne j$ a receiving center. $R\_j(t)>0$, $r\_j\ge R\_j$, dummy radius $\xi$ and fixed $d\_{ij}>0$ are lengths (m); $t$ is time (s). $\dot R\_j,\ddot R\_j$ are radius derivatives (m s⁻¹, m s⁻²). $u\_j$ is radial velocity (m s⁻¹); $\phi\_j$ is velocity potential (m² s⁻¹). $\partial\_t$ holds position fixed; $\int$ is radial integration, $\infty$ the zero-potential far field; $\pi$ is dimensionless.

**式（C3-E03）前的符号定义。** $j$ 标记发射气泡，$i\ne j$ 标记接收中心。$R\_j(t)>0$、$r\_j\ge R\_j$、积分半径 $\xi$ 及固定 $d\_{ij}>0$ 均为长度（m）；$t$ 为时间（s）。$\dot R\_j$、$\ddot R\_j$ 为半径时间导数（m s⁻¹、m s⁻²）。$u\_j$ 为径向速度（m s⁻¹）；$\phi\_j$ 为速度势（m² s⁻¹）。$\partial\_t$ 保持位置固定；$\int$ 为径向积分，$\infty$ 为速度势为零的远场；$\pi$ 无量纲。

(C3-E03) · Continuity and potential integration$$
\begin{aligned}4\pi r\_j^2u\_j(r\_j,t)&=4\pi R\_j^2\dot R\_j,\\ \phi\_j(r\_j,t)&=\int\_{\infty}^{r\_j}\frac{R\_j^2\dot R\_j}{\xi^2}\,d\xi=-\frac{R\_j^2\dot R\_j}{r\_j},\\ \partial\_t\phi\_j\big|\_{r\_j=d\_{ij}}&=-\frac{2R\_j\dot R\_j^2+R\_j^2\ddot R\_j}{d\_{ij}}.\end{aligned}
$$
![A moving spherical volume produces a monopole potential.](../assets/figures/c3-e03.svg)

A moving spherical volume produces a monopole potential.

运动球体体积产生单极子速度势。

**Symbols before Eq. (C3-E04).** $i,j=1,\ldots,N\_b$ are distinct bubble indices; $p'\_{j\to i}$ is source $j$'s pressure disturbance at $i$, $p\_{\mathrm{ext},i}$ external pressure and $p\_\infty$ remote pressure (Pa). $\rho$ is constant carrier density (kg m⁻³); $\phi\_j$ is potential (m² s⁻¹); $t$ is time (s), $\partial\_t$ its fixed-position derivative. $R\_j,d\_{ij}$ are positive lengths (m), dots time derivatives. $\sum\_{j\ne i}$ adds all other sources; $\simeq$ marks the leading far-separated approximation.

**式（C3-E04）前的符号定义。** $i,j=1,\ldots,N\_b$ 为不同气泡编号；$p'\_{j\to i}$ 是源 $j$ 在 $i$ 处的压力扰动，$p\_{\mathrm{ext},i}$ 为外压，$p\_\infty$ 为远场压力（Pa）。$\rho$ 为恒定载液密度（kg m⁻³）；$\phi\_j$ 为速度势（m² s⁻¹）；$t$ 为时间（s），$\partial\_t$ 为固定位置导数。$R\_j$、$d\_{ij}$ 为正长度（m），点表示时间导数。$\sum\_{j\ne i}$ 对其他源求和；$\simeq$ 表示充分分离时的首阶近似。

(C3-E04) · Leading unsteady-Bernoulli approximation$$
p'\_{j\to i}\simeq-\rho\partial\_t\phi\_j(d\_{ij},t)=\frac{\rho}{d\_{ij}}(R\_j^2\ddot R\_j+2R\_j\dot R\_j^2),\qquad p\_{\mathrm{ext},i}\simeq p\_\infty+\sum\_{j\ne i}p'\_{j\to i}.
$$
![The correction changes surrounding pressure; it is not a new energy reservoir.](../assets/figures/c3-e04.svg)

The correction changes surrounding pressure; it is not a new energy reservoir.

该修正改变周围压力，并不增加新的能量库。

The product rule supplies both terms in the numerator; keeping only the radius acceleration would be inconsistent. Each term divided by separation has unit m² s⁻², which density converts to pressure. The omitted squared-speed Bernoulli term, nonuniform pressure over the receiver, translation and reflected fields must remain small. Positive volume acceleration raises surrounding pressure; the correction can have either sign during a full event. A pressure-lowered surface-cavitation experiment shows shielding and later collapse of interior bubbles, with spherical modeling failing during final jetting. That is a relevant interaction benchmark, not a laser-PFC calibration. [Bremond et al. (2006)](https://doi.org/10.1103/PhysRevLett.96.224501)

分子两项均由乘积法则产生；仅保留半径加速度项不自洽。各项除以间距后单位为 m² s⁻²，再乘密度即为压力。被忽略的 Bernoulli 速度平方项、接收泡上的非均匀压力、平移及反射场必须足够小。体积正加速度升高周围压力；完整事件中修正可以取两种符号。降压表面空化实验显示内部气泡受到屏蔽并延迟塌缩，最终射流阶段球形模型失效。它是相关相互作用对照，而非激光 PFC 标定。[Bremond 等（2006）](https://doi.org/10.1103/PhysRevLett.96.224501)

**Symbols before Eq. (C3-E05).** $i,j$ index activated bubbles; $R\_i,R\_j,d\_{ij}>0$ are lengths (m), dots are time derivatives. $p\_{b,i}$ is bubble $i$'s internal pressure and $p\_\infty$ remote pressure (Pa). $\sigma\_b$ is bubble–carrier tension (N m⁻¹), $\mu$ carrier dynamic viscosity (Pa s), $\rho$ carrier density (kg m⁻³). $B\_i$ is the isolated radial driving expression (m² s⁻²); $\sum\_{j\ne i}$ sums other sources. Every term has unit m² s⁻².

**式（C3-E05）前的符号定义。** $i,j$ 标记已激活气泡；$R\_i,R\_j,d\_{ij}>0$ 为长度（m），点为时间导数。$p\_{b,i}$ 为第 $i$ 个气泡内压，$p\_\infty$ 为远场压力（Pa）。$\sigma\_b$ 为泡—载液张力（N m⁻¹），$\mu$ 为载液动力黏度（Pa s），$\rho$ 为载液密度（kg m⁻³）。$B\_i$ 为孤立泡径向驱动表达式（m² s⁻²）；$\sum\_{j\ne i}$ 对其他源求和。各项单位均为 m² s⁻²。

(C3-E05) · Coupled spherical approximation$$
\begin{aligned}R\_i\ddot R\_i+\frac32\dot R\_i^2+\sum\_{j\ne i}\frac{R\_j^2\ddot R\_j+2R\_j\dot R\_j^2}{d\_{ij}}&=B\_i,\\ B\_i&=\frac{p\_{b,i}-p\_\infty-2\sigma\_b/R\_i-4\mu\dot R\_i/R\_i}{\rho}.\end{aligned}
$$
![Substitute the corrected external pressure into each radial balance.](../assets/figures/c3-e05.svg)

Substitute the corrected external pressure into each radial balance.

将修正外压代入各径向平衡。

Step 3 — move the neighbor-pressure term to the left, producing Eq. (C3-E05). This is a coupled acceleration system, not a collection of isolated trajectories followed by multiplying their pressures. The phase-pressure law still belongs to each individual site. Taking separations to infinity removes the interaction terms and recovers the single-bubble equation. Taking radii comparable to separation violates the approximation even if the formula can still be evaluated numerically.

步骤 3——将邻泡压力项移至左侧，得到式（C3-E05）。这是耦合加速度系统，并非先各自求孤立轨迹，再相乘压力。相变压力规律仍属于各个位点。间距趋于无穷时相互作用项消失，还原单泡方程。半径与间距相当时，即使数值上仍可代入，近似也已失效。

## 3. Work the three-, four-, and five-bubble controls; then fix total energy

## 3. 求解三、四、五泡对照，再固定总能量

Step 4 — constrain identical cavities to a regular polygon, with identical initial data and pressure histories. Cyclic symmetry makes each neighbor-distance sum equal, permitting one shared radius. The following distance formula derives the sums instead of treating bubble count as a coefficient. Here pitch means neighboring-vertex distance, not polygon circumradius.

步骤 4——将相同腔体约束在正多边形顶点，采用相同初值与压力历程。循环对称使各点邻距和相等，从而允许统一半径。下式推导距离和，而不是把气泡数量当作系数。此处间距指相邻顶点距离，并非外接圆半径。

**Symbols before Eq. (C3-E06).** $N\in\{3,4,5\}$ is regular-polygon bubble count; $k=1,\ldots,N-1$ counts steps from one vertex. $s>0$ and $d\_k>0$ are neighboring-vertex and $k$-step center distances (m). $S\_N$ is the reciprocal-distance sum (m⁻¹). $\varphi\_g$ is the dimensionless golden ratio; $\sin$ takes angles in radians, $\pi$ is dimensionless, and $\sum$ sums the stated steps.

**式（C3-E06）前的符号定义。** $N\in\{3,4,5\}$ 为正多边形气泡数；$k=1,\ldots,N-1$ 为从一个顶点出发的步数。$s>0$、$d\_k>0$ 为相邻及相隔 $k$ 步的中心距离（m）。$S\_N$ 为距离倒数和（m⁻¹）。$\varphi\_g$ 为无量纲黄金比；$\sin$ 的角度采用弧度，$\pi$ 无量纲；$\sum$ 对规定步数求和。

(C3-E06) · Exact polygon geometry$$
\begin{aligned}d\_k&=s\frac{\sin(k\pi/N)}{\sin(\pi/N)},\qquad S\_N=\sum\_{k=1}^{N-1}\frac1{d\_k},\\ S\_3&=\frac2s,\qquad S\_4=\frac{2+1/\sqrt2}{s},\qquad S\_5=\frac{2+2/\varphi\_g}{s},\quad\varphi\_g=\frac{1+\sqrt5}{2}.\end{aligned}
$$
![Equal geometric sums justify a shared radial trajectory in this constrained control.](../assets/figures/c3-e06.svg)

Equal geometric sums justify a shared radial trajectory in this constrained control.

相同几何和使这一约束对照可采用共同径向轨迹。

**Symbols before Eq. (C3-E07).** $p\_\infty,p\_b$ are constant ambient and internal pressure (Pa), $\Delta p\_c>0$ their collapse-driving difference. $S=S\_N\ge0$ is the fixed reciprocal-distance sum (m⁻¹); $R(t)>0$ and $R\_{\max}>0$ are shared and initial maximum radius (m). Dots are time derivatives, $t=0$ the initial time (s); $\rho>0$ is carrier density (kg m⁻³). Surface tension and viscosity are omitted in this ideal control; $SR$ is dimensionless.

**式（C3-E07）前的符号定义。** $p\_\infty$、$p\_b$ 为恒定环境及泡内压力（Pa），$\Delta p\_c>0$ 为其塌缩驱动压差。$S=S\_N\ge0$ 为固定距离倒数和（m⁻¹）；$R(t)>0$、$R\_{\max}>0$ 为共同及初始最大半径（m）。点为时间导数，$t=0$ 为初始时刻（s）；$\rho>0$ 为载液密度（kg m⁻³）。本理想对照忽略表面张力及黏度；$SR$ 无量纲。

(C3-E07) · Symmetric constant-pressure collapse control$$
\begin{aligned}\Delta p\_c&=p\_\infty-p\_b>0,\qquad S=S\_N,\\ (1+SR)R\ddot R+\left(\frac32+2SR\right)\dot R^2&=-\frac{\Delta p\_c}{\rho},\qquad R(0)=R\_{\max},\quad\dot R(0)=0.\end{aligned}
$$
![Substitution of the common radius collects the two interaction contributions.](../assets/figures/c3-e07.svg)

Substitution of the common radius collects the two interaction contributions.

代入共同半径后合并两种相互作用贡献。

Step 5 — solve the reduced equation on the inward branch. Away from the initial turning point, introduce squared wall speed as a function of radius. Its derivative is twice wall acceleration by the chain rule. The resulting linear equation has integrating factor proportional to radius cubed times the interaction factor; the logarithmic derivatives shown below establish that choice. The solution extends continuously to the initial zero-speed point.

步骤 5——求解缩小分支。离开初始转折点后，将壁速平方视为半径的函数。链式法则使其半径导数等于两倍壁加速度。所得线性方程的积分因子正比于半径三次方乘相互作用因子；下示对数导数证明这一选择。解连续延伸至初始零速度点。

**Symbols before Eq. (C3-E08).** $y(R)\ge0$ is squared wall speed (m² s⁻²), $y'=dy/dR$ (m s⁻²); $R>0$ is radius (m) and dots its time derivatives. $S\ge0$ is neighbor sum (m⁻¹), $\rho>0$ density (kg m⁻³), $\Delta p\_c>0$ pressure difference (Pa). $\ell\_\*>0$ is an arbitrary constant reference length (m), inserted solely to make the logarithm dimensionless; it cancels from the integrating factor. $\ln$ is natural logarithm; $d/dR$ differentiates in radius. Division by $\dot R$ is used only on the moving branch.

**式（C3-E08）前的符号定义。** $y(R)\ge0$ 为壁速平方（m² s⁻²），$y'=dy/dR$（m s⁻²）；$R>0$ 为半径（m），点表示其时间导数。$S\ge0$ 为邻距和（m⁻¹），$\rho>0$ 为密度（kg m⁻³），$\Delta p\_c>0$ 为压差（Pa）。$\ell\_\*>0$ 为任意恒定参考长度（m），仅用来使对数无量纲，并在积分因子中抵消。$\ln$ 为自然对数；$d/dR$ 对半径求导。仅在运动分支除以 $\dot R$。

(C3-E08) · Chain rule and integrating-factor derivation$$
\begin{aligned}y(R)&=\dot R^2,\quad \frac{dy}{dR}=\frac{2\dot R\ddot R}{\dot R}=2\ddot R\quad(\dot R\ne0),\\ y'+\frac{3+4SR}{R(1+SR)}y&=-\frac{2\Delta p\_c}{\rho R(1+SR)},\\ \frac{3+4SR}{R(1+SR)}&=\frac3R+\frac S{1+SR}=\frac{d}{dR}\ln[R^3(1+SR)/\ell\_\*^3],\\ \frac{d}{dR}\left[R^3(1+SR)y\right]&=-\frac{2\Delta p\_c}{\rho}R^2.\end{aligned}
$$
![Every term of the integrating factor can be reconstructed from the radial equation.](../assets/figures/c3-e08.svg)

Every term of the integrating factor can be reconstructed from the radial equation.

积分因子的每一项均可从径向方程重构。

**Symbols before Eq. (C3-E09).** $R\in(0,R\_{\max}]$ and $R\_{\max}$ are current/maximum radius (m); $\xi$ is dummy radius (m), dots radius time derivatives. $y=\dot R^2$ (m² s⁻²), $S\ge0$ neighbor sum (m⁻¹), $\rho>0$ density (kg m⁻³), $\Delta p\_c>0$ pressure difference (Pa). Brackets mean upper minus lower endpoint, $\int$ definite integration and $\sqrt{\ }$ the nonnegative root; the explicit minus sign selects collapse.

**式（C3-E09）前的符号定义。** $R\in(0,R\_{\max}]$、$R\_{\max}$ 为当前／最大半径（m）；$\xi$ 为积分半径（m），点为半径时间导数。$y=\dot R^2$（m² s⁻²），$S\ge0$ 为邻距和（m⁻¹），$\rho>0$ 为密度（kg m⁻³），$\Delta p\_c>0$ 为压差（Pa）。方括号表示上端减下端，$\int$ 为定积分，$\sqrt{\ }$ 取非负根；显式负号选择塌缩。

(C3-E09) · Integrated solution on the inward branch$$
\begin{aligned}[R^3(1+SR)y]\_{R\_{\max}}^R&=-\frac{2\Delta p\_c}{\rho}\int\_{R\_{\max}}^R\xi^2d\xi=\frac{2\Delta p\_c}{3\rho}(R\_{\max}^3-R^3),\\ \dot R^2&=\frac{2\Delta p\_c}{3\rho}\frac{R\_{\max}^3-R^3}{R^3(1+SR)},\qquad \dot R=-\sqrt{\frac{2\Delta p\_c}{3\rho}\frac{R\_{\max}^3-R^3}{R^3(1+SR)}}.\end{aligned}
$$
![The initial condition removes the integration constant and the physical branch fixes the sign.](../assets/figures/c3-e09.svg)

The initial condition removes the integration constant and the physical branch fixes the sign.

初值消去积分常数，物理分支固定符号。

**Symbols before Eq. (C3-E10).** $t\_c$ is formal collapse time (s); $R,R\_{\max}>0$ are radii (m), $\dot R$ wall velocity (m s⁻¹), $|\ |$ absolute value. $\rho$ is density (kg m⁻³), $\Delta p\_c>0$ pressure difference (Pa), $S\ge0$ neighbor sum (m⁻¹). $x\in[0,1]$ is dimensionless integration radius and $\chi\ge0$ interaction strength. $C$ and $C'=dC/d\chi$ are dimensionless; integrals are convergent improper integrals at $x=1$.

**式（C3-E10）前的符号定义。** $t\_c$ 为形式塌缩时间（s）；$R,R\_{\max}>0$ 为半径（m），$\dot R$ 为壁速（m s⁻¹），$|\ |$ 为绝对值。$\rho$ 为密度（kg m⁻³），$\Delta p\_c>0$ 为压差（Pa），$S\ge0$ 为邻距和（m⁻¹）。$x\in[0,1]$ 为无量纲积分半径，$\chi\ge0$ 为相互作用强度。$C$ 及 $C'=dC/d\chi$ 无量纲；积分在 $x=1$ 处为收敛广义积分。

(C3-E10) · Collapse-time quadrature and sign check$$
\begin{aligned}t\_c&=\int\_0^{R\_{\max}}\frac{dR}{|\dot R|}=R\_{\max}\sqrt{\frac{\rho}{\Delta p\_c}}\,C(\chi),\quad x=R/R\_{\max},\quad\chi=SR\_{\max},\\ C(\chi)&=\sqrt{\frac32}\int\_0^1\sqrt{\frac{x^3(1+\chi x)}{1-x^3}}\,dx,\\ C'(\chi)&=\frac12\sqrt{\frac32}\int\_0^1\frac{x^{5/2}}{\sqrt{(1-x^3)(1+\chi x)}}\,dx>0\quad(\chi\ge0).\end{aligned}
$$
![Shared-liquid interaction increases this constrained collapse time.](../assets/figures/c3-e10.svg)

Shared-liquid interaction increases this constrained collapse time.

共享液体相互作用使这一约束塌缩时间增加。

At the upper endpoint the integrand is proportional to the inverse square root of the distance to the endpoint, so it is integrable. The differentiated integrand is positive and has the same integrable endpoint form, justifying both differentiation and monotonicity. For zero interaction, substitution of cubed radius reproduces the Chapter 1 Rayleigh coefficient 0.9146813565. Numerical quadrature for radius 30 μm, pitch 200 μm, density 1000 kg m⁻³ and pressure difference 100 kPa yields the following controls. Maximum radius divided by nearest distance is 0.15: a leading approximation, not an error-certified exact prediction.

上端积分函数正比于距端点距离的负二分之一次方，因此可积。求导后积分函数为正，并保持同一可积端点形式，从而支持交换求导与积分及单调性。零相互作用时，以半径三次方作变量代换，还原第一章 Rayleigh 系数 0.9146813565。对半径 30 μm、间距 200 μm、密度 1000 kg m⁻³、压差 100 kPa 作数值积分，得到下列对照。最大半径与最近距离之比为 0.15：属于首阶近似，并非有误差保证的精确预测。

| Configuration  构型 | $\chi$  $\chi$ | $C(\chi)$  $C(\chi)$ | Formal time (μs)  形式时间（μs） |
| --- | --- | --- | --- |
| Isolated  孤立 | 0  0 | 0.914681  0.914681 | 2.744044  2.744044 |
| Triangle  正三角形 | 0.300000  0.300000 | 1.019836  1.019836 | 3.059509  3.059509 |
| Square  正方形 | 0.406066  0.406066 | 1.054396  1.054396 | 3.163188  3.163188 |
| Pentagon  正五边形 | 0.485410  0.485410 | 1.079497  1.079497 | 3.238492  3.238492 |

Step 6 — verify the shared-liquid kinetic energy, including the pair cross terms. Green's identity converts an interaction integral to the emitting bubble boundary; the outward normal of the liquid points into the cavity. A positive outward bubble velocity therefore gives a negative liquid-normal derivative. Multiplying two negative boundary factors makes the cross contribution positive for synchronized motion.

步骤 6——核验包含两泡交叉项的共享液体动能。Green 恒等式将相互作用积分转换至发射泡边界；液体外法向指入腔体。因此向外的正泡壁速度对应负的液体法向导数。两个负的边界因子相乘，使同步运动的交叉贡献为正。

**Symbols before Eq. (C3-E11).** $K\_N$ is leading cluster liquid kinetic energy (J); $N$ count and $i,j$ site indices. $R\_i,R\_j$ are site radii, $r\_i$ radial distance from $i$, $d\_{ij}$ center separation, $R$ common radius, $R\_{\max}$ its initial maximum, $R\_{\max,N}$ fixed-total-work maximum and $R\_\*$ isolated reference radius (all m); dots are time derivatives. $b\_i,b\_j$ are source strengths $R\_i^2\dot R\_i,R\_j^2\dot R\_j$ (m³ s⁻¹); $\phi\_i,\phi\_j$ source potentials (m² s⁻¹), $\Omega$ liquid domain and $\Gamma\_j$ bubble boundary. $\nabla$ gradient, $\partial\_n$ liquid-outward normal derivative, $dV,dA,dr\_i$ volume/area/radial elements (m³, m², m), $\int$ volume/surface/radial integral and $\sum$ finite sum; $i<j$ counts each unordered pair once; $|\ |$ is vector norm and $\infty$ the far radial endpoint. $S$ equal reciprocal-distance sum (m⁻¹), $\rho$ density (kg m⁻³), $\Delta p\_c$ pressure difference (Pa), $E\_{B,\mathrm{tot}}$ fixed initial work (J), $\pi$ dimensionless. Far separation justifies retaining self and leading pair integrals; $\*$ labels a reference.

**式（C3-E11）前的符号定义。** $K\_N$ 为首阶气泡群液体动能（J）；$N$ 为数量，$i,j$ 为位点编号。$R\_i,R\_j$ 为位点半径，$r\_i$ 为至 $i$ 的径距，$d\_{ij}$ 为中心间距，$R$ 为共同半径，$R\_{\max}$ 为其初始最大值，$R\_{\max,N}$ 为固定总做功最大半径，$R\_\*$ 为孤立参考半径（均为 m）；点为时间导数。$b\_i,b\_j$ 为源强度 $R\_i^2\dot R\_i,R\_j^2\dot R\_j$（m³ s⁻¹）；$\phi\_i,\phi\_j$ 为源势（m² s⁻¹），$\Omega$ 为液体域，$\Gamma\_j$ 为泡边界。$\nabla$ 为梯度，$\partial\_n$ 为液体外法向导数，$dV,dA,dr\_i$ 为体积／面积／径向微元（m³、m²、m），$\int$ 为体积／表面／径向积分，$\sum$ 为有限求和；$i<j$ 将各无序对计一次；$|\ |$ 为向量范数，$\infty$ 为径向远端。$S$ 为相同距离倒数和（m⁻¹），$\rho$ 为密度（kg m⁻³），$\Delta p\_c$ 为压差（Pa），$E\_{B,\mathrm{tot}}$ 为固定初始做功（J），$\pi$ 无量纲。充分分离使保留自身及首阶两泡积分成立；$\*$ 标记参考。

(C3-E11) · Leading-model energy check and fixed-total-work comparison$$
\begin{aligned}b\_i&=R\_i^2\dot R\_i,\quad \phi\_i=-b\_i/r\_i,\quad K\_N\simeq\frac{\rho}{2}\sum\_{i,j=1}^{N}\int\_\Omega\nabla\phi\_i\cdot\nabla\phi\_j\,dV,\\ \int\_\Omega|\nabla\phi\_i|^2\,dV&\simeq4\pi b\_i^2\int\_{R\_i}^\infty r\_i^{-2}\,dr\_i=4\pi R\_i^3\dot R\_i^2,\\ \int\_\Omega\nabla\phi\_i\cdot\nabla\phi\_j\,dV&\simeq\int\_{\Gamma\_j}\phi\_i\partial\_n\phi\_j\,dA\simeq(-b\_i/d\_{ij})(-\dot R\_j)4\pi R\_j^2=\frac{4\pi b\_ib\_j}{d\_{ij}}\quad(i\ne j),\\ K\_N&\simeq2\pi\rho\sum\_i R\_i^3\dot R\_i^2+4\pi\rho\sum\_{i<j}\frac{b\_ib\_j}{d\_{ij}}=2\pi\rho NR^3(1+SR)\dot R^2,\\ K\_N&=\frac{4\pi N}{3}\Delta p\_c(R\_{\max}^3-R^3)\quad\text{in the leading symmetric model},\\ E\_{B,\mathrm{tot}}&=N\frac{4\pi}{3}\Delta p\_c R\_{\max,N}^3=\frac{4\pi}{3}\Delta p\_c R\_\*^3,\quad R\_{\max,N}=R\_\*N^{-1/3}.\end{aligned}
$$
![The integrated trajectory conserves the leading energy budget.](../assets/figures/c3-e11.svg)

The integrated trajectory conserves the leading energy budget.

积分轨迹守恒首阶能量预算。

Integrating inverse squared radius gives the reciprocal lower radius because the far endpoint vanishes. The harmonic source from another bubble is nearly constant on the emitting surface, giving the shown pair integral. Ordered cross terms occur twice in the squared total gradient; unordered-pair notation supplies the coefficient four. For identical motion each bubble's reciprocal-distance sum is the same, so pair counting gives half the count times that sum. Substituting Eq. (C3-E09) cancels the interaction factor and equals released pressure work. At fixed total work take the positive cube root in the final row. With an isolated reference radius of 30 μm, three, four and five bubbles have radii 20.80084, 18.89882 and 17.54411 μm. At 200-μm pitch their formal times become 2.05687, 1.89946 and 1.77980 μs. Shorter time now reflects smaller cavities; it proves neither stronger jets nor optical-efficiency gain.

对半径负二次方积分，因远端为零，得到下端半径倒数。另一泡调和源在发射表面近乎恒定，得到所示两泡积分。总梯度平方中有序交叉项出现两次；无序对记号因此对应系数四。对相同运动，每泡倒距和相同，故两泡计数为数量乘该和再除以二。代入式（C3-E09）消去相互作用因子，等于释放的压力做功。固定总做功时，在最后一行取正立方根。孤立参考半径 30 μm 时，三、四、五泡半径分别为 20.80084、18.89882、17.54411 μm；间距 200 μm 时，形式时间分别为 2.05687、1.89946、1.77980 μs。此时时间变短源于腔体更小，并不证明射流更强或光学效率提高。

A center-and-four-arm cross is not a pentagon. If the arm length is the pitch, the center's reciprocal-distance sum is four divided by pitch; an outer site's sum is the sum of one, one half and the square root of two, divided by pitch. The different sums prevent an identical shared-radius history. Likewise, a large array needs an averaging length much larger than pitch and much smaller than macroscopic variation length before homogenization is justified; volume fraction alone does not supply that separation.

中心加四臂的十字并非正五边形。若臂长为间距，中心倒距和为四除以间距；外点倒距和为一、二分之一及根号二之和除以间距。不同距离和使相同共同半径历程无法维持。同理，大阵列需平均尺度远大于间距、远小于宏观变化尺度，才能支持均匀化；仅凭体积分数不能提供这种尺度分离。

**Symbols before Eq. (C3-E12).** $\phi\_b$ is dimensionless instantaneous bubble-volume fraction; $V\_i$ bubble volume and $V\_\Omega>0$ representative-region volume (m³), $N\_b$ bubble count, $R\_i,R,s$ radius/common cubic-lattice radius/pitch (m), $\pi$ dimensionless. $\phi(\boldsymbol x,t)$ is weak far-field potential (m² s⁻¹), $p'$ pressure disturbance (Pa), $\boldsymbol x$ observation position (m), $t$ time (s), $r\_i>0$ distance to source $i$ (m), $c$ sound speed (m s⁻¹), $\rho$ density (kg m⁻³). Dots on $V\_i$ are volume time derivatives (m³ s⁻¹, m³ s⁻²); $t-r\_i/c$ is retarded time. $\sum$ sums sources; $\simeq$ is a distant, compact, weak-source approximation.

**式（C3-E12）前的符号定义。** $\phi\_b$ 为无量纲瞬时气泡体积分数；$V\_i$ 为泡体积、$V\_\Omega>0$ 为代表区体积（m³），$N\_b$ 为泡数，$R\_i,R,s$ 为半径／立方晶格共同半径／间距（m），$\pi$ 无量纲。$\phi(\boldsymbol x,t)$ 为弱扰动远场势（m² s⁻¹），$p'$ 为压力扰动（Pa），$\boldsymbol x$ 为观察位置（m），$t$ 为时间（s），$r\_i>0$ 为至源 $i$ 的距离（m），$c$ 为声速（m s⁻¹），$\rho$ 为密度（kg m⁻³）。$V\_i$ 上的点为体积时间导数（m³ s⁻¹、m³ s⁻²）；$t-r\_i/c$ 为延迟时间。$\sum$ 对源求和；$\simeq$ 为远距、紧致、弱源近似。

(C3-E12) · Volume-fraction definition and retarded monopole approximation$$
\begin{aligned}\phi\_b&=\frac{\sum\_{i=1}^{N\_b}V\_i}{V\_\Omega},\quad V\_i=\frac{4\pi}{3}R\_i^3,\quad\phi\_b\big|\_{\mathrm{cubic}}=\frac{4\pi R^3}{3s^3},\\ \phi(\boldsymbol x,t)&\simeq-\sum\_i\frac{\dot V\_i(t-r\_i/c)}{4\pi r\_i},\qquad p'(\boldsymbol x,t)\simeq\sum\_i\frac{\rho}{4\pi r\_i}\ddot V\_i(t-r\_i/c).\end{aligned}
$$
![A spatial sum needs source histories and travel times, not only site count.](../assets/figures/c3-e12.svg)

A spatial sum needs source histories and travel times, not only site count.

空间求和需要源历程及传播时间，不能只给位点数。

Step 7 — replace instantaneous source time by retarded time only in the weak, compact-source wave control. Differentiate the far-field potential at fixed observation position to obtain the pressure row. Instantaneous bubble-volume fraction differs from initial liquid-PFC loading; a planar array needs a stated layer thickness before assigning region volume. This is a propagation estimate, not a complete compressible interaction model. If neighbors alter the source histories, those histories must first be solved consistently. At 200 μm separation and 1480 m s⁻¹ sound speed, travel time is 0.13514 μs; it is short against a 3-μs radial control but not against an arbitrary nanosecond laser pressure pulse. Regular spacing does not remove edges, propagation delay or nonlinear shielding.

步骤 7——仅在弱扰动、紧致源波动对照中，以延迟时间替代瞬时源时间。在固定观察位置对远场势求导，得到压力行。瞬时气泡体积分数不同于初始液体 PFC 装载分数；平面阵列需先规定层厚度，再指定区域体积。它是传播估计，并非完整可压缩相互作用模型。若邻泡改变源历程，必须先自洽求解这些历程。200 μm 间距、1480 m s⁻¹ 声速时，传播时间为 0.13514 μs；相对于 3 μs 径向对照较短，却不能相对于任意纳秒激光压力脉冲宣称较短。规则间距无法消除边缘、传播延迟及非线性屏蔽。

## 4. Close spatial jet formation; pay for focusing with momentum and energy

## 4. 闭合空间射流形成，并核算聚焦的动量与能量

Step 8 — replace spherical radii by a resolved liquid domain when an outlet meniscus deforms or a re-entrant finger enters a cavity. A radial calculation supplies cavity scale and source timing, but has no directional jet shape. For an initially irrotational, inviscid, incompressible carrier over the inertial launch interval, introduce a velocity potential. Here the liquid interfaces are treated as material surfaces; appreciable simultaneous evaporation requires the Chapter 2 mass-flux jump instead of the following kinematic approximation.

步骤 8——当出口弯液面变形或再入液指进入腔体时，以已解析液体域替代球形半径。径向计算提供腔体尺度及源时序，却没有方向性射流形状。对惯性发射阶段初始无旋、无黏、不可压缩的载液，引入速度势。此处液体界面视为材料表面；若同时蒸发不可忽略，运动学近似必须改用第二章质量通量跳跃条件。

**Symbols before Eq. (C3-E13).** $\boldsymbol u(\boldsymbol x,t)$ is velocity (m s⁻¹), $\phi(\boldsymbol x,t)$ potential (m² s⁻¹), $\boldsymbol x$ spatial position (m), $t$ time (s), and $\Omega(t)$ the moving liquid domain. $\nabla$, $\nabla\cdot$ and $\nabla^2$ are spatial gradient, divergence and Laplacian; the central dot is an actual contraction, not an equation separator.

**式（C3-E13）前的符号定义。** $\boldsymbol u(\boldsymbol x,t)$ 为速度（m s⁻¹），$\phi(\boldsymbol x,t)$ 为势（m² s⁻¹），$\boldsymbol x$ 为空间位置（m），$t$ 为时间（s），$\Omega(t)$ 为运动液体域。$\nabla$、$\nabla\cdot$、$\nabla^2$ 为空间梯度、散度、Laplace 算子；中心点是真正缩并，并非方程分隔符。

(C3-E13) · Potential-flow reduction$$
\boldsymbol u=\nabla\phi,\qquad \nabla\cdot\boldsymbol u=0\ \Longrightarrow\ \nabla^2\phi=0\quad\text{in }\Omega(t).
$$
![Geometry enters through the domain and its boundary conditions.](../assets/figures/c3-e13.svg)

Geometry enters through the domain and its boundary conditions.

几何通过区域及边界条件进入。

**Symbols before Eq. (C3-E14).** $\boldsymbol X$ is a material interface point (m); $t$ is time (s), $d/dt$ its trajectory derivative. $\boldsymbol u$ is liquid velocity and $\boldsymbol V\_w$ prescribed wall velocity (m s⁻¹). $\boldsymbol n$ is outward from liquid toward gas or solid, unitless; $V\_n$ normal interface speed (m s⁻¹), $\partial\_n\phi=\nabla\phi\cdot\boldsymbol n$, and $\phi$ potential (m² s⁻¹). $\Gamma$ is the complete moving interface; $\phi\_\Gamma$ its potential; $\Gamma\_0,\phi\_0$ are initial data. Arrows indicate the stated far-field limit.

**式（C3-E14）前的符号定义。** $\boldsymbol X$ 为材料界面点（m）；$t$ 为时间（s），$d/dt$ 为轨迹导数。$\boldsymbol u$ 为液速，$\boldsymbol V\_w$ 为规定壁速（m s⁻¹）。$\boldsymbol n$ 从液体指向气体或固体，是无量纲单位法向；$V\_n$ 为界面法向速度（m s⁻¹），$\partial\_n\phi=\nabla\phi\cdot\boldsymbol n$，$\phi$ 为势（m² s⁻¹）。$\Gamma$ 为完整运动界面；$\phi\_\Gamma$ 为其势；$\Gamma\_0,\phi\_0$ 为初值。箭头表示规定远场极限。

(C3-E14) · Kinematic, initial and wall conditions$$
\begin{aligned}\frac{d\boldsymbol X}{dt}&=\boldsymbol u(\boldsymbol X,t),\quad V\_n=\partial\_n\phi,\quad \partial\_n\phi=\boldsymbol V\_w\cdot\boldsymbol n\quad\text{on walls},\\ (\Gamma,\phi\_\Gamma)\_{t=0}&=(\Gamma\_0,\phi\_0),\qquad \phi\to0\quad\text{in a quiescent far field}.\end{aligned}
$$
![A potential equation without initial shape and wall data cannot predict a jet.](../assets/figures/c3-e14.svg)

A potential equation without initial shape and wall data cannot predict a jet.

无初始形状及壁面数据的势方程无法预测射流。

**Symbols before Eq. (C3-E15).** $p\_l,p\_g,p\_\infty$ are interface-liquid, gas and remote pressures (Pa); $\sigma$ is the tension appropriate to that interface (N m⁻¹). $\kappa$ is signed total curvature (m⁻¹), $\nabla\_s\cdot$ surface divergence, $\boldsymbol n$ the liquid-to-gas unit normal, $R$ inner-cavity radius and $a\_j$ exterior-cylinder radius (m). $\phi\_\Gamma$ and $\phi$ are surface/bulk potential (m² s⁻¹); $\boldsymbol u$ velocity (m s⁻¹), $\rho$ density (kg m⁻³), $t$ time (s). $D/Dt$ is the material derivative, $\partial\_t$ fixed-position derivative, $\nabla$ spatial gradient, $|\ |$ Euclidean norm; labels cavity and jet select geometries.

**式（C3-E15）前的符号定义。** $p\_l,p\_g,p\_\infty$ 为界面液压、气压、远压（Pa）；$\sigma$ 为对应界面张力（N m⁻¹）。$\kappa$ 为带符号总曲率（m⁻¹），$\nabla\_s\cdot$ 为表面散度，$\boldsymbol n$ 为液体指向气体的单位法向，$R$ 为内部腔体半径、$a\_j$ 为外部圆柱半径（m）。$\phi\_\Gamma$、$\phi$ 为表面／体内势（m² s⁻¹）；$\boldsymbol u$ 为速度（m s⁻¹），$\rho$ 为密度（kg m⁻³），$t$ 为时间（s）。$D/Dt$ 为材料导数，$\partial\_t$ 为固定位置导数，$\nabla$ 为空间梯度，$|\ |$ 为 Euclidean 范数；cavity、jet 标签选择几何。

(C3-E15) · Normal stress and material Bernoulli condition$$
\begin{aligned}p\_l&=p\_g+\sigma\kappa,\quad\kappa=\nabla\_s\cdot\boldsymbol n,\quad\kappa\_{\mathrm{cavity}}=-2/R,\quad\kappa\_{\mathrm{jet}}=1/a\_j,\\ \frac{D\phi\_\Gamma}{Dt}&=\frac12|\nabla\phi|^2+\frac{p\_\infty-p\_g-\sigma\kappa}{\rho},\qquad \frac D{Dt}=\partial\_t+\boldsymbol u\cdot\nabla.\end{aligned}
$$
![Signed curvature and the material derivative keep the dynamic condition consistent.](../assets/figures/c3-e15.svg)

Signed curvature and the material derivative keep the dynamic condition consistent.

带符号曲率及材料导数使动力学条件自洽。

Step 9 — normal stress supplies the first row of Eq. (C3-E15). Eulerian Bernoulli contains minus one half of squared speed when solved for the fixed-position potential derivative; adding velocity dotted with its gradient produces the plus sign in the material derivative. At a sphere the surface potential is minus radius times wall speed. Its material derivative is minus squared wall speed minus radius times acceleration, so the condition recovers the spherical balance with resisting surface tension. This displayed reference uses a quiescent reservoir; a finite sealed cell needs its actual pressure/volume boundary and potential gauge instead of a fictitious far field. Solve the harmonic boundary-value problem and advance shape/potential until topology or compressibility invalidates the stage. An internal re-entry jet and an exterior meniscus jet are distinct events; one is not proof of the other. The calculations of Peters et al. illustrate why resolving the free surface matters. [[R4]](../reference/sources.html#r4)

步骤 9——法向应力给出式（C3-E15）第一行。将 Euler 型 Bernoulli 解为固定位置势导数时含负的二分之一速度平方；加入速度与势梯度的点积后，材料导数中变为正号。球形表面势为负的半径乘壁速，材料导数为负壁速平方减半径乘加速度，因此界面条件还原带抵抗表面张力的球形平衡。所示参考使用静止储液域；有限封闭单元需采用实际压力／体积边界及势的规范条件，而不能假造远场。应求解调和边值问题、推进形状／势，直到拓扑或可压缩性使该阶段失效。内部再入射流及外部弯液面射流是不同事件；出现一者并不能证明另一者。Peters 等的计算说明解析自由表面的必要性。[[R4]](../reference/sources.html#r4)

**Symbols before Eq. (C3-E16).** $\Pi(\boldsymbol x),\Pi\_0$ are pressure impulse per area (Pa s), $p,p\_{\mathrm{ref}}$ total and reference pressure (Pa), $\boldsymbol x$ position (m), $t,t\_0,\tau\_p>0$ time/start/pulse duration (s). $\Delta\boldsymbol u$ velocity increment and $U$ column speed (m s⁻¹), $\rho>0$ density (kg m⁻³), $z\in[0,L]$ axial coordinate, $L>0$ length (m), $A>0$ area (m²), $m>0$ liquid mass (kg). $\mathcal J$ is total directional force impulse (N s), $E$ kinetic energy (J). $\nabla,\nabla^2$ are gradient/Laplacian; $\int$ time integration and vertical bars denote a stated fixed-budget branch. The pulse approximation freezes geometry and neglects integrated convection and viscosity.

**式（C3-E16）前的符号定义。** $\Pi(\boldsymbol x),\Pi\_0$ 为单位面积压力冲量（Pa s），$p,p\_{\mathrm{ref}}$ 为总／参考压力（Pa），$\boldsymbol x$ 为位置（m），$t,t\_0,\tau\_p>0$ 为时间／开始时刻／脉冲时长（s）。$\Delta\boldsymbol u$ 为速度增量，$U$ 为液柱速度（m s⁻¹），$\rho>0$ 为密度（kg m⁻³），$z\in[0,L]$ 为轴坐标，$L>0$ 为长度（m），$A>0$ 为面积（m²），$m>0$ 为液体质量（kg）。$\mathcal J$ 为总方向力冲量（N s），$E$ 为动能（J）。$\nabla,\nabla^2$ 为梯度／Laplace 算子；$\int$ 为时间积分，竖线表示指定固定预算分支。脉冲近似冻结几何并忽略积分后的对流及黏性。

(C3-E16) · Pressure-impulse control and distinct focusing budgets$$
\begin{aligned}\Pi(\boldsymbol x)&=\int\_{t\_0}^{t\_0+\tau\_p}(p-p\_{\mathrm{ref}})\,dt,\quad \Delta\boldsymbol u\simeq-\nabla\Pi/\rho,\quad\nabla^2\Pi=0,\\ \Pi(z)&=\Pi\_0(1-z/L),\quad U=\frac{\Pi\_0}{\rho L},\quad m=\rho AL,\quad\mathcal J=\Pi\_0A=mU,\\ U\big|\_{\mathcal J\ \mathrm{fixed}}&=\frac{\mathcal J}{m},\quad E=\frac{\mathcal J^2}{2m},\qquad U\big|\_{E\ \mathrm{fixed}}=\sqrt{\frac{2E}{m}}.\end{aligned}
$$
![The pressure-impulse field and the total energy constraint must be compatible.](../assets/figures/c3-e16.svg)

The pressure-impulse field and the total energy constraint must be compatible.

压力冲量场必须与总能量约束相容。

Step 10 — integrate momentum over a short pulse and then take divergence using incompressibility. The straight-column solution obeys the two end impulse values and insulating sidewalls. Its pressure-impulse gradient gives uniform initial speed; reducing area alone at fixed impulse per area does not increase that speed. At fixed total impulse, reducing liquid mass fourfold raises speed fourfold and required kinetic energy fourfold. At fixed energy it raises uniform speed only twofold and reduces momentum by one half. These are different experiments. A concave moving meniscus concentrates a solved spatial velocity field, but mass conservation alone does not pay for that concentration. The geometry-frozen condition additionally needs small pulse displacement and viscous effects; several acoustic crossings alone do not establish it. [[R2]](../reference/sources.html#r2)

步骤 10——在短脉冲内积分动量，再利用不可压缩性取散度。直液柱解满足两端冲量值及侧壁无通量条件。其压力冲量梯度给出均匀初速度；固定单位面积冲量时仅减面积并不提高速度。固定总冲量时，液体质量降至四分之一，会使速度及所需动能均增大四倍。固定能量时均匀速度只增大两倍，而动量降为一半。这是不同实验。凹形运动弯液面会集中已求解的空间速度场，但仅凭质量守恒并不能支付聚焦代价。冻结几何还要求脉冲位移及黏性作用小；经历若干声传播周期本身不足以确立近似。[[R2]](../reference/sources.html#r2)

**Symbols before Eq. (C3-E17).** $Q$ is steady volume flow (m³ s⁻¹), $a\_{\mathrm{in}}>a\_j>0$ solid-tube inlet and free cylindrical-jet radii (m); $U\_{\mathrm{in}},U\_j$ are uniform speeds (m s⁻¹), $\alpha$ dimensionless area ratio. $p\_{\mathrm{in}},p\_g$ inlet and gas pressures, $\Delta p\_{\mathrm{loss}}\ge0$ prescribed loss (Pa); $\rho>0$ density (kg m⁻³), $\sigma\_j$ jet–gas tension (N m⁻¹), $\pi$ dimensionless. The square root requires nonnegative numerator. This is a steady inviscid-core nozzle control with optional loss, not a transient cavity solution.

**式（C3-E17）前的符号定义。** $Q$ 为稳态体积流量（m³ s⁻¹），$a\_{\mathrm{in}}>a\_j>0$ 为固体管入口及自由圆柱射流半径（m）；$U\_{\mathrm{in}},U\_j$ 为均匀速度（m s⁻¹），$\alpha$ 为无量纲面积比。$p\_{\mathrm{in}},p\_g$ 为入口及气压，$\Delta p\_{\mathrm{loss}}\ge0$ 为给定损失（Pa）；$\rho>0$ 为密度（kg m⁻³），$\sigma\_j$ 为射流—气体张力（N m⁻¹），$\pi$ 无量纲。平方根要求分子非负。它是允许损失的稳态无黏核心喷嘴对照，并非瞬态腔体解。

(C3-E17) · Continuity plus Bernoulli focusing benchmark$$
\begin{aligned}Q&=\pi a\_{\mathrm{in}}^2U\_{\mathrm{in}}=\pi a\_j^2U\_j,\qquad \alpha=(a\_j/a\_{\mathrm{in}})^2,\quad U\_{\mathrm{in}}=\alpha U\_j,\\ p\_{\mathrm{in}}-p\_g&=\frac12\rho(U\_j^2-U\_{\mathrm{in}}^2)+\frac{\sigma\_j}{a\_j}+\Delta p\_{\mathrm{loss}},\\ U\_j&=\sqrt{\frac{2[p\_{\mathrm{in}}-p\_g-\sigma\_j/a\_j-\Delta p\_{\mathrm{loss}}]}{\rho(1-\alpha^2)}}\quad(0<\alpha<1).\end{aligned}
$$
![Specify either source pressure or flow and solve the compatible remaining quantity.](../assets/figures/c3-e17.svg)

Specify either source pressure or flow and solve the compatible remaining quantity.

指定源压力或流量，再求其余相容量。

For a 40-μm inlet radius, 10-μm outlet radius and 3 m s⁻¹ inlet speed, continuity gives 48 m s⁻¹ outlet speed. With density 1000 kg m⁻³, tension 0.072 N m⁻¹ and zero loss, the required inlet overpressure is 1.1547 MPa: 1.1475 MPa kinetic increase plus 7.2 kPa capillary pressure. If overpressure is instead fixed at 0.20 MPa, Eq. (C3-E17) gives 19.6752 m s⁻¹ outlet speed and 1.22970 m s⁻¹ inlet speed. Holding the original inlet speed and the smaller pressure simultaneously would violate energy conservation. This solved control reveals a budget error; the actual evolving meniscus still requires Eqs. (C3-E13–15).

入口半径 40 μm、出口半径 10 μm、入口速度 3 m s⁻¹ 时，连续性给出出口速度 48 m s⁻¹。密度 1000 kg m⁻³、张力 0.072 N m⁻¹、零损失时，所需入口超压为 1.1547 MPa：动能增量对应 1.1475 MPa，毛细压力为 7.2 kPa。若超压改为固定 0.20 MPa，式（C3-E17）给出出口速度 19.6752 m s⁻¹、入口速度 1.22970 m s⁻¹。同时保持原入口速度及较小压力会违反能量守恒。这个已解对照揭示预算错误；实际演化弯液面仍需式（C3-E13—15）。

**Symbols before Eq. (C3-E18).** $A\_j$ is area (m²), $d\_j,L\_j>0$ diameter/emitted length (m), $\rho$ carrier density (kg m⁻³), $m\_j>0$ emitted mass (kg); the cylinder expression assumes uniform area/density. $\mathcal M\_j$ is the emitted material collection, $dm$ mass element (kg), $\boldsymbol u$ velocity field, $U\_{\mathrm{rms}}$ mass-weighted root-mean-square speed (m s⁻¹). $\boldsymbol e\_z$ is a unit vector along intended transfer; $P\_j$ its signed momentum (N s), $E\_j$ kinetic energy and $E\_{\mathrm{avail}}\ge E\_j$ available mechanical energy (J). $\int$ integrates over emitted mass; $|\ |$ denotes vector norm or scalar magnitude; $\pi$ is dimensionless.

**式（C3-E18）前的符号定义。** $A\_j$ 为面积（m²），$d\_j,L\_j>0$ 为直径／喷出长度（m），$\rho$ 为载液密度（kg m⁻³），$m\_j>0$ 为喷出质量（kg）；圆柱式假设面积及密度均匀。$\mathcal M\_j$ 为喷出材料集合，$dm$ 为质量微元（kg），$\boldsymbol u$ 为速度场，$U\_{\mathrm{rms}}$ 为质量加权均方根速度（m s⁻¹）。$\boldsymbol e\_z$ 为期望转印方向的单位向量；$P\_j$ 为该方向带符号动量（N s），$E\_j$ 为动能、$E\_{\mathrm{avail}}\ge E\_j$ 为可用机械能（J）。$\int$ 对喷出质量积分；$|\ |$ 为向量范数或标量大小；$\pi$ 无量纲。

(C3-E18) · Finite-mass definitions and Cauchy–Schwarz bound$$
\begin{aligned}A\_j&=\pi d\_j^2/4,\qquad m\_j=\rho A\_jL\_j,\qquad E\_j=\frac12\int\_{\mathcal M\_j}|\boldsymbol u|^2dm=\frac12m\_jU\_{\mathrm{rms}}^2,\\ P\_j&=\int\_{\mathcal M\_j}(\boldsymbol u\cdot\boldsymbol e\_z)\,dm,\\ |P\_j|^2&\le\left(\int\_{\mathcal M\_j}1\,dm\right)\left(\int\_{\mathcal M\_j}|\boldsymbol u\cdot\boldsymbol e\_z|^2dm\right)\le2m\_jE\_j,\qquad U\_{\mathrm{rms}}\le\sqrt{2E\_{\mathrm{avail}}/m\_j}.\end{aligned}
$$
![Finite jet mass converts an energy budget into a meaningful speed and momentum bound.](../assets/figures/c3-e18.svg)

Finite jet mass converts an energy budget into a meaningful speed and momentum bound.

有限射流质量将能量预算转化为有意义的速度及动量界。

Step 11 — apply Cauchy–Schwarz to the mass integrals of one and axial velocity, then bound axial squared velocity by total squared velocity. Equality requires every emitted element to move at the same speed along the chosen axis. Energy divided by mass has units m² s⁻²; the speed bound has units m s⁻¹. Both squared momentum and mass times energy have units kg² m² s⁻². For all jets together the proof uses total mass and total kinetic energy, so a site count does not escape the bound. Directional cancellation, a rapidly moving tiny tip, or energy in lateral flow can reduce useful momentum even when a camera records a high maximum speed.

步骤 11——对一与轴向速度的质量积分应用 Cauchy–Schwarz，再以总速度平方限制轴向速度平方。等号要求所有喷出微元以相同速度沿所选轴运动。能量除以质量单位为 m² s⁻²，因此速度界单位为 m s⁻¹。动量平方及质量乘能量的单位均为 kg² m² s⁻²。对全部射流，证明使用总质量及总动能，故增加位点数不能逃离该界。方向抵消、高速但微小的尖端，或侧向流中的能量，即使相机记录最大速度很高，也会减少有用动量。

## 5. Derive transport and the breakup test after a slender jet exists

## 5. 射流形成细长形态后推导输运及断裂检验

Step 12 — take an axisymmetric Newtonian jet in dynamically negligible gas, constant density and surface tension, negligible gravity, and no mass exchange. Let its local radius and axial velocity vary along the flight direction. Exact conservation on a fixed finite slice uses the integral of area, not one endpoint area times slice length. Divide that balance by the positive slice length and take its zero-length limit for differentiable fields to obtain differential continuity. Substitute area equals pi times radius squared and divide by positive twice pi times radius. This description begins after launch, with initial shape, velocity, inflow history and end conditions supplied by the spatial calculation or measurements. It is not valid for the strongly two-dimensional neck turning into a jet at birth.

步骤 12——采用动力学作用可忽略气体中的轴对称 Newton 流体射流，密度及表面张力恒定，忽略重力及质量交换。其局部半径、轴向速度沿飞行方向变化。固定有限切片的精确守恒使用面积积分，不能用某端面积直接乘切片长度。将平衡除以正切片长度，并对可微场取长度趋零极限，得到微分连续性。代入面积等于圆周率乘半径平方，再除以正的两倍圆周率乘半径。此描述从发射之后开始，初始形状、速度、流入历程及端部条件由空间计算或测量提供。它不适用于射流初生时强二维颈部的转向。

**Symbols before Eq. (C3-E19).** $z$ is axial position (m), $t$ time (s), $\Delta z>0$ fixed finite slice length (m), and $\xi$ its dummy axial coordinate with element $d\xi$ (m). $a(z,t)>0$ is local jet radius (m), $A(z,t)$ area (m²), $v(z,t)$ cross-sectional average axial velocity (m s⁻¹), and $\pi$ dimensionless. $\partial\_t,\partial\_z$ are fixed-coordinate derivatives; $[Av]$ denotes the volume flux (m³ s⁻¹) evaluated at the stated end. $\int$ integrates over the slice; the differential limit requires differentiable fields. The last step divides by positive $2\pi a$.

**式（C3-E19）前的符号定义。** $z$ 为轴向位置（m），$t$ 为时间（s），$\Delta z>0$ 为固定有限切片长度（m），$\xi$ 为轴向积分坐标，$d\xi$ 为其微元（m）。$a(z,t)>0$ 为局部射流半径（m），$A(z,t)$ 为面积（m²），$v(z,t)$ 为截面平均轴速（m s⁻¹），$\pi$ 无量纲。$\partial\_t,\partial\_z$ 为固定坐标导数；$[Av]$ 表示在指定端点评价的体积流率（m³ s⁻¹）。$\int$ 为切片积分；微分极限要求场可微。最后一步除以正的 $2\pi a$。

(C3-E19) · Slender-jet volume conservation$$
\begin{aligned}A(z,t)&=\pi a(z,t)^2,\\ \partial\_t\int\_z^{z+\Delta z}A(\xi,t)\,d\xi&=[Av](z,t)-[Av](z+\Delta z,t),\\ \partial\_t\frac{1}{\Delta z}\int\_z^{z+\Delta z}A\,d\xi+\frac{[Av](z+\Delta z,t)-[Av](z,t)}{\Delta z}&=0,\\ \Delta z\to0:\quad \partial\_tA+\partial\_z(Av)&=0\ \Longrightarrow\ \partial\_ta+v\partial\_za=-\frac a2\partial\_zv.\end{aligned}
$$
![Axial stretching changes radius even before capillary necking grows.](../assets/figures/c3-e19.svg)

Axial stretching changes radius even before capillary necking grows.

在毛细颈缩增长前，轴向拉伸即会改变半径。

**Symbols before Eq. (C3-E20).** $r\in[0,a]$ and $z$ are radial/axial coordinates (m), $t$ time (s); $u\_r$ is radial and $v$ axial velocity (m s⁻¹), $a>0$ radius (m), $A=\pi a^2$ area (m²). $\rho$ is density (kg m⁻³), $\mu$ Newtonian viscosity (Pa s), $\sigma\_j$ jet–gas tension (N m⁻¹); $\tau\_{zz},\tau\_{rr}$ are viscous normal stresses (Pa), subscripts coordinate components. $\kappa$ is outward liquid-to-gas curvature (m⁻¹). $\partial\_r,\partial\_z,\partial\_t$ are partial derivatives; $\partial\_{zz}$ is a second axial derivative. The axial momentum law is a slender approximation although the geometric curvature is retained in full.

**式（C3-E20）前的符号定义。** $r\in[0,a]$、$z$ 为径向／轴向坐标（m），$t$ 为时间（s）；$u\_r$ 为径向、$v$ 为轴向速度（m s⁻¹），$a>0$ 为半径（m），$A=\pi a^2$ 为面积（m²）。$\rho$ 为密度（kg m⁻³），$\mu$ 为 Newton 黏度（Pa s），$\sigma\_j$ 为射流—气体张力（N m⁻¹）；$\tau\_{zz},\tau\_{rr}$ 为黏性法向应力（Pa），下标为坐标分量。$\kappa$ 为液体朝气体外法向曲率（m⁻¹）。$\partial\_r,\partial\_z,\partial\_t$ 为偏导数；$\partial\_{zz}$ 为轴向二阶导数。虽然保留完整几何曲率，轴向动量规律仍为细长近似。

(C3-E20) · Newtonian stress and slender axial momentum$$
\begin{aligned}\partial\_r u\_r+u\_r/r+\partial\_zv&=0\ \Longrightarrow\ u\_r=-\frac r2\partial\_zv,\\ \tau\_{zz}&=2\mu\partial\_zv,\quad\tau\_{rr}=2\mu\partial\_ru\_r=-\mu\partial\_zv,\quad\tau\_{zz}-\tau\_{rr}=3\mu\partial\_zv,\\ \partial\_tv+v\partial\_zv&=-\frac{\sigma\_j}{\rho}\partial\_z\kappa+\frac{3\mu}{\rho A}\partial\_z(A\partial\_zv),\\ \kappa&=\frac1{a\sqrt{1+(\partial\_za)^2}}-\frac{\partial\_{zz}a}{[1+(\partial\_za)^2]^{3/2}}.\end{aligned}
$$
![The factor three follows from extensional stress, rather than ordinary shear drag.](../assets/figures/c3-e20.svg)

The factor three follows from extensional stress, rather than ordinary shear drag.

因子三来自拉伸应力，而不是普通剪切阻力。

Step 13 — integrate radial continuity from the axis and impose regularity to obtain radial velocity. Insert its derivative into Newtonian stresses; subtract radial from axial stress to obtain the extensional factor three. The free-surface normal stress removes radial stress from liquid pressure, leaving the axial stress difference and capillary-pressure gradient. Dividing the axial force balance by mass per unit length gives the third row of Eq. (C3-E20). Each acceleration term has unit m s⁻². Constant radius and constant velocity make the right side zero, while an axial strain changes radius through Eq. (C3-E19). These reduced equations and their energy dissipation are established in Eggers and Dupont; retaining exact curvature does not make the reduced momentum equation an exact three-dimensional theory. [[R14]](../reference/sources.html#r14)

步骤 13——从轴线积分径向连续性并施加正则性，得到径向速度。将其导数代入 Newton 应力，以轴向减径向应力，得到拉伸因子三。自由表面法向应力从液压中消去径向应力，留下轴向应力差及毛细压力梯度。轴向受力平衡除以单位长度质量，得到式（C3-E20）第三行。各加速度项单位为 m s⁻²。恒定半径及恒定速度使右侧为零，而轴向应变通过式（C3-E19）改变半径。Eggers 与 Dupont 建立了这些约化方程及其能量耗散；保留精确曲率并不使约化动量方程成为精确三维理论。[[R14]](../reference/sources.html#r14)

**Symbols before Eq. (C3-E21).** $a$ is perturbed radius and $a\_0>0$ base-cylinder radius (m); $0<\delta\_0\le\delta(t)\ll a\_0$ are initial/small disturbance amplitudes (m), $z,r$ axial/radial positions (m), $t$ time (s), $U\_j$ base axial speed (m s⁻¹), $k>0$ wavenumber (m⁻¹). $\kappa$ is curvature (m⁻¹); $\psi$ perturbation potential and $B\ne0$ its amplitude (m² s⁻¹), $g>0$ temporal growth rate (s⁻¹); $g$ does not denote gravity in this chapter. $I\_0,I\_1$ are dimensionless modified Bessel functions, orders zero/one; $q$ dimensionless wavenumber. $\rho$ density (kg m⁻³), $\sigma\_j$ tension (N m⁻¹); cosine and exponential have dimensionless arguments. This inviscid infinite-cylinder linear control neglects surrounding-gas dynamics.

**式（C3-E21）前的符号定义。** $a$ 为扰动半径，$a\_0>0$ 为基态圆柱半径（m）；$0<\delta\_0\le\delta(t)\ll a\_0$ 为初始／小扰动振幅（m），$z,r$ 为轴向／径向位置（m），$t$ 为时间（s），$U\_j$ 为基态轴速（m s⁻¹），$k>0$ 为波数（m⁻¹）。$\kappa$ 为曲率（m⁻¹）；$\psi$ 为扰动势，$B\ne0$ 为其振幅（m² s⁻¹），$g>0$ 为时间增长率（s⁻¹）；本章 $g$ 不表示重力。$I\_0,I\_1$ 为零／一阶无量纲修正 Bessel 函数；$q$ 为无量纲波数。$\rho$ 为密度（kg m⁻³），$\sigma\_j$ 为张力（N m⁻¹）；余弦及指数自变量无量纲。该无黏无限圆柱线性对照忽略周围气体动力学。

(C3-E21) · Inviscid-cylinder instability derivation$$
\begin{aligned}a&=a\_0+\delta(t)\cos[k(z-U\_jt)],\quad \kappa\simeq a\_0^{-1}+(k^2-a\_0^{-2})\delta\cos[k(z-U\_jt)],\\ \psi&=B I\_0(kr)e^{gt}\cos[k(z-U\_jt)],\quad\delta=\delta\_0e^{gt},\\ g\delta\_0&=BkI\_1(ka\_0),\quad \rho gB I\_0(ka\_0)=\sigma\_j(a\_0^{-2}-k^2)\delta\_0,\\ g^2&=\frac{\sigma\_j}{\rho a\_0^3}\,q(1-q^2)\frac{I\_1(q)}{I\_0(q)},\quad q=ka\_0\in(0,1).\end{aligned}
$$
![Kinematic and pressure conditions eliminate the potential amplitude and determine growth.](../assets/figures/c3-e21.svg)

Kinematic and pressure conditions eliminate the potential amplitude and determine growth.

运动学及压力条件消去势振幅，从而确定增长。

Step 14 — expand curvature to first order: the reciprocal radius contributes minus amplitude divided by squared base radius, and axial curvature contributes wavenumber squared times amplitude. Solve Laplace's equation with a regular radial modified-Bessel function; its radial derivative is wavenumber times the order-one function. The kinematic condition and linear Bernoulli pressure give the middle row of Eq. (C3-E21). Eliminate the nonzero potential amplitude to obtain the last row. It is positive only below dimensionless wavenumber one. Independent maximization gives 0.697019 for the fastest dimensionless wavenumber and 0.343339 for growth rate times capillary time, consistent with the classical cylinder benchmark. [MIT interfacial-phenomena derivation, Lecture 11](https://ocw.mit.edu/courses/18-357-interfacial-phenomena-fall-2010/d77da8d5f1bb8b69a62682bc0dbc5845_MIT18_357F10_Lecture11.pdf)

步骤 14——将曲率展开至一阶：半径倒数贡献负的振幅除以基态半径平方，轴向曲率贡献波数平方乘振幅。采用轴线上正则的径向修正 Bessel 函数求解 Laplace 方程；其径向导数为波数乘一阶函数。运动学条件及线性 Bernoulli 压力给出式（C3-E21）中间行。消去非零势振幅得到最后一行；仅当无量纲波数小于一时为正。独立求最大值给出最快无量纲波数 0.697019，增长率乘毛细时间为 0.343339，与经典圆柱对照一致。[MIT 界面现象推导，第 11 讲](https://ocw.mit.edu/courses/18-357-interfacial-phenomena-fall-2010/d77da8d5f1bb8b69a62682bc0dbc5845_MIT18_357F10_Lecture11.pdf)

**Symbols before Eq. (C3-E22).** $t\_\sigma,t\_{\mathrm{lin}},t\_{\mathrm{flight}}$ are capillary, linear-threshold and flight times (s); $\rho$ density (kg m⁻³), $a\_0,d\_j,H$ base radius/diameter/gap (m), $\sigma\_j$ tension (N m⁻¹), $\mu$ viscosity (Pa s), $U\_j>0$ uniform speed (m s⁻¹). $g\_{\max}>0$ fastest inviscid growth rate (s⁻¹), $\lambda\_{\max}$ its wavelength (m), $\delta\_0<\delta\_{\mathrm{crit}}\ll a\_0$ initial/chosen small threshold and $\delta\_{\mathrm{arr}}$ arrival amplitude (m). $\ln,\exp$ are natural logarithm/exponential, $\pi$ dimensionless; $\mathrm{Re}\_j,\mathrm{We}\_j,\mathrm{Oh}\_j$ are dimensionless diameter-based Reynolds, Weber and Ohnesorge numbers. Constant base state and a sufficiently long cylinder are assumed for growth.

**式（C3-E22）前的符号定义。** $t\_\sigma,t\_{\mathrm{lin}},t\_{\mathrm{flight}}$ 为毛细／线性阈值／飞行时间（s）；$\rho$ 为密度（kg m⁻³），$a\_0,d\_j,H$ 为基态半径／直径／间隙（m），$\sigma\_j$ 为张力（N m⁻¹），$\mu$ 为黏度（Pa s），$U\_j>0$ 为均匀速度（m s⁻¹）。$g\_{\max}>0$ 为最快无黏增长率（s⁻¹），$\lambda\_{\max}$ 为其波长（m），$\delta\_0<\delta\_{\mathrm{crit}}\ll a\_0$ 为初始／选定小阈值振幅，$\delta\_{\mathrm{arr}}$ 为到达振幅（m）。$\ln,\exp$ 为自然对数／指数，$\pi$ 无量纲；$\mathrm{Re}\_j,\mathrm{We}\_j,\mathrm{Oh}\_j$ 为以直径定义的无量纲 Reynolds、Weber、Ohnesorge 数。增长计算假设基态恒定且圆柱足够长。

(C3-E22) · Finite-flight growth and regime diagnostics$$
\begin{aligned}t\_\sigma&=\sqrt{\rho a\_0^3/\sigma\_j},\quad g\_{\max}=0.343339/t\_\sigma,\quad\lambda\_{\max}=2\pi a\_0/0.697019,\\ t\_{\mathrm{lin}}&=\frac1{g\_{\max}}\ln\left(\frac{\delta\_{\mathrm{crit}}}{\delta\_0}\right),\qquad\frac{\delta\_{\mathrm{arr}}}{a\_0}=\frac{\delta\_0}{a\_0}\exp\left(g\_{\max}\frac H{U\_j}\right),\quad t\_{\mathrm{flight}}=H/U\_j,\\ \mathrm{Re}\_j&=\frac{\rho U\_jd\_j}{\mu},\quad\mathrm{We}\_j=\frac{\rho U\_j^2d\_j}{\sigma\_j},\quad\mathrm{Oh}\_j=\frac{\mu}{\sqrt{\rho\sigma\_jd\_j}},\qquad d\_j=2a\_0.\end{aligned}
$$
![Compare growth during actual flight against a declared small-amplitude threshold.](../assets/figures/c3-e22.svg)

Compare growth during actual flight against a declared small-amplitude threshold.

比较实际飞行期间增长与明确的小振幅阈值。

Step 15 — take the logarithm of exponential growth to reach a selected small disturbance threshold. Capillary time squared has units (kg)/(kg s⁻²) = s². Growth tends to zero when tension tends to zero, and at the dimensionless-wavenumber zero/one endpoints. A threshold of 0.1 radius is a declared edge-of-linearity diagnostic. Substituting a whole radius gives the source's 17.7-μs estimate in the later example, but that is an extrapolation, not an exact pinch-off time. A 50-μm jet is only about one fastest wavelength long, so finite ends and startup shape matter. For stretching jets use the evolving transport equations and disturbance history; for a jet in another dense liquid use two-fluid stress and stability. Large Weber number alone does not guarantee coherent landing.

步骤 15——对指数增长取对数，求达到选定小扰动阈值的时间。毛细时间平方的单位为（kg）／（kg s⁻²）= s²。张力趋零时增长趋零，无量纲波数为零／一的端点也为零。0.1 倍半径是明确声明的线性边缘诊断阈值。代入整个半径会给出后续算例中的原文 17.7 μs 估计，但它是外推，并非精确夹断时间。50 μm 射流仅约一个最快波长长，因此有限端部及初始形状重要。拉伸射流应使用演化输运方程及扰动历程；在另一种稠密液体中的射流则需双流体应力及稳定性模型。大 Weber 数本身不能保证相干落地。

## 6. Match early impact, finite impulse, and a declared pressure observer

## 6. 匹配早期冲击、有限冲量及规定的压力观察量

Step 16 — distinguish two deceleration regimes. Steady redirection of a uniform jet onto a fixed receiver has a momentum-flux force, provided its outlet axial momentum vanishes. The initial contact instead compresses both media and launches transient waves. These are consequences of one finite incoming state, not two loads to add independently. We take positive normal velocity into the receiver, initially stationary, and define compressive pressure as excess over its precontact reference.

步骤 16——区分两种减速阶段。均匀射流在固定接收面稳态转向、且出口轴向动量消失时，存在动量流率产生的力；初始接触则压缩双方介质并发出瞬态波。这是同一有限入射状态的不同后果，并非两个可独立相加的载荷。规定进入接收体的法向速度为正，接收体初始静止，压缩压力为相对接触前参考值的超压。

**Symbols before Eq. (C3-E23).** $q\_j$ is jet dynamic-pressure scale (Pa), $\rho$ density (kg m⁻³), $U\_j>0$ uniform speed (m s⁻¹), $A\_j$ incident area (m²), $\dot m$ positive mass-flow rate (kg s⁻¹; dot on $m$ here denotes throughflow, not changing the finite emitted mass), and $F\_{\mathrm{steady}}$ receiver-normal steady force (N). Complete lateral redirection, fixed receiver, negligible other axial forces and uniform inlet are assumed.

**式（C3-E23）前的符号定义。** $q\_j$ 为射流动压尺度（Pa），$\rho$ 为密度（kg m⁻³），$U\_j>0$ 为均匀速度（m s⁻¹），$A\_j$ 为入射面积（m²），$\dot m$ 为正的质量流率（kg s⁻¹；此处 $m$ 上的点表示通过流率，并非有限喷出质量变化），$F\_{\mathrm{steady}}$ 为接收体法向稳态力（N）。假设完全侧向转流、接收体固定、其他轴向力可忽略且入口均匀。

(C3-E23) · Dynamic-pressure definition and steady momentum flux$$
q\_j=\frac12\rho U\_j^2,\qquad\dot m=\rho A\_jU\_j,\qquad F\_{\mathrm{steady}}=\dot mU\_j=\rho A\_jU\_j^2=2q\_jA\_j.
$$
![Steady force follows from momentum flux, rather than assigning dynamic pressure everywhere.](../assets/figures/c3-e23.svg)

Steady force follows from momentum flux, rather than assigning dynamic pressure everywhere.

稳态力来自动量流率，而非将动压指定至全部表面。

**Symbols before Eq. (C3-E24).** $u$ is liquid normal velocity, $U\_j$ its initial incident speed and $v\_i$ common contact velocity (m s⁻¹); $p'$ is linear compressive pressure disturbance and $p\_{\mathrm{early}}$ contact value (Pa). $\rho$ is liquid density (kg m⁻³), $c$ liquid longitudinal sound speed (m s⁻¹), $Z\_l=\rho c>0$ liquid and $Z\_r>0$ receiver longitudinal impedance (Pa s m⁻¹). $z$ is normal coordinate (m), $t$ time (s), and $\partial\_t,\partial\_z$ are partial derivatives. The two differential operators follow right/left characteristics. Both media are locally semi-infinite and initially unpressurized relative to the same contact reference; the receiver is initially at rest.

**式（C3-E24）前的符号定义。** $u$ 为液体法向速度，$U\_j$ 为初始入射速度，$v\_i$ 为共同接触速度（m s⁻¹）；$p'$ 为线性压缩压力扰动，$p\_{\mathrm{early}}$ 为接触值（Pa）。$\rho$ 为液体密度（kg m⁻³），$c$ 为液体纵向声速（m s⁻¹），$Z\_l=\rho c>0$ 为液体阻抗，$Z\_r>0$ 为接收体纵向阻抗（Pa s m⁻¹）。$z$ 为法向坐标（m），$t$ 为时间（s），$\partial\_t,\partial\_z$ 为偏导数。两个微分算子沿右／左行特征。两介质局部半无限，相对同一接触参考值初始无压力扰动；接收体初始静止。

(C3-E24) · Linear transient wave equations and impact matching$$
\begin{aligned}\partial\_tu&=-\rho^{-1}\partial\_zp',\qquad\partial\_tp'=-\rho c^2\partial\_zu,\quad Z\_l=\rho c,\\ (\partial\_t+c\partial\_z)(u+p'/Z\_l)&=0,\quad(\partial\_t-c\partial\_z)(u-p'/Z\_l)=0,\\ p\_{\mathrm{early}}&=Z\_l(U\_j-v\_i)=Z\_rv\_i\ \Longrightarrow\ v\_i=\frac{Z\_l}{Z\_l+Z\_r}U\_j,\quad p\_{\mathrm{early}}=\frac{Z\_lZ\_r}{Z\_l+Z\_r}U\_j.\end{aligned}
$$
![Pressure continuity and equal normal velocity determine the early contact state.](../assets/figures/c3-e24.svg)

Pressure continuity and equal normal velocity determine the early contact state.

压力连续及相同法向速度确定早期接触状态。

Step 17 — substitute the momentum and compression equations into each characteristic derivative; the pressure-gradient terms and velocity-gradient terms cancel. The upstream-going liquid wave reduces speed from the incoming value to contact velocity, producing pressure equal to impedance times that speed reduction. The downstream receiver wave starts from rest. Match the two pressures, add the positive impedances in the denominator, and solve for contact velocity and pressure. As receiver impedance tends to infinity, contact velocity tends to zero and pressure approaches density times sound speed times incident speed. As receiver impedance tends to zero, pressure tends to zero. These limiting cases verify the sign and physical role of compliance. This is a transient deceleration calculation, with no harmonic forcing prerequisite. [MIT continuum acoustics: conservation, impedance and interface conditions](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/50a609ff2cc992401a099bca53801474_MIT6_013S09_chap13.pdf)

步骤 17——把动量及压缩方程代入各特征导数，压力梯度及速度梯度项相互抵消。向上游传播的液体波使速度从入射值降到接触速度，压力等于阻抗乘这一降速；接收体下行波从静止状态开始。匹配双方压力，在分母相加两个正阻抗，解出接触速度及压力。接收体阻抗趋于无穷时，接触速度趋零，压力趋于密度乘声速乘入射速度；接收体阻抗趋零时，压力趋零。这些极限核验符号及柔顺性的物理作用。这是瞬态减速计算，不需要外加简谐激励前置知识。[MIT 连续介质声学：守恒、阻抗及界面条件](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/50a609ff2cc992401a099bca53801474_MIT6_013S09_chap13.pdf)

**Symbols before Eq. (C3-E25).** $\mathcal J\_{\mathrm{rec}}$ is receiver normal contact impulse, $P\_{\mathrm{in}},P\_{\mathrm{out}}$ incoming/outgoing axial liquid momentum (N s). $m\_j$ emitted mass (kg), $\rho$ liquid density (kg m⁻³), $A\_j$ area (m²), $a\_j,L\_j$ radius/length (m), $U\_j$ incident speed and $c$ sound speed (m s⁻¹). $\tau\_{\mathrm{eq}}$ is an impulse-equivalent duration (s) for a fictitious uniform rigid-contact rectangle with zero outgoing axial momentum. $t\_{\mathrm{side}},t\_{\mathrm{axial}},t\_{\mathrm{early}},t\_{\mathrm{return}}$ are side-release, axial-release, early observation and first receiver-return times (s); $\min$ selects the earliest. The liquid momentum balance excludes additional direct source forces or a separate collapse shock; receiver support reactions affect receiver motion but are not counted as a second direct liquid impulse.

**式（C3-E25）前的符号定义。** $\mathcal J\_{\mathrm{rec}}$ 为接收体法向接触冲量，$P\_{\mathrm{in}},P\_{\mathrm{out}}$ 为入／出射液体轴向动量（N s）。$m\_j$ 为喷出质量（kg），$\rho$ 为密度（kg m⁻³），$A\_j$ 为面积（m²），$a\_j,L\_j$ 为半径／长度（m），$U\_j$ 为入射速度，$c$ 为声速（m s⁻¹）。$\tau\_{\mathrm{eq}}$ 为出射轴向动量为零时，假想均匀刚性接触矩形载荷的冲量等效时长（s）。$t\_{\mathrm{side}},t\_{\mathrm{axial}},t\_{\mathrm{early}},t\_{\mathrm{return}}$ 为侧向释放／轴向释放／早期观察／首个接收体回波时间（s）；$\min$ 取最早值。液体动量平衡排除额外直接源力或独立塌缩激波；接收体支撑反力影响其运动，但不另算为第二个直接液体冲量。

(C3-E25) · Finite momentum and early-impact duration conditions$$
\begin{aligned}\mathcal J\_{\mathrm{rec}}&=P\_{\mathrm{in}}-P\_{\mathrm{out}},\quad P\_{\mathrm{in}}=m\_jU\_j=\rho A\_jL\_jU\_j,\\ (\rho cU\_j)A\_j\tau\_{\mathrm{eq}}&=m\_jU\_j\ \Longrightarrow\ \tau\_{\mathrm{eq}}=L\_j/c,\\ t\_{\mathrm{side}}&=a\_j/c,\quad t\_{\mathrm{axial}}=L\_j/c,\quad t\_{\mathrm{early}}\ll\min(t\_{\mathrm{side}},t\_{\mathrm{axial}},t\_{\mathrm{return}}).\end{aligned}
$$
![A very large initial pressure has a finite momentum budget and restricted duration.](../assets/figures/c3-e25.svg)

A very large initial pressure has a finite momentum budget and restricted duration.

很大的初始压力仍受有限动量预算及持续时间限制。

Step 18 — integrate the receiver force over the full event and use the emitted control-volume momentum balance. Zero outgoing axial momentum gives the stopping impulse. Divide that finite impulse by a hypothetical full-area water-hammer force to obtain the equivalent duration. This does not justify a rectangular pressure trace: a central one-dimensional estimate also requires lateral release and receiver reflections to be absent over the observation interval. A thin film with bending and returning waves is not automatically a semi-infinite receiver. Rebound can increase axial momentum change; a separate collapse wave or continued source work must enter its own balance rather than being silently attributed to the finite plug.

步骤 18——在完整事件中积分接收体力，并使用喷出控制体动量平衡。出射轴向动量为零时得到停止冲量，再除以假想全面积水锤力得到等效时长。这并不支持矩形压力曲线：中心一维估计还要求观察期间没有侧向释放及接收体反射。存在弯曲及回波的薄膜并不自动等于半无限接收体。反弹可增加轴向动量变化；独立塌缩波或持续源做功应计入各自平衡，不能默默归给有限液柱。

**Symbols before Eq. (C3-E26).** $p\_{\mathrm{obs}}$ is signed area–time mean excess pressure (Pa), $p$ local pressure and $p\_{\mathrm{ref}}$ fixed reference (Pa); $\boldsymbol x$ position (m), $t$ current time and $\xi$ dummy time (s). $A\_o>0$ is the fixed observer area (m²), $\tau\_o>0$ averaging duration (s), $dA$ area element (m²), $\mathcal J\_{\mathrm{rec}}\ge0$ total compressive normal impulse over the observed footprint (N s). Integrals sum the area and preceding time window. The bound assumes negligible normal viscous stress, so excess pressure equals compressive normal traction; this excess must be nonnegative throughout the full-event footprint budget, with no omitted forces. An arbitrary signed waveform, finite normal viscous stress or a different interface does not satisfy these premises.

**式（C3-E26）前的符号定义。** $p\_{\mathrm{obs}}$ 为带符号面积—时间平均超压（Pa），$p$ 为局部压力、$p\_{\mathrm{ref}}$ 为固定参考值（Pa）；$\boldsymbol x$ 为位置（m），$t$ 为当前时间、$\xi$ 为积分时间（s）。$A\_o>0$ 为固定观察面积（m²），$\tau\_o>0$ 为平均时长（s），$dA$ 为面积微元（m²），$\mathcal J\_{\mathrm{rec}}\ge0$ 为观察载荷区域上的总法向压缩冲量（N s）。积分对面积及前一时间窗口求和。界限假设法向黏性应力可忽略，因而超压等于法向压缩牵引；在采用完整事件冲量预算的整个区域内，该超压须始终非负，且不存在漏项力。任意带符号波形、有限法向黏性应力或另一界面不满足这些前提。

(C3-E26) · Observer definition and conditional impulse bound$$
\begin{aligned}p\_{\mathrm{obs}}(t)&=\frac1{A\_o\tau\_o}\int\_{t-\tau\_o}^t\int\_{A\_o}[p(\boldsymbol x,\xi)-p\_{\mathrm{ref}}]\,dA\,d\xi,\\ 0\le p\_{\mathrm{obs}}(t)&\le\frac{\mathcal J\_{\mathrm{rec}}}{A\_o\tau\_o},\\ &\text{for nonnegative excess pressure, negligible normal viscous stress,}\\ &\text{and full-event footprint impulse }\mathcal J\_{\mathrm{rec}}.\end{aligned}
$$
![A reported maximum is meaningful only for an unchanged observer.](../assets/figures/c3-e26.svg)

A reported maximum is meaningful only for an unchanged observer.

仅在观察定义不变时，报告的最大值才具有可比较含义。

**Symbols before Eq. (C3-E27).** $E\_w$ is outgoing linear plane-wave energy crossing the stated footprint/window (J), $p'$ its pressure disturbance and $\overline p$ signed area–time mean (Pa), $Z\_l>0$ constant wave impedance (Pa s m⁻¹), $A\_o>0$ area (m²), $\tau\_o>0$ duration and $t$ time (s), $dA$ area element (m²). $\int$ is area/time integration and $|\ |$ magnitude. The premise is one-way linear pressure–velocity relation $u'=p'/Z\_l$, so intensity is $p'^2/Z\_l$. This is not an energy bound on arbitrary standing-wave or solid contact traction.

**式（C3-E27）前的符号定义。** $E\_w$ 为通过规定面积／时间窗口的单向线性平面波能量（J），$p'$ 为其压力扰动、$\overline p$ 为带符号面积—时间均值（Pa），$Z\_l>0$ 为恒定波阻抗（Pa s m⁻¹），$A\_o>0$ 为面积（m²），$\tau\_o>0$ 为时长、$t$ 为时间（s），$dA$ 为面积微元（m²）。$\int$ 为面积／时间积分，$|\ |$ 为大小。前提为单向线性压力—速度关系 $u'=p'/Z\_l$，故强度为 $p'^2/Z\_l$。它不是任意驻波或固体接触牵引的能量界。

(C3-E27) · One-way-wave energy and finite-observer Cauchy–Schwarz bound$$
\begin{aligned}E\_w&=\int\_0^{\tau\_o}\int\_{A\_o}\frac{p'^2}{Z\_l}\,dA\,dt,\qquad \overline p=\frac1{A\_o\tau\_o}\int\_0^{\tau\_o}\int\_{A\_o}p'\,dA\,dt,\\ |\overline p|^2&\le\frac1{A\_o\tau\_o}\int\_0^{\tau\_o}\int\_{A\_o}p'^2\,dA\,dt=\frac{Z\_lE\_w}{A\_o\tau\_o}.\end{aligned}
$$
![Finite area and time prevent an unmeasured point spike from standing in for delivered loading.](../assets/figures/c3-e27.svg)

Finite area and time prevent an unmeasured point spike from standing in for delivered loading.

有限面积及时间避免用未测量点尖峰代替实际传递载荷。

Step 19 — a nonnegative observed load in any subwindow cannot exceed its full-event impulse, yielding Eq. (C3-E26). For a one-way linear wave apply Cauchy–Schwarz to pressure and one over the area–time region, whose measure is area times duration; substituting wave energy gives Eq. (C3-E27). The assumptions differ and must not be merged into a universal theorem. They do show why reducing an observation window or area can raise a reported peak without increasing delivered energy. A pointwise mesh spike is not an experimentally resolved maximum. The highest single-shot output and the largest repeatable intact-transfer output require separate admissible sets and different evidence.

步骤 19——任意子窗口中非负观察载荷不能超过完整事件冲量，得到式（C3-E26）。对单向线性波，在面积—时间域上对压力及一应用 Cauchy–Schwarz，其测度为面积乘时长；代入波能量即得式（C3-E27）。两者假设不同，不能合并为普适定理。它们说明减小观察时间或面积可能提高报告峰值，却不增加传递能量。网格点尖峰不是实验已解析最大值。最高单次输出及最大可重复完整转印输出需要分开的可行域及不同证据。

**Symbols before Eq. (C3-E28).** $\rho(\boldsymbol x,t)$ is compressible density (kg m⁻³), $\boldsymbol u$ velocity (m s⁻¹), $p$ absolute thermodynamic pressure (Pa), $e$ specific internal energy and $e\_t$ total specific energy (J kg⁻¹). $\boldsymbol I$ is identity tensor; $\boldsymbol\tau$ viscous stress (Pa), $\boldsymbol q$ conductive heat flux (W m⁻²), $Q\_{\mathrm{abs}}$ optical volumetric heating (W m⁻³; zero after heating if no continued absorption). $\mathcal P$ is the adopted equation-of-state function; $Y\_k$ species mass fractions, $k$ species index (dimensionless). $\boldsymbol x$ position (m), $t$ time (s), $\partial\_t$ fixed-position derivative; $\nabla\cdot$ tensor/vector divergence, $\otimes$ tensor product and $\cdot$ contraction; $|\ |$ velocity norm.

**式（C3-E28）前的符号定义。** $\rho(\boldsymbol x,t)$ 为可压缩密度（kg m⁻³），$\boldsymbol u$ 为速度（m s⁻¹），$p$ 为绝对热力学压力（Pa），$e$ 为比内能、$e\_t$ 为总比能（J kg⁻¹）。$\boldsymbol I$ 为单位张量；$\boldsymbol\tau$ 为黏性应力（Pa），$\boldsymbol q$ 为导热通量（W m⁻²），$Q\_{\mathrm{abs}}$ 为光学体积加热（W m⁻³；加热后若无继续吸收则为零）。$\mathcal P$ 为采用的状态方程函数；$Y\_k$ 为组分质量分数，$k$ 为组分编号（无量纲）。$\boldsymbol x$ 为位置（m），$t$ 为时间（s），$\partial\_t$ 为固定位置导数；$\nabla\cdot$ 为张量／向量散度，$\otimes$ 为张量积、$\cdot$ 为缩并；$|\ |$ 为速度范数。

(C3-E28) · Compressible bulk conservation and required constitutive closure$$
\begin{aligned}\partial\_t\rho+\nabla\cdot(\rho\boldsymbol u)&=0,\\ \partial\_t(\rho\boldsymbol u)+\nabla\cdot(\rho\boldsymbol u\otimes\boldsymbol u+p\boldsymbol I-\boldsymbol\tau)&=0,\\ \partial\_t(\rho e\_t)+\nabla\cdot[(\rho e\_t+p)\boldsymbol u-\boldsymbol\tau\cdot\boldsymbol u+\boldsymbol q]&=Q\_{\mathrm{abs}},\quad e\_t=e+|\boldsymbol u|^2/2,\quad p=\mathcal P(\rho,e,\{Y\_k\}).\end{aligned}
$$
![Strong compression requires conservative evolution with an appropriate equation of state.](../assets/figures/c3-e28.svg)

Strong compression requires conservative evolution with an appropriate equation of state.

强压缩需要采用适当状态方程的守恒演化。

Step 20 — when wall or jet Mach number is no longer small, replace the incompatible incompressible/linear-impact control with conservation of mass, momentum and total energy. Momentum flux includes pressure and viscous traction; total-energy flux includes pressure work, viscous work and heat. Optical heating enters only once. Species conservation, phase-interface jumps, constitutive properties and solid response close the problem. Source history and incoming jet state must be inherited consistently. Sound speed signals that a model needs refinement; it is not a universal ceiling on laser-driven jet velocity. The highest achievable target value remains unresolved until source conversion, geometry, finite inventory, admissible damage and the observer are specified and verified. [[R5]](../reference/sources.html#r5)

步骤 20——壁面或射流 Mach 数不再小时，应以质量、动量及总能量守恒替代不相容的不可压缩／线性冲击对照。动量流率包含压力及黏性牵引；总能量流率包含压力做功、黏性做功及热。光学加热仅计一次。组分守恒、相界面跳跃、本构物性及固体响应闭合问题，并须自洽继承源历程及入射射流状态。声速意味着模型需要改进，并非激光射流速度的普适上限。最高目标值仍未解决，直到源转换、几何、有限储量、允许损伤及观察量均被规定并核验。[[R5]](../reference/sources.html#r5)

## 7. Carry the declared 25-cell example into the next chapter

## 7. 将明确声明的 25 单元算例接入下一章

Teaching control, not project measurements: 25 separate, independently supplied cells on a 5 × 5 pattern with 200 μm pitch. Each has the Chapter 2 PFP teaching inventory and 50 pL carrier. Ideal patterned/addressed illumination is assumed for equal optical allocation and the stipulated interception fraction; it is not the broad Gaussian uniformity control above. These are separate cells; the interacting triangle/square/pentagon solution is not a pressure multiplier to apply here. The Chapter 2 5-μm teaching PFP core is not silently relabeled a real nanodroplet.

教学对照，并非项目测量：25 个独立供液且相互分隔的单元，按 5 × 5、200 μm 间距排列。各单元采用第二章教学 PFP 储量及 50 pL 载液。为均等光能分配及规定截获比例，假设理想图案化／逐点寻址照明，并非前面的宽 Gaussian 均匀性对照。它们是分隔单元；不能将相互作用三角形／正方形／五边形解当作增压倍数应用于此。第二章 5 μm 教学 PFP 液核也不能默默改称真实纳米液滴。

Step 21 — allocate incident optical energy, then separately declare the thermal-routing and final kinetic-energy conversion assumptions. Incident energy is 25 μJ, intercepted fraction 0.8, effective absorptance 0.5. Equal division gives 400 nJ absorbed per site. Assume 40% has reached the PFC by the activation deadline, so its 160 nJ exceeds the approximately 97.82-nJ preparation estimate from Chapter 2. This comparison does not certify the spatial temperature or nucleation timing. Independently assume final emitted-jet kinetic energy is 0.5% of absorbed energy. The thermal fraction and jet fraction represent successive transfers of the same energy, not disjoint quantities to add together.

步骤 21——先分配入射光能，再分别声明热路由及最终动能转换假设。入射能为 25 μJ，截获比例 0.8，有效吸收率 0.5。均分后各位点吸收 400 nJ。假设激活截止时有 40% 到达 PFC，因此其 160 nJ 超过第二章约 97.82 nJ 的准备估计；但这一比较不能证明空间温度或成核时序。另假设最终喷出射流动能为吸收能的 0.5%。热比例及射流比例表示同一能量的连续转移，并非可相加的互斥预算项。

**Symbols before Eq. (C3-E29).** $E\_L$ is incident laser energy, $E\_{\mathrm{abs,tot}}$ total absorbed energy, $E\_{\mathrm{abs,site}}$ per-site absorbed energy, $E\_{\mathrm{PFC,deadline}}$ energy delivered to that PFC inventory by the activation deadline, $E\_j$ final per-jet kinetic energy and $E\_{j,\mathrm{tot}}$ total jet energy (J; μJ = 10⁻⁶ J, nJ = 10⁻⁹ J). $N\_d=25$ is site count; $f\_{\mathrm{geo}}=0.8$ intercepted fraction, $A\_\lambda=0.5$ effective absorptance at laser wavelength $\lambda$ (m), $f\_T=0.40$ stipulated thermal fraction and $\eta\_j=0.005$ stipulated absorbed-to-jet kinetic efficiency (dimensionless). Subscripts label reservoirs/stages.

**式（C3-E29）前的符号定义。** $E\_L$ 为入射激光能，$E\_{\mathrm{abs,tot}}$ 为总吸收能，$E\_{\mathrm{abs,site}}$ 为单个位点吸收能，$E\_{\mathrm{PFC,deadline}}$ 为激活截止前到达该 PFC 储量的能量，$E\_j$ 为最终单射流动能、$E\_{j,\mathrm{tot}}$ 为总射流动能（J；μJ = 10⁻⁶ J，nJ = 10⁻⁹ J）。$N\_d=25$ 为位点数；$f\_{\mathrm{geo}}=0.8$ 为截获比例，$A\_\lambda=0.5$ 为激光波长 $\lambda$（m）处有效吸收率，$f\_T=0.40$ 为假设热比例，$\eta\_j=0.005$ 为假设吸收能至射流动能效率（无量纲）。下标区分能量库／阶段。

(C3-E29) · Declared optical and mechanical allocation$$
\begin{aligned}E\_{\mathrm{abs,tot}}&=f\_{\mathrm{geo}}A\_\lambda E\_L=(0.8)(0.5)(25\,\mu\mathrm J)=10\,\mu\mathrm J,\\ E\_{\mathrm{abs,site}}&=E\_{\mathrm{abs,tot}}/N\_d=400\,\mathrm{nJ},\quad E\_{\mathrm{PFC,deadline}}=f\_T E\_{\mathrm{abs,site}}=160\,\mathrm{nJ},\\ E\_j&=\eta\_j E\_{\mathrm{abs,site}}=2.00\,\mathrm{nJ},\quad E\_{j,\mathrm{tot}}=N\_dE\_j=50.0\,\mathrm{nJ}.\end{aligned}
$$
![Energy allocations follow the project chain without double counting.](../assets/figures/c3-e29.svg)

Energy allocations follow the project chain without double counting.

沿项目因果链分配能量，并避免重复计数。

**Symbols before Eq. (C3-E30).** $m\_j$ is per-jet carrier mass (kg), $\rho=1000$ kg m⁻³ carrier density; $d\_j=10\times10^{-6}$ m diameter and $L\_j=50\times10^{-6}$ m emitted length supply the first row. $E\_j=2.00\times10^{-9}$ J is per-jet kinetic energy; $U\_j$ uniform speed (m s⁻¹), $q\_j=\rho U\_j^2/2$ dynamic pressure and $p\_{\mathrm{rigid,early}}$ early rigid-contact pressure (Pa; MPa = 10⁶ Pa). $c=1480$ m s⁻¹ is stipulated sound speed; $P\_j,P\_{\mathrm{tot}}$ per-jet and total aligned incoming momentum (N s); $\pi$ dimensionless. Uniform direction, full activation and independent cells are assumed.

**式（C3-E30）前的符号定义。** $m\_j$ 为单射流载液质量（kg），$\rho=1000$ kg m⁻³ 为载液密度；$d\_j=10\times10^{-6}$ m 直径及 $L\_j=50\times10^{-6}$ m 喷出长度用于第一行。$E\_j=2.00\times10^{-9}$ J 为单射流动能；$U\_j$ 为均匀速度（m s⁻¹），$q\_j=\rho U\_j^2/2$ 为动压，$p\_{\mathrm{rigid,early}}$ 为早期刚性接触压力（Pa；MPa = 10⁶ Pa）。$c=1480$ m s⁻¹ 为给定声速；$P\_j,P\_{\mathrm{tot}}$ 为单射流及总对齐入射动量（N s）；$\pi$ 无量纲。假设方向相同、全部激活且单元独立。

(C3-E30) · Worked finite jet mass, speed and pressure scales$$
\begin{aligned}m\_j&=(1000\,\mathrm{kg\,m^{-3}})\frac{\pi(10\times10^{-6}\,\mathrm m)^2}{4}(50\times10^{-6}\,\mathrm m)\simeq3.926991\times10^{-12}\,\mathrm{kg},\\ U\_j&=\sqrt{\frac{2(2.00\times10^{-9}\,\mathrm J)}{3.926991\times10^{-12}\,\mathrm{kg}}}\simeq31.91538\,\mathrm{m\,s^{-1}},\\ q\_j&\simeq0.5092958\,\mathrm{MPa},\quad p\_{\mathrm{rigid,early}}=\rho cU\_j\simeq47.23477\,\mathrm{MPa},\\ P\_j&=m\_jU\_j\simeq1.253314\times10^{-10}\,\mathrm{N\,s},\quad P\_{\mathrm{tot}}=25P\_j\simeq3.133285\times10^{-9}\,\mathrm{N\,s}.\end{aligned}
$$
![The finite state carried to Chapter 4 includes mass and energy, not only a pressure peak.](../assets/figures/c3-e30.svg)

The finite state carried to Chapter 4 includes mass and energy, not only a pressure peak.

传入第四章的有限状态包含质量及能量，而非只有压力峰值。

| Checked quantity  已核验量 | Result  结果 | Interpretation  解释 |
| --- | --- | --- |
| Emitted volume per site  各位点喷出体积 | 3.926991 pL  3.926991 pL | Below the 50-pL carrier inventory  小于 50 pL 载液储量 |
| Total emitted mass  总喷出质量 | 98.17477 ng  98.17477 ng | 25 independent finite jets  25 个独立有限射流 |
| Emission duration estimate  发射时长估计 | 1.566643 μs  1.566643 μs | Length divided by assigned uniform speed  长度除以给定均匀速度 |
| Flight across 100 μm air gap  飞越 100 μm 气隙 | 3.133285 μs  3.133285 μs | No dense-liquid drag assumed  假设无稠密液体阻力 |
| Impulse-equivalent early duration  冲量等效早期时长 | 33.78378 ns  33.78378 ns | Not a predicted rectangular pulse  并非预测矩形脉冲 |
| Side-release scale  侧向释放尺度 | 3.378378 ns  3.378378 ns | Central 1D impact requires still earlier observation  中心一维冲击要求更早观察 |
| Reynolds / Weber / Ohnesorge  Reynolds／Weber／Ohnesorge 数 | 319.1538 / 141.4711 / 0.0372678  319.1538 / 141.4711 / 0.0372678 | Diameter-based diagnostics  以直径定义的诊断量 |
| Capillary time / fastest wavelength  毛细时间／最快波长 | 1.317616 μs / 45.07184 μm  1.317616 μs／45.07184 μm | Radius-based infinite-cylinder benchmark  以半径定义的无限圆柱对照 |
| Arrival disturbance from 1% initial amplitude  初始 1% 振幅的到达扰动 | 2.26247% of radius  半径的 2.26247% | Linear control permits coherent arrival  线性对照允许相干到达 |
| 1% to 10% radius linear-threshold time  半径 1% 到 10% 的线性阈值时间 | 8.836529 μs  8.836529 μs | A declared validity screen, not pinch-off time  声明的适用性筛查，并非夹断时间 |
| Formal extrapolation from 1% to full radius  1% 到整个半径的形式外推 | 17.67306 μs  17.67306 μs | Reproduces source estimate outside linear validity  还原原文估计，但超出线性适用范围 |

All numerical properties and efficiencies in this worked control are stipulated water-like teaching inputs, not a calibrated PFC formulation. The 47.2348-MPa value is an early rigid-contact scale with a nanosecond spatial-validity condition. Sustaining that full-area pressure over the 1.5666-μs emitted duration would demand 46.37 times the plug's available axial momentum. The incoming energy remains 2.00 nJ per site or 50.0 nJ total. Chapter 4 will test whether the actual footprint, time history and force path deliver enough opening work without damaging the film. A high early-impact scale can therefore coexist with failure of an intact-transfer fracture-energy screen.

本对照所有物性及效率均为给定类水教学输入，并非已标定 PFC 配方。47.2348 MPa 是具有纳秒空间适用条件的早期刚性接触尺度。若将其保持在全部面积上、持续整个 1.5666 μs 喷出时间，则需液柱可用轴向动量的 46.37 倍。入射能仍为每位点 2.00 nJ 或总计 50.0 nJ。第四章将检验实际载荷区域、时间历程及传力路径，能否传递足够开裂功且不损伤薄膜。因此高的早期冲击尺度完全可以与完整转印断裂能筛查失败同时存在。

## 8. Three graduation-defense questions

## 8. 三道毕业答辩式问题

### Why is a uniform 25-site PFC array not a free 25-fold pressure amplifier, and how would you calculate it fairly?

### 为什么均匀的 25 位点 PFC 阵列不是免费的 25 倍增压器？应如何公平计算？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C3-E31).** Original formulas: $i,j$ index bubbles; $R\_i,R\_j,d\_{ij}$ are radius/separation (m), dots time derivatives; $p\_{b,i},p\_\infty,\Delta p\_c>0$ are bubble pressure, ambient pressure and constant ideal collapse difference (Pa). $\sigma\_b$ tension (N m⁻¹), $\mu$ viscosity (Pa s), $\rho$ carrier density (kg m⁻³), $\sum$ sums neighbors. $N$ is count, $E\_{B,\mathrm{tot}}$ fixed total initial pressure work (J), $R\_{\max,N}$ per-bubble maximum radius and $R\_\*$ isolated reference radius (m); $\pi$ dimensionless, $\*$ reference label. The coupled row requires far separation; the fixed-work row assumes identical constant-pressure ideal cavities.

**式（C3-E31）前的符号定义。** 原始公式：$i,j$ 为气泡编号；$R\_i,R\_j,d\_{ij}$ 为半径／间距（m），点为时间导数；$p\_{b,i},p\_\infty,\Delta p\_c>0$ 为泡内压力、环境压力、恒定理想塌缩压差（Pa）。$\sigma\_b$ 为张力（N m⁻¹），$\mu$ 为黏度（Pa s），$\rho$ 为载液密度（kg m⁻³），$\sum$ 对邻泡求和。$N$ 为数量，$E\_{B,\mathrm{tot}}$ 为固定初始总压力做功（J），$R\_{\max,N}$ 为单泡最大半径、$R\_\*$ 为孤立参考半径（m）；$\pi$ 无量纲，$\*$ 为参考标签。耦合行要求充分分离；固定做功行假设相同恒定压力理想腔体。

(C3-E31) · Reference answer: original interaction and allocation formulas$$
\begin{aligned}R\_i\ddot R\_i+\frac32\dot R\_i^2&=\frac{p\_{b,i}-p\_\infty-2\sigma\_b/R\_i-4\mu\dot R\_i/R\_i}{\rho}-\sum\_{j\ne i}\frac{R\_j^2\ddot R\_j+2R\_j\dot R\_j^2}{d\_{ij}},\\ E\_{B,\mathrm{tot}}&=N\frac{4\pi}{3}\Delta p\_cR\_{\max,N}^3,\qquad R\_{\max,N}=R\_\*N^{-1/3}.\end{aligned}
$$
![Use connectivity and source allocation before any sum of outputs.](../assets/figures/c3-e31.svg)

Use connectivity and source allocation before any sum of outputs.

求和输出前先确定液体连通性及源分配。

I would first distinguish uniform core size, carrier supply, pitch, fluence and activation timing, then check whether cells are hydraulically separated. For separate cells I can add emitted energies and aligned momenta only after calculating each finite jet; pressures remain local unless their fields overlap at a defined observer. For connected bubbles I solve the coupled source histories because neighbors change surrounding pressure and liquid inertia. Regular spacing does not remove edge effects or missing activations. The three/four/five polygon control demonstrates delayed contraction at fixed per-bubble radius, while the fixed-total-work calculation makes radii shrink as count rises. Neither predicts a count-proportional useful pressure.

我会先区分均匀芯尺寸、载液供应、间距、通量及激活时序，再判断单元是否液压分隔。分隔单元中，只有各有限射流求出后才能累加喷出能量及对齐动量；压力仍为局部量，除非它们在已定义观察量中重叠。连通气泡必须求耦合源历程，因为邻泡改变周围压力及液体惯性。规则间距不能去掉边缘效应及漏激活。三／四／五泡多边形对照展示固定单泡半径时收缩延迟，而固定总做功计算要求数量增加时半径缩小。两者都不预测有用压力正比于数量。

At 25 sites and 0.95 independent activation probability, low count variability still permits only 27.7% complete activation. I would measure site-resolved activation and arrival-time variation, not only a total count. I would retain the common energy budget and propagate delays to the receiver. Near contact, coalescence, deformation or strong waves, the monopole model must be replaced; its analytic time table is a control, not the final PFC-array solution.

25 个位点、独立激活概率 0.95 时，即使数量变化小，全部激活也仅有 27.7% 概率。我会测各位点激活及到达时间变化，而不只看总数量；保留统一能量预算并把延迟传播至接收体。邻泡接触、合并、变形或强波阶段必须替换单极子模型；解析时间表只是对照，并非最终 PFC 阵列解。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Distinguishes optical/statistical uniformity from hydraulic independence, including activation and arrival-time evidence.

  区分光学／统计均匀性与液压独立性，并说明激活及到达时序证据。
* Explains neighbor-pressure coupling and fixed-total-energy allocation without multiplying single-bubble pressure by count.

  解释邻泡压力耦合及固定总能量分配，避免把单泡压力直接乘数量。
* States the separated-spherical and weak-wave limits, and keeps the polygon control separate from the independent-cell example.

  说明分离球形及弱波限制，并把多边形对照与独立单元算例分开。

### What must be solved between a cavity calculation and a useful coherent jet, and why can a faster tip be a worse transfer actuator?

### 从腔体计算到有用相干射流之间必须求解什么？为什么更快尖端可能是更差的转印致动器？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C3-E32).** Original formulas: $U\_{\mathrm{rms}}$ is mass-weighted speed, $U\_j$ uniform benchmark speed (m s⁻¹), $m\_j>0$ emitted carrier mass (kg), $E\_{\mathrm{avail}},E\_j$ available and kinetic energy (J), $P\_j$ directional momentum (N s). $a\_0,H,\delta\_0,\delta\_{\mathrm{arr}}$ are base radius, gap, initial and arriving disturbance amplitude (m); $g\_{\max}$ fastest cylinder growth rate (s⁻¹), $\exp$ exponential of dimensionless argument. Growth assumes constant inviscid base cylinder and a small perturbation in negligible surrounding gas.

**式（C3-E32）前的符号定义。** 原始公式：$U\_{\mathrm{rms}}$ 为质量加权速度，$U\_j$ 为均匀对照速度（m s⁻¹），$m\_j>0$ 为喷出载液质量（kg），$E\_{\mathrm{avail}},E\_j$ 为可用能及动能（J），$P\_j$ 为方向动量（N s）。$a\_0,H,\delta\_0,\delta\_{\mathrm{arr}}$ 为基态半径、间隙、初始及到达扰动振幅（m）；$g\_{\max}$ 为最快圆柱增长率（s⁻¹），$\exp$ 为无量纲自变量的指数。增长假设恒定无黏基态圆柱、微小扰动及周围气体动力学可忽略。

(C3-E32) · Reference answer: original finite-mass and growth formulas$$
U\_{\mathrm{rms}}\le\sqrt{\frac{2E\_{\mathrm{avail}}}{m\_j}},\qquad P\_j^2\le2m\_jE\_j,\qquad \frac{\delta\_{\mathrm{arr}}}{a\_0}=\frac{\delta\_0}{a\_0}\exp(g\_{\max}H/U\_j).
$$
![Speed, focusing and survival must refer to the same emitted liquid state.](../assets/figures/c3-e32.svg)

Speed, focusing and survival must refer to the same emitted liquid state.

速度、聚焦及存活须指向同一喷出液体状态。

A radius equation cannot tell me the jet shape or whether an internal liquid finger becomes an external transfer jet. I need the actual moving interfaces, pressure history, wall/outlet conditions and a compatible energy balance. Fixed total impulse and fixed total energy are different focusing controls: reducing mass fourfold at fixed impulse increases speed and required energy fourfold; at fixed energy speed only doubles and available directional momentum halves. Thus a tiny fast tip need not deliver useful loading. I would report tip speed, finite emitted mass, mass-weighted speed, directional momentum and energy separately.

半径方程不能告诉我射流形状，也不能证明内部液指成为外部转印射流。我需要实际运动界面、压力历程、壁面／出口条件及相容能量平衡。固定总冲量与固定总能量是不同聚焦对照：质量降为四分之一时，固定冲量使速度及所需能量均增大四倍；固定能量则只使速度增大两倍，并使可用方向动量减半。因此微小高速尖端未必提供有用载荷。我会分别报告尖端速度、有限喷出质量、质量加权速度、方向动量及能量。

After a slender jet exists, its mass and axial momentum equations determine thinning and curvature-driven redistribution. I compare disturbance growth during the actual flight with a declared small threshold. In the 25-cell control, a 1%-radius disturbance reaches about 2.26% over a 3.133-μs gap crossing, so coherent arrival is plausible within the cylinder model. The 17.7-μs full-radius extrapolation is not an exact breakup time. Finite ends, startup shape, stretch, viscosity and a dense surrounding liquid can change survival; evidence should include time-resolved jet shape and delivered mass at the receiver.

射流形成细长形态后，质量及轴向动量方程决定变细和曲率驱动的再分配。我比较实际飞行期间扰动增长与明确小阈值。在 25 单元对照中，初始半径 1% 的扰动经过 3.133 μs 跨隙后约为 2.26%，因此在圆柱模型内相干到达可行。17.7 μs 全半径外推并非精确断裂时间。有限端部、初始形状、拉伸、黏性及稠密周围液体都会改变存活；证据应包括时间分辨射流形状及接收位置到达质量。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Explains why spatial interface geometry and source/wall conditions are required for a directional emitted jet.

  解释定向喷出射流为什么需要空间界面几何及源／壁面条件。
* Separates fixed impulse, fixed energy and fixed impulse per area; connects finite mass to speed, momentum and focusing cost.

  区分固定冲量、固定能量及固定单位面积冲量，将有限质量联系至速度、动量及聚焦代价。
* Uses flight-time versus disturbance-growth reasoning and acknowledges nonlinear/finite-length breakdown instead of guaranteeing breakup-free arrival.

  用飞行时间与扰动增长推理，并承认非线性／有限长度失效，避免保证无断裂到达。

### Why can a 47-MPa early impact scale coexist with failed transfer, and what makes a reported maximum scientifically comparable?

### 为什么 47 MPa 早期冲击尺度可以与转印失败并存？怎样使报告的最大值具有科学可比性？

Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.

请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。

\*\*Reference answer and mastery criteria / 参考答案与掌握标准\*\*

**Symbols before Eq. (C3-E33).** Original formulas: $p\_{\mathrm{early}}$ is early compressive impact scale and $p\_{\mathrm{obs}}$ signed finite-observer mean (Pa), $Z\_l,Z\_r>0$ liquid/receiver impedances (Pa s m⁻¹), $\rho$ carrier density (kg m⁻³), $c$ sound speed and $U\_j$ incident speed (m s⁻¹), $L\_j$ finite jet length (m), $\tau\_{\mathrm{eq}}$ rigid stopping-impulse equivalent duration (s). $A\_o$ observation area and $dA$ element (m²), $\tau\_o$ averaging duration, $t$ current time and $\xi$ dummy time (s), $p,p\_{\mathrm{ref}}$ local/reference pressure (Pa). $\int$ integrates local pressure $p(\boldsymbol x,\xi)$ over the footprint/window, with position $\boldsymbol x$ (m) implicit. Impact is locally one-dimensional and linear; equivalent duration assumes zero outgoing axial momentum and no added force source.

**式（C3-E33）前的符号定义。** 原始公式：$p\_{\mathrm{early}}$ 为早期压缩冲击尺度，$p\_{\mathrm{obs}}$ 为带符号有限观察均值（Pa），$Z\_l,Z\_r>0$ 为液体／接收体阻抗（Pa s m⁻¹），$\rho$ 为载液密度（kg m⁻³），$c$ 为声速、$U\_j$ 为入射速度（m s⁻¹），$L\_j$ 为有限射流长度（m），$\tau\_{\mathrm{eq}}$ 为刚性停止冲量等效时长（s）。$A\_o$ 为观察面积、$dA$ 为面积微元（m²），$\tau\_o$ 为平均时长，$t$ 为当前时间、$\xi$ 为积分时间（s），$p,p\_{\mathrm{ref}}$ 为局部／参考压力（Pa）。$\int$ 将局部压力 $p(\boldsymbol x,\xi)$ 在载荷区域／窗口积分，位置 $\boldsymbol x$（m）为隐含自变量。冲击局部一维且线性；等效时长假设出射轴向动量为零且无额外力源。

(C3-E33) · Reference answer: original impact and observer formulas$$
p\_{\mathrm{early}}\simeq\frac{Z\_lZ\_r}{Z\_l+Z\_r}U\_j,\quad Z\_l=\rho c,\qquad \tau\_{\mathrm{eq}}=\frac{L\_j}{c},\qquad p\_{\mathrm{obs}}(t)=\frac1{A\_o\tau\_o}\int\_{t-\tau\_o}^t\int\_{A\_o}(p-p\_{\mathrm{ref}})\,dA\,d\xi.
$$
![A finite impact scale is an input to load-path analysis, not proof of intact release.](../assets/figures/c3-e33.svg)

A finite impact scale is an input to load-path analysis, not proof of intact release.

有限冲击尺度是传力路径分析的输入，并非完整释放的证明。

The 47.2348-MPa teaching value follows from initially compressing a nearly rigid contact, not from a pressure sustained for the emitted jet's full duration. Its corresponding incoming state is only 3.92699 ng, 2 nJ and 1.25331 × 10⁻¹⁰ N s per jet. An equivalent rectangle would last 33.78 ns, while lateral release matters on about 3.38 ns in this narrow jet. Actual pressure needs a resolved time history and receiver response. I would fix the pressure location, reference, footprint, bandwidth and averaging interval, then check momentum and energy against the same finite state.

47.2348 MPa 教学值来自近乎刚性接触的初始压缩，并非整个射流喷出期间持续的压力。其对应入射状态每射流仅为 3.92699 ng、2 nJ、1.25331 × 10⁻¹⁰ N s。等效矩形时长为 33.78 ns，而这一细射流侧向释放约在 3.38 ns 上已重要。实际压力需要已解析时间历程及接收体响应。我会固定压力位置、参考值、载荷区域、带宽及平均时间，再用同一有限状态核验动量与能量。

This does not yet determine opening at a buried release interface. Chapter 4 must transmit loading through the chosen liquid/film/PVC path and test interface strength, fracture work and payload damage. A 50-nJ total jet-energy budget can fail the release-work requirement despite an impressive nanosecond contact pressure. For a maximum I would constrain laser/absorber damage, PFC and carrier inventory, geometry, finite measured mass and observer; I would report the best verified single shot separately from a repeatable intact-transfer envelope. I would not claim a universal limit from singular collapse or count alone.

这仍未决定埋藏释放界面的张开。第四章必须沿所选液体／薄膜／PVC 路径传递载荷，并检验界面强度、断裂功及载荷损伤。即使纳秒接触压力很高，50 nJ 总射流能预算仍可能不满足释放功需求。定义最大值时，我会约束激光／吸收体损伤、PFC 及载液储量、几何、有限实测质量及观察量；把已核验的最好单次结果与可重复完整转印范围分别报告，而不从奇异塌缩或数量本身声称普适极限。

#### What a mastered answer demonstrates

#### 掌握后的回答应体现

* Distinguishes dynamic pressure, early impedance pressure, finite observed pressure and buried-interface opening traction.

  区分动压、早期阻抗压力、有限观察压力及埋藏界面张开牵引。
* Explains finite mass/energy/impulse and duration, retaining the exact 25-cell state for fracture analysis.

  解释有限质量／能量／冲量及持续时间，并保留明确的 25 单元状态用于断裂分析。
* Defines the observer and operating constraints, separates single-shot output from repeatable intact transfer, and identifies unresolved geometry/material evidence.

  定义观察量及运行约束，分开单次输出与可重复完整转印，并指出尚缺的几何／材料证据。