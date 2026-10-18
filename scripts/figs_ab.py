"""Appendix A (Chapter 90), equations 13-24."""
import math

import numpy as np

from figlib import *

G, RREF, R = 20000.0, 5e-6, 30e-6
RHO_G, ETA, L_G = 1000.0, 0.010, 30e-6


def p_el(Rr):
    q = RREF / Rr
    return G / 2 * (5 - 4 * q - q ** 4)


def W_g(Rr):
    return 2 * math.pi * G * (5 * Rr ** 3 / 3 - 2 * RREF * Rr ** 2 + RREF ** 4 / Rr - 2 * RREF ** 3 / 3)


def e13(f):
    pel = p_el(R)
    W = W_g(R)
    f.text(.5, 1.0, 12.3, 'Teaching inputs: G_g = 20 kPa, R_ref = 5 µm, R = 30 µm (sixfold expansion)', 13.5, ACC, bold=True)
    f.panel(.5, 1.5, 6.0, 2.6, 'Elastic resistance', BLUE, size=13.5)
    f.text(.65, 2.0, 5.7, 'p_el = (G_g/2)[5 − 4(5/30) − (5/30)⁴]', 12.5, FG, bold=True)
    f.text(.65, 2.55, 5.7, f'p_el = {pel:.4f} Pa', 16, BLUE, bold=True)
    f.text(.65, 3.2, 5.7, 'about 43 kPa: well below 100 kPa', 12, MUT)
    f.panel(6.8, 1.5, 6.0, 2.6, 'Stored work', WARM, size=13.5)
    f.text(6.95, 2.0, 5.7, 'W_g = 2πG_g[5R³/3 − 2R_refR² + R_ref⁴/R − 2R_ref³/3]', 11.5, FG, bold=True)
    f.text(6.95, 2.55, 5.7, f'W_g = {W:.8e} J = {W * 1e9:.4f} nJ', 15, WARM, bold=True)
    f.text(6.95, 3.2, 5.7, 'several nanojoules for a soft network', 12, MUT)
    f.chain([('R/R_ref', '30 / 5 = 6'), ('p_el', f'{pel / 1e3:.2f} kPa'), ('W_g', f'{W * 1e9:.3f} nJ')], 4.5, h=1.1, gap=.6, colors=[MUT, BLUE, WARM], size=12.5)
    f.text(.5, 6.0, 12.3, 'The pressure alone looks harmless; the work, accumulated over the whole expansion, is a finite share of the budget (next figure).', 12.5, FG)
    f.note('Teaching-input substitution of Eq. A-E13 (values recomputed from the closed forms).')


def e14(f):
    dV = 4 * math.pi / 3 * (R ** 3 - RREF ** 3)
    W100 = 100e3 * dV
    W = W_g(R)
    f.text(.5, 1.0, 12.3, 'Work needed to open the cavity against a 100 kPa overpressure', 13.5, ACC, bold=True)
    hbars(f, .5, 1.6, 12.3, [('available  W₁₀₀ = Δp_w ΔV', W100 * 1e9, ACC), ('elastic cost  W_g', W * 1e9, PINK), ('left over  W₁₀₀ − W_g', (W100 - W) * 1e9, GREEN)], 12.5, label_w=4.6, fmt='{:.3f}', unit=' nJ', size=13, bar_h=.55, gap=.3)
    f.panel(.5, 4.3, 6.0, 1.9, 'Volume and budget', ACC, size=13)
    f.text(.65, 4.8, 5.7, f'ΔV = (4π/3)(R³ − R_ref³) = {dV:.8e} m³', 12, FG, bold=True)
    f.text(.65, 5.4, 5.7, f'W₁₀₀ = (100 kPa)(ΔV) = {W100 * 1e9:.4f} nJ', 12, WARM, bold=True)
    f.panel(6.8, 4.3, 6.0, 1.9, 'Fraction', PINK, size=13)
    f.text(6.95, 4.8, 5.7, f'W_g / W₁₀₀ = {W / W100:.6f}', 15, PINK, bold=True)
    f.text(6.95, 5.45, 5.7, 'about 40 % of the work budget is taken by elasticity', 12, MUT)
    f.note('Finite work-budget comparison of Eq. A-E14 (Δp_w = 100 kPa).')


