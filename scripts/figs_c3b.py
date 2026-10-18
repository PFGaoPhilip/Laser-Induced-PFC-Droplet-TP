"""Chapter 3, equations 12-22."""
import math

import numpy as np

from figlib import *
from figphys import cylinder_growth

RHO = 1000.0
U_J = math.sqrt(2 * 2.0e-9 / 3.926991e-12)
M_J = 3.926991e-12


def e12(f):
    f.panel(.4, 1.0, 4.4, 5.3, 'Bubbles in a cubic lattice', ACC, size=13.5)
    s = .72
    r = .21
    for i in range(4):
        for j in range(4):
            f.bubble(.95 + i * s + .15, 1.85 + j * s, r, rim=WARM, lw=1.6)
    f.dim(.95 + .15, 4.95, .95 + .15 + s, 4.95, 's', MUT, 11.5, side=-1)
    f.text(.55, 5.35, 4.1, 'φ_b = Σ V_i / V_Ω = (4π/3) R³ / s³ for one bubble per cell.', 12, FG)
    x = np.linspace(0, .5, 100)
    p = Plot(f, 6.2, 1.5, 3.5, 3.7, (0, .5), (0, .55), 'R / s', 'volume fraction φ_b', (0, .1, .2, .3, .4, .5), (0, .1, .2, .3, .4, .5), fx='{:.1f}', fy='{:.1f}')
    p.curve(x, 4 * math.pi / 3 * x ** 3, ACC, 3)
    for v, c in [(.1, WARM), (.2, PINK), (.3, BLUE)]:
        y = 4 * math.pi / 3 * v ** 3
        p.pt(v, y, c, .06)
        p.label(v, y, f'{y:.3f}', c, 11, w=.9, dx=.08, dy=-.4)
    f.panel(9.9, 1.5, 3.05, 3.7, 'Delay r_i/c', WARM, size=13)
    f.dot(10.3, 3.0, .1, WARM)
    f.text(10.1, 2.2, 2.7, 'source i', 11.5, WARM, bold=True)
    f.line(10.4, 3.0, 12.4, 3.0, ACC, 2.5, arrow=True)
    f.dot(12.6, 3.0, .09, PINK)
    f.text(12.0, 3.2, 1.0, 'x', 12, PINK, bold=True)
    f.text(10.0, 3.55, 2.9, 'the signal at x now was emitted at t − r_i/c', 11, FG)
    f.text(6.2, 5.8, 6.7, 'φ(x,t) ≃ −Σ V̇_i(t − r_i/c) / (4π r_i),   p′ ≃ Σ ρ V̈_i(t − r_i/c) / (4π r_i)', 12, FG, bold=True)
    f.text(6.2, 6.3, 6.7, 'A spatial sum needs source histories and travel times, not just a site count.', 12.5, WARM)
    f.note('Volume fraction and retarded monopole approximation of Eq. C3-E12 (far, compact, weak sources).')


def e13(f):
    f.rect(.4, 1.0, 7.4, 5.3, fill=LIQ, line=LIQ2, lw=1.4, round_=True)
    f.text(.6, 1.1, 7.0, 'Liquid region Ω(t):  ∇²φ = 0,  u = ∇φ', 14, FG, bold=True)
    f.wall(.9, 5.6, 6.6)
    f.bubble(3.0, 3.9, 1.0)
    f.text(2.3, 3.75, 1.4, 'gas', 12.5, MUT, 'center')
    f.text(1.0, 1.7, 3.6, 'interface Γ(t)', 12, WARM, bold=True)
    f.text(5.3, 3.5, 2.3, 'wall', 12, MUT, bold=True)
    f.text(5.0, 1.8, 2.7, 'far field φ → 0', 12, ACC, bold=True)
    for k in range(5):
        a = math.radians(40 + k * 25)
        for rr in (1.55, 2.1):
            pass
    for ang in (20, 75, 130, 185, 330):
        a = math.radians(ang)
        f.line(3.0 + 1.1 * math.cos(a), 3.9 - 1.1 * math.sin(a), 3.0 + 1.7 * math.cos(a), 3.9 - 1.7 * math.sin(a), ACC, 2, arrow=True)
    f.panel(8.1, 1.0, 4.85, 5.3, 'Geometry enters through Ω and its boundary', ACC, size=13)
    f.text(8.25, 1.55, 4.6, 'Irrotational, incompressible flow reduces to one scalar equation:', 12.5, FG)
    f.text(8.25, 2.2, 4.6, '∇·u = 0  and  u = ∇φ  ⇒  ∇²φ = 0 in Ω(t)', 13.5, WARM, bold=True)
    f.bullets(8.25, 3.0, 4.6, ['Laplace has no time derivative: φ at one instant follows from the shape and boundary data at that instant.', 'The domain Ω(t) changes with the moving interface, so geometry drives the dynamics.', 'The equation alone predicts nothing without boundary conditions (next figure).'], 12.5)
    f.note('Potential-flow reduction of Eq. C3-E13; schematic.')


