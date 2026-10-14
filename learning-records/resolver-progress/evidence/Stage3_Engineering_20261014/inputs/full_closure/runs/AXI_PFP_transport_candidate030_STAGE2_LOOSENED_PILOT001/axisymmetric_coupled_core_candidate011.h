/* Candidate011 adds selected Fourier and viscous source half-steps to the
 * existing assembled resolved-activation core. This remains a finite
 * component candidate: full-route source/error/event admission, radiative
 * boundaries, and production qualification are still absent.
 */
#ifndef CLOSURE_AXISYMMETRIC_COUPLED_CORE_CANDIDATE011_H
#define CLOSURE_AXISYMMETRIC_COUPLED_CORE_CANDIDATE011_H
#include "geometric_flow.h"
#include "curvature.h"
#include "axisymmetric_interface_geometry.h"
#include "coupled_phase_bridge.h"
#include "coupled_thermal_bridge.h"
scalar leaf_index[],phase_composition_trial[];
static unsigned long axis_leaf_count;
static void * axis_spinodal_caches;
static double axis_inventory,axis_alpha,axis_critical_temperature;
static double axis_sigma=.072;
typedef struct {
  double phase_entropy_HKS_J_K,phase_entropy_bulk_J_K;
  double phase_entropy_primitive_remainder_J_K,phase_clock_error_mass_s;
  double heat_entropy_J_K,heat_energy_defect_J,capillary_work_J,mechanical_entropy_J_K;
  double area_m2,geometry_water_volume_defect_m3,geometry_PFC_volume_defect_m3;
  long double water_Fourier_entropy_J_K,viscous_entropy_J_K;
  long double water_Fourier_boundary_energy_out_J,viscous_boundary_energy_out_J;
  long double water_Fourier_energy_defect_J,viscous_intrinsic_work_defect_J;
  long double converted_transport_energy_roundoff_J,converted_transport_momentum_roundoff_kg_m_s;
  unsigned long phase_evaluations,spinodal_warm,spinodal_global,phase_nodes;
  unsigned long heat_evaluations,patches,geometry_failures;
  unsigned long water_Fourier_faces,viscous_faces,water_Fourier_iterations;
} ClosureAxisymmetricCoreStats;
static ClosureAxisymmetricCoreStats axis_statistics;

static double closure_axisymmetric_physical_volume(Point point) {
  return 2.*pi*dv();
}
/* Native reconstruction uses the smaller independently stored positive
 * material for representability, then orients its plane PFC->water. Raw
 * and reconstructed volumes remain separate; no thermodynamic reset. */
static int closure_axisymmetric_geometry(ClosureAxisymmetricGeometry * records) {
  vector normalF[],normalW[];scalar alphaF[],alphaW[];
  reconstruction(f_PFC,normalF,alphaF);reconstruction(a_water,normalW,alphaW);
  int failures=0;double area=0.,defectW=0.,defectF=0.;
  foreach(serial) {
    int k=(int)leaf_index[];int smaller_water=a_water[]<f_PFC[];
    double nx=smaller_water?-normalW.x[]:normalF.x[];
    double ny=smaller_water?-normalW.y[]:normalF.y[];
    double alpha=smaller_water?-alphaW[]:alphaF[];
    double volume=closure_axisymmetric_physical_volume(point);
    long double physical_mass_F=(long double)M_PFC[]*volume;
    long double physical_mass_W=(long double)M_water[]*volume;
    if((M_PFC[]>0. && !((double)physical_mass_F>0.)) ||
       (M_water[]>0. && !((double)physical_mass_W>0.))) {
      fprintf(stderr,"AXI binary64 geometry-mass conversion refusal x=%.17g r=%.17g mF=%.21Lg mW=%.21Lg\n",
        x,y,physical_mass_F,physical_mass_W);failures++;continue;
    }
    ClosureAxisymmetricGeometryInput input={x,y,Delta,nx,ny,alpha,f_PFC[],a_water[],
      (double)physical_mass_F,(double)physical_mass_W,.598};
    int status=closure_axisymmetric_interface_geometry(&input,&records[k]);
    if(status) {
      fprintf(stderr,"AXI geometry refusal status=%d level=%d x=%.17g r=%.17g aF=%.17g aW=%.17g MF=%.17g MW=%.17g\n",
        status,level,x,y,f_PFC[],a_water[],M_PFC[],M_water[]);failures++;
    } else {
      area+=records[k].area_m2;
      defectW+=fabs(records[k].water_geometry_volume_defect_m3);
      defectF+=fabs(records[k].PFC_geometry_volume_defect_m3);
    }
  }
  axis_statistics.area_m2=area;
  axis_statistics.geometry_water_volume_defect_m3=defectW;
  axis_statistics.geometry_PFC_volume_defect_m3=defectF;
  axis_statistics.geometry_failures+=failures;
  return failures?1:0;
}

