# COMSOL 6.4 逐步操作：两个简洁的单脉冲模型

将本指南放在 COMSOL 窗口旁，每次完成一个编号步骤。操作路线是：**空白 0D 模型 → 求解模型 A → 水凝胶模型 B → 密封对照 → 经验证的输出表格**。每个步骤都指出需要选择的节点、需要输入的内容以及继续之前的检查项。各个检查点文件均为你自己建立的练习文件。

模型 A 针对有限的激活后压力源和与其连通的液体出口，回答给定条件下的压力与射流速度问题。模型 B 加入球形凝胶的约束，计算同一出口还能传递多少排出动能和排出冲量。标称为 10 ns 的单次激光脉冲通过激活并完成压力均衡后的初始数据表示。本研究中的零时刻就是该初始化状态，此后不再施加源驱动。

**声明的对照假设。** 压力源为封闭的绝热理想气体，压力均匀，绝热指数恒定且大于一，可用功有限。载液密度和出口的有效流体惯性保持恒定。出口预先开放；恒定的弯月面入口压力是一项近似。模型 B 使用完整、不排水、不可压缩的新胡克凝胶，并加入 Kelvin–Voigt 损耗，将其近似为包围腔室的球形介质。初始机械速度为零，腔壁参考构形无应力，远场压力和出口端压力均为环境压力。液体向外运动和腔壁向外扩张的速度取正。后续回弹、相间交换、凝胶破裂和靶面冲击均不在本次首次向外排出过程的计算范围内。实际 PFC 和凝胶的性质需要标定。

