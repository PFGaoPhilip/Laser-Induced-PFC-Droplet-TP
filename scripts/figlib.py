"""Shared SCI-PPT drawing library for the equation figures of Chapters 1-4 and Appendix A.

Coordinates are inches on a 13.333 x 7.5 slide. Text auto-wraps to its box and is checked for overlap.
Scenes use only primitives that both the PPTX renderer and the SVG exporter support.
"""
import math
import re
import textwrap

BG, FG, ACC, MUT, AREA = '#142632', '#E7F0F3', '#8EDBD4', '#B4C7D2', '#213E4B'
WARM, GRID, BLUE, PURP, PINK, GREEN, RED = '#F2B880', '#2E4756', '#7FC8F8', '#B4A0F0', '#F28BA0', '#A8E6A1', '#F2837F'
LIQ, LIQ2, GASC, STEEL, DEEP = '#1E4A5A', '#2B6678', '#0C1820', '#3A5362', '#0F2029'
W, H = 13.333, 7.5

_SUBS = {'0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
         'a': 'ₐ', 'e': 'ₑ', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ', 'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ',
         'p': 'ₚ', 'r': 'ᵣ', 's': 'ₛ', 't': 'ₜ', 'u': 'ᵤ', 'v': 'ᵥ', 'x': 'ₓ', '+': '₊', '-': '₋', '−': '₋',
         '(': '₍', ')': '₎', '=': '₌', 'β': 'ᵦ', 'γ': 'ᵧ', 'ρ': 'ᵨ', 'φ': 'ᵩ', 'χ': 'ᵪ'}
_SUPS = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
         'n': 'ⁿ', 'i': 'ⁱ', '+': '⁺', '-': '⁻', '−': '⁻', '(': '⁽', ')': '⁾'}


def U(s):
    """Convert simple X_y / X^2 notation to Unicode sub/superscripts; leave others as written."""
    def sub(m):
        g = m.group(1) or m.group(2)
        return ''.join(_SUBS[c] for c in g) if all(c in _SUBS for c in g) else m.group(0)

    def sup(m):
        g = m.group(1) or m.group(2)
        return ''.join(_SUPS[c] for c in g) if all(c in _SUPS for c in g) else m.group(0)
    s = re.sub(r'_\{([^}]*)\}|_([A-Za-z0-9β-χ]+)', sub, s)
    return re.sub(r'\^\{([^}]*)\}|\^([0-9])', sup, s)


def _width_est(s, size):
    return max((len(l) for l in s.split('\n')), default=0) * size * 0.5 / 72


