"""Explanation–equation alternation required by the Chapter 1 handoff.

Every source row remains traceable. Repeated left-hand sides make continued
equalities readable as separate equations. A wrapped single equation can retain
two display lines; independent transformations receive separate explanations.
"""
import re

def rows(tex):
    tex=tex.strip()
    match=re.fullmatch(r'\\begin\{(aligned|gathered)\}([\s\S]*)\\end\{\1\}',tex)
    inner=match[2].strip() if match else tex
    assert r'\begin{' not in inner,'Nested environments need an explicit split'
    output=[]
    lhs=None
    for row in re.split(r'\\\\(?:\[[^\]]*\])?',inner):
        row=row.strip()
        if not row:continue
        if row.startswith(r'&\quad+') or row.startswith(r'&\quad-'):
            assert output
            output[-1]['source_tex']+=r'\\'+row
            output[-1]['display_tex']=r'\begin{aligned}'+output[-1]['row_tex']+r'\\'+row+r'\end{aligned}'
            continue
        displayed=row
        if row.startswith('&='):
            assert lhs,'Continuation needs its preceding left-hand side'
            displayed=lhs+row
        elif '&' in row:
            lhs=row.split('&',1)[0].strip()
        else:
            lhs=None
        output.append({'source_tex':row,'row_tex':displayed,
                       'display_tex':r'\begin{aligned}'+displayed+r'\end{aligned}' if '&' in displayed else displayed})
    return output

def parse(text):
    result={}
    current=None
    for line in text.strip().splitlines():
        line=line.strip()
        if not line:continue
        if line.isdigit():
            current=int(line);result[current]=[]
        else:
            en,zh=line.split('|',1)
            result[current].append((en,zh))
    return result

