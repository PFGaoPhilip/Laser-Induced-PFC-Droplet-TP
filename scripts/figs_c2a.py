"""Chapter 2, equations 01-12."""
import math

import numpy as np

from figlib import *
from figphys import psat_pfp, psat_water

ALPHA = 0.050 / (1630 * 654)


def spot(f, cx, cy, rmax, w, n=14, color=ACC):
    for i in range(n, 0, -1):
        r = rmax * i / n
        f.ellipse(cx, cy, r, fill=color, line=color, lw=0, opacity=.045 + .55 * math.exp(-2 * (r / (w * rmax / 1.0)) ** 2 * 0 - 2 * (r / w) ** 2) if False else None)


def beam(f, cx, cy, w_in, extent=1.9, n=22, color=ACC):
    """Concentric discs whose brightness follows exp(-2 r^2/w^2); w_in is the e^-2 radius in inches."""
    for i in range(n, 0, -1):
        r = extent * i / n
        f.ellipse(cx, cy, r, fill=color, line=None if False else color, lw=0, opacity=max(.05, .8 * math.exp(-2 * (r / w_in) ** 2)))


def e01(f):
    f.panel(.4, 1.0, 4.6, 5.3, 'Beam spot on the target', ACC, size=13.5)
    cx, cy, w_in = 2.7, 3.7, 1.2
    beam(f, cx, cy, w_in)
    f.ellipse(cx, cy, w_in, fill=None, line=WARM, lw=2.2)
    f.line(cx, cy, cx + w_in, cy, WARM, 2)
    f.text(cx + .3, cy + .02, .8, 'w', 15, WARM, bold=True)
    f.text(.55, 5.75, 4.3, 'Brightest on the axis, fading outward. The quoted radius w is where F drops to e⁻² of F₀.', 12, FG)
    r = np.linspace(0, 2.2, 200)
    p = Plot(f, 6.0, 1.5, 6.4, 4.0, (0, 2.2), (0, 1.1), 'r / w', 'F(r) / F₀', (0, .5, 1, 1.5, 2), (0, .25, .5, .75, 1), fx='{:.1f}', fy='{:.2f}')
    p.curve(r, np.exp(-2 * r ** 2), ACC, 3)
    p.fill(r, np.zeros_like(r), np.exp(-2 * r ** 2), ACC, .15)
    p.pt(1, math.exp(-2), WARM)
    p.vline(1, WARM)
    p.label(1, math.exp(-2), 'r = w:  F = F₀ e⁻² = 0.135 F₀', WARM, 12.5, w=3.0, dx=.15, dy=-.55)
    p.label(.1, .98, 'F(r) = F₀ exp(−2r²/w²)', ACC, 13, w=3.2)
    f.text(6.0, 6.27, 6.4, 'The same profile is called "radius w" only with this e⁻² definition; other conventions differ by √2.', 12.5, FG)
    f.note('Gaussian fluence profile of Eq. C2-E01.')


def e02(f):
    r = np.linspace(0, 2.4, 300)
    p = Plot(f, .95, 1.5, 5.6, 4.0, (0, 2.4), (0, .65), 'r / w', 'ring energy 2πrF(r) / (π w F₀)', (0, .5, 1, 1.5, 2), (0, .2, .4, .6), fx='{:.1f}', fy='{:.1f}')
    ring = 2 * r * np.exp(-2 * r ** 2) * 1.0
    p.fill(r, np.zeros_like(r), ring / 2 * 1.0, ACC, .3)
    p.curve(r, ring / 2, ACC, 3)
    p.vline(.5, WARM)
    p.label(.5, .6, 'peak ring at r = w/2', WARM, 12.5, w=2.4, dx=.12, dy=-.05)
    p.label(1.1, .3, 'area under the curve = E_L', ACC, 12.5, w=2.8)
    p2 = Plot(f, 7.3, 1.5, 5.6, 4.0, (0, 2.4), (0, 1.05), 'r / w', 'energy inside r  /  E_L', (0, .5, 1, 1.5, 2), (0, .25, .5, .75, 1), fx='{:.1f}', fy='{:.2f}')
    p2.curve(r, 1 - np.exp(-2 * r ** 2), WARM, 3)
    p2.pt(.5, 1 - math.exp(-.5), ACC)
    p2.label(.5, 1 - math.exp(-.5), '39 % inside w/2', ACC, 12, w=2.2, dx=.12, dy=.05)
    p2.pt(1, 1 - math.exp(-2), ACC)
    p2.label(1, 1 - math.exp(-2), '86.5 % inside w', ACC, 12, w=2.2, dx=.12, dy=.1)
    f.text(.95, 6.27, 12, 'E_L = 2πF₀ ∫ r e^(−2r²/w²) dr = (πw²F₀/2) ∫ e^(−x) dx = π w² F₀ / 2     (x = 2r²/w²)', 13.5, FG, bold=True)
    f.text(.95, 6.7, 12, 'Summing annular rings 2πr dr reproduces the closed form; the total is finite although the Gaussian never ends.', 12.5, WARM)
    f.note('Ring weights and cumulative energy from Eq. C2-E02.')


