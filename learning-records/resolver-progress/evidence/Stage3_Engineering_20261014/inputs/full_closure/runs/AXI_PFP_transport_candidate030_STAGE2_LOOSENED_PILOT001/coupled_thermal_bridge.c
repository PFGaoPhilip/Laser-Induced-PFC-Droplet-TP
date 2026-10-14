/* Selected TH09 heat-only operator. No mechanical, momentum or phase source.
 * Material lookup and root trials use copied caches; only the final complete
 * invocation writes physical output caches. All nodes/patches stay retained.
 */
#include "coupled_thermal_bridge.h"
#include "nonlocal_thermal_integrator.h"
#include <stddef.h>

typedef struct {
  int nodes,pfc_nodes;
  const ClosureCoupledThermalNode * input;
  ClosureBridgeCache * base;
  ClosureCoupledThermalStats * stats;
} ClosureCoupledThermalContext;

static int coupled_thermal_failed(ClosureCoupledThermalContext * c,int a,int status) {
  c->stats->material_probe_failures++;
  if(c->stats->first_probe_failure_node<0) {
    c->stats->first_probe_failure_node=a;c->stats->first_probe_bridge_status=status;
  }
  return 1;
}
static int coupled_thermal_caloric(ClosureCoupledThermalContext * c,int a,
  double value,int by_temperature,ClosureBridgeMaterial * material,
  ClosureBridgeCache * output_cache,ClosureHeatState * heat_state) {
  const ClosureCoupledThermalNode * n=c->input+a;
  double rho=n->mass_kg/n->volume_m3;
  ClosureBridgeCache cache=c->base[a];
  int status;
  if(by_temperature) {
    c->stats->material_temperature_queries++;
    status=a<c->pfc_nodes?
      closure_bridge_pfc_rho_T(rho,value,n->vapour_mass_fraction,&cache,material):
      closure_bridge_water_rho_T(rho,value,material);
  } else {
    c->stats->material_energy_queries++;
    status=a<c->pfc_nodes?
      closure_bridge_pfc_rho_e(rho,value/n->mass_kg,n->vapour_mass_fraction,&cache,material):
      closure_bridge_water_rho_e(rho,value/n->mass_kg,material);
  }
  if(status) return coupled_thermal_failed(c,a,status);
  if(!(material->T>0.) || !(material->cv>0.) || !(material->c2>0.) ||
     !isfinite(material->T+material->cv+material->c2+material->e+material->s+material->p) ||
     (a<c->pfc_nodes && !(material->p>0.)))
    return coupled_thermal_failed(c,a,100);
  double phi=0.;
  if(a<c->pfc_nodes) {
    double xi=n->vapour_mass_fraction;
    if(xi==0. || xi==1.) phi=xi;
    else if(cache.vapour_valid && cache.rho_vapour>0. && isfinite(cache.rho_vapour))
      phi=rho*xi/cache.rho_vapour;
    else return coupled_thermal_failed(c,a,101);
    if(!(phi>=0. && phi<=1.) || !isfinite(phi))
      return coupled_thermal_failed(c,a,102);
  }
  *heat_state=(ClosureHeatState){material->T,n->mass_kg*material->s,
    n->mass_kg*material->cv,phi};
  if(!closure_heat_integrator_state_valid(heat_state))
    return coupled_thermal_failed(c,a,103);
  if(output_cache) *output_cache=cache;
  return 0;
}
static int coupled_thermal_energy(void * context,int a,double E,ClosureHeatState * state) {
  ClosureBridgeMaterial material;
  return coupled_thermal_caloric(context,a,E,0,&material,NULL,state);
}
static int coupled_thermal_temperature(void * context,int a,double T,double * E,
  ClosureHeatState * state) {
  ClosureCoupledThermalContext * c=context;ClosureBridgeMaterial material;
  int status=coupled_thermal_caloric(c,a,T,1,&material,NULL,state);
  if(!status) {*E=c->input[a].mass_kg*material.e;if(!isfinite(*E)) return coupled_thermal_failed(c,a,104);}
  return status;
}
void closure_coupled_thermal_default_controls(double maximum_step_s,
  ClosureCoupledThermalControls * c) {
  if(c) *c=(ClosureCoupledThermalControls){0,64,20,80,80,.25,1.e-11,1.e-9,
    2.e-9,maximum_step_s,2.,4096,.25}; /* c030 STAGE2_LOOSENED looser energy/entropy gates */
}
static void coupled_thermal_copy_stats(const ClosureHeatIntegratorStats * i,
  ClosureCoupledThermalStats * s) {
  s->evaluations=i->evaluations;s->temperature_queries=i->temperature_queries;
  s->scalar_iterations=i->scalar_iterations;s->mean_iterations=i->mean_iterations;
  s->rejected_trials=i->rejected_trials;s->explicit_steps=i->explicit_steps;
  s->implicit_steps=i->implicit_steps;s->trial_domain_failures=i->trial_domain_failures;
  s->caloric_signed_brackets=i->caloric_signed_brackets;
  s->caloric_conditioned_only=i->caloric_conditioned_only;
  s->mean_root_probes=i->mean_root_probes;s->energy_root_probes=i->energy_root_probes;
  s->minimum_guard_s=i->minimum_guard;s->energy_defect_J=i->energy_defect;
  s->entropy_increment_J_K=i->entropy_increment;
  s->physical_entropy_integral_J_K=i->physical_entropy_integral;
  s->frozen_entropy_lower_bound_J_K=i->frozen_entropy_lower_bound;
  s->entropy_lower_margin_J_K=i->entropy_lower_margin;
  s->maximum_row_absolute_J=i->maximum_row_absolute;
  s->maximum_row_conditioned_temperature_K=i->maximum_row_conditioned_temperature;
  s->maximum_caloric_temperature_width_K=i->maximum_caloric_temperature_width;
  s->maximum_caloric_energy_width_J=i->maximum_caloric_energy_width;
  s->maximum_mean_residual_K=i->maximum_mean_residual;
  s->maximum_root_temperature_correction_K=i->maximum_root_temperature_correction;
  s->active_energy_scale_J=i->active_energy_scale;
  s->active_entropy_scale_J_K=i->active_entropy_scale;
  s->accepted_time_s=i->accepted_time;s->last_step_s=i->last_step;
  s->maximum_energy_root_residual_J=i->maximum_energy_root_residual;
  s->last_energy_root_residual_J=i->last_energy_root_residual;
  s->last_mean_root_residual_K=i->last_mean_root_residual;
  s->minimum_observed_mean_slope=i->minimum_observed_mean_slope;
  s->last_rejection_reason=i->last_rejection_reason;s->selected_mode=i->selected_mode;
  s->integrator_status=i->status;
}
int closure_coupled_thermal_step(int nodes,int pfc_nodes,
  const ClosureCoupledThermalNode * input,int patches,
  const ClosureCoupledThermalPatch * interface_patches,
  const ClosureCoupledThermalParameters * parameters,double interval_s,
  const ClosureCoupledThermalControls * controls,ClosureCoupledThermalOutput * output,
  ClosureCoupledThermalStats * stats) {
  if(!stats) return 1;
  memset(stats,0,sizeof(*stats));stats->first_probe_failure_node=-1;stats->status=1;
  if(!input || !parameters || !controls || !output || nodes<1 || pfc_nodes<0 ||
     pfc_nodes>nodes || patches<0 || (patches && !interface_patches) ||
     (pfc_nodes==0 && patches!=0) || !(interval_s>=0.) || !isfinite(interval_s) ||
     !(parameters->inventory_kg>0.) || !(parameters->critical_temperature_K>0.) ||
     !(parameters->taper_width_fraction>0.) ||
     !(parameters->k_liquid_W_m_K>0.) || !(parameters->k_vapour_W_m_K>0.) ||
     !(parameters->k_critical_W_m_K>0.) ||
     !isfinite(parameters->inventory_kg+parameters->critical_temperature_K+
       parameters->taper_width_fraction+parameters->k_liquid_W_m_K+
       parameters->k_vapour_W_m_K+parameters->k_critical_W_m_K))
    return 1;
  size_t n=(size_t)nodes,k=(size_t)patches;
  if(n>SIZE_MAX/sizeof(ClosureCoupledThermalOutput) ||
     n>SIZE_MAX/sizeof(ClosureBridgeCache) ||
     n>SIZE_MAX/sizeof(ClosureHeatNode) || k>SIZE_MAX/sizeof(ClosureHeatPatch) ||
     n>SIZE_MAX/(2*sizeof(double))) {stats->status=2;return 2;}
  ClosureHeatNode * physical=calloc(n,sizeof(*physical));
  ClosureHeatPatch * patch=k?calloc(k,sizeof(*patch)):NULL;
  ClosureBridgeCache * base=calloc(n,sizeof(*base));
  ClosureCoupledThermalOutput * proposed=calloc(n,sizeof(*proposed));
  double * energy=calloc(2*n,sizeof(*energy));
  if(!physical || (k && !patch) || !base || !proposed || !energy)
    {stats->status=2;goto finish;}
  ClosureCoupledThermalContext context={nodes,pfc_nodes,input,base,stats};
  long double mF=0.L,mW=0.L,vF=0.L,area=0.L;
  for(int a=0;a<nodes;a++) {
    const ClosureCoupledThermalNode * cell=input+a;
    if(!(cell->mass_kg>0.) || !(cell->volume_m3>0.) ||
       !isfinite(cell->mass_kg+cell->volume_m3+cell->internal_energy_J) ||
       (a<pfc_nodes && !(cell->vapour_mass_fraction>=0. && cell->vapour_mass_fraction<=1.)))
      goto finish;
    double rho=cell->mass_kg/cell->volume_m3;
    if(!(rho>0.) || !isfinite(rho)) goto finish;
    physical[a]=(ClosureHeatNode){cell->mass_kg,cell->volume_m3};
    base[a]=cell->cache;energy[a]=cell->internal_energy_J;
    ClosureBridgeMaterial material;ClosureHeatState heat;
    ClosureBridgeCache accepted;
    if(coupled_thermal_caloric(&context,a,energy[a],0,&material,&accepted,&heat))
      {stats->status=3;goto finish;}
    /* Refresh only the private accepted-old seed after a valid old-state
     * inverse. Incoming input/cache remains unchanged even on later failure. */
    base[a]=accepted;
    if(a<pfc_nodes) {mF+=cell->mass_kg;vF+=cell->volume_m3;}
    else mW+=cell->mass_kg;
  }
  for(int j=0;j<patches;j++) {
    const ClosureCoupledThermalPatch * p=interface_patches+j;
    if(!(p->area_m2>=0.) || !(p->water_conductance_W_K>=0.) ||
       !isfinite(p->area_m2+p->water_conductance_W_K) ||
       p->water_node<pfc_nodes || p->water_node>=nodes) goto finish;
    patch[j]=(ClosureHeatPatch){p->area_m2,p->water_conductance_W_K,p->water_node};
    area+=p->area_m2;
  }
  stats->PFC_mass_kg=(double)mF;stats->water_mass_kg=(double)mW;
  stats->PFC_volume_m3=(double)vF;stats->patch_area_m2=(double)area;
  stats->measured_weight_sum=(double)(mF/parameters->inventory_kg);
  ClosureHeatModel model={nodes,pfc_nodes,patches,physical,patch,
    parameters->inventory_kg,parameters->critical_temperature_K,
    parameters->taper_width_fraction,parameters->k_liquid_W_m_K,
    parameters->k_vapour_W_m_K,parameters->k_critical_W_m_K,
    coupled_thermal_energy,&context};
  ClosureHeatIntegratorControls numerical={controls->mode,controls->max_explicit_steps,
    controls->max_refinements,controls->max_scalar_iterations,controls->max_mean_iterations,
    controls->guard_fraction,controls->temperature_tolerance,controls->energy_tolerance,
    controls->entropy_roundoff,controls->maximum_step_s,controls->implicit_growth,
    controls->maximum_accepted_steps,controls->minimum_mean_root_slope};
  ClosureHeatIntegratorStats diagnostic;
  int failure=closure_heat_integrate(&model,coupled_thermal_temperature,interval_s,
    energy,energy+n,&numerical,&diagnostic);
  coupled_thermal_copy_stats(&diagnostic,stats);
  if(failure) {stats->status=4;goto finish;}
  for(int a=0;a<nodes;a++) {
    ClosureHeatState state;
    proposed[a].internal_energy_J=energy[n+a];
    if(coupled_thermal_caloric(&context,a,energy[n+a],0,
        &proposed[a].material,&proposed[a].cache,&state))
      {stats->status=5;goto finish;}
    double rebuild=fabs(input[a].mass_kg*proposed[a].material.e-energy[n+a]);
    if(rebuild>stats->maximum_caloric_energy_rebuild_J)
      stats->maximum_caloric_energy_rebuild_J=rebuild;
  }
  memcpy(output,proposed,n*sizeof(*output));stats->status=0;
finish:
  free(physical);free(patch);free(base);free(proposed);free(energy);
  return stats->status;
}
