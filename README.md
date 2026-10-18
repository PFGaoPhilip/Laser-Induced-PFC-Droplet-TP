# Laser Induced PFC Droplet TP
# 激光诱导 PFC 液滴转印

Open [index.html](index.html) from the complete folder.
Use the language and day/night buttons.
Every reader uses the chapter format and lower-right controls.
All reading assets work offline.

All 178 lesson figures use English labels in both language modes.
Open the [editable figure gallery](assets/figures-editable/index.html).
Every figure includes native PowerPoint objects, SVG, and scene JSON.
Scientific conventions and actual PowerPoint previews were reviewed before embedding.

从完整文件夹打开 [index.html](index.html)。
使用语言与日夜切换按钮。
全部阅读页采用章节格式，切换按钮位于右下角。
全部阅读资源可离线使用。

## Contents / 目录

1. [Cavitation and jets](chapters/01-cavity-pressure-inertia-and-directional-jets.html).
2. [Laser heating and finite PFC inventory](chapters/02-optical-heating-and-finite-pfc-inventory.html).
3. [Arrays, jets, impact, and the three-stage resolver](chapters/03-arrays-finite-jets-and-impact.html).
4. [Fracture and transfer](chapters/04-fracture-and-transfer.html).
5. [Jet-on-rigid-wall calculation](chapters/05-jet-on-rigid-wall.html).
6. [Appendix A: liquid, hydrogel, and both modeling studies](appendices/90-hydrogel-versus-liquid.html).

1. [空化与射流](chapters/01-cavity-pressure-inertia-and-directional-jets.html?lang=zh)。
2. [激光加热与有限 PFC 存量](chapters/02-optical-heating-and-finite-pfc-inventory.html?lang=zh)。
3. [阵列、射流、冲击与三阶段求解器](chapters/03-arrays-finite-jets-and-impact.html?lang=zh)。
4. [断裂与转印](chapters/04-fracture-and-transfer.html?lang=zh)。
5. [刚性壁面射流计算](chapters/05-jet-on-rigid-wall.html?lang=zh)。
6. [附录 A：液体、水凝胶与两项建模研究](appendices/90-hydrogel-versus-liquid.html?lang=zh)。

The resolver lesson belongs to Chapter 3.
The finite-energy and embedded-PFC studies belong to Appendix A.
Their complete readers, sources, models, and data remain linked there.

求解器课程属于第三章。
有限能量与嵌入式 PFC 研究属于附录 A。
对应单元链接完整阅读页、来源、模型与数据。

## Study / 学习

Each unit has three defense questions.
Explain the mechanism, assumptions, and limits in your own words.
Submit answers in the teaching chat for review.
Three accepted explanations establish unit mastery.

每单元设三个答辩问题。
用自己的话解释机制、假设与限制。
在教学对话提交回答，接受审阅。
三个解释均被接受后，判定该单元已掌握。

## Rebuild / 重建

Python requires BeautifulSoup4 and Markdownify.
Node.js renders the bundled KaTeX math.
Run these commands from this folder.

Python 需要 BeautifulSoup4 与 Markdownify。
Node.js 使用内置 KaTeX 渲染公式。
在本文件夹运行以下命令。

```sh
python -B scripts/build_course.py
python -B scripts/highlight_bilingual_terms.py
python -B scripts/verify_course.py
python -B scripts/verify_language_labels.py
python -B scripts/verify_lesson_revision.py
python -B scripts/package_local_revision.py
```

Rebuilds preserve the edited local study readers.
Source-refresh flags explicitly recopy accepted study deliveries.
The local package is saved under delivery/.
Forward its complete folder or ZIP.

重建保留已修订的本地研究阅读页。
来源刷新选项会明确重新复制已接受的研究交付。
本地包保存在 delivery/。
转发其完整文件夹或 ZIP。

## Scientific records / 科学记录

[Editable text](text/course.md) retains the full bilingual derivations.
The [equation registry](verification/equations.json) retains LaTeX and definitions.
Numerical controls use their stated assumptions.
Target transfer performance remains unvalidated.

[可编辑文本](text/course.md)保留完整双语推导。
[方程注册表](verification/equations.json)保留 LaTeX 与定义。
数值对照采用各自声明的假设。
目标转印性能仍未验证。

Stage1: CLOSED_LOOSENED.
Stage2: STAGE2_LOOSENED_CLOSED.
Stage3: engineering reporting and delivery complete.
Maximum: Not established.
Missing: 18 attained objectives and certificates.
Publication remains HELD_NOT_PUBLISHED.

阶段一：CLOSED_LOOSENED。
阶段二：STAGE2_LOOSENED_CLOSED。
阶段三：工程报告与交付已完成。
最大值：尚未建立。
缺少：18 项已达到的目标及证书。
发布状态保持 HELD_NOT_PUBLISHED。