DERIVATION = parse(r'''
1
Define wall speed and acceleration as successive time derivatives of radius.|将壁面速度与加速度定义为半径的一阶和二阶时间导数。
Evaluate the radial momentum law at the chosen initial instant. All pressure, capillary, viscous, and squared-speed terms remain present.|在选定初始时刻计算径向动量关系。保留压力、毛细、黏性及速度平方各项。
Set the initial wall speed to zero. The viscous and squared-speed terms vanish, but a pressure imbalance can still produce acceleration.|令初始壁面速度为零。黏性项与速度平方项消失，但压力失衡仍可产生加速度。
2
A fixed spherical shell has constant liquid mass when density is constant and the shell remains entirely liquid.|密度恒定且固定球壳始终属于液体时，壳内液体质量保持不变。
Equate mass inflow at the inner surface to mass outflow at the outer surface. Both fluxes use outward radial velocity.|令内球面的质量流入等于外球面的质量流出。两项通量均采用向外径向速度。
Divide the flux difference by shell thickness and take its zero-thickness limit. This gives the radial derivative of the volume-flux factor.|将通量差除以球壳厚度，再取厚度趋零极限。由此得到体积通量因子的径向导数。
Divide by the positive squared radius to obtain the spherical divergence form of incompressibility.|除以正的半径平方，得到不可压缩条件的球坐标散度形式。
Integrate with respect to radius at fixed time. The integration function may vary with time but cannot vary with radius.|在固定时间对半径积分。积分函数可以随时间变化，但不能随半径变化。
Apply equal liquid and interface normal speeds at the material cavity wall. This determines the integration function.|在物质空腔壁面令液体与界面法向速度相等。由此确定积分函数。
Check the inverse-square decay at twice the wall radius. The ratio is defined here for nonzero wall speed.|在两倍壁面半径处检验平方反比衰减。此处速度比要求壁面速度非零。
3
The spherical velocity has no angular dependence or tangential component. Its curl therefore vanishes in the liquid exterior.|球形速度场不依赖角度且没有切向分量。因此液体外域中的旋度为零。
Use the radial component of the potential-gradient relation and substitute the velocity obtained from continuity.|采用速度势梯度关系的径向分量，并代入连续性方程所得速度。
Integrate with respect to radius. The arbitrary function of time is the potential gauge.|对半径积分。任意时间函数对应速度势的规范自由度。
Choose zero potential at infinity. The decaying radial contribution then leaves a zero gauge function.|选择无穷远处速度势为零。衰减的径向项使规范函数取零。
Evaluate the improper radial integral explicitly. Its infinite-radius endpoint vanishes.|显式计算该径向反常积分。无穷远端点的贡献为零。
4
Apply the product rule to the radius-squared times wall-speed numerator. Both radius factors depend on time.|对半径平方与壁面速度的乘积应用乘积法则。两个半径因子均随时间变化。
Apply the chain rule along the moving wall. The total derivative includes the fixed-position derivative and the radial transport term.|沿运动壁面应用链式法则。全导数包含固定位置导数与径向输运项。
Insert the fixed-position potential derivative and the wall velocity. The transport contribution is the squared wall speed.|代入固定位置速度势导数及壁面速度。输运项为壁面速度的平方。
Combine the two squared-speed contributions. This gives the moving-wall derivative, which differs from the fixed-position derivative.|合并两个速度平方项。由此得到运动壁面导数，它与固定位置导数不同。
5
Use the vector-Laplacian identity. Both zero divergence and zero curl are required to eliminate the bulk viscous-force term.|采用矢量拉普拉斯恒等式。必须同时满足散度为零与旋度为零，才能消去体内黏性力项。
The constant-density momentum equation then reduces to Euler in the liquid bulk. Interface viscous stress is still retained later.|常密度动量方程因此在液体内部约化为欧拉方程。后文仍保留界面黏性应力。
Zero vorticity allows the two coordinate derivatives to be exchanged. The product rule then identifies the derivative of squared speed.|无旋条件允许交换这两个坐标导数。再由乘积法则识别速度平方的导数。
Write the component calculation as a vector identity. Substitute the velocity potential into the convective acceleration.|将分量计算写成矢量恒等式。把速度势代入对流加速度。
For a smooth potential, exchange spatial and time derivatives. The complete Euler equation becomes the gradient of one scalar expression.|速度势光滑时可交换空间与时间导数。整个欧拉方程由此成为一个标量表达式的梯度。
A scalar with zero gradient is spatially constant on the connected liquid domain. Its integration function can still depend on time.|在连通液体区域内，梯度为零的标量不随空间位置变化。其积分函数仍可随时间变化。
Apply zero potential and zero velocity at infinity. These reference conditions determine the Bernoulli integration function.|应用无穷远处速度势与速度均为零的条件。这些参考条件确定伯努利积分函数。
Insert that integration function into the spatially integrated momentum equation. This is the unsteady Bernoulli relation for the adopted potential flow.|将该积分函数代回空间积分后的动量方程。所得即为所采用势流的非定常伯努利关系。
Evaluate Bernoulli at the moving wall using the fixed-position time derivative. Move the kinetic term to the pressure side.|使用固定位置时间导数，在运动壁面处计算伯努利关系。将动能项移至压力差表达式中。
6
The liquid-to-gas normal of an inner spherical cavity points inward. Extend it radially without radial variation to evaluate its divergence.|内球形空腔的液体指向气体法向朝内。沿径向作不变延拓，以计算其散度。
Evaluate the normal divergence at the wall. The chosen orientation gives negative spherical curvature.|在壁面处计算法向散度。所选方向给出负的球形曲率。
Project the normal-stress jump onto the interface normal. Keep capillary pressure and liquid normal viscous stress.|将法向应力跃变投影至界面法向。保留毛细压力与液体法向黏性应力。
Differentiate the radial velocity while holding the instantaneous wall radius and wall speed fixed.|对径向速度求空间导数，同时保持该时刻的壁面半径与速度不变。
Evaluate that derivative at the wall and multiply by twice the viscosity. This supplies the viscous pressure correction.|在壁面处计算该导数，并乘以两倍黏度。由此得到黏性压力修正。
7
Start with the liquid-side pressure–inertia relation obtained from Bernoulli.|从伯努利关系得到的液体侧压力—惯性关系出发。
Replace liquid-side wall pressure with bubble pressure minus the capillary and viscous corrections.|用气泡压力减去毛细与黏性修正，替代壁面液体侧压力。
Divide by positive density and radius, then isolate acceleration. The squared-speed term must also be subtracted.|除以正的密度与半径，再解出加速度。还必须减去速度平方项。
Set both speed and acceleration to zero. The remaining pressure excess must equal the spherical capillary pressure.|令速度与加速度均为零。剩余内外压差必须等于球形毛细压力。
8
Adopt an ideal-mixture component equation of state with common gas temperature and positive bubble volume.|采用具有共同气体温度与正气泡体积的理想混合物组分状态方程。
Sum the component equations. The total amount is the sum of PFC vapor, water vapor, and permanent-gas amounts.|对各组分状态方程求和。总物质的量为 PFC 蒸气、水蒸气及非凝结气体物质的量之和。
Divide by bubble volume and separate the three terms. Each term is the corresponding partial pressure.|除以气泡体积，并将三项分开。每一项均为相应组分的分压。
9
Use the spherical volume element. It includes radial thickness and both angular measures.|采用球坐标体积元。它包含径向厚度及两个角度的积分测度。
Integrate the angular factors over the complete sphere. This produces the factor multiplying the radial integral.|在完整球面上积分角度因子。由此得到径向积分之前的球面因子。
Square the continuity velocity and combine its inverse-fourth-radius dependence with the radial volume factor.|将连续性速度平方，再将其半径负四次方与体积元的径向因子合并。
Integrate first to a finite outer radius, then take the infinite-radius limit. The exterior kinetic-energy integral converges.|先积分至有限外半径，再取无穷远极限。外域动能积分收敛。
Multiply the remaining constant factors and the wall-radius endpoint contribution.|将剩余常数因子与壁面半径端点的贡献相乘。
10
Differentiate the kinetic-energy radius and squared-speed factors using the product rule.|用乘积法则对动能中的半径因子与速度平方因子求导。
Apply the chain rule to each factor separately. Both wall speed and wall acceleration appear.|分别对每个因子应用链式法则。壁面速度与加速度均会出现。
Insert those derivatives and factor out the cavity volume rate. The remaining bracket matches radial inertia.|代入上述导数，并提取空腔体积变化率。剩余括号与径向惯性项一致。
Differentiate surface energy at constant surface tension. The changing area supplies its time dependence.|在表面张力恒定时对表面能求导。其时间变化来自面积变化。
11
Multiply the pressure form of radial momentum by cavity volume rate. The left side is the kinetic-energy rate.|将径向动量的压力形式乘以空腔体积变化率。左端成为动能变化率。
Expand the capillary contribution. It is the negative of the surface-energy rate.|展开毛细贡献。它等于表面能变化率的负值。
Expand the viscous contribution. Squared wall speed makes this power loss nonpositive for either motion direction.|展开黏性贡献。壁面速度平方使两种运动方向的该功率损失均非正。
Move the surface-energy rate to the left. Pressure work then balances stored mechanical energy and viscous loss.|将表面能变化率移至左端。压力功因此与储存机械能及黏性损失平衡。
12
Prescribe constant vapor pressure and omit surface tension and viscosity for this ideal control. Express the pressure difference with the collapse sign.|在这一理想对照中给定恒定蒸气压，并忽略表面张力与黏度。用塌缩符号约定表示压差。
Insert these restrictions into Rayleigh–Plesset. The pressure forcing is negative.|将这些限制代入 Rayleigh–Plesset 方程。压力驱动力为负。
Evaluate the initial state at maximum radius with zero wall speed. The squared-speed term vanishes.|在最大半径、壁面速度为零的初始状态求值。速度平方项消失。
Divide by the positive maximum radius. Negative initial acceleration starts the inward collapse branch.|除以正的最大半径。负初始加速度使系统进入向内塌缩分支。
13
Use squared speed as a function of radius. Away from a turning point, the chain rule replaces acceleration by half its radius derivative.|把速度平方视为半径函数。在转折点之外，由链式法则将加速度替换为其半径导数的一半。
Multiply by two and divide by positive radius. This gives a first-order linear equation.|乘以二，再除以正半径。由此得到一阶线性方程。
Choose an integrating factor whose logarithmic derivative equals the radius coefficient. Normalize it at maximum radius.|选择对数导数等于半径系数的积分因子，并在最大半径处归一化。
Integrate that logarithmic derivative between maximum radius and current positive radius. The logarithm uses a dimensionless radius ratio.|在最大半径与当前正半径之间积分该对数导数。对数的自变量是无量纲半径比。
Exponentiate the logarithm relation. The normalized integrating factor is a cubed radius ratio.|对对数关系取指数。归一化积分因子为半径比的三次方。
Multiplication by a constant maximum-radius cube gives the equivalent cubed-radius factor. Expand its product derivative explicitly.|乘以常数最大半径三次方，得到等价的半径三次方因子。显式展开其乘积导数。
14
Integrate the exact derivative from the maximum-radius state. Zero initial speed fixes the integration constant.|从最大半径状态积分该完整导数。零初速确定积分常数。
Evaluate both endpoints. The initial squared-speed contribution is zero.|计算两个端点。初始速度平方的贡献为零。
Divide by the positive current-radius cube. The squared-speed expression is nonnegative on the collapse interval.|除以正的当前半径三次方。所得速度平方在塌缩区间内非负。
Take the square root and select its negative branch. Collapse means decreasing radius.|取平方根并选择负分支。塌缩意味着半径减小。
15
Separate time from radius along the inward trajectory. The reciprocal speed retains the negative collapse sign.|沿向内轨迹分离时间与半径。速度倒数保留塌缩负号。
Introduce radius normalized by maximum radius. Rewrite the denominator using its cubed ratio.|引入以最大半径归一化的半径。用其三次方比值改写分母。
Transform both the radius differential and denominator. The Jacobian contributes one maximum-radius factor.|同时变换半径微分与分母。雅可比因子提供一个最大半径因子。
Reverse the integration limits to cancel the collapse minus sign. The resulting time integral is positive.|反转积分上下限，消去塌缩负号。所得时间积分为正。
16
Use the cube substitution to rewrite the numerator power.|采用三次方换元，改写分子的幂次。
Multiply by the substitution Jacobian. The exponents combine to negative one sixth.|乘以换元的雅可比因子。幂次合并为负六分之一。
Combine the numerical prefactors and identify the first beta-function exponent.|合并数值前因子，并识别贝塔函数的第一个指数参数。
Identify the second beta-function exponent from the square-root denominator.|由平方根分母识别贝塔函数的第二个指数参数。
Both beta-function parameters are positive. Evaluate the convergent integral to obtain the Rayleigh coefficient.|贝塔函数的两个参数均为正。计算收敛积分，得到瑞利系数。
17
Insert the squared-speed trajectory into kinetic energy and cancel density from the prefactor.|将速度平方轨迹代入动能，并在前因子中约去密度。
Distribute the radius-cubed factor. This leaves the difference between maximum and current cavity volumes.|展开半径三次方因子。由此留下最大与当前空腔体积之差对应的项。
Independently integrate constant collapse-pressure work over the decreasing cavity volume. This gives the same kinetic energy.|独立地对减小的空腔体积积分恒定塌缩压力功。所得动能相同。
Differentiate that pressure-work expression. Negative wall speed gives increasing liquid kinetic energy.|对该压力功表达式求导。负壁面速度对应液体动能增加。
Divide by the available ideal pressure-work scale. The energy fraction depends on the cubed radius ratio.|除以可用理想压力功尺度。能量比例取决于半径比的三次方。
18
Convert the declared teaching radius and pressure difference to SI units before substitution.|代入之前，先将给定教学半径与压差换算为 SI 单位。
Evaluate the density-to-pressure square root. Its units convert a radius into a time scale.|计算密度与压力比的平方根。其单位使半径能够转换为时间尺度。
Cube the maximum radius with its SI conversion included.|将已换算为 SI 单位的最大半径取三次方。
Multiply the radius scale, density-pressure factor, and Rayleigh coefficient to obtain collapse time.|将半径尺度、密度—压力因子与瑞利系数相乘，得到塌缩时间。
Multiply maximum cavity volume by collapse pressure. This is the available ideal pressure work.|将最大空腔体积乘以塌缩压力。所得为可用理想压力功。
At half radius, evaluate the cubic ratio and remaining energy fraction explicitly.|在一半半径处，显式计算三次方比值及剩余能量比例。
19
Normalize radius and divide squared ideal wall speed by squared sound speed.|将半径归一化，并将理想壁面速度平方除以声速平方。
Set wall Mach number equal to the chosen diagnostic threshold. Isolate the inverse-cubed radius term.|令壁面马赫数等于选定诊断阈值。分离半径负三次方项。
Add one to both sides. This gives the inverse cube of the threshold radius ratio.|两侧同时加一。由此得到阈值半径比的负三次方。
Take the negative one-third power and insert the declared teaching inputs.|取负三分之一次幂，并代入给定教学输入。
Evaluate the dimensionless numerical factor and its negative cube root.|计算无量纲数值因子及其负三次方根。
Multiply the resulting ratio by maximum radius. This locates the diagnostic point on the ideal trajectory.|将所得比值乘以最大半径。由此定位理想轨迹上的诊断位置。
20
Define local gauge pressure relative to the spatially uniform reference pressure.|相对于空间均匀参考压力，定义局部表压。
At one fixed liquid position, sum gauge pressure times each time-step width and take the continuum limit.|在同一固定液体位置，将表压与各时间段宽度之积求和，再取连续极限。
For mechanical impulse, integrate pressure traction over the control surface as well as time. The outward normal fixes the minus sign.|对于机械冲量，除时间外还须对控制表面积分压力牵引。向外法向确定其负号。
If the surface and orientation remain fixed and liquid-filled, exchange the surface and time integrations.|若表面及其方向固定且始终属于液体，则可交换表面积分与时间积分。
Check units. Surface integration adds an area factor, distinguishing mechanical impulse from local pressure impulse.|检验单位。表面积分增加面积因子，从而区分机械冲量与局部压力冲量。
21
Start from constant-density Navier–Stokes and divide by density. Local velocity changes through pressure gradients, convection, and viscosity. Keep the observation point fixed and integrate every term over the same event interval.|从常密度 Navier–Stokes 方程出发，并除以密度。局部速度变化来自压力梯度、对流与黏性。保持观察点固定，在同一事件区间对每一项积分。
For local acceleration, apply the fundamental theorem of calculus at the same fixed position. The integral is the velocity difference between the two event endpoints, rather than particle displacement.|对于局部加速度，在同一固定位置应用微积分基本定理。积分等于事件两个端点之间的速度差，而非质点位移。
For pressure, smoothness and a common liquid domain permit exchanging the spatial gradient and time integral. Insert the pressure-impulse definition. The reference pressure is spatially uniform, so its gradient contributes zero.|对于压力项，光滑性与共同液体区域允许交换空间梯度与时间积分。代入压力冲量定义。参考压力在空间中均匀，因此其梯度贡献为零。
For viscosity, constant kinematic viscosity can be taken outside the time integral. The velocity field is still needed throughout the interval to evaluate the remaining integral. The convective integral is also retained when the terms are assembled below.|对于黏性项，常运动黏度可提出时间积分号。计算剩余积分仍需要整个区间内的速度场。在下文合并各项时，对流积分也完整保留。
22
Estimate convective acceleration by squared characteristic speed divided by variation length. Integrating over event duration gives its velocity-change scale.|用特征速度平方除以变化长度估计对流加速度。再乘以事件持续时间，得到其速度变化尺度。
Estimate the viscous Laplacian using inverse squared variation length. Compare the resulting viscous impulse with characteristic speed.|用变化长度平方的倒数估计黏性拉普拉斯项。将所得黏性冲量与特征速度比较。
Subtract the divergence-free velocities at the two fixed event endpoints. Their velocity increment remains divergence-free.|将两个固定事件端点的无散速度相减。所得速度增量仍无散。
Take the divergence of the reduced pressure-impulse relation. With constant density, incompressibility gives Laplace's equation.|对约化压力冲量关系取散度。密度恒定时，不可压缩条件给出拉普拉斯方程。
23
Integrate the one-dimensional Laplace equation once. Its pressure-impulse gradient is constant.|对一维拉普拉斯方程积分一次。压力冲量梯度为常数。
Integrate that constant gradient from the inlet to an arbitrary column position.|从入口至任意液柱位置积分该常梯度。
Apply the prescribed inlet pressure impulse to determine the additive constant.|应用给定入口压力冲量，确定加法积分常数。
Apply zero outlet impulse. This determines the gradient and its negative sign.|应用出口冲量为零的条件。由此确定梯度及其负号。
Insert the gradient into the reduced momentum relation. The resulting axial velocity increment is positive toward the outlet.|将该梯度代入约化动量关系。所得轴向速度增量为正，指向出口。
24
Convert the teaching pressure, pulse duration, and column length to SI units.|将教学压力、脉冲持续时间及液柱长度换算为 SI 单位。
Integrate the constant pressure pulse by multiplying its amplitude and duration.|将恒压脉冲的幅值与持续时间相乘，得到其时间积分。
Calculate density times column length, then divide pressure impulse by this factor to obtain velocity change.|计算密度与液柱长度的乘积，再用压力冲量除以该因子，得到速度变化。
Evaluate displacement relative to variation length using characteristic speed and event duration.|利用特征速度与事件持续时间，计算位移相对于变化长度的比例。
Evaluate the viscous impulse ratio using kinematic viscosity and squared variation length.|利用运动黏度与变化长度平方，计算黏性冲量比值。
Calculate one-way acoustic travel time and compare it with the pressure-pulse duration.|计算单程声传播时间，并将其与压力脉冲持续时间比较。
25
Write the radial unit vector in Cartesian components and the solid-angle integration measure.|用笛卡尔分量表示径向单位矢量，并写出立体角积分测度。
Integrate the azimuthal cosine factor. This cancels the first Cartesian component over a complete revolution.|积分方位角余弦因子。第一笛卡尔分量在完整一周内相互抵消。
Integrate the azimuthal sine factor. This cancels the second Cartesian component.|积分方位角正弦因子。第二笛卡尔分量因此抵消。
Integrate the polar factor for the third component. Its two endpoint contributions are equal.|积分第三分量的极角因子。其两个端点的贡献相等。
Collect the three zero components. An exactly spherical configuration has no preferred vector direction.|合并三个零分量。严格球形构型没有优先的矢量方向。
26
Begin with mass conservation before imposing constant density. Constant density reduces it to zero velocity divergence.|先写质量守恒，再施加常密度条件。常密度使其约化为速度散度为零。
Adopt the Newtonian stress law with constant viscosity. It separates pressure and symmetric velocity-gradient stresses.|采用常黏度牛顿应力定律。该定律区分压力应力与对称速度梯度应力。
Apply momentum conservation without body force. Stress divergence produces material acceleration.|在无体积力时应用动量守恒。应力散度产生物质加速度。
Take the divergence of Newtonian stress. Constant viscosity and incompressibility remove the gradient-of-divergence contribution.|对牛顿应力取散度。常黏度与不可压缩条件消去散度梯度项。
Expand material acceleration into the local time derivative and convective acceleration.|将物质加速度展开为局部时间导数与对流加速度。
27
Represent the interface by a smooth level set increasing into gas. Its gradient defines the normal, and its time change defines normal interface speed.|用向气体侧增大的光滑水平集表示界面。其梯度确定法向，其时间变化确定界面法向速度。
For an interface transported by liquid without phase slip, impose zero material change of the level set.|对于由液体输运且没有相变滑移的界面，令水平集的物质变化为零。
Apply the clean-interface traction jump using the liquid-to-gas normal and signed curvature.|采用液体指向气体的法向与带符号曲率，应用清洁界面牵引跃变关系。
Insert gas pressure stress and liquid Newtonian stress into the traction jump.|将气体压力应力与液体牛顿应力代入牵引跃变关系。
Use unit normal magnitude and orthogonality of normal and tangent before taking projections.|在作投影之前，使用单位法向的模长条件及法向与切向的正交性。
Project the traction jump onto the normal. This gives the normal pressure and viscous-stress balance.|将牵引跃变投影至法向。由此得到法向压力与黏性应力平衡。
Project onto a tangent. Constant surface tension and negligible gas viscous stress give zero tangential liquid traction.|投影至切向。常表面张力及可忽略的气相黏性应力给出零液体切向牵引。
28
Combine incompressibility with a single-valued velocity potential. The potential must satisfy Laplace's equation.|将不可压缩条件与单值速度势结合。速度势必须满足拉普拉斯方程。
Set viscosity to zero in the interface pressure condition. Only bubble pressure and capillarity remain.|在界面压力条件中令黏度为零。仅保留气泡压力与毛细作用。
Use the far-field Bernoulli reference to isolate the fixed-position potential derivative.|采用远场伯努利参考条件，解出固定位置的速度势导数。
Replace liquid-side pressure by the inviscid interface pressure. Keep the negative kinetic contribution.|用无黏界面压力替代液体侧压力。保留负的动能贡献。
Apply the chain rule to potential evaluated along an interface marker. Its total derivative includes marker motion.|对沿界面标记点计算的速度势应用链式法则。其全导数包含标记点运动。
The marker follows liquid velocity, and the potential gradient is that same velocity. Their contraction is squared speed.|标记点随液体速度运动，速度势梯度也等于该速度。两者缩并得到速度平方。
Combine the kinetic contribution from Bernoulli with the marker-transport contribution. The material potential derivative has a positive half-squared-speed term.|合并伯努利关系中的动能贡献与标记点输运贡献。速度势物质导数因此含正的二分之一速度平方项。
29
Evaluate the spherical potential at the interface. One wall-radius factor cancels.|在界面处计算球形速度势。一个壁面半径因子约去。
Differentiate the wall potential with the product rule. This is the derivative along the moving interface.|用乘积法则对壁面速度势求导。它是沿运动界面的导数。
Insert spherical curvature and collect the squared-speed terms from the dynamic interface condition.|代入球形曲率，并合并动态界面条件中的速度平方项。
Multiply by minus one and reverse the pressure-difference signs. The inviscid radial equation is recovered.|两侧乘以负一，并反转压差符号。由此恢复无黏径向方程。
30
Linearize mass and momentum about a uniform stationary liquid. Adopt the constant-sound-speed barotropic pressure relation.|在均匀静止液体附近线性化质量与动量方程。采用常声速正压压力关系。
Differentiate continuity in time and take the divergence of momentum. This prepares elimination of the velocity perturbation.|对连续性方程取时间导数，并对动量方程取散度。由此为消去速度扰动作准备。
Eliminate velocity divergence and use the pressure–density relation. The pressure perturbation obeys the acoustic wave equation.|消去速度散度，并采用压力—密度关系。压力扰动满足声学波动方程。
Use distance equal to sound speed times travel time. Divide that travel time by the actual event-variation time.|采用传播距离等于声速乘以传播时间的关系。再将传播时间除以实际事件变化时间。
Insert the teaching communication length and sound speed. Convert the result to nanoseconds.|代入教学传播长度与声速。将结果换算为纳秒。
Divide the travel time by the short ten-nanosecond pressure-variation time.|将传播时间除以十纳秒的短压力变化时间。
Repeat with a one-microsecond event after converting it to nanoseconds.|将一微秒事件换算为纳秒后，重复计算。
Hold wall speed fixed in both cases. The Mach number remains small even though the communication-time ratios differ.|在两个情形中保持相同壁面速度。尽管传播时间比不同，马赫数仍均较小。
31
Use the spherical interface stress balance to express liquid-side pressure in terms of bubble pressure.|利用球形界面应力平衡，以气泡压力表示液体侧压力。
Use Bernoulli to express that same liquid pressure through wall inertia.|利用伯努利关系，通过壁面惯性表示同一液体压力。
Equate these two pressure expressions and isolate the acceleration contribution.|令这两个压力表达式相等，并分离加速度贡献。
Divide by positive liquid density and cavity radius. This gives acceleration for the stated pressure input.|除以正的液体密度与空腔半径。由此得到给定压力输入下的加速度。
32
Introduce squared speed and multiply the ideal radial equation by its integrating factor.|引入速度平方，并将理想径向方程乘以积分因子。
Integrate from the stationary maximum-radius state. Its initial squared speed is zero.|从最大半径处的静止状态开始积分。其初始速度平方为零。
Choose inward speed, separate time and radius, and normalize the collapse-time integral.|选择向内速度，分离时间与半径，并将塌缩时间积分无量纲化。
Independently integrate pressure work over cavity volume. This checks the trajectory's energy and integration constant.|独立地对空腔体积积分压力功。这检验轨迹的能量与积分常数。
33
Begin with the exact fixed-position integrated momentum relation. Retain convective and viscous impulses.|从精确的固定位置积分动量关系出发。保留对流与黏性冲量。
Under the stated scale and geometry conditions, neglect those two contributions relative to the leading velocity change.|在已声明的尺度与几何条件下，相对于主导速度变化忽略这两项贡献。
Apply incompressibility to the reduced velocity increment. Pressure impulse then satisfies Laplace's equation.|对约化速度增量应用不可压缩条件。压力冲量因此满足拉普拉斯方程。
Apply the inlet and outlet impulse values to the straight-column solution.|将入口与出口冲量值应用于直液柱解。
Differentiate the resulting pressure-impulse profile and divide its negative gradient by density.|对所得压力冲量分布求导，再将其负梯度除以密度。
''')

