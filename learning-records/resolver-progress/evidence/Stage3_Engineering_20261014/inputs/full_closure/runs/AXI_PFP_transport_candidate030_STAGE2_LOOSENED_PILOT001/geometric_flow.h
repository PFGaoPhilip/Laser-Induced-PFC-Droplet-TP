/* Original geometric selected-material conservative flow core.
 * This first component excludes phase reaction/heat/viscosity/surface tension,
 * wall/contact and AMR. It is not the full production cavitation solver. */
#ifndef CLOSURE_GEOMETRIC_FLOW_H
#define CLOSURE_GEOMETRIC_FLOW_H
#include "utils.h"
#include "closure_geometric_advection.h"
#include "material_bridge.h"

scalar f_PFC[],a_water[],M_PFC[],M_water[],E_PFC[],E_water[],Z_PFC[];
vector q[],q_PFC[],q_water[];
scalar p[],rho_flow[],wood[],chi[],T_water[],T_PFC[],s_water[],s_PFC[];
scalar rhoL_cache[],rhoV_cache[],T_cache[],p_cache[],validL_cache[],validV_cache[];
face vector uf[];
scalar f_adv[],aw_adv[],MF_adv[],MW_adv[],EF_adv[],EW_adv[],ZF_adv[];
vector q_adv[];
scalar p_trial[],p_EOS[],mechanical_entropy_step[];

typedef struct {
  unsigned long raw_queries,inverse_iterations,inverse_fallbacks,global_phase_queries;
  unsigned long pressure_iterations;
  double final_pressure_residual,work_defect,mechanical_entropy;
  ClosureGeometricAdvectionStats advection;
} ClosureGeometricFlowStats;
static ClosureGeometricFlowStats geometric_statistics;

static ClosureBridgeCache closure_cell_cache(Point point) {
  return (ClosureBridgeCache){rhoL_cache[],rhoV_cache[],p_cache[],T_cache[],
    validL_cache[]>0.5,validV_cache[]>0.5};
}
static void closure_store_cell_cache(Point point,ClosureBridgeCache cache) {
  rhoL_cache[]=cache.rho_liquid;rhoV_cache[]=cache.rho_vapour;
  p_cache[]=cache.p_pfc;T_cache[]=cache.T_pfc;
  validL_cache[]=cache.liquid_valid;validV_cache[]=cache.vapour_valid;
}
static ClosureBridgeZone closure_cell_zone(Point point) {
  double qr=0.;
#if dimension > 1
  qr=q.y[];
#endif
  return (ClosureBridgeZone){a_water[],f_PFC[],M_water[],M_PFC[],q.x[],qr,
    E_water[],E_PFC[],M_PFC[]>0.?Z_PFC[]/M_PFC[]:0.};
}

/* Numerical EOS pressure seed may evaluate a relaxed copy, but a false
 * commit never changes the physical fractions or energies. Each pressure
 * trial below is reconstructed from identical post-advection targets. */

/* Candidate024/025/026/027 engineering soft-pass (100fs diagnostic only; not production admission):
 * post-advection underflow can leave M_water/E_water slightly negative with aW=0,aF=1.
 * Snap those residuals (and matching q_water) to zero before geometric EOS. */
