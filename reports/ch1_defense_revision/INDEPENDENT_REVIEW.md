# Independent scientific and editorial review

Reviewed: 2026-10-19. Reviewer: separate review subagent.

## Executive outcome

All 33 current groups contain multiline derivations. Each has paired English/Chinese premises and checks. The common equation wrapper inserts the derivation into the formula column. The examined scientific chains have consistent algebra, dimensions and signs. All six review findings are resolved. The source-level scientific and multiline-derivation review passes within its stated scope.

This is a source-level scientific review. Browser rendering, deployment, and offline forwarding were outside this review. Calculations were recomputed independently after source inspection. A blinded first-principles review before seeing answer lines was not performed.

## Final layout-formatting confirmation

Read-only review confirmed the later formatting changes preserve all final relations. Splitting top-level `\qquad` summary separators replaces spacing and adjacent punctuation with gathered line breaks. It removes no mathematical operand, equality, implication, condition, integration bound, or definition. An AST check found all 33 original equation calls and verified separator-only preservation for automatically split summaries.

The three explicit replacements were compared semantically against their original results:

- E05 retains wall-pressure/inertia equality, the Eulerian potential derivative, wall kinetic term, and `3/2` coefficient.
- E21 retains pressure-gradient impulse, the negative convective integral, positive viscous integral, endpoint velocity-difference definition, and `ν=μ/ρ`.
- E28 retains potential velocity, Laplace equation, material-marker motion, both Eulerian/material dynamic conditions, their opposite kinetic-term signs, and interface-location restriction.

Intermediate derivation mathematics remains unchanged. The scientific source-review PASS and all-six-findings-resolved disposition remain valid. Numerical recomputation was unnecessary for these presentation-only changes. Browser layout verification remains the main task's responsibility.

Latest reviewed source SHA-256:

- content/chapter01.py: `0bbec794712d76babd2acc5e6a27588cdc9b7694a36c208f9f44eac2de947189`
- content/chapter01_steps.py: `5a93849296001869bf931d19297acd18a12c6d27c4c286f28771bbce10fb187d`

## Final disposition: PASS within source-review scope

Read-only confirmation verified both final refinements. E13 now states `I(Rmax)=1`, shows the definite logarithmic integral, and explicitly exponentiates. The logarithms have positive dimensionless arguments. E27 now substitutes the full stress-tensor difference and displays normal/tangent inner products before scalar projection. Their bilingual local symbol declarations remain complete.

**All six review findings are resolved.** All 33 groups contain multiple derivation rows inside their formula column. They retain paired EN/ZH premises, definitions, derivations, checks, and interpretations. The handoff's multiline derivation instruction and the owner's explicit formula-column clarification are satisfied at source level. The general interface tensor remains necessary and does not restore the deleted independent strain-tensor/dissipation calculation.

No further production changes are requested by this independent review. Frontend/browser, numbering across generated assets, and publication evidence remain separately verified by the main task. This PASS makes no physical PFC experimental-validation claim. Historical findings below describe earlier snapshots.

Final source SHA-256:

- content/chapter01.py: `778935cd3b8ade10d77edc0dfc57948236e22e26e89b9a667bacf31a584cf2d0`
- content/chapter01_steps.py: `5a93849296001869bf931d19297acd18a12c6d27c4c286f28771bbce10fb187d`

## Follow-up disposition

Reread the repaired source and rechecked all 33 groups. E02 now derives spherical divergence from shell-flux balance. E05 now displays the component convection identity and zero vector Laplacian identity. E06 now derives signed curvature using a radially constant unit-normal extension. E33 now separates 7.5 nominal crossings from zero-rise-time acoustic fronts. **All four original findings are resolved.** E27 may reuse E06’s curvature calculation; repeating it is unnecessary.

Two final explicit-step refinements were communicated to the author:

- E13: state the integrating-factor normalization. The logarithm is dimensionally valid because both arguments are dimensionless. Display the definite integration from `Rmax` to `R`, impose `I(Rmax)=1`, and then exponentiate. The current transition silently selects the arbitrary multiplicative constant.
- E27: display the stress substitution before projection. Use `(Tg−Tl)n=[(pl−pb)I−2μD]n`. State `n·n=1` and `s·n=0`, then project. This exposes the normal and tangential scalar equations already written correctly.

No substantive algebra, sign, dimensional, bilingual-parity or physical-closure error was found. The local symbol declarations cover the newly introduced Cartesian indices, sum, shell thickness, curvature operators and gauge function. The zero-vorticity identity and smooth-field derivative interchange have their assumptions stated.

The original review findings and coverage table below are retained as historical review evidence. Their “needs expansion” entries describe the initial reviewed snapshot.

Follow-up source SHA-256:

