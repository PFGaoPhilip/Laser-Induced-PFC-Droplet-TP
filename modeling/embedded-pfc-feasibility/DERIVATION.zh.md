# 水凝胶中的有限 PFC：推导与验证要求

## 1. 问题、目标与范围

确定完整水凝胶内 PFC 蒸气核膨胀所需的状态能量。计算凝胶载荷与能量。明确外部排液和塌缩压力所需的额外条件。

本**有条件研究**求解有限 PFC 质量、同心气液相、真实流体热力学、独立界面、凝胶弹性和基质黏性。瞬态从**预设的成核后种子**开始。其保留能量相对全液态参考计算。激光加热与种子形成仍未解决。

保留两类模型。第一类求解指定半径的曲面平衡与局部稳定性。第二类求解指定种子的绝热径向膨胀。首次转折、预设伸长比或时间截止时停止。两者出口流量均为零。有效无限、不排水凝胶保留径向惯性。省略液壳惯性、温度梯度、相变动力学、损伤、水蒸气、气体扩散及声辐射。内界面牵引为准静态。这些假设限定全部结果。

采用从液滴中心向外的球坐标。两种半径均为正。膨胀时径向速度为正。热力学压力为**绝对压力**。阻力和压差为带符号超压。初始液体受到外界面毛细牵引与环境载荷。无穷远处位移和速度消失，应力趋于负环境压力。PFC 质量封闭，外排质量通量为零。两相温度均匀且化学势相等。这是激活后的平衡近似。纳秒内热均匀化**尚未确立**。

全液态参考从室温、指定半径和 Laplace 压力开始。种子的初始伸长比为 1.2，速度为零，累积损耗为零。液压超过静态基质牵引 50 kPa。计入种子储能与环境功。这里假定无损制备；省略成核前热、黏性和声学损失。选定筛查值以内的凝胶弹性可逆。黏性加热基质。伸长比 2.1 是**预设停止值**。实测破坏应变**尚未确立**。

基础：质量守恒；热力学第一定律；Helmholtz 状态方程 [S2](SOURCES.md)；连续介质界面能和牵引；不可压缩 neo-Hookean 弹性；Kelvin–Voigt 黏性；球形惯性 [S6, S8](SOURCES.md)。核／壳闭合及比较为原创降阶计算。物理验证需要激活数据、半径历史、损伤、外排质量通量及指定传感器处的压力。

## 2. 符号表与约定

所有标量为实数。圆周率无量纲。长度上标表示幂；点表示时间导数。下标 `0`、`l`、`v`、`o`、`i`、`el`、`amb`、`gel`、`host` 分别表示初始、液体、蒸气、外、内、弹性、环境、凝胶及有效基质。偏导数保持指定条件变量不变。积分使用注明的坐标、面积、体积或时间测度。对数和指数的自变量无量纲。算术、不等式与极限遵循通常的实数约定。

| 符号 | 定义与适用域 | 单位 |
|---|---|---|
| $t$ | 从预设种子开始计时；非负 | s |
| $a_0,R,b,W$ | 初始液滴半径；当前外半径；蒸气核半径；径向壁速；$0<b<R$，$W=\dot R$ | m, m, m, m/s |
| $V_0,V,V_b,V_l$ | 初始液滴、当前液滴、蒸气核及液壳体积 | m³ |
| $m,m_l,m_v,x_v$ | 固定 PFC 质量；液体与蒸气质量；蒸气质量分数 | kg, kg, kg, 无量纲 |
| $T,T_0$ | 均匀 PFC 温度与初始液态参考温度 | K |
| $\rho_l,\rho_v,\rho_{l0},\rho_h$ | 液相、汽相、初始液相及有效不排水基质密度 | kg/m³ |
| $p_l,p_v,p_\infty,p_{l0}$ | 液体、蒸气、环境及初始液体绝对压力 | Pa |
| $\gamma_o,\gamma_i$ | 对照中的恒定外侧液／水及内侧液／气张力 | N/m |
| $a_H,u,s_H,g$ | 比 Helmholtz 能、内能、熵及 Gibbs 能／化学势；均为温度和密度／状态的函数 | J/kg, J/kg, J/(kg K), J/kg |
| $S,A_i,P_{abs},t'$ | PFC 总熵；蒸气核内界面面积；吸收光功率；积分时间变量 | J/K, m², W, s |
| $u_l,u_v,u_{l0},g_l,g_v$ | 各相比内能、初始液体比内能及相化学势 | J/kg |
| $G,\eta$ | 基质剪切模量及 Kelvin–Voigt 黏度 | Pa, Pa s |
| $s,r,\lambda_r,\lambda_\theta,\beta,C$ | 参考／当前基质径向坐标；径向／周向伸长比；参考／当前半径比；径向体积偏移 | m, m, 无量纲, 无量纲, 无量纲, m³ |
| $\sigma_{rr},\sigma_{\theta\theta},\chi$ | 弹性 Cauchy 应力与不可压缩约束乘子 | Pa |
| $p_{el},p_{vis},p_{need}$ | 弹性阻力、黏性阻力及基质所需静态液压 | Pa |
| $u_h,D_{rr},D_{\theta\theta}$ | 基质径向速度及对角形变率 | m/s, 1/s, 1/s |
| $U_{PFC},E_{gel},E_{surf},E_{amb},K_h,D_h$ | PFC 内能、凝胶应变能、界面能变化、环境功、径向基质动能及累积基质损耗 | J |
| $P_{dis},E_{seed},\epsilon_E$ | 基质损耗功率；相对全液态参考的保留种子能量；归一化能量残差 | W, J, 无量纲 |
| $\lambda,\epsilon,k_E,k_T$ | 外半径伸长比；小伸长扰动；闭能量／定温压力恢复导数 | 无量纲, 无量纲, Pa／单位无量纲伸长比, 同前 |
| $p_s,U_s,\tau,E_s$ | 压力、速度、时间与能量归一化尺度 | Pa, m/s, s, J |
| $\theta,\widehat W,\widehat D$ | 归一化时间、径向速度与累积损耗 | 无量纲 |
| $F_{loc},C_{abs},f_t,E_{abs}$ | 局部光能流密度、有效吸收截面、归一化脉冲形状及吸收能量 | J/m², m², 1/s, J |
| $\Delta p,r_n,\Delta\mathcal G,r_*,\Delta\mathcal G_*,J_n,\mathcal P$ | 亚稳汽核压力驱动差；汽核半径；成核自由能变化；临界半径／势垒；成核速率；激活概率 | Pa, m, J, m, J, 1/(m³ s), 无量纲 |
| $G_c,\mathcal G_f,\Pi,A_c,\delta,t_c,t_m,\delta_0,\delta_f$ | 临界断裂能；能量释放率；势能；投影裂纹面积；开度；黏聚牵引；峰值牵引；峰值开度；最终分离 | J/m², J/m², J, m², m, Pa, Pa, m, m |
| $h,a_c,E_{cr}$ | 初始液滴上方覆盖厚度、狭缝半宽及示例断裂功 | m, m, J |
| $E,\rho,p$ | 径向稳定性中的固定能量标签；一般相密度与压力 | J, kg/m³, Pa |
| $\tau_{poro},L_h$ | 孔压扩散时间及排水长度 | s, m |
| $\mathbf x,\Omega_l$ | 位置向量及液体空间域 | m, 域 |
| $q,n,F,K_l,K_v,\kappa_l,\kappa_v,H_{core}$ | 蒸气体积与质量坐标；内部 Helmholtz 能；相压力－密度斜率；体积缩放斜率；松弛蒸气核曲率 | m³, kg, J, Pa m³/kg, 同前, Pa/kg, 同前, Pa/m³ |
| $d,\lambda_{surface}$ | 中心到初始自由表面的距离及接触初始平面的伸长比 | m, 无量纲 |
| $c_h,k_p,M_p,\mu_w,\alpha_h,\tau_p$ | 声速；凝胶渗透率；孔弹性模量；孔隙液黏度；基质热扩散率；脉冲时长 | m/s, m², Pa, Pa s, m²/s, s |

