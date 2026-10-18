"""Appendix A (Chapter 90), equations 01-12."""
import math

import numpy as np

from figlib import *

G, RREF, R = 20000.0, 5e-6, 30e-6
RHO_G, ETA = 1000.0, 0.010
SIG = 0.072


def _trapz(y, x):
    return float(np.trapezoid(y, x)) if hasattr(np, 'trapezoid') else float(np.trapz(y, x))


def p_el(Rr, Rref=RREF):
    q = Rref / Rr
    return G / 2 * (5 - 4 * q - q ** 4)


def r0_of_r(r, Rr, Rref=RREF):
    return (r ** 3 - Rr ** 3 + Rref ** 3) ** (1 / 3)


def e01(f):
    f.panel(.4, 1.0, 5.4, 5.3, 'The same network shells before and after', ACC, size=13.5)
    f.ellipse(1.5, 3.1, .4, fill=GASC, line=MUT, lw=1.4)
    f.text(.9, 2.95, 1.2, 'R_ref', 10.5, MUT, 'center')
    for r in (.65, .9):
        f.ellipse(1.5, 3.1, r, fill=None, line=LIQ2, lw=1.1)
    f.text(.6, 4.45, 2.4, 'reference state', 11.5, MUT)
    f.ellipse(4.2, 3.1, .8, fill=GASC, line=WARM, lw=2.2)
    for r in (1.0, 1.2):
        f.ellipse(4.2, 3.1, r, fill=None, line=LIQ2, lw=1.1)
    f.line(2.3, 3.1, 3.0, 3.1, ACC, 3, arrow=True)
    f.text(3.7, 2.95, 1.0, 'R', 12, WARM, 'center', bold=True)
    f.text(3.0, 4.45, 2.6, 'expanded to R', 11.5, WARM)
    f.text(.6, 4.85, 5.0, 'shell volume conserved: r³ − R³ = r₀³ − R_ref³', 12, FG, bold=True)
    f.text(.6, 5.4, 5.0, 'λ_r = ∂r/∂r₀ = r₀²/r²,   λ_θ = λ_φ = r/r₀,   λ_rλ_θλ_φ = 1', 11.5, WARM, bold=True)
    x = np.linspace(RREF, 6 * RREF, 200)
    r = (x ** 3 + R ** 3 - RREF ** 3) ** (1 / 3)
    lr, lt = (x / r) ** 2, r / x
    p = Plot(f, 6.7, 1.5, 6.1, 4.0, (1, 6), (0, 6), 'reference radius r₀ / R_ref', 'stretch', (1, 2, 3, 4, 5, 6), (0, 1, 2, 3, 4, 5, 6), fx='{:g}', fy='{:g}')
    p.curve(x / RREF, lt, WARM, 3)
    p.curve(x / RREF, lr, BLUE, 3)
    p.curve(x / RREF, lr * lt * lt, FG, 2, dash=True)
    p.label(2.2, 5.0, 'λ_θ = λ_φ (tangential): stretched', WARM, 11.5, w=3.4, dy=0)
    p.label(3.2, 2.2, 'λ_r (radial): thinned', BLUE, 11.5, w=2.6, dy=0)
    p.label(3.0, .75, 'product = 1 (incompressible)', FG, 11.5, w=3.0, dy=0)
    f.text(6.7, 6.4, 6.1, f'Check: λ_rλ_θ² = {float((lr * lt * lt)[0]):.6f} … {float((lr * lt * lt)[-1]):.6f}.   Cavity grown from 5 to 30 µm.', 12, MUT)
    f.note('Exact incompressible kinematics of Eq. A-E01 for R_ref = 5 µm, R = 30 µm.')


