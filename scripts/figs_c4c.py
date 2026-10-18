"""Chapter 4, equations 25-39 (cohesive law, jet inheritance, energy screens, placement)."""
import math

import numpy as np

from figlib import *

GAM, TMAX, KN = 0.005, 0.10e6, 1e13
D0 = TMAX / KN
DC = 2 * GAM / TMAX
RHO_J, D_J, L_J, E_J, N_J = 1000.0, 10e-6, 50e-6, 2.0e-9, 25
M_J = RHO_J * math.pi * D_J ** 2 * L_J / 4
U_J = math.sqrt(2 * E_J / M_J)
E_IN = N_J * E_J
I_IN = N_J * M_J * U_J
M_F = 2330.0 * 1.0e-6 * 1.0e-6
ETA_E, ETA_I = .20, .50
E_SOL = ETA_E * E_IN
I_NET = ETA_I * I_IN
A_F = 1.0e-6


def _cohesive(d, g0, gc, T):
    return np.where(d <= g0, T * d / g0, np.where(d < gc, T * (gc - d) / (gc - g0), 0.0))


def e25(f):
    d = np.linspace(0, 140, 600)
    t = _cohesive(d * 1e-9, D0, DC, TMAX) / 1e6
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 140), (0, .13), 'opening δ  (nm)', 'traction t_n  (MPa)', (0, 20, 40, 60, 80, 100, 120, 140), (0, .05, .1), fx='{:g}', fy='{:.2f}')
    p.fill(d, np.zeros_like(d), t, ACC, .22)
    p.curve(d, t, ACC, 3.4)
    p.pt(D0 * 1e9, TMAX / 1e6, WARM)
    p.pt(DC * 1e9, 0, PINK)
    p.label(D0 * 1e9, TMAX / 1e6, 'peak T_max = 0.10 MPa at δ₀ = 10 nm', WARM, 11.5, w=3.4, dx=.15, dy=-.1)
    p.label(4, .045, 'slope K_n', ACC, 11.5, w=1.2, dy=-.1)
    p.label(DC * 1e9, 0, 'δ_c = 100 nm', PINK, 11.5, w=1.6, dx=-1.7, dy=-.5)
    p.label(52, .085, 'softening branch', MUT, 11.5, w=1.8)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Three-piece law', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'δ₀ = T_max / K_n', 13, FG, bold=True)
    f.text(7.85, 2.5, 5.0, 't_n = K_n δ                    (0 ≤ δ ≤ δ₀)', 12, WARM, bold=True)
    f.text(7.85, 3.0, 5.0, 't_n = T_max (δ_c − δ)/(δ_c − δ₀)   (δ₀ < δ < δ_c)', 11.5, WARM, bold=True)
    f.text(7.85, 3.5, 5.0, 't_n = 0                            (δ ≥ δ_c)', 12, WARM, bold=True)
    f.text(7.85, 4.15, 5.0, 'Strength, stiffness and a finite opening distance are three separate inputs.', 12, MUT)
    f.text(1.0, 6.27, 12, 'Examples use the Eq. C4-E27 values: T_max = 0.10 MPa, K_n = 10¹³ Pa/m, Γ = 0.005 J/m².', 12.5, FG)
    f.note('Adopted tensile cohesive law of Eq. C4-E25 with the teaching values.')


