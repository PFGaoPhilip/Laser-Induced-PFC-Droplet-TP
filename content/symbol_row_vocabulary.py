"""Individual bilingual definitions used to expand the original grouped clauses.

Keys are scoped to the unit: identical letters in different physical problems
must not silently inherit another unit's meaning. Numerical local states and
conditions are retained from the equation-specific declaration.
"""
from symbol_glossaries import GLOSSARIES

VOCABULARY={n:{s:(en,zh,u) for s,en,zh,u,_,_ in rows} for n,rows in GLOSSARIES.items()}

def add(n, text):
    for line in text.strip().splitlines():
        symbol,en,zh,unit=line.split('|')
        VOCABULARY[n][symbol]=(en,zh,unit)

add(1,r'''
s|Dummy radial integration coordinate|径向积分哑坐标|m
\partial_r u|Radial strain rate|径向应变率|s⁻¹
\dot V_b|Cavity volume-change rate|空腔体积变化率|m³ s⁻¹
p_{v,\mathrm{PFC}}|PFC-vapor partial pressure|PFC 蒸气分压|Pa
p_{v,w}|Water-vapor partial pressure|水蒸气分压|Pa
p_g|Noncondensable-gas partial pressure|非凝结气体分压|Pa
D_{rr}|Radial strain-rate component|径向应变率分量|s⁻¹
D_{\theta\theta}|Polar tangential strain-rate component|极角切向应变率分量|s⁻¹
D_{\psi\psi}|Azimuthal tangential strain-rate component|方位角切向应变率分量|s⁻¹
\mathcal D_\mu|Total viscous dissipation rate|总黏性耗散率|W
y|Squared wall speed|壁面速度平方|m² s⁻²
y(R)|Squared wall speed on the monotonic radius branch|单调半径分支上的壁速平方|m² s⁻²
x|Dimensionless radius divided by the maximum radius|半径除以最大半径所得无量纲量|1
q|Dimensionless substitution variable equal to the cube of the radius fraction|等于半径比例立方的无量纲换元变量|1
a|Positive first argument of the beta function|贝塔函数的正第一参数|1
b|Positive second argument of the beta function|贝塔函数的正第二参数|1
dx|Dimensionless-radius integration measure|无量纲半径积分微元|1
dq|Dimensionless substitution integration measure|无量纲换元积分微元|1
dR|Radius integration measure|半径积分微元|m
C_t|Ideal-collapse time coefficient|理想塌缩时间系数|1
B(a,b)|Beta function at the specified positive arguments|指定正参数处的贝塔函数|1
B|Beta function defined in Eq. (C1-E17)|式（C1-E17）定义的贝塔函数|1
V_{\max}|Maximum cavity volume|最大空腔体积|m³
M_w|Wall Mach number|壁面马赫数|1
M_*|Selected diagnostic Mach value|选定的诊断马赫数值|1
x_M|Radius fraction at the selected Mach value|选定马赫数处的半径比例|1
R_M|Cavity radius at the selected Mach value|选定马赫数处的空腔半径|m
c|Carrier sound speed|载液声速|m s⁻¹
p_{\mathrm{ref}}|Spatially uniform reference pressure|空间均匀参考压力|Pa
t_0|Event start time|事件开始时刻|s
t_1|Event end time|事件结束时刻|s
\tau|Specified pressure-event duration|指定压力事件时长|s
\Delta\boldsymbol u|Fixed-position liquid velocity change|固定位置的液体速度变化|m s⁻¹
\nu|Kinematic viscosity|运动黏度|m² s⁻¹
U|Characteristic liquid speed|特征液体速度|m s⁻¹
L|Specified liquid length|指定液体长度|m
z|Axial position in the liquid column|液柱中的轴向位置|m
\Pi(z)|Local column pressure impulse|液柱局部压力冲量|Pa s
\Pi_0|Driven-end pressure impulse|驱动端压力冲量|Pa s
A_0|Pressure-impulse integration constant|压力冲量积分常数|Pa s
A_1|Pressure-impulse gradient integration constant|压力冲量梯度积分常数|Pa s m⁻¹
\Delta u_z|Positive axial liquid-speed change|正的液体轴向速度变化|m s⁻¹
\Delta p|Applied column pressure difference|施加于液柱的压差|Pa
t_a|Acoustic crossing time|声传播跨越时间|s
\gamma|Stand-off ratio|离壁比|1
h|Bubble-center-to-boundary distance|气泡中心到边界的距离|m
\boldsymbol e_r|Outward radial unit vector|向外径向单位矢量|1
\boldsymbol D|Symmetric liquid strain-rate tensor|对称液体应变率张量|s⁻¹
V_n|Interface normal speed|界面法向速度|m s⁻¹
\boldsymbol s|Unit tangent to the interface|界面的单位切向矢量|1
\boldsymbol X|Material interface position|物质界面位置|m
\phi_\Gamma|Velocity potential on the liquid–gas interface|液—气界面上的速度势|m² s⁻¹
\mathcal C_e|Pressure-communication ratio|压力传播比|1
L_e|Required pressure-communication distance|所需压力传播距离|m
\tau_e|Relevant event rise or change time|相关事件上升或变化时间|s
U_{\mathrm{column}}|Ideal straight-column speed increment|理想直液柱速度增量|m s⁻¹
''')

