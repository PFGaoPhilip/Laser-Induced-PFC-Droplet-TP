"""Finite-PFC vapor-core/liquid-shell controls. SI units; no fitted activation.

Prescribed-radius equilibria and an insulated post-nucleation radial transient.
The transient has no outlet and stops before the declared intact-gel limit.
"""
from __future__ import annotations

import csv
import json
import sys
from dataclasses import asdict, dataclass, replace
from math import pi
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools'))
import CoolProp.CoolProp as CP
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root, least_squares


@dataclass(frozen=True)
class Case:
    name: str = 'PFP_r0p3um_G20kPa'
    fluid: str = 'n-Perfluoropentane'
    radius: float = 0.3e-6
    shear: float = 20e3
    viscosity: float = 0.01
    sigma_outer: float = 0.054  # liquid-PFC/aqueous reference, constant control
    sigma_inner: float = 0.00941  # PFP liquid/saturated-air proxy, constant
    ambient: float = 1e5
    initial_temperature: float = 293.15
    host_density: float = 1000.
    sound_speed: float = 1500.
    seed_stretch: float = 1.2
    seed_overpressure: float = 50e3  # conditional, above static host traction
    intact_stretch_limit: float = 2.1  # declared control, NOT measured rupture


def gel(c, R):
    b = c.radius / R
    p = c.shear / 2 * (5 - 4*b - b**4)
    e = 2*pi*c.shear*(5*R**3/3 - 2*c.radius*R**2
                     + c.radius**4/R - 2*c.radius**3/3)
    return p, e