def e26(f):
    d = np.linspace(0, 140, 600)
    t = _cohesive(d * 1e-9, D0, DC, TMAX) / 1e6
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 140), (0, .13), 'opening δ  (nm)', 't_n  (MPa)', (0, 50, 100), (0, .05, .1), fx='{:g}', fy='{:.2f}')
    p.fill(d, np.zeros_like(d), t, ACC, .3)
    p.curve(d, t, ACC, 3)
    p.fill(d[d <= 10], np.zeros(int((d <= 10).sum())), t[d <= 10], BLUE, .45)
    area = np.trapezoid(t, d * 1e-9) * 1e6 if hasattr(np, 'trapezoid') else np.trapz(t, d * 1e-9) * 1e6
    p.label(62, .095, f'area = ½ T_max δ_c\n= {area:.4f} J/m²', FG, 12, w=2.4, dy=0)
    p.label(11, .115, 'elastic part: ½ T_max δ₀', BLUE, 11.5, w=2.6)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Work to separate = area', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'Γ = ∫₀^δ_c t_n dδ = T_max δ₀ / 2 + T_max (δ_c − δ₀) / 2', 11.5, FG, bold=True)
    f.text(7.85, 2.65, 5.0, 'Γ = T_max δ_c / 2   ⇒   δ_c = 2Γ / T_max', 13, WARM, bold=True)
    f.text(7.85, 3.3, 5.0, 'δ₀ < δ_c requires K_n > T_max² / (2Γ)', 12.5, PINK, bold=True)
    f.text(7.85, 4.0, 5.0, f'Here T_max²/(2Γ) = {TMAX ** 2 / (2 * GAM):.2e} Pa/m < K_n = 1.0×10¹³ Pa/m.', 12, MUT)
    f.text(1.0, 6.27, 12, 'Complete separation needs the whole traction–opening area, not just the peak value.', 12.5, FG)
    f.note('Work integral of Eq. C4-E26 (areas by quadrature).')


def e27(f):
    f.text(.5, 1.0, 12.3, 'Cohesive admissibility check with the teaching numbers', 13.5, ACC, bold=True)
    cards = [('given', 'Γ = 0.005 J/m²\nT_max = 0.10 MPa\nK_n = 10¹³ Pa/m', MUT), ('δ₀ = T_max / K_n', '10⁵ / 10¹³ = 1.0×10⁻⁸ m = 10 nm', BLUE), ('δ_c = 2Γ / T_max', '2(0.005) / 10⁵ = 1.0×10⁻⁷ m = 100 nm', PINK)]
    for i, (h, e, c) in enumerate(cards):
        x = .5 + i * 4.15
        f.panel(x, 1.5, 3.95, 2.1, h, c, size=13)
        f.text(x + .15, 2.1, 3.7, e, 12.5, FG, 'center', bold=True)
    hbars(f, .5, 4.0, 12.3, [('δ₀  (peak)', 10, WARM), ('δ_c  (final)', 100, PINK)], 120, label_w=2.2, fmt='{:g}', unit=' nm', size=12.5, bar_h=.45, gap=.25)
    f.text(.5, 5.4, 12.3, 'δ_c is ten times δ₀: the law has a distinct softening stage, so it is admissible (δ₀ < δ_c).', 13, WARM)
    f.text(.5, 6.0, 12.3, 'These are stipulated teaching values, not measured properties of a real interface.', 12, MUT)
    f.note('Admissibility calculation of Eq. C4-E27.')


def e28(f):
    f.text(.5, 1.0, 12.3, 'The jet that arrives at the film (inherited from Chapter 3)', 13.5, ACC, bold=True)
    f.rect(.8, 1.7, 5.0, .9, fill=LIQ, line=ACC, lw=2.4)
    f.line(5.9, 2.15, 6.9, 2.15, WARM, 4, arrow=True)
    f.dim(.8, 2.95, 5.8, 2.95, 'L_j = 50 µm', MUT, 12, side=-1)
    cards = [('mass', 'm_j = ρπd_j²L_j/4', f'{M_J:.9e} kg', BLUE), ('speed', 'U_j = √(2E_j/m_j)', f'{U_J:.7f} m/s', ACC), ('energy', 'E_in = N E_j', f'{E_IN * 1e9:.1f} nJ', WARM), ('momentum', 'I_in = N m_j U_j', f'{I_IN:.9e} N s', PINK)]
    for i, (h, e, v, c) in enumerate(cards):
        x = .5 + i * 3.1
        f.panel(x, 3.4, 2.95, 2.1, h, c, size=13)
        f.text(x + .08, 3.9, 2.8, e, 11.5, FG, 'center')
        f.text(x + .08, 4.6, 2.8, v, 11.5, WARM, 'center', bold=True)
    f.text(7.2, 1.8, 5.7, 'N = 25 jets, E_j = 2 nJ each, ρ = 1000 kg/m³, d_j = 10 µm.', 12.5, FG)
    f.text(.5, 5.8, 12.3, 'The input to the solid is a finite energy and an aligned momentum, not a pressure peak.', 13, WARM)
    f.text(.5, 6.35, 12.3, 'Assumes all 25 jets are activated, aligned and identical (Chapter 3 teaching state).', 12, MUT)
    f.note('Inherited jet state of Eq. C4-E28.')