def e02(f):
    r = np.linspace(R, 4 * R, 300)
    r0 = r0_of_r(r, R)
    d = (r / r0) ** 2 - (r0 / r) ** 4
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (1, 4), (.01, 60), 'distance from the wall r / R', '(T_θθ − T_rr) / G_g', (1, 2, 3, 4), (.01, .1, 1, 10), fx='{:g}', fy='{:g}', ylog=True)
    p.fill(r / R, np.full_like(r, .01), d, ACC, .22)
    p.curve(r / R, d, ACC, 3.4)
    p.pt(1, d[0], WARM)
    p.label(1, d[0], f'at the wall: {d[0]:.2f} G_g', WARM, 12, w=2.4, dx=.15, dy=.3)
    p.label(2.0, 4, 'stress difference dies off outward (log axis)', MUT, 11.5, w=4.0)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Neo-Hookean network', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'T^e = −χI + G_g B,   B = F Fᵀ', 12.5, FG, bold=True)
    f.text(7.85, 2.55, 5.0, 'T_rr = −χ + G_g λ_r²,   T_θθ = −χ + G_g λ_θ²', 12, FG, bold=True)
    f.text(7.85, 3.1, 5.0, 'T_θθ − T_rr = G_g[(r/r₀)² − (r₀/r)⁴]', 12.5, WARM, bold=True)
    f.text(7.85, 3.75, 5.0, 'The unknown pressure χ cancels in the difference.', 12, MUT)
    f.text(1.0, 6.27, 12, 'Only the difference of normal stresses enters the force balance, so χ never has to be found.', 12.5, FG)
    f.note('Exact subtraction of Eq. A-E02 (R_ref = 5 µm, R = 30 µm).')


def e03(f):
    r = np.geomspace(R, 400 * R, 400000)
    r0 = r0_of_r(r, R)
    integrand = ((r / r0) ** 2 - (r0 / r) ** 4) / r * R
    xs = np.linspace(1, 6, 200)
    rr = xs * R
    ii = ((rr / r0_of_r(rr, R)) ** 2 - (r0_of_r(rr, R) / rr) ** 4) / rr * R
    area = _trapz(integrand / R, r)
    pel = 2 * G * _trapz(((r / r0) ** 2 - (r0 / r) ** 4) / r, r)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (1, 6), (.001, 60), 'r / R', 'integrand × R  (log axis)', (1, 2, 3, 4, 5, 6), (.001, .01, .1, 1, 10), fx='{:g}', fy='{:g}', ylog=True)
    p.fill(xs, np.full_like(xs, .001), ii, ACC, .25)
    p.curve(xs, ii, ACC, 3.2)
    p.label(2.0, 20, f'area to ∞ = {area:.4f}  ⇒  p_el = 2G_g·area = {pel / 1e3:.3f} kPa', WARM, 11.5, w=4.4, dy=0)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Radial force balance', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'dT_rr/dr = (2/r)(T_θθ − T_rr)', 13, FG, bold=True)
    f.text(7.85, 2.55, 5.0, 'T_rr(∞) = −p_∞,   T_rr(R) = −p_b + 2σ/R', 12, WARM, bold=True)
    f.text(7.85, 3.1, 5.0, 'p_el = p_b − p_∞ − 2σ/R = 2G_g ∫_R^∞ [...] dr/r', 12, WARM, bold=True)
    f.text(7.85, 3.85, 5.0, 'Integrating the balance from the wall to infinity collects all the elastic resistance.', 12, MUT)
    f.text(1.0, 6.27, 12, 'The shaded area is the accumulated resistance; later figures evaluate it in closed form.', 12.5, FG)
    f.note('Static balance of Eq. A-E03, integral evaluated numerically to 400R; closed form 43.326 kPa.')


