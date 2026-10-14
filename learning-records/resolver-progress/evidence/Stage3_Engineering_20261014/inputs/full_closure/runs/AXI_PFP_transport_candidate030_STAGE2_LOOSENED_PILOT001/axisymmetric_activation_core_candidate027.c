#include "grid/quadtree.h"
#include "axi.h"
#include "axisymmetric_coupled_core_candidate019.h"
#include "axisymmetric_transaction.h"
#include "axisymmetric_snapshot_properties.h"
#include "axisymmetric_transport_collector_candidate020.h"
#include <time.h>
/* All shared AND auxiliary momentum boundary conditions are explicit.
 * z=0 receiving wall: no-slip; r=0 axis: odd radial/even axial velocity.
 * Distant faces are closed slip solely for this short assembly diagnostic.
 * Full nonreflecting/radiative boundaries and their ledgers remain pending. */
q.x[left]=dirichlet(0);
q.y[left]=dirichlet(0);
q_PFC.x[left]=dirichlet(0);
q_PFC.y[left]=dirichlet(0);
q_water.x[left]=dirichlet(0);
q_water.y[left]=dirichlet(0);
q_adv.x[left]=dirichlet(0);
q_adv.y[left]=dirichlet(0);
q.x[right]=dirichlet(0);
q.y[right]=neumann(0);
q_PFC.x[right]=dirichlet(0);
q_PFC.y[right]=neumann(0);
q_water.x[right]=dirichlet(0);
q_water.y[right]=neumann(0);
q_adv.x[right]=dirichlet(0);
q_adv.y[right]=neumann(0);
q.y[bottom]=dirichlet(0);
q.x[bottom]=neumann(0);
q_PFC.y[bottom]=dirichlet(0);
q_PFC.x[bottom]=neumann(0);
q_water.y[bottom]=dirichlet(0);
q_water.x[bottom]=neumann(0);
q_adv.y[bottom]=dirichlet(0);
q_adv.x[bottom]=neumann(0);
q.y[top]=dirichlet(0);
q.x[top]=neumann(0);
q_PFC.y[top]=dirichlet(0);
q_PFC.x[top]=neumann(0);
q_water.y[top]=dirichlet(0);
q_water.x[top]=neumann(0);
q_adv.y[top]=dirichlet(0);
q_adv.x[top]=neumann(0);
uf.x[left]=dirichlet(0);
uf.x[right]=dirichlet(0);
uf.y[bottom]=dirichlet(0);
uf.y[top]=dirichlet(0);