static int closure_axisymmetric_state_guard(scalar pressure) {
  int failures=0;
  foreach(reduction(+:failures)) {
    if(M_PFC[]>0. && (!(f_PFC[]>0.) || !(p_cache[]>0.) || !(T_PFC[]>0.)))failures++;
    if(M_water[]>0. && (!(a_water[]>0.) || !(T_water[]>0.) || pressure[] < -1.e8))failures++;
    if(!(wood[]>0.) || !(rho_flow[]>0.) || !isfinite(pressure[]))failures++;
  }
  return failures?1:0;
}

static int closure_axisymmetric_relax_after_local_source(void) {
  if(closure_equilibrate_fields(1,p) || closure_axisymmetric_state_guard(p))return 1;
  double entropy=0.;foreach(reduction(+:entropy))
    entropy+=mechanical_entropy_step[]*closure_axisymmetric_physical_volume(point);
  axis_statistics.mechanical_entropy_J_K+=entropy;
  return 0;
}

static int closure_axisymmetric_phase(double interval,double area) {
  ClosureBridgeZone * zones=calloc(axis_leaf_count,sizeof(*zones));
  ClosureBridgeCache * caches=calloc(axis_leaf_count,sizeof(*caches));
  if(!zones || !caches){free(zones);free(caches);return 1;}
  int failures=0;double HKS=0.,bulk=0.,remainder=0.,clock_error=0.;
  unsigned long evaluations=0,warm=0,global=0,nodes=0;
  foreach(serial) {
    int k=(int)leaf_index[];zones[k]=closure_cell_zone(point);caches[k]=closure_cell_cache(point);
    if(M_PFC[]>0.) {
      double mass=M_PFC[]*closure_axisymmetric_physical_volume(point);
      if(!(mass>0. && isfinite(mass))) {
        fprintf(stderr,"AXI binary64 phase-mass conversion refusal x=%.17g r=%.17g\n",x,y);
        failures++;continue;
      }
      ClosureCoupledPhaseDiagnostics diagnostics;
      int status=closure_coupled_phase_step_cached(&zones[k],&caches[k],
        closure_coupled_phase_cache_at(axis_spinodal_caches,k),
        area/axis_inventory,axis_alpha,interval,&diagnostics);
      if(status){fprintf(stderr,"AXI phase failure status=%d native=%d x=%.17g r=%.17g dt=%.17g\n",
        status,diagnostics.native_status,x,y,interval);failures++;}
      else {
        HKS+=mass*diagnostics.entropy_HKS_J_kg_K;
        bulk+=mass*diagnostics.entropy_bulk_J_kg_K;
        remainder+=mass*diagnostics.entropy_primitive_remainder_J_kg_K;
        clock_error+=mass*fabs(diagnostics.path_time_s-interval);
        evaluations+=diagnostics.evaluations;warm+=diagnostics.spinodal_warm;
        global+=diagnostics.spinodal_global;nodes++;
      }
    }
  }
  if(!failures) {
    foreach(serial) {
      int k=(int)leaf_index[];Z_PFC[]=M_PFC[]*zones[k].xi;
      closure_store_cell_cache(point,caches[k]);
    }
    boundary({Z_PFC,rhoL_cache,rhoV_cache,p_cache,T_cache,validL_cache,validV_cache});
    axis_statistics.phase_entropy_HKS_J_K+=HKS;
    axis_statistics.phase_entropy_bulk_J_K+=bulk;
    axis_statistics.phase_entropy_primitive_remainder_J_K+=remainder;
    axis_statistics.phase_clock_error_mass_s+=clock_error;
    axis_statistics.phase_evaluations+=evaluations;
    axis_statistics.spinodal_warm+=warm;axis_statistics.spinodal_global+=global;
    axis_statistics.phase_nodes+=nodes;
  } else {
    /* Numerical guesses can be invalidated on global rollback. Physical
     * fractions/energies/composition/caches were not partially committed. */
    closure_coupled_phase_caches_free(axis_spinodal_caches);
    axis_spinodal_caches=closure_coupled_phase_caches_new(axis_leaf_count);
  }
  free(zones);free(caches);
  if(failures)return 2;
  if(closure_axisymmetric_relax_after_local_source())return 3;
  return 0;
}