def e04(f):
    xs = np.linspace(1, 8, 300)
    rr = xs * R
    q = (1 - (R ** 3 - RREF ** 3) / rr ** 3) ** (1 / 3)
    p = Plot(f, 1.0, 1.5, 3.4, 3.8, (1, 8), (0, 1.05), 'r / R', 'q', (1, 4, 8), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    p.curve(xs, q, ACC, 3)
    p.pt(1, RREF / R, WARM)
    p.label(1, RREF / R, 'q(R) = R_ref/R', WARM, 11, w=1.8, dx=.2, dy=-.3)
    p.hline(1, MUT)
    qq = np.linspace(RREF / R, .999, 100)
    p2 = Plot(f, 5.4, 1.5, 3.2, 3.8, (0, 1), (0, 2.1), 'q', 'integrand', (0, .5, 1), (0, 1, 2), fx='{:g}', fy='{:g}')
    p2.fill(qq, np.zeros_like(qq), 1 + qq ** 3, ACC, .25)
    p2.curve(np.linspace(0, 1, 100), 1 + np.linspace(0, 1, 100) ** 3, ACC, 3)
    p2.label(.05, 1.8, '(1 + q³)', ACC, 12, w=1.2)
    f.panel(9.0, 1.5, 3.95, 3.8, 'Change of variable', ACC, size=13)
    f.text(9.1, 2.0, 3.75, 'q³ = 1 − (R³ − R_ref³)/r³', 11, FG, bold=True)
    f.text(9.1, 2.6, 3.75, 'dr/r = q² dq / (1 − q³)', 11.5, FG, bold=True)
    f.text(9.1, 3.2, 3.75, '(q⁻² − q⁴) dr/r = (1 + q³) dq', 12, WARM, bold=True)
    f.text(9.1, 4.0, 3.75, 'A messy spatial integral becomes a polynomial.', 11.5, MUT)
    nchk = float(np.max(np.abs((qq ** -2 - qq ** 4) * qq ** 2 / (1 - qq ** 3) - (1 + qq ** 3))))
    f.text(1.0, 6.0, 12, f'Check: (q⁻² − q⁴) q²/(1 − q³) = 1 + q³ on the whole range (max difference {nchk:.1e}).', 12.5, FG)
    f.note('Exact change of variable of Eq. A-E04.')


def e05(f):
    x = np.linspace(1, 10, 300)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (1, 10), (0, 2.8), 'R / R_ref', 'p_el / G_g', (1, 2, 4, 6, 8, 10), (0, .5, 1, 1.5, 2, 2.5), fx='{:g}', fy='{:.1f}')
    pe = .5 * (5 - 4 / x - x ** -4.0)
    p.curve(x, pe, ACC, 3.4)
    p.hline(2.5, MUT)
    p.label(5, 2.55, 'limit 5/2', MUT, 11.5, w=1.4, dy=0)
    p.pt(6, p_el(R) / G, WARM)
    p.label(6, p_el(R) / G, f'R/R_ref = 6:\n{p_el(R) / G:.4f} G_g = {p_el(R):.1f} Pa', WARM, 11.5, w=2.6, dx=.0, dy=.35)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Closed form', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'p_el = 2G_g ∫ (1 + q³) dq   (q: R_ref/R → 1)', 11.5, FG, bold=True)
    f.text(7.85, 2.55, 5.0, '= 2G_g [q + q⁴/4]', 12.5, FG, bold=True)
    f.text(7.85, 3.1, 5.0, '= (G_g/2)[5 − 4R_ref/R − (R_ref/R)⁴]', 13, WARM, bold=True)
    f.text(7.85, 3.8, 5.0, 'Obtained from the stretch field, not a guessed constant pressure.', 12, MUT)
    f.text(1.0, 6.27, 12, 'Resistance rises steeply at first and saturates near 5G_g/2 when the cavity is many times its reference size.', 12.5, FG)
    f.note('Neo-Hookean elastic resistance of Eq. A-E05 (curve normalised by G_g).')


def e06(f):
    x = np.linspace(1, 10, 300)
    dp = 2 * (1 / x ** 2 + 1 / x ** 5)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (1, 10), (0, 4.2), 'R / R_ref', 'R_ref · dp_el/dR / G_g', (1, 2, 4, 6, 8, 10), (0, 1, 2, 3, 4), fx='{:g}', fy='{:g}')
    p.curve(x, dp, WARM, 3.4)
    p.pt(1, 4, PINK)
    p.label(1, 4, 'slope 4 at R_ref', PINK, 11.5, w=1.9, dx=.15, dy=-.1)
    p.label(4, .6, 'positive everywhere: p_el always increases', MUT, 11.5, w=3.6, dy=0)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Three checks', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'p_el(R_ref) = (G_g/2)(5 − 4 − 1) = 0', 12.5, FG, bold=True)
    f.text(7.85, 2.6, 5.0, 'dp_el/dR = 2G_g (R_ref/R² + R_ref⁴/R⁵) > 0', 12, FG, bold=True)
    f.text(7.85, 3.2, 5.0, 'lim R/R_ref → ∞: p_el → 5G_g/2', 12.5, FG, bold=True)
    f.text(7.85, 3.9, 5.0, 'Zero strain, zero resistance; expansion raises it monotonically and boundedly.', 12, MUT)
    f.text(1.0, 6.27, 12, 'These checks guard against sign errors: a negative slope or a non-zero value at R_ref would signal a mistake.', 12.5, FG)
    f.note('Limiting-state and sign checks of Eq. A-E06.')


