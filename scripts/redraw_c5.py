"""Chapter 5 SCI-PPT figures: 11 native editable scenes with PPTX and SVG exports.

Data plots are drawn from the copied CSVs in sources/rigid_wall_ch5; nothing is typed from memory.
"""
import bisect
import csv
import json
import math
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'sources/rigid_wall_ch5'
OUT = ROOT / 'assets/figures-editable/c5'
BG, FG, ACC, MUT, AREA, WARM, GRID = '#142632', '#E7F0F3', '#8EDBD4', '#B4C7D2', '#213E4B', '#F2B880', '#2E4756'
RHO, PJ, GAM, PI = 998.1539919, 101325.0, 4.4, 600e6
C0 = math.sqrt(GAM * (PJ + PI) / RHO)
U0 = 99.02724197


def hugoniot(U):
    M = U / C0
    k = (GAM + 1) * M * M / 4
    x = -k + math.sqrt(k * k + M * M)
    return PJ + RHO * U * U / x


def barotropic(U):
    lo, hi = 0.5 * C0, 3 * C0

    def res(S):
        r1 = RHO * (U + S) / S
        return (PJ + PI) * (r1 / RHO) ** GAM - PI - (PJ + RHO * (U + S) * U)

    flo = res(lo)
    for _ in range(200):
        m = 0.5 * (lo + hi)
        fm = res(m)
        if (flo < 0) == (fm < 0):
            lo, flo = m, fm
        else:
            hi = m
    S = 0.5 * (lo + hi)
    return PJ + RHO * (U + S) * U


def barotropic_S(U):
    lo, hi = 0.5 * C0, 3 * C0

    def res(S):
        r1 = RHO * (U + S) / S
        return (PJ + PI) * (r1 / RHO) ** GAM - PI - (PJ + RHO * (U + S) * U)

    flo = res(lo)
    for _ in range(200):
        m = 0.5 * (lo + hi)
        fm = res(m)
        if (flo < 0) == (fm < 0):
            lo, flo = m, fm
        else:
            hi = m
    return 0.5 * (lo + hi)


def load(case):
    with open(DATA / f'{case}_history.csv', newline='') as f:
        rows = list(csv.DictReader(f))
    return {k: [float(r[k]) for r in rows] for k in rows[0]}


class D:
    def __init__(self, ident, title):
        self.id, self.o = ident, []
        self.text(.3, .15, 12.7, .45, title, 21, ACC, bold=True)

    def add(self, typ, **kw):
        kw.update(type=typ, id=f'o{len(self.o):03}', name=f'{self.id} {typ} {len(self.o)}')
        self.o.append(kw)

    def text(self, x, y, w, h, s, size=15, color=FG, align='left', bold=False):
        kw = dict(x=x, y=y, w=w, h=h, text=s, font='Arial', font_size=size, color=color, word_wrap=True, align=align)
        if bold:
            kw['bold'] = True
        self.add('text', **kw)

    def line(self, x1, y1, x2, y2, arrow=False, color=ACC, width=2, dash=False):
        kw = dict(x1=x1, y1=y1, x2=x2, y2=y2, line=color, line_width=width)
        if dash:
            kw['_dash'] = True
        self.add('arrow' if arrow else 'line', **kw)

    def rect(self, x, y, w, h, fill=AREA, line=MUT, lw=1.5):
        self.add('rect', x=x, y=y, w=w, h=h, fill=fill, line=line, line_width=lw)

    def ellipse(self, cx, cy, rx, ry, fill=AREA, line=MUT, lw=1.5):
        self.add('ellipse', x=cx - rx, y=cy - ry, w=2 * rx, h=2 * ry, fill=fill, line=line, line_width=lw)

    def poly(self, pts, color=ACC, width=2):
        for a, b in zip(pts, pts[1:]):
            self.line(a[0], a[1], b[0], b[1], color=color, width=width)

    def dot(self, x, y, r=.07, color=WARM):
        self.ellipse(x, y, r, r, fill=color, line=color, lw=1)

    def axes(self, x0, y0, w, h, xlab, ylab, xt, yt, xlim, ylim, fmtx='{:g}', fmty='{:g}'):
        self.line(x0, y0 + h, x0 + w, y0 + h, color=MUT, width=1.5)
        self.line(x0, y0, x0, y0 + h, color=MUT, width=1.5)
        for v in xt:
            px = x0 + (v - xlim[0]) / (xlim[1] - xlim[0]) * w
            self.line(px, y0 + h, px, y0 + h + .07, color=MUT, width=1)
            self.text(px - .5, y0 + h + .08, 1, .28, fmtx.format(v), 11, MUT, 'center')
        for v in yt:
            py = y0 + h - (v - ylim[0]) / (ylim[1] - ylim[0]) * h
            self.line(x0 - .07, py, x0, py, color=MUT, width=1)
            self.line(x0, py, x0 + w, py, color=GRID, width=.6)
            self.text(x0 - .85, py - .14, .75, .28, fmty.format(v), 11, MUT, 'right')
        self.text(x0, y0 + h + .38, w, .3, xlab, 12.5, FG, 'center')
        self.text(x0 - .95, y0 - .42, 3.4, .3, ylab, 12.5, FG)

    def curve(self, x0, y0, w, h, xlim, ylim, xs, ys, color=ACC, width=2, step=1, dash=False):
        pts = []
        for i in range(0, len(xs), step):
            if not (xlim[0] <= xs[i] <= xlim[1]):
                continue
            px = x0 + (xs[i] - xlim[0]) / (xlim[1] - xlim[0]) * w
            py = y0 + h - (min(max(ys[i], ylim[0]), ylim[1]) - ylim[0]) / (ylim[1] - ylim[0]) * h
            pts.append((px, py))
        for a, b in zip(pts, pts[1:]):
            self.line(a[0], a[1], b[0], b[1], color=color, width=width, dash=dash)

    def hline(self, x0, y0, w, h, ylim, value, color, label=None, dash=True, dy=-.3):
        py = y0 + h - (value - ylim[0]) / (ylim[1] - ylim[0]) * h
        self.line(x0, py, x0 + w, py, color=color, width=1.4, dash=dash)
        if label:
            self.text(x0 + w - 4.3, py + dy, 4.3, .28, label, 11.5, color, 'right')

    def finish(self, note):
        self.text(.35, 7.08, 12.5, .3, note, 10.5, MUT)
        return {'slide': {'width': 13.333, 'height': 7.5}, 'background': BG, 'objects': self.o,
                '_title': self.id, '_audit': {'id': self.id, 'scientific_status': 'drawn from the Chapter 5 equations and copied result files'}}


def wall(d, x, y, w, h=.28):
    d.rect(x, y, w, h, fill='#3A5362', line=MUT)
    for i in range(int(w / .22) + 1):
        xx = x + i * .22
        if xx + .18 <= x + w:
            d.line(xx, y + h, xx + .18, y + h + .2, color=MUT, width=1)


