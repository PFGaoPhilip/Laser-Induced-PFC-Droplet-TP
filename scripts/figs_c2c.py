"""Chapter 2, equations 25-36."""
import math

import numpy as np
from scipy.optimize import brentq

from figlib import *
from figphys import psat_pfp

RU = 8.314462618
M_PFC = 0.2880343
RHO_D = 1630.0
A0 = 5e-6
M0 = 4 / 3 * math.pi * RHO_D * A0 ** 3


def e25(f):
    phases = [('rapid growth', .8, -.3, -1.5), ('slow growth', .1, -.1, -.6), ('collapse', 0.0, .2, 3.0)]
    p = Plot(f, 1.0, 1.5, 7.4, 4.0, (0, 3), (-2.2, 3.8), '', 'relative rate  (1/µs)', (), (-2, -1, 0, 1, 2, 3), fy='{:g}')
    p.seg(0, 0, 3, 0, MUT, 1.3)
    cols = [(ACC, 'ṁ/m (mass)'), (PINK, 'Ṫ/T (temperature)'), (WARM, '−3Ṙ/R (volume)'), ('#FFFFFF', 'ṗ/p (total)')]
    for i, (name, a, b, c) in enumerate(phases):
        vals = [a, b, c, a + b + c]
        for j, v in enumerate(vals):
            xa = i + .06 + j * .22
            bw = p.X(xa + .18) - p.X(xa)
            f.rect(p.X(xa), p.Y(max(v, 0)), bw, max(abs(p.Y(v) - p.Y(0)), .02), fill=cols[j][0], line=cols[j][0], lw=1, opacity=.85 if j < 3 else .35)
            f.text(p.X(xa) - .2, (p.Y(v) - .27) if v >= 0 else (p.Y(v) + .03), bw + .4, f'{v:+.1f}', 11, FG, 'center', wrap=False)
        f.text(p.X(i) + .1, p.Y(-2.0), 2.4, name, 12.5, MUT, 'center', bold=True)
    for j, (c, s) in enumerate(cols):
        f.rect(1.1 + j * 1.9, 5.95, .25, .2, fill=c, line=c, lw=1, opacity=.85 if j < 3 else .4)
        f.text(1.42 + j * 1.9, 5.9, 1.6, s, 11, FG, wrap=False)
    f.panel(8.7, 1.5, 4.25, 4.0, 'Three drivers of pressure', ACC, size=13.5)
    f.text(8.85, 2.0, 4.0, 'ṗ_v,s / p_v,s = ṁ_v,s/m_v,s + Ṫ_b/T_b − 3Ṙ/R', 12.5, FG, bold=True)
    f.bullets(8.85, 2.85, 4.0, ['Evaporation raises p; cooling lowers it; volume growth lowers it quickly.', 'A law written in R alone keeps only the third term.', 'A bubble can lose pressure while still evaporating if the volume term dominates.'], 12)
    f.text(1.0, 6.4, 12, 'Rates are illustrative, chosen only to show how the three terms can compete. Identity valid for a spherical bubble (V_b = 4πR³/3).', 12, MUT)
    f.note('Logarithmic derivative of the ideal-gas law, Eq. C2-E25.')


def e26(f):
    R = np.logspace(math.log10(5e-6), math.log10(80e-6), 200)
    V = 4 / 3 * math.pi * R ** 3
    p = Plot(f, 1.0, 1.5, 7.0, 4.0, (5, 80), (3e3, 5e5), 'bubble radius R  (µm)', 'p_v,PFC,eq  (Pa)', (5, 10, 20, 40, 80), (1e4, 1e5), fx='{:g}', fy='{:.0e}', xlog=True, ylog=True)
    for T, c in [(313.15, WARM), (323.15, ACC)]:
        ps = psat_pfp(T)
        pi_ = M0 * RU * T / (M_PFC * V)
        peq = np.minimum(ps, pi_)
        p.curve(R * 1e6, peq, c, 3)
        Rc = (M0 * RU * T / (M_PFC * ps) * 3 / (4 * math.pi)) ** (1 / 3)
        p.pt(Rc * 1e6, ps, c)
        f.rect(5.3, 1.75 + (0 if T > 320 else .38), .3, .2, fill=c, line=c, lw=1)
        f.text(5.72, 1.7 + (0 if T > 320 else .38), 2.4, f'{T - 273.15:.0f} °C: knee at {Rc * 1e6:.0f} µm', 11.5, c, wrap=False)
    p.label(5.3, 1.1e5, 'liquid still present:\np = p_sat(T)', FG, 11.5, w=2.2, dy=.0)
    p.label(7, 1.3e4, 'inventory exhausted:\np = mR_uT/(MV) falls as 1/R³', FG, 11.5, w=3.4)
    f.panel(8.3, 1.5, 4.65, 4.0, 'min[ saturation, inventory ]', ACC, size=13.5)
    f.text(8.45, 2.0, 4.4, 'p_v,eq = min[ p_sat(T_b),  m_PFC,0 R_u T_b / (M_PFC V_b) ]', 12.5, FG, bold=True)
    f.bullets(8.45, 2.85, 4.4, ['Until all liquid evaporates the pressure is pinned at p_sat.', 'After that the finite inventory cannot supply more vapor, so p falls as the bubble grows.', 'Assumes a closed, non-dissolving supply and fast mass exchange.'], 12)
    f.text(1.0, 6.27, 12, 'Equilibrium benchmark for the 0.8535 ng inventory of a 5 µm core at two prescribed temperatures.', 12.5, FG)
    f.note('Finite-inventory benchmark of Eq. C2-E26 with p_sat from Eq. C2-E12.')


