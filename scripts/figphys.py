"""Numerical helpers so the figures plot the actual formulas of the lessons."""
import math

import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import beta as beta_fn, iv

RHO_W, P_ATM = 1000.0, 101325.0


def rayleigh_speed(x, Rmax, rho, dpc):
    """C1-E14: wall speed (m/s, negative) at x = R/Rmax."""
    return -math.sqrt(2 * dpc / (3 * rho) * (x ** -3 - 1))


def rayleigh_curve(Rmax, rho, dpc, n=600):
    """Time-resolved ideal collapse from the quadrature of C1-E15, using x = 1 - s^2 to remove the endpoint singularity."""
    s = np.linspace(0, 1 - 1e-4, n)
    x = 1 - s ** 2
    K = math.sqrt(3 * rho / (2 * dpc))
    integrand = Rmax * K * 2 * s / np.sqrt(np.maximum(x ** -3 - 1, 1e-300))
    integrand[0] = Rmax * K * 2 / math.sqrt(3)
    t = np.concatenate([[0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(s))])
    return t, Rmax * x


def tc_coeff():
    return beta_fn(5 / 6, 0.5) / math.sqrt(6)


def rp_solve(R0, V0, t_end, rho=RHO_W, pinf=P_ATM, sigma=0.072, mu=1e-3, pg0=None, kappa=1.4, pb_fun=None,
             n=3000):
    """Rayleigh-Plesset (C1-E07) with a polytropic gas pressure unless pb_fun is given."""
    pg0 = pinf if pg0 is None else pg0

    def pb(R):
        return pb_fun(R) if pb_fun else pg0 * (R0 / R) ** (3 * kappa)

    def rhs(t, y):
        R, V = y
        acc = ((pb(R) - pinf - 2 * sigma / R - 4 * mu * V / R) / rho - 1.5 * V * V) / R
        return [V, acc]
    t = np.linspace(0, t_end, n)
    sol = solve_ivp(rhs, (0, t_end), [R0, V0], t_eval=t, rtol=1e-10, atol=1e-14, method='LSODA')
    R, V = sol.y
    return sol.t, R, V, np.array([pb(r) for r in R])


def collapse_ode(Rmax, rho, dpc, t_end, n=2000):
    """Direct integration of C1-E12 for the independent check of E15/E18."""
    def rhs(t, y):
        R, V = y
        return [V, (-dpc / rho - 1.5 * V * V) / R]
    sol = solve_ivp(rhs, (0, t_end), [Rmax, 0.0], t_eval=np.linspace(0, t_end, n), rtol=1e-11, atol=1e-16,
                    events=lambda t, y: y[0] - 0.02 * Rmax)
    return sol.t, sol.y[0], sol.y[1]


def cylinder_growth(q):
    """C3-E21: g^2 t_sigma^2 = q (1-q^2) I1(q)/I0(q); returns g*t_sigma."""
    q = np.asarray(q, dtype=float)
    return np.sqrt(np.maximum(q * (1 - q ** 2) * iv(1, q) / iv(0, q), 0))


def psat_pfp(T):
    """C2-E12 (bar -> Pa)."""
    return 1e5 * 10 ** (4.2063 - 1103.454 / (T - 39.77))


def psat_water(T):
    """C2-E13 (two branches, bar -> Pa)."""
    if T <= 303.5:
        return 1e5 * 10 ** (5.40221 - 1838.675 / (T - 31.737))
    return 1e5 * 10 ** (5.20389 - 1733.926 / (T - 39.485))


def collapse_S(Rmax, rho, dpc, S, t_end, n=1500, xstop=0.03):
    """C3-E07: (1+SR) R R'' + (3/2 + 2SR) R'^2 = -dpc/rho from rest at Rmax."""
    def rhs(t, y):
        R, V = y
        return [V, (-dpc / rho - (1.5 + 2 * S * R) * V * V) / ((1 + S * R) * R)]
    sol = solve_ivp(rhs, (0, t_end), [Rmax, 0.0], t_eval=np.linspace(0, t_end, n), rtol=1e-10, atol=1e-16,
                    events=lambda t, y: y[0] - xstop * Rmax)
    return sol.t, sol.y[0], sol.y[1]


def C_chi(chi, n=4000):
    """C3-E10: C(chi) = sqrt(3/2) * int_0^1 sqrt(x^3 (1+chi x)/(1-x^3)) dx via x = 1 - s^2."""
    s = np.linspace(0, 1, n)
    x = 1 - s ** 2
    with np.errstate(divide='ignore', invalid='ignore'):
        g = np.sqrt(x ** 3 * (1 + chi * x) / (1 - x ** 3)) * 2 * s
    g[0] = 2 * math.sqrt(1 / 3.0)
    g[-1] = 0.0
    return math.sqrt(1.5) * np.trapezoid(g, s)


def speed_S(x, Rmax, rho, dpc, chi):
    """C3-E09: wall speed with interaction, x = R/Rmax, chi = S Rmax."""
    return -math.sqrt(2 * dpc / (3 * rho) * (1 - x ** 3) / (x ** 3 * (1 + chi * x)))
