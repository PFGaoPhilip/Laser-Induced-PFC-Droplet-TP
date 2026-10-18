"""Chapter 3, equations 23-33."""
import math

import numpy as np

from figlib import *

RHO, C = 1000.0, 1480.0
U_J = math.sqrt(2 * 2.0e-9 / 3.926991e-12)
M_J = 3.926991e-12
A_J = math.pi * (5e-6) ** 2
L_J = 50e-6
P0 = RHO * C * U_J
T_EQ = L_J / C
T_SIDE = 5e-6 / C


def e23(f):
    f.panel(.4, 1.0, 6.6, 5.3, 'Steady redirection of a jet', ACC, size=13.5)
    f.rect(2.2, 1.55, 1.0, 2.0, fill=LIQ, line=ACC, lw=2.2)
    f.line(2.7, 1.5, 2.7, 3.45, ACC, 3.5, arrow=True)
    f.text(3.35, 2.2, 3.4, 'U_j, A_j', 13, ACC, bold=True)
    f.rect(1.0, 3.6, 5.2, .3, fill=STEEL, line=MUT, lw=1.4)
    for sgn in (-1, 1):
        f.line(2.7 + sgn * .6, 3.55, 2.7 + sgn * 2.4, 3.45, WARM, 3.5, arrow=True)
    f.text(1.0, 4.1, 5.8, 'all axial momentum is removed; liquid leaves sideways', 12, WARM, bold=True)
    f.text(.6, 4.6, 6.2, 'q_j = ½ρU_j²,   ṁ = ρA_jU_j', 13, FG, bold=True)
    f.text(.6, 5.05, 6.2, 'F_steady = ṁU_j = ρA_jU_j² = 2 q_j A_j', 14, WARM, bold=True)
    f.text(.6, 5.55, 6.2, f'A_j = π(5 µm)² → F = {2 * 0.5 * RHO * U_J ** 2 * A_J * 1e6:.0f} µN', 12, MUT)
    f.text(7.2, 1.05, 5.7, 'Two very different pressure scales (MPa, log axis)', 13.5, ACC, bold=True)
    hbars(f, 7.2, 1.7, 5.7, [('q_j = ½ρU_j²', .5092958, BLUE), ('ρ c U_j (early rigid contact)', 47.23477, PINK)], 100, label_w=2.8, fmt='{:.3g}', unit=' MPa', size=12, bar_h=.5, gap=.3, log=True, vmin=.1)
    f.text(7.2, 3.3, 5.7, 'Dynamic pressure is a scale; it is not a pressure applied over the whole surface.', 12.5, FG)
    f.text(7.2, 4.2, 5.7, 'Steady force follows from momentum flux with the same U_j, ρ, A_j used elsewhere. The first nanoseconds of impact (second bar) are about 90 times larger.', 12.5, WARM)
    f.note('Eq. C3-E23 with the declared jet: U_j = 31.915 m/s, d_j = 10 µm, ρ = 1000 kg/m³, c = 1480 m/s.')


def e24(f):
    x = np.logspace(-2, 2, 200)
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (.01, 100), (0, 1.05), 'receiver impedance ratio Z_r / Z_l', 'fraction of ρ c U_j  or  of U_j', (.01, .1, 1, 10, 100), (0, .25, .5, .75, 1), fx='{:g}', fy='{:.2f}', xlog=True)
    p.curve(x, x / (1 + x), ACC, 3)
    p.curve(x, 1 / (1 + x), WARM, 3, dash=True)
    p.vline(1, MUT)
    p.pt(1, .5, FG)
    p.label(1, .5, 'matched: both 1/2', FG, 11.5, w=1.8, dx=.12, dy=.15)
    p.label(.012, .08, 'free surface:\np_early → 0', MUT, 11.5, w=1.8, dy=-.35)
    p.label(20, .93, 'rigid receiver:\np_early → ρ c U_j', MUT, 11.5, w=2.0, dx=-2.1, dy=.1)
    f.panel(7.9, 1.5, 5.05, 4.0, 'Contact matching', ACC, size=13.5)
    f.text(8.05, 2.0, 4.8, '(∂ₜ ± c∂_z)(u ± p′/Z_l) = 0  (characteristics)', 12, FG, bold=True)
    f.text(8.05, 2.55, 4.8, 'p_early = Z_l(U_j − v_i) = Z_r v_i', 12.5, WARM, bold=True)
    f.text(8.05, 3.1, 4.8, 'v_i = Z_l U_j / (Z_l + Z_r)  (dashed)', 12.5, WARM, bold=True)
    f.text(8.05, 3.65, 4.8, 'p_early = Z_l Z_r U_j / (Z_l + Z_r)  (solid)', 12.5, ACC, bold=True)
    f.text(8.05, 4.35, 4.8, 'Equal pressure and equal normal velocity at the contact fix both numbers.', 12, MUT)
    f.text(1.0, 6.27, 12, 'Stiffer receivers raise the early pressure toward Z_l U_j but never above it; softer receivers lower it and let the jet keep moving.', 12.5, FG)
    f.note('Early contact state of Eq. C3-E24 (Z_l = ρ c).')


