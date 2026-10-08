"""Independent arithmetic, conservation, ODE and content controls for Chapter 3.

Run with python -B verification/chapter03-check.py. This never writes scratch.
It checks the declared reduced models, not target-geometry experimental validity.
"""
import importlib.util
import json
import math
from pathlib import Path
import re
import sys

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import minimize_scalar
from scipy.special import beta, iv
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from coursekit import EQUATIONS

checks = []
numbers = {}


def check(name, passed, detail=None):
    checks.append({"name": name, "passed": bool(passed), "detail": detail})


def close(name, actual, expected, rtol=1e-6, atol=0):
    passed = math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol)
    check(name, passed, {"actual": float(actual), "expected": float(expected)})


# 1. Independent finite activation and Gaussian control.
nd, pa = 25, 0.95
probabilities = np.array([math.comb(nd, n) * pa**n * (1-pa)**(nd-n)
                          for n in range(nd+1)])
mean = float(np.arange(nd+1) @ probabilities)
variance = float(((np.arange(nd+1)-mean)**2) @ probabilities)
close("Binomial probabilities normalize", float(sum(probabilities)), 1, rtol=1e-12)
close("Binomial mean", mean, 23.75, rtol=1e-12)
close("Binomial variance", variance, nd*pa*(1-pa), rtol=1e-12)
close("Activation relative standard deviation", math.sqrt(variance)/mean,
      0.04588314677411235, rtol=1e-12)
close("Complete activation probability", probabilities[-1], 0.27738957312183377,
      rtol=1e-12)
beam_ratio = math.sqrt(2 / -math.log(0.9))
close("Gaussian 10 percent edge decrease", math.exp(-2/beam_ratio**2), 0.9,
      rtol=1e-12)
close("Gaussian width multiplier", beam_ratio, 4.356884570660532, rtol=1e-12)
close("Broad Gaussian enclosing-circle intercepted fraction", 1-math.exp(-2/beam_ratio**2),
      0.1, rtol=1e-12)
numbers["uniformity"] = dict(mean_count=mean, count_variance=variance,
                            count_cv=math.sqrt(variance)/mean, all_active=pa**nd,
                            gaussian_radius_multiplier=beam_ratio)

# 2. Polygon geometry computed from Cartesian points, independently of chord formula.
Rmax, pitch, rho, dp = 30e-6, 200e-6, 1000.0, 1e5
gold = (1+math.sqrt(5))/2
expressions = {3: 2/pitch, 4: (2+1/math.sqrt(2))/pitch,
               5: (2+2/gold)/pitch}
cluster_rows = []
chis = [0]
for n in (3, 4, 5):
    radius = pitch / (2*math.sin(math.pi/n))
    points = np.array([[radius*math.cos(2*math.pi*i/n),
                        radius*math.sin(2*math.pi*i/n)] for i in range(n)])
    sums = [sum(1/np.linalg.norm(points[i]-points[j]) for j in range(n) if i!=j)
            for i in range(n)]
    close(f"Cartesian polygon reciprocal sum N={n}", sums[0], expressions[n],
          rtol=1e-12)
    check(f"Every polygon vertex has the same sum N={n}",
          max(sums)-min(sums)<1e-10)
    chi = expressions[n]*Rmax
    chis.append(chi)
    cluster_rows.append({"n": n, "S_per_m": expressions[n], "chi": chi})


def coefficient(chi, lower=0):
    return math.sqrt(1.5) * quad(
        lambda x: math.sqrt(x**3*(1+chi*x)/(1-x**3)), lower, 1,
        epsabs=1e-12, epsrel=1e-12)[0]


cs = [coefficient(chi) for chi in chis]
close("Isolated quadrature equals beta evaluation", cs[0],
      math.sqrt(1.5)*beta(5/6, 0.5)/3, rtol=1e-11)
check("Collapse coefficient increases across declared chi controls",
      all(cs[i+1]>cs[i] for i in range(len(cs)-1)))
expected_times = [2.744044069470488, 3.059509122642131,
                  3.163188115749175, 3.238492002894017]
for n, chi, ccoef, time in zip((1,3,4,5), chis, cs, expected_times):
    close(f"Formal collapse time N={n}", Rmax*math.sqrt(rho/dp)*ccoef*1e6,
          time, rtol=1e-10)

    # Integrate the original dimensionless second-order ODE without using y(R).
    def ode(t, state):
        x, v = state
        return [v, (-1-(1.5+2*chi*x)*v*v)/(x*(1+chi*x))]

    def stop(t, state):
        return state[0]-0.005

    stop.terminal, stop.direction = True, -1
    sol = solve_ivp(ode, (0, 2), [1, 0], events=stop,
                    rtol=2e-10, atol=1e-12, max_step=0.006)
    check(f"Original radial ODE reaches finite cutoff N={n}",
          sol.success and len(sol.t_events[0])==1)
    close(f"Original ODE time versus radius quadrature N={n}",
          sol.t_events[0][0], coefficient(chi, 0.005), rtol=5e-9)
    x, v = sol.y_events[0][0]
    predicted_v2 = 2/3*(1-x**3)/(x**3*(1+chi*x))
    close(f"Original ODE velocity versus integrated solution N={n}",
          v*v, predicted_v2, rtol=2e-8)
    close(f"Shared kinetic-energy budget at cutoff N={n}",
          x**3*(1+chi*x)*v*v, 2/3*(1-x**3), rtol=2e-8)

