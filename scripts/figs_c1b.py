"""Chapter 1, equations 10-20."""
import math

import numpy as np

from figlib import *
from figphys import rp_solve, rayleigh_curve, rayleigh_speed, collapse_ode, tc_coeff
from scipy.special import beta as beta_fn

RHO, PINF, SIG = 1000.0, 101325.0, 0.072
R0 = 5e-6


def _run(mu=1e-3):
    t, R, V, pb = rp_solve(R0, 0.0, 1.5e-6, pg0=1.0e6, mu=mu, n=4000)
    dt = t[1] - t[0]
    acc = ((pb - PINF - 2 * SIG / R - 4 * mu * V / R) / RHO - 1.5 * V * V) / R
    return t, R, V, pb, acc, dt


def e10(f):
    t, R, V, pb, acc, dt = _run()
    K = 2 * math.pi * RHO * R ** 3 * V ** 2
    Es = 4 * math.pi * SIG * R ** 2
    emax = math.ceil(max(K.max(), Es.max()) * 1e9 * 1.1 * 10) / 10
    p1 = Plot(f, 1.0, 1.5, 5.6, 3.9, (0, 1.5), (0, emax), 't  (µs)', 'energy (nJ)', (0, .5, 1, 1.5), tuple(round(emax * k / 5, 2) for k in range(6)), fx='{:.1f}', fy='{:.2f}')
    p1.curve(t * 1e6, K * 1e9, ACC, 2.8)
    p1.curve(t * 1e6, Es * 1e9, PINK, 2.8)
    p1.label(.6, emax * .97, 'liquid kinetic energy K_l = 2πρR³Ṙ²', ACC, 12, w=3.2)
    p1.label(.6, emax * .8, 'interface energy E_σ = 4πσR²', PINK, 12, w=3.2)
    dK = np.gradient(K, dt)
    dK_formula = 4 * math.pi * R ** 2 * V * RHO * (R * acc + 1.5 * V ** 2)
    dEs = np.gradient(Es, dt)
    dEs_formula = 8 * math.pi * SIG * R * V
    dK, dK_formula, dEs, dEs_formula = dK * 1e3, dK_formula * 1e3, dEs * 1e3, dEs_formula * 1e3
    pm = math.ceil(max(np.abs(dK).max(), np.abs(dEs).max()) * 1.2 * 2) / 2
    p2 = Plot(f, 7.3, 1.5, 5.6, 3.9, (0, 1.5), (-pm, pm), 't  (µs)', 'power (mW)', (0, .5, 1, 1.5), (-pm, -pm / 2, 0, pm / 2, pm), fx='{:.1f}', fy='{:.2f}')
    p2.seg(0, 0, 1.5, 0, GRID, 1.2)
    p2.curve(t * 1e6, dK, ACC, 3.2)
    p2.curve(t * 1e6, dK_formula, '#FFFFFF', 1.6, dash=True)
    p2.curve(t * 1e6, dEs, PINK, 3.2)
    p2.curve(t * 1e6, dEs_formula, '#FFFFFF', 1.6, dash=True)
    p2.label(.05, pm * .98, 'dK_l/dt  (solid: finite difference; dashed: formula)', ACC, 11, w=5.3, dy=.02)
    p2.label(.05, -pm * .8, 'dE_σ/dt = 8πσRṘ', PINK, 11.5, w=3)
    err = np.max(np.abs(dK - dK_formula)[5:-5]) / np.max(np.abs(dK))
    f.text(1.0, 6.27, 11.9, f'dK_l/dt = 4πR²Ṙ · ρ(RR̈ + 3Ṙ²/2) = V̇_b × (inertial pressure).  Formula and finite difference agree to {err * 100:.2f} % of the peak.', 13, FG)
    f.text(1.0, 6.7, 11.9, 'The same V̇_b = 4πR²Ṙ multiplies every term: volume work is what couples kinetic storage, interface storage and dissipation.', 13, WARM)
    f.note('Rayleigh–Plesset solution (R₀ = 5 µm, p_g0 = 1 MPa, γ = 1.4, σ = 0.072 N/m, μ = 1 mPa·s) differentiated with the product rule of Eq. C1-E10.')


