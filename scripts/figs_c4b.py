"""Chapter 4, equations 13-24 (clamped circular delamination benchmark)."""
import math

import numpy as np

from figlib import *

E_F, H_F, NU = 2.0e9, 10e-6, .35
DF = E_F * H_F ** 3 / (12 * (1 - NU ** 2))
B = 100e-6
GAM = 0.10
PCRIT = math.sqrt(128 * DF * GAM) / B ** 2


def _profile(f, x0, y0, w, h, color=ACC):
    s = np.linspace(-1, 1, 80)
    f.path([(x0 + w * (k + 1) / 2, y0 + h * (1 - (1 - k ** 2) ** 2)) for k in s], color, 3)
    f.line(x0 - .2, y0 + h, x0 + w + .2, y0 + h, MUT, 1.4)
    f.line(x0, y0 + h - .3, x0, y0 + h + .3, WARM, 3)
    f.line(x0 + w, y0 + h - .3, x0 + w, y0 + h + .3, WARM, 3)


def e13(f):
    f.panel(.4, 1.0, 6.9, 5.3, 'Clamped circular delamination under p₀', ACC, size=13.5)
    cx, cy = 3.85, 3.25
    f.ellipse(cx, cy, 2.2, 1.0, fill=LIQ, line=ACC, lw=2.2)
    f.line(cx - 2.2, cy, cx + 2.2, cy, MUT, 1.2, dash=True)
    f.dim(cx, cy + 1.25, cx + 2.2, cy + 1.25, 'b', MUT, 12.5)
    for k in (-1.2, 0, 1.2):
        f.line(cx + k, 1.8, cx + k, 2.35, PINK, 3, arrow=True)
    f.text(cx - 1.5, 1.4, 3.0, 'uniform pressure p₀', 12, PINK, 'center', bold=True)
    f.text(.6, 4.9, 6.6, '𝓛_r g = p₀ / D_f,   g = 𝓛_r w,   𝓛_r f = (1/r) d/dr (r df/dr)', 12.5, FG, bold=True)
    f.text(.6, 5.4, 6.6, 'w(b) = 0,  w′(b) = 0 (clamped edge);  fields regular at r = 0', 12.5, WARM, bold=True)
    f.panel(7.5, 1.0, 5.45, 5.3, 'Reading the boundary-value problem', ACC, size=13.5)
    f.bullets(7.65, 1.6, 5.2, ['Axisymmetry: only r matters, the Laplacian 𝓛_r replaces ∇².', 'The biharmonic equation D_f ∇⁴w = p₀ becomes two nested 𝓛_r equations.', 'Four constants must be fixed: two by regularity, two by the clamp.', 'Quasistatic: no inertia, so p₀ is applied slowly (maintained pressure).'], 12.5)
    f.text(7.65, 4.6, 5.2, f'Teaching film: h_f = 10 µm, E_f = 2 GPa, ν = 0.35: D_f = {DF:.4g} N m; b = 100 µm.', 12, MUT)
    f.note('Quasistatic circular-plate boundary-value problem of Eq. C4-E13.')


def e14(f):
    f.text(.5, 1.0, 12.3, 'First pair of integrations: regularity removes C₁', 13.5, ACC, bold=True)
    rows = [('start', 'd/dr (r g′) = p₀ r / D_f', BLUE), ('integrate', 'r g′ = p₀ r² / (2D_f) + C₁', BLUE), ('divide by r', 'g′ = p₀ r / (2D_f) + C₁ / r', WARM), ('regular at r = 0 ⇒ C₁ = 0', 'g′ = p₀ r / (2D_f)', PINK), ('integrate', 'g(r) = p₀ r² / (4D_f) + C₂', ACC)]
    for i, (h, e, c) in enumerate(rows):
        y = 1.55 + i * .72
        f.text(.6, y, 3.1, h, 12, c, bold=True)
        f.text(3.8, y, 5.0, e, 13, FG, bold=True)
    r = np.linspace(.03, 1, 200)
    p = Plot(f, 9.3, 1.6, 3.5, 3.4, (0, 1), (-8, 8), 'r / b', 'C₁ / r  term', (0, .5, 1), (-8, 0, 8), fx='{:g}', fy='{:g}')
    p.curve(r, 1 / r * .5, PINK, 3)
    p.label(.15, 6.5, 'C₁/r diverges', PINK, 11.5, w=2.0, dy=0)
    p.label(.4, -1.5, 'regular: C₁ = 0', ACC, 11.5, w=2.0)
    p.hline(0, ACC, dash=False, width=2.5)
    f.text(.6, 5.35, 12, 'A term C₁/r would make the slope infinite at the centre of a smooth plate; the physical solution cannot contain it.', 12.5, FG)
    f.text(.6, 5.95, 12, 'C₂ is still free: it will be fixed with the clamp conditions in Eq. C4-E16.', 12.5, WARM)
    f.note('Radial integration of Eq. C4-E14; the right plot is the C₁/r term for C₁ = 0.5 (schematic).')


