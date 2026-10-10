# Laser Induced PFC Droplet TP
# 激光诱导 PFC 液滴转印

A bilingual, project-centered theory course: four main chapters and Appendix A connect laser absorption, finite PFC phase change, cavitation jets, array interactions, actual load transmission, fracture and intact transfer.

本双语项目导向理论课程以四个主体章节及附录 A 贯通激光吸收、有限 PFC 相变、空化射流、阵列相互作用、实际载荷传递、断裂与完整转印。

[Read the website](https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/) or open `index.html` from the complete downloaded folder. All essential mathematical rendering, fonts, figures and scripts are bundled locally. Scholarly sources are optional external reading; original PDFs are excluded.

[阅读网站](https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/)，或在完整下载的文件夹中打开 `index.html`。必要数学渲染、字体、示意图及脚本均已本地打包。学术来源供可选外部阅读；不包含论文 PDF 原文。

## The single learning route
## 单一学习主线

Use the **中文 / English** button to show one language at a time. The day/night choice and saved defense answers remain available in both views.

使用 **中文 / English** 按钮单独显示一种语言。日夜模式及已保存答辩草稿在两种语言视图中均可使用。

The complete [modeling section](modeling/minimal-cavitation/index.html) connects this theory course to the accepted minimal finite-energy cavitation models: full derivation, bilingual 53-step COMSOL guide, two native MPH files, numerical histories, audit records and a downloadable folder. Its ideal-gas source and existing liquid outlet are declared controls; it does not simulate laser activation, PFC phase conversion, internal collapse jets or target impact. The source delivery was copied into `modeling/minimal-cavitation/`.

完整的[建模部分](modeling/minimal-cavitation/index.html?lang=zh)将理论课程与已核验的有限能量简洁空化模型相连接：完整推导、双语 53 步 COMSOL 指南、两个原生 MPH 文件、数值历程、核验记录及可下载文件夹。理想气体源和已有液体出口是声明的对照条件；模型不模拟激光激活、PFC 相变、内部塌缩射流或靶面冲击。源文件已复制至 `modeling/minimal-cavitation/`。

The new [embedded-PFC feasibility study](modeling/embedded-pfc-feasibility/index.html) compares PFP/PFH, initial liquid size, gel modulus and viscosity using finite real-fluid PFC and a surviving liquid shell. It includes a 32-equation derivation, printable PDF, two native COMSOL models, raw data, stability and fracture-budget screens, and a measured validation plan. Sixty native stationary and six supplied-seed transient comparisons pass. These are conditional intact-gel controls: the new velocities are radial wall speeds and exterior emission is zero. Target laser activation, rupture/channel formation, collapse jets and impact pressure remain unvalidated. The public study was copied into `modeling/embedded-pfc-feasibility/`; original-source scholarly links replace third-party paper PDFs.

新增的[嵌入式 PFC 可行性研究](modeling/embedded-pfc-feasibility/index.html)采用有限存量真实流体 PFC 与剩余液体壳层，对比 PFP／PFH、初始液体尺寸、凝胶模量及黏度。提供 32 个公式的完整推导、可打印 PDF、两个原生 COMSOL 模型、原始数据、稳定性与断裂能预算筛选及实测验证计划。60 个原生稳态和 6 个预设成核后种子瞬态对照已通过。这些是条件性的完整凝胶对照：新增速度是径向壁面速度，外部排出量为零。目标系统的激光激活、破裂／通道形成、塌缩射流及冲击压力仍未验证。公开研究已复制至 `modeling/embedded-pfc-feasibility/`；第三方论文 PDF 以原始来源链接代替。

1. Cavity pressure, carrier inertia and directional jets.
2. Laser heating, matched PFC comparisons and finite phase inventory.
3. Bubble arrays, finite emitted jets, transport and defined impact loads.
4. Direct/PVC force paths, transient film mechanics and selective fracture.
5. **Appendix A:** Conventional liquid, gel-supported pockets, embedded PFC and sealed-cavity platforms.