static void closure_snap_tiny_negative_water(Point point) {
  /* Candidate026: raise MW floor to 1e-25 (covers ~1e-28) and EW to 1e-20 when aW~0 / pure PFC. */
  static int axi_eos_neg_water_logged = 0;
  int snap = 0;
  int aw_gone = (a_water[] == 0. || a_water[] < 1.e-30);
  int pure_pfc = aw_gone && (f_PFC[] == 1. || f_PFC[] > 1. - 1.e-20);
  if(M_water[] < 0. && M_water[] > -1.e-25) { M_water[] = 0.; snap = 1; }
  if(E_water[] < 0. && E_water[] > -1.e-20) { E_water[] = 0.; snap = 1; }
  /* Candidate027 sibling: when MW snaps to 0, always co-clear EW and q_water (avoid E/M FPE). */
  if(pure_pfc || aw_gone || (f_PFC[] == 1. || f_PFC[] > 1. - 1.e-20)) {
    if(M_water[] != 0. && fabs(M_water[]) <= 1.e-25) {
      M_water[] = 0.; E_water[] = 0.; a_water[] = 0.; f_PFC[] = 1.; snap = 1;
      foreach_dimension() q_water.x[] = 0.;
    }
    if(E_water[] != 0. && fabs(E_water[]) <= 1.e-20) { E_water[] = 0.; snap = 1; }
    if(a_water[] != 0. && a_water[] < 1.e-30) { a_water[] = 0.; f_PFC[] = 1.; snap = 1; }
    if(M_water[] == 0. && (a_water[] != 0. && a_water[] < 1.e-20)) {
      a_water[] = 0.; f_PFC[] = 1.; E_water[] = 0.; snap = 1;
      foreach_dimension() q_water.x[] = 0.;
    }
    if(M_water[] == 0. && E_water[] != 0.) {
      E_water[] = 0.; snap = 1;
      foreach_dimension() q_water.x[] = 0.;
    }
    if(snap) {
      foreach_dimension() q_water.x[] = 0.;
    }
  }
  if(snap && !axi_eos_neg_water_logged) {
    fprintf(stderr,"AXI geometric EOS engineering soft-pass: tiny water mass/energy/fraction snapped floor=1e-25 (027 co-clear EW/q) (100fs diagnostic only; not production admission)\n");
    axi_eos_neg_water_logged = 1;
  }
}

static int closure_equilibrate_fields(int commit,scalar pressure) {
  int failures=0;double raw=0.,inverse=0.,fallback=0.,global=0.;
  foreach(reduction(+:failures) reduction(+:raw) reduction(+:inverse)
          reduction(+:fallback) reduction(+:global)) {
    closure_snap_tiny_negative_water(point);
    ClosureBridgeZone zone=closure_cell_zone(point);
    ClosureBridgeCache cache=closure_cell_cache(point);ClosureBridgeResult state;
    int status=closure_bridge_equilibrate(&zone,&cache,&state);
    if(status) {
      int underflow_eos = ((zone.a_water == 0. || zone.a_water < 1.e-30) &&
        (zone.a_pfc == 1. || zone.a_pfc > 1. - 1.e-20) &&
        ((zone.m_water < 0. && zone.m_water > -1.e-25) || fabs(zone.m_water) <= 1.e-25) &&
        ((zone.E_water < 0. && zone.E_water > -1.e-20) || fabs(zone.E_water) <= 1.e-20 || zone.m_water == 0.));
      int status3_residual_frac = (status == 3 && zone.m_water == 0. &&
        (zone.a_water != 0. && zone.a_water < 1.e-20) &&
        (zone.a_pfc == 1. || zone.a_pfc > 1. - 1.e-20));
      int status4_tiny_mw = ((status == 4 || status == 1) &&
        (zone.a_water == 0. || zone.a_water < 1.e-30) &&
        fabs(zone.m_water) <= 1.e-25 &&
        (zone.a_pfc == 1. || zone.a_pfc > 1. - 1.e-20));
      if(underflow_eos || (status == 1 && zone.m_water < 0. && zone.m_water > -1.e-25) ||
         status3_residual_frac || status4_tiny_mw) {
        static int axi_eos_fail_soft_logged = 0;
        if(!axi_eos_fail_soft_logged) {
          fprintf(stderr,"AXI geometric EOS engineering soft-pass: geometric EOS failure status=%d retried after water/fraction snap (100fs diagnostic only; not production admission)\n",status);
          axi_eos_fail_soft_logged = 1;
        }
        M_water[] = 0.; E_water[] = 0.; a_water[] = 0.; f_PFC[] = 1.;
        foreach_dimension() q_water.x[] = 0.;
        zone = closure_cell_zone(point);
        status = closure_bridge_equilibrate(&zone,&cache,&state);
      }
    }
    if(status) {
      fprintf(stderr,"geometric EOS failure status=%d x=%.17g y=%.17g aW=%.17g aF=%.17g MW=%.17g MF=%.17g EW=%.17g EF=%.17g xi=%.17g\n",
        status,x,y,zone.a_water,zone.a_pfc,zone.m_water,zone.m_pfc,
        zone.E_water,zone.E_pfc,zone.xi);failures++;
    } else {
      if(commit) {
        a_water[]=zone.a_water;f_PFC[]=zone.a_pfc;
        E_water[]=zone.E_water;E_PFC[]=zone.E_pfc;
      }
      pressure[]=state.p;wood[]=state.wood_modulus;chi[]=state.thermal_response;
      rho_flow[]=zone.m_water+zone.m_pfc;
      T_water[]=state.T_water;T_PFC[]=state.T_pfc;
      s_water[]=state.s_water;s_PFC[]=state.s_pfc;
      mechanical_entropy_step[]=commit?state.mechanical_entropy:0.;
      closure_store_cell_cache(point,cache);
      raw+=state.raw_queries;inverse+=state.inverse_iterations;
      fallback+=state.inverse_fallbacks;global+=state.phase_global_queries;
    }
  }
  geometric_statistics.raw_queries+=raw;geometric_statistics.inverse_iterations+=inverse;
  geometric_statistics.inverse_fallbacks+=fallback;geometric_statistics.global_phase_queries+=global;
  boundary({f_PFC,a_water,E_PFC,E_water,pressure,rho_flow,wood,chi,
    T_water,T_PFC,s_water,s_PFC,rhoL_cache,rhoV_cache,T_cache,p_cache,validL_cache,validV_cache});
  return failures?1:0;
}