def e15(f):
    f.text(.5, 1.0, 12.3, 'Second pair of integrations: build w(r)', 13.5, ACC, bold=True)
    rows = [('start', 'd/dr (r w′) = r g = p₀ r³ / (4D_f) + C₂ r', BLUE), ('integrate', 'r w′ = p₀ r⁴ / (16D_f) + C₂ r² / 2 + C₃', BLUE), ('C₃ = 0 (regular)', 'w′ = p₀ r³ / (16D_f) + C₂ r / 2', PINK), ('integrate', 'w = p₀ r⁴ / (64D_f) + C₂ r² / 4 + C₄', ACC)]
    for i, (h, e, c) in enumerate(rows):
        y = 1.55 + i * .72
        f.text(.6, y, 3.1, h, 12, c, bold=True)
        f.text(3.8, y, 5.4, e, 12.5, FG, bold=True)
    r = np.linspace(0, 1, 100)
    p = Plot(f, 9.6, 1.5, 3.2, 3.4, (0, 1), (-2.2, 1.7), 'r / b', 'terms of 64D_f w / p₀b⁴', (0, .5, 1), (-2, -1, 0, 1), fx='{:g}', fy='{:g}')
    p.curve(r, r ** 4, ACC, 2.6)
    p.curve(r, -2 * r ** 2, WARM, 2.6)
    p.curve(r, np.ones_like(r), PINK, 2.6)
    p.curve(r, (1 - r ** 2) ** 2, FG, 2.2, dash=True)
    p.label(.5, -.45, 'sum (dashed)', FG, 11, w=1.6, dy=0)
    p.label(.55, -1.7, 'r² term', WARM, 11, w=1.2)
    p.label(.45, 1.45, 'constant C₄', PINK, 11, w=1.5, dy=0)
    p.label(.3, .35, 'r⁴ term', ACC, 11, w=1.2, dy=0)
    f.text(.6, 4.7, 8.6, 'The regular solution has three pieces: quartic (from the load), quadratic and constant (both fixed by the clamp).', 12.5, FG)
    f.text(.6, 5.35, 12, 'Right: the three terms (solid) add up to the final profile (dashed), using the constants found in Eq. C4-E16.', 12, MUT)
    f.note('Radial integration of Eq. C4-E15; pieces drawn for C₂ = −p₀b²/(8D_f) and C₄ = p₀b⁴/(64D_f) (preview of Eq. C4-E16).')


def e16(f):
    r = np.linspace(0, 1, 200)
    p = Plot(f, 1.0, 1.5, 6.2, 3.9, (0, 1), (0, 1.1), 'r / b', 'w(r) / w(0)', (0, .25, .5, .75, 1), (0, .5, 1), fx='{:.2f}', fy='{:.1f}')
    p.curve(r, (1 - r ** 2) ** 2, ACC, 3.4)
    p.pt(0, 1, WARM)
    p.label(0, 1, 'w(0) = p₀b⁴/(64D_f)', WARM, 12, w=2.8, dx=.1, dy=-.15)
    p.pt(1, 0, PINK)
    p.label(.03, .12, 'clamped at r = b: w = w′ = 0', PINK, 12, w=3.0, dy=0)
    f.panel(7.5, 1.5, 5.45, 3.9, 'Fixing C₂ and C₄', ACC, size=13.5)
    f.text(7.65, 2.0, 5.2, 'w′(b) = 0:  C₂ = −p₀b² / (8D_f)', 12.5, FG, bold=True)
    f.text(7.65, 2.6, 5.2, 'w(b) = 0:  C₄ = p₀b⁴ / (64D_f)', 12.5, FG, bold=True)
    f.text(7.65, 3.35, 5.2, 'w(r) = p₀ (b² − r²)² / (64D_f)', 15, WARM, bold=True)
    f.text(7.65, 4.1, 5.2, 'Unique regular solution; the profile is a squared parabola.', 12, MUT)
    f.text(1.0, 6.0, 12, 'Both edge conditions are satisfied exactly; there is no free constant left.', 12.5, FG)
    f.note('Exact solution of Eq. C4-E16, drawn as w/w(0) = (1 − (r/b)²)².')


