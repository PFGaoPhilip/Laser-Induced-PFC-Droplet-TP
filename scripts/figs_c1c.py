"""Chapter 1, equations 21-34."""
import math

import numpy as np

from figlib import *
from figphys import rp_solve, rayleigh_curve, rayleigh_speed, tc_coeff

RHO = 1000.0


def e21(f):
    t = np.linspace(0, 2.0, 600)

    def box(t0, t1, A):
        return np.where((t >= t0) & (t <= t1), A, 0.0)
    p = Plot(f, 1.0, 1.5, 7.2, 4.0, (0, 2.0), (0, .75), 't  (µs)', 'p − p_ref  (MPa)', (0, .5, 1, 1.5, 2), (0, .2, .4, .6), fx='{:.1f}', fy='{:.1f}')
    tall = np.where(t <= 0.5, 0.6, 0)
    wide = np.where(t <= 1.5, 0.2, 0)
    xs = np.concatenate([[0], t])
    p.fill(t, np.zeros_like(t), wide, BLUE, .35)
    p.fill(t, np.zeros_like(t), tall, ACC, .45)
    p.curve(np.array([0, 0, .5, .5, 2]), np.array([0, .6, .6, 0, 0]), ACC, 3)
    p.curve(np.array([0, 0, 1.5, 1.5, 2]), np.array([0, .2, .2, 0, 0]), BLUE, 3, dash=True)
    p.label(.55, .6, 'Δp = 0.6 MPa for 0.5 µs', ACC, 12.5, w=2.8, dx=.1, dy=-.2)
    p.label(1.0, .2, 'Δp = 0.2 MPa for 1.5 µs', BLUE, 12.5, w=2.8, dx=0, dy=-.38)
    f.panel(8.6, 1.5, 4.35, 4.0, 'One impulse, two pulses', ACC, size=13.5)
    f.text(8.75, 2.0, 4.1, 'Π(x) = ∫ [p(x,t) − p_ref(t)] dt\n[Π] = Pa·s', 13.5, FG, bold=True)
    f.text(8.75, 2.85, 4.1, 'Both shaded areas equal 0.30 Pa·s, so they deliver the same impulse at this point.', 12.5, FG)
    f.text(8.75, 3.85, 4.1, 'Peak pressure alone cannot tell them apart. Amplitude and duration enter together, position by position.', 12.5, WARM)
    f.text(1.0, 6.3, 12, 'Π = 0.6 MPa × 0.5 µs = 0.2 MPa × 1.5 µs = 0.30 Pa·s', 13.5, FG, bold=True)
    f.note('Rectangular pulses chosen for clarity; any waveform with the same area gives the same Π.')


def e22(f):
    vals = [('pressure-impulse term\nΠ / (ρL) = Δu', 3.0, ACC), ('convective impulse\n~ U²τ/L', 3.0 ** 2 * .5e-6 / 1e-4, WARM), ('viscous impulse\n~ ν Δu τ/L²', 1e-6 * 3.0 * .5e-6 / 1e-8, BLUE)]
    f.text(.5, 1.0, 7.8, 'Size of each term in the integrated momentum equation (m/s, log scale)', 14, ACC, bold=True)
    x0, w = 3.4, 5.0
    lo, hi = -5, 1
    for k in range(lo, hi + 1):
        px = x0 + (k - lo) / (hi - lo) * w
        f.line(px, 1.7, px, 4.35, GRID, .8)
        f.text(px - .45, 4.4, .9, f'10^{{{k}}}', 11, MUT, 'center', wrap=False)
    for i, (s, v, c) in enumerate(vals):
        y = 1.85 + i * .85
        f.text(.5, y - .02, 2.8, s, 12, FG)
        wd = (math.log10(v) - lo) / (hi - lo) * w
        f.rect(x0, y + .05, wd, .45, fill=c, line=c, lw=1, opacity=.85)
        f.text(x0 + wd + .08, y + .1, 2.2, f'{v:.3g} m/s', 12.5, FG, bold=True)
    f.panel(9.0, 1.2, 3.95, 3.6, 'Why the short-event model works', ACC, size=13)
    f.text(9.15, 1.7, 3.7, 'Δu = −∇Π/ρ − ∫(u·∇)u dt + ν∫∇²u dt', 12.5, FG, bold=True)
    f.bullets(9.15, 2.5, 3.7, ['Uτ/L = 0.015: convection moves the fluid only 1.5 % of L.', 'ντ/L² = 5×10⁻⁵: viscosity has no time to act.', 'Dropping both leaves Δu ≃ −∇Π/ρ.'], 12)
    f.text(.5, 4.85, 12.4, 'Bars start at 10⁻⁵ m/s. If either small ratio were near 1, the corresponding bar would be as long as the first and the reduced model would fail.', 13.5, FG)
    f.text(.5, 5.85, 12.4, 'Teaching case: Π₀ = 0.30 Pa·s, ρ = 1000 kg/m³, L = 100 µm, τ = 0.5 µs, ν = 10⁻⁶ m²/s.', 12.5, MUT)
    f.note('Magnitudes from Eq. C1-E21 using the numbers of Eq. C1-E24.')


