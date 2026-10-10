"""Independent SI-unit integration of a finite cavity source, port and gel.

The source is a post-activation, finite-mass adiabatic gas control. It is not
a PFC equation of state or a prediction of optical-to-mechanical conversion.
Only the first expansion/ejection episode is retained for interpretation.
"""
from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Case:
    name: str = "A_baseline"
    energy: float = 2e-9  # available reversible work relative to ambient, J
    gas_radius: float = 15e-6
    chamber_radius: float = 30e-6
    port_radius: float = 5e-6
    liquid_length: float = 50e-6
    stroke_length: float | None = None  # default: connected chamber liquid inventory / area
    rho: float = 1000.0
    rho_gel: float = 1000.0
    ambient: float = 1e5
    kappa: float = 1.4
    surface_tension: float = 0.072
    gel: bool = False
    open_port: bool = True
    shear_modulus: float = 2e4
    gel_viscosity: float = 0.01
    loss_coefficient: float = 0.0
    resistance: float = 0.0  # fitted linear pressure/speed coefficient, Pa s/m
    sound_speed: float = 1500.0
    end_time: float = 100e-6


def available_work(p0, c):
    vg0 = 4 * np.pi * c.gas_radius**3 / 3
    veq = vg0 * (p0 / c.ambient)**(1 / c.kappa)
    return p0 * vg0 / (c.kappa - 1) * (1 - (vg0 / veq)**(c.kappa - 1)) - c.ambient * (veq - vg0)


def source_pressure(c):
    return brentq(lambda p: available_work(p, c) - c.energy,
                  c.ambient * (1 + 1e-10), 1e10, xtol=1e-6)


def quantities(y, c):
    # y = discharge-volume/area, outlet speed, chamber radius, wall speed,
    # irreversible losses, actually emitted kinetic energy, emitted impulse.
    x, u, r, w, diss, eout, iout = np.asarray(y)
    a = np.pi * c.port_radius**2
    vg0 = 4 * np.pi * c.gas_radius**3 / 3
    vc0 = 4 * np.pi * c.chamber_radius**3 / 3
    vg = vg0 + a * x + 4 * np.pi / 3 * (r**3 - c.chamber_radius**3)
    pb = source_pressure(c) * (vg0 / vg)**c.kappa
    pe = c.shear_modulus / 2 * (5 - 4 * c.chamber_radius / r - (c.chamber_radius / r)**4) if c.gel else np.zeros_like(r)
    wg = 2 * np.pi * c.shear_modulus * (5 * r**3 / 3 - 2 * c.chamber_radius * r**2 + c.chamber_radius**4 / r - 2 * c.chamber_radius**3 / 3) if c.gel else np.zeros_like(r)
    kj = c.rho * a * c.liquid_length * u**2 / 2
    kg = 2 * np.pi * c.rho_gel * r**3 * w**2 if c.gel else np.zeros_like(r)
    pcap = 2 * c.surface_tension / c.port_radius
    esurf = pcap * a * x
    ug = pb * vg / (c.kappa - 1)
    u0 = source_pressure(c) * vg0 / (c.kappa - 1)
    residual = (ug - u0 + c.ambient * (vg - vg0) + kj + kg + wg + esurf + diss + eout) / c.energy
    mout = c.rho*a*x
    rms = np.sqrt(np.maximum(0,np.divide(2*eout,mout,out=np.zeros_like(eout),where=mout>0)))
    return dict(x_m=x, u_m_s=u, r_m=r, wall_speed_m_s=w, gas_volume_m3=vg,
                source_gauge_Pa=pb-c.ambient, elastic_Pa=pe,
                gel_wall_resistance_Pa=pe + (4*c.gel_viscosity*w/r if c.gel else 0),
                radial_traction_magnitude_integral_N=4*np.pi*r**2*pe,
                confinement_hemisphere_force_N=np.pi*r**2*pe,
                jet_dynamic_Pa=c.rho*u**2/2,
                column_momentum_N_s=c.rho*a*c.liquid_length*u,
                momentum_flux_scale_N=c.rho*a*u**2,
                kinetic_column_J=kj, kinetic_gel_J=kg, elastic_J=wg,
                capillary_J=esurf, dissipation_J=diss, residual=residual,
                emitted_energy_J=eout, emitted_impulse_N_s=iout, emitted_mass_kg=mout,
                emitted_rms_speed_m_s=rms,
                liquid_inventory_margin_m3=vc0-vg0-a*x,
                port_stroke_fraction=x/(c.stroke_length if c.stroke_length is not None else (vc0-vg0)/a),
                wall_stretch=r/c.chamber_radius,
                liquid_Mach=np.abs(u)/c.sound_speed,
                wall_Mach=np.abs(w)/c.sound_speed)