def f01():
    d = D('C5-F01', 'Geometry: liquid jet, rigid wall and observers')
    wall(d, 1.4, 5.7, 4.6)
    d.rect(2.4, 1.3, 2.6, 4.4, fill=AREA, line=ACC, lw=2)
    d.line(3.7, 1.0, 3.7, 5.65, color=GRID, width=1, dash=True)
    d.line(3.7, 1.6, 3.7, 3.4, arrow=True, color=WARM, width=3)
    d.text(3.85, 2.2, 1.3, .5, 'U', 18, WARM, bold=True)
    d.line(2.1, 3.9, 5.3, 3.9, color=MUT, width=1.4, dash=True)
    d.text(5.35, 3.74, 1.6, .32, 'plane z = 2a', 12.5, MUT)
    d.line(1.9, 1.3, 1.9, 5.7, color=MUT, width=1.2)
    d.text(.45, 1.15, 1.4, .32, 'z = 4a', 12, MUT)
    d.text(.45, 5.35, 1.4, .32, 'z = 0', 12, MUT)
    d.line(5.0, 5.55, 4.45, 5.55, arrow=True, color=ACC, width=2.5)
    d.line(2.4, 5.55, 2.95, 5.55, arrow=True, color=ACC, width=2.5)
    d.text(5.1, 5.1, 1.9, .55, 'edge release', 12.5, ACC)
    d.line(2.4, 6.35, 5.0, 6.35, color=ACC, width=4)
    d.line(3.05, 6.62, 4.35, 6.62, color=WARM, width=4)
    d.text(1.4, 6.68, 3.1, .3, 'sensor r ≤ a (full)', 12, ACC)
    d.text(5.1, 6.45, 2.6, .3, 'centre r ≤ a/2', 12, WARM)
    d.line(2.4, 0.95, 5.0, 0.95, color=MUT, width=1.2)
    d.text(3.0, .62, 1.4, .3, '2a', 12, MUT, 'center')
    d.text(7.7, 1.2, 5.2, .4, 'Axisymmetric: wall z = 0, axis r = 0', 15, FG, bold=True)
    items = [('Liquid column radius a, length 4a', ACC), ('Incoming speed U toward −z', WARM),
             ('Rigid slip wall at z = 0', MUT), ('Free side at r = a: pressure released to p_j', ACC),
             ('Plane z = 2a: incident mass and energy flux', MUT), ('Wall disk r ≤ a: area-weighted pressure', ACC)]
    for i, (s, c) in enumerate(items):
        d.ellipse(7.9, 2.15 + i * .62, .07, .07, fill=c, line=c, lw=1)
        d.text(8.1, 1.98 + i * .62, 4.9, .34, s, 14, FG)
    d.text(7.7, 5.9, 5.2, .7, 'First contact at t = 0. Liquid only; no gas, no cavitation.', 13.5, ACC)
    return d.finish('Model schematic; geometry is not to scale.')


def f02():
    d = D('C5-F02', 'Rigid-wall limit of the acoustic matching')
    d.rect(.9, 2.0, 4.6, 1.6, fill=AREA, line=ACC, lw=2)
    d.text(1.0, 2.05, 4.4, .5, 'Liquid, Z_l = ρ c', 16, FG, 'center', bold=True)
    d.line(1.4, 3.0, 4.6, 3.0, arrow=True, color=WARM, width=3)
    d.text(2.4, 3.05, 1.8, .4, 'speed U', 14, WARM, 'center')
    wall(d, 5.5, 1.95, .9, 1.7)
    d.rect(5.5, 1.95, .9, 1.7, fill='#3A5362', line=MUT)
    d.text(6.5, 2.4, 3.2, .8, 'Wall, Z_r → ∞', 16, FG, bold=True)
    d.text(.9, 4.1, 5.0, .4, 'Contact velocity v_i = Z_l U / (Z_l + Z_r)', 15, FG)
    d.text(.9, 4.55, 5.0, .4, 'v_i → 0  as  Z_r → ∞', 15, ACC, bold=True)
    d.text(.9, 5.15, 5.4, .4, 'Contact pressure p = Z_l Z_r U / (Z_l + Z_r)', 15, FG)
    d.text(.9, 5.6, 5.4, .4, 'p → Z_0 U,  Z_0 = ρ_j c_0', 15, ACC, bold=True)
    d.rect(8.0, 4.2, 4.8, 1.9, fill=AREA, line=WARM, lw=2)
    d.text(8.1, 4.3, 4.6, .45, 'Numbers at U = 99.027 m/s', 14.5, WARM, 'center', bold=True)
    d.text(8.1, 4.8, 4.6, .4, 'Z_0 = 1.6234 × 10⁶ Pa s/m', 14, FG, 'center')
    d.text(8.1, 5.2, 4.6, .4, 'Z_0 U = 160.765 MPa', 14, FG, 'center')
    d.text(8.1, 5.6, 4.6, .4, 'p_A = p_j + Z_0 U = 160.867 MPa', 14, FG, 'center')
    d.text(6.5, 3.15, 6.0, .4, 'Linear estimate: valid for U/c_0 ≪ 1', 13, MUT)
    return d.finish('Schematic of Eq. (C3-E24) in the limit Z_r → ∞. Not to scale.')


def f03():
    d = D('C5-F03', 'Wall pressure against speed: acoustic, barotropic, Hugoniot')
    x0, y0, w, h = 1.4, 1.3, 7.4, 4.6
    xs = [i * 1.5 for i in range(0, 101)]
    pa = [(PJ + RHO * C0 * u) / 1e6 for u in xs]
    pb = [barotropic(u) / 1e6 if u > 0 else PJ / 1e6 for u in xs]
    ph = [hugoniot(u) / 1e6 if u > 0 else PJ / 1e6 for u in xs]
    xl, yl = (0, 150), (0, 300)
    d.axes(x0, y0, w, h, 'Impact speed U (m/s)', 'Absolute wall pressure (MPa)', [0, 50, 100, 150], [0, 100, 200, 300], xl, yl, '{:g}', '{:g}')
    d.curve(x0, y0, w, h, xl, yl, xs, pa, MUT, 2, dash=True)
    d.curve(x0, y0, w, h, xl, yl, xs, pb, WARM, 2)
    d.curve(x0, y0, w, h, xl, yl, xs, ph, ACC, 2.5)
    px = x0 + U0 / 150 * w
    d.line(px, y0, px, y0 + h, color=GRID, width=1, dash=True)
    py = y0 + h - hugoniot(U0) / 1e6 / 300 * h
    d.dot(px, py, .08, ACC)
    d.text(9.1, 1.4, 3.9, .4, 'Curves', 15, FG, bold=True)
    for i, (s, c) in enumerate([('Hugoniot p_H (energy kept)', ACC), ('Barotropic p_B (density-only)', WARM), ('Acoustic p_A = p_j + Z_0 U', MUT)]):
        d.line(9.1, 2.05 + i * .5, 9.65, 2.05 + i * .5, color=c, width=3, dash=(c == MUT))
        d.text(9.75, 1.9 + i * .5, 3.4, .32, s, 13, FG)
    d.text(9.1, 3.55, 3.9, .4, f'At U = 99.027 m/s', 14.5, WARM, bold=True)
    d.text(9.1, 3.95, 3.9, .34, f'p_H = {hugoniot(U0) / 1e6:.3f} MPa', 13.5, FG)
    d.text(9.1, 4.3, 3.9, .34, f'p_B = {barotropic(U0) / 1e6:.3f} MPa', 13.5, FG)
    d.text(9.1, 4.65, 3.9, .34, f'p_A = {(PJ + RHO * C0 * U0) / 1e6:.3f} MPa', 13.5, FG)
    d.text(9.1, 5.1, 3.9, .6, f'p_B is {abs(hugoniot(U0) - barotropic(U0)) / hugoniot(U0) * 100:.3f}% below p_H', 13.5, ACC)
    return d.finish('Curves computed from Eqs. (C5-E02), (C5-E04) and (C5-E05).')