static void core_history(FILE * stream,const ClosureAxisSnapshotCell * properties,
    const char * stage,double time,int steps) {
  double mw,mf,E,S,minimum,error,uncovered;
  closure_flow_integrals(&mw,&mf,&E,&S,&minimum,&error,&uncovered);
  S=0.;foreach(serial) {
    const ClosureAxisSnapshotCell * s=properties+(int)leaf_index[];
    S+=(M_water[]*s->water.s+M_PFC[]*s->pfc.s)*dv();
  }
  fprintf(stream,"%s,%.17g,%d,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%lu,%lu,%lu,%lu,%.17g,%.21Lg,%.21Lg,%.21Lg,%.21Lg,%.21Lg,%.21Lg,%.21Lg,%.21Lg,%lu,%lu,%lu\n",
    stage,time,steps,2.*pi*mw,2.*pi*mf,2.*pi*E,2.*pi*S,axis_statistics.area_m2,
    minimum,error,2.*pi*uncovered,geometric_statistics.final_pressure_residual,
    axis_statistics.phase_entropy_HKS_J_K,axis_statistics.phase_entropy_bulk_J_K,
    axis_statistics.heat_entropy_J_K,axis_statistics.capillary_work_J,
    axis_statistics.heat_energy_defect_J,axis_statistics.geometry_water_volume_defect_m3,
    geometric_statistics.work_defect,axis_statistics.phase_evaluations,
    axis_statistics.spinodal_warm,axis_statistics.spinodal_global,axis_statistics.heat_evaluations,
    axis_statistics.mechanical_entropy_J_K+geometric_statistics.mechanical_entropy,
    axis_statistics.water_Fourier_entropy_J_K,axis_statistics.viscous_entropy_J_K,
    axis_statistics.water_Fourier_boundary_energy_out_J,axis_statistics.viscous_boundary_energy_out_J,
    axis_statistics.water_Fourier_energy_defect_J,axis_statistics.viscous_intrinsic_work_defect_J,
    axis_statistics.converted_transport_energy_roundoff_J,axis_statistics.converted_transport_momentum_roundoff_kg_m_s,
    axis_statistics.water_Fourier_faces,axis_statistics.viscous_faces,axis_statistics.water_Fourier_iterations);
  fflush(stream);
  fprintf(stderr,"CORE STAGE PROFILE: stage=%s time=%.17g steps=%d cpu_process_seconds=%.9g raw_queries=%lu inverse_iterations=%lu inverse_fallbacks=%lu global_phase_queries=%lu phase_evaluations=%lu heat_evaluations=%lu\n",
    stage,time,steps,(double)clock()/CLOCKS_PER_SEC,geometric_statistics.raw_queries,
    geometric_statistics.inverse_iterations,geometric_statistics.inverse_fallbacks,
    geometric_statistics.global_phase_queries,axis_statistics.phase_evaluations,
    axis_statistics.heat_evaluations);
  fprintf(stderr,"CORE READONLY PROFILE: W_calls=%lu F_calls=%lu W_only=%lu F_only=%lu mixed=%lu W_CPU_s=%.9g F_CPU_s=%.9g\n",
    axis_snapshot_water_calls,axis_snapshot_PFC_calls,axis_snapshot_W_only,axis_snapshot_F_only,
    axis_snapshot_mixed,axis_snapshot_water_cpu,axis_snapshot_PFC_cpu);
}

/* Selected conditional TS transport integration for candidate011. Each call
 * is a physical source half-step; the surrounding whole-macrostep transaction
 * restores both fields and axis_statistics if any later operation refuses. */
static int core_transport_candidate011(ClosureAxisSnapshotCell * properties,
    double interval,double length,int finest,int viscosity) {
  ClosureAxisTransportCommitStats report;
  int status=closure_axis_transport_source(interval,length,finest,viscosity,properties,&report);
  if(status)return status;
  if(viscosity) {
    axis_statistics.viscous_entropy_J_K+=report.physical.viscous_entropy_J_K;
    axis_statistics.viscous_boundary_energy_out_J+=report.physical.viscous_energy_boundary_out_J;
    axis_statistics.viscous_intrinsic_work_defect_J+=report.physical.viscous_intrinsic_work_defect_J;
    axis_statistics.converted_transport_energy_roundoff_J+=report.converted_energy_roundoff_J;
    axis_statistics.converted_transport_momentum_roundoff_kg_m_s+=report.converted_momentum_roundoff_kg_m_s;
    axis_statistics.viscous_faces+=report.physical.face_count;
  } else {
    axis_statistics.water_Fourier_entropy_J_K+=report.physical.Fourier_entropy_J_K;
    axis_statistics.water_Fourier_boundary_energy_out_J+=report.physical.Fourier_energy_boundary_out_J;
    axis_statistics.water_Fourier_energy_defect_J+=report.physical.Fourier_linear_solve_energy_defect_J;
    axis_statistics.water_Fourier_faces+=report.physical.water_edge_count;
    axis_statistics.water_Fourier_iterations+=report.physical.Fourier_iterations;
    axis_statistics.converted_transport_energy_roundoff_J+=report.converted_energy_roundoff_J;
    axis_statistics.converted_transport_momentum_roundoff_kg_m_s+=report.converted_momentum_roundoff_kg_m_s;
  }
  return 0;
}

/* Temporary density+extensive physical snapshots. The canonical independent
 * writer/flux ledger is root-owned; this assembly format is not its acceptance
 * evidence. The physical volume column explicitly contains the2pi metric. */