def e11(f):
    mu = 0.01
    t, R, V, pb, acc, dt = _run(mu)
    dV = 4 * math.pi * R ** 2 * V
    W = np.concatenate([[0], np.cumsum(0.5 * ((pb - PINF) * dV)[1:] + 0.5 * ((pb - PINF) * dV)[:-1]) * dt])
    K = 2 * math.pi * RHO * R ** 3 * V ** 2
    Es = 4 * math.pi * SIG * (R ** 2 - R0 ** 2)
    pdis = 16 * math.pi * mu * R * V ** 2
    D = np.concatenate([[0], np.cumsum(0.5 * pdis[1:] + 0.5 * pdis[:-1]) * dt])
    ymax = math.ceil(max(W.max(), (K + Es + D).max()) * 1e9 * 1.1 * 10) / 10
    p = Plot(f, 1.0, 1.5, 7.2, 4.2, (0, 1.5), (0, ymax), 't  (µs)', 'cumulative energy (nJ)', (0, .5, 1, 1.5), tuple(round(ymax * k / 5, 2) for k in range(6)), fx='{:.1f}', fy='{:.2f}')
    ts = t * 1e6
    p.fill(ts, np.zeros_like(K), K * 1e9, ACC, .55)
    p.fill(ts, K * 1e9, (K + Es) * 1e9, PINK, .55)
    p.fill(ts, (K + Es) * 1e9, (K + Es + D) * 1e9, BLUE, .55)
    p.curve(ts, W * 1e9, '#FFFFFF', 2.2, dash=True)
    res = np.max(np.abs(W - (K + Es + D))) / np.max(np.abs(W))
    f.panel(8.5, 1.5, 4.45, 3.2, 'Where the pressure work goes', ACC, size=13.5)
    for i, (s, c) in enumerate([('liquid kinetic energy K_l', ACC), ('interface energy E_σ − E_σ(0)', PINK), ('viscous dissipation ∫16πμRṘ²dt ≥ 0', BLUE), ('pressure work ∫(p_b − p∞) dV (dashed)', '#FFFFFF')]):
        f.rect(8.7, 2.1 + i * .55 + .04, .3, .24, fill=c, line=c, lw=1)
        f.text(9.12, 2.1 + i * .55, 3.7, s, 11.5, FG)
    f.text(8.6, 4.35, 4.3, f'Sum of the three parts equals the work to {res * 100:.2f} %', 12, WARM, bold=True)
    f.text(1.0, 6.27, 11.9, 'd/dt (K_l + E_σ) = (p_b − p∞) V̇_b − 16πμRṘ².  Focusing can move energy between K_l and E_σ but cannot create any.', 13.5, FG)
    f.text(1.0, 6.7, 11.9, 'Viscosity μ = 10 mPa·s is chosen only to make the dissipation visible.', 12, MUT)
    f.note('Energy ledger from the Rayleigh–Plesset solution of Eq. C1-E07 using the balance of Eq. C1-E11.')