- content/chapter01.py: `778935cd3b8ade10d77edc0dfc57948236e22e26e89b9a667bacf31a584cf2d0`
- content/chapter01_steps.py: `6ebb32119eb00b9c4b390f37a5df254bc685673070bb648d55899f25979ee877`

## Inputs and snapshot

Read the complete handoff, examiner questions, `content/chapter01.py`, and `content/chapter01_steps.py`. Applied the Math-Rigor audit instructions. No literature search, simulation, controller, production edit, commit, or publication was performed.

Initial source SHA-256:

- chapter01.py: `a58db2b43c96951889410a1d9554fbf19fc695b48351afa014f2394bdb2449a2`
- chapter01_steps.py: `0a5dbbb3393c08121685f0afc0c914522c6328a6eb0fce209a58f548ac9a2bd9`

## Actionable findings

1. **E02: derive spherical divergence rather than start from it.** The handoff explicitly requests its derivation. Start from shell outward flux `4π(r+dr)²u(r+dr)-4πr²u(r)=0`. Divide by `4πdr`, take the limit, and divide by positive `r²`. This shows the geometric origin of the displayed divergence. Define `dr` before use in both languages.
2. **E05: expose the identities used to integrate momentum.** The convection-to-gradient identity is asserted. Add a Cartesian component expansion using irrotationality, or the radial calculation `u ∂r u = ∂r(u²/2)`. The claimed zero bulk viscous term needs `∇²(u e_r)=[u_rr+2u_r/r-2u/r²]e_r`; insert `u=C/r²` and show `(6-4-2)C/r⁴=0`. Keep viscous wall traction distinct.
3. **E06/E27: show the signed-curvature calculation.** Both assert `κ=-2/R`. From `n=-e_r`, use `∇s·n=(I-nn):∇n`; for a sphere derive `∇n=-(I-e_r e_r)/R`, so `κ=-tr(I-e_r e_r)/R=-2/R`. This resolves a substantive sign-convention transition without restoring deleted strain-tensor dissipation exposition.
4. **E33 answer prose: separate total duration and rise time.** “Several crossings support communication during the pulse” weakens the correct E24 warning. A rectangular pulse has zero ideal rise time. Replace this sentence with: the duration permits 7.5 nominal crossings, but its discontinuous fronts require acoustic treatment; a finite-rise history needs the independent E30 test. Keep English/Chinese equivalent.

## Independent scientific reconstruction

The liquid-to-gas normal is inward at a cavity. Therefore `κ=-2/R`. Normal projection of `(Tg-Tl)n=σκn` gives `pl-pb-2μ n·D n=σκ`. With radial `∂r u=-2Rdot/R`, this gives `pl=pb-2σ/R-4μRdot/R`. The dynamic potential condition consequently contains `-σκ`; the spherical capillary term is stabilizing. The current signs agree.

Continuity gives `u=R²Rdot/r²`. Its potential is `φ=-R²Rdot/r`. Fixed-position differentiation gives `∂tφ|R=-2Rdot²-RRddot`. Euler integration with the infinity gauge gives `(pl-p∞)/ρ=RRddot+3Rdot²/2`. This reproduces E05–E07.

Whole-exterior kinetic energy is `(ρ/2)4πR⁴Rdot²∫R∞r⁻²dr=2πρR³Rdot²`. Differentiation yields `dK/dt=4πρR²Rdot(RRddot+3Rdot²/2)`. Multiplication of RP by `4πR²Rdot` yields E11, including nonnegative loss `16πμR Rdot²`. This remains mechanical energy.

For constant collapse pressure, setting `y=Rdot²` gives `y'+3y/R=-2Δpc/(ρR)`. Multiplying by `R³`, integrating from `Rmax`, and imposing `y(Rmax)=0` gives `y=(2Δpc/3ρ)[(Rmax/R)³-1]`. Inward motion selects the negative root. The reciprocal-speed integral yields `Ct=B(5/6,1/2)/sqrt(6)`. Pressure work independently gives `K=Δpc(Vmax-V)`.

At fixed position, direct integration of every Navier–Stokes term gives the stated exact E21 velocity increment. Uniform reference pressure disappears under the spatial gradient. Dropping residual integrated accelerations is an approximation. Endpoint divergence freedom then yields the reduced Laplace impulse problem. The two-end column solution gives `Π=Π0(1-z/L)` and `Δuz=Π0/(ρL)`.

At a material interface marker, `dφ/dt=∂tφ+u·∇φ=∂tφ+|u|²`. Thus the kinetic term changes from `-|u|²/2` to `+|u|²/2`. E28 and its spherical recovery agree. Prescribed bubble pressure and complete boundary/initial data provide conditional mechanical closure. Physical PFC phase/thermal closure remains explicitly unresolved.