RESULT = parse(r'''
1
Prescribe a positive initial cavity radius.|给定正的空腔初始半径。
Prescribe initial wall speed separately; it may be zero.|独立给定初始壁面速度，其值可以为零。
Complete the exterior problem with zero far-field velocity and prescribed far-field pressure.|用零远场速度与给定远场压力补全外域问题。
2
The integrated continuity equation leaves a time-dependent radial flux factor.|积分连续性方程后，留下随时间变化的径向通量因子。
The material-wall condition fixes that factor.|物质壁面条件确定该因子。
Divide by squared radius to recover the exterior velocity used below.|除以半径平方，恢复下文所用外域速度。
3
Collect the radial integration with its zero-potential reference.|结合径向积分及其零速度势参考条件。
Differentiate the result to check that its gradient reproduces velocity.|对结果求导，检验其梯度恢复速度。
4
Hold the observation radius fixed while differentiating the potential.|对速度势求导时保持观察半径固定。
Evaluate this fixed-position derivative at the instantaneous wall radius.|在瞬时壁面半径处计算该固定位置导数。
Keep the moving-wall total derivative distinct when it is used later.|后续使用时，须区分沿运动壁面的全导数。
5
At the wall, Bernoulli balances pressure with local potential change and kinetic energy.|在壁面处，伯努利关系将压力与局部速度势变化及动能联系起来。
Insert the fixed-position derivative and the wall speed.|代入固定位置导数与壁面速度。
Combine the squared-speed coefficients to obtain the radial inertia term.|合并速度平方的系数，得到径向惯性项。
6
Collect the evaluated wall velocity gradient.|汇总在壁面处计算的速度梯度。
Insert that gradient and spherical curvature into liquid-side wall pressure.|将该梯度与球形曲率代入壁面液体侧压力。
7
Equating interface pressure with liquid inertia gives the complete constant-property spherical motion law.|令界面压力与液体惯性相等，得到完整的常物性球形运动规律。
8
Identify each equation-of-state contribution as a partial pressure. Their sum is the bubble pressure used by the radial model.|将每一项状态方程贡献识别为分压。其总和为径向模型所用气泡压力。
9
Start from kinetic-energy density integrated over the liquid exterior.|从对液体外域积分动能密度出发。
Insert the continuity velocity and complete the angular integration.|代入连续性速度，并完成角度积分。
Evaluate both radial endpoints to obtain the finite exterior kinetic energy.|计算两个径向端点，得到有限的外域动能。
10
Collect the differentiated kinetic energy in a form containing radial inertia.|将动能导数整理为包含径向惯性项的形式。
Record cavity volume and its rate for the pressure-work calculation.|写出空腔体积及其变化率，用于压力功计算。
Record surface energy and its rate at constant surface tension.|写出常表面张力下的表面能及其变化率。
11
Collect stored kinetic and surface energy on the left of the power balance.|在功率平衡左端汇总储存的动能与表面能。
The dissipation magnitude is nonnegative for positive viscosity and radius.|黏度与半径为正时，耗散量非负。
12
Define a positive collapse-pressure difference.|定义正的塌缩压差。
Start from maximum radius with a stationary wall.|从最大半径、壁面静止状态开始。
The resulting ideal radial equation drives inward collapse.|所得理想径向方程驱动向内塌缩。
13
Record the chain-rule substitution and its nonzero-speed cancellation before extending to the turning point.|记录链式法则代换及非零速度约去步骤，再延拓至转折点。
The substitution produces this first-order radius equation.|该代换得到以下关于半径的一阶方程。
Multiplication by the integrating factor turns its left side into a complete derivative.|乘以积分因子，使左端成为完整导数。
14
Write the two-endpoint integral with the initial term retained explicitly.|保留初始项，显式写出双端点积分。
Use zero initial squared speed and select the negative collapse branch.|采用初始速度平方为零的条件，并选择负的塌缩分支。
15
Integrate reciprocal inward speed and reverse the bounds to obtain positive elapsed time.|积分向内速度的倒数，并反转上下限以得到正的经过时间。
Introduce the normalized radius and transform its differential.|引入无量纲半径，并变换其微分。
Separate the dimensional time scale from its dimensionless coefficient.|将有量纲时间尺度与无量纲系数分离。
16
State the cube substitution and its Jacobian together.|一并写出三次方换元及其雅可比因子。
Identify the transformed integral with the beta function and evaluate its coefficient.|将变换后的积分识别为贝塔函数，并计算其系数。
Use the integral definition with positive beta-function arguments.|采用贝塔函数参数为正时的积分定义。
17
Insert the ideal speed into exterior kinetic energy.|将理想速度代入外域动能。
Normalize by the maximum available ideal pressure work.|用最大可用理想压力功归一化。
18
Convert the calculated collapse time to microseconds.|将算得塌缩时间换算为微秒。
Convert the available ideal pressure work to nanojoules.|将可用理想压力功换算为纳焦耳。
Evaluate the negative wall speed at half maximum radius.|计算最大半径一半处的负壁面速度。
Multiply available work by the half-radius energy fraction.|将可用功乘以一半半径处的能量比例。
19
Define wall Mach number using the magnitude of wall speed.|用壁面速度的大小定义壁面马赫数。
Collect the algebraic threshold-radius relation.|汇总阈值半径的代数关系。
Record the illustrative threshold and sound-speed inputs with the resulting radius ratio.|写明示例阈值、声速输入及所得半径比。
20
The continuum limit defines pressure impulse at a fixed liquid position.|连续极限定义固定液体位置处的压力冲量。
The integration interval is the positive event duration.|积分区间对应正的事件持续时间。
Local pressure impulse has pressure-times-time units.|局部压力冲量具有压力乘以时间的单位。
21
Assemble the integrated local, pressure, convective, and viscous terms. This relation is exact within the stated constant-property incompressible model while the observation point remains liquid. No short-event terms have yet been discarded.|合并已积分的局部、压力、对流与黏性各项。在所声明的常物性不可压缩模型内，只要观察点始终属于液体，该关系就是精确的。此时尚未舍弃任何短事件项。
Recall that this increment compares velocity at the same position at two times.|此速度增量比较的是同一位置在两个时刻的速度。
Use dynamic viscosity divided by density to define kinematic viscosity.|用动力黏度除以密度，定义运动黏度。
22
Require small convective impulse on the chosen velocity scale.|要求在所选速度尺度下，对流冲量足够小。
Require small viscous impulse on that same scale.|要求在同一尺度下，黏性冲量足够小。
Under the stated additional assumptions, retain the pressure contribution as the leading velocity change.|在已声明的附加假设下，保留压力贡献作为主导速度变化。
Apply incompressibility to this reduced relation to obtain the pressure-impulse boundary equation.|对该约化关系应用不可压缩条件，得到压力冲量边值方程。
23
The first integration makes pressure impulse linear in column position.|第一次积分使压力冲量成为液柱位置的线性函数。
The two endpoint values determine its two integration constants.|两个端点值确定两个积分常数。
Insert the resulting gradient into the axial velocity increment.|将所得梯度代入轴向速度增量。
24
Collect the pressure-pulse time integral.|汇总压力脉冲的时间积分。
Record the predicted column velocity change and acoustic travel time.|写出所预测的液柱速度变化与声传播时间。
Compare the convective, viscous, and acoustic ratios before using the reduced model.|使用约化模型之前，比较对流、黏性与声学比值。
25
Define stand-off using center-to-boundary distance divided by maximum radius.|用中心至边界距离除以最大半径，定义相对壁距。
The zero angular vector integral records the absence of a preferred direction under exact spherical symmetry.|角向矢量积分为零，表明严格球对称时没有优先方向。
26
State the constant-density mass-conservation condition.|写出常密度质量守恒条件。
Combine material acceleration and Newtonian stress divergence to obtain the spatial liquid momentum equation.|结合物质加速度与牛顿应力散度，得到空间液体动量方程。
27
Define symmetric strain rate and signed curvature using the adopted normal orientation.|根据所采用的法向方向，定义对称应变率与带符号曲率。
Collect interface kinematics and normal pressure balance.|汇总界面运动学与法向压力平衡。
Collect tangential traction and the inner-sphere curvature sign.|汇总切向牵引条件及内球面曲率符号。
28
State potential velocity and its incompressible field equation.|写出势流速度及其不可压缩场方程。
Advance each material interface marker with the local liquid velocity.|用局部液体速度推进每个物质界面标记点。
Use the inviscid interface pressure in the fixed-position Bernoulli relation.|在固定位置伯努利关系中采用无黏界面压力。
Apply the moving-marker chain rule to the potential derivative.|对速度势导数应用运动标记点链式法则。
Collect the pressure, curvature, and positive kinetic contribution on the material interface.|在物质界面上汇总压力、曲率及正的动能贡献。
29
Insert spherical wall potential and inward-normal curvature.|代入球形壁面速度势与向内法向曲率。
Use the material interface derivative in the dynamic potential condition.|在动态速度势条件中采用界面物质导数。
Recover the inviscid Rayleigh–Plesset pressure–inertia balance.|恢复无黏 Rayleigh–Plesset 压力—惯性平衡。
30
Use the wall Mach number to assess wall speed relative to sound speed.|用壁面马赫数评估壁面速度相对于声速的大小。
Separately compare acoustic crossing time with the actual event-variation time.|另行比较声传播时间与实际事件变化时间。
31
Collect the radial motion law for the pressure-to-liquid-motion explanation.|为压力驱动液体运动的解释汇总径向运动规律。
Identify the vapor and permanent-gas inputs still needed to prescribe bubble pressure.|明确给定气泡压力仍需的蒸气与非凝结气体输入。
32
State the inward branch of the ideal collapse trajectory.|写出理想塌缩轨迹的向内分支。
State its collapse time with the evaluated beta-function coefficient.|用已求得的贝塔函数系数写出其塌缩时间。
State the independently checked exterior kinetic energy.|写出经独立压力功方法检验的外域动能。
33
Begin with the fixed-position pressure-impulse definition.|从固定位置的压力冲量定义出发。
State the leading velocity-change relation and its incompressible boundary equation under the required approximations.|在所需近似下，写出主导速度变化关系及其不可压缩边值方程。
Connect the column velocity scale to the pressure-impulse boundary values, and check the acoustic response time.|将液柱速度尺度连接至压力冲量边界值，并检验声学响应时间。
''')

def narrative(identifier,derivation_tex,result_tex):
    number=int(identifier[-2:])
    output=[]
    for phase,tex,notes in [('derivation',derivation_tex,DERIVATION[number]),('result',result_tex,RESULT[number])]:
        parts=rows(tex)
        assert len(parts)==len(notes),(identifier,phase,len(parts),len(notes))
        for index,(part,(en,zh)) in enumerate(zip(parts,notes),1):
            output.append(dict(part,en=en,zh=zh,phase=phase,index=index))
    return output
