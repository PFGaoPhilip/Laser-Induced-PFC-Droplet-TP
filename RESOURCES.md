# Sources for the single project route
# 单一项目路线的来源

## Course basis
## 课程依据

The copied English course and bilingual before/after comparison are in `sources/`. Their original bytes and SHA256 are preserved. The comparison guides selection and integration; the present request adds bilingual HTML, detailed necessary derivations and three questions per chapter.

复制的英文课程及双语重构前后对比位于 `sources/`。原始字节及 SHA256 均保留。对比文档指导选材及整合；本次要求增加双语 HTML、完整展开必要推导及每章三个问题。

## Knowledge
## 知识来源

[The bibliography](reference/sources.html) provides the fifteen traceable source families and states what each supports. Classical cavitation and pressure-impulse treatments supply mechanical controls; optical PFC studies and NIST provide formulation-specific evidence and named property ranges; jet and fracture studies close the spatial-load-to-release chain; gel mechanics and hydrogel-composite transfer studies support distinct platform hypotheses.

[参考文献页](reference/sources.html)给出十五组可追溯来源，并注明各自支持的内容。经典空化及压力冲量理论提供力学对照；PFC 光学研究及 NIST 提供特定配方证据与具名物性区间；射流及断裂研究闭合空间载荷到释放的链条；凝胶力学及水凝胶复合转印研究支持不同平台假说。

## Gaps
## 尚待解决

Actual PFC formulation and shell law, measured optical/thermal routing, activation probability, spatial launch geometry, delivered solid traction and fracture resistance, high-state EOS and repeatable reset require target-specific evidence. An assigned efficiency or matched analytical calculation is not that evidence.

实际 PFC 配方及壳层规律、实测光热路径、激活概率、空间发射几何、传递到固体的牵引与断裂阻力、高状态 EOS 及可重复复位均需目标条件下的证据。预设效率或吻合的解析计算不能替代这些证据。

## Interactive teaching source — spherical carrier flow

[Christopher E. Brennen, Cavitation and Bubble Dynamics (1995), Section 2.2](https://media.library.caltech.edu/CaltechBOOK:1995.001/chap2.htm). Verified 2026-10-10. Supports the spherical incompressible exterior-liquid model, the continuity relation and the interface kinematic condition. The liquid velocity equals the interface velocity exactly in the absence of interfacial mass transfer; appreciable evaporation or condensation can require a corrected interface condition. The stepwise chat derivation is original teaching work corresponding to the course's C1-E02.

## Interactive teaching sources — impulse and directional motion

[Cooker and Peregrine (1995), Pressure-impulse theory for liquid impact problems](https://doi.org/10.1017/S0022112095003053). The pressure-impulse model is a short-event approximation, with spatial boundary conditions required to determine the velocity increment. A pressure impulse has units Pa s; it is not a sound-crossing time or a total force impulse.

[Supponen et al., Scaling laws for jets of single cavitation bubbles](https://arxiv.org/html/1703.01088). Supports the role of broken symmetry in collapse-driven internal jets. Its collapse geometry does not by itself calibrate an external PFC transfer jet.

## Formula presentation tools

[termtex](https://github.com/errantdata/termtex), installed npm version 0.9.8: a terminal stream/file/equation renderer with Unicode output and optional terminal/browser typesetting. [claude-math](https://github.com/vladimirrott/claude-math), installed npm version 0.6.0: a CLI supplying the math-unicode skill for writing terminal-readable mathematical text. The native skill was installed with the Codex skill-installer helper, without overwriting other agent settings.

The learner's downloaded source archives are retained in sources/math-rendering/downloads/. The new skill is copied into sources/skills/math-unicode/. Exact hashes, version matches and three successful formula-rendering checks are recorded in verification/math-rendering-installation-20261010.json. Terminal installation does not modify the chat UI; Unicode plus English explanation is the adopted chat presentation.

On 2026-10-10, customized the native skill as Math-Unicode at the learner's request, incorporating the full Math-Rigor workflow and a Unicode version of its worked reference. The original source snapshots above remain unchanged. The integrated package and portable ZIP are in skill-upgrades/2026-10-10-Math-Unicode/, with conversion, hash and validation evidence in verification/Math-Unicode-upgrade-20261010.json. The npm CLI versions remain unchanged; the customized skill is maintained independently of the upstream package installer.
