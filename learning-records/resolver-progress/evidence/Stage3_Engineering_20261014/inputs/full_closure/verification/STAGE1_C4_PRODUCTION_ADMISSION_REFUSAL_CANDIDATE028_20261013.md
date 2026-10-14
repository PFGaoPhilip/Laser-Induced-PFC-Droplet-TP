# C4 production admission attempt — candidate028 — FAIL

**UTC:** 2026-10-13T17:26:38.334167+00:00  
**Result:** `FAIL_PRODUCTION_ADMISSION`  
**Engineering diagnostic:** 100fs PFP reached t=1e-13 / 20 steps / exit 0 (retained).  
**Production:** **not** admitted.

## Attempt
Evaluate whether the candidate028 coupled 100fs lineage can be promoted under production C4 / G4 criteria without weakening ACCEPTANCE_CRITERIA.

## Hard refusal (first stop)
The run succeeds only with an active **engineering soft-pass stack**. Soft-pass markers were printed during the retained native run. Production admission requires the production coupled path without those engineering bypasses, plus observer/event/error harness and V1–V6 at frozen thresholds. None of those are satisfied.

## Retained evidence
- Run: `runs/AXI_PFP_transport_candidate028_100fs`
- Binary SHA-256: `b9bd675b2963b6cd49ca8607c9e6eb889e8ffb455c3dd3bb539e5717fd057c76`
- JSON twin: `STAGE1_C4_PRODUCTION_ADMISSION_REFUSAL_CANDIDATE028_20261013.json` (sha256=ed5ffb7cb6ac3c305a6f84b9856f9e189dd17bf1eddb521575996d00d1a13ab5)

## Does not authorize
Stage1 complete, C4 production PASS, V1–V6 package PASS, C5 start, or Stage2.
