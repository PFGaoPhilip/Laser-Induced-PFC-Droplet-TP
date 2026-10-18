"""Chapter 2, equations 13-24."""
import math
import random

import numpy as np

from figlib import *
from figphys import psat_pfp, psat_water

KB = 1.380649e-23
RU = 8.314462618
M_PFC = 0.2880343
M0 = 4 / 3 * math.pi * 1630 * (5e-6) ** 3


def e13(f):
    Tw1 = np.linspace(273, 303, 100)
    Tw2 = np.linspace(304, 333, 100)
    Tp = np.linspace(282.82, 337.94, 100)
    p = Plot(f, 1.0, 1.5, 7.2, 4.0, (270, 340), (.004, 5), 'temperature T  (K)', 'p_sat  (bar)', (270, 280, 290, 300, 310, 320, 330, 340), (.01, .1, 1), fx='{:g}', fy='{:g}', ylog=True)
    p.curve(Tw1, [psat_water(t) / 1e5 for t in Tw1], BLUE, 3)
    p.curve(Tw2, [psat_water(t) / 1e5 for t in Tw2], BLUE, 3)
    p.curve(Tp, psat_pfp(Tp) / 1e5, ACC, 3)
    p.f.rect(p.X(303), p.Y(5), p.X(304) - p.X(303), p.Y(.004) - p.Y(5), fill=PINK, line=PINK, lw=0, opacity=.25)
    p.label(303.5, 1.9, 'gap 303–304 K:\nno value assigned', PINK, 11.5, w=1.7, dx=-1.75, dy=-.1)
    p.label(272, .02, 'water (two fitted branches)', BLUE, 12.5, w=2.8)
    p.label(321, 3.6, 'PFP', ACC, 13, w=1.0)
    for Tm, v, c in [(323.15, psat_water(323.15) / 1e5, BLUE), (323.15, psat_pfp(323.15) / 1e5, ACC)]:
        p.pt(Tm, v, c)
        p.label(Tm, v, f'{v:.2f} bar', c, 12, w=1.2, dx=-1.3, dy=-.45)
    f.panel(8.5, 1.5, 4.45, 4.0, 'A reference, not a reservoir', ACC, size=13.5)
    f.bullets(8.65, 2.0, 4.2, ['Water is the matched-temperature comparison: 0.12 bar at 323 K against 2.05 bar for PFP.', 'Each water branch is valid only inside its own interval, 273–303 K and 304–333 K.', 'The formulas give equilibrium values; they do not promise that vapor is available.'], 12.5)
    f.text(1.0, 6.27, 12, 'Both correlations use log₁₀(p / 10⁵ Pa) = A − B / (T − C) with different A, B, C for each substance and branch.', 12.5, FG)
    f.note('Correlations of Eqs. C2-E12 and C2-E13 (log scale).')


def e14(f):
    x = np.linspace(0, 1.6, 300)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 1.6), (-.8, 1.3), 'r_n / r*', 'W / W*', (0, .5, 1, 1.5), (-.5, 0, .5, 1), fx='{:.1f}', fy='{:.1f}')
    p.seg(0, 0, 1.6, 0, GRID, 1.2)
    p.curve(x, 3 * x ** 2, PINK, 2.2, dash=True)
    p.curve(x, -2 * x ** 3, BLUE, 2.2, dash=True)
    p.curve(x, 3 * x ** 2 - 2 * x ** 3, ACC, 3.4)
    p.pt(1, 1, WARM)
    p.vline(1, WARM)
    p.label(1, 1, 'barrier W* at r* = 2σ/Δp_n', WARM, 12.5, w=3.0, dx=.1, dy=-.5)
    p.label(.05, 1.05, 'surface cost 4πσr² (grows as r²)', PINK, 11.5, w=3.0, dy=-.1)
    p.label(.6, -.55, 'volume gain −(4π/3)Δp_n r³', BLUE, 11.5, w=3.0, dy=-.1)
    p.label(1.15, .35, 'net W', ACC, 13, w=1, dx=.1)
    f.panel(7.7, 1.5, 5.25, 4.0, 'A new interface costs energy first', ACC, size=13.5)
    f.text(7.85, 2.0, 5.0, 'W(r_n) = 4πσ_vp r_n² − (4π/3) Δp_n r_n³', 13, FG, bold=True)
    f.bullets(7.85, 2.65, 5.0, ['Small nuclei: surface term wins, W rises.', 'Large nuclei: volume term wins, W falls.', 'The crossover is a barrier: a nucleus must reach r* before growth lowers its energy.', 'Δp_n = p_sat(T_i) − p_d is the superheat that drives the volume gain.'], 12.5)
    f.text(1.0, 6.27, 12, 'All curves are scaled by W* and r*, so one picture holds for any σ_vp and Δp_n (classical homogeneous capillarity).', 12.5, FG)
    f.note('Free energy of Eq. C2-E14 in scaled form: W/W* = 3x² − 2x³, x = r_n / r*.')


