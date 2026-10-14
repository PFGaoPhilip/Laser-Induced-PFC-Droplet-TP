/* Original ordinary-C material adapter. It changes no EOS/energy reference.
 * All mutable numerical cache state is per call; globals are immutable after
 * startup and may be used by threaded geometric loops. */
#include "material_bridge.h"
#include "water_mg.h"
#include "pfc_conserved_inverse.h"
#include "pfc_temperature_inverse.h"
#include "mechanical_relaxation.h"
static ClosureWaterMG bridge_water;
static const ClosurePFCFluid * bridge_fluid=NULL;

typedef struct {
  double xi,p,T;
  ClosurePFCCache cache;
  ClosurePFCInverseStats stats;
  ClosurePFCMixture last;
} ClosureBridgePFCContext;

int closure_bridge_setup(const char * species,const char * water_table) {
  bridge_fluid=!strcmp(species,"PFP")?&pfp_fluid:!strcmp(species,"PFH")?&pfh_fluid:NULL;
  if(!bridge_fluid) return 1;
  return closure_water_load(water_table,&bridge_water);
}
void closure_bridge_cleanup(void) {closure_water_free(&bridge_water);bridge_fluid=NULL;}

static int bridge_water_eos(const void * unused,double rho,double e,ClosureMaterialState * s) {
  (void)unused;ClosureWaterState water;
  int status=closure_water_rho_e(&bridge_water,rho,e,&water);
  if(status) return status;
  *s=(ClosureMaterialState){water.p,water.T,water.s,water.c2,water.p_e,water.p_rho};
  return 0;
}
static int bridge_pfc_eos(const void * context,double rho,double e,ClosureMaterialState * s) {
  ClosureBridgePFCContext * f=(ClosureBridgePFCContext *)context;
  if(closure_pfc_invert_conserved_controls(bridge_fluid,rho,e,f->xi,&f->cache,&f->p,&f->T,
      1.e-10,1.e-13,1.e-13,80,&f->stats)) return 1;
  if(f->xi==0. || f->xi==1.) {
    /* Fixed-composition caloric pure-state properties do not require an
     * absent virtual phase. Chemical reaction still needs its own complete
     * affinity/branch evaluation and must not use this shortcut. */
    ClosurePFCPhase * occupied=f->xi==0.?&f->cache.liquid:&f->cache.vapour;
    double D=occupied->vp*occupied->cv;
    *s=(ClosureMaterialState){f->p,f->T,occupied->s,occupied->c2,
      -occupied->vT/D,-occupied->uT/(rho*rho*D)};
    return 0;
  }
  /* Reuse the actual conserved-coordinate phase states. Re-solving them at
   * PT would unnecessarily move the converged volume/energy targets by its
   * separate numerical root tolerance. Populated pressure equality is saved
   * and independently checked; this is not a thermodynamic projection. */
  memset(&f->last,0,sizeof(f->last));
  f->last.liquid=f->cache.liquid;f->last.vapour=f->cache.vapour;
  f->last.liquid_available=f->cache.liquid_valid;
  f->last.vapour_available=f->cache.vapour_valid;
  f->last.coalesced=f->T>=bridge_fluid->critical_T;
  if(!f->last.liquid_available || !f->last.vapour_available ||
    closure_pfc_combine(f->p,f->T,f->xi,&f->last)) return 1;
  double D=f->last.vp*f->last.cv;
  *s=(ClosureMaterialState){f->p,f->T,f->last.s,f->last.c2,
    -f->last.vT/D,-f->last.uT/(rho*rho*D)};
  return 0;
}

