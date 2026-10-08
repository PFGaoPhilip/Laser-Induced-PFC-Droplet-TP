# Laser Induced PFC Droplet TP
# 激光诱导 PFC 液滴转印

A bilingual, project-centered theory course: four main chapters and Appendix A connect laser absorption, finite PFC phase change, cavitation jets, array interactions, actual load transmission, fracture and intact transfer.

本双语项目导向理论课程以四个主体章节及附录 A 贯通激光吸收、有限 PFC 相变、空化射流、阵列相互作用、实际载荷传递、断裂与完整转印。

[Read the website](https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/) or open `index.html` from the complete downloaded folder. All essential mathematical rendering, fonts, figures and scripts are bundled locally. Scholarly sources are optional external reading; original PDFs are excluded.

[阅读网站](https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/)，或在完整下载的文件夹中打开 `index.html`。必要数学渲染、字体、示意图及脚本均已本地打包。学术来源供可选外部阅读；不包含论文 PDF 原文。

## The single learning route
## 单一学习主线

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

Teaching numbers declare their assumptions and are not project measurements. Target-specific activation laws, jet-conversion efficiency, spatial flow/fracture solutions and hydrogel benefits remain research questions. Report the highest verified single-shot output separately from repeatable intact transfer.

教学数值均声明假设，不是项目实测。目标配方激活规律、射流转换效率、空间流动／断裂解及水凝胶优势仍属于研究问题。已核验最高单次输出与可重复完整转印应分开报告。
