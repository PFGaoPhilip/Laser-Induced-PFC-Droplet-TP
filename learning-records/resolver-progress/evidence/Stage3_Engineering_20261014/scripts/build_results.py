"""Deterministic documentation ledger/table rebuild from bundled reporting records."""
from pathlib import Path
import json, hashlib, math, csv
ROOT=Path(__file__).resolve().parents[1]
def read(rel):return json.loads((ROOT/rel).read_text(encoding='utf-8-sig'))
def source(rel,record):return {'path':rel,'record':record,'sha256':hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()}
def main():
    inherited=read('inputs/full_closure/data/STAGE3_RESULTS_LEDGER_001.json')
    prep=read('inputs/full_closure/data/accepted_preparation.json')
    ceiling=[]
    for species in ['PFP','PFH']:
        phi=prep['fluids'][species]['activated_budget']['Phi_J']
        for mass in [1,3,10,30,100]:
            ceiling.append({'id':species+'_ENERGY_CEILING_'+str(mass)+'pg','species':species,'mass_pg':mass,'value':math.sqrt(2*phi/(mass*1e-15)),'units':'m/s','tier':'R|A','available_work_J':phi,'formula':'sqrt(2*Phi_a/(mass_pg*1e-15))','source':source('inputs/full_closure/data/accepted_preparation.json','fluids.'+species+'.activated_budget.Phi_J'),'validity':'Conditional whole-water mass-qualified ceiling only if full-vector water kinetic energy never exceeds the available-work budget and all remaining availability terms are nonnegative. Not established for the loosened trajectory and not an attained objective.'})
    tpath='inputs/conditional_termtex/verification.json'
    linear={'values':read(tpath)['numericalChecks'],'tier':'R','source':source(tpath,'numericalChecks'),'validity':'Prescribed illustrative plug; lossless conversion, normal planar small-compression contact before lateral release. Distinct from solved finite-disk/time-averaged receiver pressure.'}
    erel='inputs/expert_resolution/data/envelope_rows.json';rows=read(erel);historical=[]
    for species in ['PFP','PFH']:
        selections=[('slow_in_screen','U','P',lambda r:r['mach']<=0.3 and r['closure'] in ['frozen','km_alpha0.1']),('fast_in_screen','U','P',lambda r:r['mach']<=0.3 and r['closure'] in ['isoeq','km_alpha1']),('beyond_screen','U','E',lambda r:r['mach']>0.3),('internal_contact_in_screen','p_h','E',lambda r:r['mach']<=0.3),('receiver_estimate_in_screen','p_rec','E',lambda r:r['mach']<=0.3)]
        for group,field,tier,test in selections:
            candidates=[(i,r) for i,r in enumerate(rows) if r['fluid']==species and test(r)]
            idx,row=max(candidates,key=lambda pair:pair[1][field])
            historical.append({'id':species+'_'+group,'species':species,'group':group,'value':row[field],'units':'m/s' if field=='U' else 'Pa','tier':tier,'gamma':row['gamma'],'closure':row['closure'],'profile_mass_pg':row['m_pg'],'mach':row['mach'],'sampled_axial_energy_J':row['E_j'],'source':source(erel,'['+str(idx)+'].'+field),'validity':'Largest stored historical group sample; incompressible/spherical-content reduced model, geometric sampled profile and a 0.3 Mach working screen. Speeds are not current whole-water mass quantiles. E_j is sampled axial kinetic energy, a lower bound on the sampled-region full-vector kinetic energy. Pressure values are mixed-contact/spreading estimates, not solved registered wall observers. No continuous optimum/certificate.'})
    for obj in inherited['objective_results']:
        obj['species']=obj['id'].split('_')[0]
        obj['relative_gap_target']=0.05 if '_U_' in obj['id'] else 0.1
        obj['numerical_error']=None;obj['domain_sensitivity']=None;obj['certificate_gap']=None
        obj['execution_status']='NOT_RUN';obj['exit_disposition']='WAIVED'
        obj['source']=source('inputs/full_closure/data/STAGE3_RESULTS_LEDGER_001.json','objective_results[id='+obj['id']+']')
        obj['missing_evidence_consequence']='No event-complete registered observer trajectory, feasible attained design, refinement or global certificate; no numerical optimum or certified interval can be supplied.'
    ledger={'schema':'stage3_engineering_results_v2','verdict':'DOCUMENTATION_COMPLETE_SCIENTIFIC_MAXIMUM_UNRESOLVED','strict_acceptance':False,'scope':{'species':['PFP','PFH'],'initial_unheated_diameter_um':6,'gamma_min':1.25,'gamma_max':None,'alpha_c':[0,1],'whole_water_mass_pg':[1,3,10,30,100],'pressure_disk_radius_um':[2,10],'pressure_window_ns':[2,20],'coordinates':'axisymmetric (r,z), receiver z=0, w=-u_z; absolute pressure except explicitly gauge observers','radius_definition':'gamma=h/R_m using free-field maximum radius of the SAME activated-droplet model; R_m/gamma qualification unresolved','observer_event_definitions_source':source('inputs/full_closure/PROBLEM_STATEMENT.md','P02-P06 and event amendment002'),'model_identity':'candidate030 with inherited018-030 soft-passes','certificate_targets':{'velocity_gap':0.05,'pressure_gap':0.1,'numerical_error_fraction_of_epsilon':1/3,'domain_sensitivity_fraction_of_epsilon':0.1}},'objective_results':inherited['objective_results'],'ceilings':ceiling,'linear_example':linear,'historical':historical,'historical_processed_row_count':len(rows),'historical_count_caveat':'The envelope_rows.json processed table has35 rows; older prose describes40 sampled cases. This document reports stored table rows and does not infer40 valid completed cases.','diagnostics':inherited['diagnostics'],'metadata_caveats':inherited['metadata_caveats'],'exit_waivers':inherited['exit_waivers'],'waiver_authority':source('inputs/full_closure/verification/STAGE2_LOOSENED_CLOSED_20261013.md','B. Stage2 exit-gate waivers'),'certified_maximum_available':False,'device_maximum_resolved':False,'engineering_envelope_supplied':False,'source_version_policy':'Dated closeout/waiver records and verified receipt002 control Stage3 entry; historic draft/incomplete wording remains provenance, not an entry gate. Original candidate030 metadata remains unchanged.'}
    (ROOT/'RESULTS_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    ledger['historical_failure_timeline']=[{'id':'candidate028_pilot_failure','time_s':4.400000000000003e-10,'accepted_steps':44,'exit_code':136,'tier':'diagnostic','source':source('inputs/full_closure/verification/STAGE2_PILOT_FAILURE_001.md','Exact failure'),'validity':'Historical failure, not an objective event or a physical screen.'},{'id':'candidate029_heat_abort','time_s':3.7e-10,'heat_status':4,'integrator_status':11,'tier':'diagnostic','source':source('inputs/full_closure/verification/STAGE2_PREREG_AMENDMENT_006_CANDIDATE030.json','parent_failure'),'validity':'Recorded prior abort; no completed trajectory inferred.'}]
    ledger['claim_map']={'accepted_T_route':'linear_example and inputs/conditional_termtex/equations.json E01-E24','preparation_constants_and_available_work':'scope, ceilings and inputs/full_closure/data/accepted_preparation.json','speed_allowance_table':'ceilings','historical_group_table':'historical','processed_row_count':'historical_processed_row_count','eighteen_objective_slots':'objective_results','conditional_domain_and_observers':'scope','diagnostic_endpoint_line_and_step':'diagnostics','earlier_failures':'historical_failure_timeline','metadata_caveats_and_waiver_inventory':'metadata_caveats, exit_waivers, waiver_authority','error_gap_targets':'scope.certificate_targets','absence_of_certified_or_device_maximum':'certified_maximum_available, device_maximum_resolved, engineering_envelope_supplied'}
    ledger['accepted_preparation_records']={'values':prep,'tier':'R|A / adopted-state inputs','source':source('inputs/full_closure/data/accepted_preparation.json','all accepted preparation fields'),'fresh_EOS_validation':'NOT_RUN'}
    thermo=read('inputs/expert_resolution/data/thermo_ceilings.json')
    ledger['accepted_eos_quotations']=[]
    for species in ['PFP','PFH']:
        fluid=thermo['fluids'][species];droplet=next(r for r in fluid['droplet_table'] if r['d0_um']==6)
        for quantity,value,units,selector in [('expansion_source_pressure',fluid['p_relax_spinodal'],'Pa absolute','fluids.'+species+'.p_relax_spinodal'),('cavity_radius_availability_bound',droplet['R_bound_exergy_m'],'m','fluids.'+species+'.droplet_table[d0_um=6].R_bound_exergy_m')]:
            ledger['accepted_eos_quotations'].append({'species':species,'quantity':quantity,'value':value,'units':units,'tier':'R|A','fresh_validation_status':'NOT_RUN','source':source('inputs/expert_resolution/data/thermo_ceilings.json',selector),'validity':'Quoted accepted EOS evaluation under its original assumptions/sign conditions. Expansion source pressure does not cap collapse/contact pressure; cavity radius bound is not same-model R_m qualification. No fresh EOS/sign-path audit or production adoption.'})
    receiver=read('inputs/expert_resolution/data/receiver_table.json')
    ledger['historical_pressure_model_inputs']={'values':{k:v for k,v in receiver.items() if k!='rows'},'tier':'E adopted Tait/mixed contact inputs','source':source('inputs/expert_resolution/data/receiver_table.json','rho0,c_tait,n,B,Z_water'),'validity':'Historical isentrope/mixed contact estimate, not a verified caloric Hugoniot or solved wall observer.'}
    spath='inputs/full_closure/verification/STAGE1_CANDIDATE028_VERIFIED_LOOSENED_ACCEPTANCE_20261014.json'
    ledger['soft_pass_inventory']={'inherited018_028':read(spath)['soft_pass_inventory'],'source':source(spath,'soft_pass_inventory'),'candidate029_source':source('inputs/full_closure/verification/STAGE2_PREREG_AMENDMENT_005_CANDIDATE029.json','repair.soft_passes_added'),'candidate030_source':source('inputs/full_closure/verification/STAGE2_PREREG_AMENDMENT_006_CANDIDATE030.json','repair.soft_passes'),'status':'INHERITED_ENGINEERING_ASSUMPTIONS; strict production admission remains FAIL'}
    ipath='review/INDEPENDENT_RECOMPUTE.json'
    if (ROOT/ipath).exists():
        independent=read(ipath)
        ledger['available_review_diagnostics']={'values':independent['candidate030_diagnostics'],'arithmetic_check_count':len(independent['checks']),'maximum_relative_arithmetic_difference':independent['max_arithmetic_relative_difference'],'source':source(ipath,'candidate030_diagnostics; checks; max_arithmetic_relative_difference'),'validity':'Narrow arithmetic/source review, not full-cycle G2/G5. Fresh EOS and certificate recomputation remain NOT_RUN.'}
    (ROOT/'RESULTS_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    certificate={'schema':'stage3_certificate_absence_record_v1','status':'NOT_RUN','is_certificate':False,'reason':'No attained objectives, maximizing designs, refinement, hold-outs or global upper values supplied; exit waived for documentation only.','objective_results':[{key:row[key] for key in ['id','value','attained_lower','global_upper','maximizing_design','numerical_error','domain_sensitivity','certificate_gap','certified']} for row in inherited['objective_results']]}
    (ROOT/'CERTIFICATE.json').write_text(json.dumps(certificate,indent=2)+'\n',encoding='utf-8')
    out=ROOT/'data';out.mkdir(exist_ok=True)
    with (out/'CONDITIONAL_ENERGY_CEILINGS.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f);writer.writerow(['species','mass_pg','available_work_J','ceiling_m_s','tier'])
        for row in ceiling:writer.writerow([row['species'],row['mass_pg'],row['available_work_J'],row['value'],row['tier']])
    with (out/'OBJECTIVE_STATUS.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f);writer.writerow(['id','units','value','attained_lower','global_upper','maximizing_design','status','exit_disposition'])
        for row in inherited['objective_results']:writer.writerow([row['id'],row['units'],'null','null','null','null',row['status'],row['exit_disposition']])
    print('Rebuilt RESULTS_LEDGER.json and two documentation tables; objectives remain null.')
if __name__=='__main__':main()
