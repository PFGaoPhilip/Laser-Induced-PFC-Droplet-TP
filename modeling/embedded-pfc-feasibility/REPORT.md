# Embedded PFC in hydrogel: feasibility and parameter comparison

**Decision:** optically triggered PFC cavitation inside a hydrogel is physically feasible in published specimens. The present project completes a conditional finite-PFC feasibility study and numerical verification. It does not establish a specimen-specific laser threshold, a spontaneously opened discharge channel, a collapse jet, or an impact-pressure peak. Those outputs require the spatial models and measurements specified below.

The starting limitation was substantive: the accepted spherical ideal-gas/outlet control verifies host deformation, energy storage/loss and discharge through an already present outlet. Its matched open-gel result remains **1.625 m/s peak outlet speed and 9.143 kPa peak elastic resistance**, and its sealed control expels zero liquid. These remain valid for their stated equations; they are not PFC vaporization or fracture results.

## 1. What has now been completed

Two separate native COMSOL 6.4 controls now contain **finite real-fluid PFC mass, a vapor core, a surviving liquid shell, distinct inner/outer interfaces, and intact gel mechanics**. Prescribed-radius equilibrium solves four nonlinear phase/inventory/traction conditions. The post-nucleation transient solves three mechanical/loss differential states with four thermodynamic algebraic unknowns. Native analytic Helmholtz EOS functions are compared against an independent CoolProp density-state implementation. The transient starts from a supplied seed; laser heating and nucleation are not silently replaced by an ideal-gas pressure initialization.

| Question | Current evidence | Status |
|---|---|---|
| Can a PFC droplet cavitate inside gel? | Published optical experiments in fibrin, PAAm and gelatin; PFP/PFH/PFO and several micrometre diameters | Feasible for published architectures [S1] |
| Does the new finite-PFC control conserve mass and energy? | 60 native stationary cases and six native transients compared with independent roots/integration | Numerically verified |
| Is a stationary phase root stable? | 132 radial-branch tests plus fixed-(T,V,m) internal phase/core Hessians | Constraint-specific local tests completed |
| What laser fluence activates this specimen? | Absorption, local heating, sites and activation data unavailable | Unresolved |
| Does an intact gel open a fluid-filled path? | No calibrated damage or path coupling in these controls | Unresolved |
| What exterior jet or impact pressure follows? | No outlet, directional collapse or compressible sensor model in new controls | Unresolved; emitted exterior mass is exactly zero |