fixed_total = []
for n in (3,4,5):
    rn = Rmax/n**(1/3)
    chi = expressions[n]*rn
    tn = rn*math.sqrt(rho/dp)*coefficient(chi)
    close(f"Fixed total initial work N={n}", n*4*math.pi/3*dp*rn**3,
          4*math.pi/3*dp*Rmax**3, rtol=1e-12)
    fixed_total.append({"n":n, "radius_um":rn*1e6, "chi":chi, "time_us":tn*1e6})
numbers["clusters"] = {"chi":chis, "C":cs, "times_us":expected_times,
                       "fixed_total_work":fixed_total}
center_sum, outer_sum = 4/pitch, (1+0.5+math.sqrt(2))/pitch
check("Five-bubble cross cannot use a single equal-radius trajectory",
      not math.isclose(center_sum, outer_sum))

# 3. Nozzle, finite-mass momentum and energy.
ain, aj, sig, mu = 40e-6, 10e-6, 0.072, 0.001
alpha = (aj/ain)**2
uj = 3/alpha
pressure = 0.5*rho*(uj*uj-3*3)+sig/aj
close("Fixed-flow nozzle outlet speed", uj, 48, rtol=1e-12)
close("Fixed-flow required overpressure", pressure, 1.1547e6, rtol=1e-12)
upressure = math.sqrt(2*(0.2e6-sig/aj)/(rho*(1-alpha**2)))
close("Fixed-pressure nozzle outlet speed", upressure, 19.67516599327043,
      rtol=1e-9)
close("Fixed-pressure nozzle continuity", upressure*math.pi*aj*aj,
      alpha*upressure*math.pi*ain*ain, rtol=1e-12)
close("Fixed-impulse lower-mass energy ratio", 1/(2*0.25)/(1/2), 4, rtol=1e-12)
close("Fixed-energy lower-mass momentum ratio", math.sqrt(0.25), 0.5, rtol=1e-12)
mass_elements = np.array([1, 2, 3], dtype=float)
velocity_elements = np.array([[-1, 0, 10], [3, 0, 20], [0, 5, 30]], dtype=float)
energy = 0.5*float(np.sum(mass_elements*np.sum(velocity_elements**2,axis=1)))
momentum = float(mass_elements@velocity_elements[:,2])
check("Nonuniform velocity satisfies strict finite-mass momentum bound",
      momentum**2 < 2*float(sum(mass_elements))*energy)
numbers["nozzle"] = {"fixed_flow_required_Pa":pressure,
                     "fixed_pressure_speed_m_per_s":upressure,
                     "fixed_pressure_inlet_m_per_s":alpha*upressure}

# 4. Carry the source's independently supplied 25-cell output.
laser, interception, absorption, eta = 25e-6, 0.8, 0.5, 0.005
abs_total = laser*interception*absorption
abs_site = abs_total/25
ej = eta*abs_site
d, length, gap, c = 10e-6, 50e-6, 100e-6, 1480.0
area = math.pi*d*d/4
mass = rho*area*length
speed = math.sqrt(2*ej/mass)
mom = mass*speed
num = {"absorbed_total_J":abs_total, "absorbed_site_J":abs_site,
       "deadline_core_heat_J":0.4*abs_site, "jet_energy_J":ej,
       "total_jet_energy_J":25*ej, "mass_kg":mass, "mass_ng":mass*1e12,
       "total_mass_kg":25*mass, "speed_m_per_s":speed,
       "dynamic_Pa":0.5*rho*speed**2, "rigid_early_Pa":rho*c*speed,
       "momentum_N_s":mom, "total_momentum_N_s":25*mom,
       "volume_pL":area*length*1e15, "emission_s":length/speed,
       "flight_s":gap/speed, "equivalent_early_s":length/c,
       "side_release_s":d/(2*c), "wall_hammer_emission_impulse_ratio":c/speed,
       "Mach":speed/c, "Re":rho*speed*d/mu,
       "We":rho*speed*speed*d/sig, "Oh":mu/math.sqrt(rho*sig*d)}
close("Independent-cell energy allocation", ej, 2e-9, rtol=1e-12)
close("Finite carrier mass", mass, 3.926990816987241e-12, rtol=1e-12)
close("Uniform emitted speed", speed, 31.915382432114615, rtol=1e-12)
close("Early rigid-contact pressure scale", rho*c*speed, 47234765.99952963,
      rtol=1e-12)