static void bridge_cache_decode(const ClosureBridgeCache * input,
  double xi,ClosureBridgePFCContext * output) {
  memset(output,0,sizeof(*output));output->xi=xi;
  output->p=input->p_pfc;output->T=input->T_pfc;
  if(input->liquid_valid) {
    output->stats.raw_queries++;
    if(!closure_pfc_raw(bridge_fluid,input->rho_liquid,input->T_pfc,
        &output->cache.liquid)) output->cache.liquid_valid=1;
  }
  if(input->vapour_valid) {
    output->stats.raw_queries++;
    if(!closure_pfc_raw(bridge_fluid,input->rho_vapour,input->T_pfc,
        &output->cache.vapour)) output->cache.vapour_valid=1;
  }
}
static void bridge_cache_encode(const ClosureBridgePFCContext * input,
  ClosureBridgeCache * output) {
  output->p_pfc=input->p;output->T_pfc=input->T;
  output->rho_liquid=input->cache.liquid.rho;output->rho_vapour=input->cache.vapour.rho;
  output->liquid_valid=input->cache.liquid_valid;output->vapour_valid=input->cache.vapour_valid;
}

int closure_bridge_water_initial(ClosureBridgeMaterial * result) {
  ClosureWaterState water;
  if(closure_water_rho_T(&bridge_water,1./bridge_water.v0,bridge_water.T0,&water)) return 1;
  *result=(ClosureBridgeMaterial){water.rho,water.e,water.s,water.p,water.T,
    water.c2,water.p_e,water.p_rho,water.cv};return 0;
}
int closure_bridge_water_rho_T(double rho,double T,ClosureBridgeMaterial * result) {
  ClosureWaterState water;
  if(closure_water_rho_T(&bridge_water,rho,T,&water)) return 1;
  *result=(ClosureBridgeMaterial){water.rho,water.e,water.s,water.p,water.T,
    water.c2,water.p_e,water.p_rho,water.cv};return 0;
}
int closure_bridge_water_rho_e(double rho,double e,ClosureBridgeMaterial * result) {
  ClosureWaterState water;
  if(closure_water_rho_e(&bridge_water,rho,e,&water)) return 1;
  *result=(ClosureBridgeMaterial){water.rho,water.e,water.s,water.p,water.T,
    water.c2,water.p_e,water.p_rho,water.cv};return 0;
}
int closure_bridge_pfc_PT(double p,double T,double xi,
  ClosureBridgeCache * cache,ClosureBridgeMaterial * result) {
  ClosureBridgePFCContext f;bridge_cache_decode(cache,xi,&f);
  if(closure_pfc_mixture_PT_cached(bridge_fluid,p,T,xi,&f.cache,&f.last)) return 1;
  f.p=p;f.T=T;bridge_cache_encode(&f,cache);
  double D=f.last.vp*f.last.cv;
  *result=(ClosureBridgeMaterial){f.last.rho,f.last.u,f.last.s,p,T,f.last.c2,
    -f.last.vT/D,-f.last.uT/(f.last.rho*f.last.rho*D),f.last.cv};return 0;
}
int closure_bridge_pfc_rho_e(double rho,double e,double xi,
  ClosureBridgeCache * cache,ClosureBridgeMaterial * result) {
  ClosureBridgePFCContext f;bridge_cache_decode(cache,xi,&f);
  ClosureMaterialState material;
  if(bridge_pfc_eos(&f,rho,e,&material)) return 1;
  double cv=(xi==0. || xi==1.)?
    (xi==0.?f.cache.liquid.cv:f.cache.vapour.cv):f.last.cv;
  *result=(ClosureBridgeMaterial){rho,e,material.s,material.p,material.T,
    material.c2,material.p_e,material.p_rho,cv};
  bridge_cache_encode(&f,cache);return 0;
}