def e03(f):
    f.panel(.4, 1.0, 5.0, 5.3, 'An aperture keeps the inner part', ACC, size=13.5)
    cx, cy, w_in = 2.9, 3.6, 1.0
    beam(f, cx, cy, w_in, extent=2.0)
    for k, (m, c) in enumerate([(0.5, PINK), (1.0, WARM), (1.5, BLUE)]):
        f.ellipse(cx, cy, w_in * m, fill=None, line=c, lw=2.2)
    f.text(.55, 5.75, 4.7, 'Circles: absorber apertures b_a = 0.5w, w, 1.5w. Light outside is not used.', 12, FG)
    b = np.linspace(0, 2.5, 300)
    p = Plot(f, 6.3, 1.5, 6.5, 4.0, (0, 2.5), (0, 1.05), 'b_a / w', 'f_geo', (0, .5, 1, 1.5, 2, 2.5), (0, .25, .5, .75, 1), fx='{:.1f}', fy='{:.2f}')
    p.curve(b, 1 - np.exp(-2 * b ** 2), ACC, 3)
    for m, c in [(0.5, PINK), (1.0, WARM), (1.5, BLUE)]:
        v = 1 - math.exp(-2 * m ** 2)
        p.pt(m, v, c)
        p.label(m, v, f'{v:.3f}', c, 12.5, w=1.0, dx=.1, dy=.05 if m > .5 else -.45)
    f.text(6.3, 6.27, 6.5, 'f_geo = 1 − exp(−2 b_a² / w²):  the outer annuli are removed from the useful energy.', 13, FG, bold=True)
    f.note('Interception fraction of Eq. C2-E03; b_a = w/2 gives the 0.3935 used later.')


def e04(f):
    t = np.linspace(-1, 3, 800)
    taul = 1.0
    rect = np.where((t >= 0) & (t <= taul), 1 / taul, 0.0)
    sig = .45
    gauss = np.exp(-(t - 1.0) ** 2 / (2 * sig ** 2)) / (sig * math.sqrt(2 * math.pi))
    p = Plot(f, 1.0, 1.5, 7.0, 4.0, (-.5, 2.5), (0, 1.0), 't / τ_L', 'f(t)  (1/τ_L)', (0, 1, 2), (0, .5, 1), fx='{:g}', fy='{:.1f}')
    p.fill(t, np.zeros_like(t), rect, ACC, .3)
    p.curve(np.array([-.5, 0, 0, taul, taul, 2.5]), np.array([0, 0, 1, 1, 0, 0]), ACC, 3)
    p.curve(t, gauss, WARM, 3, dash=True)
    p.label(1.05, .98, 'rectangular pulse: f = 1/τ_L', ACC, 12.5, w=2.8, dx=.1, dy=-.1)
    p.label(1.45, .6, 'Gaussian pulse, same area', WARM, 12.5, w=2.6)
    f.panel(8.3, 1.5, 4.65, 4.0, 'Energy, shape and timing', ACC, size=13.5)
    f.text(8.45, 2.0, 4.4, '∫ f(t) dt = 1\nI(r,t) = F(r) f(t)', 13.5, FG, bold=True)
    f.text(8.45, 2.85, 4.4, 'Peak irradiance for a rectangular pulse:\nI_peak = F₀ / τ_L', 13, WARM, bold=True)
    f.text(8.45, 3.8, 4.4, 'Example: F₀ = 1 J/cm², τ_L = 10 ns gives I_peak = 10⁸ W/cm². The same energy in a shorter pulse raises the peak.', 12, FG)
    f.text(1.0, 6.27, 12, 'Normalised so that f only says when the energy arrives, never how much: F(r) carries the amount.', 13, FG)
    f.note('Pulse shapes of Eq. C2-E04.')


