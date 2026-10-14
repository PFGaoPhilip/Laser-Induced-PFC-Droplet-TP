# Finite PFC in hydrogel: derivation and validation requirements

## 1. Problem, objective and scope

Determine the state energy needed to expand a PFC vapor core inside intact hydrogel. Calculate gel load and energy. Identify the additional conditions for exterior ejection and collapse pressure.

This **conditional study** solves finite PFC mass, concentric vapor and liquid phases, real-fluid thermodynamics, separate interfaces, gel elasticity and host viscosity. The transient starts from a **supplied post-nucleation seed**. Its retained energy is calculated relative to an all-liquid reference. Laser heating and seed formation remain unresolved.

Two models are retained. The first solves prescribed-radius curved equilibrium and local stability. The second solves insulated radial expansion from a prescribed seed. It stops at first turning, the declared stretch screen or the time cutoff. Both have zero outlet flow. The effectively infinite, undrained gel has radial inertia. Omitted effects are liquid-shell inertia, thermal gradients, phase-transfer kinetics, damage, water vapor, gas diffusion and acoustic radiation. Inner traction is quasistatic. These assumptions bound every result.

Use spherical coordinates directed outward from the inclusion center. Both radii are positive. Expansion has positive radial speed. Thermodynamic pressures are **absolute**. Resistance and pressure differences are signed excesses. The initial liquid has outer capillary traction and ambient loading. At infinity, displacement and speed vanish; stress approaches minus ambient pressure. PFC mass is closed and exterior mass flux is zero. Both phases have uniform temperature and equal chemical potential. This is a post-activation equilibrium approximation. Nanosecond thermal homogenization is **not established**.

The all-liquid reference starts at room temperature, prescribed radius and Laplace pressure. The seed starts at stretch 1.2 with zero speed and zero accumulated loss. Its liquid pressure exceeds static host traction by 50 kPa. Include seed storage and ambient work. Preparation is lossless here; pre-seed heat, viscous and acoustic losses are omitted. Gel elasticity remains reversible up to the selected screen. Viscosity heats the host. Stretch 2.1 is a **declared stopping screen**. Measured failure strain is **not established**.

Foundations: mass conservation; the first law; Helmholtz EOS [S2](SOURCES.md); continuum interface energy and traction; incompressible neo-Hookean elasticity; Kelvin–Voigt viscosity; spherical inertia [S6, S8](SOURCES.md). The core/shell closure and comparisons are original reduced-model calculations. Physical validation requires activation data, radius histories, damage, exterior mass flux and pressure at a defined sensor.

## 2. Symbol glossary and conventions

All scalars are real. Pi is the dimensionless circle constant. Superscripts on lengths are ordinary powers; a dot denotes differentiation with time. Subscripts `0`, `l`, `v`, `o`, `i`, `el`, `amb`, `gel`, and `host` label initial, liquid, vapor, outer, inner, elastic, ambient, gel and effective host quantities. A partial derivative holds the displayed conditioning variable fixed. Integrals use the stated coordinate, area, volume or time measure. Logs and exponentials act on dimensionless arguments. Ordinary arithmetic, inequalities and limits have their usual real meanings.

| Symbol | Definition and domain | Unit |
|---|---|---|
| $t$ | Time since supplied seed, nonnegative | s |
| $a_0,R,b,W$ | Initial liquid-droplet radius; current outer radius; vapor-core radius; radial wall speed; $0<b<R$, $W=\dot R$ | m, m, m, m/s |
| $V_0,V,V_b,V_l$ | Initial inclusion, current inclusion, vapor-core and liquid-shell volumes | m³ |
| $m,m_l,m_v,x_v$ | Fixed PFC mass; liquid and vapor masses; vapor mass fraction | kg, kg, kg, dimensionless |
| $T,T_0$ | Uniform PFC temperature and initial liquid reference temperature | K |
| $\rho_l,\rho_v,\rho_{l0},\rho_h$ | Liquid, vapor, initial liquid and effective undrained host densities | kg/m³ |
| $p_l,p_v,p_\infty,p_{l0}$ | Absolute liquid, vapor, ambient and initial liquid pressures | Pa |
| $\gamma_o,\gamma_i$ | Constant outer liquid/aqueous and inner liquid/gas tensions in the controls | N/m |
| $a_H,u,s_H,g$ | Specific Helmholtz energy, internal energy, entropy and Gibbs energy/chemical potential, each as a function of temperature and density/state | J/kg, J/kg, J/(kg K), J/kg |
| $S,A_i,P_{abs},t'$ | Total PFC entropy; inner-core area; absorbed optical power; dummy time | J/K, m², W, s |
| $u_l,u_v,u_{l0},g_l,g_v$ | Phase-specific internal energies, initial liquid internal energy and phase chemical potentials | J/kg |
| $G,\eta$ | Host shear modulus and Kelvin–Voigt viscosity | Pa, Pa s |
| $s,r,\lambda_r,\lambda_\theta,\beta,C$ | Reference/current host radial coordinates; radial/circumferential stretches; reference/current radius ratio; radial-volume offset | m, m, dimensionless, dimensionless, dimensionless, m³ |
| $\sigma_{rr},\sigma_{\theta\theta},\chi$ | Elastic Cauchy stresses and incompressibility multiplier | Pa |
| $p_{el},p_{vis},p_{need}$ | Elastic resistance, viscous resistance, and static liquid pressure required by host | Pa |
| $u_h,D_{rr},D_{\theta\theta}$ | Host radial velocity and diagonal rates of deformation | m/s, 1/s, 1/s |
| $U_{PFC},E_{gel},E_{surf},E_{amb},K_h,D_h$ | PFC internal energy, gel strain energy, interface-energy change, ambient work, radial host kinetic energy and cumulative host loss | J |
| $P_{dis},E_{seed},\epsilon_E$ | Host loss power, retained seed energy relative to all-liquid reference, and normalized energy residual | W, J, dimensionless |
| $\lambda,\epsilon,k_E,k_T$ | Outer-radius stretch; small stretch perturbation; closed-energy/fixed-temperature pressure-restoration derivatives | dimensionless, dimensionless, Pa per dimensionless stretch, same |
| $p_s,U_s,\tau,E_s$ | Pressure, speed, time and energy normalization scales | Pa, m/s, s, J |
| $\theta,\widehat W,\widehat D$ | Normalized time, radial speed and accumulated loss | dimensionless |
| $F_{loc},C_{abs},f_t,E_{abs}$ | Local optical fluence, effective absorption cross section, normalized pulse shape and absorbed energy | J/m², m², 1/s, J |
| $\Delta p,r_n,\Delta\mathcal G,r_*,\Delta\mathcal G_*,J_n,\mathcal P$ | Metastable nucleus pressure driving difference; nucleus radius; nucleation free-energy change; critical radius/barrier; nucleation rate; activation probability | Pa, m, J, m, J, 1/(m³ s), dimensionless |
| $G_c,\mathcal G_f,\Pi,A_c,\delta,t_c,t_m,\delta_0,\delta_f$ | Critical fracture energy; energy release rate; potential energy; projected crack area; opening; cohesive traction; peak traction; peak-opening displacement; final separation | J/m², J/m², J, m², m, Pa, Pa, m, m |
| $h,a_c,E_{cr}$ | Cover thickness above initial inclusion, slit half-width and illustrative fracture-work requirement | m, m, J |
| $E,\rho,p$ | Fixed energy label in radial stability; generic phase density and pressure | J, kg/m³, Pa |
| $\tau_{poro},L_h$ | Pore-pressure diffusion time and drainage length | s, m |
| $\mathbf x,\Omega_l$ | Position vector and liquid spatial domain | m, domain |
| $q,n,F,K_l,K_v,\kappa_l,\kappa_v,H_{core}$ | Vapor volume and mass coordinates; internal Helmholtz energy; phase pressure-density slopes; volume-scaled slopes; relaxed core curvature | m³, kg, J, Pa m³/kg, same, Pa/kg, same, Pa/m³ |
| $d,\lambda_{surface}$ | Center-to-initial-free-surface distance and initial-plane encounter stretch | m, dimensionless |
| $c_h,k_p,M_p,\mu_w,\alpha_h,\tau_p$ | Sound speed; gel permeability; poroelastic modulus; pore-fluid viscosity; host thermal diffusivity; pulse duration | m/s, m², Pa, Pa s, m²/s, s |