def e23(f):
    cx, cy, Rr = 1.1, 6.2, 5.0
    th0 = math.pi / 2
    f.poly([(cx, cy)] + [(cx + Rr * math.cos(a), cy - Rr * math.sin(a)) for a in np.linspace(0, th0, 40)], fill=LIQ, line=LIQ2, lw=1.4)
    for k in range(1, 5):
        a = th0 * k / 5
        f.line(cx, cy, cx + Rr * math.cos(a), cy - Rr * math.sin(a), MUT, 1.1, dash=True)
        f.text(cx + (Rr + .05) * math.cos(a), cy - (Rr + .05) * math.sin(a) - .1, 1.0, f'Π = {1 - k / 5:.1f} Π₀', 10.5, MUT, wrap=False)
    f.line(cx, cy, cx + Rr, cy, WARM, 4)
    f.text(cx + 1.0, cy + .08, 3.2, 'driven boundary: Π = Π₀', 12.5, WARM, bold=True)
    f.line(cx, cy, cx, cy - Rr, ACC, 4)
    f.text(cx + .1, cy - Rr - .35, 3.4, 'free boundary: Π = 0', 12.5, ACC, bold=True)
    for rr in (1.2, 2.4, 3.6):
        pts = [(cx + rr * math.cos(a), cy - rr * math.sin(a)) for a in np.linspace(.15, th0 - .15, 20)]
        f.path(pts, WARM, 1.2, opacity=.7)
        a = th0 / 2 + .1
        L = .65 / (rr / 1.2)
        px, py = cx + rr * math.cos(a), cy - rr * math.sin(a)
        f.line(px, py, px - L * math.sin(a) * 1.0, py - L * math.cos(a) * 1.0, WARM, 3, arrow=True)
    f.text(7.5, 1.1, 5.4, 'Reduced model: ∇²Π = 0', 15, ACC, bold=True)
    f.bullets(7.5, 1.65, 5.4, ['Incompressible short event: ∇·Δu = 0 and Δu ≃ −∇Π/ρ give Laplace\'s equation for Π.',
                              'Π is fixed on the boundaries (Π₀ on the driven wall, 0 at the free surface); the interior follows from geometry alone.',
                              'Here Π = Π₀(1 − θ/θ₀) in a right-angle corner is harmonic, so Δu points along circular arcs toward the free side.',
                              'Arrow length ∝ 1/r: the impulse gradient is steepest near the corner.'], 12.5)
    f.panel(7.5, 5.0, 5.4, 1.75, None, MUT)
    f.text(7.65, 5.07, 5.1, 'Conditions: Uτ/L ≪ 1 and ντ/L² ≪ 1.', 13, FG, bold=True)
    f.text(7.65, 5.5, 5.1, 'Result: the velocity right after the pulse depends on the shape of the liquid region, not on a detailed pressure history.', 12.5, WARM)
    f.note('Corner example: an exact harmonic solution chosen to show the geometry dependence; not a model of the laser event.')


