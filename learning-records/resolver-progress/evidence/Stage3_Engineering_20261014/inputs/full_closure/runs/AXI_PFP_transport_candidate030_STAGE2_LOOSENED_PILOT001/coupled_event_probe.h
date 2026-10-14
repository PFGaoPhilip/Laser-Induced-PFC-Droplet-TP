#ifndef CLOSURE_COUPLED_EVENT_PROBE_H
#define CLOSURE_COUPLED_EVENT_PROBE_H

/* Ordinary-C, parser-neutral accepted-endpoint diagnostic API.  No occupancy
   cutoff, EOS call, state modification, time horizon or contact certification. */
#include <stddef.h>
#include <stdint.h>

typedef struct {
  uint64_t leaf_index, nominal_z, nominal_r;
  unsigned level;
  long double z_lo, z_hi, r_lo, r_hi, physical_volume;
  long double water_mass, pfc_mass;
  double delta, normal_z, normal_r, alpha;
  double water_fraction, pfc_fraction, axial_velocity;
  int geometry_resolved; /* 1 only after positive material polygons resolved */
} ClosureEventLeaf;

typedef struct {
  long double lo, hi;
  uint64_t first_leaf, last_leaf;
} ClosureAxisInterval;

typedef struct {
  size_t axis_leaves, interval_count, isolated_points, ambiguous_leaves;
  int coverage_complete, axis_wall_contact, axis_film_known;
  long double pfc_mass, axis_film_gap, axis_film_max_delta, axis_film_cells;
  int status; /* 0 represented arithmetic valid; 2 topology/coverage uncertain */
} ClosureEventAxisReport;

/* Every actual leaf is supplied. Axis completeness is checked on [z0,z1].
   The output capacity must be >= the number of axis leaves.  Input errors
   (return 1) leave outputs untouched; geometric uncertainty (return 2) emits
   diagnostics and known positive intervals but cannot establish clearance.
   Return 3 means allocation/capacity failure.  Bounds must be the canonical
   represented dyadic square bounds, not independently rounded face estimates. */
int closure_event_axis(const ClosureEventLeaf *, size_t, long double z0,
                       long double z1, ClosureAxisInterval *, size_t,
                       ClosureEventAxisReport *);

typedef struct {
  long double lo, hi;
  int found, sampled_sign_change, unique_root_proved;
  size_t unresolved_samples;
} ClosureEventBracket;

typedef struct {
  long double time, pfc_volume, volume_rate_lo, volume_rate_hi;
  long double pfc_mass, axis_lo, axis_hi;
  size_t axis_intervals;
  int accepted_complete, axis_uncertain, axis_wall_contact;
  int global_wall_contact; /* -1 unknown, 0 checked detached, 1 contact */
} ClosureEventSample;

typedef struct {
  int initialized, last_strict_sign, stage, ancestry_lost;
  int any_wall_contact, global_wall_unknown;
  long double last_time, last_strict_time, previous_axis_lo, previous_axis_hi;
  size_t samples, unresolved_rate_samples, pending_unresolved;
  size_t maxima, minima, early_minima, previous_axis_intervals;
  int previous_axis_uncertain, previous_detached;
  long double previous_pfc_mass;
  ClosureEventBracket growth_max, collapse_min, rebound_max, axis_clearance;
  long double clearance_location_lo, clearance_location_hi;
} ClosureEventState;

void closure_event_state_init(ClosureEventState *);
/* Successful samples must be strictly ordered complete accepted endpoints.
   Return 1 leaves the state untouched. Brackets are sampled sign-change or
   axis-clearance candidates; unique_root_proved remains zero. In particular,
   axis_clearance is never itself the axial liquid-liquid impact time. */
int closure_event_push(ClosureEventState *, const ClosureEventSample *);

#endif