Gel modulus, viscosity, optical cross section, cover, cohesive strength and toughness are stipulated. They are unmeasured for the target formulation. [The source ledger](SOURCES.md) states the support for interface and EOS inputs.

## 3. Numbered derivation

### Step 1 — Define volumes, finite phase inventory and initial reference

**Symbols before Eq. (E01):** $a_0,R,b$ are initial liquid, current outer and vapor-core radii (m), with $0<b<R$; $V_0,V,V_b,V_l$ are corresponding volumes (m³); pi is dimensionless. These are geometric identities for concentric spheres.

$$
V_0=\frac{4\pi a_0^3}{3},\qquad
V=\frac{4\pi R^3}{3},\qquad
V_b=\frac{4\pi b^3}{3},\qquad V_l=V-V_b. \tag{E01}
$$

The last identity subtracts the vapor volume from the whole inclusion. The surviving liquid shell is a separate domain; neither outer volume nor core volume is a PFC mass by itself.

**Symbols before Eq. (E02):** $m,m_l,m_v$ are fixed total, liquid and vapor PFC masses (kg); $\rho_{l0},\rho_l,\rho_v$ are initial liquid and current phase densities (kg/m³); $V_0,V_l,V_b$ are volumes (m³); $x_v$ is the dimensionless vapor mass fraction. Densities and total mass are strictly positive.

$$
\begin{aligned}
m&=\rho_{l0}V_0,\qquad m_l=\rho_lV_l,\qquad m_v=\rho_vV_b,\\
m_l+m_v&=m,\qquad x_v=\frac{m_v}{m},\qquad 0<x_v<1. \tag{E02}
\end{aligned}
$$

The first row defines masses from EOS densities. The second imposes closed PFC inventory and divides by its positive initial mass. A root with negative shell volume or a vapor fraction outside the indicated interval is rejected, even if the nonlinear solver reports convergence.

**Symbols before Eq. (E03):** $p_{l0},p_\infty$ are initial liquid and ambient absolute pressures (Pa); $\gamma_o$ is constant outer tension (N/m); $a_0$ is initial radius (m); $T_0$ is initial temperature (K); $\rho_{l0}$ is initial liquid density (kg/m³); $\rho_l(T,p)$ denotes the liquid EOS density function. The initial gel is unstretched.

$$
p_{l0}=p_\infty+\frac{2\gamma_o}{a_0},\qquad
\rho_{l0}=\rho_l(T_0,p_{l0}). \tag{E03}
$$

The first relation adopts the spherical capillary traction at the initially liquid outer interface. The second evaluates a liquid state at that pressure, rather than using an unrelated gas density. The jump has units N/m divided by m, or Pa, and decreases with increasing radius.

### Step 2 — Use a real-fluid EOS and keep both interfaces distinct

**Symbols before Eq. (E04):** $a_H(T,\rho)$ is specific Helmholtz energy (J/kg); $T$ is temperature (K); $\rho$ is a generic phase density (kg/m³); $p,u,s_H,g$ are pressure (Pa), specific internal energy (J/kg), entropy (J/(kg K)), and chemical potential (J/kg). Partial derivatives are at fixed subscripted variable. These thermodynamic identities are evaluated using the adopted EOS [S2](SOURCES.md).

$$
\begin{aligned}
p&=\rho^2\left(\frac{\partial a_H}{\partial\rho}\right)_T,
&s_H&=-\left(\frac{\partial a_H}{\partial T}\right)_\rho,\\
u&=a_H+Ts_H,
&g&=a_H+\frac{p}{\rho}. \tag{E04}
\end{aligned}
$$

The first row differentiates the Helmholtz representation at its stated independent variables. The second reconstructs internal and Gibbs energies. Pressure divided by density has unit J/kg, so the Gibbs expression is dimensionally consistent. Both phases use the same energy reference. No constant ideal-gas exponent or separately fitted pressure pulse appears.

**Symbols before Eq. (E05):** $p_v,p_l$ are vapor and liquid absolute pressures (Pa); $g_v,g_l$ are vapor and liquid chemical potentials (J/kg); $\gamma_i$ is constant inner tension (N/m); $b$ is positive vapor-core radius (m); $T$ is uniform temperature (K). Equal temperature and instantaneous phase equilibrium are adopted constitutive approximations; interfaces are spherical.

$$
p_v-p_l=\frac{2\gamma_i}{b},\qquad g_l(T,p_l)=g_v(T,p_v). \tag{E05}
$$

The capillary relation uses the **inner** liquid/gas interface. Chemical equilibrium equates chemical potential at the different phase pressures; it does not replace either pressure by a flat-interface saturation value. Using 0.072 N/m water/gas tension for every interface would change the problem. A very small core also raises the capillary jump; continuum curvature and constant tension become uncertain at molecular scales.

### Step 3 — Derive the intact spherical gel resistance

