# ACCEPTANCE CRITERIA — "fully solved" for the conditional problem 𝒫

Use this file twice:

- **Internal review.** You run it yourself, the agent that did the work, before handback.
- **Final acceptance.** The final acceptor re-checks the result independently.

Labels E, T, A, F and problems P1–P10 are defined in [HANDOFF.md](HANDOFF.md). Stages S0–S9 are in [PLAN.md](PLAN.md).

**Thresholds.** The defaults below are binding unless the frozen `PREREGISTRATION.json` sets different values with written justification.

**ε.** ε_U = 5% (relative) for J_U, ε_P = 10% for J_P, δ_num ≤ ε/3, and ledger |R| ≤ 1% Φ_a.

**Evidence runs.** These are x*, every run used in the certificate (samples, hold-outs, refinement levels), and the S5 calibration designs.

## Verdict rule

| Verdict | Condition |
|---|---|
| **RESOLVED_CONDITIONALLY** (fully solved for 𝒫) | Every gate G0–G11 passes. |
| **PARTIALLY_RESOLVED** | G0 passes, but at least one other gate fails. List each failing gate and its evidence. |
| **NOT_RESOLVED** | G0 fails, or G1 fails (no single declared problem), or no evidence run passes G2 and G5. |

A gate either passes or fails; there is no partial pass. Do not weaken a threshold to make a gate pass. A changed threshold needs a pre-registration amendment logged before the affected runs, with its reason and with every affected run redone.

## Gates

In the table, ★ marks a gate the final acceptor will independently recompute, not just read.