static int closure_axisymmetric_heat(double interval,const ClosureAxisymmetricGeometry * geometry) {
  int nf=0,nw=0,np=0;
  foreach(serial){nf+=M_PFC[]>0.;nw+=M_water[]>0.;np+=geometry[(int)leaf_index[]].has_interface;}
  if(!np)return 0;
  int nodes=nf+nw;
  ClosureCoupledThermalNode * input=calloc(nodes,sizeof(*input));
  ClosureCoupledThermalOutput * output=calloc(nodes,sizeof(*output));
  ClosureCoupledThermalPatch * patches=calloc(np,sizeof(*patches));
  int * fi=malloc(axis_leaf_count*sizeof(int)),*wi=malloc(axis_leaf_count*sizeof(int));
  if(!input || !output || !patches || !fi || !wi) {
    free(input);free(output);free(patches);free(fi);free(wi);return 1;
  }
  int fidx=0,widx=nf,pidx=0,failures=0;
  foreach(serial) {
    int k=(int)leaf_index[];double volume=closure_axisymmetric_physical_volume(point);
    double rho=M_water[]+M_PFC[],kinetic=.5*(sq(q.x[])+sq(q.y[]))/(rho*rho);
    fi[k]=wi[k]=-1;
    if(M_PFC[]>0.) {
      fi[k]=fidx;input[fidx++]=(ClosureCoupledThermalNode){M_PFC[]*volume,
        f_PFC[]*volume,(E_PFC[]-M_PFC[]*kinetic)*volume,Z_PFC[]/M_PFC[],closure_cell_cache(point)};
    }
    if(M_water[]>0.) {
      wi[k]=widx;input[widx++]=(ClosureCoupledThermalNode){M_water[]*volume,
        a_water[]*volume,(E_water[]-M_water[]*kinetic)*volume,0.,closure_cell_cache(point)};
    }
    if((M_PFC[]>0. && !(input[fi[k]].mass_kg>0. && input[fi[k]].volume_m3>0.)) ||
       (M_water[]>0. && !(input[wi[k]].mass_kg>0. && input[wi[k]].volume_m3>0.)))failures++;
    if(geometry[k].has_interface) {
      if(wi[k]<0)failures++;
      else patches[pidx++]=(ClosureCoupledThermalPatch){geometry[k].area_m2,
        geometry[k].water_conductance_W_K,wi[k]};
    }
  }
  ClosureCoupledThermalParameters parameters={axis_inventory,axis_critical_temperature,.02,.06,.012,.036};
  ClosureCoupledThermalControls controls;closure_coupled_thermal_default_controls(interval,&controls);
  ClosureCoupledThermalStats diagnostics={0};
  int status=failures?2:closure_coupled_thermal_step(nodes,nf,input,np,patches,
    &parameters,interval,&controls,output,&diagnostics);
  if(!status) {
    foreach(serial) {
      int k=(int)leaf_index[];double volume=closure_axisymmetric_physical_volume(point);
      double rho=M_water[]+M_PFC[],kinetic=.5*(sq(q.x[])+sq(q.y[]))/(rho*rho);
      if(fi[k]>=0) {
        E_PFC[]=output[fi[k]].internal_energy_J/volume+M_PFC[]*kinetic;
        closure_store_cell_cache(point,output[fi[k]].cache);
      }
      if(wi[k]>=0)E_water[]=output[wi[k]].internal_energy_J/volume+M_water[]*kinetic;
    }
    boundary({E_PFC,E_water,rhoL_cache,rhoV_cache,p_cache,T_cache,validL_cache,validV_cache});
    axis_statistics.heat_entropy_J_K+=diagnostics.physical_entropy_integral_J_K;
    axis_statistics.heat_energy_defect_J+=diagnostics.energy_defect_J;
    axis_statistics.heat_evaluations+=diagnostics.evaluations;axis_statistics.patches+=np;
  } else fprintf(stderr,"AXI heat failure status=%d source=%d bridge=%d node=%d\n",status,
    diagnostics.integrator_status,diagnostics.first_probe_bridge_status,diagnostics.first_probe_failure_node);
  free(input);free(output);free(patches);free(fi);free(wi);
  if(status)return 2;
  return closure_axisymmetric_relax_after_local_source()?3:0;
}

