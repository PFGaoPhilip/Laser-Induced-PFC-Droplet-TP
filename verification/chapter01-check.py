"""Independent numerical and structural controls for authored Chapter 1.

This is a check of stated reduced models, not an experimental validation or
an independent expert review. Run with Python -B to avoid compile products.
"""
from pathlib import Path
import importlib.util
import sys
import json
import math
import re
import hashlib
from scipy.integrate import quad
from scipy.special import beta
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("chapter01", ROOT / "content/chapter01.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
from coursekit import EQUATIONS

checks = []


def close(name, actual, expected, rel=2e-11, abs_tol=1e-12):
    passed = math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol)
    checks.append({"name": name, "actual": actual, "expected": expected,
                   "relative_tolerance": rel, "absolute_tolerance": abs_tol,
                   "passed": passed})
    if not passed:
        raise AssertionError(f"{name}: {actual} != {expected}")


def gate(name, condition, detail):
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


# Beta evaluation and a separate direct quadrature of radius-fraction integral.
ct_beta = beta(5/6, 1/2) / math.sqrt(6)
ct_direct = math.sqrt(3/2) * quad(
    lambda x: x**1.5 / math.sqrt(1-x**3), 0, 1,
    epsabs=2e-12, epsrel=2e-12)[0]
close("Rayleigh coefficient: direct radius integral versus beta", ct_direct, ct_beta)
close("Rayleigh coefficient: published benchmark", ct_beta, 0.9146813565019628)

rho, dp, rmax = 1000.0, 100e3, 30e-6
tc = ct_beta*rmax*math.sqrt(rho/dp)
eb = 4*math.pi/3*dp*rmax**3
speed = -math.sqrt(2*dp/(3*rho)*(8-1))
kh = 2*math.pi*rho*(rmax/2)**3*speed**2
close("Source collapse-time example (seconds)", tc, 2.7440440695058887e-6)
close("Source pressure-work example (joules)", eb, 11.309733552923255e-9)
close("Source inward speed at half radius", speed, -21.602468994692867)
close("Half-radius kinetic energy equals 7/8 of maximum pressure work", kh, 7*eb/8, abs_tol=1e-20)

# Direct substitution into the governing equation at three nonsingular radii.
for x in (0.9, 0.5, 0.2):
    radius = rmax*x
    speed_sq = 2*dp/(3*rho)*(x**-3-1)
    accel = -dp/rho*rmax**3/radius**4
    close(f"Rayleigh governing-equation residual at R/Rmax={x}",
          radius*accel+1.5*speed_sq, -dp/rho)
    kinetic = 2*math.pi*rho*radius**3*speed_sq
    close(f"Conservation: kinetic energy versus lost-volume work at {x}",
          kinetic, eb*(1-x**3), abs_tol=1e-20)

# Potential derivatives: one manufactured smooth radius law, independent
# central differences, using a fixed observation radius and a moving point.
radius0, speed0, accel0, obs_radius = 1.0, 2.0, 3.0, 2.0
def radiuslaw(t):
    return radius0+speed0*t+0.5*accel0*t*t
def speedlaw(t):
    return speed0+accel0*t
def fixed_phi(t):
    return -radiuslaw(t)**2*speedlaw(t)/obs_radius
def wall_phi(t):
    return -radiuslaw(t)*speedlaw(t)
delta=1e-6
fixed_num=(fixed_phi(delta)-fixed_phi(-delta))/(2*delta)
wall_num=(wall_phi(delta)-wall_phi(-delta))/(2*delta)
close("Fixed-position potential time derivative", fixed_num,
      -(2*radius0*speed0**2+radius0**2*accel0)/obs_radius, rel=2e-10)
close("Moving-wall potential time derivative", wall_num,
      -(speed0**2+radius0*accel0), rel=2e-10)

# Nondimensional exterior quadratures avoid numerical issues from micrometer
# integration bounds and independently verify the spatial integration factors.
i_energy=quad(lambda z:z**-2,1,math.inf,epsabs=1e-12)[0]
i_visc=quad(lambda z:z**-4,1,math.inf,epsabs=1e-12)[0]
close("Exterior kinetic shell integral", i_energy, 1.0)
close("Exterior strain-dissipation shell integral", i_visc, 1/3)
radius=rmax/2; viscosity=.001
diss_by_integral=48*math.pi*viscosity*radius*speed**2*i_visc
diss_by_energy=16*math.pi*viscosity*radius*speed**2
close("Viscous dissipation recovered from radial strain integral", diss_by_integral, diss_by_energy)

