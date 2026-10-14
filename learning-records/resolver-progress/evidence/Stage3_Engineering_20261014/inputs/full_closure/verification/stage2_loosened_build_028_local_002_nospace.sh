#!/usr/bin/env bash
set -euo pipefail

F='/mnt/c/L. Jay Guo/Laser_Induced_PFC_Droplet_TP/reports/Cavitation_Limits_20261011/full_closure'
BUILD="$F/runs/STAGE2_BASILISK_QCC_BUILD_002"
RUN="$F/runs/AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001"
TARBALL="$F/solver/downloads/basilisk.tar.gz"
BUILD_LINK='/tmp/cavitation_stage2_basilisk_002'
RUN_LINK='/tmp/cavitation_stage2_pilot_001'

if [ -e "$BUILD" ] || [ -e "$BUILD_LINK" ] || [ -e "$RUN_LINK" ]; then
  printf 'Refusing to overwrite a pre-existing build or alias path.\n' >&2
  exit 90
fi
mkdir -p "$BUILD"
tar xzf "$TARBALL" -C "$BUILD"
ln -s "$BUILD" "$BUILD_LINK"
ln -s "$RUN" "$RUN_LINK"
cd "$BUILD_LINK/basilisk/src"
export BASILISK="$PWD"
if [[ "$BASILISK" == *' '* ]]; then
  printf 'No-space Basilisk alias failed: %s\n' "$BASILISK" >&2
  exit 91
fi
if [ ! -e config ]; then ln -s config.gcc config; fi
make -C ast -j1
make qcc -j4

{
  printf 'gcc: '; gcc --version | head -n 1
  printf 'glibc: '; getconf GNU_LIBC_VERSION
  printf 'logical_basilisk_path: %s\n' "$BASILISK"
  printf 'qcc_sha256: '; sha256sum qcc | awk '{print $1}'
  printf 'qcc_source_sha256: '; sha256sum qcc.c | awk '{print $1}'
} > "$RUN_LINK/local_toolchain_identity.txt"

cd "$RUN_LINK"
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
cp "$BASILISK/qcc" qcc
printf 'Local 028-lineage build completed; no simulation was launched.\n'
