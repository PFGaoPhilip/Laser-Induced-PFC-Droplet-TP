# 两个最简的单次激光诱导空化模型

## 问题、系统构型与适用范围

模型 A 计算源压力和首次排液的出口速率。输入为给定源功、气体体积和液体存量。它同时推导相应能量上限。模型 B 加入水凝胶顺应性与损耗，计算凝胶载荷和剩余排出量。

初始球形腔室内含气体和载液。已有液体出口将腔室连向外部。初始连通的腔室液体决定有限排出量。通道有效惯性另行指定。模型 A 固定腔壁。模型 B 在腔壁外设置完整、不排水的球形水凝胶。气体膨胀使腔室增大，或将液体经出口排出。密封对照将出口运动设为零。该结构描述膨胀驱动的外部排液。塌缩射流和凝胶穿透需要不同模型。

**单次 10 ns 光脉冲**以激活后的初始数据表示。零时刻位于激活和压力均衡之后。模型省略光热、成核和能量转换，没有周期载荷。首次向外排液持续至速率回零。液体耗尽或有效性筛查触发时提前停止。密封对照在腔壁首次转向时停止。速度最大值在这些过程中计算。后续塌缩和回弹不在范围内。

时间从激活后的初态开始。出口速度向外为正。排液坐标等于排出体积除以出口面积。径向正方向从腔室中心指向凝胶。腔壁速度为正表示膨胀。环境绝对压力恒定。初始腔壁相对环境无应力，全部机械速度为零。腔室压力均匀。忽略气团形状及内部气液表面张力。外部弯月面提供毛细阻力。远场径向应力趋于负环境压力，位移衰减。出口处为环境压力，并附加给定弯月面压力。开放算例要求已有通道。密封算例排液量为零。

**本构假设。** 源为封闭绝热理想气体，指数恒定。该对照不采用 PFC 蒸气状态方程。液体和不排水凝胶密度恒定。液柱具有固定有效惯性和有限排出量。凝胶采用不可压缩新胡克弹性及 Kelvin–Voigt 黏性。出口可添加线性及二次损耗。出口聚焦、自由表面形状、断裂、相交换和扩散尚未解决。球形凝胶定律近似带小出口的腔室。平面层力学需要单独模型。材料预测需要校准。

