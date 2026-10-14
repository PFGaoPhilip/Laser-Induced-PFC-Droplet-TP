# Stage2 local toolchain build failure 001 — retained

- Date: 2026-10-14
- Scope: Build-only attempt for the preregistered 028-lineage pilot. No simulator execution occurred.
- Frozen build script: `verification/stage2_loosened_build_028_local_001.sh`, SHA-256 `88485284c009ca754fe5563d49674d61439ab504c49065285c8355cb25ffa06c`.
- Basilisk source archive: `solver/downloads/basilisk.tar.gz`, SHA-256 `de851a91712aa83b0592e1e1ae8f7d7e2ffe1ade0266433434700f8c313fbed4`.
- Exact failing build phase: `make -C ast -j1`, compiling `ast/interpreter/interpreter.c`.
- Exact diagnostic: `cc: error: Jay: No such file or directory` and `cc: error: Guo/Laser_Induced_PFC_Droplet_TP/reports/Cavitation_Limits_20261011/full_closure/runs/STAGE2_BASILISK_QCC_BUILD_001/basilisk/src": No such file or directory`; Make exited 2.
- Cause: the project path contains spaces and the Basilisk Makefile's `-DBASILISK=...` argument was not escaped as one compiler argument.
- Classification: local build-path/tooling failure; not a simulation result, physical-domain failure, or resolver failure. No admin installation, source edit, or Stage1 work occurred.
- Disposition: preserve this attempt and its partial build tree. Retry with a new-named builder using a no-space temporary build directory; retain the same archived Basilisk source and 028 model sources. Do not overwrite this record.