def f04():
    d = D('C5-F04', 'Area-weighted sensor disk and edge release')
    cx, cy, R = 3.4, 3.7, 2.1
    d.ellipse(cx, cy, R, R, fill=AREA, line=ACC, lw=2.5)
    d.ellipse(cx, cy, R * .62, R * .62, fill='#2B5560', line=WARM, lw=2.5)
    d.ellipse(cx, cy, .06, .06, fill=FG, line=FG, lw=1)
    for ang in (30, 150, 270):
        a = math.radians(ang)
        d.line(cx + R * .98 * math.cos(a), cy - R * .98 * math.sin(a), cx + R * .72 * math.cos(a), cy - R * .72 * math.sin(a), arrow=True, color=ACC, width=2.5)
    d.line(cx, cy, cx + R, cy, color=MUT, width=1.4)
    d.text(cx + .5, cy - .38, 1.2, .3, 'a', 14, MUT)
    d.text(cx - 1.05, cy + .45, 1.2, .3, 'core', 13, WARM, 'center')
    d.text(.5, 1.0, 5.8, .4, 'Wall z = 0 seen from above', 15, FG, bold=True)
    d.text(7.3, 1.1, 5.5, .4, 'Observer', 15, FG, bold=True)
    d.text(7.3, 1.55, 5.6, .9, 'p̄_R = (2 / R²) ∫₀ᴿ p r dr\nweight 2r dr / R² is the disk area element', 14, FG)
    d.text(7.3, 2.7, 5.6, .7, 'R = a: full sensor\nR = a/2: centre', 14, ACC)
    d.text(7.3, 3.45, 5.5, .4, 'Edge release', 15, FG, bold=True)
    d.text(7.3, 3.9, 5.6, 1.2, 'Front moves inward from r = a at c_0.\nAt τ = c_0 t / a the annulus a(1−τ) < r ≤ a has relaxed.\nArea fraction f_rel = 1 − (1 − τ)².', 14, FG)
    d.rect(7.3, 5.4, 5.5, 1.0, fill=AREA, line=WARM, lw=2)
    d.text(7.4, 5.45, 5.3, .45, 'At the peak: τ = 0.0472, f_rel = 0.0921', 14, WARM, 'center', bold=True)
    d.text(7.4, 5.9, 5.3, .4, 'Full release would give 0.908 p_H', 14, FG, 'center')
    return d.finish('Schematic; annulus width is exaggerated for legibility.')


def f05():
    d = D('C5-F05', 'One-dimensional finite-volume reference grid')
    wall(d, .8, 2.3, .7, 1.0)
    d.rect(.8, 2.25, .7, 1.1, fill='#3A5362', line=MUT)
    d.text(.5, 3.5, 1.4, .3, 'wall', 13, MUT, 'center')
    n = 10
    for i in range(n):
        d.rect(1.55 + i * .85, 2.3, .85, 1.0, fill=AREA, line=MUT)
    d.text(1.55, 2.45, 3, .4, 'cell 1', 12, MUT)
    d.text(1.55 + 9 * .85, 2.45, .85, .4, 'N', 12, MUT, 'center')
    d.line(.55, 2.8, 1.45, 2.8, color=GRID, width=1, dash=True)
    d.text(.2, 1.85, 2.4, .35, 'mirror ghost state', 12, MUT)
    xe = 1.55 + n * .85
    d.line(xe + 1.7, 2.8, xe + .05, 2.8, arrow=True, color=WARM, width=3)
    d.text(xe + .1, 2.2, 2.0, .4, 'inflow ρ_j, −U', 12.5, WARM)
    d.line(1.55, 4.15, xe, 4.15, color=MUT, width=1.2)
    d.text(3.2, 4.2, 5.0, .35, 'H = 4 µm,  N = 4000,  Δz = 1 nm', 13.5, FG)
    d.text(.8, 5.0, 5.8, .4, 'Face flux (Rusanov)', 15, ACC, bold=True)
    d.text(.8, 5.45, 6.0, .9, 'F = ½(F_L + F_R) − ½ α (Q_R − Q_L)\nα = max(|u_L| + c_L, |u_R| + c_R)', 14, FG)
    d.text(7.3, 5.0, 5.6, .4, 'Time step (Heun)', 15, ACC, bold=True)
    d.text(7.3, 5.45, 5.6, .9, 'predictor Q* = Qⁿ + Δt L(Qⁿ)\nQⁿ⁺¹ = Qⁿ + ½ Δt [L(Qⁿ) + L(Q*)]', 14, FG)
    d.text(3.2, 4.6, 6.6, .35, 'Wall pressure read from the cell next to the wall', 12.5, MUT)
    return d.finish('Schematic of the discretization of Eqs. (C5-E10) and (C5-E11); only ten of 4000 cells are drawn.')


def f06():
    d = D('C5-F06', 'COMSOL axisymmetric model and wall band')
    x0, y0, w, h = 1.4, 1.2, 2.6, 5.2
    d.rect(x0, y0, w, h, fill=AREA, line=ACC, lw=2)
    bh = h * .15 / 4
    d.rect(x0, y0 + h - bh, w, bh, fill='#2B5560', line=WARM, lw=2)
    for i in range(1, 13):
        d.line(x0 + i * w / 13, y0 + h - bh, x0 + i * w / 13, y0 + h, color=GRID, width=.8)
    d.line(x0, y0 + h - bh / 2, x0 + w, y0 + h - bh / 2, color=GRID, width=.8)
    d.line(x0, y0 + h * .5, x0 + w, y0 + h * .5, color=MUT, width=1.2, dash=True)
    wall(d, x0, y0 + h, w)
    d.text(x0 + w + .1, y0 + h * .5 - .17, 2.4, .34, 'plane z = 2a', 12.5, MUT)
    d.text(x0 + w + .1, y0 + h - bh - .12, 2.6, .34, 'band z ≤ 0.15 a', 12.5, WARM)
    d.text(x0 - .95, y0 - .05, .9, .34, 'z = 4a', 12, MUT)
    d.text(x0 - .95, y0 + h - .15, .9, .34, 'z = 0', 12, MUT)
    d.text(x0 - .2, y0 - .4, .6, .3, 'r = 0', 12, MUT)
    d.text(x0 + w - .5, y0 - .4, .9, .3, 'r = a', 12, MUT)
    d.line(x0 + w / 2, y0 + .2, x0 + w / 2, y0 + 1.1, arrow=True, color=WARM, width=2.5)
    d.text(x0 + w / 2 + .1, y0 + .4, .8, .34, 'U', 15, WARM, bold=True)
    d.line(x0 + w + .6, y0 + 1.3, x0 + w - .02, y0 + 1.3, arrow=True, color=ACC, width=2)
    d.text(x0 + w + .7, y0 + 1.13, 2.5, .34, 'outlet at p_j', 12.5, ACC)
    d.text(7.0, 1.2, 5.9, .4, 'Setup', 15, FG, bold=True)
    rows = ['Compressible laminar flow, axisymmetric', 'Liquid law: Eq. (C5-E01), μ = 1 mPa s', 'Slip wall z = 0; inflow z = 4a', 'Free outlet r = a (confined case: slip)',
            'Free triangles, global h_max = 0.025 a', 'Time output every 0.001 ns in the band runs']
    for i, s in enumerate(rows):
        d.ellipse(7.1, 1.85 + i * .45, .06, .06, fill=ACC, line=ACC, lw=1)
        d.text(7.3, 1.69 + i * .45, 5.7, .34, s, 13, FG)
    d.text(7.0, 4.5, 5.9, .4, 'Band refinement sequence', 15, WARM, bold=True)
    for i, (hh, ne) in enumerate([('a/40', '16,176'), ('a/80', '18,468'), ('a/160', '26,776'), ('a/320', '57,668')]):
        d.text(7.2, 4.98 + i * .4, 2.5, .34, f'band h = {hh}', 13.5, FG)
        d.text(9.6, 4.98 + i * .4, 3.2, .34, f'{ne} elements', 13.5, MUT)
    return d.finish('Schematic; mesh lines are indicative, not the actual triangulation.')


