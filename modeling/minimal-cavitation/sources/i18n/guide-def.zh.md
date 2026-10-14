## D — 加入水凝胶约束，建立模型 B

### 步骤 32 — 返回基准模型，并另存模型 B 副本

**位置：** `File → Open`，然后选择 `File → Save As`。

**操作：** 打开步骤 28 中保存的 `A_baseline_my_rebuild.mph`。将其另存为独立副本 `practice/B_01_from_A.mph`。把组件的 Label 改为 `c: Model B practice`。其 Name 保持为 `c`。

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

**操作：** 将五行表替换为下面完整的七行表。两个量的设置均保留为 Dimensionless。`rr=R/Rc0` 是腔壁半径比，`ww=Uw/Us` 是归一化腔壁速度。其余状态量的含义仍与步骤 13 相同。将 `rr` 的初始值设为 **1**。另外六个状态量的初始值以及每个 `ut_0` 条目均为零。[B_equations.tsv](resources/gui/B_equations.tsv) 是带表头的复制／粘贴参考文件。

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

**操作：** 两个节点均保留 1 ns 输出时间列表。所有字段与步骤 18 的设置一致。初始状态必须来自更新后的物理场方程表。现有的 `ODE1` 方程组现在包含七个状态量。不要手动把旧的 A 末态解选作新的初始状态。

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

**输入：** 在一个图组中绘制 `c.stretch`，Unit 为 `1`。在另一个图组中绘制 `c.Uw`，Unit 为 `m/s`。在一个压力图组中绘制 `c.pEl`、`c.pRes`、`c.pb-pInf` 和 `c.qJet`，单位全部为 `kPa`。使用当前 B 数据集，以 Time 为横轴。

**检查：** 初始拉伸比为 1，初始腔壁速度为零。`pEl` 表示弹性阻力压力，`pRes` 还包含黏性阻力压力。腔室驱动压力也用于克服腔壁惯性，因此不能与任一阻力曲线互换。基准模型的最大弹性阻力压力约为 **9.143 kPa**。

### 步骤 39 — 绘制定义明确的约束力

**位置：** 再添加一个 `1D Plot Group → Global`，标签设为 `B hemisphere resistance`。

**输入：** 绘制 `c.Fconf`，Unit 为 `uN`。该量定义为一个半球上的弹性腔壁牵引力沿轴向的合力。也可加入 `pi*c.R^2*c.pRes`，单位同样为 `uN`，标签设为 `Elastic plus viscous hemisphere resistance`。

**检查：** 最大弹性力约为 **33.77 µN**。这是明确定义的半球合力。球对称的腔壁牵引力在整个球面上的净矢量合力为零。该数值不是实测的靶面作用力，也不是通过空间求解得到的平面层作用力。

### 步骤 40 — 求取模型 B 的最大值

**位置：** 复制或创建一个 `Global Evaluation` 节点。标签设为 `B temporal maxima`。

**输入：** 使用当前 B 数据集。Time selection 设为 All。Transformation 设为 Maximum。求值：`c.U`，单位 `m/s`。`c.qJet` 和 `c.pEl`，单位 `kPa`。`c.Fconf`，单位 `uN`。`c.stretch`、`c.communication`、两个马赫数诊断量，以及 `abs(c.energyResidual)`，单位均为 `1`。

**检查：** 每个最大值分别来自该量自身的时间历程。如果腔壁半径已经变化，不要把最大压力乘以初始面积来计算约束力。应对完整的 `Fconf` 表达式求值。接受输出结果时仍必须包含适用性检查。

### 步骤 41 — 求取模型 B 的排出输出

**位置：** `Global Evaluation`，标签设为 `B endpoint output`。

**输入：** 使用当前 B 数据集。**Time selection Last**。**Transformation None**。使用与步骤 27 相同的末端表达式列表。

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

