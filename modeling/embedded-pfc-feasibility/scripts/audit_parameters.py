"""Stability, optical-energy and crack-energy screens; all are conditional."""
import csv,json
from dataclasses import fields
from math import pi
import numpy as np
from scipy.optimize import root
from pfc_model import ROOT,Case,Pfc,gel,write_csv


def stationary_perturbation(p,R,base,bath=False):
    c=p.c;V=4*pi*R**3/3
    initial=[base['T_K'],np.log(base['liquid_density_kg_m3']),
             np.log(base['vapor_density_kg_m3']),np.log(base['bubble_radius_m'])]
    target=base['equilibrium_state_energy_J']
    if bath:initial=initial[1:]
    def f(x):
        T,lr,lv,lb=([base['T_K'],*x] if bath else x)
        rl,rv,b=np.exp([lr,lv,lb]);pl,pv,ul,uv,gl,gv=p.phase(T,rl,rv)
        Vb=4*pi*b**3/3;ml,mv=rl*(V-Vb),rv*Vb
        residual=[(pv-pl-2*c.sigma_inner/b)/1e5,(gl-gv)/1e5,(ml+mv)/p.mass-1]
        if not bath:
            energy=(ml*ul+mv*uv-p.mass*p.u0+gel(c,R)[1]+c.ambient*(V-p.V0)
                    +4*pi*(c.sigma_outer*(R**2-c.radius**2)+c.sigma_inner*b*b))
            residual.append((energy-target)/(p.mass*1e5))
        return residual
    s=root(f,initial,tol=1e-10)
    if max(abs(np.array(f(s.x))))>1e-7:raise RuntimeError('Stability perturbation failed')
    T,lr,lv,lb=([base['T_K'],*s.x] if bath else s.x)
    snap=p.snapshot(R,T,*np.exp([lr,lv,lb]))
    p.validate(snap)
    return snap['liquid_pressure_Pa']-(c.ambient+gel(c,R)[0]+2*c.sigma_outer/R)