def e17(f):
    r = np.linspace(0, 1, 200)
    w = (1 - r ** 2) ** 2
    wp = -4 * r * (1 - r ** 2)
    p = Plot(f, 1.0, 1.5, 6.2, 3.9, (0, 1), (-1.6, 1.2), 'r / b', 'w/w(0)  and  w′ b/w(0)', (0, .25, .5, .75, 1), (-1.5, -1, -.5, 0, .5, 1), fx='{:.2f}', fy='{:g}')
    p.curve(r, w, ACC, 3)
    p.curve(r, wp, WARM, 3)
    p.label(.05, .8, 'w', ACC, 13, w=.6, dx=.5)
    p.label(.52, -.45, "w′ = p₀r(r²−b²)\n/(16D_f)", WARM, 11.5, w=1.8, dy=0)
    f.panel(7.5, 1.5, 5.45, 3.9, 'Direct verification', ACC, size=13.5)
    f.text(7.65, 2.0, 5.2, '𝓛_r(r²) = 4,   𝓛_r(r⁴) = 16 r²', 12.5, FG, bold=True)
    f.text(7.65, 2.55, 5.2, '𝓛_r w ∝ −8 + 16 r²,  𝓛_r²w ∝ 64  ⇒  D_f 𝓛_r²w = p₀', 11.5, FG, bold=True)
    f.text(7.65, 3.1, 5.2, 'w′(r) = p₀ r (r² − b²) / (16D_f)', 12.5, WARM, bold=True)
    f.text(7.65, 3.8, 5.2, 'Slope zero at r = 0 and r = b; steepest between.', 12, MUT)
    f.text(1.0, 6.0, 12, 'Differentiating the answer back reproduces the governing equation, so the solution is verified, not assumed.', 12.5, FG)
    f.note('Verification of Eq. C4-E17.')


def e18(f):
    r = np.linspace(0, 1, 300)
    w = (1 - r ** 2) ** 2
    ann = 2 * math.pi * r * w
    p = Plot(f, 1.0, 1.5, 6.2, 3.9, (0, 1), (0, 2.2), 'r / b', 'integrand 2π w r', (0, .25, .5, .75, 1), (0, 1, 2), fx='{:.2f}', fy='{:g}')
    p.fill(r, np.zeros_like(r), ann, ACC, .3)
    p.curve(r, ann, ACC, 3)
    area = float(np.trapezoid(ann, r)) if hasattr(np, 'trapezoid') else float(np.trapz(ann, r))
    p.label(.55, 2.2, f'area = π/3 = {area:.4f}', WARM, 12.5, w=2.8)
    f.panel(7.5, 1.5, 5.45, 3.9, 'Blister volume', ACC, size=13.5)
    f.text(7.65, 2.0, 5.2, 'V_bl = 2π ∫₀ᵇ w r dr', 13, FG, bold=True)
    f.text(7.65, 2.55, 5.2, '= π p₀ / (32D_f) ∫ (b⁴r − 2b²r³ + r⁵) dr', 12, FG, bold=True)
    f.text(7.65, 3.1, 5.2, 'bracket at r = b:  b⁶ (1/2 − 1/2 + 1/6) = b⁶/6', 12, MUT)
    f.text(7.65, 3.7, 5.2, 'V_bl = π p₀ b⁶ / (192 D_f)', 15, WARM, bold=True)
    f.text(1.0, 6.0, 12, 'The volume sums the opening of all concentric annuli; the numerical area under 2π w r reproduces the closed form.', 12.5, FG)
    f.note('Volume integral of Eq. C4-E18 (normalised: w/w(0) = (1 − x²)², x = r/b, area π/3 in units w(0)b²).')