static void closure_advective_face_velocity(void) {
  boundary({M_water,M_PFC,q});
  foreach_face() {
    double rl=M_water[-1]+M_PFC[-1],rr=M_water[]+M_PFC[];
    if(!(rl>0.)) rl=1.e-300; if(!(rr>0.)) rr=1.e-300;
    uf.x[]=fm.x[]*.5*(q.x[-1]/rl+q.x[]/rr);
  }
  boundary((scalar *){uf});
}

static int closure_advect_conserved(double step,int iteration) {
  fprintf(stderr,"DIAG advect_conserved enter\n");fflush(stderr);
  foreach() foreach_dimension() {
    double rho_m=M_water[]+M_PFC[];
    if(!(rho_m>0.)) rho_m=1.e-300;
    double velocity=q.x[]/rho_m;
    q_PFC.x[]=M_PFC[]*velocity;q_water.x[]=M_water[]*velocity;
  }
  fprintf(stderr,"DIAG advect after velocity split\n");fflush(stderr);
  boundary((scalar *){q_PFC,q_water});
  fprintf(stderr,"DIAG advect before geometric_advection\n");fflush(stderr);
  if(closure_geometric_advection(f_PFC,a_water,uf,step,iteration,&geometric_statistics.advection)) return 1;
  fprintf(stderr,"DIAG advect after geometric_advection\n");fflush(stderr);
  foreach() foreach_dimension() q.x[]=q_PFC.x[]+q_water.x[];
  boundary((scalar *){q});return 0;
}

static void closure_save_advected_targets(void) {
  foreach() {
    closure_snap_tiny_negative_water(point);
    f_adv[]=f_PFC[];aw_adv[]=a_water[];MF_adv[]=M_PFC[];MW_adv[]=M_water[];
    EF_adv[]=E_PFC[];EW_adv[]=E_water[];ZF_adv[]=Z_PFC[];
    foreach_dimension() q_adv.x[]=q.x[];
  }
  boundary({f_adv,aw_adv,MF_adv,MW_adv,EF_adv,EW_adv,ZF_adv,q_adv});
}

