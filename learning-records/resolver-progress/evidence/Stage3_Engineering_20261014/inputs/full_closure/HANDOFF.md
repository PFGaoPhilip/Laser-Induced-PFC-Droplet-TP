# HANDOFF — attainable maximum for the conditional laser-induced PFC cavitation question

Prepared 11–12 October 2026 by the acceptance reviewer for the agent that will close the remaining gap. Three files work together:

- **HANDOFF.md** (this file): destination, current state, open problems, rules, decisions.
- **[PLAN.md](PLAN.md)**: stages S0–S9, each with a binding completion criterion.
- **[ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md)**: gates G0–G11. You review yourself against them before handing back; I then re-check them.

## 0. Read first

Root `R` = `C:\L. Jay Guo\Laser_Induced_PFC_Droplet_TP\reports\Cavitation_Limits_20261011`.

| Label | Path | Role |
|---|---|---|
| E | `R\expert_resolution` | 35-page expert report, scripts, data. Frozen evidence. |
| T | `R\conditional_termtex` | Accepted conditional ceiling answer, equations E01–E24. Frozen. |
| A | `R\expert_acceptance` | Acceptance review, verdict PARTIALLY_RESOLVED. Frozen. |
| F | `R\full_closure` | This folder. All new work goes here. |
| P | `C:\L. Jay Guo\Laser_Induced_PFC_Droplet_TP` | Project root (project log). |

Read in this order: this file; `A\EXPERT_ACCEPTANCE_REVIEW.md` (sections "Findings ranked by effect on acceptance" and "Smallest theoretical work needed"); ACCEPTANCE_CRITERIA.md; PLAN.md. Consult as needed: `E\README.md`; `E\tex\01_setup.tex` (hypotheses H0–H4, observables O1–O7, design set); `E\tex\05_spherical.tex`, `06_jet.tex`, `07_receiver.tex`, `09_envelope.tex`, `10_program.tex`; `E\scripts\bubble_km.py`, `bim_axisym.py`; `E\NEXT_AGENT_HANDOFF.md` §3 (environment pitfalls and runtimes, still valid).

Completion criterion: you can state the destination (§1), the ten open problems (§3) and the decisions you must make or ask about (§6) without looking.

## 1. Destination: what "fully solved" means

The question: *"Theoretically, what's the highest pressure or jetting velocity one could achieve from laser induced cavitation? I mean only conditional theoretical solution."*

There are two routes. The **ceiling route** is complete and accepted: T's energy ceiling, linear-contact ceiling and prescribed-cutoff Rayleigh maximum. Keep it unchanged and quote it. This handoff is about the **attainability route**: the highest output the declared PFC cavitation process can actually reach.

**Fully solved** means: for a conditional problem 𝒫 declared in writing before the optimization campaign (preparation, constitutive model, admissible design set 𝒟, objective functionals, tolerance ε), and for every declared objective J:

1. **Attained.** A design x* ∈ 𝒟 has a computed trajectory that satisfies the model equations and every declared validity condition all the way to the objective event, with no validity stop, abort, screen or extrapolation.
2. **Certified.** A justified global upper value J_up ≥ sup over 𝒟 satisfies (J_up − J(x*))/J(x*) ≤ ε, with numerical error included.
3. **Energy-consistent.** Mass, energy and exergy ledgers close along every trajectory used, and exergy destruction, computed from its local sources, is nonnegative.
4. **Not an artifact.** x* is interior to 𝒟, or lies on a bound declared as a physical or user-approved application constraint, never on a model-validity limit.
5. **Stated.** A one-paragraph answer gives J* ± ε, x* and the conditions, keeps the ceiling route, and traces every number to data.

Gates G0–G11 make each item testable. Claim "fully solved" only when all of them pass.

## 2. Where things stand