基础为第一定律、体积守恒和非定常伯努利方程。再加入给定源状态方程及球形凝胶本构模型。[课程](https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/)说明机制与有限能量预算。第 1–3 章及附录 A 提供这些模型模块。[Brennen，第 2 章](https://media.library.caltech.edu/CaltechBOOK:1995.001/chap2.htm)讨论球形动量及多方过程假设。气体体积耦合、有限行程规则和诊断量在此推导。

## 符号表与约定

所有长度以 m 表示，时间以 s 表示，质量以 kg 表示，压力以 Pa 表示，能量以 J 表示，力以 N 表示。下标 `0` 和 `ref` 分别表示初始状态与无应力状态；`g`、`j`、`el`、`cap`、`dis` 和 `obs` 分别表示气体、排出射流、弹性、毛细、耗散和观测量。标量上的上标表示幂。上方一点表示对时间求导。积分针对所显示的实变量或表面进行。绝对值表示标量的大小。上方尖帽表示下文定义的归一化状态。常数 pi 无量纲。算术运算采用通常的实数意义。任何标量都不用于两个不同的角色。

| 符号 | 含义与限制 | 单位 |
|---|---|---|
| $t$ | 从初始化的激活后状态起算的时间 | s |
| $x,U$ | 排出体积除以出口面积，以及出口速度 | m, m/s |
| $R,W$ | 腔室半径和腔壁速度；$W=\dot R$ | m, m/s |
| $R_{\mathrm{ref}},R_{g0}$ | 无应力腔室半径和初始气体团半径 | m |
| $a,L,L_b,A$ | 出口半径、有效流体惯性长度、可排出体积对应的长度，以及面积 | m, m, m, m² |
| $V_g,V_{g0},V_{c0},V_{\mathrm{eq}}$ | 当前气体、初始气体、初始腔室，以及与环境平衡时的气体体积 | m³ |
| $p_b,p_0,p_\infty$ | 当前绝对源压力、初始绝对源压力，以及绝对环境压力 | Pa |
| $\kappa$ | 恒定的绝热理想气体指数，严格大于一 | 无量纲 |
| $\mathcal U_g,E_0$ | 气体内能，以及相对于环境的可用绝热膨胀功 | J |
| $\rho,\rho_g,m_c$ | 载液密度、不排水凝胶密度，以及液柱的有效惯性质量 | kg/m³, kg/m³, kg |
| $\sigma,p_{\mathrm{cap}},E_{\mathrm{cap}}$ | 有效表面张力、弯月面阻力，以及可逆的弯月面功 | N/m, Pa, J |
| $\mathcal R,K_o,p_{\mathrm{loss}}$ | 经拟合的出口线性阻力、无量纲二次损失系数，以及出口耗散压降 | Pa s/m, 无量纲, Pa |
| $b_o$ | 出口标志：开放通道为一，密封为零 | 无量纲 |
| $G,\eta_g$ | 正的凝胶剪切模量和非负的有效网络黏度 | Pa, Pa s |
| $r,s,\xi$ | 当前凝胶径向坐标、参考径向坐标，以及功积分中的半径哑变量 | m |
| $\lambda_r,\lambda_t,\beta$ | 径向伸长比、两个相等的切向伸长比之一，以及换元比值 $s/r$ | 无量纲 |
| $T_{rr},T_{tt},\chi$ | 径向/切向弹性柯西应力，以及不可压缩性乘子 | Pa |
| $p_{\mathrm{el}},p_{\mathrm{res}}$ | 弹性腔壁阻力，以及弹性与黏性合计的腔壁阻力 | Pa |
| $K_c,K_g,W_g,D,E_j$ | 液柱动能、凝胶动能、弹性功、不可逆损失，以及排出动能 | J |
| $P_{\mathrm{port}},P_{\mathrm{gel}}$ | 出口与凝胶的不可逆耗散功率 | W |
| $F_{\mathrm{hem}}$ | 一个腔室半球上弹性阻力的轴向合力 | N |
| $\theta,d\Omega$ | 相对于出口轴线的极角，以及立体角微元 | 无量纲 |
| $U_s,\tau,I_s$ | 速度、时间和排出冲量的归一化尺度 | m/s, s, N s |
| $\widehat x,\widehat U,\widehat R,\widehat W,\widehat D,\widehat E_j,\widehat I_j$ | 七个归一化运动与记账状态 | 无量纲 |
| $\varepsilon_E$ | 能量残差除以可用功 | 无量纲 |
| $U_{\mathrm{rms}},q_j,I_j,m_j$ | 排出液体的均方根速度、出口动压尺度、排出冲量，以及排出质量 | m/s, Pa, N s, kg |
| $A_{\mathrm{obs}},\tau_{\mathrm{obs}},\bar p_{\mathrm{arrest}}$ | 预先声明的观测面积、平均时间区间，以及平均制动压力上界 | m², s, Pa |
| $T_U,T_E,T_I,T_q$ | 匹配算例的峰值速度、排出动能、排出冲量，以及峰值动压之比 | 无量纲 |
| $c_L,L_{\mathrm{comm}},\mathcal C_p,M_j,M_w$ | 参考压力均衡传播速度、路径长度、均衡传播比，以及液体/腔壁马赫数诊断量 | m/s, m, 无量纲 |

| $z,z_i,z_o$ | 流线坐标以及入口/出口位置 | m |
| $u(z,t),f(z),\mathcal A(z)$ | 局部速度、固定的面积比剖面，以及局部横截面积 | m/s, 无量纲, m² |
| $\mathcal F(V_g)$ | 气体内能加上对环境做功，并以初始体积为参考 | J |

## 步骤 1 — 守恒体积并声明有限源

**式 (E01) — 几何恒等式。**

**式 (E01) 之前的符号定义：** $A$ 为出口面积（m²）；$a$ 为出口半径（m）；$V_{g0},V_{c0},V_g$ 分别为初始气体、初始腔室和当前气体体积（m³）；$R_{g0},R_{\mathrm{ref}},R$ 分别为初始气体、参考腔室和当前腔室半径（m）；$x$ 为排出体积除以面积（m）；$L_b$ 为可排出体积对应的长度（m）；pi 无量纲。

$$
\begin{aligned}
A&=\pi a^2,\qquad V_{g0}=\frac{4\pi R_{g0}^3}{3},\qquad V_{c0}=\frac{4\pi R_{\mathrm{ref}}^3}{3},\\
V_g&=V_{g0}+Ax+\frac{4\pi}{3}(R^3-R_{\mathrm{ref}}^3),\qquad L_b=(V_{c0}-V_{g0})/A.
\end{aligned}
$$

第二行守恒腔室液体体积。气体增加量等于排液体积与腔室扩张体积之和。模型 A 将腔室扩张量设为零。有限液体排出量耗尽时停止。

**式 (E02) — 初始数据与允许的向外行程。**

**式 (E02) 之前的符号定义：** $x,R$ 为长度（m）；$U,W$ 分别为液体和腔壁速度（m/s）；$R_{\mathrm{ref}},L_b$ 为正的参考半径和可排出体积对应的长度（m）；$A$ 为面积（m²）；$V_{c0},V_{g0}$ 为初始体积（m³）；自变量取零表示初始化。

$$
x(0)=0,\quad U(0)=0,\quad R(0)=R_{\mathrm{ref}},\quad W(0)=0,
\qquad 0\le x\le L_b,\qquad Ax<V_{c0}-V_{g0}.
$$

零初始速度是给定的激活后输入。成核不在范围内。有限行程约束排出质量。

**式 (E03) — 所采用的理想气体能量与绝热第一定律。**

**式 (E03) 之前的符号定义：** $\mathcal U_g$ 为内能（J）；$p_b$ 为绝对源压力（Pa）；$V_g$ 为气体体积（m³）；$\kappa>1$ 为恒定的理想气体指数；$d$ 表示沿封闭绝热源轨迹的微分。

$$
\mathcal U_g=\frac{p_bV_g}{\kappa-1},\qquad
d\mathcal U_g=-p_b\,dV_g,\qquad
V_g\,dp_b+p_b\,dV_g=-(\kappa-1)p_b\,dV_g.
$$

第一式定义源本构模型。第二式应用绝热第一定律。初始化后无热量及质量交换。对第一式求微分，再乘以指数减一，得到第三式。凝结及后续 PFC 蒸气生成不在范围内。

**式 (E04) — 积分压力定律。**

**式 (E04) 之前的符号定义：** $p_b,p_0$ 为正的当前和初始绝对压力（Pa）；$V_g,V_{g0}$ 为正的当前和初始体积（m³）；$\kappa>1$ 无量纲；$\ln$ 是无量纲比值的对数；$d$ 为沿轨迹的微分。

$$
\begin{aligned}
V_g\,dp_b&=-\kappa p_b\,dV_g,\\
\frac{dp_b}{p_b}&=-\kappa\frac{dV_g}{V_g},\\
\ln\frac{p_b}{p_0}&=-\kappa\ln\frac{V_g}{V_{g0}},\\
p_b&=p_0\left(\frac{V_{g0}}{V_g}\right)^\kappa.
\end{aligned}
$$

整理式 (E03) 的微分项。除以正压力和正体积。从初态积分以确定常数。取指数得到压力定律。膨胀降低压力。没有给定周期源。

## 步骤 2 — 计算有限功预算

**式 (E05) — 环境平衡与可用膨胀功。**

**式 (E05) 之前的符号定义：** $V_{\mathrm{eq}},V_{g0}$ 为气体体积（m³）；$p_0>p_\infty>0$ 分别为初始源与环境的绝对压力（Pa）；$\kappa>1$ 无量纲；$E_0$ 为可用绝热膨胀功（J）；$v$ 为正的气体体积哑变量（m³）；积分沿预先声明的压力—体积路径进行。

$$
\begin{aligned}
p_\infty&=p_0(V_{g0}/V_{\mathrm{eq}})^\kappa
\quad\Longrightarrow\quad V_{\mathrm{eq}}=V_{g0}(p_0/p_\infty)^{1/\kappa},\\
E_0&=\int_{V_{g0}}^{V_{\mathrm{eq}}}
\left[p_0\left(\frac{V_{g0}}v\right)^\kappa-p_\infty\right]dv\\
&=p_0V_{g0}^\kappa\left[\frac{v^{1-\kappa}}{1-\kappa}\right]_{V_{g0}}^{V_{\mathrm{eq}}}
-p_\infty(V_{\mathrm{eq}}-V_{g0})\\
&=\frac{p_0V_{g0}}{\kappa-1}
\left[1-\left(\frac{V_{g0}}{V_{\mathrm{eq}}}\right)^{\kappa-1}\right]
-p_\infty(V_{\mathrm{eq}}-V_{g0}).
\end{aligned}
$$

在环境压力下应用式 (E04)。取正根得到平衡体积。积分超压定义可用功。对体积幂积分；其指数不等于一。代入两端点，再提出初始体积。压力乘体积的单位为 J。数值反演此单调关系，得到初始压力。改变功预算即改变初态，后续无功输入。

可用功指**激活后的机械可用能**。入射光能另行定义。用测得的压力—体积路径确定可用功；或结合吸收能量及有依据的转换、相态模型。源质量和相组成必须支持给定初态。转换效率与 PFC 状态方程仍未指定。


**式 (E05a) — 有限可用功反演的唯一性。**

**式 (E05a) 之前的符号定义：** $E_0$ 为可用功（J）；$p_0>p_\infty$ 分别为初始和环境压力（Pa）；$V_{g0},V_{\mathrm{eq}},v$ 分别为初始、平衡和哑变量气体体积（m³）；$\kappa>1$ 无量纲；$\partial/\partial p_0$ 表示保持初始体积、环境压力和指数不变的偏导数；$\lim$ 表示所指定的压力极限。

$$
\begin{aligned}
\frac{\partial E_0}{\partial p_0}
&=\int_{V_{g0}}^{V_{\mathrm{eq}}}(V_{g0}/v)^\kappa dv
+[p_0(V_{g0}/V_{\mathrm{eq}})^\kappa-p_\infty]\frac{\partial V_{\mathrm{eq}}}{\partial p_0}\\
&=\frac{V_{g0}}{\kappa-1}[1-(V_{g0}/V_{\mathrm{eq}})^{\kappa-1}]>0,\\
E_0\big|_{p_0=p_\infty}&=0,\qquad \lim_{p_0\to\infty}\frac{E_0}{p_0}=\frac{V_{g0}}{\kappa-1}.
\end{aligned}
$$

第一行应用莱布尼茨求导。端点压力等于环境压力，故端点项为零。积分剩余正幂函数，得到第二行。源压等于环境压力时，可用功为零。高源压下，平衡体积项以次线性增长，得到最后极限。因此，正可用功唯一确定初始压力。

## 步骤 3 — 加速出口流动并保留实际排出输出

**式 (E06) — 惯性、毛细阻力与出口损失。**

**式 (E06) 之前的符号定义：** $m_c$ 为液柱有效惯性质量（kg）；$\rho$ 为载液密度（kg/m³）；$A$ 为出口面积（m²）；$L,a$ 分别为流体惯性长度和出口半径（m）；$p_{\mathrm{cap}},p_{\mathrm{loss}}$ 为压力（Pa）；$\sigma$ 为表面张力（N/m）；$\mathcal R\ge0$ 为经拟合的阻力（Pa s/m）；$K_o\ge0$ 无量纲；$U$ 为出口速度（m/s）；绝对值表示大小。

$$
m_c=\rho AL,\qquad p_{\mathrm{cap}}=2\sigma/a,\qquad
p_{\mathrm{loss}}=\mathcal R U+\rho K_oU|U|/2.
$$

液柱惯性和排出质量分别定义。弯月面假定为接触线固定的半球。不同曲率需要不同入口压力。线性阻力应测量或拟合。短时过程采用稳态泊肃叶阻力需要依据。关于速度为奇函数的压降在两个方向均耗散能量。

本过程的弯月面压力恒定。其积分为克服恒定保守载荷的功。模型不计算演化的自由表面能。射流形成时持续保持半球曲率尚未建立。曲率变化、接触线运动或破碎需要修改入口模型。

**式 (E06a) — 推导流体惯性与流出的动能压头。**

**式 (E06a) 之前的符号定义：** $z,z_i,z_o$ 分别为流线坐标和入口/出口位置（m）；$u(z,t)$ 为局部速度，$U(t)$ 为出口速度（m/s）；$f(z)$ 为固定的无量纲剖面；$A,\mathcal A(z)$ 分别为出口和局部面积（m²）；$L$ 为流体惯性长度（m）；$\rho$ 为密度（kg/m³）；$p(z,t)$ 为压力（Pa）；$t$ 为时间（s）；$\partial_t,\partial_z$ 为固定位置的偏导数；上方一点表示时间导数。大储液腔近似将入口速度设为零，将出口剖面值设为一。

$$
\begin{aligned}
u(z,t)&=f(z)U(t),\quad f(z)=A/\mathcal A(z),\quad L=\int_{z_i}^{z_o}f(z)dz,\\
\rho(\partial_tu+u\partial_zu)&=-\partial_zp,\\
\int_{z_i}^{z_o}(\partial_tu+u\partial_zu)dz
&=L\dot U+[u^2/2]_{z_i}^{z_o}=L\dot U+U^2/2,\\
\frac12\rho\int_{z_i}^{z_o}\mathcal A(z)u^2dz
&=\frac12\rho AU^2\int_{z_i}^{z_o}f(z)dz=\frac12\rho ALU^2.
\end{aligned}
$$

固定几何连续性给出第一行速度分布。第二行应用无黏流线欧拉动量方程。积分固定分布得到惯性。积分对流项得到端点动能压头。忽略储液腔入口速度，保留出口压头。在能量积分中代入连续性面积关系，得到相同惯性长度。该近似描述已有通道。自由表面聚焦和横向动能不在范围内。有效惯性与损耗应针对真实几何校准。

**式 (E07) — 非定常伯努利方程与显式出口标志。**

**式 (E07) 之前的符号定义：** $x$ 为排出体积除以出口面积（m）；$U$ 为向外的出口速度（m/s）；上方一点表示时间导数；$b_o$ 为开放/密封标志；$\rho$ 为密度（kg/m³）；$L$ 为流体惯性长度（m）；$p_b,p_\infty,p_{\mathrm{cap}},p_{\mathrm{loss}}$ 分别为源、环境、弯月面和耗散压力（Pa）。

$$
\begin{aligned}
p_b-p_\infty-p_{\mathrm{cap}}-p_{\mathrm{loss}}&=\rho L\dot U+\rho U^2/2\quad(b_o=1),\\
\dot x&=b_oU,\qquad
\dot U=\frac{b_o}{\rho L}(p_b-p_\infty-p_{\mathrm{cap}}-p_{\mathrm{loss}}-\rho U^2/2).
\end{aligned}
$$

积分式 (E06a) 的压力梯度。加入给定弯月面压降与耗散压降。除以正密度和正惯性长度，得到出口加速度。密封出口保持零初始速度。动能压头项计入离开出口的能量。

**式 (E08) — 液柱储能与耗散功率。**

**式 (E08) 之前的符号定义：** $K_c,E_{\mathrm{cap}}$ 为储存能量（J）；$m_c$ 为有效惯性质量（kg）；$U$ 为出口速度（m/s）；$p_{\mathrm{cap}},p_b,p_\infty$ 为压力（Pa）；$A$ 为面积（m²）；$x$ 为排出体积除以面积（m）；$P_{\mathrm{port}}$ 为耗散功率（W）；$\mathcal R$ 为阻力（Pa s/m）；$\rho$ 为密度（kg/m³）；$K_o,b_o$ 无量纲；$d/dt$ 为时间导数。

$$
\begin{aligned}
K_c&=m_cU^2/2,\qquad E_{\mathrm{cap}}=p_{\mathrm{cap}}Ax,\\
P_{\mathrm{port}}&=b_oA(\mathcal R U^2+\rho K_o|U|^3/2)\ge0,\\
\frac{d}{dt}(K_c+E_{\mathrm{cap}})&=b_oA(p_b-p_\infty)U-P_{\mathrm{port}}-b_o\rho AU^3/2.
\end{aligned}
$$

对储能求导并代入式 (E07)。加入弯月面功以抵消弯月面压力项。耗散压降乘体积流率给出耗散功率。最后的动能压头项给出排出功率。液柱储能与不可逆损失分别保留。

**式 (E08a) — 有限的排出质量、动能与冲量。**

**式 (E08a) 之前的符号定义：** $m_j$ 为排出质量（kg）；$E_j$ 为排出动能（J）；$I_j$ 为排出的轴向冲量（N s）；$\rho$ 为密度（kg/m³）；$A$ 为面积（m²）；$x$ 为排出体积除以面积（m）；$U$ 为非负的出口速度（m/s）；$b_o$ 为出口标志；上方一点表示时间导数，自变量取零表示初始化。

$$
m_j=\rho Ax,\quad \dot E_j=b_o\rho AU^3/2,\quad
\dot I_j=b_o\rho AU^2,\quad E_j(0)=I_j(0)=0.
$$

质量流率乘比动能，得到排出功率。质量流率乘轴向速度，得到排出冲量变化率。各变化率对时间积分。液柱能量与动量描述瞬时存储。排出能量与冲量描述已排出的量。

## 步骤 4 — 只保留约束所需的凝胶力学

**式 (E09) — 不可压缩球形映射与主伸长比。**

**式 (E09) 之前的符号定义：** $r,s,R,R_{\mathrm{ref}}$ 分别为当前材料半径、参考材料半径、当前腔壁半径和参考腔壁半径（m）；$\lambda_r,\lambda_t$ 为无量纲的径向和切向伸长比；$\partial r/\partial s$ 表示固定时间的微分；$r\ge R>0$ 且 $s\ge R_{\mathrm{ref}}>0$。

$$
\begin{aligned}
r^3-R^3&=s^3-R_{\mathrm{ref}}^3,\\
3r^2\frac{\partial r}{\partial s}&=3s^2,\\
\lambda_r&=\frac{s^2}{r^2},\qquad\lambda_t=\frac rs,\qquad
\lambda_r\lambda_t^2=1.
\end{aligned}
$$

令腔壁外参考体积与当前材料体积相等。对映射求导得到第二行。径向、切向长度比给出第三行。它们的乘积检查局部体积守恒。

**式 (E10) — 预先声明的新胡克应力与径向平衡。**

**式 (E10) 之前的符号定义：** $T_{rr},T_{tt},\chi$ 分别为径向/切向柯西应力和不可压缩性乘子（Pa）；$G$ 为剪切模量（Pa）；$\lambda_r,\lambda_t$ 为伸长比；$r,s$ 为材料半径（m）；$dT_{rr}/dr$ 为径向导数（Pa/m）。

$$
\begin{aligned}
T_{rr}&=-\chi+G\lambda_r^2,\qquad T_{tt}=-\chi+G\lambda_t^2,\\
T_{tt}-T_{rr}&=G[(r/s)^2-(s/r)^4],\\
\frac{dT_{rr}}{dr}&=\frac2r(T_{tt}-T_{rr}).
\end{aligned}
$$

第一行是采用的本构定律。应力相减以消去约束压力。第三行给出球形弹性平衡。积分得到弹性阻力。下文另行加入径向惯性和黏性。

**式 (E11) — 求取球形弹性阻力。**

**式 (E11) 之前的符号定义：** $p_{\mathrm{el}}$ 为弹性阻力压力（Pa）；$G$ 为剪切模量（Pa）；$R,R_{\mathrm{ref}},r,s$ 为半径（m）；$\beta=s/r$ 为正的无量纲积分变量；$d$ 表示微分；径向积分采用无限介质的应力边界条件。

$$
\begin{aligned}
p_{\mathrm{el}}&=2G\int_R^\infty[(r/s)^2-(s/r)^4]\frac{dr}{r},\\
\beta^3&=1-\frac{R^3-R_{\mathrm{ref}}^3}{r^3},\quad
\frac{dr}{r}=\frac{\beta^2\,d\beta}{1-\beta^3},\\
[(r/s)^2-(s/r)^4]\frac{dr}{r}
&=\frac{1-\beta^6}{1-\beta^3}\,d\beta=(1+\beta^3)d\beta,\\
p_{\mathrm{el}}&=2G\int_{R_{\mathrm{ref}}/R}^{1}(1+\beta^3)d\beta
=2G[\beta+\beta^4/4]_{R_{\mathrm{ref}}/R}^{1}\\
&=\frac G2\left[5-4\frac{R_{\mathrm{ref}}}{R}-\left(\frac{R_{\mathrm{ref}}}{R}\right)^4\right].
\end{aligned}
$$

积分式 (E10) 的应力差。在固定腔壁半径下对体积映射求微分。代入得到第三行。平方差因式分解，再约去公因子。壁面端点为参考半径除以当前半径。远场端点为一。积分多项式，再代入两端点。最后两行恢复附录 A 的式 (A-E05)，无需波场。

**式 (E12) — 积分可恢复的凝胶功。**

**式 (E12) 之前的符号定义：** $W_g$ 为弹性功（J）；$G$ 为剪切模量（Pa）；$R,R_{\mathrm{ref}},\xi$ 分别为当前腔壁、参考腔壁和哑变量腔壁半径（m）；$p_{\mathrm{el}}(\xi)$ 为式 (E11) 在哑变量半径处求得的压力（Pa）；pi 无量纲。

$$
\begin{aligned}
W_g&=4\pi\int_{R_{\mathrm{ref}}}^{R}p_{\mathrm{el}}(\xi)\xi^2d\xi\\
&=2\pi G\int_{R_{\mathrm{ref}}}^{R}
(5\xi^2-4R_{\mathrm{ref}}\xi-R_{\mathrm{ref}}^4\xi^{-2})d\xi\\
&=2\pi G\left[\frac{5\xi^3}{3}-2R_{\mathrm{ref}}\xi^2+\frac{R_{\mathrm{ref}}^4}{\xi}\right]_{R_{\mathrm{ref}}}^{R}\\
&=2\pi G\left[\frac{5R^3}{3}-2R_{\mathrm{ref}}R^2+\frac{R_{\mathrm{ref}}^4}{R}-\frac{2R_{\mathrm{ref}}^3}{3}\right].
\end{aligned}
$$

第一行积分球形体积变化对应的表面力功。代入式 (E11)，逐项积分各幂。计算两端点。下端点为参考半径立方的三分之二。模量乘体积的单位为 J。此能量为可恢复弹性储能。

**式 (E13) — 凝胶阻力检查。**

**式 (E13) 之前的符号定义：** $p_{\mathrm{el}}$ 为压力（Pa）；$W_g$ 为能量（J）；$G$ 为模量（Pa）；$R,R_{\mathrm{ref}},\delta R$ 为长度（m）；$d/dR$ 为对半径求导；$O$ 表示所指定小位移阶数的项；$\lim$ 为所声明的半径极限。

$$
\begin{aligned}
p_{\mathrm{el}}(R_{\mathrm{ref}})&=0,\qquad W_g(R_{\mathrm{ref}})=0,\\
\frac{dp_{\mathrm{el}}}{dR}&=2G\left(\frac{R_{\mathrm{ref}}}{R^2}+\frac{R_{\mathrm{ref}}^4}{R^5}\right)>0,\qquad
\frac{dW_g}{dR}=4\pi R^2p_{\mathrm{el}},\\
p_{\mathrm{el}}(R_{\mathrm{ref}}+\delta R)&=4G\frac{\delta R}{R_{\mathrm{ref}}}+O(G\delta R^2/R_{\mathrm{ref}}^2),\\
W_g(R_{\mathrm{ref}}+\delta R)&=8\pi G R_{\mathrm{ref}}\delta R^2+O(G\delta R^3),\qquad
\lim_{R/R_{\mathrm{ref}}\to\infty}p_{\mathrm{el}}=\frac52G.
\end{aligned}
$$

代入无应力半径以检查参考状态。对功求导以检查表面力。泰勒展开给出正小应变刚度与二次储能。半径比趋于无穷时，压力达到平台，功仍随体积增长。耐损伤能力和有效射流形成尚未建立。

## 步骤 5 — 加入径向惯性与黏性损耗

**式 (E14) — 球形径向动能与牛顿型凝胶损耗。**

**式 (E14) 之前的符号定义：** $K_g$ 为凝胶径向动能（J）；$\rho_g$ 为密度（kg/m³）；$R,W$ 分别为腔壁半径和速度（m, m/s）；$r$ 为空间半径（m）；$\eta_g$ 为网络黏度（Pa s）；$P_{\mathrm{gel}}$ 为不可逆功率（W）；$p_{\mathrm{res}},p_{\mathrm{el}}$ 为腔壁阻力压力（Pa）；pi 无量纲。

$$
\begin{aligned}
K_g&=\int_R^\infty\frac12\rho_g\left(\frac{R^2W}{r^2}\right)^2 4\pi r^2dr
=2\pi\rho_gR^4W^2\left[-\frac1r\right]_R^\infty
=2\pi\rho_gR^3W^2,\\
p_{\mathrm{res}}&=p_{\mathrm{el}}+\frac{4\eta_gW}{R},\qquad
P_{\mathrm{gel}}=16\pi\eta_gRW^2\ge0.
\end{aligned}
$$

体积映射给出径向速度。平方后得到收敛的径向平方反比积分。采用附录 Kelvin–Voigt 系数，见式 (A-E09)–(A-E12)。黏性阻碍腔壁双向运动，耗散功率非负。辐射与波场损耗不在范围内。

**式 (E15) — 径向运动及其能量恒等式。**

**式 (E15) 之前的符号定义：** $R,W$ 分别为腔壁半径和速度（m, m/s）；上方一点表示时间导数；$\rho_g$ 为密度（kg/m³）；$p_b,p_\infty,p_{\mathrm{el}}$ 为压力（Pa）；$\eta_g$ 为黏度（Pa s）；$K_g,W_g$ 为能量（J）；$P_{\mathrm{gel}}$ 为功率（W）；pi 无量纲。

$$
\begin{aligned}
\dot R&=W,\qquad
\rho_g\left(R\dot W+\frac32W^2\right)=p_b-p_\infty-p_{\mathrm{el}}-\frac{4\eta_gW}{R},\\
\frac{dK_g}{dt}&=2\pi\rho_g(3R^2W^3+2R^3W\dot W)
=4\pi R^2W\,\rho_g\left(R\dot W+\frac32W^2\right),\\
\frac{d}{dt}(K_g+W_g)&=4\pi R^2W(p_b-p_\infty)-P_{\mathrm{gel}}.
\end{aligned}
$$

第一行采用不排水球形动量平衡。初始弹性超压为零。对式 (E14) 的动能应用乘积求导。代入腔壁运动学关系，得到第二行。第一行乘体积变化率。代入式 (E13) 的弹性功及式 (E14) 的黏性功率，得到第三行。模型 A 固定半径，径向动能和弹性储能均为零。

**式 (E16) — 明确定义的约束力。**

**式 (E16) 之前的符号定义：** $F_{\mathrm{hem}}$ 为一个半球上的轴向力（N）；$p_{\mathrm{el}}$ 为均匀的球形弹性阻力（Pa）；$R$ 为半径（m）；$\theta$ 为从出口轴线量起的极角；pi 无量纲；积分将表面力投影到该轴线上。

$$
F_{\mathrm{hem}}=\int_0^{\pi/2}p_{\mathrm{el}}\cos\theta\,2\pi R^2\sin\theta\,d\theta
=2\pi R^2p_{\mathrm{el}}\left[\frac{\sin^2\theta}{2}\right]_0^{\pi/2}
=\pi R^2p_{\mathrm{el}}.
$$

此力是一半球上的方向合力。完整球面因对称性而合力为零。积分整球压力大小得到不同量。靶面区域需要单独指定面积与载荷路径。

## 步骤 6 — 闭合并审查耦合能量平衡

**式 (E17) — 源的总体积变化率与累积损失。**

**式 (E17) 之前的符号定义：** $V_g$ 为气体体积（m³）；$A$ 为面积（m²）；$U,W$ 为速度（m/s）；$R$ 为半径（m）；$b_o$ 为开放/密封标志；$D$ 为累积损失（J）；$P_{\mathrm{port}},P_{\mathrm{gel}}$ 为功率（W）；上方一点表示时间导数。

$$
\dot V_g=b_oAU+4\pi R^2W,\qquad
\dot D=P_{\mathrm{port}}+P_{\mathrm{gel}},\qquad D(0)=0.
$$

对式 (E01) 求导，代入两个运动学关系。出口与凝胶分别运动，其耗散功率相加。

**式 (E18) — 显式抵消源到接收端的功交换。**

**式 (E18) 之前的符号定义：** $\mathcal U_g,K_c,K_g,W_g,E_{\mathrm{cap}},D,E_j$ 为储存、损失和排出的能量（J）；$p_b,p_\infty$ 为压力（Pa）；$V_g$ 为气体体积（m³）；$A$ 为面积（m²）；$U,W$ 为速度（m/s）；$R$ 为半径（m）；$b_o$ 无量纲；$d/dt$ 为时间导数；pi 无量纲。

$$
\begin{aligned}
\frac{d}{dt}(\mathcal U_g+p_\infty V_g+K_c+K_g+W_g+E_{\mathrm{cap}}+D+E_j)
&=(-p_b+p_\infty)\dot V_g+(p_b-p_\infty)(b_oAU+4\pi R^2W)\\
&=0.
\end{aligned}
$$

结合式 (E03) 的源第一定律与式 (E08) 的液柱储能。加入式 (E15) 的径向储能及式 (E17) 的累计损失。各耗散功率与对应累计项抵消。排出动能功率与式 (E08a) 抵消。代入体积变化率，抵消剩余源交换项。此平衡由一个演化源压力闭合。另行指定独立半径历史会破坏闭合。

**式 (E19) — 数值验收残差。**

**式 (E19) 之前的符号定义：** $\varepsilon_E$ 为无量纲残差；$p_b,p_0,p_\infty$ 为压力（Pa）；$V_g,V_{g0}$ 为体积（m³）；$\kappa>1$ 无量纲；$K_c,K_g,W_g,E_{\mathrm{cap}},D,E_j,E_0$ 为储存、损失、排出和可用的能量（J），其中可用功严格为正。

$$
\varepsilon_E=
\frac{p_bV_g/(\kappa-1)-p_0V_{g0}/(\kappa-1)+p_\infty(V_g-V_{g0})+K_c+K_g+W_g+E_{\mathrm{cap}}+D+E_j}{E_0}.
$$

从式 (E18) 减去初始储能，再归一化。保留凝胶动能及弹性储能。接近零的残差检查数值守恒。状态方程与几何校准需要独立证据。

## 步骤 7 — 将方程映射到原生 COMSOL 状态

**式 (E20) — 归一化定义。**

**式 (E20) 之前的符号定义：** $U_s$ 为速度尺度（m/s）；$\tau$ 为时间尺度（s）；$I_s$ 为冲量尺度（N s）；$R_{\mathrm{ref}},L_b,R,x$ 为长度（m）；$U,W$ 为速度（m/s）；$m_c$ 为有效液柱质量（kg）；$D,E_j,E_0$ 分别为损失、排出动能和可用功（J）；$I_j$ 为排出冲量（N s）；七个带尖帽的状态是无量纲的归一化量。

$$
\begin{aligned}
\tau&=R_{\mathrm{ref}}/U_s,\qquad I_s=m_cU_s,\\
\widehat x&=x/L_b,\quad\widehat U=U/U_s,\quad\widehat R=R/R_{\mathrm{ref}},\quad\widehat W=W/U_s,\\
\widehat D&=D/E_0,\qquad\widehat E_j=E_j/E_0,\qquad\widehat I_j=I_j/I_s.
\end{aligned}
$$

归一化改变尺度，模型不变。原生状态为 `qq`、`vv`、`rr`、`ww`、`dd`、`ee`、`ii`。模型 A 省略两个径向状态，剩余五个标量。模型 B 使用七个。三个状态累积损失、排出能量及排出冲量。

**式 (E21) — 在物理时间中积分的无量纲残差。**

**式 (E21) 之前的符号定义：** 所有带尖帽的状态均无量纲；其上方一点表示对物理时间求导（1/s）；$\tau$ 为时间（s）；$b_o$ 为出口标志；$U,W,U_s$ 为速度（m/s）；$L,L_b,R,R_{\mathrm{ref}}$ 为长度（m）；$\rho,\rho_g$ 为密度（kg/m³）；$p_b,p_\infty,p_{\mathrm{cap}},p_{\mathrm{loss}},p_{\mathrm{el}}$ 为压力（Pa）；$\eta_g$ 为黏度（Pa s）；$P_{\mathrm{port}},P_{\mathrm{gel}}$ 为功率（W）；$E_0$ 为功（J）；$A$ 为面积（m²）；$I_s$ 为冲量尺度（N s）。

$$
\begin{aligned}
0&=\tau(\dot{\widehat x}-b_oU/L_b),\\
0&=\tau\left[\dot{\widehat U}-\frac{b_o(p_b-p_\infty-p_{\mathrm{cap}}-p_{\mathrm{loss}}-\rho U^2/2)}{\rho LU_s}\right],\\
0&=\tau(\dot{\widehat R}-W/R_{\mathrm{ref}}),\\
0&=\tau\left[\dot{\widehat W}-\frac{(p_b-p_\infty-p_{\mathrm{el}}-4\eta_gW/R)/\rho_g-3W^2/2}{RU_s}\right],\\
0&=\tau[\dot{\widehat D}-(P_{\mathrm{port}}+P_{\mathrm{gel}})/E_0],\\
0&=\tau(\dot{\widehat E_j}-b_o\rho AU^3/(2E_0)),\\
0&=\tau(\dot{\widehat I_j}-b_o\rho AU^2/I_s).
\end{aligned}
$$

将式 (E20) 代入运动及累计方程。速度导数与累计量分别除以对应尺度。每行乘时间尺度。全部残差无量纲。模型 A 固定腔壁，并省略径向两行。气体总体积决定代数源压力。

## 步骤 8 — 约束已定义的速度、排出输出与压力观测量

**式 (E22a) — 证明源机械势的最小值。**

**式 (E22a) 之前的符号定义：** $\mathcal F$ 为源内能加上对环境做功，并以初始体积为参考（J）；$\mathcal U_g$ 为内能（J）；$p_\infty,p_b$ 为正的压力（Pa）；$V_g,V_{g0},V_{\mathrm{eq}}$ 为体积（m³）；$\kappa>1$ 无量纲；$E_0$ 为可用功（J）；导数均针对正的气体体积。

$$
\mathcal F(V_g)=\mathcal U_g(V_g)+p_\infty(V_g-V_{g0}),\quad
\mathcal F'(V_g)=p_\infty-p_b,\quad
\mathcal F''(V_g)=\kappa p_b/V_g>0,\quad
\mathcal F(V_{g0})-\mathcal F(V_{\mathrm{eq}})=E_0.
$$

源第一定律给出一阶导数。对式 (E04) 求导得到二阶导数。严格凸性使环境压力状态成为唯一全局最小值。计算势差得到式 (E05)，建立采用模型中的功预算。

**式 (E22) — 区分出口速度与排出均方根速度的上限。**

**式 (E22) 之前的符号定义：** $K_c,E_j,E_0$ 分别为液柱动能、排出动能和可用功（J）；$m_c>0$ 为有效液柱惯性质量（kg）；$m_j>0$ 为实际排出质量（kg）；$U$ 为出口速度（m/s）；$U_{\mathrm{rms}}$ 为排出液体按质量加权的均方根速度（m/s）；$q_j$ 为出口动压尺度（Pa）；$\rho$ 为密度（kg/m³）；$A,L$ 分别为出口面积和流体惯性长度（m², m）；平方根取非负值。

$$
\begin{aligned}
K_c+E_j&\le E_0,\qquad |U|\le\sqrt{2E_0/m_c},\\
U_{\mathrm{rms}}&=\sqrt{2E_j/m_j}\le\sqrt{2E_0/m_j},\\
q_j&=\rho U^2/2\le E_0/(AL).
\end{aligned}
$$

向外分支中的各接收能量均非负。结合式 (E18) 与式 (E22a) 的最小值。分离液柱动能，再除以正有效质量，得到出口速率上限。排出能量与正排出质量定义均方根速率上限。代入式 (E06) 的液柱质量，得到动压上限。出口上限依赖有效惯性。排出均方根上限来自守恒和给定质量。液体耗尽可能使轨迹提前终止。

有限能量预算需要正的质量下界。缺少该下界时，无法计算普适均方根速率最大值。逐点压力最大值需要接触或压缩模型。缺少：面积、持续时间和载荷路径。源压力、出口动压和观测压力是不同量。

**式 (E23) — 有限排出冲量与平均制动压力上界。**

**式 (E23) 之前的符号定义：** $I_j$ 为排出冲量（N s）；$m_j$ 为排出质量（kg）；$m$ 为累积排出质量坐标的哑变量（kg）；$U(m)$ 为按排出质量重新参数化的同一出口速度历史（m/s）；$E_j,E_0$ 分别为排出动能与可用功（J）；$A_{\mathrm{obs}}$ 为正的观测面积（m²）；$\tau_{\mathrm{obs}}$ 为正的平均时间（s）；$\bar p_{\mathrm{arrest}}$ 为这些排出液体微团所贡献的平均正制动压力（Pa）。

$$
\begin{aligned}
I_j^2&=\left(\int_0^{m_j}U(m)dm\right)^2
\le\left(\int_0^{m_j}1dm\right)\left(\int_0^{m_j}U(m)^2dm\right)
=2m_jE_j\le2m_jE_0,\\
\bar p_{\mathrm{arrest}}&\le I_j/(A_{\mathrm{obs}}\tau_{\mathrm{obs}}).
\end{aligned}
$$

对可积有限速度历史应用柯西–施瓦茨不等式。两个积分分别为排出质量与排出能量的两倍。假定液体微团停止且不反向，也无额外驱动。接收冲量受入射冲量约束。除以指定面积和时长，得到平均压力。默认值为出口面积和一微秒。瞬时冲击压力未计算。传播与水锤不在范围内。

**式 (E24) — 匹配的单次过程传导指标。**

**式 (E24) 之前的符号定义：** $T_U,T_E,T_I,T_q$ 为无量纲比值；下标 $A,B$ 表示源状态、密度和出口几何相同的匹配刚性算例与水凝胶算例；$U_{A,\max},U_{B,\max}$ 为首次过程的出口速度最大值（m/s）；$E_{j,A},E_{j,B}$ 为各自过程终点时累积的排出动能（J）；$I_{j,A},I_{j,B}$ 为排出冲量（N s）；$q_{j,A,\max},q_{j,B,\max}$ 为首次过程的动压最大值（Pa）；刚性参考算例中的各个分母均为正。

$$
T_U=U_{B,\max}/U_{A,\max},\quad
T_E=E_{j,B}/E_{j,A},\quad T_I=I_{j,B}/I_{j,A},\quad
T_q=q_{j,B,\max}/q_{j,A,\max}=T_U^2.
$$

相同密度下，动压比等于速度比平方。排出能量和冲量需积分完整历史。峰值速度无法确定这些积分。各开放算例在速率回零、存量耗尽或筛查触发时停止。匹配算例终点因此可以不同。各比值比较单次激发的有限输出，区别于频域传递函数。密封通道的各排出比值均为零。

## 步骤 9 — 声明适用区间并检查压力均衡传播速率

**式 (E25) — 压力均衡传播与马赫数诊断。**

**式 (E25) 之前的符号定义：** $\mathcal C_p,M_j,M_w$ 为无量纲诊断量；$L_{\mathrm{comm}}$ 为压力均衡传播长度（m），模型 A 取流体惯性长度，模型 B 取流体惯性长度与腔室直径中的较大值；$c_L$ 为参考速度（m/s）；$p_b$ 为正的绝对压力（Pa）；$\dot p_b$ 为其时间导数（Pa/s）；$\kappa$ 无量纲；$V_g,\dot V_g$ 分别为体积及其变化率（m³, m³/s）；$U,W$ 为速度（m/s）；绝对值表示大小。

$$
\mathcal C_p=\frac{L_{\mathrm{comm}}}{c_L}\frac{|\dot p_b|}{p_b}
=\frac{L_{\mathrm{comm}}}{c_L}\frac{\kappa|\dot V_g|}{V_g},\qquad
M_j=\frac{|U|}{c_L},\qquad M_w=\frac{|W|}{c_L}.
$$

对式 (E04) 作对数微分，得到第二个传播表达式。比较压力变化与压力均衡传播时间。模型不求解传播场。开放基准的传播诊断量低于 0.1。该值为规定筛查限值，误差上界尚未验证。两个马赫诊断量也需低于 0.1。

不排水近似要求事件远短于溶剂排水时间。课程对示例 30 微米尺度估计排水时间为 1.5 s。此处事件持续微秒。实际渗透率及速率相关模量仍未测量。检查小出口几何、正液体存量及完整凝胶。检查有限行程结束前是否气体贯通。20% 伸长停止条件是规定的变形筛查。缺少实测断裂应变。

单独检查密封算例的传播比。能量守恒无法解决压力传播筛查失败。压力历史预测需要通过该筛查。

## 完成的模型能够确定什么

模型给出条件性的首次过程解和最大值。它们推导能量上限、球形凝胶阻力及可恢复功，并计算匹配有限输出比。普适空化最大值尚未建立。校准后的 PFC 极限及省略的 10 ns 激活压力尚未解决。塌缩射流最大值和完整凝胶穿透也尚未解决。

实验验证需要激活后的相体积与压力。实测压力—体积路径可给出源功。记录吸收脉冲能量与转换依据。指定运动液体质量、出口几何及通道状态。测量事件应变率下的凝胶模量和黏度。同次测量空腔体积、排出速度、质量与腔壁变形。声明比较位置及平均时间窗。比较源压力、动压和全部四个有限输出比。
