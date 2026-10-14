# Conditional PFC attainability problem — specification in progress

**Status:** S1 is not complete. Application decisions, observables, caloric EOS, phase/heat laws and the detached-wall transport baseline are selected. Their native components and ideal-material pressure-work core have passed separate checks, while the complete geometric coupling, critical/cooling paths, detached-film coverage and event/domain conditions remain under verification. `PREREGISTRATION.json` is an unfrozen draft. No optimization campaign or attained optimum is reported. Open items at the end of this document must be closed before calling this a single verified initial–boundary-value problem.

The requested output is the greatest directed water-carrier speed at each prescribed participating mass, and the greatest solved rigid-wall pressure at each prescribed space/time average, attainable from one thermally activated PFC droplet. The answer is conditional on preparation and constitutive assumptions, and does not determine the user's actual device maximum. The accepted energy/contact/cutoff ceilings in `../conditional_termtex` remain unchanged; the present work concerns attainability.

## 1. Preparation and application decisions

H0: deposition is thermal and excludes optical breakdown. H1: the entire PFC droplet is uniformly activated before the modeled motion. H2: the accepted preparation is isobaric at ambient pressure, with the finite-droplet Laplace correction neglected in the preparation EOS. H3: after activation, no further useful energy or work is supplied; the far environment is at the stated dead state. H4: continuum equations and the explicitly declared thermodynamic and transport closures are adopted. None of these assumptions is a measured property of a device.

The initial unheated diameter is 6 micrometres. Ambient temperature is 293.15 K and absolute pressure is 101325 Pa. The carrier is water, air-free and without gel, above an impermeable rigid planar receiver. `data/accepted_preparation.json` copies the accepted source records in `expert_resolution/data/thermo_ceilings.json`, with their original hash and locators, without repeating the verified activation calculation.

| Species | Activated temperature (K) | PFC mass (kg) | Accepted activated availability (J) | Accepted activation heat (J) |
|---|---:|---:|---:|---:|
| PFP | 386.48623647227214 | 1.8337513994824743e-13 | 2.722572407203039e-9 | 1.9856954254439094e-8 |
| PFH | 415.2367593324791 | 1.912192981884642e-13 | 4.622122564638143e-9 | 2.7127507911661847e-8 |

These are inputs and thermodynamic allowances, not attained output speeds or wall loads. Surface energy is tracked relative to the activated initial interface, not silently set to zero during collapse; see `SYSTEM_EXERGY_CONVENTIONS.md`, B13. An initially uniform pressure and a curved tension-bearing interface are mechanically unbalanced when the preparation Laplace correction is neglected. The dynamic initial adjustment must be solved and included in the ledger; it cannot be removed by a hidden equilibrium reset.

The user approved D6/D7/D8 in one answer, quoted verbatim:

> Detached cavity: γ ≥ 1.25; confirm the listed masses and pressure averages (recommended).

D7 means **all aqueous liquid-carrier mass**, throughout the spatial domain, including every interfacial water fraction. It does not mean a geometrically selected jet. PFC is a distinct material; its kinetic energy is included in the total ledger and reported separately, rather than silently discarded or inserted into the water-carrier velocity observable.

## 2. Coordinates, operators and notation

The receiver is the plane of axial coordinate zero. Cylindrical radius is nonnegative; the initial droplet centre lies above the receiver. Directed speed is positive toward the receiver. Pressures are absolute except explicit gauge differences. All integrals include the axisymmetric volume/area Jacobian; a meridional cell area alone is not a physical volume. In a Basilisk axisymmetric grid with axial coordinate `x` and radial coordinate `y`, the declared axial velocity is `u.x` and radius is `y`.

