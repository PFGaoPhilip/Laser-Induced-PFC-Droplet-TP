# COMSOL 6.4 逐步操作：两个简洁的单脉冲模型

在本指南旁打开 COMSOL。逐步完成操作。操作路线是：**空白 0D 模型 → 求解模型 A → 水凝胶模型 B → 密封对照 → 经验证的输出表格**。每步给出节点、输入和检查项。检查点保存于练习文件夹。

模型 A 计算有限源的压力和出口速率。模型 B 加入球形凝胶约束、排出能量及冲量。标称 10 ns 脉冲提供激活后初始数据。零时刻位于压力均衡之后。后续无驱动。

**声明的对照假设。** 压力源为封闭的绝热理想气体，压力均匀，绝热指数恒定且大于一，可用功有限。载液密度和出口的有效流体惯性保持恒定。出口预先开放。恒定的弯月面入口压力是一项近似。模型 B 使用完整、不排水、不可压缩的新胡克凝胶，并加入 Kelvin–Voigt 损耗，将其近似为包围腔室的球形介质。初始机械速度为零，腔壁参考构形无应力，远场压力和出口端压力均为环境压力。液体向外运动和腔壁向外扩张的速度取正。后续回弹、相间交换、凝胶破裂和靶面冲击均不在本次首次向外排出过程的计算范围内。实际 PFC 和凝胶的性质需要标定。

