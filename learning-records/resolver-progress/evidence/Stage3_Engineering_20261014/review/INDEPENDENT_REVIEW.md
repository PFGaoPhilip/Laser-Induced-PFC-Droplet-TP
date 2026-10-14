# Independent Stage3 acceptance review

The attainable PFP/PFH velocity and registered receiver-pressure optima remain unresolved. All 18 declared slots lack attained values, designs and certified lower/upper pairs. This review supports an honestly qualified engineering documentation package under the owner-accepted loosened policy. It does not establish strict acceptance, a certified PFC maximum or an actual-device maximum. Stage1 and Stage2 remain closed; no campaign was restarted.

## Independence and available-number audit

The reviewer used a standalone Python standard-library implementation with no production processing imports and no new solver execution. Its source is [independent_recompute.py](../scripts/independent_recompute.py); its deterministic output is [INDEPENDENT_RECOMPUTE.json](INDEPENDENT_RECOMPUTE.json). It recomputes cylindrical participating mass, lossless speed, linear-contact arithmetic, adopted-state mass/work/availability products, Tait contact via a density-ratio bisection, the mixed nonlinear-jet/linear-target contact via a second interface-speed bisection, stored profile energy ratios and propagation estimates, legacy growth bookkeeping remainders, and partial candidate030 mass diagnostics.

All **239 arithmetic comparisons PASS**, with maximum relative discrepancy **7.270960063791253e-14** against the stored values. This only establishes arithmetic agreement with the stated adopted inputs. The 1e-9 relative comparison screen in this script is an arithmetic tolerance, not a substituted physical acceptance threshold. It is substantially tighter than the inherited epsilon/10 comparison thresholds.

The accepted original ten-pg values 737.563556583431 and 961.2491872558332 m/s use rounded 2.72 and 4.62 nJ. Exact accepted availability inputs instead give 737.9122450810853 and 961.4699750525903 m/s. Both routes are recorded; the original is preserved. No zero fills were used. The accepted radius and expansion-source-pressure EOS values are source-only quotations; independent fresh EOS integration/evaluation is **NOT_RUN**, not PASS.

An initial naive legacy remainder calculation subtracted useful growth work and content availability. It differed from each stored remainder by the small mechanical closure mismatch. The corrected independent calculation sums the stored surface, gel, viscous and acoustic terms directly; it reproduces all 18 remainders. Both the initial difference and its diagnosis are retained in the JSON. This documentary correction does not repair the historical thermodynamic failure: PFP remainders are negative (approximately -1.98% to -2.68% of activation availability), so they cannot be identified with physical nonnegative destruction. Historical acoustic values are estimates, and a bookkeeping remainder is not an independently measured entropy-production term.

The random seed is 20261014. Two stored historical record indices are retained in the JSON as an arithmetic provenance spot check. There is no x-star or objective evidence-run ensemble: recomputation of current J_U, J_P, the complete trajectory residual, Richardson error and certified J_up at x-star/two randomly selected evidence runs is **NOT_RUN**, with all corresponding quantities null. The historical spot check does not replace that absent audit.

## Source reconciliation and retained failures

The historical processed envelope contains 35 rows. Older prose referring to 40 sampled cases cannot establish 40 successful trajectories. Stored fast/slow samples, Mach-screen violations and pressure estimates are distinguished in the recomputation output. The maximum in-screen internal mixed-contact estimates are 292.3180241469137 MPa (PFP) and 307.47079561558753 MPa (PFH); receiver-wave estimates are 21.025716016783834 and 22.36855815501231 MPa. Those quantities are tier E estimates, not registered receiver averages or current attainable bounds. Historic profile speed is not the whole-water mass quantile, and stored sampled axial energy is not full-vector water kinetic energy.