def e24(f):
    L = 100.0
    x0, x1, yc = 1.3, 8.3, 1.9
    f.rect(x0, yc - .35, x1 - x0, .7, fill=LIQ, line=LIQ2, lw=1.5)
    f.rect(x0 - .2, yc - .45, .2, .9, fill=STEEL, line=MUT, lw=1.3)
    f.text(x0 - .5, yc - .95, 2.4, 'driven end z = 0', 11.5, WARM, bold=True)
    f.text(x1 - 1.6, yc - .95, 2.6, 'outlet z = L', 11.5, ACC, bold=True)
    for k in range(4):
        px = x0 + .6 + k * 1.4
        f.line(px, yc, px + .9, yc, ACC, 3, arrow=True)
    f.dim(x0, yc + .55, x1, yc + .55, 'L = 100 µm', MUT, 11.5, off=-.02)
    p = Plot(f, x0, 3.0, x1 - x0, 2.5, (0, 1), (0, 1.1), 'z / L', 'Π / Π₀', (0, .25, .5, .75, 1), (0, .5, 1), fx='{:.2f}', fy='{:.1f}')
    z = np.linspace(0, 1, 50)
    p.curve(z, 1 - z, WARM, 3.2)
    p.pt(0, 1, WARM)
    p.pt(1, 0, ACC)
    p.label(.35, .72, 'Π(z) = Π₀(1 − z/L)', WARM, 13, w=3, dx=.15, dy=-.1)
    f.panel(8.9, 1.2, 4.05, 4.6, 'Straight column', ACC, size=13.5)
    f.text(9.05, 1.7, 3.8, 'd²Π/dz² = 0\nΠ = Π₀ (1 − z/L)', 13, FG, bold=True)
    f.text(9.05, 2.55, 3.8, 'Δu_z = −(1/ρ) dΠ/dz = Π₀ / (ρL)', 13, ACC, bold=True)
    f.text(9.05, 3.2, 3.8, 'With Π₀ = 0.30 Pa·s, ρ = 1000 kg/m³, L = 100 µm:', 12, FG)
    f.text(9.05, 3.75, 3.8, 'Δu_z = 3.0 m/s', 17, WARM, bold=True)
    f.text(9.05, 4.4, 3.8, 'The impulse drops linearly, so every slice gets the same velocity change toward the outlet.', 12, MUT)
    f.text(.5, 6.2, 12.4, 'A constant gradient means uniform acceleration: the whole column leaves the driven end as one plug.', 13.5, FG)
    f.note('Boundary values Π(0) = Π₀, Π(L) = 0 (Eq. C1-E23).')


def e25(f):
    f.text(.5, 1.0, 12.3, 'Time scales of the declared impulse case (log axis, µs)', 14, ACC, bold=True)
    x0, w = 1.0, 11.3
    lo, hi = -2, 5

    def X(v):
        return x0 + (math.log10(v) - lo) / (hi - lo) * w
    f.line(x0, 3.4, x0 + w, 3.4, MUT, 2)
    for k in range(lo, hi + 1):
        px = x0 + (k - lo) / (hi - lo) * w
        f.line(px, 3.4, px, 3.48, MUT, 1.2)
        f.text(px - .5, 3.5, 1.0, f'10^{{{k}}}', 11, MUT, 'center', wrap=False)
    ev = [(.0667, 'acoustic crossing\nt_a = L/c = 0.067 µs', BLUE, 2.35), (.5, 'pulse duration\nτ = 0.5 µs', ACC, 1.55), (33.3, 'convective time\nL/U = 33 µs', WARM, 2.35), (1e4, 'viscous time\nL²/ν = 10 ms', PINK, 1.55)]
    for v, s, c, ty in ev:
        px = X(v)
        f.line(px, 3.4, px, ty + .75, c, 2.2)
        f.dot(px, 3.4, .09, c)
        f.text(px - 1.2, ty, 2.4, s, 12, c, 'center', bold=True)
    f.text(x0, 4.1, w, 'Ratios of the declared case', 13.5, ACC, bold=True)
    cards = [('Uτ/L = 0.015', 'τ ≪ convective time ✓', WARM), ('ντ/L² = 5×10⁻⁵', 'τ ≪ viscous time ✓', PINK), ('τ / t_a = 7.5', 'τ is longer than the acoustic crossing, so pressure equalises along the column', BLUE)]
    for i, (h, b, c) in enumerate(cards):
        x = x0 + i * 3.85
        f.panel(x, 4.5, 3.6, 1.55, None, c)
        f.text(x + .1, 4.58, 3.4, h, 15, c, 'center', bold=True)
        f.text(x + .1, 5.05, 3.4, b, 12, FG, 'center')
    f.text(.5, 6.35, 12.3, 'Pressure impulse (Pa·s) and acoustic time (s) are different quantities: one measures the load delivered, the other how fast pressure communicates.', 12.5, FG)
    f.note('Π₀ = Δpτ = 0.60 MPa × 0.50 µs = 0.30 Pa·s; U = 3.0 m/s; c = 1500 m/s; L = 100 µm; ν = 10⁻⁶ m²/s.')