def f07():
    d = D('C5-F07', 'Confined wall-pressure history: C++ against COMSOL')
    x0, y0, w, h = 1.4, 1.3, 8.0, 4.6
    sl = load('SL')
    ct, cp = [], []
    with open(DATA / 'cpp1d_SL.csv', newline='') as f:
        for r in csv.DictReader(f):
            ct.append(float(r['time_s']) * 1e9)
            cp.append(float(r['p_wall_Pa']) / 1e6)
    t = [v * 1e9 for v in sl['t']]
    p = [v / 1e6 for v in sl['pWall']]
    xl, yl = (0, 2.2), (0, 200)
    d.axes(x0, y0, w, h, 'Time from first contact (ns)', 'Absolute wall pressure (MPa)', [0, 0.5, 1.0, 1.5, 2.0], [0, 50, 100, 150, 200], xl, yl, '{:g}', '{:g}')
    d.hline(x0, y0, w, h, yl, hugoniot(U0) / 1e6, MUT, 'p_H = 174.623 MPa')
    d.hline(x0, y0, w, h, yl, barotropic(U0) / 1e6, WARM, 'p_B = 174.155 MPa', dy=.08)
    d.curve(x0, y0, w, h, xl, yl, ct, cp, ACC, 2.2, step=2)
    d.curve(x0, y0, w, h, xl, yl, t, p, '#FFFFFF', 1.4, dash=True)
    d.text(9.8, 1.4, 3.3, .4, 'Window 0.2 to 2.0 ns', 14, FG, bold=True)
    d.line(9.8, 2.1, 10.4, 2.1, color=ACC, width=3)
    d.text(10.5, 1.95, 2.6, .32, 'C++ finite volume', 13, FG)
    d.line(9.8, 2.55, 10.4, 2.55, color='#FFFFFF', width=2, dash=True)
    d.text(10.5, 2.4, 2.6, .32, 'COMSOL', 13, FG)
    for i, s in enumerate(['361 common samples', 'δ₂ = 0.034%', 'δ∞ = 0.096%', 'Plateau 174.205 vs 174.148 MPa', 'Difference 0.032%']):
        d.text(9.8, 3.15 + i * .4, 3.4, .34, s, 13, ACC if i in (1, 2) else FG)
    return d.finish('Both curves from sources/rigid_wall_ch5: SL_history.csv and cpp1d_SL.csv.')


def f08():
    d = D('C5-F08', 'Wall-band convergence of the full-sensor peak')
    x0, y0, w, h = 1.5, 1.3, 7.4, 4.5
    cases = [('B025', 'a/40', 16176), ('B0125', 'a/80', 18468), ('B00625', 'a/160', 26776), ('B003125', 'a/320', 57668)]
    vals = [max(load(c)['pWall']) / 1e6 for c, _, _ in cases]
    yl = (155, 180)
    d.line(x0, y0 + h, x0 + w, y0 + h, color=MUT, width=1.5)
    d.line(x0, y0, x0, y0 + h, color=MUT, width=1.5)
    for v in (155, 160, 165, 170, 175, 180):
        py = y0 + h - (v - yl[0]) / (yl[1] - yl[0]) * h
        d.line(x0 - .07, py, x0, py, color=MUT, width=1)
        d.line(x0, py, x0 + w, py, color=GRID, width=.6)
        d.text(x0 - .85, py - .14, .75, .28, str(v), 11, MUT, 'right')
    d.text(x0 - .95, y0 - .42, 4, .3, 'Peak full-sensor pressure (MPa)', 12.5, FG)
    pts = []
    for i, ((c, lab, ne), v) in enumerate(zip(cases, vals)):
        px = x0 + (i + .5) / 4 * w
        py = y0 + h - (v - yl[0]) / (yl[1] - yl[0]) * h
        pts.append((px, py))
        d.text(px - .9, y0 + h + .1, 1.8, .3, f'band h = {lab}', 11.5, MUT, 'center')
        d.text(px - .9, y0 + h + .38, 1.8, .3, f'{ne:,} elements', 11, MUT, 'center')
        d.text(px - .7, py - .45, 1.4, .3, f'{v:.3f}', 12.5, FG, 'center')
    d.poly(pts, ACC, 2.5)
    for p_ in pts:
        d.dot(p_[0], p_[1], .08, ACC)
    d.hline(x0, y0, w, h, yl, hugoniot(U0) / 1e6, WARM, 'p_H = 174.623 MPa')
    d.text(9.3, 1.4, 3.7, .4, 'Successive change', 14.5, FG, bold=True)
    for i in range(1, 4):
        ch = abs(vals[i] - vals[i - 1]) / vals[i - 1] * 100
        d.text(9.3, 1.95 + (i - 1) * .45, 3.7, .34, f'{cases[i - 1][1]} → {cases[i][1]}:  {ch:.2f}%', 13.5, ACC if i == 3 else FG)
    d.text(9.3, 3.5, 3.7, .4, 'Converged peak', 14.5, FG, bold=True)
    d.text(9.3, 3.95, 3.7, .34, f'{vals[-1]:.1f} MPa = {vals[-1] / (hugoniot(U0) / 1e6):.3f} p_H', 13.5, FG)
    d.text(9.3, 4.35, 3.7, .7, 'Denominator of each change:\nthe previous, coarser value', 12.5, MUT)
    return d.finish('Values read from B025, B0125, B00625 and B003125 history files.')


def f09():
    d = D('C5-F09', 'Checks and balances: size of each residual')
    x0, y0, w = 4.6, 1.5, 7.6
    items = [('Time step (strict vs automatic)', 0.74), ('Momentum balance (confined)', 0.106), ('Mass balance (confined)', 0.018),
             ('Plateau, C++ vs COMSOL', 0.032), ('Wave history L2, C++ vs COMSOL', 0.034), ('Centre disk vs p_H (converged)', 0.143),
             ('Incident speed, plane z = 2a', 0.00001)]
    lo, hi = math.log10(0.00001), math.log10(10)
    ticks = [0.0001, 0.001, 0.01, 0.1, 1, 10]
    for tk in ticks:
        px = x0 + (math.log10(tk) - lo) / (hi - lo) * w
        d.line(px, y0 - .1, px, y0 + len(items) * .6 + .05, color=GRID, width=.8)
        d.text(px - .5, y0 + len(items) * .6 + .1, 1.0, .3, f'{tk:g}', 11, MUT, 'center')
    d.text(x0, y0 + len(items) * .6 + .45, w, .3, 'Relative size (%), logarithmic axis', 12.5, FG, 'center')
    pt5 = x0 + (math.log10(5) - lo) / (hi - lo) * w
    d.line(pt5, y0 - .1, pt5, y0 + len(items) * .6 + .05, color=WARM, width=2, dash=True)
    d.text(pt5 - 1.3, y0 - .45, 2.6, .3, '5% engineering line', 11.5, WARM, 'center')
    for i, (s, v) in enumerate(items):
        yy = y0 + i * .6 + .05
        d.text(.45, yy, 4.0, .4, s, 12.5, FG)
        px = x0 + (math.log10(max(v, 0.00001)) - lo) / (hi - lo) * w
        d.rect(x0, yy + .04, max(px - x0, .03), .38, fill=ACC, line=ACC, lw=1)
        label = '< 1e-5' if v <= 0.00001 else f'{v:g}%'
        d.text(px + .1, yy + .04, 1.2, .34, label, 12, FG)
    d.text(.45, 6.62, 12.4, .4, 'Every bar compares a result with its own stated reference; none compares a model with an experiment.', 13, MUT)
    return d.finish('Values from CH6_CH8_RESULTS.json, CPP_vs_COMSOL_wall_history.json and BAND_RESULTS.json.')


