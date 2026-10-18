"""Chapter 3, equations 01-11."""
import math

import numpy as np
from scipy.stats import binom

from figlib import *
from figphys import rp_solve, collapse_S, C_chi, speed_S

RHO, DPC, RMAX = 1000.0, 1e5, 30e-6


def e01(f):
    N, pa = 25, 0.95
    k = np.arange(10, 26)
    pm = binom.pmf(k, N, pa)
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (9.4, 25.6), (0, .42), 'activated sites N_b', 'probability', (10, 15, 20, 25), (0, .1, .2, .3, .4), fx='{:g}', fy='{:.1f}')
    for kk, v in zip(k, pm):
        c = WARM if kk == N else ACC
        f.rect(p.X(kk - .4), p.Y(v), p.X(kk + .4) - p.X(kk - .4), p.Y(0) - p.Y(v), fill=c, line=c, lw=1, opacity=.85)
    p.vline(N * pa, PINK)
    p.label(N * pa, .41, 'mean 23.75', PINK, 12.5, w=1.6, dx=-1.7, dy=0)
    p.label(N, pm[-1], 'all 25: 27.7 %', WARM, 12.5, w=1.9, dx=-2.0, dy=-.5)
    f.panel(7.9, 1.5, 5.05, 4.0, 'N_d = 25 independent sites, p_a = 0.95', ACC, size=13)
    cv = math.sqrt((1 - pa) / (N * pa))
    rows = [('E[N_b] = N_d p_a', f'{N * pa:.2f}'), ('Var(N_b) = N_d p_a (1 − p_a)', f'{N * pa * (1 - pa):.4f}'), ('CV = √[(1 − p_a)/(N_d p_a)]', f'{cv * 100:.3f} %'), ('Pr(N_b = N_d) = p_a^N_d', f'{pa ** N:.5f}')]
    y = 2.0
    for a, b in rows:
        f.text(8.05, y, 3.5, a, 12, FG)
        f.text(11.4, y, 1.4, b, 13, WARM, bold=True, wrap=False)
        y += .55
    f.text(8.05, 4.35, 4.8, 'Count reproducibility (CV small) and complete activation (all 25) are different tests: here CV is 4.6 % but all 25 fire in only 28 % of shots.', 12, FG)
    f.text(1.0, 6.27, 12, 'Binomial model: sites activate independently with the same probability; common heating or feedback would break that assumption.', 12.5, MUT)
    f.note('Statistics of Eq. C3-E01 (exact binomial distribution).')


def e02(f):
    cx, cy, w_in = 2.7, 3.7, 1.85
    f.panel(.4, 1.0, 4.6, 5.3, 'Array inside the beam', ACC, size=13.5)
    for i in range(22, 0, -1):
        r = 2.0 * i / 22
        f.ellipse(cx, cy, r, fill=ACC, line=ACC, lw=0, opacity=max(.05, .75 * math.exp(-2 * (r / w_in) ** 2)))
    f.ellipse(cx, cy, w_in, fill=None, line=WARM, lw=2)
    f.text(cx - .3, cy - w_in - .35, 1.4, 'beam w', 11.5, WARM, bold=True)
    RA = w_in / 4.357
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            f.ellipse(cx + dx * RA * .6, cy + dy * RA * .6, .045, fill=FG, line=FG, lw=1)
    f.ellipse(cx, cy, RA, fill=None, line=PINK, lw=2.4)
    f.text(cx + .1, cy + RA + .05, 1.3, 'R_A', 12, PINK, bold=True)
    f.text(.55, 5.6, 4.3, 'Wide beam, small array: edge sites receive nearly the same fluence as the centre.', 12, FG)
    eps = np.linspace(.01, .3, 200)
    p = Plot(f, 6.3, 1.5, 6.5, 4.0, (0, .3), (0, 12), 'allowed edge decrease ε', 'required beam radius  w / R_A', (0, .1, .2, .3), (0, 3, 6, 9, 12), fx='{:.1f}', fy='{:g}')
    p.curve(eps, np.sqrt(2 / (-np.log(1 - eps))), ACC, 3)
    for e_, c in [(.1, WARM), (.05, BLUE), (.02, PINK)]:
        v = math.sqrt(2 / (-math.log(1 - e_)))
        p.pt(e_, v, c)
        p.label(e_, v, f'ε = {e_:g}: w ≥ {v:.2f} R_A', c, 12, w=2.4, dx=.12 if e_ > .03 else .1, dy=-.1)
    f.text(6.3, 6.27, 6.5, 'w ≥ R_A √[ 2 / (−ln(1 − ε)) ].  A 10 % edge drop needs w = 4.357 R_A.', 13, FG, bold=True)
    f.note('Optical-uniformity condition of Eq. C3-E02; this is checked before any cavity mechanics.')


