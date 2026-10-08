"""Independent analytical/numerical controls for the Chapter 5 teaching model.

No target PFC hydrogel is simulated and no experimental validation is claimed.
"""
from pathlib import Path
import importlib.util
import json
import math
import re
import sys

from scipy.integrate import quad
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import coursekit

spec = importlib.util.spec_from_file_location("chapter05_check_content", ROOT / "content/chapter05.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
chapter = module.CHAPTER
eqs = [e for e in coursekit.EQUATIONS if e["id"].startswith("C5-")]
checks = []


def check(name, passed, detail):
    checks.append({"name": name, "passed": bool(passed), "detail": detail})
    if not passed:
        raise AssertionError(name)


def near(name, computed, expected, rel=1e-9, abs_tol=1e-16):
    check(name, math.isclose(computed, expected, rel_tol=rel, abs_tol=abs_tol),
          {"computed": computed, "expected": expected, "relative_tolerance": rel})


G = 20000.0
A = 5e-6
R = 30e-6
rho = 1000.0


def p_el(radius):
    return G / 2 * (5 - 4 * A / radius - (A / radius)**4)


def stored(radius):
    return 2 * math.pi * G * (5 * radius**3 / 3 - 2 * A * radius**2
                             + A**4 / radius - 2 * A**3 / 3)


near("declared wall elastic pressure", p_el(R), 43325.61728395062)
near("declared closed-form work", stored(R), 4.516039439535328e-9)
near("work from direct pressure-volume quadrature",
     quad(lambda x: 4 * math.pi * x**2 * p_el(x), A, R,
          epsabs=1e-20, epsrel=1e-11)[0], stored(R))

# A separately derived volume integral of the constitutive strain energy:
# W = ∫ (G/2)(λr² + 2λθ² - 3) 4πr0² dr0.
# q = r0/r gives r0²dr0 = (R³-A³)q²/(1-q³)² dq.
# Factoring the two quadratic zeroes yields a regular integrand at q=1.
c = R**3 - A**3
W_volume = 2 * math.pi * G * c * quad(
    lambda q: (q + 1)**2 * (q*q + 2) / (1 + q + q*q)**2,
    A / R, 1, epsabs=1e-12, epsrel=1e-12)[0]
near("independent network strain-energy volume integral", W_volume, stored(R))

for scale in [1.0, 1.2, 2.0, 6.0, 20.0]:
    rad = A * scale
    q_lower = A / rad
    by_q = 2 * G * quad(lambda q: 1 + q**3, q_lower, 1)[0]
    near(f"transformed stress-integral pressure at R/A={scale}", by_q, p_el(rad), abs_tol=1e-10)
    h = rad * 1e-5
    slope = (stored(rad + h) - stored(rad - h)) / (2 * h)
    near(f"work derivative equals area times resistance at R/A={scale}",
         slope, 4 * math.pi * rad**2 * p_el(rad), rel=2e-8, abs_tol=1e-12)

near("reference pressure vanishes", p_el(A), 0)
near("reference work vanishes", stored(A), 0, abs_tol=1e-20)
check("large-expansion pressure asymptote", abs(p_el(A * 1e8) / (2.5 * G) - 1) < 1e-7,
      {"normalized_pressure": p_el(A * 1e8) / (2.5 * G)})
check("elastic restoration changes sign on contraction", p_el(A / 2) < 0,
      {"contracted_pressure_Pa": p_el(A / 2), "scope": "intact mathematical model, not rupture validation"})

for material_radius in [A, 2*A, 20*A]:
    current_radius = (material_radius**3 + R**3 - A**3)**(1/3)
    lr = (material_radius / current_radius)**2
    lt = current_radius / material_radius
    near("principal stretches preserve local material volume", lr * lt * lt, 1)

dV = 4 * math.pi / 3 * (R**3 - A**3)
W_100 = 100000 * dV
near("constant-pressure displacement work", W_100, 11.257373675363425e-9)
near("fraction stored in gel", stored(R) / W_100, 0.40116279069767447)
near("finite expansion ledger residual", W_100 - stored(R), 6.741334235828097e-9)

eta = 0.010
rdot = -10.0
p_visc = -4 * eta * rdot / R
P_loss = 16 * math.pi * eta * R * rdot**2
near("inward speed viscous pressure sign", p_visc, 13333.333333333334)
near("viscous loss power", P_loss, 0.0015079644737231008)
near("viscous mechanical power is negative loss", p_visc * 4 * math.pi * R**2 * rdot, -P_loss)

# Check the differential energy identity on arbitrary admissible instantaneous state.
sigma = 0.072
pdiff = 80000.0
rddot = ((pdiff - 2*sigma/R - p_el(R) - 4*eta*rdot/R) / rho - 1.5*rdot**2) / R
dK = 2 * math.pi * rho * (3*R**2*rdot**3 + 2*R**3*rdot*rddot)
dW = 4 * math.pi * R**2 * p_el(R) * rdot
dSurface = 8 * math.pi * sigma * R * rdot
rhs_work = pdiff * 4 * math.pi * R**2 * rdot - P_loss
near("radial pressure law conserves mechanical energy with viscous loss",
     dK + dW + dSurface, rhs_work)

L = 30e-6
cs = math.sqrt(G / rho)
ts = L / cs
tc = 0.9146813565 * L * math.sqrt(rho / 100000)
near("shear wave speed", cs, 4.47213595499958)
near("shear crossing time", ts, 6.708203932499369e-6)
near("ideal liquid-collapse comparison", tc, 2.7440440695e-6)
near("two-model time ratio", ts / tc, 2.444641471709924)
permeability = 1e-17
mu_l = 0.001
M_d = 60000.0
D = permeability * M_d / mu_l
near("illustrative poroelastic diffusion coefficient", D, 6e-10)
near("illustrative drainage time", L**2 / D, 1.5)

html = chapter["body"]
soup = BeautifulSoup(html, "html.parser")
check("exactly three defense questions", chapter["question_ids"] == ["C5-Q1", "C5-Q2", "C5-Q3"]
      and len(soup.select("article.defense")) == 3, chapter["question_ids"])
check("unique equation identifiers", len(set(e["id"] for e in eqs)) == len(eqs), len(eqs))
check("every formula has local definitions and a meaningful figure",
      all(e["symbols_en"] and e["symbols_zh"] and e["diagram"]["labels"] and e["diagram"]["notes"] for e in eqs), len(eqs))
check("every reference answer begins with a quoted equation",
      all(x.select_one("details.answer").find("section", recursive=False) is not None
          and x.select_one("details.answer").find("section", recursive=False).get("class") == ["equation-unit"]
          for x in soup.select("article.defense")), "C5-E21, C5-E22, C5-E23 precede answer prose")
check("no escaped-LaTeX control characters in prose", not any(c in html for c in "\t\r\b\f"), "Raw authoring literals preserve LaTeX")
check("no private local computer paths in course prose", re.search(r'file:/{3}|(?<![A-Za-z0-9])[A-Z]:[\\/]', html, re.I) is None, "Content only")

en_words = sum(len(x.get_text(" ", strip=True).split()) for x in soup.select('[lang="en"]'))
en_prose_words = sum(len(x.get_text(" ", strip=True).split()) for x in soup.select('[lang="en"]')
                     if not x.find_parent(class_="symbols"))
review = {
    "chapter": 5,
    "date": "2026-10-09",
    "status": "authored_and_self_audited_not_learner_mastered",
    "scope": "Promoted source Appendix A; four retained platform mechanisms; no COMSOL model or target pressure maximum claimed",
    "equations": len(eqs),
    "defense_questions": 3,
    "english_words_including_local_definitions": en_words,
    "english_words_excluding_local_definitions": en_prose_words,
    "checks": checks,
    "checks_passed": sum(x["passed"] for x in checks),
    "sources_verified": [
        {"id": "r11", "doi": "10.1073/pnas.2318739121", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10835071/", "access": "Primary full-text search result accessible; direct open subsequently returned bot-check. Publisher DOI page returned cookie page.", "supports": "Sealed hydrogel composite, laser-induced water-vapor bulging and delamination. Not a PFC liquid-jet demonstration.", "derived_or_original": "Four-architecture comparison and proposed discriminating tests are conditional analysis, not reported paper results."},
        {"id": "r12", "doi": "10.1017/S0022112000003347", "url": "https://research.uni-luebeck.de/en/publications/dynamics-of-laser-induced-cavitation-bubbles-near-an-elastic-boun/", "access": "Author-affiliated institutional primary abstract read directly.", "supports": "Deformable boundary recoil, liquid jets toward/away from boundary, gel material ejection, and 960 m/s reported maximum in that experiment.", "limits": "Cannot transfer speed or stabilization to the proposed PFC geometry; full article body not reread this turn."},
        {"id": "r13", "doi": "10.1017/jfm.2015.7", "url": "https://par.nsf.gov/servlets/purl/10033369", "access": "Primary accepted-paper indexed excerpt verified mapping Eq. 2.15 and neo-Hookean resistance Eq. 2.18. Direct PDF requests returned timeout/502; publisher abstract verified via Cambridge.", "supports": "Finite-strain nonlinear-elastic radial framework and pressure formula.", "derived_or_original": "Mapping/stretch/stress/Jacobian/work algebra and conservation controls are fully rederived here; no reliance on truncated indexed rendering of dynamic Eq. 2.17."},
        {"doi": "10.1039/D0SM02243H", "url": "https://pubs.rsc.org/en/content/articlehtml/2021/sm/d0sm02243h", "access": "Primary article/search text read.", "supports": "Poroelastic coefficient scales as modulus times permeability / solvent viscosity and drainage time as length squared / coefficient.", "limits": "Chapter illustrative permeability and modulus are declared, not assigned from the study."}
    ],
    "derivation_gaps_repaired": [
        "Explicit volume mapping and incompressible principal stretches",
        "Elimination of the unknown pressure multiplier by the tangential-radial stress difference",
        "Changed stress integral limits, Jacobian, factorization and endpoint branch at zero deformation",
        "Full elastic-work antiderivative with lower-endpoint subtraction",
        "Both fixed-position and convective acceleration in the integrated radial momentum law",
        "Mechanical-energy identity and nonnegative viscous loss sign",
        "Kelvin–Voigt retardation vs held-strain stress relaxation",
        "Darcy-plus-storage diffusion derivation with its distinct small-perturbation assumptions"
    ],
    "semantic_audit": [
        "Rref is not automatically the liquid-PFC core a0 or current vapor radius",
        "5Gg/2 is an intact constitutive pressure asymptote, not fracture threshold or jet stabilization proof",
        "Stored work may return, but useful recovery requires timing/geometry; dashpot loss cannot return",
        "Shear timescale tests nonradial support communication and does not erase inertia already in the spherical model",
        "Longitudinal wave speed is a separate compressible extension; no shock peak is claimed",
        "Open liquid pocket, bulk inclusion, liquid site and sealed blister retain separate load/flow paths",
        "Both direct-film and intact-PVC-transmitted force paths remain available",
        "Largest single-event verified output and repeatable intact transfer are reported separately"
    ],
    "unresolved_limits": [
        "Rate/temperature/strain-dependent network law and damage at sixfold wall stretch unvalidated",
        "Actual PFC shell chemistry, activation and phase pressure history in the gel unknown",
        "Prestress, finite geometry, outlet evolution and solvent-network slip may invalidate the simple control",
        "Hydrogel jet stabilization and intact-transfer improvements require synchronized repeated-event evidence",
        "Actual fracture, receiver adhesion, placement and reset laws are not measured by this chapter",
        "No independent expert review of this chapter performed by this worker; numerical controls do not replace material validation"
    ],
    "cleanup": "Used Python -B; no compile/cache/temporary files created by this check. Review JSON and check script are intentional verification artifacts. Root integrates project log.",
}
(ROOT / "verification/chapter05-review.json").write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({"checks_passed": review["checks_passed"], "equations": len(eqs),
                  "questions": 3, "english_words": en_words,
                  "english_prose_words": en_prose_words}, ensure_ascii=True))