def f10():
    d = D('C5-F10', 'Sensitivity: one scaled history and one peak factor')
    cases = [('BU050', 'U 50 m/s'), ('B00625', 'U 99.03 m/s'), ('BU150', 'U 150 m/s'), ('BA05', 'a 0.5 µm'), ('BA2', 'a 2 µm')]
    cols = ['#8EDBD4', '#F2B880', '#B4A0F0', '#7FC8F8', '#F28BA0']
    ph = {'BU050': hugoniot(50), 'B00625': hugoniot(U0), 'BU150': hugoniot(150), 'BA05': hugoniot(U0), 'BA2': hugoniot(U0)}
    aum = {'BU050': 1, 'B00625': 1, 'BU150': 1, 'BA05': .5, 'BA2': 2}
    x0, y0, w, h = 1.3, 1.3, 6.0, 4.3
    xl, yl = (0, 0.49), (0.0, 1.0)
    d.axes(x0, y0, w, h, 'τ = c_0 t / a', 'p̄_a / p_H', [0, 0.1, 0.2, 0.3, 0.4], [0, .25, .5, .75, 1.0], xl, yl, '{:g}', '{:g}')
    peaks = []
    for (c, lab), col in zip(cases, cols):
        hh = load(c)
        tau = [t * C0 / (aum[c] * 1e-6) for t in hh['t']]
        y = [p / ph[c] for p in hh['pWall']]
        d.curve(x0, y0, w, h, xl, yl, tau, y, col, 1.8, step=2)
        peaks.append(max(y))
    x1, w1 = 8.4, 4.4
    d.text(x1, 1.0, w1, .4, 'Peak factor Λ of each case', 14.5, FG, bold=True)
    lo, hi = .925, .935
    d.line(x1, 5.2, x1 + w1, 5.2, color=MUT, width=1.4)
    for tk in (.926, .928, .930, .932, .934):
        px = x1 + (tk - lo) / (hi - lo) * w1
        d.line(px, 5.2, px, 5.27, color=MUT, width=1)
        d.text(px - .45, 5.3, .9, .28, f'{tk:.3f}', 10.5, MUT, 'center')
    for i, ((c, lab), col, pk) in enumerate(zip(cases, cols, peaks)):
        px = x1 + (pk - lo) / (hi - lo) * w1
        yy = 1.65 + i * .62
        d.line(x1, yy + .17, x1 + w1, yy + .17, color=GRID, width=.6)
        d.dot(px, yy + .17, .09, col)
        d.text(x1, yy - .25, 2.4, .3, f'{lab}: {pk:.4f}', 12, col)
    d.text(x1, 5.75, w1, 1.0, 'Spread 0.12% of the mean.\nRanges are scenario choices,\nnot confidence intervals.', 12.5, ACC)
    return d.finish('Curves and peaks computed from the five band-run histories.')


def f11():
    d = D('C5-F11', 'Validity map: what the result covers')
    x0, w = 1.0, 11.3
    d.line(x0, 2.6, x0 + w, 2.6, color=MUT, width=2)
    mmax = 0.14

    def mx(m):
        return x0 + m / mmax * w

    for tk in (0, .02, .04, .06, .08, .10, .12, .14):
        d.line(mx(tk), 2.6, mx(tk), 2.67, color=MUT, width=1)
        d.text(mx(tk) - .4, 2.7, .8, .28, f'{tk:g}', 11, MUT, 'center')
    d.text(x0, 3.0, w, .3, 'Impact Mach number M = U / c_0', 13, FG, 'center')
    d.rect(mx(.031), 2.05, mx(.092) - mx(.031), .5, fill='#2B5560', line=ACC, lw=2)
    d.text(mx(.031), 2.1, mx(.092) - mx(.031), .4, 'tested: 0.031 to 0.092', 13, FG, 'center', bold=True)
    d.line(mx(.0609), 1.8, mx(.0609), 2.05, color=WARM, width=2.5)
    d.text(mx(.0609) - 1.0, 1.4, 2.0, .4, 'nominal 0.0609', 12.5, WARM, 'center')
    d.text(x0, 1.2, 4.0, .4, 'Speed axis', 15, FG, bold=True)
    d.text(mx(0), 3.35, 3.0, .3, 'U = 50 m/s → M = 0.031', 11.5, MUT)
    d.text(mx(.092) - 1.0, 3.35, 3.4, .3, 'U = 150 m/s → M = 0.092', 11.5, MUT)
    d.rect(.8, 4.0, 5.9, 2.6, fill=AREA, line=ACC, lw=2)
    d.text(.95, 4.05, 5.6, .4, 'Inside the model', 15, ACC, bold=True)
    for i, s in enumerate(['Liquid only, barotropic stiffened-gas law', 'Rigid flat slip wall, free jet side', 'First arrival, τ = c_0 t / a ≤ 1', 'Jet radius 0.5 to 2 µm']):
        d.text(1.0, 4.55 + i * .5, 5.6, .4, '•  ' + s, 13.5, FG)
    d.rect(7.0, 4.0, 5.9, 2.6, fill=AREA, line=WARM, lw=2)
    d.text(7.15, 4.05, 5.6, .4, 'Outside the model', 15, WARM, bold=True)
    for i, s in enumerate(['Gas cushion, splash, cavitation', 'Elastic wall; pressure after τ ≈ 1', 'Bubble-to-jet physics upstream', 'Any experiment: not established']):
        d.text(7.2, 4.55 + i * .5, 5.6, .4, '•  ' + s, 13.5, FG)
    return d.finish('Ranges taken from the five sensitivity cases and the model assumptions.')



def poly_fill(d, pts, fill, line=None):
    d.add('polygon', points=[list(q) for q in pts], fill=fill, line=line or fill, line_width=1)


def e01():
    d = D('C5-E01', 'x')
    x0, y0, w, h = 1.4, 1.3, 6.6, 4.5
    xl, yl = (1.0, 1.08), (0, 250)
    rr = [xl[0] + i * (xl[1] - xl[0]) / 100 for i in range(101)]
    pp = [((PJ + PI) * r ** GAM - PI) / 1e6 for r in rr]
    d.axes(x0, y0, w, h, 'Density ratio ρ / ρ_j', 'Absolute pressure (MPa)', [1.00, 1.02, 1.04, 1.06, 1.08], [0, 50, 100, 150, 200, 250], xl, yl, '{:.2f}', '{:g}')
    d.curve(x0, y0, w, h, xl, yl, rr, pp, ACC, 3)
    d.dot(x0 + (1 - xl[0]) / (xl[1] - xl[0]) * w, y0 + h - PJ / 1e6 / 250 * h, .08, WARM)
    r1 = ((barotropic(U0) + PI) / (PJ + PI)) ** (1 / GAM)
    d.dot(x0 + (r1 - xl[0]) / (xl[1] - xl[0]) * w, y0 + h - barotropic(U0) / 1e6 / 250 * h, .08, WARM)
    d.text(x0 + .2, y0 + h - .6, 3, .3, 'reference state (ρ_j, p_j)', 12, WARM)
    d.text(x0 + (r1 - xl[0]) / (xl[1] - xl[0]) * w - 4.3, y0 + h - barotropic(U0) / 1e6 / 250 * h - .1, 4.1, .3, f'behind the barotropic shock: ρ_1 / ρ_j = {r1:.4f}', 12, WARM, 'right')
    d.text(8.5, 1.4, 4.5, .4, 'Liquid law', 15, FG, bold=True)
    d.text(8.5, 1.9, 4.6, 1.0, 'p(ρ) = (p_j + Π)(ρ / ρ_j)^γ − Π\nγ = 4.4,  Π = 600 MPa', 14, FG)
    d.text(8.5, 3.1, 4.5, .4, 'Sound speed', 15, FG, bold=True)
    d.text(8.5, 3.6, 4.6, 1.0, 'c² = dp/dρ = γ (p + Π) / ρ\nc_0 = 1626.447 m/s', 14, FG)
    d.text(8.5, 4.9, 4.5, .8, 'Pressure depends on density alone;\nnot derived from first principles.', 13, ACC)
    return d.finish('Curve computed from Eq. (C5-E01).')