class Pfc:
    def __init__(self, case):
        self.c = case
        self.l = CP.AbstractState('HEOS', case.fluid)
        self.v = CP.AbstractState('HEOS', case.fluid)
        self.l.specify_phase(CP.iphase_liquid)
        self.v.specify_phase(CP.iphase_gas)
        self.V0 = 4*pi*case.radius**3/3
        self.p0 = case.ambient + 2*case.sigma_outer/case.radius
        self.l.update(CP.PT_INPUTS, self.p0, case.initial_temperature)
        self.rho0 = self.l.rhomass()
        self.u0 = self.l.umass()
        self.mass = self.rho0*self.V0
        self.Tc = CP.PropsSI('Tcrit', case.fluid)

    def phase(self, T, rho_l, rho_v):
        self.l.update(CP.DmassT_INPUTS, rho_l, T)
        self.v.update(CP.DmassT_INPUTS, rho_v, T)
        return (self.l.p(), self.v.p(), self.l.umass(), self.v.umass(),
                self.l.gibbsmass(), self.v.gibbsmass())

    def validate(self, snap):
        """Reject inadmissible algebraic branches, independently of root status."""
        if not (all(np.isfinite(v) for v in snap.values())
                and 0 < snap['bubble_radius_m'] < snap['R_m']
                and 0 < snap['vapor_fraction'] < 1
                and 200 < snap['T_K'] < self.Tc - .1
                and snap['liquid_density_kg_m3'] > snap['vapor_density_kg_m3'] > 0
                and min(snap['liquid_pressure_Pa'], snap['vapor_pressure_Pa']) > 0
                and min(snap['liquid_compressibility_slope_Pa_m3_kg'],
                        snap['vapor_compressibility_slope_Pa_m3_kg']) > 0):
            raise ValueError('Algebraic state left the admissible finite-PFC core-shell domain')

    def at_pressure(self, R, pL, seed=None):
        """Independent density-EOS root for imposed radius and liquid pressure."""
        c = self.c
        V = 4*pi*R**3/3
        if seed is None:
            ts = CP.PropsSI('T', 'P', min(pL + 2*c.sigma_inner/R, 1.8e6), 'Q', 0, c.fluid)
            rl=CP.PropsSI('Dmass','T',ts,'Q',0,c.fluid)
            rv=CP.PropsSI('Dmass','T',ts,'Q',1,c.fluid)
            f=np.clip((rl*V-self.mass)/((rl-rv)*V),.01,.95)
            seed = [ts, np.log(rl), np.log(rv), np.log(f)/3]

        def evaluate(x):
            T, lr, lv, logratio = x
            rl,rv=np.exp([lr,lv]);b=R*np.exp(logratio)
            try:
                pl,pv,ul,uv,gl,gv=self.phase(T,rl,rv)
                Vb = 4*pi*b**3/3
                return np.array([(pl-pL)/1e5,
                                 (pv-pL-2*c.sigma_inner/b)/1e5,
                                 (gl-gv)/1e5,
                                 (rl*(V-Vb)+rv*Vb)/self.mass-1])
            except (ValueError,OverflowError):
                return np.full(4,1e6)

        solution = root(evaluate, seed, tol=2e-10)
        if np.max(np.abs(evaluate(solution.x))) > 1e-8:
            solution=least_squares(evaluate,seed,bounds=([220,np.log(650),np.log(.001),-7],
                                     [self.Tc-.2,np.log(2200),np.log(600),-1e-8]),
                                   x_scale=[350,1,1,1],xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=500)
        if np.max(np.abs(evaluate(solution.x))) > 1e-8:
            raise RuntimeError('No converged core-shell root: ' + solution.message)
        T, lr,lv, logratio = solution.x
        b = R*np.exp(logratio)
        snap = self.snapshot(R, T, np.exp(lr),np.exp(lv), b)
        self.validate(snap)
        snap['root_seed'] = solution.x.tolist()
        return snap

    def snapshot(self, R, T, rl, rv, b):
        pL, pV, ul, uv, gl, gv = self.phase(T, rl, rv)
        V = 4*pi*R**3/3
        Vb = 4*pi*b**3/3
        ml, mv = rl*(V-Vb), rv*Vb
        c = self.c
        pe, eg = gel(c, R)
        es = 4*pi*(c.sigma_outer*(R**2-c.radius**2)+c.sigma_inner*b**2)
        ea = c.ambient*(V-self.V0)
        up = ml*ul+mv*uv
        return dict(R_m=R, T_K=T, liquid_density_kg_m3=rl, vapor_density_kg_m3=rv,
                    bubble_radius_m=b, shell_thickness_m=R-b,
                    liquid_pressure_Pa=pL, vapor_pressure_Pa=pV,
                    vapor_fraction=mv/self.mass, mass_kg=ml+mv,
                    mass_relative_residual=(ml+mv)/self.mass-1,
                    chemical_residual_J_kg=gl-gv,
                    inner_traction_residual_Pa=pV-pL-2*c.sigma_inner/b,
                    gel_pressure_Pa=pe, gel_energy_J=eg,
                    surface_energy_change_J=es, ambient_work_J=ea,
                    PFC_internal_change_J=up-self.mass*self.u0,
                    equilibrium_state_energy_J=up-self.mass*self.u0+eg+es+ea,
                    PFC_internal_J=up,
                    liquid_compressibility_slope_Pa_m3_kg=self.l.first_partial_deriv(CP.iP, CP.iDmass, CP.iT),
                    vapor_compressibility_slope_Pa_m3_kg=self.v.first_partial_deriv(CP.iP, CP.iDmass, CP.iT))

    def flash(self, R, internal, seed):
        """Four-equation Dmass,T closure, independent of native COMSOL DAE."""
        c = self.c
        V = 4*pi*R**3/3
        scaleE = self.mass*1e5

        def f(x):
            T, logrl, logrv, logb = x
            rl, rv, b = np.exp([logrl, logrv, logb])
            try:
                pL, pV, ul, uv, gl, gv = self.phase(T, rl, rv)
                Vb = 4*pi*b**3/3
                return np.array([(pV-pL-2*c.sigma_inner/b)/1e5,
                                 (gl-gv)/1e5,
                                 (rl*(V-Vb)+rv*Vb)/self.mass-1,
                                 (rl*(V-Vb)*ul+rv*Vb*uv-internal)/scaleE])
            except (ValueError, OverflowError):
                return np.full(4, 1e6)

        sol = root(f, seed, tol=1e-10)
        err = np.max(np.abs(f(sol.x)))
        if not np.all(np.isfinite(sol.x)) or err > 2e-7:
            raise RuntimeError(f'Energy flash failed, residual={err:.3e}')
        T, logrl, logrv, logb = sol.x
        snap = self.snapshot(R, T, np.exp(logrl), np.exp(logrv), np.exp(logb))
        self.validate(snap)
        return sol.x, snap


