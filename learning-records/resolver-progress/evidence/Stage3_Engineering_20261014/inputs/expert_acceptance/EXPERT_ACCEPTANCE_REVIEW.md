**Overall verdict: PARTIALLY_RESOLVED.** The clarified question is solved for the declared mathematical energy/contact ceilings and a Rayleigh collapse stopped at a prescribed positive radius. The submission does **not** establish the highest attainable pressure or jetting velocity of the conditional PFC cavitation benchmark. Its PFC results are a sampled reduced-model envelope, accompanied by correctly disclosed estimates and unresolved endpoints.

This verdict uses “could achieve from cavitation” to require a feasible cavitation trajectory when an attainable maximum is claimed. If the intended question is restricted further to “what upper bound follows from a prescribed work budget, mass and contact law?”, that narrower question is **RESOLVED_CONDITIONALLY**. Missing actual-device measurements are not the reason for the overall partial verdict.

Review date: 11 October 2026. Reviewer: independent scientific acceptance agent. This is not an external human-expert review or experimental validation.

## Scope and evidence references

The user's governing clarification is: “I mean only conditional theoretical solution.” I therefore permit assumed initial conditions, constitutive laws and material parameters, provided they are stated, internally consistent and used within their declared model. An unknown condensation coefficient may be prescribed for a conditional calculation; measuring it is not a prerequisite.

The reviewed answer is T/CONDITIONAL_SOLUTION.md, supported by the 35-page expert report and retained numerical evidence. Its own text distinguishes an energy-admissible maximum from a cavitation-attainable maximum. Earlier elementary-mathematics and delivery checks do not establish the latter.

In this review, E denotes expert_resolution, T denotes conditional_termtex, R denotes their parent Cavitation_Limits_20261011 directory, and A denotes expert_acceptance. These refer to the original read-only workspace directories. In the forwarded packet, the same citations resolve after extracting the supplied evidence archives into evidence/unpacked/expert_resolution and evidence/unpacked/conditional_termtex. The original handoff is supplied separately in evidence. Equation E01 below always means **T/E01**; expert-report equations use **X** identifiers.

| Scope | Verdict | What is established |
|---|---|---|
| Fixed available work, positive prescribed mass, uniform/RMS velocity and declared linear contact | RESOLVED_CONDITIONALLY | Sharp algebraic ceilings in the energy-admissible class, with the required equality assumptions. No cavitation reachability proof is implied. |
| Spherical Rayleigh model, constant positive drive, initial rest, prescribed positive stopping radius | RESOLVED_CONDITIONALLY | Exact maximum inward wall-speed magnitude on that truncated trajectory. This is a wall speed, not a directed jet speed. |
| Fully activated 6 µm PFP/PFH benchmark and its continuous cavitation optimum | PARTIALLY_RESOLVED | Thermodynamic premises and sampled reduced dynamics are developed; feasible compressible focusing/contact and continuous optimization remain unresolved. |
| Pressure observables | PARTIALLY_RESOLVED | Conditional linear-contact and observer bounds are established. Internal mixed-contact and receiver-wave values are estimates; no solved receiver-contact or sensor maximum is supplied. |
| Universal maximum or transfer to an actual device | OUT_OF_SCOPE | Neither is certified. Their absence does not invalidate the accepted conditional theorems. |

## Independent reconstruction of the central results

**1. Energy ceiling and equality.** Let \(E_{\mathrm{av}}\ge0\) be total mechanically available work in joules, relative to the declared reference state, including every accessible initial contribution. Let \(m_{\mathrm j}>0\) be a prescribed participating mass in kilograms, \(U_{\mathrm j}\ge0\) a uniform jet speed in metres per second, and \(K_{\mathrm j}\) its kinetic energy in joules. Then

