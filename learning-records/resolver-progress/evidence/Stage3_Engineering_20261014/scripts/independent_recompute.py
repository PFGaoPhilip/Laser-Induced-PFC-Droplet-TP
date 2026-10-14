"""Independent Stage3 arithmetic only. Stdlib; no solver/production imports.

Run from any directory: python -B scripts/independent_recompute.py [--root PACKAGE].
Writes deterministic review/INDEPENDENT_RECOMPUTE.json. Source-only EOS values
and absent objective/certificate recomputations remain explicitly NOT_RUN.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    root = parser.parse_args().root.resolve()
    sources = {}
    def load(path):
        p = root / path
        sources[path] = hashlib.sha256(p.read_bytes()).hexdigest()
        return json.loads(p.read_text(encoding='utf-8-sig'))
    checks = []
    def check(ident, value, expected, unit, tier, path, selector, method):
        relative = abs(value-expected)/abs(expected) if expected else abs(value-expected)
        checks.append(dict(id=ident, status='PASS' if relative <= 1e-9 else 'FAIL',
                           value=value, source_value=expected, relative_difference=relative,
                           unit=unit, tier=tier, source=dict(path=path,selector=selector), method=method))
    tpath = 'inputs/conditional_termtex/verification.json'
    t = load(tpath)['numericalChecks']
    mass = t['density_kg_m3']*math.pi*t['jetRadius_m']**2*t['jetLength_m']
    speed = math.sqrt(2*t['availableWork_J']/mass)
    for key,value,unit in [('jetMass_kg',mass,'kg'),('energyVelocity_m_s',speed,'m/s'),
                           ('Mach',speed/t['soundSpeed_m_s'],'1'),
                           ('rigidPressure_Pa',t['density_kg_m3']*t['soundSpeed_m_s']*speed,'Pa'),
                           ('equalImpedancePressure_Pa',t['density_kg_m3']*t['soundSpeed_m_s']*speed/2,'Pa')]:
        check('T_'+key,value,t[key],unit,'R|A',tpath,'numericalChecks.'+key,'cylindrical mass; lossless energy; adopted linear contact')
    for species,phi in [('PFP',2.72e-9),('PFH',4.62e-9)]:
        key=species+'_10pgEnergyVelocity_m_s'
        check('T_'+key,math.sqrt(2*phi/1e-14),t[key],'m/s','R|A',tpath,'numericalChecks.'+key,'original rounded energy input, preserved unchanged')
    epath = 'inputs/expert_resolution/data/thermo_ceilings.json'
    thermo = load(epath)
    budgets = {}
    source_only = []
    for species,fluid in thermo['fluids'].items():
        row=next(x for x in fluid['droplet_table'] if x['d0_um']==6)
        budgets[species]=row['Phi_J']
        for key,value,unit in [('mass_kg',fluid['rho_l_T0_P0']*4*math.pi*row['a0_m']**3/3,'kg'),
                               ('Q_act_J',row['mass_kg']*row['q_act_J_kg'],'J'),
                               ('Phi_J',row['mass_kg']*row['psi_J_kg'],'J'),
                               ('eta_II',row['Phi_J']/row['Q_act_J'],'1'),
                               ('W_adiabatic_J',row['mass_kg']*row['w_adiabatic_J_kg'],'J'),
                               ('R_bound_over_a0',row['R_bound_exergy_m']/row['a0_m'],'1')]:
            check(species+'_'+key,value,row[key],unit,'R|A',epath,'fluids.'+species+'.droplet_table[d0_um=6].'+key,'stored-state arithmetic; not fresh EOS validation')
        source_only += [dict(id=species+'_radius_EOS',status='NOT_RUN',value=row['R_bound_exergy_m'],unit='m',tier='R|A',source=dict(path=epath,selector='fluids.'+species+'.droplet_table[d0_um=6].R_bound_exergy_m'),reason='accepted stable-EOS integral evaluation quoted; no independent EOS package/integration in this arithmetic review'),
                        dict(id=species+'_source_pressure_EOS',status='NOT_RUN',value=fluid['p_relax_spinodal'],unit='Pa absolute',tier='R|A',source=dict(path=epath,selector='fluids.'+species+'.p_relax_spinodal'),reason='accepted expansion-source premise/EOS evaluation quoted; no new EOS run or global sign proof')]
    energy_allowances=[dict(species=s,mass_pg=m,value_m_s=math.sqrt(2*phi/(m*1e-15)),tier='R|A',status='ARITHMETIC_ONLY') for s,phi in budgets.items() for m in [1,3,10,30,100]]
    rpath='inputs/expert_resolution/data/receiver_table.json'
    receiver=load(rpath)
    rho,n,B,p0=receiver['rho0'],receiver['n'],receiver['B'],thermo['P0_Pa']
    c=math.sqrt(n*(p0+B)/rho)
    Z=rho*c
    check('Tait_sound_speed',c,receiver['c_tait'],'m/s','E',rpath,'c_tait','derivative of adopted Tait isentrope at upstream state')
    def contact(u):
        # Compressive density ratio q>1: u^2=dp*(q-1)/(rho*q).
        if u == 0: return 0.0
        lo,hi=1.0,2.0
        def value(q): return (p0+B)*(q**n-1)*(q-1)/(rho*q)
        while value(hi)<u*u: hi*=2
        for _ in range(100):
            mid=(lo+hi)/2
            if value(mid)<u*u: lo=mid
            else: hi=mid
        return (p0+B)*(((lo+hi)/2)**n-1)
    def mixed(u):
        lo,hi=0.0,u
        for _ in range(100):
            v=(lo+hi)/2
            if contact(u-v)>Z*v: lo=v
            else: hi=v
        return Z*(lo+hi)/2
    for i,row in enumerate(receiver['rows']):
        check('receiver_rigid_'+str(i),contact(row['U']),row['p_rigid_tait'],'Pa','E',rpath,'rows['+str(i)+'].p_rigid_tait','independent compression-ratio bisection of mass/momentum jump plus Tait isentrope')
        check('receiver_mixed_'+str(i),mixed(row['U']),row['p_equal_impedance_tait'],'Pa','E',rpath,'rows['+str(i)+'].p_equal_impedance_tait','independent interface-speed bisection; jet nonlinear, target linear')
    hpath='inputs/expert_resolution/data/envelope_rows.json'
    envelope=load(hpath)
    for i,row in enumerate(envelope):
        for field,value,unit in [('m_pg',row['m_j']/1e-15,'pg'),('Ej_over_Phi',row['E_j']/budgets[row['fluid']],'1'),
                                 ('U_ceiling_at_mj',math.sqrt(2*budgets[row['fluid']]/row['m_j']),'m/s'),
                                 ('p_rec',2*row['p_h']*min(1,row['a_j_um']/row['d_um']),'Pa'),
                                 ('p_h',mixed(row['U']),'Pa')]:
            check('historical_'+str(i)+'_'+field,value,row[field],unit,'E' if field.startswith('p') else 'P',hpath,'rows['+str(i)+'].'+field,'stored profile arithmetic or independent mixed contact; not current whole-water/wall objective')
    summary=[]
    for species in ['PFP','PFH']:
        indexes=[i for i,row in enumerate(envelope) if row['fluid']==species]
        groups=[('slow_in_screen','U',[i for i in indexes if envelope[i]['mach']<=.3 and envelope[i]['closure'] in ['frozen','km_alpha0.1']],'P'),
                ('fast_in_screen','U',[i for i in indexes if envelope[i]['mach']<=.3 and envelope[i]['closure'] in ['isoeq','km_alpha1']],'P'),
                ('beyond_screen','U',[i for i in indexes if envelope[i]['mach']>.3],'E'),
                ('internal_contact_in_screen','p_h',[i for i in indexes if envelope[i]['mach']<=.3],'E'),
                ('receiver_estimate_in_screen','p_rec',[i for i in indexes if envelope[i]['mach']<=.3],'E')]
        for group,field,selected,tier in groups:
            ix=max(selected,key=lambda i:envelope[i][field]); row=envelope[ix]
            summary.append(dict(species=species,group=group,field=field,value=row[field],tier=tier,source=dict(path=hpath,row_index=ix),closure=row['closure'],gamma=row['gamma'],mach=row['mach']))
    kpath='inputs/expert_resolution/data/km_sweep.json'
    km=load(kpath)
    old_residuals=[]
    for i,row in enumerate(km):
        par=row['params']
        if abs(par['d0']-6e-6)>1e-15 or par['G']!=0 or par['x_air']!=0: continue
        ledger=row['energy_ledger']
        residual=ledger['Phi_activation']-ledger['Phi_content_at_Rmax']-sum(ledger[key] for key in ['E_surface','E_gel_elastic','D_viscous','E_acoustic_radiated_est'])
        naive=ledger['Phi_activation']-ledger['useful_work_to_Rmax']-ledger['Phi_content_at_Rmax']
        check('legacy_remainder_'+str(i),residual,ledger['exergy_destroyed_or_unaccounted'],'J','U',kpath,'rows['+str(i)+'].energy_ledger','Phi_activation minus Phi_content_at_Rmax minus stored surface/gel/viscous/acoustic terms; bookkeeping remainder is not measured destruction')
        old_residuals.append(dict(row_index=i,species=par['fluid'],mode=par['mode'],alpha_c=par['alpha_c'],remainder_J=residual,percent_of_Phi=100*residual/ledger['Phi_activation'],initial_naive_difference_J=naive-ledger['exergy_destroyed_or_unaccounted'],initial_naive_formula='Phi minus useful_work minus Phi_content omits the mechanical closure mismatch; corrected by independently summing stored terms'))
    h='inputs/full_closure/runs/AXI_PFP_transport_candidate030_STAGE2_LOOSENED_PILOT001/history.csv'
    raw=(root/h).read_bytes(); sources[h]=hashlib.sha256(raw).hexdigest()
    records=list(csv.DictReader(raw.decode('utf-8-sig').splitlines()))
    accepted=[(i+2,row) for i,row in enumerate(records) if row['stage']=='accepted']
    line,last=accepted[-1]; initial=records[0]
    last_numeric={key:float(value) for key,value in last.items() if key!='stage'}
    mass_drift={key:max(abs(float(row[key])-float(initial[key]))/float(initial[key]) for _,row in accepted) for key in ['water_mass_kg','PFC_mass_kg']}
    diagnostic=dict(source=h,source_sha256=sources[h],last_accepted_line=line,accepted_record_count=len(accepted),last_accepted=last_numeric,time_ns=last_numeric['time_s']*1e9,max_relative_mass_drift=mass_drift,objective_event_established=False,completion_established=False,ledger_residual_recomputed=None,reason='history contains diagnostics, not a complete exergy ledger, registered observers, or objective event; legacy meta exit is not candidate030 completion')
    seed=20261014
    sampled=random.Random(seed).sample(range(len(envelope)),2)
    objective_path='inputs/full_closure/data/STAGE3_RESULTS_LEDGER_001.json'
    status=load(objective_path)
    assert len(status['objective_results'])==18
    assert all(row['value'] is None and row['maximizing_design'] is None for row in status['objective_results'])
    objectives=[dict(id=row['id'],status='NOT_RUN',value=None,attained_lower=None,global_upper=None,maximizing_design=None,reason='no registered objective evidence run or certificate supplied; inherited Stage2 waiver') for row in status['objective_results']]
    result=dict(schema='stage3_independent_arithmetic_review_v1',deterministic=True,seed=seed,production_code_imported=False,solver_rerun=False,
                checks=checks,source_only_EOS_checks=source_only,max_arithmetic_relative_difference=max(x['relative_difference'] for x in checks),
                energy_allowances=energy_allowances,historical_summary=summary,historical_processed_rows=len(envelope),historical_random_record_indices=sampled,
                historic_remainders=old_residuals,candidate030_diagnostics=diagnostic,objective_recompute=objectives,
                certificate_recompute=dict(status='NOT_RUN',x_star=None,random_evidence_runs=None,J_U=None,J_P=None,R=None,Richardson_delta_num=None,J_up=None,reason='no x_star/evidence-run/refinement/certificate records; seed does not create missing samples'),sources=sources,
                interpretation='Arithmetic PASS establishes agreement with stored adopted inputs; it does not establish material validity, registered objective feasibility, certification, or device transfer.')
    output=root/'review/INDEPENDENT_RECOMPUTE.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8',newline='\n')
    print('Independent arithmetic:',len(checks),'checks;',sum(x['status']=='FAIL' for x in checks),'failures; maximum relative difference',result['max_arithmetic_relative_difference'])


if __name__=='__main__':
    main()
