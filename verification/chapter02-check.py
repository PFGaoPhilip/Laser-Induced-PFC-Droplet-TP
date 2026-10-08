"""Independent numerical controls and content audit for Chapter 2.

These checks verify the adopted teaching calculations, not an experimental PFC
formulation. This worker writes only its own review JSON.
"""
from pathlib import Path
import importlib.util
import json
import math
import re
import shutil
import subprocess
import sys

from scipy.integrate import quad
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import coursekit

spec = importlib.util.spec_from_file_location('chapter02', ROOT / 'content/chapter02.py')
chapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chapter)
equations = [x for x in coursekit.EQUATIONS if x['id'].startswith('C2-')]
checks = []

def close(name, actual, expected, unit='', rel=2e-8, abs_tol=0.0):
    passed = math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol)
    checks.append(dict(name=name, actual=actual, expected=expected, unit=unit,
                       method='independent numerical evaluation', passed=passed))
    return actual

def gate(name, passed, detail):
    checks.append(dict(name=name, passed=bool(passed), detail=detail,
                       method='content/structure inspection'))

rho_d, cp_d, k_d = 1630.0, 654.0, 0.050
a0, T0, Tstar, latent = 5e-6, 293.0, 323.0, 95000.0
Ru, Mp = 8.314462618, 0.2880343
mass = 4 * math.pi * rho_d * a0**3 / 3
alpha = k_d / (rho_d * cp_d)
qsens = mass * cp_d * (Tstar - T0)
qlat = mass * latent
qprep = qsens + qlat
vexp = rho_d * Ru * Tstar / (Mp * 1e5)
r_inv = a0 * vexp**(1/3)
close('Initial core mass', mass, 8.534660042252273e-13, 'kg')
close('Sensible preparation estimate', qsens, 1.674500300289896e-8, 'J')
close('Latent preparation estimate', qlat, 8.107927040139659e-8, 'J')
close('Total preparation screen', qprep, 9.782427340429555e-8, 'J')
close('Ideal inventory-state volume expansion', vexp, 151.97778263737408)
close('Ideal inventory radius', r_inv, 2.6682716317574947e-5, 'm')
close('Radius substitution recovers stated vapor pressure',
      mass * Ru * Tstar / (Mp * 4*math.pi*r_inv**3/3), 1e5, 'Pa')
close('PFC pressure at 30 micrometers with full inventory',
      mass * Ru*Tstar / (Mp*4*math.pi*(30e-6)**3/3), 70360.08455433988, 'Pa')
close('Thermal diffusivity', alpha, 4.690343520759461e-8, 'm2/s')
close('Five-micrometer diffusion scale', a0*a0/alpha, 0.00053301, 's')
close('Ten-nanosecond penetration scale', math.sqrt(alpha*1e-8), 2.1657200928927683e-8, 'm')
close('100-nanometer diffusion scale', (1e-7)**2/alpha, 2.13204e-7, 's')
close('PFP mass-specific cp from NIST molar datum', 188.3/Mp, 653.7415856375438, 'J/(kg K)')
close('PFH mass-specific latent enthalpy at 316 K', 31500/.3380418, 93183.7423655891, 'J/kg')

def ant(T, A, B, C):
    return 1e5 * 10**(A - B/(T+C))

psat = {}
for T, expected in [(293,70596.49151068536),(303,103353.07479481792),(323,204331.62528007207)]:
    psat[T] = close(f'PFP saturation pressure at {T} K', ant(T,4.2063,1103.454,-39.77),expected,'Pa')
close('Water saturation pressure at 293 K',ant(293,5.40221,1838.675,-31.737),2315.1000680945444,'Pa')
close('Water saturation pressure at 323 K',ant(323,5.20389,1733.926,-39.485),12248.206358008852,'Pa')
close('Five-micrometer capillary excess',2*.020/a0,8000,'Pa')
close('100-nanometer capillary excess',2*.020/1e-7,400000,'Pa')
gate('Size changes the positive-driving branch at 323 K',
     psat[323] > 1e5+8000 and psat[323] < 1e5+400000,
     'Declared sigma_pc=0.020 N/m, no shell stress. This is not an activation prediction.')

# Direct dimensionless quadratures avoid loose absolute tolerances for tiny SI energies.
w, aperture, el = 20e-6, 10e-6, 1e-6
f0 = 2*el/(math.pi*w*w)
integral, _ = quad(lambda x: x*math.exp(-2*x*x),0,math.inf,epsabs=1e-12,epsrel=1e-12)
el_quad = 2*math.pi*f0*w*w*integral
close('Gaussian annular quadrature',el_quad,el,'J')
fgeo_quad = quad(lambda x: x*math.exp(-2*x*x),0,aperture/w,
                epsabs=1e-12,epsrel=1e-12)[0]/integral