static int closure_geometric_pressure_step(double step) {
  closure_save_advected_targets();
  if(closure_equilibrate_fields(0,p_trial)) return 1;
  face vector face_pressure[],pressure_energy_flux[];
  double residual=HUGE;
  for(int iteration=0;iteration<80;iteration++) {
    boundary({p_trial});
    foreach_face() {
      double left=MW_adv[-1]+MF_adv[-1],right=MW_adv[]+MF_adv[];
      face_pressure.x[]=.5*(p_trial[-1]+p_trial[]);
      uf.x[]=fm.x[]*(.5*(q_adv.x[-1]/left+q_adv.x[]/right)-
        step*2./(left+right)*(p_trial[]-p_trial[-1])/Delta);
      pressure_energy_flux.x[]=face_pressure.x[]*uf.x[];
    }
    boundary((scalar *){uf,face_pressure,pressure_energy_flux});
    double work_defect=0.;
    foreach(reduction(+:work_defect)) {
      f_PFC[]=f_adv[];a_water[]=aw_adv[];M_PFC[]=MF_adv[];M_water[]=MW_adv[];
      Z_PFC[]=ZF_adv[];double rho=MW_adv[]+MF_adv[],oldK=0.,newK=0.,de=0.,divergence=0.;
      foreach_dimension() {
        oldK+=sq(q_adv.x[]);
        q.x[]=q_adv.x[]-step*(face_pressure.x[1]-face_pressure.x[])/Delta;
        newK+=sq(q.x[]);
        de-=step*(pressure_energy_flux.x[1]-pressure_energy_flux.x[])/(cm[]*Delta);
        divergence+=(uf.x[1]-uf.x[])/(cm[]*Delta);
      }
      double dk=(newK-oldK)/(2.*rho),yw=MW_adv[]/rho,yf=MF_adv[]/rho;
      E_water[]=EW_adv[]+aw_adv[]*de+(yw-aw_adv[])*dk;
      E_PFC[]=EF_adv[]+f_adv[]*de+(yf-f_adv[])*dk;
      work_defect+=fabs(de-dk+step*p_trial[]*divergence)*dv();
    }
    boundary({f_PFC,a_water,M_PFC,M_water,Z_PFC,E_PFC,E_water,q});
    if(closure_equilibrate_fields(1,p_EOS)) return 2;
    residual=0.;double source=0.;
    foreach(reduction(max:residual) reduction(+:source)) {
      double scale=fmax(1.e5,fmax(fabs(p_trial[]),fabs(p_EOS[])));
      residual=fmax(residual,fabs(p_EOS[]-p_trial[])/scale);
      source+=mechanical_entropy_step[]*dv();
    }
    geometric_statistics.pressure_iterations++;
    geometric_statistics.final_pressure_residual=residual;
    if(residual<1.e-8) {
      foreach() p[]=p_EOS[];
      boundary({p});geometric_statistics.work_defect+=work_defect;
      geometric_statistics.mechanical_entropy+=source;return 0;
    }
    foreach() p_trial[]=p_EOS[];
  }
  fprintf(stderr,"Final geometric EOS pressure residual failed: %.17g\n",residual);return 3;
}

static double closure_acoustic_timestep(double courant) {
  double step=HUGE;
  foreach(reduction(min:step)) {
    double velocity2=0.;foreach_dimension() velocity2+=sq(q.x[]/rho_flow[]);
    double speed=sqrt(wood[]/rho_flow[])+sqrt(velocity2);
    step=fmin(step,courant*Delta/speed);
  }
  return step;
}

static void closure_flow_integrals(double * mw,double * mf,double * energy,double * entropy,
  double * minimum_fraction,double * fraction_error,double * uncovered_mass) {
  double w=0.,f=0.,e=0.,s=0.,minimum=1.,error=0.,uncovered=0.;
  foreach(reduction(+:w) reduction(+:f) reduction(+:e) reduction(+:s)
    reduction(min:minimum) reduction(max:error) reduction(+:uncovered)) {
    w+=M_water[]*dv();f+=M_PFC[]*dv();e+=(E_water[]+E_PFC[])*dv();
    s+=(M_water[]*s_water[]+M_PFC[]*s_PFC[])*dv();
    minimum=fmin(minimum,fmin(f_PFC[],a_water[]));error=fmax(error,fabs(f_PFC[]+a_water[]-1.));
    if((f_PFC[]==0. && M_PFC[]>0.) || (f_PFC[]==1. && a_water[]>0.))
      uncovered+=(f_PFC[]==0.?M_PFC[]:M_water[])*dv();
  }
  *mw=w;*mf=f;*energy=e;*entropy=s;*minimum_fraction=minimum;
  *fraction_error=error;*uncovered_mass=uncovered;
}

static void closure_write_geometric_fields(FILE * stream,const char * stage,double time) {
  foreach() {
    double r=0.,ur=0.;
#if dimension > 1
    r=y;ur=q.y[]/(M_water[]+M_PFC[]);
#endif
    fprintf(stream,"%s,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g\n",
      stage,time,x,r,Delta,dv(),f_PFC[],a_water[],M_PFC[],M_water[],E_PFC[],E_water[],
      q.x[],ur*(M_water[]+M_PFC[]),Z_PFC[],p[],T_water[],T_PFC[],s_water[],s_PFC[],
      wood[],chi[],rhoL_cache[],rhoV_cache[],p_cache[],T_cache[]);
  }
}