凝胶模量、黏度、光截面、覆盖厚度、黏聚强度及韧性均为预设值。目标配方尚未实测。[来源台账](SOURCES.md)说明界面与状态方程输入的依据。

## 3. 分步推导

### 步骤 1 — 定义体积、有限相质量与初始参考

**式 (E01) 前的符号：**$a_0,R,b$ 为初始液体、当前外侧及蒸气核半径（m），满足 $0<b<R$；$V_0,V,V_b,V_l$ 为对应体积（m³）；圆周率无量纲。这些是同心球的几何恒等式。

$$
V_0=\frac{4\pi a_0^3}{3},\qquad
V=\frac{4\pi R^3}{3},\qquad
V_b=\frac{4\pi b^3}{3},\qquad V_l=V-V_b. \tag{E01}
$$

末式从液滴总体积减去蒸气体积。剩余液体壳层是独立区域。体积须乘相密度才能得到质量。

**式 (E02) 前的符号：**$m,m_l,m_v$ 为固定总 PFC、液相及汽相质量（kg）；$\rho_{l0},\rho_l,\rho_v$ 为初始液相及当前相密度（kg/m³）；$V_0,V_l,V_b$ 为体积（m³）；$x_v$ 为无量纲蒸气质量分数。密度与总质量严格为正。

$$
\begin{aligned}
m&=\rho_{l0}V_0,\qquad m_l=\rho_lV_l,\qquad m_v=\rho_vV_b,\\
m_l+m_v&=m,\qquad x_v=\frac{m_v}{m},\qquad 0<x_v<1. \tag{E02}
\end{aligned}
$$

首行用状态方程密度定义质量。次行施加封闭 PFC 质量守恒，并除以正初始质量。负液壳体积或越界蒸气分数的根均被拒绝，即使非线性求解器收敛。

**式 (E03) 前的符号：**$p_{l0},p_\infty$ 为初始液体与环境绝对压力（Pa）；$\gamma_o$ 为恒定外张力（N/m）；$a_0$ 为初始半径（m）；$T_0$ 为初始温度（K）；$\rho_{l0}$ 为初始液体密度（kg/m³）；$\rho_l(T,p)$ 为液相状态方程密度函数。初始凝胶未伸长。

$$
p_{l0}=p_\infty+\frac{2\gamma_o}{a_0},\qquad
\rho_{l0}=\rho_l(T_0,p_{l0}). \tag{E03}
$$

首式采用初始液态外界面的球形毛细牵引。次式在该压力下求液体状态。压差单位为 N/m 除以 m，即 Pa，并随半径增加而下降。

### 步骤 2 — 使用真实流体状态方程并分别处理界面

**式 (E04) 前的符号：**$a_H(T,\rho)$ 为比 Helmholtz 能（J/kg）；$T$ 为温度（K）；$\rho$ 为一般相密度（kg/m³）；$p,u,s_H,g$ 分别为压力（Pa）、比内能（J/kg）、比熵（J/(kg K)）及化学势（J/kg）。偏导保持下标变量不变。采用状态方程 [S2](SOURCES.md)求这些热力学恒等式。

$$
\begin{aligned}
p&=\rho^2\left(\frac{\partial a_H}{\partial\rho}\right)_T,
&s_H&=-\left(\frac{\partial a_H}{\partial T}\right)_\rho,\\
u&=a_H+Ts_H,
&g&=a_H+\frac{p}{\rho}. \tag{E04}
\end{aligned}
$$

首行按指定自变量对 Helmholtz 能求导。次行重建内能与 Gibbs 能。压力除以密度的单位是 J/kg，因此 Gibbs 表达式量纲一致。两相采用相同能量参考。压力由真实流体状态方程计算。

**式 (E05) 前的符号：**$p_v,p_l$ 为蒸气与液体绝对压力（Pa）；$g_v,g_l$ 为两相化学势（J/kg）；$\gamma_i$ 为恒定内张力（N/m）；$b$ 为正蒸气核半径（m）；$T$ 为均匀温度（K）。等温与瞬时相平衡为采用的本构近似；界面为球形。

$$
p_v-p_l=\frac{2\gamma_i}{b},\qquad g_l(T,p_l)=g_v(T,p_v). \tag{E05}
$$

毛细关系使用**内侧**液／气界面。化学平衡令不同相压力下的化学势相等。平面饱和压力不能直接替代它们。将全部界面张力设为水／气的 0.072 N/m 会改变问题。小蒸气核提高毛细压差；分子尺度下连续曲率和恒定张力近似变得不确定。

### 步骤 3 — 推导完整球形凝胶阻力