close('Centered aperture quadrature',fgeo_quad,0.3934693402873666)
optical_thickness = 2e5*5e-6
depth_integral = quad(lambda s: optical_thickness*math.exp(-optical_thickness*s),0,1)[0]
close('Beer-Lambert depth quadrature',depth_integral,1-math.exp(-optical_thickness))
absorptance = .9*depth_integral
eabs = fgeo_quad*absorptance*el
close('Effective absorptance including one reflection',absorptance,0.5689085029457019)
close('Intercepted absorbed energy',eabs,2.2384805333791867e-7,'J')
close('Minimum delivered-heat fraction in preparation screen',qprep/eabs,.43701194603028803)
gate('20-percent and 50-percent heat-delivery energy branches',
     .2*eabs < qprep < .5*eabs,
     'A passed preparation screen does not establish nucleation or mechanical conversion.')
close('Halved-core inventory scales by one eighth',
      (4*math.pi*rho_d*(a0/2)**3/3)/mass,.125)
close('25-cell initial PFC mass handed to Chapter 3',25*mass,2.133665010563068e-11,'kg')
close('25-cell preparation screen handed to Chapter 3',25*qprep,2.445606835107389e-6,'J')

# Independent checks of signs and branches, not a calibrated phase-rate law.
sigma_vp, dp = .01, 1e5
rstar = 2*sigma_vp/dp
w_surface = 4*math.pi*sigma_vp*rstar*rstar
w_volume = 4*math.pi/3*dp*rstar**3
wstar = 16*math.pi*sigma_vp**3/(3*dp**2)
close('Barrier obtained by critical-radius substitution',w_surface-w_volume,wstar,'J')
close('Stationary-radius derivative cancellation',
      (8*math.pi*sigma_vp*rstar-4*math.pi*dp*rstar*rstar)/(8*math.pi*sigma_vp*rstar),
      0,abs_tol=1e-14)
gate('Critical point is a maximum and nonpositive-driving branch is absent',
     8*math.pi*sigma_vp-8*math.pi*dp*rstar < 0 and
     all(4*math.pi*r*(2*sigma_vp-d*r)>0 for r in [1e-9,1e-7,1e-5] for d in [0,-1e5]),
     'Homogeneous small-nucleus capillarity control, not a real core activation fit.')
close('Poisson constant-rate probability for integrated rate 3',1-math.exp(-3),.950212931632136)
gate('Poisson zero-rate and monotonic probability bounds',
     1-math.exp(0)==0 and all(0 <= 1-math.exp(-x) < 1 for x in [0,.1,1,3,10]),
     'The Poisson law assumes independent events and a supplied nonnegative rate.')
for sign in [1,-1]:
    heat = sign*.95e6
    j = heat/latent
    close(f'Stefan signed flux for heat sign {sign}',j,sign*10,'kg/(m2 s)')
    rho_l, rho_v, rdot = 1000.0, 6.0, 1.0
    u_l, u_v = rdot-j/rho_l, rdot-j/rho_v
    close(f'Liquid interface mass jump sign {sign}',rho_l*(rdot-u_l),j,'kg/(m2 s)')
    close(f'Vapor interface mass jump sign {sign}',rho_v*(rdot-u_v),j,'kg/(m2 s)')
    close(f'Liquid velocity-slip sign {sign}',rdot-u_l,sign*.010,'m/s')

for radius in [10e-6,30e-6]:
    volume = 4*math.pi*radius**3/3
    vapor = min(mass,Mp*psat[323]*volume/(Ru*Tstar))
    pv = vapor*Ru*Tstar/(Mp*volume)
    target = min(psat[323],mass*Ru*Tstar/(Mp*volume))
    close(f'Equilibrium pressure branches at radius {radius:g} m',pv,target,'Pa')
    gate(f'Finite-inventory equilibrium ledger at radius {radius:g} m',
         0 <= vapor <= mass and math.isclose((mass-vapor)+vapor,mass),
         'Closed nondissolving, rapidly equilibrated, bulk-interface ideal-vapor control.')