# Check the energy identity with all capillary and viscous terms retained.
radius, speed, sigma, pb, pinf = 50e-6, -20.0, .072, 8000.0, 100000.0
rhs=pb-pinf-2*sigma/radius-4*viscosity*speed/radius
accel=(rhs/rho-1.5*speed**2)/radius
lhs_energy=2*math.pi*rho*(3*radius**2*speed**3+2*radius**3*speed*accel)+8*math.pi*sigma*radius*speed
rhs_energy=(pb-pinf)*4*math.pi*radius**2*speed-16*math.pi*viscosity*radius*speed**2
close("Full RP energy identity including viscous and capillary terms", lhs_energy, rhs_energy)
close("Full RP stress sign for inward velocity", -4*viscosity*speed/radius, 1600.0)

c, m_star=1500.0,.1
x_m=(1+3*rho*c*c*m_star*m_star/(2*dp))**(-1/3)
mach_at_x=math.sqrt(2*dp/(3*rho)*(x_m**-3-1))/c
close("Selected ideal-trajectory Mach diagnostic radius fraction", x_m, 0.14348740311819275)
close("Ideal wall Mach equals chosen diagnostic at that radius", mach_at_x, m_star)

duration,length,delta_p=.50e-6,100e-6,.60e6
impulse=delta_p*duration
u_column=impulse/(rho*length)
ta=length/c
nu=viscosity/rho
close("Column pressure impulse",impulse,.30)
close("Column speed increment",u_column,3.0)
close("Sound-crossing time in seconds",ta,6.666666666666667e-8,abs_tol=1e-18)
close("Column displacement diagnostic",u_column*duration/length,.015)
close("Column viscous-impulse diagnostic",nu*duration/length**2,5e-5)
close("Number of acoustic crossings during pulse",duration/ta,7.5)
for z in (0.0,length/3,length):
    pi=impulse*(1-z/length)
    close(f"Straight-column linear impulse at z/L={z/length:g}",pi,.30*(1-z/length))

soup=BeautifulSoup(mod.body,"html.parser")
ids=[q["id"] for q in EQUATIONS]
gate("Unique equation IDs",len(ids)==len(set(ids)),ids)
gate("Sequential complete equation IDs",ids==[f"C1-E{n:02d}" for n in range(1,35)],ids)
gate("Exactly three defense questions",len(soup.select("article.defense"))==3,mod.CHAPTER["question_ids"])
for entry in EQUATIONS:
    gate(entry["id"]+" bilingual local definitions",bool(entry["symbols_en"]) and bool(entry["symbols_zh"]),"Local declarations supplied before the display")
    gate(entry["id"]+" immediate physical diagram",bool(entry["diagram"]["labels"]) and bool(entry["diagram"]["notes"]),entry["diagram"])
for q in soup.select("article.defense"):
    first=q.select_one("details.answer").find(recursive=False)
    gate(q["id"]+" formulas first in reference answer",first is not None and first.name=="summary", "The first substantive content follows the summary")
    first_section=q.select_one("details.answer > section")
    gate(q["id"]+" original formula section present",first_section is not None,first_section.get("id") if first_section else None)