Verdict: **PARTIALLY_RESOLVED** (A's review). An independent re-check on 11 October 2026 reproduced its central results and reached the same verdict.

Accepted conditionally, do not redo: T E01–E24 (energy ceiling √(2E_av/m_j), linear contact, the 5 nJ plug example at 84.10 m/s and 126.16/63.08 MPa, the Rayleigh cutoff, and the 10 pg allowances of 737.56/961.25 m/s). Also accepted: the activated-state availability 2.7225724/4.6221226 nJ for 6 µm PFP/PFH, as a conditional evaluation (A, claim C05).

Not established: any attainable PFC maximum. E's jet speeds (65/187 m/s slow condensation; 360/378 m/s fast, in-screen) are sampled reduced-model predictions. The 444.6 m/s screen and the 482/715 m/s beyond-screen values are estimates. The 292/307 MPa internal and ≈21/22 MPa receiver pressures are estimates.

The gap is theory and computation. Missing device measurements are **not** the blocker: preparation, the condensation coefficient and the geometry may all be prescribed.

## 3. Open problems

| ID | Problem | Evidence | Fixed in |
|---|---|---|---|
| P1 | No attained continuous optimum. The envelope has 40 sampled cases (5 stand-offs, 4 discrete closures) with no certificate. Fast-closure maxima sit at the arbitrary edge γ = 4; slow-closure maxima sit at γ = 1.25. | A, blocking B1; `E\tex\09_envelope.tex` §"The answer for benchmark B1" | S1, S6, S7 |
| P2 | Fast trajectories leave their models. Keller–Miksis (KM) stops at \|Ṙ\| = 0.3c in 7 of the 18 6-µm water cases (PFP α_c ≥ 0.5 and isoeq; PFH α_c ≥ 0.3 and isoeq). The incompressible boundary-integral method (BIM) runs past its 444.6 m/s screen and stops at a 0.01L tip–wall gap. Its content is a spherical p–V record continued as inverse volume. | A, blocking B2; `E\tex\06_jet.tex` validity items (ii) and (vi); `E\data\km_sweep.json` field `mach_limit_reached` | S4, S5 |
| P3 | The phase switch keeps pressure continuous but not energy or entropy. At the switch from real EOS to ideal vapour, T drops 293.335 → 280.607 K (PFP) and 341.187 → 313.533 K (PFH). Φ_content is then evaluated with the real EOS at the ideal-model temperature. | `E\scripts\bubble_km.py` lines 339–347 and 405–421; `km_sweep.json` fields `T_switch_eos`, `T_switch_ideal` | S2 |
| P4 | The ledger does not close, and it stops at R_max. `exergy_destroyed_or_unaccounted` is −1.98% to −2.68% of Φ_a in all 9 PFP rows (physically impossible) and +7.4% to +31.9% in all 9 PFH rows. Condensed PFC is assigned zero exergy, no heat-transfer exergy term exists, and E_rad is a residual. No ledger covers the collapse. | `E\RESULTS_LEDGER.json` key `six_micrometre_phase_reference_bookkeeping`; `bubble_km.py` lines 391–421 | S2 |
| P5 | Sampled axial kinetic energy is reported as "jet kinetic energy". `jet_mass_velocity` keeps only −u_z and drops points within 0.6 element lengths of the surface. | A, qualification Q1; `E\scripts\bim_axisym.py` lines 571–580; E text hits listed in PLAN S3.5 | S3 |
| P6 | Pressures are estimates: mixed nonlinear-jet/linear-opponent contact, Tait in place of a Hugoniot, an assumed spreading law, and no solved receiver loading. | A, Q2 and claim C08; `E\tex\07_receiver.tex` | S3, S6 (G8) |
| P7 | Convergence is uneven. BIM shows 4.74% spatial and 4.91% step sensitivity; three N96/cap-0.02 runs and the N128 run abort; KM drifts 2.59% at the last grid. | A, Q4; `E\verification\pfc_bim_convergence.json` | S5, S7 |
| P8 | Most of the growth is in the real-EOS flash stage. Quality reaches 1 only at R = 17.05 µm (PFP, 0.76 R_max, t = 1.07 µs) and 13.46 µm (PFH, 0.60 R_max, 0.69 µs). At γ = 1.25 that is 0.61 h and 0.48 h, so the wall acts during the flash. A 2D model must include the flash content; a spherical restart at the switch is invalid. | `km_sweep.json` fields `R_switch`, `R_max`, `t_switch` (frozen rows) | S4, S5 |
| P9 | Uniform-pressure (homobaric) content is outside its own validity in fast collapse. PFC vapour sound speed is 84–99 m/s (CoolProp HEOS; cp/cv ≈ 1.03–1.04), while fast collapses reach 444.6 m/s wall speed, a vapour-side Mach number of about 5. | CoolProp check, 11 Oct 2026; KM results | S4.0, S7.2 |
| P10 | Editorial: the hazard interval is 1 ns–1 µs in `E\tex\01_setup.tex` but 1 ns–1 ms in the parameter-ledger prose. The decision summary's "remaining gap" item lists measurements before the theory gap. | A, E1; `E\tex\00_summary.tex` item 6 | S3.5 (errata) |

## 4. Ground rules

- **User rules bind.** Read `C:\Users\carl_\.claude\CLAUDE.md` (Codex: `C:\Users\carl_\.codex\AGENTS.md`). The ones that matter most here:
  - Reply to the user in English.
  - After each piece of work, append to the logs and clean up task-created intermediates.
  - Write derivations to the "scientific theory" standard: setup first, every symbol defined, numbered steps, dimension and limit checks, honest citations, gaps flagged.
  - Give every HTML file a day/night toggle.
  - Relocation-test deliverable folders, then zip them.
- **Frozen evidence.** E, T, A and the other files in R stay byte-for-byte unchanged; `BASELINE_HASHES.json` records the baseline. Outside F, the only permitted changes in R are appended entries in `R\WORK_LOG.md` and the delivery ZIP `R\Full_Closure_<YYYYMMDD>.zip`. To change an E script, copy it into F and change the copy. Corrections to E go into `F\ERRATA_TO_EXPERT_RESOLUTION.md`.
- **Logs.** Append, newest at the end, to `F\WORK_LOG.md`, `R\WORK_LOG.md`, `P\WORK_LOG.md` and the workspace log `C:\L. Jay Guo\WORK_LOG.md`. `E\WORK_LOG.md` is frozen.
- **Git.** The repository is `C:\L. Jay Guo`. Make no commits and no history changes. Many unrelated files are already modified by other work; leave them alone.
- **Subagents.** Launch them only when the user authorizes in the CLAUDE.md format (`N subs, Model. 1. A. ...`). Otherwise work alone; you may recommend a reviewer.
- **Installs.** User-space only: `pip --user`, micromamba in the WSL home, source builds in your home. Ask the user before anything needing sudo or admin rights, changes to `.wslconfig`, or licensed software.
- **Long jobs.** Run them in the background with logs under `F\runs\`. Checkpoint so a crash or pause loses at most one run.
- **Claims.** Call a value a maximum only after its gates pass; until then use E's tiers R/P/E/U (`E\tex\09_envelope.tex`). Forbidden: "experimentally validated"; "independently reviewed" unless an authorized reviewer did it; "universal maximum"; any validity-screen or censored value presented as a maximum.

## 5. Environment facts

These were checked on 11–12 October 2026 and are expensive to rediscover.

- **Shell.** Windows PowerShell 5: `&&` and bash-style quoting fail. Chain with `;` or put commands in script files.
- **Python.** Python 3.11 with numpy, scipy, sympy, CoolProp 8.0.0, matplotlib and PyMuPDF. numba is absent but installable (PyPI is reachable). Windows multiprocessing uses spawn, so pool code must sit in a script under `if __name__ == "__main__":`.
- **Hardware.** 32 logical CPUs, 15.2 GB RAM. WSL sees about 7 GB.
- **WSL.** `Ubuntu-20.04` starts on demand. It has gcc, g++, make, gawk, git, curl, wget and python3. It lacks gfortran, cmake, flex, bison and MPI. `sudo` needs a password (non-interactive use is blocked), so get toolchains with micromamba from conda-forge, which WSL can reach.
- **Network.** WSL runs in NAT mode without the Windows proxy mirrored. basilisk.fr was unreachable from WSL but reachable from Windows: download there and use the file via `/mnt/c/...`. GitHub, conda-forge and PyPI respond.
- **TeX Live 2025 and Node 24.** Paths and the LaTeX escaping hazards are in `E\NEXT_AGENT_HANDOFF.md` §3.

## 6. Decisions

| ID | Decision | Default | Who |
|---|---|---|---|
| D1 | Species | PFP and PFH, answered separately | Agent |
| D2 | Preparation | 6 µm droplet, full homogeneous activation at T_k = 386.5/415.2 K, H0–H4 as assumptions (unchanged from E) | Agent |
| D3 | Environment | Water at 293.15 K and 101.325 kPa, air-free, no gel, rigid planar receiver, axisymmetric | Agent |
| D4 | Liquid model | Compressible water with a sourced EOS valid over the reached Hugoniot range, Newtonian viscosity, surface tension; values from `E\PARAMETER_LEDGER.json` where present | Agent |
| D5 | Phase transfer | Hertz–Knudsen–Schrage (HKS) with α_c ∈ [0, 1] as a design coordinate, plus a declared carrier thermal model. Isothermal equilibrium (isoeq) is reported only as an idealized reference outside 𝒟, because it drops interfacial latent heating. | Agent (user may override) |
| D6 | Lower stand-off bound | Ask the user. Default γ ≥ 1.25 ("detached cavity": no receiver contact during growth). The pressure optimum will probably sit on this bound, so it must be an application decision. Options: keep 1.25; near-contact (≈ 1.0 plus a film margin); include attached cavities (γ < 1, which needs contact-line physics). | **User** |
| D7 | Velocity objective | J_U(m_*), directed mass-qualified speed (definition in PLAN S3.1), for m_* ∈ {1, 3, 10, 30, 100} pg. The O1 tip speed is a diagnostic, certified only if mesh-converged. | User confirms |
| D8 | Pressure objective | O7 receiver pressure averaged over a centred disk of radius r_o and a duration τ_o, with r_o ∈ {2, 10} µm and τ_o ∈ {2, 20} ns. Point peaks and internal-impact pressures are diagnostics. | User confirms |
| D9 | Tolerances | ε_U = 5% and ε_P = 10% relative; numerical error ≤ ε/3; ledger residual ≤ 1% Φ_a | Agent |
| D10 | Upper stand-off bound | Large enough that every objective is shown to fall below J(x*) − ε toward it. Start at 8 and extend if needed. | Agent |
| D11 | Corrections to E | An errata file in F. Edit and recompile E only if the user asks. | Agent |

Ask D6, and confirm D7 and D8, in a single structured question at the start of S1, with the recommendation and its consequence spelled out. Proceed on the other defaults. Record every decision in `PREREGISTRATION.json` before S6. A decision changed after S6 starts requires a logged amendment and a rerun of everything it affects.

## 7. Deliverable layout

```text
full_closure/
  HANDOFF.md  PLAN.md  ACCEPTANCE_CRITERIA.md  BASELINE_HASHES.json  tools/tree_hash.py
  PROBLEM_STATEMENT.md       S1  declared problem with every symbol and assumption
  PREREGISTRATION.json       S1/S6  objectives, design set, tolerances, sampling plan, thresholds
  scripts/                   content model, ledger, observables, certificate, tables, plots
  solver/                    solver source or config, DESIGN.md, build notes, version and hashes
  runs/                      per-run metadata, logs and compact outputs (bulky raw fields stay out of the ZIP)
  data/                      aggregated results
  verification/              ladder V1-V6, ledgers, convergence, certificate, independent recompute
  report/                    LaTeX source and compiled PDF
  FINAL_ANSWER.md            one-page answer
  RESULTS_LEDGER.json        every reported number with tier, source record and validity
  ERRATA_TO_EXPERT_RESOLUTION.md
  INTERNAL_REVIEW.md / INTERNAL_REVIEW.json
  README.md  WORK_LOG.md
```

The delivery ZIP of F goes next to it, at `R\Full_Closure_<YYYYMMDD>.zip`. Bulky raw fields are left out and listed in `README.md`.

## 8. Working protocol

- **Order.** Work through PLAN.md in order. Each stage's completion criterion is binding; a stage is done only when it holds.
- **Checkpoint.** At the end of every stage, and before any long compute, append a log entry giving the state, the next step and how to resume.
- **Pre-register.** Freeze `PREREGISTRATION.json` before the S6 campaign and record its SHA-256 in `F\WORK_LOG.md`. Tolerances and thresholds stay fixed once results exist.
- **Failures stay.** Every failed or aborted run remains in `runs\` with its diagnosis.
- **Persist.** Keep working until every gate passes. Stop only to ask the user something that is theirs to decide (D6, installs needing admin rights, scope changes), or to declare BLOCKED under ACCEPTANCE_CRITERIA.md "Blocked protocol". A gate is never passed by weakening it.
- **Hand back.** When your internal review shows every gate passing, send the handback message from ACCEPTANCE_CRITERIA.md.

## 9. Suggested skills

| Skill | Path | Use |
|---|---|---|
| Math-Rigor | `C:\Users\carl_\.codex\skills\math-rigor\SKILL.md` | Existence, monotonicity and ledger identities |
| Math-LaTeX | `C:\Users\carl_\.codex\skills\math-latex\SKILL.md` | The report |
| Math-TermTex | `C:\Users\carl_\.codex\skills\Math-TermTex\SKILL.md` | Formulas in FINAL_ANSWER.md, consistent with T |
| matt-enmi-diagnosing-bugs | `C:\Users\carl_\.codex\skills\matt-enmi-diagnosing-bugs\SKILL.md` | Ledger residuals, solver aborts |
| matt-enmi-tdd | `C:\Users\carl_\.codex\skills\matt-enmi-tdd\SKILL.md` | The verification ladder as tests |
| matt-enmi-research, paper-search, paper-download | `C:\Users\carl_\.codex\skills\...` | EOS constants and benchmark papers from primary sources |
| CCS-pause, matt-proui-handoff | `C:\Users\carl_\.codex\skills\...` | A session that must stop mid-stage |

## 10. Start prompt

```text
Read C:\L. Jay Guo\Laser_Induced_PFC_Droplet_TP\reports\Cavitation_Limits_20261011\full_closure\HANDOFF.md, then ACCEPTANCE_CRITERIA.md and PLAN.md in the same folder. Your job: make the conditional question "Theoretically, what's the highest pressure or jetting velocity one could achieve from laser induced cavitation? (conditional theoretical solution only)" fully solved for the declared PFC benchmark, meaning an attained, energy-consistent, certified optimum, by executing PLAN.md stages S0-S9. At the start of S1, ask me decision D6 and confirm D7/D8 in one structured question; use the stated defaults for everything else. Keep working until every gate G0-G11 passes in your own internal review, then send the handback message. Keep expert_resolution, conditional_termtex and expert_acceptance byte-for-byte unchanged; all new work goes in full_closure. Reply to me in English. No Git commits.
```