def e05(f):
    mu = 2e5
    z = np.linspace(0, 20, 300)
    f.panel(.4, 1.0, 4.4, 5.3, 'Light entering an absorber', ACC, size=13.5)
    y0 = 1.7
    f.rect(1.0, 2.0, 3.2, 3.6, fill=LIQ, line=LIQ2, lw=1.4)
    for k in range(7):
        yy = 2.0 + k * .5
        f.rect(1.0, yy, 3.2, .5, fill=WARM, line=None if False else WARM, lw=0, opacity=.55 * math.exp(-mu * (k * .5 / 3.6 * 20e-6)) )
    for k in range(4):
        L = 1.0 * math.exp(-k * .35)
        f.line(1.5 + k * .75, 1.5, 1.5 + k * .75, 1.5 + max(L, .3) * .45, ACC, 2.4, arrow=True)
    f.text(.55, 5.7, 4.1, 'Deeper layers see less light, so they heat less: Q_abs = μ_a I(z).', 12, FG)
    p = Plot(f, 6.1, 1.5, 6.6, 4.0, (0, 20), (0, 1.05), 'depth z  (µm)', 'I(z) / I_in', (0, 5, 10, 15, 20), (0, .25, .5, .75, 1), fx='{:g}', fy='{:.2f}')
    p.curve(z, np.exp(-mu * z * 1e-6), ACC, 3)
    p.fill(z, np.zeros_like(z), np.exp(-mu * z * 1e-6), WARM, .18)
    p.pt(5, math.exp(-1), WARM)
    p.vline(5, WARM)
    p.label(5, math.exp(-1), '1/μ_a = 5 µm: I = I_in/e = 0.37 I_in', WARM, 12.5, w=3.6, dx=.15, dy=-.55)
    p.label(9, .75, 'I(z) = I_in e^(−μ_a z)\nμ_a = 2×10⁵ m⁻¹', ACC, 13, w=3, dy=-.1)
    f.text(6.1, 6.27, 6.6, 'Heat deposition follows the same curve: most of it lands within a few 1/μ_a of the surface.', 13, FG)
    f.note('Beer–Lambert decay of Eq. C2-E05 with the teaching absorption coefficient.')


def e06(f):
    EL = 1000.0
    fg = 1 - math.exp(-2 * .25)
    A = .9 * (1 - math.exp(-1))
    steps = [('incident E_L', EL, ACC), ('outside aperture', -(1 - fg) * EL, PINK), ('reflected 10 %', -fg * .1 * EL, BLUE), ('transmitted', -fg * .9 * math.exp(-1) * EL, PURP), ('absorbed E_abs', None, WARM)]
    p = waterfall(f, 1.0, 1.5, 7.2, 4.0, steps, 1100, fmt='{:.0f}', yticks=(0, 250, 500, 750, 1000), ylabel='energy (nJ)')
    f.panel(8.5, 1.5, 4.45, 4.0, 'Each factor acts once', ACC, size=13.5)
    f.text(8.65, 2.0, 4.2, 'f_geo = 1 − e^(−2(10/20)²) = 0.3935', 12.5, ACC, bold=True)
    f.text(8.65, 2.55, 4.2, 'A_λ = (1 − 0.10)(1 − e^(−1)) = 0.5689', 12.5, BLUE, bold=True)
    f.text(8.65, 3.1, 4.2, f'E_abs = f_geo A_λ E_L = {fg * A * EL:.1f} nJ', 13, WARM, bold=True)
    f.text(8.65, 3.8, 4.2, 'Interception, front-face reflection and internal absorption are separate, multiplied losses; none is counted twice.', 12, FG)
    f.text(1.0, 6.27, 12, 'Energy accounting for E_L = 1 µJ, aperture 10 µm, beam radius 20 µm, μ_a h_a = 1, R_λ = 0.10 (declared inputs).', 12.5, MUT)
    f.note('Energy balance of Eq. C2-E06, numbers as in Eq. C2-E31.')