完整的理论基础、推导、符号表和有效性审查见 [MODEL_SPEC.md](MODEL_SPEC.md) 与[完整离线报告](index.html#theory)。本指南将这些方程转化为可在 COMSOL 中直接输入的内容；表达式表采用 COMSOL 语法。

![模型机制及定义的输出量](assets/guide-mechanisms.svg)

*带标注的机制示意图。模型 A 固定腔壁。模型 B 允许压力源体积通过出口排液和凝胶腔壁扩张共同增加。图中表示标量平衡关系，不表示空间场分布。*

## A — 熟悉界面并建立练习模型

### 步骤 01 — 识别三个工作区域

**位置:** COMSOL Desktop。

**操作:** 找到左侧的 **Model Builder**（模型开发器）、中间显示所选节点设置的 **Settings**（设置），以及右侧用于绘图的 **Graphics**（图形）。Progress、Messages、Log 和 Results 表格通常位于下方。节点路径如 `Global Definitions → Parameters 1`，表示展开第一个节点并选中其子节点。右键操作会在鼠标所指节点下创建子节点。修改表格单元格后，按 Tab 或单击单元格外部，提交输入内容。

**检查:** 在输入任何方程之前，你能够选中一个节点，并看到它对应的 Settings 内容发生变化。

![COMSOL 工作区域](assets/guide-interface.svg)

*这是界面示意图，并非屏幕截图。具体位置取决于窗口布局；定位时以节点名和字段名为准。*

### 步骤 02 — 新建模型

**位置:** `File → New → Model Wizard`。

**操作:** 打开 COMSOL Multiphysics 6.4。在 New 页面选择 Model Wizard。切换模型之前，将已有工作保存到其自身文件中。在本指南旁新建一个 `practice/` 文件夹，用于练习；后续提示保存时，可在 Save As 对话框中创建该文件夹。

**检查:** 向导显示 **Select Space Dimension**（选择空间维度）。

### 步骤 03 — 选择空间维度

**位置:** `Model Wizard → Select Space Dimension`。

**输入:** 选择 **0D**。

**检查:** 向导进入 Select Physics。未知量将是随时间变化的标量。腔室和出口半径作为参数出现在方程中；此模型无需创建球体或圆柱体几何。

### 步骤 04 — 添加标量方程接口

**位置:** `Select Physics → Mathematics → ODE and DAE Interfaces → Global ODEs and DAEs`。

**操作:** 选择 Global ODEs and DAEs，并单击 **Add**。如果列表较长，可搜索该接口的完整名称。只保留一个该接口。

**检查:** Added physics interfaces 中包含 Global ODEs and DAEs。该接口提供后面使用的 Global Equations（全局方程）表。

**排错:** 清除搜索筛选条件，并确认已选择 0D。交付的原生文件仅记录基础 COMSOL 许可证；凝胶本构关系通过标量表达式输入。

### 步骤 05 — 添加瞬态研究

**位置:** `Model Wizard → Study → General Studies`。

**输入:** 选择 **Time Dependent**（瞬态），然后单击 **Done**。

**检查:** Model Builder 中包含一个 Component、Global ODEs and DAEs，以及 `Study 1 → Step 1: Time Dependent`。

### 步骤 06 — 设置组件命名空间

**位置:** 单击 `Component 1`。

**输入:** 将 **Name** 设为 `c`，将 **Label** 设为 `c: Model A practice`。保留 SI 单位制。Name 决定表达式（如 `c.U`）所用的命名空间；Label 仅改变界面显示的名称。

**检查:** 组件的 Name 为 `c`。仅在 Label 中写入字母 c，并不会改变命名空间。

**排错:** 如果 Name 仍为 `comp1`，现在就更正。下面所有结果表达式和停止表达式都使用 `c.` 前缀。参见[组件 Name 文档](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_modeling.19.007.html)。

### 步骤 07 — 保存第一个检查点

**位置:** `File → Save As`。

**输入:** 保存为 `practice/A_01_setup.mph`。此后使用 Ctrl+S 保存；在下面指定的阶段另存新的检查点文件。

**检查:** 标题栏显示你的练习文件名。`models/` 中已经验收的原生文件仍可用于对照。

## B — 输入模型 A 的全部参数与表达式

### 步骤 08 — 输入全部 32 个参数

**位置:** `Global Definitions → Parameters 1`。

**操作:** 输入下表的全部行，或单击表格下方的 **Load from File**，选择 [A_parameters_import.txt](resources/gui/A_parameters_import.txt)。该导入文件包含两列，以制表符分隔，不含表头。将其一次性导入参数表即可。参数说明见下表。如果手动输入，请严格保留每个名称的大小写以及单位外的方括号。

**检查:** 共计 32 个参数名，没有重复名称。表格尚未填完时，依赖关系可能暂时无法解析；应在全部行输入完成后再检查 Value 列。`p0` 为绝对压力，`E0` 是由该压力推得的表达式。

| 名称 | 表达式 — 原样输入 | 含义 |
| --- | --- | --- |
| `tauLaser` | `10[ns]` | 单次光脉冲，以激活后的初始状态代替；不求解脉冲起始过程 |
| `Rg0` | `15[um]` | 激活后的压力源半径；不是液态 PFC 液滴半径 |
| `Rc0` | `30[um]` | 初始无应力的球形腔室半径 |
| `a` | `5.0E-6[m]` | 预先存在的液体出口半径 |
| `L` | `50[um]` | 有效液柱惯性长度 |
| `Lbudget` | `(Vc0-Vg0)/A` | 连通腔室的液体存量除以出口面积；与惯性长度不同 |
| `rho` | `1000[kg/m^3]` | 指定的类水载液密度 |
| `rhoG` | `1000[kg/m^3]` | 指定的不排水凝胶密度 |
| `pInf` | `100[kPa]` | 环境绝对压力 |
| `kap` | `1.4` | 绝热理想气体对照模型的指数；不是经过验证的 PFC 蒸气状态方程 |
| `p0` | `379631.6312499547[Pa]` | 激活后的压力源绝对压力，由构建程序根据可用功设定 |
| `sigma` | `0.072[N/m]` | 指定的类水表面张力 |
| `G` | `20000.0[Pa]` | 完整、不可压缩的新胡克凝胶的剪切模量 |
| `etaG` | `0.01[Pa*s]` | Kelvin-Voigt 有效网络黏度 |
| `Kloss` | `0.0` | 给定条件下的出口局部损失系数，无量纲 |
| `Rloss` | `0[Pa*s/m]` | 实测或拟合的压力与速度之比形式的阻力系数；不是瞬时 Poiseuille 近似 |
| `outletOpen` | `1` | 1 表示预先存在的开放液体通道；0 表示密封对照 |
| `cL` | `1500[m/s]` | 仅用于有效性诊断的参考压力均衡传播速度 |
| `Us` | `10[m/s]` | 无量纲状态变量的速度尺度 |
| `tau` | `Rc0/Us` | 数值无量纲化所用的时间尺度 |
| `A` | `pi*a^2` | 液塞横截面积 |
| `Vg0` | `4*pi*Rg0^3/3` | 有限气体压力源的初始体积 |
| `Vc0` | `4*pi*Rc0^3/3` | 初始腔室体积 |
| `Veq` | `Vg0*(p0/pInf)^(1/kap)` | 环境压力下的气体体积 |
| `E0` | `p0*Vg0/(kap-1)*(1-(Vg0/Veq)^(kap-1))-pInf*(Veq-Vg0)` | 相对于环境压力的压力源可用可逆功 |
| `mJet` | `rho*A*L` | 有效液柱惯性质量，不是排出质量 |
| `Iscale` | `mJet*Us` | 排出冲量累积量的动量尺度 |
| `Uceiling` | `sqrt(2*E0/mJet)` | 仅由能量和液柱惯性确定的出口峰值速度上界；不是已达到的速度 |
| `qCeiling` | `E0/(A*L)` | 仅由能量确定的液体动压上界 |
| `pCap` | `2*sigma/a` | 钉扎半球形弯月面的阻力 |
| `tObs` | `1[us]` | 为仅基于冲量的制动压力上界所声明的平均时间区间 |
| `AObs` | `A` | 所声明的压力观测面积 |

### 步骤 09 — 检查初始能量与几何参数

**位置:** 仍在 `Parameters 1` 中，查看 Value 列。

**对照检查:**

| 物理量 | 预期值 |
| --- | --- |
| 初始气体体积 `Vg0` | 1.413716694e-14 m³ |
| 初始腔室体积 `Vc0` | 1.130973355e-13 m³ |
| 出口面积 `A` | 7.853981634e-11 m² |
| 有限液体存量对应的长度 `Lbudget` | 1260.000000 µm |
| 惯性长度 `L` | 50 µm |
| 弯月面压力 `pCap` | 28.8 kPa |
| 时间尺度 `tau` | 3 µs |
| 初始绝对压力 `p0` | 379.631631 kPa |
| 可用功 `E0` | 2 nJ |
| 液柱速度上界 `Uceiling` | 31.915382 m/s |

**原因:** `L` 定义液体惯性。`Lbudget` 定义连通液体最多能排出多少；二者含义不同。2 nJ 表示激活后的机械可用功，不是入射激光能量。`tauLaser=10[ns]` 记录短脉冲假设；它不是随时间变化的驱动函数，仅改变它不会改变本解。

**排错:** 可用功为负或平衡体积无效，通常表明压力或单位输入有误。使用提供的绝对压力 `p0`，不要用 279.632 kPa 的表压替换它。

### 步骤 10 — 创建 Variables 并输入压力源几何表达式

**位置:** 右键选择 `Component c → Definitions → Variables`。

**操作:** 将 Label 设为 `Source, outlet and accounting`。输入下面的前七行。也可以通过 **Load from File** 选择 [A_variables_import.txt](resources/gui/A_variables_import.txt)，一次导入完整的 33 行表格，再按步骤 10–12 检查三个分组。在此组件表内使用局部名称，不要在 Name 列添加 `c.`。

**检查:** 通过 `R=Rc0` 固定腔室半径；腔壁速度严格为 `0[m/s]`。气体体积包含已经排出的液体所对应的体积。在步骤 14 添加方程行后，`qq` 和 `vv` 才会获得定义。

| 名称 | 表达式 — 原样输入 | 单位 | 含义 |
| --- | --- | --- | --- |
| `x` | `Lbudget*qq` | `m` | 已排出液体体积除以出口面积，m |
| `U` | `Us*vv` | `m/s` | 液塞向外运动速度，m/s |
| `R` | `Rc0` | `m` | 腔壁半径，m |
| `Uw` | `0[m/s]` | `m/s` | 腔壁扩张速度，m/s |
| `Vg` | `Vg0+A*x+4*pi*(R^3-Rc0^3)/3` | `m^3` | 包含排液和腔室扩张贡献的有限气体体积 |
| `Vdot` | `A*U+4*pi*R^2*Uw` | `m^3/s` | 压力源体积的总变化率 |
| `pb` | `p0*(Vg0/Vg)^kap` | `Pa` | 有限理想气体对照压力源的均匀绝对压力 |

### 步骤 11 — 输入阻力与储存能量表达式

**位置:** 同一个 Variables 节点。

**操作:** 如果手动输入，添加下面七行。模型 A 将凝胶相关项设为带单位的零。损耗表达式可用于后续敏感性对照；基准损耗输入为零。

**检查:** 液柱能量 `Kjet` 使用有效液柱惯性。它与下一步输入的排出动能 `Eout` 不同。弯月面功是所声明的恒定入口压力对照模型所做的功；本模型不求解自由表面的演变。

| 名称 | 表达式 — 原样输入 | 单位 | 含义 |
| --- | --- | --- | --- |
| `pEl` | `0[Pa]` | `Pa` | 球形凝胶腔壁处的弹性阻力压力 |
| `pRes` | `0[Pa]` | `Pa` | 凝胶腔壁的弹性与黏性阻力之和 |
| `Wgel` | `0[J]` | `J` | 可恢复的凝胶弹性功 |
| `Kgel` | `0[J]` | `J` | 球形凝胶的径向动能 |
| `Kjet` | `mJet*U^2/2` | `J` | 有效液柱惯性储存的动能；不是排出动能 |
| `Esurf` | `pCap*A*x` | `J` | 向外运动期间的可逆弯月面功 |
| `ploss` | `Rloss*U+rho*Kloss*U*abs(U)/2` | `Pa` | 所声明的耗散性出口压降 |

### 步骤 12 — 输入加速度、排出量及检查表达式

**位置:** 同一个 Variables 节点。

**操作:** 添加剩余的 19 行。将排出流体的动压项 `-rho*U^2/2` 保留在 `acc` 中，并将 `Eout` 保留在 `energyResidual` 中。这些项计入真正离开出口的能量。删除它们会改变模型。

**检查:** 完成后的节点包含 33 个名称。`Eout`、`Iout` 和 `Mout` 分别表示实际排出动能、轴向排出冲量和排出液体质量。`Ijet` 表示瞬时有效液柱动量。压力均衡传播比是根据标量变化率计算的有效性诊断量。

| 名称 | 表达式 — 原样输入 | 单位 | 含义 |
| --- | --- | --- | --- |
| `acc` | `outletOpen*(pb-pInf-pCap-ploss-rho*U^2/2)/(rho*L)` | `m/s^2` | 由含排出流体动压项的非定常 Bernoulli 关系得到的出口加速度 |
| `wallAcc` | `0[m/s^2]` | `m/s^2` | 球形凝胶腔壁加速度 |
| `Pdis` | `outletOpen*A*(Rloss*U^2+rho*Kloss*abs(U)^3/2)` | `W` | 非负的出口与凝胶不可逆损耗功率 |
| `Edis` | `E0*dd` | `J` | 累积不可逆损耗 |
| `Eout` | `E0*ee` | `J` | 实际从出口排出的动能 |
| `Iout` | `Iscale*ii` | `N*s` | 实际从出口排出的轴向动量 |
| `Mout` | `rho*A*x` | `kg` | 有限的排出液体质量 |
| `Pout` | `outletOpen*rho*A*U^3/2` | `W` | 向外运动分支的排出动能功率 |
| `energyResidual` | `(pb*Vg/(kap-1)-p0*Vg0/(kap-1)+pInf*(Vg-Vg0)+Kjet+Kgel+Wgel+Esurf+Edis+Eout)/E0` | `1` | 包含实际流出量的归一化能量残差 |
| `Fconf` | `pi*R^2*pEl` | `N` | 一个凝胶半球上的轴向合力，不是整个球体的净合力 |
| `qJet` | `rho*U^2/2` | `Pa` | 液塞动压尺度，不是冲击压力 |
| `Ijet` | `mJet*U` | `N*s` | 有效液柱动量；实际排出冲量为 Iout |
| `Fflux` | `rho*A*U^2` | `N` | 动量通量尺度，不是经求解得到的非定常靶面作用力 |
| `pArrestBound` | `Iout/(AObs*tObs)` | `Pa` | 根据排出冲量和所声明观测条件得到的平均制动压力上界 |
| `stroke` | `x/Lbudget` | `1` | 已用排液体积占有限存量的比例 |
| `stretch` | `R/Rc0` | `1` | 凝胶内腔壁的周向伸长比 |
| `Mjet` | `abs(U)/cL` | `1` | 液体速度的马赫数诊断量 |
| `Mwall` | `abs(Uw)/cL` | `1` | 腔壁速度的马赫数诊断量 |
| `communication` | `L/cL*kap*abs(Vdot)/Vg` | `1` | 压力变化的均衡传播比；不求解传播场 |

### 步骤 13 — 设置方程的物理量类型

**位置:** `Component c → Global ODEs and DAEs → Global Equations 1`。

**输入:** 保留方程组名称 `ODE1`。将 **Dependent variable quantity**（因变量物理量）设为 **Dimensionless (1)**，将 **Source term quantity**（源项物理量）设为 **Dimensionless (1)**。输入五行方程之前，删除默认占位方程行。

**检查:** 两个物理量均为无量纲。每个方程中的因子 `tau` 将变化率转化为无量纲残差。

**输入方程之前明确状态量含义:** `qq=x/Lbudget`；`vv=U/Us`；`dd=Edis/E0`；`ee=Eout/E0`；`ii=Iout/Iscale`。这五个标量是求解未知量。Variables 节点提供代数表达式，并不增加独立未知量。

### 步骤 14 — 输入全部五行全局方程

**位置:** 步骤 13 的 Global Equations 表。

**操作:** 输入下表的每一行，包括两列初始值。表中的方程字段 `f(u,ut,utt,t)` 是由 COMSOL 设为零的残差。对于较长的行，选中该行并在表格下方编辑其字段。[A_equations.tsv](resources/gui/A_equations.tsv) 是带表头的复制粘贴参考文件；参数和变量节点中的 Load from File 按钮不能将它导入本方程表。

**检查:** 名称仅为 `qq`、`vv`、`dd`、`ee`、`ii`，初始值全部为零。`ii` 所在行对动量通量进行积分，而不是将 `mJet*U` 赋给排出冲量。

| 名称 | f(u,ut,utt,t) — 原样输入 | u_0 | ut_0 |
| --- | --- | --- | --- |
| `qq` | `tau*(qqt-outletOpen*U/Lbudget)` | `0` | `0` |
| `vv` | `tau*(vvt-acc/Us)` | `0` | `0` |
| `dd` | `tau*(ddt-Pdis/E0)` | `0` | `0` |
| `ee` | `tau*(eet-Pout/E0)` | `0` | `0` |
| `ii` | `tau*(iit-outletOpen*rho*A*U^2/Iscale)` | `0` | `0` |

### 步骤 15 — 检查导数拼写与初始条件

**位置:** 五行方程及 Variables 节点。

**操作:** 检查 `qqt`、`vvt`、`ddt`、`eet`、`iit`。它们是 COMSOL 的一阶时间导数名称：`vvt` 是 `vv` 的时间导数。不要输入 `vv*t`，后者表示乘法。初始值 `ut_0=0` 沿用已验收的设置；一阶方程负责计算随时间演变的导数。

**检查:** 初始速度为零，不代表初始加速度为零。在基准压力下，`acc` 的初值为正。压力源、体积和输出表达式现在应能通过这五个已声明状态量解析。参见[全局方程文档](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_equationbased.32.089.html)。

### 步骤 16 — 输入输出时间列表

**位置:** `Study 1 → Step 1: Time Dependent`。

**输入:** 保持 Time unit 为 **s**，将 Output times 替换为：

```text
range(0,1[ns],100[us])
```

**检查:** 所请求的时间列表从零开始，到 100 µs 结束，输出间隔为 1 ns。停止条件会提前终止首次过程。这个列表用于数值采样，不代表 10 ns 光脉冲。

### 步骤 17 — 显示瞬态求解器

**位置:** 右键选择 `Study 1 → Show Default Solver`。

**操作:** 展开 `Solver Configurations → Solution 1`，单击 **Time-Dependent Solver 1**。如果这些节点已经存在，直接展开即可。保留自动生成的 Dependent Variables 节点；它将 `ODE1` 方程组连接到求解器。

**检查:** 在 Settings 中可以看到并已选中 Time-Dependent Solver 1。没有添加第二个研究或第二个物理场接口。

### 步骤 18 — 按已验收的求解器设置逐项配置

**位置:** `Solution 1 → Time-Dependent Solver 1`。

**输入:** 使用下表所列的 General、Absolute Tolerance 和 Time Stepping 设置。如果 General 继承研究设置，在 **Defined by study step** 中选择 **User defined**。求解器时间列表必须与步骤 16 相同。

| 设置区域 / 字段 | 设为 |
|---|---|
| General → Defined by study step | User defined |
| General → Output times | `range(0,1[ns],100[us])` |
| General → Relative tolerance | `1e-9` |
| Absolute Tolerance → Global method | Scaled |
| Absolute Tolerance → Tolerance method | Factor |
| Absolute Tolerance → Tolerance factor | `0.1` |
| Absolute Tolerance → variable Method | Use global |
| Time Stepping → Solver type | Implicit |
| Time Stepping → Method | BDF |
| Time Stepping → Steps taken by solver | Strict |
| Time Stepping → Algebraic Variable Settings → Consistent initialization | Off |

**检查:** 可见 BDF、Strict、`1e-9` 和初始化 Off。保留自动选定的初始步长、BDF 阶次及变量尺度。这些方程是一阶常微分方程；将初始化设为 Off 可保留指定的零初始速度。Strict 步进会到达所列时间，必要时还可采用额外内部步。参见[瞬态求解器文档](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_solver.36.139.html)。

### 步骤 19 — 添加全部四条停止规则

**位置:** 右键选择 `Time-Dependent Solver 1 → Stop Condition`。

**操作:** 添加下面四行。**每一行**都将 **Stop if** 设为 **Negative (<0)**，并勾选 **Active**。在 Output at Stop 下，保持 **Add solution = No**，与已验收文件一致。Add warning 可以保持启用。

**检查:** 存在四行启用的规则。由于此求解器节点位于组件命名空间之外，组件表达式需带 `c.` 前缀。

| 停止表达式 | Stop if | Active | 说明 |
| --- | --- | --- | --- |
| `if(outletOpen>0.5,c.U,c.Uw)` | Negative (<0) | Yes | 首次向外排出过程结束，或密封腔壁到达首次转向点 |
| `Lbudget-c.x` | Negative (<0) | Yes | 连通腔室的液体存量耗尽 |
| `1.2-c.stretch` | Negative (<0) | Yes | 声明的 20% 腔壁伸长筛选阈值（不是实测破裂阈值） |
| `0.1-max(c.Mjet,c.Mwall)` | Negative (<0) | Yes | 声明的马赫数 0.1 筛选阈值 |

**原因:** 第一行在首次向外速度回落并穿过零时停止。在密封情况下，它改为检查腔壁速度。其余各行限制液体存量、声明的伸长筛选阈值及马赫数筛选阈值。初始零速度不为负，因此基准计算能够启动。压力均衡传播的筛选阈值在步骤 28 求解完成后检查；它不是在线停止规则。参见[停止条件文档](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_solver.36.212.html)。

### 步骤 20 — 完成求解前检查

**位置:** Parameters、Variables、Global Equations、Time-Dependent 研究及其求解器。

**逐项检查:** 32 个参数；33 个变量；5 行方程；两个方程物理量均为 Dimensionless；全部状态初值为零；研究和求解器均使用 1 ns 时间列表；BDF Strict；一致初始化为 Off；四条已启用的 Negative 停止规则。Initial Values of Variables Solved For 必须来自物理场初始值，而不是此前的非零解。

**操作:** 保存检查点 `practice/A_02_ready_to_solve.mph`。如果未知变量消息提到 `comp1` 或 `c`，更正命名空间；如果提到 `qq` 或 `vv`，检查方程的 Name 列。

### 步骤 21 — 计算首次向外排出过程

**位置:** `Study 1` 工具栏，或右键选择 `Study 1 → Compute`。

**操作:** 单击 Compute，观察 Progress 和 Log。求解完成后再打开结果表。当停止条件满足时出现警告是预期行为，但警告说明必须对应某一条已声明规则。

**检查:** 储存的过程在约 **33.885 µs** 结束，早于所请求的 100 µs。基准情况下液体向外排出，速度达到峰值后逐渐回到零附近。若求解失败，应阅读最先导致失败的错误，不要继续绘制旧解。

## C — 绘图、求值并回答模型 A 的问题

### 步骤 22 — 绘制出口速度

**位置:** 右键选择 `Results → 1D Plot Group`；再右键单击新建绘图组 → **Global**。

**输入:** 将组的 Label 设为 `A outlet speed`。选择 Study 1 / Solution 1 对应的数据集。在 Global 的 y-Axis Data 表中输入 `c.U`，Unit 为 `m/s`，Description 为 `Outward outlet speed`。在 x-Axis Data 中使用 **Time** 作为横轴来源；如果可选，将时间单位设为 `us`。否则保留秒，并按秒读取坐标轴。单击 **Plot**。

**检查:** 速度从零开始，在约 **15.3761 m/s** 达到峰值，随后衰减至零附近。这些标量数据不应使用 Surface 或 Volume 绘图。

### 步骤 23 — 分别绘制各类压力输出

**位置:** 再添加一个 `1D Plot Group → Global`。

**输入:** 将 Label 设为 `A pressure definitions`。使用相同的数据集和时间横轴，输入：

| 表达式 | 单位 | 说明 |
|---|---|---|
| `c.pb-pInf` | `kPa` | 腔室压力源超压 |
| `c.qJet` | `kPa` | 出口动压尺度 |
| `pInf` | `kPa` | 环境绝对压力参考值 |

**检查:** 初始源超压约为 **279.632 kPa**；出口最大动压约为 **118.212 kPa**。腔室绝对压力为 `c.pb`，其中包含环境压力。动压是出口处的动能尺度，并不计算靶面冲击峰值压力。

### 步骤 24 — 绘制能量收支

**位置:** 再添加一个 `1D Plot Group → Global`，将 Label 设为 `A energy accounting`。

**输入:** 将下列无量纲量对时间绘图，Unit 均设为 `1`：

| 表达式 | 含义 |
|---|---|
| `c.Kjet/E0` | 有效液柱运动中储存的能量 |
| `c.Eout/E0` | 实际随排液排出的动能 |
| `c.Esurf/E0` | 恒定弯月面载荷对照模型所做的功 |
| `c.Edis/E0` | 累积不可逆损耗 |
| `c.energyResidual` | 归一化第一定律残差 |

**检查:** `Eout` 在向外排出过程中增加，而液柱储存动能先增大后减小。过程末端，较低的 `Kjet` 可以与显著的排出动能同时存在。残差保持在零附近。尚未分配到这四个去向的能量，对应压力源剩余可用功。

### 步骤 25 — 创建完整时间历程表

**位置:** 右键选择 `Results → Derived Values → Global Evaluation`。

**输入:** 将节点 Label 设为 `A complete first-ejection history`。选择 Study 1 的解数据集，并设置 **Time selection = All**。保持 **Data Series Operation → Transformation = None**。输入下面完整的表达式表，并单击 **Evaluate**。[global_evaluation.tsv](resources/gui/global_evaluation.tsv) 是带表头的复制粘贴参考文件。

**检查:** 获得覆盖已求解过程的多行时间数据，而不是单个最大值，也不是假定的 100 µs 末端值。排出量各列与液柱储存动能及动量分别列出。

| 表达式 | 单位 | 说明 |
| --- | --- | --- |
| `t` | `s` | 初始化后的时间 |
| `c.x` | `m` | 排出体积 / 出口面积 |
| `c.U` | `m/s` | 出口向外速度 |
| `c.R` | `m` | 腔壁半径 |
| `c.Uw` | `m/s` | 腔壁扩张速度 |
| `c.Vg` | `m^3` | 气体压力源体积 |
| `c.pb-pInf` | `Pa` | 源表压 |
| `c.pEl` | `Pa` | 凝胶弹性压力 |
| `c.pRes` | `Pa` | 凝胶弹性与黏性阻力之和 |
| `c.Fconf` | `N` | 弹性半球合力 |
| `c.qJet` | `Pa` | 出口动压尺度 |
| `c.Ijet` | `N*s` | 有效液柱动量 |
| `c.Fflux` | `N` | 动量通量尺度 |
| `c.Kjet` | `J` | 液柱储存动能 |
| `c.Kgel` | `J` | 凝胶径向动能 |
| `c.Wgel` | `J` | 凝胶弹性功 |
| `c.Esurf` | `J` | 恒定弯月面载荷所做的功 |
| `c.Edis` | `J` | 不可逆损耗 |
| `c.energyResidual` | `1` | 归一化能量残差 |
| `c.stroke` | `1` | 已用液体存量的比例 |
| `c.stretch` | `1` | 内腔壁伸长比 |
| `c.Mjet` | `1` | 液体马赫数诊断量 |
| `c.Mwall` | `1` | 腔壁马赫数诊断量 |
| `c.communication` | `1` | 压力均衡传播筛选量 |
| `c.acc` | `m/s^2` | 出口加速度 |
| `c.wallAcc` | `m/s^2` | 腔壁加速度 |
| `c.pArrestBound` | `Pa` | 声明的平均制动压力上界 |
| `c.Eout` | `J` | 实际排出动能 |
| `c.Iout` | `N*s` | 实际轴向排出冲量 |
| `c.Mout` | `kg` | 实际排出液体质量 |

### 步骤 26 — 正确计算时间历程最大值

**位置:** 单独添加一个 `Derived Values → Global Evaluation` 节点。

**输入:** 将 Label 设为 `A temporal maxima`。Dataset = Study 1 的解；Time selection = All；**Data Series Operation → Transformation = Maximum**。输入下列表达式并执行 Evaluate。如果 Data Series Operation 处于折叠状态，先将其展开。

| 表达式 | 单位 | 基准目标值 |
|---|---|---|
| `c.U` | `m/s` | 约 15.37608 |
| `c.pb-pInf` | `kPa` | 约 279.63163 |
| `c.qJet` | `kPa` | 约 118.2119 |
| `abs(c.energyResidual)` | `1` | 小于 `1e-6` |
| `c.communication` | `1` | 小于 `0.1` |
| `c.stroke` | `1` | 不超过 `1`，允许数值容差 |

**检查:** 这些值是所列各标量随时间的最大值，不是空间最大值。源压力达到最大值的时刻，不一定与速度达到最大值的时刻相同。

### 步骤 27 — 计算实际末端输出

**位置:** 再添加一个 `Global Evaluation`，将 Label 设为 `A endpoint output`。

**输入:** Dataset = Study 1 的解；**Time selection = Last**；**Transformation = None**。输入 `t`、`c.Eout`、`c.Iout`、`c.Mout`、`c.x`、`c.U` 和 `c.energyResidual`，单位使用下表所列值。

| 表达式 | 单位 | 已验收的最后储存值 |
| --- | --- | --- |
| `t` | `us` | 33.8850 |
| `c.Eout` | `nJ` | 1.391345448 |
| `c.Iout` | `N*s` | 2.270809686e-10 |
| `c.Mout` | `ng` | 20.9678882 |
| `c.x` | `um` | 266.9714446 |
| `c.U` | `m/s` | 0.0001702102 |
| `c.energyResidual` | `1` | -1.0350e-10 |

**检查:** Last 表示本次因停止条件而终止的解中，最后储存的时刻，约为 33.885 µs；它不是标称的 100 µs 结束时刻。Stop Condition 在离散求解步上检查，因此精确的过零时刻与最后储存行略有差异。比较排出量时，应统一使用这一末端约定。

### 步骤 28 — 验收并保存基准模型

**位置:** 刚刚创建的曲线、最大值表和末端表。

**操作:** 检查初始液体与腔壁速度为零，气体体积和绝对压力为正，报告的整个过程均为向外速度，归一化残差小于 `1e-6`，压力均衡传播比小于 `0.1`，两个马赫数诊断量均小于 `0.1`，且已用液体存量不超过有限存量上限。检查停止原因。然后保存为 `practice/A_baseline_my_rebuild.mph`。

**检查:** 基准峰值与 15.37608 m/s 一致，末端排出动能约为 1.391345 nJ。这些检查验证的是所声明对照模型的实现，不能用于标定 PFC 状态方程或激光能量转换。

### 步骤 29 — 通过绝对压力选择压力源可用功

**位置:** `Global Definitions → Parameters 1`。

**操作:** 对于所采样的压力源可用功，使用下表绝对压力。这些压力是在相同的 `Rg0`、`kap` 和 `pInf` 下，通过反解有限绝热可用功关系得到的。修改 `p0`，保留 `E0` 表达式。比较压力源可用功时，其余输入保持不变。

| 可用功 | 绝对压力 p0 — 原样输入 |
| --- | --- |
| 0.5 nJ | `220113.1907789512[Pa]` |
| 2 nJ | `379631.6312499268[Pa]` |
| 5 nJ | `612212.3087264621[Pa]` |

**检查:** `E0` 的 Value 列应求值得到目标可用功。如果改变压力源半径、环境压力或绝热指数，应使用 [MODEL_SPEC.md](MODEL_SPEC.md) 中的步骤 2，或 [reference.py](scripts/reference.py) 中的 `source_pressure` 重新计算这一映射。此时，上述三组压力表不再适用。

### 步骤 30 — 复现九工况的条件包络

**位置:** Parameters、Study 1 的 Compute，以及 `A temporal maxima`。

**操作:** 对下面试算表的每一行执行完整流程：设置 `p0` 和 `a`；提交两个单元格；核对 `E0`；从初始值重新计算 Study 1；针对新计算的数据集，对最大值和末端节点执行 Evaluate；记录峰值速度、两种已定义压力、排出动能、排出冲量及有效性诊断量。如果需要保留该解，使用独立的练习文件名保存每次试算。对每一行都重复完整流程。

| 工况 | E0 (nJ) | p0 | a | 预期峰值 U (m/s) |
| --- | --- | --- | --- | --- |
| A_E0.5nJ_a3um | 0.5 | `220113.1907789512[Pa]` | `3[um]` | 8.560117 |
| A_E0.5nJ_a5um | 0.5 | `220113.1907789512[Pa]` | `5[um]` | 8.068346 |
| A_E0.5nJ_a10um | 0.5 | `220113.1907789512[Pa]` | `10[um]` | 5.860144 |
| A_E2nJ_a3um | 2 | `379631.6312499268[Pa]` | `3[um]` | 17.286430 |
| A_E2nJ_a5um | 2 | `379631.6312499268[Pa]` | `5[um]` | 15.376078 |
| A_E2nJ_a10um | 2 | `379631.6312499268[Pa]` | `10[um]` | 11.237538 |
| A_E5nJ_a3um | 5 | `612212.3087264621[Pa]` | `3[um]` | 25.279819 |
| A_E5nJ_a5um | 5 | `612212.3087264621[Pa]` | `5[um]` | 22.350558 |
| A_E5nJ_a10um | 5 | `612212.3087264621[Pa]` | `10[um]` | 16.601975 |

**检查:** 所采样工况中的最高速度约为 **25.27982 m/s**，对应 5 nJ 可用功和 3 µm 出口半径。其源超压约为 512.212 kPa，动压尺度约为 319.535 kPa。该最大值以所声明的工况族为条件；提高可用功或改变结构，会改变工况族。

### 步骤 31 — 解读压力与速度上限

**位置:** 参数值 `Uceiling`、`qCeiling` 以及九工况结果。

**操作:** 逐个工况将求解得到的最大速度与 `Uceiling` 比较，将求解得到的动压与 `qCeiling` 比较。这些上界将全部可用功分配给液柱运动，因此大于实际达到的峰值。使用所附[条件速度包络图](assets/conditional_velocity_envelope.png)查看已验收的比较结果。

**检查:** 基准工况仅由能量确定的速度上界约为 **31.9154 m/s**，而求解得到的速度为 15.3761 m/s。将腔室压力、出口动压和仅由能量确定的上界分别记录在不同列中。本模型不预测已排除的激活瞬态过程和靶面冲击压力。

## D — 加入水凝胶约束，建立模型 B

### 步骤 32 — 返回基准模型，并另存模型 B 副本

**位置：** `File → Open`，然后选择 `File → Save As`。

**操作：** 打开步骤 28 中保存的 `A_baseline_my_rebuild.mph`。将其另存为独立副本 `practice/B_01_from_A.mph`。把组件的 Label 改为 `c: Model B practice`；其 Name 保持为 `c`。

**检查：** 当前编辑的是模型 B 的练习副本。确认 `p0=379631.6312499547[Pa]`、`a=5[um]` 或其以米表示的等价值、`G=20[kPa]`、`etaG=0.010[Pa*s]`、`rhoG=1000[kg/m^3]`、`Kloss=0`、`Rloss=0[Pa*s/m]`、`outletOpen=1`。这些是相互匹配的基准输入。如果在另一个空白模型中建立 B，[B_parameters_import.txt](resources/gui/B_parameters_import.txt) 包含完整的基准参数表。

### 步骤 33 — 替换九个与凝胶有关的表达式

**位置：** `Component c → Definitions → Source, outlet and accounting`。

**操作：** 替换下面列出的九个现有行。保留模型 A 的另外 24 个表达式。可使用 [B_variables_patch_import.txt](resources/gui/B_variables_patch_import.txt) 更新这些名称对应的表达式，也可以手动编辑其 Expression 单元格。[B_variables_import.txt](resources/gui/B_variables_import.txt) 包含全部 33 行 B 变量，适用于新建的 Variables 表。

**检查：** 现在气体体积同时取决于排出的液体和扩张的腔壁半径。`pEl`、`Wgel`、`Kgel` 以及凝胶损耗均已启用。`rr` 和 `ww` 将在下一张步骤卡中得到定义。

| 名称 | 表达式 — 按原样输入 | 单位 | 含义 |
| --- | --- | --- | --- |
| `R` | `Rc0*rr` | `m` | 腔壁半径，m |
| `Uw` | `Us*ww` | `m/s` | 腔壁扩张速度，m/s |
| `pEl` | `G/2*(5-4*Rc0/R-(Rc0/R)^4)` | `Pa` | 球形凝胶腔壁处的弹性阻力压力 |
| `pRes` | `pEl+4*etaG*Uw/R` | `Pa` | 凝胶腔壁的弹性与黏性阻力压力之和 |
| `Wgel` | `2*pi*G*(5*R^3/3-2*Rc0*R^2+Rc0^4/R-2*Rc0^3/3)` | `J` | 凝胶中可恢复的弹性功 |
| `Kgel` | `2*pi*rhoG*R^3*Uw^2` | `J` | 球形凝胶的径向动能 |
| `wallAcc` | `((pb-pInf-pRes)/rhoG-1.5*Uw^2)/R` | `m/s^2` | 球形凝胶腔壁的加速度 |
| `Pdis` | `outletOpen*A*(Rloss*U^2+rho*Kloss*abs(U)^3/2)+16*pi*etaG*R*Uw^2` | `W` | 非负的出口与凝胶不可逆损耗功率 |
| `communication` | `max(L,2*Rc0)/cL*kap*abs(Vdot)/Vg` | `1` | 压力变化的均衡传播比；不求解传播场 |

### 步骤 34 — 输入模型 B 的七行方程

**位置：** 现有的 `Global Equations 1` 表。

**操作：** 将五行表替换为下面完整的七行表；两个量的设置均保留为 Dimensionless。`rr=R/Rc0` 是腔壁半径比，`ww=Uw/Us` 是归一化腔壁速度。其余状态量的含义仍与步骤 13 相同。将 `rr` 的初始值设为 **1**。另外六个状态量的初始值以及每个 `ut_0` 条目均为零。[B_equations.tsv](resources/gui/B_equations.tsv) 是带表头的复制／粘贴参考文件。

**检查：** 名称依次为 `qq`、`vv`、`rr`、`ww`、`dd`、`ee`、`ii`，共七行。把 `rr` 的初始值设为零会产生零半径奇点，这是错误的。

| 名称 | f(u,ut,utt,t) — 按原样输入 | u_0 | ut_0 |
| --- | --- | --- | --- |
| `qq` | `tau*(qqt-outletOpen*U/Lbudget)` | `0` | `0` |
| `vv` | `tau*(vvt-acc/Us)` | `0` | `0` |
| `rr` | `tau*(rrt-Uw/Rc0)` | `1` | `0` |
| `ww` | `tau*(wwt-wallAcc/Us)` | `0` | `0` |
| `dd` | `tau*(ddt-Pdis/E0)` | `0` | `0` |
| `ee` | `tau*(eet-Pout/E0)` | `0` | `0` |
| `ii` | `tau*(iit-outletOpen*rho*A*U^2/Iscale)` | `0` | `0` |

### 步骤 35 — 重新核对继承的研究与求解器

**位置：** `Study 1 → Time Dependent`，然后选择 `Solution 1 → Time-Dependent Solver 1`。

**操作：** 两个节点均保留 1 ns 输出时间列表；所有字段与步骤 18 的设置一致。初始状态必须来自更新后的物理场方程表。现有的 `ODE1` 方程组现在包含七个状态量；不要手动把旧的 A 末态解选作新的初始状态。

**检查：** 求解器中启用的 Global ODEs and DAEs 接口只有一个。Consistent initialization 仍为 Off。如果编辑物理场后重新生成默认求解器，计算前需重新输入步骤 18 的设置，并重新建立步骤 19 的四条停止规则。

### 步骤 36 — 检查模型 B 的停止逻辑

**位置：** 继承的 `Time-Dependent Solver 1 → Stop Condition`。

**操作：** 对照步骤 19 核对全部四行。每行均保持 Active，并设为 Negative。第一个表达式仍必须是 `if(outletOpen>0.5,c.U,c.Uw)`。

**检查：** 开放出口的 B 在出口速度首次回落至零时结束，密封的 B 则在腔壁速度首次回落至零时结束。20% 拉伸规则是预先声明的适用性筛查条件，不是实测的凝胶破裂阈值。停止警告会说明保留的是哪一次运动过程。

### 步骤 37 — 计算开放出口的凝胶基准模型

**位置：** `Study 1 → Compute`。

**操作：** 保存为 `practice/B_02_ready_to_solve.mph`，然后在 `outletOpen=1` 时执行 Compute。完成后，如有需要，在继承的绘图与求值节点中重新选择当前的 Study 1 数据集。将这些节点的标签改为含 B 的名称，以便与已保存的 A 练习文件中的结果区分。

**检查：** 出口峰值速度约为 **1.62538 m/s**，保留的向外排出过程在约 **1.937 µs** 时结束。这些结果与 A 不同，因为腔壁扩张和凝胶损耗为源可用功增加了其他去向。

### 步骤 38 — 绘制腔壁运动与凝胶阻力

**位置：** 添加 `Results → 1D Plot Group → Global` 节点。

**输入：** 在一个图组中绘制 `c.stretch`，Unit 为 `1`；在另一个图组中绘制 `c.Uw`，Unit 为 `m/s`。在一个压力图组中绘制 `c.pEl`、`c.pRes`、`c.pb-pInf` 和 `c.qJet`，单位全部为 `kPa`。使用当前 B 数据集，以 Time 为横轴。

**检查：** 初始拉伸比为 1，初始腔壁速度为零。`pEl` 表示弹性阻力压力，`pRes` 还包含黏性阻力压力。腔室驱动压力也用于克服腔壁惯性，因此不能与任一阻力曲线互换。基准模型的最大弹性阻力压力约为 **9.143 kPa**。

### 步骤 39 — 绘制定义明确的约束力

**位置：** 再添加一个 `1D Plot Group → Global`，标签设为 `B hemisphere resistance`。

**输入：** 绘制 `c.Fconf`，Unit 为 `uN`。该量定义为一个半球上的弹性腔壁牵引力沿轴向的合力。也可加入 `pi*c.R^2*c.pRes`，单位同样为 `uN`，标签设为 `Elastic plus viscous hemisphere resistance`。

**检查：** 最大弹性力约为 **33.77 µN**。这是明确定义的半球合力。球对称的腔壁牵引力在整个球面上的净矢量合力为零；该数值不是实测的靶面作用力，也不是通过空间求解得到的平面层作用力。

### 步骤 40 — 求取模型 B 的最大值

**位置：** 复制或创建一个 `Global Evaluation` 节点；标签设为 `B temporal maxima`。

**输入：** 使用当前 B 数据集；Time selection 设为 All；Transformation 设为 Maximum。求值：`c.U`，单位 `m/s`；`c.qJet` 和 `c.pEl`，单位 `kPa`；`c.Fconf`，单位 `uN`；`c.stretch`、`c.communication`、两个马赫数诊断量，以及 `abs(c.energyResidual)`，单位均为 `1`。

**检查：** 每个最大值分别来自该量自身的时间历程。如果腔壁半径已经变化，不要把最大压力乘以初始面积来计算约束力；应对完整的 `Fconf` 表达式求值。接受输出结果时仍必须包含适用性检查。

### 步骤 41 — 求取模型 B 的排出输出

**位置：** `Global Evaluation`，标签设为 `B endpoint output`。

**输入：** 使用当前 B 数据集；**Time selection Last**；**Transformation None**。使用与步骤 27 相同的末端表达式列表。

| 表达式 | 单位 | 已通过验证的最后存储值 |
| --- | --- | --- |
| `t` | `us` | 1.9370 |
| `c.Eout` | `nJ` | 0.000136295 |
| `c.Iout` | `N*s` | 1.982567108e-13 |
| `c.Mout` | `ng` | 0.1561203 |
| `c.x` | `um` | 1.9877850 |
| `c.U` | `m/s` | 0.0007545839 |
| `c.energyResidual` | `1` | -1.2237e-07 |

**检查：** 很小的排出动能对应 B 中完整但短暂的排出过程。不能用 `Kjet` 代替这项排出动能，也不能用 `Ijet` 代替排出冲量。仅有速度峰值无法得到全过程积分输出。

### 步骤 42 — 计算相互匹配的传导比

**位置：** 在 B 模型中再添加两个 Global Evaluation 节点。

**操作：** 首先保留步骤 26–27 中与 B 匹配的 A 峰值和末端值。对于本基准，以下表达式把这些已验证的 A 值作为明确的分母。如果改变源状态或几何参数，就必须把每个分母替换为新匹配的 A 对照模型中对应的数值。

| 表达式（单位 1） | Time selection → Transformation | 含义 |
| --- | --- | --- |
| `c.U/(15.376077990105143[m/s])` | All → Maximum | 峰值速度比 |
| `c.qJet/(118211.88717889792[Pa])` | All → Maximum | 峰值动压比 |
| `c.Eout/(1.3913454479823484e-09[J])` | Last → None | 排出动能比 |
| `c.Iout/(2.2708096862657052e-10[N*s])` | Last → None | 排出冲量比 |

**检查：** 峰值速度／动压比使用 All times + Maximum；排出动能／冲量比使用 Last + None。将无量纲比值乘以 100，即可报告百分比。预期基准结果约为：**速度 10.5709%**、**动压 1.1174%**、**排出动能 0.00980%**、**排出冲量 0.08731%**。在密度相同时，只有动压比等于速度比的平方。对整个排出过程积分得到的能量比和冲量比取决于完整的排出时间历程。

### 步骤 43 — 求解密封水凝胶对照模型

**位置：** Parameters，然后执行 Study 1 的 Compute。

**操作：** 将开放出口的基准模型保存为 `practice/B_open_baseline_my_rebuild.mph`。另存独立副本 `practice/B_sealed_control_my_rebuild.mph`。仅将 `outletOpen` 改为 `0`，然后从物理场初始值重新计算。保留第一个停止表达式中的条件切换。

**检查：** `U`、`x`、`Mout`、`Eout` 和 `Iout` 在整个过程中保持为零。腔壁可以运动，气体压力也可以变化。密封对照的最大弹性压力约为 **9.6259 kPa**，最大拉伸比约为 **1.15252**，末端时间约为 **2.452 µs**。密封腔壁的响应不是外部液体射流。

### 步骤 44 — 运行凝胶与损耗敏感性对照

**位置：** 重新打开 `B_open_baseline_my_rebuild.mph`；每次试算均编辑 Parameters 并执行 Compute。

**操作：** 使用下面的七案例表。对于每一行，恢复其他基准值，提交已修改的单元格，从相同的初始状态重新计算，并对相同的最大值／末端值／适用性筛查节点执行 Evaluate。以不同的练习文件名保存各次输出。可使用已验证的[原生案例登记表](data/native_case_register.json) 对照完整输出。

| 案例 | G | etaG | Kloss | outletOpen | 预期峰值 U（m/s） |
| --- | --- | --- | --- | --- | --- |
| B_open_baseline | `20[kPa]` | `0.01[Pa*s]` | `0.0` | `1` | 1.625385 |
| B_sealed_control | `20[kPa]` | `0.01[Pa*s]` | `0.0` | `0` | 0.000000 |
| B_open_loss_K1 | `20[kPa]` | `0.01[Pa*s]` | `1` | `1` | 1.615803 |
| B_open_G5kPa | `5[kPa]` | `0.01[Pa*s]` | `0.0` | `1` | 1.624346 |
| B_open_G100kPa | `100[kPa]` | `0.01[Pa*s]` | `0.0` | `1` | 1.631024 |
| B_open_eta0 | `20[kPa]` | `0[Pa*s]` | `0.0` | `1` | 1.619889 |
| B_open_eta0p1 | `20[kPa]` | `0.1[Pa*s]` | `0.0` | `1` | 1.677217 |

**检查：** 每次试算仍仅取首次事件结果。改变模量或黏度可以同时改变峰值和排出持续时间；描述其影响前，先检查能量分配和停止原因。不要认为某一种刚度变化趋势就证明了普适的传导规律。

## E — 验证、导出并保存结果

### 步骤 45 — 执行 2 ns / 1 ns 分辨率检查

**位置：** Time Dependent 研究与 Time-Dependent Solver 1。

**操作：** 在基准副本中，将两个时间列表均设为 `range(0,2[ns],100[us])`；执行 Compute，记录 U 峰值、最后的 Eout 和最后的 Iout。再将两个列表均改回 `range(0,1[ns],100[us])`；执行 Compute，并再次记录这些量。保持容差、输入和停止规则不变。以 1 ns 的数值为分母，比较相对变化。

**检查：** 已验证的峰值速度相对变化约为：A 的 `1.4e-8`，开放出口 B 的 `9.5e-7`。重新建立的基准模型应得到低于 `1e-4` 的峰值变化。末端量可能随离散的停止时间而变化，也要检查这些变化。最终保留 1 ns 基准。只改变绘图插值并不构成求解器分辨率测试。

### 步骤 46 — 应用完整验收清单

**位置：** 对 All times 使用 Maximum 或 Minimum 的 Global Evaluation，以及末端结果表。

**操作：** 分别检查下列条件。如果某项物理适用性筛查未通过，应记录该失效范围，而不能把对应输出报告为已接受的预测。

| 检查项 | 表达式／方法 | 本组对照的验收条件 |
|---|---|---|
| 初始值 | 第一个存储行 | U 和 Uw 为零；B 的拉伸比为 1 |
| 热力学第一定律 | `abs(c.energyResidual)` 的最大值 | 低于 `1e-6` |
| 气体体积与绝对压力 | `c.Vg` 的最小值、`c.pb` 的最小值 | 两者均为正 |
| 有限液体存量 | `c.stroke` 的最大值 | 在数值容差内不超过 1 |
| 腔壁拉伸比 | `c.stretch` 的最大值 | 不超过预先声明的 1.2 筛查界限 |
| 液体／腔壁马赫数 | `c.Mjet`、`c.Mwall` 的最大值 | 低于 0.1 |
| 均匀压力适用范围 | `c.communication` 的最大值 | 低于 0.1 |
| 向外排出过程 | 检查 U 和停止说明 | 不包含后续回弹 |
| 有限输出 | 最后的 Eout、Iout 和 Mout | 非负；密封输出为零 |
| 实现一致性 | 对照已声明的输入和输出表 | 与已验证案例及数值审计一致 |

**检查：** 随附的 17 案例 [NUMERICAL_AUDIT.json](verification/NUMERICAL_AUDIT.json) 中，最大的归一化第一定律残差约为 `1.26e-7`，原生求解与独立参考解之间最大的归一化时间曲线差异约为 `1.15e-4`。这些是实现检查；材料／相态标定需另行完成。

### 步骤 47 — 导出完整时间历程与汇总表

**位置：** 各个 Global Evaluation 生成的 Results 表。

**操作：** 使用 All times 和 Transformation None 对完整时间历程节点求值。在生成的表格工具栏中使用 Save/Export，将 CSV 保存到 `practice/`，例如 `A_baseline_GUI_history.csv` 或 `B_open_GUI_history.csv`。最大值表与末端表应分别导出，以保持其含义清楚。表格说明中应包含单位，或者保留 COMSOL 自带单位的表头。

**检查：** 时间历程 CSV 有许多时间行，并包含排出动能、冲量和质量。最大值 CSV 不是时间历程。确认末端 CSV 报告的是实际停止时间。原生求解与独立对照 CSV 已包含在 `data/` 中。

### 步骤 48 — 保存最终练习副本

**位置：** `File → Save As`。

**操作：** 将 A 基准、B 开放出口基准和 B 密封对照保存为分别命名的练习 MPH 文件。每个已求解案例应连同匹配的输入值和结果表一起保存。如果希望 B 的主要练习文件是开放出口基准，应在敏感性试算后恢复到该基准。

**检查：** 重新打开每个练习文件，核对标题、输入值和存储的绘图数据。两个已保存基准均使用 1 ns 输出间隔。你自己的练习文件放在 `practice/` 中；交付 ZIP 不包含该文件夹。

### 步骤 49 — 检查交付的原生模型

**位置：** `File → Open`，选择 `models/` 中任一原生文件。

**操作：** 检查 Parameters 1、组件的 Variables 节点、Global Equations 1、Time-Dependent Solver 1、其 Stop Condition，以及已保存的结果图／表。交付文件中的接口标签描述的是保留的运动／收支统计状态量；它们可能与向导的默认标题不同。通过 Global Equations 1 识别该接口。

**检查：** A 有五行状态量，B 有七行。两者均有 32 个参数、33 个变量、一个 Global Equations 接口及存储解。已通过验收的基准文件已在新的 COMSOL 进程中重新载入，也已从解压后的包中重新载入；报告中链接了数值与可移植性证据。

### 步骤 50 — 必要时使用可复现的脚本流程

**位置：** 在整个自包含文件夹的独立工作副本中打开 Windows PowerShell。

**操作：** 安装 COMSOL 6.4 后运行：

```powershell
.\Run-Rebuild.ps1
.\Run-Verify.ps1
.\Run-CheckGuide.ps1
python -m pip install -r requirements.txt
python scripts/reference.py
python scripts/verify_results.py
python scripts/build_guide.py
```

`Run-Rebuild.ps1` 建立 17 案例组，并写入原生文件和时间历程。`Run-Verify.ps1` 执行新进程检查和 2 ns / 1 ns 检查，并保存采用更细输出时间间隔的基准解。Python 参考程序独立积分有量纲方程。由于这些命令会替换生成的模型／数据，请在工作副本中重建。如果 COMSOL 安装在其他位置，请在 PowerShell 运行脚本中使用 `-ComsolBin`。

**检查：** 原生批处理日志必须显示运行完成，且没有内部 Java 错误；仅检查 shell 退出码并不足够。求解器错误详情位于 `build/`。此流程复现的方程与 GUI 表格中的方程相同。

## F — 修正常见错误，并准确报告结论

### 步骤 51 — 诊断首个故障

**位置：** Messages/Log 中首个构成原因的错误或异常输出，以及其中指出的节点。

**操作：** 改动其他无关设置前，先使用下面对应的具体修正方法。

| 现象 | 检查对象 | 修正方法 |
|---|---|---|
| 无法识别 `c.U` | 组件 Name | 将 Name 设为 c，或在全部位置一致地替换命名空间 |
| 无法识别 `qq`、`rr` 或其导数 | 方程 Name 列 | 准确输入五个／七个名称；完成 B 的新增行 |
| 出现六／八个方程，而非五／七个 | 占位行 | 删除练习表中未使用的默认行 |
| 残差单位错误 | 方程量设置与 `tau` 因子 | 两个量均设为 Dimensionless；保留每个完整残差表达式 |
| 源可用功错误 | `p0`、`pInf`、单位 | 使用绝对压力 p0；保留 E0 的派生表达式 |
| B 出现零半径奇点 | 初始 `rr` | 将 rr 设为 1，而不是零 |
| 初始速度非零 | 初始化与复用的解 | 初始化设为 Off；从物理场初始值开始 |
| 在零时刻立即停止 | Stop if 列 | 全部四行均使用 Negative (<0)，而不是默认的 Boolean True |
| 出现后续反向运动或重复过程 | Stop Condition 缺失／禁用 | 恢复首次向外运动返回规则和其他所有行 |
| 能量残差漂移 | 加速度与输出项 | 保留流出的动能水头和 Eout；使用完整的源体积 |
| 得到错误的巨大“射流能量” | 选取的结果表达式 | 使用 Eout，而非存储的 Kjet |
| 排出冲量错误 | 选取的结果表达式 | 使用 Iout，而非液柱动量 Ijet |
| 求解 B 后仍显示旧 A 结果 | 结果 Dataset | 选择当前 B 解，重新执行 Evaluate |
| 空间图为空 | 绘图类型 | 添加 1D Plot Group → Global |
| 误以为“Last”输出位于 100 µs | 实际存储时间 | 使用 Last 对 t 求值；停止条件会截断所请求的时间列表 |
| 凝胶试算超出物理筛查条件 | 均衡传播／拉伸比／马赫数 | 将其归类为超出已声明的适用范围 |

**检查：** 只有在修正了相关输入或节点后才重新计算。如果输入发生变化，应重新运行守恒与适用性检查；此前已接受的表格可能不再适用。

### 步骤 52 — 将对照模型与实验相联系

**位置：** 实验记录和 Parameters 表。

**操作：** 提供有证据支持的激活后气体／相体积及压力—体积路径，或有依据的可用功估计；实际连通液体体积与出口有效流体惯性；载液性质；相关速率下的凝胶模量／黏度；以及通道是否已存在。条件允许时，在同一次激光激发中测量空腔体积、腔壁运动以及排出速度／质量。利用这些数据更新对照模型，再重复完整验收流程。

**检查：** 5 nJ 可用功输入不自动等同于 5 nJ 光学脉冲。球形凝胶对照不是精确的平面水凝胶层模型。完整密封凝胶中不会预测出穿透凝胶的外部射流。每次报告最大值或传导比时，都应同时保留这些结构与校准说明。

### 步骤 53 — 完成操作指南

**位置：** 您保存的练习模型文件与输出表。

**检查是否能够独立复现：** 15.3761 m/s 的 A 基准；25.2798 m/s 的最大已采样案例；1.62538 m/s 的开放出口凝胶基准；其 9.143 kPa 弹性阻力压力和 33.77 µN 半球力；相互匹配的排出动能／冲量比；以及密封对照中为零的排出输出。核验停止规则、数值检查和物理适用性筛查，而不应只核对峰值。

**完成记录：** 记录软件版本、输入案例、源状态假设、实际存储的末端时间、峰值定义、排出输出定义、最大守恒残差、均衡传播／马赫数／拉伸比检查以及分辨率加密对照。[项目日志](WORK_LOG.md) 和[结果报告](RESULTS.md) 提供了随附对照模型已通过验收的记录。

## 参考文献与配套文件

本次参考的 [M1 课程](https://pfgaophilip.github.io/cavitation-course/comsol/lessons/M1.html) 提供了循序渐进的界面说明格式。本指南的参数、变量和方程表取自当前两个已求解的原生文件，并非 M1 中其他模型的建模配方。归档的 HTML／文本位于 `sources/reference-lesson/`；本指南的原生模型元数据位于 `sources/native-guide-evidence/`。

- [完整推导与假设](MODEL_SPEC.md) · [可编辑 LaTeX 源文件](THEORY_DERIVATION.tex) · [离线结果](index.html)。
- [模型 A](models/Model_A_Finite_Energy_Pressure_Jet.mph) · [模型 B](models/Model_B_Hydrogel_Confinement_Jet_Transmission.mph)。
- [COMSOL 模型向导](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_environment.18.43.html)、[全局方程](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_equationbased.32.089.html)、[时间求解器](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_solver.36.139.html)、[停止条件](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_solver.36.212.html)。

验证范围：已将表格与保存的原生方程核对；已使用 COMSOL 原生 API 检查参数／变量导入及 A 到 B 的转换；目标结果来自已通过验收的求解对照模型。插图均为示意图。不宣称已完成实时 Desktop 界面逐项点击验证。
