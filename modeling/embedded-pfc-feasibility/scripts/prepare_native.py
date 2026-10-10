import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    eq=list(csv.DictReader((ROOT/'data/equilibrium_comparison.csv').open(encoding='utf8')))
    def selected(x):
        return (float(x['radius']) in [.3e-6,3e-6] or x['name'].startswith('PFP_interface'))
    eq=[x for x in eq if selected(x)]
    # Native final stored stationary state has the declared baseline parameters.
    base=[x for x in eq if x['fluid']=='n-Perfluoropentane' and
          abs(float(x['radius'])-.3e-6)<1e-20 and float(x['shear'])==20000
          and x['name'].startswith('n-') and float(x['stretch'])==2.1]
    eq=[x for x in eq if x not in base]+base
    summaries=json.loads((ROOT/'data/transient_summary.json').read_text())
    out=['public class NativeCases {']
    names=[];values=[]
    for i,x in enumerate(eq):
        f=lambda k:float(x[k])
        q=[f('radius'),f('shear'),f('viscosity'),f('sigma_outer'),f('sigma_inner'),
           f('initial_PFC_mass_kg')/(4*3.141592653589793*f('radius')**3/3),
           # The independent initial internal reference is recomputed explicitly.
           0,1 if x['fluid']=='n-Perfluorohexane' else 0,f('stretch'),f('equilibrium_state_energy_J'),
           f('T_K'),f('liquid_density_kg_m3'),f('vapor_density_kg_m3'),f('bubble_radius_m')/f('R_m')]
        import sys
        sys.path.insert(0,str(ROOT/'.tools'))
        import CoolProp.CoolProp as CP
        q[6]=CP.PropsSI('Umass','T',f('initial_temperature'),'P',f('ambient')+2*f('sigma_outer')/f('radius'),x['fluid'])
        names.append(f"EQ_{i:03d}_{x['fluid'].split('-')[-1]}_r{f('radius')*1e6:g}_G{f('shear')/1000:g}_L{f('stretch'):g}")
        values.append(q)
        x['native_name']=names[-1]
    out.append('public static final String[] EQ_NAMES='+json.dumps(names).replace('[','{').replace(']','}')+';')
    out.append('public static final double[][] EQUILIBRIUM='+json.dumps(values).replace('[','{').replace(']','}')+';')
    values=[];names=[]
    for s in summaries:
        x=s['initial_phase_state'];r=s['radius']
        q=[r,s['shear'],s['viscosity'],s['sigma_outer'],s['sigma_inner'],
           s['initial_PFC_mass_kg']/(4*3.141592653589793*r**3/3),
           CP.PropsSI('Umass','T',s['initial_temperature'],'P',s['ambient']+2*s['sigma_outer']/r,s['fluid']),
           0,s['seed_stretch'],s['retained_seed_energy_J'],x['T_K'],
           x['liquid_density_kg_m3'],x['vapor_density_kg_m3'],x['bubble_radius_m']/x['R_m']]
        names.append(s['name']);values.append(q)
    out.append('public static final String[] TR_NAMES='+json.dumps(names).replace('[','{').replace(']','}')+';')
    out.append('public static final double[][] TRANSIENT='+json.dumps(values).replace('[','{').replace(']','}')+';')
    out.append('}')
    (ROOT/'scripts/NativeCases.java').write_text('\n'.join(out),encoding='utf8')
    (ROOT/'data/native_case_inputs.json').write_text(json.dumps({'equilibrium':eq,'transient':summaries},indent=2),encoding='utf8')
    print('PREPARED_NATIVE',len(eq),'stationary and',len(summaries),'transient cases')

if __name__=='__main__':main()