def e15(f):
    Rd = np.linspace(-20, 20, 200)
    vis = -4 * ETA * Rd / R
    Pd = 16 * math.pi * ETA * R * Rd ** 2
    p = Plot(f, 1.0, 1.5, 3.4, 3.8, (-20, 20), (-30, 30), 'wall speed Ṙ  (m/s)', 'RHS viscous term (kPa)', (-20, 0, 20), (-30, -15, 0, 15, 30), fx='{:g}', fy='{:g}')
    p.curve(Rd, vis / 1e3, BLUE, 3)
    p.pt(-10, -4 * ETA * (-10) / R / 1e3, WARM)
    p.label(-10, 13.3, '+13.33 kPa at Ṙ = −10 m/s', WARM, 11, w=2.4, dx=.15, dy=-.1)
    q = Plot(f, 5.8, 1.5, 3.4, 3.8, (-20, 20), (0, 6), 'wall speed Ṙ  (m/s)', 'P_dis  (mW)', (-20, 0, 20), (0, 2, 4, 6), fx='{:g}', fy='{:g}')
    q.curve(Rd, Pd * 1e3, PINK, 3)
    q.pt(-10, 16 * math.pi * ETA * R * 100 * 1e3, WARM)
    q.label(-10, 1.508, 'P_dis = 1.508 mW', WARM, 11, w=1.8, dx=.2, dy=-.5)
    f.panel(9.5, 1.5, 3.45, 3.8, 'Sign and loss', ACC, size=13)
    f.text(9.6, 2.0, 3.25, '−4η_gṘ/R = +13 333.3 Pa', 11.5, FG, bold=True)
    f.text(9.6, 2.55, 3.25, 'P_dis = 16πη_gRṘ² = 1.50796447×10⁻³ W', 11, FG, bold=True)
    f.text(9.6, 3.35, 3.25, 'Inward motion flips the pressure term; dissipated power stays positive.', 11.5, MUT)
    f.text(1.0, 6.0, 12, 'η_g = 0.010 Pa s, R = 30 µm, Ṙ = −10 m/s. The viscous term is linear in Ṙ, the dissipation is quadratic.', 12.5, FG)
    f.note('Signed-pressure and positive-loss check of Eq. A-E15.')


def e16(f):
    f.text(.5, 1.0, 12.3, 'Deborah number: relaxation time against event duration', 13.5, ACC, bold=True)
    f.text(.5, 1.5, 12.3, 'De = τ_rel / τ_e', 22, FG, 'center', bold=True)
    x = np.logspace(-3, 3, 100)
    p = Plot(f, 1.0, 2.3, 7.4, 2.6, (1e-3, 1e3), (0, 1.05), 'De  (log scale)', 'elastic share (conventional)', (1e-3, 1e-2, 1e-1, 1, 10, 100, 1e3), (0, .5, 1), fx='{:g}', fy='{:.1f}', xlog=True)
    p.fill(x[x < .1], np.zeros(int((x < .1).sum())), np.ones(int((x < .1).sum())), BLUE, .15)
    p.fill(x[x > 10], np.zeros(int((x > 10).sum())), np.ones(int((x > 10).sum())), WARM, .15)
    p.curve(x, x / (1 + x), ACC, 3)
    p.label(2e-3, .85, 'De ≪ 1: the network relaxes during the event', BLUE, 11, w=3.0, dy=0)
    p.label(15, .45, 'De ≫ 1:\nsolid-like', WARM, 11, w=1.6, dy=0)
    p.label(.15, .18, 'De ~ 1: both matter', ACC, 11, w=2.2, dy=0)
    f.panel(8.7, 2.3, 4.25, 2.6, 'What decides it', ACC, size=13)
    f.bullets(8.85, 2.8, 4.0, ['τ_rel: how long the network takes to relax.', 'τ_e: how long the jet or load lasts.', 'The ratio, not either time alone, sets the behaviour.'], 11.5)
    f.text(.5, 5.7, 12.3, 'The event duration determines which part of the network response can act before the jet or load arrives.', 12.5, FG)
    f.text(.5, 6.3, 12.3, 'The curve x/(1+x) is a conventional illustration of a Maxwell-type crossover, not a result derived from Eq. A-E16.', 12, MUT)
    f.note('Definition of Eq. A-E16; the share curve is illustrative only.')


