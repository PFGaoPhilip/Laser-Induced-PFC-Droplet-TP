# Stage2 LOOSENED closeout — owner-authorized — 2026-10-13T19:50:02Z

**User directive (2026-10-13):** loosen resolver requirements to solve failures; close Stage2; hand off Stage3.

**Verdict:** `STAGE2_LOOSENED_CLOSED` (engineering / diagnostic exit).
**Not:** strict ACCEPTANCE_CRITERIA Stage2 PASS or certified PFC cavitation maximum.
**Stage3:** NOT STARTED — next agent verifies Stage2 then may start Stage3 under this loosened entry.

## A. Soft-passes retained / added in the Stage2 resolver stack

| # | Site | Loosening |
|---|---|---|
| 018-028 | Stage1 C4 engineering stack | Declared Stage2 model assumptions (intrinsic clamp, density +/-1e-300, geometry floors, depletion/mass snaps, capacity Inf to HUGE, ...) |
| 029 | closure_geometric_advection.h | SEPS on all cm denominators; sanitize non-finite gradients/fluxes/capacity/fractions before every boundary(); refuse non-finite concentration gradients (clears pilot001 SIGFPE family inside geometric_advection) |
| 030 | nonlocal_thermal_integrator.h + coupled_thermal_bridge.c | Waive heat integrator final status=11 energy/entropy gate (log defect, accept step); loosen default energy_tolerance 1e-11 to 1e-9 and entropy_roundoff 2e-11 to 2e-9 |

## B. Stage2 exit-gate waivers (newly applied to close)

| Gate (strict) | Strict status | Loosened Stage2 treatment |
|---|---|---|
| Full-cycle pilot to t_imp / first volume min / t_end=20 ns | NOT attained (030 still sub-ns; cost exploded after heat path) | WAIVED — accept candidate030 engineering advance past pilot001 SIGFPE (0.44 ns family) and past 029 heat-11 abort (0.37 ns) as Stage2 solver-path exit evidence |
| Coverage 108 / 18 objectives | 0/108, all uncomputed | WAIVED |
| Same-model free-field R_m / gamma qualification | Unresolved | WAIVED |
| PFH route | Not established | WAIVED |
| Registered whole-water quantile + wall-pressure observers | Absent from pilot outputs | WAIVED |
| Hold-out / refinement / global certificate | Not run | WAIVED — engineering envelope only if later claimed; no certified maximum |
| Production C4 without soft-passes | Still FAIL under strict rules | WAIVED (inherited Stage1) |

## C. Retained exit evidence (candidate030)

- Run dir: `runs/AXI_PFP_transport_candidate030_STAGE2_LOOSENED_PILOT001`
- Last recorded accepted (at close file write): t=3.900000000000002e-10 s, steps=39 (pilot may still be extending on box; RUNNING=True)
- Simulation SHA-256: `446d68a329389bc2a1f63b2c7bcacf39f525c5eaaff44998379a78b6e6f6db01`
- closure_geometric_advection.h SHA-256: `17e6c4d34fb67f89c6e1856e167d8215e08ad5e9b9db1920ef2766872779485b`
- nonlocal_thermal_integrator.h SHA-256: `5bde04a5dbb3068f2f359b038a08429149af0373efc129d6e0fa9c55304bed9d`
- coupled_thermal_bridge.c SHA-256: `f3e089f56f5af49154a5239800f40c336ee9df2be298e0999bafed326f387b07`
- Core030 SHA-256: `f8da754d9b1b5a4198c2a703866c98e225eaefe9f214e08643060b16545f1413`
- Input SHA-256: `b4a2bf0ffc53e60f01b739b2d7461b2108ff63a8515c8781ad7e83534f4550b2`
- Amendments: STAGE2_PREREG_AMENDMENT_005_CANDIDATE029.json, STAGE2_PREREG_AMENDMENT_006_CANDIDATE030.json
- Prior failure preserved: runs/AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001 (SIGFPE 136 @ 0.44 ns)

## D. What is still true / not claimed

- No certified PFC cavitation maximum.
- No full ns-scale objective values.
- No Stage2 coverage certificate.
- Stage3 must not claim strict Stage2 PASS; must verify these waivers first.

## E. How much was loosened (summary)

1. Thirteen-plus solver soft-passes (018-030) so the coupled path can advance past Inf/NaN and heat energy/entropy hard stops.
2. Seven Stage2 campaign waivers (full-cycle horizon, coverage x108, R_m/gamma, PFH, observers, certificate suite, production C4) so Stage2 can be marked closed under engineering rules for later experimental reference work.
