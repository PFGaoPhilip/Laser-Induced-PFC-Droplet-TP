#!/usr/bin/env bash
set -euo pipefail

F='/mnt/c/L. Jay Guo/Laser_Induced_PFC_Droplet_TP/reports/Cavitation_Limits_20261011/full_closure'
BUILD="$F/runs/STAGE2_BASILISK_QCC_BUILD_001"
RUN="$F/runs/AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001"
TARBALL="$F/solver/downloads/basilisk.tar.gz"

mkdir -p "$BUILD"
tar xzf "$TARBALL" -C "$BUILD"
cd "$BUILD/basilisk/src"
if [ ! -e config ]; then ln -s config.gcc config; fi
export BASILISK="$PWD"
make -C ast -j1
make qcc -j4

{
  printf 'gcc: '; gcc --version | head -n 1
  printf 'glibc: '; getconf GNU_LIBC_VERSION
  printf 'qcc_sha256: '; sha256sum qcc | awk '{print $1}'
  printf 'qcc_source_sha256: '; sha256sum qcc.c | awk '{print $1}'
} > "$RUN/local_toolchain_identity.txt"

cd "$RUN"
export PATH="$BASILISK:$PATH"
objects=()
for source in material_bridge.c coupled_phase_bridge.c coupled_thermal_bridge.c axisymmetric_interface_geometry.c axisymmetric_transport_graph.c scaled_plic_geometry.c axisymmetric_transport_manifest.c; do
  stem=${source%.c}
  if /usr/bin/gcc -O2 -Wall -c "$source" -o "$stem.o" > "$stem.compiler.stdout" 2> "$stem.compiler.stderr"; then
    printf '0\n' > "$stem.compiler.exit_status"
  else
    rc=$?
    printf '%s\n' "$rc" > "$stem.compiler.exit_status"
    exit "$rc"
  fi
  objects+=("$stem.o")
done
if "$BASILISK/qcc" -O2 -Wall axisymmetric_activation_core_candidate028.c "${objects[@]}" -o simulation -lm > qcc.compiler.stdout 2> qcc.compiler.stderr; then
  printf '0\n' > qcc.compiler.exit_status
else
  rc=$?
  printf '%s\n' "$rc" > qcc.compiler.exit_status
  exit "$rc"
fi
sha256sum simulation > binary_sha256.txt
sha256sum /usr/bin/gcc "$BASILISK/qcc" > actual_toolchain_sha256.txt
printf 'Local 028-lineage build completed; no simulation was launched.\n'