add(2,r'''
t|Time|时间|s
t^{\prime}|Dummy integration time|积分哑时间|s
dt|Time integration element|时间积分微元|s
r|Transverse distance from the laser-beam axis|到激光光束轴线的横向距离|m
F(r)|Local laser fluence|局部激光能量面密度|J m⁻²
F_0|On-axis laser fluence|轴上激光能量面密度|J m⁻²
w|Transverse Gaussian beam radius at the e⁻² level|横向高斯光束 e⁻² 半径|m
x|Dimensionless integration substitution|无量纲积分换元变量|1
f_{\mathrm{geo}}|Intercepted incident-energy fraction|截获的入射能量比例|1
b_a|Centered absorber-aperture radius|同轴吸收体窗口半径|m
f(t)|Normalized temporal pulse shape|归一化时间脉冲形状|s⁻¹
I(r,t)|Local instantaneous irradiance|局部瞬时辐照度|W m⁻²
I_{\mathrm{peak}}|On-axis peak irradiance|轴上峰值辐照度|W m⁻²
\tau_L|Rectangular laser-pulse duration|矩形激光脉冲时长|s
z|Depth inside the absorber|吸收体内部深度|m
I(z)|Irradiance inside the absorber|吸收体内部辐照度|W m⁻²
I_{\mathrm{in}}|Irradiance entering the absorber|进入吸收体的辐照度|W m⁻²
I^{\prime}|Dummy irradiance integration variable|辐照度积分哑变量|W m⁻²
z^{\prime}|Dummy depth integration coordinate|深度积分哑坐标|m
\mu_a|Optical absorption coefficient|光学吸收系数|m⁻¹
Q_{\mathrm{abs}}|Optical volumetric heat deposition|光学体积生热率|W m⁻³
h_a|Absorber thickness|吸收体厚度|m
\mathcal R_\lambda|Front-face reflected energy fraction at the selected wavelength|所选波长下的前表面反射能量比例|1
\lambda|Laser wavelength|激光波长|m
A_\lambda|Effective absorptance of incident light|相对于入射光的有效吸收率|1
\Omega_a|Absorbing volume or integration domain|吸收体体积或积分域|m³
dV|Volume integration element|体积积分微元|m³
\boldsymbol q|Conductive heat flux|传导热通量|W m⁻²
\boldsymbol u|Material velocity|物质速度|m s⁻¹
q_n|Signed normal conductive heat flux|带符号法向传导热通量|W m⁻²
\boldsymbol q_A|Conductive heat flux in material A|材料 A 中的传导热通量|W m⁻²
\boldsymbol q_B|Conductive heat flux in material B|材料 B 中的传导热通量|W m⁻²
\boldsymbol n_{AB}|Unit normal from material A into material B|从材料 A 指向材料 B 的单位法向|1
T_A|Temperature on contact side A|接触面 A 侧温度|K
T_B|Temperature on contact side B|接触面 B 侧温度|K
\mathcal R_T|Area-specific thermal contact resistance|单位面积热接触阻力|m² K W⁻¹
\Delta T|Characteristic temperature change|特征温度变化|K
L_h|Heating distance|加热距离|m
t_{\mathrm{th}}|Thermal diffusion-time estimate|热扩散时间估计|s
\tau_h|Available heating duration|可用加热时长|s
\delta_T|Thermal penetration-depth estimate|热渗透深度估计|m
\alpha_d|PFC-liquid thermal diffusivity|PFC 液体热扩散率|m² s⁻¹
p_d|Initial liquid-PFC core pressure|初始液态 PFC 核压力|Pa
p_c|Carrier-liquid pressure|载液压力|Pa
a|Liquid-PFC core radius|液态 PFC 核半径|m
\Pi_{\mathrm{shell}}|Shell-supported excess pressure|壳层支撑超压|Pa
p_{\mathrm{sat,PFP}}(T)|Bulk equilibrium PFP vapor pressure|体相平衡 PFP 蒸气压|Pa
p_{\mathrm{sat,w}}|Bulk equilibrium water vapor pressure|体相平衡水蒸气压|Pa
p_{\mathrm{sat,PFC}}(T_i)|Bulk PFC saturation pressure at the interface temperature|界面温度处的体相 PFC 饱和蒸气压|Pa
p_{\mathrm{sat,PFC}}(T_b)|Bulk PFC saturation pressure at the bubble temperature|气泡温度处的体相 PFC 饱和蒸气压|Pa
T_i|Local phase-interface temperature|局部相界面温度|K
T_b|Common bulk bubble temperature|共同体相气泡温度|K
\Delta p_n|Vapor-nucleation driving pressure difference|汽化成核驱动压差|Pa
W(r_n)|Vapor-nucleus formation free energy|汽核形成自由能|J
W|Vapor-nucleus formation free energy|汽核形成自由能|J
r_n|Vapor-nucleus radius|汽核半径|m
r_*|Positive critical nucleus radius|正的临界汽核半径|m
W_*|Critical-nucleus free-energy barrier|临界汽核自由能势垒|J
J(T,p)|Prescribed local nucleation-event rate per liquid volume|给定的单位液体体积局部成核事件速率|m⁻³ s⁻¹
p|Local or prescribed thermodynamic pressure as specified|按情景指定的局部或给定热力学压力|Pa
V_d(t)|Remaining liquid-PFC region and its volume|剩余液态 PFC 区域及其体积|m³
V_d(t^{\prime})|Remaining liquid-PFC region at the integration time|积分时刻的剩余液态 PFC 区域|m³
\Lambda(t)|Total nucleation-event rate|总成核事件速率|s⁻¹
S(t)|No-event survival probability|尚未发生事件的概率|1
P_{\mathrm{act}}|Activation probability|激活概率|1
m_{\mathrm{PFC},0}|Finite initial PFC mass|有限初始 PFC 质量|kg
\rho_d|Initial liquid-PFC density|初始液态 PFC 密度|kg m⁻³
m_{\mathrm{diss}}|Dissolved PFC mass|溶解 PFC 质量|kg
m_{\mathrm{esc}}|Cumulative escaped PFC mass|累计逸出 PFC 质量|kg
m_{v,s}|Vapor-domain mass of species s|组分 s 的蒸气域质量|kg
\dot m_{v,s}|Signed net mass-entry rate of species s|组分 s 的带符号净流入质量速率|kg s⁻¹
\Gamma_s|Interface in contact with species s|与组分 s 接触的界面|—
dA|Surface-area integration element|表面积积分微元|m²
\rho_l|Adjacent liquid density|邻接液体密度|kg m⁻³
\rho_v|Adjacent vapor density|邻接蒸气密度|kg m⁻³
\boldsymbol u_l|Adjacent liquid velocity|邻接液体速度|m s⁻¹
\boldsymbol u_v|Adjacent vapor velocity|邻接蒸气速度|m s⁻¹
\boldsymbol v_\Gamma|Phase-interface velocity|相界面速度|m s⁻¹
\boldsymbol n|Unit normal from liquid into vapor|从液体指向蒸气的单位法向|1
\boldsymbol e_r|Outward radial unit vector|向外径向单位向量|1
\dot R|Spherical interface radial velocity|球形界面径向速度|m s⁻¹
u_l(R)|Outward radial liquid velocity adjacent to the interface|邻接界面处向外的液体径向速度|m s⁻¹
h_{v,s}|Specific vapor enthalpy of species s at the actual boundary state|实际边界状态下组分 s 的蒸气比焓|J kg⁻¹
h_{l,s}|Specific liquid enthalpy of species s at the interface|界面处组分 s 的液体比焓|J kg⁻¹
\boldsymbol q_l|Liquid-side conductive heat flux|液体侧传导热通量|W m⁻²
\boldsymbol q_v|Vapor-side conductive heat flux|蒸气侧传导热通量|W m⁻²
\eta|Phase index selecting liquid or vapor|选择液体或蒸气的相指标|1
k_\eta|Thermal conductivity of the selected phase|所选相的导热系数|W m⁻¹ K⁻¹
T_\eta|Temperature of the selected phase|所选相的温度|K
\dot Q_b|Net conductive heat input, excluding transported mass enthalpy|不含随质量输运焓的净传导热输入|W
p_b|Uniform total absolute bubble pressure|均匀总绝对气泡压力|Pa
s|Species index|组分指标|1
N_s|Number of declared species|声明的组分数|1
e_s(T_b)|Species specific internal energy with a consistent reference|采用一致参考的组分比内能|J kg⁻¹
c_{v,s}|Species constant-volume specific heat|组分定容比热容|J kg⁻¹ K⁻¹
p_{v,s}|Partial pressure of species s|组分 s 的分压|Pa
\mathcal P|Adopted equation-of-state function|采用的状态方程函数|—
\rho_b|Bubble-mixture density|气泡混合物密度|kg m⁻³
e_b|Mixture specific internal energy|混合物比内能|J kg⁻¹
\boldsymbol Y|Species mass-fraction vector with entries summing to one|各分量之和为一的组分质量分数向量|1
m_{v,\mathrm{eq}}|Equilibrium-control PFC vapor mass|平衡参照中的 PFC 蒸气质量|kg
M_{\mathrm{PFC}}|PFC molar mass|PFC 摩尔质量|kg mol⁻¹
p_{v,\mathrm{PFC,eq}}|Ideal equilibrium PFC partial pressure|理想平衡 PFC 分压|Pa
p_{v,\mathrm{PFC}}|PFC vapor partial pressure|PFC 蒸气分压|Pa
Q_{\mathrm{sens}}|Estimated sensible preparation energy|估计的显热制备能量|J
Q_{\mathrm{lat}}|Estimated latent preparation energy|估计的潜热制备能量|J
Q_{\mathrm{prep}}|Estimated total preparation energy|估计的总制备能量|J
c_{p,d}|Constant liquid-PFC specific heat|恒定液态 PFC 比热容|J kg⁻¹ K⁻¹
T_*|Selected final reference temperature, not critical-nucleus temperature|选定的最终参照温度，并非临界汽核温度|K
T_0|Initial liquid temperature|初始液体温度|K
L_v|Declared latent enthalpy per mass|声明的单位质量潜焓|J kg⁻¹
Q_{\mathrm{iso}}|Heat required for the stated constant-pressure preparation path|所述恒压制备路径的需热|J
T_{\mathrm{sat}}|Liquid–vapor coexistence temperature at the prescribed pressure|给定压力下的液—汽共存温度|K
c_{p,l}|Temperature- and pressure-dependent liquid specific heat at constant pressure|依赖温度与压力的液体定压比热|J kg⁻¹ K⁻¹
c_{p,v}|Temperature- and pressure-dependent vapor specific heat at constant pressure|依赖温度与压力的蒸气定压比热|J kg⁻¹ K⁻¹
L_v(T_{\mathrm{sat}},p)|Specific latent enthalpy at liquid–vapor coexistence|液—汽共存状态的比潜焓|J kg⁻¹
R_{b,\mathrm{inv}}|Ideal inventory-state bubble radius|理想库存状态气泡半径|m
\eta_{\mathrm{th,min}}|Minimum heat-delivery fraction in the stated loss-excluding estimate|所述不含损失估计中的最低热输送比例|1
''')