**Symbols before Eq. (E06):** $s,r$ are positive reference and current host radial coordinates (m); $R,a_0$ are current and initial inclusion radii (m); $C$ is the volume-offset parameter (m³); $\lambda_r,\lambda_\theta$ are dimensionless radial/circumferential stretches; $d r/d s$ is the radial derivative. Incompressible spherical motion and $r\ge R$ are assumed.

$$
\begin{aligned}
r^3-R^3&=s^3-a_0^3,\qquad C=R^3-a_0^3,\\
r^3&=s^3+C,\qquad 3r^2\frac{dr}{ds}=3s^2,\\
\lambda_r&=\frac{dr}{ds}=\frac{s^2}{r^2},\qquad
\lambda_\theta=\frac{r}{s},\qquad
\lambda_r\lambda_\theta^2=1. \tag{E06}
\end{aligned}
$$

The first row conserves host volume between inner and any outer material sphere. The second collects constants and differentiates with respect to reference radius. Division by positive squared radius yields the third row, which verifies unit volume ratio explicitly.

**Symbols before Eq. (E07):** $\sigma_{rr},\sigma_{\theta\theta},\chi,G$ are elastic radial stress, tangential stress, incompressibility multiplier and positive shear modulus (Pa); $\lambda_r,\lambda_\theta$ are dimensionless stretches from Eq. (E06); $r$ is current radius (m); $d/dr$ is spatial differentiation. This is the incompressible neo-Hookean constitutive control and elastic radial equilibrium.

$$
\sigma_{rr}=-\chi+G\lambda_r^2,\qquad
\sigma_{\theta\theta}=-\chi+G\lambda_\theta^2,\qquad
\frac{d\sigma_{rr}}{dr}=-\frac{2(\sigma_{rr}-\sigma_{\theta\theta})}{r}. \tag{E07}
$$

The first two expressions declare the host material law. Their subtraction eliminates the unknown multiplier. The last relation is the spherically symmetric divergence of elastic stress, used to obtain the elastic traction component; inertia and viscosity are added separately below.

**Symbols before Eq. (E08):** $p_{el}$ is elastic wall resistance (Pa); $G$ is shear modulus (Pa); $R,a_0,r,s$ are radii (m); $\beta=s/r$ is dimensionless; $C=R^3-a_0^3$ is positive during expansion (m³); $\int$ denotes definite spatial integration. Upper endpoint infinity means an effectively infinite host. At exactly $R=a_0$, resistance follows by continuity.

$$
\begin{aligned}
p_{el}
&=2G\int_R^\infty\left[\left(\frac r s\right)^2-\left(\frac s r\right)^4\right]\frac{dr}{r},\\
\beta^3&=1-\frac C{r^3},\qquad
3\beta^2\,d\beta=\frac{3C}{r^4}\,dr,\qquad
\frac{dr}{r}=\frac{\beta^2}{1-\beta^3}\,d\beta,\\
p_{el}
&=2G\int_{a_0/R}^{1}\frac{1-\beta^6}{1-\beta^3}\,d\beta
=2G\int_{a_0/R}^{1}(1+\beta^3)\,d\beta,\\
p_{el}
&=2G\left[\beta+\frac{\beta^4}{4}\right]_{a_0/R}^{1}
=\frac G2\left[5-4\frac{a_0}{R}-\left(\frac{a_0}{R}\right)^4\right]. \tag{E08}
\end{aligned}
$$

Integrating Eq. (E07) with the far stress condition gives the first row. Eq. (E06) gives the variable transformation and its Jacobian. At the inner boundary the ratio is the initial/current inclusion radius; at infinity it tends to one. Factoring the numerator as the product of one minus the cube and one plus the cube permits cancellation for every finite radius in expansion; the endpoint integral has a removable limiting value. The final row evaluates both endpoints. This derivation makes the geometry assumption visible; it is not a planar-layer fracture law.

**Symbols before Eq. (E09):** $E_{gel}$ is recoverable gel strain energy (J); $p_{el}$ is resistance (Pa); $R,a_0,\xi$ are current, initial and dummy radii (m); $G$ is shear modulus (Pa); $dE_{gel}/dR$ is the radius derivative. All integrals are along the reversible intact branch. $\pi$ is the dimensionless circle constant.

$$
\begin{aligned}
E_{gel}
&=\int_{a_0}^{R}4\pi\xi^2p_{el}(\xi)\,d\xi\\
&=2\pi G\int_{a_0}^{R}(5\xi^2-4a_0\xi-a_0^4\xi^{-2})\,d\xi\\
&=2\pi G\left[\frac{5\xi^3}{3}-2a_0\xi^2+\frac{a_0^4}{\xi}\right]_{a_0}^{R}\\
&=2\pi G\left[\frac{5R^3}{3}-2a_0R^2+\frac{a_0^4}{R}-\frac{2a_0^3}{3}\right],\\
\frac{dE_{gel}}{dR}&=4\pi R^2p_{el}(R). \tag{E09}
\end{aligned}
$$

The first row defines work as pressure times incremental cavity volume. The second substitutes Eq. (E08) and expands. Integrating each power gives the third row; evaluating the initial endpoint yields the constant in the fourth. Differentiation verifies the last identity independently and is also checked symbolically by the audit script.

**Symbols before Eq. (E10):** $\lambda=R/a_0$ is stretch; $\epsilon$ is small dimensionless stretch excess; $p_{el}$ is resistance (Pa); $E_{gel}$ is strain energy (J); $G$ is modulus (Pa); $a_0$ is radius (m); $O$ denotes the asymptotic remainder order as excess tends to zero. $\pi$ is the dimensionless circle constant.

$$
\begin{aligned}
\lambda=1:&\quad p_{el}=0,\quad E_{gel}=0,\\
\lambda\to\infty:&\quad p_{el}\to\frac{5G}{2},\\
\lambda=1+\epsilon:&\quad p_{el}=4G\epsilon+O(\epsilon^2),\qquad
E_{gel}=8\pi G a_0^3\epsilon^2+O(\epsilon^3). \tag{E10}
\end{aligned}
$$

The zero-stretch results follow by direct substitution into Eqs. (E08)–(E09). Letting the radius ratios tend to zero gives the large-stretch elastic limit. Expanding reciprocal stretch and its fourth power to first order gives the pressure expansion; integrating its product with the leading cavity-volume derivative gives the energy expansion. The large-stretch pressure limit is a property of this intact neo-Hookean model; it is **not** a rupture pressure for a real hydrogel.

### Step 4 — Obtain host inertia and viscous dissipation

**Symbols before Eq. (E11):** $u_h(r,t)$ is radial host speed (m/s); $R,r$ are inclusion and host radii (m); $W$ is inner-wall speed (m/s); $\rho_h$ is host density (kg/m³); $K_h$ is host kinetic energy (J); $\int$ is spatial integration over an effectively infinite incompressible host. $\pi$ is the dimensionless circle constant.

