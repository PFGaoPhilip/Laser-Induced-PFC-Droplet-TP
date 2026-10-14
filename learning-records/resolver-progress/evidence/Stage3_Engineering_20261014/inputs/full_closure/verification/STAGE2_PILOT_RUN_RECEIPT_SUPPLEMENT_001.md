# Stage2 pilot run receipt supplement 001 — preregistration stamp discrepancy

- Date: 2026-10-14
- Case: `AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001`
- Status when noted: simulation in progress; preserve the original `pilot_run_meta.txt` and raw outputs.
- Frozen Stage2 preregistration: `verification/STAGE2_PREREGISTRATION_002_LOOSENED_PILOT.json`, SHA-256 `40a37b2667941f2237ce26620caf145a3cad2e0497d3c15ad041fa37a137a67f`.
- Frozen pre-run toolchain amendment: `verification/STAGE2_PREREG_AMENDMENT_004_PILOT_TOOLCHAIN_FREEZE.json`, SHA-256 `b05d4e67d2b9518ee73b324fcec1e8b3faa353b73c80bf2fefa0d203365db20f`.
- Frozen simulation runner: `verification/stage2_loosened_run_028_pilot_001.sh`, SHA-256 `20bfc804c123e2e92c91f0ec4f3ec5185944aceac1bb057a947e32e2539aa560`.
- Bound executable SHA-256: `27beffe3b107ba5c37d833d42f46241e0d722052030e3beb4b479d21abf412bc`.
- Bound input SHA-256: `b4a2bf0ffc53e60f01b739b2d7461b2108ff63a8515c8781ad7e83534f4550b2`.

## Discrepancy

The run launcher was invoked with `STAGE2_PREREG_SHA` accidentally set to the amendment hash `b05d4e67...`, the same value correctly supplied to `STAGE2_TOOLCHAIN_AMENDMENT_SHA`. Therefore the `preregistration_sha256` line written to `pilot_run_meta.txt` is wrong. The expected preregistration hash is `40a37b2667941f2237ce26620caf145a3cad2e0497d3c15ad041fa37a137a67f`.

The runner's frozen command line and arguments are unchanged and the trajectory executable reads its physical/runtime parameters from the explicit argument vector and input file; the erroneous variable is used only for run metadata. This does not change the simulated model or trajectory, but it is a provenance receipt defect. Preserve the raw metadata unchanged, pair it with this supplement, and do not treat the incorrect line as a valid hash binding. The pilot remains a `STAGE2_LOOSENED` engineering diagnostic, and its gamma remains unresolved pending same-model free-field `R_m`.