def e29(f):
    f.text(.5, 1.0, 12.3, 'Declared coupling turns jet budgets into payload budgets', 13.5, ACC, bold=True)
    f.chain([('jet energy', f'E_in = {E_IN * 1e9:.0f} nJ'), ('× η_E = 0.20', f'E_solid = {E_SOL * 1e9:.1f} nJ')], 1.6, h=1.1, gap=.9, x0=.5, total=6.0, colors=[WARM, ACC], size=12.5)
    f.chain([('jet impulse', f'I_in = {I_IN * 1e9:.4f} nN s'), ('× η_I = 0.50', f'I_net = {I_NET * 1e9:.4f} nN s')], 1.6, h=1.1, gap=.9, x0=6.9, total=6.0, colors=[PINK, BLUE], size=12.5)
    f.panel(.5, 3.2, 6.0, 2.3, 'The film mass', ACC, size=13)
    f.rect(1.0, 4.1, 2.0, .22, fill=STEEL, line=MUT, lw=1.4)
    f.text(3.2, 3.75, 3.2, 'A_f = 1.00 mm² = 1.00×10⁻⁶ m²\nh_f = 1.00 µm, ρ_f = 2330 kg/m³', 11, FG)
    f.text(.65, 4.8, 5.8, 'm_f = ρ_f A_f h_f = (2330)(1.00×10⁻⁶)(1.00×10⁻⁶) = 2.33×10⁻⁹ kg', 11.5, WARM, bold=True)
    f.panel(6.8, 3.2, 6.0, 2.3, 'What the factors mean', WARM, size=13)
    f.bullets(6.95, 3.7, 5.7, ['η_E, η_I are declared fractions of energy and impulse that reach the film.', 'They are assumptions, not predictions of the model.'], 12)
    f.text(.5, 5.8, 12.3, 'Conditional budgets: every later pass or fail depends on η_E = 0.20 and η_I = 0.50.', 13, WARM)
    f.note('Coupling allocation of Eq. C4-E29 (declared teaching values).')


def e30(f):
    v = np.linspace(0, 2.5, 200)
    GA = .02
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 2.5), (0, 30), 'film departure speed v_f  (m/s)', 'E_req  (nJ)', (0, .5, 1, 1.5, 2, 2.5), (0, 10, 20, 30), fx='{:.1f}', fy='{:g}')
    for G, c in [(.005, ACC), (.02, PINK)]:
        p.curve(v, (G * A_F + .5 * M_F * v ** 2) * 1e9, c, 3)
    p.hline(E_SOL * 1e9, WARM)
    p.label(.1, 14, 'E_solid = 10 nJ (budget)', WARM, 11.5, w=2.4, dy=0)
    p.label(1.4, 6.2, 'Γ = 0.005 J/m²: Γ A_f = 5 nJ', ACC, 11.5, w=3.0)
    p.label(.05, 27.5, 'Γ = 0.020 J/m²: Γ A_f = 20 nJ', PINK, 11.5, w=3.0, dy=0)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Necessary, not sufficient', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'E_req(v_f) = Γ A_f + ½ m_f v_f²', 13, FG, bold=True)
    f.text(7.85, 2.5, 5.0, 'I_req(v_f) = m_f v_f', 13, FG, bold=True)
    f.text(7.85, 3.1, 5.0, 'pass:  E_solid ≥ E_req  and  I_net ≥ I_req', 12.5, WARM, bold=True)
    f.text(7.85, 3.8, 5.0, 'The whole release area A_f, not a pressure peak, sets the fracture energy cost.', 12, MUT)
    f.text(1.0, 6.27, 12, 'Energy to open the interface (Γ A_f) plus energy to move the released film (½ m_f v_f²).', 12.5, FG)
    f.note('Global screens of Eq. C4-E30 (A_f = 1 mm², m_f = 2.33 µg).')


