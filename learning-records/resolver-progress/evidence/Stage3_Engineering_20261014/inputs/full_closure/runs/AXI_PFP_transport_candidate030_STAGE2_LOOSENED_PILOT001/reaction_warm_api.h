#ifndef CLOSURE_REACTION_WARM_API_H
#define CLOSURE_REACTION_WARM_API_H
typedef struct { unsigned long saved,seed_uses,fallbacks,exhaustions; } ClosureReactionWarmDiagnostic;
void closure_coupled_phase_warm_get(ClosureReactionWarmDiagnostic *);
#endif