def e07(f):
    xi = np.linspace(RREF, 6 * RREF, 1500)
    pe = np.array([p_el(v) for v in xi])
    Wnum = 4 * math.pi * _trapz(pe * xi ** 2, xi)
    Wcl = 2 * math.pi * G * (5 * R ** 3 / 3 - 2 * RREF * R ** 2 + RREF ** 4 / R - 2 * RREF ** 3 / 3)
    Rs = np.linspace(RREF, 6 * RREF, 120)
    Wc = 2 * math.pi * G * (5 * Rs ** 3 / 3 - 2 * RREF * Rs ** 2 + RREF ** 4 / Rs - 2 * RREF ** 3 / 3)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (5, 30), (0, 5.2), 'cavity radius R  (µm)', 'stored work W_g  (nJ)', (5, 10, 15, 20, 25, 30), (0, 1, 2, 3, 4, 5), fx='{:g}', fy='{:g}')
    p.fill(Rs * 1e6, np.zeros_like(Rs), Wc * 1e9, ACC, .22)
    p.curve(Rs * 1e6, Wc * 1e9, ACC, 3.4)
    p.pt(30, Wcl * 1e9, WARM)
    p.label(30, Wcl * 1e9, f'W_g(30 µm) = {Wcl * 1e9:.4f} nJ', WARM, 12, w=2.8, dx=-2.9, dy=-.5)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Integrate pressure over volume', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'W_g = 4π ∫ p_el(ξ) ξ² dξ', 13, FG, bold=True)
    f.text(7.85, 2.55, 5.0, '= 2πG_g [5ξ³/3 − 2R_ref ξ² + R_ref⁴/ξ]', 11.5, WARM, bold=True)
    f.text(7.85, 3.1, 5.0, 'W_g = 2πG_g[5R³/3 − 2R_ref R² + R_ref⁴/R − 2R_ref³/3]', 11, WARM, bold=True)
    f.text(7.85, 3.8, 5.0, f'Numerical quadrature: {Wnum * 1e9:.6f} nJ;  closed form: {Wcl * 1e9:.6f} nJ.', 12, MUT)
    f.text(1.0, 6.27, 12, '4πξ² dξ is the cavity volume increment, so the integral is work done against the network.', 12.5, FG)
    f.note('Elastic work of Eq. A-E07 (R_ref = 5 µm, G_g = 20 kPa).')


def e08(f):
    d = np.linspace(0, .5, 100)
    x = 1 + d
    pex = G / 2 * (5 - 4 / x - x ** -4.0)
    plin = 4 * G * d
    p = Plot(f, 1.0, 1.5, 3.6, 3.8, (0, .5), (0, 40), 'δR / R_ref', 'p_el  (kPa)', (0, .25, .5), (0, 10, 20, 30, 40), fx='{:g}', fy='{:g}')
    p.curve(d, pex / 1e3, ACC, 3)
    p.curve(d, plin / 1e3, WARM, 2, dash=True)
    p.label(.02, 36, 'exact', ACC, 11.5, w=.9)
    p.label(.02, 31, 'linear 4G_g δR/R_ref', WARM, 11.5, w=2.2)
    Rr = RREF
    xr = 1 + d
    Wex = 2 * math.pi * G * Rr ** 3 * (5 * xr ** 3 / 3 - 2 * xr ** 2 + 1 / xr - 2 / 3)
    Wlin = 8 * math.pi * G * Rr ** 3 * d ** 2
    q = Plot(f, 5.7, 1.5, 3.6, 3.8, (0, .5), (0, .02), 'δR / R_ref', 'W_g  (nJ)', (0, .25, .5), (0, .005, .01, .015, .02), fx='{:g}', fy='{:.3f}')
    q.curve(d, Wex * 1e9, ACC, 3)
    q.curve(d, Wlin * 1e9, WARM, 2, dash=True)
    q.label(.02, .0185, 'exact', ACC, 11.5, w=.9)
    q.label(.02, .0165, 'quadratic 8πG_g R_ref δR²', WARM, 11.5, w=3.2, dy=0)
    f.panel(9.6, 1.5, 3.35, 3.8, 'Work conjugacy', ACC, size=13)
    f.text(9.7, 2.0, 3.15, 'dW_g/dR = 4πR² p_el', 12, FG, bold=True)
    f.text(9.7, 2.65, 3.15, 'p_el ≈ 4G_g δR/R_ref', 12, WARM, bold=True)
    f.text(9.7, 3.3, 3.15, 'W_g ≈ 8πG_g R_ref δR²', 12, WARM, bold=True)
    f.text(9.7, 4.0, 3.15, 'Linear pressure, quadratic work.', 11.5, MUT)
    f.text(1.0, 6.0, 12, 'The dashed small-deformation laws are tangent to the exact curves at δR = 0 and drift away only as the stretch grows.', 12.5, FG)
    f.note('Work conjugacy and small-deformation limits of Eq. A-E08.')