def e14(f):
    f.rect(.4, 1.0, 7.9, 5.3, fill=LIQ, line=LIQ2, lw=1.4, round_=True)
    f.wall(.9, 5.55, 7.0)
    f.bubble(3.2, 3.9, 1.0)
    f.text(2.5, 3.75, 1.4, 'gas', 12.5, MUT, 'center')
    a = math.radians(55)
    px, py = 3.2 + math.cos(a), 3.9 - math.sin(a)
    f.dot(px, py, .09, WARM)
    f.text(.7, 2.1, 3.6, 'X: material point on Γ', 11.5, WARM, bold=True)
    f.line(px, py, px + .75, py - .55, WARM, 3, arrow=True)
    f.text(px + .8, py - .6, 2.5, 'dX/dt = u(X, t)', 12, WARM, bold=True)
    f.line(px - .1, py + .05, px - .6, py + .45, ACC, 3, arrow=True)
    f.text(.7, 2.5, 3.6, 'V_n = ∂ₙφ  (normal speed)', 11.5, ACC, bold=True)
    f.line(5.2, 5.5, 5.2, 5.0, PINK, 3, arrow=True)
    f.text(5.35, 4.75, 2.9, 'wall: ∂ₙφ = V_w·n', 12, PINK, bold=True)
    f.text(5.3, 1.15, 2.9, 'far field: φ → 0', 12, FG, bold=True)
    f.text(.6, 1.1, 3.8, 'initial data: (Γ, φ_Γ) at t = 0 = (Γ₀, φ₀)', 12, WARM, bold=True)
    f.panel(8.6, 1.0, 4.35, 5.3, 'Four things a jet prediction needs', ACC, size=13)
    f.bullets(8.6 + .15, 1.6, 4.1, ['Kinematic condition: the surface moves with the liquid, dX/dt = u(X, t), and V_n = ∂ₙφ.', 'Wall condition: the liquid cannot pass through a moving wall, ∂ₙφ = V_w·n.', 'Far field: the liquid is quiescent far away, φ → 0.', 'Initial shape Γ₀ and potential φ₀.'], 12.5)
    f.text(8.75, 4.9, 4.1, 'Without the last item the potential equation has no starting state, so it cannot predict a jet.', 12.5, WARM)
    f.note('Boundary and initial conditions of Eq. C3-E14.')


def e15(f):
    sig = .072
    f.panel(.4, 1.0, 4.0, 4.4, 'Cavity (gas inside liquid)', ACC, size=13.5)
    f.bubble(2.4, 3.1, .85)
    for a in (40, 140, 250):
        t = math.radians(a)
        f.line(2.4 + .85 * math.cos(t), 3.1 - .85 * math.sin(t), 2.4 + .3 * math.cos(t), 3.1 - .3 * math.sin(t), PINK, 3, arrow=True)
    f.text(.6, 4.2, 3.6, 'n points into the gas', 12, PINK, bold=True)
    f.text(.6, 4.65, 3.6, 'κ = −2/R,  p_l = p_g − 2σ/R', 12.5, FG, bold=True)
    f.text(.6, 5.05, 3.6, f'R = 10 µm: −2σ/R = {-2 * sig / 1e-5 / 1e3:.1f} kPa', 12, MUT)
    f.panel(4.6, 1.0, 4.0, 4.4, 'Liquid jet (liquid inside gas)', WARM, size=13.5)
    f.rect(5.6, 1.9, 2.0, 1.7, fill=LIQ, line=ACC, lw=2.4)
    f.line(5.6, 3.6, 7.6, 3.6, ACC, 2.4)
    for yy in (2.2, 2.75, 3.3):
        pass
    for x_ in (6.0, 7.2):
        f.line(x_, 1.9, x_, 1.35, PINK, 3, arrow=True)
    f.text(4.8, 4.2, 3.6, 'n points out into the gas', 12, PINK, bold=True)
    f.text(4.8, 4.65, 3.6, 'κ = +1/a_j,  p_l = p_g + σ/a_j', 12.5, FG, bold=True)
    f.text(4.8, 5.05, 3.6, f'a_j = 5 µm: +σ/a_j = +{sig / 5e-6 / 1e3:.1f} kPa', 12, MUT)
    f.panel(8.8, 1.0, 4.15, 4.4, 'Dynamic condition on Γ', ACC, size=13)
    f.text(8.95, 1.5, 3.9, 'p_l = p_g + σκ,   κ = ∇_s·n', 12.5, FG, bold=True)
    f.text(8.95, 2.2, 3.9, 'Dφ_Γ/Dt = ½|∇φ|² + (p∞ − p_g − σκ)/ρ', 12.5, WARM, bold=True)
    f.text(8.95, 3.2, 3.9, 'D/Dt = ∂ₜ + u·∇ follows the moving surface point.', 12, FG)
    f.text(8.95, 4.0, 3.9, 'A wrong sign of κ reverses the capillary pressure and the surface evolution.', 12, MUT)
    f.text(.5, 5.7, 12.4, 'Same σ, opposite signs: a concave-to-liquid cavity lowers the liquid pressure; a liquid cylinder raises it.', 13, WARM)
    f.note('Signed curvature and material Bernoulli condition of Eq. C3-E15 (σ = 0.072 N/m for the example).')