**式 (E06) 前的符号：**$s,r$ 为正参考与当前基质径向坐标（m）；$R,a_0$ 为当前与初始液滴半径（m）；$C$ 为体积偏移参数（m³）；$\lambda_r,\lambda_\theta$ 为无量纲径向／周向伸长比；$d r/d s$ 为径向导数。假设球形不可压缩运动，且 $r\ge R$。

$$
\begin{aligned}
r^3-R^3&=s^3-a_0^3,\qquad C=R^3-a_0^3,\\
r^3&=s^3+C,\qquad 3r^2\frac{dr}{ds}=3s^2,\\
\lambda_r&=\frac{dr}{ds}=\frac{s^2}{r^2},\qquad
\lambda_\theta=\frac{r}{s},\qquad
\lambda_r\lambda_\theta^2=1. \tag{E06}
\end{aligned}
$$

首行保持内界面与任意外侧材料球间的基质体积。次行合并常量并对参考半径求导。除以正半径平方得到第三行，明确验证体积比为一。

**式 (E07) 前的符号：**$\sigma_{rr},\sigma_{\theta\theta},\chi,G$ 为弹性径向应力、切向应力、不可压缩乘子及正剪切模量（Pa）；$\lambda_r,\lambda_\theta$ 为式 (E06) 的无量纲伸长比；$r$ 为当前半径（m）；$d/dr$ 表示空间求导。采用不可压缩 neo-Hookean 本构与弹性径向平衡。

$$
\sigma_{rr}=-\chi+G\lambda_r^2,\qquad
\sigma_{\theta\theta}=-\chi+G\lambda_\theta^2,\qquad
\frac{d\sigma_{rr}}{dr}=-\frac{2(\sigma_{rr}-\sigma_{\theta\theta})}{r}. \tag{E07}
$$

前两式定义基质材料律。相减消去未知乘子。末式为球对称弹性应力散度，用于计算弹性牵引。惯性与黏性在下文分别加入。

**式 (E08) 前的符号：**$p_{el}$ 为弹性壁阻力（Pa）；$G$ 为剪切模量（Pa）；$R,a_0,r,s$ 为半径（m）；$\beta=s/r$ 无量纲；$C=R^3-a_0^3$ 在膨胀时为正（m³）；$\int$ 表示空间定积分。上限无穷表示有效无限基质。$R=a_0$ 时取连续极限。

$$
\begin{aligned}
p_{el}
&=2G\int_R^\infty\left[\left(\frac r s\right)^2-\left(\frac s r\right)^4\right]\frac{dr}{r},\\
\beta^3&=1-\frac C{r^3},\qquad
3\beta^2\,d\beta=\frac{3C}{r^4}\,dr,\qquad
\frac{dr}{r}=\frac{\beta^2}{1-\beta^3}\,d\beta,\\
p_{el}
&=2G\int_{a_0/R}^{1}\frac{1-\beta^6}{1-\beta^3}\,d\beta
=2G\int_{a_0/R}^{1}(1+\beta^3)\,d\beta,\\
p_{el}
&=2G\left[\beta+\frac{\beta^4}{4}\right]_{a_0/R}^{1}
=\frac G2\left[5-4\frac{a_0}{R}-\left(\frac{a_0}{R}\right)^4\right]. \tag{E08}
\end{aligned}
$$

结合远场应力条件积分式 (E07)，得到首行。式 (E06) 给出变量变换及 Jacobian。内边界比值为初始／当前液滴半径；无穷远处趋于一。分子分解为一减三次方与一加三次方的乘积。在有限膨胀半径处约去非零因子。端点采用可去极限。末行计算两个端点。该结果依赖球形几何。平面层断裂需要另一模型。

**式 (E09) 前的符号：**$E_{gel}$ 为可恢复凝胶应变能（J）；$p_{el}$ 为阻力（Pa）；$R,a_0,\xi$ 为当前、初始与积分半径（m）；$G$ 为剪切模量（Pa）；$dE_{gel}/dR$ 为半径导数。积分沿可逆完整分支进行。 $\pi$ 为无量纲圆周率。

$$
\begin{aligned}
E_{gel}
&=\int_{a_0}^{R}4\pi\xi^2p_{el}(\xi)\,d\xi\\
&=2\pi G\int_{a_0}^{R}(5\xi^2-4a_0\xi-a_0^4\xi^{-2})\,d\xi\\
&=2\pi G\left[\frac{5\xi^3}{3}-2a_0\xi^2+\frac{a_0^4}{\xi}\right]_{a_0}^{R}\\
&=2\pi G\left[\frac{5R^3}{3}-2a_0R^2+\frac{a_0^4}{R}-\frac{2a_0^3}{3}\right],\\
\frac{dE_{gel}}{dR}&=4\pi R^2p_{el}(R). \tag{E09}
\end{aligned}
$$

首行以压力乘腔体体积增量定义功。次行代入式 (E08) 并展开。逐项积分各幂得到第三行。初始端点给出第四行常量。求导独立验证末式；审查脚本也作符号检验。

**式 (E10) 前的符号：**$\lambda=R/a_0$ 为伸长比；$\epsilon$ 为小无量纲伸长增量；$p_{el}$ 为阻力（Pa）；$E_{gel}$ 为应变能（J）；$G$ 为模量（Pa）；$a_0$ 为半径（m）；$O$ 表示增量趋零时的渐近余项阶数。 $\pi$ 为无量纲圆周率。

$$
\begin{aligned}
\lambda=1:&\quad p_{el}=0,\quad E_{gel}=0,\\
\lambda\to\infty:&\quad p_{el}\to\frac{5G}{2},\\
\lambda=1+\epsilon:&\quad p_{el}=4G\epsilon+O(\epsilon^2),\qquad
E_{gel}=8\pi G a_0^3\epsilon^2+O(\epsilon^3). \tag{E10}
\end{aligned}
$$

直接代入式 (E08)–(E09)，得到零伸长结果。半径比趋零给出大伸长弹性极限。将倒数伸长比及四次幂展开到一阶，得到压力展开。积分该压力与主阶体积导数的乘积，得到能量展开。大伸长压力极限属于完整 neo-Hookean 模型。实际凝胶破裂压力**尚未确立**。

### 步骤 4 — 计算基质惯性与黏性耗散

**式 (E11) 前的符号：**$u_h(r,t)$ 为基质径向速度（m/s）；$R,r$ 为液滴与基质半径（m）；$W$ 为内壁速度（m/s）；$\rho_h$ 为基质密度（kg/m³）；$K_h$ 为基质动能（J）；$\int$ 在有效无限不可压缩基质中作空间积分。 $\pi$ 为无量纲圆周率。