def e12(f):
    x = np.linspace(1, 4, 200)
    p = Plot(f, 1.0, 1.55, 5.2, 3.7, (1, 4), (-2.2, 1.2), 'r / R', 'strain rate / (Ṙ/R)', (1, 2, 3, 4), (-2, -1, 0, 1), fy='{:g}')
    p.seg(1, 0, 4, 0, GRID, 1.2)
    p.curve(x, -2 / x ** 3, PINK, 3)
    p.curve(x, 1 / x ** 3, ACC, 3)
    p.label(1.3, -1.45, 'D_rr = −2R²Ṙ/r³ (radial)', PINK, 12, w=3)
    p.label(1.5, .9, 'D_θθ = D_ψψ = R²Ṙ/r³ (tangential)', ACC, 12, w=3.4, dy=-.2)
    p.f.text(1.0, 5.95, 5.3, 'D_rr + 2D_θθ = 0: no net volume change (incompressible).', 12.5, FG)
    p2 = Plot(f, 7.2, 1.55, 5.6, 3.7, (1, 4), (0, 1.05), 'r / R', 'dissipation inside r', (1, 2, 3, 4), (0, .25, .5, .75, 1), fy='{:.2f}')
    p2.curve(x, 1 - 1 / x ** 3, WARM, 3)
    p2.pt(2, 7 / 8, ACC)
    p2.label(2, 7 / 8, '87.5 % inside r = 2R', ACC, 12, w=2.4, dx=.14, dy=.05)
    p2.label(2.2, .35, '𝒟 = ∫ 2μ(D_rr² + 2D_θθ²) 4πr² dr\n= 48πμR⁴Ṙ² ∫ r⁻⁴ dr = 16πμRṘ²', FG, 11.5, w=3.4)
    x0, y0 = 4.5, 3.55
    f.rect(x0, y0 - .2, .5, .5, fill=None, line=MUT, lw=1.2)
    f.rect(x0 - .1, y0 - .05, .78, .2, fill=LIQ2, line=ACC, lw=1.8, opacity=.9)
    f.line(x0 - .35, y0 + .05, x0 - .12, y0 + .05, ACC, 2, arrow=True)
    f.line(x0 + .85, y0 + .05, x0 + .66, y0 + .05, ACC, 2, arrow=True)
    f.line(x0 + .25, y0 - .38, x0 + .25, y0 - .2, PINK, 2, arrow=True)
    f.line(x0 + .25, y0 + .48, x0 + .25, y0 + .3, PINK, 2, arrow=True)
    f.text(f_x := 7.2, 5.85, 5.7, 'A shell element is squeezed radially and stretched around the sphere; most of this shearing happens near the wall.', 12.5, FG)
    f.text(1.0, 6.6, 11.9, 'Direct strain-rate integration reproduces the energy-balance loss of Eq. C1-E11 exactly.', 13, WARM)
    f.note('Profiles from Eq. C1-E12; the expanding case Ṙ > 0 is drawn (signs flip for collapse).')


def e13(f):
    f.panel(.4, 1.0, 4.6, 5.5, 'Ideal collapse, starting at rest', ACC, size=13.5)
    cx, cy = 2.7, 3.6
    f.ellipse(cx, cy, 1.15, fill=LIQ, line=LIQ2, lw=1.2)
    f.bubble(cx, cy, 1.0)
    f.text(cx - .8, cy - .38, 1.6, 'p_v only', 12.5, MUT, 'center')
    f.text(cx - .8, cy - .05, 1.6, 'R(0) = R_max', 12.5, WARM, 'center', bold=True)
    f.text(cx - .8, cy + .28, 1.6, 'Ṙ(0) = 0', 12.5, WARM, 'center', bold=True)
    for a in range(0, 360, 45):
        t = math.radians(a)
        f.line(cx + 1.95 * math.cos(t), cy - 1.95 * math.sin(t), cx + 1.3 * math.cos(t), cy - 1.3 * math.sin(t), ACC, 2.4, arrow=True)
    f.text(.55, 5.7, 4.3, 'p∞ squeezes the liquid; the gas pushes back only with p_v.   Δp_c = p∞ − p_v > 0.', 12.5, FG)
    Rmax, rho, dpc = 30e-6, 1000., 1e5
    tt, RR = rayleigh_curve(Rmax, rho, dpc)
    tc = tt[-1]
    p = Plot(f, 6.1, 1.5, 6.5, 3.9, (0, 3.0), (0, 1.05), 't  (µs)', 'R / R_max', (0, 1, 2, 3), (0, .25, .5, .75, 1), fx='{:.0f}', fy='{:.2f}')
    p.curve(tt * 1e6, RR / Rmax, ACC, 3)
    p.vline(tc * 1e6, WARM)
    p.label(tc * 1e6, .55, f't_c = {tc * 1e6:.2f} µs', WARM, 13, w=1.9, dx=-1.95, dy=0)
    p.pt(0, 1, WARM)
    p.label(.05, 1.0, 'flat start (Ṙ = 0)', WARM, 12, w=2.2, dy=.1, dx=.12)
    p.label(1.35, .12, 'steepest at the end', ACC, 12, w=2.2)
    f.text(6.1, 6.27, 6.6, 'R R̈ + (3/2)Ṙ² = −Δp_c/ρ,  R(0) = R_max,  Ṙ(0) = 0', 13.5, FG, bold=True)
    f.text(6.1, 6.68, 6.6, 'The model has no gas, viscosity, tension or compressibility, so nothing stops the collapse.', 12.5, WARM)
    f.note('R(t) from the quadrature of Eq. C1-E16; R_max = 30 µm, ρ = 1000 kg/m³, Δp_c = 100 kPa.')