The transferred candidate030 history has 43 accepted records, last at line 432, time 0.43000000000000027 ns. Maximum accepted-record relative mass drift is 3.7732884106127866e-16 for water and 2.3402317923312148e-15 for PFC. These narrow diagnostics do not pass full-cycle mass/thermodynamic consistency. The snapshot does not reach a registered objective event. The legacy candidate028 meta.json zero exit is not candidate030 completion evidence. The candidate030 pilot metadata lacks a completed exit receipt.

Historical closeout prose says candidate030 progressed past the prior 0.44 ns SIGFPE family; its contemporaneous numeric endpoint was 0.39 ns and the transferred endpoint is 0.43 ns. The accepted engineering close is preserved, while that stronger progress claim is unsupported by the transferred snapshot. Candidate028's 0.44 ns failure and candidate029's 0.37 ns heat stop remain failures; there is no assumption about present external-run state.

## Gate dispositions

The strict gates in [ACCEPTANCE_CRITERIA.md](../inputs/full_closure/ACCEPTANCE_CRITERIA.md) are preserved. WAIVED denotes an accepted reporting disposition, never a measured scientific pass. G0/G10/G11 await root's final integrated preservation, documentation and delivery checks. Detailed evidence and the strict outcome are in [INDEPENDENT_REVIEW.json](INDEPENDENT_REVIEW.json).

| Gate | Reporting disposition | Scientific outcome retained |
|---|---|---|
| G0 preservation | NOT_RUN here; root owns final audit | Pending final evidence/history check |
| G1 declared problem | FAIL | The accepted problem itself states unresolved assembled-model, domain/tail and event-existence links prevent G1 PASS |
| G2 thermodynamics | FAIL | Historical nonphysical negative remainder; complete current trajectory ledger/switch consistency absent |
| G3 observables/errata | WAIVED for unavailable registered observers | NOT_RUN for current full-water/registered pressure implementation and coverage audit |
| G4 solver verification | WAIVED under Stage1 accepted verification exit | Strict V1–V6 suite and production admission unestablished; no PASS |
| G5 feasibility | WAIVED | FAIL: no completed current objective event/full-cycle evidence |
| G6 accuracy | WAIVED | NOT_RUN: no current maximizing-design refinement/domain suite |
| G7 certificate | WAIVED | NOT_RUN: no attained design, hold-outs, upper enclosure or certificate |
| G8 pressure | WAIVED | NOT_RUN: no solved registered pressure observer history |
| G9 physical consistency | WAIVED for inherited whole-path qualification | FAIL: complete physical qualification absent; conditional arithmetic survives |
| G10 documentation | NOT_RUN here; root owns integration | Strict numerical optimum answer unavailable; loosened documentation can pass its own checks |
| G11 delivery | NOT_RUN here; root owns delivery | Pending relocation/CRC/log/cleanup checks |

Under the unchanged strict verdict rule, G1 FAIL implies **NOT_RESOLVED**. That describes the strict scientific maximum problem, not permission to reopen accepted Stage1/Stage2. Reporting completion is a separate engineering disposition.

## Seven Stage2 waiver consequences

1. **Full-cycle pilot/horizon — WAIVED:** impact, post-growth first minimum, rebound and 20 ns trajectory are not established; sub-ns advance supplies a diagnostic snapshot only.
2. **Coverage/objectives — WAIVED:** 0/108 completed registered campaign coverage and all 18 uncomputed slots; no sampled coverage enclosure or optimum.
3. **Free-field radius/stand-off — WAIVED:** no same-model free-field R_m qualification; candidate030 gamma cannot be certified from an inherited radius or source ceiling.
4. **PFH route — WAIVED:** no comparable candidate030 PFH production trajectory; historical PFH estimates retain their earlier model identity.
5. **Registered observers — WAIVED:** no whole-water quantile or wall-pressure disk/window outputs; historical masks/contact/spreading estimates cannot substitute.
6. **Hold-outs/refinement/certification — WAIVED:** velocity 5%, pressure 10%, numerical epsilon/3 and domain epsilon/10 targets remain unestablished; all certificate pairs/designs null.
7. **Production C4 — WAIVED:** candidate018–030 soft-passes remain adopted engineering assumptions; the strict production-admission failure is retained.