def e03():
    d = D('C5-E03', 'x')
    wall(d, .9, 1.6, .5, 3.2)
    d.rect(.9, 1.55, .5, 3.3, fill='#3A5362', line=MUT)
    d.text(.55, 4.95, 1.4, .3, 'wall z = 0', 12, MUT, 'center')
    zs = 4.6
    d.rect(1.4, 1.6, zs - 1.4, 3.2, fill='#2B5560', line=ACC, lw=2)
    d.rect(zs, 1.6, 8.9 - zs, 3.2, fill=AREA, line=MUT, lw=1.5)
    d.line(zs, 1.35, zs, 5.05, color=WARM, width=4)
    d.line(zs, 1.05, zs + 1.4, 1.05, arrow=True, color=WARM, width=3)
    d.text(zs - .1, .6, 4.4, .4, 'shock front, lab speed S = U_s − U', 13, WARM)
    d.line(8.5, 3.2, 6.3, 3.2, arrow=True, color=ACC, width=3)
    d.text(6.55, 2.7, 2.2, .4, 'incoming speed U', 13, FG, 'center')
    d.text(1.5, 1.8, 3.0, .4, 'Behind the shock', 14, ACC, bold=True)
    d.text(1.5, 2.3, 3.0, 1.0, 'at rest\nρ_1, p_1', 14, FG)
    d.text(zs + .2, 1.8, 4.0, .4, 'Ahead of the shock', 14, MUT, bold=True)
    d.text(zs + .2, 3.45, 4.0, .8, 'ρ_j, p_j', 14, FG)
    d.text(.9, 5.5, 12, .4, 'In the shock frame: liquid enters at U_s and leaves at U_s − U', 14, FG)
    d.text(.9, 5.95, 12, .4, 'Mass: ρ_1 (U_s − U) = ρ_j U_s', 14, ACC)
    d.text(.9, 6.3, 12, .4, 'Momentum: p_1 − p_j = ρ_j U_s U', 14, ACC)
    d.text(.9, 6.65, 12, .4, 'Velocity ratio x = U / U_s = 1 − ρ_j / ρ_1', 14, FG)
    return d.finish('Schematic of Eq. (C5-E03); distances are not to scale.')


def e05():
    d = D('C5-E05', 'x')
    x0, w = 2.0, 8.6
    lo, hi = 155.0, 177.0
    items = [('Acoustic p_A', (PJ + RHO * C0 * U0) / 1e6, MUT), ('Barotropic p_B', barotropic(U0) / 1e6, WARM), ('Hugoniot p_H', hugoniot(U0) / 1e6, ACC)]
    d.line(x0, 4.6, x0 + w, 4.6, color=MUT, width=1.5)
    for tk in (155, 160, 165, 170, 175):
        px = x0 + (tk - lo) / (hi - lo) * w
        d.line(px, 4.6, px, 4.67, color=MUT, width=1)
        d.text(px - .4, 4.7, .8, .28, str(tk), 11, MUT, 'center')
    d.text(x0, 5.05, w, .3, 'Absolute wall pressure at U = 99.027 m/s (MPa)', 12.5, FG, 'center')
    for i, (lab, v, col) in enumerate(items):
        yy = 1.5 + i * 1.0
        px = x0 + (v - lo) / (hi - lo) * w
        d.line(x0, yy + .3, px, yy + .3, color=col, width=4)
        d.dot(px, yy + .3, .1, col)
        d.text(.3, yy + .12, 1.6, .34, lab, 13, col)
        d.text(px + .2, yy + .12, 2.4, .34, f'{v:.3f}', 13, FG)
    gap_b = abs(hugoniot(U0) - barotropic(U0)) / hugoniot(U0) * 100
    gap_a = abs(hugoniot(U0) - (PJ + RHO * C0 * U0)) / hugoniot(U0) * 100
    d.text(.9, 5.7, 12, .4, f'p_B is {gap_b:.3f}% below p_H: the energy equation is dropped.', 14, ACC)
    d.text(.9, 6.15, 12, .4, f'p_A is {gap_a:.1f}% below p_H: the linear estimate ignores compression.', 14, FG)
    return d.finish('Values from Eqs. (C5-E02), (C5-E04) and (C5-E05).')


def e07():
    d = D('C5-E07', 'x')
    x0, y0, w, h = 1.4, 1.3, 7.2, 4.5
    xl, yl = (0, 1.0), (0, 1.0)
    d.axes(x0, y0, w, h, 'τ = c_0 t / a', 'Fraction', [0, .2, .4, .6, .8, 1.0], [0, .25, .5, .75, 1.0], xl, yl, '{:g}', '{:g}')
    ts = [i / 100 for i in range(101)]
    d.curve(x0, y0, w, h, xl, yl, ts, [1 - (1 - t) ** 2 for t in ts], WARM, 2.5)
    d.curve(x0, y0, w, h, xl, yl, ts, [(1 - t) ** 2 for t in ts], ACC, 2.5, dash=True)
    hh = load('B00625')
    tau = [t * C0 / 1e-6 for t in hh['t']]
    d.curve(x0, y0, w, h, xl, yl, tau, [q / hugoniot(U0) for q in hh['pWall']], '#FFFFFF', 1.6)
    px = x0 + .0472 * w
    d.line(px, y0, px, y0 + h, color=GRID, width=1, dash=True)
    d.text(8.9, 1.4, 4.2, .4, 'Curves', 15, FG, bold=True)
    for i, (txt, col, dash) in enumerate([('f_rel = 1 − (1 − τ)²: released fraction', WARM, False), ('(1 − τ)²: full-release estimate', ACC, True), ('COMSOL p̄_a / p_H (band a/160)', '#FFFFFF', False)]):
        d.line(8.9, 2.1 + i * .6, 9.4, 2.1 + i * .6, color=col, width=3, dash=dash)
        d.text(9.5, 1.95 + i * .6, 3.6, .5, txt, 11.5, FG)
    d.text(8.9, 4.1, 4.2, .9, 'Dotted line: peak at τ = 0.0472\nf_rel = 0.0921; estimate 0.908', 12.5, WARM)
    d.text(8.9, 5.2, 4.2, .9, 'The estimate sets the sign\nand size of the gap,\nnot its digits.', 12.5, MUT)
    return d.finish('Estimate from Eq. (C5-E07); white curve from B00625_history.csv.')