def e16(f):
    m = np.logspace(-13.3, -10.5, 100)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (5e-14, 3e-11), (3, 3000), 'liquid mass m  (kg)', 'jet speed U  (m/s)', (1e-13, 1e-12, 1e-11), (3, 10, 30, 100, 300, 1000), fx='{:.0e}', fy='{:g}', xlog=True, ylog=True)
    J = M_J * U_J
    E = .5 * M_J * U_J ** 2
    p.curve(m, J / m, PINK, 3)
    p.curve(m, np.sqrt(2 * E / m), ACC, 3)
    p.pt(M_J, U_J, WARM)
    p.label(M_J, U_J, '3.93 ng, 31.9 m/s: the declared jet', WARM, 12, w=3.3, dx=-3.45, dy=.12)
    p.label(6e-14, 1200, 'fixed impulse J: U = J/m', PINK, 12, w=3, dy=-.05)
    p.label(2e-13, 120, 'fixed energy E: U = √(2E/m)', ACC, 12, w=3.2)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Two different budgets', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'Π(z) = Π₀(1 − z/L),  U = Π₀/(ρL)\nm = ρAL,  J = Π₀A = mU', 12.5, FG, bold=True)
    f.text(7.85, 2.9, 5.0, f'J = {J:.3e} N s,   E = {E * 1e9:.2f} nJ', 12.5, WARM, bold=True)
    f.bullets(7.85, 3.45, 5.0, ['Quarter the mass at fixed J: speed ×4, energy ×4.', 'Quarter the mass at fixed E: speed ×2, momentum ÷2.', 'The pressure-impulse field and the total energy must both be satisfied.'], 12)
    f.text(1.0, 6.27, 12, 'Focusing a given source into a lighter jet buys speed only at a price set by which quantity is conserved.', 12.5, FG)
    f.note('Pressure-impulse column and focusing budgets of Eq. C3-E16 (m = 3.927 ng, E = 2 nJ).')


def e17(f):
    f.panel(.4, 1.0, 6.4, 5.3, 'Contracting tube feeding a jet', ACC, size=13.5)
    f.poly([(.8, 2.4), (2.6, 2.4), (4.2, 3.2), (6.4, 3.2), (6.4, 3.9), (4.2, 3.9), (2.6, 4.7), (.8, 4.7)], fill=LIQ, line=ACC, lw=2.2)
    f.text(.9, 1.7, 2.5, 'a_in, U_in, p_in', 12, ACC, bold=True)
    f.text(4.0, 2.6, 2.5, 'jet a_j, U_j', 12, WARM, bold=True)
    f.line(1.0, 3.55, 2.2, 3.55, ACC, 2.4, arrow=True)
    f.line(4.4, 3.55, 6.3, 3.55, WARM, 4, arrow=True)
    f.text(.6, 5.0, 6.0, 'Q = π a_in² U_in = π a_j² U_j,   α = (a_j/a_in)²', 12.5, FG, bold=True)
    f.text(.6, 5.5, 6.0, 'Bernoulli with tension and loss gives the jet speed.', 12, MUT)
    al = np.linspace(.001, .95, 200)
    p = Plot(f, 8.0, 1.5, 4.9, 3.5, (0, 1), (1, 4), 'area ratio α', 'U_j / √(2Δ/ρ)', (0, .25, .5, .75, 1), (1, 2, 3, 4), fx='{:.2f}', fy='{:g}')
    p.curve(al, 1 / np.sqrt(1 - al ** 2), ACC, 3)
    p.pt(.0625, 1 / math.sqrt(1 - .0625 ** 2), WARM)
    p.label(.1, 1.35, 'α = 0.0625 (a_j/a_in = 1/4): 1.002', WARM, 11.5, w=3.3, dy=.1)
    p.label(.45, 3.6, 'diverges as α → 1', PINK, 11.5, w=2.2)
    f.text(7.3, 5.8, 5.6, 'U_j = √{ 2[p_in − p_g − σ_j/a_j − Δp_loss] / [ρ(1 − α²)] },  0 < α < 1.', 12, FG, bold=True)
    f.text(.5, 6.35, 12.4, 'Specify either the source pressure or the flow, then solve for the compatible rest. Valid for a steady, inviscid core only.', 12.5, WARM)
    f.note('Continuity + Bernoulli benchmark of Eq. C3-E17; Δ = p_in − p_g − σ_j/a_j − Δp_loss.')