| Symbol | Definition and domain | Unit |
|---|---|---|
| \(r,z,t\) | cylindrical radius, axial height, time since activated preparation | m, m, s |
| \(h,R_a,R_m,\gamma\) | initial centre height, activated outer radius, same-model free-field maximum outer radius, stand-off | m, m, m, dimensionless |
| \(\alpha_c,\xi\) | condensation accommodation coefficient in the selected kinetic law; PFC vapour mass fraction | dimensionless, each in [0,1] |
| \(T_0,p_\infty\) | ambient dead-state temperature and absolute pressure | K, Pa |
| \(\rho,\boldsymbol u,u_z,w,p,T,e,s\) | density, velocity, axial component, directed component, pressure, temperature, specific internal energy and entropy | kg/m³, m/s, m/s, m/s, Pa, K, J/kg, J/(kg K) |
| \(f_w,f_F\) | water and PFC material-volume fractions; they sum to one | dimensionless |
| \(\rho_w,\rho_F\) | density intrinsic to the water/PFC material | kg/m³ |
| \(g_l,g_v,g_F,v_F\) | specific Gibbs potentials of liquid/vapour PFC and their frozen-composition mixture; PFC specific volume | J/kg, J/kg, J/kg, m³/kg |
| \(\boldsymbol\tau,\boldsymbol q\) | complete viscous stress and conductive heat flux | Pa, W/m² |
| \(\mu,\zeta,k,\sigma\) | nonnegative shear viscosity, bulk viscosity, thermal conductivity, constant outer surface tension | Pa s, Pa s, W/(m K), N/m |
| \(A_b,V_b,j,A_{\rm phase}\) | actual outer PFC area and volume, evaporation-positive phase mass flux, effective phase-transfer area | m², m³, kg/(m² s), m² |
| \(m_*,U,m_{\ge U},K_w,K_F\) | positive water participating mass, nonnegative velocity threshold, water mass above threshold, full-vector water and PFC kinetic energies | kg, m/s, kg, J, J |
| \(t_{\rm imp},t_{\rm grow},t_{\min},t_U,t_{\rm end}\) | first axial carrier-liquid contact inside content; first growth maximum; first subsequent collapse minimum; velocity-window end; subsequent first rebound maximum | s |
| \(r_o,\tau_o,P,J_U,J_P\) | observer-disk radius, averaging duration, disk-averaged gauge pressure, velocity objective, pressure objective | m, s, Pa, m/s, Pa |
| \(\mathcal D,\epsilon_U,\epsilon_P,\delta_{\rm num}\) | design set, relative velocity/pressure tolerances, relative numerical error | dimensionless apart from design coordinates |

Subscripts are material, reference, or event labels, not multiplication. A dot is a time derivative. Gradient and divergence act on physical coordinates; indicator functions equal one when their predicate holds and zero otherwise; supremum is the least upper bound; maximum requires attainment. Tensor product and contraction have their ordinary component definitions. Numerical superscripts are powers; transpose is a tensor transpose. Thermodynamic derivatives hold every other named argument fixed. Every new constitutive parameter must be added to this glossary before the corresponding equation is finalized.

## 3. Governing continuum class and initial/boundary conditions

Each material obeys mass, momentum and total-energy conservation with a caloric EOS, as written and derived for the ledger in `SYSTEM_EXERGY_CONVENTIONS.md`, B01–B06. `PRESSURE_WORK_AND_PROJECTION.md` derives the conservative pressure-energy partition and final actual EOS pressure residual. `TRANSPORT_AND_SURFACE_WORK.md`, TS01–TS11, specifies full axisymmetric Newtonian stress, mass-assigned kinetic work, viscosity-volume-assigned intrinsic heating, water Fourier exchange and actual outer surface energy. `verification/TRANSPORT_SELECTION_001.json` records the selected constants and original PFC viscosity proxy. Direct viscous, heat and phase entropy sources are computed separately; finite work or area defects are numerical errors and cannot become inferred destruction.

The selected water EOS is the one-potential caloric Mie–Grüneisen completion in `WATER_MIE_GRUNEISEN_CANDIDATE.md`, recorded before native verification in `verification/PRODUCTION_WATER_SELECTION_001.json`. Its pressure/density principal Hugoniot is calibrated to Stewart–Ahrens2005 Eq18; constant isochoric heat capacity and a constant Grüneisen coefficient are calibrated to ambient IAPWS properties and then adopted as constitutive premises. `verification/WATER_MG_SOURCE_QUALIFICATION_001.json` separates those thermal assumptions from the source's alternatives and strict fit endpoint. Its tensile reference is an explicit metastable-liquid extension. A single Helmholtz energy determines pressure, internal energy, entropy, temperature and sound speed. Off-Hugoniot thermal/release accuracy is not established by matching the shock fit. Native property/inverse checks have passed in `verification/Water_MG_native_attempt002.json`; actual flow/shocks, reached-state coverage and coupled transport remain pending. The selected tensile premise is absolute pressure not below -100 MPa with strict EOS stability, an original conditional no-secondary-water-cavitation threshold rather than measured nucleation strength. A maximizing case on that validity threshold is unacceptable. The earlier sourced NASG remains a separately preserved implementation benchmark and sensitivity alternative; its successful tests do not verify the new production EOS.