def e27(f):
    a = np.logspace(-6.3, -4.6, 100)
    m = 4 / 3 * math.pi * RHO_D * a ** 3
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (5e-7, 3e-5), (1e-15, 1e-10), 'core radius a  (m)', 'PFC mass  (kg)', (1e-6, 1e-5), (1e-15, 1e-14, 1e-13, 1e-12, 1e-11, 1e-10), fx='{:.0e}', fy='{:.0e}', xlog=True, ylog=True)
    p.curve(a, m, ACC, 3)
    for r, c in [(1e-6, BLUE), (5e-6, WARM), (1e-5, PINK)]:
        v = 4 / 3 * math.pi * RHO_D * r ** 3
        p.pt(r, v, c)
        p.label(r, v, f'{r * 1e6:g} µm: {v * 1e12:.4g} ng', c, 12, w=2.2, dy=-.5 if r < 2e-6 else .12 if r < 8e-6 else -.5, dx=.12 if r < 8e-6 else -2.35)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Start every ledger from the real volume', ACC, size=13)
    f.text(7.85, 2.0, 5.0, 'm_PFC,0 = (4π/3)(1630)(5×10⁻⁶)³', 13.5, FG, bold=True)
    f.text(7.85, 2.55, 5.0, '= 8.5347×10⁻¹³ kg = 0.8535 ng', 15, WARM, bold=True)
    f.ellipse(9.0, 4.1, .9, fill=LIQ, line=ACC, lw=2)
    f.text(8.0, 3.95, 2.0, '5 µm', 12.5, FG, 'center', bold=True)
    f.text(10.2, 3.6, 2.6, 'about 0.85 nanogram,\na fixed, finite budget', 12.5, FG)
    f.text(1.0, 6.27, 12, 'Mass scales as a³: a 10 µm core carries eight times as much PFC as a 5 µm core. Every later vapor amount is bounded by this number.', 12.5, FG)
    f.note('Initial PFC mass of Eq. C2-E27 (ρ_d = 1630 kg/m³).')


def e28(f):
    mass = M0
    qs = 654 * (323 - 293) * mass * 1e9
    ql = 95000 * mass * 1e9
    f.panel(.4, 1.0, 6.0, 5.4, 'Enthalpy path (schematic)', ACC, size=13.5)
    f.line(1.0, 5.5, 1.0, 1.8, MUT, 1.5, arrow=True)
    f.line(1.0, 5.5, 6.0, 5.5, MUT, 1.5, arrow=True)
    f.text(1.1, 1.6, 2.0, 'enthalpy H', 11.5, MUT)
    f.text(5.0, 5.55, 1.5, 'T', 12, MUT)
    f.line(1.4, 5.0, 3.4, 4.3, BLUE, 4)
    f.line(3.4, 4.3, 3.4, 2.7, PINK, 4)
    f.text(1.5, 4.9, 2.4, 'sensible\n293 → 323 K', 11.5, BLUE, bold=True)
    f.text(3.55, 3.3, 2.6, 'latent step L_v', 11.5, PINK, bold=True)
    f.dot(1.4, 5.0, .07, MUT)
    f.dot(3.4, 2.7, .07, MUT)
    f.text(.55, 5.8, 5.7, 'Constant-property estimate: heat the liquid to T*, then add one latent step.', 11.5, FG)
    f.text(6.8, 1.05, 6.1, 'Energy to prepare the PFC (nJ)', 14, ACC, bold=True)
    hbars(f, 6.8, 1.7, 6.1, [('sensible  m c_p (T* − T₀)', qs, BLUE), ('latent  m L_v', ql, PINK), ('total  Q_prep', qs + ql, ACC)], 110, label_w=2.6, fmt='{:.2f}', unit=' nJ', size=12, bar_h=.5, gap=.3)
    f.text(6.8, 4.1, 6.1, f'{qs:.3f} + {ql:.3f} = {qs + ql:.3f} nJ', 14, WARM, bold=True)
    f.text(6.8, 4.65, 6.1, 'Latent heat is 83 % of this estimate, so evaporating the droplet costs far more than warming it.', 12.5, FG)
    f.text(1.0, 6.5, 12, 'Inputs: m = 0.8535 ng, c_p = 654 J/(kg K), L_v = 95 kJ/kg, T₀ = 293 K, T* = 323 K (declared, constant-property).', 11.5, MUT)
    f.note('Preparation-path estimate of Eq. C2-E28.')


