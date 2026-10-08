"""Independent algebra, quadrature and finite-budget checks for Chapter 4.

Run with Python -B. This verifies adopted teaching models, not actual transfer.
"""
from pathlib import Path
import importlib.util
import json
import math
import re
import os
import shutil
import subprocess
import sys

import sympy as sp
from scipy.integrate import quad
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / 'content'))
import chapter04
from coursekit import EQUATIONS

checks = []


def check(name, passed, detail=None):
    checks.append(dict(name=name, passed=bool(passed), detail=detail))


def close(name, actual, expected, rtol=1e-10, atol=0):
    check(name, math.isclose(float(actual), float(expected), rel_tol=rtol, abs_tol=atol),
          dict(actual=float(actual), expected=float(expected)))


# Reconstruct the radial operator independently from the authored integrations.
r, b, p, D, nu = sp.symbols('r b p D nu', positive=True)
w = p * (b*b - r*r)**2 / (64*D)


def lap(f):
    return sp.diff(r*sp.diff(f, r), r)/r


check('Circular-plate governing residual', sp.simplify(D*lap(lap(w))-p) == 0)
check('Clamped displacement boundary', sp.simplify(w.subs(r, b)) == 0)
check('Clamped slope boundary', sp.simplify(sp.diff(w, r).subs(r, b)) == 0)
check('Regular centre slope', sp.limit(sp.diff(w, r), r, 0) == 0)
v_bl = sp.simplify(2*sp.pi*sp.integrate(w*r, (r, 0, b)))
check('Exact blister volume', sp.simplify(v_bl-sp.pi*p*b**6/(192*D)) == 0)
kr = -sp.diff(w, r, 2)
kt = -sp.diff(w, r)/r
u_b = sp.simplify(D*sp.pi*sp.integrate((kr**2+kt**2+2*nu*kr*kt)*r, (r, 0, b)))
check('Curvature energy equals half pressure-volume', sp.simplify(u_b-p*v_bl/2) == 0)
potential = u_b-p*v_bl
g_p = sp.simplify(-sp.diff(potential, b)/(2*sp.pi*b))
check('Pressure-controlled energy-release rate', sp.simplify(g_p-p*p*b**4/(128*D)) == 0)
V = sp.symbols('V', positive=True)
u_v = 96*D*V**2/(sp.pi*b**6)
g_v = sp.simplify(-sp.diff(u_v, b)/(2*sp.pi*b))
check('Volume-controlled energy-release rate', sp.simplify(g_v-288*D*V**2/(sp.pi**2*b**8)) == 0)
check('Same-state fixed-control expression', sp.simplify(g_v-g_p.subs(p, 192*D*V/(sp.pi*b**6))) == 0)
check('Opposite load-control slopes', sp.diff(g_p, b).is_positive and sp.diff(g_v, b).is_negative)
# Check the isotropic tensor contraction behind the two integrations by parts.
x, yy = sp.symbols('x yy')
W = sp.Function('W')(x, yy)
coords = [x, yy]
lap_W = sp.diff(W, x, 2)+sp.diff(W, yy, 2)
B = [[D*((1-nu)*sp.diff(W, coords[i], coords[j])+(nu*lap_W if i==j else 0))
      for j in range(2)] for i in range(2)]
bulk_contraction = sum(sp.diff(B[i][j], coords[i], coords[j]) for i in range(2) for j in range(2))
check('Twice-integrated bending tensor equals biharmonic force',
      sp.simplify(bulk_contraction-D*(sp.diff(lap_W, x, 2)+sp.diff(lap_W, yy, 2))) == 0)
check('Zero-load derivative compliance is finite positive', sp.simplify(sp.diff(v_bl, p)-sp.pi*b**6/(192*D)) == 0)
check('Zero-load volume and elastic energy vanish', sp.simplify(v_bl.subs(p, 0)) == 0 and sp.simplify(u_b.subs(p, 0)) == 0)