def e14(f):
    x = np.linspace(.25, 1, 300)
    p = Plot(f, 7.8, 1.45, 5.0, 1.9, (0.25, 1), (0, 64), '', 'y (scaled)', (.25, .5, .75, 1), (0, 20, 40, 60), fx='{:.2f}')
    p.curve(x, x ** -3 - 1, PINK, 3)
    p.label(.5, 55, 'y = Ṙ² ∝ x⁻³ − 1: blows up inward', PINK, 12, w=4.2)
    xx = np.linspace(0, 1, 200)
    p2 = Plot(f, 7.8, 4.15, 5.0, 1.9, (0, 1), (0, 1.1), 'x = R / R_max', 'R³y (scaled)', (0, .25, .5, .75, 1), (0, .5, 1), fx='{:.2f}', fy='{:.1f}')
    p2.curve(xx, 1 - xx ** 3, ACC, 3)
    p2.seg(.45, 1 - .45 ** 3, .8, 1 - .45 ** 3 - 3 * .45 ** 2 * .35, WARM, 2, dash=True)
    p2.label(.05, .55, 'R³y = 1 − x³: simple, slope ∝ −R²', ACC, 12, w=3.2, dy=-.02)
    f.panel(.4, 1.0, 6.4, 5.4, 'Why the radius replaces time', ACC, size=13.5)
    steps = [('y(R) = Ṙ²,  Ṙ ≠ 0', 'dy/dR = 2R̈'), ('Rewrite R R̈ + (3/2)Ṙ² = −Δp_c/ρ', 'y′ + 3y/R = −2Δp_c/(ρR)'),
             ('Multiply by the integrating factor R³', 'd(R³y)/dR = R³y′ + 3R²y = −(2Δp_c/ρ) R²'), ('Integrate from R_max (y = 0)', 'R³y = (2Δp_c/3ρ)(R_max³ − R³)')]
    y = 1.55
    for i, (a_, b_) in enumerate(steps):
        f.text(.6, y, 5.9, f'{i + 1}  {a_}', 13, WARM, bold=True)
        y = f.text(.85, y + .34, 5.7, b_, 13, FG) + .3
    f.text(.6, y + .05, 5.9, 'On the monotonic inward branch R is a valid independent variable. The factor R³ makes the left side an exact derivative.', 12.5, MUT)
    f.note('Curves are y = Ṙ² and R³y from Eqs. C1-E14 and C1-E15 (scaled as labelled).')


def e15(f):
    Rmax, rho, dpc = 30e-6, 1000., 1e5
    x = np.logspace(-1.7, 0, 300)
    sp = np.array([abs(rayleigh_speed(v, Rmax, rho, dpc)) if v < 1 else 1e-9 for v in x])
    p = Plot(f, 1.1, 1.5, 6.4, 4.1, (0.02, 1.0), (1, 1000), 'R / R_max', '|Ṙ|  (m/s)', (.02, .05, .1, .2, .5, 1), (1, 10, 100, 1000), fx='{:g}', xlog=True, ylog=True)
    p.curve(x, sp, ACC, 3)
    asym = np.sqrt(2 * dpc / (3 * rho)) * x ** -1.5
    p.curve(x, asym, WARM, 1.8, dash=True)
    p.pt(.5, abs(rayleigh_speed(.5, Rmax, rho, dpc)), WARM)
    p.label(.5, 21.6, '21.6 m/s at R = R_max/2', WARM, 12, w=2.4, dx=-2.55, dy=.0)
    p.pt(.1, abs(rayleigh_speed(.1, Rmax, rho, dpc)), PINK)
    p.label(.1, 258, '258 m/s at R = R_max/10', PINK, 12, w=2.6, dx=.15, dy=-.1)
    p.label(.022, 10, 'dashed: ∝ R^(−3/2) as R → 0', WARM, 11.5, w=3.4)
    f.panel(7.9, 1.5, 5.05, 4.1, 'Reading the solution', ACC, size=13.5)
    f.text(8.05, 2.0, 4.8, 'Ṙ = −√{ (2Δp_c/3ρ) [ (R_max/R)³ − 1 ] }', 13, FG, bold=True)
    f.bullets(8.05, 2.75, 4.8, ['The start R = R_max at rest fixes the constant: Ṙ = 0 there.',
                                'The minus sign selects the inward branch (collapse).',
                                'As R → 0, |Ṙ| grows without bound: this is the model\'s singularity, not a physical speed limit.',
                                'Real collapse is stopped by gas, viscosity, tension and compressibility long before.'], 12.5)
    f.text(1.1, 6.27, 12, 'Teaching inputs: R_max = 30 µm, ρ = 1000 kg/m³, Δp_c = 100 kPa.', 12.5, MUT)
    f.note('Wall speed from Eq. C1-E15 (log–log axes).')