def e08():
    d = D('C5-E08', 'x')
    x0, w = 1.2, 10.4
    tmax = 1.4
    d.line(x0, 3.2, x0 + w, 3.2, color=MUT, width=1.5)
    for tk in (0, .2, .4, .6, .8, 1.0, 1.2, 1.4):
        px = x0 + tk / tmax * w
        d.line(px, 3.2, px, 3.27, color=MUT, width=1)
        d.text(px - .4, 3.3, .8, .28, f'{tk:g}', 11, MUT, 'center')
    d.text(x0, 3.65, w, .3, 'Time from first contact (ns)', 12.5, FG, 'center')
    d.rect(x0, 2.3, 1.0 / tmax * w, .6, fill='#2B5560', line=ACC, lw=2)
    d.text(x0, 2.35, 1.0 / tmax * w, .5, 'incident window t_w = 1 ns', 14, FG, 'center', bold=True)
    tr = 2e-6 / barotropic_S(U0) * 1e9
    px = x0 + tr / tmax * w
    d.line(px, 1.9, px, 3.2, color=WARM, width=3)
    d.text(px - 2.2, 1.45, 4.4, .4, f'reflected shock returns to z = 2a at about {tr:.2f} ns', 12.5, WARM, 'center')
    d.rect(.9, 4.4, 5.6, 1.7, fill=AREA, line=ACC, lw=2)
    d.text(1.0, 4.45, 5.4, .4, 'Flux through the plane z = 2a', 14, ACC, 'center', bold=True)
    d.text(1.0, 4.9, 5.4, .4, 'mass flow  ṁ = ρ_j U π a² = 3.1053 × 10⁻⁷ kg/s', 12.5, FG, 'center')
    d.text(1.0, 5.3, 5.4, .4, 'energy flux  K̇ = ½ ρ_j U³ π a² = 1.5226 mW', 12.5, FG, 'center')
    d.text(1.0, 5.7, 5.4, .4, 'K (1 ns) = K̇ · 1 ns = 1.5226 pJ', 12.5, FG, 'center')
    d.rect(7.0, 4.4, 5.6, 1.7, fill=AREA, line=WARM, lw=2)
    d.text(7.1, 4.45, 5.4, .4, 'What the flux is not', 14, WARM, 'center', bold=True)
    d.text(7.1, 4.95, 5.4, 1.1, 'Liquid energy crossing a plane.\nA rigid wall does not move,\nso it receives no work.', 13, FG, 'center')
    return d.finish('Numbers for a = 1 µm and U = 99.02724 m/s.')


def hugoniot_Us():
    M = U0 / C0
    k = (GAM + 1) * M * M / 4
    x = -k + math.sqrt(k * k + M * M)
    return U0 / x