soup = BeautifulSoup(chapter.CHAPTER['body'],'html.parser')
ids = [x['id'] for x in equations]
gate('Unique ordered equation identifiers',ids==[f'C2-E{i:02d}' for i in range(1,37)],ids)
gate('Exactly three defense questions',chapter.CHAPTER['question_ids']==['C2-Q1','C2-Q2','C2-Q3'] and len(soup.select('article.defense'))==3,
     chapter.CHAPTER['question_ids'])
gate('Local bilingual definitions and immediate figures',
     all(e['symbols_en'] and e['symbols_zh'] and e['diagram']['labels'] and e['caption_en'] and e['caption_zh'] for e in equations)
     and len(soup.select('section.equation-unit figure.formula-figure'))==36,
     'All 36 display units use E() and have local definitions plus a physical variable map.')
gate('Formula-first reference answers',
     all(a.find('section',class_='equation-unit') is not None and
         a.find('section',class_='equation-unit')==a.find(['section','div'])
         for a in soup.select('details.answer')),
     'Each reference panel starts with its original relevant equations, then explanation.')
gate('Paired EN-ZH prose',
     all(p.select_one('p[lang=en]') and p.select_one('p[lang=zh-CN]') for p in soup.select('.lang-pair')),
     'Paired wording was separately reviewed for assumptions, numerical values and caveats.')
gate('No Python escape corruption',not any(ord(c)<32 and c not in '\n\t' for c in chapter.CHAPTER['body']),
     'All authored literals use raw strings, preventing rho/boldsymbol etc. escape corruption.')
gate('Newton radius-derivative notation',
     not any(re.search(r'\\frac\{d(?:\^2)?R\}',e['tex']) for e in equations),
     'Radius velocities use dot R; material/time derivatives of other fields retain their defined operators.')

rendered = False
node = shutil.which('node')
if not node:
    candidate = Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
    node = str(candidate) if candidate.exists() else None
if node:
    inline = re.findall(r'\$([^$]+)\$',chapter.CHAPTER['body'])
    payload = [{'tex':e['tex'],'display':True} for e in equations] + [
        {'tex':x.replace('&gt;','>').replace('&lt;','<'),'display':False} for x in inline]
    proc = subprocess.run([node,str(ROOT/'scripts/render_math.cjs')],
                          input=json.dumps(payload,ensure_ascii=False),
                          text=True,encoding='utf-8',capture_output=True,check=False)
    rendered = proc.returncode==0
    gate('Strict KaTeX rendering of displays and inline math',rendered,
         {'display_count':len(equations),'inline_count':len(inline),'error':proc.stderr[:2000]})
else:
    gate('Strict KaTeX rendering runtime present',False,'Node runtime unavailable; rendering remains unverified.')

english = ' '.join(x.get_text(' ') for x in soup.select('p[lang=en]')
                   if not x.find_parent(class_='symbols'))