The preferred production architecture now being assessed resolves PFC material inertia and spatial pressure. In each PFC cell, the liquid and vapour share local pressure and temperature but need not be in chemical equilibrium. A frozen-composition Gibbs potential defines all properties; finite phase conversion conserves cell mass and total energy. This local common-pressure condition does **not** impose one uniform pressure over the entire cavity.

**Symbols before Eq. (P01):** PFC vapour mass fraction \(\xi\in[0,1]\); Gibbs potentials \(g_l(p,T),g_v(p,T),g_F(p,T,\xi)\) (J/kg); pressure \(p\) (Pa); positive temperature \(T\) (K); specific volume \(v_F\) (m³/kg), entropy \(s_F\) (J/(kg K)), and internal energy \(e_F\) (J/kg). A subscripted partial derivative holds the displayed remaining arguments fixed.

$$
\begin{aligned}
g_F(p,T,\xi)&=(1-\xi)g_l(p,T)+\xi g_v(p,T),\\
v_F&=\left(\frac{\partial g_F}{\partial p}\right)_{T,\xi},\qquad
s_F=-\left(\frac{\partial g_F}{\partial T}\right)_{p,\xi},\\
e_F&=g_F+Ts_F-pv_F .
\end{aligned}
\tag{P01}
$$

The mixture includes the condensed PFC volume. Properties and derivatives come from the same thermodynamic potential; independently interpolating pressure, energy and entropy would not preserve the Gibbs identity. Stable/metastable branches are the components connected to the physical dilute vapour and dense liquid branches. Neither an absent virtual phase nor a failed lookup can trigger an unrecorded numerical reset. The selected continuous affinity birth/spinodal completion is recorded in `verification/PRODUCTION_PHASE_SELECTION_001.json` and its path/documentary addenda, with exact equations in `verification/SELECTED_PHASE_DOMAIN_001.md`. Fixed-volume/energy entropy tests and numerical root uncertainty are distinct from the still-unproved uniform critical invariant-domain premise; critical/cooling and complete coupled paths remain required checks.

The selected D5 kinetic interpretation is declared in `verification/S2_PREREGISTRATION_AMENDMENT_001.json`, which preserves the original preregistration and all prior bidirectional prototypes. `CONTENT_THERMODYNAMICS.md` CT03-CT04 derives the law and checks its entropy sign and equal-coefficient Schrage limit. It fixes evaporation accommodation at one and uses the design coefficient only on the condensation-sign branch of the net fugacity difference. This is an original conditional constitutive premise with HKS scaling, not a published unequal-forward/backward Schrage formula or measured PFC kinetics. The separately selected bulk completion shares the Gibbs-affinity sign, with exact endpoint tangent projection. Alpha zero suppresses HKS condensation while permitting evaporation and the separately declared bulk conversion. No source or reference is switched to an ideal vapour at extinction.

The native production normalization and area convention are selected before coupled runs in `verification/PRODUCTION_CONVENTIONS_001.json`. The mass-specific gas constant uses the exact universal-constant normalization stored in the selected HEOS potential, 8.314462618 J/(mol K) divided by species molar mass. This gives the same Gibbs-affinity/fugacity identity in every native component. The earlier Python prototype's extra universal-constant digits are preserved in its evidence; their relative normalization difference is 1.84e-11, not a fit or a source-accuracy claim.

**Symbols before Eq. (P01a):** fixed accepted PFC inventory \(M_F>0\) (kg); actual complete outer PFC/water interface area \(A_b(t)\) (m²), including every detached fragment; PFC cell-volume mass density \(c_F=f_F\rho_F\) (kg/m³); mass-specific area \(a_M\) (m²/kg); effective local phase area density \(a_{\rm ph}\) (m⁻¹); signed HKS-scaled mass flux \(j\) (kg/(m² s)); PFC vapour mass fraction \(\xi\); material derivative \(D/Dt=\partial/\partial t+\boldsymbol u\cdot\boldsymbol\nabla\); phase entropy-generation density \(\dot s_{\rm ph}\) (W/(m³ K)); local Gibbs potentials \(g_l,g_v\) (J/kg) and temperature \(T>0\) (K). The derivative here denotes the phase-transfer contribution alone.

$$
\begin{aligned}
a_M(t)&=A_b(t)/M_F,\qquad a_{\rm ph}=c_Fa_M,\\
\left.\frac{D\xi}{Dt}\right|_{\rm HKS}&=a_Mj,\\
\dot s_{\rm ph}&=a_{\rm ph}j(g_l-g_v)/T\ge0.
\end{aligned}
\tag{P01a}
$$