def equilibrium(c, stretches=(1.2, 1.5, 1.8, 2.1)):
    p = Pfc(c)
    rows = []
    seed = None
    for lam in stretches:
        R = lam*c.radius
        pl = c.ambient + gel(c, R)[0] + 2*c.sigma_outer/R
        s = p.at_pressure(R, pl, seed)
        seed = s.pop('root_seed')
        rows.append({**asdict(c), 'stretch':lam, 'initial_PFC_mass_kg':p.mass, **s})
    return rows


def transient(c, method='DOP853', step_fraction=.01, rtol=2e-8, samples=801):
    p = Pfc(c)
    R0 = c.seed_stretch*c.radius
    pl = c.ambient + gel(c, R0)[0] + 2*c.sigma_outer/R0 + c.seed_overpressure
    s0 = p.at_pressure(R0, pl)
    total = s0['equilibrium_state_energy_J']
    # Initial energy includes pre-existing seed surface and deformed host.
    # No energy is silently supplied by an ideal-gas pressure initialization.
    seed = np.array([s0['T_K'], np.log(s0['liquid_density_kg_m3']),
                     np.log(s0['vapor_density_kg_m3']), np.log(s0['bubble_radius_m'])])
    Us = np.sqrt(1e5/c.host_density)
    tau = c.radius/Us
    Escale = p.mass*1e5
    last = seed.copy()

    def rhs(theta, y):
        nonlocal last
        lam, v, d = y
        R, W, D = lam*c.radius, v*Us, d*Escale
        pe, eg = gel(c, R)
        # Inner surface depends on algebraic bubble radius, so flash must
        # enforce TOTAL energy, not PFC energy alone.
        V = 4*pi*R**3/3
        K = 2*pi*c.host_density*R**3*W**2
        eo = 4*pi*c.sigma_outer*(R**2-c.radius**2)

        def f(x):
            T, lr, lv, lb = x
            rl, rv, b = np.exp([lr, lv, lb])
            pL, pV, ul, uv, gl, gv = p.phase(T, rl, rv)
            Vb = 4*pi*b**3/3
            up = rl*(V-Vb)*ul+rv*Vb*uv
            return [(pV-pL-2*c.sigma_inner/b)/1e5, (gl-gv)/1e5,
                    (rl*(V-Vb)+rv*Vb)/p.mass-1,
                    (up-p.mass*p.u0+eg+eo+4*pi*c.sigma_inner*b*b
                     +c.ambient*(V-p.V0)+K+D-total)/Escale]

        sol = root(f, last, tol=1e-10)
        err = max(abs(np.asarray(f(sol.x))))
        if not np.all(np.isfinite(sol.x)) or not np.isfinite(err) or err > 2e-7:
            raise RuntimeError(f'Total-energy flash failed at lam={lam:.8g}, {err:.3e}')
        last = sol.x
        T, lr, lv, lb = last
        rl, rv, b = np.exp([lr, lv, lb])
        snap = p.snapshot(R, T, rl, rv, b)
        p.validate(snap)
        pL = snap['liquid_pressure_Pa']
        acc = ((pL-c.ambient-pe-2*c.sigma_outer/R-4*c.viscosity*W/R)
               /c.host_density-1.5*W*W)/R
        diss = 16*pi*c.viscosity*R*W*W
        return [v, tau*acc/Us, tau*diss/Escale]

    def turning(theta, y): return y[1]
    turning.direction = -1
    turning.terminal = True
    def intact(theta,y): return c.intact_stretch_limit-y[0]
    intact.direction=-1
    intact.terminal=True
    def mach(theta,y): return .1-abs(y[1])*Us/c.sound_speed
    mach.direction=-1
    mach.terminal=True
    sol=solve_ivp(rhs,(0,50),[c.seed_stretch,0,0],method=method,rtol=rtol,
                  atol=[1e-10,1e-9,1e-11],max_step=step_fraction,
                  events=[turning,intact,mach],dense_output=True)
    if not sol.success: raise RuntimeError(sol.message)
    # Resolve the fast viscous startup even when the later accounting window
    # is long. A uniform reporting grid can hide a converged startup waveform.
    early=np.geomspace(max(1e-8,sol.t[-1]*1e-8),min(1.,sol.t[-1]),301)
    tt=np.unique(np.concatenate((np.linspace(0,sol.t[-1],samples),early)))
    yy=sol.sol(tt)
    rows=[]
    last=seed.copy()
    for theta,y in zip(tt,yy.T):
        rhs(theta,y)
        T,lr,lv,lb=last
        snap=p.snapshot(y[0]*c.radius,T,np.exp(lr),np.exp(lv),np.exp(lb))
        W=y[1]*Us
        D=y[2]*Escale
        K=2*pi*c.host_density*snap['R_m']**3*W*W
        residual=(snap['equilibrium_state_energy_J']+K+D-total)/total
        rows.append(dict(time_s=theta*tau,stretch=y[0],radial_speed_m_s=W,
                         dissipated_J=D,host_kinetic_J=K,total_energy_residual=residual,
                         exterior_emitted_mass_kg=0.,**snap))
    endpoint='first_expansion_turning_point'
    if len(sol.t_events[1]):endpoint='declared_intact_stretch_limit'
    if len(sol.t_events[2]):endpoint='Mach_screen'
    if not any(len(x) for x in sol.t_events):endpoint='time_window_end'
    summary=dict(**asdict(c),method=method,retained_seed_energy_J=total,
                 initial_PFC_mass_kg=p.mass,event=endpoint,event_time_s=tt[-1]*tau,
                 maximum_stretch=float(yy[0].max()),
                 peak_radial_speed_m_s=max(x['radial_speed_m_s'] for x in rows),
                 peak_elastic_pressure_Pa=max(x['gel_pressure_Pa'] for x in rows),
                 max_energy_residual=max(abs(x['total_energy_residual']) for x in rows),
                 max_mass_residual=max(abs(x['mass_relative_residual']) for x in rows),
                 max_chemical_residual_J_kg=max(abs(x['chemical_residual_J_kg']) for x in rows),
                 max_inner_traction_residual_Pa=max(abs(x['inner_traction_residual_Pa']) for x in rows),
                 min_shell_thickness_m=min(x['shell_thickness_m'] for x in rows),
                 emitted_mass_kg=0., initial_phase_state=s0, end_state=rows[-1])
    return rows,summary