def e31(f):
    f.text(.5, 1.0, 12.3, 'Failed release-energy screen: Γ = 0.020 J/m²', 13.5, ACC, bold=True)
    hbars(f, .5, 1.7, 12.3, [('energy needed  Γ A_f', 20.0, PINK), ('energy available  E_solid', 10.0, ACC)], 24, label_w=4.0, fmt='{:.1f}', unit=' nJ', size=13, bar_h=.6, gap=.35)
    f.panel(.5, 3.9, 6.0, 2.3, 'Arithmetic', ACC, size=13)
    f.text(.65, 4.4, 5.7, 'Γ A_f = (0.020)(1.00×10⁻⁶) J = 20.0 nJ', 12.5, FG, bold=True)
    f.text(.65, 5.0, 5.7, '20.0 nJ  >  E_solid = 10.0 nJ', 14, PINK, bold=True)
    f.panel(6.8, 3.9, 6.0, 2.3, 'Verdict', PINK, size=13)
    f.text(6.95, 4.4, 5.7, 'FAIL: the assigned source cannot release the whole interface even before adding departure energy.', 13, WARM, bold=True)
    f.text(6.95, 5.4, 5.7, 'The failure is for this declared Γ and η_E.', 11.5, MUT)
    f.note('Failed screen of Eq. C4-E31.')


def e32(f):
    vf = .5
    ek = .5 * M_F * vf ** 2 * 1e9
    f.text(.5, 1.0, 12.3, 'Passed screens for Γ = 0.005 J/m² and v_f = 0.50 m/s', 13.5, ACC, bold=True)
    waterfall(f, .5, 1.7, 6.2, 3.3, [('Γ A_f', 5.0, ACC), ('½ m_f v_f²', ek, BLUE), ('= E_req', None, WARM)], 11, fmt='{:.3f}', yticks=(0, 5, 10), ylabel='')
    f.text(7.2, 1.05, 5.6, 'Energy budget (nJ)', 13, ACC, bold=True)
    hbars(f, 7.2, 1.7, 5.6, [('E_req(0.50 m/s)', 5 + ek, WARM), ('E_solid', 10.0, ACC)], 11, label_w=2.0, fmt='{:.3f}', unit=' nJ', size=12, bar_h=.5, gap=.3)
    f.text(7.2, 3.5, 5.6, 'Impulse budget (nN s)', 13, ACC, bold=True)
    hbars(f, 7.2, 4.0, 5.6, [('I_req', M_F * vf * 1e9, WARM), ('I_net', I_NET * 1e9, ACC)], 1.8, label_w=2.0, fmt='{:.3f}', unit=' nN s', size=12, bar_h=.5, gap=.3)
    f.text(.5, 5.3, 12.3, f'E_req(0.50 m/s) = 5.00 + {ek:.5f} = {5 + ek:.5f} nJ  <  E_solid = 10.0 nJ', 13, WARM, bold=True)
    f.text(.5, 5.85, 12.3, f'I_req = m_f v_f = (2.33×10⁻⁹)(0.50) = {M_F * vf:.3e} N s  <  I_net = {I_NET:.3e} N s', 13, FG, bold=True)
    f.text(.5, 6.45, 12.3, 'Both necessary budgets pass; success is still not established.', 12.5, MUT)
    f.note('Passed screens of Eq. C4-E32.')