def e19(f):
    V = np.linspace(0, 1, 100)
    p = Plot(f, 1.0, 1.5, 6.2, 3.9, (0, 1), (-1.1, 1.1), 'V_bl / V*', 'energy / (p*V*)', (0, .25, .5, .75, 1), (-1, -.5, 0, .5, 1), fx='{:.2f}', fy='{:g}')
    p.curve(V, V ** 2 / 2, BLUE, 3)
    p.curve(V, -V, PINK, 3)
    p.curve(V, V ** 2 / 2 - V, ACC, 3.4)
    p.seg(0, 0, 1, 0, GRID, 1.2)
    p.label(.1, .85, 'U_b = V²/(2C_b)  (stored)', BLUE, 11.5, w=2.8, dy=0)
    p.label(.08, -.8, '−p₀V  (source work)', PINK, 11.5, w=2.6, dy=0)
    p.pt(1, -.5, WARM)
    p.label(1, -.5, '𝒫 = −p₀V/2', WARM, 12, w=1.8, dx=-1.9, dy=-.3)
    f.panel(7.5, 1.5, 5.45, 3.9, 'Maintained pressure', ACC, size=13.5)
    f.text(7.65, 2.0, 5.2, 'C_b = ∂V_bl/∂p₀ = π b⁶ / (192 D_f),   V_bl = C_b p₀', 11.5, FG, bold=True)
    f.text(7.65, 2.6, 5.2, 'U_b = V_bl² / (2C_b) = p₀V_bl / 2', 12.5, FG, bold=True)
    f.text(7.65, 3.15, 5.2, '𝒫 = U_b − p₀V_bl = −π p₀² b⁶ / (384 D_f)', 12.5, WARM, bold=True)
    f.text(7.65, 3.9, 5.2, 'Half of the source work is stored; the other half is the loss of potential.', 12, MUT)
    f.text(1.0, 6.0, 12, 'With p₀ held fixed the source does work p₀V; the total potential is negative: the system gains energy by opening.', 12.5, FG)
    f.note('Potential under maintained pressure, Eq. C4-E19 (normalised: V* = 1, p* = 1; U_b = V²/2 along the linear compliance).')


def e20(f):
    b = np.linspace(.5, 1.5, 100)
    p = Plot(f, 1.0, 1.5, 6.2, 3.9, (.5, 1.5), (-1.4, 0), 'b / b₀', '𝒫 / 𝒫(b₀)', (.5, .75, 1, 1.25, 1.5), (-1.2, -.8, -.4, 0), fx='{:.2f}', fy='{:.1f}')
    P = -b ** 6
    p.curve(b, P, ACC, 3)
    p.pt(1, -1, WARM)
    p.label(1.12, -.5, 'slope −6𝒫₀/b₀\nat b = b₀', WARM, 11.5, w=2.0, dy=0)
    f.panel(7.5, 1.5, 5.45, 3.9, 'From potential to G', ACC, size=13.5)
    f.text(7.65, 1.95, 5.2, 'A_c = π b²,   dA_c/db = 2π b', 12.5, FG, bold=True)
    f.text(7.65, 2.5, 5.2, '(d𝒫/db)_{p₀} = −6π p₀² b⁵ / (384 D_f)', 12.5, FG, bold=True)
    f.text(7.65, 3.05, 5.2, 'G = −(d𝒫/db) / (dA_c/db)', 12.5, WARM, bold=True)
    f.text(7.65, 3.65, 5.2, 'G_p₀ = p₀² b⁴ / (128 D_f)', 15, WARM, bold=True)
    f.text(7.65, 4.4, 5.2, 'Pressure squared times radius to the fourth.', 12, MUT)
    f.text(1.0, 6.0, 12, '𝒫 ∝ b⁶ falls faster as the blister grows: at fixed pressure each increment of area releases more energy.', 12.5, FG)
    f.note('Energy-release rate of Eq. C4-E20 (curve is −b⁶ normalised, schematic of the b⁶ dependence).')