def integrate(c, rtol=2e-10, max_step=2e-9, samples=1001):
    a = np.pi * c.port_radius**2
    vg0 = 4*np.pi*c.gas_radius**3/3
    p0 = source_pressure(c)
    pcap = 2*c.surface_tension/c.port_radius

    def rhs(t, y):
        x,u,r,w,d,eout,iout = y
        vg = vg0+a*x+4*np.pi/3*(r**3-c.chamber_radius**3)
        p = p0*(vg0/vg)**c.kappa-c.ambient
        pe = c.shear_modulus/2*(5-4*c.chamber_radius/r-(c.chamber_radius/r)**4) if c.gel else 0
        ploss = c.resistance*u+c.rho*c.loss_coefficient*u*abs(u)/2
        du = (p-pcap-ploss-c.rho*u*u/2)/(c.rho*c.liquid_length) if c.open_port else 0
        dw = ((p-pe-4*c.gel_viscosity*w/r)/c.rho_gel-1.5*w*w)/r if c.gel else 0
        dp = a*(c.resistance*u*u+c.rho*c.loss_coefficient*abs(u)**3/2) if c.open_port else 0
        dg = 16*np.pi*c.gel_viscosity*r*w*w if c.gel else 0
        return [u if c.open_port else 0,du,w if c.gel else 0,dw,dp+dg,
                c.rho*a*u**3/2 if c.open_port else 0,
                c.rho*a*u*u if c.open_port else 0]

    def peak(t,y):
        return y[1] if c.open_port else y[3]
    peak.terminal = True
    peak.direction = -1
    budget=c.stroke_length if c.stroke_length is not None else (4*np.pi/3*(c.chamber_radius**3-c.gas_radius**3))/a
    def stroke(t,y): return budget-y[0]
    stroke.terminal=True
    stroke.direction=-1
    def stretch(t,y): return 1.2-y[2]/c.chamber_radius
    stretch.terminal=True
    stretch.direction=-1
    y0=[0,0,c.chamber_radius,0,0,0,0]
    # Sealed case begins at zero wall speed; initial derivative is positive.
    sol=solve_ivp(rhs,(0,c.end_time),y0,method='DOP853',rtol=rtol,
                  atol=[1e-17,1e-8,1e-17,1e-8,1e-21,1e-22,1e-22],max_step=max_step,
                  events=[peak,stroke,stretch],dense_output=True)
    if not sol.success: raise RuntimeError(sol.message)
    end=sol.t[-1]
    t=np.linspace(0,end,samples)
    vals=quantities(sol.sol(t),c)
    event='first_outward_ejection_end' if c.open_port else 'first_wall_expansion_maximum'
    if len(sol.t_events[1]): event='finite_liquid_stroke_limit'
    if len(sol.t_events[2]): event='declared_20_percent_stretch_screen'
    if not any(len(e) for e in sol.t_events): event='end_of_declared_time_window'
    summary={**asdict(c), 'p0_absolute_Pa':p0,'available_work_J':available_work(p0,c),
             'effective_column_mass_kg':c.rho*a*c.liquid_length,
             'energy_only_speed_ceiling_m_s':np.sqrt(2*c.energy/(c.rho*a*c.liquid_length)),
             'energy_only_dynamic_pressure_ceiling_Pa':c.energy/(a*c.liquid_length),
             'stop_event':event,'event_time_s':end,
             'max_abs_energy_residual':float(np.max(np.abs(vals['residual']))),
             'source_pressure_peak_gauge_Pa':float(np.max(vals['source_gauge_Pa'])),
             'max_jet_speed_m_s':float(np.max(vals['u_m_s'])),
             'max_jet_dynamic_pressure_Pa':float(np.max(vals['jet_dynamic_Pa'])),
             'max_elastic_resistance_Pa':float(np.max(vals['elastic_Pa'])),
             'max_confinement_hemisphere_force_N':float(np.max(vals['confinement_hemisphere_force_N'])),
             'max_wall_stretch':float(np.max(vals['wall_stretch'])),
             'max_liquid_Mach':float(np.max(vals['liquid_Mach'])),
             'max_wall_Mach':float(np.max(vals['wall_Mach'])),
             'max_port_stroke_fraction':float(np.max(vals['port_stroke_fraction']))}
    summary['end_state']={k:float(v[-1]) for k,v in vals.items()}
    return t,vals,summary


