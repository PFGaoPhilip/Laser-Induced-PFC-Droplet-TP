**A conditional theoretical solution is possible without device measurements.** Fix the available mechanical work and the participating jet mass, then choose a contact-pressure model. Below is the same solution with actual stacked Math-TermTex formulas.

Assume a uniform liquid jet moving normally toward an initially stationary planar receiver. Positive velocity points into the receiver; contact pressure means compression above ambient. There is no subsequent energy input. Lossless conversion defines the energy ceiling, and first-contact pressure is evaluated before lateral release. Linear contact formulas additionally require weak compression in both media.

The notation is fixed throughout:

| Symbol | Meaning and domain | Unit |
|---|---|---|
| E_av; K_j | Nonnegative available mechanical work; jet kinetic energy | J |
| m_j | Prescribed positive participating jet mass | kg |
| U_j; v | Nonnegative uniform jet speed; interface velocity toward receiver | m/s |
| rho, written ρ; c | Positive liquid density; positive sound speed | kg/m^3; m/s |
| Z_j; Z_t | Jet acoustic impedance; nonnegative receiver impedance | Pa·s/m |
| Delta p_c, written Δp_c | First-contact pressure above ambient | Pa |
| a; L; M | Positive cylindrical-jet radius; positive length; Mach number | m; m; dimensionless |
| t; R(t); x | Time; spherical-bubble radius; dummy radius under integration | s; m; m |
| R_max; R_min | Positive initial maximum bubble radius; prescribed cutoff radius | m |
| Rdot; Rddot | First and second time derivatives of radius | m/s; m/s^2 |
| Delta p, written Δp | Constant positive far-field pressure minus cavity pressure | Pa |
| q(R); q'(R) | Squared wall speed; its derivative with respect to radius | m^2/s^2; m/s^2 |
| U_wall,max | Largest inward wall-speed magnitude on the prescribed radius interval | m/s |

Subscripts j, t and c label the jet, target and contact; av labels available work. The label max denotes a maximum in the stated model. Superscripts energy, linear, rigid and equal are model labels; numerical superscripts are powers. PFP and PFH later label perfluoropentane and perfluorohexane. Multiplication, division and comparisons have their usual real-number meanings; roots are nonnegative roots. Dots mean time derivatives, a prime means differentiation in radius, and integrals below are definite integrals of continuous functions.

**1. Derive the energy ceiling.** This is a consequence of the available-work budget and the kinetic-energy identity for a uniform jet.

**Symbols before Eq. (E01):** K_j is jet kinetic energy (J); m_j > 0 is jet mass (kg); U_j ≥ 0 is uniform speed (m/s); E_av ≥ 0 is available mechanical work (J). The index j labels the jet; av labels availability.

```text
     1   2
K  = ─m U  ≤ E
 j   2 j j    av
```

Multiply the inequality by two, then divide by the strictly positive mass.

**Symbols before Eq. (E02):** m_j > 0 is jet mass (kg); U_j ≥ 0 is speed (m/s); E_av ≥ 0 is available work (J). The first inequality has units J; the second has units m^2/s^2.

```text
                    2E
   2            2     av
m U  ≤ 2E  ,   U  ≤ ────
 j j     av     j    m
                      j
```

The square root is monotone on nonnegative arguments. Because speed is nonnegative, the lossless maximum in this energy-constrained class is:

**Symbols before Eq. (E03):** U_j,max^(energy) is the largest energy-admissible uniform speed (m/s); E_av ≥ 0 is available work (J); m_j > 0 is prescribed mass (kg). The superscript energy labels the model.

```text
               ┌────┐
               │2E
 (energy)      │  av
U         = ╲  │────
 j,max       ╲ │ m
              ╲│  j
```

Substituting this speed into one-half times mass times speed squared recovers exactly E_av. The dimension check is J/kg = m^2/s^2, so its square root has units m/s. Zero available work gives zero speed. Without a positive minimum participating mass, finite energy alone supplies no finite point-tip velocity ceiling.

Attainment requires the whole budget to become kinetic energy of that prescribed jet. A nonuniform jet obeys the corresponding mass-weighted RMS bound; a fastest-tip bound additionally requires a velocity profile or a specified mass moving at that speed. Available mechanical work generally falls below absorbed laser energy. Its thermodynamic basis is retained in the [completed availability derivation](resources/evidence/04_thermo.tex).

