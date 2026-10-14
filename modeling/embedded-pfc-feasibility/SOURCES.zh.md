# 来源与支持的论断

主要文献与官方来源核对于 2026-10-11。本项目计算值为有条件模型结果。它们与文献实测值分别记录。

| 编号 | 来源 | 支持范围与未确立事项 |
|---|---|---|
| S1 | Abeid、Fabiilli、Aliabouzar 和 Estrada (2024)，[软材料内光致液滴空化超高速动力学的实验与数值研究](https://doi.org/10.1016/j.jmbbm.2024.106776)；[作者手稿](https://pmc.ncbi.nlm.nih.gov/articles/PMC12557251/) | 纤维蛋白、聚丙烯酰胺和明胶内 PFC 液滴实验确立光致空化可行性。比较 PFP/PFH/PFO 及 3/6/12 µm **直径**。装置采用单次 532 nm、4 ns 脉冲。1.3–1.8 mJ 是装置脉冲能量，单滴吸收能量另需测量。相关气泡模型含水蒸气和不凝气体。当前纯 PFC 平衡对照、外部射流与目标配方验证尚未确立。 |
| S2 | Gao 等 (2021)，[正全氟丁烷、正全氟戊烷及正全氟己烷热力学性质状态方程](https://doi.org/10.1021/acs.iecr.1c02969)；[PFP 官方实现](https://coolprop.org/fluid_properties/fluids/n-Perfluoropentane.html)、[PFH 实现](https://coolprop.org/fluid_properties/fluids/n-Perfluorohexane.html) | 采用 Helmholtz 真实流体状态方程计算压力、内能与化学势。包内保存 CoolProp 8.0.0 系数 JSON。光学吸收、成核速率、凝胶性能、断裂能与界面律须另行提供。 |
| S3 | [NIST Chemistry WebBook：全氟戊烷](https://webbook.nist.gov/cgi/cbook.cgi?ID=C678262&Mask=4) | 分子量 288.0343 g/mol；汇编沸点 302.6–303.2 K；标准汽化焓条目 26.6 与 27.5 kJ/mol。这些是体相参考量。纳米液滴激活温度及各模型状态潜热须独立确定。 |
| S4 | Kandadai (2010)，[生物聚合物流变与界面张力：作者学位论文](https://collections.lib.utah.edu/dl_files/40/6e/406e61ce35554485df3ea659a68ff430277482b7.pdf)，印刷页 113–119、表 5.2–5.3；[相关文章](https://doi.org/10.1021/la100307r) | 室温 PFP／饱和空气张力 9.41 mN/m，PFP／蒸馏水张力 54 mN/m。用作独立内外恒定对照。高温 PFP／凝胶表面应力尚未实测。 |
| S5 | [1.1 MHz 异质成核诱导全氟己烷乳液声致液滴汽化](https://doi.org/10.1021/acs.langmuir.3c02272)，表 2 及成核讨论 | 20 °C 的 PFH 液／气参考张力为 12 ± 2 mN/m。文献区分各界面与异质成核。为控制状态方程比较，PFH 使用与 PFP 相同的**预设** 54 mN/m 外张力。PFH／凝胶张力尚未实测。 |
| S6 | Luo 等 (2020)，[用激光空化流变测量水凝胶弹性模量与破坏应变](https://www.nature.com/articles/s41598-020-68621-y) | 气泡半径测量结合黏弹气泡模型可识别模量和破坏应变。支持在相关动态范围内测量性能。准静态模量与高速性能等同性尚未确立。伸长比 2.1 的普适破裂含义尚未确立。 |
| S7 | Zhao 等 (2023)，[影响相变全氟碳纳米液滴重复瞬态光学汽化阈值及寿命的因素](https://doi.org/10.3390/nano13152238) | 光激活受配方与照射影响。此前约 18.6 mJ/cm² 阈值对应约 309 nm **直径**的条件化群体，温度 0 °C，1064 nm／5 ns，PAAm 环境。室温单个未条件化 300 nm **半径**液滴的阈值仍需标定。 |
| S8 | Brennen (1995)，[《空化与气泡动力学》第 2 章](https://media.library.caltech.edu/CaltechBOOK:1995.001/chap2.htm) | 支持球形惯性、气泡热力学及不可压缩描述的适用限制。定向塌缩射流与激波压力历史需要空间模型。 |
| S9 | COMSOL 6.4，[损伤](https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_solid.07.040.html)、[损伤模型](https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_theory.06.036.html) | 相应许可产品提供超弹性相场损伤及断裂能／长度输入。开放充液通道还需要流体耦合。 |
| S10 | COMSOL 6.4，[层合复合材料混合模式脱粘](https://doc.comsol.com/6.4/doc/com.comsol.help.models.sme.cohesive_zone_debonding/cohesive_zone_debonding.html) | 官方黏聚牵引－分离示例，以及 Interior Contact 下 Adhesion/Decohesion 设置。它提供软件实现参考。目标凝胶标定与验证仍需实验。 |

此前来源背景位于 `sources/prior_interface_evidence.md`。论文链接指向原始仓库或 DOI 页面。包内包含状态方程系数、推导、模型、数据与审查记录。已接受的英文 PDF 保留原始来源台账。`PUBLICATION.md`记录当前包的来源。
