# How to complete the actual embedded-droplet mechanism

The delivered native models solve a finite-PFC phase/mechanical screen. The sequence below defines the additional work and measurable acceptance gates needed to make a specimen-specific embedded-droplet model predictive. Each gate has a distinct observable; agreement with a gas/outlet control cannot substitute for it.

## A. Fix the specimen and observable

Record PFC species/purity, radius distribution explicitly as **radius or diameter**, shell chemistry/thickness, absorber type/loading/cross section, gel formulation/hydration, inclusion center depth and cover thickness, gel thickness/support conditions, surrounding liquid/air and initial temperature. Measure the laser wavelength, pulse shape, local fluence and focal spot at the specimen. Specify the desired output: activation probability, radius history, intact gel load, channel creation, exterior emitted mass/impulse, internal collapse jet, or pressure at a sensor.

Use the 6 µm-diameter PFP inclusion and a single free surface as the first spatial geometry if the sample is not yet fixed. This matches one published size class and keeps curvature corrections smaller than in a nanodroplet; it is a practical validation choice, not a demonstrated optimum. Retain a 0.6 µm-diameter case as the curvature/viscous comparison. The current calculations use 20 kPa shear modulus and 0.01 Pa s viscosity only as controls. Do not identify a reported Young's modulus with shear modulus; for an approximately incompressible small-strain material, divide Young's modulus by approximately three after checking the measurement convention.

## B. Resolve laser heating and activation first

Build spatial heat transfer for absorber, PFC, coating and aqueous gel, with heat-source normalization such that the integral of deposited power equals the measured absorbed energy. A spatially confined pulse requires local temperature, not a uniform-droplet temperature assumption. Resolve the absorber's thermal contact or represent it with a calibrated heat-transfer source. The PFC/gel boundary passes heat; the far thermal boundary starts at the measured ambient temperature. Verify the source integral and sensible heating against an analytic constant-property control, then refine the spatial/time grid around the absorber and pulse.

Before vaporization, retain a metastable liquid state where physically meaningful. Use a calibrated heterogeneous nucleation hazard with absorber/site geometry and the actual liquid pressure. Compare activation/no-activation fractions over fluence using no-absorber, no-droplet and liquid-water controls. A successful phase-equilibrium root is not an activation event. Neither ambient boiling temperature nor a conditioned population's threshold supplies a single-droplet target threshold.

Required evidence: pulse-energy/source normalization error below 0.5%; activation probability versus fluence and size; repeatability and uncertainty; local temperature or an independently supported absorber heat model. These numerical tolerances are proposed project criteria, not universal accuracy standards. A minimum of three distinct fluences around onset is a screening experiment, not enough by itself to establish a reliable probability distribution.

## C. Couple finite phase inventory to prefracture mechanics

Start with one nucleated inclusion and an intact host. Preserve separate PFC liquid/vapor inventories and, if heating creates water vapor, a separate aqueous-vapor inventory. Use the real-fluid EOS for PFC and consistent energy references. Resolve interface curvature, phase-transfer kinetics and the latent enthalpy flux in the interfacial heat balance. Do not add latent heat again if already included by an enthalpy/internal-energy formulation. Include liquid-shell inertia and thermal gradients when their omission changes the radius history.

For early growth far from external boundaries, compare with the delivered spherical core/shell control under its exact insulated/equilibrium assumptions. Then add finite-depth 2D axisymmetric gel and fluid domains, finite deformation, appropriate dynamic viscoelasticity and moving interfaces. Axisymmetry is conditional on observed geometry. Use a finite outer-domain convergence check, stress-free/free-surface or measured support conditions, and explicitly represent pore-fluid drainage if the undrained timescale screen fails. Keep radius forcing and pressure forcing separate; imposing both measured radius and an arbitrary pressure history overconstrains the mechanics.

