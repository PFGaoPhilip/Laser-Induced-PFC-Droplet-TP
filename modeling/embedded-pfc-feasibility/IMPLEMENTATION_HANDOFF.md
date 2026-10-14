# Validation plan for an embedded PFC droplet

The native models solve finite-PFC phase equilibrium and radial mechanics. The following gates define specimen-specific prediction. Validate each observable independently.

## A. Fix the specimen and observable

Record species, purity and size distribution. Label every size as **radius or diameter**. Record shell chemistry/thickness, absorber loading/cross section, gel formulation/hydration, center depth, cover, gel thickness and supports. Record surrounding liquid/air and initial temperature. Measure wavelength, pulse shape, local fluence and focal spot. Define the required output: activation probability, radius history, gel load, channel creation, emitted mass/impulse, collapse jet or sensor pressure.

If the sample is unspecified, start with a 6 µm PFP diameter and one free surface. This matches a published size class and reduces curvature effects. An optimum is **not established**. Retain a 0.6 µm diameter for curvature/viscosity comparison. Current 20 kPa modulus and 0.01 Pa s viscosity are stipulated. For approximately incompressible, small-strain material, shear modulus is approximately Young’s modulus divided by three. Check measurement conventions before conversion.

## B. Resolve laser heating and activation first

Resolve heat transfer in absorber, PFC, coating and aqueous gel. Normalize deposited power to measured absorbed energy. Compute local temperature during confined heating. Resolve thermal contact or calibrate the absorber heat-transfer source. Permit heat transfer at PFC/gel interfaces. Initialize the far boundary at measured ambient temperature. Check source integral and sensible heating against a constant-property analytic case. Refine space and time around the absorber and pulse.

Retain metastable liquid before vaporization where physically meaningful. Calibrate heterogeneous nucleation using site geometry and liquid pressure. Measure activation fractions versus fluence. Include no-absorber, no-droplet and water controls. Phase-root convergence does not establish activation. Ambient boiling temperature and conditioned-population thresholds cannot calibrate the target droplet.

**Evidence:** source-normalization error below 0.5%; activation probability versus fluence and size; repeatability and uncertainty; local temperature or an independently supported absorber model. Tolerances are proposed project criteria. Three onset fluences provide an initial screen. A reliable probability distribution needs additional trials.

## C. Couple finite phase inventory to prefracture mechanics

Begin with one nucleated inclusion and intact host. Track PFC liquid and vapor masses separately. Add aqueous-vapor inventory if water vapor forms. Use real-fluid EOS and consistent energy references. Resolve curvature, phase-transfer rate and interfacial enthalpy flux. An enthalpy/internal-energy formulation may already include latent heat; avoid double counting. Add shell inertia and thermal gradients when radius histories require them.

Benchmark early interior growth against the spherical model under its stated assumptions. Add finite-depth axisymmetric gel/fluid domains, finite deformation, dynamic viscoelasticity and moving interfaces. Use axisymmetry when observations support it. Refine the outer domain. Apply measured support or free-surface conditions. Resolve drainage if the undrained timescale condition fails. Choose radius or pressure forcing consistently. Imposing measured radius and arbitrary pressure together overconstrains mechanics.

**Evidence:** mass residual below 0.1%; energy residual below 1%; mesh/time/domain refinement changes radius, event time and load by less than 2%. Compare radius histories and displacement fields at **held-out** energies and formulations. Include measurement uncertainty. A provisional 10% agreement target needs more precise observations. Fit absorber energy and viscosity using independent observables.

## D. Add fracture and a fluid-filled path

Measure high-rate strength and fracture energy at relevant hydration and temperature. Use a calibrated cohesive law when the crack path is known. Otherwise validate a tensile damage/fracture law and regularization length. [COMSOL damage documentation](https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_solid.07.040.html) and the [cohesive example](https://doc.comsol.com/6.4/doc/com.comsol.help.models.sme.cohesive_zone_debonding/cohesive_zone_debonding.html) describe available implementations. Check installed modules and licenses.

Specify how a crack becomes a fluid domain. A cohesive gap needs aperture, contact, pressure and filling. Diffuse damage needs a permeability/aperture coupling or consistent fluid remeshing. Check mass conservation and pressure work during coupling. Fixed ALE topology requires an explicit treatment when a ligament opens. An initially prescribed channel tests discharge through an existing path.

**Evidence:** initiation time/location, crack opening and surface connection, exterior-ejection threshold, fracture work and mesh/regularization convergence. Calibrate one cover thickness and predict another. Include sealed, pre-opened and tougher-gel controls. Cover, width and toughness are separate inputs.

## E. Resolve exterior ejection, collapse and sensor pressure

After hydraulic connection, solve liquid supply, aperture and exterior free surface. Integrate mass, kinetic-energy and momentum flux over time. Compare emitted mass and impulse directly. Track composition when the liquid shell disappears. Use the resulting gas/aqueous-gel interface law. Include receiver geometry and breakup for transfer predictions.

Collapse jets require nonspherical, compressible multiphase conservation. Benchmark a water bubble near a known boundary. Then test a gas/gel boundary and the actual PFC/water-vapor mixture with damaged geometry. Resolve acoustic propagation, receiver position and sensor averaging. Use a suitable EOS, radiation/damping boundaries and a shock-capable method. Impact peaks require resolved pressure histories.

**Evidence:** high-speed shape and jet images, collapse time, sensor position, bandwidth, impulse and pressure convergence with mesh/time/bandwidth. Compare held-out cases. Singular incompressible pressure extrapolation fails this gate.

## F. Parameter program and deliverable contract

Sweep size, species, interface chemistry, fluence/absorption, dynamic modulus/viscosity, cover, strength/toughness, permeability and gas content. Screen one factor at a time, then test dominant interactions. Mechanical comparisons hold **absorbed energy** fixed. Optical comparisons hold **incident fluence and absorption law** fixed. Propagate measured input intervals and report rejected branches and failed solves.

Freeze calibration inputs before held-out tests. Deliver spatial models, source/parameter ledger, source integral, phase/mass/energy accounting, native exports, independent controls and convergence evidence. Separate measured and assumed inputs. Target-mechanism validation requires gates B–E to pass for the target architecture.
