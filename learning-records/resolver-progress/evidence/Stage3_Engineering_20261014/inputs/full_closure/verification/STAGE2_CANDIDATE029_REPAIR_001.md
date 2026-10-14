# Stage2 candidate029 repair — STAGE2_LOOSENED — 2026-10-13T19:23:04.393212+00:00

## Diagnosis (pilot001 / candidate028 lineage)
- Exit 136 SIGFPE at t=4.4e-10 s after 44 accepted steps.
- Last marker: `DIAG advect before geometric_advection` (no after).
- Candidate028 capacity Inf clamp **already fired earlier** in that run.
- Therefore this is a **new** geometric_advection Inf/NaN site under ns stretch, not a missing 028 patch.

## Repair (new-named candidate029)
- File: `runs/AXI_PFP_transport_candidate029_STAGE2_LOOSENED_PILOT001/closure_geometric_advection.h`
  - SHA-256 `17e6c4d34fb67f89c6e1856e167d8215e08ad5e9b9db1920ef2766872779485b`
- Core: `axisymmetric_activation_core_candidate029.c` SHA-256 `afd19794f1cd9f09ef5c3b049c88281780a6eff92bf77af605d7f8a86bddf5bc`
- Binary: `simulation` SHA-256 `58c987b074367788a45995113bd40f1c2c8e754f007bd3834f9470081ff421bb`
- Input unchanged SHA-256 `b4a2bf0ffc53e60f01b739b2d7461b2108ff63a8515c8781ad7e83534f4550b2`
- Soft-passes: SEPS on cm factors; sanitize non-finite fields before every `boundary()`; non-finite concentration gradients → 0; retain 018–028.

## Policy
Owner-authorized **loosened Stage2**. Do not reopen Stage1. No certified maximum. Label all outputs `STAGE2_LOOSENED`.