$$
\begin{aligned}
4\pi r^2u_h&=4\pi R^2W,\qquad u_h=\frac{R^2W}{r^2},\\
K_h&=\frac{\rho_h}{2}\int_R^\infty u_h^2\,4\pi r^2\,dr\\
&=2\pi\rho_hR^4W^2\int_R^\infty r^{-2}\,dr
=2\pi\rho_hR^3W^2. \tag{E11}
\end{aligned}
$$

Incompressibility gives the first flux relation; division by positive area gives velocity. Substituting velocity squared in kinetic energy cancels two radius powers. The antiderivative of inverse squared radius is minus inverse radius, whose far endpoint is zero and inner endpoint contributes inverse inclusion radius. This retains host inertia but omits liquid-shell inertia, which must be tested in the full spatial model.

**Symbols before Eq. (E12):** $D_{rr},D_{\theta\theta}$ are host radial/tangential deformation rates (1/s); $u_h$ is radial speed (m/s); $r,R$ are radii (m); $W$ is wall speed (m/s); $\eta$ is effective viscosity (Pa s); $P_{dis}$ is viscous-loss power (W); $p_{vis}$ is viscous wall resistance (Pa). There are two equal tangential components. $\pi$ is the dimensionless circle constant.

$$
\begin{aligned}
D_{rr}&=\frac{\partial u_h}{\partial r}=-\frac{2R^2W}{r^3},\qquad
D_{\theta\theta}=\frac{u_h}{r}=\frac{R^2W}{r^3},\\
P_{dis}&=\int_R^\infty 2\eta(D_{rr}^2+2D_{\theta\theta}^2)\,4\pi r^2\,dr\\
&=48\pi\eta R^4W^2\int_R^\infty r^{-4}\,dr
=16\pi\eta R W^2,\\
p_{vis}&=\frac{P_{dis}}{4\pi R^2W}=\frac{4\eta W}{R}\quad(W\ne0),
\qquad p_{vis}=0\quad(W=0). \tag{E12}
\end{aligned}
$$

Differentiate Eq. (E11) and divide its velocity by radius for the first row. Squaring and summing the three deformation-rate components yields six equal factors; the integral of inverse fourth power contributes inverse cubed radius divided by three. Dividing loss power by signed volume flux gives viscous traction when speed is nonzero; its continuous zero-speed limit avoids division by zero. Loss power stays nonnegative in either motion direction.

**Symbols before Eq. (E13):** $R,W$ are radius and speed (m, m/s); $\rho_h$ is density (kg/m³); $p_l,p_\infty,p_{el},p_{vis},p_{need}$ are pressures (Pa); $\gamma_o$ is outer tension (N/m); dots are time derivatives. The radial momentum equation is the adopted incompressible host approximation.

$$
\begin{aligned}
p_{need}&=p_\infty+p_{el}+\frac{2\gamma_o}{R},\\
\dot R&=W,\qquad
\rho_h\left(R\dot W+\frac32W^2\right)=p_l-p_{need}-p_{vis},\\
\dot W&=\frac{1}{R}\left[\frac{p_l-p_{need}-4\eta W/R}{\rho_h}-\frac32W^2\right]. \tag{E13}
\end{aligned}
$$

The first row collects static ambient, elastic and outer capillary resistance. The second is spherical inertia driven by the remaining traction. Dividing by positive density and radius, and substituting Eq. (E12), gives the third. Each side of the momentum equation is Pa. A positive excess traction gives positive acceleration at zero initial speed. With zero elasticity and viscosity the equation reduces to the capillary spherical-inertia control, not a directional-jet model.

### Step 5 — Account for PFC internal, interface, gel, ambient and kinetic energy

**Symbols before Eq. (E14):** $U_{PFC},E_{surf},E_{amb}$ are internal energy, interface-energy change and ambient work (J); $m_l,m_v$ are phase masses (kg); $u_l,u_v$ are phase internal energies (J/kg); $\gamma_o,\gamma_i$ are distinct constant tensions (N/m); $R,a_0,b$ are radii (m); $p_\infty$ is ambient pressure (Pa); $V,V_0$ are inclusion volumes (m³). Initial internal energy is referenced separately below. $\pi$ is the dimensionless circle constant.

$$
U_{PFC}=m_lu_l+m_vu_v,\qquad
E_{surf}=4\pi[\gamma_o(R^2-a_0^2)+\gamma_i b^2],\qquad
E_{amb}=p_\infty(V-V_0). \tag{E14}
$$

Internal energy includes phase conversion through the actual phase energies. Adding a second independent latent-heat term would double count it. The initial state has the outer liquid surface but no vapor core; the inner surface energy is therefore all new. Both surface terms have units N/m times m², or J. Constant tension assumes negligible interface entropy and ignores shell/coating rearrangement.

**Symbols before Eq. (E15):** $U_{PFC}$ is PFC internal energy (J); $T$ is common phase temperature (K); $S$ is total PFC entropy (J/K); $g_l,g_v$ are phase chemical potentials (J/kg); $m_l,m_v$ are masses (kg); $p_l,p_v$ are pressures (Pa); $V_l,V_b,V$ are phase/total volumes (m³); $\gamma_i$ is constant inner tension (N/m); $A_i=4\pi b^2$ is core area (m²); $d$ is a differential along an admissible equilibrium trajectory. $b$ is the positive core radius (m).

$$
\begin{aligned}
dU_{PFC}&=T\,dS-p_l\,dV_l-p_v\,dV_b+g_l\,dm_l+g_v\,dm_v,\\
dm_l&=-dm_v,\quad g_l=g_v,\quad dV_l=dV-dV_b,\\
dU_{PFC}&=T\,dS-p_l\,dV-(p_v-p_l)\,dV_b,\\
\gamma_i\,dA_i&=\frac{2\gamma_i}{b}\,dV_b=(p_v-p_l)\,dV_b,\\
d(U_{PFC}+\gamma_i A_i)&=T\,dS-p_l\,dV. \tag{E15}
\end{aligned}
$$

The first row applies the thermodynamic fundamental relation to each phase and sums them. Closed mass and Eq. (E05) cancel the chemical terms; volume subtraction yields the third row. Differentiating core area and volume gives their ratio of two divided by core radius; Eq. (E05) then cancels the inner traction work with surface-energy change. The last relation explains why a curved core's interface energy belongs in the conserved total. For reversible, insulated phase adjustment, the temperature–entropy term is zero. The audit checks entropy drift without imposing an entropy equation.