def e03(f):
    f.panel(.4, 1.0, 5.6, 5.3, 'A moving sphere is a monopole source', ACC, size=13.5)
    cx, cy = 1.5, 3.7
    f.bubble(cx, cy, .45)
    f.text(cx - .55, cy - .95, 1.2, 'bubble j', 12, WARM, 'center', bold=True)
    f.line(cx + .55, cy, cx + .95, cy, ACC, 2.5, arrow=True)
    f.dim(cx, cy + .9, 4.8, cy + .9, 'd_ij', MUT, 12.5)
    f.dot(4.8, cy, .09, PINK)
    f.text(4.2, cy - .6, 1.6, 'receiving\ncentre i', 11.5, PINK, 'center', bold=True)
    for k in (.85, 1.1):
        f.ellipse(cx, cy, k, fill=None, line=LIQ2, lw=1.2, opacity=.9)
    f.text(.6, 5.55, 5.3, 'Flux through every sphere is the same: 4πr²u = 4πR²Ṙ.', 12, FG)
    r = np.linspace(1, 10, 200)
    Rv, V, A = 1.0, 1.0, -.4
    p = Plot(f, 7.0, 1.5, 5.8, 3.5, (1, 10), (-2.2, 0), 'd_ij / R_j', '∂ₜφ_j at d_ij', (1, 2, 5, 10), (-2, -1.5, -1, -.5, 0), fx='{:g}', fy='{:.1f}')
    p.curve(r, -(2 * Rv * V ** 2 + Rv ** 2 * A) / r, ACC, 3)
    p.label(2.2, -1.0, '∂ₜφ_j = −(2R_jṘ_j² + R_j²R̈_j) / d_ij', ACC, 11.5, w=3.8, dy=-.1)
    p.pt(5, -(2 * Rv * V ** 2 + Rv ** 2 * A) / 5, WARM)
    p.label(5, -(2 * Rv * V ** 2 + Rv ** 2 * A) / 5, 'falls as 1/d', WARM, 12, w=1.5, dx=.12, dy=-.45)
    f.text(7.0, 5.8, 5.8, 'φ_j = −R_j²Ṙ_j / r_j  (zero at infinity).  Units R = Ṙ = 1, R̈ = −0.4.', 12, MUT)
    f.text(.5, 6.45, 12.4, 'The neighbour feels a potential that depends on the source history through R_j, Ṙ_j, R̈_j and falls off with distance.', 12.5, WARM)
    f.note('Monopole potential of Eq. C3-E03.')