**2. Derive first-contact pressure.** Adopt planar linear acoustics and continuity of interface pressure and velocity. The incoming jet slows from its initial speed to the interface speed; the receiver starts at rest.

**Symbols before Eq. (E04):** Z_j > 0 and Z_t ≥ 0 are jet and receiver impedances (Pa·s/m); ρ > 0 is liquid density (kg/m^3); c > 0 is sound speed (m/s); Δp_c is contact pressure above ambient (Pa); U_j ≥ 0 and v are jet and interface velocities (m/s).

```text
Z  = ρc,   Δp  = Z (U  - v) = Z v
 j           c    j  j         t
```

Expand the jet-side product, add its interface-velocity term to both sides, and divide by the positive sum of impedances.

**Symbols before Eq. (E05):** Z_j > 0 and Z_t ≥ 0 are impedances (Pa·s/m); U_j ≥ 0 and v are jet and interface velocities (m/s). Their positive impedance sum permits the division.

```text
 Z U  - Z v = Z v
  j j    j     t
 Z U  = (Z  + Z )v
  j j     j    t
        Z
         j
 v = ───────U
     Z  + Z  j
      j    t
```

Substitute the interface velocity into the receiver-side pressure relation, then collect the impedance factors.

**Symbols before Eq. (E06):** Δp_c is contact pressure above ambient (Pa); Z_j > 0 and Z_t ≥ 0 are impedances (Pa·s/m); U_j ≥ 0 is jet speed (m/s). The denominator is strictly positive.

```text
        ⎛   Z     ⎞     Z Z
        ⎜    j    ⎟      j t
Δp  = Z ⎜───────U ⎟ = ───────U
  c    t⎜Z  + Z  j⎟   Z  + Z  j
        ⎝ j    t  ⎠    j    t
```

Pressure is a nondecreasing function of speed in this model. Insert Eq. (E03) to obtain its conditional maximum.

**Symbols before Eq. (E07):** Δp_c,max^(linear) is maximum contact excess pressure in the linear model (Pa); Z_j > 0 and Z_t ≥ 0 are impedances (Pa·s/m); E_av ≥ 0 is available work (J); m_j > 0 is prescribed jet mass (kg). The superscript linear is a model label.

```text
                       ┌────┐
               Z Z     │2E
  (linear)      j t    │  av
Δp         = ───────╲  │────
  c,max      Z  + Z  ╲ │ m
              j    t  ╲│  j
```

For a rigid receiver, divide the effective-impedance numerator and denominator by receiver impedance and let that impedance increase without bound. The effective impedance tends to jet impedance, equal to density times sound speed.

**Symbols before Eq. (E08):** Δp_c,max^(rigid) is rigid-receiver contact excess-pressure ceiling (Pa); ρ > 0 is jet density (kg/m^3); c > 0 is sound speed (m/s); E_av ≥ 0 is available work (J); m_j > 0 is mass (kg). The superscript rigid labels the receiver limit.

```text
                 ┌────┐
                 │2E
  (rigid)        │  av
Δp        = ρc╲  │────
  c,max        ╲ │ m
                ╲│  j
```

For equal positive impedances, their product divided by their sum equals one-half the jet impedance.

**Symbols before Eq. (E09):** Δp_c,max^(equal) is equal-impedance contact excess-pressure ceiling (Pa); ρ > 0 is density (kg/m^3); c > 0 is sound speed (m/s); E_av ≥ 0 is available work (J); m_j > 0 is mass (kg). The superscript equal labels the impedance condition.

```text
                  ┌────┐
                  │2E
  (equal)   1     │  av
Δp        = ─ρc╲  │────
  c,max     2   ╲ │ m
                 ╲│  j
```

Impedance times velocity has units (Pa·s/m)(m/s) = Pa. Both pressure and interface velocity satisfy the original two contact relations by substitution. Zero receiver impedance gives zero contact compression; the rigid limit gives zero interface velocity. Strong shocks require a compressible equation of state and shock conservation equations. These contact pressures concern the short initial impact, while propagated receiver or sensor pressure is a separate observable. The [retained receiver derivation](resources/evidence/07_receiver.tex) states those distinctions.

**3. Evaluate a numerical conditional example.** Prescribe available work 5 nJ, a water-jet radius of 3 µm and length of 50 µm, density 1000 kg/m^3 and sound speed 1500 m/s. These are illustrative model inputs, not device measurements. The circular cross-section gives cylindrical volume, and multiplying by density gives mass.