Integrating the area density gives \(A_b\) when the conserved PFC mass equals the fixed inventory. Uniform local pressure, temperature and composition therefore recover the spherical \(A_bj\) HKS contribution, without a global pressure reset. The displayed entropy term is that HKS contribution; the total physical phase entropy uses the actually projected combined HKS/bulk rate, as specified in `verification/SELECTED_PHASE_DOMAIN_001.md` and its documentary clarifications. Reaction preserves local PFC mass, volume, momentum and energy; latent energy is already in the EOS and is not added again as a heat source. At zero or unit vapour fraction, a rate pointing outside the composition interval is inactive, while an inward rate may create the absent phase only if its physical branch exists. Conservative integration must locate an endpoint without clipping an accepted state. A narrow numerical sign bracket is not a bound on true root uncertainty when EOS/source evaluation noise is larger; `REACTION_NUMERICAL_CONTRACT.md` records the independent comparison and conditioning.

This is a declared nonlocal homogenized-area premise. A remote fragment's changing outer area immediately changes all local reaction coefficients. It does not resolve the internal liquid/vapour area or its surface energy, and it does not establish microscopic nucleation kinetics. Only the actual outer surface energy is tracked. `verification/PHASE_AREA_REVIEW.md` derives the normalization, homogeneous limit, entropy sign and an optional local-area sensitivity law. Production must separately audit area reconstruction, integrated area density and PFC mass; renormalizing by a drifting measured inventory is prohibited.


The selected thermal interface is the conservative nonlocal mass-weighted patch network in `NONLOCAL_THERMAL_INTERFACE.md`, selected in `verification/THERMAL_INTERFACE_SELECTION_001.json`. It reduces to the earlier spherical core/thermal-layer resistance in its homogeneous limit, uses only actual outer water/PFC contact patches, and carries direct positive entropy. Its label-neutral critical taper is a conditional transport hypothesis. Fixed-source native checks pass in `verification/native_thermal_component002.json`; that component result does not verify assembled PDE heat coupling. The physical state/transactional source convention is documented in SOURCE_DOMAIN_AND_SPLITTING.md; the positive PFC pressure path guard is enforced in both production caloric directions, while rejected numerical inversion/bracket probes and standalone pure-phase diagnostics remain separate.

The activated PFC starts at rest, with zero vapour mass and the accepted activated internal energy and entropy. The water starts at rest at the stated ambient state using the selected MG density and reference, rather than inserting an inherited density inconsistent with that EOS. Initial geometric discretization must preserve the accepted fixed PFC inventory without a thermodynamic reset. The outer environment imposes its ambient state with a verified nonreflecting or sufficiently remote boundary. The selected wall is stationary no-slip with zero normal conductive flux. The complete intrinsic viscous work/heating and outer capillary force/area ledger are specified in `TRANSPORT_AND_SURFACE_WORK.md`; native geometric, wall and AMR coupling are not yet verified. Detached wall films must be demonstrated through each objective horizon. No wetting/contact-line law is presently selected: any actual contact region remains unresolved and cannot be omitted from the global domain. Thermal and mechanical interface work must conserve total energy including outer surface tension. There is no restart at a spherical maximum radius or real/ideal EOS switch.

## 4. Admissible design set and what its bounds mean

Species and preparation are fixed separately; each species has a continuous accommodation/stand-off optimization. The accommodation interval is a physical kinetic range. The lower stand-off is a user-approved application bound. The word detached must also be checked against actual computed growth/contact geometry; the ratio alone is not a proof of a positive resolved liquid film.

**Symbols before Eq. (P02):** design set \(\mathcal D\), dimensionless accommodation \(\alpha_c\), initial centre height \(h>0\) (m), same-model free-field maximum radius \(R_m>0\) (m), and dimensionless stand-off \(\gamma\). Each species is optimized separately.

$$
\gamma=\frac{h}{R_m},\qquad
\mathcal D=\{(\alpha_c,\gamma):0\le\alpha_c\le1,\ \gamma\ge1.25\} .
\tag{P02}
$$

A computational scan ending at stand-off eight is not a physical or application upper bound. D10 requires extending the scan and enclosing the unsampled tail. Directed water speed has a nonzero spherical free-field limit; it cannot be assumed to decay to zero with stand-off. A compactification by inverse stand-off can help an existence argument, but its zero endpoint is the free-field limit and is not a finite-height attained design. The certificate must bound that endpoint/tail separately. Proof of continuity and existence across contact/no-contact/no-rebound regimes is still open; it will not be asserted from a finite sample plot.