\[
K_{\mathrm j}=\tfrac12m_{\mathrm j}U_{\mathrm j}^{2}\le E_{\mathrm{av}}
\ \Longrightarrow\
U_{\mathrm j}^{2}\le\frac{2E_{\mathrm{av}}}{m_{\mathrm j}}
\ \Longrightarrow\
U_{\mathrm j}\le\sqrt{\frac{2E_{\mathrm{av}}}{m_{\mathrm j}}}.
\]

For a nonuniform velocity field, the same expression bounds its mass-weighted RMS speed, with the corresponding kinetic-energy definition. It also bounds the speed of a specified mass moving at least that fast. It does not bound an unrestricted point tip merely by inserting an arbitrary mass. Equality requires all available work in that defined jet and no remaining accessible energy or dissipation. A uniform energy-admissible state attains equality in that algebraic class; the submitted work does not construct a PFC collapse attaining it. Units of energy/mass are m²/s². The ceiling vanishes with zero work and increases without a finite point-speed cap when the prescribed mass tends to zero.

For thermal preparation, absorbed or incident optical energy must not be substituted for available work without the appropriate budget argument. E/tex/04_thermo.tex, X3–X8, supplies the first/second-law availability result for its stated reservoir, reference, nonnegative residual and no-external-work assumptions. The direct numerical PFC evaluations below support the adopted activated-state budgets, separately from the subsequent reduced trajectory.

**2. Linear planar normal contact.** Let \(\rho>0\) be jet density in kg/m³, \(c>0\) its small-signal sound speed in m/s, \(Z_{\mathrm j}=\rho c>0\) its impedance in Pa·s/m, and \(Z_{\mathrm t}\ge0\) the opposing impedance in the same units. Initially the jet moves normally at \(U_{\mathrm j}\), the opposing medium is at rest, and both have the same ambient pressure. Let \(v\) be interface velocity and \(\Delta p_{\mathrm c}\) the pressure increment in pascals. Before release, the declared linear half-space law gives

\[
Z_{\mathrm j}(U_{\mathrm j}-v)=Z_{\mathrm t}v,\qquad
v=\frac{Z_{\mathrm j}}{Z_{\mathrm j}+Z_{\mathrm t}}U_{\mathrm j},\qquad
\Delta p_{\mathrm c}=\frac{Z_{\mathrm j}Z_{\mathrm t}}{Z_{\mathrm j}+Z_{\mathrm t}}U_{\mathrm j}.
\]

Pressure is monotone in speed, so inserting the energy ceiling gives T/E07. The rigid limit is \(Z_{\mathrm j}U_{\mathrm j}\); equal impedances give \(Z_{\mathrm j}U_{\mathrm j}/2\). No extra reflection factor belongs in an already matched contact pressure. The approximation needs small compression and a planar normal contact interval before lateral or finite-length release. It is not an exact nonlinear shock ceiling.

For the illustrative plug, radius \(a=3\,\mu\mathrm m\), length \(L=50\,\mu\mathrm m\), density \(1000\,\mathrm{kg/m^3}\), sound speed \(1500\,\mathrm{m/s}\), and available work \(5\,\mathrm{nJ}\) give independently:

| Quantity | Recalculated value |
|---|---:|
| Plug mass \(\rho\pi a^2L\) | 1.413716694115 ng |
| Energy-ceiling speed | 84.1044174007 m/s |
| Speed/sound-speed ratio | 0.0560696116 |
| Rigid linear-contact increment | 126.156626101 MPa |
| Equal-impedance linear-contact increment | 63.0783130505 MPa |

These are declared mathematical controls. Even at this relatively low speed, the expert report's different water/Tait constants produce a rigid-contact estimate of 138.462 MPa at 84.1 m/s, versus 124.102 MPa for its own linear constants. Thus 126.157 MPa should remain expressly a **linear-model** ceiling for the illustrative constants.

