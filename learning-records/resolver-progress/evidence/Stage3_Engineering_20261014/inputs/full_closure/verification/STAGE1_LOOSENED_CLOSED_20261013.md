# Stage1 LOOSENED closeout — user-authorized — 2026-10-13T17:27:16.287462+00:00

**User directive (2026-10-13):** loosen solution requirements to close Stage1; report how much was loosened.

**Verdict:** `STAGE1_LOOSENED_CLOSED` (engineering / diagnostic exit).  
**Not:** strict `ACCEPTANCE_CRITERIA` Stage1 PASS.  
**Stage2:** remains **NOT READY** until the owner explicitly accepts these waivers for optimization.

---

## A. Code-level soft-passes already in the C4 100fs chain (candidates 018–028)

These changed run-local solver behavior so the coupled PFP diagnostic could advance. They are **engineering bypasses**, not production physics.

| # | Refusal cleared | Loosening |
|---|---|---|
| **018** | viscous intrinsic &lt;0 → status=7 | Clamp negative viscous intrinsic to 0 before energy update |
| **019** | (relax path) | Relax soft-pass hook added; **did not** clear the then-active status=21 |
| **020** | density-conversion underflow → status=21 | Soft-pass density conversion at ±1e-300 |
| **021** | geometry UNRESOLVED status=2 → activation 16 | Residual near-zero water/PFC floor → pure-material early-exit |
| **022** | advection `negative-depletion-complement` status=11 | Snap near-zero negative depletion complement (bi~1e-66) |
| **023** | geometry INVALID_INPUT (MW tiny negative) | Snap tiny negative water mass before geometry |
| **024** | geometric EOS status=1 (neg MW/EW) | Snap tiny negative MW/EW + EOS retry |
| **025** | geometric EOS status=3 (residual aW with MW=EW=0) | Snap residual aW→0 / aF→1 |
| **026** | EOS status=4 + caloric water_status=100 (tiny +MW at aW=0) | Raise MW floor to 1e-25 / EW 1e-20 when aW≈0; caloric treat absent |
| **027** | (sibling) same family | Co-clear EW/aW/q_water on MW snap; guard rho≤0 in face/momentum |
| **028** | SIGFPE after viscous_first (Inf capacity) | Clamp non-finite / &gt;HUGE capacity ratios to HUGE; SEPS in capacity factor |

**028 diagnostic result retained:** qcc=0, sim=0, t=1e-13, 20 accepted steps, physical_domain_status=0.  
Binary sha256=`b9bd675b2963b6cd49ca8607c9e6eb889e8ffb455c3dd3bb539e5717fd057c76`.

---

## B. Gate waivers newly applied to mark Stage1 LOOSENED_CLOSED

Per user authorization to close Stage1 by loosening requirements. Each line is a **waiver of a strict gate**, not evidence that the gate passed.

| Gate (strict) | Strict status | Loosened Stage1 treatment |
|---|---|---|
| C4 **production** coupled admission | FAIL (soft-pass stack; no production harness) | **WAIVED** — accept 028 `PASS_SCOPED_100FS_ENGINEERING` as the C4 solver-path exit evidence |
| **V1–V6** production G4 package | V3/V6 NOT_RUN; production G4 not established | **WAIVED** — retain prior component V1/V2/V5 records; do not block Stage1 exit on V3/V4/V6 |
| **C5** three activation→rebound calibrations | Not started (blocked on integrated C4) | **WAIVED** — not required for loosened Stage1 exit |
| **C3** whole-path G9 / D1–D6 | HARD STOP (owner freeze missing) | **WAIVED for exit** — D1–D6 remain open **owner asks** for any later strict/G9 work; not invented |
| Independent Stage1 self-audit | Not run | **WAIVED** for loosened exit |
| ACCEPTANCE_CRITERIA unchanged text | Still controlling for strict claims | **Not rewritten** — this file records waivers beside it |

---

## C. What is still true / not claimed

- No certified PFC cavitation maximum.
- No production C4 without soft-passes.
- No C5 calibration PASS.
- No whole-path G9 proof.
- Stage2 optimization **must not start** until the owner explicitly accepts `STAGE1_LOOSENED_CLOSED` as sufficient entry, or restores strict gates.

## D. How much was loosened (summary)

1. **Eleven solver soft-passes** (018–028) that replace hard refusals/crashes with clamps, floors, snaps, and Inf guards at machine-epsilon / underflow scales.  
2. **Five Stage1 exit-gate waivers** (C4 production, V1–V6 package, C5×3, C3/G9 D1–D6, self-audit) so Stage1 can be marked closed under engineering rules.

Relative to strict ACCEPTANCE_CRITERIA, this is a **large** loosening: the coupled 100fs path runs only because of (1), and Stage1 closes only because of (2).

## E. Artifact pointers

- 028 repair: `verification/STAGE1_EXPERT_REPAIR_CANDIDATE028_20261013/`
- Prior honest inventory: `verification/STAGE1_CLOSEOUT_STATUS_20261013_BOX_C028.md` (still accurate for **strict** status)
- Production refusal retained: `verification/STAGE1_C4_PRODUCTION_ADMISSION_REFUSAL_CANDIDATE028_20261013.md`
- C3 block memo: `verification/STAGE1_C3_D1_D6_EXECUTION_BLOCKED_20261013.md`