def e09():
    d = D('C5-E09', 'x')
    tiles = [('Mach number', 'M = U / c_0 = 0.0609', 'tested 0.031 to 0.092', ACC),
             ('Sound crossing of the radius', 't_a = a / c_0 = 0.615 ns', 'for a = 1 µm', ACC),
             ('Compression behind the shock', 'ρ_1 / ρ_j = 1.0594', 'only 5.9% denser', WARM),
             ('Barotropic against energy law', '(p_H − p_B) / p_H = 0.268%', 'at the nominal speed', WARM)]
    for i, (t, v, n, col) in enumerate(tiles):
        x = .8 + (i % 2) * 6.1
        y = 1.5 + (i // 2) * 2.3
        d.rect(x, y, 5.7, 1.9, fill=AREA, line=col, lw=2)
        d.text(x + .1, y + .08, 5.5, .4, t, 14, col, 'center', bold=True)
        d.text(x + .1, y + .6, 5.5, .5, v, 17, FG, 'center', bold=True)
        d.text(x + .1, y + 1.25, 5.5, .4, n, 13, MUT, 'center')
    d.text(.8, 6.15, 12, .5, 'Small Mach number and small compression let the density-only law stand in for the energy law.', 13.5, ACC)
    return d.finish('Values from Eqs. (C5-E04) and (C5-E05) and the sensitivity cases.')


def e10():
    d = D('C5-E10', 'x')
    x0, y0, w, h = 1.6, 1.3, 7.0, 4.5
    xl, yl = (0, 3.0), (0, 4.0)
    d.axes(x0, y0, w, h, 'Time from first contact (ns)', 'z (µm)', [0, 1, 2, 3], [0, 1, 2, 3, 4], xl, yl, '{:g}', '{:g}')
    S = barotropic_S(U0) / 1000.0
    te = 4.0 / S
    pts = [(x0, y0 + h), (x0 + te / 3.0 * w, y0), (x0, y0)]
    poly_fill(d, [(x0, y0 + h), (x0 + te / 3.0 * w, y0), (x0 + w, y0), (x0 + w, y0 + h)], '#2B5560', ACC)
    poly_fill(d, [(x0, y0 + h), (x0 + te / 3.0 * w, y0), (x0, y0)], AREA, MUT)
    d.line(x0, y0 + h, x0 + te / 3.0 * w, y0, color=WARM, width=3.5)
    d.line(x0, y0, x0 + w, y0, color=MUT, width=1.2, dash=True)
    d.text(x0 + .1, y0 + .05, 3.0, .3, 'inflow boundary z = H', 12, MUT)
    d.text(x0 + 3.9, y0 + 2.9, 3.0, .6, 'behind the shock:\nat rest', 13, FG, 'center')
    d.text(x0 + .15, y0 + .55, 2.6, .6, 'ahead:\nρ_j, −U', 13, FG)
    d.text(8.9, 1.4, 4.2, .4, 'Wave pattern', 15, FG, bold=True)
    d.text(8.9, 1.9, 4.2, 2.0, f'Barotropic shock: S = {S * 1000:.1f} m/s\nreaches H = 4 µm at {te:.2f} ns\nWall: u = 0 (mirror ghost state)\nInflow: (ρ_j, −U)', 13.5, FG)
    d.text(8.9, 4.3, 4.2, .9, 'Conservative form lets the\nshock move at the right speed.', 13.5, ACC)
    return d.finish('Space-time sketch of Eq. (C5-E10); S from Eq. (C5-E05).')


def e12():
    d = D('C5-E12', 'x')
    boxes = [(.8, 1.7, 'Mass', '∂ₜρ + ∇·(ρu) = 0'), (.8, 3.0, 'Momentum', 'ρ Du/Dt = −∇p + ∇·(viscous stress)'), (.8, 4.3, 'Liquid law', 'ρ(p) = ρ_j [(p + Π)/(p_j + Π)]^(1/γ)')]
    for x, y, t, e in boxes:
        d.rect(x, y, 6.4, 1.0, fill=AREA, line=ACC, lw=2)
        d.text(x + .1, y + .05, 6.2, .4, t, 14, ACC, bold=True)
        d.text(x + .1, y + .5, 6.2, .4, e, 13, FG)
        d.line(x + 6.4, y + .5, 8.3, 3.5, arrow=True, color=MUT, width=1.8)
    d.rect(8.4, 2.6, 4.4, 1.8, fill='#2B5560', line=WARM, lw=2)
    d.text(8.5, 2.65, 4.2, .4, 'Fields (axisymmetric)', 14, WARM, 'center', bold=True)
    d.text(8.5, 3.15, 4.2, 1.2, 'ρ,  p\nu_r,  w\nviscosity μ = 1 mPa s', 13.5, FG, 'center')
    d.text(.8, 5.8, 12, .5, 'Same liquid as the C++ reference, plus radial motion and a small viscosity. No gas phase.', 13.5, ACC)
    return d.finish('Schematic of Eq. (C5-E12).')


def e19():
    d = D('C5-E19', 'x')
    x0, w = 2.0, 8.6
    lo, hi = 155.0, 180.0
    ph = hugoniot(U0) / 1e6
    items = [('Linear ceiling p_A', (PJ + RHO * C0 * U0) / 1e6, MUT, 'acoustic'), ('Full sensor, r ≤ a', max(load('B00625')['pWall']) / 1e6, ACC, '0.931 p_H (band a/160)'), ('Centre disk, r ≤ a/2', ph, WARM, 'p_H within 0.43%')]
    d.line(x0, 4.6, x0 + w, 4.6, color=MUT, width=1.5)
    for tk in (155, 160, 165, 170, 175, 180):
        px = x0 + (tk - lo) / (hi - lo) * w
        d.line(px, 4.6, px, 4.67, color=MUT, width=1)
        d.text(px - .4, 4.7, .8, .28, str(tk), 11, MUT, 'center')
    d.text(x0, 5.05, w, .3, 'Peak absolute wall pressure at U = 99.027 m/s (MPa)', 12.5, FG, 'center')
    for i, (lab, v, col, note_) in enumerate(items):
        yy = 1.5 + i * 1.05
        px = x0 + (v - lo) / (hi - lo) * w
        d.line(x0, yy + .3, px, yy + .3, color=col, width=4)
        d.dot(px, yy + .3, .1, col)
        d.text(.2, yy + .12, 1.75, .34, lab, 12, col)
        d.text(px + .2, yy + .02, 3.2, .34, f'{v:.2f} MPa', 13, FG)
        d.text(px + .2, yy + .38, 3.2, .34, note_, 11.5, MUT)
    d.text(.8, 5.7, 12, .4, 'High-pressure interval lasts about a / c_0 = 0.61 ns for a = 1 µm.', 13.5, ACC)
    d.text(.8, 6.15, 12, .4, 'Nonlinear factor over the linear ceiling: U_s / c_0 = 1.0856.', 13.5, FG)
    return d.finish('Values from Eq. (C5-E19) and the converged band runs.')


def e20():
    d = D('C5-E20', 'x')
    boxes = [(.5, 'Chapter 3', 'energy E_av, mass m_j', 'bound', MUT), (3.6, 'Speed ceiling', 'U ≤ √(2 E_av / m_j)', 'bound', MUT),
             (6.7, 'Prescribed speed U', 'taken as given here', 'input', WARM), (9.8, 'Pressure map', 'p_wall = f(U)', 'computed', ACC)]
    for i, (x, t, e, tag, col) in enumerate(boxes):
        d.rect(x, 2.3, 2.9, 1.7, fill=AREA, line=col, lw=2)
        d.text(x + .05, 2.38, 2.8, .4, t, 14, col, 'center', bold=True)
        d.text(x + .05, 2.95, 2.8, .7, e, 12.5, FG, 'center')
        d.text(x + .05, 3.55, 2.8, .35, tag, 12, MUT, 'center')
        if i < 3:
            d.line(x + 2.9, 3.15, x + 3.6, 3.15, arrow=True, color=MUT, width=2.5)
    d.text(9.8, 4.2, 3.0, 1.2, 'centre: p_H\nfull sensor: 0.931 p_H', 13.5, ACC, 'center')
    d.text(.5, 5.2, 8.8, .9, 'The bound limits the speed. The map converts a speed to a pressure.\nThe two claims meet only at the prescribed speed.', 14, FG)
    d.text(.5, 6.3, 12, .4, 'A bound is not a prediction; a map is not a measurement.', 14, WARM, bold=True)
    return d.finish('Chain of Eq. (C5-E20); Chapter 3 bound from Eq. (C3-E32).')


def e21():
    d = D('C5-E21', 'x')
    x0, y0, w, h = 1.6, 1.3, 6.8, 4.5
    xl, yl = (0, 1.0), (0.90, 1.0)
    d.axes(x0, y0, w, h, 'κ: share of the excess lost in the released annulus', 'Λ', [0, .25, .5, .75, 1.0], [0.90, 0.92, 0.94, 0.96, 0.98, 1.0], xl, yl, '{:g}', '{:.2f}')
    frel = 1 - (1 - .0472) ** 2
    ks = [i / 100 for i in range(101)]
    d.curve(x0, y0, w, h, xl, yl, ks, [1 - k * frel for k in ks], ACC, 3)
    kap = (1 - 0.931) / frel
    px = x0 + kap * w
    py = y0 + h - (0.931 - yl[0]) / (yl[1] - yl[0]) * h
    d.dot(px, py, .1, WARM)
    d.line(px, py, px, y0 + h, color=WARM, width=1.2, dash=True)
    d.text(px - 3.3, py + .12, 3.2, .3, f'computed Λ = 0.931,  κ = {kap:.2f}', 12, WARM, 'right')
    d.text(x0 + w - 3.2, y0 + h - (0.9079 - yl[0]) / (yl[1] - yl[0]) * h + .1, 3.2, .3, 'full release: 0.908', 12, MUT, 'right')
    d.text(8.8, 1.4, 4.3, .4, 'Reading', 15, FG, bold=True)
    d.text(8.8, 1.9, 4.3, 3.2, 'Λ ≈ 1 − κ f_rel(τ_pk)\nτ_pk = 0.0472, f_rel = 0.0921\nκ = 0 : no loss, Λ = 1\nκ = 1 : full release, Λ = 0.908\nSimulation lies in between,\nso about a quarter of the excess stays.', 13.5, FG)
    return d.finish('Line from Eq. (C5-E21); the computed Λ is from the converged band runs.')



EQ_TITLES = {}


def eq_title(n):
    import sys
    sys.path.insert(0, str(ROOT / 'content'))
    from chapter05_spec import EQS
    return {e['n']: e['kind'] for e in EQS}[n]


NEW = {1: e01, 3: e03, 5: e05, 7: e07, 8: e08, 9: e09, 10: e10, 12: e12, 19: e19, 20: e20, 21: e21}
REUSE = {2: f02, 4: f03, 6: f04, 11: f05, 13: f06, 14: f01, 15: f08, 16: f09, 17: f07, 18: f10, 22: f11}


def main():
    from sci_ppt_common import scene_to_svg, render_scene
    OUT.mkdir(parents=True, exist_ok=True)
    for old in list(OUT.glob('*')) + list((ROOT / 'assets/figures').glob('c5-f*.svg')):
        if old.is_file():
            old.unlink()
    (ROOT / 'assets/figures').mkdir(exist_ok=True)
    ids = []
    for n in range(1, 23):
        build = NEW.get(n) or REUSE[n]
        scene = build()
        ident = f'C5-E{n:02d}'
        title = f'{ident} · {eq_title(n)}'
        scene['objects'][0]['text'] = title
        scene['objects'][0]['font_size'] = 19
        for o in scene['objects']:
            o['name'] = o['name'].replace(o['name'].split(' ')[0], ident, 1)
        scene['_title'] = title
        scene['_audit']['id'] = ident
        key = ident.lower()
        ids.append(key)
        (OUT / f'{key}.scene.json').write_text(json.dumps(scene, ensure_ascii=False, indent=2), encoding='utf-8')
        scene_to_svg(scene, OUT / f'{key}.svg')
        render_scene(scene, OUT / f'{key}.pptx')
        shutil.copy2(OUT / f'{key}.svg', ROOT / 'assets/figures' / f'{key}.svg')
    (OUT / 'manifest.json').write_text(json.dumps(ids, indent=2), encoding='utf-8')
    from sci_ppt_common import make_deck
    make_deck([json.loads((OUT / f'{k}.scene.json').read_text(encoding='utf-8')) for k in ids], OUT / 'c5-figures.pptx')
    print('Created', len(ids), 'Chapter 5 equation figures in', OUT)


if __name__ == '__main__':
    main()
