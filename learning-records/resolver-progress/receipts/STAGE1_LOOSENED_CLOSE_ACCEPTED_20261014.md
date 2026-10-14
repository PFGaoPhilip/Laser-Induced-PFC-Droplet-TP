# Stage1 closure accepted after local verification — 14 October 2026

**Authoritative continuation status: CLOSED_LOOSENED. Strict ACCEPTANCE_CRITERIA PASS: false. Stage2 started: false.**

The owner explicitly accepts the expert's loosened closure and asks for a Stage2 handoff without Stage2 execution. Root checked candidate028's retained artifacts without rerunning it. All six principal hashes match the expert report, all83 preregistered bindings match, and all82 copied-file bindings match. The recorded freeze event was located in verification/stage1_continuation_20261012 and its hash and entry binding match. history.csv has202 rows,20 accepted steps with contiguous step IDs/increasing times, and final t=1e-13s. qcc and simulation status files both record0. Four distinct soft-pass markers and physical_domain_status=0 appear in stderr. That last status is not production admission.

Verification receipt: verification/STAGE1_CANDIDATE028_VERIFIED_LOOSENED_ACCEPTANCE_20261014.json; SHA256 c455be9ff168689d4d068fe8d8df1d664a6ea571b14b3d581e81cfaa35a91a5f.

## All eleven code-level soft-passes carried forward

| Candidate | Modification |
|---|---|
| 018 | Negative viscous intrinsic increment clamped to zero before the energy update. |
| 019 | Relaxation soft-pass hook added; it did not clear the then-active status21. |
| 020 | Density-conversion underflow soft-passed at +/-1e-300. |
| 021 | Residual near-zero water/PFC geometry floored into a pure-material early exit. |
| 022 | Near-zero negative depletion complement snapped (reported scale about1e-66). |
| 023 | Tiny negative water mass snapped before geometry. |
| 024 | Tiny negative water mass/energy snapped, followed by EOS retry. |
| 025 | Residual water fraction snapped to zero / PFC fraction to one. |
| 026 | MW floor1e-25 and EW floor1e-20 when aW is near zero; caloric consumer treats the water as absent. |
| 027 | Water energy/fraction/auxiliary momentum co-cleared with water-mass snap; nonpositive-density guards applied. |
| 028 | Nonfinite or oversized geometric capacity ratios clamped to HUGE; SEPS added in the capacity factor. |

## All five exit-gate waivers carried forward

| Waived strict gate | Retained strict disposition |
|---|---|
| C4 production admission | Strict FAIL_PRODUCTION_ADMISSION retained; candidate028 engineering diagnostic accepted for exit. |
| V1–V6 production package | Production package unestablished; V3/V6 NOT_RUN and V4 incomplete; prior component records retained. |
| C5 three activation-to-rebound calibrations | Not started; explicitly waived for Stage1 exit. |
| C3 whole-path G9 / D1–D6 execution qualification | Design proposals/correction exist; admitted source/critical route and whole-path signs unproved; waived for exit. |
| Independent Stage1 self-audit | Not run; explicitly waived. Current narrow artifact check is not that self-audit. |

ACCEPTANCE_CRITERIA.md is preserved unchanged. The waivers close the engineering Stage1 work boundary; they do not create missing scientific evidence or pass the strict gates. Earlier strict failures, candidate011/earlier successors and production admission refusal remain retained. No further mass/EOS changes were made here.

## Verification limits

Transferred fields.csv is absent, so this is an artifact/endpoint verification rather than a full trajectory audit. Meta timestamps describe metadata written after execution and do not independently establish run duration or historical freeze timing. One reported marker shorthand differs from its actual emitted label; the actual (027 co-clear EW/q) marker is present. The11-entry stack is declared in the expert's controlling waiver inventory; four marker families were observed at runtime. The independent Stage1 self-audit remains waived.

No gate is refused for this owner-authorized engineering closure. Future strict maximum/certificate claims still require the applicable feasibility, error, coverage and global-certificate evidence; this closure cannot supply it. No certified PFC cavitation maximum has been computed; the actual-device maximum remains unresolved.

## Stage2 transfer

Use verification/STAGE1_LOOSENED_CLOSE_STAGE2_HANDOFF_20261014/STAGE2_HANDOFF.md and STAGE2_START_PROMPT.txt. This new handoff supersedes older NOT_READY continuation wording solely because the owner has now accepted the listed loosened entry policy and local verification is acceptable. Stage2 has not started: no Stage2 preregistration is created/frozen and no Stage2 model/campaign/optimization run was executed. Begin it only in the next explicitly tasked session.