E_f, h_f, nu_f, b_v, gamma = 2e9, 10e-6, .35, 100e-6, .10
D_v = E_f*h_f**3/(12*(1-nu_f**2))
p_c = math.sqrt(128*D_v*gamma)/b_v**2
wc = p_c*b_v**4/(64*D_v)
volume_q = 2*math.pi*quad(lambda rr: p_c*(b_v*b_v-rr*rr)**2/(64*D_v)*rr,
                       0, b_v, epsabs=1e-27, epsrel=1e-12)[0]
energy_q = D_v*math.pi*quad(
    lambda rr: ((-p_c*(3*rr**2-b_v*b_v)/(16*D_v))**2
                +(-p_c*(rr**2-b_v*b_v)/(16*D_v))**2
                +2*nu_f*(-p_c*(3*rr**2-b_v*b_v)/(16*D_v))
                *(-p_c*(rr**2-b_v*b_v)/(16*D_v)))*rr,
    0, b_v, epsabs=1e-22, epsrel=1e-12)[0]
close('Numerical stiffness', D_v, 1.8993352326685665e-7)
close('Critical maintained pressure', p_c, 155921.425654583)
close('Centre deflection', wc, 1.2826973532365306e-6)
close('Independent volume quadrature', volume_q, math.pi*p_c*b_v**6/(192*D_v))
close('Independent bending energy quadrature', energy_q, .5*p_c*volume_q)
close('Critical driving force equals resistance', p_c**2*b_v**4/(128*D_v), gamma)
sigma_edge = 3*p_c*b_v*b_v/(4*h_f*h_f)
close('Edge bending stress', sigma_edge, 11694106.924093723)

Tmax, Kn, gamma_c = 1e5, 1e13, .005
d0, dc = Tmax/Kn, 2*gamma_c/Tmax
ascending = quad(lambda dd: Kn*dd, 0, d0, epsabs=1e-16)[0]
descending = quad(lambda dd: Tmax*(dc-dd)/(dc-d0), d0, dc, epsabs=1e-16)[0]
close('Cohesive work quadrature', ascending+descending, gamma_c)
check('Cohesive opening order', 0 < d0 < dc)
check('Cohesive stiffness admissibility', Kn > Tmax*Tmax/(2*gamma_c))

rho, diameter, length, N, Ej = 1000., 10e-6, 50e-6, 25, 2e-9
mj = rho*math.pi*diameter**2*length/4
speed = math.sqrt(2*Ej/mj)
Ein, Iin = N*Ej, N*mj*speed
mf, area = 2330.*1e-6*1e-6, 1e-6
Esolid, Inet = .2*Ein, .5*Iin
minimum_speed = .5
close('Carrier jet mass', mj, 3.926990816987242e-12)
close('Uniform jet speed', speed, 31.915382432114615)
close('Total finite incoming momentum', Iin, 3.133285343288751e-9)
close('Total finite incoming kinetic energy', Ein, 50e-9)
close('Payload mass in kg', mf, 2.33e-9)
close('Payload mass in micrograms', mf/1e-9, 2.33)
check('High-fracture-energy exclusion', .020*area > Esolid)
minimum_energy = .005*area+.5*mf*minimum_speed**2
required_impulse = mf*minimum_speed
close('Low-fracture-energy minimum total', minimum_energy, 5.29125e-9)
close('Minimum required net impulse', required_impulse, 1.165e-9)
check('Low-fracture-energy necessary screens', minimum_energy < Esolid and required_impulse < Inet)
vcm, kcm = Inet/mf, Inet**2/(2*mf)
close('Exact impulse implied payload speed', vcm, .6723788290319208)
close('Exact impulse implied kinetic energy', kcm, 5.266886825358426e-10)
check('Full actual-impulse energy compatibility', .005*area+kcm < Esolid)
m_A, J_A = 2330*1e-6, Inet/area
close('Areal velocity jump equals global translation', J_A/m_A, vcm)
close('Uniform areal kinetic integration equals CM energy', J_A**2/(2*m_A)*area, kcm)
close('One-degree placement error', 100e-6*math.tan(math.radians(1)), 1.7455064928217586e-6)