def e17(f):
    tau = ETA / G
    t = np.linspace(0, 4, 300)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 4), (0, 1.05), 'time  t / τ_KV', 'γ(t) / γ₀', (0, 1, 2, 3, 4), (0, .25, .5, .75, 1), fx='{:g}', fy='{:.2f}')
    p.curve(t, np.exp(-t), ACC, 3.4)
    p.pt(1, math.exp(-1), WARM)
    p.vline(1, WARM)
    p.hline(math.exp(-1), MUT)
    p.label(1, math.exp(-1), '1/e at t = τ_KV', WARM, 12, w=2.0, dx=.15, dy=-.5)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Kelvin–Voigt dashpot in shear', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'T_sh = G_g γ + η_g γ̇', 13, FG, bold=True)
    f.text(7.85, 2.55, 5.0, 'T_sh = 0:  γ̇ = −(G_g/η_g) γ', 12.5, FG, bold=True)
    f.text(7.85, 3.1, 5.0, 'γ = γ₀ exp(−t/τ_KV),   τ_KV = η_g/G_g', 12.5, WARM, bold=True)
    f.text(7.85, 3.7, 5.0, f'τ_KV = 0.010 / 20 000 = {tau * 1e6:.2f} µs', 13, WARM, bold=True)
    f.text(7.85, 4.3, 5.0, 'This is the recovery time after unloading; it is not a relaxation time for stress under constant strain.', 11.5, MUT)
    f.text(1.0, 6.27, 12, 'A Kelvin–Voigt solid recovers strain exponentially; it cannot relax stress at constant strain, so τ_KV must not be reused as τ_rel.', 12.5, FG)
    f.note('Linear constitutive check of Eq. A-E17 (G_g = 20 kPa, η_g = 0.010 Pa s).')


def e18(f):
    cs = math.sqrt(G / RHO_G)
    ts = L_G / cs
    tc = 0.9146813565 * 30e-6 * math.sqrt(1000 / 100e3)
    f.text(.5, 1.0, 12.3, 'How long does the gel need to answer, compared with the collapse it is meant to follow?', 13.5, ACC, bold=True)
    hbars(f, .5, 1.6, 12.3, [('shear-wave crossing  t_s = L_g / c_s', ts * 1e6, WARM), ('ideal liquid collapse  t_c,liq', tc * 1e6, ACC)], 8, label_w=5.0, fmt='{:.4f}', unit=' µs', size=13, bar_h=.6, gap=.35)
    f.panel(.5, 3.9, 6.0, 2.3, 'Numbers', ACC, size=13)
    f.text(.65, 4.4, 5.7, f'c_s = √(G_g/ρ_g) = {cs:.8f} m/s', 12, FG, bold=True)
    f.text(.65, 4.95, 5.7, f't_s = 30 µm / c_s = {ts * 1e6:.8f} µs', 12, FG, bold=True)
    f.text(.65, 5.5, 5.7, f't_c,liq = 0.91468 R_max √(ρ_l/Δp_c) = {tc * 1e6:.8f} µs', 11.5, FG, bold=True)
    f.panel(6.8, 3.9, 6.0, 2.3, 'Ratio', WARM, size=13)
    f.text(6.95, 4.5, 5.7, f't_s / t_c,liq = {ts / tc:.8f}', 15, WARM, bold=True)
    f.text(6.95, 5.2, 5.7, 'The gel communicates slower than the ideal liquid collapses: it cannot be treated as quasi-static over the event.', 12, FG)
    f.note('Teaching response-time comparison of Eq. A-E18 (R_max = 30 µm, ρ_l = 1000 kg/m³, Δp_c = 100 kPa, L_g = 30 µm).')


def e19(f):
    Kb = np.logspace(5, 10, 200)
    cL = np.sqrt((Kb + 4 * G / 3) / RHO_G)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (1e5, 1e10), (1, 1e4), 'bulk modulus K_bulk  (Pa)', 'longitudinal speed c_L  (m/s)', (1e5, 1e6, 1e7, 1e8, 1e9, 1e10), (1, 10, 100, 1e3, 1e4), fx='{:.0e}', fy='{:g}', xlog=True, ylog=True)
    p.curve(Kb, cL, ACC, 3.4)
    p.hline(math.sqrt(G / RHO_G), PINK)
    p.label(3e5, 9, 'c_s = 4.47 m/s (shear)', PINK, 11.5, w=2.6, dy=0)
    Kw = 2.2e9
    cw = math.sqrt((Kw + 4 * G / 3) / RHO_G)
    p.pt(Kw, cw, WARM)
    p.label(Kw, cw, f'K = 2.2 GPa (assumed): c_L = {cw:.0f} m/s', WARM, 11.5, w=3.6, dx=-3.7, dy=.1)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Compressional crossing', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'c_L ≃ √[(K_bulk + 4G_g/3)/ρ_g]', 13, FG, bold=True)
    f.text(7.85, 2.55, 5.0, 't_L = L_g / c_L,    M_w = |Ṙ| / c_L', 12.5, WARM, bold=True)
    f.text(7.85, 3.2, 5.0, f't_L = {L_G / cw * 1e9:.1f} ns,   M_w = {10 / cw:.4f}  (|Ṙ| = 10 m/s)', 12, WARM, bold=True)
    f.text(7.85, 3.9, 5.0, 'K_bulk = 2.2 GPa is an assumed water-like value for illustration; the real gel must be characterised.', 11.5, MUT)
    f.text(1.0, 6.27, 12, 'Shear and longitudinal waves differ by about 330×: a water-rich gel answers compression almost instantly and shear slowly.', 12.5, FG)
    f.note('Separate compressibility diagnostic of Eq. A-E19 (L_g = 30 µm).')