def e25(f):
    t = np.linspace(0, 45, 600)
    p = Plot(f, 1.0, 1.5, 7.0, 3.9, (0, 45), (0, 1.2), 'time from first contact  (ns)', 'p / (ρ c U_j)', (0, 10, 20, 30, 40), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    tau = T_EQ * 1e9
    ts = T_SIDE * 1e9
    p.fill(t, np.zeros_like(t), np.where(t <= tau, 1.0, 0), ACC, .22)
    p.curve(np.array([0, 0, tau, tau, 45]), np.array([0, 1, 1, 0, 0]), ACC, 3)
    p.vline(ts, PINK)
    p.vline(.3, WARM)
    p.label(ts, 1.15, f't_side = a_j/c = {ts:.2f} ns', PINK, 12, w=2.6, dx=.15, dy=-.1)
    p.label(tau, .6, f'τ_eq = L_j/c = {tau:.2f} ns\n(impulse-equivalent)', ACC, 12, w=3.2, dx=-3.3, dy=0)
    p.label(.3, .4, 'early\nobservation', WARM, 11.5, w=1.3, dx=.1)
    f.panel(8.3, 1.5, 4.65, 3.9, 'Finite momentum, finite duration', ACC, size=13)
    f.text(8.45, 2.0, 4.4, 'P_in = m_j U_j = ρA_jL_jU_j = 1.2533×10⁻¹⁰ N s', 12, FG, bold=True)
    f.text(8.45, 2.7, 4.4, '(ρcU_j) A_j τ_eq = m_j U_j ⇒ τ_eq = L_j / c', 12, WARM, bold=True)
    f.bullets(8.45, 3.4, 4.4, ['A side-release wave reaches the centre after t_side, 10 times sooner than τ_eq.', 'The 47 MPa scale only holds for t_early ≪ min(t_side, t_axial, t_return).'], 11.5)
    f.text(1.0, 6.0, 12, 'The very large early pressure belongs to a rectangle of equal impulse that the real jet cannot sustain: its duration is limited by finite length and free sides.', 12.5, FG)
    f.note('Early-impact duration conditions of Eq. C3-E25 (c = 1480 m/s, L_j = 50 µm, a_j = 5 µm).')


def e26(f):
    tau = T_EQ * 1e9
    t = np.linspace(0, 200, 2000)
    dt = t[1] - t[0]
    pulse = np.where(t <= tau, 1.0, 0.0)
    p = Plot(f, 1.0, 1.5, 7.0, 3.9, (0, 160), (0, 1.15), 'time t  (ns)', 'p_obs / (ρ c U_j)', (0, 40, 80, 120, 160), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    p.curve(t, pulse, MUT, 1.6, dash=True)
    for to, c in [(10, ACC), (tau, WARM), (100, PINK)]:
        n = int(to / dt)
        cs = np.concatenate([[0], np.cumsum(pulse)]) * dt
        avg = np.array([(cs[i + 1] - cs[max(0, i + 1 - n)]) / to for i in range(len(t))])
        p.curve(t, avg, c, 3)
        b = min(tau / to, 1.1)
        if b < 1.1:
            p.hline(b, c, dash=True, width=1.2)
    p.label(105, .9, 'dashed grey:\nthe underlying pulse', MUT, 11.5, w=2.2, dy=0)
    p.label(48, .8, 'τ_o = 10 ns', ACC, 11.5, w=1.6)
    p.label(78, .56, f'τ_o = {tau:.1f} ns: bound = 1', WARM, 11.5, w=2.8)
    p.label(60, .12, 'τ_o = 100 ns: bound = 0.34', PINK, 11.5, w=2.8)
    f.panel(8.3, 1.5, 4.65, 3.9, 'A maximum needs an observer', ACC, size=13)
    f.text(8.45, 2.0, 4.4, 'p_obs(t) = (1/A_oτ_o) ∫∫ (p − p_ref) dA dξ', 12, FG, bold=True)
    f.text(8.45, 2.6, 4.4, '0 ≤ p_obs ≤ J_rec / (A_o τ_o)', 13, WARM, bold=True)
    f.text(8.45, 3.2, 4.4, 'valid for nonnegative excess pressure, negligible normal viscous stress and the full-event footprint impulse J_rec', 11.5, MUT)
    f.text(8.45, 4.4, 4.4, 'Same pulse, three observers: the reported peak changes by a factor 3 with the window alone.', 12, FG)
    f.text(1.0, 6.0, 12, 'Dashed horizontal lines are the bound J_rec/(A_oτ_o) for each window (the 10 ns bound lies above the plot). Quote location, footprint and window with any value.', 12, FG)
    f.note('Observer and bound of Eq. C3-E26 for the declared rectangular pulse.')


def e27(f):
    x = np.logspace(0, 1.5, 200)
    p = Plot(f, 1.0, 1.5, 6.6, 3.9, (1, 31.6), (.1, 1.2), 'window ratio τ_o / τ_eq', '|p̄| / p₀', (1, 2, 5, 10, 30), (.1, .2, .5, 1), fx='{:g}', fy='{:g}', xlog=True, ylog=True)
    p.curve(x, 1 / x, ACC, 3)
    p.curve(x, 1 / np.sqrt(x), WARM, 3, dash=True)
    p.label(1.1, .14, '|p̄| = p₀ τ_eq/τ_o  (actual mean)', ACC, 12, w=3.2, dy=0)
    p.label(2.2, .8, 'bound √(Z_l E_w / A_oτ_o) = p₀ √(τ_eq/τ_o)', WARM, 12, w=3.8, dy=-.2)
    f.panel(7.9, 1.5, 5.05, 3.9, 'Finite window, finite energy', ACC, size=13.5)
    f.text(8.05, 2.0, 4.8, 'E_w = ∫∫ p′²/Z_l dA dt', 12.5, FG, bold=True)
    f.text(8.05, 2.5, 4.8, '|p̄|² ≤ (1/A_oτ_o) ∫∫ p′² dA dt = Z_l E_w/(A_oτ_o)', 12, WARM, bold=True)
    f.bullets(8.05, 3.2, 4.8, ['Mean ≤ root-mean-square (Cauchy–Schwarz).', 'The bound uses the one-way wave relation u′ = p′/Z_l.', 'A point spike with no measured area or time cannot stand for delivered loading.'], 12)
    f.text(1.0, 6.0, 12, 'For a window longer than the pulse the true mean falls as 1/x while the energy bound falls only as 1/√x: the bound is safe, not tight.', 12.5, FG)
    f.note('One-way-wave energy bound of Eq. C3-E27 evaluated for a rectangular pulse of amplitude p₀ and duration τ_eq.')


def e28(f):
    f.panel(.4, 1.0, 12.55, 3.2, 'Compressible conservation in a fixed volume', ACC, size=13.5)
    boxes = [('Mass', '∂ₜρ + ∇·(ρu) = 0', 'what enters equals the change of density', BLUE), ('Momentum', '∂ₜ(ρu) + ∇·(ρu⊗u + pI − τ) = 0', 'pressure and viscous traction cross the surface', ACC), ('Total energy', '∂ₜ(ρe_t) + ∇·[(ρe_t + p)u − τ·u + q] = Q_abs', 'pressure work, viscous work, heat, optical source', WARM)]
    for i, (h, e, d, c) in enumerate(boxes):
        x = .6 + i * 4.15
        f.panel(x, 1.6, 4.0, 2.4, None, c)
        f.text(x + .1, 1.68, 3.8, h, 14, c, 'center', bold=True)
        f.text(x + .1, 2.2, 3.8, e, 12.5, FG, 'center', bold=True)
        f.text(x + .1, 3.3, 3.8, d, 11.5, MUT, 'center')
    f.panel(.4, 4.45, 6.1, 1.85, 'Closure still required', PINK, size=13)
    f.text(.55, 4.9, 5.8, 'p = 𝒫(ρ, e, {Y_k}),   e_t = e + |u|²/2', 13, FG, bold=True)
    f.text(.55, 5.45, 5.8, 'An equation of state, species fractions and interface jump conditions complete the system.', 12, MUT)
    f.panel(6.7, 4.45, 6.25, 1.85, 'Why it matters at impact', ACC, size=13)
    f.text(6.85, 4.9, 5.95, 'Strong compression is not captured by the incompressible potential model. Optical heating Q_abs is counted once, and the solid response needs its own law.', 12, FG)
    f.note('Compressible bulk conservation of Eq. C3-E28; schematic.')


def e29(f):
    vals = [('incident laser energy E_L', 25000.0, ACC), ('absorbed E_abs,tot = 0.8 × 0.5 × E_L', 10000.0, BLUE), ('per site E_abs,site = E_abs,tot / 25', 400.0, WARM), ('to PFC by deadline f_T E_abs,site (f_T = 0.40)', 160.0, PINK), ('jet kinetic energy E_j = η_j E_abs,site', 2.0, GREEN)]
    f.text(.5, 1.0, 12.4, 'From 25 µJ of laser light to 2 nJ of jet kinetic energy (nJ, log axis)', 14, ACC, bold=True)
    hbars(f, .5, 1.6, 12.4, vals, 30000, label_w=5.6, fmt='{:g}', unit=' nJ', size=12.5, bar_h=.45, gap=.25, log=True, vmin=1)
    f.panel(.5, 4.9, 6.0, 1.45, None, MUT)
    f.text(.65, 5.0, 5.7, 'Efficiencies are stipulated: f_geo = 0.8, A_λ = 0.5, f_T = 0.40, η_j = 0.005.', 12.5, FG)
    f.text(.65, 5.55, 5.7, 'N_d = 25 sites share the energy equally.', 12.5, MUT)
    f.panel(6.7, 4.9, 6.2, 1.45, 'Total jet energy', WARM, size=13)
    f.text(6.85, 5.4, 5.9, 'E_j,tot = N_d E_j = 25 × 2.00 nJ = 50.0 nJ', 14, WARM, bold=True)
    f.note('Allocation chain of Eq. C3-E29: each stage uses only the energy left by the previous one (no double counting).')


def e30(f):
    f.text(.5, 1.0, 12.4, 'The declared jet drawn to scale (10 µm diameter, 50 µm long)', 14, ACC, bold=True)
    f.rect(.8, 1.8, 5.0, 1.0, fill=LIQ, line=ACC, lw=2.4)
    f.line(5.9, 2.3, 6.9, 2.3, WARM, 4, arrow=True)
    f.text(6.0, 1.85, 1.5, 'U_j', 13, WARM, bold=True)
    f.dim(.8, 3.15, 5.8, 3.15, 'L_j = 50 µm', MUT, 12, side=-1)
    f.line(.65, 1.8, .65, 2.8, MUT, 1.3)
    f.text(.8, 1.4, 3.0, 'd_j = 10 µm (cylinder height)', 11.5, MUT)
    cards = [('mass', 'm_j = ρ π d_j² L_j / 4', '3.927 ng', BLUE), ('speed', 'U_j = √(2E_j/m_j), E_j = 2 nJ', '31.915 m/s', ACC), ('dynamic pressure', 'q_j = ½ρU_j²', '0.5093 MPa', WARM), ('early rigid contact', 'ρ c U_j (c = 1480 m/s)', '47.23 MPa', PINK), ('momentum', 'P_j = m_j U_j;  25 jets: 25 P_j', '1.2533×10⁻¹⁰ N s; 3.1333×10⁻⁹ N s', GREEN)]
    for i, (h, e, v, c) in enumerate(cards):
        x = .5 + i * 2.5
        f.panel(x, 3.7, 2.35, 2.5, None, c)
        f.text(x + .08, 3.78, 2.2, h, 12.5, c, 'center', bold=True)
        f.text(x + .08, 4.3, 2.2, e, 11, FG, 'center')
        f.text(x + .08, 5.2, 2.2, v, 12.5, WARM, 'center', bold=True)
    f.text(7.6, 1.9, 5.3, 'The state carried into Chapter 4 includes mass, energy and momentum, not a pressure peak alone.', 13, FG)
    f.note('Worked finite jet of Eq. C3-E30 (ρ = 1000 kg/m³, uniform direction, full activation, independent cells).')


def e31(f):
    N = np.arange(1, 26)
    p = Plot(f, 9.5, 1.95, 3.3, 3.0, (1, 25), (0, 1.1), 'N', 'R_max,N / R_*', (1, 5, 10, 15, 20, 25), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    p.curve(N, N ** (-1 / 3), ACC, 3)
    f.text(8.4, 1.05, 4.5, 'Fixed total work shrinks each bubble', 13, ACC, bold=True)
    f.panel(.4, 1.0, 7.7, 2.6, 'Coupled radial equation', ACC, size=13.5)
    f.text(.55, 1.5, 7.4, 'R_iR̈_i + (3/2)Ṙ_i² = [p_b,i − p∞ − 2σ_b/R_i − 4μṘ_i/R_i]/ρ − Σ_{j≠i} (R_j²R̈_j + 2R_jṘ_j²)/d_ij', 12, FG, bold=True)
    f.text(.55, 2.35, 7.4, 'Neighbours change the pressure each bubble feels, so single-bubble results cannot simply be multiplied by the count.', 12.5, MUT)
    f.panel(.4, 3.8, 7.7, 2.5, 'Fixed total pressure work', WARM, size=13.5)
    f.text(.55, 4.3, 7.4, 'E_B,tot = N (4π/3) Δp_c R_max,N³,   R_max,N = R_* N^(−1/3)', 13, FG, bold=True)
    f.text(.55, 5.0, 7.4, 'Identical constant-pressure ideal cavities; the coupled row needs far separation.', 12, MUT)
    f.text(8.4, 5.55, 4.5, 'Use connectivity and source allocation before summing outputs.', 12.5, WARM)
    f.note('Reference formulas of the Defence 1 answer: Eqs. C3-E05 and C3-E11.')


def e32(f):
    P = np.linspace(0, 2.2e-10, 100)
    p = Plot(f, 9.5, 1.95, 3.3, 3.0, (0, 2.2e-10), (0, 6), 'P_j  (N s)', 'E_j  (nJ)', (0, 1e-10, 2e-10), (0, 2, 4, 6), fx='{:.0e}', fy='{:g}')
    p.curve(P, P ** 2 / (2 * M_J) * 1e9, ACC, 3)
    p.fill(P, P ** 2 / (2 * M_J) * 1e9, np.full_like(P, 6), ACC, .18)
    f.text(8.4, 1.05, 4.4, 'P² ≤ 2mE: the allowed region', 13, ACC, bold=True)
    f.panel(.4, 1.0, 7.7, 1.9, 'Bounds from finite mass', ACC, size=13.5)
    f.text(.55, 1.5, 7.4, 'U_rms ≤ √(2E_avail / m_j),    P_j² ≤ 2 m_j E_j', 14, FG, bold=True)
    f.panel(.4, 3.1, 7.7, 1.7, 'Growth during flight', WARM, size=13.5)
    f.text(.55, 3.6, 7.4, 'δ_arr / a₀ = (δ₀/a₀) exp(g_max H / U_j)', 14, FG, bold=True)
    f.text(.55, 4.2, 7.4, 'g_max is the fastest inviscid growth rate of a cylinder.', 12, MUT)
    f.text(.4, 5.35, 12.5, 'Speed, focusing and survival must all refer to the same emitted liquid state: the same m_j, E_j and U_j.', 13, WARM)
    f.text(.4, 5.95, 12.5, 'Teaching case: m_j = 3.927 ng, E_j = 2 nJ gives U_rms ≤ 31.9 m/s and P_j ≤ 1.253×10⁻¹⁰ N s; flight 3.13 µs → δ/a₀ grows from 1 % to 2.26 %.', 12.5, FG)
    f.note('Reference formulas of the Defence 2 answer: Eqs. C3-E18, E21, E22.')


def e33(f):
    x = np.logspace(-2, 2, 100)
    p = Plot(f, 9.5, 1.95, 3.3, 3.0, (.01, 100), (0, 1.05), 'Z_r / Z_l', 'p/ρcU', (.01, 1, 100), (0, .5, 1), fx='{:g}', fy='{:.1f}', xlog=True)
    p.curve(x, x / (1 + x), ACC, 3)
    f.text(8.4, 1.05, 4.4, 'Contact pressure fraction', 13, ACC, bold=True)
    f.panel(.4, 1.0, 7.7, 1.55, 'Early contact', ACC, size=13.5)
    f.text(.55, 1.45, 7.4, 'p_early ≃ Z_l Z_r U_j / (Z_l + Z_r),   Z_l = ρc', 14, FG, bold=True)
    f.panel(.4, 2.7, 7.7, 1.55, 'Duration', WARM, size=13.5)
    f.text(.55, 3.15, 7.4, 'τ_eq = L_j / c', 14, FG, bold=True)
    f.panel(.4, 4.4, 7.7, 1.9, 'Observer', PINK, size=13.5)
    f.text(.55, 4.85, 7.4, 'p_obs(t) = (1/A_oτ_o) ∫∫ (p − p_ref) dA dξ', 13.5, FG, bold=True)
    f.text(8.4, 5.55, 4.5, 'A finite impact scale is an input to load-path analysis, not proof of intact release.', 12.5, WARM)
    f.note('Reference formulas of the Defence 3 answer: Eqs. C3-E24, E25, E26.')


FIGS = {23: e23, 24: e24, 25: e25, 26: e26, 27: e27, 28: e28, 29: e29, 30: e30, 31: e31, 32: e32, 33: e33}