soup = BeautifulSoup(chapter04.CHAPTER['body'], 'html.parser')
eqs = [e for e in EQUATIONS if e['id'].startswith('C4-')]
check('Exactly 41 displayed equations', len(eqs) == 41)
check('Equation identifiers unique', len({e['id'] for e in eqs}) == len(eqs))
check('Exactly three defense questions', len(soup.select('article.defense')) == 3)
for q in soup.select('article.defense'):
    reference = q.select_one('details.answer')
    contents = [c for c in reference.children if getattr(c, 'name', None) and c.name != 'summary']
    check(q['id']+': formulas first', 'equation-unit' in contents[0].get('class', []))
    check(q['id']+': three semantic rubric criteria', len(reference.select('li')) == 3)
for eqn in eqs:
    check(eqn['id']+': local bilingual definitions and physical figure labels',
          bool(eqn['symbols_en'] and eqn['symbols_zh'] and eqn['diagram']['labels']))
    check(eqn['id']+': no control-character escape corruption',
          not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', eqn['tex']))
node = os.environ.get('NODE_BINARY') or shutil.which('node')
if node and Path(node).exists():
    rendered = subprocess.run([str(node), str(ROOT/'scripts/render_math.cjs')],
                              input=json.dumps([dict(tex=e['tex'], display=True) for e in eqs]),
                              text=True, encoding='utf-8', capture_output=True)
    check('All 41 equations pass strict KaTeX', rendered.returncode == 0, rendered.stderr[-1000:])
    if rendered.returncode == 0:
        check('All rendered displays returned', len(json.loads(rendered.stdout)) == len(eqs))
else:
    check('Strict KaTeX runtime available', False, 'Install Node.js or set NODE_BINARY')

prose = [p.get_text(' ', strip=True) for p in soup.select('p[lang="en"]')
         if not p.find_parent(class_='symbols') and not p.find_parent('figcaption')]
words = len(re.findall(r'\b[\w’-]+\b', ' '.join(prose)))

report = dict(
    chapter=4, date='2026-10-09', status='verified' if all(c['passed'] for c in checks) else 'needs-repair',
    equation_count=len(eqs), defense_question_count=3, english_prose_word_count=words,
    checks=checks,
    numerical_values=dict(
        D_f_Nm=D_v, critical_pressure_Pa=p_c, centre_deflection_m=wc,
        blister_volume_m3=volume_q, edge_bending_stress_Pa=sigma_edge,
        triangular_cohesive_peak_opening_m=d0, triangular_cohesive_final_opening_m=dc,
        carrier_mass_per_jet_kg=mj, jet_speed_m_s=speed, total_jet_energy_J=Ein,
        total_incoming_momentum_Ns=Iin, payload_mass_kg=mf, assigned_solid_energy_J=Esolid,
        assigned_net_impulse_Ns=Inet, high_fracture_release_cost_J=.020*area,
        low_fracture_minimum_cost_J=minimum_energy, minimum_required_impulse_Ns=required_impulse,
        actual_net_impulse_speed_m_s=vcm, actual_net_impulse_kinetic_energy_J=kcm,
        consistent_low_fracture_total_J=.005*area+kcm),
    source_verification=[
        dict(url='https://ocw.mit.edu/courses/2-080j-structural-mechanics-fall-2013/resources/mit2_080jf13_lecture7/',
             pdf_url='https://ocw.mit.edu/courses/2-080j-structural-mechanics-fall-2013/f8fd2ad49d100766335b4e129a8a4791_MIT2_080JF13_Lecture7.pdf',
             locator='Lecture 7, Eqs. 7.9, 7.15–7.24, 7.30–7.34; PDF pp. 1–4',
             support='Axisymmetric linear plate operator, regular clamped circular displacement and edge stress benchmark.',
             inspected='Primary university course notes, full extracted PDF text; no original PDF copied into public deliverables.'),
        dict(url='https://rogersgroup.northwestern.edu/files/2007/laprinting.pdf',
             doi='10.1021/la701555n', locator='Abstract and introduction, author-hosted Langmuir paper',
             support='Transfer printing as competing fracture with actual geometry, temperature and rate-dependent interface resistance.',
             limitation='No PDMS fitted values adopted for PFC/PVC teaching examples.'),
    ],
    original_derivations=[
        'Areal mass and bending stiffness from through-thickness integrals.',
        'Variational plate energy to transverse dynamic balance, including mixed-curvature coefficient cancellation.',
        'Both integration-by-parts boundary terms and fixed-clamp disappearance, plus the transient plate power identity.',
        'Exact pulse-integrated plate balance before the free-impulse approximation.',
        'Regular circular plate: all four integrations, singular constants excluded, clamp constants solved.',
        'Blister volume, source-inclusive pressure potential, radius-to-area derivative and critical pressure.',
        'Fixed-volume comparison: instantaneous expression and opposite propagation trends.',
        'Triangular cohesive branch work and positive softening-interval condition.',
        'Single consistent finite array release budget and actual-net-impulse energy compatibility.',
    ],
    semantic_audit=[
        'Solid-to-liquid traction normal produces compressive pressure stress but upward exposed-face force if liquid is beneath the film.',
        'Pressure maximum, applied impulse, net payload impulse, delivered work and opening traction are kept distinct.',
        'Intact PVC blocks passage; its transmitted traction remains an unknown contact/bond result.',
        'Two-sheet conditional model is not claimed as a fully bonded laminate bending model.',
        'Pretension, inertia, cohesive resistance and support reactions are omitted only where declared.',
        'Quasistatic source-inclusive potential is not applied as a dynamic jet fracture solution.',
        'Changing imposed control changes crack evolution despite same-state pressure expression.',
        'Compliance is defined by pressure derivative at fixed radius, with zero-load continuation rather than division by zero.',
        'Full release cost ΓA includes all intended area; lower fracture-energy example does not establish spatial crack completion.',
        'Exact actual net impulse implies 0.67238 m/s; 0.50 m/s is explicitly only a minimum requirement.',
        '2.33e-9 kg is 2.33 micrograms, not nanograms; geometry label corrected during second pass.',
        'Patterned/addressed equal optical allocation is retained; no broad Gaussian uniformity/interception mismatch introduced.',
        'All local displayed symbol declarations, units, diagram variables and bilingual meanings checked in a second pass.',
    ],
    unresolved=[
        'Actual absorption/jet efficiency and both useful-solid/net-impulse coupling fractions are not calibrated.',
        'Actual donor/release geometry, PVC contact/bond law and transmitted pressure history are not specified.',
        'Release strength, mixed-mode/rate/temperature fracture resistance, payload allowable stress and competing paths require data.',
        'The 10%-thickness/radius plate is a benchmark; finite-thickness, shear and large-deformation errors require refinement.',
        'Spatial crack coverage, puncture, rotation, landing adhesion and repeated cooling/condensation/inventory are not solved.',
        'Symbolic and numerical checks are self-audit controls, not an independent expert review or experimental validation.',
    ],
    cleanup='Ran with -B; KaTeX through pipes; no compile/temp intermediates generated by this worker.',
)
(ROOT/'verification/chapter04-review.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(dict(status=report['status'], passed=sum(c['passed'] for c in checks),
                      total=len(checks), equations=len(eqs), defenses=3, english_words=words)))
for c in checks:
    if not c['passed']:
        print(json.dumps(c, ensure_ascii=True))
raise SystemExit(0 if report['status'] == 'verified' else 1)