def e09(f):
    x = np.linspace(1, 5, 200)
    p = Plot(f, 1.0, 1.5, 6.0, 4.0, (1, 5), (-2.2, 1.2), 'r / R', 'strain rate  (units Ṙ / R)', (1, 2, 3, 4, 5), (-2, -1, 0, 1), fx='{:g}', fy='{:g}')
    p.curve(x, -2 / x ** 3, PINK, 3)
    p.curve(x, 1 / x ** 3, ACC, 3)
    p.label(1.9, -1.55, 'D_rr = −2R²Ṙ/r³  (radial)', PINK, 11.5, w=3.0, dy=0)
    p.label(2.0, .55, 'D_θθ = D_φφ = R²Ṙ/r³  (tangential)', ACC, 11.5, w=3.6, dy=0)
    p.seg(1, 0, 5, 0, GRID, 1.2)
    f.panel(7.2, 1.5, 5.75, 4.0, 'Kelvin–Voigt closure', ACC, size=13.5)
    f.text(7.35, 2.0, 5.5, 'T = T^e + 2η_g D,   u_r = R²Ṙ / r²', 12.5, FG, bold=True)
    f.text(7.35, 2.6, 5.5, 'trace D = −2 + 1 + 1 = 0  (incompressible)', 12, WARM, bold=True)
    f.text(7.35, 3.2, 5.5, 'T_θθ − T_rr = (elastic) + 6η_g R²Ṙ / r³', 12.5, WARM, bold=True)
    f.text(7.35, 3.9, 5.5, 'The viscous term follows the strain rate of the medium, not the mass of the bubble.', 12, MUT)
    f.text(1.0, 6.27, 12, 'Radial strain rate is −2 and tangential +1 in units of Ṙ R²/r³: incompressibility forces the 2 : 1 split.', 12.5, FG)
    f.note('Radial kinematics and viscous stress difference of Eq. A-E09.')


def e10(f):
    Rd, Rdd = -10.0, 2.0e6
    r = np.geomspace(R, 400 * R, 400000)
    ar = (2 * R * Rd ** 2 + R ** 2 * Rdd) / r ** 2 - 2 * R ** 4 * Rd ** 2 / r ** 5
    I1 = _trapz(ar, r) + (2 * R * Rd ** 2 + R ** 2 * Rdd) / (400 * R)
    claim = R * Rdd + 1.5 * Rd ** 2
    xs = np.linspace(1, 6, 200)
    rr = xs * R
    ars = (2 * R * Rd ** 2 + R ** 2 * Rdd) / rr ** 2 - 2 * R ** 4 * Rd ** 2 / rr ** 5
    p = Plot(f, 1.0, 1.5, 6.2, 4.0, (1, 6), (0, 9500), 'r / R', 'a_r  (10³ m/s²)', (1, 2, 3, 4, 5, 6), (0, 2500, 5000, 7500), fx='{:g}', fy='{:g}')
    p.fill(xs, np.zeros_like(xs), ars / 1e3, ACC, .22)
    p.curve(xs, ars / 1e3, ACC, 3.2)
    p.label(2.3, 6800, f'∫_R^∞ a_r dr = {I1:.4f} m²/s²', WARM, 11.5, w=3.8, dy=0)
    p.label(2.3, 5800, f'R R̈ + (3/2) Ṙ² = {claim:.4f} m²/s²', FG, 11.5, w=3.8, dy=0)
    f.panel(7.5, 1.5, 5.45, 4.0, 'Integrating the momentum law', ACC, size=13.5)
    f.text(7.65, 2.0, 5.2, 'ρ_g a_r = ∂T_rr/∂r + (2/r)(T_rr − T_θθ)', 12, FG, bold=True)
    f.text(7.65, 2.55, 5.2, 'ρ_g ∫a_r dr = ρ_g (R R̈ + 3Ṙ²/2)', 12.5, WARM, bold=True)
    f.text(7.65, 3.1, 5.2, 'viscous part: 2∫(…)(−6η_gR²Ṙ/r³)dr/r → −4η_g Ṙ/R', 11.5, WARM, bold=True)
    f.text(7.65, 3.8, 5.2, 'Acceleration and viscous stress give two distinct radial contributions.', 12, MUT)
    f.text(1.0, 6.27, 12, f'Numerical check with R = 30 µm, Ṙ = −10 m/s, R̈ = 2×10⁶ m/s²: area under a_r agrees with R R̈ + 3Ṙ²/2 to {abs(I1 - claim) / claim * 100:.4f} %.', 12, FG)
    f.note('Evaluated integrals of Eq. A-E10 (quadrature to 400R plus the 1/r² tail beyond it, added analytically).')