add(3,r'''
U_j|Uniform jet speed|均匀射流速度|m s⁻¹
E_j|Jet kinetic energy|射流动能|J
p_a|Identical independent site-activation probability|相同且独立的位点激活概率|1
\mathbb E|Expectation operator|期望算子|—
\operatorname{Var}|Variance operator|方差算子|—
\Pr|Probability operator|概率算子|—
\mathrm{CV}|Standard deviation divided by the nonzero mean|标准差除以非零均值|1
F(r)|Gaussian pulse fluence at transverse distance r|横向距离 r 处的高斯脉冲能量面密度|J m⁻²
F_0|On-axis fluence|轴上能量面密度|J m⁻²
r|Transverse distance from the laser axis|到激光轴线的横向距离|m
R_A|Radius enclosing the illuminated array|围住受光阵列的半径|m
w|Gaussian beam radius at the e⁻² level|高斯光束 e⁻² 半径|m
\epsilon|Allowed fractional edge-fluence decrease|允许的边缘能量面密度相对降低量|1
R_j|Radius of source bubble j|源气泡 j 的半径|m
R_j(t)|Time-dependent radius of source bubble j|源气泡 j 的随时间变化半径|m
r_j|Radial distance from the center of source bubble j|到源气泡 j 中心的径向距离|m
\xi|Dummy radial integration coordinate|径向积分哑坐标|m
t|Time|时间|s
\dot R_j|Wall radial velocity of source bubble j|源气泡 j 的壁面径向速度|m s⁻¹
\ddot R_j|Wall radial acceleration of source bubble j|源气泡 j 的壁面径向加速度|m s⁻²
u_j|Radial liquid velocity associated with source j|与源 j 对应的液体径向速度|m s⁻¹
\phi_j|Velocity potential of source bubble j|源气泡 j 的速度势|m² s⁻¹
p'_{j\to i}|Pressure disturbance produced by source j at center i|源 j 在中心 i 处产生的压力扰动|Pa
p_{\mathrm{ext},i}|External pressure acting on bubble i|作用于气泡 i 的外部压力|Pa
p_\infty|Remote carrier pressure|远场载液压力|Pa
p_b|Uniform internal bubble pressure in the stated control|指定对照中的均匀气泡内部压力|Pa
p_{b,i}|Internal pressure of bubble i|气泡 i 的内部压力|Pa
B_i|Isolated radial driving expression|孤立气泡径向驱动表达式|m² s⁻²
N|Number of bubbles or jets in the stated control|指定对照中的气泡或射流数|1
k|Step index around the regular polygon|沿正多边形计数的步指标|1
d_k|Bubble-center separation across k polygon steps|相隔 k 个多边形步长的气泡中心距离|m
S_N|Reciprocal-distance sum for the N-site polygon|N 位点多边形的距离倒数和|m⁻¹
S|Fixed reciprocal-distance neighbor sum|固定的邻泡距离倒数和|m⁻¹
\varphi_g|Golden ratio|黄金比|1
\Delta p_c|Positive constant ideal-collapse pressure difference|正的恒定理想塌缩压差|Pa
R|Shared instantaneous bubble radius|共同瞬时气泡半径|m
R(t)|Shared time-dependent bubble radius|共同的随时间变化气泡半径|m
\dot R|Bubble-wall radial velocity|气泡壁面径向速度|m s⁻¹
\ddot R|Bubble-wall radial acceleration|气泡壁面径向加速度|m s⁻²
y(R)|Squared wall speed on the moving radius branch|运动半径分支上的壁速平方|m² s⁻²
y|Squared wall speed|壁面速度平方|m² s⁻²
y'|Derivative of squared wall speed with respect to radius|壁速平方对半径的导数|m s⁻²
\ell_*|Arbitrary constant reference length for the logarithm|用于对数的任意恒定参考长度|m
t_c|Formal ideal-control collapse time|理想对照中的形式塌缩时间|s
x|Dimensionless integration radius|无量纲积分半径|1
\chi|Dimensionless interaction strength|无量纲相互作用强度|1
C|Collapse-time coefficient as a function of interaction strength|相互作用强度的塌缩时间系数函数|1
C'|Derivative of that coefficient with respect to interaction strength|该系数对相互作用强度的导数|1
K_N|Leading-order liquid kinetic energy of the bubble cluster|气泡群的首阶液体动能|J
r_i|Radial distance from source center i|到源中心 i 的径向距离|m
R_{\max,N}|Per-bubble maximum radius under fixed total initial work|固定初始总做功下的单泡最大半径|m
R_*|Isolated-bubble reference radius|孤立气泡参考半径|m
b_i|Volume-source strength of bubble i|气泡 i 的体积源强度|m³ s⁻¹
b_j|Volume-source strength of bubble j|气泡 j 的体积源强度|m³ s⁻¹
\phi_i|Velocity potential of source bubble i|源气泡 i 的速度势|m² s⁻¹
\Omega|Liquid integration domain|液体积分域|—
\Gamma_j|Boundary of bubble j|气泡 j 的边界|—
dV|Volume integration element|体积积分微元|m³
dA|Area integration element|面积积分微元|m²
dr_i|Radial integration element from center i|以中心 i 为原点的径向积分微元|m
E_{B,\mathrm{tot}}|Fixed total initial pressure-work budget|固定初始总压力做功预算|J
\phi_b|Instantaneous bubble-volume fraction|瞬时气泡体积分数|1
V_i|Volume of bubble i|气泡 i 的体积|m³
V_\Omega|Representative-region volume|代表区域体积|m³
\dot V_i|First time derivative of bubble-i volume|气泡 i 体积的一阶时间导数|m³ s⁻¹
\ddot V_i|Second time derivative of bubble-i volume|气泡 i 体积的二阶时间导数|m³ s⁻²
\phi(\boldsymbol x,t)|Weak far-field velocity potential|弱扰动远场速度势|m² s⁻¹
p'|Pressure disturbance about the specified reference|相对于指定参考值的压力扰动|Pa
\boldsymbol x|Spatial observation position|空间观察位置|m
\boldsymbol u(\boldsymbol x,t)|Liquid velocity field|液体速度场|m s⁻¹
\Omega(t)|Moving liquid domain|运动液体域|—
\boldsymbol X|Material interface point|物质界面点|m
\boldsymbol V_w|Prescribed solid-wall velocity|给定固体壁面速度|m s⁻¹
\boldsymbol n|Unit normal outward from liquid toward gas or solid|从液体朝向气体或固体的外单位法向|1
V_n|Interface normal speed|界面法向速度|m s⁻¹
\phi_\Gamma|Interface velocity potential|界面速度势|m² s⁻¹
\Gamma|Complete moving liquid interface|完整运动液体界面|—
\Gamma_0|Prescribed initial interface geometry|给定初始界面几何|—
\phi_0|Prescribed initial velocity potential|给定初始速度势|m² s⁻¹
p_l|Interface-liquid pressure|界面液体压力|Pa
p_g|Adjacent gas pressure|邻接气体压力|Pa
\sigma|Surface tension of the specified interface|指定界面的表面张力|N m⁻¹
\kappa|Signed sum of interface principal curvatures|带符号的界面两主曲率之和|m⁻¹
a_j|Exterior cylindrical-jet radius|外部圆柱射流半径|m
\Pi(\boldsymbol x)|Local pressure impulse per unit area|局部单位面积压力冲量|Pa s
\Pi_0|Driven-end pressure impulse|驱动端压力冲量|Pa s
p|Local liquid pressure|局部液体压力|Pa
p_{\mathrm{ref}}|Specified reference pressure|指定参考压力|Pa
t_0|Pulse start time|脉冲开始时刻|s
\tau_p|Pressure-pulse duration|压力脉冲时长|s
\Delta\boldsymbol u|Fixed-position velocity increment|固定位置的速度增量|m s⁻¹
U|Uniform column speed increment|均匀液柱速度增量|m s⁻¹
z|Axial liquid-column or jet position|液柱或射流的轴向位置|m
L|Liquid-column length|液柱长度|m
A|Liquid-column cross-sectional area|液柱截面积|m²
m|Liquid-column mass|液柱质量|kg
\mathcal J|Total directional force impulse|总方向力冲量|N s
Q|Steady volume-flow rate|稳态体积流率|m³ s⁻¹
a_{\mathrm{in}}|Solid-tube inlet radius|固体管入口半径|m
U_{\mathrm{in}}|Uniform inlet speed|均匀入口速度|m s⁻¹
\alpha|Inlet-to-jet area ratio as defined by the equation|由公式定义的入口与射流面积比|1
p_{\mathrm{in}}|Tube-inlet pressure|管入口压力|Pa
\Delta p_{\mathrm{loss}}|Prescribed pressure loss|给定压力损失|Pa
A_j|Jet cross-sectional area|射流截面积|m²
\mathcal M_j|Collection of emitted material|喷出材料集合|—
dm|Emitted-mass integration element|喷出质量积分微元|kg
\boldsymbol e_z|Unit vector along the intended transfer direction|沿期望转印方向的单位矢量|1
P_j|Signed jet momentum along the transfer direction|沿转印方向的带符号射流动量|N s
E_{\mathrm{avail}}|Available mechanical-energy budget|可用力学能量预算|J
\Delta z|Fixed finite axial-slice length|固定有限轴向切片长度|m
d\xi|Integration-coordinate element|积分坐标微元|m
a(z,t)|Local jet radius|局部射流半径|m
A(z,t)|Local jet cross-sectional area|局部射流截面积|m²
v(z,t)|Cross-section-averaged axial velocity|截面平均轴向速度|m s⁻¹
u_r|Radial liquid velocity|液体径向速度|m s⁻¹
v|Axial liquid velocity|液体轴向速度|m s⁻¹
a|Jet radius|射流半径|m
\tau_{zz}|Axial viscous normal stress|轴向黏性法向应力|Pa
\tau_{rr}|Radial viscous normal stress|径向黏性法向应力|Pa
a_0|Base-cylinder radius|基态圆柱半径|m
\delta_0|Initial small radius-disturbance amplitude|初始微小半径扰动振幅|m
\delta(t)|Time-dependent small radius-disturbance amplitude|随时间变化的微小半径扰动振幅|m
\delta_{\mathrm{crit}}|Chosen small linear-response threshold amplitude|选定的微小线性响应阈值振幅|m
\delta_{\mathrm{arr}}|Disturbance amplitude at arrival|到达时的扰动振幅|m
\psi|Jet perturbation velocity potential|射流扰动速度势|m² s⁻¹
B|Amplitude of the perturbation velocity potential|扰动速度势的振幅|m² s⁻¹
g|Temporal growth rate of the jet disturbance, not gravity|射流扰动的时间增长率，并非重力加速度|s⁻¹
I_0|Modified Bessel function of order zero|零阶修正贝塞尔函数|1
I_1|Modified Bessel function of order one|一阶修正贝塞尔函数|1
q|Dimensionless axial wavenumber|无量纲轴向波数|1
t_\sigma|Capillary response-time scale|毛细响应时间尺度|s
t_{\mathrm{lin}}|Time to the selected small linear threshold|达到选定微小线性阈值的时间|s
t_{\mathrm{flight}}|Jet flight time|射流飞行时间|s
H|Liquid-jet flight gap|液体射流飞行间隙|m
g_{\max}|Fastest inviscid cylinder-disturbance growth rate|无黏圆柱扰动的最快增长率|s⁻¹
\lambda_{\max}|Wavelength of the fastest-growing disturbance|最快增长扰动的波长|m
\mathrm{Re}_j|Diameter-based jet Reynolds number|以直径定义的射流雷诺数|1
\mathrm{We}_j|Diameter-based jet Weber number|以直径定义的射流韦伯数|1
\mathrm{Oh}_j|Diameter-based jet Ohnesorge number|以直径定义的射流奥内佐格数|1
q_j|Jet dynamic-pressure scale|射流动压尺度|Pa
\dot m|Positive throughflow mass rate, not the derivative of finite emitted mass|正的通过质量流率，并非有限喷出质量的导数|kg s⁻¹
F_{\mathrm{steady}}|Receiver-normal steady force|接收体法向稳态力|N
u|Liquid normal velocity in the impact control|冲击对照中的液体法向速度|m s⁻¹
v_i|Common contact velocity|共同接触速度|m s⁻¹
p_{\mathrm{early}}|Early compressive contact pressure scale|早期压缩接触压力尺度|Pa
Z_l|Liquid longitudinal wave impedance|液体纵向波阻抗|Pa s m⁻¹
Z_r|Receiver longitudinal wave impedance|接收体纵向波阻抗|Pa s m⁻¹
\mathcal J_{\mathrm{rec}}|Normal contact impulse delivered to the receiver|传给接收体的法向接触冲量|N s
P_{\mathrm{in}}|Incoming axial liquid momentum|入射液体轴向动量|N s
P_{\mathrm{out}}|Outgoing axial liquid momentum|出射液体轴向动量|N s
\tau_{\mathrm{eq}}|Impulse-equivalent duration of the fictitious rigid-contact rectangle|假想刚性接触矩形载荷的冲量等效时长|s
t_{\mathrm{side}}|Side-release time|侧向释放时间|s
t_{\mathrm{axial}}|Axial-release time|轴向释放时间|s
t_{\mathrm{early}}|Early observation time|早期观察时间|s
t_{\mathrm{return}}|First receiver-return time|首个接收体回波时间|s
p_{\mathrm{obs}}|Signed finite-area/time mean excess pressure|带符号的有限面积／时间平均超压|Pa
A_o|Fixed observer area|固定观察面积|m²
\tau_o|Observer averaging duration|观察者平均时长|s
E_w|Outgoing one-way linear plane-wave energy|向外传播的单向线性平面波能量|J
\overline p|Signed area–time mean pressure disturbance|带符号的面积—时间平均压力扰动|Pa
\rho(\boldsymbol x,t)|Compressible density field|可压缩密度场|kg m⁻³
e|Specific internal energy|比内能|J kg⁻¹
e_t|Total specific energy|总比能|J kg⁻¹
\boldsymbol I|Identity tensor|单位张量|1
\boldsymbol\tau|Viscous stress tensor|黏性应力张量|Pa
\boldsymbol q|Conductive heat flux|传导热通量|W m⁻²
Q_{\mathrm{abs}}|Optical volumetric heating|光学体积生热率|W m⁻³
\mathcal P|Adopted equation-of-state function|采用的状态方程函数|—
Y_k|Mass fraction of species k|组分 k 的质量分数|1
E_L|Incident laser energy|入射激光能量|J
E_{\mathrm{abs,tot}}|Total absorbed optical energy|总吸收光能|J
E_{\mathrm{abs,site}}|Absorbed optical energy per site|单个位点吸收光能|J
E_{\mathrm{PFC,deadline}}|Energy delivered to the PFC inventory by the activation deadline|激活截止时刻前传给 PFC 储量的能量|J
E_{j,\mathrm{tot}}|Total jet kinetic energy|总射流动能|J
f_{\mathrm{geo}}|Intercepted incident-energy fraction|截获的入射能量比例|1
A_\lambda|Effective absorptance at the selected wavelength|所选波长下的有效吸收率|1
\lambda|Laser wavelength|激光波长|m
f_T|Stipulated thermal-delivery fraction|假设的热输送比例|1
\eta_j|Stipulated absorbed-to-jet kinetic-energy efficiency|假设的吸收能至射流动能效率|1
p_{\mathrm{rigid,early}}|Early rigid-contact pressure|早期刚性接触压力|Pa
P_{\mathrm{tot}}|Total aligned incoming jet momentum|总对齐入射射流动量|N s
''')