def e04(f):
    t, R, V, pb = rp_solve(5e-6, 0.0, 1.0e-6, pg0=1e6, n=3000)
    dt = t[1] - t[0]
    acc = np.gradient(np.gradient(R, dt), dt)
    i = int(np.argmax(np.abs(acc[10:-10]))) + 10
    Ri, Vi, Ai = R[i], V[i], acc[i]
    d = np.linspace(15e-6, 100e-6, 200)
    pp = 1000 * (Ri ** 2 * Ai + 2 * Ri * Vi ** 2) / d
    ymx = math.ceil(pp.max() / 1e5) / 10
    p = Plot(f, 7.6, 1.5, 5.2, 4.0, (15, 100), (0, ymx * 1.05), 'distance d_ij  (µm)', 'p′ (MPa)', (20, 40, 60, 80, 100), tuple(round(ymx * k / 4, 2) for k in range(5)), fx='{:g}', fy='{:.2f}')
    p.curve(d * 1e6, pp / 1e6, ACC, 3)
    p.label(30, ymx * .85, "p′ = ρ(R_j²R̈_j + 2R_jṘ_j²) / d_ij", ACC, 12, w=4.5)
    f.panel(.4, 1.0, 6.2, 5.3, 'Neighbours add pressure at i', ACC, size=13.5)
    cx, cy = 3.5, 3.6
    f.bubble(cx, cy, .45, rim=PINK)
    f.text(cx - .4, cy - .15, .8, 'i', 14, PINK, 'center', bold=True)
    for k, (ang, dist) in enumerate([(20, 1.8), (110, 1.4), (200, 1.9), (290, 1.5)]):
        a = math.radians(ang)
        bx, by = cx + dist * math.cos(a), cy - dist * math.sin(a)
        f.bubble(bx, by, .3)
        f.line(bx - .3 * math.cos(a), by + .3 * math.sin(a), cx + .55 * math.cos(a), cy - .55 * math.sin(a), ACC, 2.4, arrow=True)
    f.text(.55, 5.35, 5.8, 'p_ext,i ≈ p∞ + Σ_{j≠i} p′_{j→i}: each source changes the surrounding pressure; none adds energy.', 12, FG)
    f.text(6.9, 6.3, 6.0, f'Snapshot of fastest wall acceleration of a 5 µm bubble: R = {Ri * 1e6:.1f} µm, Ṙ = {Vi:.0f} m/s, R̈ = {Ai:.1e} m/s².', 11.5, MUT)
    f.note('Leading unsteady-Bernoulli correction of Eq. C3-E04; snapshot from a Rayleigh–Plesset run (p_g0 = 1 MPa).')


def e05(f):
    R0 = 5e-6
    pg0 = 1e6

    def run(d):
        def rhs(t, y):
            R, V = y
            pb = pg0 * (R0 / R) ** 4.2
            B = (pb - 101325 - 2 * .072 / R - 4e-3 * V / R) / RHO
            if d is None:
                return [V, (B - 1.5 * V * V) / R]
            return [V, (B - 1.5 * V * V - 2 * R * V * V / d) / (R + R * R / d)]
        from scipy.integrate import solve_ivp
        sol = solve_ivp(rhs, (0, 1.5e-6), [R0, 0.0], t_eval=np.linspace(0, 1.5e-6, 600), rtol=1e-10, atol=1e-16)
        return sol.t, sol.y[0]
    p = Plot(f, 1.0, 1.5, 6.5, 4.0, (0, 1.5), (0, 3.2), 't  (µs)', 'R / R₀', (0, .5, 1, 1.5), (0, 1, 2, 3), fx='{:.1f}', fy='{:g}')
    for d, c, lab in [(None, ACC, 'isolated bubble'), (30e-6, WARM, 'neighbour at d = 30 µm'), (15e-6, PINK, 'neighbour at d = 15 µm')]:
        t, R = run(d)
        p.curve(t * 1e6, R / R0, c, 3)
    for i, (c, lab) in enumerate([(ACC, 'isolated bubble'), (WARM, 'identical neighbour, d = 30 µm'), (PINK, 'identical neighbour, d = 15 µm')]):
        f.rect(1.3, 1.62 + i * .36, .3, .2, fill=c, line=c, lw=1)
        f.text(1.72, 1.57 + i * .36, 4.2, lab, 12, c, wrap=False)
    f.panel(7.8, 1.5, 5.15, 4.0, 'Same equation, extra inertia', ACC, size=13.5)
    f.text(7.95, 2.0, 4.9, 'R_iR̈_i + (3/2)Ṙ_i² + Σ (R_j²R̈_j + 2R_jṘ_j²)/d_ij = B_i', 12, FG, bold=True)
    f.text(7.95, 2.85, 4.9, 'B_i = [p_b,i − p∞ − 2σ_b/R_i − 4μṘ_i/R_i] / ρ  (isolated driving)', 11.5, MUT)
    f.bullets(7.95, 3.6, 4.9, ['Identical neighbours move together, so the extra term acts as added liquid mass.', 'The closer the neighbour, the slower the expansion.', 'Energy is shared, not created.'], 12)
    f.text(1.0, 6.27, 12, 'Two identical bubbles (p_g0 = 1 MPa, γ = 1.4) integrated with the coupled equation of Eq. C3-E05.', 12.5, FG)
    f.note('Coupled spherical approximation of Eq. C3-E05 for N = 2 identical bubbles.')


