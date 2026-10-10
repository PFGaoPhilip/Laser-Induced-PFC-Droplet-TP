"""Audit native COMSOL numbers against independent dimensional calculations."""
from __future__ import annotations
import csv
import hashlib
import json
import re
from pathlib import Path

import numpy as np
import sympy as sp

from reference import ROOT


def read_native(path):
    lines=Path(path).read_text(encoding='utf-8-sig').splitlines()
    header=next(x for x in lines if x.startswith('% Time'))[2:]
    names=[re.sub(r' \([^)]*\)$','',n) for n in next(csv.reader([header]))][1:]
    a=np.loadtxt(path,comments='%',delimiter=',',ndmin=2)[:,1:]
    return {n:a[:,i] for i,n in enumerate(names)}


def peak(values,key): return float(np.max(values[key]))


def main():
    summaries=json.loads((ROOT/'data/reference_summary.json').read_text(encoding='utf-8'))
    register=[]
    for s in summaries:
        name=s['name'];n=read_native(ROOT/'data'/f'{name}_native.csv')
        ref=np.genfromtxt(ROOT/'data'/f'{name}_reference.csv',delimiter=',',names=True)
        t=n['time_s']
        if not all(np.all(np.isfinite(v)) for v in n.values()): raise AssertionError(name+' nonfinite output')
        errs={}
        for key,scale in [('u_m_s',max(s['max_jet_speed_m_s'],1)),
                          ('r_m',s['chamber_radius']),
                          ('source_gauge_Pa',max(s['source_pressure_peak_gauge_Pa'],1)),
                          ('wall_speed_m_s',max(float(np.max(abs(ref['wall_speed_m_s']))),1))]:
            truth=np.interp(t,ref['time_s'],ref[key])
            errs[key]=float(np.max(np.abs(n[key]-truth))/scale)
        maxerr=max(errs.values())
        energy=peak({"e":np.abs(n['residual'])},'e')
        if maxerr>0.001: raise AssertionError(f'{name} waveform mismatch {errs}')
        if energy>1e-6: raise AssertionError(f'{name} energy residual {energy}')
        umax=peak(n,'u_m_s');qmax=peak(n,'jet_dynamic_Pa')
        if umax>s['energy_only_speed_ceiling_m_s']*(1+1e-8): raise AssertionError('energy ceiling')
        if peak(n,'port_stroke_fraction')>1+1e-6: raise AssertionError('finite stroke')
        if min(n['source_gauge_Pa'])+s['ambient']<=0: raise AssertionError('absolute gas pressure')
        if peak(n,'communication_ratio')>0.1: raise AssertionError('uniform pressure communication screen')
        if max(peak(n,'liquid_Mach'),peak(n,'wall_Mach'))>0.1: raise AssertionError('Mach screen')
        if not s['open_port'] and (umax>1e-10 or peak(n,'emitted_impulse_N_s')>1e-18): raise AssertionError('sealed control emits liquid')
        if np.any(n['emitted_impulse_N_s']**2 > 2*n['emitted_mass_kg']*n['emitted_energy_J']+1e-28): raise AssertionError('emitted momentum/energy bound')
        register.append({'name':name,'native_samples':len(t),
                         'output_step_s':float(t[1]-t[0]),'last_time_s':float(t[-1]),
                         'event_reference':s['stop_event'],'reference_event_time_s':s['event_time_s'],
                         'native_max_jet_speed_m_s':umax,
                         'native_max_source_gauge_Pa':peak(n,'source_gauge_Pa'),
                         'native_max_jet_dynamic_Pa':qmax,
                         'native_max_elastic_Pa':peak(n,'elastic_Pa'),
                         'native_max_hemisphere_force_N':peak(n,'confinement_hemisphere_force_N'),
                         'native_max_stretch':peak(n,'wall_stretch'),
                         'native_max_communication':peak(n,'communication_ratio'),
                         'native_max_Mach':max(peak(n,'liquid_Mach'),peak(n,'wall_Mach')),
                         'max_native_energy_residual':energy,
                         'normalized_waveform_errors':errs,
                         'max_normalized_waveform_error':maxerr,
                         'energy_only_speed_ceiling_m_s':s['energy_only_speed_ceiling_m_s'],
                         'energy_only_dynamic_pressure_ceiling_Pa':s['energy_only_dynamic_pressure_ceiling_Pa'],
                         'source_energy_J':s['energy'],'port_radius_m':s['port_radius'],
                         'last_native_state':{k:float(v[-1]) for k,v in n.items()},
                         'status':'PASS'})

    time_checks=[]
    for name in ['A_baseline','B_open_baseline']:
        original=read_native(ROOT/'verification'/f'{name}_original_baseline.csv')
        old=read_native(ROOT/'verification'/f'{name}_coarse_2ns.csv')
        fresh=read_native(ROOT/'verification'/f'{name}_fresh_process_baseline.csv')
        fine=read_native(ROOT/'data'/f'{name}_native.csv')
        scale=max(peak(old,'u_m_s'),1)
        reproducible=abs(peak(fresh,'u_m_s')-peak(original,'u_m_s'))/scale
        refinement=abs(peak(fine,'u_m_s')-peak(old,'u_m_s'))/scale
        if reproducible>1e-8 or refinement>0.001: raise AssertionError('fresh process / temporal convergence')
        if abs(fine['u_m_s'][0])>1e-10 or abs(fine['wall_speed_m_s'][0])>1e-10: raise AssertionError('zero initial velocity')
        time_checks.append({'name':name,'fresh_process_peak_relative_error':reproducible,
                            '2ns_to_1ns_peak_relative_change':refinement,
                            'refined_zero_initial_liquid_velocity':float(fine['u_m_s'][0]),
                            'refined_zero_initial_wall_velocity':float(fine['wall_speed_m_s'][0]),
                            'status':'PASS'})

    # These symbolic identities check algebra; they are not peer review.
    R,R0,G=sp.symbols('R R0 G',positive=True)
    pel=G/2*(5-4*R0/R-(R0/R)**4)
    wg=2*sp.pi*G*(5*R**3/3-2*R0*R**2+R0**4/R-2*R0**3/3)
    symbolic={'gel_traction_work_identity':str(sp.simplify(sp.diff(wg,R)-4*sp.pi*R**2*pel)),
              'reference_elastic_work':str(sp.simplify(wg.subs(R,R0))),
              'reference_elastic_pressure':str(sp.simplify(pel.subs(R,R0))),
              'small_strain_pressure_slope':str(sp.simplify(sp.diff(pel,R).subs(R,R0))),
              'gel_large_expansion_pressure_limit':str(sp.limit(pel,R,sp.oo))}
    if any(symbolic[x]!='0' for x in ['gel_traction_work_identity','reference_elastic_work','reference_elastic_pressure']): raise AssertionError('gel algebra')
    p0,v,v0,k=sp.symbols('p0 v v0 k',positive=True)
    gas=p0*v0**k*v**(1-k)/(k-1)
    symbolic['gas_adiabatic_first_law']=str(sp.simplify(sp.diff(gas,v)+p0*(v0/v)**k))
    if symbolic['gas_adiabatic_first_law']!='0': raise AssertionError('gas algebra')

    md=(ROOT/'MODEL_SPEC.md').read_text(encoding='utf-8')
    displays=re.findall(r'\$\$(.*?)\$\$',md,re.S)
    identifiers=re.findall(r'\*\*Eq\. \((E\d+[a-z]?)\)',md)
    declarations=re.findall(r'\*\*Symbols before Eq\. \((E\d+[a-z]?)\)',md)
    if len(displays)!=29 or len(set(identifiers))!=29 or identifiers!=declarations: raise AssertionError('display/declaration coverage')
    equations=re.findall(r'"tau\*\([^\n]+', (ROOT/'scripts/MinimalCavitation.java').read_text(encoding='utf-8'))
    if 'sin(' in ''.join(equations) or 'cos(' in ''.join(equations): raise AssertionError('periodic driving')
    files=[]
    for p in sorted((ROOT/'models').glob('*.mph')):
        files.append({'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    if len(files)!=2: raise AssertionError('deliver exactly two native final files')
    baseline=next(x for x in register if x['name']=='A_baseline')
    b=next(x for x in register if x['name']=='B_open_baseline')
    ratio=b['native_max_jet_speed_m_s']/baseline['native_max_jet_speed_m_s']
    report={'status':'PASS','native_case_count':len(register),
            'physics':'GlobalEquations only, verified by fresh COMSOL reload',
            'periodic_loading':False,'optical_pulse_marker_ns':10,
            'mathematical_displays':len(displays),'local_symbol_declarations':len(declarations),
            'maximum_native_energy_residual':max(x['max_native_energy_residual'] for x in register),
            'maximum_native_reference_normalized_waveform_error':max(x['max_normalized_waveform_error'] for x in register),
            'maximum_communication_screen':max(x['native_max_communication'] for x in register),
            'first_event_velocity_transmission':ratio,
            'first_event_dynamic_pressure_transmission':ratio**2,
            'first_event_emitted_energy_transmission':b['last_native_state']['emitted_energy_J']/baseline['last_native_state']['emitted_energy_J'],
            'first_event_emitted_impulse_transmission':b['last_native_state']['emitted_impulse_N_s']/baseline['last_native_state']['emitted_impulse_N_s'],
            'temporal_and_fresh_process_checks':time_checks,
            'symbolic_algebra_checks':symbolic,'native_files':files,
            'independent_peer_review':'Not performed; independent numerical integration and self-audit are distinguished from peer review.',
            'unresolved_calibration':['PFC EOS / phase inventory','post-activation source-state and laser conversion calibration','rate-dependent gel properties','actual outlet geometry / fracture / focusing / target pressure']}
    (ROOT/'verification/NUMERICAL_AUDIT.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    (ROOT/'data/native_case_register.json').write_text(json.dumps(register,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