def e07(f):
    f.panel(.4, 1.0, 6.4, 5.4, 'Energy balance of a small parcel', ACC, size=13.5)
    f.rect(2.5, 2.7, 2.2, 1.6, fill=LIQ2, line=ACC, lw=2.4, opacity=.9)
    f.text(2.5, 3.2, 2.2, 'ρ c_p DT/Dt', 13.5, FG, 'center', bold=True)
    f.line(1.0, 3.5, 2.45, 3.5, PINK, 3.5, arrow=True)
    f.text(.55, 3.0, 1.9, 'conduction in\n−∇·q', 12, PINK, 'center', bold=True)
    f.line(4.75, 3.5, 6.2, 3.5, PINK, 3.5, arrow=True)
    f.text(4.8, 3.0, 1.9, 'conduction out', 12, PINK, 'center')
    f.line(3.6, 2.0, 3.6, 2.65, WARM, 3.5, arrow=True)
    f.text(2.6, 1.55, 2.4, 'absorbed light Q_abs', 12, WARM, 'center', bold=True)
    f.text(.6, 4.7, 6.0, 'Stored heat rate  =  net conduction  +  optical source', 13.5, FG, bold=True)
    f.text(.6, 5.2, 6.0, 'q = −k∇T (Fourier),   D/Dt = ∂/∂t + u·∇', 12.5, MUT)
    f.panel(7.1, 1.0, 5.85, 5.4, 'Two different heating jobs', ACC, size=13.5)
    f.rect(7.4, 2.0, 1.6, 3.4, fill=STEEL, line=MUT, lw=1.4)
    f.text(7.4, 3.4, 1.6, 'absorber\nQ_abs ≠ 0', 12.5, WARM, 'center', bold=True)
    f.line(9.05, 3.7, 9.9, 3.7, PINK, 3.5, arrow=True)
    f.ellipse(11.1, 3.7, 1.0, fill=LIQ, line=ACC, lw=2.2)
    f.text(10.2, 3.55, 1.8, 'PFC\nQ_abs = 0', 12.5, ACC, 'center', bold=True)
    f.text(7.3, 5.55, 5.5, 'Heating the absorber and heating the PFC are separate steps joined only by conduction across the contact.', 12.5, FG)
    f.note('Reduced heat equation of Eq. C2-E07; sketch of the heat path.')


def e08(f):
    z = np.linspace(-1, 1, 400)
    qn = 1.0
    RT = 0.35
    TA = 1.0 - .5 * (z + 1) * 0 - .35 * (z + 1) * 0.0
    zA = z[z < 0]
    zB = z[z >= 0]
    TAprof = .85 + (-.2) * (zA)  # gently falling toward the contact
    TBprof = .85 - .2 * 0 - RT - .25 * zB * 1.0
    p = Plot(f, 1.0, 1.5, 7.0, 4.0, (-1, 1), (0, 1.1), 'position across the contact', 'temperature (relative)', (), (0, .5, 1), fy='{:.1f}')
    ta = .85 - .2 * zA
    tb = .85 - .2 * 0 - RT - .2 * zB
    p.curve(zA, ta, WARM, 3)
    p.curve(zB, tb, ACC, 3)
    p.seg(0, ta[-1], 0, tb[0], PINK, 2.5)
    p.vline(0, MUT)
    p.label(-.9, 1.05, 'material A', WARM, 13, w=1.8, dy=-.05)
    p.label(.55, 1.05, 'material B', ACC, 13, w=1.8, dy=-.05)
    p.label(.05, .75, 'T_A − T_B = R_T q_n', PINK, 13, w=2.8, dx=.12, dy=.0)
    p.arrow(-.8, .12, -.2, .12, PINK, 3)
    p.arrow(.2, .12, .8, .12, PINK, 3)
    p.label(-.5, .2, 'q_n', PINK, 13, w=.8, dx=0, dy=-.1)
    p.label(.45, .2, 'q_n (same)', PINK, 12, w=1.4, dx=0, dy=-.1)
    f.panel(8.3, 1.5, 4.65, 4.0, 'Resistance at the contact', ACC, size=13.5)
    f.text(8.45, 2.0, 4.4, 'Flux continuity:\nq_A·n = q_B·n = q_n', 13, FG, bold=True)
    f.text(8.45, 2.85, 4.4, 'Temperature jump:\nT_A − T_B = R_T q_n', 13, PINK, bold=True)
    f.text(8.45, 3.7, 4.4, 'R_T (m²K/W) is a property of the interface. The same heat flows, but a temperature step builds up and delays heating of side B.', 12, FG)
    f.text(1.0, 6.27, 12, 'Light is absorbed in A, yet B warms only after heat crosses the contact: absorbed energy is not delivered energy.', 12.5, WARM)
    f.note('Contact conditions of Eq. C2-E08; profile is schematic.')


