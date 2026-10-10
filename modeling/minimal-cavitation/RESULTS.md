# Results and interpretation

The two final native models use **Global Equations only**. Model A has two flow states and three accounting accumulators; Model B adds two gel-wall states. A single nominal **10 ns pulse is represented by the initialized post-activation state**. Optical heating, nucleation and the excluded initial pressure transient are not simulated.

The baseline uses available work 2 nJ, initial gas radius 15 µm, chamber radius 30 µm, outlet radius 5 µm, effective liquid inertance length 50 µm, water-like density 1000 kg/m³, ambient pressure 100 kPa, and adiabatic ideal-gas exponent 1.4. The channel's connected chamber-liquid inventory supplies the finite discharge budget. The gel baseline uses G = 20 kPa and effective viscosity 0.010 Pa s. These are stipulated controls, not calibrated PFC or hydrogel measurements.

| Defined output | Rigid chamber A | Open hydrogel B |
|---|---:|---:|
| Initial chamber overpressure | 279.632 kPa | 279.632 kPa |
| Highest first-ejection outlet speed | 15.37608 m/s | 1.62538 m/s |
| Highest outlet dynamic-pressure scale | 118.2119 kPa | 1.3209 kPa |
| Emitted mass over first ejection | 20.96789 ng | 0.15612 ng |
| Actual emitted energy | 1.391345 nJ | 0.000136 nJ |
| Actual emitted impulse | 2.270810e-10 N s | 1.982567e-13 N s |
| First outward ejection duration | 33.8850 µs | 1.9370 µs |
| Largest elastic confinement pressure | — | 9.1430 kPa |
| Largest one-hemisphere elastic force | — | 33.7705 µN |

In this declared family, the strongest sampled outlet-speed case is **A_E5nJ_a3um**: **25.27982 m/s**, source overpressure **512.212 kPa**, and outlet dynamic-pressure scale **319.535 kPa**. The family samples available work 0.5, 2 and 5 nJ and outlet radii 3, 5 and 10 µm, at the same initial gas/chamber radii and inertance length. It is a conditional sampled envelope, not an experimentally established universal limit.

The baseline energy-only outlet ceiling is **31.91538 m/s** and its energy-only dynamic-pressure ceiling is **509.296 kPa**. These are upper bounds. The solved flow pays for emitted kinetic energy, column inertia, meniscus work and residual source availability, so its achieved maximum is smaller.

Open-gel peak-speed transmission is **10.5709%**. Actual emitted-energy transmission is **0.00980%**, and emitted-impulse transmission is **0.08731%**. Energy and impulse were integrated from outlet fluxes; they are not the speed ratio squared. This geometry gives gel motion an additional energy route and a much shorter first ejection. It does not prove that every hydrogel reduces output or that larger modulus/viscosity monotonically weakens jetting.

The sealed control emits zero liquid mass, energy and impulse. Its maximum elastic pressure is 9.6259 kPa and its maximum inner-wall stretch is 1.15252. A finite pressure or wall deformation under intact gel must not be relabeled as an external jet.

The observer diagnostic is only a mean arrest-pressure bound derived from the actual emitted impulse, with a declared outlet-sized area and 1 µs averaging interval. It does not calculate impact peak pressure, arriving mass after breakup, transmission into a solid target, or fracture of unbroken gel.

![Native first-ejection histories](assets/first_event_histories.png)

![Conditional velocity family](assets/conditional_velocity_envelope.png)

![Energy destinations and actual emitted output](assets/energy_and_transmission.png)

![Defined gel resistance and confinement force](assets/gel_confinement.png)

Native verification passed for all 17 cases. The largest normalized energy residual is 1.260e-07; the largest native/independent normalized waveform error is 1.152e-04; the largest pressure-communication diagnostic is 0.08356, below the declared 0.1 screen. Both final models were reloaded and solved in a fresh COMSOL process, and baseline peak velocities passed the 2 ns / 1 ns time-resolution check. These verify implementation and convergence of the stated controls. PFC EOS/phase inventory, laser conversion, rate-dependent gel calibration and actual device geometry remain unresolved experimental inputs.

See [the full worked derivation](MODEL_SPEC.md), [native case register](data/native_case_register.json), [numerical audit](verification/NUMERICAL_AUDIT.json) and the two native files in [models/](models/).