Required evidence: mass residual below 0.1%, total-energy residual below 1%; mesh/time/domain refinement changing maximum radius, event time and defined load by less than 2%; radius-versus-time and displacement-field agreement on **held-out** laser energies/gel formulations. Acceptance against measurements must incorporate their uncertainty; a provisional 10% radius or timing target is meaningful only when the observations are more precise than that. Fit absorber energy and gel viscosity with multiple independent observables so they cannot compensate silently for each other.

## D. Add fracture and a fluid-filled path

Measure high-rate gel strength, failure behavior and fracture energy at the relevant hydration and temperature. If the path is observed in advance, a calibrated cohesive law on that path is economical. If the path is unknown, use a tensile-driven damage/fracture model with a justified regularization length and crack-path validation. [COMSOL's damage documentation](https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_solid.07.040.html) and [cohesive example](https://doc.comsol.com/6.4/doc/com.comsol.help.models.sme.cohesive_zone_debonding/cohesive_zone_debonding.html) describe available solid-mechanics routes; license/module availability must be checked on the actual installation.

Decide how a crack becomes a fluid domain. A soft/damaged solid element does not automatically become a liquid channel. A cohesive gap needs aperture, contact, pressure loading and fluid filling; a diffuse fracture description needs a coupled permeability/aperture or a consistently remeshed fluid region. Demonstrate that changing this coupling does not create or destroy mass or add unaccounted pressure work. A fixed ALE mesh cannot simply change topology when an initially intact ligament opens. Prescribing a channel from the start tests the pre-channel control, not channel formation.

Required evidence: crack initiation time/location, opening/path to free surface, measured threshold for exterior ejection, fracture-energy accounting, and mesh/regularization convergence. Calibrate on one cover thickness and predict a different thickness. Include an intact sealed control, a deliberately pre-opened channel control and a tougher-gel control. Keep cover thickness, crack width and fracture energy as separate inputs; modulus does not determine toughness.

## E. Resolve exterior ejection, collapse and sensor pressure

Once a hydraulic connection exists, solve exterior liquid supply, actual aperture and free surface. Integrate outlet mass flux, kinetic-energy flux and momentum flux over time. Compare expelled mass and impulse rather than deriving them from a peak-speed ratio. Follow gas/liquid composition as the liquid PFC shell vanishes; the resulting gas/aqueous-gel interface has a different law. Include receiver geometry and jet breakup if transfer success is the output.

Internal collapse jets require nonspherical geometry and compressible multiphase fluid conservation. Spherical radial motion cannot predict their direction or tip speed. Start with a water bubble near a known boundary as a jet benchmark, then a specified gas/gel boundary, then the actual PFC/water-vapor mixture and damaged geometry. Resolve acoustic propagation and the actual sensor/receiver point and averaging interval. Use an appropriate equation of state, physical damping/radiation boundary and a shock-capable numerical method. A dynamic-pressure scale or water-hammer scale is not a resolved impact peak.

Required evidence: high-speed shape/jet movies, collapse time, hydrophone/receiver location, bandwidth and impulse, pressure-trace convergence with mesh/time/bandwidth, and comparison against held-out cases. A singular incompressible collapse-pressure extrapolation fails this gate regardless of conservation of the earlier expansion control.

## F. Parameter program and deliverable contract

Sweep size, PFC species, outer/inner interface chemistry, local optical fluence/absorption, gel dynamic modulus/viscosity, cover thickness, fracture strength/toughness, pore permeability and gas content. Use one-factor screens to identify regimes, then a structured interaction design for the dominant terms. Hold **absorbed energy** fixed for a mechanical material comparison; hold **incident fluence and actual absorption law** fixed for an optical design comparison. These are different experiments. Propagate measured input intervals to output intervals and report excluded branches and failed solves.

Freeze calibration inputs before the held-out comparisons. Deliver the solved spatial model, source/parameter ledger, source-energy integral, complete phase/mass/energy accounting, native exports, independent numerical controls, convergence evidence and a clear list of measured versus assumed quantities. Only after gates B–E pass for the target architecture can the full embedded PFC mechanism be labelled validated.