def write_csv(path,rows):
    with path.open('w',newline='',encoding='utf8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def main():
    rows=[]; failures=[]
    for fluid,sinner in [('n-Perfluoropentane',.00941),('n-Perfluorohexane',.012)]:
        for radius in [.15,.3,1.5,3.,6.]:
            for g in [5.,20.,100.]:
                c=replace(Case(),name=f'{fluid}_r{radius:g}um_G{g:g}kPa',
                          fluid=fluid,radius=radius*1e-6,shear=g*1e3,sigma_inner=sinner)
                try:rows.extend(equilibrium(c))
                except Exception as e:failures.append(dict(case=asdict(c),error=str(e)))
    # Interface sensitivities are assumptions, never silently borrowed coatings.
    for sig in [.005,.018,.054]:
        c=replace(Case(),name=f'PFP_interface_{sig:g}',sigma_outer=sig)
        try: rows.extend(equilibrium(c))
        except Exception as e:failures.append(dict(case=asdict(c),error=str(e)))
    write_csv(ROOT/'data/equilibrium_comparison.csv',rows)
    (ROOT/'data/excluded_cases.json').write_text(json.dumps(failures,indent=2),encoding='utf8')
    summaries=[]
    for radius in [.3,3.]:
        for eta in [0.,.01,.1]:
            c=replace(Case(),name=f'PFP_r{radius:g}um_eta{eta:g}',radius=radius*1e-6,viscosity=eta)
            data,summary=transient(c)
            write_csv(ROOT/'data'/f'{c.name}_reference.csv',data)
            summaries.append(summary)
            print(c.name,summary['event'],summary['maximum_stretch'],summary['peak_radial_speed_m_s'])
    (ROOT/'data/transient_summary.json').write_text(json.dumps(summaries,indent=2),encoding='utf8')
    (ROOT/'data/inputs.json').write_text(json.dumps([asdict(Case()),*[s['case'] for s in failures]],indent=2),encoding='utf8')
    print('EQUILIBRIUM_ROWS',len(rows),'EXCLUDED_PARAMETER_CASES',len(failures))


if __name__=='__main__':main()
