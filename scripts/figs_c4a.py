"""Chapter 4, equations 01-12 plus 40, 41."""
import math

import numpy as np

from figlib import *

RHO_F, H_F, E_F, NU = 2330.0, 10e-6, 2.0e9, .35
DF = E_F * H_F ** 3 / (12 * (1 - NU ** 2))


def _film(f, x, y, w, label=True):
    f.rect(x, y, w, .22, fill=STEEL, line=MUT, lw=1.4)
    if label:
        f.text(x, y + .26, w, 'solid film', 11.5, MUT, 'center')


def e01(f):
    f.panel(.4, 1.0, 7.4, 5.3, 'Traction on the exposed film face', ACC, size=13.5)
    f.rect(.8, 3.42, 6.6, 1.18, fill=LIQ, line=LIQ2, lw=1)
    f.rect(.8, 1.6, 6.6, 1.6, fill=STEEL, line=MUT, lw=1.2, opacity=.8)
    f.text(.9, 1.7, 3, 'solid film', 12, MUT, bold=True)
    f.text(.9, 3.6, 3, 'liquid', 12, ACC, bold=True)
    f.line(2.2, 3.2, 2.2, 2.4, WARM, 3, arrow=True)
    f.text(1.0, 2.5, 1.0, 'n_f', 12, WARM, 'right', bold=True)
    f.line(4.4, 3.25, 4.4, 4.2, PINK, 3.5, arrow=True)
    f.text(4.55, 3.95, 2.7, 'normal part −p n', 11.5, PINK, bold=True)
    f.line(5.0, 3.1, 6.4, 3.1, BLUE, 3.5, arrow=True)
    f.text(5.0, 2.55, 2.4, 'shear part 2μ D·n', 11.5, BLUE, bold=True)
    f.text(.6, 5.15, 7.0, 'D_u = (∇u + ∇uᵀ)/2,   T_l = −pI + 2μD_u,   t_l = T_l n_f', 12.5, FG, bold=True)
    f.text(.6, 5.65, 7.0, 'The normal fixes the sign: positive pressure presses on the film.', 12, MUT)
    f.panel(8.0, 1.0, 4.95, 5.3, 'Two parts of one traction', ACC, size=13.5)
    hbars(f, 8.15, 1.7, 4.7, [('pressure −p (Pa)', 47.2e6, PINK), ('viscous 2μD (Pa)', 3.2e3, BLUE)], 1e8, label_w=1.9, fmt='{:.3g}', unit='', size=11.5, bar_h=.4, gap=.25, log=True, vmin=1e3)
    f.bullets(8.15, 3.1, 4.7, ['Pressure acts along n; viscous stress adds a tangential part.', 'For μ = 1 mPa s and strain rate 3×10⁶ s⁻¹ the shear is thousands of Pa, far below the 47 MPa contact scale.', 'The film feels the traction, not the liquid velocity.'], 12)
    f.note('Newtonian traction of Eq. C4-E01; bar values are order-of-magnitude illustrations (log axis).')