def e09(f):
    tau = np.logspace(-9, -3, 100)
    p = Plot(f, 1.0, 1.5, 5.6, 4.0, (1e-9, 1e-3), (1e-9, 1e-5), 'heating time τ_h  (s)', 'penetration δ_T  (m)', (1e-9, 1e-7, 1e-5, 1e-3), (1e-9, 1e-8, 1e-7, 1e-6, 1e-5), fx='{:.0e}', fy='{:.0e}', xlog=True, ylog=True)
    p.curve(tau, np.sqrt(ALPHA * tau), ACC, 3)
    p.pt(1e-8, math.sqrt(ALPHA * 1e-8), WARM)
    p.label(1e-8, math.sqrt(ALPHA * 1e-8), 'δ_T ≈ 22 nm at 10 ns', WARM, 12, w=2.4, dx=.12, dy=-.45)
    p.label(2e-6, 4e-8, 'δ_T ~ √(α τ_h)', ACC, 13, w=2.4)
    L = np.logspace(-8, -4, 100)
    p2 = Plot(f, 7.4, 1.5, 5.5, 4.0, (1e-8, 1e-4), (1e-9, 1e1), 'distance L_h  (m)', 'diffusion time t_th  (s)', (1e-8, 1e-6, 1e-4), (1e-9, 1e-5, 1e-1), fx='{:.0e}', fy='{:.0e}', xlog=True, ylog=True)
    p2.curve(L, L ** 2 / ALPHA, WARM, 3)
    p2.pt(5e-6, 25e-12 / ALPHA, ACC)
    p2.label(5e-6, 25e-12 / ALPHA, 't_th ≈ 0.53 ms to cross 5 µm', ACC, 12, w=2.6, dx=-2.8, dy=-.5)
    p2.label(2e-8, 1e-6, 't_th ~ L_h²/α', WARM, 13, w=2.4)
    f.text(1.0, 6.27, 12, 'α = k/(ρc_p) = 4.69×10⁻⁸ m²/s for the PFC liquid.  Heat travels a distance δ in a time ~ δ²/α, so doubling δ costs four times as long.', 12.5, FG)
    f.note('Scalings of Eq. C2-E09 evaluated with the PFC liquid properties of Eq. C2-E10.')


def e10(f):
    d = math.sqrt(ALPHA * 1e-8)
    z = np.linspace(0, 6, 300)
    p = Plot(f, 1.0, 1.5, 6.4, 4.0, (0, 6), (0, 1.05), 'depth into the droplet  z  (µm)', 'T − T₀ (relative to surface)', (0, 1, 2, 3, 4, 5, 6), (0, .25, .5, .75, 1), fx='{:g}', fy='{:.2f}')
    from scipy.special import erfc
    for tt, c, lab in [(1e-8, ACC, 't = 10 ns (end of pulse)'), (1e-6, WARM, 't = 1 µs'), (1e-4, PINK, 't = 100 µs')]:
        p.curve(z, erfc(z * 1e-6 / (2 * math.sqrt(ALPHA * tt))), c, 3)
    p.curve(z, np.where(z < .25, 1.0, np.nan) * 0 + np.nan, ACC, 1)
    p.vline(5, MUT)
    p.label(5, .8, 'PFC core\nradius 5 µm', MUT, 12, w=1.5, dx=-1.6, dy=0)
    p.label(.08, .55, 'at 10 ns only the outer\n~22 nm is warm', ACC, 12, w=2.8, dy=-.1)
    p.label(.7, .26, '1 µs: 0.2 µm', WARM, 12, w=1.8)
    p.label(2.5, .62, '100 µs: 2 µm', PINK, 12, w=1.8)
    f.panel(7.7, 1.5, 5.25, 4.0, 'Declared numbers', ACC, size=13.5)
    rows = [('α = 0.050 / (1630 × 654)', '= 4.690×10⁻⁸ m²/s'), ('t_th ~ (5 µm)² / α', '= 5.33×10⁻⁴ s'), ('δ_T ~ √(α × 10 ns)', '= 2.17×10⁻⁸ m')]
    y = 2.0
    for a, b in rows:
        y = f.text(7.85, y, 5.0, a, 12.5, FG)
        y = f.text(8.0, y, 4.9, b, 14, WARM, bold=True) + .15
    f.text(7.85, y + .1, 5.0, 'A 10 ns pulse heats a layer 230 times thinner than the droplet radius. Uniform temperature in a micron-scale core is not implied by a short pulse.', 12, FG)
    f.text(1.0, 6.27, 12, 'Profiles: erfc(z / 2√(αt)), the conduction solution for a surface held at fixed temperature (scale illustration).', 12, MUT)
    f.note('Numbers of Eq. C2-E10; profile shapes use the same α.')