def e29(f):
    Tsat = brentq(lambda t: psat_pfp(t) - 1e5, 283, 338)
    cpl, Lv, cpv = 654.0, 95000.0, 900.0
    T0, Ts = 293.15, 323.15
    q1, q3 = cpl * (Tsat - T0), cpv * (Ts - Tsat)
    f.text(.5, 1.0, 7.5, 'Specific enthalpy gained along the constant-pressure path (kJ/kg)', 13.5, ACC, bold=True)
    Tl = np.linspace(T0, Tsat, 20)
    Tv = np.linspace(Tsat, Ts, 20)
    p = Plot(f, 1.0, 1.85, 6.7, 3.6, (290, 326), (0, 125), 'temperature T  (K)', 'H − H₀  (kJ/kg)', (290, 300, 310, 320), (0, 25, 50, 75, 100, 125), fx='{:g}')
    h1 = cpl * (Tl - T0) / 1e3
    h2 = (Lv + cpl * (Tsat - T0)) / 1e3
    h3 = (cpl * (Tsat - T0) + Lv + cpv * (Tv - Tsat)) / 1e3
    p.curve(Tl, h1, BLUE, 3.4)
    p.seg(Tsat, h1[-1], Tsat, h2 + 0 * 1, PINK, 3.4)
    p.curve(Tv, h3, ACC, 3.4)
    p.label(293, 12, f'liquid: c_p,l = 654 J/(kg K)\nto T_sat = {Tsat:.1f} K', BLUE, 11.5, w=2.8, dy=-.1)
    p.label(Tsat, 55, 'latent step\nL_v = 95 kJ/kg', PINK, 11.5, w=1.8, dx=.12)
    p.label(311, 118, 'vapor: c_p,v (assumed 0.9 kJ/(kg K))', ACC, 11.5, w=3.6)
    f.panel(8.0, 1.5, 4.95, 4.0, 'Each phase uses its own c_p', ACC, size=13.5)
    f.text(8.15, 2.0, 4.7, 'Q_iso = m [ ∫c_p,l dT + L_v(T_sat, p) + ∫c_p,v dT ]', 12.5, FG, bold=True)
    f.bullets(8.15, 2.85, 4.7, [f'Liquid heating stops at T_sat = {Tsat:.1f} K (1 bar), not at T*.', 'Vapor heating from T_sat to T* uses c_p,v, a different number.', 'The earlier estimate heated the liquid all the way to T*.'], 12)
    f.text(1.0, 6.0, 12, f'Per kilogram: {q1 / 1e3:.1f} kJ liquid + 95 kJ latent + {q3 / 1e3:.1f} kJ vapor (c_p,v is an assumed illustration).', 12, MUT)
    f.text(1.0, 6.45, 12, 'Latent enthalpy still dominates, but the sensible parts must follow the phase actually being heated.', 12.5, FG)
    f.note('Refined constant-pressure path of Eq. C2-E29; T_sat from Eq. C2-E12 at 1 bar.')