[S1: embedded-droplet experiments](https://doi.org/10.1016/j.jmbbm.2024.106776) support physical feasibility, not calibration of the present equations. Their associated bubble description includes water vapor and noncondensable gas, which the new PFC-only controls omit. The complete equation derivation, definitions, limits and checks are in [DERIVATION.md](DERIVATION.md); the source ledger is [SOURCES.md](SOURCES.md).

## 2. Declared parameters and comparison rules

| Input | Comparison values | Meaning |
|---|---|---|
| PFC species | PFP; PFH | Gao/CoolProp 8.0.0 real-fluid EOS [S2] |
| Initial radius / diameter | 0.15, 0.3, 1.5, 3, 6 µm / 0.3, 0.6, 3, 6, 12 µm | Initial LIQUID size, not initial gas size |
| Shear modulus | 5, 20, 100 kPa | Stipulated intact neo-Hookean controls; not measured target gel |
| Effective viscosity | 0, 0.01, 0.1 Pa s | Kelvin-Voigt controls, not target high-rate fits |
| Outer / inner tensions | Outer 54 mN/m; PFP inner 9.41, PFH inner 12 mN/m | Room-temperature reference proxies held constant; PFH outer value is stipulated [S4,S5] |
| Outer-tension sensitivity | 5, 18, 54 mN/m for PFP radius 0.3 µm | Alternative stipulated interfaces; no coating equivalence asserted |
| Initial conditions | 293.15 K, ambient 100 kPa; liquid initially at ambient + outer Laplace pressure | Absolute pressures, finite liquid mass |
| Stationary stretch | 1.2, 1.5, 1.8, 2.1 | Equal-size mechanical/phase state comparisons, not laser trajectories |
| Transient seed | Stretch 1.2, zero wall speed, liquid pressure 50 kPa above static host requirement | Conditional post-nucleation state; retained seed energy calculated |
| Stopping screens | First expansion turning, stretch 2.1, Mach 0.1 or 50 reference time scales | 2.1 is not measured rupture; domain exits are rejected/stopped |
| Host and boundaries | Density 1000 kg/m³, sound-speed screen 1500 m/s; effectively infinite undrained host | No external free surface, fracture, outlet, or mass leakage |

Equal stationary stretch compares the energies needed to occupy different equilibrium states. It does **not** hold laser energy fixed. The viscosity sweep holds the same retained seed energy within each size. A laser-design comparison must instead hold local incident fluence and the actual absorption law fixed. A material-response comparison should hold absorbed energy and geometry fixed. Initial seed energy is retained storage plus ambient work relative to the all-liquid reference under lossless preparation; real absorbed energy also pays pre-seed conduction, viscous and acoustic losses and may heat water/coating.

## 3. Size and PFC species

At stretch 2.1, shear modulus 20 kPa and the same stipulated 54 mN/m outer interface:

| PFC | Initial diameter (µm) | State temperature (K) | Equilibrium state energy | Vapor MASS fraction |
|---|---|---|---|---|
| PFP | 0.6 | 339.79 | 12.26 pJ | 20.19% |
| PFH | 0.6 | 371.74 | 19.61 pJ | 21.70% |
| PFP | 6 | 313.78 | 5.476 nJ | 9.22% |
| PFH | 6 | 342.72 | 11.703 nJ | 9.60% |

![Finite-PFC size and species comparison](assets/size_species_comparison.svg)

PFP requires lower state temperature and energy than PFH in these controls. The 0.6 µm inclusion has a much smaller total budget but stronger capillary confinement: its initial outer Laplace excess is 360 kPa, versus 36 kPa for 6 µm diameter. At 20 kPa modulus, the elastic-to-capillary ratio is 0.111 and 1.111, respectively. Thus reducing diameter does not simply make phase change easier. The temperature values describe curved phase-equilibrium states with finite mass; they are neither homogeneous-nucleation temperatures nor measured optical thresholds.

The surviving liquid shell matters: even after outer volume has grown by 2.1 cubed, only about 20.2% of PFP mass is vapor in the smaller reference, and about 9.2% in the larger. Modeling the entire inclusion as a pre-existing gas discards this inventory constraint and the sensible/phase energy. Bulk boiling temperature and a constant latent heat alone cannot reproduce this control.

## 4. Gel stiffness and interface chemistry

PFP equilibria at matched stretch 2.1 and outer tension 54 mN/m:

| Initial diameter (µm) | Shear modulus (kPa) | State temperature (K) | State energy | Elastic resistance (kPa) |
|---|---|---|---|---|
| 0.6 | 5 | 337.26 | 11.57 pJ | 7.610 |
| 0.6 | 20 | 339.79 | 12.26 pJ | 30.438 |
| 0.6 | 100 | 351.43 | 15.55 pJ | 152.191 |
| 6 | 5 | 308.97 | 4.342 nJ | 7.610 |
| 6 | 20 | 313.78 | 5.476 nJ | 30.438 |
| 6 | 100 | 332.70 | 10.226 nJ | 152.191 |

Higher shear modulus increases gel resistance and the required finite-PFC state budget. Size changes which cost dominates; modulus is relatively more influential when capillary confinement is weaker. The new 20 kPa, stretch-2.1 resistance is **30.438 kPa**. It is a different state from the accepted outlet model's 9.143 kPa peak, not a correction to that result. Gel shear modulus also does not determine fracture toughness or strength; they must be measured independently.

For 0.6 µm-diameter PFP at 20 kPa modulus and stretch 2.1:

| Stipulated outer tension (mN/m) | State temperature (K) | State energy |
|---|---|---|
| 5 | 318.78 | 6.70 pJ |
| 18 | 325.42 | 8.39 pJ |
| 54 | 339.79 | 12.26 pJ |

Interface chemistry is a first-order input at the smaller size. Inner PFC liquid/vapor tension controls the core jump, whereas outer liquid/aqueous tension controls initial compression and gel traction. Published values belong to their actual interface, coating, composition and temperature. Neither a coated emulsion's low tension nor water/gas tension should be assigned to every interface. When the liquid shell disappears, a new gas/aqueous-gel interface and phase closure are needed.

## 5. Viscosity and radial expansion

PFP, 20 kPa shear modulus, the specified seed, and no hydraulic outlet:

| Initial diameter (µm) | Viscosity (Pa s) | Retained seed energy | Peak RADIAL speed (m/s) | End time (µs) | Endpoint |
|---|---|---|---|---|---|
| 0.6 | 0 | 13.50 pJ | 6.0888 | 0.0669 | stretch 2.1 screen |
| 0.6 | 0.01 | 13.50 pJ | 0.9596 | 0.3384 | stretch 2.1 screen |
| 0.6 | 0.1 | 13.50 pJ | 0.0957 | 1.5000 | time window ends; unfinished growth |
| 6 | 0 | 5.857 nJ | 4.1132 | 0.8470 | stretch 2.1 screen |
| 6 | 0.01 | 5.857 nJ | 2.7231 | 1.2022 | stretch 2.1 screen |
| 6 | 0.1 | 5.857 nJ | 0.4497 | 8.5620 | stretch 2.1 screen |

![Viscosity controls](assets/radial_viscosity_controls.svg)

At viscosity 0.01 Pa s, the 0.6 µm case reaches the declared stretch screen in 0.3384 µs with 0.9596 m/s peak radial speed; the 6 µm case reaches it in 1.2022 µs with 2.7231 m/s peak radial speed. These are wall speeds, not exterior or collapse jets. All six cases have **zero exterior emitted mass**. The high-viscosity smaller case has not finished expansion when its 1.5 µs reporting window ends; it must not be classified as a smaller maximum bubble solely from that cutoff.

The dimensionless viscous coefficient at 0.01 Pa s is 3.333 for the smaller radius and 0.333 for the larger. Increasing viscosity slows radial growth within these matched-seed controls. It need not universally reduce velocity through an independently imposed outlet: the earlier outlet architecture can redirect energy between wall motion and discharge. Different observables and architectures require separate comparisons.

## 6. Equilibrium existence and stability

All 132 sampled stationary states have finite inventory, positive liquid-shell thickness, ordered phase densities and positive phase pressure-density slopes. They also pass a local **internal** phase/core Hessian test at fixed temperature, total volume and mass; minimum bulk-to-capillary curvature ratio is 20.4526. This does not imply nucleation accessibility or stability to all shape perturbations.

There are **36** non-restoring closed-energy radial states and **94** non-restoring fixed-temperature radial states. The thermal constraint changes the stability question. Halving the stretch perturbation changes closed-energy slopes by at most 3.205e-05 relative, with no sign changes. Hence successful phase-root convergence alone is insufficient to choose a sustainable expansion branch.

![Radial stability comparison](assets/radial_stability.svg)

## 7. Laser, cover and fracture: what the budgets do and do not decide

At an illustrative **local incident** fluence of 20 mJ/cm² (200 J/m²), the projected-disk incident energies are 56.55 pJ and 5.655 nJ for the 0.6 and 6 µm diameters. The PFP stretch-2.1 state budgets divided by those disk energies are 0.217 and 0.968. These are required effective cross-section ratios under a lossless all-energy-to-state comparison, not measured absorption fractions or activation thresholds. A cross section divided by geometric area is not automatically bounded by one. Absorber/coating heating, depth attenuation, heterogeneous sites and preparation losses remain unknown. The published nanodroplet threshold in [S7](https://doi.org/10.3390/nano13152238) belongs to a different diameter, formulation, temperature and exposure history.

Using a stipulated host thermal diffusivity 1.4 × 10^-7 m²/s and 5 ns pulse, the Fourier numbers are 0.00778 and 0.0000778. Small values indicate spatially confined pulse heating, not uniform PFC temperature. The activation stage therefore needs spatial heat transfer and a rate/probability model before the present equilibrium closure can be applied after a seed has formed.

The crack-work comparison sweeps cover 1/5/20/50 µm, slit half-width 0.5/1/5 µm, and toughness 0.1/1/10/100 J/m². These are hypothetical slit costs, not measured gel ranges or computed crack paths. For a 20 µm cover, 0.5 µm half-width and 1 J/m² toughness, slit work is 20 pJ. The retained seed budgets are 13.50 pJ for the smaller PFP case and 5.857 nJ for the larger. The smaller budget is below that cost if only retained seed energy is allocated; this is **not a proof of fracture impossibility**, because cooling, changed interface topology, prestress and other reference-subtracted energy changes can alter available work. The larger budget exceeding it likewise proves neither initiation nor a connected aperture.

![Fracture budget comparison](assets/fracture_budget.svg)

Finite depth is an independent gate. Center distance to the initial free-surface plane equals radius plus cover. A 3 µm-radius droplet under 1 µm cover has an initial-plane encounter stretch of 1.333, before the 2.1 screen. Its infinite-host history cannot serve as a quantitative intact-interior prediction for that depth. The CSV records this geometry gate and standoff for every comparison; even cases not intersecting the initial plane require finite-domain convergence.

## 8. A concrete route to the full embedded model

| Stage | Model change | Required independent observable |
|---|---|---|
| 1. Laser and onset | Spatial absorber/PFC/water/gel heat transfer; normalized optical source; metastable liquid and calibrated heterogeneous nucleation hazard | Absorbed/local fluence and activation probability over size/fluence |
| 2. Intact expansion | Finite PFC and aqueous inventories; curved interfaces and phase-transfer heat balance; finite-depth gel dynamics; shell inertia/rate rheology when needed | Radius-time trace, displacement field, temperature/composition evidence |
| 3. Channel formation | Measured rate-dependent strength and fracture energy; cohesive/damage law; actual gap aperture, fluid filling and pressure work | Crack time/path/opening, ejection threshold versus cover |
| 4. Exterior ejection | Connected crack/outlet plus supplied liquid and exterior free surface; integrated mass, kinetic-energy and momentum flux | Emitted mass, velocity history and impulse |
| 5. Collapse and pressure | Nonspherical compressible multiphase calculation, actual boundary/receiver and sensor averaging | Resolved jet movies, hydrophone trace, location/bandwidth and impulse |

The executable development contract is in [IMPLEMENTATION_HANDOFF.md](IMPLEMENTATION_HANDOFF.md), including initial/boundary conditions, proposed numerical tolerances, calibration controls and held-out comparisons. Start with one 6 µm-diameter PFP inclusion and a specified free surface as a practical micro-scale validation geometry, then retain the 0.6 µm case to expose curvature/viscosity effects. This is a proposed validation order, not an optimized droplet choice or a target recipe. Measure the actual optical absorption, high-rate gel properties, fracture toughness/strength and depth before quantitative target prediction. Damage in a solid model must be coupled to an actual fluid-filled path; an initially imposed outlet only verifies discharge after a path exists.

## 9. Numerical evidence and delivery

The native/reference audit passes: maximum stationary relative difference **4.516e-09**, maximum normalized transient waveform difference **2.958e-05**, and maximum native normalized energy residual **4.971e-09**. Independent DOP853/Radau controls and tighter steps agree; thermodynamic entropy drift is checked separately from the imposed energy equation. Fresh-process native reload/refinement evidence is delivered in `verification/`. The independent mathematical review identified and corrected seed-energy wording, fracture-budget bounds, finite-cover applicability, branch guards, stability scope and local notation.

Open [index.html](index.html) for the offline reader and computed-state selector. Native models are [curved equilibrium](models/Embedded_PFC_Curved_Equilibrium.mph) and [post-nucleation intact gel](models/Embedded_PFC_PostNucleation_Intact_Gel.mph). They are new files; the accepted ideal-gas/outlet models remain unchanged. The package includes runnable Java/Python sources, raw parameter/native/reference CSVs, LaTeX and printable derivation, source copies, and verification records. See [README.md](README.md) for reproduction commands.

**Completion status:** the reduced finite-PFC feasibility and parameter comparison is completed and numerically verified. The actual embedded laser-to-fracture-to-jet mechanism remains a specimen-specific spatial validation task; none of its missing mechanisms is relabelled as solved by conservation or solver agreement.
