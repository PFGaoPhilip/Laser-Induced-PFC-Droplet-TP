#!/usr/bin/env bash
# Build only. Frozen inputs remain unchanged. Run in an existing Linux environment.
set -euo pipefail
lesson=$(cd "$(dirname "$0")/.." && pwd)
target=${1:?Usage: bash native/build.sh /absolute/new/build-directory}
case "$target" in /*) ;; *) echo 'Use an absolute Linux output path'; exit 2;; esac
case "$target" in *' '*) echo 'qcc requires an output path without spaces'; exit 2;; esac
if [ -e "$target" ]; then echo 'Output must not exist'; exit 2; fi
mkdir -p "$target"
tar -xzf "$lesson/native/basilisk.tar.gz" -C "$target"
cd "$target/basilisk/src"
export BASILISK="$PWD"
if [ ! -e config ]; then ln -s config.gcc config; fi
make -C ast -j1
make qcc -j4
qcc_path="$PWD/qcc"
mkdir "$target/model"
cp "$lesson"/evidence/Stage3_Engineering_20261014/inputs/full_closure/runs/AXI_PFP_transport_candidate030_STAGE2_LOOSENED_PILOT001/*.[ch] "$target/model/"
cp -R "$lesson"/evidence/Stage3_Engineering_20261014/inputs/full_closure/runs/AXI_PFP_transport_candidate030_STAGE2_LOOSENED_PILOT001/input "$target/model/"
cd "$target/model"
objects=()
for unit in material_bridge coupled_phase_bridge coupled_thermal_bridge axisymmetric_interface_geometry axisymmetric_transport_graph scaled_plic_geometry axisymmetric_transport_manifest; do
    gcc -O2 -Wall -c "$unit.c" -o "$unit.o"
    objects+=("$unit.o")
done
"$qcc_path" -O2 -Wall axisymmetric_activation_core_candidate030.c "${objects[@]}" -o simulation -lm
sha256sum simulation > BUILD_SHA256.txt
printf 'Build complete. No simulation executed. Output: %s\n' "$target/model"