def e26(f):
    f.panel(.4, 1.0, 4.4, 5.4, 'Perfect symmetry picks no direction', ACC, size=13.5)
    cx, cy = 2.6, 3.7
    f.bubble(cx, cy, .9)
    for k in range(12):
        a = 2 * math.pi * k / 12
        f.line(cx + .95 * math.cos(a), cy - .95 * math.sin(a), cx + 1.55 * math.cos(a), cy - 1.55 * math.sin(a), ACC, 2.4, arrow=True)
    f.text(.55, 5.5, 4.1, '∮ e_r dΩ = 0: outward unit vectors cancel in pairs, so a lone sphere has no preferred jet direction.', 12.5, FG)
    f.rect(5.2, 6.0, 7.7, .28, fill=STEEL, line=MUT, lw=1.3)
    for i in range(30):
        f.line(5.3 + i * .25, 6.28, 5.45 + i * .25, 6.45, MUT, 1)
    f.text(5.2, 1.0, 7.7, 'Stand-off γ = h / R_max locates the boundary', 14, ACC, bold=True)
    for (gx, g, r) in [(6.4, 0.6, 1.0), (9.0, 1.2, 0.9), (11.7, 2.6, 0.75)]:
        h = g * r * 1.0 / 1.0
        cy2 = 6.0 - g * r * 1.4
        f.ellipse(gx, cy2, r * .65, fill=GASC, line=WARM, lw=2)
        f.line(gx, cy2, gx, 6.0, MUT, 1.2, dash=True)
        f.dim(gx + r * .8, cy2, gx + r * .8, 6.0, '', MUT, 11)
        f.text(gx + r * .8 + .12, (cy2 + 6.0) / 2 - .1, 1.5, f'h = {g} R_max', 11, MUT, wrap=False)
        f.text(gx - .8, cy2 - r * .65 - .45, 1.6, f'γ = {g}', 13.5, ACC, 'center', bold=True)
    f.text(5.2, 1.5, 7.7, 'Small γ: boundary close, strong asymmetry.   Large γ: far boundary, nearly spherical.', 12.5, FG)
    f.note('Definitions of Eq. C1-E25. Positions drawn to show the trend; radii are not to scale.')


def e27(f):
    f.panel(.4, 1.0, 4.2, 5.4, 'Continuity: ∇·u = 0', ACC, size=13.5)
    f.rect(1.4, 2.5, 2.2, 1.7, fill=LIQ, line=ACC, lw=2)
    for dy in (-.5, 0, .5):
        f.line(.75, 3.35 + dy, 1.35, 3.35 + dy, ACC, 2.6, arrow=True)
        f.line(3.65, 3.35 + dy, 4.25, 3.35 + dy, ACC, 2.6, arrow=True)
    f.text(1.5, 3.1, 2.0, 'volume in\n= volume out', 13, FG, 'center', bold=True)
    f.text(.55, 4.65, 3.9, 'The liquid does not compress: whatever flows into a region flows out, so a moving bubble wall must push liquid outward.', 12.5, FG)
    f.panel(4.9, 1.0, 8.05, 5.4, 'Momentum: ρ Du/Dt = −∇p + μ∇²u', ACC, size=13.5)
    ox, oy = 5.9, 4.8
    f.line(ox, oy, ox + 3.0, oy - 1.0, ACC, 3.5, arrow=True)
    f.line(ox, oy, ox + 3.0, oy, PINK, 3, arrow=True)
    f.line(ox + 3.0, oy, ox + 3.0, oy - 1.0, BLUE, 3, arrow=True)
    f.dot(ox, oy, .08, FG)
    f.text(ox + 3.15, oy - 1.4, 3.6, 'ρ Du/Dt (inertia)', 13, ACC, bold=True)
    f.text(ox + 1.0, oy + .08, 3.0, '−∇p (pressure gradient)', 13, PINK, bold=True)
    f.text(ox + 3.15, oy - .6, 3.6, 'μ∇²u (viscous diffusion)', 13, BLUE, bold=True)
    f.text(5.1, 1.5, 7.7, 'Per unit volume, the mass-times-acceleration vector equals the sum of the forces:', 13, FG)
    f.text(5.1, 2.05, 7.7, 'The same fixed set of equations governs every later spatial calculation: the pressure field supplies the push, the viscous term damps it, and the convective part u·∇u makes the flow nonlinear.', 12.5, MUT)
    f.text(5.1, 3.1, 7.7, 'Du/Dt = ∂u/∂t + (u·∇)u', 14, WARM, bold=True)
    f.note('Vectors are schematic; constant ρ and μ.')


