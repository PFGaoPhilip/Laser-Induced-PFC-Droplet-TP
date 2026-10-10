# Independent semantic review — Chinese model specification

Reviewed the complete `MODEL_SPEC.zh.md` against `MODEL_SPEC.md`: architecture and assumptions, symbol glossary, all nine derivation steps, and the final capability/experimental-verification statements. Root's existing comparison establishes that all 257 mathematical expressions match; this review instead examines the meaning and completeness of the surrounding definitions, derivation explanations and qualifications. It is not a new simulation or independent validation of the material laws.

No substantive scientific mistranslation or omitted scientific assumption was identified:

- The finite post-activation source, zero mechanical initial velocities, closed adiabatic ideal-gas control, constant densities, open-channel requirement and exclusion of nucleation, conversion, phase exchange, rupture, collapse jets and later rebound are retained. The actual PFC EOS and material properties remain uncalibrated.
- E01–E05a preserve distinct chamber-growth and discharge volumes, separate liquid inventory and effective inertance, absolute source/ambient pressures, finite work above ambient, pressure-law derivation and monotone work inversion. Mechanical availability remains distinct from incident or absorbed optical energy.
- E06–E08a preserve the constant-meniscus approximation, fitted losses, unsteady Bernoulli derivation, outgoing kinetic head and actual emitted-energy/impulse fluxes. Stored column energy/momentum are explicitly distinguished from emitted quantities; the text does not introduce a spatial wave field.
- E09–E15 preserve incompressibility, principal stretches, neo-Hookean stress difference, infinite-medium boundary condition, the integration substitution, recoverable elastic work, limiting checks, radial inertial energy and nonnegative Kelvin–Voigt loss. The pressure plateau is not presented as a fracture limit or useful-jet guarantee.
- E16 preserves the one-hemisphere axial resultant and zero complete-sphere net force. Target-patch force still needs its own area and load path.
- E17–E21 preserve common source-volume coupling, explicit energy cancellation, the emitted-energy accumulator, the conservation-versus-calibration distinction and the five/seven-state normalization in physical time.
- E22a–E24 preserve the potential minimum, conditional column-speed bound, conservation-based mass-weighted emitted-RMS bound, dynamic-pressure bound, observer-area/time requirements, no-reversal/no-extra-actuator arrest assumptions, matched positive denominators and the distinction between peak ratios and integrated outputs.
- E25 and the conclusion preserve diagnostic-only communication, Mach and stretch screens, drainage assumptions, unmeasured permeability/rate dependence, separate sealed-case classification, channel geometry limitations and the absence of a universal maximum prediction.

One inherited wording qualification should be clarified in both languages:

1. **E24 explanatory paragraph, current line 479 in both specifications.** English says “Endpoints can differ because each case has its own first-event maximum or inventory stop”; Chinese faithfully renders this as “由于各算例有各自的首次过程极值或液体存量终止条件，终点可以不同。” A reader can interpret “maximum/极值” as the outlet-speed peak, although the open-case episode actually stops on the first outward-speed return through zero, the inventory limit or a declared screen. This ambiguity originates in the English source, not the translation. Suggested English replacement: “Each open-case episode ends at its first outlet-speed return through zero, liquid-inventory limit or declared validity screen, so matched cases can have different endpoints.” Suggested Chinese replacement: “各开放算例在出口速度首次回落并穿过零、液体存量耗尽或达到已声明的有效性筛查条件时终止，因此匹配算例的终点可以不同。” The prior architecture section and GUI stopping instructions already state the correct conditions; no equation or native model change is indicated.

Optional Chinese editorial refinements:

- **E23 explanatory paragraph, current line 467:** “两个积分分别为排出质量和排出动能的两倍” is consistent with the equation but could read more unambiguously as “第一个积分等于排出质量，第二个积分等于排出动能的两倍。”
- **Arrest-pressure terminology, current lines 49, 454 and 456:** “制停压力” is scientifically understandable. The guide uses “制动压力”; using one term across both documents would improve consistency without changing the mean impulse-based bound or its limitations.

Only this peer-review file was written. No translation, script, asset, native model, other report or log was changed. Line numbers identify the reviewed versions and may shift after integration.
