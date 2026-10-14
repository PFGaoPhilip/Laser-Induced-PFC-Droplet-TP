#!/usr/bin/env bash
set -euo pipefail

F='/mnt/c/L. Jay Guo/Laser_Induced_PFC_Droplet_TP/reports/Cavitation_Limits_20261011/full_closure'
RUN="$F/runs/AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001"
TARBALL="$F/solver/downloads/basilisk.tar.gz"
TMP='/tmp/stage2_basilisk_qcc_003'
SRC='/tmp/stage2_pilot_source_003'

if [ -e "$TMP" ] || [ -e "$SRC" ]; then
  printf 'Refusing to overwrite pre-existing isolated build paths.\n' >&2
  exit 90
fi
if [ -e "$RUN/simulation" ] || [ -e "$RUN/qcc" ]; then
  printf 'Refusing to overwrite a pre-existing pilot executable.\n' >&2
  exit 91
fi
test "$(sha256sum "$TARBALL" | awk '{print $1}')" = 'de851a91712aa83b0592e1e1ae8f7d7e2ffe1ade0266433434700f8c313fbed4'
mkdir -p "$TMP" "$SRC"
cp -- "$TARBALL" "$TMP/basilisk.tar.gz"
test "$(sha256sum "$TMP/basilisk.tar.gz" | awk '{print $1}')" = 'de851a91712aa83b0592e1e1ae8f7d7e2ffe1ade0266433434700f8c313fbed4'
tar xzf "$TMP/basilisk.tar.gz" -C "$TMP"
cp -a "$RUN/." "$SRC/"

cd "$TMP/basilisk/src"
export BASILISK="$PWD"
test "$BASILISK" = '/tmp/stage2_basilisk_qcc_003/basilisk/src'
if [ ! -e config ]; then ln -s config.gcc config; fi
make -C ast -j1 > "$TMP/ast_build.stdout" 2> "$TMP/ast_build.stderr"
make qcc -j4 > "$TMP/qcc_build.stdout" 2> "$TMP/qcc_build.stderr"

cd "$SRC"
export PATH="$BASILISK:$PATH"
objects=()
for source in material_bridge.c coupled_phase_bridge.c coupled_thermal_bridge.c axisymmetric_interface_geometry.c axisymmetric_transport_graph.c scaled_plic_geometry.c axisymmetric_transport_manifest.c; do
  stem=${source%.c}
  /usr/bin/gcc -O2 -Wall -c "$source" -o "$stem.o" > "$stem.compiler.stdout" 2> "$stem.compiler.stderr"
  printf '0\n' > "$stem.compiler.exit_status"
  objects+=("$stem.o")
done
"$BASILISK/qcc" -O2 -Wall axisymmetric_activation_core_candidate028.c "${objects[@]}" -o simulation -lm > qcc.compiler.stdout 2> qcc.compiler.stderr
printf '0\n' > qcc.compiler.exit_status

{
  printf 'gcc: '; gcc --version | head -n 1
  printf 'glibc: '; getconf GNU_LIBC_VERSION
  printf 'logical_basilisk_path: %s\n' "$BASILISK"
  printf 'basilisk_archive_sha256: '; sha256sum "$TMP/basilisk.tar.gz" | awk '{print $1}'
  printf 'qcc_sha256: '; sha256sum "$BASILISK/qcc" | awk '{print $1}'
  printf 'qcc_source_sha256: '; sha256sum "$BASILISK/qcc.c" | awk '{print $1}'
  printf 'simulation_sha256: '; sha256sum simulation | awk '{print $1}'
  printf 'gcc_sha256: '; sha256sum /usr/bin/gcc | awk '{print $1}'
} > "$SRC/local_toolchain_identity.txt"

cp -- "$BASILISK/qcc" "$RUN/qcc"
cp -- "$SRC/simulation" "$RUN/simulation"
cp -- "$SRC/local_toolchain_identity.txt" "$RUN/local_toolchain_identity.txt"
cp -- "$SRC/qcc.compiler.stdout" "$RUN/qcc.compiler.stdout"
cp -- "$SRC/qcc.compiler.stderr" "$RUN/qcc.compiler.stderr"
cp -- "$SRC/qcc.compiler.exit_status" "$RUN/qcc.compiler.exit_status"
for source in material_bridge.c coupled_phase_bridge.c coupled_thermal_bridge.c axisymmetric_interface_geometry.c axisymmetric_transport_graph.c scaled_plic_geometry.c axisymmetric_transport_manifest.c; do
  stem=${source%.c}
  cp -- "$SRC/$stem.o" "$RUN/$stem.o"
  cp -- "$SRC/$stem.compiler.stdout" "$RUN/$stem.compiler.stdout"
  cp -- "$SRC/$stem.compiler.stderr" "$RUN/$stem.compiler.stderr"
  cp -- "$SRC/$stem.compiler.exit_status" "$RUN/$stem.compiler.exit_status"
done
cp -- "$TMP/ast_build.stdout" "$RUN/ast_build.stdout"
cp -- "$TMP/ast_build.stderr" "$RUN/ast_build.stderr"
cp -- "$TMP/qcc_build.stdout" "$RUN/qcc_build.stdout"
cp -- "$TMP/qcc_build.stderr" "$RUN/qcc_build.stderr"
printf 'Local 028-lineage build completed under Linux /tmp; no simulation was launched.\n'