**Symbols before Eq. (E16):** $E_{seed}$ is retained seed energy relative to the all-liquid reference (J), under lossless seed preparation; $m$ is fixed PFC mass (kg); $u_{l0}$ is initial liquid internal energy (J/kg); $U_{PFC},E_{gel},E_{surf},E_{amb},K_h,D_h$ are PFC, gel, interface, ambient, kinetic and loss energies (J); $t,t'$ are end and dummy time (s), with the prime a label; $P_{dis}$ is loss power (W); $\epsilon_E$ is dimensionless. This is an insulated post-seed control; no later heat source or outflow exists.

$$
\begin{aligned}
D_h(t)&=\int_0^t P_{dis}(t')\,dt',\qquad \dot D_h=P_{dis},\\
E_{seed}&=U_{PFC}-m u_{l0}+E_{gel}+E_{surf}+E_{amb}+K_h+D_h,\\
\epsilon_E&=\frac{U_{PFC}-m u_{l0}+E_{gel}+E_{surf}+E_{amb}+K_h+D_h-E_{seed}}{E_{seed}}. \tag{E16}
\end{aligned}
$$

The first row defines cumulative host loss. The second is the retained-seed-energy balance relative to the all-liquid reference. The last defines its numerical residual for positive retained seed energy. Equality with experimentally absorbed laser energy would additionally require accounting for pre-seed conduction, host dissipation, acoustic emission, and heat delivered to other materials. They are absent from the preparation control; the calculated budget is not an activation threshold. Gel dissipation is included as energy transferred into unrecovered host heating; it is not also fed back into PFC heat. These controls neglect heat conduction between host and PFC.

**Symbols before Eq. (E17):** $K_h$ is host kinetic energy (J); $\rho_h$ is density (kg/m³); $R,W$ are radius and speed (m, m/s); $p_l,p_\infty,p_{el},p_{vis}$ are pressures (Pa); $\gamma_o$ is outer tension (N/m); dots indicate time derivatives. The power calculation applies along Eq. (E13). $\pi$ is the dimensionless circle constant.

$$
\begin{aligned}
\dot K_h&=2\pi\rho_h[3R^2W^3+2R^3W\dot W]\\
&=4\pi R^2W\rho_h\left[R\dot W+\frac32W^2\right]\\
&=4\pi R^2W\left[p_l-p_\infty-p_{el}-\frac{2\gamma_o}{R}-p_{vis}\right]. \tag{E17}
\end{aligned}
$$

Differentiate Eq. (E11) using the product rule and Eq. (E13)'s radius derivative. Factor the common volume flux and substitute momentum. Eq. (E09) removes elastic power, differentiation of Eq. (E14) removes ambient and outer surface power, and Eq. (E12) removes viscous power in the derivative of Eq. (E16). Eq. (E15) removes the remaining PFC/core-interface power. Thus the adopted dynamics are consistent with the stated first law. Symbolic differentiation verifies the first two rows; native/reference comparisons verify implementation, not the omitted physics.

### Step 6 — Write the stationary and transient closures

**Symbols before Eq. (E18):** $R,b$ are prescribed outer/unknown core radii (m); $T$ is common unknown temperature (K); $\rho_l,\rho_v$ are unknown densities (kg/m³); $p(T,\rho),g(T,\rho)$ are EOS pressure and chemical-potential functions (Pa, J/kg); $p_{need}$ is static required liquid pressure (Pa); $\gamma_i$ is inner tension (N/m); $V,V_b$ are volumes (m³); $m$ is fixed mass (kg). The root must satisfy positive phase compressibility and valid inventory.

$$
\begin{cases}
p(T,\rho_l)-p_{need}=0,\\
p(T,\rho_v)-p(T,\rho_l)-2\gamma_i/b=0,\\
g(T,\rho_l)-g(T,\rho_v)=0,\\
\rho_l(V-V_b)+\rho_vV_b-m=0.
\end{cases} \tag{E18}
$$

These four equations determine temperature, densities and core radius at prescribed stretch. They establish a static phase root. Stability and nucleation-barrier crossing require separate tests. Eq. (E16) gives state energy with zero kinetic energy and loss. Native stationary solves use perturbed initial guesses and solve all four equations.

**Symbols before Eq. (E19):** $R,W,D_h$ are radius, speed and accumulated loss (m, m/s, J). Dots denote time derivatives. $T$ is temperature (K); $\rho_l,\rho_v,\rho_h$ are liquid, vapor and host densities (kg/m³); $b$ is core radius (m). $p_l,p_{need}$ are pressures (Pa); $\eta$ is viscosity (Pa s); $\gamma_i$ is inner tension (N/m). $p(T,\rho)$ and $g(T,\rho)$ are EOS pressure (Pa) and chemical potential (J/kg), with $\rho$ the density argument (kg/m³). $V,V_b$ are inclusion/core volumes (m³); $m$ is fixed mass (kg). $U_{PFC},E_{gel},E_{surf},E_{amb},K_h,E_{seed}$ are internal, gel, surface, ambient, kinetic and seed energies (J). $u_{l0}$ is initial liquid specific internal energy (J/kg). $\pi$ is the dimensionless circle constant. $R,b,\rho_h$ are positive; phases remain admissible.

$$
\begin{aligned}
\dot R&=W,\\
\dot W&=\frac{(p_l-p_{need}-4\eta W/R)/\rho_h-3W^2/2}{R},\\
\dot D_h&=16\pi\eta R W^2,\\
0&=p(T,\rho_v)-p(T,\rho_l)-2\gamma_i/b,\\
0&=g(T,\rho_l)-g(T,\rho_v),\\
0&=\rho_l(V-V_b)+\rho_vV_b-m,\\
0&=U_{PFC}-m u_{l0}+E_{gel}+E_{surf}+E_{amb}+K_h+D_h-E_{seed}.
\tag{E19}
\end{aligned}
$$

The first three equations are radius, momentum and cumulative loss. Inner traction, phase equilibrium, mass and total energy supply four algebraic conditions. The native model has seven normalized Global Equations variables. The Python solver independently eliminates the four algebraic unknowns with a thermodynamic root and integrates three differential states. This is a solver-formulation comparison on the same constitutive assumptions; it is not an independent empirical theory.

**Symbols before Eq. (E20):** $p_s,U_s,\tau,E_s$ are positive pressure, speed, time and energy scales (Pa, m/s, s, J). $\rho_h,a_0,m$ are positive host density, initial radius and PFC mass (kg/m³, m, kg). $\theta,\lambda,\widehat W,\widehat D$ are dimensionless time, radius, speed and loss; hats label normalized quantities. $t,R,W,D_h$ are dimensional time, radius, speed and loss (s, m, m/s, J). $p_l,p_{need}$ are pressures (Pa); $\eta$ is viscosity (Pa s). $d/d\theta$ is differentiation in normalized time. The square root is the positive branch; $\lambda>0$ permits division.

$$
\begin{aligned}
U_s&=\sqrt{p_s/\rho_h},\quad \tau=a_0/U_s,\quad E_s=m(10^5\ {\rm J/kg}),\\
\theta&=t/\tau,\quad\lambda=R/a_0,\quad\widehat W=W/U_s,\quad\widehat D=D_h/E_s,\\
\frac{d\lambda}{d\theta}&=\widehat W,\\
\frac{d\widehat W}{d\theta}
&=\frac1\lambda\left[\frac{p_l-p_{need}}{p_s}
-4\frac{\eta}{a_0\sqrt{\rho_h p_s}}\frac{\widehat W}{\lambda}
-\frac32\widehat W^2\right]. \tag{E20}
\end{aligned}
$$

The first two rows define scales and variables. The chain rule gives the third. Substitute dimensional radius and speed into Eq. (E13), multiply by the time/speed scale, and use the squared speed definition to divide all driving pressures by the pressure scale. The dimensionless coefficient of viscous resistance is therefore inversely proportional to initial radius at fixed viscosity and pressure scale. A square root of positive pressure/density is valid and gives speed units.

### Step 7 — Test stability under the stated thermal constraint

**Symbols before Eq. (E21):** $\lambda$ is stretch; $\epsilon$ is a small dimensionless perturbation; $p_l(\lambda;E)$ is the liquid pressure from closed total-energy phase closure with a fixed energy label $E$ (J); $p_{need}(\lambda)$ is static required pressure (Pa); $k_E$ is closed-energy pressure-restoration derivative (Pa per stretch). The center state is an admissible stationary root and the neighboring phase roots must remain admissible.

$$
k_E=-\left.\frac{d[p_l(\lambda;E)-p_{need}(\lambda)]}{d\lambda}\right|_E
\approx-\frac{[p_l-p_{need}]_{\lambda+\epsilon,E}-[p_l-p_{need}]_{\lambda-\epsilon,E}}{2\epsilon}. \tag{E21}
$$

A positive slope restores radial perturbations. Increased radius receives inward imbalance; decreased radius receives outward imbalance. A negative slope is locally unstable. Recompute phase and energy roots at stretch offsets 0.0001 and 0.00005. Keep both neighboring states admissible. Step 11 tests internal phase/core variations separately. Nonspherical stability is **not established**. The fixed-temperature derivative $k_T$ (Pa per stretch) holds temperature instead of energy. Of 132 sampled states, 36 are non-restoring at closed energy and 94 at fixed temperature.

### Step 8 — Keep optical heating and nucleation as separate measurable gates

**Symbols before Eq. (E22):** $F_{loc}$ is local fluence (J/m²); $C_{abs}$ is effective absorption cross section (m²); $f_t(t)$ is nonnegative pulse shape (1/s); $t$ is time (s); $P_{abs}(t)$ is absorbed power (W); $E_{abs}$ is absorbed energy (J). The time integral of pulse shape is unity. Subscript `abs` labels absorbed energy/power, not an experimentally known coefficient.

$$
\int f_t(t)\,dt=1,\qquad
P_{abs}(t)=F_{loc}C_{abs}f_t(t),\qquad
E_{abs}=\int P_{abs}(t)\,dt=F_{loc}C_{abs}. \tag{E22}
$$

Substitute the power expression in the energy integral and take the fixed fluence/cross section outside the integral. The normalization gives the final identity. A projected-disk comparison divides cross section by the positive area $\pi a_0^2$ (m²); it is an effective geometric ratio, not automatically an absorption fraction bounded by one. Absorber cross section, loading, heat delivered to PFC versus water, and fluence attenuation with embedding depth must be measured. The seed's retained energy cannot replace these measurements.

**Symbols before Eq. (E23):** $\Delta\mathcal G(r_n)$ is nucleus formation free energy (J); $r_n$ is trial vapor-nucleus radius (m); $\gamma_i$ is liquid/vapor tension (N/m); $\Delta p>0$ is the pressure driving difference for a metastable-liquid nucleation approximation (Pa); $r_*$ is critical nucleus radius (m); $\Delta\mathcal G_*$ is critical barrier (J). This is the classical homogeneous, spherical, constant-tension approximation; it does not describe an absorber's heterogeneous nucleation site. $\pi$ is the dimensionless circle constant.

$$
\begin{aligned}
\Delta\mathcal G(r_n)&=4\pi\gamma_i r_n^2-\frac{4\pi}{3}\Delta p\,r_n^3,\\
\frac{d\Delta\mathcal G}{dr_n}&=8\pi\gamma_i r_n-4\pi\Delta p\,r_n^2
=4\pi r_n(2\gamma_i-\Delta p\,r_n),\\
r_*&=\frac{2\gamma_i}{\Delta p},\qquad
\left.\frac{d^2\Delta\mathcal G}{dr_n^2}\right|_{r_*}=-8\pi\gamma_i<0,\\
\Delta\mathcal G_*&=4\pi\gamma_i\frac{4\gamma_i^2}{\Delta p^2}
-\frac{4\pi}{3}\Delta p\frac{8\gamma_i^3}{\Delta p^3}
=\frac{16\pi\gamma_i^3}{3\Delta p^2}. \tag{E23}
\end{aligned}
$$

The first row adopts surface cost minus pressure-volume gain. Differentiate explicitly, factor, and solve the positive-radius stationary branch. The zero-radius branch is the initial boundary state, not a critical finite nucleus. The negative second derivative establishes a barrier maximum. Substituting the critical radius yields the last row. The pressure difference must be computed from the actual metastable liquid state and phase driving chemical potential, not from ambient boiling temperature alone. Nonpositive driving pressure has no positive critical radius in this approximation. Neither the heterogeneous site factor nor a kinetic prefactor is calibrated here.

**Symbols before Eq. (E24):** $\mathcal P$ is activation probability; $J_n(T,p_l)$ is a nucleation-rate density (1/(m³ s)); $V_l(t)$ is liquid volume (m³); $t,t'$ are end and dummy times (s); $T$ is local temperature (K); $p_l$ is liquid pressure (Pa); $\mathbf x$ is spatial position (m); $\Omega_l(t)$ is the liquid domain; $dV$ is volume measure (m³); exp is the exponential of a dimensionless argument. This is a Poisson-hazard hypothesis for independent nucleation events. The second equality requires a spatially uniform rate within the liquid.

$$
\begin{aligned}
\mathcal P(t)&=1-\exp\left[-\int_0^t\int_{\Omega_l(t')}J_n(T(\mathbf x,t'),p_l(\mathbf x,t'))\,dV\,dt'\right],\\
&=1-\exp\left[-\int_0^t J_n(T(t'),p_l(t'))V_l(t')\,dt'\right]\quad\text{(uniform-rate control)}. \tag{E24}
\end{aligned}
$$

The hazard is dimensionless and nonnegative. Probability therefore lies between zero and one. Heterogeneous nucleation needs a site or area hazard with matching units. **Unresolved:** absorber/site distribution, kinetic prefactor and temperature history. Activation thresholds are **not established**. Measure activation fractions versus fluence with no-droplet and no-absorber controls.

### Step 9 — Require fracture work and a hydraulic connection before exterior ejection

**Symbols before Eq. (E25):** $\mathcal G_f$ is energy release rate (J/m²); $\Pi$ is appropriate mechanical potential energy (J); $A_c$ is projected crack advance area (m²); $G_c$ is critical fracture energy (J/m²). The derivative is under the stated mechanical loading constraint; temperature, rate and hydration affect material toughness.

$$
\mathcal G_f=-\frac{d\Pi}{dA_c},\qquad
\mathcal G_f\ge G_c\quad\hbox{is an energetic propagation condition}. \tag{E25}
$$

The energy condition leaves crack initiation, path, aperture and filling unresolved. Fixed-pressure and closed-energy loading give different release rates. Measure toughness and strength independently of modulus. These native controls contain no damage law.

**Symbols before Eq. (E26):** $t_c(\delta)$ is cohesive normal traction (Pa); $\delta$ is opening (m); $t_m>0$ is peak traction (Pa); $0<\delta_0<\delta_f$ are opening at peak and final separation (m); $G_c$ is fracture energy per projected crack area including both fracture faces (J/m²); $d\delta$ is the opening measure. This is an example bilinear cohesive constitutive law, requiring calibration.

$$
\begin{aligned}
t_c(\delta)&=\begin{cases}
t_m\delta/\delta_0,&0\le\delta\le\delta_0,\\
t_m(\delta_f-\delta)/(\delta_f-\delta_0),&\delta_0<\delta\le\delta_f,\\
0,&\delta>\delta_f,
\end{cases}\\
G_c&=\int_0^{\delta_f}t_c(\delta)\,d\delta
=\frac{t_m\delta_0}{2}+\frac{t_m(\delta_f-\delta_0)}2
=\frac{t_m\delta_f}{2},\\
\delta_f&=\frac{2G_c}{t_m}. \tag{E26}
\end{aligned}
$$

Integrate the rising linear segment as one triangle and the falling segment as the second. Their base lengths sum to final opening, so peak-opening displacement cancels from total work. Division by positive peak strength gives final separation. The relation has units J/m² divided by Pa, or m. Toughness alone cannot set peak traction or initial cohesive stiffness. Official COMSOL examples describe this implementation route [S10](SOURCES.md); no target gel values are supplied here.

**Symbols before Eq. (E27):** $h$ is cover thickness from the **initial** droplet surface to the gel free surface (m); $a_c$ is assumed rectangular slit half-width (m); $A_c$ is slit projected crack area (m²); $G_c$ is fracture energy including both faces (J/m²); $E_{cr}$ is fracture-work estimate (J); $E_{seed}$ is retained seed energy (J). This idealized slit geometry and retained-seed-energy-only allocation are stipulated screens, not a computed crack path or universal fracture-energy bound.

$$
\begin{aligned}
A_c&=2a_ch,\qquad E_{cr}=G_cA_c=2G_ca_ch,\\
E_{seed}<E_{cr}&\ \Longrightarrow\ \hbox{slit work exceeds retained seed energy alone}. \tag{E27}
\end{aligned}
$$

Slit length times width gives projected area. Area times toughness gives work. Compare that work with the assigned retained seed energy. Fracture impossibility is **not established**. Cooling can reduce PFC internal energy; changing topology can release interface energy. An upper bound needs all other reference-energy changes to be nonnegative, or an endpoint-specific available-energy calculation. Neither condition is established here. Flaws, path length, width, prestress and later heat also affect the budget. Passing this screen leaves initiation, connection, aperture and liquid supply unresolved. Cover affects the assumed slit cost; the trajectory still uses an infinite host. Define center-to-surface distance $d=a_0+h$ (m). Define encounter stretch $\lambda_{surface}=d/a_0$ (dimensionless). At $R\ge d$, the inclusion intersects the initial surface plane. Smaller standoff still requires finite-domain convergence. A 3 µm radius under 1 µm cover gives encounter stretch 1.333, below 2.1.

### Step 10 — Check length/time regimes and distinguish velocities/pressures

**Symbols before Eq. (E28):** $G,\eta$ are shear modulus and viscosity (Pa, Pa s); $a_0$ is positive initial radius (m); $\gamma_o$ is positive outer tension (N/m); $\rho_h,p_s$ are positive host density and pressure scale (kg/m³, Pa); $\alpha_h$ is host thermal diffusivity (m²/s); $\tau_p$ is pulse duration (s); $W,c_h$ are radial speed and positive sound speed (m/s). Vertical bars mean absolute value. The square root takes its positive branch. Every ratio is dimensionless.

$$
\frac{Ga_0}{\gamma_o},\qquad
\frac{\eta}{a_0\sqrt{\rho_h p_s}},\qquad
\frac{\alpha_h\tau_p}{a_0^2},\qquad
\frac{|W|}{c_h}. \tag{E28}
$$

The first compares elastic and capillary pressure scales. The second is the coefficient derived in Eq. (E20). The third is a host thermal Fourier number; a small value during a pulse means heat is spatially confined, **not** that the PFC is thermally uniform. The fourth screens compressible effects in radial motion. The delivered controls use a declared Mach limit of 0.1; full pressure-wave and collapse predictions require compressible spatial conservation with appropriate fluid EOS and sensor location/bandwidth.

**Symbols before Eq. (E29):** $\tau_{poro}$ is a pore-pressure diffusion timescale (s); $\mu_w$ is pore-fluid viscosity (Pa s); $L_h$ is the relevant drainage distance (m); $k_p$ is permeability (m²); $M_p$ is poroelastic modulus (Pa). This is a dimensional poroelastic diffusion estimate; these target inputs are not measured here.

$$
\tau_{poro}\sim\frac{\mu_w L_h^2}{k_p M_p}. \tag{E29}
$$

The diffusivity scale is permeability times modulus divided by fluid viscosity; dividing squared drainage length by that diffusivity gives time. Compare the event duration with this timescale before retaining an undrained host. The relevant distance is the local drainage path, not automatically the laser spot or gel thickness. Particularly for nanoscale cavities, choosing a permeability without measurement can invalidate the intact undrained approximation.

Radial wall speed, liquid velocity in a connected outlet, and an internal collapse microjet speed are different observables even though all have speed units. Source pressure, elastic resistance, dynamic pressure, pressure at a target and pressure at a finite-bandwidth sensor are also different observables. A perfectly spherical isolated model cannot generate directional jet momentum. The original 1.625 m/s outlet result cannot be reassigned to the radial speeds in this study or used as a collapse speed. A water-hammer pressure scale is not a measured peak; compressibility, contact duration, geometry and receiver response determine the actual pressure trace.

### Step 11 — Check internal core/phase stability at fixed temperature, volume and mass

**Symbols before Eq. (E30):** $T$ is fixed uniform temperature (K); $V$ is fixed inclusion volume (m³); $m$ is fixed PFC mass (kg). Independent coordinates are vapor volume $q=V_b$ (m³) and vapor mass $n=m_v$ (kg), with $0<q<V$ and $0<n<m$. Liquid volume is $V_l=V-q$ (m³); liquid mass is $m_l=m-n$ (kg). Phase densities are $\rho_l=m_l/V_l$ and $\rho_v=n/q$ (kg/m³). Core radius is $b=(3q/(4\pi))^{1/3}$ (m). $F$ is internal Helmholtz energy including the core surface (J); $a_H(T,\rho)$ is specific Helmholtz energy (J/kg); $\gamma_i$ is constant inner tension (N/m); $\pi$ is the circle constant. Outer surface, gel and ambient terms are constant at fixed outer volume.

$$
F(q,n)=m_l a_H(T,\rho_l)+n a_H(T,\rho_v)+4\pi\gamma_i b^2. \tag{E30}
$$

For each phase, the fixed-temperature differential is chemical potential times mass change minus pressure times volume change. Define $g_l,g_v$ (J/kg) and $p_l,p_v$ (Pa) as phase chemical potentials and pressures; subscripts $n,q$ on $F$ denote partial derivatives with respect to those coordinates at fixed other coordinates. Liquid mass and volume changes are the negatives of the vapor changes. Therefore $F_n=g_v-g_l$ (J/kg) and $F_q=p_l-p_v+2\gamma_i/b$ (Pa). Both vanish at the adopted curved-equilibrium root.

**Symbols before Eq. (E31):** $F$ is internal Helmholtz energy (J); subscripts $n,q$ denote partial derivatives in vapor mass $n$ (kg) and volume $q$ (m³), holding other coordinates fixed. $T$ is fixed temperature (K). $p_l,p_v$ are phase pressures (Pa); $\rho_l,\rho_v$ are phase densities (kg/m³); $V_l=V-q$ is liquid volume (m³). $K_l=(\partial p_l/\partial\rho_l)_T$ and $K_v=(\partial p_v/\partial\rho_v)_T$ are positive pressure-density slopes (Pa m³/kg). $\kappa_l=K_l/V_l$ and $\kappa_v=K_v/q$ are scaled slopes (Pa/kg). $\gamma_i$ is inner tension (N/m); $b$ is core radius (m); $\pi$ is the circle constant. At fixed temperature, $dg=dp/\rho$. Density derivatives are $\partial_n\rho_l=-1/V_l$, $\partial_n\rho_v=1/q$, $\partial_q\rho_l=\rho_l/V_l$ and $\partial_q\rho_v=-\rho_v/q$. Mass derivatives have units m^-3. Volume derivatives have units kg/m^6.

$$
\begin{aligned}
F_{nn}&=\frac{\kappa_l}{\rho_l}+\frac{\kappa_v}{\rho_v},
&F_{nq}&=-(\kappa_l+\kappa_v),\\
F_{qq}&=\rho_l\kappa_l+\rho_v\kappa_v-\frac{\gamma_i}{2\pi b^4},
&\frac{d(2\gamma_i/b)}{dq}&=-\frac{2\gamma_i}{b^2}\frac{1}{4\pi b^2}.
\tag{E31}
\end{aligned}
$$

The surface derivative uses $dq/db=4\pi b^2$. Positive pressure-density slopes give $F_{nn}>0$. Mass curvature has units J/kg²; mixed curvature has units Pa/kg; volume curvature has units Pa/m³. For a symmetric Hessian with positive mass curvature, positive definiteness requires a positive Schur complement. **Symbols before Eq. (E32):** $H_{core}$ is that complement (Pa/m³); $F_{qq},F_{nq},F_{nn}$ are volume, mixed and mass curvatures (Pa/m³, Pa/kg, J/kg²). $\kappa_l,\kappa_v$ are positive scaled pressure-density slopes (Pa/kg); $\rho_l,\rho_v$ are phase densities (kg/m³); $\gamma_i$ is inner tension (N/m); $b$ is positive core radius (m); $\pi$ is the dimensionless circle constant. The test holds temperature, total volume and total mass fixed.

$$
\begin{aligned}
H_{core}&=F_{qq}-\frac{F_{nq}^2}{F_{nn}}\\
&=\rho_l\kappa_l+\rho_v\kappa_v
-\frac{\rho_l\rho_v(\kappa_l+\kappa_v)^2}{\kappa_l\rho_v+\kappa_v\rho_l}
-\frac{\gamma_i}{2\pi b^4}\\
&=\frac{\kappa_l\kappa_v(\rho_l-\rho_v)^2}
{\kappa_l\rho_v+\kappa_v\rho_l}-\frac{\gamma_i}{2\pi b^4}. \tag{E32}
\end{aligned}
$$

Use the positive common denominator for the bulk terms. Squared $\kappa_l$ and $\kappa_v$ terms cancel the mixed-curvature terms. The numerator becomes $\kappa_l\kappa_v(\rho_l^2-2\rho_l\rho_v+\rho_v^2)$. Bulk compressibility stabilizes this volume variation; capillarity destabilizes it. All 132 roots have positive mass curvature and Schur complement. The minimum bulk-to-capillary ratio is 20.4526. This establishes a local internal minimum at fixed $(T,V,m)$. Global accessibility, nucleation probability, shape stability and finite-depth dynamics are **not established**.

## 4. Audit and unresolved links

The audit checks local symbols, units, algebra, branches and references. Automated calculations reconstruct gel-energy and kinetic-power derivatives, phase inventory, traction, chemical equilibrium and seed-energy accounting. Independent waveforms and entropy drift are compared. Stability is tested separately from root existence. These checks verify the declared equations and their implementation.

**Unresolved:** optical heat distribution; metastable and heterogeneous nucleation probability; temperature gradients and phase-transfer rates; shell inertia; target high-rate rheology and fracture; surface geometry and crack filling; water vapor and noncondensable gas; nonspherical collapse, breakup and shock/impact pressure. [The implementation plan](IMPLEMENTATION_HANDOFF.md) lists the required measurements. Full target-mechanism validation is **not established**.