| Gate | Requirement (pass condition) | Evidence |
|---|---|---|
| **G0 Preservation** ★ | All four baseline trees reproduce exactly with `python -B tools\tree_hash.py` (method in `BASELINE_HASHES.json`). Git HEAD is still `04112243d9ed9e2eee693a592a1f7ba09ecc5851`: no commit, rebase or reset by you. Outside F, your only changes are appended entries in `R\WORK_LOG.md`, `P\WORK_LOG.md` and `C:\L. Jay Guo\WORK_LOG.md`, plus the delivery ZIP `R\Full_Closure_<YYYYMMDD>.zip`. | `verification\preservation.json` (hashes before and after, HEAD, the diff of the three logs showing appends only) |
| **G1 Declared problem** | `PROBLEM_STATEMENT.md` contains everything S1 requires. Every symbol is defined before use, every bound of 𝒟 carries a justification label, the existence argument states whether it is proved or numerically justified, and D1–D11 are recorded with D6 quoting the user. The SHA-256 of the frozen `PREREGISTRATION.json` is logged *before* the earliest campaign run; run metadata timestamps prove the order. Any amendment is logged before its affected runs, with those runs redone. | `PROBLEM_STATEMENT.md`, `PREREGISTRATION.json`, `F\WORK_LOG.md`, `runs\*\meta.json` |
| **G2 Thermodynamic consistency** ★ | (a) The diagnosis explains each of the 18 old 6-µm residuals to ≤ 0.2% Φ_a. (b) At every model switch, \|ΔΦ_content\| ≤ 10⁻⁴ Φ_a, with p, u and s continuous. (c) For every evidence run and every saved t ≤ t_end, \|R(t)\| ≤ 1% Φ_a; X_dest(t) ≥ 0 and non-decreasing; E_rad is computed from the surface flux. (d) PFC mass is conserved to ≤ 10⁻⁶ relative, liquid mass to ≤ 10⁻⁴. | `verification\ledger_diagnosis.json`, `verification\ledger_spherical.json`, `runs\*\ledger.csv` |
| **G3 Observables and errata** | J_U(m_*) and J_P(r_o, τ_o) are implemented exactly as `PROBLEM_STATEMENT.md` defines them, integrating over the whole liquid domain with no jet-region mask. If any mass is left uncovered, it is bounded and included in ε. Every reported energy uses the full vector velocity, or is explicitly labelled directed/axial. The S3 unit tests pass. The errata covers every grep hit from PLAN S3.5 (file:line and correction), plus the P10 items. | `verification\observable_tests.json`, `ERRATA_TO_EXPERT_RESOLUTION.md` |
| **G4 Solver verification** ★ | V1–V6 pass at their pre-registered thresholds (defaults: V2 1%, V3 ≤ 3%, V5 ≤ 0.5%, V6 2%). Every V4 citation was checked against the primary source. Solver version, source hash, build flags and platform are recorded. | `verification\V1..V6_*.json`, `solver\SOLVER_IDENTITY.json` |
| **G5 Feasibility** | Every evidence run reaches its objective event (t_imp or the first volume minimum for J_U; t_end for J_P) with no abort, no validity stop and no extrapolation. There is no positivity or clipping intervention in a window that affects an objective, unless G6 refinement shows it is immaterial. Numerical indicators stay within limits: at the time J_U(m_*) is reached, ≥ 8 cells across the radius of the liquid region with w ≥ J_U(m_*); ≥ 4 cells across any liquid film that affects an objective; liquid tension never beyond the declared threshold. Constitutive-domain excursions are declared in 𝒫 and their sensitivity is reported. Failed runs are kept with a diagnosis. None remains unrepaired in a region that could hold the maximum. | `runs\*\meta.json`, `runs\*\indicators.csv`, `verification\failed_runs.md` |
| **G6 Numerical accuracy** ★ | At each x* and at every competitor within 2ε: at least 3 mesh levels plus a time-step halving. Convergence is monotone (or the deviation is explained), and the Richardson estimate gives δ_num ≤ ε/3. Doubling the domain changes the objective by ≤ ε/10. | `verification\refinement_*.json`, `verification\domain_check.json` |
| **G7 Certificate** ★ | For each species and objective: J_low = J(x*) is attained by an evidence run; J_up bounds sup over 𝒟 of J and includes the interpolation bound plus δ_num; (J_up − J_low)/J_low ≤ ε. Hold-out runs fall inside their predicted bounds. Any dimension reduction (for example α_c = 1) is justified by proof or by the S6.2 sign tests. Every regime piece of 𝒟 is covered. x* is classified (interior, physical bound, or D6-approved application bound) and lies on no model-validity limit. | `certificate\CERTIFICATE.json`, `certificate\samples.csv`, `certificate\holdout.json` |
| **G8 Pressure** | J_P comes from the solved wall-pressure history of the evidence runs. No contact estimate, spreading law or linear-acoustic closure is substituted for it. G5–G7 hold for J_P separately. Internal-impact and pointwise peak pressures appear only as labelled diagnostics. | `runs\*\wall_pressure.csv`, `certificate\CERTIFICATE.json` |
| **G9 Physical consistency** | J*_U(m_*) ≤ √(2Φ_a/m_*) for every m_*, with the gap explained. At all times, K_liquid, E_rad and X_dest are ≤ Φ_a. Low-Mach behaviour agrees with V3. The P9 check passes at x* (PLAN S7.2). The constitutive sensitivity table is present; it is reported but not part of ε. The comparison with E's sampled envelope explains every difference larger than ε. | `report\`, `verification\p9_check.json`, `verification\sensitivity.json` |
| **G10 Answer and documentation** ★ | The first paragraph of `FINAL_ANSWER.md` answers the question for 𝒫: J* ± ε per species and objective, x*, and the conditions. T's ceiling results are quoted unchanged. Every claim carries a tier. Every number traces from `FINAL_ANSWER.md` to `RESULTS_LEDGER.json` to a data record. The report compiles with no errors, no undefined references and no overfull boxes, and every page has been visually inspected (recorded). Derivations follow the user's rules. The claim scan finds no forbidden phrase and no number stated more strongly than its tier. | `FINAL_ANSWER.md`, `RESULTS_LEDGER.json`, `report\*.log`, `verification\claim_scan.json`, `verification\page_inspection.md` |
| **G11 Delivery** | Entries are appended to all four logs, and existing entries are never rewritten. Relocation test: extract `R\Full_Closure_<YYYYMMDD>.zip` to an unrelated path; the bundled scripts rebuild the tables and report from bundled data, and the outputs match. The ZIP CRC test passes. Intermediates are cleaned, or a policy block is recorded. `git status` shows no change attributable to you outside F, the three appended logs and the ZIP. | `verification\relocation.json`, `F\WORK_LOG.md`, the ZIP |

**Forbidden claims** (for the G10 claim scan): the list in HANDOFF §4 "Claims", plus:

- "theoretical maximum" without "for 𝒫";
- "the jet carries", or "jet energy", for a sampled axial quantity;
- "converged" without δ_num;
- any device or transfer claim;
- a tier-E or tier-U number presented as R or P.

## Red-team questions

Answer each in `INTERNAL_REVIEW.md`, with evidence paths.

1. Could the true maximum lie in a part of 𝒟 that you did not sample, or that only failed runs covered? Where is the largest gap between the bound and the samples?
2. Does x* sit on a model-validity limit, or would it move off 𝒟 if a validity indicator were relaxed? If so, the optimum belongs to the model, not to 𝒫.
3. Is the maximum set by numerics? Does J at x* still change monotonically at the finest mesh, and could the jet tip still be under-resolved at the time of J_U?
4. Is any J_U value caused by a few fast cells (spray or numerical droplets) rather than real liquid mass? How much mass sits above J_U(m_*) at the finest level?
5. Does the ledger close for the *wrong* reason? For example, could one term be computed by difference somewhere, or could destruction be hidden in a numerical dissipation term?
6. Does any reported energy or pressure exceed the ceilings in T or the activation exergy Φ_a at any time?
7. Is the α_c monotonicity actually established at the γ values that matter, or assumed?
8. Is the content-uniformity assumption (P9) significant at x*? What does the resolved or perturbed variant give?
9. Would a sceptical expert accept J_P as a *receiver* pressure? Check the observer size against the cells it covers and the averaging window against the time step, and confirm the wall stress is solved, not post-processed from a model.
10. Which single assumption in 𝒫 would change J* the most, and is that sensitivity stated next to the answer?

