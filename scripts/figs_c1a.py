"""Chapter 1, equations 01-09."""
import math
import random

import numpy as np

from figlib import *
from figphys import rp_solve, psat_pfp, psat_water


def e01(f):
    f.rect(.4, 1.0, 4.7, 5.3, fill=LIQ, line=LIQ2, lw=1.5, round_=True)
    f.text(.55, 1.07, 4.4, 'State at t = 0', 14, ACC, bold=True)
    cx, cy, r = 2.75, 3.55, .85
    f.liquid_rings(cx, cy, r, n=4, step=.38)
    f.bubble(cx, cy, r)
    f.text(cx - .4, cy - .5, .8, 'gas', 12, MUT, 'center')
    f.line(cx, cy, cx + r, cy, WARM, 2.2)
    f.text(cx + .2, cy + .05, .7, 'R₀', 14, WARM, bold=True)
    a = math.radians(50)
    f.line(cx + r * math.cos(a), cy - r * math.sin(a), cx + (r + .8) * math.cos(a), cy - (r + .8) * math.sin(a), ACC, 3, arrow=True)
    f.text(cx + 1.0, cy - 2.0, 1.9, 'Ṙ(0) = U₀', 14, ACC, bold=True)
    for k in range(4):
        f.line(.7 + k * 1.1, 5.65, .7 + k * 1.1, 5.2, MUT, 1.5, arrow=True, opacity=.6)
    f.text(.55, 5.7, 4.4, 'far field r → ∞:  u → 0,  p → p∞(t)', 13, FG)
    t, R, V, _ = rp_solve(5e-6, 10.0, 1.6e-6, pg0=0.8e6, n=1500)
    ymax = float(math.ceil(R.max() / 5e-6 * 1.08))
    p = Plot(f, 6.2, 1.5, 6.3, 4.3, (0, 1.6), (0, ymax), 't  (µs)', 'R(t) / R₀', (0, .4, .8, 1.2, 1.6), tuple(range(0, int(ymax) + 1, max(1, int(ymax) // 4))), fx='{:.1f}')
    p.curve(t * 1e6, R / 5e-6, ACC, 2.8)
    p.pt(0, 1, WARM)
    s = (10.0 / 5e-6) * 1e-6
    p.seg(0, 1, min(.6, (ymax - 1) / s), 1 + s * min(.6, (ymax - 1) / s), WARM, 1.8, dash=True)
    p.label(.05, 1.0, 'start: R₀ and slope Ṙ(0) = U₀', WARM, 12.5, w=3.4, dx=.15, dy=.12)
    p.label(.9, ymax * .55, 'R(t) afterwards', ACC, 12.5, w=2.2)
    f.text(6.2, 6.45, 6.5, 'Both initial values and the far-field pressure p∞(t) are inputs, not results.', 13, FG)
    f.note('Trajectory: Rayleigh–Plesset solution for an illustrative 5 µm gas bubble (Eq. C1-E07), drawn only to mark the initial data.')


def e02(f):
    cx, cy, R = 2.75, 3.6, .65
    f.rect(.4, 1.0, 4.7, 5.3, fill=LIQ, line=LIQ2, lw=1.5, round_=True)
    f.text(.55, 1.07, 4.4, 'Concentric shells carry one flux', 14, ACC, bold=True)
    ms = [1.0, 1.6, 2.3, 3.2]
    for k, m in enumerate(ms):
        f.ellipse(cx, cy, R * m, fill=None, line=LIQ2 if k else WARM, lw=1.3 if k else 2)
    f.bubble(cx, cy, R, rim=WARM)
    for k, (m, ang) in enumerate(zip(ms, (80, 55, 30, 5))):
        a = math.radians(ang)
        L = .75 / m ** 2 + .12
        x1, y1 = cx + R * m * math.cos(a), cy - R * m * math.sin(a)
        f.line(x1, y1, x1 + L * math.cos(a), y1 - L * math.sin(a), ACC, 2.6, arrow=True)
        f.text(x1 + (L + .08) * math.cos(a) - .05, y1 - (L + .08) * math.sin(a) - .12, 1.1, f'{1 / m ** 2:.2f} Ṙ', 11.5, FG, wrap=False)
    f.text(.55, 5.55, 4.4, 'Shell area grows as r², so the radial speed falls as 1/r². Arrow length = speed.', 12.5, FG)
    x = np.linspace(1, 4, 120)
    p = Plot(f, 6.1, 1.5, 6.4, 4.3, (1, 4), (0, 1.25), 'r / R', 'dimensionless', (1, 2, 3, 4), (0, .25, .5, .75, 1.0), fy='{:.2f}')
    p.curve(x, 1 / x ** 2, ACC, 3)
    p.curve(x, np.ones_like(x), WARM, 2.4, dash=True)
    p.pt(2, .25, ACC)
    p.label(2, .25, 'u(2R) = Ṙ/4', ACC, 13, w=1.8, dx=.14, dy=-.4)
    p.label(1.2, 1.2, 'r²u / (R²Ṙ) = 1 on every shell', WARM, 12.5, w=4.4, dy=-.05)
    p.label(2.5, .62, 'u / Ṙ = (R/r)²', ACC, 13, w=2.4)
    f.text(6.1, 6.45, 6.4, 'From ∇·u = 0: r²u = C(t). The wall condition u(R) = Ṙ gives C = R²Ṙ.', 13, FG)
    f.note('Curves from u = R²Ṙ/r² (Eq. C1-E02).')


def e03(f):
    x = np.linspace(1, 5, 150)
    p = Plot(f, .95, 1.5, 6.3, 4.3, (1, 5), (-1.05, 0), 'r / R', 'φ / (R Ṙ)', (1, 2, 3, 4, 5), (-1, -.75, -.5, -.25, 0), fy='{:.2f}')
    p.curve(x, -1 / x, ACC, 3)
    p.label(2.9, -.55, 'φ = −R²Ṙ / r → 0 at infinity', ACC, 13, w=3.0, dy=-.5)
    x0 = 1.6
    sl = 1 / x0 ** 2
    p.pt(x0, -1 / x0, WARM)
    p.seg(x0 - .5, -1 / x0 - sl * .5, x0 + .9, -1 / x0 + sl * .9, WARM, 1.8, dash=True)
    p.label(x0, -1 / x0, 'tangent slope at r = 1.6R is u = (R/r)²Ṙ = 0.39 Ṙ', WARM, 12, w=3.6, dx=.5, dy=.3)
    f.panel(7.7, 1.45, 5.25, 4.9, 'Derivation in three moves', ACC)
    steps = [('1  Start from the flux law', 'u(s) = R²Ṙ / s²'),
             ('2  Integrate inward from infinity', 'φ(r) = ∫ u ds from ∞ to r\nφ(r) = −R²Ṙ / r'),
             ('3  Differentiate in space', '∂φ/∂r = R²Ṙ / r² = u  ✓'),
             ('Why the reference is fixed first', 'φ is defined only up to a constant. Setting φ(∞) = 0 before taking any time derivative keeps Eq. C1-E04 unambiguous.')]
    y = 1.95
    for h, b in steps:
        y = f.text(7.9, y, 4.9, h, 13, WARM, bold=True)
        y = f.text(8.05, y, 4.7, b, 12.5, FG) + .16
    f.text(.95, 6.45, 6.3, 'Plot for R = 1, Ṙ = 1; the shape is the same for any R and Ṙ.', 12.5, MUT)
    f.note('Potential from Eq. C1-E03.')


def e04(f):
    cx, cy, R = 2.5, 3.5, .8
    f.rect(.4, 1.0, 4.4, 5.3, fill=LIQ, line=LIQ2, lw=1.5, round_=True)
    f.text(.55, 1.07, 4.1, 'Two observers, one potential', 14, ACC, bold=True)
    f.bubble(cx, cy, R)
    f.ellipse(cx, cy, R * 1.3, fill=None, line=WARM, lw=1.3, opacity=.7)
    f.line(cx + R * 1.0, cy - R * 1.0, cx + R * 1.55, cy - R * 1.55, WARM, 2.4, arrow=True)
    f.text(cx + .3, cy - 2.05, 2.3, 'wall point moves outward', 12, WARM)
    f.dot(cx + 1.9, cy + .8, .1, ACC)
    f.text(cx + .7, cy + .98, 1.9, 'fixed point r = 2R', 12, ACC)
    f.text(.55, 5.35, 4.1, 'The fixed point feels φ change only because R(t) changes. A point riding the wall also moves to larger r.', 12.5, FG)
    vals = [('∂φ/∂t at fixed r = 2R', -(2 - .5) / 2, ACC), ('∂φ/∂t at fixed r = R', -(2 - .5), BLUE), ('dφ/dt following the wall', -1 + .5, WARM)]
    f.text(5.2, 1.05, 7.7, 'Three derivatives for R = 1, Ṙ = 1, R̈ = −0.5', 14, ACC, bold=True)
    zero, w = 11.4, 3.6
    f.line(zero, 1.6, zero, 4.6, MUT, 1.3)
    for i, (s, v, col) in enumerate(vals):
        y = 1.85 + i * .95
        f.text(5.2, y, 3.2, s, 13, FG)
        f.rect(zero + v / 2 * w, y + .02, abs(v) / 2 * w, .45, fill=col, line=col, lw=1)
        f.text(zero + .12, y + .05, .9, f'{v:+.2f}', 13, FG, bold=True)
    f.panel(5.2, 4.8, 7.7, 1.15, None, MUT)
    f.text(5.35, 4.88, 7.4, 'Chain rule at the wall:   dφ/dt = ∂φ/∂t + Ṙ ∂φ/∂r\n−0.5 = −1.5 + (1)(1)', 14, FG, bold=True)
    f.text(5.2, 6.2, 7.7, 'Using the wrong derivative changes the wall pressure of Eq. C1-E05 by a whole Ṙ² term.', 13, WARM)
    f.note('Values from Eq. C1-E04 with R = 1, Ṙ = 1, R̈ = −0.5 (units m² s⁻²).')


def e05(f):
    x = np.linspace(1, 4, 150)

    def prof(Rd_, Rdd_):
        return (Rdd_ + 2 * Rd_ ** 2) / x - Rd_ ** 2 / (2 * x ** 4)
    p = Plot(f, .95, 1.5, 5.9, 4.3, (1, 4), (-1, 4), 'r / R', '(p − p∞) / ρ', (1, 2, 3, 4), (-1, 0, 1, 2, 3, 4), fy='{:g}')
    p.seg(1, 0, 4, 0, GRID, 1.2)
    ya, yb = prof(1, -.5), prof(-1, 2)
    p.curve(x, ya, ACC, 2.8)
    p.curve(x, yb, WARM, 2.8)
    p.pt(1, ya[0], ACC)
    p.pt(1, yb[0], WARM)
    p.label(2.6, 1.05, 'expanding, slowing\nṘ = 1, R̈ = −0.5', ACC, 12, w=2.2)
    p.label(1.7, 3.9, 'collapsing, decelerating\nṘ = −1, R̈ = +2', WARM, 12, w=2.6, dy=-.15)
    f.panel(7.2, 1.45, 5.75, 3.55, 'The wall value has three pieces', ACC)
    f.text(7.35, 1.95, 5.5, 'p_l − p∞ = ρ [ R R̈ + 2Ṙ² − Ṙ²/2 ]', 14, FG, bold=True)
    rows = [('R R̈', 'wall acceleration', -.5, BLUE), ('2Ṙ²', 'unsteady potential', 2.0, ACC), ('−Ṙ²/2', 'Bernoulli kinetic term', -.5, PINK)]
    zero = 10.9
    f.line(zero, 2.5, zero, 4.05, MUT, 1.2)
    for i, (a, b, v, col) in enumerate(rows):
        y = 2.5 + i * .5
        f.text(7.35, y, 1.0, a, 13, col, bold=True)
        f.text(8.3, y + .02, 2.1, b, 11, MUT)
        f.rect(zero if v > 0 else zero + v * .55, y + .05, abs(v) * .55, .3, fill=col, line=col, lw=1)
    f.text(7.35, 4.2, 5.5, 'Expanding case: −0.5 + 2 − 0.5 = 1.0 = R R̈ + 3Ṙ²/2', 12.5, WARM)
    f.text(7.2, 5.2, 5.75, 'The pressure is stored in the liquid by its inertia: p_l exceeds p∞ whenever R R̈ + 3Ṙ²/2 > 0.', 13, FG)
    f.text(7.2, 6.1, 5.75, 'Far away the acceleration term decays as 1/r, the Ṙ² term as 1/r⁴.', 12.5, MUT)
    f.note('Profile: p − p∞ = ρ[(R²R̈ + 2RṘ²)/r − R⁴Ṙ²/(2r⁴)] from the unsteady Bernoulli equation, R = 1.')


def e06(f):
    cx, cy, R = 2.5, 3.5, 1.0
    f.rect(.4, 1.0, 4.4, 5.3, fill=LIQ, line=LIQ2, lw=1.5, round_=True)
    f.text(.55, 1.07, 4.1, 'Stresses on the wall of a collapsing bubble', 13.5, ACC, bold=True)
    f.bubble(cx, cy, R)
    f.text(cx - .6, cy - .12, 1.2, 'p_b', 14, WARM, 'center', bold=True)
    for a, col, lbl, dr in [(40, WARM, 'p_b', 1), (140, ACC, 'p_l', -1), (220, PINK, '2σ/R', -1), (320, BLUE, '4μṘ/R', -1)]:
        r1, r2 = (R - .5, R + .05) if dr > 0 else (R + .6, R + .02)
        t = math.radians(a)
        f.line(cx + r1 * math.cos(t), cy - r1 * math.sin(t), cx + r2 * math.cos(t), cy - r2 * math.sin(t), col, 2.8, arrow=True)
        f.text(cx + (R + .95) * math.cos(t) - .55, cy - (R + .95) * math.sin(t) - .12, 1.1, lbl, 13, col, 'center', bold=True)
    f.text(.55, 5.2, 4.1, 'Gas pushes out; tension pulls in; viscosity resists the strain rate ∂u/∂r = −2Ṙ/R at the wall.', 12.5, FG)
    pb, st, vi = 120.0, 14.4, 2.0
    pl = pb - st + vi
    p = Plot(f, 5.9, 1.5, 6.9, 4.3, (0, 4), (0, 140), '', 'pressure (kPa)', (), (0, 40, 80, 120), fy='{:g}')
    cols = [(WARM, 0, pb, 'p_b = 120'), (PINK, pb - st, pb, '−2σ/R = −14.4'), (BLUE, pb - st, pl, '−4μṘ/R = +2.0'), (ACC, 0, pl, 'p_l = 107.6')]
    for i, (c, lo, hi, s) in enumerate(cols):
        xa = i + .12
        f.rect(p.X(xa), p.Y(hi), p.X(xa + .76) - p.X(xa), p.Y(lo) - p.Y(hi), fill=c, line=c, lw=1, opacity=.85)
        f.text(p.X(xa) - .3, p.Y(hi) - .32, 1.4, s, 11.5, FG, 'center', wrap=False)
    f.text(5.9, 6.2, 6.9, 'R = 10 µm, σ = 0.072 N/m, μ = 1 mPa·s, Ṙ = −5 m/s, p_b = 120 kPa', 11.5, MUT)
    f.text(5.9, 6.55, 6.9, 'Inward motion makes the viscous term raise p_l; tension always lowers it.', 13, WARM)
    f.note('Boundary condition p_l = p_b − 2σ/R − 4μṘ/R (Eq. C1-E06); numbers computed from it.')


def e07(f):
    R0 = 5e-6
    t, R, V, pb = rp_solve(R0, 0.0, 1.5e-6, pg0=1.0e6, n=3000)
    t2, R2, V2, _ = rp_solve(R0, 0.0, 1.5e-6, pg0=1.0e6, sigma=0.0, mu=0.0, n=3000)
    p = Plot(f, .95, 1.5, 6.3, 3.9, (0, 1.5), (0, 3.2), 't  (µs)', 'R / R₀', (0, .5, 1.0, 1.5), (0, 1, 2, 3), fx='{:.1f}')
    p.curve(t * 1e6, R / R0, ACC, 3)
    p.curve(t2 * 1e6, R2 / R0, MUT, 1.9, dash=True)
    p.label(.05, 3.18, 'with surface tension and viscosity', ACC, 12.5, w=4, dy=-.05)
    p.label(.05, 2.85, 'ideal: σ = μ = 0, same start', MUT, 12.5, w=4, dy=-.05)
    dt = t[1] - t[0]
    acc_fd = np.gradient(np.gradient(R, dt), dt)
    i = int(np.argmax(np.abs(V)))
    j = i + 60
    lhs = 1000 * (R[j] * acc_fd[j] + 1.5 * V[j] ** 2)
    terms = [('ρ(RR̈ + 3Ṙ²/2)', lhs, ACC), ('p_b − p∞', pb[j] - 101325, WARM), ('−2σ/R', -2 * 0.072 / R[j], PINK), ('−4μṘ/R', -4e-3 * V[j] / R[j], BLUE)]
    f.panel(7.6, 1.45, 5.35, 4.1, 'Every term is a pressure', ACC, size=13.5)
    mx = max(abs(v) for _, v, _ in terms)
    zero = 10.4
    f.line(zero, 2.0, zero, 4.45, MUT, 1.2)
    for k, (s, v, c) in enumerate(terms):
        y = 2.05 + k * .6
        f.text(7.75, y + .02, 2.3, s, 12, c, bold=True)
        wd = abs(v) / mx * 1.5
        f.rect(zero if v > 0 else zero - wd, y + .05, max(wd, .03), .32, fill=c, line=c, lw=1)
        f.text(zero + (wd if v > 0 else 0) + .06 if v > 0 else zero + .08, y + .05, 1.5, f'{v / 1e3:+.0f} kPa', 11.5, FG)
    rhs = sum(v for _, v, _ in terms[1:])
    f.text(7.75, 4.55, 5.0, f't = {t[j] * 1e6:.2f} µs.  Left side from finite-difference R̈ of the solution; right side from the pressures.  Mismatch {abs(lhs - rhs) / abs(rhs) * 100:.1f} %.', 11, MUT)
    f.text(.95, 6.2, 12, 'One scalar equation for R(t): liquid inertia on the left, driving and resisting pressures on the right.', 13.5, FG)
    f.text(.95, 6.6, 12, 'Gas pressure here is polytropic, p_b = p_g0 (R₀/R)^{3γ}, γ = 1.4, p_g0 = 1 MPa: an illustration of the closure still to be supplied.', 11.5, MUT)
    f.note('Numerical integration of Eq. C1-E07; R₀ = 5 µm, ρ = 1000 kg/m³, p∞ = 101.3 kPa, σ = 0.072 N/m, μ = 1 mPa·s.')


def e08(f):
    Ts = [303.0, 313.0, 323.0, 333.0]
    pg = 0.05
    p = Plot(f, 6.0, 1.5, 6.8, 4.0, (0, 4), (0, 4.2), '', 'partial pressure (bar)', (), (0, 1, 2, 3, 4), fy='{:g}')
    for i, T in enumerate(Ts):
        a, b = psat_pfp(T) / 1e5, psat_water(T) / 1e5
        tot = a + b + pg
        xa = i + .17
        bw = p.X(xa + .66) - p.X(xa)
        y = 0
        for v, c in ((a, ACC), (b, BLUE), (pg, WARM)):
            f.rect(p.X(xa), p.Y(y + v), bw, p.Y(y) - p.Y(y + v), fill=c, line=c, lw=1, opacity=.85)
            y += v
        f.text(p.X(xa) - .25, p.Y(tot) - .32, bw + .5, f'p_b = {tot:.2f}', 12, FG, 'center', bold=True, wrap=False)
        f.text(p.X(xa) - .2, p.Y(0) + .09, bw + .4, f'{T - 273.15:.0f} °C', 11.5, MUT, 'center')
    f.text(5.5, 5.95, 7.5, 'Bars are saturation values (upper bounds) from C2-E12 and C2-E13. The 0.05 bar gas part is an assumed placeholder.', 12, MUT)
    for i, (s, c) in enumerate([('PFC vapor', ACC), ('water vapor', BLUE), ('permanent gas', WARM)]):
        f.rect(5.5 + i * 2.5, 6.58, .25, .22, fill=c, line=c, lw=1)
        f.text(5.82 + i * 2.5, 6.52, 2.2, s, 12, FG, wrap=False)
    f.panel(.4, 1.0, 4.6, 5.5, 'Dalton additivity in one bubble', ACC, size=13.5)
    f.text(.55, 1.55, 4.3, 'p_b = p_v,PFC + p_v,w + p_g', 14.5, WARM, bold=True)
    f.ellipse(2.7, 3.7, 1.45, fill=GASC, line=WARM, lw=2.2)
    rnd = random.Random(4)
    for c in [ACC] * 9 + [BLUE] * 5 + [WARM] * 3:
        a, r = rnd.random() * 6.28, 1.15 * math.sqrt(rnd.random())
        f.dot(2.7 + r * math.cos(a), 3.7 + r * math.sin(a), .08, c)
    f.text(.55, 5.35, 4.3, 'PFC vapor, water vapor and permanent gas fill one volume at one temperature; their pressures add.', 12.5, FG)
    f.note('The radius equation needs p_b from the contents (a thermodynamic closure), not from R alone.')


def e09(f):
    x = np.linspace(1, 6, 200)
    p = Plot(f, .95, 1.5, 6.0, 4.0, (1, 6), (0, 1.05), 'r / R', 'K(<r) / K(∞)', (1, 2, 3, 4, 5, 6), (0, .25, .5, .75, 1.0), fy='{:.2f}')
    p.curve(x, 1 - 1 / x, ACC, 3)
    p.hline(1.0, WARM)
    p.pt(2, .5, WARM)
    p.label(2, .5, '50 % inside r = 2R', WARM, 12.5, w=2.4, dx=.14, dy=.04)
    p.pt(4, .75, WARM)
    p.label(4, .75, '75 % inside r = 4R', WARM, 12.5, w=2.4, dx=.14, dy=.04)
    p.label(2.6, 1.0, 'K(∞) = 2πρR³Ṙ² is finite', WARM, 12, w=3.2, dy=.04)
    f.panel(7.3, 1.45, 5.65, 4.7, 'Energy lives in thin shells', ACC)
    f.text(7.45, 1.95, 5.4, 'dK = ½ρu² · 4πr² dr  ∝  r⁻² dr', 13.5, FG, bold=True)
    cx, cy, R = 10.1, 3.75, .45
    for k, m in enumerate([3.2, 2.5, 1.9, 1.45, 1.15]):
        f.ellipse(cx, cy, R * m, fill=LIQ if k % 2 == 0 else LIQ2, line=MUT, lw=.8, opacity=.85)
    f.bubble(cx, cy, R, rim=WARM)
    f.text(7.45, 5.3, 5.4, 'u² ∝ r⁻⁴ but shell volume ∝ r²: the integrand falls as r⁻², so even an infinite liquid holds finite energy.', 12.5, FG)
    f.text(.95, 6.27, 12, 'K_l = ∫ ½ρu² 4πr² dr = 2πρR⁴Ṙ² ∫ r⁻² dr = 2πρR³Ṙ²', 13.5, FG, bold=True)
    f.text(.95, 6.7, 12, 'Half of it is within one extra bubble radius of the wall.', 13, WARM)
    f.note('Cumulative fraction K(<r)/K = 1 − R/r from Eq. C1-E09.')


FIGS = {1: e01, 2: e02, 3: e03, 4: e04, 5: e05, 6: e06, 7: e07, 8: e08, 9: e09}
