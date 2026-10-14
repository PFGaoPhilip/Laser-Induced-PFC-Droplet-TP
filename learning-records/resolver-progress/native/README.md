# Native build and optional future run

Use existing Linux/WSL with gcc, make and tar.
Copy this entire lesson folder into Linux.
Keep the build destination free of spaces.

```sh
bash native/build.sh /tmp/pfc_lesson_unique_build
```

This compiles the actual candidate030 sources.
The script performs no simulation.
This new recipe has not been executed here.
The archived candidate028 build record documents the toolchain lineage.
It does not establish a candidate030 completion.

The following historical inputs explain argument ordering.
They are a reproducibility reference, not a request for another campaign.
Run future simulations in an independently scoped writable directory.
Never execute inside the evidence snapshot.

```sh
mkdir /tmp/pfc_future_run_unique
cd /tmp/pfc_future_run_unique
/tmp/pfc_lesson_unique_build/model/simulation \
  PFP /tmp/pfc_lesson_unique_build/model/input/cold_energy_N1025.bin \
  386.48623647227214 1.8337513994824743e-13 3.3495599259759347e-06 \
  0.000128 3.2e-05 4 8 8e-06 0.3 2e-08 1e-11 0.2 1
```

Temperature is K; masses are kg; lengths are m; times are s.
Centre height is 32 µm. It is not the normalized stand-off γ.
See the lesson and native source for validity guards.