def e18(f):
    P = np.linspace(0, 2.2e-10, 200)
    E = P ** 2 / (2 * M_J) * 1e9
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 2.2e-10), (0, 6), 'directed momentum P_j  (N s)', 'kinetic energy E_j  (nJ)', (0, 5e-11, 1e-10, 1.5e-10, 2e-10), (0, 2, 4, 6), fx='{:.0e}', fy='{:g}')
    p.fill(P, E, np.full_like(P, 6), ACC, .18)
    p.curve(P, E, ACC, 3)
    Pj = M_J * U_J
    p.pt(Pj, 2.0, WARM)
    p.label(Pj, 2.0, 'uniform jet: on the boundary', WARM, 12, w=2.6, dx=.12, dy=.25)
    p.pt(.7 * Pj, 2.0, PINK)
    p.label(.7 * Pj, 2.0, 'spread of velocities:\nsame E, less P', PINK, 11.5, w=2.2, dx=-2.35, dy=-.55)
    p.label(2.2e-11, 5.4, 'allowed: E ≥ P²/2m', ACC, 12.5, w=2.4)
    p.label(1.4e-10, .5, 'forbidden', MUT, 12, w=1.2)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Cauchy–Schwarz on the jet liquid', ACC, size=13)
    f.text(7.85, 2.0, 5.0, 'A_j = πd_j²/4,  m_j = ρA_jL_j', 12.5, FG, bold=True)
    f.text(7.85, 2.5, 5.0, 'm_j = 1000 × π(10 µm)²/4 × 50 µm = 3.927 ng', 12, WARM, bold=True)
    f.text(7.85, 3.1, 5.0, '|P_j|² ≤ (∫dm)(∫u_z² dm) ≤ 2 m_j E_j', 12.5, FG, bold=True)
    f.text(7.85, 3.7, 5.0, 'U_rms ≤ √(2E_avail / m_j)', 12.5, ACC, bold=True)
    f.text(7.85, 4.3, 5.0, 'Finite mass turns an energy budget into a bound on both speed and momentum.', 12, MUT)
    f.text(1.0, 6.27, 12, 'The jet carries at most P = √(2 m E) of useful momentum; a non-uniform velocity spends energy without adding momentum.', 12.5, FG)
    f.note('Finite-mass definitions and bound of Eq. C3-E18.')