def e21(f):
    x = np.linspace(0, 2, 100)
    p = Plot(f, 1.0, 1.5, 6.2, 3.9, (0, 2), (0, 4.2), 'p₀ / p₀,crit', 'G / Γ', (0, .5, 1, 1.5, 2), (0, 1, 2, 3, 4), fx='{:.1f}', fy='{:g}')
    p.curve(x, x ** 2, ACC, 3.4)
    p.hline(1, WARM)
    p.vline(1, WARM)
    p.pt(1, 1, WARM)
    p.label(1.05, 1, 'onset: G = Γ', WARM, 12, w=1.8, dx=.2, dy=.45)
    p.label(.1, 3.5, 'G/Γ = (p₀/p₀,crit)²', ACC, 12, w=3.0)
    f.panel(7.5, 1.5, 5.45, 3.9, 'Threshold pressure', ACC, size=13.5)
    f.text(7.65, 2.0, 5.2, 'G_p₀ = Γ  ⇒  p₀,crit = √(128 D_f Γ) / b²', 13, FG, bold=True)
    f.text(7.65, 2.9, 5.2, 'G / Γ = (p₀ / p₀,crit)²', 13, WARM, bold=True)
    f.bullets(7.65, 3.6, 5.2, ['Doubling p₀ quadruples G.', 'A bigger blister (b) lowers the pressure needed as 1/b².'], 12)
    f.text(1.0, 6.0, 12, 'The threshold depends on geometry and fracture resistance, not on pressure alone: a pressure peak without b and Γ says nothing.', 12.5, FG)
    f.note('Onset threshold of Eq. C4-E21.')


def e22(f):
    b = np.linspace(.5, 2, 100)
    p = Plot(f, 1.0, 1.5, 6.2, 3.9, (.5, 2), (.01, 100), 'b / b₀', 'G / G(b₀)', (.5, 1, 1.5, 2), (.01, .1, 1, 10, 100), fx='{:g}', fy='{:g}', ylog=True)
    p.curve(b, b ** 4, WARM, 3.2)
    p.curve(b, b ** -8, PINK, 3.2)
    p.hline(1, MUT)
    p.label(1.1, 40, 'fixed pressure: G ∝ b⁴ (grows: unstable)', WARM, 11.5, w=3.6, dy=0)
    p.label(.52, .03, 'fixed volume: G ∝ b⁻⁸ (falls: stable)', PINK, 11.5, w=3.4, dy=0)
    f.panel(7.5, 1.5, 5.45, 3.9, 'Same plate, two load controls', ACC, size=13.5)
    f.text(7.65, 1.95, 5.2, 'U_b|V̄ = V̄² / (2C_b) = 96 D_f V̄² / (π b⁶)', 11.5, FG, bold=True)
    f.text(7.65, 2.5, 5.2, 'p(b) = 192 D_f V̄ / (π b⁶)', 12.5, FG, bold=True)
    f.text(7.65, 3.05, 5.2, 'G_V̄ = 288 D_f V̄² / (π² b⁸) = p(b)² b⁴ / (128 D_f)', 11.5, WARM, bold=True)
    f.text(7.65, 3.8, 5.2, 'Same formula in p, but p itself falls as b⁻⁶ at fixed volume.', 12, MUT)
    f.text(1.0, 6.0, 12, 'A maintained pressure source lets the crack run away; a fixed liquid volume arrests it. Always state the control.', 12.5, FG)
    f.note('Loading-control comparison of Eq. C4-E22.')