def e06(f):
    phi = (1 + math.sqrt(5)) / 2
    S = {3: 2.0, 4: 2 + 1 / math.sqrt(2), 5: 2 + 2 / phi}
    for k, (N, cx) in enumerate([(3, 2.4), (4, 6.6), (5, 10.8)]):
        cy = 3.65
        r = 1.35
        pts = [(cx + r * math.sin(2 * math.pi * j / N), cy - r * math.cos(2 * math.pi * j / N)) for j in range(N)]
        f.poly(pts, fill=LIQ, line=ACC, lw=1.6)
        for a in range(N):
            for b in range(a + 2, N):
                if not (a == 0 and b == N - 1):
                    f.line(pts[a][0], pts[a][1], pts[b][0], pts[b][1], MUT, 1.1, dash=True)
        for (x, y) in pts:
            f.bubble(x, y, .2, rim=WARM)
        f.text(cx - 1.4, 5.15, 2.8, f'N = {N}', 15, ACC, 'center', bold=True)
        f.text(cx - 1.6, 5.5, 3.2, f'S_{N} s = {S[N]:.4f}', 14, WARM, 'center', bold=True)
    f.text(.5, 1.05, 12.3, 'Regular polygons of N bubbles, neighbouring distance s', 14, ACC, bold=True)
    f.text(.5, 1.5, 12.3, 'd_k = s sin(kπ/N) / sin(π/N),   S_N = Σ_{k=1}^{N−1} 1/d_k', 14, FG, bold=True)
    f.text(.5, 6.0, 12.3, 'S₃ = 2/s,   S₄ = (2 + 1/√2)/s,   S₅ = (2 + 2/φ)/s,   φ = (1 + √5)/2', 13.5, FG)
    f.text(.5, 6.5, 12.3, 'Every bubble sees the same sum of reciprocal distances, so they can share one radius history in this constrained control.', 12.5, WARM)
    f.note('Exact polygon geometry of Eq. C3-E06 (chords drawn dashed).')


def _chis():
    return [(0.0, ACC), (1.0, WARM), (3.0, PINK)]


def e07(f):
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (0, 4.5), (0, 1.05), 't  (µs)', 'R / R_max', (0, 1, 2, 3, 4), (0, .25, .5, .75, 1), fx='{:g}', fy='{:.2f}')
    for chi, c in _chis():
        t, R, V = collapse_S(RMAX, RHO, DPC, chi / RMAX, 8e-6)
        p.curve(t * 1e6, R / RMAX, c, 3)
        p.vline(t[-1] * 1e6, c, dash=True, width=1)
    for i, (chi, c) in enumerate(_chis()):
        f.rect(1.3, 4.2 + i * .36, .3, .2, fill=c, line=c, lw=1)
        f.text(1.72, 4.15 + i * .36, 4.2, f'χ = S R_max = {chi:g}' + ('  (no neighbours)' if chi == 0 else ''), 12, c, wrap=False)
    f.panel(7.9, 1.5, 5.05, 4.0, 'Symmetric constant-pressure control', ACC, size=13)
    f.text(8.05, 2.0, 4.8, '(1 + SR) R R̈ + (3/2 + 2SR) Ṙ² = −Δp_c / ρ', 12.5, FG, bold=True)
    f.bullets(8.05, 2.75, 4.8, ['S = S_N is the reciprocal-distance sum from the polygon.', 'Start at rest at R_max: R(0) = R_max, Ṙ(0) = 0.', 'Larger χ means stronger coupling and a later collapse.', 'Surface tension and viscosity are omitted in this ideal control.'], 12)
    f.text(1.0, 6.27, 12, 'Inputs: R_max = 30 µm, ρ = 1000 kg/m³, Δp_c = 100 kPa. Dashed lines mark each collapse time.', 12.5, MUT)
    f.note('Numerical integration of Eq. C3-E07.')