class Fig:
    def __init__(self, ident, kind, title_size=19):
        self.id, self.o, self.tb, self.n = ident, [], [], 0
        self.text(.3, .13, 12.7, f'{ident} · {kind}', title_size, ACC, bold=True, wrap=False)

    def add(self, typ, **kw):
        kw.update(type=typ, id=f'o{len(self.o):03}', name=f'{self.id} {typ} {len(self.o)}')
        self.o.append(kw)

    def text(self, x, y, w, s, size=13, color=FG, align='left', bold=False, wrap=True, italic=False):
        s = U(s)
        if wrap:
            cpl = max(4, int(w * 72 / (size * 0.53)))
            lines = []
            for para in s.split('\n'):
                lines += textwrap.wrap(para, cpl, break_long_words=False, break_on_hyphens=False) or ['']
            s = '\n'.join(lines)
        n = s.count('\n') + 1
        h = n * size * 1.22 / 72 + 0.05
        kw = dict(x=x, y=y, w=w, h=h, text=s, font='Arial', font_size=size, color=color, word_wrap=False,
                  align=align, valign='top', margin=0.02)
        if bold:
            kw['bold'] = True
        if italic:
            kw['italic'] = True
        self.add('text', **kw)
        ew = min(w, _width_est(s, size)) if align == 'left' else min(w, _width_est(s, size))
        bx = x if align == 'left' else (x + (w - ew) / 2 if align == 'center' else x + w - ew)
        self.tb.append((bx, y, ew, h, s[:30]))
        return y + h

    def line(self, x1, y1, x2, y2, color=ACC, width=2, arrow=False, dash=False, opacity=None):
        kw = dict(x1=x1, y1=y1, x2=x2, y2=y2, line=color, line_width=width)
        if dash:
            kw['_dash'] = True
        if opacity is not None:
            kw['opacity'] = opacity
        self.add('arrow' if arrow else 'line', **kw)

    def rect(self, x, y, w, h, fill=AREA, line=MUT, lw=1.5, opacity=None, round_=False):
        kw = dict(x=x, y=y, w=w, h=h, fill=fill, line=line, line_width=lw)
        if opacity is not None:
            kw['opacity'] = opacity
        self.add('round_rect' if round_ else 'rect', **kw)

    def ellipse(self, cx, cy, rx, ry=None, fill=AREA, line=MUT, lw=1.5, opacity=None):
        ry = rx if ry is None else ry
        kw = dict(x=cx - rx, y=cy - ry, w=2 * rx, h=2 * ry, fill=fill, line=line, line_width=lw)
        if opacity is not None:
            kw['opacity'] = opacity
        self.add('ellipse', **kw)

    def dot(self, x, y, r=.07, color=WARM):
        self.ellipse(x, y, r, r, fill=color, line=color, lw=1)

    def poly(self, pts, fill=AREA, line=MUT, lw=1.2, opacity=None):
        kw = dict(points=[[float(a), float(b)] for a, b in pts], fill=fill, line=line, line_width=lw)
        if opacity is not None:
            kw['opacity'] = opacity
        self.add('polygon', **kw)

    def path(self, pts, color=ACC, width=2, dash=False, opacity=None):
        """Open polyline as one editable object."""
        pts = [list(map(float, p)) for p in pts]
        if len(pts) < 2:
            return
        while len(pts) < 3:
            pts.append(pts[-1])
        kw = dict(points=pts, fill=None, line=color, line_width=width, _open=True)
        if dash:
            kw['_dash'] = True
        if opacity is not None:
            kw['opacity'] = opacity
        self.add('polygon', **kw)

    # ---- composite pieces ---------------------------------------------------------------
    def panel(self, x, y, w, h, title=None, color=MUT, fill=AREA, size=13.5):
        self.rect(x, y, w, h, fill=fill, line=color, lw=1.6, round_=True)
        if title:
            self.text(x + .12, y + .06, w - .24, title, size, color, bold=True)

    def bullets(self, x, y, w, items, size=12.5, color=FG, gap=.05, dot_color=ACC):
        for s in items:
            bottom = self.text(x + .22, y, w - .22, s, size, color)
            self.dot(x + .08, y + size * .62 / 72, .045, dot_color)
            y = bottom + gap
        return y

    def side(self, title, items, x=8.75, y=.95, w=4.25, color=ACC, size=12.5):
        self.text(x, y, w, title, 15, color, bold=True)
        return self.bullets(x, y + .42, w, items, size)

    def note(self, s):
        self.text(.35, 7.12, 12.6, s, 10, MUT, wrap=False)

    def bubble(self, cx, cy, r, rim=WARM, gas=GASC, lw=2.2):
        self.ellipse(cx, cy, r, r, fill=gas, line=rim, lw=lw)

    def liquid_rings(self, cx, cy, r0, n=4, step=.35, color=LIQ2):
        for i in range(n):
            self.ellipse(cx, cy, r0 + step * (i + 1), fill=None, line=color, lw=1.2, opacity=max(.15, .8 - .18 * i))

    def radial_arrows(self, cx, cy, r1, r2, n=8, color=ACC, width=2, start=0.0, scale=None):
        for k in range(n):
            a = start + 2 * math.pi * k / n
            rr2 = r2 if scale is None else r1 + (r2 - r1) * scale[k % len(scale)]
            self.line(cx + r1 * math.cos(a), cy - r1 * math.sin(a), cx + rr2 * math.cos(a), cy - rr2 * math.sin(a),
                      color, width, arrow=True)

    def wall(self, x, y, w, h=.26, up=False):
        self.rect(x, y, w, h, fill=STEEL, line=MUT, lw=1.3)
        n = int(w / .2)
        for i in range(n):
            xx = x + i * .2 + .02
            if up:
                self.line(xx, y, xx + .15, y - .17, MUT, 1)
            else:
                self.line(xx, y + h, xx + .15, y + h + .17, MUT, 1)

    def spring(self, x1, y1, x2, y2, n=6, amp=.12, color=ACC, width=2):
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy)
        ux, uy, nx, ny = dx / L, dy / L, -dy / L, dx / L
        pts = [(x1, y1), (x1 + ux * L * .12, y1 + uy * L * .12)]
        for i in range(n * 2):
            t = .12 + .76 * (i + .5) / (n * 2)
            s = amp if i % 2 == 0 else -amp
            pts.append((x1 + ux * L * t + nx * s, y1 + uy * L * t + ny * s))
        pts += [(x1 + ux * L * .88, y1 + uy * L * .88), (x2, y2)]
        self.path(pts, color, width)

    def dashpot(self, x1, y1, x2, y2, color=ACC, width=2):
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy)
        ux, uy, nx, ny = dx / L, dy / L, -dy / L, dx / L
        a, b = .3, .62
        c = lambda t, s: (x1 + ux * L * t + nx * s, y1 + uy * L * t + ny * s)
        self.path([c(0, 0), c(b, 0)], color, width)
        self.path([c(a, .13), c(b + .08, .13), c(b + .08, -.13), c(a, -.13)], color, width)
        self.path([c(b, .1), c(b, -.1)], color, width + 1)
        self.path([c(b + .08, 0), c(1, 0)], color, width)

    def dim(self, x1, y1, x2, y2, label, color=MUT, size=12, off=.0, side=1):
        """Dimension line with end ticks and a centred label."""
        self.line(x1, y1, x2, y2, color, 1.3, arrow=False)
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        for (px, py) in ((x1, y1), (x2, y2)):
            self.line(px - nx * .07, py - ny * .07, px + nx * .07, py + ny * .07, color, 1.3)
        mx, my = (x1 + x2) / 2 + nx * (.2 + off) * side, (y1 + y2) / 2 + ny * (.2 + off) * side
        self.text(mx - 1.0, my - size * .6 / 72, 2.0, label, size, color, 'center')

    def chain(self, boxes, y, h=.9, gap=.45, x0=.5, total=12.3, colors=None, size=12.5, title_size=13.5):
        """Row of titled boxes joined by arrows; boxes = [(title, body), ...]."""
        n = len(boxes)
        bw = (total - gap * (n - 1)) / n
        for i, (t, b) in enumerate(boxes):
            col = (colors or [ACC] * n)[i]
            x = x0 + i * (bw + gap)
            self.panel(x, y, bw, h, None, col)
            yy = self.text(x + .08, y + .06, bw - .16, t, title_size, col, 'center', bold=True)
            self.text(x + .08, yy + .02, bw - .16, b, size, FG, 'center')
            if i < n - 1:
                self.line(x + bw + .03, y + h / 2, x + bw + gap - .03, y + h / 2, MUT, 2.2, arrow=True)

    # ---- output -------------------------------------------------------------------------
    def check(self):
        warns = []
        for i, a in enumerate(self.tb):
            if a[0] < -0.01 or a[0] + a[2] > W + .01 or a[1] + a[3] > H + .01:
                warns.append(f'off-canvas: {a[4]!r}')
            for b in self.tb[i + 1:]:
                ox = min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0])
                oy = min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1])
                if ox > .04 and oy > .04:
                    warns.append(f'overlap: {a[4]!r} / {b[4]!r}')
        return warns

    def scene(self):
        return {'slide': {'width': W, 'height': H}, 'background': BG, 'objects': self.o, '_title': self.id,
                '_audit': {'id': self.id, 'scientific_status': 'drawn from the equation and its stated numbers'}}


