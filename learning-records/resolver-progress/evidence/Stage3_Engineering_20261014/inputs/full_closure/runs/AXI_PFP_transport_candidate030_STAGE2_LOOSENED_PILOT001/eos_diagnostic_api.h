/* Parser-neutral numerical diagnostic only. No physical EOS/source data. */
#ifndef CLOSURE_EOS_DIAGNOSTIC_API_H
#define CLOSURE_EOS_DIAGNOSTIC_API_H
#define CLOSURE_EOS_DIAG_STAGES 8
#define CLOSURE_EOS_DIAG_CLASSES 3

enum ClosureEOSDiagStage {
  CLOSURE_EOS_INITIALIZATION=0, CLOSURE_EOS_PHASE_SOURCE,
  CLOSURE_EOS_INTERFACE_HEAT_SOURCE, CLOSURE_EOS_WATER_FOURIER_SOURCE,
  CLOSURE_EOS_VISCOUS_SOURCE, CLOSURE_EOS_MECHANICAL_REFRESH,
  CLOSURE_EOS_PRESSURE_CAPILLARY_ITERATION, CLOSURE_EOS_READONLY_SNAPSHOT
};
enum ClosureEOSDiagClass {
  CLOSURE_EOS_W_ONLY=0, CLOSURE_EOS_F_ONLY, CLOSURE_EOS_MIXED
};
enum ClosureEOSDiagMetric {
  CLOSURE_EOS_PFC_POTENTIAL=0,
  CLOSURE_EOS_PFC_CALORIC_RAW,
  CLOSURE_EOS_PFC_PRESSURE_STIFFNESS,
  CLOSURE_EOS_PFC_PRESSURE_ROOT,
  CLOSURE_EOS_PFC_PT_DISCOVERY,
  CLOSURE_EOS_PFC_PT_CACHED,
  CLOSURE_EOS_PFC_MIXTURE_PT,
  CLOSURE_EOS_PFC_MIXTURE_PT_CACHED,
  CLOSURE_EOS_PFC_INVERSE_PT,
  CLOSURE_EOS_PFC_INVERSE_PT_CACHED,
  CLOSURE_EOS_PFC_DENSITY_INVERSE,
  CLOSURE_EOS_PFC_ENDPOINT_INVERSE,
  CLOSURE_EOS_PFC_CONSERVED_INVERSE,
  CLOSURE_EOS_PFC_TEMPERATURE_INVERSE,
  CLOSURE_EOS_PFC_SPINODAL_K,
  CLOSURE_EOS_PFC_SPINODAL_K_DERIVATIVE,
  CLOSURE_EOS_PFC_SPINODAL_DISCOVERY,
  CLOSURE_EOS_PFC_SPINODAL_CACHED,
  CLOSURE_EOS_WATER_COLD_POTENTIAL,
  CLOSURE_EOS_WATER_CALORIC_RAW,
  CLOSURE_EOS_WATER_RHO_T_ENTRY,
  CLOSURE_EOS_WATER_RHO_P_ENTRY,
  CLOSURE_EOS_PFC_PT_LOCAL_ACCEPTED,
  CLOSURE_EOS_PFC_PT_GLOBAL_FALLBACK,
  CLOSURE_EOS_PFC_DENSITY_LOCAL_ACCEPTED,
  CLOSURE_EOS_PFC_DENSITY_GLOBAL_FALLBACK,
  CLOSURE_EOS_PFC_SPINODAL_SAME_T_ACCEPTED,
  CLOSURE_EOS_PFC_SPINODAL_WARM_ACCEPTED,
  CLOSURE_EOS_PFC_SPINODAL_GLOBAL_FALLBACK,
  CLOSURE_EOS_PFC_PT_TRIAL_REJECTED,
  CLOSURE_EOS_PFC_DENSITY_TRIAL_REJECTED,
  CLOSURE_EOS_PFC_TEMPERATURE_TRIAL_REJECTED,
  CLOSURE_EOS_PFC_SPINODAL_LOCAL_REJECTED,
  CLOSURE_EOS_PHASE_SOURCE_TRIAL_REJECTED,
  CLOSURE_EOS_DIAG_METRICS
};

typedef struct {
  unsigned long long calls[CLOSURE_EOS_DIAG_METRICS];
  unsigned long long unsuccessful_calls[CLOSURE_EOS_DIAG_METRICS];
  double inclusive_CPU_seconds[CLOSURE_EOS_DIAG_METRICS];
} ClosureEOSDiagCell;
typedef struct {
  ClosureEOSDiagCell stage_class[CLOSURE_EOS_DIAG_STAGES][CLOSURE_EOS_DIAG_CLASSES];
  ClosureEOSDiagCell unattributed;
  unsigned long long invalid_context_requests,invalid_heat_node_requests;
  int enabled,timing_enabled;
} ClosureEOSDiagStats;
typedef struct {
  double cpu_start;
  int stage,material_class,metric,enabled,timing_enabled;
} ClosureEOSDiagToken;
typedef struct {int stage,material_class,changed;} ClosureEOSDiagContext;

/* Reset clears counters and context; it does not enable instrumentation.
 * Context is a caller label, not inferred from a queried virtual phase.
 * One serial process only; mutable diagnostic counters are not thread-safe.
 * Timers are inclusive. Nested rows must never be added as disjoint CPU work.
 * Unsuccessful discovery may mean physical absence or numerical failure;
 * it is not automatically a rejected physical trajectory.
 */
void closure_eos_diag_reset(void);
void closure_eos_diag_enable(int enabled);
void closure_eos_diag_set_timing(int enabled);
int closure_eos_diag_set_context(int stage,int material_class);
void closure_eos_diag_get_context(int * stage,int * material_class);
void closure_eos_diag_get_stats(ClosureEOSDiagStats * stats);
/* Immutable caller-owned map, valid for one serial heat invocation. Both
 * material nodes from a mixed geometric leaf receive MIXED. Clear before
 * freeing the map. No material fraction or thermal input is altered. */
int closure_eos_diag_set_heat_node_classes(const int * classes,unsigned long nodes);
void closure_eos_diag_clear_heat_node_classes(void);
ClosureEOSDiagContext closure_eos_diag_enter_heat_node(unsigned long node);
void closure_eos_diag_leave_heat_node(ClosureEOSDiagContext context);
ClosureEOSDiagToken closure_eos_diag_enter(int metric);
void closure_eos_diag_leave(ClosureEOSDiagToken token,int status);
void closure_eos_diag_note(int metric,unsigned long long count);
#endif
