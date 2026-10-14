# PLAN — stages S0–S9 to an attained, certified conditional optimum

Labels E, T, A, F, R, P, problem IDs P1–P10 and decision IDs D1–D11 are defined in [HANDOFF.md](HANDOFF.md). Gate IDs G0–G11 are defined in [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md). A stage is finished only when its completion criterion holds.

Conventions follow `E\tex\01_setup.tex`:

- Axisymmetric coordinates (r, z); the rigid receiver is the plane z = 0; the cavity centre starts at z = h > 0.
- Stand-off γ = h/R_m, where R_m is the free-field maximum radius of the same activated droplet.
- The directed velocity toward the receiver is w = −u_z.
- Pressures are absolute unless called gauge. Φ_a is the activation exergy (J).

Effort is dominated by S4–S6. Expect several sessions, roughly two working weeks; checkpoint accordingly.

## S0 — Baseline and preservation (≈ 0.5 h)

1. Confirm the Git root `C:\L. Jay Guo` and record `git status --short` in `F\WORK_LOG.md`. The many unrelated modified files belong to other work.
2. Run `python -B tools\tree_hash.py <tree> [--exclude ...]` for the four entries in `BASELINE_HASHES.json` and compare the results.
3. Append a start entry to `F\WORK_LOG.md`.

**Completion criterion:** all four tree hashes match the baseline. If any differs, stop and tell the user that evidence changed before your work began.

## S1 — Declare the conditional problem 𝒫 (≈ 0.5 day plus the user's reply)