class Plot:
    """Axes with data-coordinate drawing on a Fig."""

    def __init__(self, f, x0, y0, w, h, xlim, ylim, xlabel='', ylabel='', xticks=(), yticks=(), fx='{:g}', fy='{:g}',
                 xlog=False, ylog=False, grid=True, label_size=12, tick_size=10.5):
        self.f, self.x0, self.y0, self.w, self.h, self.xlim, self.ylim = f, x0, y0, w, h, xlim, ylim
        self.xlog, self.ylog = xlog, ylog
        f.line(x0, y0 + h, x0 + w, y0 + h, MUT, 1.5)
        f.line(x0, y0, x0, y0 + h, MUT, 1.5)
        for v in xticks:
            px = self.X(v)
            f.line(px, y0 + h, px, y0 + h + .07, MUT, 1)
            if grid:
                f.line(px, y0, px, y0 + h, GRID, .6)
            f.text(px - .5, y0 + h + .09, 1.0, fx.format(v), tick_size, MUT, 'center', wrap=False)
        for v in yticks:
            if v == ylim[0] and xticks and xticks[0] == xlim[0]:
                py = self.Y(v)
                f.line(x0 - .07, py, x0, py, MUT, 1)
                continue
            py = self.Y(v)
            f.line(x0 - .07, py, x0, py, MUT, 1)
            if grid:
                f.line(x0, py, x0 + w, py, GRID, .6)
            f.text(x0 - .95, py - .09, .85, fy.format(v), tick_size, MUT, 'right', wrap=False)
        if xlabel:
            f.text(x0, y0 + h + .31, w, xlabel, label_size, FG, 'center', wrap=False)
        if ylabel:
            f.text(x0 - .6, y0 - .38, max(w, 3.0), ylabel, label_size, FG, wrap=False)

    def _m(self, v, lim, log):
        a, b = lim
        if log:
            v, a, b = math.log10(max(v, 1e-300)), math.log10(a), math.log10(b)
        return (v - a) / (b - a)

    def X(self, v):
        return self.x0 + self._m(v, self.xlim, self.xlog) * self.w

    def Y(self, v):
        return self.y0 + self.h - self._m(v, self.ylim, self.ylog) * self.h

    def _inside(self, x, y):
        return (self.xlim[0] <= x <= self.xlim[1]) and (self.ylim[0] <= y <= self.ylim[1])

    def curve(self, xs, ys, color=ACC, width=2.2, dash=False, maxpts=140):
        step = max(1, len(xs) // maxpts)
        pts, run = [], []
        for i in list(range(0, len(xs), step)) + ([len(xs) - 1] if (len(xs) - 1) % step else []):
            x, y = xs[i], ys[i]
            if y is None or not math.isfinite(y) or not self._inside(x, y):
                if run:
                    pts.append(run)
                run = []
                continue
            run.append((self.X(x), self.Y(y)))
        if run:
            pts.append(run)
        for r in pts:
            if len(r) >= 2:
                self.f.path(r, color, width, dash)

    def fill(self, xs, ylo, yhi, color=ACC, opacity=.25, line=None):
        up = [(self.X(x), self.Y(min(max(y, self.ylim[0]), self.ylim[1]))) for x, y in zip(xs, yhi)]
        dn = [(self.X(x), self.Y(min(max(y, self.ylim[0]), self.ylim[1]))) for x, y in zip(xs, ylo)][::-1]
        self.f.poly(up + dn, fill=color, line=line or color, lw=.8, opacity=opacity)

    def pt(self, x, y, color=WARM, r=.08):
        self.f.dot(self.X(x), self.Y(y), r, color)

    def vline(self, x, color=WARM, dash=True, width=1.3):
        self.f.line(self.X(x), self.y0, self.X(x), self.y0 + self.h, color, width, dash=dash)

    def hline(self, y, color=WARM, dash=True, width=1.3):
        self.f.line(self.x0, self.Y(y), self.x0 + self.w, self.Y(y), color, width, dash=dash)

    def label(self, x, y, s, color=FG, size=11.5, w=2.6, align='left', dx=.08, dy=-.1):
        self.f.text(self.X(x) + dx, self.Y(y) + dy, w, s, size, color, align, wrap=True)

    def arrow(self, x1, y1, x2, y2, color=ACC, width=2):
        self.f.line(self.X(x1), self.Y(y1), self.X(x2), self.Y(y2), color, width, arrow=True)

    def seg(self, x1, y1, x2, y2, color=MUT, width=1.4, dash=False):
        self.f.line(self.X(x1), self.Y(y1), self.X(x2), self.Y(y2), color, width, dash=dash)


def linspace(a, b, n):
    return [a + (b - a) * i / (n - 1) for i in range(n)]


def hbars(f, x0, y0, w, rows, vmax, bar_h=.42, gap=.2, label_w=3.0, fmt='{:.3g}', unit='', size=12.5, log=False, vmin=None):
    """Horizontal bars: rows = [(label, value, color)]; bars start after the label column."""
    bx = x0 + label_w
    bw = w - label_w - 1.4
    for i, (lab, v, col) in enumerate(rows):
        y = y0 + i * (bar_h + gap)
        f.text(x0, y + .02, label_w - .1, lab, size, FG)
        if log:
            frac = (math.log10(v) - math.log10(vmin)) / (math.log10(vmax) - math.log10(vmin))
        else:
            frac = v / vmax
        wd = max(frac * bw, .03)
        f.rect(bx, y, wd, bar_h, fill=col, line=col, lw=1, opacity=.85)
        f.text(bx + wd + .08, y + .05, 1.5, fmt.format(v) + unit, size, FG, bold=True, wrap=False)
    return y0 + len(rows) * (bar_h + gap)


def waterfall(f, x0, y0, w, h, steps, ymax, fmt='{:.1f}', label_size=11.5, yticks=None, ylabel='', total_color=ACC):
    """steps = [(label, delta, color)] with the first a start total and optional last total marked by ('=', None, color)."""
    p = Plot(f, x0, y0, w, h, (0, len(steps)), (0, ymax), '', ylabel, (), yticks or (), fy='{:g}')
    run = 0.0
    for i, (lab, d, col) in enumerate(steps):
        xa = i + .14
        bw = p.X(xa + .72) - p.X(xa)
        if d is None:
            lo, hi, txt = 0, run, fmt.format(run)
        elif i == 0:
            lo, hi, txt, run = 0, d, fmt.format(d), d
        else:
            lo, hi = (run + d, run) if d < 0 else (run, run + d)
            txt = ('+' if d > 0 else '') + fmt.format(d)
            run += d
        f.rect(p.X(xa), p.Y(hi), bw, max(p.Y(lo) - p.Y(hi), .02), fill=col, line=col, lw=1, opacity=.85)
        f.text(p.X(xa) - .25, p.Y(hi) - .3, bw + .5, txt, label_size, FG, 'center', bold=True, wrap=False)
        f.text(p.X(xa) - .3, p.Y(0) + .08, bw + .6, lab, label_size - .5, MUT, 'center')
    return p