def e30(f):
    T = 323.15
    pp = np.logspace(4, 6.3, 100)
    ratio = (RHO_D * RU * T / (M_PFC * pp)) ** (1 / 3)
    p = Plot(f, 1.0, 1.5, 6.0, 4.0, (1e4, 2e6), (1, 15), 'PFC partial pressure p_v,PFC  (Pa)', 'R_b,inv / a₀', (1e4, 1e5, 1e6), (1, 2, 5, 10), fx='{:.0e}', fy='{:g}', xlog=True, ylog=True)
    p.curve(pp, ratio, ACC, 3)
    r1 = (RHO_D * RU * T / (M_PFC * 1e5)) ** (1 / 3)
    p.pt(1e5, r1, WARM)
    p.label(1e5, r1, f'1 bar: {r1:.3f} a₀ = {r1 * 5:.2f} µm', WARM, 12, w=2.8, dx=.12, dy=-.5)
    p.label(2e4, 8.5, 'R ∝ p^(−1/3)', ACC, 12.5, w=1.8)
    f.panel(7.4, 1.5, 5.55, 4.0, 'To scale at 1 bar and 323 K', ACC, size=13.5)
    f.ellipse(10.7, 4.25, 1.2, fill=GASC, line=WARM, lw=2.4)
    f.ellipse(10.7, 4.25, 1.2 / r1, fill=LIQ, line=ACC, lw=2.2)
    f.text(7.55, 2.0, 5.3, '(R_b,inv / a₀)³ = ρ_d R_u T* / (M_PFC p_v,PFC) = 151.98', 12, FG, bold=True)
    f.text(7.55, 2.7, 2.9, f'bubble R = {r1 * 5:.2f} µm\n(radius ratio {r1:.2f})', 12, WARM, bold=True)
    f.text(7.55, 3.9, 2.8, 'droplet a₀ = 5 µm', 12, ACC, bold=True)
    f.text(1.0, 6.27, 12, 'If every PFC molecule becomes ideal vapor at 1 bar, the bubble is 5.3 times the droplet radius, 152 times its volume.', 12.5, FG)
    f.note('Inventory radius of Eq. C2-E30 (M_PFC = 0.2880343 kg/mol, ρ_d = 1630 kg/m³).')


def e31(f):
    fg = 1 - math.exp(-2 * .25)
    A = .9 * (1 - math.exp(-1))
    Eabs = fg * A * 1000
    Q = 97.8243
    f.text(.5, 1.0, 12, 'From 1 µJ of laser light to the 97.8 nJ the PFC must receive (nJ)', 14, ACC, bold=True)
    hbars(f, .5, 1.6, 12.2, [('incident E_L', 1000, ACC), ('absorbed E_abs = f_geo A_λ E_L', Eabs, WARM), ('needed Q_prep (constant-property)', Q, PINK)], 1000, label_w=4.6, fmt='{:.1f}', unit=' nJ', size=13, bar_h=.55, gap=.3)
    f.panel(.5, 4.2, 6.0, 2.1, None, MUT)
    f.text(.65, 4.28, 5.7, f'f_geo = 1 − e^(−2(10/20)²) = {fg:.6f}', 12.5, FG)
    f.text(.65, 4.68, 5.7, f'A_λ = 0.90 × (1 − e^(−1)) = {A:.6f}', 12.5, FG)
    f.text(.65, 5.08, 5.7, f'E_abs = {fg:.6f} × {A:.6f} × 1 µJ = {Eabs:.3f} nJ', 12.5, WARM, bold=True)
    f.text(.65, 5.6, 5.7, 'No loss between absorption and PFC is included in this screen.', 11.5, MUT)
    f.panel(6.8, 4.2, 6.0, 2.1, 'Minimum heat-delivery fraction', ACC, size=13)
    f.text(6.95, 4.62, 5.7, f'η_th,min = Q_prep / E_abs = {Q:.4f} / {Eabs:.3f} = {Q / Eabs:.6f}', 12.5, FG, bold=True)
    f.text(6.95, 5.2, 5.7, 'At least 43.7 % of the declared absorbed energy must reach the PFC as heat, even with no losses.', 13, WARM, bold=True)
    f.note('Energy screen of Eq. C2-E31; all inputs are declared teaching values.')