**3. Prescribed-cutoff Rayleigh trajectory.** Let \(R(t)>0\) be spherical radius in metres, \(R_{\max}>0\) its initial radius, \(0<R_{\min}\le R_{\max}\) the prescribed stopping radius, and \(\Delta p>0\) a constant inward pressure drive in pascals. Time \(t\) is in seconds; dots denote time derivatives. The liquid is infinite, quiescent at infinity, incompressible, inviscid and tension-free, with density \(\rho>0\); content pressure is constant. Initial conditions are \(R(0)=R_{\max}\), \(\dot R(0)=0\), and the selected collapse branch has \(\dot R<0\) thereafter. Define \(q(R)=\dot R^2\), in m²/s². Away from initial rest, the chain rule gives \(q'=2\ddot R\); the first integral extends continuously to initial rest:

\[
\frac{R}{2}q'+\frac32q=-\frac{\Delta p}{\rho},\qquad
(R^3q)'=-\frac{2\Delta p}{\rho}R^2,\qquad
q=\frac{2\Delta p}{3\rho}\left[\left(\frac{R_{\max}}{R}\right)^3-1\right].
\]

I independently differentiated this expression and substituted it into the governing equation; the symbolic residual is exactly zero and \(q(R_{\max})=0\). Since \(q'=-2\Delta pR_{\max}^3/(\rho R^4)<0\), the maximum inward wall-speed magnitude on the specified interval occurs at \(R_{\min}\), as T/E20 states. It vanishes when the two prescribed radii coincide. Its divergence as \(R_{\min}\to 0\) is the singular endpoint of that ideal model, not a physical maximum. This interpretation agrees with the author-hosted [Brennen Chapter 2](https://media.library.caltech.edu/CaltechBOOK:1995.001/chap2.htm), which discusses the breakdown of incompressibility and spherical symmetry at collapse.

## Required claim ledger

“Accepted conditionally” means accepted within stated hypotheses. “Prediction only” and “estimate only” do not certify a physical optimum.

| ID / submitted claim | Status | Inspected evidence and finding |
|---|---|---|
| C01. Energy velocity ceiling | ACCEPTED_CONDITIONALLY | T/E01–E03; E/tex/04_thermo.tex, X3–X8; E/tex/01_setup.tex, O2. Correct for positive prescribed participating mass, uniform/RMS speed or mass-qualified speed and a complete available-work budget. Equality is energy admissibility; cavitation attainability remains separate. |
| C02. Linear contact and its maximum | ACCEPTED_CONDITIONALLY | T/E04–E09; E/tex/07_receiver.tex, P1/P4, PDF pp.25–26. Algebra and rigid/equal limits are correct. Small-compression, normal planar contact and pre-release applicability are required. No second reflection factor in matched contact. |
| C03. 5 nJ illustrative plug | ACCEPTED_CONDITIONALLY | T/E10–E12 and its stated numerical assumptions. All five values above independently reproduced. This is neither a computed PFC plug nor a nonlinear-contact upper bound. |
| C04. Rayleigh positive-radius cutoff | ACCEPTED_CONDITIONALLY | T/E13–E22; E/tex/05_spherical.tex, X22–X23, PDF pp.13–14. Chain rule, integral, initial-rest continuation, sign, units, monotonicity and governing substitution pass. The maximum is truncated spherical wall speed. The positive cutoff is imposed, not derived from PFC physics. |
| C05. Activation, source pressure, availability and cavity radius | ACCEPTED_CONDITIONALLY | E/tex/04_thermo.tex, X11–X17/Proposition 1; data/thermo_ceilings.json, 6 µm rows; verification/psrc_checks.json; PDF pp.10–12. Direct independent HEOS evaluations reproduce activation-state availability 2.7225724/4.6221226 nJ at 386.486/415.237 K. The 1.265/1.085 MPa **absolute expansion-source** ceilings require H0/H2/H4/H5, equilibrium/no overshoot and assumed global EOS signs; they do not bound collapse/contact pressure. The 23.782/24.219 µm radii are numerical evaluations of a conditional stable-EOS availability ceiling, not certified reachable jet optima. Finite EOS-sign samples do not prove the global premises. Constant-hot-state 5 ns CNT hazard gives expected count one, about 63.2% event probability, not deterministic full activation or a demonstrated uniform isobaric laser preparation. |
| C06. PFC jet speeds 65/187 and 360/378 m/s | PREDICTION_ONLY | data/bim_pfc.json and envelope_rows.json; scripts/bim_axisym.py result/run/jet_mass_velocity; scripts/bim_runs.py; E/tex/06_jet.tex, J3/J5/J6, PDF pp.19–24. Slow largest samples are PFP frozen, gamma=1.25, 65.2742 and PFH KM-alpha=0.1, gamma=4, 186.9489 m/s. In-screen fast largest samples are PFP KM-alpha=1, gamma=4, 360.1701 and PFH isoeq, gamma=3, 377.5101 m/s. They are internal far-pole speeds before a 0.01L tip–wall gap, not emitted or arriving jets. Forty cases, 35 valid impact/profile rows, five stand-offs and four discrete closures do not prove a continuous optimum or a bracket over all phase histories. |
| C07. 444.6 m/s screen; 482/715 m/s beyond-screen values | ESTIMATE_ONLY | E/tex/06_jet.tex; envelope_crossings.json; verification/pfc_bim_convergence.json; km_sweep.json; PDF pp.21–24. The screen is 0.3 times the adopted water sound speed. Nominal beyond-screen isoeq/gamma=4 values are 481.5316/715.4791 m/s. Log-linear crossing estimates and Mach-censored KM traces establish reduced-model screening/censoring only. They supply no physical maximum, no demonstrated achieved physical lower bound, and no justified post-screen endpoint. |
| C08. Internal 292/307 MPa; receiver approximately 21/22 MPa | ESTIMATE_ONLY | E/tex/07_receiver.tex, X34–X37; scripts/receiver.py; scripts/extra_tables.py envelope; receiver_table.json and envelope_rows.json; PDF pp.25–26, 29–30. All 35 mixed-contact and spreading rows independently reproduced. Largest in-screen internal estimates are 292.318/307.471 MPa; largest receiver-wave estimates are 21.026/22.369 MPa and arise at different cases. The nonlinear jet/linear opponent closure is not symmetric nonlinear two-water impact, and barotropic Tait replaces a full energy Hugoniot. Spreading/reflection is an assumed wave estimate. No direct target-contact trajectory or sensor peak is solved. Conditional linear observer bounds X36–X37 are accepted separately. |
| C09. Prescribed 10 pg energetic allowances | ACCEPTED_CONDITIONALLY | T/E23–E24; T discussion of prescribed mass and attainability. With rounded budgets 2.72/4.62 nJ and additional mass 10 pg, independent speeds are 737.5636/961.2492 m/s. These are uniform/RMS or mass-qualified energetic allowances. Neither the PFC trajectory nor that participating fast mass is constructed; contact at these speeds needs a compressible model. |
| C10. Numerics/conservation | PREDICTION_ONLY | Raw BIM original/refinement/stabilization/extra files; verification/pfc_bim_convergence.json, km_refine.json, km_refine_summary.json, km_energy_conservation.json, bim_unit_tests.json; bubble_km.py phase switch/ledger; PDF pp.15,21–24,33–34. Independent raw-row checks confirm the reported sensitivities and failed-attempt exclusions. Kernel/Rayleigh/mechanical tests support implementation, not full thermochemical validation. The negative PFP growth exergy remainder and pressure-only phase switch prevent a closed physical feasibility certificate. Claiming complete thermochemical conservation would require correction. |
| C11. Closure of the clarified question | UNRESOLVED | T explicitly separates attainability; E/tex/09_envelope.tex and E/tex/10_program.tex; README; final NEXT_AGENT_HANDOFF addendum. Conditional mathematical ceilings are resolved. A continuous attainable PFC cavitation/pressure optimum is not. The missing step is a consistent feasible trajectory and an optimization certificate in a specified regularized design class, not merely actual-device calibration. |

The source-pressure numerical values in C05 are conditional **EOS extrapolation values** when the metastable spinodal branch is invoked. Acceptance of the hypothetical equilibrium/sign assumptions does not establish them as experimentally verified material ceilings. The primary [CoolProp PFP documentation](https://coolprop.org/fluid_properties/fluids/n-Perfluoropentane.html) and [PFH documentation](https://coolprop.org/fluid_properties/fluids/n-Perfluorohexane.html) identify the Gao EOS and its nominal limits; they do not certify metastable-spinodal accuracy.

## Coverage of all 24 equations in the current answer

All actual text grids in T/CONDITIONAL_SOLUTION.md match their corresponding saved grids in T/equations.json exactly. I compared the authored LaTeX expressions, layout/engine records and displayed grids, and reconstructed the mathematical content. This check does not claim visual observation of the user's chat renderer.

| T equation | Independent finding |
|---|---|
| E01 | Correct energy inequality for the declared uniform mass; the RMS extension needs its appropriate integral definition. |
| E02 | Correct multiplication by 2 and division by positive mass. |
| E03 | Correct nonnegative square root; “max” denotes the energy-admissible class. |
| E04 | Correct impedance dimensions and linear initial-contact matching. |
| E05 | Correct interface-velocity solution; denominator is positive because jet impedance is positive. |
| E06 | Correct substitution and effective impedance. |
| E07 | Correct monotone composition within the linear law's applicable speed range. |
| E08 | Correct rigid-impedance limit. |
| E09 | Correct equal-impedance limit; pressure increment is half the rigid value. |
| E10 | Cylinder mass independently reproduced; kg-to-ng conversion correct. |
| E11 | Independent energy-ceiling speed 84.1044174 m/s. |
| E12 | Independent Mach ratio 0.0560696; a scale check, not a proof of exact linearity. |
| E13 | Correct governing Rayleigh equation under the stated inviscid, tension-free, incompressible constant-drive assumptions. |
| E14 | Chain rule correct on the monotone collapse branch; division by wall velocity cannot be performed at initial rest, handled by continuation. |
| E15 | Correct substitution and multiplication by 2. |
| E16 | Product rule and integrating factor correct. |
| E17 | Correct oriented limits from initial radius to the smaller current radius. |
| E18 | Correct antiderivative and initial boundary term. |
| E19 | Correct use of initial rest and division by positive radius cubed. |
| E20 | Correct maximum wall-speed magnitude at a prescribed positive minimum radius. |
| E21 | Correct derivative; strictly negative for positive drive and radii. |
| E22 | Governing-equation substitution gives exact zero residual. |
| E23 | Correct rounded 737.5636 m/s allowance for 2.72 nJ and prescribed 10 pg, displayed approximately 738. |
| E24 | Correct rounded 961.2492 m/s allowance for 4.62 nJ and prescribed 10 pg, displayed approximately 961. |

## Findings ranked by effect on acceptance

**Blocking B1 — no attained continuous cavitation optimum.** The algebraic maximizing state is not shown to lie in the reachable set of a PFC collapse. The numerical jets are a 6 µm, 5 ns hazard, air-free water slice, not an optimization of the broader design set X2; even that slice is sampled at five stand-offs and four prescribed content laws. No existence/attainment proof, global search with a justified error certificate, or proved phase-history envelope closes the supremum. The current report candidly discloses this. The issue blocks calling its values the highest attainable cavitation output, not acceptance of its bounds.

**Blocking B2 — the fast/end-contact trajectory lacks a consistent physical closure.** Keller–Miksis stops at Mach 0.3; incompressible BIM carries fast samples beyond its working screen and stops before contact. Importing a spherical pressure–volume record, continuing it as inverse volume, and using a subsequent contact estimate does not construct the compressible asymmetric collapse/contact event. For the thermochemical trajectory, the real-EOS-to-ideal-vapour switch preserves pressure but does not establish energy/entropy-reference continuity. For the frozen 6 µm PFP control, the growth ledger's exergy remainder is −0.0717339 nJ, or −2.63478% of the activated budget; physical exergy destruction cannot be negative. Neither a residual-defined radiation term nor a small mechanical bookkeeping residual repairs this. These limits block a physical feasibility/maximum certificate; the standalone availability theorem survives.

**Material qualification Q1 — sampled axial energy is labelled as jet kinetic-energy partition.** In scripts/bim_axisym.py, jet_mass_velocity stores speed as the negative axial velocity component and E_kin as half the sum of mass times that component squared. It omits the radial component and excludes near-interface quadrature points. E/tex/06_jet.tex, energy-partition text/J6, and the envelope tables call the resulting ratio a fraction of jet kinetic energy or say the jet “carries” that fraction. The saved quantity is specifically **sampled axial kinetic energy**, not full vector jet kinetic energy. Its values and axial-energy identities reproduce correctly. Total-vector partition/conservation wording requires correction or a complete vector calculation. This finding does not invalidate the energy inequality or the pole-speed samples.

**Material qualification Q2 — pressure estimates are not pressure maxima.** X34 imposes exact mass/momentum jumps with a Tait isentrope in place of the full thermodynamic Hugoniot; its limitations are stated. The opposing medium is treated linearly in the mixed contact calculation. A1-style small-signal reflection and spherical spreading cannot resolve a toroidal nonlinear wave, cavity scattering, target loading or observer response. The reported approximately 1 ns release times also use an approximate geometric/acoustic scale. These numbers must retain their estimate labels and pressure references. No receiver/sensor optimum is accepted.

**Material qualification Q3 — conditional premises are stronger than finite checks.** Full uniform isobaric preparation is assumed, not obtained from the 5 ns hot-state hazard. Homogeneous CNT, temperature-extrapolated interfacial tension and metastable EOS accuracy are constitutive choices. H5 excludes nonequilibrium overshoot; finite derivative/monotonicity samples in psrc_checks do not certify every point of the assumed domain. The evaluated source ceiling is confined to expansion. Conditional theory may adopt these premises, but must not describe their numerical checks as proving physical material validity.

**Material qualification Q4 — convergence is uneven and quantity-specific.** Independent raw-data recomputation gives:

- Valid original 64→96 same-cap BIM speed change up to 4.7375867%; three requested 96/0.02 attempts abort.
- Original64-grid cap-halving change up to 0.3065408%.
- Four successful 64→96 cap 0.01 comparisons change speed by at most 0.3207392%; these are distinct tests, not replacements for the aborted same-cap pairs.
- Selected PFH KM-alpha=1/gamma=4 at 96 nodes changes speed 4.9107159%, sampled axial energy 8.8663648% and coverage 4.6596048% when the cap is halved.
- The 128-node follow-up aborts before impact; its raw 133.7734 m/s diagnostic is correctly excluded.
- Selected spatial profile changes reach 35.9214986% in retained mass and 7.8843277% in sampled axial energy.
- PFP-alpha=0.3 KM 160→320 changes the uncensored wall speed 2.5937128%; all six refined cases have the ideal-vapour warning.
- The finest 96-node constant-pressure benchmark discrepancies are −5.92769% to −3.40426% against the retained Supponen table interpolation. This is benchmark discrepancy, not a mesh error or validation of the PFC closure.

Equal Mach-stop speeds are imposed event values, not converged physical peak speeds. Original failures are retained honestly, and the report appropriately separates them from targeted successful controls.

**Editorial E1 — broad hazard-interval range differs between tables.** X2/Section 1.5 gives 1 ns–1 µs; the parameter ledger prose gives 1 ns–1 ms. This does not affect the fixed 5 ns examples or the overall verdict, but a future continuous optimization must specify one domain consistently.

## Smallest theoretical work needed for full conditional closure

Two completion routes should remain explicit. The **ceiling-only route is already complete**: retain T/E01–E24 and their assumptions, call the quantities conditional mathematical ceilings, and decline cavitation attainability. The following tasks are needed only to answer the stronger “highest one could achieve from cavitation” interpretation.

| Task | Required input / work type | Completion check |
|---|---|---|
| T1. Fix the conditional reachable class and objective | Chosen assumptions: select one species, fixed budget/prepared state, positive mass-qualified or RMS objective, geometry/stand-off interval, phase-transfer law, and regularization/contact event. For pressure, select source, internal contact, receiver-wave or declared area/time observer. | A single consistent initial/boundary-value problem and parameter domain; finite observation/mass scales; explicit reason a maximum exists or a supremum is the appropriate object. Assumed preparation is acceptable. |
| T2. Close phase energetics and the fast trajectory | New derivation/computation: use a compatible energy/entropy reference through phase transitions; choose and couple a compressible asymmetric carrier/content model, and include viscosity if part of the declared class. A restricted analytic regularized model is also acceptable if it has a solved feasible trajectory. | Mass, full energy and entropy accounting close independently within a justified numerical error; no unexplained negative exergy destruction; selected event is reached without a validity-stop extrapolation. Measuring the real condensation coefficient is not required if it is prescribed. |
| T3. Establish the attainable optimum | New proof/computation: construct feasible candidate trajectories in the T1 domain; optimize continuously or prove monotonicity/global bounds. Evaluate participating mass/full profile consistently, rather than relying on an unrestricted tip or sparse envelope. | Feasible lower value and justified global upper value coincide to a declared accuracy, or an exact theorem establishes attainment; domain boundaries and breakdown branches are accounted for. Mesh/step/event errors are below the claimed optimization uncertainty. |
| T4. Close pressure only if pressure is the selected objective | Chosen receiver/observer law plus new proof/computation: solve the compatible contact/wave problem, with release, propagation and receiver response where included. | Pressure observable and reference remain fixed; feasible trajectory, energy-consistent pressure history and global optimization certificate are supplied. A linear abstract contact theorem alone suffices only for the narrower ceiling class. |

Actual laser absorption, specimen material calibration, heterogeneous nucleation measurements and sensor characterization would be needed for **device transfer**. They are not additional acceptance requirements for a conditional theoretical model. Gel rupture/direct ejection need not be solved if the accepted conditional architecture excludes them explicitly.

## Approved short answer to the clarified question

> Under stated conditions, a finite theoretical ceiling can be given. If the mechanically available work is \(E_{\mathrm{av}}\) and the prescribed jet mass is \(m_{\mathrm j}>0\), its uniform or mass-weighted RMS speed satisfies \(U\le\sqrt{2E_{\mathrm{av}}/m_{\mathrm j}}\). Under planar linear normal contact, the pressure increment is bounded by \([Z_{\mathrm j}Z_{\mathrm t}/(Z_{\mathrm j}+Z_{\mathrm t})]\sqrt{2E_{\mathrm{av}}/m_{\mathrm j}}\), where the two \(Z\)'s are acoustic impedances. For the declared 5 nJ, 3 µm-radius, 50 µm-long water plug, this gives 84.10 m/s and 126.16 MPa at a rigid receiver, or 63.08 MPa for equal impedances. These are conditional mathematical ceilings. The 6 µm PFP/PFH calculations predict largest sampled in-screen internal tip speeds of 360/378 m/s; they have not established the highest attainable cavitation speed or pressure under those conditions.

This wording answers the accepted mathematical subquestion and states the remaining cavitation-theory gap. It does not promote the 10 pg allowances, Mach screen or pressure estimates into achieved maxima.

## Verification, sources, limitations and preservation

I read the assignment and current manifest, scope/current-answer documents, completion addendum, all 35 PDF pages, master and listed LaTeX sources/macros/tables, parameter/result ledgers, retained data and numerical-validity records. Implementation inspection covered the available-work/phase equations, phase switch, potential-flow event/profile definition, contact law, and every relevant aggregation/filter/refinement portion of the nine listed Python scripts. Large numerical JSON files were parsed and relevant rows/arrays traced; no scientific sweep was repeated. The JSON review lists all 82 inventoried files with inspection scope.

Independent checks used Python with bytecode creation disabled, SymPy, standard JSON/math/hash/ZIP tools, SciPy scalar root finding and direct CoolProp8.0.0 state evaluations. No submitted solver, report generator or COMSOL job was executed. Key results:

- Symbolic Rayleigh and contact residuals exactly zero; correct initial and limiting states.
- Independent plug and 10 pg arithmetic above.
- Direct liquid-phase HEOS states reproduced the two activated budgets without importing submitted code.
- All 35 valid envelope profile mass sums and sampled axial-energy identities reproduced; case/event/filter meanings checked against implementation.
- All 35 pressure rows reproduced through an independent compression-ratio root, rather than the submitted shock-speed root implementation; maximum relative discrepancy below 3.9×10⁻¹³.
- Refinement sensitivities, original-data preservation comparisons and excluded aborted branches traced/recomputed as detailed above.
- All 24 saved Math-TermTex grids matched the Markdown grids. Existing PDF/reader/relocation audits were inspected as presentation evidence; I did not repeat browser or every-page visual layout tests. No presentation inconsistency found changes the scientific conclusion.

Source checks used the retained local extracts and provenance and primary online documents. [Supponen2016](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/scaling-laws-for-jets-of-single-cavitation-bubbles/D80ECE02832AFE259B522055298B5FD3) and its retained author manuscript support the internal pre-impact jet definition and the conditional potential-flow benchmark; they do not certify the PFC phase closure. [Supponen2017](https://arxiv.org/abs/1708.04049), local Eq.4 and discussion, supports the low-Mach liquid/liquid factor and its stated limitations. [Lechner2020](https://arxiv.org/abs/2005.05733) supports the adopted Tait parameters and the distinction between conventional and near-wall annular-collision jets. [Reuter and Ohl2021](https://d-nb.info/1265094349/34) describes an approximately millimetre-scale near-wall needle jet traversing gas; its reported high speed is not a PFC benchmark maximum. The [Gao EOS record at NIST](https://www.nist.gov/publications/equations-state-thermodynamic-properties-three-perfluorocarbons-n-perfluorobutane-n) and the linked official property documentation confirm the EOS provenance and limited validity context. A DOI-resolver tool error for Supponen2016 was bypassed by the publisher page and available local author manuscript; no decisive premise was inaccessible.

The forwarded licensed archive intentionally omits four local extracts: Brennen1995_chap2.txt, Supponen2016.txt, Supponen2017.txt and Lechner2020.txt. I had read-only access to those originals. Their provenance/primary references and THIRD_PARTY_NOTICES remain in the packet; it should not be described as containing those four full texts. ZIP CRC checks passed for both input archives.

All 82 updated manifest inputs match their listed SHA-256 values. The complete authoritative scientific trees retain their initial counts and aggregate hashes (sorted relative-path/SHA pairs encoded as compact JSON):

| Tree | Files | SHA-256 |
|---|---:|---|
| E |233|daf6071825833ac613f67f8995d64ba723d459a765902e1087a0b9517787f91a|
| T |23|c9e7276d5fe03b1b905c634995f8f47460cc8eaeb91d5ad4dbe520a26959573e|

The final acceptance-prompt hash is 34b3ce693fa9c8ebb4b00ded5503146032b4cf46e621e146d7c2afb5273ee904. The original report PDF, reader and both input ZIP hashes also match the retained manifest. Root's prompt/manifest licensing clarification was observed separately from scientific inputs.

I wrote only EXPERT_ACCEPTANCE_REVIEW.md, EXPERT_ACCEPTANCE_REVIEW.json and REVIEW_WORK_LOG.md in A. No evidence file, prior audit, archive, model or scientific input was changed, no Git commit was made, and no temporary build artifacts were created. Root owns shared-project logging and packaging.