def e20(f):
    L = np.logspace(-6, -3, 100)
    k, Md, mu = 1e-17, 60e3, 1e-3
    t = mu * L ** 2 / (k * Md)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (1e-6, 1e-3), (1e-9, 1e3), 'drainage length L_g  (m)', 't_poro  (s)', (1e-6, 1e-5, 1e-4, 1e-3), (1e-9, 1e-6, 1e-3, 1, 1e3), fx='{:.0e}', fy='{:.0e}', xlog=True, ylog=True)
    p.curve(L, t, ACC, 3.4)
    p.pt(30e-6, mu * (30e-6) ** 2 / (k * Md), WARM)
    p.label(30e-6, 1.5, 't_poro = 1.5 s at 30 µm', WARM, 12, w=2.8, dx=.15, dy=.4)
    p.hline(3e-6, PINK)
    p.label(1.5e-6, 3e-6, 'event time 3 µs', PINK, 11.5, w=2.2, dy=-.45)
    p.label(1.5e-5, 1e2, 'slope 2: t ∝ L_g²', MUT, 11.5, w=2.4, dy=0)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Darcy flow and diffusion', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'j_l = −(k/μ_l) ∇p_pore', 12.5, FG, bold=True)
    f.text(7.85, 2.5, 5.0, '∂p/∂t = D_poro ∇²p,   D_poro = k M_d / μ_l', 12, WARM, bold=True)
    f.text(7.85, 3.05, 5.0, 't_poro ~ L_g² / D_poro = μ_l L_g² / (k M_d)', 12, WARM, bold=True)
    f.text(7.85, 3.65, 5.0, 'k = 10⁻¹⁷ m², M_d = 60 kPa, μ_l = 1 mPa s (prescribed teaching values).', 11.5, MUT)
    f.text(7.85, 4.35, 5.0, 'A 3 µs event is approximately undrained at 30 µm; local solvent motion remains possible.', 11.5, FG)
    f.text(1.0, 6.27, 12, 'Permeability and modulus are inputs from characterisation; only the quadratic scaling with length is a result of the model.', 12.5, FG)
    f.note('Darcy/storage drainage time of Eq. A-E20.')


def e21(f):
    f.text(.5, 1.0, 12.3, 'Recalled radial control: expansion and resistance, not an outlet', 13.5, ACC, bold=True)
    f.text(.5, 1.5, 12.3, 'ρ_g(RR̈ + 3Ṙ²/2) = p_b − p_∞ − 2σ/R − p_el(R) − 4η_gṘ/R', 16, FG, 'center', bold=True)
    items = [('inertia', 'ρ_g(RR̈ + 3Ṙ²/2)', BLUE), ('driving', 'p_b − p_∞', ACC), ('capillary', '2σ/R', WARM), ('elastic', 'p_el(R)', PINK), ('viscous', '4η_gṘ/R', GREEN)]
    for i, (h, e, c) in enumerate(items):
        x = .5 + i * 2.5
        f.panel(x, 2.5, 2.35, 1.7, h, c, size=13)
        f.text(x + .08, 3.15, 2.2, e, 11.5, FG, 'center', bold=True)
    f.panel(.5, 4.5, 6.0, 1.75, 'What it describes', ACC, size=13)
    f.text(.65, 5.0, 5.7, 'Spherical expansion of a cavity and the resistance of the gel to it.', 12, FG)
    f.panel(6.8, 4.5, 6.0, 1.75, 'What it cannot do', PINK, size=13)
    f.text(6.95, 5.0, 5.7, 'It does not manufacture an outlet: no hole, no jet exit, no directional flow.', 12, FG)
    f.note('Original answer recalled: Eq. A-E11 (Defence 1).')


