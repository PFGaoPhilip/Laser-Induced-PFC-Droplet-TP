/* Ordinary-C heat source API for the geometric flow wrapper.
 * This header deliberately contains no native EOS/integrator implementation,
 * so qcc only sees plain data and function declarations.
 *
 * Node order: every occupied PFC node first, then every occupied incident
 * water patch node exactly once (optional supplied nonincident water retained).
 * Every supplied mass/subvolume is strictly positive, without a threshold.
 * Patch water_node uses that joint array's index; repeated incident patches
 * on a single water node are allowed. Caller must prove complete PFC/patch
 * collection; this heat source does not replace whole-domain water observers.
 * input energies are extensive INTERNAL energies, not total vector energies.
 * Momentum, mass, volume, xi and mechanical relaxation are outside this API.
 */
#ifndef CLOSURE_COUPLED_THERMAL_BRIDGE_H
#define CLOSURE_COUPLED_THERMAL_BRIDGE_H
#include "material_bridge.h"

typedef struct {
  double mass_kg,volume_m3,internal_energy_J,vapour_mass_fraction;
  ClosureBridgeCache cache;
} ClosureCoupledThermalNode;
typedef struct {
  double area_m2,water_conductance_W_K;
  int water_node;
} ClosureCoupledThermalPatch;
typedef struct {
  double inventory_kg,critical_temperature_K,taper_width_fraction;
  double k_liquid_W_m_K,k_vapour_W_m_K,k_critical_W_m_K;
} ClosureCoupledThermalParameters;
typedef struct {
  int mode,max_explicit_steps,max_refinements,max_scalar_iterations,max_mean_iterations;
  double guard_fraction,temperature_tolerance,energy_tolerance,entropy_roundoff;
  double maximum_step_s,implicit_growth;
  unsigned long maximum_accepted_steps;
  double minimum_mean_root_slope;
} ClosureCoupledThermalControls;
typedef struct {
  double internal_energy_J;
  ClosureBridgeMaterial material;
  ClosureBridgeCache cache;
} ClosureCoupledThermalOutput;
typedef struct {
  unsigned long evaluations,temperature_queries,scalar_iterations,mean_iterations;
  unsigned long rejected_trials,explicit_steps,implicit_steps,trial_domain_failures;
  unsigned long caloric_signed_brackets,caloric_conditioned_only;
  unsigned long mean_root_probes,energy_root_probes;
  unsigned long material_energy_queries,material_temperature_queries,material_probe_failures;
  double minimum_guard_s,energy_defect_J,entropy_increment_J_K,physical_entropy_integral_J_K;
  double frozen_entropy_lower_bound_J_K,entropy_lower_margin_J_K;
  double maximum_row_absolute_J,maximum_row_conditioned_temperature_K;
  double maximum_caloric_temperature_width_K,maximum_caloric_energy_width_J;
  double maximum_mean_residual_K,maximum_root_temperature_correction_K;
  double active_energy_scale_J,active_entropy_scale_J_K,accepted_time_s,last_step_s;
  double maximum_energy_root_residual_J,last_energy_root_residual_J,last_mean_root_residual_K;
  double minimum_observed_mean_slope,maximum_caloric_energy_rebuild_J;
  double PFC_mass_kg,water_mass_kg,PFC_volume_m3,patch_area_m2,measured_weight_sum;
  int last_rejection_reason,selected_mode,integrator_status,status;
  int first_probe_failure_node,first_probe_bridge_status;
} ClosureCoupledThermalStats;

/* Numerical defaults from scalable preregistration003, mode0=AUTO.
 * Caller supplies the maximum numerical source substep and freezes any
 * campaign changes before affected runs. No physical parameter is defaulted.
 */
void closure_coupled_thermal_default_controls(double maximum_step_s,
  ClosureCoupledThermalControls *);

/* Requires prior successful closure_bridge_setup for the selected species
 * and water potential. It neither initializes nor cleans up those globals.
 * Every caloric old/probe/stage/end state must satisfy stable populated
 * branches, positive T/Cv/c2 and selected extra PFC pressure>0 path guard.
 * Failed caloric probes are numerical diagnostics, not committed states.
 * Output, including returned caches, stays byte unchanged on nonzero return.
 * stats describes any rejected attempt; only status0 commits the whole array.
 *
 * Status:1invalid input,2allocation,3initial caloric state,4integration,
 * 5final caloric state. integrator_status and raw probe status remain separate.
 */
int closure_coupled_thermal_step(int nodes,int pfc_nodes,
  const ClosureCoupledThermalNode * input,int patches,
  const ClosureCoupledThermalPatch * interface_patches,
  const ClosureCoupledThermalParameters *,double interval_s,
  const ClosureCoupledThermalControls *,ClosureCoupledThermalOutput * output,
  ClosureCoupledThermalStats * stats);
#endif