## 5. Exact observables

The velocity mass levels are 1, 3, 10, 30 and 100 pg, with one pg equal to one trillionth of a gram. The water mass measure includes every water-containing cell fraction. Resting water outside the finite computation does not affect a positive threshold, but any unresolved moving mass outside the computation must be bounded and included in the numerical error.

**Symbols before Eq. (P03):** axial velocity \(u_z\), directed speed \(w\) and threshold \(U\ge0\) (m/s); water volume fraction \(f_w\) (dimensionless); intrinsic water density \(\rho_w>0\) (kg/m³); physical volume measure \(dV\) (m³); time \(t\) (s); superlevel water mass \(m_{\ge U}\) and prescribed mass \(m_*>0\) (kg); indicator \(\boldsymbol1\); water-domain integration; supremum of nonnegative thresholds.

$$
\begin{aligned}
w&=-u_z,\\
m_{\ge U}(t)&=\int f_w\rho_w\,\boldsymbol1[w\ge U]\,dV,\\
U(m_*,t)&=\sup\{U\ge0:m_{\ge U}(t)\ge m_*\},
\end{aligned}
\tag{P03}
$$

If the set is empty, the mass-qualified speed at that time is zero. This does not license setting an undefined event window to zero.

**Symbols before Eq. (P04):** directed mass-qualified speed \(U(m_*,t)\) and objective \(J_U(m_*)\) (m/s); prescribed water mass \(m_*>0\) (kg); time \(t\), first internal impact time \(t_{\rm imp}\), first post-growth collapse minimum time \(t_{\min}\), and the velocity observation-end time \(t_U\) (s). The first growth maximum time \(t_{\rm grow}\) (s) is the first positive-to-negative crossing of the total PFC volume rate after an interval of positive growth. The collapse minimum is the first negative-to-positive crossing after that maximum. Maximum is taken on a closed event-defined interval.

$$
J_U(m_*)=\max_{0\le t\le t_U}U(m_*,t),\qquad
t_U=\begin{cases}t_{\rm imp},&\text{impact occurs before the post-growth collapse minimum},\\
t_{\min},&\text{otherwise, if that collapse minimum exists}.\end{cases}
\tag{P04}
$$

The impact is the first axial carrier-liquid contact inside the PFC content, not contact with the receiving wall. The neglected preparation Laplace correction can produce a tiny initial compression minimum before flash expansion. That early extremum is recorded separately and does not define the main cavitation-collapse event. Every trajectory and objective interval still starts at time zero, retaining the initial motion, all early extrema and their energy transfers. This event clarification is recorded before affected runs in `verification/S2_PREREGISTRATION_AMENDMENT_002.json`. A no-growth/no-collapse regime is unresolved until the fixed objective is properly defined there or the regime is proved absent. An arbitrary simulation stop is not an event.

**Symbols before Eq. (P05):** full vector velocity \(\boldsymbol u\) (m/s), water and PFC volume fractions \(f_w,f_F\), intrinsic densities \(\rho_w,\rho_F\) (kg/m³), physical volume element \(dV\) (m³), full-vector kinetic energies \(K_w,K_F\) (J), and squared Euclidean speed \(|\boldsymbol u|^2\).

$$
K_w=\tfrac12\int f_w\rho_w|\boldsymbol u|^2\,dV,\qquad
K_F=\tfrac12\int f_F\rho_F|\boldsymbol u|^2\,dV .
\tag{P05}
$$

Any directed or sampled axial energy is explicitly labelled and does not replace these full-vector quantities.

The pressure disk radii are 2 and 10 micrometres. Averaging durations are 2 and 20 ns. Pressure is taken from the solved water stress/pressure at the rigid plane; contact and spreading estimates are not substitutes.