int closure_bridge_pfc_rho_T(double rho,double T,double xi,
  ClosureBridgeCache * cache,ClosureBridgeMaterial * result) {
  if(!bridge_fluid || !(rho>0.) || !(T>0.) || !(xi>=0. && xi<=1.)) return 1;
  ClosureBridgePFCContext f;bridge_cache_decode(cache,xi,&f);
  if(xi==0. || xi==1.) {
    int liquid=xi==0.;
    ClosurePFCPhase old=liquid?f.cache.liquid:f.cache.vapour,occupied;
    if(!(liquid?f.cache.liquid_valid:f.cache.vapour_valid)) return 2;
    /* The occupied branch is inherited from a labelled accepted state.
     * Finite stable-path sampling is numerical continuation evidence, not
     * an interval proof that arbitrary far probes remain on that branch. */
    for(int j=1;j<=16;j++) {
      double theta=j/16.,r=old.rho+theta*(rho-old.rho),temperature=old.T+theta*(T-old.T);
      if(closure_pfc_raw(bridge_fluid,r,temperature,&occupied)) return 3;
      if(temperature<bridge_fluid->critical_T &&
          (liquid?r<=bridge_fluid->critical_rho:r>=bridge_fluid->critical_rho)) return 4;
    }
    if(liquid) {f.cache.liquid=occupied;f.cache.liquid_valid=1;}
    else {f.cache.vapour=occupied;f.cache.vapour_valid=1;}
    f.p=occupied.p;f.T=T;
    double D=occupied.vp*occupied.cv;
    *result=(ClosureBridgeMaterial){rho,occupied.u,occupied.s,occupied.p,T,
      occupied.c2,-occupied.vT/D,-occupied.uT/(rho*rho*D),occupied.cv};
    bridge_cache_encode(&f,cache);return 0;
  }
  ClosurePFCMixture state;
  ClosurePFCTemperatureInverseStats temperature_stats;
  if(!closure_pfc_temperature_inverse(bridge_fluid,rho,T,xi,&f.cache,&state,
      1.e-10,1.e-13,80,&temperature_stats)) {
    double D=state.vp*state.cv;
    *result=(ClosureBridgeMaterial){rho,state.u,state.s,state.p,T,state.c2,
      -state.vT/D,-state.uT/(rho*rho*D),state.cv};
    f.p=state.p;f.T=T;bridge_cache_encode(&f,cache);return 0;
  }
  /* Failed fast trials leave the numeric cache unchanged. Retry the original
   * PT-coordinate method at the identical rho/T/xi target, never a floor or
   * a different thermodynamic state. Both failures are explicit to caller. */
  double target=1./rho,p=f.p;
  if(closure_pfc_mixture_PT_cached(bridge_fluid,p,T,xi,&f.cache,&state)) return 5;
  for(int k=0;k<80;k++) {
    double residual=state.v-target;
    if(fabs(residual)/target<1.e-13) {
      double D=state.vp*state.cv;
      *result=(ClosureBridgeMaterial){rho,state.u,state.s,p,T,state.c2,
        -state.vT/D,-state.uT/(rho*rho*D),state.cv};
      f.p=p;f.T=T;bridge_cache_encode(&f,cache);return 0;
    }
    if(!(state.vp<0.) || !isfinite(state.vp)) return 6;
    double dp=-residual/state.vp;int accepted=0;
    for(int j=0;j<28;j++) {
      double trial_p=p+ldexp(dp,-j);
      ClosurePFCCache trial_cache=f.cache;ClosurePFCMixture trial;
      if(!closure_pfc_mixture_PT_cached(bridge_fluid,trial_p,T,xi,&trial_cache,&trial) &&
          fabs(trial.v-target)<fabs(residual)) {
        p=trial_p;f.cache=trial_cache;state=trial;accepted=1;break;
      }
    }
    if(!accepted) return 7;
  }
  return 8;
}