$$
\begin{aligned}
4\pi r^2u_h&=4\pi R^2W,\qquad u_h=\frac{R^2W}{r^2},\\
K_h&=\frac{\rho_h}{2}\int_R^\infty u_h^2\,4\pi r^2\,dr\\
&=2\pi\rho_hR^4W^2\int_R^\infty r^{-2}\,dr
=2\pi\rho_hR^3W^2. \tag{E11}
\end{aligned}
$$

不可压缩条件给出首个通量关系。除以正面积得到速度。将速度平方代入动能，约去两个半径幂。反平方半径的原函数为负反半径。无穷远端点为零；内端点贡献液滴半径倒数。保留基质惯性，省略液壳惯性。完整空间模型须检验此省略。

**式 (E12) 前的符号：**$D_{rr},D_{\theta\theta}$ 为基质径向／切向形变率（1/s）；$u_h$ 为径向速度（m/s）；$r,R$ 为半径（m）；$W$ 为壁速（m/s）；$\eta$ 为有效黏度（Pa s）；$P_{dis}$ 为黏性损耗功率（W）；$p_{vis}$ 为黏性壁阻力（Pa）。两个切向分量相等。 $\pi$ 为无量纲圆周率。

$$
\begin{aligned}
D_{rr}&=\frac{\partial u_h}{\partial r}=-\frac{2R^2W}{r^3},\qquad
D_{\theta\theta}=\frac{u_h}{r}=\frac{R^2W}{r^3},\\
P_{dis}&=\int_R^\infty 2\eta(D_{rr}^2+2D_{\theta\theta}^2)\,4\pi r^2\,dr\\
&=48\pi\eta R^4W^2\int_R^\infty r^{-4}\,dr
=16\pi\eta R W^2,\\
p_{vis}&=\frac{P_{dis}}{4\pi R^2W}=\frac{4\eta W}{R}\quad(W\ne0),
\qquad p_{vis}=0\quad(W=0). \tag{E12}
\end{aligned}
$$

对式 (E11) 求导，并将速度除以半径，得到首行。三个形变率分量平方求和，得到六倍共同因子。反四次幂积分贡献反三次方半径除以三。非零壁速时，损耗功率除以带符号体积通量得到黏性牵引。零壁速采用连续极限，避免除零。两种运动方向的损耗功率均非负。

**式 (E13) 前的符号：**$R,W$ 为半径与速度（m、m/s）；$\rho_h$ 为密度（kg/m³）；$p_l,p_\infty,p_{el},p_{vis},p_{need}$ 为压力（Pa）；$\gamma_o$ 为外张力（N/m）；点为时间导数。径向动量方程采用不可压缩基质近似。

$$
\begin{aligned}
p_{need}&=p_\infty+p_{el}+\frac{2\gamma_o}{R},\\
\dot R&=W,\qquad
\rho_h\left(R\dot W+\frac32W^2\right)=p_l-p_{need}-p_{vis},\\
\dot W&=\frac{1}{R}\left[\frac{p_l-p_{need}-4\eta W/R}{\rho_h}-\frac32W^2\right]. \tag{E13}
\end{aligned}
$$

首行合并环境、弹性和外侧毛细静态阻力。次行由剩余牵引驱动球形惯性。除以正密度和半径，再代入式 (E12)，得到第三行。动量方程两侧单位均为 Pa。初速为零时，正超额牵引产生正加速度。弹性与黏性为零时，退化为毛细球形惯性对照。定向射流须另行求解。

### 步骤 5 — 核算 PFC、界面、凝胶、环境与动能

**式 (E14) 前的符号：**$U_{PFC},E_{surf},E_{amb}$ 为内能、界面能变化与环境功（J）；$m_l,m_v$ 为相质量（kg）；$u_l,u_v$ 为各相比内能（J/kg）；$\gamma_o,\gamma_i$ 为两个独立恒定张力（N/m）；$R,a_0,b$ 为半径（m）；$p_\infty$ 为环境压力（Pa）；$V,V_0$ 为液滴体积（m³）。初始内能参考在下文定义。 $\pi$ 为无量纲圆周率。

$$
U_{PFC}=m_lu_l+m_vu_v,\qquad
E_{surf}=4\pi[\gamma_o(R^2-a_0^2)+\gamma_i b^2],\qquad
E_{amb}=p_\infty(V-V_0). \tag{E14}
$$

实际相内能已包含相变能量。另加独立潜热项会重复计数。初始状态有外侧液体表面，无蒸气核。因此内表面能全部新增。两种表面项的单位均为 N/m 乘 m²，即 J。恒定张力假设界面熵可忽略，并省略壳／涂层重排。

**式 (E15) 前的符号：**$U_{PFC}$ 为 PFC 内能（J）；$T$ 为共同相温度（K）；$S$ 为 PFC 总熵（J/K）；$g_l,g_v$ 为化学势（J/kg）；$m_l,m_v$ 为质量（kg）；$p_l,p_v$ 为压力（Pa）；$V_l,V_b,V$ 为相／总体积（m³）；$\gamma_i$ 为恒定内张力（N/m）；$A_i=4\pi b^2$ 为蒸气核面积（m²）；$d$ 为沿可容许平衡轨迹的微分。 $b$ 为正蒸气核半径（m）。

$$
\begin{aligned}
dU_{PFC}&=T\,dS-p_l\,dV_l-p_v\,dV_b+g_l\,dm_l+g_v\,dm_v,\\
dm_l&=-dm_v,\quad g_l=g_v,\quad dV_l=dV-dV_b,\\
dU_{PFC}&=T\,dS-p_l\,dV-(p_v-p_l)\,dV_b,\\
\gamma_i\,dA_i&=\frac{2\gamma_i}{b}\,dV_b=(p_v-p_l)\,dV_b,\\
d(U_{PFC}+\gamma_i A_i)&=T\,dS-p_l\,dV. \tag{E15}
\end{aligned}
$$

首行分别应用热力学基本关系并求和。封闭质量与式 (E05) 消去化学项。体积相减给出第三行。对蒸气核面积和体积求导，其比值为二除以核半径。式 (E05) 使内牵引功与表面能变化相消。末式说明曲面核界面能必须计入总能量。可逆绝热调相时，温度－熵项为零。审查在未施加熵方程时检验熵漂移。