def e28(f):
    f.panel(.4, 1.0, 5.4, 5.4, 'Interface patch and conventions', ACC, size=13.5)
    cx, cy, R = 3.0, 3.85, 1.3
    f.ellipse(cx, cy, R + .4, fill=LIQ, line=LIQ2, lw=1)
    f.bubble(cx, cy, R)
    for a in (35, 115, 200):
        t = math.radians(a)
        px, py = cx + R * math.cos(t), cy - R * math.sin(t)
        f.line(px, py, px - .85 * math.cos(t), py + .85 * math.sin(t), PINK, 3, arrow=True)
        f.line(px, py, px - .7 * math.sin(t), py - .7 * math.cos(t), BLUE, 2.4, arrow=True)
    t = math.radians(35)
    f.text(cx + 1.1, cy - 2.05, 2.6, 'n: liquid → gas', 13, PINK, bold=True)
    f.text(cx + 1.4, cy - 1.45, 2.6, 's: tangent', 13, BLUE, bold=True)
    f.text(.55, 5.75, 5.1, 'For a bubble the normal points inward, so the sphere curvature is κ = −2/R.', 12.5, FG)
    f.text(6.1, 1.0, 6.8, 'Three conditions on the interface Γ', 14, ACC, bold=True)
    rows = [('Kinematic', 'V_n = u · n', 'the surface moves with the liquid normal to itself'), ('Normal stress', 'p_l = p_b + σκ + 2μ n·D·n', 'σκ = −2σ/R for a sphere'), ('Tangential stress', '2μ s·D·n = 0', 'gas cannot support shear')]
    y = 1.55
    for h, e, d in rows:
        f.panel(6.1, y, 6.85, 1.45, None, MUT)
        f.text(6.25, y + .06, 6.5, h, 13, WARM, bold=True)
        f.text(6.25, y + .45, 6.5, e, 14, FG, bold=True)
        f.text(6.25, y + .95, 6.5, d, 12, MUT)
        y += 1.6
    f.text(6.1, 6.35, 6.8, 'One sign convention for n, κ and D is required, or the terms cancel wrongly.', 12.5, FG)
    f.note('D = ½(∇u + ∇uᵀ) is the strain-rate tensor (Eq. C1-E27).')


def e29(f):
    cx, cy = 3.4, 3.7
    f.panel(.4, 1.0, 6.0, 5.4, 'A shape that is not a sphere', ACC, size=13.5)
    pts = []
    for a in np.linspace(0, 2 * math.pi, 80):
        r = 1.2 * (1 + .25 * math.cos(2 * a) + .12 * math.cos(a))
        pts.append((cx + r * math.cos(a) * 1.15, cy - r * math.sin(a) * .85))
    f.poly(pts, fill=GASC, line=WARM, lw=2.4)
    f.text(cx - .4, cy - .1, .8, 'Γ', 20, WARM, 'center', bold=True)
    f.wall(.8, 5.9, 5.2)
    for a in (0, 60, 120, 180, 240, 300):
        t = math.radians(a)
        r = 1.2 * (1 + .25 * math.cos(2 * t) + .12 * math.cos(t))
        px, py = cx + r * math.cos(t) * 1.15, cy - r * math.sin(t) * .85
        f.line(px, py, px + .55 * math.cos(t), py - .55 * math.sin(t), ACC, 2.2, arrow=True)
    f.text(.55, 5.3, 5.7, 'Surface velocity u = ∇φ differs from point to point; the shape changes as it is carried along.', 12, FG)
    steps = [('1', 'Known φ on Γ', 'solve ∇²φ = 0 in the liquid', ACC), ('2', 'u = ∇φ at the surface', 'normal speed V_n = ∂φ/∂n', BLUE), ('3', 'Advect: dX/dt = u(X, t)', 'new shape Γ(t + dt), new curvature κ', WARM), ('4', 'Update φ on Γ', 'Dφ/Dt = ½|u|² + (p∞ − p_b − σκ)/ρ', PINK)]
    f.text(6.7, 1.0, 6.2, 'Closure loop (inviscid, before impact)', 14, ACC, bold=True)
    y = 1.5
    for n, h, d, c in steps:
        f.panel(6.7, y, 6.25, 1.0, None, c)
        f.ellipse(7.05, y + .5, .24, fill=c, line=c, lw=1)
        f.text(6.93, y + .3, .25, n, 13, BG, 'center', bold=True)
        f.text(7.5, y + .08, 5.35, h, 13, c, bold=True)
        f.text(7.5, y + .5, 5.35, d, 11.5, FG)
        if n != '4':
            f.line(9.8, y + 1.0, 9.8, y + 1.2, MUT, 2, arrow=True)
        y += 1.2
    f.text(6.7, 6.35, 6.2, 'The shape and the potential evolve together; changing geometry is what creates focusing.', 12.5, WARM)
    f.note('Schematic of the loop of Eq. C1-E28; the deformed shape is illustrative.')


