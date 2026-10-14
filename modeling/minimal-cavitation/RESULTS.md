# Results and interpretation

Both native models use **Global Equations**. Model A solves two flow states and three accumulators. Model B adds two gel-wall states. The nominal **10 ns pulse is represented by post-activation initial data**. Optical heating, nucleation and the activation pressure transient are excluded.

Baseline inputs: available work 2 nJ; initial gas radius 15 µm; chamber radius 30 µm; outlet radius 5 µm; effective inertance length 50 µm; density 1000 kg/m³; ambient pressure 100 kPa; adiabatic exponent 1.4. Connected chamber liquid sets the finite discharge budget. Gel inputs are G = 20 kPa and viscosity 0.010 Pa s. These inputs define the controls. PFC and hydrogel calibration remain unresolved.

| Defined output | Rigid chamber A | Open hydrogel B |
|---|---:|---:|
| Initial chamber overpressure | 279.632 kPa | 279.632 kPa |
| Highest first-ejection outlet speed | 15.37608 m/s | 1.62538 m/s |
| Highest outlet dynamic-pressure scale | 118.2119 kPa | 1.3209 kPa |
| Emitted mass over first ejection | 20.96789 ng | 0.15612 ng |
| Emitted energy | 1.391345 nJ | 0.000136 nJ |
| Emitted impulse | 2.270810e-10 N s | 1.982567e-13 N s |
| First outward ejection duration | 33.8850 µs | 1.9370 µs |
| Largest elastic confinement pressure | — | 9.1430 kPa |
| Largest one-hemisphere elastic force | — | 33.7705 µN |

The highest sampled outlet speed occurs in **A_E5nJ_a3um**: **25.27982 m/s**. Source overpressure is **512.212 kPa**. Outlet dynamic pressure is **319.535 kPa**. The family samples work 0.5, 2 and 5 nJ. It samples outlet radii 3, 5 and 10 µm. Initial gas/chamber radii and inertance length stay fixed. These are conditional maxima within the sampled family. A universal limit is not established.

The baseline energy ceiling is **31.91538 m/s**. Its dynamic-pressure ceiling is **509.296 kPa**. The solution also spends energy on emission and meniscus work. Energy remains in column motion and the source. The solved maximum is therefore below these bounds.

Open-gel peak-speed transmission is **10.5709%**. Emitted-energy transmission is **0.00980%**. Emitted-impulse transmission is **0.08731%**. Integrate outlet fluxes to obtain energy and impulse. Peak-speed ratios cannot replace those integrals. Here gel motion receives energy and shortens the first ejection. General monotonic effects of modulus and viscosity are not established.

The sealed control emits zero mass, energy and impulse. Its maximum elastic pressure is 9.6259 kPa. Its maximum inner-wall stretch is 1.15252. The gel deforms while external discharge remains zero.

The observer diagnostic bounds mean arrest pressure from emitted impulse. It uses outlet area and a 1 µs interval. Peak impact pressure is not established. Missing: contact dynamics, arriving mass, target transmission and gel fracture.

![Native first-ejection histories](assets/first_event_histories.png)

![Conditional velocity family](assets/conditional_velocity_envelope.png)

![Energy allocation and emitted output](assets/energy_and_transmission.png)

![Defined gel resistance and confinement force](assets/gel_confinement.png)

Native verification passed for all 17 cases. Maximum normalized energy residual: 1.260e-07. Maximum native/reference waveform error: 1.152e-04. Maximum pressure-communication diagnostic: 0.08356, below the stipulated 0.1 screen. Both baselines were reloaded and solved in a fresh COMSOL process. Peak velocities passed the 2 ns / 1 ns resolution check. These checks verify the specified implementation and temporal convergence. Experimental validation remains unresolved. Missing: PFC EOS/phase inventory, laser conversion, gel calibration and device geometry.

See [the full worked derivation](MODEL_SPEC.md), [native case register](data/native_case_register.json), [numerical audit](verification/NUMERICAL_AUDIT.json) and the two native files in [models/](models/).