def e11(f):
    a = np.logspace(-7.3, -4.3, 100)
    p = Plot(f, 6.7, 1.5, 6.0, 4.0, (5e-8, 5e-5), (1e3, 1e7), 'core radius a  (m)', '2σ_pc / a  (Pa)', (1e-7, 1e-6, 1e-5), (1e3, 1e4, 1e5, 1e6, 1e7), fx='{:.0e}', fy='{:.0e}', xlog=True, ylog=True)
    p.curve(a, 2 * .02 / a, ACC, 3)
    p.pt(5e-6, 8e3, WARM)
    p.label(5e-6, 8e3, '5 µm: 8 kPa', WARM, 12.5, w=1.9, dx=.12, dy=-.5)
    p.pt(1e-7, 4e5, PINK)
    p.label(1e-7, 4e5, '0.1 µm: 400 kPa', PINK, 12.5, w=2.2, dx=.12, dy=-.1)
    f.panel(.4, 1.0, 5.4, 5.3, 'Smaller inclusion, larger capillary pressure', ACC, size=13)
    f.ellipse(1.9, 3.2, 1.15, fill=LIQ, line=ACC, lw=2.2)
    f.text(1.1, 3.0, 1.6, 'a = 5 µm\n8 kPa', 12.5, FG, 'center', bold=True)
    f.ellipse(4.4, 3.2, .35, fill=LIQ, line=PINK, lw=2.2)
    f.text(3.8, 3.7, 1.4, 'a = 0.1 µm\n400 kPa', 11.5, PINK, 'center', bold=True)
    f.text(.55, 4.55, 5.0, 'p_d ≃ p_c + 2σ_pc/a + Π_shell', 13.5, WARM, bold=True)
    f.text(.55, 5.0, 5.0, 'σ_pc = 0.020 N/m (teaching value); the shell term is added separately.', 12, FG)
    f.text(6.1, 6.27, 6.8, 'Same tension, 50 times smaller radius: capillary pressure 50 times larger (2σ/a is inversely proportional to a).', 12.5, FG)
    f.note('Static capillary control of Eq. C2-E11.')


def e12(f):
    T = np.linspace(282.82, 337.94, 200)
    p = Plot(f, 1.0, 1.5, 7.2, 4.0, (280, 340), (.05, 20), 'temperature T  (K)', 'p_sat,PFP  (bar)', (280, 290, 300, 310, 320, 330, 340), (.1, 1, 10), fx='{:g}', fy='{:g}', ylog=True)
    p.curve(T, psat_pfp(T) / 1e5, ACC, 3)
    p.hline(1.0, MUT)
    Tb = 1103.454 / (4.2063 - 0) + 39.77
    from scipy.optimize import brentq
    Tb = brentq(lambda t: psat_pfp(t) - 1e5, 283, 338)
    p.pt(Tb, 1.0, WARM)
    p.label(Tb, 1.0, f'1 bar at {Tb:.1f} K', WARM, 12.5, w=2.2, dx=.12, dy=.08)
    for Tm, c in [(293.15, BLUE), (323.15, PINK)]:
        v = psat_pfp(Tm) / 1e5
        p.pt(Tm, v, c)
        p.label(Tm, v, f'{Tm:.0f} K: {v:.2f} bar', c, 12, w=2.0, dx=.12, dy=-.45)
    f.panel(8.5, 1.5, 4.45, 4.0, 'What the curve says', ACC, size=13.5)
    f.text(8.65, 2.0, 4.2, 'log₁₀(p/10⁵ Pa) = 4.2063 − 1103.454 K/(T − 39.77 K)', 12.5, FG, bold=True)
    f.bullets(8.65, 2.9, 4.2, ['Valid only for 282.82 K ≤ T ≤ 337.94 K.', 'It gives the equilibrium vapor pressure of bulk liquid.', 'Reaching it does not by itself start a bubble: nucleation is a separate step.'], 12.5)
    f.text(1.0, 6.27, 12, 'At 293 K the saturation pressure is below 1 bar; the liquid is superheated only when the surroundings or the liquid pressure sit below the curve.', 12.5, FG)
    f.note('Empirical PFP correlation of Eq. C2-E12 (log scale).')


FIGS = {1: e01, 2: e02, 3: e03, 4: e04, 5: e05, 6: e06, 7: e07, 8: e08, 9: e09, 10: e10, 11: e11, 12: e12}
