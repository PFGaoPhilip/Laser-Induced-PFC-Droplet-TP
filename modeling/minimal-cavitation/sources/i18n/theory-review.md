# Chinese theory translation review

Completed on 2026-10-10. The complete `MODEL_SPEC.md` was read before translating it into `MODEL_SPEC.zh.md`. Terminology was checked against `sources/i18n/TERMINOLOGY.csv`. The translation contains one continuous Simplified Chinese version, with no paragraph-paired English text and no summary substitutions.

## Exact preservation checks

Checks compared the source and target as UTF-8 text, normalizing only the text reader's line endings. They compare ordered expression lists, not merely counts.

| Checked item | Source count | Chinese count | Result |
|---|---:|---:|---|
| Display LaTeX expressions, including delimiters | 29 | 29 | Exact ordered match |
| Inline LaTeX expressions, including delimiters | 228 | 228 | Exact ordered match |
| Combined inline/display LaTeX expressions | 257 | 257 | Exact ordered match |
| Inline backtick code spans | 15 | 15 | Exact ordered match |
| Fenced code blocks | 0 | 0 | Exact ordered match |
| Equation-identifier occurrences, including appendix references | 85 | 85 | Exact ordered match |
| Bold displayed-equation labels | 29 | 29 | Exact ordered ID match |
| URLs | 2 | 2 | Exact ordered match |
| Headings | 13 | 13 | Structure retained; heading prose translated |
| Markdown table rows, including header/separator | 34 | 34 | Structure retained |
| Table data-row unit cells | 32 | 32 | Exact match after translating `dimensionless` to 无量纲 |
| Paragraph blocks separated by blank lines | 145 | 145 | Structure retained |
| Nonempty lines | 358 | 358 | Structure retained |

The source has 29 displayed equations, with IDs **E01–E25 plus E05a, E06a, E08a and E22a**. It does not contain consecutively numbered E26–E29. This original numbering, including the placement of E22a before E22, is retained.

Source SHA-256: `6baee589e884bc4fcde6d20e5154efeee4b533b740edaefbcccbefc0ce947bc2`.

Translation SHA-256: `b04c32d152faeba55dfa65535e9979cd3d1733cff3042649bad7912804d487b7`.

## Scientific and terminology review

The second pass checked the source scope and all nine derivation steps, including their assumptions, initial/boundary conditions, intermediate algebra, units, sign conventions, limiting checks and references. No numerical or physical claim was added, removed or strengthened.

- The source remains a closed, constant-exponent adiabatic ideal-gas control. It is explicitly not a calibrated PFC-vapor EOS, phase-change prediction or optical-to-mechanical conversion model.
- 可用功 and 激活后的机械可用能 retain the distinction between post-activation mechanical availability and incident optical energy.
- 有效流体惯性 and 流体惯性长度 retain the distinction between liquid-column inertance and the separate finite liquid-discharge budget. Actual emitted mass, energy and impulse are not replaced by stored-column quantities.
- 源压力, 动压 and 观测压力 remain distinct. The dynamic-pressure scale is not represented as a target impact peak. The mean 制停压力 bound retains its specified observer area, averaging time, no-reversal and no-extra-actuator conditions.
- The force remains the axial resultant on **one hemisphere**. The full-sphere vector resultant remains zero; no full-sphere integral of pressure magnitude is presented as a net confinement force.
- 新胡克 follows the supplied terminology table. Kelvin–Voigt, PFC, COMSOL and the cited author's name remain recognizable proper names. Identifiers and English words inside mathematical expressions were left verbatim.
- 压力均衡传播 refers only to the timescale diagnostic. It does not introduce a solved spatial propagation or wave field. Necessary transient radial inertia is not presented as an additional oscillation model.
- The first outward-event scope, existing-channel requirement, sealed zero-emission control, no later collapse/rebound calculation, unmeasured permeability/moduli, and declared rather than measured 20% stretch screen remain explicit.
- Transmission ratios remain matched single-shot finite-output comparisons. The energy and impulse ratios are independently integrated, rather than inferred from peak speed.

No translation-specific scientific ambiguity remains unresolved. “Arrest pressure” is rendered 制停压力 to make the stopping operation explicit; “communication” is rendered 压力均衡传播 in accordance with the supplied glossary. The original model's uncalibrated material inputs and unresolved fracture, phase exchange, diffusion and free-surface focusing remain unresolved physics, rather than being bridged by translation.

Only `MODEL_SPEC.zh.md` and this review note were created by this translator. No native model, script, asset, shared log or other translator's file was changed. No task-generated build intermediates were created.