def e30(f):
    R0 = 5e-6
    t, R, V, pb = rp_solve(R0, 0.0, 1.5e-6, pg0=1.0e6, mu=0.0, n=4000)
    dt = t[1] - t[0]
    acc = np.gradient(np.gradient(R, dt), dt)
    lhs = -V ** 2 - R * acc
    rhs = (101325 - pb + 2 * .072 / R) / RHO + .5 * V ** 2
    idx = slice(6, -6)
    ym = float(np.ceil(np.max(np.abs(lhs[6:-6])) * 1.15 / 1000) * 1000)
    p = Plot(f, 7.5, 1.5, 5.4, 3.9, (0, 1.5), (-ym, ym), 't  (µs)', 'closure terms (m²/s²)', (0, .5, 1, 1.5), (-ym, -ym / 2, 0, ym / 2, ym), fx='{:.1f}', fy='{:.0f}')
    p.seg(0, 0, 1.5, 0, GRID, 1.2)
    p.curve((t * 1e6)[idx], lhs[idx], ACC, 3.2)
    p.curve((t * 1e6)[idx], rhs[idx], '#FFFFFF', 1.6, dash=True)
    err = np.max(np.abs(lhs - rhs)[idx]) / np.max(np.abs(lhs)[idx])
    p.label(.05, ym * .98, f'solid: left side, dashed: right side; relative gap {err:.0e}', FG, 11, w=5.2, dy=.0)
    f.panel(.4, 1.0, 6.2, 5.4, 'The general closure contains the sphere', ACC, size=13.5)
    steps = [('General closure, Eq. C1-E28', 'D φ/Dt = ½|u|² + (p∞ − p_b − σκ)/ρ', ACC), ('Insert the sphere', 'φ_Γ = −RṘ,   κ = −2/R', WARM), ('Differentiate along the wall', '−Ṙ² − RR̈ = (p∞ − p_b + 2σ/R)/ρ + ½Ṙ²', BLUE), ('Rearrange', 'ρ(RR̈ + 3Ṙ²/2) = p_b − p∞ − 2σ/R', PINK)]
    y = 1.5
    for h, e, c in steps:
        f.text(.6, y, 5.8, h, 12.5, c, bold=True)
        y = f.text(.85, y + .32, 5.6, e, 12.5, FG) + .28
        if h != 'Rearrange':
            f.line(3.4, y - .2, 3.4, y, MUT, 2, arrow=True)
            y += .06
    f.text(.6, 5.55, 5.8, 'This is the Rayleigh–Plesset equation without viscosity: the spatial theory returns the spherical model in its own limit.', 12, MUT)
    f.text(7.5, 6.2, 5.4, 'Check: R(t) from the solution, R̈ by finite differences. The two sides coincide, so the algebra above is exact.', 12.5, FG)
    f.note('Inviscid Rayleigh–Plesset run: R₀ = 5 µm, p_g0 = 1 MPa, γ = 1.4, σ = 0.072 N/m.')


