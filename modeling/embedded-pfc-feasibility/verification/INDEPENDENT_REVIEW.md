# Independent mathematical review and resolution

One separate read-only reviewer audited the reduced equations and archived inputs on 2026-10-11. This is independent agent review within the project, not experimental validation or external peer review. No target-specimen measurements were supplied.

The review found no substantive algebraic error in the finite-mass inventory, curved chemical/traction equilibrium, distinct interface energies, spherical neo-Hookean strain energy, host kinetic energy, viscous loss, or first-law cancellation under the declared approximations.

| Finding | Resolution and practical consequence |
|---|---|
| Reference-subtracted seed energy was presented as an upper fracture-work bound without proving a lower bound on other energies | Changed all fracture CSV screens and Eq. E27 to a retained-seed-only allocation comparison. No energetic impossibility is inferred. |
| Seed endpoint energy omitted preparation losses | Renamed native parameter to `Eseed`, Python summary to `retained_seed_energy_J`, and report/derivation definitions accordingly. Pre-seed conduction, gel/acoustic losses and energy absorbed by other materials remain uncomputed. |
| Python transient bypassed its phase-domain checks | Added shared finite-state, ordered-density, positive-pressure/compressibility, temperature, inventory and shell guards to the actual RHS. Domain violations abort rather than produce a reported continuation. Native phase-exhaustion/Mach/stretch/turning screens remain active. All delivered states pass the independent domain audit. |
| Infinite-host histories were compared with arbitrary cover thickness | Added center distance, initial-plane encounter stretch, standoff and geometry-gate columns. Shallow cases cannot be treated as coupled finite-depth predictions. |
| Radial restoration was described too broadly | Restricted it to the reduced radial branch and stated thermal constraint; added half-increment convergence and a separately derived fixed-(T,V,m) phase/core Hessian test. All 132 internal Hessians are positive; this is not global or nonspherical stability. |
| Local notation and uniform-rate hazard assumptions | Added missing temperature/time/glossary definitions and the general space-time hazard integral, with the uniform-rate reduction explicitly labelled. |

The reviewer supplied the core/phase Hessian derivation and independently computed its signs from archived states; the project implementation now reproduces that test. Corrections were followed by numerical regression checks and static/PDF regeneration. The retained equations are conditional controls; laser activation, damage/path creation, water-vapor/gas composition, shell kinetics, collapse jets and resolved sensor pressure remain outside their solved scope.

Final read-only review of the corrected comparison and derivation accepted them as a conditional feasibility/numerical-verification deliverable, with no remaining substantive scope issue. It confirmed that neither claims target-specific activation, fracture, jet or impact-pressure validation.
