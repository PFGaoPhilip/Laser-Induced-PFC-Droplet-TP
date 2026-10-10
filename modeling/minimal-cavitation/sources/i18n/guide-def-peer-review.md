# Independent semantic review — Chinese guide sections D–F

Reviewed `guide-def.zh.md` against sections D–F and References in `STEP_BY_STEP.md`, covering Steps 32–53. This is a scientific-meaning and completeness review, distinct from the translator's executable-token checks. It does not constitute a new simulation, native-file audit or Desktop click-through.

No substantive scientific mistranslation was identified in the requested critical points:

- Steps 32–34 preserve the matched baseline, all nine gel-dependent substitutions, seven solved states, `rr=1`, the other six zero state values and all zero derivative initial values. The zero-radius singularity warning is retained.
- Steps 35–36 retain physics-based initial states, one active interface, initialization Off, the conditional outlet/wall stopping expression, and the need to restore settings and all four stops after regenerating the solver. The stretch screen remains distinct from measured fracture.
- Steps 38–40 distinguish elastic resistance, viscous resistance and driving pressure. The force is an axial resultant on one hemisphere, with zero net vector force on the complete sphere; it is not asserted to be target force or planar-layer force. The instruction to evaluate the complete force expression rather than combine independently maximized pressure and initial area is retained.
- Steps 41–42 retain the emitted/stored distinction, matched A denominators, replacement of all denominators after changing inputs, peak versus endpoint evaluation, and the density condition for the squared speed relation. Integrated energy/impulse ratios remain dependent on complete histories.
- Step 43 preserves the sealed control's zero outlet displacement, speed, emitted mass, energy and impulse while permitting wall motion and pressure change.
- Steps 44–46 and 52–53 preserve conditional first-event results, the prohibition on universal stiffness/transmission claims, conservation and positivity checks, inventory/stretch/Mach/communication screens, numerical refinement, optical/mechanical energy separation and spherical-versus-planar scope.
- References and the final verification-scope paragraph preserve provenance and the limitation on live UI verification claims.

Findings requiring or allowing editorial action:

1. **Completeness correction — Step 53, immediately after its heading (current line 268).** The source's “Where: Your saved practice files and output tables.” is omitted. Restore `**位置：** 已保存的练习文件和输出表。` before the independent-reproduction checklist. This is a small card-completeness issue, not a scientific error.
2. **Optional precision — Step 49, 操作 (current line 207).** “运动／能量统计状态量” narrows the source's “motion/accounting states” to energy, although the retained accumulators also include emitted impulse. Prefer “运动／收支统计状态量”. No equation or output definition is affected.
3. **Optional precision — Step 46, final 检查 paragraph (current line 185).** “材料／相变校准” renders “material/phase calibration” specifically as phase-change calibration. “材料／相态标定” or “材料与相态模型的标定” keeps the source broader. The existing text still correctly distinguishes implementation checks from experimental calibration.

No translation files, scripts, assets, models or logs were changed during this review. Line numbers refer to the reviewed fragment and may shift during integration.
