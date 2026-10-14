# Stage2 loosened progress status 001

**Status: `STAGE2_LOOSENED_INCOMPLETE_ROUTE_FAILURE`.** Stage2 has started under the owner-accepted experimental-reference policy, but is not complete. Stage1 remains `CLOSED_LOOSENED`; it was not reopened. Stage3 has not started.

## Executed evidence

- Frozen Stage2 scope remains PFP/PFH; gamma `[1.25, infinity)`; alpha_c `[0,1]`; water masses `{1,3,10,30,100}` pg; pressure disks `{2,10}` µm and windows `{2,20}` ns. Candidate soft-pass stack 018–028 is the declared engineering model identity.
- One new 028-lineage PFP diagnostic was built and run from a frozen source/input/toolchain package. It used alpha_c=0.3, h=32 µm, a 20 ns requested horizon, 10 ps maximum step, and CFL=0.2. Because same-model free-field R_m was not established, its gamma is unknown and this case is excluded from gamma-qualified coverage.
- The run exited 136 (`SIGFPE`) at 0.44 ns, step 44, during the advection/geometric-advection portion. The last diagnostic marker is before `geometric_advection`; the root cause remains unresolved. Exact evidence and hashes are in `STAGE2_PILOT_FAILURE_001.md` and the run directory.
- The run produced 404,771,442 bytes of partial `fields.csv` and 253,520 bytes of `history.csv`. These stop before the growth maximum, impact, first volume minimum, or rebound and do not supply the registered whole-water quantile or receiver pressure observers. They are not objective values.
- The run receipt has a preregistration-stamp typo. The raw receipt is preserved and paired with `STAGE2_PILOT_RUN_RECEIPT_SUPPLEMENT_001.md`; this is disclosed in the failure record.

## Coverage and certification status

- Initial coarse coverage: **0/108** cases run. The new snapshot is `data/STAGE2_LOOSENED_CASE_STATUS_SNAPSHOT_001.csv` (SHA-256 `1b4e06361e77523088bbc16918999f6ce9a95c10332218e77b3fb65463248d0c`). The frozen planned register remains unchanged.
- Fixed gamma-tail anchors (16 and 32) and reserved tail hold-outs (12 and 24): **not run**. There is no training set from which to freeze hold-out predictions.
- Near-maximum and competitor hold-outs: **not instantiated or run** because there are no training maxima/competitive boxes.
- Mesh/time refinement, doubled-domain studies, P9/content checks, and constitutive sensitivities: **not run** because no certificate-critical designs or complete event trajectories exist.
- The objective ledger `data/STAGE2_LOOSENED_OBJECTIVE_STATUS_001.csv` (SHA-256 `c3aff015bbf22d314aaccd07bed3cec32eeaad309bbe36119dd4b01e8034e82a`) contains 18 rows; all are `NOT_COMPUTED`. There are no attained lower values or justified global upper values.
- Consequently no objective meets the 5% velocity or 10% pressure global-gap target. Numerical error `<= epsilon/3`, domain sensitivity `<= epsilon/10`, and whole-domain coverage remain unestablished. No certified maximum or engineering envelope has been computed.

## Resumable next action

Transfer the SIGFPE resolver failure to the Expert using `STAGE2_EXPERT_HANDOFF_PILOT_RESOLVER_FAILURE_001.md`. Do not locally repair or overwrite this failed candidate. Continue with a new-named candidate and a pre-run amendment only after the Expert supplies a focused diagnosis/repair. Keep Stage2 outputs labeled `STAGE2_LOOSENED`, preserve the full unbounded gamma tail and all unresolved regimes, and stop before Stage3.