def e33(f):
    vcm = I_NET / M_F
    kcm = I_NET ** 2 / (2 * M_F) * 1e9
    f.text(.5, 1.0, 12.3, 'Do the energy and momentum budgets describe the same motion?', 13.5, ACC, bold=True)
    v = np.linspace(0, 1.2, 100)
    p = Plot(f, 1.0, 2.0, 6.4, 3.3, (0, 1.2), (0, 12), 'film speed v  (m/s)', 'energy  (nJ)', (0, .3, .6, .9, 1.2), (0, 5, 10), fx='{:.1f}', fy='{:g}')
    p.curve(v, (5 + .5 * M_F * v ** 2 * 1e9), ACC, 3)
    p.hline(E_SOL * 1e9, WARM)
    p.vline(vcm, PINK)
    p.pt(vcm, 5 + kcm, ACC)
    p.label(vcm, 5 + kcm, f'{5 + kcm:.3f} nJ at v_CM', ACC, 11.5, w=2.4, dx=-2.5, dy=-.6)
    p.label(.05, 11.6, 'E_solid = 10 nJ', WARM, 11.5, w=1.8, dy=0)
    p.label(vcm, 1.5, f'v_CM = I_net/m_f = {vcm:.4f} m/s', PINK, 11.5, w=3.0, dx=.1)
    f.panel(7.7, 1.6, 5.25, 3.9, 'Implied speed and energy', ACC, size=13.5)
    f.text(7.85, 2.1, 5.0, f'v_CM = I_net / m_f = {vcm:.9f} m/s', 12, FG, bold=True)
    f.text(7.85, 2.65, 5.0, f'K_CM = I_net² / (2 m_f) = {kcm:.9f} nJ', 12, FG, bold=True)
    f.text(7.85, 3.2, 5.0, f'Γ A_f + K_CM = {5 + kcm:.9f} nJ  <  E_solid', 12, WARM, bold=True)
    f.text(7.85, 3.95, 5.0, 'Check: the impulse budget and low-Γ energy budget agree at the implied speed.', 12, MUT)
    f.text(1.0, 6.0, 12, 'Compatibility is a screen: it shows the two budgets do not contradict each other, not that the film actually leaves.', 12.5, FG)
    f.note('Energy–momentum compatibility of Eq. C4-E33.')


def e34(f):
    H = 100e-6
    th = np.linspace(0, 5, 100)
    p = Plot(f, 8.0, 1.5, 4.8, 3.8, (0, 5), (0, 9), 'launch error θ  (degrees)', 'Δx  (µm)', (0, 1, 2, 3, 4, 5), (0, 2, 4, 6, 8), fx='{:g}', fy='{:g}')
    p.curve(th, H * np.tan(np.radians(th)) * 1e6, ACC, 3)
    p.pt(1, H * math.tan(math.radians(1)) * 1e6, WARM)
    p.label(1, H * math.tan(math.radians(1)) * 1e6, 'θ = 1°: Δx = 1.7455 µm', WARM, 12, w=2.8, dx=.15, dy=.2)
    f.panel(.4, 1.0, 6.5, 5.3, 'Ballistic placement', ACC, size=13.5)
    f.rect(.8, 1.7, 5.7, .3, fill=STEEL, line=MUT, lw=1.4)
    f.text(.8, 1.4, 2.4, 'exit plane (jet source)', 11.5, MUT)
    f.rect(.8, 4.4, 5.7, .3, fill=STEEL, line=MUT, lw=1.4)
    f.text(.8, 4.75, 2.4, 'film plane', 11.5, MUT)
    f.line(2.6, 2.0, 2.6, 4.4, MUT, 1.3, dash=True)
    f.line(2.6, 2.0, 3.35, 4.35, WARM, 3.5, arrow=True)
    f.dim(.7, 2.0, .7, 4.4, 'H_f', MUT, 12, side=1)
    f.dim(2.6, 4.95, 3.4, 4.95, 'Δx', PINK, 12.5, side=-1)
    f.text(3.6, 2.8, 2.8, 'θ', 14, WARM, bold=True)
    f.text(.6, 5.45, 6.1, 'Δx = H_f tan θ,   H_f = 100 µm,   θ = 1° ⇒ Δx = 1.74551 µm', 12.5, FG, bold=True)
    f.text(7.2, 6.15, 5.6, 'A receiving gap converts a small angular error into a placement error; compare Δx with the feature size.', 12, WARM)
    f.note('Ballistic placement of Eq. C4-E34 (the sketch angle is exaggerated).')