1. 腔体压力、载液惯性与定向射流。
2. 激光加热、匹配条件的 PFC 对照与有限相存量。
3. 气泡阵列、有限喷出射流、输运与明确冲击载荷。
4. 直接／PVC 受力路径、瞬态薄膜力学与选择性断裂。
5. **附录 A：**常规液体、凝胶支撑液体口袋、嵌入 PFC 与密闭腔体平台。

## Defense and mastery
## 答辩与掌握

Each chapter and Appendix A ends with exactly three questions, detailed formula-first reference answers, and a semantic rubric. Save your own-word responses, then copy or download them into the teaching chat for feedback. The teacher marks a unit mastered only after all three explanations demonstrate understanding. Reading, browsing and form completion do not automatically mark mastery.

每章及附录 A 的末尾均有恰好三个问题，附先引原公式的详细参考答案及理解评估标准。保存自己的解释后，复制或下载至教学对话获得反馈。只有三个解释均展示理解后，教师才将该单元标记为已掌握。阅读、浏览及填写表单不会自动标记掌握。

## Editable source and checks
## 可编辑来源与核验

Before every equation, individual bilingual definitions are arranged two per row with a continuous vertical divider. Narrow screens show one variable per row. Each entry states its own meaning and units; conventions and applicability conditions follow the table.

每个公式前均提供独立的英中符号定义，宽屏每行两项，以连续竖线隔开；窄屏每行一项。各项分别说明含义与单位，表后保留约定及适用条件。

`text/course.md` retains complete bilingual prose and LaTeX formula text. `content/chapter01.py` through `chapter05.py` contain editable chapter sources. `verification/equations.json` preserves local symbol declarations and physical-variable maps for every display. Chapter checks and integration audits are included separately from experimental validation.

`text/course.md` 保留完整双语正文及 LaTeX 公式文本。`content/chapter01.py` 至 `chapter05.py` 为可编辑章节来源。`verification/equations.json` 保存每个公式前的符号定义与物理变量图信息。各章核验与整合审计均与实验验证明确区分。

`content/equation_symbol_rows.json` contains the reviewed individual entries, their units, and the original bilingual fragments for traceability. The builder renders these records directly.

`content/equation_symbol_rows.json` 保存核验后的独立条目、对应单位及用于追溯的原始英中文本片段；网页构建器直接渲染这些记录。

To rebuild, install Python with BeautifulSoup4 and Markdownify, and use Node.js. The numerical chapter checks also use SciPy and SymPy. Run the commands below from this folder. KaTeX is bundled with its license. Set `NODE_BINARY` only when Node is not on the normal executable path.

重建时需要装有 BeautifulSoup4 与 Markdownify 的 Python，以及 Node.js。各章数值核验还使用 SciPy 与 SymPy。请在本文件夹执行以下命令。KaTeX 及其许可证已打包。仅在 Node 不在通常可执行路径时设置 `NODE_BINARY`。

```sh
python -B scripts/build_course.py
python -B scripts/highlight_bilingual_terms.py
python -B scripts/verify_course.py
python -B scripts/package_site.py
```

After rebuilding course pages, run `python -B scripts/integrate_modeling.py --course-only` and `python -B scripts/integrate_embedded_pfc.py` in the authoring workspace to restore the modeling entry points before packaging. The integration scripts use the completed local study deliveries. Public study files and their bundled numerical recipes are usable independently; `python -B scripts/verify_embedded_publication.py --study-directory modeling/embedded-pfc-feasibility` checks the curated study's integrity and relative assets.

Teaching numbers declare their assumptions and are not project measurements. Target-specific activation laws, jet-conversion efficiency, spatial flow/fracture solutions and hydrogel benefits remain research questions. Report the highest verified single-shot output separately from repeatable intact transfer.

教学数值均声明假设，不是项目实测。目标配方激活规律、射流转换效率、空间流动／断裂解及水凝胶优势仍属于研究问题。已核验最高单次输出与可重复完整转印应分开报告。