**检查：** 峰值速度／动压比使用 All times + Maximum。排出动能／冲量比使用 Last + None。将无量纲比值乘以 100，即可报告百分比。预期基准结果约为：**速度 10.5709%**、**动压 1.1174%**、**排出动能 0.00980%**、**排出冲量 0.08731%**。在密度相同时，只有动压比等于速度比的平方。对整个排出过程积分得到的能量比和冲量比取决于完整的排出时间历程。

### 步骤 43 — 求解密封水凝胶对照模型

**位置：** Parameters，然后执行 Study 1 的 Compute。

**操作：** 将开放出口的基准模型保存为 `practice/B_open_baseline_my_rebuild.mph`。另存独立副本 `practice/B_sealed_control_my_rebuild.mph`。仅将 `outletOpen` 改为 `0`，然后从物理场初始值重新计算。保留第一个停止表达式中的条件切换。

**检查：** `U`、`x`、`Mout`、`Eout` 和 `Iout` 在整个过程中保持为零。腔壁可以运动，气体压力也可以变化。密封对照的最大弹性压力约为 **9.6259 kPa**，最大拉伸比约为 **1.15252**，末端时间约为 **2.452 µs**。密封腔壁的响应不是外部液体射流。

### 步骤 44 — 运行凝胶与损耗敏感性对照

**位置：** 重新打开 `B_open_baseline_my_rebuild.mph`。每次试算均编辑 Parameters 并执行 Compute。

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

**检查：** 每次试算仍仅取首次事件结果。改变模量或黏度可以同时改变峰值和排出持续时间。描述其影响前，先检查能量分配和停止原因。不要认为某一种刚度变化趋势就证明了普适的传导规律。

## E — 验证、导出并保存结果

### 步骤 45 — 执行 2 ns / 1 ns 分辨率检查

**位置：** Time Dependent 研究与 Time-Dependent Solver 1。

**操作：** 在基准副本中，将两个时间列表均设为 `range(0,2[ns],100[us])`。执行 Compute，记录 U 峰值、最后的 Eout 和最后的 Iout。再将两个列表均改回 `range(0,1[ns],100[us])`。执行 Compute，并再次记录这些量。保持容差、输入和停止规则不变。以 1 ns 的数值为分母，比较相对变化。

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

**检查：** 随附的 17 案例 [NUMERICAL_AUDIT.json](verification/NUMERICAL_AUDIT.json) 中，最大的归一化第一定律残差约为 `1.26e-7`，原生求解与独立参考解之间最大的归一化时间曲线差异约为 `1.15e-4`。这些是实现检查。材料／相态标定需另行完成。

### 步骤 47 — 导出完整时间历程与汇总表

**位置：** 各个 Global Evaluation 生成的 Results 表。

**操作：** 使用 All times 和 Transformation None 对完整时间历程节点求值。在生成的表格工具栏中使用 Save/Export，将 CSV 保存到 `practice/`，例如 `A_baseline_GUI_history.csv` 或 `B_open_GUI_history.csv`。最大值表与末端表应分别导出，以保持其含义清楚。表格说明中应包含单位，或者保留 COMSOL 自带单位的表头。

**检查：** 时间历程 CSV 有许多时间行，并包含排出动能、冲量和质量。最大值 CSV 不是时间历程。确认末端 CSV 报告的是实际停止时间。原生求解与独立对照 CSV 已包含在 `data/` 中。

### 步骤 48 — 保存最终练习副本

**位置：** `File → Save As`。

**操作：** 将 A 基准、B 开放出口基准和 B 密封对照保存为分别命名的练习 MPH 文件。每个已求解案例应连同匹配的输入值和结果表一起保存。如果希望 B 的主要练习文件是开放出口基准，应在敏感性试算后恢复到该基准。

**检查：** 重新打开每个练习文件，核对标题、输入值和存储的绘图数据。两个已保存基准均使用 1 ns 输出间隔。你自己的练习文件放在 `practice/` 中。交付 ZIP 不包含该文件夹。

### 步骤 49 — 检查交付的原生模型

**位置：** `File → Open`，选择 `models/` 中任一原生文件。

