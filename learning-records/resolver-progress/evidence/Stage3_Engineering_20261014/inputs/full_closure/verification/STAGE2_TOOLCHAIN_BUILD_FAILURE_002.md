# Stage2 local toolchain build failure 002 — retained

- Date: 2026-10-14
- Scope: Build-only attempt for the preregistered 028-lineage pilot. No simulator execution occurred.
- Frozen builder: `verification/stage2_loosened_build_028_local_002_nospace.sh`.
- Basilisk source archive: `solver/downloads/basilisk.tar.gz`, SHA-256 `de851a91712aa83b0592e1e1ae8f7d7e2ffe1ade0266433434700f8c313fbed4`.
- Failure: `make -C ast -j1` again compiled the `BASILISK` macro using the physical project path containing spaces. Although the shell entered through a `/tmp` symlink, GNU make/compiler resolved it to `/mnt/c/L. Jay Guo/...`.
- Exact diagnostic: `cc: error: Jay: No such file or directory` and `cc: error: Guo/Laser_Induced_PFC_Droplet_TP/reports/Cavitation_Limits_20261011/full_closure/runs/STAGE2_BASILISK_QCC_BUILD_002/basilisk/src": No such file or directory`; Make exited 2.
- Classification: repeated local build-path/tooling failure; not a simulation result, physical-domain failure, or resolver failure. No admin installation, model-source change, or simulation occurred.
- Disposition: preserve this attempt and its partial build tree. The next new-named builder will extract, compile, and generate the simulation entirely under `/tmp` with no-space source paths, then copy the binary and build records into the registered project run directory.