def e31(f):
    c = 1500.0
    f.text(.5, 1.0, 6.2, 'A pressure pulse crossing a distance L_e', 14, ACC, bold=True)
    for k, (tau, lbl, col) in enumerate([(300, 'slow rise: τ_e ≫ L_e/c', ACC), (20, 'fast rise: τ_e ≪ L_e/c', PINK)]):
        y0 = 1.65 + k * 2.1
        f.rect(.6, y0 + .75, 5.6, .55, fill=LIQ, line=LIQ2, lw=1.2)
        f.text(.6, y0 - .1, 5.6, lbl, 12.5, col, bold=True)
        xs = np.linspace(.6, 6.2, 80)
        w = (tau / 300.0) * 3.4 + .3
        prof = 1 / (1 + np.exp(-(3.6 - xs) / w * 1.6))
        f.path([(x, y0 + 1.3 - .85 * v) for x, v in zip(xs, prof)], col, 3)
        f.text(.6, y0 + 1.36, 5.6, 'pressure along the column at one instant', 10.5, MUT)
    L = np.logspace(-5, -2, 100)
    p = Plot(f, 7.5, 1.55, 5.4, 3.6, (1e-5, 1e-2), (1e-2, 1e2), 'communication length L_e  (m)', '𝒞_e = L_e / (c τ_e)', (1e-5, 1e-4, 1e-3, 1e-2), (1e-2, 1, 1e2), fx='{:.0e}', fy='{:.0e}', xlog=True, ylog=True)
    for tau, col, lab in [(1e-7, PINK, 'τ_e = 0.1 µs'), (1e-5, ACC, 'τ_e = 10 µs')]:
        p.curve(L, L / (c * tau), col, 3)
    p.hline(1, WARM)
    p.label(1.5e-5, 1, '𝒞_e = 1', WARM, 12, w=1.2, dy=-.3)
    p.label(2e-4, 20, 'τ_e = 0.1 µs', PINK, 12, w=1.8)
    p.label(1.2e-3, .3, 'τ_e = 10 µs', ACC, 12, w=1.8)
    f.text(7.5, 5.7, 5.4, 'M_w = |Ṙ|/c  and  𝒞_e = L_e/(cτ_e)  test different things.', 12.5, FG, bold=True)
    f.text(.5, 6.2, 12.4, 'A pulse can need compressibility even when the wall is slow: 𝒞_e ≳ 1 means pressure cannot equalise during the rise.', 13, WARM)
    f.note('c = 1500 m/s; curves from the definition 𝒞_e = L_e/(c τ_e) of Eq. C1-E30.')


def e32(f):
    f.chain([('Source pressure', 'p_b from the contents (E08), not from R alone'), ('Radius motion', 'Rayleigh–Plesset: p_b − p∞ − 2σ/R − 4μṘ/R (E07)'),
             ('Liquid response', 'inertia stores the work; impulse Π gives early speed (E05, E21)'), ('Geometry', 'stand-off and walls decide direction (E26–E29)')],
            1.4, h=1.7, gap=.45, colors=[WARM, ACC, BLUE, PINK], size=12.5)
    f.panel(.5, 3.5, 12.3, 1.55, None, MUT)
    f.text(.65, 3.58, 12.0, 'Reference formulas of the defence answer', 13.5, ACC, bold=True)
    f.text(.65, 4.0, 12.0, 'ρ(RR̈ + 3Ṙ²/2) = p_b − p∞ − 2σ/R − 4μṘ/R\np_b = p_v,PFC + p_v,w + p_g', 14, FG, bold=True)
    f.text(.5, 5.3, 12.3, 'The source pressure moves carrier liquid. Whether that motion becomes a useful jet is decided by geometry, not by the pressure alone.', 13.5, WARM)
    f.text(.5, 5.9, 12.3, 'Every term of the radius equation is a pressure (Pa); every term of the composition is a partial pressure.', 12.5, MUT)
    f.note('Summary of Eqs. C1-E07 and C1-E08.')