def e15(f):
    sig = .010
    r = np.linspace(0, .22e-6, 300)
    dps = [(2e5, ACC), (4e5, WARM), (8e5, PINK)]
    ymax = 5.0
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (0, .22), (-4, ymax), 'nucleus radius r_n  (µm)', 'W  (10⁻¹⁶ J)', (0, .05, .1, .15, .2), (-4, -2, 0, 2, 4), fx='{:.2f}', fy='{:g}')
    p.seg(0, 0, .22, 0, GRID, 1.2)
    for dp, c in dps:
        W = 4 * math.pi * sig * r ** 2 - 4 * math.pi / 3 * dp * r ** 3
        p.curve(r * 1e6, W * 1e16, c, 3)
        rs = 2 * sig / dp
        Ws = 16 * math.pi * sig ** 3 / (3 * dp ** 2)
        p.pt(rs * 1e6, Ws * 1e16, c)
    for i, (dp, c) in enumerate(dps):
        f.rect(5.0, 1.75 + i * .38, .3, .2, fill=c, line=c, lw=1)
        f.text(5.42, 1.7 + i * .38, 2.2, f'Δp = {dp / 1e5:.0f} bar: r* = {2 * sig / dp * 1e6:.3f} µm', 11.5, c, wrap=False)
    f.panel(8.0, 1.5, 4.95, 4.0, 'Setting dW/dr_n = 0', ACC, size=13.5)
    f.text(8.15, 2.0, 4.7, 'dW/dr_n = 4π r_n (2σ_vp − Δp_n r_n)', 13, FG, bold=True)
    f.text(8.15, 2.55, 4.7, 'r* = 2σ_vp / Δp_n   (Δp_n > 0)', 13, WARM, bold=True)
    f.text(8.15, 3.1, 4.7, 'd²W/dr_n² at r* = −8πσ_vp < 0', 13, PINK, bold=True)
    f.text(8.15, 3.75, 4.7, 'Negative curvature means a maximum, not a stable nucleus: larger superheat only moves the peak to smaller r.', 12, FG)
    f.text(1.0, 6.27, 12, 'Illustrative σ_vp = 0.010 N/m (assumed). Doubling Δp_n halves r* and cuts the barrier by four.', 12.5, MUT)
    f.note('Critical radius and branch check of Eq. C2-E15.')