add(4,r'''
m_A|Film areal mass|薄膜面密度|kg m⁻²
\boldsymbol u(\boldsymbol x,t)|Liquid velocity field|液体速度场|m s⁻¹
\boldsymbol x|In-plane or spatial position as specified|按情景指定的面内或空间位置|m
t|Time|时间|s
dt|Time integration element|时间积分微元|s
\boldsymbol D_u|Liquid strain-rate tensor|液体应变率张量|s⁻¹
\boldsymbol T_l|Liquid Cauchy stress tensor|液体柯西应力张量|Pa
p|Liquid pressure|液体压力|Pa
\mu|Liquid dynamic viscosity|液体动力黏度|Pa s
\boldsymbol I|Identity tensor|单位张量|1
\boldsymbol n_f|Unit normal from the solid into the liquid|由固体指向液体的单位法向|1
\boldsymbol t_l|Liquid traction on the solid|液体作用于固体的牵引|Pa
A_f(t)|Loaded solid surface at time t|时刻 t 的受载固体表面|m²
dA|Area integration element|面积积分微元|m²
\boldsymbol F_l|Resultant applied liquid force|施加的液体合力|N
\boldsymbol I_l|Applied liquid force impulse|施加的液体力冲量|N s
\mathcal W_l|Work delivered by liquid to the solid|液体传给固体的功|J
\boldsymbol v_f|Local solid-surface velocity|局部固体表面速度|m s⁻¹
t_a|Load-event start time|载荷事件开始时刻|s
t_b|Load-event end time|载荷事件结束时刻|s
z|Thickness coordinate measured from the neutral midplane|从中性中面计量的厚度坐标|m
dz|Thickness integration element|厚度积分微元|m
\Omega_f|Reference film plane|参考薄膜平面|m²
\partial\Omega_f|Boundary of the reference film plane|参考薄膜平面的边界|—
w(x,y,t)|Transverse film displacement|薄膜横向位移|m
w(\boldsymbol x,t)|Film displacement in the positive departure direction|沿正离开方向的薄膜位移|m
w|Film or blister transverse displacement|薄膜或鼓泡的横向位移|m
\dot w|Film transverse velocity|薄膜横向速度|m s⁻¹
\ddot w|Film transverse acceleration|薄膜横向加速度|m s⁻²
x|First Cartesian in-plane coordinate|第一笛卡尔面内坐标|m
y|Second Cartesian in-plane coordinate|第二笛卡尔面内坐标|m
K_f|Film kinetic energy|薄膜动能|J
U_b|Plate bending energy, not bubble internal energy in this unit|板弯曲能，本单元不表示气泡内能|J
U_T|Stored pretension energy|预张力储能|J
U_f|Recoverable solid energy including recoverable interface energy|包含可恢复界面能的可恢复固体能量|J
d\ell|Boundary or crack-front arc-length element|边界或裂纹前沿弧长微元|m
\delta w|Admissible infinitesimal displacement variation|可容许的无穷小位移变分|m
\delta U_b|Bending-energy variation|弯曲能变分|J
\delta U_T|Pretension-energy variation|预张力能变分|J
\alpha|First Cartesian in-plane direction index|第一笛卡尔面内方向指标|1
\beta|Second Cartesian in-plane direction index|第二笛卡尔面内方向指标|1
w_{\alpha\beta}|Second spatial derivative of transverse displacement|横向位移的二阶空间导数|m⁻¹
B_{\alpha\beta}|Bending-energy tensor conjugate to curvature|与曲率共轭的弯曲能张量|N
\delta_{\alpha\beta}|Kronecker identity, distinct from a variation|克罗内克恒等符号，与变分不同|1
n_\alpha|Component of the outward in-plane unit normal|面内外单位法向的分量|1
n_\beta|Component of the outward in-plane unit normal|面内外单位法向的分量|1
T_0|Prescribed isotropic tensile force per edge length|给定的单位边长各向同性拉力|N m⁻¹
w_P|PVC displacement along the common positive direction|沿共同正方向的 PVC 位移|m
m_{A,P}|PVC areal mass|PVC 面密度|kg m⁻²
D_P|PVC bending stiffness|PVC 弯曲刚度|N m
T_P|Prescribed PVC pretension|给定 PVC 预张力|N m⁻¹
p_{\rm load}|Net applied transverse traction projected positively|投影到正方向的净施加横向牵引|Pa
t_{\rm coh}|Cohesive traction resisting film opening|阻碍薄膜张开的内聚牵引|Pa
p_{\rm liq}|Net liquid traction applied to PVC|液体施加于 PVC 的净牵引|Pa
t_{P\to f}|Transmitted PVC-to-film traction projected positively|投影到正方向的 PVC 至薄膜传递牵引|Pa
J_A|Local applied force impulse per unit area|局部单位面积施加力冲量|Pa s
\Delta\dot w|Film velocity change from rest|薄膜从静止开始的速度变化|m s⁻¹
\mathcal E_A|Resulting kinetic energy per area|所得单位面积动能|J m⁻²
t_b^{\rm scale}|Bending response-time estimate|弯曲响应时间估计|s
t_T^{\rm scale}|Pretension response-time estimate|预张力响应时间估计|s
t_n^{\rm scale}|Normal-cohesion response-time estimate|法向内聚响应时间估计|s
a_f|Lateral deformation length|横向变形长度|m
\mathcal P|Mechanical potential including the stated loading system|包含指定加载系统的力学势能|J
A_c|Crack or delaminated area|裂纹或脱层面积|m²
\mathcal C|Held loading-control label, not a material coefficient|固定加载控制量的标记，并非材料系数|—
\psi|Mode-mixture parameter|模态混合参数|1
T_i|Interface temperature|界面温度|K
v_c|Crack-front speed|裂纹前沿速度|m s⁻¹
P_{\rm load}|Mechanical power delivered to the solid|传给固体的力学功率|W
P_{\rm other}|Additional nonfracture dissipation rate|额外非断裂耗散率|W
\mathcal L_c|Active crack-front line|活动裂纹前沿线|—
r|Radial coordinate in the plate plane|板平面内的径向坐标|m
b|Existing circular-delamination radius|现有圆形脱层半径|m
w(r)|Blister opening displacement|鼓泡张开位移|m
p_0|Externally maintained pressure difference|外部维持的恒定压差|Pa
\mathscr L_r|Axisymmetric planar Laplacian|轴对称平面拉普拉斯算子|m⁻²
f|Arbitrary smooth radial test function, with units set by its argument in the operator check|任意光滑径向测试函数，单位由算子检验中的具体对象确定|—
g|Sum of radial plate curvatures|径向板曲率之和|m⁻¹
g(r)|Sum of radial plate curvatures|径向板曲率之和|m⁻¹
C_1|Curvature integration constant|曲率积分常数|m⁻¹
C_2|Curvature integration constant|曲率积分常数|m⁻¹
C_3|Displacement integration constant|位移积分常数|m
C_4|Displacement integration constant|位移积分常数|m
w^{\prime}|Dimensionless radial displacement slope|无量纲径向位移斜率|1
w(0)|Center displacement|中心位移|m
V_{\rm bl}|Added blister volume|新增鼓泡体积|m³
dr|Radial integration element|径向积分微元|m
C_b|Blister volume compliance at fixed crack radius|固定裂纹半径下的鼓泡体积柔度|m³ Pa⁻¹
v|Dummy volume along the fixed-radius elastic loading curve|固定半径弹性加载曲线上的体积哑变量|m³
dv|Dummy-volume integration element|体积哑变量积分微元|m³
G_{p_0}|Energy-release rate at fixed maintained pressure|固定恒定压力下的能量释放率|J m⁻²
p_{0,\rm crit}|Positive critical maintained pressure for crack onset|裂纹起始扩展所需的正临界恒定压力|Pa
\bar V|Imposed fixed added volume, not an average|施加的固定新增体积，并非平均值|m³
p(b)|Pressure required at the stated radius under fixed volume|固定体积下指定半径所需的压力|Pa
G_{\bar V}|Energy-release rate at fixed added volume|固定新增体积下的能量释放率|J m⁻²
M_r(b)|Radial bending moment per edge length at the crack edge|裂纹边缘单位边长的径向弯矩|N
\sigma_{rr}|Radial normal bending stress|径向法向弯曲应力|Pa
\delta|Physical relative tensile opening in the cohesive law|内聚关系中的实际相对拉伸张开|m
d\delta|Opening integration element|张开积分微元|m
t_n(\delta)|Magnitude of tensile cohesive traction|拉伸内聚牵引大小|Pa
t_n|Magnitude of tensile cohesive traction|拉伸内聚牵引大小|Pa
T_{\max}|Peak tensile cohesive traction|峰值拉伸内聚牵引|Pa
\delta_0|Opening at peak cohesive traction|峰值内聚牵引处的张开量|m
\delta_c|Opening at complete cohesive separation|内聚完全分离处的张开量|m
m_j|Liquid mass in one uniform cylindrical jet|单股均匀圆柱射流中的液体质量|kg
\rho|Carrier-liquid density|载液密度|kg m⁻³
d_j|Jet diameter|射流直径|m
L_j|Emitted jet length|喷出射流长度|m
E_j|Assigned kinetic energy per jet|指定的单射流动能|J
U_j|Uniform jet speed|均匀射流速度|m s⁻¹
N|Number of identically supplied independent jets|供能相同且独立的射流数|1
E_{\rm in}|Total incoming jet kinetic energy|入射射流总动能|J
I_{\rm in}|Aligned incoming jet momentum|对齐入射射流动量|N s
E_{\rm solid}|Assigned useful solid-energy budget|指定的有效固体能量预算|J
I_{\rm net}|Net opening-direction impulse after all load-path reactions|考虑全部载荷路径反作用后的净张开方向冲量|N s
\eta_E|Stipulated useful solid-energy fraction|假设的有效固体能量比例|1
\eta_I|Stipulated net-impulse fraction|假设的净冲量比例|1
E_{\rm req}(v_f)|Minimum fracture-plus-translation energy|最低断裂加平动能量|J
I_{\rm req}(v_f)|Required net impulse for the minimum departure speed|达到最低离开速度所需的净冲量|N s
E_{\rm req}|Minimum fracture-plus-translation energy|最低断裂加平动能量|J
I_{\rm req}|Required net impulse|所需净冲量|N s
v_f|Minimum required payload departure speed|被转印对象最低要求离开速度|m s⁻¹
v_{\rm CM}|Actual final center-of-mass speed|实际最终质心速度|m s⁻¹
K_{\rm CM}|Center-of-mass kinetic energy|质心动能|J
\Delta x|Lateral payload offset|被转印对象横向偏移|m
H_f|Normal payload flight gap|被转印对象法向飞行间隙|m
\theta|Departure angle relative to the receiver normal|相对于接收体法向的离开角|rad
''')