def e02(f):
    t = np.linspace(0, 40, 300)
    F = np.where(t < 34, 1.0, 0.0) * (1 - np.exp(-t / 1.5))
    p = Plot(f, 1.0, 1.5, 6.4, 3.6, (0, 40), (0, 1.2), 'time  (ns)', 'F_l(t) (relative)', (0, 10, 20, 30, 40), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    p.fill(t, np.zeros_like(t), F, ACC, .25)
    p.curve(t, F, ACC, 3)
    p.vline(0, MUT)
    p.label(2, .5, 'area = impulse I_l = ∫F dt', ACC, 12, w=3, dx=.8)
    p.label(30, 1.12, 't_b', MUT, 11.5, w=.5)
    f.panel(7.7, 1.5, 5.25, 3.6, 'Three different integrals', ACC, size=13.5)
    for i, (a, b, c) in enumerate([('force', 'F_l = ∫ t_l dA', BLUE), ('impulse', 'I_l = ∫ F_l dt', WARM), ('work', 'W_l = ∫∫ t_l·v_f dA dt', PINK)]):
        y = 2.05 + i * .78
        f.text(7.85, y, 1.2, a, 12.5, c, bold=True)
        f.text(9.0, y, 3.8, b, 12.5, FG, bold=True)
    f.text(7.85, 4.35, 4.9, 'Work needs the surface velocity v_f; force and impulse do not.', 12, MUT)
    f.text(1.0, 6.0, 12, 'The same footprint A_f(t) supplies force and impulse. A load on a wall that does not move delivers impulse but no work.', 12.5, FG)
    f.text(1.0, 6.5, 12, 'Event window: t_a to t_b.', 12, MUT)
    f.note('Exact definitions of Eq. C4-E02; curve is a schematic force history.')


def e03(f):
    z = np.linspace(-.5, .5, 100)
    f.panel(.4, 1.0, 6.2, 5.3, 'One film, two thickness integrals', ACC, size=13.5)
    f.rect(1.0, 2.2, 3.6, 2.4, fill=LIQ, line=ACC, lw=2)
    f.dim(4.85, 2.2, 4.85, 4.6, 'h_f', MUT, 12, side=1)
    f.line(1.0, 3.4, 4.6, 3.4, MUT, 1.2, dash=True)
    f.text(1.3, 3.45, 1.5, 'mid-plane', 11, MUT)
    f.text(1.2, 2.35, 3.0, 'density ρ_f is uniform', 11.5, FG)
    f.text(.6, 5.0, 5.8, 'm_A = ∫ρ_f dz = ρ_f h_f', 13, ACC, bold=True)
    f.text(.6, 5.5, 5.8, 'D_f = E_f/(1−ν²) ∫z² dz = E_f h_f³ / [12(1−ν_f²)]', 12.5, WARM, bold=True)
    zz = np.linspace(-.5, .5, 100)
    p = Plot(f, 7.2, 1.5, 2.6, 3.6, (0, 1), (-.5, .5), 'weight', 'z / h_f', (0, 1), (-.5, 0, .5), fx='{:g}', fy='{:g}')
    f.rect(p.X(0), p.Y(.5), p.X(1) - p.X(0), p.Y(-.5) - p.Y(.5), fill=ACC, line=ACC, lw=1, opacity=.3)
    p.label(.05, .4, 'inertia: 1', ACC, 11.5, w=1.4)
    q = Plot(f, 10.5, 1.5, 2.4, 3.6, (0, .3), (-.5, .5), 'z²', '', (0, .25), (-.5, 0, .5), fx='{:g}', fy='{:g}')
    q.curve(zz ** 2, zz, WARM, 3)
    q.label(.02, .42, 'stiffness: z²', WARM, 11.5, w=1.4)
    f.text(7.2, 5.95, 5.7, f'h_f = 10 µm, E_f = 2 GPa, ν_f = 0.35: m_A = {RHO_F * H_F * 1e3:.3f} g/m², D_f = {DF:.4g} N m.', 12, FG)
    f.text(7.2, 6.55, 5.7, 'Outer fibres dominate bending: thickness enters as h³, inertia only as h.', 12, WARM)
    f.note('Plate parameters of Eq. C4-E03 (ρ_f = 2330 kg/m³ for the film mass).')


def e04(f):
    f.text(.5, 1.0, 12.3, 'Three energies of a vibrating film (shaded: where each is evaluated)', 13.5, ACC, bold=True)
    xs = np.linspace(0, 1, 120)
    cards = [('Kinetic K_f', 'm_A/2 ∫ ẇ² dA', 'velocity of every patch', BLUE), ('Bending U_b', 'D_f/2 ∫ [w_xx² + w_yy² + 2ν w_xx w_yy + 2(1−ν) w_xy²] dA', 'curvature of the surface', WARM), ('Tension U_T', 'T₀/2 ∫ |∇w|² dA', 'slope of the surface', PINK)]
    for i, (h, e, n, c) in enumerate(cards):
        x = .5 + i * 4.15
        f.panel(x, 1.5, 3.95, 4.0, h, c, size=13.5)
        yb = 3.3
        if i == 0:
            for k in range(7):
                xx = x + .35 + k * .5
                h_ = .8 * math.sin(math.pi * (k + .5) / 7)
                f.line(xx, yb, xx, yb - h_, c, 3, arrow=True)
            f.line(x + .3, yb, x + 3.6, yb, MUT, 1.4)
        elif i == 1:
            f.path([(x + .3 + 3.3 * s, yb - .75 * math.sin(math.pi * s) ** 2 * math.cos(math.pi * s * 2)) for s in xs], c, 3)
            f.text(x + .4, 1.95, 3.2, 'sharp bends cost most', 11.5, c)
        else:
            f.path([(x + .3 + 3.3 * s, yb - .8 * math.sin(math.pi * s)) for s in xs], c, 3)
            f.line(x + .3, yb - .8 * math.pi * 0, x + 1.2, yb - .8 * math.sin(math.pi * .27) * 1.0, MUT, 1.5, dash=True)
            f.text(x + .4, 1.95, 3.2, 'steep slopes cost most', 11.5, c)
        f.text(x + .1, 4.25, 3.75, e, 11, FG, 'center', bold=True)
        f.text(x + .1, 5.1, 3.75, n, 11.5, MUT, 'center')
    f.text(.5, 5.8, 12.3, 'Bending is stored by curvature, tension by slope, kinetic energy by velocity: three separate integrals over the same film Ω_f.', 12.5, FG)
    f.text(.5, 6.35, 12.3, 'Valid for small deflection, uniform thin plate, with in-plane tension T₀ taken as given.', 12, MUT)
    f.note('Linear-plate energies of Eq. C4-E04; the pictures are schematic.')


def e40(f):
    f.text(.5, 1.0, 12.3, 'Integrating by parts twice moves derivatives from δw onto the moment tensor', 13.5, ACC, bold=True)
    steps = [('Start', 'δU_b = ∫ B_αβ ∂α∂β(δw) dA', 'derivatives sit on δw', ACC), ('Once', '= ∮ n_α B_αβ ∂β(δw) dℓ − ∫ (∂α B_αβ) ∂β(δw) dA', 'edge moment term appears', WARM), ('Twice', '= ∮ n_α B_αβ ∂β δw dℓ − ∮ n_β ∂αB_αβ δw dℓ + ∫ (∂α∂β B_αβ) δw dA', 'edge shear term appears', PINK)]
    for i, (h, e, n, c) in enumerate(steps):
        y = 1.55 + i * 1.2
        f.panel(.5, y, 12.3, 1.05, None, c)
        f.text(.65, y + .08, 1.1, h, 13, c, bold=True)
        f.text(1.8, y + .1, 7.6, e, 12, FG, bold=True)
        f.text(9.6, y + .1, 3.1, n, 11.5, MUT)
    f.panel(.5, 5.2, 6.0, 1.15, 'B_αβ', WARM, size=13)
    f.text(.65, 5.6, 5.7, 'B_αβ = D_f[(1−ν_f) w_αβ + ν_f δ_αβ ∇²w]', 12, FG, bold=True)
    f.panel(6.8, 5.2, 6.0, 1.15, 'Fixed clamp', ACC, size=13)
    f.text(6.95, 5.6, 5.7, 'w = 0 and ∂ₙw = 0 on the edge ⇒ both boundary terms vanish', 12, FG, bold=True)
    f.note('Boundary terms of Eq. C4-E40 (the term order follows the equation).')


def e05(f):
    f.text(.5, 1.0, 12.3, 'With a fixed clamp, the boundary terms drop and one operator is left', 13.5, ACC, bold=True)
    f.panel(.5, 1.5, 6.0, 2.5, 'Bending variation', WARM, size=13.5)
    f.text(.65, 2.0, 5.7, 'coefficient of w_xxyy:  2ν_f + 2(1 − ν_f) = 2', 12.5, FG, bold=True)
    f.text(.65, 2.6, 5.7, 'δU_b = D_f ∫ (w_xxxx + 2w_xxyy + w_yyyy) δw dA = D_f ∫ ∇⁴w δw dA', 12, WARM, bold=True)
    f.text(.65, 3.35, 5.7, 'Poisson ratio cancels from the interior operator.', 11.5, MUT)
    f.panel(6.8, 1.5, 6.0, 2.5, 'Tension variation', PINK, size=13.5)
    f.text(6.95, 2.0, 5.7, 'δU_T = T₀ ∫ ∇w·∇δw dA', 12.5, FG, bold=True)
    f.text(6.95, 2.55, 5.7, '= −T₀ ∫ ∇²w δw dA   (δw = 0 on the clamp)', 12.5, PINK, bold=True)
    nu = np.linspace(0, .5, 50)
    p = Plot(f, 1.0, 4.4, 5.2, 1.7, (0, .5), (1.5, 2.5), 'ν_f', 'coefficient', (0, .25, .5), (2,), fx='{:g}', fy='{:g}')
    p.curve(nu, 2 * nu + 2 * (1 - nu), ACC, 3)
    p.label(.05, 2.3, '2ν + 2(1 − ν) = 2 for every ν', ACC, 11.5, w=3.4)
    f.text(7.0, 4.4, 5.8, 'Result: D_f ∇⁴w − T₀ ∇²w are the elastic restoring terms.', 13.5, WARM, bold=True)
    f.text(7.0, 5.1, 5.8, 'They are the same terms that enter the transient balance of Eq. C4-E06.', 12.5, FG)
    f.note('Clamped variational identity of Eq. C4-E05.')


def e06(f):
    f.rect(.5, 1.0, 6.2, 5.3, fill=LIQ, line=LIQ2, lw=1.2, round_=True)
    f.text(.65, 1.05, 5.9, 'Film element: four forces balance inertia', 13, ACC, bold=True)
    f.rect(1.2, 3.5, 4.8, .3, fill=STEEL, line=MUT, lw=1.5)
    f.line(3.6, 2.3, 3.6, 3.45, PINK, 4, arrow=True)
    f.text(3.7, 2.4, 2.8, 'p_load (pressure)', 11.5, PINK, bold=True)
    f.line(2.2, 4.4, 2.2, 3.85, BLUE, 3.5, arrow=True)
    f.text(1.0, 4.5, 2.5, 'D_f∇⁴w − T₀∇²w (elastic)', 11.5, BLUE, bold=True)
    f.line(5.0, 4.4, 5.0, 3.85, WARM, 3.5, arrow=True)
    f.text(4.0, 4.5, 2.5, 't_coh (cohesive)', 11.5, WARM, bold=True)
    f.line(3.6, 2.8, 3.6, 2.45, MUT, 1, dash=True)
    f.text(1.0, 5.25, 5.5, 'm_A ẅ + D_f∇⁴w − T₀∇²w = p_load − t_coh', 12.5, FG, bold=True)
    f.text(1.0, 5.75, 5.5, 'm_A ẅ is the inertia that is left over.', 12, MUT)
    f.panel(6.9, 1.0, 6.05, 5.3, 'Initial and boundary data', ACC, size=13.5)
    f.bullets(7.05, 1.6, 5.8, ['At rest at t = 0:  w = 0,  ẇ = 0 everywhere.', 'Clamped edge:  w = 0 and ∂ₙw = 0 (no deflection, no slope).', 'Loading enters only through p_load; cohesive resistance only through t_coh.'], 12.5)
    f.text(7.05, 3.8, 5.8, 'Without the initial data the equation has many solutions; without the clamp it cannot be solved.', 12.5, WARM)
    f.text(7.05, 4.7, 5.8, 'Reduced model: small deflection, thin uniform film, tension T₀ prescribed.', 12, MUT)
    f.note('Reduced transient plate balance of Eq. C4-E06; schematic.')


def e41(f):
    steps = [('applied work', 1.0, ACC), ('− cohesive loss', -.25, WARM), ('= stored + moving', None, BLUE)]
    f.panel(.4, 1.0, 5.9, 5.3, 'Power ledger (schematic)', ACC, size=13.5)
    waterfall(f, .7, 1.7, 5.3, 3.3, steps, 1.2, fmt='{:.2f}', yticks=(0, .5, 1), ylabel='')
    f.text(.6, 5.45, 5.6, 'd(K_f + U_b + U_T)/dt = ∫ p_load ẇ dA − ∫ t_coh ẇ dA', 11.5, FG, bold=True)
    f.text(.6, 5.9, 5.6, 'Each term has units of watts.', 11.5, MUT)
    f.panel(6.5, 1.0, 6.45, 5.3, 'Multiply the balance by ẇ and integrate', ACC, size=13.5)
    rows = [('inertia', '∫ m_A ẅ ẇ dA = dK_f/dt', BLUE), ('bending', '∫ D_f ∇⁴w ẇ dA = dU_b/dt', WARM), ('tension', '−∫ T₀ ∇²w ẇ dA = dU_T/dt', PINK)]
    for i, (a, b, c) in enumerate(rows):
        y = 1.65 + i * .75
        f.text(6.7, y, 1.3, a, 12.5, c, bold=True)
        f.text(8.0, y, 4.9, b, 12.5, FG, bold=True)
    f.text(6.7, 4.0, 6.1, 'These identities need the fixed clamp: boundary power terms are zero.', 12, WARM)
    f.text(6.7, 4.7, 6.1, 'Reading: the film cannot gain energy except through the work of the load, minus what the cohesive layer takes.', 12.5, FG)
    f.note('Plate power identity of Eq. C4-E41; waterfall values are illustrative.')


def e07(f):
    f.rect(.5, 1.0, 7.2, 5.3, fill=LIQ, line=LIQ2, lw=1.2, round_=True)
    f.text(.65, 1.05, 6.9, 'Two sheets in series', 13.5, ACC, bold=True)
    f.line(2.0, 1.9, 2.0, 2.75, PINK, 4, arrow=True)
    f.text(2.1, 1.85, 3, 'p_liq from the liquid', 11.5, PINK, bold=True)
    f.rect(1.2, 2.8, 5.6, .3, fill=STEEL, line=MUT, lw=1.5)
    f.text(3.9, 2.45, 2.5, 'PVC sheet (P)', 12, MUT, bold=True)
    f.spring(3.0, 3.1, 3.0, 4.0, 6, .1, ACC, 2)
    f.spring(5.0, 3.1, 5.0, 4.0, 6, .1, ACC, 2)
    f.text(3.2, 3.4, 2.0, 'contact\nload t_P→f', 11, ACC, bold=True)
    f.rect(1.2, 4.0, 5.6, .3, fill=STEEL, line=MUT, lw=1.5)
    f.text(1.2, 4.4, 2.0, 'film (f)', 12, MUT, bold=True)
    f.line(4.0, 5.2, 4.0, 4.4, WARM, 3.5, arrow=True)
    f.text(4.1, 4.85, 3.0, 't_coh (resists)', 11.5, WARM, bold=True)
    f.text(1.0, 5.6, 6.5, 'The film sees t_P→f, not p_liq: the intermediate sheet filters the load.', 12, WARM)
    f.panel(7.9, 1.0, 5.05, 5.3, 'Two coupled plate equations', ACC, size=13.5)
    f.text(8.05, 1.55, 4.8, 'm_A,P ẅ_P + D_P∇⁴w_P − T_P∇²w_P = p_liq − t_P→f', 11.5, FG, bold=True)
    f.text(8.05, 2.55, 4.8, 'm_A ẅ + D_f∇⁴w − T₀∇²w = t_P→f − t_coh', 11.5, FG, bold=True)
    f.text(8.05, 3.5, 4.8, 'The same t_P→f is a loss for P and a load for f (Newton third law).', 12, MUT)
    f.text(8.05, 4.4, 4.8, 'Conditional: valid only while the sheets stay in contact; t_P→f itself needs a contact law.', 12, WARM)
    f.note('Coupled-sheet model of Eq. C4-E07; schematic.')


def e08(f):
    t = np.linspace(0, 40, 400)
    pl = np.where(t < 34, 1.0, 0.0)
    react = np.cumsum(.015 * (1 - np.exp(-t / 10))) * (t[1] - t[0])
    p = Plot(f, 1.0, 1.5, 6.4, 3.6, (0, 40), (0, 1.2), 'time (ns)', 'pressure / reaction (rel.)', (0, 10, 20, 30, 40), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    p.fill(t, np.zeros_like(t), pl, ACC, .25)
    p.curve(t, pl, ACC, 3)
    r = .03 * (1 - np.exp(-t / 5)) * (t / 40) * 4
    p.curve(t, r, WARM, 3)
    p.label(5, .8, 'J_A = ∫ p_load dt (applied)', ACC, 12, w=3.2)
    p.label(8, .3, 'reactions ∫ [D_f∇⁴w − T₀∇²w + t_coh] dt', WARM, 11.5, w=4.2, dy=.05)
    f.panel(7.7, 1.5, 5.25, 3.6, 'Exact pulse integral', ACC, size=13.5)
    f.text(7.85, 2.05, 5.0, 'm_A[ẇ(t_b) − ẇ(t_a)] = J_A − ∫ [D_f∇⁴w − T₀∇²w + t_coh] dt', 12, FG, bold=True)
    f.bullets(7.85, 3.1, 5.0, ['Left: momentum per area gained.', 'Right: applied impulse minus impulse of the reactions.', 'Reactions are small only if the pulse is shorter than the plate response.'], 12)
    f.text(1.0, 6.0, 12, 'A free velocity jump J_A/m_A is only the upper limit: elastic and cohesive reactions subtract from it.', 12.5, FG)
    f.note('Time-integrated momentum balance of Eq. C4-E08; curves are schematic.')


def e09(f):
    mA = RHO_F * H_F
    J = np.linspace(0, .1, 100)
    p = Plot(f, 1.0, 1.5, 6.0, 3.8, (0, .1), (0, 5), 'areal impulse J_A  (N s / m²)', 'film speed Δẇ  (m/s)', (0, .025, .05, .075, .1), (0, 1, 2, 3, 4, 5), fx='{:.3f}', fy='{:g}')
    p.curve(J, J / mA, ACC, 3)
    p.label(.005, 4.4, 'Δẇ = J_A / m_A', ACC, 12.5, w=2.4)
    q = Plot(f, 7.8, 1.5, 5.1, 3.8, (0, .1), (0, .25), 'areal impulse J_A  (N s / m²)', '𝓔_A  (J / m²)', (0, .05, .1), (0, .1, .2), fx='{:.2f}', fy='{:.1f}')
    q.curve(J, J ** 2 / (2 * mA), WARM, 3)
    q.label(.005, .22, '𝓔_A = J_A² / (2m_A)', WARM, 12, w=2.8)
    f.text(1.0, 6.1, 12, f'Speed grows linearly with impulse, energy quadratically. Here m_A = ρ_f h_f = {mA * 1e3:.1f} g/m² (ρ_f = 2330 kg/m³, h_f = 10 µm).', 12, FG)
    f.text(1.0, 6.6, 12, 'Valid for a pulse much shorter than the plate response times (next figure); this energy may later feed deformation and fracture.', 12.5, WARM)
    f.note('Short-pulse free response of Eq. C4-E09.')


def e10(f):
    af = 100e-6
    mA = RHO_F * H_F
    tb = af ** 2 * math.sqrt(mA / DF)
    Tn = 1.0
    f.text(.5, 1.0, 12.3, 'Compare the pulse with three response times', 13.5, ACC, bold=True)
    vals = [('t_b = a_f² √(m_A/D_f)  (bending)', tb * 1e9, WARM), ('t_T = a_f √(m_A/T₀)  (tension, T₀ = 1 N/m)', af * math.sqrt(mA / Tn) * 1e9, BLUE), ('t_n = √(m_A/K_n)  (cohesive, K_n = 10¹³ Pa/m)', math.sqrt(mA / 1e13) * 1e9, PINK), ('impulse-equivalent pulse τ_eq', 33.78, ACC)]
    hbars(f, .5, 1.6, 12.3, vals, 1e6, label_w=5.4, fmt='{:.3g}', unit=' ns', size=12.5, bar_h=.5, gap=.3, log=True, vmin=1)
    f.panel(.5, 5.0, 6.0, 1.5, 'Short pulse', ACC, size=13)
    f.text(.65, 5.45, 5.7, 'τ ≪ response time: the film cannot react during the pulse, so it gets a free velocity (Eq. C4-E09).', 12, FG)
    f.panel(6.8, 5.0, 6.0, 1.5, 'Long pulse', WARM, size=13)
    f.text(6.95, 5.45, 5.7, 'τ ≳ response time: elastic and cohesive reactions act during the pulse and reduce the net impulse.', 12, FG)
    f.note('Term-balance times of Eq. C4-E10 for a_f = 100 µm, h_f = 10 µm (E_f = 2 GPa, ν = 0.35); T₀ and K_n are illustrative.')


def e11(f):
    f.panel(.4, 1.0, 6.3, 5.3, 'Energy released per area of crack', ACC, size=13.5)
    f.rect(.8, 2.0, 5.5, .35, fill=STEEL, line=MUT, lw=1.4)
    f.rect(.8, 3.9, 5.5, .35, fill=STEEL, line=MUT, lw=1.4)
    f.rect(.8, 2.35, 5.5, 1.55, fill=LIQ, line=None if False else MUT, lw=.8, opacity=.5)
    f.poly([(.8, 3.0), (3.0, 3.0), (3.0, 3.25), (.8, 3.25)], fill=BG, line=WARM, lw=2)
    f.text(1.0, 2.55, 1.8, 'open crack', 11.5, WARM, bold=True)
    f.line(3.0, 3.12, 4.0, 3.12, PINK, 3.5, arrow=True)
    f.text(3.1, 2.65, 3.0, 'advances by dA_c', 11.5, PINK, bold=True)
    f.text(.6, 4.6, 6.0, 'G = −∂𝒫/∂A_c |𝒞   (𝒞 = the chosen load control)', 12.5, FG, bold=True)
    f.text(.6, 5.1, 6.0, 'Fracture advances when G ≥ Γ(ψ, T_i, v_c).', 12.5, WARM, bold=True)
    f.text(.6, 5.65, 6.0, '𝒫 depends on the control: fixed load and fixed displacement differ.', 11.5, MUT)
    G = np.linspace(0, 2.5, 100)
    p = Plot(f, 7.5, 1.5, 5.3, 3.6, (0, 2.5), (0, 1.2), 'driving force G / Γ', 'crack state', (0, 1, 2), (0, 1), fx='{:g}', fy='{:g}')
    p.curve(np.array([0, 1, 1, 2.5]), np.array([0, 0, 1, 1]), ACC, 3)
    p.vline(1, WARM)
    p.label(.05, .4, 'stays shut', MUT, 12, w=1.6)
    p.label(1.15, .5, 'advances', ACC, 12, w=1.4)
    p.label(1, 1.12, 'G = Γ', WARM, 12, w=1, dx=.1)
    f.text(7.5, 6.0, 5.4, 'Quasistatic criterion: needs G computed with the correct load path.', 12, FG)
    f.note('Energy-release criterion of Eq. C4-E11; schematic threshold.')


def e12(f):
    steps = [('P_load (power in)', 1.0, ACC), ('− dK/dt − dU/dt', -.45, BLUE), ('− Γ v_c ℓ (fracture)', -.4, WARM), ('− P_other', -.15, PINK), ('= 0', None, MUT)]
    f.text(.5, 1.0, 6.0, 'Where the load power goes (schematic share)', 13.5, ACC, bold=True)
    waterfall(f, .7, 1.7, 6.0, 3.3, steps, 1.2, fmt='{:.2f}', yticks=(0, .5, 1), ylabel='')
    f.panel(7.2, 1.0, 5.75, 4.3, 'Dynamic balance on a moving crack', ACC, size=13.5)
    f.text(7.35, 1.55, 5.5, 'P_load = d(K_f + U_f)/dt + ∫ Γ v_c dℓ + P_other', 12, FG, bold=True)
    f.bullets(7.35, 2.35, 5.5, ['K_f: motion of the film, U_f: elastic energy.', 'Γ v_c along the front length is the fracture power.', 'P_other: dissipation or radiation not otherwise counted.'], 12)
    f.text(7.35, 4.0, 5.5, 'Part of the load work is stored as kinetic energy before the crack moves.', 12, WARM)
    f.text(.5, 5.6, 12.3, 'Quasistatic G ≥ Γ is the slow limit of this balance (K_f → 0).', 12.5, FG)
    f.text(.5, 6.15, 12.3, 'Conditional: needs a fracture-resistance law Γ(ψ, T_i, v_c) for the actual interface.', 12, MUT)
    f.note('Dynamic energy balance of Eq. C4-E12; shares are illustrative.')


FIGS = {1: e01, 2: e02, 3: e03, 4: e04, 40: e40, 5: e05, 6: e06, 41: e41, 7: e07, 8: e08, 9: e09, 10: e10, 11: e11, 12: e12}
