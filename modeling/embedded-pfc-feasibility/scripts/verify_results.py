"""Numerical implementation checks, NOT specimen-level physical validation."""
import csv,json
from dataclasses import fields
from math import pi
import numpy as np
import sympy as sp
from scipy.interpolate import PchipInterpolator
from pfc_model import ROOT,Case,Pfc,transient,CP


def native_csv(path):
    lines=path.read_text(encoding='utf-8-sig').splitlines()
    header=next(x for x in lines if x.startswith('%') and 'time_s' in x)
    # COMSOL decorates descriptions with '(unit)' or uses expressions.
    labels=[x.strip().split(' (')[0].lstrip('%').strip() for x in header.split(',')]
    rows=np.array([[float(x) for x in line.split(',')] for line in lines if line and not line.startswith('%')])
    return {k:rows[:,i] for i,k in enumerate(labels)}


def main():
    native=json.loads((ROOT/'data/native_case_inputs.json').read_text())
    eq_checks=[]
    for x in native['equilibrium']:
        d=native_csv(ROOT/'data'/f"{x['native_name']}_native.csv")
        errors={k:abs(float(d[k][0])-float(x[k]))/max(abs(float(x[k])),1e-20)
                for k in ['T_K','liquid_density_kg_m3','vapor_density_kg_m3','bubble_radius_m',
                          'liquid_pressure_Pa','vapor_pressure_Pa','vapor_fraction','equilibrium_state_energy_J']}
        assert max(errors.values())<1e-6,(x['native_name'],errors)
        assert abs(d['mass_relative_residual'][0])<1e-8
        eq_checks.append(dict(case=x['native_name'],relative_errors=errors))
    tr_checks=[]
    for s in native['transient']:
        d=native_csv(ROOT/'data'/f"{s['name']}_native.csv")
        ref=list(csv.DictReader((ROOT/'data'/f"{s['name']}_reference.csv").open(encoding='utf8')))
        t=np.array([float(x['time_s']) for x in ref])
        checks={}
        for k in ['stretch','radial_speed_m_s','T_K','vapor_fraction','bubble_radius_m','dissipated_J']:
            v=np.array([float(x[k]) for x in ref]);actual=PchipInterpolator(t,v)(d['time_s'])
            # All native stored times precede its resolved stopping condition.
            valid=d['time_s']<=t[-1]+1e-16
            checks[k]=float(np.max(np.abs(actual[valid]-d[k][valid]))/max(np.max(np.abs(v)),1e-25))
        assert max(checks.values())<5e-4,(s['name'],checks)
        assert np.max(np.abs(d['total_energy_residual']))<1e-6
        assert np.all(d['exterior_emitted_mass_kg']==0)
        assert np.min(d['shell_thickness_m'])>0
        # A thermodynamic entropy check is not an equation enforced by the DAE.
        p=Pfc(Case(**{k:s[k] for k in {f.name for f in fields(Case)}}))
        entropy=[]
        for i in range(len(d['time_s'])):
            T=d['T_K'][i];rl=d['liquid_density_kg_m3'][i];rv=d['vapor_density_kg_m3'][i]
            p.phase(T,rl,rv)
            R=d['stretch'][i]*s['radius'];b=d['bubble_radius_m'][i]
            p.validate(p.snapshot(R,T,rl,rv,b))
            mv=rv*4*pi*b**3/3;ml=rl*4*pi*(R**3-b**3)/3
            entropy.append(ml*p.l.smass()+mv*p.v.smass())
        entropy=np.array(entropy)
        drift=float(np.max(abs(entropy-entropy[0]))/(p.mass*CP.PropsSI('GAS_CONSTANT',p.c.fluid)/CP.PropsSI('MOLARMASS',p.c.fluid)))
        assert drift<2e-5,(s['name'],drift)
        tr_checks.append(dict(case=s['name'],waveform_errors=checks,
                              energy_residual=float(np.max(abs(d['total_energy_residual']))),
                              mass_residual=float(np.max(abs(d['mass_relative_residual']))),
                              entropy_drift_over_mass_Rspec=drift,
                              native_end_s=float(d['time_s'][-1]),reference_end_s=float(t[-1])))
    refinements=[]
    for radius in [.3e-6,3e-6]:
        c=Case(name=f'refine_{radius:g}',radius=radius)
        _,a=transient(c,method='DOP853',step_fraction=.005,rtol=5e-9,samples=1201)
        _,b=transient(c,method='Radau',step_fraction=.02,rtol=2e-8,samples=1201)
        err=abs(a['peak_radial_speed_m_s']-b['peak_radial_speed_m_s'])/a['peak_radial_speed_m_s']
        time_err=abs(a['event_time_s']-b['event_time_s'])/a['event_time_s']
        assert err<1e-5 and time_err<1e-5
        refinements.append(dict(radius_m=radius,DOP853=a['peak_radial_speed_m_s'],Radau=b['peak_radial_speed_m_s'],
                                speed_relative_difference=err,event_time_relative_difference=time_err))
    R,a,G,rho,W,A=sp.symbols('R a G rho W A',positive=True)
    pe=G/2*(5-4*a/R-(a/R)**4)
    eg=2*sp.pi*G*(5*R**3/3-2*a*R**2+a**4/R-2*a**3/3)
    kinetic=2*sp.pi*rho*R**3*W**2
    assert sp.simplify(sp.diff(eg,R)-4*sp.pi*R**2*pe)==0
    assert sp.simplify(sp.diff(kinetic,R)*W+sp.diff(kinetic,W)*A
                       -4*sp.pi*R**2*W*rho*(R*A+sp.Rational(3,2)*W**2))==0
    audit=dict(status='PASS',stationary_native_cases=len(eq_checks),transient_native_cases=len(tr_checks),
               equilibrium_checks=eq_checks,transient_checks=tr_checks,reference_refinements=refinements,
               maximum_stationary_relative_error=max(max(x['relative_errors'].values()) for x in eq_checks),
               maximum_transient_normalized_waveform_error=max(max(x['waveform_errors'].values()) for x in tr_checks),
               maximum_native_energy_residual=max(x['energy_residual'] for x in tr_checks),
               symbolic_identities=['dEgel/dR=4pi R^2 pEl','dKhost/dt=4pi R^2 W rho(R acceleration+1.5 W^2)'],
               physical_validation='NOT PERFORMED: target activation, geometry, interfaces, rate properties and fracture data are missing.')
    (ROOT/'verification/NUMERICAL_AUDIT.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
    print({k:v for k,v in audit.items() if not isinstance(v,list)})

if __name__=='__main__':main()