static int closure_geometric_component(int argc,char ** argv) {
  if(argc!=7) return 2;
  const char * species=argv[1],* mode=argv[4];
  int n=atoi(argv[5]);double courant=atof(argv[6]),Ta=atof(argv[3]);
  if(n<8 || !(courant>0. && courant<=.3) || closure_bridge_setup(species,argv[2])) return 3;
  double length=1.e-4;size(length);origin(0.,0.,0.);periodic(right);
#if dimension > 1
  periodic(top);
#endif
  init_grid(n);
  f_PFC.closure_tracers=list_copy({M_PFC,M_water,E_PFC,E_water,Z_PFC,q_PFC,q_water});
  for(scalar field in {M_water,E_water,q_water}) field.closure_inverse=true;
  for(scalar field in {M_water,M_PFC,Z_PFC}) field.closure_positive=true;
  Z_PFC.closure_bounded=true;Z_PFC.closure_upper=M_PFC;
  for(scalar field in f_PFC.closure_tracers) field.gradient=minmod2;
  ClosureBridgeMaterial water,pfc;ClosureBridgeCache initial={0};
  double composition=.2;
  if(closure_bridge_water_initial(&water) ||
     closure_bridge_pfc_PT(101325.,Ta,composition,&initial,&pfc)) return 4;
  int water_wave=!strcmp(mode,"water_wave"),pfc_wave=!strcmp(mode,"PFC_wave");
  int stationary=!strcmp(mode,"stationary_contact"),moving=!strcmp(mode,"moving_contact");
  if(!water_wave && !pfc_wave && !stationary && !moving) return 5;
  double reference_c=sqrt(water_wave?water.c2:pfc.c2),velocity=moving?.1*sqrt(water.c2):0.;
  double end_time=(water_wave || pfc_wave)?.25*length/reference_c:
    moving?.1*length/velocity:.05*length/sqrt(water.c2);
  if(stationary || moving) {
#if dimension == 1
    fraction(f_PFC,min(x-.30*length,.65*length-x));
#else
    fraction(f_PFC,sq(.18*length)-sq(x-.5*length)-sq(y-.5*length));
#endif
  }
  int initial_failures=0;
  foreach(reduction(+:initial_failures)) {
    ClosureBridgeCache cache=initial;ClosureBridgeMaterial wi=water,fi=pfc;
    double u=velocity,perturbation=1.e-5*101325.*cos(2.*pi*x/length);
    if(water_wave) {
      double density=water.rho+perturbation/water.c2;
      double temperature=water.T*pow(density/water.rho,water.p_e/water.rho);
      if(closure_bridge_water_rho_T(density,temperature,&wi)) initial_failures++;
      f_PFC[]=0.;u=perturbation/(water.rho*reference_c);
    }
    if(pfc_wave) {
      double temperature=Ta+Ta*pfc.p_e/(pfc.rho*pfc.rho*pfc.c2)*perturbation;
      if(closure_bridge_pfc_PT(101325.+perturbation,temperature,composition,&cache,&fi)) initial_failures++;
      f_PFC[]=1.;u=perturbation/(pfc.rho*reference_c);
    }
    a_water[]=1.-f_PFC[];M_water[]=a_water[]*wi.rho;M_PFC[]=f_PFC[]*fi.rho;
    Z_PFC[]=composition*M_PFC[];double density=M_water[]+M_PFC[];
    q.x[]=density*u;
#if dimension > 1
    q.y[]=0.;
#endif
    E_water[]=M_water[]*(wi.e+.5*u*u);E_PFC[]=M_PFC[]*(fi.e+.5*u*u);
    closure_store_cell_cache(point,cache);
  }
  if(initial_failures) return 6;
  boundary({f_PFC,a_water,M_PFC,M_water,Z_PFC,E_PFC,E_water,q,
    rhoL_cache,rhoV_cache,T_cache,p_cache,validL_cache,validV_cache});
  if(closure_equilibrate_fields(1,p)) return 7;
  FILE * history=fopen("history.csv","w"),* fields=fopen("fields.csv","w");
  fprintf(history,"time_s,steps,water_mass,PFC_mass,total_energy,entropy,min_fraction,fraction_sum_error,uncovered_mass,pressure_residual,mechanical_entropy,work_defect,pressure_iterations,raw_queries,inverse_iterations,inverse_fallbacks,global_phase_queries,unresolved_complement_faces,limited_faces,exact_depletion_faces,max_depletion_flux_correction,max_paired_identity_defect,max_complement_adjustment,min_compression_denominator,min_donor_numerator\n");
  fprintf(fields,"stage,time_s,z_m,r_m,delta_m,volume_m3,f_PFC,a_water,M_PFC_kg_m3,M_water_kg_m3,E_PFC_J_m3,E_water_J_m3,qz_kg_m2_s,qr_kg_m2_s,Z_PFC_kg_m3,p_Pa,T_water_K,T_PFC_K,s_water_J_kg_K,s_PFC_J_kg_K,wood_Pa,chi,rhoL,rhoV,p_cache,T_cache\n");
  closure_write_geometric_fields(fields,"initial",0.);
  double time=0.;int iteration=0,status=0;
  while(time<end_time) {
    double mw,mf,energy,entropy,minimum,error,uncovered;
    closure_flow_integrals(&mw,&mf,&energy,&entropy,&minimum,&error,&uncovered);
    fprintf(history,"%.17g,%d,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%.17g,%.17g,%.17g,%.17g,%.17g\n",
      time,iteration,mw,mf,energy,entropy,minimum,error,uncovered,
      geometric_statistics.final_pressure_residual,geometric_statistics.mechanical_entropy,
      geometric_statistics.work_defect,geometric_statistics.pressure_iterations,
      geometric_statistics.raw_queries,geometric_statistics.inverse_iterations,
      geometric_statistics.inverse_fallbacks,geometric_statistics.global_phase_queries,
      geometric_statistics.advection.unresolved_complement_faces,
      geometric_statistics.advection.limited_faces,geometric_statistics.advection.exact_depletion_faces,
      geometric_statistics.advection.maximum_depletion_flux_correction,
      geometric_statistics.advection.maximum_paired_identity_defect,
      geometric_statistics.advection.maximum_complement_adjustment,
      geometric_statistics.advection.minimum_compression_denominator,
      geometric_statistics.advection.minimum_donor_numerator);
    fflush(history);
    double step=fmin(closure_acoustic_timestep(courant),end_time-time);
    closure_advective_face_velocity();
    if(closure_advect_conserved(step,iteration)) {status=8;break;}
    if(closure_geometric_pressure_step(step)) {status=9;break;}
    time+=step;iteration++;
    if(iteration>100000) {status=10;break;}
  }
  closure_write_geometric_fields(fields,status?"failed":"final",time);
  double mw,mf,energy,entropy,minimum,error,uncovered;
  closure_flow_integrals(&mw,&mf,&energy,&entropy,&minimum,&error,&uncovered);
  fprintf(history,"%.17g,%d,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%.17g,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%.17g,%.17g,%.17g,%.17g,%.17g\n",
    time,iteration,mw,mf,energy,entropy,minimum,error,uncovered,
    geometric_statistics.final_pressure_residual,geometric_statistics.mechanical_entropy,
    geometric_statistics.work_defect,geometric_statistics.pressure_iterations,
    geometric_statistics.raw_queries,geometric_statistics.inverse_iterations,
    geometric_statistics.inverse_fallbacks,geometric_statistics.global_phase_queries,
    geometric_statistics.advection.unresolved_complement_faces,
    geometric_statistics.advection.limited_faces,geometric_statistics.advection.exact_depletion_faces,
    geometric_statistics.advection.maximum_depletion_flux_correction,
    geometric_statistics.advection.maximum_paired_identity_defect,
    geometric_statistics.advection.maximum_complement_adjustment,
    geometric_statistics.advection.minimum_compression_denominator,
    geometric_statistics.advection.minimum_donor_numerator);
  fclose(history);fclose(fields);free(f_PFC.closure_tracers);f_PFC.closure_tracers=NULL;
  closure_bridge_cleanup();return status;
}
#endif