def e35(f):
    f.text(.5, 1.0, 12.3, 'Defence 1: load, impulse and work are three different quantities', 13.5, ACC, bold=True)
    cards = [('traction', 't_l = T_l n_f', 'Pa (local)', 'what the film feels at a point', BLUE), ('impulse', 'I_l = ∫∫ t_l dA dt', 'N s', 'area and time integrated', WARM), ('work', 'W_l = ∫∫ t_l·v_f dA dt', 'J', 'needs surface motion v_f', PINK)]
    for i, (h, e, u, n, c) in enumerate(cards):
        x = .5 + i * 4.15
        f.panel(x, 1.5, 3.95, 3.3, h, c, size=14)
        f.text(x + .1, 2.1, 3.75, e, 13, FG, 'center', bold=True)
        f.text(x + .1, 2.95, 3.75, f'unit: {u}', 12.5, c, 'center', bold=True)
        f.text(x + .1, 3.6, 3.75, n, 12, MUT, 'center')
    f.text(.5, 5.1, 12.3, 'Pressure alone says nothing about momentum or energy: duration, footprint and motion decide.', 13, WARM)
    f.text(.5, 5.7, 12.3, 'A stiff, immobile wall receives force and impulse but zero work.', 12.5, FG)
    f.note('Reference formulas of the Defence 1 answer: Eqs. C4-E01 and C4-E02.')


def e36(f):
    f.text(.5, 1.0, 12.3, 'Defence 1: global screens', 13.5, ACC, bold=True)
    f.panel(.5, 1.5, 6.0, 2.3, 'Energy', WARM, size=13.5)
    f.text(.65, 2.1, 5.7, 'E_solid ≥ Γ A_f + ½ m_f v_f²', 14, FG, bold=True)
    f.text(.65, 2.8, 5.7, 'fracture cost + kinetic energy of departure', 12, MUT)
    f.panel(6.8, 1.5, 6.0, 2.3, 'Momentum', PINK, size=13.5)
    f.text(6.95, 2.1, 5.7, 'I_net ≥ m_f v_f', 14, FG, bold=True)
    f.text(6.95, 2.8, 5.7, 'net impulse must carry the film at v_f', 12, MUT)
    hbars(f, .5, 4.2, 12.3, [('E_solid 10.0 nJ vs Γ A_f 5.0 nJ (passes)', 10 / 10, ACC), ('E_solid 10.0 nJ vs Γ A_f 20.0 nJ (fails)', 10 / 20, PINK)], 1.0, label_w=6.4, fmt='{:.2f}', unit=' of need', size=12, bar_h=.4, gap=.25)
    f.text(.5, 5.7, 12.3, 'Both screens must pass for the same Γ, A_f, m_f and v_f; the 20 nJ case already fails the first.', 12.5, WARM)
    f.note('Reference formulas of the Defence 1 answer: Eqs. C4-E30 to E33 (bar = budget / need, capped at 1).')