Authority: [accepted Stage2 closeout](../inputs/full_closure/verification/STAGE2_LOOSENED_CLOSED_20261013.md), [accepted Stage1 close](../inputs/full_closure/verification/STAGE1_LOOSENED_CLOSE_ACCEPTED_20261014.md), [Stage3 original frozen preregistration](../inputs/full_closure/verification/STAGE3_PREREGISTRATION_001_LOOSENED_WRITEUP.json) and [verified Stage3 entry receipt002](../inputs/full_closure/verification/STAGE2_LOOSENED_CLOSE_VERIFY_STAGE3_ENTRY_20261014_002.json). The prior six-hash entry audit is reused, not repeated.

## Ten independent red-team answers

**1. Unsampled or failed domain:** Yes. No current coverage or global enclosure exists. Gamma spans [1.25,infinity) without a finite upper application bound, and accommodation spans [0,1]. The unsampled tail/free-field endpoint and failed regimes may contain a supremum. There is no certified bound-minus-sample gap to rank; it is null. A finite historical scan cannot establish tail decay, particularly because directed free-field water speed need not vanish. Evidence: [problem](../inputs/full_closure/PROBLEM_STATEMENT.md), P02 and domain discussion; [objective ledger](../inputs/full_closure/data/STAGE3_RESULTS_LEDGER_001.json).

**2. Model-validity limit and x-star:** No x-star exists. Classification or movement under relaxed indicators is NOT_RUN. Mach 0.3 historical stops are model working screens; beyond-screen samples are estimates rather than admitted optima. Same-model radius qualification remains waived. Evidence: [historical rows](../inputs/expert_resolution/data/envelope_rows.json), [expert acceptance](../inputs/expert_acceptance/EXPERT_ACCEPTANCE_REVIEW.md), [accepted waiver receipt](../inputs/full_closure/verification/STAGE2_LOOSENED_CLOSE_VERIFY_STAGE3_ENTRY_20261014_002.json).

**3. Numerical maximum or tip resolution:** Unknown. No x-star, three-level current refinement, step halving or domain doubling is available. The historical suite retained aborted attempts and nontrivial sensitivities; its previous refinement does not transfer to candidate030. Forty-three accepted time steps establish neither event-time resolution nor numerical error. Evidence: [historical verification ledger](../inputs/expert_resolution/RESULTS_LEDGER.json), numerical_verification; [candidate030 history](../inputs/full_closure/runs/AXI_PFP_transport_candidate030_STAGE2_LOOSENED_PILOT001/history.csv).

**4. Fast cells or physical mass:** Unknown for current J_U. Whole-water masses must be {1,3,10,30,100} pg with fractional water mass, no jet-region mask. No fields/registered quantile outputs or finest-level above-threshold mass are supplied; that mass remains null. Partial total mass conservation does not show physical quantile coverage or exclude fast-cell artifacts. Evidence: [problem](../inputs/full_closure/PROBLEM_STATEMENT.md), P03–P04; [recompute diagnostics](INDEPENDENT_RECOMPUTE.json).

**5. Ledger closes for wrong reason:** This risk remains. The historical growth remainder is computed by difference and is not independent destruction; its PFP negativity is a physical warning. The current history records positive entropy terms, mass and operator defects, but lacks sufficient full-reference terms to reconstruct the complete exergy residual independently. Soft-pass030 accepts heat energy/entropy gate defects; small mass drift or a pressure solver residual does not remove that qualification. Evidence: [historical raw ledger](../inputs/expert_resolution/data/km_sweep.json), energy_ledger; [candidate030 history](../inputs/full_closure/runs/AXI_PFP_transport_candidate030_STAGE2_LOOSENED_PILOT001/history.csv); [Stage2 close](../inputs/full_closure/verification/STAGE2_LOOSENED_CLOSED_20261013.md).