static int closure_axisymmetric_pressure_capillary(double step) {
  closure_save_advected_targets();
  if(closure_equilibrate_fields(0,p_trial))return 1;
  scalar kappa[];curvature(f_PFC,kappa,axis_sigma);boundary({kappa});
  face vector capillary_force[],face_pressure[],pressure_energy_flux[];
  int capillary_failures=0;
  foreach_face(reduction(+:capillary_failures)) {
    capillary_force.x[]=0.;
    if(f_PFC[]!=f_PFC[-1] && fm.x[]>0. && y!=0.) {
      double potential=0.;
      if(kappa[]<nodata && kappa[-1]<nodata)potential=.5*(kappa[]+kappa[-1]);
      else if(kappa[]<nodata)potential=kappa[];
      else if(kappa[-1]<nodata)potential=kappa[-1];
      else {capillary_failures++;continue;}
      capillary_force.x[]=potential*(f_PFC[]-f_PFC[-1])/Delta;
    }
  }
  if(capillary_failures){fprintf(stderr,"AXI unresolved capillary faces=%d\n",capillary_failures);return 2;}
  boundary((scalar *){capillary_force});
  for(int iteration=0;iteration<80;iteration++) {
    boundary({p_trial});
    foreach_face() {
      double rl=MW_adv[-1]+MF_adv[-1],rr=MW_adv[]+MF_adv[];
      face_pressure.x[]=.5*(p_trial[-1]+p_trial[]);
      uf.x[]=fm.x[]*(.5*(q_adv.x[-1]/rl+q_adv.x[]/rr)+
        step*2./(rl+rr)*(capillary_force.x[]-(p_trial[]-p_trial[-1])/Delta));
      pressure_energy_flux.x[]=face_pressure.x[]*uf.x[];
    }
    boundary((scalar *){uf,face_pressure,pressure_energy_flux});
    double cap_work=0.,work_defect=0.;
    foreach(reduction(+:cap_work) reduction(+:work_defect)) {
      f_PFC[]=f_adv[];a_water[]=aw_adv[];M_PFC[]=MF_adv[];M_water[]=MW_adv[];Z_PFC[]=ZF_adv[];
      double rho=MW_adv[]+MF_adv[],de=0.,Wp=0.,Ws=0.,divergence=0.;
      foreach_dimension() {
        double Fp=-(face_pressure.x[1]-face_pressure.x[])/Delta;
        double Fs=.5*(capillary_force.x[1]+capillary_force.x[]);
        q.x[]=q_adv.x[]+step*(Fp+Fs);
        double midpoint=(q.x[]+q_adv.x[])/(2.*rho);
        Wp+=step*midpoint*Fp;Ws+=step*midpoint*Fs;
        de-=step*(pressure_energy_flux.x[1]-pressure_energy_flux.x[])/(cm[]*Delta);
        divergence+=(uf.x[1]-uf.x[])/(cm[]*Delta);
      }
      double yw=MW_adv[]/rho,yf=MF_adv[]/rho;
      E_water[]=EW_adv[]+aw_adv[]*de+(yw-aw_adv[])*Wp+yw*Ws;
      E_PFC[]=EF_adv[]+f_adv[]*de+(yf-f_adv[])*Wp+yf*Ws;
      double volume=closure_axisymmetric_physical_volume(point);
      cap_work+=Ws*volume;work_defect+=fabs(de-Wp+step*p_trial[]*divergence)*volume;
    }
    boundary({f_PFC,a_water,M_PFC,M_water,Z_PFC,E_PFC,E_water,q});
    if(closure_equilibrate_fields(1,p_EOS) || closure_axisymmetric_state_guard(p_EOS))return 3;
    double residual=0.,entropy=0.;
    foreach(reduction(max:residual) reduction(+:entropy)) {
      residual=fmax(residual,fabs(p_EOS[]-p_trial[])/fmax(1.e5,fmax(fabs(p_EOS[]),fabs(p_trial[]))));
      entropy+=mechanical_entropy_step[]*closure_axisymmetric_physical_volume(point);
    }
    geometric_statistics.pressure_iterations++;geometric_statistics.final_pressure_residual=residual;
    if(residual<1.e-8) {
      foreach()p[]=p_EOS[];
      boundary({p});axis_statistics.capillary_work_J+=cap_work;
      geometric_statistics.work_defect+=work_defect;
      geometric_statistics.mechanical_entropy+=entropy;return 0;
    }
    foreach()p_trial[]=p_EOS[];
  }
  fprintf(stderr,"AXI pressure iteration failed residual=%.17g\n",geometric_statistics.final_pressure_residual);
  return 4;
}
#endif