1. Ask D6, and confirm D7 and D8, in one structured question. Give the recommendation and its consequence: the pressure optimum is likely to sit on the lower stand-off bound.
2. Write `PROBLEM_STATEMENT.md`, to the user's derivation standard. It contains:
   - **Preparation.** H0–H4 restated as assumptions, with the activated states taken from `E\data\thermo_ceilings.json` and cited.
   - **Governing equations of the declared model class.**
     - Compressible liquid: mass, momentum and total energy, with an EOS whose constants carry sources, plus viscosity and surface tension.
     - The cavity-content model from S2, covering the flash stage (P8).
     - Interface conditions, wall and far-field conditions.
     - Initial state: the activated droplet at rest in quiescent water.
   - **𝒟**, with every bound labelled *physical*, *application* (user-approved) or *model-validity*.
   - **Objectives** J_U(m_*) and J_P(r_o, τ_o), with the exact formulas and events from S3.
   - **Validity indicators**, split into two kinds:
     - *Numerical* indicators must pass: resolution, positivity and clipping interventions, abort, liquid tension beyond the declared cavitation threshold.
     - *Constitutive-domain* indicators may be exceeded only as declared assumptions, with their sensitivity reported (for example, vapour EOS states beyond HEOS's fitted range).
   - **Tolerances** from D9.
   - **Existence argument:** compactness of 𝒟 plus continuity or upper semicontinuity of each J, either proved or labelled as numerically justified. Regime changes such as impact versus no impact are treated as separate closed pieces.
3. Draft `PREREGISTRATION.json`; it is frozen at S6.0.

**Completion criterion:** one document defines a single initial–boundary-value problem and parameter domain. Every symbol is defined before use, every bound of 𝒟 carries a justification label, D1–D11 are recorded, and D6 quotes the user's answer.

## S2 — Content thermodynamics and exergy ledger (fixes P3, P4; ≈ 1–2 days)

Goal: a cavity-content model with one consistent thermodynamic reference from activation to the end of every objective window, and a ledger whose exergy destruction is computed, not inferred.

1. **Diagnose first.** Copy `E\scripts\bubble_km.py` and its dependencies into `F\scripts\` and reproduce the 18 6-µm residuals. Quantify each suspect contribution:
   - (i) the pressure-continuous switch: compute the content's Δu, Δs and ΔΦ across it;
   - (ii) Φ_content evaluated with HEOS at the ideal-model temperature;
   - (iii) condensed PFC assigned zero exergy;
   - (iv) the missing exergy transfer with heat between content and carrier;
   - (v) E_rad defined as a residual;
   - (vi) the mixed energy reference: the content uses ideal-gas u = c_v·T and h_v = c_p,v·T_i (`bubble_km.py:255,276`) while the interfacial latent heat L(T_i) comes from HEOS (line 222);
   - (vii) clipping interventions: the content-temperature floor of 50 K (line 255), and the interface-temperature bounds [150 K, T_c − 0.5 K] with the ±20 K Newton step limit (lines 230–231). Count how often each is active;
   - (viii) anything else you find.

   Write `verification\ledger_diagnosis.json`.
   *Criterion:* the identified contributions explain each of the 18 residuals to ≤ 0.2% Φ_a.
2. **Content model.** Use one EOS reference for every stage. Either:
   - (a) HEOS throughout, via (ρ, u) flashes or pre-tabulated properties; or
   - (b) a vapour model (ideal or Noble–Abel stiffened gas) whose reference constants make p, u and s continuous at the switch. Write out the matching equations, and check the model against HEOS along each trajectory.

   In both cases:
   - Phase transfer is HKS with α_c, with latent heat released at the interface.
   - The interface temperature comes from a declared carrier thermal model driven by the actual interface area, reducing to E's spherical heat-diffusion model in the spherical limit.
   - The cavity volume includes the volume of condensed PFC liquid.
3. **Ledger.** Write the exergy balance of the declared system (content + liquid inside a control surface Σ + rigid receiver) from t = 0 to t:

   Φ_a = Φ_content + K_liquid + Φ_liquid,compression + Φ_thermal-layer + E_surface + E_rad + X_dest + R(t)

   - At t = 0, Φ_content = Φ_a and every other term is zero.
   - K_liquid uses the full vector velocity.
   - E_surface = σ(A(t) − A(0)).
   - E_rad is the flux ∫∫(p − p∞) u·n dS dt through Σ, not a residual.
   - X_dest = T0 ∫ σ_gen dt, accumulated from local sources: viscous dissipation, conduction across finite gradients, HKS interfacial irreversibility, and shock entropy jumps (which require an energy-conserving liquid EOS).
   - R(t) is the residual, and it is the only inferred term.
4. **Spherical test bed.** Rerun the 18 6-µm water cases with the new content model in a spherical solver, to the first volume minimum or the KM Mach event. KM is only a test bed here; state its O(M) radiation term and use it for E_rad.

**Completion criterion:** at every model switch |ΔΦ_content| ≤ 10⁻⁴ Φ_a. In all 18 cases, at every saved time, |R(t)| ≤ 1% Φ_a and X_dest(t) is ≥ 0 and non-decreasing. R decreases under step or grid refinement in two cases. Results are in `verification\ledger_spherical.json`.

## S3 — Observables and errata (fixes P5; ≈ 0.5 day)

1. **Directed mass-qualified speed.** Over the whole liquid domain, with no geometric jet region and no near-interface exclusion:
   - m(≥U, t) = ∫_liquid ρ · 1[w ≥ U] dV;
   - U(m_*, t) = sup{U ≥ 0 : m(≥U, t) ≥ m_*}, taken as 0 when the set is empty;
   - J_U(m_*) = max of U(m_*, t) over t ∈ [0, t_imp].

   t_imp is the first liquid–liquid contact on the axis inside the cavity, i.e. the jet tip meeting the opposite interface. If no impact occurs before the first volume minimum, the window ends there and the regime is recorded.
2. **Kinetic energies.** Report the full vector K = ½∫ρ|u|² dV wherever energy is reported. The directed part ½∫ρw²·1[w > 0] dV is labelled as such. E's geometric-jet quantities are diagnostics only.
3. **Pressure observable O7.**
   - P(r_o, t) = (π r_o²)⁻¹ ∫₀^{r_o} (p_wall(r, t) − p∞) 2πr dr;
   - J_P(r_o, τ_o) = max over t of τ_o⁻¹ ∫_t^{t+τ_o} P(r_o, t′) dt′, on the window [0, t_end].

   t_end is the first rebound maximum after the first volume minimum. If the solver uses viscosity, also record the wall normal viscous stress and show it is negligible. The pointwise peak wall pressure is a diagnostic.
4. **Unit tests.** Use analytic fields (uniform translation; Rayleigh radial flow) with exact m(≥U), K and P, and pass them to round-off. As a regression, recompute E's sampled axial energy for one stored case and show it beside the new full-vector definition.
5. **Errata.** Write `ERRATA_TO_EXPERT_RESOLUTION.md`.
   - **P5 wording.** List every place E reports the sampled axial quantity as jet energy. Search two ways, because prose wraps across lines:
     - multiline and case-insensitive for `jet\s+(carries|takes|kinetic\s+energy)|carrying\s+\$`;
     - for the macros and fields that carry the number: `Ef(min|max)\b|envMaxEf|jetEfrac|Ej_over_Phi`.

     Hits verified on 12 October 2026:
     - `tex\00_summary.tex:33`;
     - `tex\03_ledger.tex:52`;
     - `tex\06_jet.tex:126`;
     - `tex\06_jet.tex:192–193` (the constant-pressure benchmark's 23–24% of cavity energy);
     - `tex\09_envelope.tex:46`;
     - `generated\table_envelope.tex:17`, from `scripts\extra_tables.py:377`;
     - `scripts\build_reader.py:138`, which generates `READER.html`;
     - `NEXT_AGENT_HANDOFF.md:132`.

     The macros come from `scripts\extra_tables.py:198,390–405`. The general bound K_j ≤ Φ_a (`tex\04_thermo.tex:55`) remains correct and needs no erratum. The corrected statement: "sampled axial kinetic energy, a lower bound on the full kinetic energy of the sampled jet region".
   - **P10.** Add the τ_h interval inconsistency and the decision-summary framing.

**Completion criterion:** the unit tests pass, and the errata covers every grep hit with file:line and its correction.

## S4 — Compressible solver (fixes P2, P8, P9; critical path, ≈ 2–5 days)

### S4.0 Architecture note (`solver\DESIGN.md`)

- **Declared model.** A compressible, viscous, thermodynamically complete liquid (energy equation; EOS with temperature and entropy) surrounding a cavity whose content is the S2 model, including the flash stage. The interface condition is p_liquid = p_b(t) − σκ plus viscous normal stress; p_b comes from the content model, fed by the cavity volume and area.
- **P9.** Uniform content pressure is a declared assumption, H6, with indicator M_v = max|u_n,interface| / c_vapour. P9 requires either a bounded-effect argument or a resolved-vapour comparison at x* (S7.2).

### S4.1 Selection spike (time box: one session)

Preference order:

1. Basilisk all-Mach two-phase: axisymmetric, adaptive, with surface tension and viscosity. Couple the content by a *homobaric projection*: each step, reset all gas cells to the uniform p_b(t), with negligible gas momentum. Download the source on Windows (network note in HANDOFF §5) and build in WSL user space; use micromamba for flex or bison if the build needs them.
2. Another established axisymmetric compressible multiphase code (ECOGEN, MFC, OpenFOAM), built in user space.
3. A custom axisymmetric compressible-liquid solver with a free-surface cavity boundary (ghost fluid with level set, or VOF).

Take the first that builds and passes V2 at coarse resolution within the time box, and record the decision with evidence. Candidate references, to verify from primary sources before citing:

- Fuster & Popinet 2018, J. Comput. Phys. (all-Mach method);
- Saini et al. 2022, J. Fluid Mech. (compressible collapse at a wall);
- Johnsen & Colonius 2009, J. Fluid Mech. (non-spherical collapse, wall pressure);
- Lauer et al. 2012, Comput. Fluids (vapour-bubble collapse near a wall).

### S4.2 Verification ladder

Each test has a script in `verification\` and a pass/fail JSON. Thresholds are pre-registered.

- **V1 — EOS and shocks.** 1D Riemann problems in the declared water EOS against the exact solution. The Hugoniot is compared with sourced shock data across the pressure range the campaign reaches.
- **V2 — Spherical dynamics.** A spherical cavity without a wall, against KM and Gilmore integrations with identical content: R(t) within 1% up to |Ṙ|/c = 0.3, with the observed convergence order reported. Beyond 0.3, compare with Gilmore and report (no pass threshold).
- **V3 — Low-Mach jet.** A constant-pressure cavity near a rigid wall at γ = 2 and 3, inviscid, with the driving reduced so the maximum liquid Mach number is below 0.1. Jet speed must agree with E's validated BIM and with Supponen et al. 2016 within the combined numerical uncertainty (target ≤ 3%).
- **V4 — Published compressible benchmark.** One near-wall case with tabulated outputs; pre-register the case and its tolerance.
- **V5 — Energy budget.** In an inviscid closed-domain test, total energy plus the radiated flux balances to ≤ 0.5%.
- **V6 — Content coupling.** Spherical PFP and PFH cases with α_c ∈ {0, 0.3, 1}, against the S2 spherical model: R_max, collapse time and the wall-speed history within 2% up to Mach 0.3.

**Completion criterion:** V1–V6 pass, and the solver identity (version, source hash, build flags, platform) is recorded in `solver\`.

## S5 — Coupled PFC model and full-trajectory checks (≈ 1–2 days)

1. **Initial condition.** The activated droplet (radius R_a) at rest in its activated state. The whole flash stage is simulated; there is no spherical restart at the switch (P8).
2. **Calibration designs.** Run three, for example PFH α_c = 1 at γ = 2, PFP α_c = 0.3 at γ = 1.5, and PFH α_c = 0 at γ = 3. Each must reach t_end with:
   - the S2 ledger thresholds holding;
   - PFC mass conserved to ≤ 10⁻⁶ relative in the content model and liquid mass to ≤ 10⁻⁴ in the solver;
   - every numerical indicator within its limit.

   From a resolution study, choose production settings with δ_num ≤ ε/3.
3. **Domain checks.** Doubling the far field changes each objective by ≤ ε/10. Either outer-boundary reflections cannot reach the receiver before t_end, or a non-reflecting condition is verified.

**Completion criterion:** the three calibration designs pass every trajectory check, and the production settings (levels, CFL, domain) are written into `PREREGISTRATION.json`.

## S6 — Campaign: feasible set, monotonicity, optimization (≈ 2–5 days, mostly compute)

- **S6.0 Freeze.** Finalize `PREREGISTRATION.json`: objectives, 𝒟, production settings, sampling plan, ε, thresholds and certificate method. Record its SHA-256 in `F\WORK_LOG.md` before the first campaign run.
- **S6.1 Regime map.** Per species, a coarse scan over γ ∈ {1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 8} (respecting D6) and α_c ∈ {0, 0.03, 0.1, 0.3, 0.5, 1}. Record impact versus no impact, the validity indicators and the objective values; coarse values carry their coarse-mesh error from S5.
- **S6.2 Dimension reduction (optional).** Reducing to the α_c = 1 boundary needs monotonicity of each objective in α_c, established by proof or by sign tests. A sign test passes if, at ≥ 3 values of γ spanning the optimum region, consecutive differences exceed their combined numerical error with a consistent sign. Otherwise optimize in two dimensions.
- **S6.3 Optimization.** For each species and objective, bracket the maximum and refine it at the production mesh: Brent or golden-section in γ on the α_c boundary, or 2D adaptive sampling.
  - **Bound.** Use a piecewise bound: either a second-difference curvature estimate with a safety factor ≥ 2, or a Lipschitz bound. State which.
  - **Hold-out.** Place at least one hold-out run between samples near each maximum to test the bound's prediction.
  - **Shared runs.** Every run yields all m_* values and all observers at once.
- **S6.4 Coverage.** Every region of 𝒟 is covered by valid evaluations or by a stated bound. A failed run in a region that could hold the maximum is rerun (smaller step, finer mesh, second solver route) until it is valid; otherwise that region is unresolved and G7 fails.

**Completion criterion:** for each species and objective, J_low (attained) and J_up (bound) exist with a gap ≤ ε, and the maximizer's location is classified as interior, physical bound or application bound.

## S7 — Accuracy at the optimum and closure checks (≈ 1 day)

1. **Refinement.** At each x*, and at any competitor within 2ε, run 3 mesh levels and a time-step halving. Take the Richardson estimate δ_num and include it in the certificate value.
2. **P9 check.** At x*, report M_v. If M_v > 0.3 while p_b exceeds 5% of the liquid driving pressure, run a resolved-vapour or perturbed-content variant and show that the objective changes by ≤ ε/3.
3. **Constitutive sensitivity.** These are declared assumptions, not errors, so they do not enter ε. Report how J* moves with the EOS constants (± their source uncertainty), surface tension, viscosity on/off and the carrier thermal model.

**Completion criterion:** δ_num ≤ ε/3 at every certificate-critical point, the P9 check passes, and the sensitivity table is written.

## S8 — Write-up (≈ 1–2 days)

1. **Report.** LaTeX in `report\`. It covers the problem statement, the content thermodynamics and ledger derivation, the solver and its verification, the campaign, the certificate, results and validity, and the relation to the ceilings (J*_U(m_*) ≤ √(2Φ_a/m_*), with the gap explained). It also compares with E's sampled envelope (what changed and why). Follow the user's derivation rules.
2. **`FINAL_ANSWER.md`.**
   - The first paragraph answers the question for 𝒫: J*_U(m_*) per species and m_*, and J*_P per observer, each ± ε, with x* and the conditions.
   - Then T's ceiling route, quoted unchanged.
   - Then what 𝒫 excludes: device transfer, optical breakdown, and attached cavities unless D6 included them.
3. **`RESULTS_LEDGER.json`** holds every number in the answer and the report, with tier, file, record and validity.
4. **`README.md`.**

**Completion criterion:** every number in `FINAL_ANSWER.md` maps to a ledger entry, and each entry maps to a data record. The report compiles with no errors, undefined references or overfull boxes, and every page has been visually inspected.

## S9 — Internal review, delivery, handback (≈ 0.5–1 day)

1. Run the internal review protocol in ACCEPTANCE_CRITERIA.md: fix, rerun the affected gates, repeat until all pass.
2. Delivery:
   - append to the four logs;
   - zip F to `R\Full_Closure_<YYYYMMDD>.zip`;
   - relocation-test it: extract to an unrelated path, rebuild the tables and report from bundled data, compare;
   - check the ZIP CRC;
   - clean up only verified task-created paths inside F. If a policy blocks a deletion, record it and leave the files.
3. Send the handback message.

**Completion criterion:** `INTERNAL_REVIEW.json` shows every gate passing, the baseline hashes still match, and the handback message has been sent.