推导、符号及有效性检查见 [MODEL_SPEC.md](MODEL_SPEC.md) 与[完整离线报告](index.html#theory)。下表用 COMSOL 语法表示这些方程。

![模型机制及定义的输出量](assets/guide-mechanisms.svg)

*机制示意图。模型 A 固定腔壁。模型 B 允许出口排液和腔壁扩张。两者均增加源体积。*

## A — 熟悉界面并建立练习模型

### 步骤 01 — 识别三个工作区域

**位置:** COMSOL Desktop。

**操作:** 找到左侧的 **Model Builder**（模型开发器）、中间显示所选节点设置的 **Settings**（设置），以及右侧用于绘图的 **Graphics**（图形）。Progress、Messages、Log 和 Results 表格通常位于下方。节点路径如 `Global Definitions → Parameters 1`，表示展开第一个节点并选中其子节点。右键操作会在鼠标所指节点下创建子节点。修改表格单元格后，按 Tab 或单击单元格外部，提交输入内容。

**检查:** 选中一个节点，确认 Settings 随之变化。

![COMSOL 工作区域](assets/guide-interface.svg)

*界面示意图。布局随窗口而变化。按节点名和字段名定位。*

### 步骤 02 — 新建模型

**位置:** `File → New → Model Wizard`。

**操作:** 打开 COMSOL Multiphysics 6.4。在 New 页面选择 Model Wizard。切换模型前保存已有工作。在本指南旁新建一个 `practice/` 文件夹，用于练习。后续提示保存时，可在 Save As 对话框中创建该文件夹。

**检查:** 向导显示 **Select Space Dimension**（选择空间维度）。

### 步骤 03 — 选择空间维度

**位置:** `Model Wizard → Select Space Dimension`。

**输入:** 选择 **0D**。

**检查:** 向导进入 Select Physics。未知量为时间相关标量。腔室和出口半径作为参数输入。此模型无需空间几何。

### 步骤 04 — 添加标量方程接口

**位置:** `Select Physics → Mathematics → ODE and DAE Interfaces → Global ODEs and DAEs`。

**操作:** 选择 Global ODEs and DAEs，并单击 **Add**。需要时搜索接口全名。添加一个接口。

**检查:** Added physics interfaces 中包含 Global ODEs and DAEs。该接口提供 Global Equations（全局方程）表。

**排错:** 清除搜索筛选条件，并确认已选择 0D。原生文件采用基础 COMSOL 许可证。凝胶力学以标量表达式输入。

### 步骤 05 — 添加瞬态研究

**位置:** `Model Wizard → Study → General Studies`。

**输入:** 选择 **Time Dependent**（瞬态），然后单击 **Done**。

**检查:** Model Builder 中包含一个 Component、Global ODEs and DAEs，以及 `Study 1 → Step 1: Time Dependent`。

### 步骤 06 — 设置组件命名空间

**位置:** 单击 `Component 1`。

**输入:** 将 **Name** 设为 `c`，将 **Label** 设为 `c: Model A practice`。保留 SI 单位制。Name 设置命名空间，如 `c.U`。Label 设置显示名称。

**检查:** 组件的 Name 为 `c`。Label 不改变命名空间。

**排错:** 如果 Name 仍为 `comp1`，现在就更正。下面所有结果表达式和停止表达式都使用 `c.` 前缀。参见[组件 Name 文档](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_modeling.19.007.html)。

### 步骤 07 — 保存第一个检查点

**位置:** `File → Save As`。

**输入:** 保存为 `practice/A_01_setup.mph`。之后使用 Ctrl+S。按下列阶段另存检查点。

**检查:** 标题栏显示你的练习文件名。`models/` 中已经验收的原生文件仍可用于对照。

## B — 输入模型 A 的全部参数与表达式

### 步骤 08 — 输入全部 32 个参数

**位置:** `Global Definitions → Parameters 1`。

**操作:** 输入下表的全部行，或单击表格下方的 **Load from File**，选择 [A_parameters_import.txt](resources/gui/A_parameters_import.txt)。该导入文件包含两列，以制表符分隔，不含表头。将其一次性导入参数表即可。参数说明见下表。如果手动输入，请严格保留每个名称的大小写以及单位外的方括号。

**检查:** 共计 32 个参数名，没有重复名称。表格尚未填完时，依赖关系可能暂时无法解析。应在全部行输入完成后再检查 Value 列。`p0` 为绝对压力，`E0` 是由该压力推得的表达式。

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

**原因:** `L` 定义液体惯性。`Lbudget` 定义连通液体最多能排出多少。二者含义不同。2 nJ 表示激活后的机械可用功，不是入射激光能量。`tauLaser=10[ns]` 记录短脉冲假设。它不是随时间变化的驱动函数，仅改变它不会改变本解。

**排错:** 可用功为负或平衡体积无效，通常表明压力或单位输入有误。使用提供的绝对压力 `p0`，不要用 279.632 kPa 的表压替换它。

### 步骤 10 — 创建 Variables 并输入压力源几何表达式

**位置:** 右键选择 `Component c → Definitions → Variables`。

**操作:** 将 Label 设为 `Source, outlet and accounting`。输入下面的前七行。也可以通过 **Load from File** 选择 [A_variables_import.txt](resources/gui/A_variables_import.txt)，一次导入完整的 33 行表格，再按步骤 10–12 检查三个分组。在此组件表内使用局部名称，不要在 Name 列添加 `c.`。

**检查:** 通过 `R=Rc0` 固定腔室半径。腔壁速度严格为 `0[m/s]`。气体体积包含已经排出的液体所对应的体积。在步骤 14 添加方程行后，`qq` 和 `vv` 才会获得定义。

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

**操作:** 如果手动输入，添加下面七行。模型 A 将凝胶相关项设为带单位的零。损耗表达式可用于后续敏感性对照。基准损耗输入为零。

**检查:** 液柱能量 `Kjet` 使用有效液柱惯性。它与下一步输入的排出动能 `Eout` 不同。弯月面功是所声明的恒定入口压力对照模型所做的功。本模型不求解自由表面的演变。

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

**输入方程之前明确状态量含义:** `qq=x/Lbudget`。`vv=U/Us`。`dd=Edis/E0`。`ee=Eout/E0`。`ii=Iout/Iscale`。这五个标量是求解未知量。Variables 节点提供代数表达式，并不增加独立未知量。

### 步骤 14 — 输入全部五行全局方程

**位置:** 步骤 13 的 Global Equations 表。

**操作:** 输入下表的每一行，包括两列初始值。表中的方程字段 `f(u,ut,utt,t)` 是由 COMSOL 设为零的残差。对于较长的行，选中该行并在表格下方编辑其字段。[A_equations.tsv](resources/gui/A_equations.tsv) 是带表头的复制粘贴参考文件。参数和变量节点中的 Load from File 按钮不能将它导入本方程表。

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

**操作:** 检查 `qqt`、`vvt`、`ddt`、`eet`、`iit`。它们是 COMSOL 的一阶时间导数名称：`vvt` 是 `vv` 的时间导数。不要输入 `vv*t`，后者表示乘法。初始值 `ut_0=0` 沿用已验收的设置。一阶方程负责计算随时间演变的导数。

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

**操作:** 展开 `Solver Configurations → Solution 1`，单击 **Time-Dependent Solver 1**。如果这些节点已经存在，直接展开即可。保留自动生成的 Dependent Variables 节点。它将 `ODE1` 方程组连接到求解器。

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

**检查:** 可见 BDF、Strict、`1e-9` 和初始化 Off。保留自动选定的初始步长、BDF 阶次及变量尺度。这些方程是一阶常微分方程。将初始化设为 Off 可保留指定的零初始速度。Strict 步进会到达所列时间，必要时还可采用额外内部步。参见[瞬态求解器文档](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_solver.36.139.html)。

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

**原因:** 第一行在首次向外速度回落并穿过零时停止。在密封情况下，它改为检查腔壁速度。其余各行限制液体存量、声明的伸长筛选阈值及马赫数筛选阈值。初始零速度不为负，因此基准计算能够启动。压力均衡传播的筛选阈值在步骤 28 求解完成后检查。它不是在线停止规则。参见[停止条件文档](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_solver.36.212.html)。

### 步骤 20 — 完成求解前检查

**位置:** Parameters、Variables、Global Equations、Time-Dependent 研究及其求解器。

**逐项检查:** 32 个参数。33 个变量。5 行方程。两个方程物理量均为 Dimensionless。全部状态初值为零。研究和求解器均使用 1 ns 时间列表。BDF Strict。一致初始化为 Off。四条已启用的 Negative 停止规则。Initial Values of Variables Solved For 必须来自物理场初始值，而不是此前的非零解。

**操作:** 保存检查点 `practice/A_02_ready_to_solve.mph`。如果未知变量消息提到 `comp1` 或 `c`，更正命名空间。如果提到 `qq` 或 `vv`，检查方程的 Name 列。

### 步骤 21 — 计算首次向外排出过程

**位置:** `Study 1` 工具栏，或右键选择 `Study 1 → Compute`。

**操作:** 单击 Compute，观察 Progress 和 Log。求解完成后再打开结果表。当停止条件满足时出现警告是预期行为，但警告说明必须对应某一条已声明规则。

**检查:** 储存的过程在约 **33.885 µs** 结束，早于所请求的 100 µs。基准情况下液体向外排出，速度达到峰值后逐渐回到零附近。若求解失败，应阅读最先导致失败的错误，不要继续绘制旧解。

## C — 绘图、求值并回答模型 A 的问题

### 步骤 22 — 绘制出口速度

**位置:** 右键选择 `Results → 1D Plot Group`。再右键单击新建绘图组 → **Global**。

**输入:** 将组的 Label 设为 `A outlet speed`。选择 Study 1 / Solution 1 对应的数据集。在 Global 的 y-Axis Data 表中输入 `c.U`，Unit 为 `m/s`，Description 为 `Outward outlet speed`。在 x-Axis Data 中使用 **Time** 作为横轴来源。如果可选，将时间单位设为 `us`。否则保留秒，并按秒读取坐标轴。单击 **Plot**。

**检查:** 速度从零开始，在约 **15.3761 m/s** 达到峰值，随后衰减至零附近。这些标量数据不应使用 Surface 或 Volume 绘图。

### 步骤 23 — 分别绘制各类压力输出

**位置:** 再添加一个 `1D Plot Group → Global`。

**输入:** 将 Label 设为 `A pressure definitions`。使用相同的数据集和时间横轴，输入：

| 表达式 | 单位 | 说明 |
|---|---|---|
| `c.pb-pInf` | `kPa` | 腔室压力源超压 |
| `c.qJet` | `kPa` | 出口动压尺度 |
| `pInf` | `kPa` | 环境绝对压力参考值 |

**检查:** 初始源超压约为 **279.632 kPa**。出口最大动压约为 **118.212 kPa**。腔室绝对压力为 `c.pb`，其中包含环境压力。动压是出口处的动能尺度，并不计算靶面冲击峰值压力。

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

**输入:** 将 Label 设为 `A temporal maxima`。Dataset = Study 1 的解。Time selection = All。**Data Series Operation → Transformation = Maximum**。输入下列表达式并执行 Evaluate。如果 Data Series Operation 处于折叠状态，先将其展开。

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

**输入:** Dataset = Study 1 的解。**Time selection = Last**。**Transformation = None**。输入 `t`、`c.Eout`、`c.Iout`、`c.Mout`、`c.x`、`c.U` 和 `c.energyResidual`，单位使用下表所列值。

| 表达式 | 单位 | 已验收的最后储存值 |
| --- | --- | --- |
| `t` | `us` | 33.8850 |
| `c.Eout` | `nJ` | 1.391345448 |
| `c.Iout` | `N*s` | 2.270809686e-10 |
| `c.Mout` | `ng` | 20.9678882 |
| `c.x` | `um` | 266.9714446 |
| `c.U` | `m/s` | 0.0001702102 |
| `c.energyResidual` | `1` | -1.0350e-10 |

**检查:** Last 表示本次因停止条件而终止的解中，最后储存的时刻，约为 33.885 µs。它不是标称的 100 µs 结束时刻。Stop Condition 在离散求解步上检查，因此精确的过零时刻与最后储存行略有差异。比较排出量时，应统一使用这一末端约定。

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

**操作:** 对下面试算表的每一行执行完整流程：设置 `p0` 和 `a`。提交两个单元格。核对 `E0`。从初始值重新计算 Study 1。针对新计算的数据集，对最大值和末端节点执行 Evaluate。记录峰值速度、两种已定义压力、排出动能、排出冲量及有效性诊断量。如果需要保留该解，使用独立的练习文件名保存每次试算。对每一行都重复完整流程。

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

**检查:** 所采样工况中的最高速度约为 **25.27982 m/s**，对应 5 nJ 可用功和 3 µm 出口半径。其源超压约为 512.212 kPa，动压尺度约为 319.535 kPa。该最大值以所声明的工况族为条件。提高可用功或改变结构，会改变工况族。

### 步骤 31 — 解读压力与速度上限

**位置:** 参数值 `Uceiling`、`qCeiling` 以及九工况结果。

**操作:** 逐个工况将求解得到的最大速度与 `Uceiling` 比较，将求解得到的动压与 `qCeiling` 比较。这些上界将全部可用功分配给液柱运动，因此大于实际达到的峰值。使用所附[条件速度包络图](assets/conditional_velocity_envelope.png)查看已验收的比较结果。

**检查:** 基准工况仅由能量确定的速度上界约为 **31.9154 m/s**，而求解得到的速度为 15.3761 m/s。将腔室压力、出口动压和仅由能量确定的上界分别记录在不同列中。本模型不预测已排除的激活瞬态过程和靶面冲击压力。