def e37(f):
    r = np.linspace(0, 1, 100)
    p = Plot(f, 1.0, 1.5, 4.8, 3.8, (0, 1), (0, 1.1), 'r / b', 'w / w(0)', (0, .5, 1), (0, .5, 1), fx='{:g}', fy='{:g}')
    p.curve(r, (1 - r ** 2) ** 2, ACC, 3)
    q = Plot(f, 6.5, 1.5, 3.1, 3.8, (0, 2), (0, 4), 'p₀ / p₀,crit', 'G / Γ', (0, 1, 2), (0, 2, 4), fx='{:g}', fy='{:g}')
    q.curve(np.linspace(0, 2, 60), np.linspace(0, 2, 60) ** 2, WARM, 3)
    q.pt(1, 1, WARM)
    f.panel(9.9, 1.5, 3.05, 3.8, 'Formulas', ACC, size=13)
    f.text(10.0, 2.0, 2.85, 'w = p₀(b² − r²)² / (64 D_f)', 11, FG, bold=True)
    f.text(10.0, 2.7, 2.85, 'G = p₀²b⁴ / (128 D_f)', 11, FG, bold=True)
    f.text(10.0, 3.4, 2.85, 'p₀,crit = √(128 D_f Γ) / b²', 11, WARM, bold=True)
    f.text(1.0, 6.0, 12, 'Defence 2: the 156 kPa threshold belongs to this plate, this clamp, this interface energy and a maintained-pressure source.', 12.5, FG)
    f.text(1.0, 6.5, 12, 'Change the loading control (fixed volume) or the geometry and the threshold changes.', 12, MUT)
    f.note('Reference formulas of the Defence 2 answer: Eqs. C4-E16, E20, E21.')


def e38(f):
    d = np.linspace(0, 140, 400)
    t = _cohesive(d * 1e-9, D0, DC, TMAX) / 1e6
    p = Plot(f, 1.0, 1.5, 5.2, 3.8, (0, 140), (0, .13), 'δ (nm)', 't_n (MPa)', (0, 50, 100), (0, .05, .1), fx='{:g}', fy='{:.2f}')
    p.fill(d, np.zeros_like(d), t, ACC, .3)
    p.curve(d, t, ACC, 3)
    p.label(75, .09, 'Γ = ½ T_max δ_c', FG, 12, w=2.2, dy=0)
    f.panel(6.5, 1.5, 6.45, 3.8, 'Two conditions together', ACC, size=13.5)
    f.text(6.65, 2.0, 6.2, 'Γ = ∫₀^δ_c t_n dδ = ½ T_max δ_c', 13, FG, bold=True)
    f.text(6.65, 2.6, 6.2, 'G ≥ Γ(ψ, T_i, v_c)', 13, WARM, bold=True)
    f.bullets(6.65, 3.2, 6.2, ['Initiation: peak traction T_max must be reached.', 'Separation: the area Γ must be supplied over the full opening δ_c.', 'Both must refer to the interface that actually fails.'], 12)
    f.text(1.0, 6.0, 12, 'Defence 3: release succeeds only if both initiation and separation work are provided at the correct interface.', 12.5, FG)
    f.note('Reference formulas of the Defence 3 answer: Eqs. C4-E11, E25, E26.')


def e39(f):
    f.text(.5, 1.0, 12.3, 'Defence 3: passing global budgets starts, rather than completes, the argument', 13.5, ACC, bold=True)
    f.chain([('energy', 'E_solid ≥ Γ A_f + ½ m_f v_f²'), ('momentum', 'I_net ≥ m_f v_f'), ('placement', 'Δx = H_f tan θ')], 1.5, h=1.5, gap=.5, colors=[WARM, PINK, ACC], size=12.5)
    f.panel(.5, 3.4, 6.0, 2.6, 'Passed means', ACC, size=13)
    f.bullets(.65, 3.9, 5.7, ['The budgets are large enough: a necessary condition.', 'No contradiction between energy and momentum.', 'Placement error is smaller than the feature, if it is.'], 12)
    f.panel(6.8, 3.4, 6.0, 2.6, 'Still not shown', PINK, size=13)
    f.bullets(6.95, 3.9, 5.7, ['That the crack front actually advances (needs G ≥ Γ locally).', 'That the film stays intact on departure.', 'That the real coupling fractions are 0.20 and 0.50.'], 12)
    f.note('Reference formulas of the Defence 3 answer: Eqs. C4-E30 and C4-E34.')


FIGS = {25: e25, 26: e26, 27: e27, 28: e28, 29: e29, 30: e30, 31: e31, 32: e32, 33: e33, 34: e34, 35: e35, 36: e36, 37: e37, 38: e38, 39: e39}