def e22(f):
    x = np.linspace(1, 10, 200)
    p = Plot(f, 1.0, 1.5, 3.6, 3.8, (1, 10), (0, 2.8), 'R / R_ref', 'p_el / G_g', (1, 5, 10), (0, 1, 2), fx='{:g}', fy='{:g}')
    p.curve(x, .5 * (5 - 4 / x - x ** -4.0), ACC, 3)
    Rs = np.linspace(1, 10, 200)
    W = 2 * math.pi * 1 * (5 * Rs ** 3 / 3 - 2 * Rs ** 2 + 1 / Rs - 2 / 3)
    q = Plot(f, 5.8, 1.5, 3.6, 3.8, (1, 10), (1, 3000), 'R / R_ref', 'W_g / (G_g R_ref³)', (1, 5, 10), (1, 10, 100, 1000), fx='{:g}', fy='{:g}', ylog=True)
    q.curve(Rs[1:], W[1:], WARM, 3)
    f.panel(9.6, 1.5, 3.35, 3.8, 'Formulas', ACC, size=13)
    f.text(9.7, 2.0, 3.15, 'p_el = (G_g/2)[5 − 4R_ref/R − (R_ref/R)⁴]', 10.5, FG, bold=True)
    f.text(9.7, 3.0, 3.15, 'W_g = 2πG_g[5R³/3 − 2R_refR² + R_ref⁴/R − 2R_ref³/3]', 10.5, WARM, bold=True)
    f.text(9.7, 4.3, 3.15, 'pressure saturates; work keeps growing as R³', 11, MUT)
    f.text(1.0, 6.0, 12, 'Defence 2: resistance pressure and elastic work answer different parts of the feasibility question: a modest pressure can still cost a finite work.', 12.5, FG)
    f.note('Original pressure and work formulas recalled: Eqs. A-E05 and A-E07 (Defence 2).')


def e23(f):
    f.text(.5, 1.0, 12.3, 'Three timescale comparisons, three assumptions', 13.5, ACC, bold=True)
    cs = math.sqrt(G / RHO_G)
    cards = [('Deborah number', 'De = τ_rel / τ_e', 'does the network relax during the event?', 'viscoelastic response', BLUE),
             ('Shear crossing', f't_s = L_g / √(G_g/ρ_g) = {L_G / cs * 1e6:.2f} µs', 'is the gel quasi-static over the event?', 'inertia / wave travel', WARM),
             ('Drainage', 't_poro ~ μ_l L_g² / (k M_d) = 1.5 s', 'can solvent leave during the event?', 'poroelastic transport', PINK)]
    for i, (h, e, q, n, c) in enumerate(cards):
        x = .5 + i * 4.15
        f.panel(x, 1.5, 3.95, 3.4, h, c, size=13.5)
        f.text(x + .1, 2.1, 3.75, e, 12, FG, 'center', bold=True)
        f.text(x + .1, 3.2, 3.75, q, 12, WARM, 'center')
        f.text(x + .1, 4.1, 3.75, n, 11.5, MUT, 'center')
    f.text(.5, 5.3, 12.3, 'Each ratio against the event time constrains a different physical assumption; one passing test does not cover the others.', 12.5, FG)
    f.note('Original event-response formulas recalled: Eqs. A-E16, A-E18, A-E20 (Defence 3).')


def e24(f):
    f.text(.5, 1.0, 12.3, 'Follow the delivered load to the intended interface and the final placement', 13.5, ACC, bold=True)
    f.chain([('load', 't_load on A_t'), ('impulse', 'J_target = ∫∫ t_load dA dt'), ('interface', 'W_sep,min = ∫ Γ_c dA'), ('placement', 'final position')], 1.6, h=1.5, gap=.55, colors=[BLUE, WARM, PINK, GREEN], size=12)
    f.panel(.5, 3.5, 6.0, 2.4, 'Delivered', ACC, size=13)
    f.text(.65, 4.0, 5.7, 'J_target = ∫_{t₀}^{t₁} ∫_{A_t} t_load dA dt', 12.5, FG, bold=True)
    f.text(.65, 4.7, 5.7, 'the load that actually reaches the target footprint A_t over its time window', 12, MUT)
    f.panel(6.8, 3.5, 6.0, 2.4, 'Required', WARM, size=13)
    f.text(6.95, 4.0, 5.7, 'W_sep,min = ∫_{A_rel} Γ_c dA', 12.5, FG, bold=True)
    f.text(6.95, 4.7, 5.7, 'the least energy to separate the intended release area', 12, MUT)
    f.text(.5, 6.2, 12.3, 'A fair comparison with the gel path must use the same load, interface and placement accounting.', 12.5, FG)
    f.note('Original load and interface-work accounting: Eq. A-E24 (Defence 3).')


FIGS = {13: e13, 14: e14, 15: e15, 16: e16, 17: e17, 18: e18, 19: e19, 20: e20, 21: e21, 22: e22, 23: e23, 24: e24}