**6. Ceiling or activation-availability exceedance:** The independently checked reported historical sampled axial energy ratios do not establish a full-vector all-time comparison. No current complete water-energy/radiation/destruction history is available, so the requested all-time check is NOT_RUN. Contact/collapse pressure can exceed the 1.265/1.085 MPa absolute expansion-source ceilings without contradicting those expansion-only premises. The linear-contact formula is not a universal nonlinear shock cap. Exact-input mass ceilings remain conditional on a complete nonnegative availability budget; no energy fraction is silently reset. Evidence: [thermodynamic source](../inputs/expert_resolution/tex/04_thermo.tex), [pressure source](../inputs/expert_resolution/tex/07_receiver.tex), [recomputation](INDEPENDENT_RECOMPUTE.json).

**7. Accommodation monotonicity:** Not established over the declared relevant gamma domain. Historical discrete closures do not prove a derivative sign, regime-transition behaviour or global monotonicity. Alpha_c stays in [0,1]; there is no justified reduction to alpha_c=1. Evidence: [problem](../inputs/full_closure/PROBLEM_STATEMENT.md), [historical rows](../inputs/expert_resolution/data/envelope_rows.json), [waived certificate suite](../inputs/full_closure/verification/STAGE2_LOOSENED_CLOSED_20261013.md).

**8. Content uniformity/P9 at x-star:** NOT_RUN because there is no x-star and no matched resolved/perturbed comparison. The live candidate030 model assumptions are preserved; the old spherical uniform-content comparison does not validate current asymmetric optimal events. No quantitative P9 sensitivity is invented. Evidence: [acceptance P9 requirement](../inputs/full_closure/ACCEPTANCE_CRITERIA.md), G9/red-team8; [model/problem](../inputs/full_closure/PROBLEM_STATEMENT.md).

**9. Receiver pressure:** A skeptical expert cannot accept the current historical estimate as registered J_P. Disk radii {2,10} micrometres and windows {2,20} ns need solved rigid-plane pressure histories with the prescribed event horizon. There are no registered histories, covered-cell counts or window/time-step adequacy results. A Tait internal contact model plus linear spreading/reflection is tier E, not solved wall stress. Wall viscous normal stress must also be checked before pressure alone is called complete loading. Evidence: [problem](../inputs/full_closure/PROBLEM_STATEMENT.md), P05–P06; [historical pressure source](../inputs/expert_resolution/tex/07_receiver.tex); [observer waiver](../inputs/full_closure/verification/STAGE2_LOOSENED_CLOSED_20261013.md).

**10. Most influential assumption:** No sensitivity ranking of an attainable optimum is possible because neither the optimum nor a matched sensitivity suite exists. Uniform activation/budget, reference consistency, condensation model, compressibility, content uniformity and wall/contact geometry are plausible material choices; none is assigned a fabricated largest effect. This limitation is stated beside the answer in [FINAL_ANSWER.md](../FINAL_ANSWER.md). The accepted thermal/continuum/receiver model excludes optical-breakdown and device-transfer conclusions. Evidence: [problem H0–H4](../inputs/full_closure/PROBLEM_STATEMENT.md), [historical acceptance qualifications](../inputs/expert_acceptance/EXPERT_ACCEPTANCE_REVIEW.md).

## Fresh final-answer review

The root draft was reread from disk. Its numerical historical selections match independent grouping and its exact-input ceilings agree with independent arithmetic. It distinguishes the old illustrative linear-contact plug from PFC outputs, retains the rounded-input discrepancy, excludes current registered pressure optima, and preserves all 18 nulls and the candidate030 provenance caveat. No attained/certified/device maximum is asserted. Root must finalize G0, G10 and G11 after PDF/reader/relocation/archive checks. Review records are source-bound; no preserved upstream evidence was edited and no fresh upstream research was repeated.