close("Total aligned momentum", 25*mom, 3.133285343288751e-9, rtol=1e-12)
check("Emitted carrier volume respects supplied 50-pL inventory", num["volume_pL"]<50)
close("Rigid impulse-equivalent rectangle matches finite momentum",
      rho*c*speed*area*length/c, mom, rtol=1e-12)
close("Steady redirecting force times passage time matches finite momentum",
      rho*area*speed*speed*length/speed, mom, rtol=1e-12)
close("Receiver-impedance rigid limit",
      (rho*c)*(1e15)/(rho*c+1e15)*speed, rho*c*speed, rtol=1e-8)
check("Soft-receiver contact pressure tends toward zero",
      (rho*c)*1e-6/(rho*c+1e-6)*speed < 1e-3)

# 5. Independently maximize the exact inviscid-cylinder relation.
a = d/2
tcap = math.sqrt(rho*a**3/sig)
def growth_dimensionless(q):
    return math.sqrt(q*(1-q*q)*iv(1,q)/iv(0,q))
opt = minimize_scalar(lambda q: -growth_dimensionless(q), bounds=(1e-8,1-1e-8),
                      method="bounded", options={"xatol":1e-14})
qmax = opt.x
gmax = growth_dimensionless(qmax)/tcap
close("Fastest cylinder dimensionless wavenumber", qmax, 0.6970188977, rtol=1e-7)
close("Fastest dimensionless cylinder growth", gmax*tcap, 0.343338701861,
      rtol=1e-10)
close("Radius-based capillary time", tcap, 1.317615691736825e-6, rtol=1e-12)
arrival = 0.01*math.exp(gmax*gap/speed)
linear_time = math.log(10)/gmax
formal_time = math.log(100)/gmax
close("Arrival disturbance relative to radius", arrival, 0.022624723819386,
      rtol=1e-10)
close("Small 10-percent-radius threshold time", linear_time, 8.836528575626e-6,
      rtol=1e-10)
close("Formal full-radius extrapolation is twice linear threshold time",
      formal_time, 2*linear_time, rtol=1e-12)
check("Declared cylinder control survives flight to small threshold",
      gap/speed<linear_time and arrival<0.1)
num.update({"capillary_time_s":tcap, "qmax":qmax,
            "growth_max_per_s":gmax, "fastest_wavelength_m":2*math.pi*a/qmax,
            "arrival_relative_radius":arrival, "small_threshold_s":linear_time,
            "formal_full_radius_extrapolation_s":formal_time})
numbers["independent_25_cell_control"] = num

# 6. Authored-source structure. This does not claim full physics verification.
chapter_source = ROOT/"content"/"chapter03.py"
source = chapter_source.read_text(encoding="utf-8")
compile(source, str(chapter_source), "exec")
spec = importlib.util.spec_from_file_location("chapter03", chapter_source)
chapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chapter)
equations = [e for e in EQUATIONS if e["id"].startswith("C3-")]
soup = BeautifulSoup(chapter.CHAPTER["body"], "html.parser")
check("Exactly three defense questions", len(soup.select("article.defense"))==3)
check("Chapter defense IDs unique and expected",
      chapter.CHAPTER["question_ids"]==["C3-Q1","C3-Q2","C3-Q3"])
check("Exactly 33 uniquely identified displays",
      len(equations)==33 and len(set(e["id"] for e in equations))==33)
check("Every display has local EN/ZH definitions and diagram labels",
      all(e["symbols_en"] and e["symbols_zh"] and e["diagram"]["labels"]
          and e["diagram"]["notes"] for e in equations))
check("Every reference answer starts with original formula",
      all([child for child in x.select_one("details.answer").find_all(recursive=False)
           if child.name!="summary"][0].name=="section"
          for x in soup.select("article.defense")))
check("No accidental control characters in authored HTML",
      not any(ord(ch)<32 and ch not in "\n\t\r" for ch in chapter.CHAPTER["body"]))
check("Public citation links contain no local computer paths",
      not any(re.search(r"(?i)^(file:|[A-Z]:[\\/])", x.get("href",""))
              for x in soup.find_all("a")))
check("Separate patterned illumination explicitly declared",
      "Ideal patterned/addressed illumination" in chapter.CHAPTER["body"])
check("Per-jet and total mass labels use ng rather than pg",
      "3.926991 ng" in source and "98.17477 ng" in source
      and "3.926991 pg" not in source)
english_words = sum(len(re.findall(r"\b[\w'-]+\b", x.get_text()))
                    for x in soup.select('[lang="en"]'))
report = {"status":"pass" if all(x["passed"] for x in checks) else "fail",
          "checks_count":len(checks), "checks":checks, "numerical_results":numbers,
          "equations":len(equations), "questions":3,
          "english_words_including_local_definitions":english_words}
print(json.dumps(report,ensure_ascii=False,indent=2))
if report["status"]!="pass":
    raise SystemExit(1)