**操作：** 检查 Parameters 1、组件的 Variables 节点、Global Equations 1、Time-Dependent Solver 1、其 Stop Condition，以及已保存的结果图／表。交付文件中的接口标签描述的是保留的运动／收支统计状态量。它们可能与向导的默认标题不同。通过 Global Equations 1 识别该接口。

**检查：** A 有五行状态量，B 有七行。两者均有 32 个参数、33 个变量、一个 Global Equations 接口及存储解。已通过验收的基准文件已在新的 COMSOL 进程中重新载入，也已从解压后的包中重新载入。报告中链接了数值与可移植性证据。

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

**检查：** 原生批处理日志必须显示运行完成，且没有内部 Java 错误。仅检查 shell 退出码并不足够。求解器错误详情位于 `build/`。此流程复现的方程与 GUI 表格中的方程相同。

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

**检查：** 只有在修正了相关输入或节点后才重新计算。如果输入发生变化，应重新运行守恒与适用性检查。此前已接受的表格可能不再适用。

### 步骤 52 — 将对照模型与实验相联系

**位置：** 实验记录和 Parameters 表。

**操作：** 提供有证据支持的激活后气体／相体积及压力—体积路径，或有依据的可用功估计。实际连通液体体积与出口有效流体惯性。载液性质。相关速率下的凝胶模量／黏度。以及通道是否已存在。条件允许时，在同一次激光激发中测量空腔体积、腔壁运动以及排出速度／质量。利用这些数据更新对照模型，再重复完整验收流程。

**检查：** 5 nJ 可用功输入不自动等同于 5 nJ 光学脉冲。球形凝胶对照不是精确的平面水凝胶层模型。完整密封凝胶中不会预测出穿透凝胶的外部射流。每次报告最大值或传导比时，都应同时保留这些结构与校准说明。

### 步骤 53 — 完成操作指南

**位置：** 您保存的练习模型文件与输出表。

**检查是否能够独立复现：** 15.3761 m/s 的 A 基准。25.2798 m/s 的最大已采样案例。1.62538 m/s 的开放出口凝胶基准。其 9.143 kPa 弹性阻力压力和 33.77 µN 半球力。相互匹配的排出动能／冲量比。以及密封对照中为零的排出输出。核验停止规则、数值检查和物理适用性筛查，而不应只核对峰值。

**完成记录：** 记录软件版本、输入案例、源状态假设、实际存储的末端时间、峰值定义、排出输出定义、最大守恒残差、均衡传播／马赫数／拉伸比检查以及分辨率加密对照。[项目日志](PUBLICATION.md) 和[结果报告](RESULTS.md) 提供了随附对照模型已通过验收的记录。

## 参考文献与配套文件

本次参考的 [M1 课程](https://pfgaophilip.github.io/cavitation-course/comsol/lessons/M1.html) 提供了循序渐进的界面说明格式。本指南的参数、变量和方程表取自当前两个已求解的原生文件，并非 M1 中其他模型的建模配方。归档的 HTML／文本位于 `sources/reference-lesson/`。本指南的原生模型元数据位于 `sources/native-guide-evidence/`。

- [完整推导与假设](MODEL_SPEC.md) · [可编辑 LaTeX 源文件](THEORY_DERIVATION.tex) · [离线结果](index.html)。
- [模型 A](models/Model_A_Finite_Energy_Pressure_Jet.mph) · [模型 B](models/Model_B_Hydrogel_Confinement_Jet_Transmission.mph)。
- [COMSOL 模型向导](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_environment.18.43.html)、[全局方程](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_equationbased.32.089.html)、[时间求解器](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_solver.36.139.html)、[停止条件](https://doc.comsol.com/6.4/doc/com.comsol.help.comsol/comsol_ref_solver.36.212.html)。

验证范围：已将表格与保存的原生方程核对。已使用 COMSOL 原生 API 检查参数／变量导入及 A 到 B 的转换。目标结果来自已通过验收的求解对照模型。插图均为示意图。不宣称已完成实时 Desktop 界面逐项点击验证。