**式 (E16) 前的符号：**$E_{seed}$ 为无损种子制备下相对全液态参考的保留能量（J）；$m$ 为固定 PFC 质量（kg）；$u_{l0}$ 为初始液体比内能（J/kg）；$U_{PFC},E_{gel},E_{surf},E_{amb},K_h,D_h$ 为 PFC、凝胶、界面、环境、动能与损耗能量（J）；$t,t'$ 为结束与积分时间（s），撇号是标签；$P_{dis}$ 为损耗功率（W）；$\epsilon_E$ 无量纲。种子后的系统绝热；无后续热源或外流。

$$
\begin{aligned}
D_h(t)&=\int_0^t P_{dis}(t')\,dt',\qquad \dot D_h=P_{dis},\\
E_{seed}&=U_{PFC}-m u_{l0}+E_{gel}+E_{surf}+E_{amb}+K_h+D_h,\\
\epsilon_E&=\frac{U_{PFC}-m u_{l0}+E_{gel}+E_{surf}+E_{amb}+K_h+D_h-E_{seed}}{E_{seed}}. \tag{E16}
\end{aligned}
$$

首行定义累积基质损耗。次行相对全液态参考核算保留种子能量。末行在正种子能量下定义数值残差。与实测激光吸收能量对应时，还须核算成核前导热、基质耗散、声辐射及其他材料受热。这里未计算这些制备过程，因此预算无法给出激活阈值。凝胶耗散成为不可恢复的基质热，未重复反馈给 PFC。模型省略基质与 PFC 间导热。

**式 (E17) 前的符号：**$K_h$ 为基质动能（J）；$\rho_h$ 为密度（kg/m³）；$R,W$ 为半径与速度（m、m/s）；$p_l,p_\infty,p_{el},p_{vis}$ 为压力（Pa）；$\gamma_o$ 为外张力（N/m）；点为时间导数。功率计算沿式 (E13) 进行。 $\pi$ 为无量纲圆周率。

$$
\begin{aligned}
\dot K_h&=2\pi\rho_h[3R^2W^3+2R^3W\dot W]\\
&=4\pi R^2W\rho_h\left[R\dot W+\frac32W^2\right]\\
&=4\pi R^2W\left[p_l-p_\infty-p_{el}-\frac{2\gamma_o}{R}-p_{vis}\right]. \tag{E17}
\end{aligned}
$$

对式 (E11) 应用乘积法则与式 (E13) 的半径导数。提取共同体积通量并代入动量。对式 (E16) 求导时，式 (E09) 消去弹性功率；式 (E14) 的导数消去环境与外表面功率；式 (E12) 消去黏性功率。式 (E15) 消去剩余 PFC／内界面功率。因此采用的动力学与第一定律一致。符号求导检验前两行；原生／参考比较检验实现。省略物理仍待验证。

### 步骤 6 — 写出稳态与瞬态闭合

**式 (E18) 前的符号：**$R,b$ 为指定外半径与未知核半径（m）；$T$ 为未知共同温度（K）；$\rho_l,\rho_v$ 为未知密度（kg/m³）；$p(T,\rho),g(T,\rho)$ 为状态方程压力及化学势函数（Pa、J/kg）；$p_{need}$ 为静态所需液压（Pa）；$\gamma_i$ 为内张力（N/m）；$V,V_b$ 为体积（m³）；$m$ 为固定质量（kg）。根须满足正相压缩性与有效质量分配。

$$
\begin{cases}
p(T,\rho_l)-p_{need}=0,\\
p(T,\rho_v)-p(T,\rho_l)-2\gamma_i/b=0,\\
g(T,\rho_l)-g(T,\rho_v)=0,\\
\rho_l(V-V_b)+\rho_vV_b-m=0.
\end{cases} \tag{E18}
$$

在指定伸长比下，这四式确定温度、密度及核半径。它们给出静态相平衡根。稳定性与越过成核势垒须分别检验。动能和损耗为零时，式 (E16) 给出状态能量。原生稳态模型从扰动初猜求解全部四式。

**式 (E19) 前的符号：**$R,W,D_h$ 为半径、壁速与累积损耗（m、m/s、J）；$T,\rho_l,\rho_v,b$ 为四个代数未知量（K、kg/m³、kg/m³、m）；$p_l,p_{need}$ 为压力（Pa）；$\eta,\rho_h,\gamma_i$ 为黏度、基质密度及内张力（Pa s、kg/m³、N/m）；$p(T,\rho),g(T,\rho)$ 为状态方程压力与化学势函数（Pa、J/kg），$\rho$ 为密度自变量（kg/m³）；$V,V_b$ 为液滴与核体积（m³）；$m$ 为固定质量（kg）；$U_{PFC},u_{l0},E_{gel},E_{surf},E_{amb},K_h,E_{seed}$ 为此前定义的能量／参考比内能（J、J/kg）。点为时间导数。$\pi$ 为无量纲圆周率。$R,b,\rho_h$ 为正；相态须有效。

$$
\begin{aligned}
\dot R&=W,\\
\dot W&=\frac{(p_l-p_{need}-4\eta W/R)/\rho_h-3W^2/2}{R},\\
\dot D_h&=16\pi\eta R W^2,\\
0&=p(T,\rho_v)-p(T,\rho_l)-2\gamma_i/b,\\
0&=g(T,\rho_l)-g(T,\rho_v),\\
0&=\rho_l(V-V_b)+\rho_vV_b-m,\\
0&=U_{PFC}-m u_{l0}+E_{gel}+E_{surf}+E_{amb}+K_h+D_h-E_{seed}.
\tag{E19}
\end{aligned}
$$

前三式分别计算半径、动量及累积损耗。内牵引、相平衡、质量与总能量给出四个代数条件。原生模型有七个归一化 Global Equations 变量。Python 独立求热力学根以消去四个代数未知量，并积分三个微分状态。比较的是相同本构假设下的求解实现。独立实验理论仍待建立。

**式 (E20) 前的符号：**$p_s,U_s,\tau,E_s$ 为正压力、速度、时间与能量尺度（Pa、m/s、s、J）；$\rho_h,a_0,m$ 为正基质密度、初始半径与质量（kg/m³、m、kg）；$\theta,\lambda,\widehat W,\widehat D$ 为归一化时间、半径、速度及损耗；$t,R,W,D_h$ 为有量纲时间、半径、速度及损耗（s、m、m/s、J）；$p_l,p_{need}$ 为压力（Pa）；$\eta$ 为黏度（Pa s）。帽号表示无量纲量。$d/d\theta$ 为归一化时间求导。平方根取正分支；$\lambda>0$ 允许相除。

$$
\begin{aligned}
U_s&=\sqrt{p_s/\rho_h},\quad \tau=a_0/U_s,\quad E_s=m(10^5\ {\rm J/kg}),\\
\theta&=t/\tau,\quad\lambda=R/a_0,\quad\widehat W=W/U_s,\quad\widehat D=D_h/E_s,\\
\frac{d\lambda}{d\theta}&=\widehat W,\\
\frac{d\widehat W}{d\theta}
&=\frac1\lambda\left[\frac{p_l-p_{need}}{p_s}
-4\frac{\eta}{a_0\sqrt{\rho_h p_s}}\frac{\widehat W}{\lambda}
-\frac32\widehat W^2\right]. \tag{E20}
\end{aligned}
$$

前两行定义尺度与变量。链式法则给出第三行。将有量纲半径与速度代入式 (E13)，乘以时间／速度尺度，再用速度平方定义将各驱动压力除以压力尺度。因此固定黏度与压力尺度时，无量纲黏性系数反比于初始半径。正压力／密度允许取平方根，所得单位为速度。

### 步骤 7 — 在指定热约束下检验稳定性

**式 (E21) 前的符号：**$\lambda$ 为伸长比；$\epsilon$ 为小无量纲扰动；$p_l(\lambda;E)$ 为闭总能量相态闭合的液压（Pa），固定能量标签 $E$ 单位为 J；$p_{need}(\lambda)$ 为静态所需压力（Pa）；$k_E$ 为闭能量压力恢复导数（Pa／单位伸长比）。中心状态为可容许稳态根；两侧相根也须可容许。

$$
k_E=-\left.\frac{d[p_l(\lambda;E)-p_{need}(\lambda)]}{d\lambda}\right|_E
\approx-\frac{[p_l-p_{need}]_{\lambda+\epsilon,E}-[p_l-p_{need}]_{\lambda-\epsilon,E}}{2\epsilon}. \tag{E21}
$$

正斜率使径向扰动恢复。半径增大产生向内不平衡；半径减小产生向外不平衡。负斜率局部不稳定。在伸长偏移 0.0001 和 0.00005 处重新求相态与能量根。两侧状态须有效。步骤 11 单独检验内部相态／核变化。非球形稳定性**尚未确立**。定温导数 $k_T$（Pa／单位伸长比）固定温度。132 个采样状态中，闭能量非恢复状态为 36 个，定温为 94 个。

### 步骤 8 — 分别测量光学加热与成核

**式 (E22) 前的符号：**$F_{loc}$ 为局部能流密度（J/m²）；$C_{abs}$ 为有效吸收截面（m²）；$f_t(t)$ 为非负脉冲形状（1/s）；$t$ 为时间（s）；$P_{abs}(t)$ 为吸收功率（W）；$E_{abs}$ 为吸收能量（J）。脉冲形状的时间积分为一。下标 `abs` 表示吸收，系数尚未实测。

$$
\int f_t(t)\,dt=1,\qquad
P_{abs}(t)=F_{loc}C_{abs}f_t(t),\qquad
E_{abs}=\int P_{abs}(t)\,dt=F_{loc}C_{abs}. \tag{E22}
$$

将功率表达式代入能量积分，并提出固定能流密度与截面。归一化得到末式。投影圆盘比较将截面除以正面积 $\pi a_0^2$（m²）。该有效几何比值可以超过一。须测量吸收截面、负载量、PFC 与水的热分配及深度衰减。保留种子能量不能替代这些数据。

**式 (E23) 前的符号：**$\Delta\mathcal G(r_n)$ 为汽核形成自由能（J）；$r_n$ 为试探蒸气核半径（m）；$\gamma_i$ 为液／汽张力（N/m）；$\Delta p>0$ 为亚稳液体成核近似的驱动压差（Pa）；$r_*$ 为临界核半径（m）；$\Delta\mathcal G_*$ 为临界势垒（J）。采用经典均质、球形、恒定张力近似。吸收体异质位点需单独建模。 $\pi$ 为无量纲圆周率。

$$
\begin{aligned}
\Delta\mathcal G(r_n)&=4\pi\gamma_i r_n^2-\frac{4\pi}{3}\Delta p\,r_n^3,\\
\frac{d\Delta\mathcal G}{dr_n}&=8\pi\gamma_i r_n-4\pi\Delta p\,r_n^2
=4\pi r_n(2\gamma_i-\Delta p\,r_n),\\
r_*&=\frac{2\gamma_i}{\Delta p},\qquad
\left.\frac{d^2\Delta\mathcal G}{dr_n^2}\right|_{r_*}=-8\pi\gamma_i<0,\\
\Delta\mathcal G_*&=4\pi\gamma_i\frac{4\gamma_i^2}{\Delta p^2}
-\frac{4\pi}{3}\Delta p\frac{8\gamma_i^3}{\Delta p^3}
=\frac{16\pi\gamma_i^3}{3\Delta p^2}. \tag{E23}
\end{aligned}
$$

首行采用表面成本减压力－体积收益。显式求导、因式分解并求正半径驻点。零半径是初始边界状态。负二阶导说明驻点为势垒最大值。代入临界半径得到末行。驱动压差须由实际亚稳液体状态及相变驱动化学势计算。环境沸点无法单独给出它。非正压差下没有正临界半径。异质位点因子与动力学前因子尚未标定。

**式 (E24) 前的符号：**$\mathcal P$ 为激活概率；$J_n(T,p_l)$ 为成核速率密度（1/(m³ s)）；$V_l(t)$ 为液体体积（m³）；$t,t'$ 为结束与积分时间（s）；$T$ 为局部温度（K）；$p_l$ 为液压（Pa）；$\mathbf x$ 为空间位置（m）；$\Omega_l(t)$ 为液体域；$dV$ 为体积测度（m³）；exp 为无量纲自变量的指数函数。采用独立成核事件的 Poisson 危险率假设。第二个等号要求液域内速率均匀。

$$
\begin{aligned}
\mathcal P(t)&=1-\exp\left[-\int_0^t\int_{\Omega_l(t')}J_n(T(\mathbf x,t'),p_l(\mathbf x,t'))\,dV\,dt'\right],\\
&=1-\exp\left[-\int_0^t J_n(T(t'),p_l(t'))V_l(t')\,dt'\right]\quad\text{(uniform-rate control)}. \tag{E24}
\end{aligned}
$$

危险率积分无量纲且非负。因此概率位于零与一之间。异质成核需要单位匹配的位点或面积危险率。**未解决：**吸收体／位点分布、动力学前因子及温度历史。激活阈值**尚未确立**。须测量随能流密度变化的激活比例，并设置无液滴及无吸收体对照。

### 步骤 9 — 外部排液需要断裂功与液压连通

**式 (E25) 前的符号：**$\mathcal G_f$ 为能量释放率（J/m²）；$\Pi$ 为适当的力学势能（J）；$A_c$ 为投影裂纹扩展面积（m²）；$G_c$ 为临界断裂能（J/m²）。导数在指定载荷约束下求取；温度、速率及含水量影响韧性。

$$
\mathcal G_f=-\frac{d\Pi}{dA_c},\qquad
\mathcal G_f\ge G_c\quad\hbox{is an energetic propagation condition}. \tag{E25}
$$

能量条件仍未确定起裂、路径、开度与充液。定压和闭能量载荷给出不同释放率。韧性与强度须独立于模量实测。当前原生对照不含损伤律。

**式 (E26) 前的符号：**$t_c(\delta)$ 为黏聚法向牵引（Pa）；$\delta$ 为开度（m）；$t_m>0$ 为峰值牵引（Pa）；$0<\delta_0<\delta_f$ 为峰值开度与最终分离（m）；$G_c$ 为每单位投影裂纹面积、包含两个断裂面的断裂能（J/m²）；$d\delta$ 为开度积分测度。这是需要标定的双线性黏聚本构示例。

$$
\begin{aligned}
t_c(\delta)&=\begin{cases}
t_m\delta/\delta_0,&0\le\delta\le\delta_0,\\
t_m(\delta_f-\delta)/(\delta_f-\delta_0),&\delta_0<\delta\le\delta_f,\\
0,&\delta>\delta_f,
\end{cases}\\
G_c&=\int_0^{\delta_f}t_c(\delta)\,d\delta
=\frac{t_m\delta_0}{2}+\frac{t_m(\delta_f-\delta_0)}2
=\frac{t_m\delta_f}{2},\\
\delta_f&=\frac{2G_c}{t_m}. \tag{E26}
\end{aligned}
$$

上升段与下降段分别按三角形积分。两段底边相加等于最终开度，峰值开度从总功中消去。除以正峰值强度得到最终分离。单位为 J/m² 除以 Pa，即 m。韧性无法单独确定峰值牵引与初始黏聚刚度。COMSOL 官方示例说明实现路线 [S10](SOURCES.md)。这里未给出目标凝胶实测值。

**式 (E27) 前的符号：**$h$ 为**初始**液滴表面到凝胶自由表面的覆盖厚度（m）；$a_c$ 为假定矩形狭缝半宽（m）；$A_c$ 为投影裂纹面积（m²）；$G_c$ 为包含两面的断裂能（J/m²）；$E_{cr}$ 为断裂功估计（J）；$E_{seed}$ 为保留种子能量（J）。理想狭缝与种子能量分配为预设筛查。裂纹路径与普适能量上界尚未求出。

$$
\begin{aligned}
A_c&=2a_ch,\qquad E_{cr}=G_cA_c=2G_ca_ch,\\
E_{seed}<E_{cr}&\ \Longrightarrow\ \hbox{slit work exceeds retained seed energy alone}. \tag{E27}
\end{aligned}
$$

狭缝长度乘宽度得到投影面积。面积乘韧性得到功。将该功与分配的保留种子能量比较。断裂不可能性**尚未确立**。冷却可降低 PFC 内能；拓扑变化可释放界面能。上界需要其他参考能量变化均非负，或计算指定终态的可用能量。这里两者均未确立。缺陷、路径、宽度、预应力及后续热量也影响预算。通过筛查仍未确定起裂、连通、开度与供液。覆盖厚度改变假定狭缝成本；轨迹仍使用无限基质。定义中心到表面距离 $d=a_0+h$（m）。定义接触伸长比 $\lambda_{surface}=d/a_0$（无量纲）。$R\ge d$ 时液滴与初始表面平面相交。更小间距仍需检验有限域收敛。3 µm 半径、1 µm 覆盖给出伸长比 1.333，低于 2.1。

### 步骤 10 — 检验长度／时间范围并区分观测量

**式 (E28) 前的符号：**$G,\eta$ 为剪切模量与黏度（Pa、Pa s）；$a_0$ 为初始半径（m）；$\gamma_o$ 为外张力（N/m）；$\rho_h,p_s$ 为基质密度与压力尺度（kg/m³、Pa）；$\alpha_h$ 为基质热扩散率（m²/s）；$\tau_p$ 为激光时长（s）；$W,c_h$ 为径向速度与声速（m/s）。竖线表示绝对值。平方根取正分支。分母各尺度为正。各比值无量纲。

$$
\frac{Ga_0}{\gamma_o},\qquad
\frac{\eta}{a_0\sqrt{\rho_h p_s}},\qquad
\frac{\alpha_h\tau_p}{a_0^2},\qquad
\frac{|W|}{c_h}. \tag{E28}
$$

首项比较弹性与毛细压力尺度。第二项为式 (E20) 的系数。第三项是基质热 Fourier 数。脉冲期间该值较小表示加热局部化；PFC 温度均匀性仍待检验。第四项筛查径向运动的可压缩效应。对照采用 Mach 0.1 上限。压力波与塌缩预测需要可压缩空间守恒、相应流体状态方程及传感器位置／带宽。

**式 (E29) 前的符号：**$\tau_{poro}$ 为孔压扩散时间尺度（s）；$\mu_w$ 为孔隙液黏度（Pa s）；$L_h$ 为排水距离（m）；$k_p$ 为渗透率（m²）；$M_p$ 为孔弹性模量（Pa）。采用量纲孔弹性扩散估计；目标输入尚未实测。

$$
\tau_{poro}\sim\frac{\mu_w L_h^2}{k_p M_p}. \tag{E29}
$$

扩散率尺度为渗透率乘模量再除以流体黏度。排水长度平方除以该扩散率得到时间。采用不排水基质前，须与事件时长比较。相关长度是局部排水路径，应根据实际几何确定。特别对纳米腔体，未经测量的渗透率可能使不排水近似失效。

径向壁速、连通出口液速与内部塌缩微射流速度是不同观测量。源压力、弹性阻力、动压、目标压力与有限带宽传感器压力也各不相同。理想孤立球形模型没有定向射流动量。原始 1.625 m/s 出口结果属于其出口算例，无法直接赋给当前径向运动或塌缩。水锤尺度无法给出实测峰值。实际压力曲线由可压缩性、接触时长、几何与接收体响应决定。

### 步骤 11 — 固定温度、体积与质量的内部稳定性

**式 (E30) 前的符号：**$T$ 为固定均匀温度（K）；$V$ 为固定液滴体积（m³）；$m$ 为固定 PFC 质量（kg）。独立坐标为蒸气体积 $q=V_b$（m³）及蒸气质量 $n=m_v$（kg），满足 $0<q<V$、$0<n<m$。液体体积 $V_l=V-q$（m³）；液体质量 $m_l=m-n$（kg）。密度为 $\rho_l=m_l/V_l$、$\rho_v=n/q$（kg/m³）。蒸气核半径 $b=(3q/(4\pi))^{1/3}$（m）。$F$ 为含核表面的内部 Helmholtz 能（J）；$a_H(T,\rho)$ 为比 Helmholtz 能（J/kg）；$\gamma_i$ 为恒定内张力（N/m）；$\pi$ 为圆周率。固定外体积时，外表面、凝胶及环境项不变。

$$
F(q,n)=m_l a_H(T,\rho_l)+n a_H(T,\rho_v)+4\pi\gamma_i b^2. \tag{E30}
$$

各相的定温微分为化学势乘质量变化减压力乘体积变化。定义 $g_l,g_v$（J/kg）和 $p_l,p_v$（Pa）为相化学势与压力；$F$ 的下标 $n,q$ 表示固定其他坐标时对蒸气质量／体积的偏导。液相质量与体积变化等于相应汽相变化的负值。因此 $F_n=g_v-g_l$（J/kg），$F_q=p_l-p_v+2\gamma_i/b$（Pa）。采用的曲面平衡根处两者均为零。

**式 (E31) 前的符号：**$F$ 为内部 Helmholtz 能（J）；下标 $n,q$ 表示对蒸气质量 $n$（kg）与体积 $q$（m³）的偏导，保持其他坐标不变。$T$ 为固定温度（K）。$p_l,p_v$ 为相压力（Pa）；$\rho_l,\rho_v$ 为相密度（kg/m³）；$V_l=V-q$ 为液体体积（m³）。$K_l=(\partial p_l/\partial\rho_l)_T$、$K_v=(\partial p_v/\partial\rho_v)_T$ 为正压力－密度斜率（Pa m³/kg）。$\kappa_l=K_l/V_l$、$\kappa_v=K_v/q$ 为缩放斜率（Pa/kg）。$\gamma_i$ 为内张力（N/m）；$b$ 为核半径（m）；$\pi$ 为圆周率。定温时 $dg=dp/\rho$。密度导数为 $\partial_n\rho_l=-1/V_l$、$\partial_n\rho_v=1/q$、$\partial_q\rho_l=\rho_l/V_l$、$\partial_q\rho_v=-\rho_v/q$。质量导数单位 m^-3；体积导数单位 kg/m^6。

$$
\begin{aligned}
F_{nn}&=\frac{\kappa_l}{\rho_l}+\frac{\kappa_v}{\rho_v},
&F_{nq}&=-(\kappa_l+\kappa_v),\\
F_{qq}&=\rho_l\kappa_l+\rho_v\kappa_v-\frac{\gamma_i}{2\pi b^4},
&\frac{d(2\gamma_i/b)}{dq}&=-\frac{2\gamma_i}{b^2}\frac{1}{4\pi b^2}.
\tag{E31}
\end{aligned}
$$

表面导数使用 $dq/db=4\pi b^2$。正压力－密度斜率给出 $F_{nn}>0$。质量曲率单位 J/kg²，混合曲率单位 Pa/kg，体积曲率单位 Pa/m³。对称 Hessian 在质量曲率为正时，其正定性要求 Schur 补为正。**式 (E32) 前的符号：**$H_{core}$ 为该补（Pa/m³）；$F_{qq},F_{nq},F_{nn}$ 为体积、混合与质量曲率（Pa/m³、Pa/kg、J/kg²）。$\kappa_l,\kappa_v$ 为正缩放压力－密度斜率（Pa/kg）；$\rho_l,\rho_v$ 为相密度（kg/m³）；$\gamma_i$ 为内张力（N/m）；$b$ 为正核半径（m）；$\pi$ 为无量纲圆周率。检验保持温度、总体积和总质量不变。

$$
\begin{aligned}
H_{core}&=F_{qq}-\frac{F_{nq}^2}{F_{nn}}\\
&=\rho_l\kappa_l+\rho_v\kappa_v
-\frac{\rho_l\rho_v(\kappa_l+\kappa_v)^2}{\kappa_l\rho_v+\kappa_v\rho_l}
-\frac{\gamma_i}{2\pi b^4}\\
&=\frac{\kappa_l\kappa_v(\rho_l-\rho_v)^2}
{\kappa_l\rho_v+\kappa_v\rho_l}-\frac{\gamma_i}{2\pi b^4}. \tag{E32}
\end{aligned}
$$

体积项使用正公分母。$\kappa_l$ 和 $\kappa_v$ 的平方项与混合曲率中的对应项相消。分子化为 $\kappa_l\kappa_v(\rho_l^2-2\rho_l\rho_v+\rho_v^2)$。体积压缩性稳定该体积变化；毛细作用使其不稳定。132 个根的质量曲率及 Schur 补均为正。最小体积／毛细比为 20.4526。这确立固定 $(T,V,m)$ 的局部内部极小值。全局可达性、成核概率、形状稳定性与有限深度动力学**尚未确立**。

## 4. 审查与未解决环节

审查检验局部符号、单位、代数、分支与引用。自动计算重建凝胶能量及动能功率导数、相质量、牵引、化学平衡与种子能量。比较独立波形与熵漂移。稳定性与求根成功分开检验。这些检验验证指定方程及其实现。

**未解决：**光学热分布；亚稳与异质成核概率；温度梯度及相变速率；液壳惯性；目标高速流变与断裂；表面几何及裂纹充液；水蒸气和不凝气体；非球形塌缩、破碎及冲击压力。[实施计划](IMPLEMENTATION_HANDOFF.md)列出所需测量。完整目标机制验证**尚未确立**。
