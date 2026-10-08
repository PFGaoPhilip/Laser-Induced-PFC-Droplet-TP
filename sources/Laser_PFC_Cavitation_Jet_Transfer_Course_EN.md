# Laser-Pulse-Induced PFC-Droplet Cavitation-Jet Transfer
## A Project-Centered Theory Course

**Scope.** This course develops the theory needed to explain, calculate, and evaluate transfer driven by laser-activated perfluorocarbon (PFC) droplets. It assumes introductory fluid mechanics, thermodynamics, and solid mechanics, but no previous training in cavitation. Software procedures and previous simulation results are outside its scope.

The physical argument follows one continuous chain:

**Absorbed laser energy → local heating and nucleation → finite-inventory phase change → bubble-driven flow → directional liquid jet → transmitted mechanical loading → interfacial fracture → intact release and placement.**

Each arrow requires its own physical condition. A vapor bubble does not necessarily produce a jet; a jet does not necessarily open the intended interface; and release does not necessarily produce successful transfer.

The main configuration is an array of PFC-containing liquid sites that actuates a transferable film or micro-object. A site may be a separate aqueous droplet containing PFC inclusions, or a patterned region within a connected liquid layer. These configurations share thermodynamics but differ in hydrodynamic coupling. An intact intermediate PVC sheet and a hydrogel platform are treated as changes to the load path, not interchangeable accessories.

**How to use the calculations.** Equations are derived as progressively more informative approximations. Numerical examples are explicitly declared teaching cases, not measurements or predictions for an unidentified experimental formulation. SI units are used unless stated otherwise. Pressures in phase-equilibrium and equation-of-state calculations are absolute; pressure differences and mechanical loads have their reference pressure stated. Every newly introduced symbol is defined before its first equation.

## Contents