def e08(f):
    x = np.linspace(.02, 1, 300)
    p = Plot(f, 7.6, 1.5, 5.3, 3.9, (.2, 1), (0, 16), 'x = R / R_max', 'coefficient × R_max', (.2, .4, .6, .8, 1), (0, 4, 8, 12, 16), fx='{:.1f}', fy='{:g}')
    chi = 1.0
    full = (3 + 4 * chi * x) / (x * (1 + chi * x))
    p.curve(x, full, WARM, 3)
    p.curve(x, 3 / x, ACC, 2, dash=True)
    p.curve(x, chi / (1 + chi * x), PINK, 2, dash=True)
    p.label(.3, 15.5, '(3 + 4SR)/[R(1 + SR)], χ = 1', WARM, 11.5, w=3.4, dy=-.05)
    p.label(.62, 6.2, '3/R', ACC, 12, w=.8)
    p.label(.55, 1.5, 'S/(1 + SR)', PINK, 12, w=1.6)
    f.panel(.4, 1.0, 6.6, 5.3, 'Rebuilding the integrating factor', ACC, size=13.5)
    steps = [('y = Ṙ²,  dy/dR = 2R̈', 'turns the radial equation into a first-order ODE for y(R)'), ('y′ + [(3 + 4SR)/(R(1 + SR))] y = −2Δp_c / [ρR(1 + SR)]', 'linear first order'),
             ('(3 + 4SR)/(R(1 + SR)) = 3/R + S/(1 + SR)', 'partial fractions: both pieces are logarithmic derivatives'), ('integrating factor R³(1 + SR)', 'then d/dR [R³(1 + SR) y] = −(2Δp_c/ρ) R²')]
    y = 1.5
    for i, (a, b) in enumerate(steps):
        f.text(.6, y, 6.2, f'{i + 1}  {a}', 12.5, WARM, bold=True)
        y = f.text(.85, y + .5 if len(a) > 48 else y + .33, 6.0, b, 12, FG) + .3
    f.text(7.3, 6.25, 5.6, 'The two dashed pieces add to the solid curve (partial fractions).', 12, FG)
    f.note('Integrating factor of Eq. C3-E08.')


def e09(f):
    x = np.linspace(.04, 1, 300)
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (0, 1), (0, 300), 'R / R_max', '|Ṙ|  (m/s)', (0, .25, .5, .75, 1), (0, 100, 200, 300), fx='{:.2f}', fy='{:g}')
    for chi, c in _chis():
        sp = np.array([abs(speed_S(v, RMAX, RHO, DPC, chi)) if v < 1 else 0 for v in x])
        p.curve(x, sp, c, 3)
        v5 = abs(speed_S(.5, RMAX, RHO, DPC, chi))
        p.pt(.5, v5, c, .06)
    for i, (chi, c) in enumerate(_chis()):
        f.rect(4.0, 1.62 + i * .36, .3, .2, fill=c, line=c, lw=1)
        f.text(4.42, 1.57 + i * .36, 3.2, f'χ = {chi:g}:  |Ṙ| at R_max/2 = {abs(speed_S(.5, RMAX, RHO, DPC, chi)):.1f} m/s', 11.5, c, wrap=False)
    f.panel(7.9, 1.5, 5.05, 4.0, 'Integrated solution', ACC, size=13.5)
    f.text(8.05, 2.0, 4.8, 'Ṙ = −√{ (2Δp_c/3ρ) (R_max³ − R³) / [R³ (1 + SR)] }', 12, FG, bold=True)
    f.bullets(8.05, 2.8, 4.8, ['[R³(1 + SR) y] from R_max to R integrates to (2Δp_c/3ρ)(R_max³ − R³).', 'The condition y(R_max) = 0 removes the constant.', 'The minus sign selects the inward branch.', 'Interaction (χ > 0) lowers the speed at every radius.'], 12)
    f.text(1.0, 6.27, 12, 'Speed at half radius: 21.6 m/s for an isolated bubble, lower when neighbours add inertia.', 12.5, FG)
    f.note('Integrated speed of Eq. C3-E09 (R_max = 30 µm, ρ = 1000 kg/m³, Δp_c = 100 kPa).')