def e11(f):
    dpw = 100e3
    sig = 2 * SIG / R
    pe = p_el(R)
    vis = -4 * ETA * (-10.0) / R
    inertia = dpw - sig - pe + vis
    f.text(.5, 1.0, 6.5, 'Pressure ledger at one instant (kPa)', 13.5, ACC, bold=True)
    steps = [('p_b − p_∞', dpw / 1e3, ACC), ('− 2σ/R', -sig / 1e3, WARM), ('− p_el', -pe / 1e3, PINK), ('− 4η_gṘ/R', vis / 1e3, BLUE), ('= ρ_g(RR̈ + 3Ṙ²/2)', None, GREEN)]
    waterfall(f, .6, 1.6, 7.0, 3.6, steps, 125, fmt='{:.1f}', yticks=(0, 25, 50, 75, 100, 125), ylabel='')
    f.panel(8.0, 1.0, 4.95, 4.4, 'Spherical radial control', ACC, size=13.5)
    f.text(8.15, 1.5, 4.7, 'ρ_g(RR̈ + 3Ṙ²/2) = p_b − p_∞ − 2σ/R − p_el − 4η_gṘ/R', 11.5, FG, bold=True)
    f.bullets(8.15, 2.5, 4.7, ['Left: inertia of the surrounding gel.', 'Right: driving overpressure minus capillary, elastic and viscous resistance.', 'Inward motion (Ṙ < 0) turns the viscous term into a push.'], 12)
    f.text(.6, 5.55, 12.3, f'Illustration: p_b − p_∞ = 100 kPa, R = 30 µm, Ṙ = −10 m/s, σ = 0.072 N/m (assumed), η_g = 0.010 Pa s, G_g = 20 kPa, R_ref = 5 µm.', 12, MUT)
    f.text(.6, 6.1, 12.3, 'The model quantifies cavity work before any directional-flow calculation; it does not create an outlet.', 12.5, FG)
    f.note('Radial control of Eq. A-E11 (values illustrative; the inertia bar is what is left over).')


def e12(f):
    steps = [('(p_b−p_∞)V̇', 1.0, ACC), ('− P_dis', -.28, PINK), ('− dE_σ/dt', -.05, WARM), ('− dW_g/dt', -.32, BLUE), ('= dK_g/dt', None, GREEN)]
    f.text(.5, 1.0, 7.0, 'Where the pressure power goes (schematic share)', 13.5, ACC, bold=True)
    waterfall(f, .6, 1.6, 7.0, 3.6, steps, 1.2, fmt='{:.2f}', yticks=(0, .25, .5, .75, 1), ylabel='')
    f.panel(8.0, 1.0, 4.95, 4.4, 'Energy bookkeeping', ACC, size=13.5)
    f.text(8.15, 1.5, 4.7, 'K_g = 2πρ_gR³Ṙ²,   E_σ = 4πσR²', 12, FG, bold=True)
    f.text(8.15, 2.05, 4.7, 'd(K_g + W_g + E_σ)/dt = (p_b − p_∞)V̇ − P_dis', 11.5, WARM, bold=True)
    f.text(8.15, 2.7, 4.7, 'P_dis = 16πη_g R Ṙ² ≥ 0', 12.5, PINK, bold=True)
    f.text(8.15, 3.35, 4.7, 'Network work is recoverable; viscous dissipation is not.', 12, MUT)
    f.text(.6, 5.55, 12.3, 'Pressure work splits into medium inertia, recoverable network energy, surface energy and a positive viscous loss.', 12.5, FG)
    f.text(.6, 6.1, 12.3, 'Shares are illustrative; the identity itself is exact within the model.', 12, MUT)
    f.note('Mechanical energy balance of Eq. A-E12 (shares schematic).')


FIGS = {1: e01, 2: e02, 3: e03, 4: e04, 5: e05, 6: e06, 7: e07, 8: e08, 9: e09, 10: e10, 11: e11, 12: e12}