def cases():
    base=Case()
    aa=[replace(base,name=f'A_E{e:g}nJ_a{a:g}um',energy=e*1e-9,port_radius=a*1e-6)
        for e in [0.5,2,5] for a in [3,5,10]]
    aa.insert(0,base)
    bb=[replace(base,name='B_open_baseline',gel=True),
        replace(base,name='B_sealed_control',gel=True,open_port=False),
        replace(base,name='B_open_loss_K1',gel=True,loss_coefficient=1),
        replace(base,name='B_open_G5kPa',gel=True,shear_modulus=5e3),
        replace(base,name='B_open_G100kPa',gel=True,shear_modulus=1e5),
        replace(base,name='B_open_eta0',gel=True,gel_viscosity=0),
        replace(base,name='B_open_eta0p1',gel=True,gel_viscosity=0.1)]
    return aa,bb


def main():
    out=ROOT/'data';out.mkdir(exist_ok=True)
    all_s=[]
    for c in sum(cases(),[]):
        t,v,s=integrate(c)
        with (out/(c.name+'_reference.csv')).open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f);w.writerow(['time_s',*v]);w.writerows(zip(t,*v.values()))
        all_s.append(s)
    # Exact independent gel benchmark and additional numerical integration route.
    c=replace(Case(),gel=True,shear_modulus=2e4,chamber_radius=5e-6)
    val=quantities([0,0,30e-6,0,0,0,0],c)
    baseline=all_s[0]
    for s in all_s:
        s['matched_rigid_speed_ratio']=s['max_jet_speed_m_s']/baseline['max_jet_speed_m_s'] if s['name'].startswith('B_') else None
        s['matched_rigid_column_kinetic_energy_ratio']=s['max_jet_speed_m_s']**2/baseline['max_jet_speed_m_s']**2 if s['name'].startswith('B_') else None
        s['matched_rigid_emitted_energy_ratio']=s['end_state']['emitted_energy_J']/baseline['end_state']['emitted_energy_J'] if s['name'].startswith('B_') else None
        s['matched_rigid_emitted_impulse_ratio']=s['end_state']['emitted_impulse_N_s']/baseline['end_state']['emitted_impulse_N_s'] if s['name'].startswith('B_') else None
    (out/'reference_summary.json').write_text(json.dumps(all_s,indent=2),encoding='utf-8')
    (out/'case_inputs.json').write_text(json.dumps([asdict(c) for c in sum(cases(),[])],indent=2),encoding='utf-8')
    audit={'gel_30um_elastic_Pa':float(val['elastic_Pa']),
           'gel_30um_work_J':float(val['elastic_J']),
           'gel_expected_elastic_Pa':43325.61728395062,
           'gel_expected_work_J':4.516039439485027e-9,
           'baseline_energy_work_relative_error':abs(baseline['available_work_J']/baseline['energy']-1),
           'all_reference_energy_residual_max':max(s['max_abs_energy_residual'] for s in all_s)}
    (out/'reference_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
    for s in all_s:
        print(s['name'], 'Umax',round(s['max_jet_speed_m_s'],5),'pel',round(s['max_elastic_resistance_Pa'],3),
              'time_us',round(s['event_time_s']*1e6,5),'event',s['stop_event'],
              'residual',f"{s['max_abs_energy_residual']:.2e}")
    print('AUDIT',audit)


if __name__=='__main__': main()
