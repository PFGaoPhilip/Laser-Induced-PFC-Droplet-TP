/* Parser-neutral diagnostic CPU/counter record, not a physical source. */
#ifndef CLOSURE_REACTION_PROFILE_API_H
#define CLOSURE_REACTION_PROFILE_API_H
#define CLOSURE_PHASE_PROFILE_STAGES 5
typedef struct {
  double stage_cpu[5],inverse_cpu[5],mixture_cpu[5],rates_cpu[5],spinodal_cpu[5];
  unsigned long inverse_calls[5],mixture_calls[5],rates_calls[5],spinodal_calls[5];
  unsigned long continuation_segments,root_iterations;
  double source_cpu;
} ClosurePhaseCPUProfile;
void closure_coupled_phase_profile_reset(void);
void closure_coupled_phase_profile_get(ClosurePhaseCPUProfile *);
#endif