def e19(f):
    f.panel(.4, 1.0, 7.7, 5.3, 'Slender jet: a(z, t) stretched by v(z, t)', ACC, size=13.5)
    zs = np.linspace(.9, 7.5, 60)
    a = .75 - .11 * (zs - .9) + .06 * np.sin(zs * 1.4)
    yc = 3.6
    f.poly([(z, yc - r) for z, r in zip(zs, a)] + [(z, yc + r) for z, r in zip(zs[::-1], a[::-1])], fill=LIQ, line=ACC, lw=2.2)
    for z in (1.6, 3.2, 4.8, 6.4):
        L = .35 + (z - 1.6) * .2
        f.line(z, yc, z + L, yc, WARM, 3, arrow=True)
    f.text(1.0, 4.65, 6.9, 'v(z): speed grows along z, so the column is stretched and thins', 12, WARM, bold=True)
    z0, z1 = 3.0, 4.2
    f.rect(z0, 2.0, z1 - z0, 3.2, fill=None, line=PINK, lw=1.8)
    f.text(z0 - .3, 1.55, 2.0, 'slice Δz', 12, PINK, bold=True)
    f.line(z0 - .45, 2.6, z0 - .05, 2.6, ACC, 2.4, arrow=True)
    f.line(z1 + .05, 2.6, z1 + .45, 2.6, ACC, 2.4, arrow=True)
    f.text(1.0, 5.4, 3.0, '[Av](z)', 12, ACC, bold=True)
    f.text(4.6, 5.4, 3.0, '[Av](z + Δz)', 12, ACC, bold=True)
    f.panel(8.3, 1.0, 4.65, 5.3, 'Volume balance of the slice', ACC, size=13)
    f.text(8.45, 1.55, 4.4, 'A = πa²;  ∂ₜ∫A dξ = [Av](z) − [Av](z + Δz)', 12, FG, bold=True)
    f.text(8.45, 2.35, 4.4, 'Δz → 0:  ∂ₜA + ∂_z(Av) = 0', 13, WARM, bold=True)
    f.text(8.45, 3.0, 4.4, 'dividing by 2πa:', 11.5, MUT)
    f.text(8.45, 3.4, 4.4, '∂ₜa + v ∂_z a = −(a/2) ∂_z v', 14, ACC, bold=True)
    f.text(8.45, 4.2, 4.4, 'If ∂_z v > 0 the right side is negative: the radius shrinks even before capillary necking grows.', 12, FG)
    f.note('Slender-jet volume conservation of Eq. C3-E19; schematic geometry.')


def e20(f):
    q = .7
    zz = np.linspace(0, 2 * math.pi, 300)
    d = .12
    a = 1 + d * np.cos(zz)
    ap = -d * np.sin(zz) * q
    app = -d * np.cos(zz) * q * q
    kap = 1 / (a * np.sqrt(1 + ap ** 2)) - app / (1 + ap ** 2) ** 1.5
    p = Plot(f, 1.0, 1.6, 6.0, 3.5, (0, 2 * math.pi), (.7, 1.3), 'k z  (one wavelength)', 'κ a₀', (0, math.pi, 2 * math.pi), (.8, 1.0, 1.2), fx='{:.2f}', fy='{:.1f}')
    p.curve(zz, kap, ACC, 3)
    p.curve(zz, 1 / a, MUT, 1.8, dash=True)
    p.curve(zz, np.ones_like(zz), GRID, 1.2)
    p.label(.3, 1.27, 'κ(z) of Eq. C3-E20 for a = a₀(1 + 0.12 cos kz), k a₀ = 0.7', ACC, 11, w=5.4, dy=-.05)
    p.label(3.4, .76, 'dashed: 1/a alone', MUT, 11.5, w=2.2)
    f.text(1.0, 1.1, 6.0, 'Curvature varies along the jet and drives the flow', 13.5, ACC, bold=True)
    f.panel(7.4, 1.0, 5.55, 2.35, 'Why the factor is three', WARM, size=13)
    f.text(7.55, 1.5, 5.3, 'u_r = −(r/2) ∂_z v,   τ_zz = 2μ ∂_z v,   τ_rr = −μ ∂_z v', 12, FG, bold=True)
    f.text(7.55, 2.1, 5.3, 'τ_zz − τ_rr = 3μ ∂_z v:  extensional stress is three times the shear-viscosity scale.', 12.5, WARM)
    hbars(f, 7.5, 3.55, 5.45, [('simple shear: μ', 1, BLUE), ('stretching: 3μ', 3, WARM)], 3.2, label_w=2.4, fmt='{:g}', unit='μ', size=12, bar_h=.4, gap=.2)
    f.text(7.5, 4.9, 5.4, '∂ₜv + v∂_z v = −(σ_j/ρ) ∂_z κ + [3μ/(ρA)] ∂_z(A ∂_z v)', 12, FG, bold=True)
    f.text(1.0, 6.0, 6.0, 'Where the jet is thinner (a < a₀ with k a₀ < 1) κ is larger, so pressure pushes liquid toward the thicker parts.', 12, FG)
    f.text(7.5, 5.55, 5.4, 'The slender axial momentum law keeps the full geometric curvature.', 11.5, MUT)
    f.note('Newtonian stress and slender momentum of Eq. C3-E20.')