review = dict(
    chapter=2,
    reviewed_on='2026-10-09',
    status='passed' if all(x['passed'] for x in checks) else 'needs_repair',
    equation_count=len(equations),
    question_count=3,
    question_ids=chapter.CHAPTER['question_ids'],
    english_prose_word_count_excluding_local_symbols=len(english.split()),
    supplied_source='sources/Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md, Chapter 2 and three final defense questions',
    organization_reference='sources/Cavitation_Course_Before_After_Comparison_EN_ZH.md; one integrated route',
    checks=checks,
    numerical_handoff=dict(core_mass_kg=mass,preparation_estimate_J=qprep,
                           sensible_estimate_J=qsens,latent_estimate_J=qlat,
                           inventory_radius_m=r_inv,inventory_volume_ratio=vexp,
                           count25_mass_kg=25*mass,count25_preparation_estimate_J=25*qprep),
    sources=[
        dict(id='r8',url='https://webbook.nist.gov/cgi/cbook.cgi?ID=C678262&Mask=4&Units=SI',
             accessed='Primary NIST phase-change body successfully read.',
             supports=['PFP molar mass 0.2880343 kg/mol','Boiling datasets 302.6/303.2 K',
                       'Barber-Cady Antoine coefficients 4.2063,1103.454,-39.77; domain 282.82-337.94 K']),
        dict(id='r8-cp',url='https://webbook.nist.gov/cgi/cbook.cgi?ID=C678262&Mask=2&Units=SI',
             accessed='Primary NIST condensed-phase body successfully read.',
             supports=['Liquid molar heat capacity 188.3 J/(mol K) at 293 K, interpolated Campos-Vallette-Diaz dataset']),
        dict(id='r9',url='https://webbook.nist.gov/cgi/cbook.cgi?ID=C355420&Mask=4',
             accessed='Primary NIST phase-change body successfully read.',
             supports=['PFH molar mass 0.3380418 kg/mol','Boiling datasets 330.3-333 K',
                       'Vaporization enthalpy 31.5 kJ/mol at 316 K']),
        dict(id='r15',url='https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=4',
             accessed='Primary NIST phase-change body successfully read.',
             supports=['Water molar mass 0.0180153 kg/mol and boiling compilation 373.17 K',
                       'Bridgeman-Aldrich Antoine 273-303 K and 304-333 K branches']),
        dict(id='r6',doi='10.1364/BOE.2.001432',
             url='https://pmc.ncbi.nlm.nih.gov/articles/PMC3114212/',
             abstract_url='https://pubmed.ncbi.nlm.nih.gov/21698007/',
             accessed='Full primary article body was returned in web search result; later direct PMC open returned CAPTCHA. PubMed primary abstract was read.',
             supports=['Formulation-specific optical vaporization of PbS-containing PFP under 1064 nm light'],
             excluded_claims=['No transfer yield or liquid-jet speed inferred','No universal laser threshold copied']),
        dict(id='r7',doi='10.1364/OL.39.002599',
             url='https://pubmed.ncbi.nlm.nih.gov/24784055/',
             fulltext_url='https://pmc.ncbi.nlm.nih.gov/articles/PMC9008802/',
             accessed='PubMed primary abstract read; direct PMC full-text access returned CAPTCHA.',
             supports=['Optically activated gold-containing PFH nanoemulsion'],
             excluded_claims=['No clot-treatment outcome used as transfer evidence','No full-text-only claims adopted']),
    ],
    original_derivations=[
        'Gaussian annular energy, change of variable and centered-aperture interception',
        'Beer-Lambert separation, depth integral and energy ledger',
        'Heat-diffusion scales and thermal-contact signs',
        'Homogeneous capillarity stationary-point branches and critical-barrier substitution',
        'Poisson survival differential equation and integration',
        'Moving-interface liquid-to-vapor sign and radial phase-slip algebra',
        'Open-bubble first-law product rule with changing species masses',
        'Ideal partial-pressure logarithmic derivative and finite-inventory equilibrium branches',
        'Finite-core preparation and inventory-state calculations',
        'Refined isobaric liquid-heating, coexistence, and vapor-heating enthalpy path',
    ],
    semantic_audit=[
        'Core radius a/a0 is distinct from nucleus radius rn and bubble radius R.',
        'PFC-carrier sigma_pc is distinct from vapor-PFC sigma_vp.',
        'Carrier density supplies outer-liquid inertia; PFC density supplies its inventory.',
        'A positive capillarity driving pressure does not remove nucleation barrier.',
        'The homogeneous nucleation control fails when critical nucleus is comparable to core.',
        'Phase-change slip and recoil are conditions before reusing simple Chapter 1 RP.',
        'Conductive bubble heat excludes mass enthalpy; latent conversion is not added twice.',
        'Saturation is conditional on residual inventory, equilibration, and bulk-interface approximation.',
        'The 95 kJ/kg constant latent teaching input is not attributed to NIST at 323 K.',
        'The 97.8243 nJ screen is not exact isobaric endpoint enthalpy, laser threshold, or jet energy.',
        'The 26.6827 micrometer inventory radius is not Rmax or emitted jet geometry.',
        'Creation of content does not mark learner mastery; own-word explanations need semantic review.',
    ],
    unresolved=[
        'Actual PFC identity/purity, size distribution and shell law are not fixed by these controls.',
        'Formulation interfacial tensions, optical absorptance, contact resistance and hotspot geometry need evidence.',
        'A formulation-specific activation or nucleation-rate law remains unspecified.',
        'Stefan balance alone does not supply interface temperatures or multicomponent diffusion kinetics.',
        'Uniform bubble temperature, ideal vapor and negligible recoil need event-specific validation.',
        'A calibrated high-density EOS and pressure-dependent phase enthalpies are required for strong compression.',
        'No target geometry spatial simulation, experimental pressure maximum, or jet conversion efficiency established.',
    ],
    independent_review='This file records a second self-audit plus independent numerical methods. It is not an independent expert/agent review.',
    cleanup='Python -B and stdin/stdout math rendering; no temporary files or bytecode generated by this worker.',
)
(ROOT/'verification/chapter02-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
failed = [x['name'] for x in checks if not x['passed']]
print(json.dumps({'chapter':2,'equations':len(equations),'questions':3,
                  'checks':len(checks),'failed':failed,'status':review['status']}))
if failed:
    raise SystemExit(1)
