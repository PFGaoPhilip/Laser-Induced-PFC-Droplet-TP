# What Changes After the Course Restructuring?
# 课程重构前后有哪些不同？

**The main change is from several parallel collections of theory to one project-centered learning sequence. It is not simply a shorter table of contents, and it does not make every topic more detailed.** The rewritten course prioritizes explaining and calculating the complete transfer process, rather than preserving the coverage of the original textbooks. [^1]

**最主要的变化，是从几套并列的理论资料，变成一条围绕项目展开的学习主线。它不只是缩短目录，也不意味着每个知识点都讲得更深。** 重构版优先保证读者能够解释和初步计算完整的转印过程，而不再优先保证原教材的知识覆盖率。

One qualification matters: the original course already contains substantial project theory. G10–G12 cover lasers, PFC droplets, and film detachment; T01–T04 cover optical deposition through release; and J02 contains actual moving-interface and boundary-integral theory. The problem is therefore better described as **fragmentation, repeated entry points, and uneven integration**, rather than a complete absence of foundations. Also, L02–L04 are listed as planned extensions, not three completed chapters. [^2]

有一点需要准确区分：原课程已经包含相当多的项目理论。G10–G12讲激光、PFC液滴与薄膜脱离；T01–T04覆盖光能沉积到释放；J02也确实包含运动界面与边界积分理论。因此，更准确的问题是**内容分散、入口重复，以及基础与应用衔接不均匀**，而不是完全没有理论基础。另外，L02–L04在原课程中标注的是计划扩展，并非已经写完的三章。

## 1. The organization changes: one main route replaces parallel routes
## 1. 组织方式变化：从多条路线并列，变成一条主线

The original keeps a textbook-reference route alongside a J-series mechanics route followed by laser/PFC specialization. The rewrite instead makes the project’s causal chain explicit throughout: **laser absorption → heating and nucleation → finite PFC phase change → bubble motion → directional jetting → transmitted loading → interfacial fracture → intact transfer**. Chapter 1 still establishes the minimum mechanics first; the course does not abandon prerequisites just to follow chronological order. [^3] [^4]

原版同时保留教材参考路线，以及先学J系列力学、再进入激光／PFC的项目路线。重构版则始终围绕同一条因果链：**激光吸收 → 加热与成核 → 有限PFC相变 → 气泡运动 → 定向射流 → 载荷传递 → 界面断裂 → 完整转印**。第一章仍然先建立必要的力学基础，并不是为了按事件顺序讲课，就放弃前置知识。

The following is a content correspondence, not a claim that every old paragraph or derivation has been retained. The source material is selected and redistributed into the four chapters and one appendix. [^5]

下面是知识内容的对应关系，不代表旧版每一段文字、每一个推导都被保留。原资料经过筛选后，重新分配到四章和一个附录中。

| New unit / 新单元 | Main material consolidated / 主要整合内容 | Central learning question / 核心学习问题 |
|---|---|---|
| **Chapter 1: Cavitation and jets**<br>**第1章：空化与射流基础** | Selected G-series mechanics and J01–J02 foundations.<br>G系列中的必要力学基础，以及J01–J02的基础内容。 | How does cavity pressure accelerate liquid, and why does a directional jet require asymmetry?<br>腔体压力如何加速液体？为什么形成定向射流必须有不对称性？ |
| **Chapter 2: PFC versus ordinary droplets**<br>**第2章：PFC与普通液滴对比** | Laser deposition, nucleation, heat/mass transfer, PFC properties, and L01 source thermodynamics.<br>激光沉积、成核、传热传质、PFC物性与L01源热力学。 | Under matched conditions, what does PFC actually change—and what does it not guarantee?<br>在匹配条件下，PFC究竟改变了什么，又不能保证什么？ |
| **Chapter 3: Arrays and preliminary calculations**<br>**第3章：阵列与初步计算** | Jet formation/transport/impact concepts and the array and finite-limit material from Appendix B.<br>射流形成、输运、冲击，以及原附录B中的阵列与有限极限内容。 | How do individual sites combine into a finite, physically consistent mechanical output?<br>单个位点如何共同形成有限且符合物理约束的力学输出？ |
| **Chapter 4: Fracture and transfer**<br>**第4章：断裂与转印** | Film/PVC loading, transient structural response, interface separation, and transfer criteria.<br>薄膜／PVC受载、瞬态结构响应、界面分离与转印判据。 | Does the delivered load release the intended interface without destroying the payload?<br>实际传递的载荷能否释放目标界面，同时不损坏被转印对象？ |
| **Appendix A: Hydrogel versus liquid**<br>**附录A：水凝胶与液体平台** | Hydrogel confinement, constitutive resistance, response times, and architecture comparison.<br>水凝胶约束、本构阻力、响应时间与结构方案比较。 | Does the gel improve the complete transfer process, or merely change the mechanism?<br>凝胶是在改善完整转印过程，还是仅仅改变了致动机制？ |

