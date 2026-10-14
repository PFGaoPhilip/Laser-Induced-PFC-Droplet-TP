#include "coupled_phase_bridge.h"
#include "pfc_reaction.h"
static const ClosurePFCFluid * coupled_phase_fluid=NULL;

int closure_coupled_phase_setup(const char * species) {
  coupled_phase_fluid=!strcmp(species,"PFP")?&pfp_fluid:
    !strcmp(species,"PFH")?&pfh_fluid:NULL;
  return coupled_phase_fluid?0:1;
}

void * closure_coupled_phase_caches_new(unsigned long nodes) {
  return calloc(nodes,sizeof(ClosurePFCSpinodalCache));
}
void closure_coupled_phase_caches_free(void * caches){free(caches);}
void * closure_coupled_phase_cache_at(void * caches,unsigned long i) {
  return caches?&((ClosurePFCSpinodalCache *)caches)[i]:NULL;
}
int closure_coupled_phase_step_cached(ClosureBridgeZone * zone,ClosureBridgeCache * cache,
  void * numerical_spinodal_cache,
  double area_per_mass,double alpha,double interval,ClosureCoupledPhaseDiagnostics * d) {
  memset(d,0,sizeof(*d));
  if(!coupled_phase_fluid || !(interval>=0.) || !isfinite(interval) ||
     !(area_per_mass>=0.) || !isfinite(area_per_mass) ||
     !(alpha>=0. && alpha<=1.)) return 1;
  if(!(zone->m_water>=0.) || !isfinite(zone->m_water) ||
     !(zone->m_pfc>=0.) || !isfinite(zone->m_pfc) ||
     !(zone->a_water>=0. && zone->a_water<=1.) ||
     !(zone->a_pfc>=0. && zone->a_pfc<=1.) ||
     fabs(zone->a_water+zone->a_pfc-1.)>1.e-12 ||
     !isfinite(zone->q_z) || !isfinite(zone->q_r) ||
     !isfinite(zone->E_water) || !isfinite(zone->E_pfc) ||
     (zone->m_water>0. && !(zone->a_water>0.)) ||
     (zone->m_water==0. && zone->a_water!=0.))return 2;
  if(zone->m_pfc==0.)return zone->a_pfc==0.?0:2;
  if(!(zone->m_pfc>0.) || !(zone->a_pfc>0.) ||
     !(zone->xi>=0. && zone->xi<=1.) ||
     !(cache->p_pfc>0.) || !(cache->T_pfc>0.)) return 2;
  double density=zone->m_water+zone->m_pfc;
  if(!(density>0.))return 2;
  double kinetic=.5*(zone->q_z*zone->q_z+zone->q_r*zone->q_r)/(density*density);
  double rho=zone->m_pfc/zone->a_pfc,u=zone->E_pfc/zone->m_pfc-kinetic;
  ClosurePFCCache native_cache={0};
  if(cache->liquid_valid) {
    if(closure_pfc_raw(coupled_phase_fluid,cache->rho_liquid,cache->T_pfc,
        &native_cache.liquid))return 3;
    native_cache.liquid_valid=1;
  }
  if(cache->vapour_valid) {
    if(closure_pfc_raw(coupled_phase_fluid,cache->rho_vapour,cache->T_pfc,
        &native_cache.vapour))return 3;
    native_cache.vapour_valid=1;
  }
  ClosurePFCReactionParameters parameters=closure_pfc_reaction_defaults();
  parameters.alpha_condensation=alpha;parameters.area_per_mass=area_per_mass;
  ClosurePFCSpinodalCache trial_spinodal={0};
  if(numerical_spinodal_cache) {
    trial_spinodal=*(ClosurePFCSpinodalCache *)numerical_spinodal_cache;
    parameters.spinodal_cache=&trial_spinodal;
  }
  ClosurePFCReactionStep out;
  int status=closure_pfc_reaction_step(coupled_phase_fluid,rho,u,zone->xi,
    cache->p_pfc,cache->T_pfc,interval,&native_cache,&parameters,&out);
  d->native_status=status;
  if(status)return 10+status;
  if(!(out.state.p>0.) || !(out.state.T>0.) ||
     !(out.xi_after>=0. && out.xi_after<=1.))return 4;
  d->xi_before=zone->xi;d->xi_after=out.xi_after;
  d->p_before=cache->p_pfc;d->p_after=out.state.p;
  d->T_before=cache->T_pfc;d->T_after=out.state.T;
  d->entropy_HKS_J_kg_K=out.source_entropy_HKS;
  d->entropy_bulk_J_kg_K=out.source_entropy_bulk;
  d->entropy_path_J_kg_K=out.source_entropy_path;
  d->raw_entropy_change_J_kg_K=out.specific_entropy_change;
  d->entropy_primitive_remainder_J_kg_K=out.entropy_primitive_remainder;
  d->path_time_s=out.source_path_time;
  d->entropy_quadrature_error_J_kg_K=out.entropy_quadrature_error;
  d->time_quadrature_error_s=out.time_quadrature_error;
  d->volume_residual=out.eos_volume_residual;
  d->energy_residual=out.eos_energy_residual;
  d->composition_residual=out.implicit_composition_residual;
  d->evaluations=out.evaluations;d->rejected_trials=out.rejected_trials;
  d->quadrature_nodes=out.quadrature_nodes;
  d->endpoint_complementarity=out.endpoint_complementarity;
  d->canonical_supercritical=out.canonical_supercritical_label;
  if(numerical_spinodal_cache) {
    const ClosurePFCSpinodalCache * prior=numerical_spinodal_cache;
    d->spinodal_same_T=trial_spinodal.same_T_queries-prior->same_T_queries;
    d->spinodal_warm=trial_spinodal.warm_queries-prior->warm_queries;
    d->spinodal_global=trial_spinodal.global_queries-prior->global_queries;
    d->spinodal_raw_K=trial_spinodal.raw_K_queries-prior->raw_K_queries;
    *(ClosurePFCSpinodalCache *)numerical_spinodal_cache=trial_spinodal;
  }
  /* Transactional physical commit. No latent term or caloric/EOS reset. */
  zone->xi=out.xi_after;
  cache->p_pfc=out.state.p;cache->T_pfc=out.state.T;
  cache->rho_liquid=out.eos_cache.liquid.rho;
  cache->rho_vapour=out.eos_cache.vapour.rho;
  cache->liquid_valid=out.eos_cache.liquid_valid;
  cache->vapour_valid=out.eos_cache.vapour_valid;
  return 0;
}
int closure_coupled_phase_step(ClosureBridgeZone * zone,ClosureBridgeCache * cache,
  double area_per_mass,double alpha,double interval,ClosureCoupledPhaseDiagnostics * d) {
  return closure_coupled_phase_step_cached(zone,cache,NULL,area_per_mass,alpha,interval,d);
}