def e16(f):
    x = np.linspace(0, .9995, 800)
    g = x ** 1.5 / np.sqrt(1 - x ** 3)
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (0, 1), (0, 6), 'x = R / R_max', 'x^(3/2) / √(1 − x³)', (0, .25, .5, .75, 1), (0, 2, 4, 6), fx='{:.2f}')
    p.fill(x, np.zeros_like(x), np.minimum(g, 6), ACC, .3)
    p.curve(x, g, ACC, 3)
    p.vline(1, PINK, dash=True)
    p.label(.55, 5.8, 'integrand → ∞ like (1 − x)^(−1/2)\nat the endpoint: infinite height,\nfinite area', PINK, 12, w=3.2, dy=-.1)
    area = tc_coeff() / math.sqrt(1.5) * 1.0
    p.label(.1, 1.6, f'shaded area ∫ = {math.sqrt(2 / 3) * tc_coeff():.4f}', ACC, 12.5, w=3.2)
    f.panel(7.9, 1.5, 5.05, 4.0, 'Collapse time in dimensionless form', ACC, size=13.5)
    f.text(8.05, 2.0, 4.8, 't_c = ∫ dR / |Ṙ|\n= R_max √(ρ/Δp_c) · C_t', 13, FG, bold=True)
    f.text(8.05, 3.0, 4.8, 'C_t = √(3/2) ∫₀¹ x^(3/2) / √(1 − x³) dx', 13, WARM, bold=True)
    f.text(8.05, 3.65, 4.8, f'= √(3/2) × {math.sqrt(2 / 3) * tc_coeff():.4f} = {tc_coeff():.6f}', 13, FG)
    f.text(8.05, 4.3, 4.8, 'The substitution x = R/R_max and dR = R_max dx moves all dimensions into the prefactor.', 12, MUT)
    f.text(1.0, 6.27, 12, 'The endpoint singularity is integrable, so the ideal collapse takes a finite time, 0.91468 R_max √(ρ/Δp_c).', 13, FG)
    f.note('Integrand from Eq. C1-E16; area by numerical quadrature.')


def e17(f):
    q = np.linspace(.0005, .9995, 1500)
    h = q ** (-1 / 6) / np.sqrt(1 - q)
    B = beta_fn(5 / 6, .5)
    p = Plot(f, 1.0, 1.5, 6.0, 3.8, (0, 1), (0, 6), 'q = x³', 'q^(−1/6) (1 − q)^(−1/2)', (0, .25, .5, .75, 1), (0, 2, 4, 6), fx='{:.2f}')
    p.fill(q, np.zeros_like(q), np.minimum(h, 6), WARM, .28)
    p.curve(q, h, WARM, 3)
    p.label(.1, 5.5, f'area = B(5/6, 1/2) = {B:.4f}', WARM, 12.5, w=3.4)
    p.label(.03, 3.2, 'mild q^(−1/6)\nspike at 0', MUT, 11.5, w=1.6)
    p.label(.55, 3.6, 'sharp (1 − q)^(−1/2)\nspike at 1', MUT, 11.5, w=2.0)
    xs = np.linspace(0, 1, 100)
    p2 = Plot(f, 8.1, 1.5, 4.5, 3.8, (0, 1), (0, 1), 'x = R / R_max', 'q = x³', (0, .5, 1), (0, .5, 1), fx='{:g}', fy='{:g}')
    p2.curve(xs, xs ** 3, ACC, 3)
    p2.seg(0, 0, 1, 1, GRID, 1.2, dash=True)
    p2.label(.1, .85, 'dx = (1/3) q^(−2/3) dq', ACC, 12, w=2.6)
    f.text(1.0, 6.27, 12, 'C_t = (1/√6) B(5/6, 1/2) = 2.2405/√6 = 0.9146813565…', 14, FG, bold=True)
    f.text(1.0, 6.7, 12, 'The cube-law change of variable turns the collapse integral into a standard beta integral with known value.', 13, WARM)
    f.note('B(a, b) = ∫ q^(a−1)(1 − q)^(b−1) dq for a, b > 0 (Eq. C1-E17).')