**Appendix B no longer remains a separate reading detour.** Its array-coupling and pressure/velocity-limit arguments belong primarily in Chapter 3, while the elementary single-bubble collapse and finite-inventory prerequisites sit in Chapters 1 and 2. This is a conceptual merger, not a verbatim insertion of the old appendix. [^6] [^7] [^8]

**附录B不再作为需要额外绕去阅读的独立内容。** 其中的阵列耦合、压力与速度极限主要归入第3章；单泡塌缩、有限PFC存量等前置基础则放在第1、2章。这是按知识依赖关系合并，而不是把旧附录原封不动塞进第3章。

## 2. The selection changes: remove the vibration curriculum, not necessary transient physics
## 2. 取舍方式变化：取消振动知识主线，而不是删除必要的瞬态物理

The rewrite has no separate harmonic-oscillation or resonance curriculum. However, it retains liquid inertia, collapse, pressure impulse, compressibility checks, short-time impact impedance, film inertia, and gel response times where they affect the project. **Removing externally driven acoustic-cavitation teaching is not the same as assuming that laser-driven events have no pressure-wave or transient-response physics.** [^9] [^10] [^11]

重构版不再安排独立的简谐振荡、共振等学习主线。但液体惯性、塌缩、压力冲量、可压缩性检查、短时冲击阻抗、薄膜惯性，以及凝胶响应时间，只要影响项目结果，就仍然保留。**去除外加声波驱动空化的教学主线，不等于假设激光诱导过程没有压力波和瞬态响应。**

PFC is also treated as the working phase-change material throughout the source calculation—not as a late example of a generic gas bubble. Chapter 2 connects absorber location and heat-transfer time to activation, finite liquid inventory, evaporation/condensation, and bubble-pressure closure. Its comparison asks about useful transfer performance, not simply which liquid has the lowest boiling point. [^12] [^13]

PFC也不再只是通用气泡理论讲完之后顺带举出的材料例子，而是贯穿源项计算的实际相变介质。第2章把吸收体位置、传热时间、激活条件、有限液体存量、蒸发／冷凝和泡内压力闭合联系起来。比较的目标是有效转印性能，而不只是“哪种液体的沸点最低”。

## 3. The teaching changes: connected derivations and calculations, with explicit limits
## 3. 教学方式变化：把推导与计算串起来，同时标明边界

The rewrite retains derivations needed to understand the main chain. For example, the bubble equation follows from continuity, velocity potential, Bernoulli, and interfacial stress balance; the blister-fracture example proceeds from plate deflection to cavity volume, potential energy, and energy-release rate. The intention is to show why the equations connect, not merely place relevant formulas next to each other. [^14] [^15]

重构版保留理解主线所必需的推导。例如，气泡方程依次从连续性、速度势、伯努利方程和界面应力平衡得到；鼓泡断裂算例依次从薄板挠度推到腔体体积、势能和能量释放率。重点是解释这些方程为什么能连接起来，而不是把看似相关的公式摆在一起。