## Internal review protocol

1. **Freeze.** Stop editing results. Record the tree hash of F (excluding `INTERNAL_REVIEW.*`) in `F\WORK_LOG.md`.
2. **Fresh pass from disk.** Re-read `PROBLEM_STATEMENT.md`, `CERTIFICATE.json`, `FINAL_ANSWER.md` and the report as if you had not written them. Do not rely on what you remember of the work.
3. **Independent recompute.** Write `verification\independent_recompute.py`, sharing no code with the production post-processing. From saved raw run outputs it recomputes:
   - J_U, J_P and the ledger residual R(t) for x* and two randomly chosen evidence runs (record the seed);
   - the Richardson δ_num;
   - J_up.

   Any difference greater than ε/10 fails the affected gate.
4. **Gate check.** Fill in every gate in `INTERNAL_REVIEW.json` (schema below), citing evidence paths and measured values.
5. **Red team.** Answer the 10 questions above in `INTERNAL_REVIEW.md`.
6. **Fix loop.** For every failed gate or adverse red-team answer: fix it, rerun every gate the fix touches (and anything downstream), and log the change. Repeat until all gates pass, or until the blocked protocol applies.
7. **Optional reviewer subagent.** Use one only if the user authorizes it in the user's subagent format. Give it this file, the frozen tree and no other context. Its findings count only after you independently confirm them.

## Blocked protocol

A gate is *blocked* only when all of these hold:

- two documented independent attempts failed (for a solver, two different routes);
- the diagnosis isolates a cause that you cannot fix within the user's rules (for example, admin rights, unavailable data, or compute beyond this machine);
- no reformulation inside the declared 𝒫 avoids it.

Then:

1. Write `BLOCKED.md`: the gate, the attempts, the evidence, and options with their consequences. The options are:
   - (a) redeclare 𝒫 to a model class you can solve, stating exactly what "fully solved" then covers;
   - (b) a resource the user provides;
   - (c) hand back as PARTIALLY_RESOLVED.
2. Ask the user in one structured question.

Never weaken a gate or relabel a failure as a success.

## `INTERNAL_REVIEW.json` schema

```json
{
  "schema": "full_closure_internal_review_v1",
  "reviewed_at": "ISO-8601 with offset",
  "frozen_tree_sha256": "hex (F, excluding INTERNAL_REVIEW.*)",
  "preregistration_sha256": "hex",
  "verdict_proposed": "RESOLVED_CONDITIONALLY | PARTIALLY_RESOLVED | NOT_RESOLVED",
  "answer": {
    "PFP": {"J_U": {"m_star_pg": {"1": {"value_m_s": 0, "eps_rel": 0, "x_star": {"gamma": 0, "alpha_c": 0}}}},
            "J_P": {"r_o_um,tau_o_ns": {"2,2": {"value_MPa": 0, "eps_rel": 0, "x_star": {}}}}},
    "PFH": {}
  },
  "gates": {
    "G0": {"status": "PASS | FAIL", "measured": {}, "evidence": ["relative/path"], "notes": ""}
  },
  "independent_recompute": {"seed": 0, "max_rel_difference": 0, "script": "verification/independent_recompute.py"},
  "red_team": [{"q": 1, "answer": "", "evidence": ["relative/path"]}],
  "fix_loop": [{"iteration": 1, "failed_gates": [], "change": "", "rerun_gates": []}],
  "open_issues": []
}
```

The `answer` block holds every m_* in D7 and every observer in D8. `gates` holds all of G0–G11.

## Handback message (send only after the internal review)

Lead with the verdict and the answer, in English and in plain sentences. Then give, in this order:

1. the conditional answer for 𝒫, each value ± ε with x*;
2. the gate table with status;
3. what 𝒫 excludes;
4. paths to `FINAL_ANSWER.md`, `INTERNAL_REVIEW.md`, `INTERNAL_REVIEW.json`, `CERTIFICATE.json` and the ZIP;
5. anything blocked or needing the user's decision.

Do not claim more than the gates show.

## What the final acceptor will re-check

The final acceptor will:

- recompute every ★ gate from your files with their own scripts: tree hashes; ledger residuals for x* and random runs; one ladder test; δ_num; J_up from the samples; five numbers traced at random;
- read `PROBLEM_STATEMENT.md` and the report against the user's derivation rules;
- answer the red-team questions independently.

Any difference from your `INTERNAL_REVIEW.json` beyond ε/10 sends the work back.