en_prose=" ".join(p.get_text(" ",strip=True) for p in soup.select('p[lang="en"]') if not p.find_parent(class_="symbols"))
en_all=" ".join(p.get_text(" ",strip=True) for p in soup.select('p[lang="en"]'))
report={
    "chapter":1,
    "status":"passed",
    "equation_count":len(ids),
    "defense_question_count":3,
    "english_prose_words_excluding_local_definitions":len(re.findall(r"\b[\w'-]+\b",en_prose)),
    "english_words_including_local_definitions":len(re.findall(r"\b[\w'-]+\b",en_all)),
    "check_count":len(checks),
    "checks":checks,
    "source_sha256":hashlib.sha256((ROOT/"sources/Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md").read_bytes()).hexdigest(),
    "comparison_sha256":hashlib.sha256((ROOT/"sources/Cavitation_Course_Before_After_Comparison_EN_ZH.md").read_bytes()).hexdigest(),
    "primary_sources_visited":[
        {"url":"https://media.library.caltech.edu/CaltechBOOK%3A1995.001/chap2.htm","support":"Classical spherical flow and normal stress; gas/thermal/compressibility limits. The chapter's algebra is worked anew from conservation.","access":"Full chapter text"},
        {"url":"https://arxiv.org/html/1703.01088","support":"Published Rayleigh factor beta integral, symmetry and boundary dependence of collapse jets; not used as a PFC calibration.","access":"Full article HTML"},
        {"url":"https://research-portal.uea.ac.uk/en/publications/pressure-impulse-theory-for-liquid-impact-problems/","support":"Cooker and Peregrine 1995 publication identity/DOI. Reduced model and omitted terms are derived explicitly here.","access":"Author university bibliographic record"},
        {"url":"https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/pressureimpulse-theory-for-liquid-impact-problems/CA64B545C3897DB7F783834C00B5469D","support":"Primary publisher metadata and pressure-impulse abstract/search result.","access":"Publisher result; DOI open initially failed"},
        {"url":"https://ivopeters.org/wp-content/uploads/2014/11/2013-highly-focused-supersonic-microjets-numerical-simulations.pdf","support":"Author-hosted paper verifies meniscus-focused jet differs from void-collapse jet, and potential-flow moving-boundary formulation. No experimental speed/efficiency imported to target PFC.","access":"Full author-hosted PDF text, not downloaded or published"},
    ],
    "repaired_derivation_gaps":[
        "Eulerian fixed-position potential derivative is shown before evaluation at the moving wall; material derivative distinguished explicitly.",
        "Newtonian radial strain and interface normal traction produce the capillary and viscous terms with checked signs.",
        "Exterior kinetic integral, product-rule derivative, and positive viscous dissipation are worked and cross-checked independently by strain integration.",
        "Rayleigh monotonic-branch cancellation excludes the initial zero-speed point and is extended continuously; integration constant, negative root and Jacobian are explicit.",
        "Collapse coefficient obtained by direct integral and beta function; ideal kinetic energy equals lost-volume pressure work.",
        "Pressure-impulse reduction contains explicit convective and viscous residuals before approximation and derives the harmonic field and straight-column endpoint solution.",
        "Spatial liquid-to-gas curvature convention, kinematic/normal/tangential stress conditions, Eulerian/material Bernoulli derivatives and spherical recovery are explicit.",
    ],
    "semantic_second_pass":{
        "method":"Author reconstruction from each equation to preceding definitions/premises; numerical controls supplement it. No independent expert review claimed.",
        "items_checked":["Every E() has EN/ZH local definitions and physical diagram metadata.","Pressure differences have references; EOS/partial pressures remain absolute.","Carrier density differs from PFC inventory density.","Real phase transfer is deferred explicitly rather than hidden in fixed-mass gas closure.","No external acoustic resonance curriculum introduced.","Point singularity not used as universal pressure or jet-speed maximum.","Pressure impulse and sound-crossing time have distinct dimensions.","The integrated teaching route leads directly to Chapter 2, with no parallel foundational entry path.","Exactly three chapter defenses and no additional quizzes; reference answers quote original formulas first."]},
    "remaining_limits":[
        "No calibrated optical/PFC thermodynamic pressure history, experimental target geometry or jet-conversion efficiency is assumed.",
        "No numerical moving-interface solution for a particular target is supplied; its closed boundary-value problem is stated.",
        "The ideal zero-radius trajectory and chosen Mach diagnostic do not predict physical arrest or an achievable maximum.",
        "Short-impulse residual ratios are scale diagnostics, not strict errors for singular wall layers/contact lines.",
        "Jet self-impact/topology, compressibility, finite arriving mass and receiver load require subsequent project stages.",
        "New chapter content is pending learner mastery; writing or saving responses does not certify understanding.",
    ],
    "compile_cleanup":"Run with -B; no bytecode, temporary math files or downloaded PDFs created by this worker. Parent owns combined build and project log.",
}
target=ROOT/"verification/chapter01-review.json"
target.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({key:report[key] for key in ("status","equation_count","defense_question_count","english_prose_words_excluding_local_definitions","english_words_including_local_definitions","check_count")},indent=2))