int closure_bridge_equilibrate(ClosureBridgeZone * zone,
  ClosureBridgeCache * cache,ClosureBridgeResult * result) {
  memset(result,0,sizeof(*result));
  if(!bridge_fluid || !(zone->m_water>=0. && zone->m_pfc>=0.) ||
    !(zone->xi>=0. && zone->xi<=1.)) return 1;
  double rho=zone->m_water+zone->m_pfc;
  if(!(rho>0.)) return 1;
  double k=.5*(zone->q_z*zone->q_z+zone->q_r*zone->q_r)/(rho*rho);
  double Uw=zone->E_water-zone->m_water*k,Uf=zone->E_pfc-zone->m_pfc*k;
  ClosureBridgePFCContext f;
  if(zone->m_pfc>0.) bridge_cache_decode(cache,zone->xi,&f);
  else memset(&f,0,sizeof(f));
  ClosureMaterialState water={0},pfc={0};
  if(zone->m_pfc==0.) {
    if(zone->a_water!=1. || zone->a_pfc!=0. ||
      bridge_water_eos(NULL,zone->m_water,Uw/zone->m_water,&water)) return 2;
    result->p=water.p;result->wood_modulus=zone->m_water*water.c2;
    result->thermal_response=water.p_e/zone->m_water;
  } else if(zone->m_water==0.) {
    if(zone->a_water!=0. || zone->a_pfc!=1. ||
      bridge_pfc_eos(&f,zone->m_pfc,Uf/zone->m_pfc,&pfc)) return 3;
    result->p=pfc.p;result->wood_modulus=zone->m_pfc*pfc.c2;
    result->thermal_response=pfc.p_e/zone->m_pfc;
  } else {
    ClosureMechanicalCell mixture={zone->a_water,zone->a_pfc,zone->m_water,
      zone->m_pfc,Uw,Uf};ClosureMechanicalResult source;
    if(closure_mechanical_relax(&mixture,bridge_water_eos,NULL,bridge_pfc_eos,&f,
        1.e-9,1.e-11,400,&source)) {
      fprintf(stderr,"bridge mechanical failure status=%d gap=%.17g steps=%d rejected=%d aW=%.17g aF=%.17g MW=%.17g MF=%.17g UW=%.17g UF=%.17g cached_p=%.17g cached_T=%.17g\n",
        source.status,source.final_relative_pressure_gap,source.steps,source.rejected_steps,
        zone->a_water,zone->a_pfc,zone->m_water,zone->m_pfc,Uw,Uf,f.p,f.T);
      return 4;
    }
    zone->a_water=mixture.water_fraction;zone->a_pfc=mixture.pfc_fraction;
    Uw=mixture.water_internal_energy_density;Uf=mixture.pfc_internal_energy_density;
    zone->E_water=Uw+zone->m_water*k;zone->E_pfc=Uf+zone->m_pfc*k;
    if(bridge_water_eos(NULL,zone->m_water/zone->a_water,Uw/zone->m_water,&water) ||
      bridge_pfc_eos(&f,zone->m_pfc/zone->a_pfc,Uf/zone->m_pfc,&pfc)) return 5;
    result->p=.5*(water.p+pfc.p);result->mechanical_entropy=source.integrated_entropy_source;
    double Bw=zone->m_water/zone->a_water*water.c2,Bf=zone->m_pfc/zone->a_pfc*pfc.c2;
    result->wood_modulus=1./(zone->a_water/Bw+zone->a_pfc/Bf);
    result->thermal_response=result->wood_modulus*(
      zone->a_water*(water.p_e/(zone->m_water/zone->a_water))/Bw+
      zone->a_pfc*(pfc.p_e/(zone->m_pfc/zone->a_pfc))/Bf);
  }
  result->T_water=water.T;result->T_pfc=pfc.T;
  result->s_water=water.s;result->s_pfc=pfc.s;
  result->c_water2=water.c2;result->c_pfc2=pfc.c2;
  result->raw_queries=f.stats.raw_queries;result->inverse_iterations=f.stats.iterations;
  result->inverse_fallbacks=f.stats.fallback_queries;
  result->phase_local_queries=f.cache.local_queries;
  result->phase_global_queries=f.cache.global_queries;
  if(zone->m_pfc>0.) bridge_cache_encode(&f,cache);
  return 0;
}