A connected teaching example then runs from a PFC-core inventory calculation to a 25-site array, finite jet mass and energy, impact, and film release. Its most useful lesson is that **an approximately 47 MPa early-impact pressure scale can coexist with failure of the transfer-energy requirement**. This makes the distinction between “large local pressure” and “successful release” concrete. All efficiencies and geometry assumptions in that example are declared; the values are not experimental predictions for your project. [^16] [^17]

随后，一个贯穿算例从PFC液核存量计算，接到25个位点的阵列、有限射流质量与能量、冲击，再接到薄膜释放。它最有价值的结论是：**早期冲击压力尺度即使约为47 MPa，转印所需的能量条件仍可能不满足。** 这样就把“局部压力很大”和“成功释放”之间的区别具体算出来了。算例中的效率和几何假设均已声明，这些数值不是对你实际项目的实验预测。

**The trade-off is real:** some specialist derivations are shorter. The original J02 explicitly develops a boundary-integral formulation for moving-interface formation; the rewrite states the necessary spatial equations and boundary requirements more compactly. It therefore improves continuity and project focus, but does not replace every detailed treatment in the old material. [^18] [^19]

**代价也是真实存在的：**部分专题推导被压缩了。原J02明确展开了运动界面形成的边界积分表述；重构版则更紧凑地给出所需空间控制方程和边界条件。因此，它改善的是连贯性和项目聚焦程度，并不能替代旧资料中每一个更深入的专题。

## 4. The assessment changes: three synthesis questions for the entire course
## 4. 考核方式变化：整门课只保留三个综合简答题

The three questions are **for the whole course, not three per chapter**. They test whether you can explain the source-to-jet chain, calculate an array without treating bubble count as a free pressure multiplier, and connect loading to fracture while distinguishing hydrogel architectures. The text explicitly accepts correct explanations in your own words; reproducing formulas and numerical examples is not required. Worked examples remain teaching material, not an additional homework set. [^20]

三个问题是**整门课总共三个，不是每章三个**。分别检验你能否解释从热源到射流的因果链、在不把气泡数量当作免费增压倍数的前提下计算阵列，以及把载荷与断裂联系起来并区分不同水凝胶结构。正文明确规定：用自己的话解释正确即可，不要求复现公式和数值算例。已解算例仍是教学内容，而不是另外一套作业。

In other words, the assessment shifts from demonstrating completion of individual topics to defending a project-level explanation: **What causes the next stage? What assumptions make that calculation valid? What evidence would show that the process actually works?**

也就是说，考核从证明“某个知识点做过了”，变成能够为项目层面的解释进行答辩：**下一阶段由什么驱动？计算在什么假设下成立？需要什么证据才能说明过程确实可行？**

## 5. What the rewrite does—and does not—deliver
## 5. 重构实际交付了什么，又没有交付什么

The new document provides a coherent theory route, named material references, preliminary analytical calculations, and explicit links between fluid motion and transfer fracture. It does **not** establish a unique experimental PFC formulation, a calibrated jet-conversion efficiency, a geometry-specific jet solution, or verified hydrogel feasibility. For example, the 25-site worked example assumes separate liquid cells; it must not be mistaken for a solved, strongly interacting array in one continuous liquid domain. [^21] [^22] [^23]

新文档提供了连贯的理论路线、明确的材料参考、初步解析计算，以及流体运动与转印断裂之间的联系。但它**没有**确定唯一的实际PFC配方，没有完成射流转换效率标定，没有给出特定装置几何的完整射流解，也没有验证水凝胶方案必然可行。例如，25个位点的贯穿算例假设各液体单元相互独立，不能把它当成同一连续液体中强耦合阵列的求解结果。