static void core_fields(FILE * stream,const ClosureAxisymmetricGeometry * geometry,
    const ClosureAxisSnapshotCell * properties,const char * stage,double time,int steps) {
  scalar * transaction_fields=closure_axisymmetric_transaction_fields();
  foreach(serial) {
    int leaf=(int)leaf_index[];const ClosureAxisymmetricGeometry * g=geometry+leaf;
    const ClosureAxisSnapshotCell * s=properties+leaf;
    double V=closure_axisymmetric_physical_volume(point),rho=M_water[]+M_PFC[];
    double K=.5*(sq(q.x[])+sq(q.y[]))/(rho*rho);
    fprintf(stream,"%s,%.17g,%d,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g",
      stage,time,level,x,y,Delta,V,f_PFC[],a_water[],M_PFC[],M_water[],E_PFC[],E_water[],
      q.x[]/rho,q.y[]/rho,M_PFC[]*V,M_water[]*V,E_PFC[]*V,E_water[]*V,
      M_PFC[]>0.?Z_PFC[]/M_PFC[]:0.,p[],s->water.T,s->pfc.T,s->water.s,s->pfc.s,
      M_water[]>0.?E_water[]/M_water[]-K:0.,M_PFC[]>0.?E_PFC[]/M_PFC[]-K:0.,s->pfc.p);
    fprintf(stream,",%d,%d,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%d,%d,%.17g,%d,%d",
      steps,leaf,g->area_m2,g->PFC_raw_volume_m3,g->water_raw_volume_m3,
      g->PFC_geometry_volume_m3,g->water_geometry_volume_m3,g->distance_water_m,
      g->water_conductance_W_K,g->water_geometry_volume_defect_m3,
      g->PFC_geometry_volume_defect_m3,g->has_interface,g->rounded_primary_complement,
      s->water.p,s->water_status,s->PFC_status);
    for(scalar field in transaction_fields)fprintf(stream,",%.17g",field[]);
    fputc('\n',stream);
  }
  free(transaction_fields);fflush(stream);
}

static int core_snapshot(FILE * history,FILE * fields,const ClosureAxisymmetricGeometry * geometry,
    ClosureAxisSnapshotCell * properties,const char * stage,double time,int steps) {
  int status=closure_axis_snapshot_properties(properties);
  const char * label=status?"invalid_caloric_snapshot":stage;
  if(status)fprintf(stderr,"CORE SNAPSHOT REFUSED: requested_stage=%s time=%.17g steps=%d\n",stage,time,steps);
  core_history(history,properties,label,time,steps);core_fields(fields,geometry,properties,label,time,steps);
  return status;
}