def e21(f):
    q = np.linspace(0, 1, 4000)
    g = cylinder_growth(q)
    qm = q[int(np.argmax(g))]
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 1), (0, .4), 'dimensionless wavenumber q = k a₀', 'growth rate g t_σ', (0, .25, .5, .75, 1), (0, .1, .2, .3, .4), fx='{:.2f}', fy='{:.1f}')
    p.curve(q, g, ACC, 3)
    p.fill(q, np.zeros_like(q), g, ACC, .18)
    p.pt(qm, g.max(), WARM)
    p.vline(qm, WARM)
    p.label(qm, g.max(), f'peak: q = {qm:.3f}, g t_σ = {g.max():.4f}', WARM, 12, w=3.2, dx=-3.3, dy=-.05)
    p.label(.82, .06, 'stable for q ≥ 1', MUT, 11.5, w=1.4)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Rayleigh–Plateau growth (inviscid)', ACC, size=13)
    f.text(7.85, 2.0, 5.0, 'g² = (σ_j / ρa₀³) q(1 − q²) I₁(q)/I₀(q)', 12.5, FG, bold=True)
    f.text(7.85, 2.6, 5.0, 'a = a₀ + δ(t) cos[k(z − U_j t)],  δ = δ₀ e^(gt)', 12, WARM, bold=True)
    zz = np.linspace(7.9, 12.8, 100)
    yc = 4.45
    f.poly([(z, yc - .5 - .17 * math.cos((z - 7.9) * 2.1)) for z in zz] + [(z, yc + .5 + .17 * math.cos((z - 7.9) * 2.1)) for z in zz[::-1]], fill=LIQ, line=ACC, lw=2)
    f.dim(7.9, 5.35, 7.9 + math.pi / 2.1, 5.35, 'λ = 2πa₀/q', MUT, 11.5, side=-1)
    f.text(1.0, 6.27, 12, 'Surface tension destabilises a liquid cylinder for 0 < q < 1; the fastest mode has wavelength λ_max = 2πa₀ / 0.697.', 12.5, FG)
    f.note('Linear growth rate of Eq. C3-E21 from the modified Bessel functions I₀, I₁.')


def e22(f):
    a0 = 5e-6
    ts = math.sqrt(1000 * a0 ** 3 / .072)
    gmax = .343339 / ts
    t = np.linspace(0, 20, 300)
    d = .01 * np.exp(gmax * t * 1e-6)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 20), (.005, 1.5), 'time  (µs)', 'δ / a₀', (0, 5, 10, 15, 20), (.01, .1, 1), fx='{:g}', fy='{:g}', ylog=True)
    p.curve(t, d, ACC, 3)
    tf = 3.133
    p.vline(tf, WARM)
    p.pt(tf, .01 * math.exp(gmax * tf * 1e-6), WARM)
    p.label(tf, .0226, 'flight 3.13 µs: 1 % → 2.26 %', WARM, 12, w=3.0, dx=.15, dy=-.6)
    tl = math.log(100) / gmax * 1e6
    p.vline(tl, PINK)
    p.label(tl, .5, f'δ = a₀ at {tl:.1f} µs', PINK, 12, w=1.8, dx=-1.9, dy=-.1)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Declared flight case', ACC, size=13.5)
    rows = [('t_σ = √(ρa₀³/σ_j)', f'{ts * 1e6:.3f} µs'), ('g_max = 0.343339 / t_σ', f'{gmax * 1e-6:.4f} µs⁻¹'), ('Re = ρU_jd_j/μ', '319'), ('We = ρU_j²d_j/σ_j', '141'), ('Oh = μ/√(ρσ_jd_j)', '0.0373')]
    y = 2.0
    for a, b in rows:
        f.text(7.85, y, 3.2, a, 12.5, FG)
        f.text(11.0, y, 1.8, b, 13, WARM, bold=True, wrap=False)
        y += .5
    f.text(7.85, 4.7, 5.0, 'Growth during the actual flight stays small, but extrapolating to the 17.7 µs threshold leaves exact breakup unresolved.', 12, MUT)
    f.text(1.0, 6.27, 12, 'δ_arr/a₀ = (δ₀/a₀) exp(g_max H/U_j) with H = 100 µm, U_j = 31.9 m/s, a₀ = 5 µm, ρ = 1000 kg/m³, σ_j = 0.072 N/m, μ = 1 mPa s.', 12, FG)
    f.note('Finite-flight growth and regime numbers of Eq. C3-E22 (log vertical axis).')


FIGS = {12: e12, 13: e13, 14: e14, 15: e15, 16: e16, 17: e17, 18: e18, 19: e19, 20: e20, 21: e21, 22: e22}