# Mathematical constants have the same role across units; derivatives and
# integral conventions remain next to the local table, not mixed with variables.
for vocabulary in VOCABULARY.values():
    vocabulary[r'\pi']=('Circle constant','圆周率','1')

add(5,r'''
r_0|Reference material radius|参考物质半径|m
r|Current material radius|当前物质半径|m
\lambda_r|Radial principal stretch|径向主伸长比|1
\lambda_\theta|Polar tangential principal stretch|极角切向主伸长比|1
\lambda_\phi|Azimuthal tangential principal stretch|方位角切向主伸长比|1
\theta|Polar tangential coordinate label|极角切向坐标标记|—
\phi|Azimuthal tangential coordinate label|方位角切向坐标标记|—
\mathbf T^e|Elastic Cauchy stress tensor, tension positive|拉伸取正的弹性柯西应力张量|Pa
T^e_{rr}|Radial elastic Cauchy stress|径向弹性柯西应力|Pa
T^e_{\theta\theta}|Polar tangential elastic Cauchy stress|极角切向弹性柯西应力|Pa
T^e_{\phi\phi}|Azimuthal tangential elastic Cauchy stress|方位角切向弹性柯西应力|Pa
\chi|Incompressibility multiplier|不可压缩约束乘子|Pa
\mathbf I|Identity tensor|单位张量|1
\mathbf F|Deformation gradient|变形梯度|1
\mathbf B|Left Cauchy–Green tensor|左柯西—格林张量|1
p_b|Cavity pressure|空腔压力|Pa
p_\infty|Far-field pressure|远场压力|Pa
q|Reference-to-current radial-coordinate ratio|参考与当前径向坐标之比|1
q(R)|Coordinate-ratio value at the cavity wall|空腔壁面处的坐标比值|1
q(\infty)|Coordinate-ratio value in the far-field limit|远场极限处的坐标比值|1
dq|Dimensionless coordinate-ratio integration element|无量纲坐标比积分微元|1
dr|Current-radius integration element|当前半径积分微元|m
\xi|Dummy cavity-radius integration coordinate|空腔半径积分哑坐标|m
d\xi|Dummy-radius integration element|半径哑坐标积分微元|m
\delta R|Small departure from the reference cavity radius|偏离参考空腔半径的微小变化|m
\mathbf T|Total Cauchy stress tensor|总柯西应力张量|Pa
\mathbf D|Material strain-rate tensor|物质应变率张量|s⁻¹
u_r|Radial material velocity|物质径向速度|m s⁻¹
t|Time|时间|s
\dot R|Cavity-wall radial velocity|空腔壁面径向速度|m s⁻¹
\ddot R|Cavity-wall radial acceleration|空腔壁面径向加速度|m s⁻²
a_r|Material radial acceleration|物质径向加速度|m s⁻²
T_{rr}|Total radial Cauchy stress|总径向柯西应力|Pa
T_{\theta\theta}|Total polar tangential Cauchy stress|总极角切向柯西应力|Pa
\sigma|Constant interface surface tension|恒定界面表面张力|N m⁻¹
p_{\mathrm{el}}(R)|Signed elastic cavity-pressure resistance|带符号弹性空腔压力阻力|Pa
p_{\mathrm{el}}(\xi)|Elastic resistance at the dummy integration radius|积分哑半径处的弹性阻力|Pa
E_\sigma|Interface energy|界面能|J
\dot V|Cavity volume-change rate|空腔体积变化率|m³ s⁻¹
P_{\mathrm{dis}}|Nonnegative viscous dissipation power|非负黏性耗散功率|W
\Delta V|Expanded cavity volume relative to the reference state|相对于参考状态的空腔膨胀体积|m³
\Delta p_w|Illustrative constant net pressure-work input|示例中的恒定净压力功输入压差|Pa
W_{100}|Illustrative pressure work using a 100-kPa input|采用 100 kPa 输入的示例压力功|J
p_{\mathrm{visc,RHS}}|Signed viscous pressure on the radial equation's right-hand side|径向方程右侧的带符号黏性压力|Pa
\mathrm{De}|Event Deborah number|事件德博拉数|1
T_{\mathrm{sh}}|Shear stress|剪切应力|Pa
\gamma|Small shear strain|微小剪切应变|1
\dot\gamma|Shear-strain rate|剪切应变率|s⁻¹
\gamma_0|Initial shear strain|初始剪切应变|1
\tau_{\mathrm{KV}}|Kelvin–Voigt zero-stress recovery time, not a stress-memory relaxation time|Kelvin–Voigt 零应力恢复时间，并非应力记忆松弛时间|s
c_s|Small-strain shear-wave speed estimate|小应变剪切波速度估计|m s⁻¹
t_s|Shear crossing-time estimate|剪切跨越时间估计|s
t_{c,\mathrm{liq}}|Ideal empty-cavity liquid-collapse time|液体中理想空腔塌缩时间|s
R_{\max}|Maximum liquid-control cavity radius|液体对照中的最大空腔半径|m
\rho_l|Liquid-control density|液体对照密度|kg m⁻³
\Delta p_c|Positive liquid-control collapse pressure gap|液体对照中的正塌缩压差|Pa
c_L|Longitudinal-wave speed in the separate compressible extension|独立可压缩扩展中的纵波速度|m s⁻¹
t_L|Longitudinal crossing-time estimate|纵波跨越时间估计|s
M_w|Wall Mach number|壁面马赫数|1
\mathbf j_l|Solvent volume flux relative to the network|相对于网络的溶剂体积通量|m s⁻¹
p_{\mathrm{pore}}|Incremental pore pressure|孔隙压力增量|Pa
M_d|Adopted storage/constrained drained modulus|采用的储存／受约束排水模量|Pa
D_{\mathrm{poro}}|Poroelastic diffusion coefficient|孔弹性扩散系数|m² s⁻¹
t_{\mathrm{poro}}|Drainage-time estimate|排水时间估计|s
\mathbf J_{\mathrm{target}}|Vector impulse delivered to the specified target|传给指定目标的矢量冲量|N s
\mathbf t_{\mathrm{load}}|External load traction|外部载荷牵引|Pa
A_t|Target loading area|目标受载面积|m²
t_0|Specified event start time|指定事件开始时刻|s
t_1|Specified event end time|指定事件结束时刻|s
W_{\mathrm{sep,min}}|Necessary fracture-work budget|必要断裂功预算|J
A_{\mathrm{rel}}|Intended interface release area|目标界面释放面积|m²
\Gamma_c|Interface fracture energy conditional on mode and rate|取决于模态与速率的界面断裂能|J m⁻²
dA|Area integration element|面积积分微元|m²
dt|Time integration element|时间积分微元|s
''')