def e16(f):
    sig = .010
    T = 323.0
    dp = np.logspace(5, 8, 100)
    Ws = 16 * math.pi * sig ** 3 / (3 * dp ** 2)
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (1e5, 1e8), (1, 1e7), 'driving pressure Δp_n  (Pa)', 'W* / k_B T', (1e5, 1e6, 1e7, 1e8), (1, 1e2, 1e4, 1e6), fx='{:.0e}', fy='{:.0e}', xlog=True, ylog=True)
    p.curve(dp, Ws / (KB * T), ACC, 3)
    for d, c in [(1e6, WARM), (1e7, PINK)]:
        v = 16 * math.pi * sig ** 3 / (3 * d ** 2) / (KB * T)
        p.pt(d, v, c)
        p.label(d, v, f'Δp = {d / 1e5:.0f} bar: {v:,.0f} k_BT', c, 12, w=2.8, dx=.1, dy=-.5 if d < 5e6 else -.5)
    p.label(2e5, 3e5, 'slope −2', ACC, 12.5, w=1.2)
    f.panel(8.2, 1.5, 4.75, 4.0, 'The barrier does not vanish', ACC, size=13.5)
    f.text(8.35, 2.0, 4.5, 'W* = 16π σ_vp³ / (3 Δp_n²)', 14, FG, bold=True)
    f.text(8.35, 2.6, 4.5, 'Derivation: W(r*) = (16 − 32/3) π σ³/Δp² = (16/3) π σ³/Δp²', 12, MUT)
    f.bullets(8.35, 3.4, 4.5, ['Positive superheat shrinks the barrier but never removes it.', 'Relative to thermal energy k_B T the barrier is still thousands of units at 10 bar.'], 12.5)
    f.text(1.0, 6.27, 12, 'Illustrative σ_vp = 0.010 N/m (assumed), T = 323 K. Thermal fluctuations alone rarely cross barriers of many k_B T.', 12.5, MUT)
    f.note('Barrier height of Eq. C2-E16, homogeneous locally isothermal small-nucleus model.')