**Symbols before Eq. (E10):** m_j is jet mass (kg); ρ = 1000 kg/m^3 is density; π is the dimensionless circle constant; a = 3 µm is radius; L = 50 µm is length. One µm is 10^-6 m; one ng is 10^-12 kg.

```text
        2                    -12
m  = ρπa L = 1.413716694 × 10    kg
 j
```

Insert that mass and the specified available work into Eq. (E03).

**Symbols before Eq. (E11):** U_j,max^(energy) is the energy-admissible speed (m/s). The numerator uses available work 5 × 10^-9 J; the denominator uses jet mass 1.413716694 × 10^-12 kg. J and kg mean joule and kilogram; m/s means metres per second.

```text
               ┌──────────────────────┐
               │            -9
 (energy)      │    2(5 × 10   J)
U         = ╲  │──────────────────────  ≈ 84.1044 m/s
 j,max       ╲ │                -12
              ╲│1.413716694 × 10    kg
```

The rigid-contact calculation multiplies 1000 × 1500 × 84.1044174, giving 126156626 Pa. Equal impedances halve that pressure.

| Quantity | Conditional ideal-model maximum |
|---|---:|
| Uniform jet velocity | **84.1 m/s** |
| First-contact pressure against a rigid receiver | **126 MPa above ambient** |
| First-contact pressure against an equal-impedance medium | **63.1 MPa above ambient** |

Check the jet's compression scale by dividing its velocity by sound speed.

**Symbols before Eq. (E12):** M is the dimensionless Mach number; U_j is jet speed (m/s), here 84.1044 m/s; c is sound speed (m/s), here 1500 m/s. The displayed numerical quotient uses both velocities in those same units.

```text
    U
     j   84.1044
M = ── = ─────── ≈ 0.05607
    c      1500
```

For a rigid receiver, contact pressure divided by density times sound speed squared equals this Mach number. Its small value supports the weak-compression approximation for the jet; the receiver must also satisfy the adopted linear response. Whether a particular cavity produces this prescribed plug remains a separate focusing problem.

**4. Solve the conditional spherical-collapse model.** Assume a spherical bubble in an infinite inviscid, incompressible liquid, constant positive collapse-pressure difference, negligible surface tension and no gas cushioning. Radius is positive outward, so its time derivative is negative during collapse. Initially the bubble is at its maximum radius and at rest. The adopted Rayleigh equation is sourced; the integration below is shown explicitly. [Obreschkow et al., *Physical Review E* 85, 066303 (2012)](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.85.066303)

**Symbols before Eq. (E13):** R > 0 is bubble radius (m); Rdot and Rddot are its first and second time derivatives (m/s and m/s^2), shown by dot accents; Δp > 0 is constant collapse drive (Pa); ρ > 0 is liquid density (kg/m^3). Every term has units m^2/s^2.

```text
     3 2    Δp
RR̈ + ─Ṙ  = -──
     2      ρ
```

Define squared wall speed as a function of radius. On the monotone collapse interval the radius derivative in time is nonzero, permitting the chain-rule quotient. The result extends continuously to the initial-rest endpoint.

**Symbols before Eq. (E14):** q(R) is squared wall speed (m^2/s^2); R is radius (m); t is time (s); Rdot < 0 and Rddot are radial velocity and acceleration (m/s and m/s^2). d/dR and d/dt differentiate in radius and time; dq/dt means the derivative of q evaluated along R(t).

```text
        2
q(R) = Ṙ
 dq   dq/dt   2ṘR̈
 ── = ───── = ─── = 2R̈
 dR   dR/dt    Ṙ
```

Substitute one-half the radius derivative of squared speed for radial acceleration, then multiply the governing equation by two.

**Symbols before Eq. (E15):** R > 0 is radius (m); q is squared wall speed (m^2/s^2); dq/dR is its radius derivative (m/s^2); Δp > 0 is collapse drive (Pa); ρ > 0 is density (kg/m^3).

```text
Rdq   3     Δp
─── + ─q = -──
2dR   2     ρ
  dq         2Δp
 R── + 3q = -───
  dR          ρ
```

Apply the product rule, factor out radius squared, and insert the last row of Eq. (E15).

**Symbols before Eq. (E16):** R > 0 is radius (m); q is squared wall speed (m^2/s^2); dq/dR is its radius derivative (m/s^2); Δp > 0 is collapse drive (Pa); ρ > 0 is density (kg/m^3). d/dR is radius differentiation; each row has units m^4/s^2.