def e10(f):
    chi = np.linspace(0, 6, 40)
    C = np.array([C_chi(c) for c in chi])
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (0, 6), (.8, 2.2), 'interaction strength χ = S R_max', 'C(χ) = t_c / [R_max √(ρ/Δp_c)]', (0, 1, 2, 3, 4, 5, 6), (1, 1.5, 2), fx='{:g}', fy='{:.1f}')
    p.curve(chi, C, ACC, 3)
    p.pt(0, C[0], WARM)
    p.label(0, C[0], 'C(0) = 0.9147: isolated', WARM, 12, w=2.4, dx=.15, dy=-.45)
    for c_, col in [(1, PINK), (3, BLUE)]:
        v = C_chi(c_)
        p.pt(c_, v, col)
        p.label(c_, v, f'χ = {c_}: {v:.3f}', col, 12, w=1.8, dx=.12, dy=-.45)
    f.panel(7.9, 1.5, 5.05, 4.0, 'Interaction delays the collapse', ACC, size=13.5)
    f.text(8.05, 2.0, 4.8, 'C(χ) = √(3/2) ∫₀¹ √[ x³(1 + χx) / (1 − x³) ] dx', 12, FG, bold=True)
    f.text(8.05, 2.8, 4.8, "C′(χ) = ½√(3/2) ∫₀¹ x^(5/2) / √[(1 − x³)(1 + χx)] dx > 0", 11.5, WARM, bold=True)
    f.bullets(8.05, 3.5, 4.8, ['The integrand of C′ is positive, so C always rises with χ.', 'At χ = 3 the formal collapse time is 1.85 times the isolated one.'], 12)
    f.text(1.0, 6.27, 12, 'Time to collapse t_c = R_max √(ρ/Δp_c) C(χ): shared liquid inertia makes every bubble slower, never faster.', 12.5, FG)
    f.note('Collapse-time quadrature and sign check of Eq. C3-E10.')


def e11(f):
    N = np.arange(1, 26)
    p = Plot(f, 1.0, 1.5, 5.6, 3.9, (1, 25), (0, 1.1), 'number of bubbles N', 'R_max,N / R_*', (1, 5, 10, 15, 20, 25), (0, .25, .5, .75, 1), fx='{:g}', fy='{:.2f}')
    p.curve(N, N ** (-1 / 3), ACC, 3)
    p.pt(25, 25 ** (-1 / 3), WARM)
    p.label(25, 25 ** (-1 / 3), 'N = 25: 0.342', WARM, 12, w=1.6, dx=-1.7, dy=-.5)
    p.label(2, .95, 'R_max,N = R_* N^(−1/3)', ACC, 12.5, w=3.0)
    EBt = 1.0
    q = Plot(f, 7.4, 1.5, 5.5, 3.9, (1, 25), (0, 1.1), 'number of bubbles N', 'energy (relative to isolated)', (1, 5, 10, 15, 20, 25), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    q.curve(N, np.ones_like(N, dtype=float), WARM, 3)
    q.curve(N, 1.0 / N, ACC, 3, dash=True)
    q.label(3, 1.0, 'total work E_B,tot = (4π/3)Δp_c R_*³: fixed', WARM, 11.5, w=4.2, dy=-.38)
    q.label(8, .3, 'work per bubble = E_B,tot / N', ACC, 11.5, w=3.2)
    f.text(1.0, 6.0, 12, 'K_N ≃ 2πρ N R³(1 + SR) Ṙ² = (4πN/3) Δp_c (R_max³ − R³)   in the leading symmetric model (energy balance holds).', 12.5, FG, bold=True)
    f.text(1.0, 6.5, 12, 'Splitting a fixed pressure-work budget among N bubbles shrinks each one: R_max,N = R_* N^(−1/3).', 12.5, WARM)
    f.note('Energy check and fixed-total-work comparison of Eq. C3-E11.')


FIGS = {1: e01, 2: e02, 3: e03, 4: e04, 5: e05, 6: e06, 7: e07, 8: e08, 9: e09, 10: e10, 11: e11}