def main():
    raw=list(csv.DictReader((ROOT/'data/equilibrium_comparison.csv').open(encoding='utf8')))
    names={x.name for x in fields(Case)}
    stability=[]; optical=[]
    for row in raw:
        numeric={k:(v if k in ['name','fluid'] else float(v)) for k,v in row.items()}
        c=Case(**{k:v for k,v in numeric.items() if k in names});p=Pfc(c)
        lam=numeric['stretch'];eps=1e-4
        st=dict(name=c.name,fluid=c.fluid,radius_m=c.radius,shear_Pa=c.shear,stretch=lam)
        for bath in [False,True]:
            force=[stationary_perturbation(p,c.radius*(lam+d),numeric,bath) for d in [-eps,eps]]
            key=('fixed_bath' if bath else 'closed_energy')+'_restoring_Pa_per_stretch'
            st[key]=-(force[1]-force[0])/(2*eps)
            finer=[stationary_perturbation(p,c.radius*(lam+d),numeric,bath) for d in [-eps/2,eps/2]]
            st[key+'_half_step']=-(finer[1]-finer[0])/eps
            st[key+'_step_relative_change']=abs(st[key]-st[key+'_half_step'])/max(abs(st[key+'_half_step']),1.)
        b=numeric['bubble_radius_m'];Vb=4*pi*b**3/3
        Vl=4*pi*(lam*c.radius)**3/3-Vb
        rl=numeric['liquid_density_kg_m3'];rv=numeric['vapor_density_kg_m3']
        kl=numeric['liquid_compressibility_slope_Pa_m3_kg']/Vl
        kv=numeric['vapor_compressibility_slope_Pa_m3_kg']/Vb
        bulk=kl*kv*(rl-rv)**2/(kl*rv+kv*rl)
        cap=c.sigma_inner/(2*pi*b**4)
        st.update(core_phase_Hessian_Pa_per_m3=bulk-cap,
                  core_phase_bulk_to_capillary_Hessian_ratio=bulk/cap,
                  core_phase_mass_curvature_J_per_kg2=kl/rl+kv/rv)
        stability.append(st)
        if lam==2.1:
            F=200. # 20 mJ/cm2 = 200 J/m2, illustrative local incident fluence
            Q=numeric['equilibrium_state_energy_J']
            optical.append(dict(name=c.name,fluid=c.fluid,radius_m=c.radius,shear_Pa=c.shear,
                                sigma_outer_N_m=c.sigma_outer,stretch=lam,T_K=numeric['T_K'],
                                state_energy_J=Q,vapor_mass_fraction=numeric['vapor_fraction'],
                                incident_disk_energy_J=F*pi*c.radius**2,
                                required_effective_cross_section_ratio=Q/(F*pi*c.radius**2),
                                elasto_capillary_Ga_over_sigma=c.shear*c.radius/c.sigma_outer,
                                viscous_scale_eta_over_a_sqrt_rhop=c.viscosity/(c.radius*np.sqrt(c.host_density*1e5)),
                                pulse_Fourier_host_alpha_5ns=1.4e-7*5e-9/c.radius**2,
                                closed_energy_restoring_Pa_per_stretch=st['closed_energy_restoring_Pa_per_stretch']))
    write_csv(ROOT/'data/stability_comparison.csv',stability)
    write_csv(ROOT/'data/optical_energy_screen.csv',optical)
    transient=json.loads((ROOT/'data/transient_summary.json').read_text())
    fracture=[]
    for s in transient:
        if s['viscosity']!=.01:continue
        for cover in [1e-6,5e-6,20e-6,50e-6]:
            for halfwidth in [.5e-6,1e-6,5e-6]:
                for gc in [.1,1,10,100]:
                    # A rectangular slit projected area includes both faces in Gc.
                    # A retained-seed-energy-only allocation screen. This is NOT
                    # a universal fracture-work bound: other reference-subtracted
                    # energies may decrease when a new topology opens.
                    req=gc*2*halfwidth*cover
                    ratio=s['retained_seed_energy_J']/req
                    d=s['radius']+cover
                    surface_stretch=d/s['radius']
                    fracture.append(dict(case=s['name'],cover_m=cover,slit_halfwidth_m=halfwidth,
                                         fracture_energy_J_m2=gc,projected_crack_area_m2=2*halfwidth*cover,
                                         fracture_work_only_J=req,retained_seed_energy_J=s['retained_seed_energy_J'],
                                         retained_seed_energy_over_fracture_work=ratio,
                                         center_to_surface_m=d,surface_encounter_stretch=surface_stretch,
                                         standoff_over_max_radius=d/(s['maximum_stretch']*s['radius']),
                                         geometry_gate='intersects_initial_free_surface_plane' if s['maximum_stretch']>=surface_stretch else 'finite_domain_check_required',
                                         screen='requires_more_than_retained_seed_energy_alone' if ratio<1 else 'within_retained_seed_only_budget_not_proved'))
    write_csv(ROOT/'data/fracture_energy_screen.csv',fracture)
    audit=dict(equilibrium_states=len(raw),stability_states=len(stability),fracture_screens=len(fracture),
               closed_energy_unstable_states=sum(x['closed_energy_restoring_Pa_per_stretch']<=0 for x in stability),
               fixed_bath_unstable_states=sum(x['fixed_bath_restoring_Pa_per_stretch']<=0 for x in stability),
               core_phase_fixed_T_V_m_unstable_states=sum(x['core_phase_Hessian_Pa_per_m3']<=0 for x in stability),
               min_core_phase_bulk_to_capillary_Hessian_ratio=min(x['core_phase_bulk_to_capillary_Hessian_ratio'] for x in stability),
               max_closed_energy_slope_step_relative_change=max(x['closed_energy_restoring_Pa_per_stretch_step_relative_change'] for x in stability),
               max_fixed_bath_slope_step_relative_change=max(x['fixed_bath_restoring_Pa_per_stretch_step_relative_change'] for x in stability),
               closed_energy_slope_sign_changes=sum(x['closed_energy_restoring_Pa_per_stretch']*x['closed_energy_restoring_Pa_per_stretch_half_step']<=0 for x in stability),
               note='Local reduced-radial restoration and fixed-(T,V,m) internal Hessian do not prove global stability, morphology, or nucleation accessibility.')
    (ROOT/'verification/PARAMETER_AUDIT.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
    print(json.dumps(audit))

if __name__=='__main__':main()