def e32(f):
    cards = [('1  Optical energy', 'E_L = π w² F₀ / 2', 'Gaussian beam energy', ACC), ('2  Absorbed share', 'E_abs = f_geo A_λ E_L', 'aperture × absorptance', WARM),
             ('3  Where the heat goes', 't_th ~ L_h² / α', 'time to cross a distance', BLUE), ('4  Penetration', 'δ_T ~ √(α τ_h)', 'distance reached in the pulse', PINK)]
    for i, (h, e, n, c) in enumerate(cards):
        x = .5 + (i % 2) * 6.25
        y = 1.2 + (i // 2) * 2.15
        f.panel(x, y, 6.05, 1.95, None, c)
        f.ellipse(x + .45, y + .5, .27, fill=c, line=c, lw=1)
        f.text(x + .33, y + .3, .25, str(i + 1), 14, BG, 'center', bold=True)
        f.text(x + .9, y + .12, 5.0, h[3:], 13.5, c, bold=True)
        f.text(x + .9, y + .65, 5.0, e, 17, FG, bold=True)
        f.text(x + .9, y + 1.3, 5.0, n, 12, MUT)
    f.text(.5, 5.65, 12.3, 'Light must be intercepted, absorbed, and then conducted to the PFC. Each step has its own formula and its own limit.', 13.5, WARM)
    f.text(.5, 6.2, 12.3, 'A short pulse does not imply uniform temperature: compare the heat penetration δ_T with the distance to the PFC.', 12.5, FG)
    f.note('Reference formulas of the Defence 1 answer: Eqs. C2-E02, E06, E09.')


def e33(f):
    f.chain([('Confinement', 'p_d ≃ p_c + 2σ_pc/a + Π_shell'), ('Superheat', 'Δp_n = p_sat(T_i) − p_d'), ('Critical radius', 'r* = 2σ_vp / Δp_n'), ('Barrier', 'W* = 16π σ_vp³ / (3 Δp_n²)')],
            1.2, h=1.5, gap=.5, colors=[ACC, WARM, BLUE, PINK], size=13)
    x = np.linspace(0, 1.6, 200)
    p = Plot(f, 1.0, 3.3, 5.8, 2.6, (0, 1.6), (-.5, 1.3), 'r_n / r*', 'W / W*', (0, .5, 1, 1.5), (0, 1), fx='{:.1f}', fy='{:g}')
    p.curve(x, 3 * x ** 2 - 2 * x ** 3, ACC, 3)
    p.pt(1, 1, WARM)
    p.label(1, 1, 'r*, W*', WARM, 12.5, w=1.2, dx=.1, dy=-.4)
    f.panel(7.2, 3.3, 5.7, 2.9, 'Read it from left to right', ACC, size=13)
    f.bullets(7.35, 3.8, 5.4, ['Confinement sets the liquid pressure p_d; a smaller core raises it.', 'Superheat is how far p_sat at the interface temperature lies above p_d.', 'More superheat shrinks r* and W*, but the barrier stays positive.'], 12)
    f.text(1.0, 6.6, 12, 'The formulas assume homogeneous nucleation, a locally isothermal small nucleus and Δp_n > 0.', 12.5, FG)
    f.note('Reference formulas of the Defence 2 answer: Eqs. C2-E11, E14, E15, E16.')


def e34(f):
    f.text(.5, 1.0, 12.3, 'P_act = 1 − exp[ − ∫₀ᵗ ∫ J(T, p) dV dt′ ]    (V = V_d(t′))', 20, FG, 'center', bold=True)
    boxes = [('J(T, p)', 'nucleation rate\nm⁻³ s⁻¹', 'must be supplied by the material', PINK), ('V_d(t′)', 'liquid volume that\ncan nucleate\nm³', 'shrinks as PFC leaves the liquid', ACC), ('t′ from 0 to t', 'time spent in the\nactivating state\ns', 'set by the heating history', WARM)]
    for i, (h, d, n, c) in enumerate(boxes):
        x = .6 + i * 4.15
        f.panel(x, 2.0, 3.9, 2.7, None, c)
        f.text(x + .1, 2.1, 3.7, h, 17, c, 'center', bold=True)
        f.text(x + .1, 2.85, 3.7, d, 13, FG, 'center')
        f.text(x + .1, 4.0, 3.7, n, 11.5, MUT, 'center')
        if i < 2:
            f.text(x + 3.88, 3.0, .3, '×', 20, MUT, 'center', bold=True)
    f.text(.6, 5.05, 12.2, 'The exponent is the expected number of events. Independent events and a finite integrated rate give a probability between 0 and 1.', 13, FG)
    f.text(.6, 5.7, 12.2, 'The formula organises the problem but does not replace the missing, material-specific J(T, p).', 13.5, WARM, bold=True)
    f.note('Activation probability of Eq. C2-E34 (Poisson model).')


def e35(f):
    cards = [('Initial mass', 'm_PFC,0 = (4π/3) ρ_d a₀³', 'fixed by the real core volume', ACC), ('Ledger', 'm_l + m_v + m_diss + m_esc = m_PFC,0', 'no external compound supply', WARM), ('Vapor pressure', 'p_v,PFC V_b = (m_v / M_PFC) R_u T_b', 'ideal PFC partial pressure', BLUE)]
    for i, (h, e, n, c) in enumerate(cards):
        x = .5 + i * 4.2
        f.panel(x, 1.2, 4.0, 3.1, None, c)
        f.text(x + .1, 1.3, 3.8, h, 14.5, c, 'center', bold=True)
        f.text(x + .1, 2.1, 3.8, e, 14, FG, 'center', bold=True)
        f.text(x + .1, 3.6, 3.8, n, 12, MUT, 'center')
    f.panel(.5, 4.55, 12.2, 1.7, 'How the three connect', ACC, size=13.5)
    f.text(.65, 5.0, 11.9, 'The mass ledger caps m_v; the gas law turns m_v into a pressure; the pressure feeds the radius equation of Chapter 1.', 13, FG)
    f.text(.65, 5.6, 11.9, 'If m_v never exceeds m_PFC,0, then the vapor pressure at fixed V_b and T_b cannot exceed m_PFC,0 R_u T_b / (M_PFC V_b).', 12.5, WARM)
    f.note('Reference formulas of the Defence 3 answer: Eqs. C2-E18, E24, E27.')


def e36(f):
    f.panel(.5, 1.1, 4.0, 4.9, 'Interface energy jump', ACC, size=13.5)
    f.rect(.8, 2.0, 1.6, 2.4, fill=LIQ, line=LIQ2, lw=1)
    f.rect(2.4, 2.0, 1.8, 2.4, fill=GASC, line=MUT, lw=1)
    f.line(2.4, 1.9, 2.4, 4.5, WARM, 3)
    f.line(1.0, 3.2, 2.35, 3.2, PINK, 3, arrow=True)
    f.line(2.5, 3.2, 3.5, 3.2, ACC, 2, arrow=True)
    f.text(.7, 1.55, 1.5, 'liquid', 11.5, ACC, bold=True)
    f.text(2.6, 1.55, 1.5, 'vapor', 11.5, MUT, bold=True)
    f.text(.65, 4.6, 3.7, 'j_s L_v,s = (q_l − q_v)·n', 13, FG, bold=True)
    f.text(.65, 5.2, 3.7, 'unbalanced heat becomes latent heat', 11.5, MUT)
    f.panel(4.7, 1.1, 4.0, 4.9, 'Bubble ledger', WARM, size=13.5)
    f.ellipse(6.7, 3.2, .85, fill=GASC, line=WARM, lw=2.4)
    f.text(6.0, 3.05, 1.4, 'U_b', 15, FG, 'center', bold=True)
    f.line(4.95, 3.2, 5.8, 3.2, PINK, 3, arrow=True)
    f.line(7.6, 2.6, 8.3, 2.1, WARM, 3, arrow=True)
    f.line(6.7, 1.8, 6.7, 2.3, ACC, 3, arrow=True)
    f.text(4.85, 4.6, 3.7, 'U̇_b = Q̇_b − p_b V̇_b + Σ h_v,s ṁ_v,s', 12.5, FG, bold=True)
    f.text(4.85, 5.3, 3.7, 'heat, work and carried enthalpy', 11.5, MUT)
    f.panel(8.9, 1.1, 4.0, 4.9, 'Velocity slip', PINK, size=13.5)
    f.line(9.2, 4.0, 9.2, 1.9, MUT, 1.2)
    f.line(9.3, 2.7, 11.6, 2.7, WARM, 3.5, arrow=True)
    f.line(9.3, 3.4, 11.1, 3.4, ACC, 3.5, arrow=True)
    f.text(9.35, 2.2, 3.3, 'wall: Ṙ', 11.5, WARM, bold=True)
    f.text(9.35, 3.45, 3.3, 'liquid: u_l(R)', 11.5, ACC, bold=True)
    f.text(9.05, 4.6, 3.7, 'u_l(R) = Ṙ − j_s / ρ_l', 13, FG, bold=True)
    f.text(9.05, 5.2, 3.7, 'evaporation separates them', 11.5, MUT)
    f.text(.5, 6.2, 12.3, 'Conserved energy and mass at the interface prevent unlimited vapor and double-counted latent heat.', 13, WARM)
    f.note('Reference formulas of Defence 4: Eqs. C2-E20, E21, E22.')


FIGS = {25: e25, 26: e26, 27: e27, 28: e28, 29: e29, 30: e30, 31: e31, 32: e32, 33: e33, 34: e34, 35: e35, 36: e36}