def e23(f):
    f.text(.5, 1.0, 12.3, 'Teaching calculation, step by step', 13.5, ACC, bold=True)
    cards = [('plate stiffness', 'D_f = E_f h_f³ / [12(1 − ν²)]', 'E_f = 2.00 GPa, h_f = 10.0 µm, ν = 0.35', f'D_f = {DF:.6e} N m', BLUE), ('critical pressure', 'p₀,crit = √(128 D_f Γ) / b²', 'Γ = 0.10 J/m², b = 100 µm', f'p₀,crit = {PCRIT / 1e3:.3f} kPa', WARM)]
    for i, (h, e, i2, v, c) in enumerate(cards):
        x = .5 + i * 6.25
        f.panel(x, 1.5, 6.05, 2.4, h, c, size=13.5)
        f.text(x + .15, 2.0, 5.8, e, 13, FG, bold=True)
        f.text(x + .15, 2.55, 5.8, i2, 12, MUT)
        f.text(x + .15, 3.1, 5.8, v, 15, c, bold=True)
    f.chain([('inputs', 'E_f, h_f, ν, Γ, b'), ('D_f', f'{DF:.3e} N m'), ('√(128 D_f Γ)', f'{math.sqrt(128 * DF * GAM):.4e}'), ('÷ b²', f'{PCRIT / 1e3:.2f} kPa')], 4.3, h=1.1, gap=.5, colors=[MUT, BLUE, PINK, WARM], size=12.5)
    f.text(.5, 5.7, 12.3, 'The 156 kPa threshold is conditional: it holds for this plate, this interface energy and this geometry, with pressure maintained.', 13, WARM)
    f.text(.5, 6.3, 12.3, 'It is far below the 47 MPa early-contact scale of Chapter 3, but the pulse lasts only nanoseconds.', 12.5, FG)
    f.note('Checked substitution of Eq. C4-E23 (all inputs are declared teaching values).')


def e24(f):
    w0 = PCRIT * B ** 4 / (64 * DF)
    V = math.pi * PCRIT * B ** 6 / (192 * DF)
    Mr = PCRIT * B ** 2 / 8
    sig = 6 * Mr / H_F ** 2
    f.text(.5, 1.0, 12.3, 'Three checks on the 156 kPa threshold', 13.5, ACC, bold=True)
    f.panel(.5, 1.5, 4.0, 3.8, 'Deflection', ACC, size=13.5)
    f.path([(.8 + 3.4 * (k + 1) / 2, 2.4 + 1.2 * (1 - (1 - k * k) ** 2)) for k in np.linspace(-1, 1, 60)], ACC, 3)
    f.text(.7, 3.7, 3.6, f'w(0) = {w0 * 1e6:.4f} µm', 13, FG, 'center', bold=True)
    f.text(.7, 4.2, 3.6, f'w(0)/h_f = {w0 / H_F:.5f}', 13, WARM, 'center', bold=True)
    f.text(.7, 4.7, 3.6, 'small-deflection theory needs w ≪ h_f', 11.5, MUT, 'center')
    f.panel(4.7, 1.5, 4.0, 3.8, 'Blister volume', WARM, size=13.5)
    f.text(4.9, 2.2, 3.6, f'V_bl = {V:.5e} m³', 13, FG, 'center', bold=True)
    f.text(4.9, 2.9, 3.6, '= 13.4 pL (about 13 400 µm³)', 12, MUT, 'center')
    f.text(4.9, 3.7, 3.6, 'the liquid volume needed to inflate the blister', 11.5, MUT, 'center')
    f.panel(8.9, 1.5, 4.05, 3.8, 'Edge bending stress', PINK, size=13.5)
    f.text(9.05, 2.0, 3.8, '|M_r(b)| = p₀,crit b² / 8', 12.5, FG, 'center', bold=True)
    f.text(9.05, 2.7, 3.8, f'|σ_rr|_edge = 6|M_r|/h_f² = {sig / 1e6:.4f} MPa', 12, WARM, 'center', bold=True)
    f.text(9.05, 3.6, 3.8, 'a tensile stress at the clamp: compare with the payload strength', 11.5, MUT, 'center')
    f.text(.5, 5.7, 12.3, f'Deflection is only {w0 / H_F * 100:.1f} % of the thickness, so linear theory holds; edge bending stress of {sig / 1e6:.1f} MPa must still be checked against the payload material.', 12.5, FG)
    f.text(.5, 6.35, 12.3, 'The payload strength is an input that must be supplied; no value is assumed here.', 12, MUT)
    f.note('Checks of Eq. C4-E24 at p₀ = p₀,crit.')


FIGS = {13: e13, 14: e14, 15: e15, 16: e16, 17: e17, 18: e18, 19: e19, 20: e20, 21: e21, 22: e22, 23: e23, 24: e24}