def e18(f):
    Rmax, rho, dpc = 30e-6, 1000., 1e5
    EB = 4 * math.pi / 3 * dpc * Rmax ** 3
    x = np.linspace(.02, 1, 200)
    t, R, V = collapse_ode(Rmax, rho, dpc, 3e-6)
    Kn = 2 * math.pi * rho * R ** 3 * V ** 2
    ok = np.isfinite(Kn)
    xr = R / Rmax
    p = Plot(f, 1.0, 1.5, 6.5, 4.0, (0, 1), (0, 1.05), 'R / R_max', 'K_l / E_B', (0, .25, .5, .75, 1), (0, .25, .5, .75, 1), fx='{:.2f}', fy='{:.2f}')
    p.curve(x, 1 - x ** 3, ACC, 3)
    idx = np.linspace(2, len(xr) - 3, 24).astype(int)
    for i in idx:
        p.pt(xr[i], Kn[i] / EB, WARM, .06)
    err = np.max(np.abs(Kn[ok] / EB - (1 - xr[ok] ** 3)))
    p.label(.04, .42, 'line: 1 − (R/R_max)³ from Eq. C1-E18', ACC, 12, w=3.4, dy=.0)
    p.label(.04, .28, f'dots: direct ODE solution; largest difference {err:.0e}', WARM, 12, w=3.4, dy=.0)
    f.panel(8.0, 1.5, 4.95, 4.0, 'Two independent routes', ACC, size=13.5)
    f.text(8.15, 2.0, 4.7, 'Route 1: speed solution\nK_l = 2πρR³Ṙ² with Ṙ from Eq. C1-E15', 12.5, FG)
    f.text(8.15, 3.0, 4.7, 'Route 2: pressure work\nE_B = Δp_c V_max = (4π/3) Δp_c R_max³', 12.5, FG)
    f.text(8.15, 4.0, 4.7, 'K_l/E_B = 1 − (R/R_max)³  holds at every radius, so no energy is created or lost.', 12.5, WARM, bold=True)
    f.text(1.0, 6.27, 12, 'Half the radius has released 7/8 of the stored pressure work as kinetic energy.', 13.5, FG)
    f.note('Dots: numerical integration of R R̈ + 3Ṙ²/2 = −Δp_c/ρ (Eq. C1-E13); no viscosity, tension or gas.')


def e19(f):
    Rmax, rho, dpc = 30e-6, 1000., 1e5
    EB = 4 * math.pi / 3 * dpc * Rmax ** 3
    tt, RR = rayleigh_curve(Rmax, rho, dpc)
    tc = tt[-1]
    K = 2 * math.pi * rho * RR ** 3 * (np.array([abs(rayleigh_speed(min(r / Rmax, 0.9999), Rmax, rho, dpc)) for r in RR])) ** 2
    ih = int(np.argmin(np.abs(RR - Rmax / 2)))
    p1 = Plot(f, 1.0, 1.4, 6.3, 2.0, (0, 3), (0, 32), '', 'R  (µm)', (0, 1, 2, 3), (0, 10, 20, 30), fx='{:.0f}')
    p1.curve(tt * 1e6, RR * 1e6, ACC, 3)
    p1.pt(tt[ih] * 1e6, 15, WARM)
    p1.vline(tc * 1e6, PINK)
    p1.label(tt[ih] * 1e6, 15, f'R = R_max/2 at {tt[ih] * 1e6:.2f} µs', WARM, 11.5, w=2.6, dx=-2.7, dy=-.05)
    p1.label(tc * 1e6, 29, f't_c = {tc * 1e6:.3f} µs', PINK, 12, w=1.8, dx=-1.9, dy=0)
    p2 = Plot(f, 1.0, 4.2, 6.3, 1.9, (0, 3), (0, 13), 't  (µs)', 'K_l  (nJ)', (0, 1, 2, 3), (0, 4, 8, 12), fx='{:.0f}')
    p2.curve(tt * 1e6, K * 1e9, ACC, 3)
    p2.hline(EB * 1e9, WARM)
    p2.label(.1, EB * 1e9, f'E_B = {EB * 1e9:.4f} nJ', WARM, 12, w=2.4, dy=-.32)
    p2.pt(tt[ih] * 1e6, 7 / 8 * EB * 1e9, WARM)
    p2.label(tt[ih] * 1e6, 7 / 8 * EB * 1e9, 'K_l = 7/8 E_B = 9.896 nJ', WARM, 11.5, w=2.4, dx=-2.5, dy=.12)
    f.panel(7.7, 1.4, 5.25, 4.95, 'The declared numbers', ACC, size=13.5)
    rows = [('Collapse time', f't_c = 0.9147 × 30 µm × √(1000/10⁵) = {tc * 1e6:.4f} µs'),
            ('Work scale', 'E_B = (4π/3)(10⁵)(30 µm)³ = 11.3097 nJ'),
            ('Half-radius speed', 'Ṙ = −√[(2×10⁵/(3×1000))(8 − 1)] = −21.6025 m/s'),
            ('Half-radius energy', 'K_l = (7/8) E_B = 9.8960 nJ')]
    y = 1.95
    for h, b in rows:
        y = f.text(7.9, y, 4.9, h, 13, WARM, bold=True)
        y = f.text(8.0, y, 4.8, b, 12, FG) + .18
    f.text(7.9, y + .05, 4.9, 'Inputs: ρ = 1000 kg/m³, Δp_c = 100 kPa, R_max = 30 µm. A teaching case, not a measurement.', 11.5, MUT)
    f.note('All values from Eq. C1-E19 and the Rayleigh curve of Eq. C1-E16.')


