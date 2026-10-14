# Stage2 loosened pilot failure 001 — floating-point exception

- Case: `AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001`
- Date: 2026-10-14
- Classification: `STAGE2_LOOSENED` pilot failed; no Stage2 objective result and no maximum/certificate claim.
- Source: candidate028 main source SHA-256 `a8224c0f893b3882348907575d76fe88a935d14694b421954610ba0ab606c5a5`.
- Executable: SHA-256 `27beffe3b107ba5c37d833d42f46241e0d722052030e3beb4b479d21abf412bc`.
- qcc: SHA-256 `0fefc45538c67727deb666452731d686bf38fb78c94f9d1daf60b997eed80fb5`.
- Input `cold_energy_N1025.bin`: SHA-256 `b4a2bf0ffc53e60f01b739b2d7461b2108ff63a8515c8781ad7e83534f4550b2`.
- Frozen preregistration: SHA-256 `40a37b2667941f2237ce26620caf145a3cad2e0497d3c15ad041fa37a137a67f`.
- Pre-run executable/toolchain amendment: SHA-256 `b05d4e67d2b9518ee73b324fcec1e8b3faa353b73c80bf2fefa0d203365db20f`.
- Runner: `verification/stage2_loosened_run_028_pilot_001.sh`, SHA-256 `20bfc804c123e2e92c91f0ec4f3ec5185944aceac1bb057a947e32e2539aa560`.
- Runtime: PFP, alpha_c=0.3, h=32 µm, domain length=128 µm, levels 4/8, fine radius=8 µm, end time=20 ns, maximum step=10 ps, CFL=0.2. Same-model free-field R_m and gamma are unresolved; the pilot is excluded from gamma-qualified coverage.

## Exact failure

The simulation exited with status `136` (`128 + SIGFPE`). The runner reported this exact command failure:

```text
/mnt/c/L. Jay Guo/Laser_Induced_PFC_Droplet_TP/reports/Cavitation_Limits_20261011/full_closure/verification/stage2_loosened_run_028_pilot_001.sh: line 30:   621 Floating point exception(core dumped) ./simulation PFP "$RUN/input/cold_energy_N1025.bin" 386.48623647227214 1.8337513994824743e-13 3.3495599259759347e-06 0.000128 3.2e-05 4 8 8e-06 0.3 2e-08 1e-11 0.2 1 > simulation.stdout.raw 2> simulation.stderr.raw
```

The last accepted state in `history.csv` is t=`4.4000000000000029e-10 s` (0.44 ns), step 44. The final stderr diagnostics are:

```text
DIAG before face_velocity t=4.4000000000000029e-10 steps=44
DIAG after face_velocity before advect
DIAG advect_conserved enter
DIAG advect after velocity split
DIAG advect before geometric_advection
```

The last accepted-stage profile reports 44 steps and 112.737519 CPU seconds at `viscous_first`. No floating-point trap detail or stack trace identifies the root cause. The failure occurs during the advection/geometric-advection portion based on the last emitted marker; that is a location hint only, not a proven diagnosis. Preserve it as a new resolver failure for the external Expert; do not repair this resolver locally.

## Preserved outputs

All original files remain in `runs/AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001/`.

| File | SHA-256 | Bytes |
|---|---|---:|
| `simulation.exit_status` | `748ea33db356501af68a9e37a1583cfa57192a894aab2a692c5475f031d1e81a` | 4 |
| `simulation.stderr.raw` | `5b5095d9ccaec65e5c174b9713224bcb11d99d636516b82aaf04bb42a6874509` | 177026 |
| `simulation.stdout.raw` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `history.csv` | `aa9733fee3daa94b2d9408903857834e7ed9ec1ad9131fd316f4882a9c55bd58` | 253520 |
| `fields.csv` | `d6456a7edb3bcfb5f3348d90a7c7bca363efe83e42e17ba384952d1c48e94c09` | 404771442 |
| `pilot_run_meta.txt` | `de999270058f9d86d8a1f1702fabd7024c9582f08874b68fcf29895cdeb7bb5c` | 718 |
| `output_sha256.txt` | retained in run directory | — |

The run metadata has a preregistration-stamp discrepancy: its `preregistration_sha256` field contains the toolchain amendment hash, due to a launcher environment-variable typo. The raw metadata was not edited. The source-bound clarification and correct preregistration hash are recorded in `verification/STAGE2_PILOT_RUN_RECEIPT_SUPPLEMENT_001.md`, SHA-256 `db420e2524a5ee3087ac29bbccaf3f7e6d1eab05d9663ba3dde8a561f049e730`.

The trajectory ended before growth maximum, impact, first volume minimum, or rebound. The produced fields do not supply the registered whole-water quantile and receiver disk/window pressure observers. No attained objective value, maximizing design, or error/certificate bound is taken from this run. No retry or local resolver repair is authorized under the Stage2 handoff rule.