def e17(f):
    t = np.linspace(0, 5, 500)
    cases = [('A: Λ = 2/µs for 1 µs', ACC, 2.0, 1.0), ('B: Λ = 0.5/µs for 4 µs', WARM, .5, 4.0), ('C: Λ = 2/µs for 0.2 µs', PINK, 2.0, .2)]
    p1 = Plot(f, 1.0, 1.5, 5.6, 1.7, (0, 5), (0, 2.6), '', 'Λ(t)  (1/µs)', (0, 1, 2, 3, 4, 5), (0, 1, 2), fx='{:g}', fy='{:g}')
    p2 = Plot(f, 1.0, 3.95, 5.6, 1.75, (0, 5), (0, 1.05), 't  (µs)', 'P_act', (0, 1, 2, 3, 4, 5), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    for lab, c, L, T in cases:
        rate = np.where(t <= T, L, 0)
        p1.curve(t, rate, c, 2.6)
        cum = np.cumsum(rate) * (t[1] - t[0])
        p2.curve(t, 1 - np.exp(-cum), c, 3)
        p2.pt(5, 1 - math.exp(-L * T), c, .06)
    f.panel(7.3, 1.5, 5.65, 4.2, 'P_act = 1 − exp(−∫∫ J dV dt)', ACC, size=13.5)
    for i, (lab, c, L, T) in enumerate(cases):
        y = 2.1 + i * .62
        f.rect(7.5, y + .05, .3, .22, fill=c, line=c, lw=1)
        f.text(7.95, y, 3.0, lab, 12, c, bold=True)
        f.text(10.9, y, 2.0, f'∫Λ dt = {L * T:.1f}  →  P = {1 - math.exp(-L * T):.2f}', 11.5, FG, wrap=False)
    f.text(7.5, 4.1, 5.3, 'A and B have different rates and durations but the same integral, so they end at the same activation probability. C has the high rate but too little time.', 12.5, FG)
    f.text(1.0, 6.27, 12, 'Rate alone does not decide activation: the product of rate and time spent in the activating state does. J(T, p) must be supplied by the material.', 12.5, WARM)
    f.note('Independent Poisson events; survival S = exp(−∫Λ dt) (Eq. C2-E17). Rates are illustrative.')


def e18(f):
    t = np.linspace(0, 4, 400)
    liq = .95 / (1 + np.exp(3 * (t - 1.0)))
    ev = 1 - liq
    mdis = .12 * ev * (1 - np.exp(-t / 1.5))
    mesc_n = .35 * ev * (1 - np.exp(-np.clip(t - 2.0, 0, None) / .8))
    mvapor = 1 - liq - mdis - mesc_n
    ml, mvapor, mdis, mesc_n = [np.clip(a_, 0, 1) * M0 * 1e12 for a_ in (liq, mvapor, mdis, mesc_n)]
    p = Plot(f, 1.0, 1.5, 7.0, 4.0, (0, 4), (0, M0 * 1e12 * 1.08), 'time  (arbitrary units)', 'PFC mass  (ng)', (0, 1, 2, 3, 4), (0, .2, .4, .6, .8), fx='{:g}', fy='{:.1f}')
    base = np.zeros_like(t)
    for arr, c in [(ml, BLUE), (mvapor, ACC), (mdis, WARM), (mesc_n, PINK)]:
        top = base + arr
        p.fill(t, base, top, c, .55)
        base = top
    p.hline(M0 * 1e12, '#FFFFFF')
    p.label(.1, M0 * 1e12, f'm_PFC,0 = {M0 * 1e12:.3f} ng (never exceeded)', FG, 12, w=4, dy=-.32)
    f.panel(8.3, 1.5, 4.65, 4.0, 'Four compartments, one total', ACC, size=13.5)
    for i, (s, c) in enumerate([('m_l  liquid PFC remaining', BLUE), ('m_v  vapor inside the domain', ACC), ('m_diss  dissolved PFC', WARM), ('m_esc  escaped (vented) PFC', PINK)]):
        f.rect(8.5, 2.1 + i * .5 + .04, .3, .22, fill=c, line=c, lw=1)
        f.text(8.92, 2.1 + i * .5, 3.9, s, 12, FG)
    f.text(8.45, 4.2, 4.4, 'm_l + m_v + m_diss + m_esc = m_PFC,0 at every instant (no external supply).', 12.5, WARM, bold=True)
    f.text(1.0, 6.27, 12, 'm_PFC,0 = (4π/3) ρ_d a₀³ = 0.8535 ng for a 5 µm core.  The split among compartments is a schematic here, not a calculation.', 12.5, FG)
    f.note('Mass ledger of Eq. C2-E18; compartment histories are illustrative.')


def e19(f):
    f.panel(.4, 1.0, 6.4, 5.4, 'Which surface evaporates PFC?', ACC, size=13.5)
    cx, cy = 3.3, 3.8
    f.ellipse(cx, cy, 1.5, fill=LIQ, line=ACC, lw=2.4)
    f.ellipse(cx + 1.0, cy - .1, 1.3, fill=GASC, line=WARM, lw=2.4, opacity=.95)
    arc = [(cx + 1.5 * math.cos(a_), cy - 1.5 * math.sin(a_)) for a_ in np.linspace(-math.pi, math.pi, 400)]
    arc = [q for q in arc if math.hypot(q[0] - (cx + 1.0), q[1] - (cy - .1)) < 1.3]
    f.path(arc, PINK, 5)
    f.text(cx + 1.6, cy + 1.25, 2.0, 'Γ_s: droplet surface\nin contact with vapor', 11.5, PINK, bold=True)
    f.text(1.3, 2.0, 2.5, 'PFC droplet', 12.5, ACC, bold=True)
    f.text(3.9, 2.0, 2.6, 'vapor bubble', 12.5, WARM, bold=True)
    f.line(2.5, 3.7, 2.1, 3.7, ACC, 3, arrow=True)
    f.text(.55, 5.55, 6.1, 'Evaporation occurs on the part of the droplet surface that touches vapor, Γ_s. It need not coincide with the whole bubble surface.', 12.5, FG)
    f.panel(7.1, 1.0, 5.85, 5.4, 'Mass balance of species s', ACC, size=13.5)
    f.text(7.25, 1.5, 5.6, 'ṁ_v,s |phase = ∫ over Γ_s of j_s dA', 14, FG, bold=True)
    f.text(7.25, 2.2, 5.6, 'j_s: signed liquid-to-vapor mass flux (kg m⁻² s⁻¹)', 12.5, MUT)
    f.panel(7.25, 2.85, 5.55, 1.55, None, WARM)
    f.text(7.4, 2.93, 5.3, 'Special case only', 13, WARM, bold=True)
    f.text(7.4, 3.35, 5.3, 'ṁ = 4πR² j_s   when the whole spherical bubble wall of radius R is in uniform contact with the PFC.', 12.5, FG)
    f.text(7.25, 4.65, 5.6, 'Phase change is only one term: escape and dissolution are accounted for separately in the ledger of Eq. C2-E18.', 12.5, FG)
    f.note('Area integral of Eq. C2-E19; sketch is schematic.')


def e20(f):
    f.panel(.4, 1.0, 6.2, 5.4, 'Interface speed is not liquid speed', ACC, size=13.5)
    cx, cy = 1.9, 3.8
    xi = 3.3
    f.rect(.7, 2.2, xi - .7, 3.1, fill=GASC, line=None if False else MUT, lw=1, opacity=.9)
    f.rect(xi, 2.2, 6.2 - xi - .2, 3.1, fill=LIQ, line=MUT, lw=1)
    f.line(xi, 2.1, xi, 5.4, WARM, 4)
    f.text(1.0, 2.3, 2.0, 'vapor\n(bubble)', 12.5, MUT, bold=True)
    f.text(4.5, 2.3, 1.8, 'liquid', 12.5, ACC, bold=True)
    f.line(xi, 3.2, xi + 2.4, 3.2, WARM, 4, arrow=True)
    f.text(xi + .1, 2.7, 2.5, 'v_Γ = Ṙ  (10 m/s)', 12, WARM, bold=True)
    f.line(xi + .6, 4.0, xi + .6 + 1.92, 4.0, ACC, 4, arrow=True)
    f.text(xi + .1, 4.1, 2.5, 'u_l(R) = 8 m/s', 12, ACC, bold=True)
    f.line(xi + 2.52, 4.0, xi + 2.4, 4.0, PINK, 1)
    f.dim(xi + 2.4 - .48, 4.7, xi + 2.4, 4.7, '', PINK, 11)
    f.text(xi - .3, 4.85, 3.0, 'Ṙ − u_l = 2 m/s', 12, PINK, bold=True)
    f.text(.55, 5.55, 5.9, 'The interface outruns the adjacent liquid: liquid is converted to vapor at the surface.', 12, FG)
    f.panel(6.9, 1.0, 6.05, 5.4, 'Single-component jump condition', ACC, size=13.5)
    f.text(7.05, 1.5, 5.8, 'j_s = ρ_l (u_l − v_Γ)·n = ρ_v (u_v − v_Γ)·n', 13.5, FG, bold=True)
    f.text(7.05, 2.2, 5.8, 'n = −e_r (liquid → vapor),  v_Γ = Ṙ e_r', 12.5, MUT)
    f.text(7.05, 2.85, 5.8, 'j_s = ρ_l [Ṙ − u_l(R)]', 14, WARM, bold=True)
    f.text(7.05, 3.5, 5.8, 'u_l(R) = Ṙ − j_s / ρ_l', 14, ACC, bold=True)
    f.text(7.05, 4.2, 5.8, 'With no phase change, j_s = 0 and the liquid at the wall moves with the wall (u_l = Ṙ). Evaporation breaks that equality.', 12.5, FG)
    f.text(7.05, 5.35, 5.8, 'Speeds in the left panel are illustrative.', 11.5, MUT)
    f.note('Mass jump of Eq. C2-E20.')


def e21(f):
    z = np.linspace(-1, 1, 400)
    p = Plot(f, 1.0, 1.5, 6.4, 3.8, (-1, 1), (0, 1.1), 'distance from the interface (liquid | vapor)', 'temperature (relative)', (), (), )
    zl, zv = z[z < 0], z[z >= 0]
    p.curve(zl, .9 + .35 * zl, WARM, 3)
    p.curve(zv, .9 - .08 * zv * 1, ACC, 3)
    p.vline(0, MUT)
    p.pt(0, .9, PINK)
    p.label(-.9, 1.05, 'liquid: steep gradient\n(larger q_l)', WARM, 12, w=2.4, dy=-.1)
    p.label(.15, 1.05, 'vapor: gentle gradient\n(smaller q_v)', ACC, 12, w=2.4, dy=-.1)
    p.arrow(-.5, .25, -.05, .25, WARM, 3.5)
    p.arrow(.05, .25, .5, .25, ACC, 2)
    p.label(-.55, .33, 'q_l·n', WARM, 12.5, w=1.2, dy=-.1)
    p.label(.15, .33, 'q_v·n', ACC, 12.5, w=1.2, dy=-.1)
    f.panel(7.7, 1.5, 5.25, 3.8, 'Heat that is not passed on becomes latent heat', ACC, size=13)
    f.text(7.85, 2.0, 5.0, 'j_s L_v,s = (q_l − q_v)·n', 14, FG, bold=True)
    f.text(7.85, 2.6, 5.0, 'L_v,s = h_v,s − h_l,s > 0 (J/kg)', 12.5, MUT)
    hb = hbars(f, 7.85, 3.15, 4.9, [('q_l·n arriving', 1000, WARM), ('q_v·n leaving', 200, ACC), ('j L_v = difference', 800, PINK)], 1000, label_w=2.0, fmt='{:.0f}', unit=' W/m²', size=11.5, bar_h=.32, gap=.14)
    f.text(1.0, 5.95, 12, 'Fourier law on each side: q_η = −k_η ∇T_η, η = l, v. Signs are fixed by n pointing liquid → vapor.', 12.5, FG)
    f.text(1.0, 6.45, 12, 'Example: 800 W/m² of unbalanced heat with L_v = 95 kJ/kg evaporates j = 8.4 g m⁻² s⁻¹. Fluxes shown are illustrative.', 12.5, WARM)
    f.note('Reduced energy jump of Eq. C2-E21.')


def e22(f):
    f.panel(.4, 1.0, 6.4, 5.4, 'Open bubble as a control volume', ACC, size=13.5)
    cx, cy = 3.4, 3.7
    f.ellipse(cx, cy, 1.2, fill=GASC, line=WARM, lw=2.6)
    f.text(cx - .8, cy - .3, 1.6, 'U_b\nuniform T_b, p_b', 12.5, FG, 'center', bold=True)
    f.line(cx - 2.9, cy, cx - 1.25, cy, PINK, 4, arrow=True)
    f.text(.55, cy - .65, 1.9, 'heat in Q̇_b\n(conduction)', 12, PINK, bold=True)
    f.line(cx - 1.0, cy - 2.0, cx - .6, cy - 1.22, ACC, 4, arrow=True)
    f.text(cx - 2.5, cy - 2.4, 2.8, 'vapor in:  Σ h_v,s ṁ_v,s', 12, ACC, bold=True)
    a = math.radians(40)
    f.line(cx + 1.25 * math.cos(a), cy - 1.25 * math.sin(a), cx + 2.15 * math.cos(a), cy - 2.15 * math.sin(a), WARM, 4, arrow=True)
    f.text(cx + 1.3, cy - 2.35, 2.6, 'work out: p_b V̇_b', 12, WARM, bold=True)
    f.text(.55, 5.7, 6.0, 'V_b = (4π/3)R³, V̇_b = 4πR²Ṙ', 12, MUT)
    steps = [('Q̇_b', .3, PINK), ('Σ h ṁ', 1.1, ACC), ('−p_b V̇_b', -.9, WARM), ('= U̇_b', None, BLUE)]
    f.text(7.1, 1.05, 5.8, 'Power ledger (illustrative values, W)', 13.5, ACC, bold=True)
    waterfall(f, 7.2, 1.7, 5.6, 3.4, steps, 1.7, fmt='{:.1f}', yticks=(0, .5, 1, 1.5), ylabel='')
    f.text(7.1, 5.85, 5.8, 'U̇_b = Q̇_b − p_b V̇_b + Σ h_v,s ṁ_v,s. Transported enthalpy and conduction are different terms.', 12, FG)
    f.note('First law of Eq. C2-E22; the numbers in the ledger are illustrative.')


def e23(f):
    T = 323.0
    he = RU * T / M_PFC
    f.panel(.4, 1.0, 5.6, 5.4, 'From U_b to a temperature equation', ACC, size=13.5)
    steps = [('Internal energy', 'U_b = Σ m_v,s e_s(T_b)'), ('Product rule', 'U̇_b = (Σ m c_v) Ṫ_b + Σ e_s ṁ_v,s'), ('Insert the first law', '(Σ m c_v) Ṫ_b = Q̇_b − p_b V̇_b + Σ (h_v,s − e_s) ṁ_v,s')]
    y = 1.5
    for h, e in steps:
        f.text(.6, y, 5.2, h, 12.5, WARM, bold=True)
        y = f.text(.85, y + .33, 5.0, e, 12.5, FG) + .3
    f.text(.6, y, 5.2, f'For an ideal vapor h − e = R_u T / M = {he / 1e3:.1f} kJ/kg at 323 K, so every mass added also carries the work term.', 12, MUT)
    steps2 = [('Σ(h−e)ṁ', 1.30, ACC), ('Q̇_b', .30, PINK), ('−p V̇', -.90, WARM), ('= (Σmc_v) Ṫ', None, BLUE)]
    f.text(6.3, 1.05, 6.6, 'Terms that change the bubble temperature (illustrative, W)', 13, ACC, bold=True)
    waterfall(f, 6.5, 1.7, 6.3, 3.4, steps2, 1.9, fmt='{:.2f}', yticks=(0, .5, 1, 1.5), ylabel='')
    f.text(6.3, 5.85, 6.6, 'A fixed-mass polytropic law cannot hold while ṁ_v,s ≠ 0: the mass terms change the temperature as well.', 12.5, FG)
    f.note('Thermal closure of Eq. C2-E23; waterfall values are illustrative.')


def e24(f):
    R = np.logspace(math.log10(5e-6), math.log10(80e-6), 100)
    V = 4 / 3 * math.pi * R ** 3
    pv = M0 * RU * 323.15 / (M_PFC * V)
    p = Plot(f, 1.0, 1.5, 6.6, 4.0, (5, 80), (1e3, 1e8), 'bubble radius R  (µm)', 'ideal p_v,PFC  (Pa)', (5, 10, 20, 40, 80), (1e3, 1e4, 1e5, 1e6, 1e7, 1e8), fx='{:g}', fy='{:.0e}', xlog=True, ylog=True)
    p.curve(R * 1e6, pv, ACC, 3)
    Rinv = 26.6827
    p.pt(Rinv, 1e5, WARM)
    p.label(Rinv, 1e5, 'R = 26.7 µm: p = 1 bar', WARM, 12, w=2.4, dx=.1, dy=-.5)
    p.label(11, 2e7, 'p ∝ m T / R³ for fixed m, T', ACC, 12.5, w=3, dy=-.05)
    f.panel(8.3, 1.5, 4.65, 4.0, 'Pressure responds to three things', ACC, size=13.5)
    f.text(8.45, 2.0, 4.4, 'p_v,s V_b = (m_v,s / M_s) R_u T_b\np_b = Σ p_v,s', 12.5, FG, bold=True)
    f.bullets(8.45, 2.85, 4.4, ['species mass m_v,s (evaporation raises p)', 'temperature T_b (heating raises p)', 'volume V_b (expansion lowers p)'], 12.5)
    f.text(8.45, 4.35, 4.4, 'This ideal-mixture control is a first model; a real-mixture equation of state p = 𝒫(ρ_b, e_b, Y) is the required refinement.', 12, MUT)
    f.text(1.0, 6.27, 12, 'Curve for the fixed PFP inventory of a 5 µm droplet (0.8535 ng) at 323 K. Expansion alone drops p by a factor 1000 for a tenfold radius.', 12.5, FG)
    f.note('Ideal-gas control of Eq. C2-E24 with M_PFC = 0.2880343 kg/mol.')


FIGS = {13: e13, 14: e14, 15: e15, 16: e16, 17: e17, 18: e18, 19: e19, 20: e20, 21: e21, 22: e22, 23: e23, 24: e24}