```text
   3
d(R q)     2     3dq
────── = 3R q + R ──
  dR              dR
    3
 d(R q)    2⎛ dq     ⎞
 ────── = R ⎜R── + 3q⎟
   dR       ⎝ dR     ⎠
    3
 d(R q)    2Δp 2
 ────── = -───R
   dR       ρ
```

Integrate from the initial maximum radius to the current radius. Because the upper radius is smaller, the right integral is negative; its leading minus sign makes the accumulated squared-speed term positive.

**Symbols before Eq. (E17):** R and R_max > 0 are current and initial radii (m), with R ≤ R_max; x is the dummy radius (m); q(x) is squared wall speed (m^2/s^2); Δp > 0 is collapse drive (Pa); ρ > 0 is density (kg/m^3). The integral bounds label radii; d/dx differentiates in dummy radius. Each integral expression has units m^5/s^2.

```text
 R      3               R
⌠    d(x q(x))      2Δp⌠     2
⎮    ─────────dx = -───⎮    x dx
⌡        dx          ρ ⌡
 R                      R
  max                    max
```

The fundamental theorem evaluates the left integral at both endpoints. The right antiderivative is radius cubed divided by three, whose derivative is radius squared.

**Symbols before Eq. (E18):** R and R_max are current and initial radii (m); q(R) and q(R_max) are squared wall speeds (m^2/s^2); Δp > 0 is collapse drive (Pa); ρ > 0 is density (kg/m^3). The subscript max labels the initial maximum radius.

```text
 3        3             2Δp⎛ 3    3  ⎞
R q(R) - R   q(R   ) = -───⎜R  - R   ⎟
          max   max      3ρ⎝      max⎠
```

Initial rest sets squared speed at the maximum radius to zero. Reverse the subtraction using the minus sign, then divide by positive radius cubed and distribute that division.

**Symbols before Eq. (E19):** R > 0 and R_max ≥ R are current and initial radii (m); q(R) is squared wall speed (m^2/s^2), with q(R_max) = 0; Δp > 0 is collapse drive (Pa); ρ > 0 is density (kg/m^3). The bracket in the second row is dimensionless.

```text
 3       2Δp⎛ 3      3⎞
R q(R) = ───⎜R    - R ⎟
          3ρ⎝ max     ⎠
           ⎡      3    ⎤
           ⎢⎛R   ⎞     ⎥
        2Δp⎢⎜ max⎟     ⎥
 q(R) = ───⎢⎜────⎟  - 1⎥
         3ρ⎣⎝ R  ⎠     ⎦
```

Squared speed increases as radius decreases. On the prescribed interval ending at positive cutoff radius, the largest inward speed magnitude is the nonnegative square root evaluated at that cutoff.

**Symbols before Eq. (E20):** U_wall,max is the largest inward wall-speed magnitude (m/s); Δp > 0 is collapse drive (Pa); ρ > 0 is density (kg/m^3); R_max > 0 is the initial radius (m); 0 < R_min ≤ R_max is the prescribed cutoff radius (m).

```text
                ┌────────────────┐
                │   ⎡      3    ⎤
                │   ⎢⎛R   ⎞     ⎥
            ╲   │2Δp⎢⎜ max⎟     ⎥
U         =  ╲  │───⎢⎜────⎟  - 1⎥
 wall,max     ╲ │ 3ρ⎢⎜R   ⎟     ⎥
               ╲│   ⎣⎝ min⎠     ⎦
```

Verify the governing equation rather than relying only on the integration. Differentiating Eq. (E19), the derivative of inverse radius cubed brings down minus three; that cancels its coefficient's factor of three.

**Symbols before Eq. (E21):** q'(R) is the radius derivative of squared speed (m/s^2); Δp > 0 is collapse drive (Pa); R_max > 0 is initial radius (m); R > 0 is current radius (m); ρ > 0 is density (kg/m^3). The prime denotes d/dR.

```text
              3
         2Δp R
              max
q′(R) = -────────
             4
           ρR
```

Substitute this derivative and Eq. (E19) into the transformed governing equation. The two equal terms containing the cubed radius ratio cancel, leaving the required constant drive.