def e33(f):
    Rmax, rho, dpc = 30e-6, 1000., 1e5
    x = np.logspace(-1.3, 0, 200)
    sp = np.array([abs(rayleigh_speed(v, Rmax, rho, dpc)) if v < 1 else 1e-9 for v in x])
    p1 = Plot(f, .9, 1.7, 3.6, 3.3, (.05, 1), (1, 1000), 'R / R_max', '|Ṙ| (m/s)', (.05, .1, .5, 1), (1, 10, 100, 1000), fx='{:g}', xlog=True, ylog=True)
    p1.curve(x, sp, ACC, 3)
    tt, RR = rayleigh_curve(Rmax, rho, dpc)
    p2 = Plot(f, 5.4, 1.7, 3.6, 3.3, (0, 3), (0, 31), 't (µs)', 'R (µm)', (0, 1, 2, 3), (0, 10, 20, 30), fx='{:.0f}')
    p2.curve(tt * 1e6, RR * 1e6, WARM, 3)
    p2.vline(tt[-1] * 1e6, PINK)
    xx = np.linspace(0, 1, 100)
    p3 = Plot(f, 9.8, 1.7, 3.1, 3.3, (0, 1), (0, 1.05), 'R / R_max', 'K_l / E_B', (0, .5, 1), (0, .5, 1), fx='{:g}', fy='{:g}')
    p3.curve(xx, 1 - xx ** 3, BLUE, 3)
    for (x0, t, c, s) in [(.9, 'Speed', ACC, 'Ṙ = −√{(2Δp_c/3ρ)[(R_max/R)³ − 1]}'), (5.4, 'Time', WARM, f't_c = B(5/6,1/2)/√6 · R_max√(ρ/Δp_c) = {tt[-1] * 1e6:.3f} µs'), (9.8, 'Energy', BLUE, 'K_l = (4π/3)Δp_c(R_max³ − R³)')]:
        f.text(x0, 1.05, 3.5, t, 14.5, c, bold=True)
        f.text(x0, 5.75, 3.7, s, 11.5, FG)
    f.text(.5, 6.45, 12.4, 'The singular speed belongs to an ideal radial trajectory (no gas, viscosity, tension or compressibility), not to a validated physical maximum.', 12.5, WARM)
    f.note('Teaching inputs R_max = 30 µm, ρ = 1000 kg/m³, Δp_c = 100 kPa (Eqs. C1-E14, E16, E18).')


def e34(f):
    t = np.linspace(0, 2, 400)
    p = Plot(f, 1.0, 1.7, 3.9, 2.5, (0, 2), (0, .75), 't (µs)', 'p − p_ref (MPa)', (0, 1, 2), (0, .3, .6), fx='{:g}', fy='{:.1f}')
    p.fill(t, np.zeros_like(t), np.where(t <= .5, .6, 0), ACC, .45)
    p.curve(np.array([0, 0, .5, .5, 2]), np.array([0, .6, .6, 0, 0]), ACC, 3)
    p.label(.55, .6, 'Π = ∫(p − p_ref)dt', ACC, 11.5, w=2.4, dx=.1, dy=-.15)
    f.text(1.0, 1.05, 3.9, '1  Pulse → impulse', 14, ACC, bold=True)
    f.text(5.4, 1.05, 3.9, '2  Impulse → velocity', 14, WARM, bold=True)
    f.rect(5.5, 2.4, 3.3, .8, fill=LIQ, line=LIQ2, lw=1.4)
    f.rect(5.35, 2.3, .15, 1.0, fill=STEEL, line=MUT, lw=1.2)
    for k in range(3):
        f.line(5.75 + k * 1.0, 2.8, 6.4 + k * 1.0, 2.8, WARM, 3, arrow=True)
    f.text(5.5, 3.35, 3.3, 'Δu ≃ −∇Π/ρ,   ∇²Π = 0', 12.5, FG, bold=True)
    f.text(5.5, 3.85, 3.3, 'U_column = Π₀/(ρL) = 3.0 m/s', 12.5, WARM, bold=True)
    f.text(9.5, 1.05, 3.4, '3  Check the limits', 14, PINK, bold=True)
    f.bullets(9.5, 1.6, 3.4, ['Uτ/L = 0.015 ≪ 1', 'ντ/L² = 5×10⁻⁵ ≪ 1', 't_a = L/c = 0.067 µs: acoustic time, not the impulse'], 12)
    f.panel(.5, 4.55, 12.3, 1.55, None, MUT)
    f.text(.65, 4.63, 12.0, 'Reference formulas', 13.5, ACC, bold=True)
    f.text(.65, 5.0, 12.0, 'Π(x) = ∫(p − p_ref)dt;   Δu ≃ −∇Π/ρ,  ∇²Π = 0\nU_column = Π₀/(ρL);   t_a = L/c', 14, FG, bold=True)
    f.text(.5, 6.3, 12.4, 'The impulse benchmark gives the early velocity field; the moving-interface problem that follows is a separate calculation.', 13, WARM)
    f.note('Summary of Eqs. C1-E20 to C1-E24 for the declared case.')


FIGS = {21: e21, 22: e22, 23: e23, 24: e24, 25: e25, 26: e26, 27: e27, 28: e28, 29: e29, 30: e30, 31: e31, 32: e32, 33: e33, 34: e34}