int main(int argc,char ** argv) {
  clock_t cpu_started=clock();
  if(argc!=16 && argc!=17)return 1;
  int diagnostic_refusal=argc==17?atoi(argv[16]):0;
  if(diagnostic_refusal<0 || diagnostic_refusal>6)return 1;
  const char * species=argv[1];double Ta=atof(argv[3]),mass=atof(argv[4]),radius=atof(argv[5]);
  double length=atof(argv[6]),stand=atof(argv[7]),fine_radius=atof(argv[10]);
  int base=atoi(argv[8]),fine=atoi(argv[9]),with_heat=atoi(argv[15]);
  double end_time=atof(argv[12]),maximum_step=atof(argv[13]),courant=atof(argv[14]);
  axis_alpha=atof(argv[11]);axis_inventory=mass;
  axis_critical_temperature=!strcmp(species,"PFP")?421.0000013150284:448.000000604543;
  if(!(mass>0. && radius>0. && length>0. && stand>radius && stand+radius<length) ||
     !(fine_radius>radius && base>=3 && fine>=base && fine<=12) ||
     !(end_time>0. && maximum_step>0. && courant>0. && courant<=.3) ||
     !(axis_alpha>=0. && axis_alpha<=1.) || (with_heat!=0 && with_heat!=1) ||
     closure_bridge_setup(species,argv[2]) || closure_coupled_phase_setup(species))return 2;
  size(length);origin(0.,0.,0.);init_grid(1<<base);
  event("metric");
  refine(level<fine && fabs(x-stand)<fine_radius+Delta && y<fine_radius+Delta);
  event("metric");
  axis_leaf_count=0;foreach(serial)leaf_index[]=axis_leaf_count++;
  axis_spinodal_caches=closure_coupled_phase_caches_new(axis_leaf_count);
  ClosureAxisymmetricGeometry * geometry=calloc(axis_leaf_count,sizeof(*geometry));
  ClosureAxisSnapshotCell * properties=calloc(axis_leaf_count,sizeof(*properties));
  ClosureAxisymmetricTransaction transaction;
  if(!axis_spinodal_caches || !geometry || !properties || closure_axisymmetric_transaction_prepare(&transaction))return 3;
  f_PFC.closure_tracers=list_copy({M_PFC,M_water,E_PFC,E_water,Z_PFC,q_PFC,q_water});
  for(scalar field in {M_water,E_water,q_water})field.closure_inverse=true;
  for(scalar field in {M_water,M_PFC,Z_PFC})field.closure_positive=true;
  Z_PFC.closure_bounded=true;Z_PFC.closure_upper=M_PFC;
  for(scalar field in f_PFC.closure_tracers)field.gradient=minmod2;
  for(scalar field in {M_water,M_PFC,E_water,E_PFC,Z_PFC,q,q_adv,q_PFC,q_water})
    field.restriction=restriction_volume_average;
  ClosureBridgeMaterial water,pfc;ClosureBridgeCache initial={0};
  if(closure_bridge_water_initial(&water) || closure_bridge_pfc_PT(101325.,Ta,0.,&initial,&pfc))return 4;
  double low=.8*radius,high=1.2*radius,chosen=radius,mass_error=HUGE;
  for(int iteration=0;iteration<80;iteration++) {
    chosen=.5*(low+high);fraction(f_PFC,sq(chosen)-sq(x-stand)-sq(y));
    double reconstructed=0.;foreach(reduction(+:reconstructed))
      reconstructed+=f_PFC[]*pfc.rho*closure_axisymmetric_physical_volume(point);
    mass_error=(reconstructed-mass)/mass;
    if(fabs(mass_error)<1.e-10)break;
    if(mass_error>0.)high=chosen;else low=chosen;
  }
  if(!(fabs(mass_error)<1.e-6))return 5;
  foreach() {
    a_water[]=1.-f_PFC[];M_water[]=a_water[]*water.rho;M_PFC[]=f_PFC[]*pfc.rho;
    E_water[]=M_water[]*water.e;E_PFC[]=M_PFC[]*pfc.e;Z_PFC[]=0.;
q.x[]=q.y[]=0.;
    closure_store_cell_cache(point,initial);
  }
  boundary({f_PFC,a_water,M_water,M_PFC,E_water,E_PFC,Z_PFC,q,
    rhoL_cache,rhoV_cache,p_cache,T_cache,validL_cache,validV_cache});
  if(closure_equilibrate_fields(1,p) || closure_axisymmetric_state_guard(p) ||
     closure_axisymmetric_geometry(geometry))return 6;
  closure_save_advected_targets();
  foreach() {
    p_trial[]=p[];p_EOS[]=p[];
    foreach_dimension(){q_PFC.x[]=0.;q_water.x[]=0.;}
  }
  boundary({p_trial,p_EOS,q_PFC,q_water});
  closure_advective_face_velocity();
  FILE * history=fopen("history.csv","w"),* fields=fopen("fields.csv","w");
  if(!history || !fields)return 7;
  fprintf(stderr,"CANDIDATE011 COMPONENT ONLY: selected viscous/Fourier half-steps enabled; full production admission absent; physicalV=2pi*dv; leaves=%lu initial_radius=%.17g activated_nominal_radius=%.17g mass_relative_error=%.17g\n",
    axis_leaf_count,chosen,radius,mass_error);
  fprintf(history,"stage,time_s,steps,water_mass_kg,PFC_mass_kg,bulk_energy_J,entropy_J_K,area_m2,min_fraction,fraction_sum_error,uncovered_mass_kg,pressure_residual,phase_HKS_entropy_J_K,phase_bulk_entropy_J_K,interface_heat_entropy_J_K,capillary_work_J,interface_heat_energy_defect_J,water_geometry_volume_defect_m3,pressure_work_defect_J,phase_evaluations,spinodal_warm,spinodal_global,heat_evaluations,mechanical_entropy_J_K,water_Fourier_entropy_J_K,viscous_entropy_J_K,water_Fourier_boundary_energy_out_J,viscous_boundary_energy_out_J,water_Fourier_energy_defect_J,viscous_intrinsic_work_defect_J,converted_transport_energy_roundoff_J,converted_transport_momentum_roundoff_kg_m_s,water_Fourier_edges,viscous_faces,water_Fourier_iterations\n");
  fprintf(fields,"stage,time_s,level,z_m,r_m,Delta_m,volume_m3,a_F,a_W,M_F_kg_m3,M_W_kg_m3,E_F_J_m3,E_W_J_m3,u_z_m_s,u_r_m_s,m_F_kg,m_W_kg,E_F_J,E_W_J,xi,p_Pa,T_W_K,T_F_K,s_W_J_kg_K,s_F_J_kg_K,e_W_J_kg,e_F_J_kg,p_F_Pa,steps,leaf_id,area_m2,PFC_raw_volume_m3,water_raw_volume_m3,PFC_geometry_volume_m3,water_geometry_volume_m3,distance_water_m,water_conductance_W_K,water_geometry_volume_defect_m3,PFC_geometry_volume_defect_m3,has_interface,rounded_primary_complement,p_W_actual_Pa,water_caloric_status,PFC_caloric_status");
  for(int field=0;field<transaction.fields;field++)fprintf(fields,",rollback_field_%d",field);
  fputc('\n',fields);
  if(core_snapshot(history,fields,geometry,properties,"initial",0.,0))return 17;
  double time=0.,macrostep_start_time=0.;int iteration=0,status=0,macrostep_start_iteration=0;
  while(time<end_time) {
    macrostep_start_time=time;macrostep_start_iteration=iteration;
    if(closure_axisymmetric_transaction_capture(&transaction,geometry)){status=18;break;}
    double step=fmin(end_time-time,fmin(maximum_step,closure_acoustic_timestep(courant)));
    if(!(step>0. && isfinite(step))){status=8;break;}
    if(closure_axisymmetric_phase(.5*step,axis_statistics.area_m2) ||
       closure_axisymmetric_geometry(geometry)){status=9;break;}
    if(core_snapshot(history,fields,geometry,properties,"phase_first",time,iteration)){status=17;break;}
    if(diagnostic_refusal==1){status=91;break;}
    if(with_heat && (closure_axisymmetric_heat(.5*step,geometry) ||
       closure_axisymmetric_geometry(geometry))){status=10;break;}
    if(core_snapshot(history,fields,geometry,properties,"thermal_first",time,iteration)){status=17;break;}
    if(diagnostic_refusal==2){status=92;break;}
    if(core_transport_candidate011(properties,.5*step,length,fine,0) ||
       closure_axisymmetric_geometry(geometry)){status=20;break;}
    if(core_snapshot(history,fields,geometry,properties,"water_Fourier_first",time,iteration)){status=17;break;}
    {
      int transport_status=core_transport_candidate011(properties,.5*step,length,fine,1);
      int geometry_status=transport_status?0:closure_axisymmetric_geometry(geometry);
      if(transport_status || geometry_status){
        fprintf(stderr,"AXI status=21 detail transport=%d geometry=%d\n",transport_status,geometry_status);
        status=21;break;
      }
    }
    if(core_snapshot(history,fields,geometry,properties,"viscous_first",time,iteration)){status=17;break;}
    fprintf(stderr,"DIAG before face_velocity t=%.17g steps=%d\n",time,iteration);fflush(stderr);
    closure_advective_face_velocity();
    fprintf(stderr,"DIAG after face_velocity before advect\n");fflush(stderr);
    if(closure_advect_conserved(step,iteration)){status=11;break;}
    fprintf(stderr,"DIAG after advect before geometry\n");fflush(stderr);
    if(closure_axisymmetric_geometry(geometry)){status=16;break;}
    fprintf(stderr,"DIAG after geometry before advected snapshot\n");fflush(stderr);
    if(core_snapshot(history,fields,geometry,properties,"advected",time,iteration)){status=17;break;}
    if(diagnostic_refusal==3){status=93;break;}
    if(closure_axisymmetric_pressure_capillary(step) ||
       closure_axisymmetric_geometry(geometry)){status=12;break;}
    if(core_snapshot(history,fields,geometry,properties,"pressure_capillary",time+step,iteration)){status=17;break;}
    if(diagnostic_refusal==4){status=94;break;}
    if(core_transport_candidate011(properties,.5*step,length,fine,1) ||
       closure_axisymmetric_geometry(geometry)){status=22;break;}
    if(core_snapshot(history,fields,geometry,properties,"viscous_last",time+step,iteration)){status=17;break;}
    if(core_transport_candidate011(properties,.5*step,length,fine,0) ||
       closure_axisymmetric_geometry(geometry)){status=23;break;}
    if(core_snapshot(history,fields,geometry,properties,"water_Fourier_last",time+step,iteration)){status=17;break;}
    if(with_heat && (closure_axisymmetric_heat(.5*step,geometry) ||
       closure_axisymmetric_geometry(geometry))){status=13;break;}
    if(core_snapshot(history,fields,geometry,properties,"thermal_last",time+step,iteration)){status=17;break;}
    if(diagnostic_refusal==5){status=95;break;}
    if(closure_axisymmetric_phase(.5*step,axis_statistics.area_m2) ||
       closure_axisymmetric_geometry(geometry)){status=14;break;}
    if(diagnostic_refusal==6){status=96;break;}
    time+=step;iteration++;if(core_snapshot(history,fields,geometry,properties,"accepted",time,iteration)){status=17;break;}
    if(iteration>100000){status=15;break;}
  }
  if(status && transaction.valid) {
    core_snapshot(history,fields,geometry,properties,"rejected_trial",time,iteration);
    fprintf(stderr,"CORE REJECTED TRIAL: status=%d raw_queries=%lu phase_evaluations=%lu heat_evaluations=%lu before_macrostep_restore\n",
      status,geometric_statistics.raw_queries,axis_statistics.phase_evaluations,axis_statistics.heat_evaluations);
    int restored=closure_axisymmetric_transaction_restore(&transaction,geometry);
    if(!restored)restored=closure_axisymmetric_transaction_matches(&transaction,geometry);
    fprintf(stderr,"CORE MACROSTEP RESTORE: status=%d exact_all_scalar_geometry_statistics=%d fields=%d leaves=%lu\n",
      restored,restored==0,transaction.fields,transaction.leaf_count);
    if(restored){fprintf(stderr,"AXI global restore failed status=%d\n",restored);status=19;}
    else {time=macrostep_start_time;iteration=macrostep_start_iteration;}
    core_snapshot(history,fields,geometry,properties,"failed_rolled_back",time,iteration);
  } else core_snapshot(history,fields,geometry,properties,status?"failed":"final",time,iteration);
  fprintf(stderr,"CORE PROFILE: cpu_seconds=%.9g raw_queries=%lu inverse_iterations=%lu inverse_fallbacks=%lu global_phase_queries=%lu phase_evaluations=%lu heat_evaluations=%lu physical_domain_status=%d\n",
    (double)(clock()-cpu_started)/CLOCKS_PER_SEC,geometric_statistics.raw_queries,
    geometric_statistics.inverse_iterations,geometric_statistics.inverse_fallbacks,
    geometric_statistics.global_phase_queries,axis_statistics.phase_evaluations,
    axis_statistics.heat_evaluations,status);
  fclose(history);fclose(fields);free(geometry);free(properties);closure_axisymmetric_transaction_free(&transaction);
  closure_coupled_phase_caches_free(axis_spinodal_caches);
  free(f_PFC.closure_tracers);f_PFC.closure_tracers=NULL;closure_bridge_cleanup();return status;
}