**Symbols before Eq. (E22):** R and R_max are positive radii (m); q(R) is squared wall speed (m^2/s^2); q'(R) is its radius derivative (m/s^2); Δp > 0 is collapse drive (Pa); ρ > 0 is density (kg/m^3). Each row has units m^2/s^2.

```text
                          3     ⎡      3    ⎤
                    ⎛R   ⎞      ⎢⎛R   ⎞     ⎥
R        3        Δp⎜ max⎟    Δp⎢⎜ max⎟     ⎥
─q′(R) + ─q(R) = -──⎜────⎟  + ──⎢⎜────⎟  - 1⎥
2        2        ρ ⎝ R  ⎠    ρ ⎣⎝ R  ⎠     ⎦
 R        3        Δp
 ─q′(R) + ─q(R) = -──
 2        2        ρ
```

The radius ratio is dimensionless and Δp/ρ has units m^2/s^2. At the initial radius, Eq. (E19) gives zero speed, recovering initial rest. A cutoff equal to the initial radius gives zero maximum speed. As the cutoff tends to zero, the ideal expression diverges. This is a spherical **wall-speed** result; directional jet speed requires asymmetric collapse and focusing. A physical cutoff, gas cushioning or compressible continuation must regularize collapse before interpreting the singular endpoint physically.

**5. Apply the retained PFC conditional benchmark.** PFP means perfluoropentane and PFH means perfluorohexane. The benchmark uses one fully and homogeneously activated **6 µm diameter** droplet, PFP at 386.5 K or PFH at 415.2 K, in water at 293.15 K and ambient pressure 101.325 kPa. The rigid-wall stand-off ratio, defined using bubble-centre distance divided by its reference maximum spherical radius, ranges from 1.25 to 4.

| Quantity | PFP | PFH | Interpretation |
|---|---:|---:|---|
| Available-work ceiling | 2.72 nJ | 4.62 nJ | Conditional thermodynamic ceiling |
| Largest sampled slow-condensation jet speed | 65 m/s | 187 m/s | Reduced-model prediction |
| Largest sampled fast-condensation speed inside the adopted screen | 360 m/s | 378 m/s | Reduced-model prediction |
| Largest sampled internal impact-pressure scale | 292 MPa | 307 MPa | Mixed-contact estimate |

These values retain the completed report's conditions and tiers. Slow and fast condensation refer to the specified control closures; they are not certified bounds on every possible phase-transfer history. The pressure estimates concern internal jet impact on the opposite bubble interface. The approximately **445 m/s** screen is an incompressible-model cutoff. Establishing faster PFC predictions requires compressible continuation. [Accepted envelope source](resources/evidence/09_envelope.tex), [retained numerical table](resources/evidence/table_envelope.tex).

For a **separately prescribed uniform 10 pg jet**, insert the two availability ceilings into Eq. (E03). This mass is an additional illustrative condition, not a claim about the mass of the fastest computed jets.

**Symbols before Eq. (E23):** U_PFP,max is the energy-admissible uniform-jet ceiling for PFP (m/s); available work is 2.72 nJ and prescribed jet mass is 10 pg. One nJ is 10^-9 J; one pg is 10^-15 kg. PFP and max are species and ceiling labels.

```text
             ┌──────────┐
             │2(2.72 nJ)
U        = ╲ │──────────  ≈ 738 m/s
 PFP,max    ╲│  10 pg
```

Apply the same mass condition to the PFH availability ceiling.

**Symbols before Eq. (E24):** U_PFH,max is the energy-admissible uniform-jet ceiling for PFH (m/s); available work is 4.62 nJ and prescribed jet mass is 10 pg. One nJ is 10^-9 J; one pg is 10^-15 kg. PFH and max are species and ceiling labels.

```text
             ┌──────────┐
             │2(4.62 nJ)
U        = ╲ │──────────  ≈ 961 m/s
 PFH,max    ╲│  10 pg
```

These are energetic allowances. Attainment depends on collapse transferring the specified work into that mass. With sound speed 1500 m/s, their Mach numbers are approximately 0.492 and 0.641; corresponding impact pressures require a compressible shock model.

Verification: all 24 formula grids were inspected against their authored sources using termtex 0.9.8 with normal-size lower and upper annotations. Arithmetic, dimensions, branch conditions, limiting cases and the Rayleigh-equation substitution were checked. A separate agent independently confirmed the mathematics and numerical examples. This does not establish physical attainment of the energetic ceilings or validate the unresolved compressible PFC focusing problem.