The delivered artifact is a standalone **English Markdown course**, not a rebuilt website. M1–M4 were excluded from the theory rewrite, not revised or validated. Mathematical models remain because they are part of the theory; software-operation lessons do not. The published website has not been changed by delivery of that Markdown file. [^24]

已经交付的是一份独立的**英文Markdown课程**，不是重新搭建的网站。M1–M4没有纳入理论重写，也没有在本次工作中被修改或验证。数学模型仍然保留，因为它们属于理论；软件操作课程则不包括在内。交付这份Markdown文件，并没有改变已经发布的网站。

**Overall: the old course is more useful as a broad reference library; the rewrite is more useful as the main reading route for this project. You gain a clearer chain from assumptions to calculations to transfer criteria, while giving up some breadth and specialist detail.**

**总体而言：旧版更适合作为广泛查阅的参考资料库；重构版更适合作为这个项目的主读教材。你获得的是从假设、计算到转印判据的清晰主线，代价是部分知识覆盖面和专题细节。**

---

## Source notes / 来源说明

The original archive and published course pages were compared with the previously delivered English Markdown. The mapping above is an editorial comparison, not a paragraph-by-paragraph preservation claim.

对照依据为原课程压缩包、公开课程页面，以及此前交付的英文Markdown。上述知识对应关系属于编辑性比较，不代表逐段完整保留。

[^1]: Rewritten course: Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md, opening scope and Chapter 1. Retrieved excerpt L14-L24.
[^2]: Original course: SCHEDULE.html, complete course schedule. Original course: course/chapters/J02-interface-motion-and-focusing.html. Original course: index.html, published course routes and L02–L04 status.
[^3]: Original course: index.html, published course routes and L02–L04 status.
[^4]: Rewritten course: Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md, opening scope and Chapter 1. Retrieved excerpt L16-L31.
[^5]: Rewritten course: Chapter 4, Appendix A, defense questions, and source basis. Retrieved excerpt L959-L962.
[^6]: Original course: course/appendixes/B-pressure-limits.html.
[^7]: Rewritten course: Chapter 3. Retrieved excerpt L332-L410.
[^8]: Rewritten course: Chapter 3. Retrieved excerpt L526-L588.
[^9]: Rewritten course: Chapter 1.6 and Chapter 2. Retrieved excerpt L16-L33.
[^10]: Rewritten course: Chapter 3. Retrieved excerpt L526-L556.
[^11]: Rewritten course: Chapter 4, Appendix A, defense questions, and source basis. Retrieved excerpt L674-L696.
[^12]: Rewritten course: Chapter 1.6 and Chapter 2. Retrieved excerpt L40-L55.
[^13]: Rewritten course: Chapter 1.6 and Chapter 2. Retrieved excerpt L176-L250.
[^14]: Rewritten course: Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md, opening scope and Chapter 1. Retrieved excerpt L58-L114.
[^15]: Rewritten course: Chapter 4, Appendix A, defense questions, and source basis. Retrieved excerpt L722-L760.
[^16]: Rewritten course: Chapter 3. Retrieved excerpt L590-L618.
[^17]: Rewritten course: Chapter 4, Appendix A, defense questions, and source basis. Retrieved excerpt L789-L815.
[^18]: Original course: course/chapters/J02-interface-motion-and-focusing.html.
[^19]: Rewritten course: Chapter 1.6 and Chapter 2. Retrieved excerpt L16-L33.
[^20]: Rewritten course: Chapter 4, Appendix A, defense questions, and source basis. Retrieved excerpt L940-L955.
[^21]: Rewritten course: Chapter 1.6 and Chapter 2. Retrieved excerpt L174-L174.
[^22]: Rewritten course: Chapter 3. Retrieved excerpt L592-L600.
[^23]: Rewritten course: Chapter 4, Appendix A, defense questions, and source basis. Retrieved excerpt L926-L936.
[^24]: Rewritten course: Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md, opening scope and Chapter 1. Retrieved excerpt L14-L24.
