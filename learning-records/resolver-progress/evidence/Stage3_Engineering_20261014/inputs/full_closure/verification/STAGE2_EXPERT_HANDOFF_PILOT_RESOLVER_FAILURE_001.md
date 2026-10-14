# Expert handoff and start prompt — Stage2 pilot resolver failure 001

## Continue from

```text
C:\L. Jay Guo\Laser_Induced_PFC_Droplet_TP\reports\Cavitation_Limits_20261011\full_closure
```

**Expert Agent: diagnose the new Stage2 candidate028-lineage SIGFPE described below and return a focused, source-bound repair recommendation or a new-named candidate for owner review.** Stage2 must remain `STAGE2_LOOSENED`; do not reopen Stage1 or impose its waived strict gates as Stage2 entry requirements. Do not start Stage3.

## Owner-approved model and scope

The output is for later experimental references; strict 100% acceptance is not the goal. Stage1 is owner-accepted `CLOSED_LOOSENED`, not a strict `ACCEPTANCE_CRITERIA` PASS. Carry candidate soft-pass stack 018–028 as declared Stage2 engineering model assumptions. Preserve all inherited EOS, reference, activation, PFC inventory, and whole-water definitions. Do not silently reset mass, EOS, energy, tolerances, or references. Keep gamma `[1.25, infinity)`, alpha_c `[0,1]`, masses `{1,3,10,30,100}` pg, and pressure disk/window pairs `{2,10}` µm × `{2,20}` ns. Stage2 outputs are conditional engineering references; do not call an engineering envelope a certified maximum.

## Failure to diagnose

Case `AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001` requested a PFP diagnostic with alpha_c=0.3, h=32 µm, domain length 128 µm, mesh levels 4/8, fine radius 8 µm, end time 20 ns, maximum step 10 ps, and CFL=0.2. Same-model free-field `R_m` was not established, so gamma is unresolved and this diagnostic is not gamma-qualified coverage.

The simulation exited `136` (`SIGFPE`) after 44 accepted steps at t=`4.4000000000000029e-10 s` (0.44 ns). The process reported `Floating point exception(core dumped)`. The last stderr markers are `DIAG advect_conserved enter`, `DIAG advect after velocity split`, and `DIAG advect before geometric_advection`. The crash occurred after the last marker; this does not prove the failing operation or root cause. No floating-point trap detail or stack trace was captured. Do not infer a diagnosis from that marker alone.

### Frozen identity

- Stage2 preregistration 002 SHA-256: `40a37b2667941f2237ce26620caf145a3cad2e0497d3c15ad041fa37a137a67f`.
- Pre-run toolchain amendment 004 SHA-256: `b05d4e67d2b9518ee73b324fcec1e8b3faa353b73c80bf2fefa0d203365db20f`.
- Source/input binding manifest SHA-256: `7192224f58dc300250c09ab93faa413d89098be8619d3617a6f47161e6c09fd4`; 83 bindings checked, 0 mismatches.
- Candidate028 main source SHA-256: `a8224c0f893b3882348907575d76fe88a935d14694b421954610ba0ab606c5a5`.
- Built simulation SHA-256: `27beffe3b107ba5c37d833d42f46241e0d722052030e3beb4b479d21abf412bc`.
- Built qcc SHA-256: `0fefc45538c67727deb666452731d686bf38fb78c94f9d1daf60b997eed80fb5`; qcc source SHA-256 `c1109463ef8702c033b53243c126f85b933976f86c99ef52123c0a1cb6949335`.
- Build source archive SHA-256: `de851a91712aa83b0592e1e1ae8f7d7e2ffe1ade0266433434700f8c313fbed4`.
- Compiler: GCC 9.4.0, glibc 2.31; build exit status 0. Compiler warnings and full logs are retained.
- Input `cold_energy_N1025.bin` SHA-256: `b4a2bf0ffc53e60f01b739b2d7461b2108ff63a8515c8781ad7e83534f4550b2`.
- Frozen run script SHA-256: `20bfc804c123e2e92c91f0ec4f3ec5185944aceac1bb057a947e32e2539aa560`.

Exact runtime argument vector:

```text
PFP input/cold_energy_N1025.bin 386.48623647227214 1.8337513994824743e-13 3.3495599259759347e-06 0.000128 3.2e-05 4 8 8e-06 0.3 2e-08 1e-11 0.2 1
```

### Preserved failure outputs

All originals remain under `runs/AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001/`.

| Output | SHA-256 |
|---|---|
| `simulation.exit_status` (`136\n`) | `748ea33db356501af68a9e37a1583cfa57192a894aab2a692c5475f031d1e81a` |
| `simulation.stderr.raw` | `5b5095d9ccaec65e5c174b9713224bcb11d99d636516b82aaf04bb42a6874509` |
| `simulation.stdout.raw` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| partial `history.csv` | `aa9733fee3daa94b2d9408903857834e7ed9ec1ad9131fd316f4882a9c55bd58` |
| partial `fields.csv` | `d6456a7edb3bcfb5f3348d90a7c7bca363efe83e42e17ba384952d1c48e94c09` |
| `pilot_run_meta.txt` | `de999270058f9d86d8a1f1702fabd7024c9582f08874b68fcf29895cdeb7bb5c` |
| `output_sha256.txt` | `6514a8927a2db3619f3561d923a022632635de50339358c16d9fbf612f973b64` |

The raw `pilot_run_meta.txt` has a known provenance defect: the launcher accidentally supplied the amendment hash in the preregistration field. It was not edited. The correct preregistration hash and explanation are in `verification/STAGE2_PILOT_RUN_RECEIPT_SUPPLEMENT_001.md` (SHA-256 `db420e2524a5ee3087ac29bbccaf3f7e6d1eab05d9663ba3dde8a561f049e730`). The runner uses that variable only for metadata; the frozen source, input, executable, and argument vector are independently bound.

The 404 MB fields and history stop before growth maximum, impact, collapse, or rebound and do not contain the registered whole-water velocity quantile or wall-disk/window pressure observers. Do not turn these partial fields into objective values. There is no Stage2 coverage or certificate result: 0/108 initial cases run and all 18 objectives remain uncomputed. The current state is documented in `verification/STAGE2_LOOSENED_PROGRESS_STATUS_001.md`.

## Requested Expert work

1. Diagnose the SIGFPE from the preserved candidate028 source, compiler output, and partial fields/history; state the exact failing operation and root cause if the evidence supports it. If not, specify the smallest additional diagnostic needed.
2. Do not edit or replace the historical pilot, source bundle, preregistration, or logs. If a repair is warranted, return a **new-named** candidate and an exact diff, explain how it preserves the accepted physical/model choices and the 018–028 assumptions, and list all source/build/input hashes.
3. Propose a minimal, bounded validation sequence for a new candidate, with a pre-run preregistration amendment and clear success/failure conditions. Do not call the 0.44 ns run a trajectory qualification; the target remains event-capable ns-scale history plus separate same-model free-field `R_m` and registered observers.
4. State any additional route limitations that still prevent Stage2 coverage: PFH executable/route, same-model `R_m`, whole-water quantiles, receiver wall-pressure observers, and any required full-cycle events.
5. Return a short next-action prompt suitable for the owner to authorize the expert repair/retry. Keep Stage3 out of scope.

The local agent has not attempted a resolver repair and will not retry this resolver locally. Continue only with independent Stage2 documentation/status work until an Expert repair is available. Preserve all failures and keep every engineering prediction explicitly uncertified unless its applicable certificate gates pass.