def e20(f):
    Rmax, rho, dpc, c = 30e-6, 1000., 1e5, 1500.
    x = np.logspace(-1.6, 0, 300)
    M = np.array([abs(rayleigh_speed(v, Rmax, rho, dpc)) / c if v < 1 else 1e-9 for v in x])
    xM = (1 + 3 * rho * c ** 2 * .1 ** 2 / (2 * dpc)) ** (-1 / 3)
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (0.025, 1.0), (1e-3, 1.0), 'R / R_max', 'wall Mach number |Ṙ| / c', (.025, .05, .1, .2, .5, 1), (1e-3, 1e-2, 1e-1, 1), fx='{:g}', fy='{:g}', xlog=True, ylog=True)
    p.curve(x, np.minimum(M, 1.0), ACC, 3)
    p.hline(.1, WARM)
    p.label(.5, .1, 'M* = 0.1', WARM, 12.5, w=1.5, dy=-.32)
    sh = [v for v in x if v <= xM]
    p.f.poly([(p.X(sh[0]), p.Y(1.0)), (p.X(xM), p.Y(1.0)), (p.X(xM), p.Y(1e-3)), (p.X(sh[0]), p.Y(1e-3))], fill=PINK, line=PINK, lw=.5, opacity=.18)
    p.vline(xM, PINK)
    p.pt(xM, .1, PINK)
    p.label(xM, .1, f'x_M = {xM:.6f}', PINK, 12, w=2.2, dx=.1, dy=-.5)
    p.label(.027, .004, 'incompressible model\nnot trusted here', PINK, 12, w=2.2, dy=-.5)
    f.panel(8.0, 1.5, 4.95, 4.0, 'A diagnostic, not a limit', ACC, size=13.5)
    f.text(8.15, 2.0, 4.7, 'x_M = [ 1 + 3ρc²M*² / (2Δp_c) ]^(−1/3)', 13, FG, bold=True)
    f.bullets(8.15, 2.65, 4.7, ['With c = 1500 m/s and M* = 0.1 the ideal collapse reaches M* at R = 0.143 R_max.',
                                'Inside that radius the speed is large enough that liquid compressibility must be added.',
                                'The ideal trajectory itself is not a physical prediction.'], 12.5)
    f.text(1.0, 6.27, 12, 'Wall Mach number M_w = |Ṙ|/c grows as R shrinks, so the incompressible formulas lose validity near the end of the collapse.', 13, FG)
    f.note('Curve from Eq. C1-E15 with c = 1500 m/s; threshold from Eq. C1-E20 (teaching inputs).')


FIGS = {10: e10, 11: e11, 12: e12, 13: e13, 14: e14, 15: e15, 16: e16, 17: e17, 18: e18, 19: e19, 20: e20}
