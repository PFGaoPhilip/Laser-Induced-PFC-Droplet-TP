#!/usr/bin/env bash
set -euo pipefail

: "${STAGE2_PREREG_SHA:?set to the frozen Stage2 preregistration SHA-256}"
: "${STAGE2_TOOLCHAIN_AMENDMENT_SHA:?set to the frozen toolchain amendment SHA-256}"
: "${STAGE2_SIMULATION_SHA:?set to the audited pilot binary SHA-256}"
: "${STAGE2_INPUT_SHA:?set to the frozen pilot input SHA-256}"
F='/mnt/c/L. Jay Guo/Laser_Induced_PFC_Droplet_TP/reports/Cavitation_Limits_20261011/full_closure'
RUN="$F/runs/AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001"
cd "$RUN"

actual_simulation_sha=$(sha256sum simulation | awk '{print $1}')
actual_input_sha=$(sha256sum input/cold_energy_N1025.bin | awk '{print $1}')
test "$actual_simulation_sha" = "$STAGE2_SIMULATION_SHA"
test "$actual_input_sha" = "$STAGE2_INPUT_SHA"

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  printf 'case_id=AXI_PFP_transport_candidate028_STAGE2_LOOSENED_PILOT001\n'
  printf 'interpretation=STAGE2_LOOSENED engineering pilot; not strict PASS or certified maximum\n'
  printf 'preregistration_sha256=%s\n' "$STAGE2_PREREG_SHA"
  printf 'toolchain_amendment_sha256=%s\n' "$STAGE2_TOOLCHAIN_AMENDMENT_SHA"
  printf 'simulation_sha256=%s\n' "$actual_simulation_sha"
  printf 'input_sha256=%s\n' "$actual_input_sha"
  printf 'start_utc=%s\n' "$start_utc"
  printf 'arguments=PFP cold_energy_N1025.bin 386.48623647227214 1.8337513994824743e-13 3.3495599259759347e-06 0.000128 3.2e-05 4 8 8e-06 0.3 2e-08 1e-11 0.2 1\n'
} > pilot_run_meta.txt

set +e
./simulation PFP "$RUN/input/cold_energy_N1025.bin" 386.48623647227214 1.8337513994824743e-13 3.3495599259759347e-06 0.000128 3.2e-05 4 8 8e-06 0.3 2e-08 1e-11 0.2 1 > simulation.stdout.raw 2> simulation.stderr.raw
run_status=$?
set -e
printf '%s\n' "$run_status" > simulation.exit_status
printf 'end_utc=%s\nexit_status=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$run_status" >> pilot_run_meta.txt
find . -maxdepth 1 -type f \( -name '*.csv' -o -name '*.raw' -o -name '*.exit_status' -o -name 'pilot_run_meta.txt' \) -print0 | sort -z | xargs -0 -r sha256sum > output_sha256.txt
exit "$run_status"