Linearized continuity, momentum, and `p'=c²ρ'` give `p'_tt=c²∇²p'`. One-way travel is `Le/c`; the separate pressure-change time gives `Ce=Le/(cτe)`. The current operational examples distinguish this from wall Mach number correctly.

## Numerical reproduction

Executed Python with independent SciPy adaptive quadrature of `sqrt(3/2)∫0¹x^(3/2)/sqrt(1-x³) dx`. Recomputed the worked examples directly from SI inputs.

| Quantity | Independently computed |
|---|---:|
| Collapse coefficient | 0.9146813564901628 |
| 30 μm collapse time | 2.74404406947049 μs |
| Pressure-work energy | 11.3097335529233 nJ |
| Half-radius wall-speed magnitude | 21.6024689946929 m/s |
| Mach-cutoff radius fraction | 0.143487403118193 |
| Column pressure impulse | 0.30 Pa s |
| Column speed increment | 3.0 m/s |
| 100 μm acoustic crossing time | 66.6666666666667 ns |
| Communication ratio, 10 ns rise | 6.66666666666667 |
| Communication ratio, 1 μs rise | 0.0666666666666667 |

All agree with the current displayed precision. Numerical agreement verifies arithmetic within the adopted models. It supplies no experimental validation.

## All-group coverage

“Rows” counts derivation rows before the additional original result. All groups have EN/ZH premises and checks. Every source-level group was inspected semantically.

| Group | Rows | Scientific/editorial assessment |
|---|---:|---|
| E01 | 3 | Prescribed data correctly distinguished from consequences. |
| E02 | 4 | Result correct; shell-flux origin needs expansion. |
| E03 | 5 | Potential, gauge, topology and role explained. |
| E04 | 4 | Eulerian and moving derivatives consistent. |
| E05 | 7 | Bernoulli chain correct; intermediate identities need expansion. |
| E06 | 4 | Stress and capillary signs correct; curvature needs derivation. |
| E07 | 4 | RP substitution and static limit correct. |
| E08 | 3 | Ideal mixture is identified as a conditional closure. |
| E09 | 5 | Shell measure, limits and energy correct. |
| E10 | 4 | Product rule and moving-boundary dependence correct. |
| E11 | 4 | Mechanical power, surface storage and viscous loss correct. |
| E12 | 4 | Ideal collapse assumptions and inward acceleration correct. |
| E13 | 5 | Integrating factor and turning-point restriction correct. |
| E14 | 4 | Initial constant and negative branch correct. |
| E15 | 4 | Reciprocal-speed bounds and differential correct. |
| E16 | 5 | Beta Jacobian, exponents and coefficient correct. |
| E17 | 5 | Density cancellation and independent work correct. |
| E18 | 6 | SI conversion and numerical example correct. |
| E19 | 6 | Mach threshold inversion and interpretation correct. |
| E20 | 5 | Fixed observer and surface impulse distinction correct. |
| E21 | 4 | Time integration and gradient interchange correct. |
| E22 | 4 | Residual scaling and conditional Laplace reduction correct. |
| E23 | 5 | Column boundary constants and sign correct. |
| E24 | 6 | Arithmetic correct; rectangular acoustic warning present. |
| E25 | 5 | Angular cancellation and geometry distinction correct. |
| E26 | 5 | Newtonian constitutive origin and bulk equations correct. |
| E27 | 5 | Stress projection and kinematics correct; curvature needs calculation. |
| E28 | 7 | Conditional closure and material derivative correct. |
| E29 | 4 | Inviscid spherical recovery correct. |
| E30 | 8 | Acoustic derivation and operational contrast correct. |
| E31 | 4 | Oral pressure/inertia chain correct. |
| E32 | 4 | Oral collapse chain and conditional limits correct. |
| E33 | 5 | Oral impulse chain correct; duration/rise-time prose needs repair. |

## Bilingual and scope audit

The EN/ZH explanations preserve the same assumptions, signs, omissions and interpretations in the inspected snapshot. All 33 expansions include both languages. Local definitions precede the formula through the shared wrapper. No original deleted E12 tensor-component/dissipation exposition remains in the current Chapter 1 source. The general tensor in E27 is needed for spatial interface traction. It is distinct from the deleted redundant calculation.

Bilingual browser behavior, equation wrapping, KaTeX rendering and symbol-panel extraction need the main agent's separate frontend verification. This review cannot certify source metadata parity generated elsewhere.

## Remaining limitations

No new physical PFC validation was attempted. The adopted models require their stated pressure input and geometry. Actual thermodynamic/phase kinetics, topology changes and impact loading remain outside these derived benchmarks. External source-to-claim verification was not repeated. Existing citations need the main task's source audit.