1. [Introduction to Cavitation Dynamics and Fundamental Properties of Cavitation Jets](#chapter-1)
2. [Comparison of Cavitation Performance of PFC Droplets and Ordinary Liquid Droplets](#chapter-2)
3. [Cavitation-Jet Dynamics of Uniform Droplet Arrays and Preliminary Calculations](#chapter-3)
4. [Fundamentals of Transfer Fracture Mechanics and Laser-Pulse-Induced PFC-Droplet Cavitation-Jet Transfer](#chapter-4)
5. [Appendix A. Comparison of Hydrogel and Conventional Liquid Platforms](#appendix-a)

[Three Research-Defense Questions and Reference Answers](#defense-questions) · [References and Source Basis](#references)

---

<a id="chapter-1"></a>
# 1. Introduction to Cavitation Dynamics and Fundamental Properties of Cavitation Jets

## 1.1 The objects and mechanisms in this project

A **PFC droplet** is initially a liquid inclusion. A **bubble** is a cavity containing vapor, noncondensable gas, or both. The PFC-droplet radius and bubble radius are different quantities: the former measures the available liquid inventory; the latter measures a dynamically evolving cavity that may also contain water vapor and gas.

Cavitation conventionally emphasizes cavity formation associated with a reduction in liquid pressure. Laser heating can instead initiate **thermal vaporization** at a locally elevated temperature. The resulting cavity can subsequently undergo inertial growth, collapse, and jetting. In this course, “laser-induced cavitation” describes this entire transient, while the activation mechanism is identified explicitly rather than assumed to be pressure-driven.

Four visually similar events must be distinguished:

| Event | What actually moves | Relevance to transfer |
|---|---|---|
| Expansion-driven ejection | Bubble expansion displaces carrier liquid toward a meniscus or outlet | Can launch an external liquid jet toward a payload |
| Collapse-driven re-entrant jet | An asymmetric liquid interface penetrates the collapsing cavity | Can strike a nearby surface; it is not automatically an outgoing free jet |
| Sealed-cavity inflation | A growing cavity deforms a membrane or compliant stamp | Can drive fracture without any liquid jet crossing a gap |
| Liquid-bridge stretching | A moving solid pulls a liquid filament behind it | May be a consequence of release, rather than its driving mechanism |

The first experimental classification is therefore geometric: identify the cavity, the liquid that becomes the jet, the available exit, and the surface receiving the load. Bubble brightness or a final detached object alone does not establish the intermediate mechanism. Studies of asymmetric bubble collapse and pressure-driven meniscus focusing provide relevant jet physics, but their boundary conditions must match the configuration being analyzed. [R3](#r3), [R4](#r4)

## 1.2 Deriving the spherical bubble equation

Begin with one spherical bubble in an unbounded, incompressible, Newtonian carrier liquid. Let time be $t$, bubble radius be $R(t)$, radial position be $r$, and radial liquid velocity be $u(r,t)$. A dot denotes differentiation with respect to time. Assume spherical symmetry, no motion at infinity, and negligible phase-change-induced velocity slip at the interface.

Incompressibility requires the volume flux through every concentric sphere to be equal. The interface moves at $\dot R$, so

$$
4\pi r^2u(r,t)=4\pi R^2\dot R,
\qquad
u(r,t)=\frac{R^2\dot R}{r^2}.
$$

The inverse-square spatial decay means that the bubble accelerates a surrounding volume of carrier liquid, not just its own vapor.

Let $\phi(r,t)$ be a velocity potential, defined by $u=\partial\phi/\partial r$. Choosing its value to vanish at infinity gives

$$
\phi(r,t)=-\frac{R^2\dot R}{r}.
$$

Let $\rho$ be carrier-liquid density, $p_\infty(t)$ the far-field pressure, and $p_l(R,t)$ the liquid pressure immediately outside the interface. Unsteady Bernoulli gives

$$
\frac{p_l(R,t)-p_\infty(t)}{\rho}
=-\left.\frac{\partial\phi}{\partial t}\right|_{r=R}
-\frac{\dot R^2}{2}
=R\ddot R+\frac{3}{2}\dot R^2.
$$

The time derivative of $\phi$ is taken at fixed spatial position before evaluating it at $r=R$. This distinction produces the coefficient $3/2$ correctly.

Let $p_b(t)$ be spatially uniform bubble pressure, $\sigma$ the effective bubble–carrier surface tension, and $\mu$ the carrier dynamic viscosity. The spherical normal-stress balance is

$$
p_l(R,t)=p_b(t)-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}.
$$

Substitution yields the **Rayleigh–Plesset equation**:

$$
\boxed{
\rho\left(R\ddot R+\frac{3}{2}\dot R^2\right)
=p_b-p_\infty-\frac{2\sigma}{R}-\frac{4\mu\dot R}{R}.
}
\tag{1.1}
$$

The right side is the pressure available to accelerate the liquid after capillary and viscous stresses are included. The viscous term reverses sign with velocity and always opposes the motion. The density is primarily that of the **surrounding carrier**, not automatically the much denser PFC liquid.

Equation (1.1) requires an initial radius and velocity and a law for $p_b$. It does not supply nucleation, laser absorption, or phase change. In a PFC-containing aqueous system, define the partial pressures of PFC vapor, water vapor, and noncondensable gas as $p_{v,\mathrm{PFC}}$, $p_{v,w}$, and $p_g$, respectively. Then

$$
p_b=p_{v,\mathrm{PFC}}+p_{v,w}+p_g.
\tag{1.2}
$$

Chapter 2 supplies the corresponding mass and energy balances. A fixed-mass polytropic gas law can be useful for a gas-bubble control, but it does not automatically describe an evaporating and condensing PFC reservoir. The classical spherical theory and modern laser-cavitation analyses explain why this distinction matters. [R1](#r1), [R5](#r5)

## 1.3 Mechanical energy: what bubble growth stores

Let $K_l$ be the kinetic energy of the surrounding liquid. Substituting the radial velocity into the volume integral gives

$$
K_l=\int_R^\infty\frac{1}{2}\rho u^2\,4\pi r^2\,dr
=2\pi\rho R^3\dot R^2.
\tag{1.3}
$$

Thus even a small cavity can involve substantial liquid inertia. Its mechanical energy cannot be estimated from vapor mass alone.

Let $V_b=4\pi R^3/3$ be bubble volume. Multiply Equation (1.1) by $\dot V_b=4\pi R^2\dot R$. For constant surface tension, direct differentiation of Equation (1.3) gives

$$
\frac{dK_l}{dt}
=(p_b-p_\infty)\dot V_b
-\frac{d}{dt}\left(4\pi\sigma R^2\right)
-16\pi\mu R\dot R^2.
\tag{1.4}
$$

Pressure work becomes liquid kinetic energy, surface energy, and irreversible viscous dissipation. During expansion, the bubble can do work on the liquid. During collapse, surrounding pressure can return stored mechanical energy to a smaller region. Neither process implies that all incident laser energy becomes jet kinetic energy.

This balance also explains an important design trade-off: stronger confinement may promote useful directionality while requiring additional pressure work or storing energy in a deformable boundary.

## 1.4 A collapse calculation that can be solved by hand

Consider an idealized cavity initially at rest at maximum radius $R_{\max}$. Let its internal pressure be a constant vapor pressure $p_v$, and define a positive collapse-driving difference $\Delta p_c=p_\infty-p_v$. Neglect surface tension, viscosity, permanent gas, and liquid compressibility.

Equation (1.1) becomes

$$
R\ddot R+\frac{3}{2}\dot R^2=-\frac{\Delta p_c}{\rho}.
$$

To integrate it, define $y(R)=\dot R^2$. The chain rule gives $\ddot R=\tfrac12dy/dR$, hence

$$
\frac{dy}{dR}+\frac{3y}{R}
=-\frac{2\Delta p_c}{\rho R}.
$$

Multiplication by $R^3$ makes the left side an exact derivative. Integrating from $R_{\max}$, where $y=0$, to $R$ gives

$$
\dot R^2=
\frac{2\Delta p_c}{3\rho}
\left[\left(\frac{R_{\max}}{R}\right)^3-1\right].
\tag{1.5}
$$

The collapse branch has $\dot R<0$. Integrating $dt=dR/\dot R$ gives the classical Rayleigh collapse time

$$
t_c=0.914681\,R_{\max}\sqrt{\frac{\rho}{\Delta p_c}}.
\tag{1.6}
$$

Define the pressure-work scale $E_B$ associated with the maximum cavity volume as

$$
E_B=\frac{4\pi}{3}\Delta p_cR_{\max}^3.
\tag{1.7}
$$

For a declared water-like control with $R_{\max}=30\,\mu\mathrm m$, $\rho=1000\,\mathrm{kg\,m^{-3}}$, and $\Delta p_c=100\,\mathrm{kPa}$, Equations (1.5)–(1.7) give $t_c=2.744\,\mu\mathrm s$, $E_B=11.31\,\mathrm{nJ}$, and an inward wall speed of $21.60\,\mathrm{m\,s^{-1}}$ at $R=R_{\max}/2$.

These are reference scales, not a predicted PFC event. In particular, a hot PFC-rich bubble may not have $p_b<p_\infty$ until sufficient cooling and condensation occur. The divergence of Equation (1.5) as $R\rightarrow0$ is the breakdown of the assumptions, not an unlimited physical jet speed. [R1](#r1), [R5](#r5)

## 1.5 How a cavity produces a directional jet

A perfectly spherical cavity in an otherwise uniform infinite liquid has no preferred direction. Direction arises from **broken symmetry**: an outlet, curved meniscus, nearby wall, free surface, neighboring cavity, or spatially nonuniform loading.

Let $h$ be the distance from bubble center to a relevant boundary. Define the dimensionless stand-off distance $\gamma=h/R_{\max}$. The boundary type and $\gamma$ together influence the evolving shape. A rigid wall often promotes a collapse jet toward the wall. A free or deformable boundary can produce a different direction or multiple interacting jets. There is no boundary-independent conversion from $R_{\max}$ to jet speed. [R3](#r3), [R12](#r12)

A useful short-event approximation follows directly from momentum conservation. Let $\boldsymbol u$ be liquid velocity, $p_{\mathrm{ref}}$ a reference pressure, and $\Pi(\boldsymbol x)$ the local **pressure impulse**, with units Pa·s, accumulated from event start $t_0$ to end $t_1$:

$$
\Pi(\boldsymbol x)=\int_{t_0}^{t_1}[p(\boldsymbol x,t)-p_{\mathrm{ref}}]\,dt.
$$

If interface displacement, convective acceleration, and viscous impulse are small over this short interval, integrating $\rho\,\partial\boldsymbol u/\partial t=-\nabla p$ gives

$$
\Delta\boldsymbol u=-\frac{\nabla\Pi}{\rho}.
\tag{1.8}
$$

Taking the divergence and enforcing incompressibility gives $\nabla^2\Pi=0$ in the liquid, with boundary conditions supplied by the actual cavity, walls, and meniscus. Thus **the spatial distribution of pressure impulse**, not a scalar pressure maximum alone, generates the velocity field. [R2](#r2)

For a simple liquid column of length $L$, suppose the pressure impulse drops approximately linearly from $\Pi_0$ at the driven end to zero at the outlet. Let $U$ denote the resulting column velocity increment. Equation (1.8) reduces to

$$
U\simeq\frac{\Pi_0}{\rho L}.
\tag{1.9}
$$

An outlet or curved free surface can then focus this moving liquid. Focusing redistributes momentum and energy into a smaller region; it does not generate extra energy. The approximation must end once substantial interface motion changes the geometry.

## 1.6 What is needed beyond a spherical radius

To calculate a jet, resolve the liquid motion and the moving interface in space. For a Newtonian incompressible carrier with gravity negligible during the event, the minimum bulk equations are

$$
\nabla\cdot\boldsymbol u=0,
\qquad
\rho\left(\frac{\partial\boldsymbol u}{\partial t}
+\boldsymbol u\cdot\nabla\boldsymbol u\right)
=-\nabla p+\mu\nabla^2\boldsymbol u.
\tag{1.10}
$$

These equations require a kinematic condition for the moving interface, a normal-stress condition including curvature and surface tension, the bubble-pressure closure, and the actual solid/free-surface boundaries. If phase transfer is appreciable, the interface and liquid velocities differ as derived in Section 2.5.

Let $c$ be carrier sound speed, $L_e$ the distance over which loading must communicate, and $\tau_e$ its characteristic rise time. The two diagnostic ratios are the bubble-wall Mach number $M_w=|\dot R|/c$ and the communication ratio $L_e/(c\tau_e)$. An incompressible approximation becomes questionable when either is no longer small. Compressibility is retained here only to describe rapid pressure transmission, impact, and the termination of singular collapse approximations—not to introduce a separate course on harmonic acoustics.

**Chapter connection.** The spherical equation establishes the pressure–inertia balance. The spatial equations establish how boundaries turn radial motion into a jet. Neither is predictive until the absorbed energy, phase inventory, and internal pressure are supplied; those are the subject of Chapter 2.

---

<a id="chapter-2"></a>
# 2. Comparison of Cavitation Performance of PFC Droplets and Ordinary Liquid Droplets

## 2.1 Define a fair comparison before choosing a material

Here an “ordinary liquid droplet” means a **PFC-free aqueous carrier droplet** with otherwise comparable outer geometry, absorber, optical exposure, and surroundings. Comparing a PFC nanoemulsion with a differently focused laser in a different water geometry cannot isolate the benefit of PFC.

PFC is a family of compounds, not a single material. Perfluoro-n-pentane (PFP) and perfluoro-n-hexane (PFH) are useful named references, but neither is automatically the experimental formulation in this project. Optical vaporization has been demonstrated for particular absorber-loaded PFC systems; those results establish possible activation routes, not a universal threshold or jet velocity. [R6](#r6), [R7](#r7)

| Property or question | PFC-containing aqueous site | Matched PFC-free aqueous site |
|---|---|---|
| Volatile inventory | Finite PFC cores, potentially water vapor, and dissolved gas | Water and dissolved gas |
| Initial phase transition | Depends on PFC identity, core size, shell, temperature, and pressure | Depends on water heating, nuclei, and pressure |
| Optical energy deposition | Often determined mainly by an added absorber and its location | Also requires a specified absorption mechanism |
| Liquid accelerated into the jet | Usually predominantly carrier liquid, unless geometry shows otherwise | Carrier liquid |
| Collapse and reset | Governed by cooling, condensation, residual gas, and remaining PFC | Governed by cooling, condensation, and residual gas |
| Appropriate performance metrics | Activation reliability, emitted mass and velocity, useful impulse, intact-transfer yield, reset | The same metrics under the same constraints |

A lower activation threshold is valuable only when it improves this complete process. Easier vaporization can also produce a persistent gas-filled cavity, less repeatable collapse, or unwanted expansion. “More volatile” and “better transfer actuator” are therefore different claims.

## 2.2 From laser specifications to heat actually reaching PFC

Let $F(r)$ be incident fluence, meaning pulse energy per illuminated area; let $F_0$ be its on-axis value; and let $w$ be the radius at which a Gaussian fluence falls to $e^{-2}$ of its maximum. The total incident pulse energy is $E_L$. For a circular Gaussian beam,

$$
F(r)=F_0\exp\left(-\frac{2r^2}{w^2}\right),
\qquad
E_L=\int_0^\infty F(r)\,2\pi r\,dr
=\frac{\pi w^2F_0}{2}.
\tag{2.1}
$$

Let $f(t)$ be a normalized temporal pulse shape with $\int f(t)dt=1$. Local irradiance is $I(r,t)=F(r)f(t)$, in W·m$^{-2}$. Pulse energy, fluence, and peak irradiance are not interchangeable: changing spot size or pulse duration changes local conditions even at fixed $E_L$.

For absorption-only transport after light enters an absorber, let $z$ be depth, $\mu_a$ the absorption coefficient, and $Q_{\mathrm{abs}}$ the volumetric heat source. Then

$$
\frac{\partial I}{\partial z}=-\mu_a I,
\qquad
Q_{\mathrm{abs}}=\mu_a I.
\tag{2.2}
$$

A uniform slab of thickness $h_a$ absorbs the fraction $1-e^{-\mu_a h_a}$ of the light entering it under these assumptions. Reflection, beam interception, and scattering must be treated separately when relevant. For a measured or declared effective absorptance $A_\lambda$ and intercepted fraction $f_{\mathrm{geo}}$, the total absorbed energy is

$$
E_{\mathrm{abs}}=f_{\mathrm{geo}}A_\lambda E_L
=\int\!\int_{\Omega_a}Q_{\mathrm{abs}}\,dV\,dt,
\tag{2.3}
$$

where $\Omega_a$ is the absorbing volume. Use either equivalent boundary heating or volume heating for the same absorbed energy, not both. If the absorber is a solid layer, energy deposited there becomes PFC heat only after interfacial heat transfer. If it consists of dispersed particles, their distribution and aggregation determine local hotspots.

Let $T$ be temperature, $c_p$ specific heat capacity, $k$ thermal conductivity, and $\alpha=k/(\rho c_p)$ thermal diffusivity in the phase being considered. Before phase change, the heat equation is

$$
\rho c_p\left(\frac{\partial T}{\partial t}
+\boldsymbol u\cdot\nabla T\right)
=\nabla\cdot(k\nabla T)+Q_{\mathrm{abs}}.
\tag{2.4}
$$

Across adjoining materials, apply heat-flux continuity and either temperature continuity or a specified thermal contact resistance. The relevant diffusion time over heating distance $L_h$ and thermal penetration during heating duration $\tau_h$ are

$$
t_{\mathrm{th}}\sim\frac{L_h^2}{\alpha},
\qquad
\delta_T\sim\sqrt{\alpha\tau_h}.
\tag{2.5}
$$

For an illustrative PFP-like liquid with declared $\rho_d=1630\,\mathrm{kg\,m^{-3}}$, $c_{p,d}=654\,\mathrm{J\,kg^{-1}K^{-1}}$, and $k_d=0.050\,\mathrm{W\,m^{-1}K^{-1}}$, the diffusivity is $4.69\times10^{-8}\,\mathrm{m^2\,s^{-1}}$. Diffusion across $5\,\mu\mathrm m$ takes approximately $533\,\mu\mathrm s$, while penetration during a $10\,\mathrm{ns}$ pulse is only about $22\,\mathrm{nm}$. Uniform heating of a micron-scale core is therefore not justified merely because the incident laser pulse is short. Distributed absorption or post-pulse conduction must supply that heating. The heat-capacity value is a rounded near-293 K reference; the other coefficients are declared constant-coefficient teaching inputs. [R8](#r8)

Optical breakdown and plasma-driven cavities are a separate source mechanism. They should be introduced only when the laser conditions and observations support them, rather than inserted into a thermal PFC model by default.

## 2.3 Volatility is not the same as an activation threshold

Let $a$ be the initial PFC-core radius, $p_c$ the surrounding carrier pressure, $\sigma_{pc}$ the PFC–carrier interfacial tension, and $\Pi_{\mathrm{shell}}$ the additional pressure sustained by a shell. Before a vapor nucleus appears, the approximate PFC-liquid pressure is

$$
p_d=p_c+\frac{2\sigma_{pc}}{a}+\Pi_{\mathrm{shell}}.
\tag{2.6}
$$

For a declared $\sigma_{pc}=0.020\,\mathrm{N\,m^{-1}}$, the capillary pressure is $8\,\mathrm{kPa}$ at $a=5\,\mu\mathrm m$, but $400\,\mathrm{kPa}$ at $a=100\,\mathrm{nm}$. These numbers illustrate size sensitivity; the interfacial tension of an actual surfactant-coated formulation must be measured or justified.

To understand the nucleation barrier, let $r_n$ be the radius of a vapor nucleus inside the PFC liquid, $\sigma_{vp}$ its vapor–PFC surface tension, $T_i$ the local interface temperature, and $p_{\mathrm{sat,PFC}}(T_i)$ the equilibrium vapor pressure. Define the positive thermodynamic driving pressure as $\Delta p_n=p_{\mathrm{sat,PFC}}(T_i)-p_d$. For a homogeneous spherical nucleus under a capillarity approximation, its formation free energy $W$ is

$$
W(r_n)=4\pi\sigma_{vp}r_n^2
-\frac{4\pi}{3}\Delta p_n r_n^3.
\tag{2.7}
$$

The surface term penalizes creation of a new interface; the volume term favors the lower-free-energy vapor state. Differentiating and setting $dW/dr_n=0$ gives the critical radius $r_*$ and barrier $W_*$:

$$
r_*=\frac{2\sigma_{vp}}{\Delta p_n},
\qquad
W_*=\frac{16\pi\sigma_{vp}^3}{3\Delta p_n^2}.
\tag{2.8}
$$

A positive driving pressure does not eliminate the barrier. Heterogeneous sites, absorber surfaces, shell defects, and finite-core geometry change the activation process. The two surface tensions in Equations (2.6) and (2.8) describe different interfaces and must not be silently equated.

For predictive onset, supply either a justified nucleation-rate law or a formulation-specific activation probability. Let $J(T,p)$ be the homogeneous nucleation rate per volume per time and $P_{\mathrm{act}}$ the probability of at least one nucleation event in a specified droplet. Under a Poisson assumption,

$$
P_{\mathrm{act}}=1-\exp\left[-\int\!\int_{V_d(t)}J(T,p)\,dV\,dt\right],
\tag{2.9}
$$

where $V_d(t)$ is the remaining liquid-core volume. A fitted experimental activation law can replace this expression when homogeneous nucleation is not the correct mechanism. A post-nucleation calculation may instead start from a declared seed; it must not then claim to have predicted activation.

## 2.4 Named PFC reference properties and their proper use

NIST reports the following compound-specific reference data. Multiple tabulated values reflect different source datasets, not a confidence interval for a particular formulation. [R8](#r8), [R9](#r9), [R15](#r15)

| Reference material | Formula; molar mass | Representative normal-boiling data | Other useful reference |
|---|---|---|---|
| Perfluoro-n-pentane, PFP | C$_5$F$_{12}$; $0.2880343\,\mathrm{kg\,mol^{-1}}$ | Approximately 302.6–303.2 K | Liquid $c_p\approx653.7\,\mathrm{J\,kg^{-1}K^{-1}}$ at 293 K from the listed interpolated dataset |
| Perfluoro-n-hexane, PFH | C$_6$F$_{14}$; $0.3380418\,\mathrm{kg\,mol^{-1}}$ | Listed measurements approximately 330.3–333 K | Vaporization enthalpy $31.5\,\mathrm{kJ\,mol^{-1}}$ at 316 K, equivalent to $93.18\,\mathrm{kJ\,kg^{-1}}$ |
| Water, PFC-free reference | H$_2$O; $0.0180153\,\mathrm{kg\,mol^{-1}}$ | Approximately 373.17 K in the listed compilation | Its saturation pressure at the same near-room temperature is much lower than PFP's |

For a specific PFP reference correlation, let $T$ be in kelvin and express saturation pressure relative to $1\,\mathrm{bar}=10^5\,\mathrm{Pa}$. The Barber–Cady correlation tabulated by NIST is

$$
\log_{10}\left(\frac{p_{\mathrm{sat,PFP}}}{1\,\mathrm{bar}}\right)
=4.2063-\frac{1103.454}{T-39.77},
\quad 282.82\le T\le337.94\,\mathrm K.
\tag{2.10}
$$

It gives about $70.60\,\mathrm{kPa}$ at 293 K, $103.35\,\mathrm{kPa}$ at 303 K, and $204.33\,\mathrm{kPa}$ at 323 K. The correlation is an equilibrium bulk-fluid relation within its stated range. It is neither a shell rupture law nor a nanodroplet optical threshold.

For comparison, the NIST water correlations give approximately $2.32\,\mathrm{kPa}$ at 293 K and $12.25\,\mathrm{kPa}$ at 323 K. Thus, at 323 K the reference PFP saturation pressure is above a 100 kPa environment, whereas water's is far below it. This demonstrates the thermodynamic attraction of a low-boiling PFC under matched temperature and ambient pressure. Capillary pressure, shells, nucleation kinetics, and heat-transfer limitations must still be included before concluding that a particular inclusion activates. [R8](#r8), [R15](#r15)

The required material specification is therefore more than a boiling point: compound and purity, core-size distribution, shell and surfactant, absorber distribution, carrier properties, temperature-dependent transport, and an equation of state over the accessed pressure–temperature range. PFC properties govern its own inventory and phase change; carrier properties govern most surrounding flow. Formulated interfacial tensions and viscosities should not be replaced by neat-liquid values without justification.

## 2.5 Finite inventory, evaporation, and condensation

Let $a_0$ be initial core radius and $\rho_d$ its initial liquid density. Its initial PFC mass is

$$
m_{\mathrm{PFC},0}=\frac{4\pi}{3}\rho_da_0^3.
\tag{2.11}
$$

Let $m_l$, $m_v$, $m_{\mathrm{diss}}$, and $m_{\mathrm{esc}}$ denote remaining liquid PFC, PFC vapor in the modeled domain, dissolved PFC, and cumulative escaped PFC, respectively. For an initially closed inventory with no subsequent external supply,

$$
m_l+m_v+m_{\mathrm{diss}}+m_{\mathrm{esc}}
=m_{\mathrm{PFC},0}.
\tag{2.12}
$$

For a closed, nondissolving control this reduces to $m_l+m_v=m_{\mathrm{PFC},0}$. A water carrier is not an unlimited source of PFC vapor. Likewise, once a vent opens, the in-domain PFC mass need not remain constant.

For species $s$, let $j_s$ be interfacial mass flux, positive from liquid into vapor, and let $\Gamma_s$ be the interface through which that species changes phase. Its phase-change contribution is

$$
\left.\frac{dm_{v,s}}{dt}\right|_{\mathrm{phase}}
=\int_{\Gamma_s}j_s\,dA.
\tag{2.13}
$$

Using $4\pi R^2j_s$ is valid only when that species contacts the entire spherical bubble surface with uniform flux. A residual PFC core inside an aqueous mixture does not automatically satisfy this condition.

Let $\boldsymbol n$ point from liquid into vapor, $\boldsymbol v_\Gamma$ be interface velocity, and subscripts $l,v$ indicate the adjacent liquid and vapor. Conservation of mass at the interface gives

$$
j_s=\rho_l(\boldsymbol u_l-\boldsymbol v_\Gamma)\cdot\boldsymbol n
=\rho_v(\boldsymbol u_v-\boldsymbol v_\Gamma)\cdot\boldsymbol n
\tag{2.14}
$$

for a single-component interface. For an outward-growing spherical bubble, the liquid-to-vapor normal points inward. The radial liquid velocity just outside the bubble is therefore

$$
u_l(R)=\dot R-\frac{j_s}{\rho_l}.
\tag{2.15}
$$

The negligible phase-change velocity-slip approximation used in Section 1.2 requires $|j_s|/\rho_l\ll|\dot R|$. A mixture additionally needs species diffusion and the corresponding component fluxes.

Let $L_{v,s}$ be latent enthalpy per unit mass and $\boldsymbol q_l$, $\boldsymbol q_v$ the conductive heat-flux vectors on the two sides. Neglecting interfacial energy storage and small kinetic-energy corrections, the Stefan heat balance is

$$
j_sL_{v,s}=(\boldsymbol q_l-\boldsymbol q_v)\cdot\boldsymbol n,
\qquad
\boldsymbol q=-k\nabla T.
\tag{2.16}
$$

Positive heat supply supports evaporation; heat removal can drive negative $j_s$, meaning condensation. During rapid compression, condensation may be too slow to maintain equilibrium saturation pressure, and the retained vapor cushions collapse.

For a uniform-state bubble, let $U_b$ be internal energy, $\dot Q_b$ its net conductive heat input, and $h_{v,s}$ the specific enthalpy carried by species entering the bubble. Ignoring resolved internal kinetic energy, the open-system energy balance is

$$
\frac{dU_b}{dt}
=\dot Q_b-p_b\dot V_b+\sum_s h_{v,s}\dot m_{v,s}.
\tag{2.17}
$$

The mass-flux enthalpy is not included again in $\dot Q_b$. Equations (2.16) and (2.17) must use consistent thermodynamic reference states: adding a second independent “latent-heat source” would double-count energy. Escaping vapor carries both mass and enthalpy out of the chosen control volume.

Let $M_s$ be species molar mass, $R_u=8.314462618\,\mathrm{J\,mol^{-1}K^{-1}}$ the universal gas constant, and $T_b$ uniform bubble temperature. A dilute ideal-vapor approximation gives

$$
p_{v,s}V_b=\frac{m_{v,s}}{M_s}R_uT_b.
\tag{2.18}
$$

The partial pressures then enter Equation (1.2). At higher density or strong compression, replace Equation (2.18) with a valid real-fluid or mixture equation of state. Saturation pressure can be imposed only while sufficient liquid inventory and sufficiently rapid heat/mass exchange support that equilibrium. A noncondensable gas component must remain in the pressure balance even after most vapor condenses.

## 2.6 A complete single-core inventory calculation

Use a declared reference core with $a_0=5\,\mu\mathrm m$, $\rho_d=1630\,\mathrm{kg\,m^{-3}}$, $c_{p,d}=654\,\mathrm{J\,kg^{-1}K^{-1}}$, and constant reference latent enthalpy $L_v=95\,\mathrm{kJ\,kg^{-1}}$. Take initial temperature $T_0=293\,\mathrm K$ and an illustrative final vapor state at $T_*=323\,\mathrm K$. These constant properties define an estimate, not a high-state material law.

Equation (2.11) gives $m_{\mathrm{PFC},0}=8.535\times10^{-13}\,\mathrm{kg}$, or $0.8535\,\mathrm{ng}$. Let $Q_{\mathrm{sens}}$ and $Q_{\mathrm{lat}}$ be approximate sensible and vaporization enthalpy requirements for a chosen near-constant-pressure preparation path. Then

$$
Q_{\mathrm{sens}}\approx m_{\mathrm{PFC},0}c_{p,d}(T_*-T_0)
=16.75\,\mathrm{nJ},
$$

$$
Q_{\mathrm{lat}}\approx m_{\mathrm{PFC},0}L_v
=81.08\,\mathrm{nJ}.
$$

Their sum, approximately $97.82\,\mathrm{nJ}$, screens whether the available heat is of the right order to prepare the specified vapor state. It neglects the detailed pressure path, spatial temperature gradients, shell mechanics, and carrier heating. It is not a nucleation threshold or an amount of energy automatically available for jetting.

As a separate mass-conservation check, suppose all PFC becomes ideal vapor at $T_*$ with PFC partial pressure $p_{v,\mathrm{PFC}}=100\,\mathrm{kPa}$. Let $R_{b,\mathrm{inv}}$ be the radius corresponding to that inventory and state. Combining Equations (2.11) and (2.18) gives

$$
\frac{R_{b,\mathrm{inv}}}{a_0}
=\left(\frac{\rho_dR_uT_*}{M_{\mathrm{PFC}}p_{v,\mathrm{PFC}}}\right)^{1/3}.
\tag{2.19}
$$

Using $M_{\mathrm{PFC}}=0.2880343\,\mathrm{kg\,mol^{-1}}$ gives a volume expansion factor of about 152 and $R_{b,\mathrm{inv}}=26.68\,\mu\mathrm m$. This is an inventory radius at an assumed vapor state, not a dynamical maximum. At 323 K the chosen 100 kPa PFC partial pressure is below the saturation pressure from Equation (2.10); it represents a fully vaporized, unsaturated reference, not coexistence with an unlimited equilibrium liquid reservoir.

**Chapter connection.** The single-site calculation now has a specified optical input, thermal path, activation condition, finite phase inventory, and pressure closure. Chapter 3 combines such sites without assuming that uniform spacing guarantees independent or simultaneous jets.

---

<a id="chapter-3"></a>
# 3. Cavitation-Jet Dynamics of Uniform Droplet Arrays and Preliminary Calculations

## 3.1 “Uniform array” describes several independent properties

Let $N_d$ be the number of PFC-containing sites and $s$ their center-to-center pitch. Uniform core sizes, uniform outer carrier-droplet sizes, uniform spatial spacing, uniform laser fluence, and uniform activation time are separate conditions. Achieving one does not establish the others.

The first distinction is hydraulic connectivity. **Separate liquid cells** can emit approximately independent jets when solid partitions or sufficient separation suppress interaction. **Bubbles sharing a continuous carrier** exchange pressure and accelerate common liquid. A regular pattern in the latter case does not justify multiplying a single-bubble pressure by the number of bubbles.

Let $p_a$ be the identical activation probability of each site. Under independent, one-event-per-site activation, the number $N_b$ of activated sites is binomial. Its mean, variance, coefficient of variation, and probability of complete activation are

$$
\mathbb E[N_b]=N_dp_a,
\qquad
\operatorname{Var}(N_b)=N_dp_a(1-p_a),
$$

$$
\mathrm{CV}(N_b)=\sqrt{\frac{1-p_a}{N_dp_a}},
\qquad
P(N_b=N_d)=p_a^{N_d}.
\tag{3.1}
$$

For 25 sites with $p_a=0.95$, the count varies by only about 4.59% relative to its mean, yet the probability that all sites activate is only 27.7%. A visually repeatable total bubble count can therefore conceal missing actuators. Shared heating and mechanical interactions can also invalidate the independence assumption.

Beam uniformity can be checked before invoking any bubble model. Let $R_A$ be the radius enclosing the array and $\epsilon$ the allowed fractional fluence decrease from center to edge. Equation (2.1) requires

$$
\frac{F(R_A)}{F_0}\ge1-\epsilon
\quad\Longrightarrow\quad
w\ge R_A\sqrt{\frac{2}{-\ln(1-\epsilon)}}.
\tag{3.2}
$$

For 10% allowable variation, $w\ge4.357R_A$. A broad Gaussian can meet this condition but wastes incident energy outside the array; patterned illumination or independently addressed sites changes the optical allocation. This is an optical-uniformity calculation, not an activation guarantee.

## 3.2 Deriving a first interaction correction

Consider separated spherical bubbles in a common incompressible liquid. Let $R_i(t)$ be bubble $i$'s radius, $d_{ij}$ the fixed distance between centers $i$ and $j$, and $p_{b,i}$ its internal pressure. Assume the bubbles remain nearly spherical, $R_i/d_{ij}\ll1$, and pressure communication is fast compared with their radial evolution.

The leading velocity potential produced by bubble $j$ at distance $r_j$ is $\phi_j=-R_j^2\dot R_j/r_j$. Its leading pressure disturbance at center $i$ is obtained from $-\rho\partial\phi_j/\partial t$:

$$
p'_{j\rightarrow i}
\simeq\frac{\rho}{d_{ij}}
\left(R_j^2\ddot R_j+2R_j\dot R_j^2\right).
\tag{3.3}
$$

This approximation retains the source's radial acceleration and neglects higher-order spatial variation and inter-bubble convective terms. The effective surrounding pressure for bubble $i$ becomes $p_\infty+\sum_{j\ne i}p'_{j\rightarrow i}$. Substitution into Equation (1.1) gives

$$
R_i\ddot R_i+\frac32\dot R_i^2
=
\frac{p_{b,i}-p_\infty-2\sigma/R_i-4\mu\dot R_i/R_i}{\rho}
-\sum_{j\ne i}
\frac{R_j^2\ddot R_j+2R_j\dot R_j^2}{d_{ij}}.
\tag{3.4}
$$

Every bubble acceleration is coupled to the others. For PFC bubbles, each $p_{b,i}$ must still be obtained from the finite thermal and phase balances of Chapter 2. Equation (3.4) does not describe coalescence, a re-entrant jet, or a film boundary; it is a first calculation of interaction before those complications become dominant.

## 3.3 Three-, four-, and five-bubble calculations

A symmetric analytical control makes the interaction understandable without a software workflow. Place identical bubbles at the vertices of a regular polygon, with equal initial states and equal internal-pressure histories. Let all radii remain $R(t)$ and define the geometric sum $S=\sum_{j\ne i}1/d_{ij}$, which is the same for every vertex.

For the ideal constant-$\Delta p_c$ collapse used in Section 1.4, Equation (3.4) reduces to

$$
(1+SR)R\ddot R+
\left(\frac32+2SR\right)\dot R^2
=-\frac{\Delta p_c}{\rho}.
\tag{3.5}
$$

The factor $1+SR$ represents the leading increase in effective inertia associated with moving shared liquid. It is not an increase in available energy.

To integrate, set $y(R)=\dot R^2$ again. Multiplication of the resulting first-order equation by the appropriate factor gives

$$
\frac{d}{dR}\left[R^3(1+SR)y\right]
=-\frac{2\Delta p_c}{\rho}R^2.
$$

Applying $y(R_{\max})=0$ yields

$$
\dot R^2=
\frac{2\Delta p_c}{3\rho}
\frac{R_{\max}^3-R^3}{R^3(1+SR)}.
\tag{3.6}
$$

Let $\chi=SR_{\max}$ be a dimensionless interaction measure and $x=R/R_{\max}$ a dimensionless radius. The formal collapse time is

$$
t_c=R_{\max}\sqrt{\frac{\rho}{\Delta p_c}}\,C(\chi),
\qquad
C(\chi)=\sqrt{\frac32}
\int_0^1\sqrt{\frac{x^3(1+\chi x)}{1-x^3}}\,dx.
\tag{3.7}
$$

Use $R_{\max}=30\,\mu\mathrm m$, neighboring-vertex pitch $s=200\,\mu\mathrm m$, $\rho=1000\,\mathrm{kg\,m^{-3}}$, and $\Delta p_c=100\,\mathrm{kPa}$. For the pentagon, define the golden ratio $\varphi_g=(1+\sqrt5)/2$.

| Configuration | Geometric sum $S$ | $\chi$ | Formal collapse time |
|---|---:|---:|---:|
| Isolated bubble | $0$ | 0 | $2.744\,\mu\mathrm s$ |
| Three bubbles: equilateral triangle | $2/s$ | 0.3000 | $3.060\,\mu\mathrm s$ |
| Four bubbles: square | $(2+1/\sqrt2)/s$ | 0.4061 | $3.163\,\mu\mathrm s$ |
| Five bubbles: regular pentagon | $(2+2/\varphi_g)/s$ | 0.4854 | $3.238\,\mu\mathrm s$ |

In this particular symmetric collapse control, interaction slows the radial contraction. The calculation does **not** show that arrays always weaken jets: jet direction and focusing require spatial interface dynamics, and real PFC pressure histories need not remain constant. The zero-radius endpoint is only a formal analytical benchmark, with the same physical limitation as Equation (1.6).

This comparison holds maximum radius per bubble fixed; its total initial pressure-work scale increases with bubble number. It is not a demonstration of improved performance at fixed total laser energy. A five-bubble cross with a central bubble is also not equivalent to a regular pentagon: the center and outer sites have different neighbor-distance sums, so identical starting sizes do not preserve identical radial histories.

## 3.4 Extending from a cluster to an array

Let $V_\Omega$ be a representative array-region volume and $V_i$ each bubble volume. The instantaneous vapor-volume fraction is

$$
\phi_b=\frac{\sum_i V_i}{V_\Omega}.
\tag{3.8}
$$

For an ideal three-dimensional cubic lattice with one spherical bubble of radius $R$ per cell of side $s$, this becomes $\phi_b=4\pi R^3/(3s^3)$. It is not the same as the PFC-liquid loading fraction before activation, and it is not directly applicable to a single planar layer without defining that layer's thickness.

A homogenized description additionally requires an averaging length much larger than the pitch and much smaller than the scale over which the array changes. Near edges, outlets, defects, or a film, this separation may fail. Small volume fraction alone does not prove negligible interaction because the cumulative influence of many neighbors can remain significant.

If travel time matters but disturbances remain weak, let $r_i$ be distance from source $i$ to an observation point and $c$ carrier sound speed. A leading far-field transient estimate is

$$
p'(\boldsymbol x,t)
\simeq\sum_i\frac{\rho}{4\pi r_i}
\ddot V_i\left(t-\frac{r_i}{c}\right).
\tag{3.9}
$$

The dot here differentiates bubble volume in time. Both activation delay and propagation delay affect overlap. Equation (3.9) is a distant-source, weak-disturbance estimate, not a pressure law inside the near-field jet or at a moving film. Source interaction can also alter $V_i(t)$, so source histories cannot always be prescribed independently.

## 3.5 Turning an energy allocation into a jet calculation

Define a jet cross-sectional diameter $d_j$, radius $r_j=d_j/2$, and an emitted liquid length $L_j$. For an approximately cylindrical, uniform-density emitted portion, its cross-sectional area $A_j$ and mass $m_j$ are

$$
A_j=\frac{\pi d_j^2}{4},
\qquad
m_j=\rho A_jL_j.
\tag{3.10}
$$

Let $E_j$ be its kinetic energy and $U_{\mathrm{rms}}$ its mass-weighted root-mean-square speed. By definition,

$$
E_j=\frac12m_jU_{\mathrm{rms}}^2.
\tag{3.11}
$$

If $E_{\mathrm{avail}}$ is the mechanical energy available to that jet, energy conservation imposes

$$
U_{\mathrm{rms}}\le\sqrt{\frac{2E_{\mathrm{avail}}}{m_j}}.
\tag{3.12}
$$

Let $P_j$ be the jet momentum in the intended transfer direction. Applying the Cauchy–Schwarz inequality to the mass integral of velocity gives

$$
P_j^2\le2m_jE_j.
\tag{3.13}
$$

Equality requires a uniform velocity directed along that axis. A very fast, tiny jet tip may have little energy or useful momentum. Report tip speed separately from a finite-mass or finite-volume velocity.

For a simple allocation model, define $\eta_j=E_j/E_{\mathrm{abs,site}}$, where $E_{\mathrm{abs,site}}$ is absorbed energy assigned to one site. This conversion factor must come from a resolved energy balance or measurement; assigning it is a conditional estimate. It cannot be obtained merely by subtracting latent heat from laser energy, because thermal storage, phase work, carrier motion, surface creation, and heat loss occur together.

A well-posed energy budget also includes any deliberately supplied initial pressure energy or recoverable elastic energy. The laser is not necessarily the only energy reservoir. Conversely, the same bubble pressure work must not be counted twice as both “stored bubble energy” and a second independent source.

**A geometry-based jet description.** An assigned energy fraction is not the only way to proceed. Once an approximately axisymmetric slender jet exists, its cross-section and velocity can be evolved directly. Let $z$ be axial position, $a_j(z,t)$ the local jet radius, $A_j(z,t)=\pi a_j^2$ its local area, and $v_j(z,t)$ its cross-sectionally averaged axial velocity. A slice conserves liquid volume, giving

$$
\partial_t A_j+\partial_z(A_jv_j)=0.
\tag{3.13a}
$$

Let $\kappa_j$ be free-surface curvature, positive for a cylindrical liquid thread, and $\sigma_j$ be jet–gas surface tension. For constant external gas pressure, constant surface tension, and a slender Newtonian jet, the leading axial momentum equation is

$$
\partial_t v_j+v_j\partial_zv_j
=-\frac{\sigma_j}{\rho}\partial_z\kappa_j
+\frac{3\mu}{\rho A_j}\partial_z(A_j\partial_zv_j),
\qquad
\kappa_j=\frac{1}{a_j\sqrt{1+(\partial_za_j)^2}}
-\frac{\partial_{zz}a_j}{[1+(\partial_za_j)^2]^{3/2}}.
\tag{3.13b}
$$

The factor 3 in the viscous term is the Newtonian extensional-viscosity factor under these assumptions. Surface-curvature gradients accelerate liquid from one portion of the thread to another, while stretching changes its area through Equation (3.13a). [R14](#r14)

Initial jet shape and velocity, the inflow history, and end conditions must come from the bubble–meniscus launch calculation or measurements. Equations (3.13a) and (3.13b) then predict transport and thinning rather than assuming a fixed cylindrical shape. They do not replace a two- or three-dimensional launch calculation when a cavity first collapses, turns a corner, or forms a re-entrant jet. This establishes a usable theoretical division: radial dynamics for cavity scales, spatial interface dynamics for jet creation, and slender-jet dynamics for subsequent transport when its assumptions hold.

## 3.6 Will the emitted liquid remain a coherent jet?

For the following comparisons, use the jet–surrounding-phase surface tension $\sigma_j$, which may differ from the bubble–carrier surface tension used earlier. For representative jet speed $U_j$, define the Reynolds, Weber, and Ohnesorge numbers using diameter $d_j$:

$$
\mathrm{Re}_j=\frac{\rho U_jd_j}{\mu},
\qquad
\mathrm{We}_j=\frac{\rho U_j^2d_j}{\sigma_j},
\qquad
\mathrm{Oh}_j=\frac{\mu}{\sqrt{\rho\sigma_jd_j}}.
\tag{3.14}
$$

These compare inertia with viscosity, inertia with surface tension, and viscous effects with inertial–capillary effects, respectively. They do not independently predict the breakup location.

A cylindrical liquid thread tends to reduce surface area by developing necks and droplets. Define the radius-based capillary time $t_\sigma=\sqrt{\rho r_j^3/\sigma_j}$. For an ideal long inviscid cylinder in a dynamically negligible surrounding gas, axisymmetric disturbances with wavelength greater than $2\pi r_j$ grow. The fastest-growing wavelength is approximately $9.02r_j$, with growth rate $s_{\max}\approx0.343/t_\sigma$.

Let $\delta_0$ be the initial amplitude of that unstable disturbance. Linear growth gives $\delta(t)=\delta_0e^{s_{\max}t}$. Estimating neck formation when $\delta$ becomes comparable to $r_j$ gives

$$
t_{\mathrm{break}}\sim
\frac{t_\sigma}{0.343}\ln\left(\frac{r_j}{\delta_0}\right).
\tag{3.15}
$$

This is a disturbance-dependent estimate, not a universal jet lifetime. Finite ends, viscosity, axial stretching, wetting, and the surrounding liquid change the result. Slender-jet theory supplies a next level of description when the jet remains approximately axisymmetric. [R14](#r14)

Let $H$ be the flight gap. The simple flight time is $t_{\mathrm{flight}}=H/U_j$. Comparing flight and breakup times establishes whether coherent arrival is plausible. A jet traveling through another dense liquid needs the corresponding two-fluid resistance and stability treatment; an air-gap calculation cannot be reused unchanged.

## 3.7 Impact pressure, useful impulse, and finite limits

Three pressure quantities have different meanings. The internal bubble pressure drives cavity motion. The jet dynamic-pressure scale describes flow deceleration. The earliest compressive impact pulse describes short-time stress transmission. None is automatically the opening traction at a buried release interface.

For jet speed $U_j$, define dynamic pressure $q_j$ as

$$
q_j=\frac12\rho U_j^2.
\tag{3.16}
$$

For a short, locally one-dimensional impact, let $Z_l=\rho c$ be the liquid longitudinal impedance and $Z_r$ the receiver's effective longitudinal impedance. Let $v_i$ be initial interface velocity. Matching pressure and velocity across the impact gives $p_{\mathrm{early}}=Z_l(U_j-v_i)=Z_rv_i$, hence

$$
p_{\mathrm{early}}\simeq
\frac{Z_lZ_r}{Z_l+Z_r}U_j.
\tag{3.17}
$$

For a nearly rigid receiver, this approaches $\rho cU_j$. This result describes the initial compressive contact before important lateral release or finite-thickness reflections. It is not a steady pressure sustained for the entire jet duration, and a thin flexible film does not generally behave as a semi-infinite rigid receiver.

A momentum check prevents misuse of the large value. If a jet of length $L_j$ is stopped without rebound, its incoming momentum is $m_jU_j$. If pressure $\rho cU_j$ were the sole uniform stopping load over area $A_j$, the equivalent duration $\tau_{\mathrm{eq}}$ would satisfy

$$
(\rho cU_j)A_j\tau_{\mathrm{eq}}=m_jU_j
\quad\Longrightarrow\quad
\tau_{\mathrm{eq}}=\frac{L_j}{c}.
\tag{3.18}
$$

This is an impulse-equivalent duration, not a prescribed rectangular pulse. Real pulse shapes, reflected waves, spreading, and later flow redistribute the load. A much larger pressure cannot be assigned arbitrarily long duration without supplying the corresponding momentum and energy.

Pressure maxima also require an observation definition. Let $A_o$ be a specified observation area and $\tau_o$ a specified averaging time. A simple signed, area–time averaged pressure is

$$
p_{\mathrm{obs}}(t)=
\frac{1}{A_o\tau_o}
\int_{t-\tau_o}^{t}\int_{A_o}
[p(\boldsymbol x,s_t)-p_{\mathrm{ref}}] \,dA\,ds_t,
\tag{3.19}
$$

where $s_t$ is a dummy time variable. Record the location, reference pressure, area, bandwidth, and whether the measurement is in the fluid, on the exposed surface, or at the release interface. A pointwise numerical spike is not equivalent to a finite-bandwidth mechanical load.

There is consequently no meaningful geometry-free “maximum cavitation-jet pressure.” A defensible maximum is conditional on a bounded operating set: laser energy and pulse duration, absorber damage limit, PFC inventory, geometry, allowed jet mass, and the chosen observer. Equation (3.12) bounds finite-mass speed for a stated available energy, but does not bound an arbitrarily small mathematical tip. Sound speed is a criterion for changing the fluid model, not a universal speed ceiling. [R3](#r3), [R4](#r4), [R5](#r5)

At fixed total bubble mechanical energy, dividing it among $N$ equal cavities gives $R_{\max}\propto N^{-1/3}$ under Equation (1.7), rather than leaving every radius unchanged. At fixed total emitted mass and kinetic energy, Equation (3.13) also limits total aligned momentum. Increasing bubble count alone is therefore not a free pressure or impulse multiplier.

When compressibility is needed, let $e$ be specific internal energy, $e_t=e+|\boldsymbol u|^2/2$ total specific energy, $\boldsymbol\tau$ viscous stress, $\boldsymbol I$ the identity tensor, and $\boldsymbol q$ conductive heat flux. The bulk conservation equations are

$$
\begin{aligned}
\partial_t\rho+\nabla\cdot(\rho\boldsymbol u)&=0,\\
\partial_t(\rho\boldsymbol u)
+\nabla\cdot(\rho\boldsymbol u\otimes\boldsymbol u+p\boldsymbol I-\boldsymbol\tau)&=0,\\
\partial_t(\rho e_t)
+\nabla\cdot[(\rho e_t+p)\boldsymbol u-\boldsymbol\tau\cdot\boldsymbol u+\boldsymbol q]
&=Q_{\mathrm{abs}}.
\end{aligned}
\tag{3.20}
$$

Close them with an appropriate equation of state, thermal and transport properties, species conservation where needed, and moving-interface jump conditions. These equations replace—not supplement with a second independent pressure source—the incompatible incompressible impact approximation when shocks and strong compression must be resolved.

## 3.8 An integrated array-to-jet calculation

Consider a declared **5 × 5 array of separately supplied liquid cells**, with $200\,\mu\mathrm m$ pitch. Each cell contains the PFC mass used in Section 2.6, initially supplies $50\,\mathrm{pL}$ of carrier liquid, and emits one jet into an air gap. Inter-cell hydrodynamic interaction is neglected for this example. The interacting clusters of Section 3.3 are a separate control, not an additional multiplier.

Take total incident laser energy $E_L=25\,\mu\mathrm J$, intercepted fraction $f_{\mathrm{geo}}=0.8$, and effective absorptance $A_\lambda=0.5$. Equal optical allocation gives $E_{\mathrm{abs}}=10\,\mu\mathrm J$ total and $400\,\mathrm{nJ}$ per site.

As a declared thermal-routing assumption, suppose 40% of each site's absorbed energy has reached its PFC inventory by the relevant activation deadline: $160\,\mathrm{nJ}$ per core. This exceeds the approximate $97.82\,\mathrm{nJ}$ preparation requirement, but does not establish the necessary spatial temperature or nucleation rate. In particular, the diffusion-time check in Section 2.2 still applies.

Separately suppose the overall absorbed-energy-to-emitted-jet kinetic conversion is $\eta_j=0.005$. Each jet then has $E_j=2.00\,\mathrm{nJ}$. This is an assumed output allocation, not a deduction from the thermal fraction; intermediate heat transfer and final jet energy are not disjoint budget entries to add together.

Use water-like carrier properties $\rho=1000\,\mathrm{kg\,m^{-3}}$, $\mu=1.0\times10^{-3}\,\mathrm{Pa\,s}$, $\sigma_j=0.072\,\mathrm{N\,m^{-1}}$, and $c=1480\,\mathrm{m\,s^{-1}}$. Let each nearly uniform jet have $d_j=10\,\mu\mathrm m$ and $L_j=50\,\mu\mathrm m$. Let the air gap be $H=100\,\mu\mathrm m$.

| Calculated quantity | Result | Interpretation |
|---|---:|---|
| Emitted mass per jet, $\rho\pi d_j^2L_j/4$ | $3.927\times10^{-12}\,\mathrm{kg}$ | Carrier-liquid mass; not PFC vapor mass |
| Uniform-speed estimate, $\sqrt{2E_j/m_j}$ | $31.92\,\mathrm{m\,s^{-1}}$ | Conditional on the assigned kinetic-energy fraction |
| Dynamic-pressure scale | $0.509\,\mathrm{MPa}$ | Not the actual buried-interface traction |
| Early rigid-contact pressure scale | $47.23\,\mathrm{MPa}$ | Short-time impedance estimate only |
| Momentum per jet | $1.253\times10^{-10}\,\mathrm{N\,s}$ | Before redirection, spreading, and solid coupling |
| Total kinetic energy of 25 jets | $50.0\,\mathrm{nJ}$ | Sum for the stated independent cells |
| Total aligned incoming momentum | $3.133\times10^{-9}\,\mathrm{N\,s}$ | Upper incoming directional sum before load-path losses |
| Impulse-equivalent early-contact duration, $L_j/c$ | $33.78\,\mathrm{ns}$ | Not the full emission duration |
| Emission timescale, $L_j/U_j$ | $1.567\,\mu\mathrm s$ | A geometrical plug-flow estimate |
| Flight time, $H/U_j$ | $3.133\,\mu\mathrm s$ | Air-gap control |
| $\mathrm{Re}_j$, $\mathrm{We}_j$, $\mathrm{Oh}_j$ | 319, 141, 0.0373 | Inertia-dominated launch with capillary breakup still possible |

The emitted liquid volume is $m_j/\rho=3.927\,\mathrm{pL}$ per site, below the assigned $50\,\mathrm{pL}$ carrier inventory. The radius-based capillary time is $1.318\,\mu\mathrm s$. With an assumed initial disturbance amplitude $\delta_0=0.01r_j$, Equation (3.15) gives approximately $17.7\,\mu\mathrm s$ for the ideal fastest-growing disturbance to reach the radius scale. Coherent arrival over the specified gap is therefore plausible in this control, but the estimate does not test startup shape, finite-length effects, or actual disturbance amplitudes.

**Chapter connection.** The important output is not “47 MPa.” It is a finite liquid mass, velocity field, momentum, kinetic energy, impact footprint, and time history at a specified surface. Chapter 4 determines whether that loading can release and place an intact object.

---

<a id="chapter-4"></a>
# 4. Fundamentals of Transfer Fracture Mechanics and Laser-Pulse-Induced PFC-Droplet Cavitation-Jet Transfer

## 4.1 Begin with the actual load path

The transferable object must separate from a **donor/release interface** and arrive at a **receiving surface**. The liquid-facing surface need not be the release interface. Draw the stack mentally in the direction of force transmission before assigning any pressure to a fracture law.

| Configuration | Mechanical path | Correct theoretical interpretation |
|---|---|---|
| Direct liquid-to-film actuation | Bubble-driven liquid or jet → film → release interface | Fluid traction drives film deformation and crack advance |
| Intact PVC-mediated actuation | Liquid or jet → PVC → contact/bonded layer → film → release interface | PVC inertia, compliance, reflections, and contact determine the transmitted load |
| Sealed interfacial cavity | Vapor pressure → cavity wall or stamp → release interface | Pressure-driven bulging and fracture; no outgoing liquid jet is required |
| Open liquid pocket in a gel support | Bubble-driven pocket liquid → actual outlet → jet → payload | Jetting is possible only if the pocket geometry supplies a liquid flow path |

An intact PVC sheet is a barrier to liquid passage. A jet striking it cannot also be assumed to strike the film directly unless a real opening or rupture is present. Similarly, observing a hydrogel stamp bulge and release an object does not demonstrate a liquid cavitation jet. The published hydrogel-composite transfer mechanism is discussed in Appendix A. [R11](#r11)

## 4.2 From fluid motion to film loading

Let $\boldsymbol D_u=[\nabla\boldsymbol u+(\nabla\boldsymbol u)^T]/2$ be the liquid strain-rate tensor, and $\boldsymbol n_f$ the unit normal pointing outward from the solid into the liquid. The Newtonian liquid stress $\boldsymbol T_l$ and the traction applied to the solid are

$$
\boldsymbol T_l=-p\boldsymbol I+2\mu\boldsymbol D_u,
\qquad
\boldsymbol t_l=\boldsymbol T_l\boldsymbol n_f.
\tag{4.1}
$$

Both pressure and viscous shear contribute. The pressure contribution can compress the payload even while its subsequent bending opens an interface elsewhere. “Positive fluid pressure” is therefore not synonymous with “positive opening traction.”

Let $A_f$ be the loaded solid surface, $\boldsymbol v_f$ its velocity, $\boldsymbol F_l$ the resultant fluid force, and $\mathcal W_l$ the work transferred from fluid to solid during the event. Then

$$
\boldsymbol F_l(t)=\int_{A_f}\boldsymbol t_l\,dA,
\qquad
\mathcal W_l=\int\!\int_{A_f}\boldsymbol t_l\cdot\boldsymbol v_f\,dA\,dt.
\tag{4.2}
$$

Force integrated in time gives impulse; traction dotted with velocity and integrated in time gives work. These are distinct. A short high-pressure pulse on an almost stationary rigid surface can transmit substantial stress but little deformation work.

For an intact intermediate sheet, Equation (4.1) first loads that sheet. Its motion and contact then determine the next traction. The fluid pressure history should not be copied unchanged to every interface in the stack.

## 4.3 The minimum transient film mechanics

Consider a thin isotropic film with thickness $h_f$, density $\rho_f$, Young's modulus $E_f$, and Poisson's ratio $\nu_f$. Define areal mass $m_A=\rho_fh_f$ and bending stiffness $D_f=E_fh_f^3/[12(1-\nu_f^2)]$. Let $w(x,y,t)$ be displacement in the intended opening direction, $T_0$ uniform in-plane pretension per unit length, $p_{\mathrm{load}}$ the applied net transverse load, and $t_{\mathrm{coh}}$ the resisting cohesive traction. The small-slope plate equation is

$$
m_A\frac{\partial^2w}{\partial t^2}
+D_f\nabla^4w-T_0\nabla^2w
=p_{\mathrm{load}}-t_{\mathrm{coh}}.
\tag{4.3}
$$

Here $\nabla$ acts in the film plane. The boundaries must be specified: clamped edges, free edges, existing delamination, or evolving contact lead to different responses. For example, a clamped boundary imposes both $w=0$ and zero normal slope. Large deformation requires membrane stretching and geometric nonlinearity; a multilayer stack requires its actual bending and extensional stiffnesses.

The inertia term is essential for a short laser-driven load. There is no need to introduce a modal or harmonic-vibration curriculum to use it. If the applied pulse is sufficiently short that the integrated bending, pretension, and cohesive forces are negligible during that pulse, define the local applied impulse per area as $J_A=\int p_{\mathrm{load}}dt$. Integrating Equation (4.3) gives the approximate velocity jump and areal kinetic energy

$$
\Delta\dot w\simeq\frac{J_A}{m_A},
\qquad
\mathcal E_A\simeq\frac{J_A^2}{2m_A}.
\tag{4.4}
$$

The film may then deform and fracture after the pressure maximum has passed. If substrate constraints or cohesive forces deliver comparable impulse during loading, use the full balance instead. Likewise, do not add a separate “fluid added mass” when the same fluid inertia is already included through a resolved coupled fluid traction.

## 4.4 Strength, adhesion energy, and fracture toughness

Three interface properties are often confused. The **peak cohesive traction** $T_{\max}$ has units Pa and characterizes local separation strength. The **reversible work of adhesion** is a thermodynamic surface-energy difference. The practical **fracture energy** $\Gamma$ has units J·m$^{-2}$ and includes the dissipation associated with advancing the interface under the relevant conditions.

Let $A_c$ be crack area and $\mathcal P$ the total potential energy of a quasistatic mechanical system under a stated loading control. Define energy-release rate $G$ as

$$
G=-\left.\frac{\partial\mathcal P}{\partial A_c}\right|_{\text{specified loading control}}.
\tag{4.5}
$$

The crack can advance when the available energy-release rate reaches the appropriate resistance. Let $\psi$ describe the mixture of opening and shear, $T_i$ the interface temperature, and $v_c$ crack-front speed. Then the initiation/propagation criterion is represented by

$$
G\ge\Gamma(\psi,T_i,v_c).
\tag{4.6}
$$

The energy available to a crack depends on geometry, compliance, loading history, and whether the external system holds pressure, force, or displacement fixed. Under rapid loading, kinetic energy and energy flux into the moving crack must be retained; a quasistatic potential derivative alone is insufficient.

Transfer is also a **competing-fracture problem**. The desired interface must release before an unintended interface separates or the payload tears. Rate-dependent adhesion can change which path wins, as established in transfer-printing fracture studies. [R10](#r10)

There is no physically meaningful comparison of a pressure in MPa with an adhesion energy in J·m$^{-2}$ without a deformation length and a mechanical model connecting them.

## 4.5 Deriving a pressure-to-fracture relation for a simple blister

A solvable limit shows exactly how geometry enters. Consider a circular pre-existing delamination of radius $b$ under a thin plate of bending stiffness $D_f$. The plate is clamped at the delamination edge and loaded by uniform, externally maintained pressure difference $p_0$. Neglect inertia, membrane stretching, and pretension.

With radial coordinate $r$, the axisymmetric solution of $D_f\nabla^4w=p_0$, satisfying zero displacement and slope at $r=b$, is

$$
w(r)=\frac{p_0}{64D_f}(b^2-r^2)^2.
\tag{4.7}
$$

Let $V_{\mathrm{bl}}$ be the added blister volume. Integrating the displacement gives

$$
V_{\mathrm{bl}}=2\pi\int_0^b w(r)r\,dr
=\frac{\pi p_0b^6}{192D_f}.
\tag{4.8}
$$

For a linear elastic structure, stored strain energy is $p_0V_{\mathrm{bl}}/2$. The maintained pressure source performs work $p_0V_{\mathrm{bl}}$, so total potential energy is $\mathcal P=-p_0V_{\mathrm{bl}}/2$. Since crack area is $A_c=\pi b^2$, Equation (4.5) becomes

$$
G=-\frac{d\mathcal P/db}{dA_c/db}
=\frac{p_0^2b^4}{128D_f}.
\tag{4.9}
$$

For constant fracture energy $\Gamma$, the critical maintained pressure is therefore

$$
p_{0,\mathrm{crit}}=\frac{\sqrt{128D_f\Gamma}}{b^2}.
\tag{4.10}
$$

A larger existing delamination can propagate under a much lower pressure. The same pressure applied over a tiny jet footprint and over a broad blister therefore need not have comparable fracture consequences.

For a separate illustrative plate with $E_f=2\,\mathrm{GPa}$, $h_f=10\,\mu\mathrm m$, $\nu_f=0.35$, $b=100\,\mu\mathrm m$, and $\Gamma=0.10\,\mathrm{J\,m^{-2}}$, the bending stiffness is $1.899\times10^{-7}\,\mathrm{N\,m}$ and the critical pressure is about $156\,\mathrm{kPa}$. Equation (4.7) then gives central deflection about $1.28\,\mu\mathrm m$, allowing the small-deflection assumption to be checked.

This is a quasistatic constant-pressure blister, not a short jet impact. In a sealed laser-heated cavity, pressure usually changes as volume, temperature, and vapor mass change. Its thermodynamics must be coupled to the film rather than replaced by an infinite constant-pressure source. A dynamic jet-driven crack likewise requires the actual time-dependent traction and film inertia.

## 4.6 A local cohesive law connects strength and separation work

For an interface without a prescribed crack path length, a traction–separation description can represent crack initiation and growth. Let $\delta$ be local opening, $K_n$ initial normal stiffness per area, $\delta_0=T_{\max}/K_n$ the opening at peak traction, and $\delta_c$ final separation. A simple monotonic triangular law is

$$
t_n(\delta)=
\begin{cases}
K_n\delta, & 0\le\delta\le\delta_0,\\
T_{\max}\dfrac{\delta_c-\delta}{\delta_c-\delta_0},
& \delta_0<\delta<\delta_c,\\
0, & \delta\ge\delta_c.
\end{cases}
\tag{4.11}
$$

The fracture energy is the area under this curve:

$$
\Gamma=\int_0^{\delta_c}t_n(\delta)\,d\delta
=\frac12T_{\max}\delta_c.
\tag{4.12}
$$

A complete transient law must additionally specify unloading, irreversible damage, compression/contact, and mixed-mode separation. Compression should not accumulate tensile opening damage merely because its pressure magnitude is large. The parameters must correspond to the actual release interface and relevant temperature and rate.

Equations (4.11) and (4.12) make the two requirements visible: reaching the local strength can initiate damage, but enough separation work must still be supplied to complete release. Conversely, a favorable total-energy budget does not guarantee that the load reaches the correct interface or initiates a crack there.

## 4.7 Completing the array example: does the film actually release?

Return to the 25-jet calculation in Section 3.8. Let the transferable film have area $A_f=1\,\mathrm{mm^2}$, thickness $h_f=1\,\mu\mathrm m$, and density $\rho_f=2330\,\mathrm{kg\,m^{-3}}$. Its mass is

$$
m_f=\rho_fA_fh_f=2.33\times10^{-9}\,\mathrm{kg}.
$$

For a conditional global screening calculation, suppose the actual load path makes 20% of incoming jet kinetic energy available for film deformation, release, and outgoing motion. Let that useful energy be $E_{\mathrm{solid}}=10.0\,\mathrm{nJ}$. Also suppose the net opening-direction impulse on the payload after load-path reactions is 50% of the aligned incoming jet momentum: $I_{\mathrm{net}}=1.567\times10^{-9}\,\mathrm{N\,s}$. These are stated coupling assumptions, not measured efficiencies or universal transmission factors.

Let $v_f$ be required outgoing center-of-mass speed. Starting from rest, with no additional recoverable solid-energy source, necessary global screens are

$$
E_{\mathrm{solid}}
\ge\Gamma A_f+\frac12m_fv_f^2,
\qquad
I_{\mathrm{net}}\ge m_fv_f.
\tag{4.13}
$$

The impulse condition uses the **net** external impulse after interface and support reactions; incoming liquid momentum alone is not enough. The energy condition omits residual bending, rotation, viscous losses, and unintended fracture, so passing it does not prove success.

For $\Gamma=0.020\,\mathrm{J\,m^{-2}}$, separation alone requires $20.0\,\mathrm{nJ}$, already greater than the assigned useful energy. Under these assumptions, complete release fails the energy screen even though the earlier rigid-impact pressure scale was about 47 MPa.

Now change only the assumed release-interface fracture energy to $0.005\,\mathrm{J\,m^{-2}}$ and require $v_f=0.50\,\mathrm{m\,s^{-1}}$. Separation requires $5.00\,\mathrm{nJ}$ and translation requires $0.291\,\mathrm{nJ}$. Their sum, $5.291\,\mathrm{nJ}$, is below $10.0\,\mathrm{nJ}$. Required net impulse is $1.165\times10^{-9}\,\mathrm{N\,s}$, also below the assigned value.

The necessary screens now pass. The next theoretical checks are spatial: whether the crack reaches the whole intended interface, whether the 25 footprints cause local puncture or excessive bending, and whether the object arrives intact. The lower fracture energy was selected to demonstrate the calculation, not claimed as a measured property or a proposed treatment.

## 4.8 Release, placement, and reset define the useful operating window

A successful operating condition must complete the whole chain without a competing failure. Activation must occur where intended; cavity motion must produce the desired jet or pressure-driven actuator; the delivered traction must release the intended interface; and the payload must survive both departure and landing.

Placement adds geometrical constraints. Let $\theta$ be the outgoing trajectory angle relative to the target normal and $H_f$ the free-flight distance of the payload. Neglecting drag and gravity over a short flight, the lateral offset is

$$
\Delta x=H_f\tan\theta.
\tag{4.14}
$$

Thus a small angular error becomes a placement error at finite gap. Nonuniform site activation can also generate torque and rotation even when total impulse is adequate. The receiving surface must arrest the payload without rebound or damage and provide the intended final adhesion.

Reset depends on cooling, condensation, remaining liquid inventory, shell integrity, and removal or retention of gas. A good first shot does not establish repeatable operation. Persistent cavities can alter optical absorption, wetting, pressure transmission, and the available PFC inventory for the next pulse.

The minimum evidence needed to test the theory is correspondingly specific: deposited energy and activation statistics; bubble size and shape versus time; finite jet mass, speed, direction, and arrival time; actual solid motion and crack progression; and final placement and reset. Each measurement constrains a distinct link. Fitting only a maximum bubble radius cannot independently determine absorption, phase kinetics, jet efficiency, and interfacial toughness.

**Project-level conclusion.** The design objective is an operating window for reproducible intact transfer, not the largest isolated pressure value. The useful calculation proceeds from energy deposition to phase state, from phase state to liquid motion, from motion to interface loading, and from interface loading to fracture and placement.

---

<a id="appendix-a"></a>
# Appendix A. Comparison of Hydrogel and Conventional Liquid Platforms

## A.1 A hydrogel changes both geometry and constitutive behavior

A conventional liquid carrier offers little static shear resistance, although viscosity and confinement can resist motion. A hydrogel contains a load-bearing polymer network and liquid. It can locate PFC droplets and preserve a patterned geometry, but it can also store elastic energy, dissipate motion, resist cavity growth, and fail. “More viscous water” is therefore not a sufficient description.

The first decision is the physical architecture:

| Platform | Available cavity/flow path | Principal advantage to evaluate | Principal cost or failure mechanism |
|---|---|---|---|
| PFC in a free or weakly confined liquid site | Liquid can move toward the meniscus or outlet | Direct liquid displacement and relatively simple carrier mechanics | Site motion, wetting variability, spreading, and neighboring-flow interactions |
| PFC in a liquid pocket supported by gel | Liquid motion is confined by a compliant wall and a defined opening | Positional control with a designed jet exit | Wall deformation consumes or returns energy and changes focusing |
| PFC embedded directly in bulk gel | Cavity expansion deforms the surrounding network | Stable initial inclusion location | Network resistance, damage, trapped vapor, and possible solid-rich ejecta |
| Sealed cavity beneath a gel/composite stamp | Expansion mainly deforms a solid boundary | Distributed actuation and conformal contact | This is a blister actuator, not necessarily liquid-jet transfer |

The hydrogel-composite transfer study by Li and colleagues demonstrates laser-driven vapor-cavity deformation in a composite stamp. It is relevant evidence for thermally driven pressure–deformation–fracture coupling, but it does not establish that bulk-gel-embedded PFC droplets emit coherent liquid jets or that hydrogel improves a PFC-jet process. [R11](#r11)

An elastic boundary can also redirect bubble-driven jets and undergo significant deformation. Its effect depends on stiffness, geometry, and event duration rather than on the word “hydrogel” alone. [R12](#r12)

## A.2 A finite-strain cavity calculation for an intact gel

Consider a spherical cavity in an infinite, incompressible, initially stress-free neo-Hookean solid. Let $R_{\mathrm{ref}}$ be the initial stress-free cavity radius, $R$ its current radius, and $G_g$ the gel shear modulus. This reference cavity is not automatically equal to the original PFC-core radius.

Let $r_0$ and $r$ be the reference and current radial positions of a material point. Conservation of the volume of material between the cavity wall and that point gives

$$
r^3-R^3=r_0^3-R_{\mathrm{ref}}^3.
\tag{A.1}
$$

The circumferential stretch is $r/r_0$ and the radial stretch follows from incompressibility. Substituting these stretches into the neo-Hookean stress law and integrating radial equilibrium gives the elastic pressure resistance

$$
p_{\mathrm{el}}(R)
=\frac{G_g}{2}
\left[5-4\frac{R_{\mathrm{ref}}}{R}
-\left(\frac{R_{\mathrm{ref}}}{R}\right)^4\right].
\tag{A.2}
$$

It vanishes at the stress-free radius and approaches $5G_g/2$ for large expansion in this ideal constitutive model. That asymptotic value is not a gel-fracture threshold. Real gels can stiffen, soften, tear, or develop a damaged zone. Nonlinear viscoelastic bubble theory provides the basis for distinguishing finite-strain network resistance from simple viscosity. [R13](#r13)

Let $\eta_g$ be a Kelvin–Voigt viscous coefficient and $\rho_g$ the effective density of the incompressible medium. Under the same spherical and negligible-phase-slip assumptions used in Chapter 1, a simple intact-medium radial control is

$$
\rho_g\left(R\ddot R+\frac32\dot R^2\right)
=p_b-p_\infty-\frac{2\sigma}{R}
-p_{\mathrm{el}}(R)-\frac{4\eta_g\dot R}{R}.
\tag{A.3}
$$

The viscous term is the chosen medium's constitutive dissipation; it should not be added to another viscosity term representing the same resistance. A liquid pocket surrounded by gel is a layered fluid–solid problem and does not in general obey Equation (A.3).

Let $W_g$ be elastic work stored during expansion from $R_{\mathrm{ref}}$ to $R$. Its work-conjugate form is

$$
W_g=4\pi\int_{R_{\mathrm{ref}}}^{R}p_{\mathrm{el}}(\xi)\xi^2\,d\xi,
\tag{A.4}
$$

where $\xi$ is a dummy radius. The corresponding viscous dissipation rate is $16\pi\eta_gR\dot R^2$. Elastic work can partly return on recoil; viscous dissipation cannot. This distinction matters when assessing whether gel deformation suppresses or redirects useful jet energy.

For a declared $G_g=20\,\mathrm{kPa}$ and expansion from $R_{\mathrm{ref}}=5\,\mu\mathrm m$ to $R=30\,\mu\mathrm m$, Equation (A.2) gives $p_{\mathrm{el}}=43.33\,\mathrm{kPa}$. This is a significant addition to a $100\,\mathrm{kPa}$ pressure scale; it cannot be ignored merely because the gel feels soft under slow handling.

## A.3 Compare the event duration with material response times

Let $\tau_{\mathrm{rel}}$ be a relevant stress-relaxation time and $\tau_e$ the cavity/jet event duration. Their ratio is the event-based Deborah number

$$
\mathrm{De}=\frac{\tau_{\mathrm{rel}}}{\tau_e}.
\tag{A.5}
$$

Large $\mathrm{De}$ means the network has little time to relax during the event. Small $\mathrm{De}$ means relaxation can substantially change the effective resistance. The appropriate modulus is therefore associated with the actual time, strain, and temperature range, not simply a slow indentation value.

Let $c_s=\sqrt{G_g/\rho_g}$ be a small-strain shear-wave speed estimate and $L_g$ the relevant gel length. The shear communication time is $t_s=L_g/c_s$. For $G_g=20\,\mathrm{kPa}$, $\rho_g=1000\,\mathrm{kg\,m^{-3}}$, and $L_g=30\,\mu\mathrm m$, this is $6.71\,\mu\mathrm s$, longer than the $2.744\,\mu\mathrm s$ liquid-collapse reference in Section 1.4. This comparison flags that an instantaneous quasistatic response of the entire surrounding gel should not be assumed. Small shear stiffness also does not imply small resistance to rapid volumetric compression.

Water drainage supplies another timescale. Let $k_{\mathrm{perm}}$ be gel permeability, $\mu_l$ solvent viscosity, and $M_d$ a relevant drained compressional modulus. A poroelastic diffusion estimate gives

$$
t_{\mathrm{poro}}\sim
\frac{\mu_lL_g^2}{k_{\mathrm{perm}}M_d}.
\tag{A.6}
$$

Events much faster than this drainage time are approximately undrained at that length scale. The assumptions behind a single-phase incompressible gel control must be reconsidered when drainage, relative solvent motion, or network rupture becomes important.

## A.4 What a fair platform comparison must establish

Compare platforms with matched PFC inventory and size distribution, absorber placement and absorbed energy, initial temperature, load path, target interface, and defined outlet geometry. Matching incident laser energy alone is insufficient if the gel changes absorption or heat transfer.

For **bulk embedding**, the central feasibility condition is not merely successful PFC vaporization. The calculation must show where displaced material goes and whether an actual carrier-liquid jet can form without unacceptable network rupture or contamination. A cavity that remains buried and spherical does not supply an external jet.

For an **open liquid pocket**, the gel can act primarily as a compliant support while the pocket supplies liquid for jetting. This separates the effect of support compliance from the stronger assumption that a jet can traverse intact bulk gel. Whether it improves performance remains a geometry- and material-dependent prediction to be tested.

For a **sealed blister**, use the phase, film-deformation, and fracture equations directly. It may be a valid transfer actuator even though it is not the same mechanism as liquid-jet transfer. Calling both “cavitation transfer” does not make their efficiencies, thresholds, or failure modes interchangeable.

The decisive comparison is the resulting intact-transfer window: activation reliability, useful emitted or transmitted impulse, selective fracture, payload integrity, placement error, contamination, and reset. Hydrogel is favorable only when its positional and contact benefits outweigh its thermal, elastic, dissipative, and failure costs for the chosen architecture.

---

<a id="defense-questions"></a>
# Three Research-Defense Questions and Reference Answers

These are the only end-of-course questions. A correct explanation in the learner's own words is sufficient; memorizing equations or reproducing the numerical examples is not required.

## Question 1 — What must happen between laser absorption and a useful PFC-driven transfer jet?

**Reference answer.** The absorber must first deposit energy in a location from which enough heat reaches the PFC on the relevant timescale. The local state must overcome the actual nucleation or shell-controlled activation condition; a low bulk boiling point alone is insufficient. Finite PFC mass then evaporates according to heat and mass transfer, setting bubble pressure together with water vapor and permanent gas. That pressure accelerates mainly the surrounding carrier. A directional jet requires an outlet, meniscus, wall, or another source of asymmetry. The jet must contain enough coherent liquid mass and momentum and must point toward the intended load path. PFC can make activation easier without guaranteeing a stronger jet, because persistent vapor, heat loss, confinement, and poor focusing can prevent useful conversion.

## Question 2 — How would you calculate a uniform array without assuming that pressure simply increases in proportion to droplet count?

**Reference answer.** I would first distinguish separate cells from bubbles sharing one liquid domain and check optical uniformity and activation statistics. Each site needs its own finite PFC inventory, heat input, and pressure history. Separate cells can be summed only after calculating their emitted masses, energies, directions, and arrival times. Connected bubbles require an interaction calculation because neighboring bubbles change the surrounding pressure and effective liquid inertia; even identical starting droplets can develop different histories near array edges. I would keep total energy accounting explicit when changing site count, report velocity for a specified finite liquid mass, and define where and over what area and time pressure is measured. A larger count is useful only if it improves the delivered load under the same stated constraints.

## Question 3 — Why can a high-pressure jet fail to transfer an intact film, and what changes when the platform is hydrogel?

**Reference answer.** A pressure maximum does not specify its area, duration, direction, or the work delivered to the release interface. The actual liquid–solid–interface load path determines film motion and crack driving force. Successful transfer needs sufficient opening strength and fracture work at the intended interface, without tearing the payload or releasing another interface first, followed by acceptable landing and adhesion. An intact PVC sheet changes that load path rather than allowing the jet to pass through it. Hydrogel additionally changes cavity confinement, elastic storage, dissipation, drainage, and possible damage. A buried gel cavity, an open liquid pocket, and a sealed blister are different actuators. I would compare their complete transfer and reset behavior, not infer success from a larger bubble or a larger local pressure.

---

<a id="references"></a>
# References and Source Basis

**Course source.** Reorganized from the user-supplied `cavitation-course-main.zip` and its accompanying public course. The source basis includes the G/T foundations, J-series jet mechanics, L01 laser/PFC material, both theoretical appendices, and the laser/PFC theory and parameter references. Software lessons and previous model results are not used as evidence. The analytical derivations and numerical examples in this course are teaching calculations with declared assumptions; literature examples are not relabeled as project measurements.

<a id="r1"></a>
**[R1]** Rayleigh, Lord. (1917). “On the pressure developed in a liquid during the collapse of a spherical cavity.” *Philosophical Magazine*, **34**, 94–98. DOI: `10.1080/14786440808635681`. Foundational spherical-collapse reference for Chapter 1.

<a id="r2"></a>
**[R2]** Cooker, M. J., and Peregrine, D. H. (1995). “Pressure-impulse theory for liquid impact problems.” *Journal of Fluid Mechanics*, **297**, 193–214. DOI: `10.1017/S0022112095003053`. Short-event pressure-impulse formulation.

<a id="r3"></a>
**[R3]** Supponen, O., Obreschkow, D., Tinguely, M., Kobel, P., Dorsaz, N., and Farhat, M. (2016). “Scaling laws for jets of single cavitation bubbles.” *Journal of Fluid Mechanics*, **802**, 263–293. DOI: `10.1017/jfm.2016.463`. Geometry and asymmetry dependence of collapse jets; not a universal PFC-transfer calibration.

<a id="r4"></a>
**[R4]** Peters, I. R., Tagawa, Y., Oudalov, N., Sun, C., Prosperetti, A., Lohse, D., and van der Meer, D. (2013). “Highly focused supersonic microjets: numerical simulations.” *Journal of Fluid Mechanics*, **719**, 587–605. DOI: `10.1017/jfm.2013.26`. Pressure-driven meniscus focusing and spatial jet formation.

<a id="r5"></a>
**[R5]** Liang, X.-X., Linz, N., Freidank, S., Paltauf, G., and Vogel, A. (2022). “Comprehensive analysis of spherical bubble oscillations and shock wave emission in laser-induced cavitation.” *Journal of Fluid Mechanics*, **940**, A5. DOI: `10.1017/jfm.2022.202`. Laser-cavity thermodynamics, energy partition, and compressibility; used only for the relevant single-event physics.

<a id="r6"></a>
**[R6]** Strohm, E., Rui, M., Gorelikov, I., Matsuura, N., and Kolios, M. (2011). “Vaporization of perfluorocarbon droplets using optical irradiation.” *Biomedical Optics Express*, **2**(6), 1432–1442. DOI: `10.1364/BOE.2.001432`. Formulation-specific optical PFC activation evidence.

<a id="r7"></a>
**[R7]** Wei, C.-W., et al. (2014). “Laser-induced cavitation in nanoemulsion with gold nanospheres for blood clot disruption: in vitro results.” *Optics Letters*, **39**(9), 2599–2602. DOI: `10.1364/OL.39.002599`. Optical activation of an absorber-containing PFH system; not a transfer-jet performance measurement.

<a id="r8"></a>
**[R8]** NIST Chemistry WebBook, Standard Reference Database 69. “Pentane, dodecafluoro-” (CAS 678-26-2): phase-change and condensed-phase thermochemistry entries. Database DOI: `10.18434/T4D303`. PFP molar mass, normal-boiling data, Barber–Cady vapor-pressure correlation, and the listed Campos-Vallette–Diaz heat-capacity datum. Correlation validity and datum temperature are stated in Chapter 2.

<a id="r9"></a>
**[R9]** NIST Chemistry WebBook, Standard Reference Database 69. “Hexane, tetradecafluoro-” (CAS 355-42-0): phase-change entry. Database DOI: `10.18434/T4D303`. PFH molar mass, normal-boiling datasets, and vaporization enthalpy at the specified temperature.

<a id="r10"></a>
**[R10]** Feng, X., Meitl, M. A., Bowen, A. M., Huang, Y., Nuzzo, R. G., and Rogers, J. A. (2007). “Competing fracture in kinetically controlled transfer printing.” *Langmuir*, **23**(25), 12555–12560. DOI: `10.1021/la701555n`. Competing interfaces and rate-dependent transfer fracture.

<a id="r11"></a>
**[R11]** Li, C., Luo, H., Lin, X., Zhang, S., and Song, J. (2024). “Laser-driven noncontact bubble transfer printing via a hydrogel composite stamp.” *Proceedings of the National Academy of Sciences*, **121**(5), e2318739121. DOI: `10.1073/pnas.2318739121`. Hydrogel-composite vapor-cavity actuation and transfer; distinguished here from PFC liquid-jet transfer.

<a id="r12"></a>
**[R12]** Brujan, E.-A., Nahen, K., Schmidt, P., and Vogel, A. (2001). “Dynamics of laser-induced cavitation bubbles near an elastic boundary.” *Journal of Fluid Mechanics*, **433**, 251–281. DOI: `10.1017/S0022112000003347`. Deformable-boundary effects on bubble and jet motion.

<a id="r13"></a>
**[R13]** Gaudron, R., Warnez, M. T., and Johnsen, E. (2015). “Bubble dynamics in a viscoelastic medium with nonlinear elasticity.” *Journal of Fluid Mechanics*, **766**, 54–75. DOI: `10.1017/jfm.2015.7`. Finite-strain viscoelastic cavity mechanics.

<a id="r14"></a>
**[R14]** Eggers, J., and Dupont, T. F. (1994). “Drop formation in a one-dimensional approximation of the Navier–Stokes equation.” *Journal of Fluid Mechanics*, **262**, 205–221. DOI: `10.1017/S0022112094000480`. Slender free-surface liquid dynamics and breakup.

<a id="r15"></a>
**[R15]** NIST Chemistry WebBook, Standard Reference Database 69. “Water” (CAS 7732-18-5): phase-change entry. Database DOI: `10.18434/T4D303`. Water normal-boiling data and the Bridgeman–Aldrich vapor-pressure correlations. The 293 K calculation uses the listed 273–303 K correlation; the 323 K calculation uses the listed 304–333 K correlation.
