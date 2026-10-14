/* Ordinary-C phase adapter; native thermodynamics stays outside qcc parsing.
 * Changes composition only at fixed material mass/subvolume/internal energy
 * and shared momentum. Mechanical and surface work are separate operators. */
#ifndef CLOSURE_COUPLED_PHASE_BRIDGE_H
#define CLOSURE_COUPLED_PHASE_BRIDGE_H
#include "material_bridge.h"
typedef struct {
  double xi_before,xi_after,p_before,p_after,T_before,T_after;
  double entropy_HKS_J_kg_K,entropy_bulk_J_kg_K,entropy_path_J_kg_K;
  double raw_entropy_change_J_kg_K,entropy_primitive_remainder_J_kg_K;
  double path_time_s,entropy_quadrature_error_J_kg_K,time_quadrature_error_s;
  double volume_residual,energy_residual,composition_residual;
  unsigned long evaluations,rejected_trials,quadrature_nodes;
  unsigned long spinodal_same_T,spinodal_warm,spinodal_global,spinodal_raw_K;
  int native_status,endpoint_complementarity,canonical_supercritical;
} ClosureCoupledPhaseDiagnostics;
int closure_coupled_phase_setup(const char * species);
/* Opaque caller-owned numerical records. Allocate once per fixed leaf;
 * rejected whole-source trials use copied records and commit only on status0.
 * NULL uses the accepted reference discovery, without the optional cache. */
void * closure_coupled_phase_caches_new(unsigned long nodes);
void closure_coupled_phase_caches_free(void *);
void * closure_coupled_phase_cache_at(void *,unsigned long index);
int closure_coupled_phase_step_cached(ClosureBridgeZone *,ClosureBridgeCache *,
  void * numerical_spinodal_cache,double area_per_mass_m2_kg,
  double alpha_condensation,double interval_s,ClosureCoupledPhaseDiagnostics *);
int closure_coupled_phase_step(ClosureBridgeZone * zone,ClosureBridgeCache * cache,
  double area_per_mass_m2_kg,double alpha_condensation,double interval_s,
  ClosureCoupledPhaseDiagnostics * diagnostics);
#endif