**Symbols before Eq. (P06):** observer radius \(r_o>0\) and dummy radius \(r\) (m); time \(t\), dummy time \(t'\), end time \(t_{\rm end}\), and duration \(\tau_o>0\) (s); wall pressure \(p_{\rm wall}\), ambient pressure \(p_\infty\), disk average \(P\), and objective \(J_P\) (Pa); circumference factor \(2\pi r\); maximum over windows entirely contained in the objective interval.

$$
\begin{aligned}
P(r_o,t)&=\frac{1}{\pi r_o^2}\int_0^{r_o}[p_{\rm wall}(r,t)-p_\infty]2\pi r\,dr,\\
J_P(r_o,\tau_o)&=\max_{0\le t\le t_{\rm end}-\tau_o}
\frac1{\tau_o}\int_t^{t+\tau_o}P(r_o,t')\,dt'.
\end{aligned}
\tag{P06}
$$

The end time is the first rebound maximum after the post-growth collapse minimum: the first subsequent positive-to-negative volume-rate crossing. It must exist and exceed the averaging duration. All averaging windows start at nonnegative time and can include the initial preparation adjustment; no earlier pressure history is discarded. The wall normal viscous stress is retained as a separate diagnostic, and its negligibility must be checked before interpreting pressure alone as the complete wall load. Pointwise pressure and internal-impact pressure remain diagnostics.

## 6. Tolerances, validity and certification

Relative objective tolerances are 5% for every velocity mass and 10% for every pressure observer. Numerical error must be at most one third of the corresponding tolerance; domain-doubling changes must be at most one tenth. The exergy residual must not exceed 1% of accepted activated availability at any saved objective time; local destruction must be nonnegative and nondecreasing, PFC mass error at most one part per million, and liquid mass error at most one part in ten thousand.

Numerical indicators include EOS inversion residuals, positive temperature/density, thermodynamic stability, intervention counts, endpoint/event resolution, resolved films, and the required eight cells across the fast-liquid radius. Failed runs and trial-state rejections stay recorded; no Mach stop, pressure screen or constitutive lookup limit is an optimum. Constitutive-domain excursions must be declared separately and sensitivity tested. Water's selected tensile premise, thermal/phase control variations and native potential accuracy have separate records; the actual reached-state envelope, source/domain margins and full sensitivity table remain to be computed.

An attained valid design and a global upper value with the required gap are both necessary. PLAN permits a numerically justified certificate using estimated curvature with a safety factor of at least two, hold-outs and numerical error. That lane must explicitly declare its uniform regularity/interpolation and tail premises, test them against independent samples, and cover every event regime and the infinite-stand-off tail. Finite second differences do not prove an unsampled derivative bound. A numerical certificate conditional on a supported premise is tier P; it is not a rigorous supremum proof. The optional rigorous-enclosure lane remains separate. No actual PFC enclosure is currently supplied.

## 7. D1–D11 record and remaining S1 decisions

| Decision | Record |
|---|---|
| D1 | Species PFP and PFH, optimized and reported separately. The attainability route is the scope described in the opening paragraphs, not this decision's species label. |
| D2 | 6 micrometre unheated diameter, accepted full homogeneous activated states; no optical deposition trajectory inferred. |
| D3 | Water at 293.15 K/101325 Pa, air-free, gel-free, rigid plane, axisymmetric. |
| D4 | Selected single-potential caloric Mie–Grüneisen water completion of the sourced principal Hugoniot, full Newtonian/Fourier transport and constant outer tension. Native property components pass; actual shock/geometric coupling, source coverage and detached-film domain verification remain pending. |
| D5 | Condensation accommodation in [0,1], with fixed unit evaporation accommodation. The selected original sign-dependent net-affinity mobility has HKS dimensional scaling; selected continuous affinity birth/spinodal conversion and endpoint tangent projection carry nonnegative direct phase entropy. Alpha zero suppresses HKS condensation while evaporation and separately declared bulk conversion remain active. Unequal-direction microscopic detailed balance is not claimed. Isoeq is outside the kinetic design set. Uniform critical invariance, cooling and full coupled paths remain unverified. |
| D6 | User-approved lower stand-off 1.25; exact answer quoted in section 1. |
| D7 | Confirmed masses {1,3,10,30,100} pg; full-domain aqueous-carrier definition, PFC kinetic energy accounted separately. |
| D8 | Confirmed disk radii {2,10} micrometres and durations {2,20} ns. |
| D9 | Fixed 5%/10% objective tolerances, numerical one-third, ledger 1%; no weakening. |
| D10 | Scan begins at 8, extends as necessary; the remaining tail requires an enclosure, not an assumed zero or application cutoff. |
| D11 | Corrections only in `ERRATA_TO_EXPERT_RESOLUTION.md`; E remains frozen. |

S1 closes only after: the selected conservative operators form one assembled model; critical/cooling/endpoint paths and initial pressure/surface/heat conditions are verified; detached-film coverage or a complete contact model covers every relevant regime; event existence/no-event treatment is resolved; and the supported global-domain/tail premises are stated. Preparation, application scope, objective formulas, constitutive choices and tolerances are recorded, but these unresolved links prevent a G1 PASS.
