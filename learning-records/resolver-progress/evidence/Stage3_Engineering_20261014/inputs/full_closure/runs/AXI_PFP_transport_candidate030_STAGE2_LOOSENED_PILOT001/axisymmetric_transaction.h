/* Whole-macrostep transaction for the fixed, locally refined AXI tree.
 * Include after axisymmetric_coupled_core.h. The trial is still archived on
 * failure; restore changes no accepted state and does not retry/clip it.
 * AMR/topology-changing macrosteps require a separate tree transaction.
 */
#ifndef CLOSURE_AXISYMMETRIC_TRANSACTION_H
#define CLOSURE_AXISYMMETRIC_TRANSACTION_H
typedef struct {
  double * state;
  double * face_velocity;
  ClosureAxisymmetricGeometry * geometry;
  ClosureAxisymmetricCoreStats accepted_statistics;
  ClosureGeometricFlowStats accepted_flow_statistics;
  unsigned long leaf_count;
  unsigned long face_count;
  int fields,valid;
} ClosureAxisymmetricTransaction;
static scalar * closure_axisymmetric_transaction_fields(void) {
  return list_copy({f_PFC,a_water,M_PFC,M_water,E_PFC,E_water,Z_PFC,q,q_PFC,q_water,q_adv,
    p,rho_flow,wood,chi,T_water,T_PFC,s_water,s_PFC,rhoL_cache,rhoV_cache,T_cache,p_cache,
    validL_cache,validV_cache,mechanical_entropy_step,f_adv,aw_adv,MF_adv,MW_adv,EF_adv,EW_adv,ZF_adv,
    p_trial,p_EOS});
}
static int closure_axisymmetric_transaction_prepare(ClosureAxisymmetricTransaction * transaction) {
  if(!transaction)return 1;memset(transaction,0,sizeof(*transaction));
  scalar * variables=closure_axisymmetric_transaction_fields();int fields=list_len(variables);free(variables);
  if(fields<1 || axis_leaf_count<1)return 2;
  transaction->state=malloc((size_t)fields*axis_leaf_count*sizeof(double));
  transaction->geometry=malloc(axis_leaf_count*sizeof(ClosureAxisymmetricGeometry));
  unsigned long face_count=0;foreach_face(serial)face_count++;
  transaction->face_velocity=malloc(face_count*sizeof(double));
  if(!transaction->state || !transaction->geometry || !transaction->face_velocity) {
    free(transaction->state);free(transaction->geometry);free(transaction->face_velocity);
    memset(transaction,0,sizeof(*transaction));return 3;
  }
  transaction->fields=fields;transaction->leaf_count=axis_leaf_count;transaction->face_count=face_count;return 0;
}
static int closure_axisymmetric_transaction_capture(ClosureAxisymmetricTransaction * transaction,
    const ClosureAxisymmetricGeometry * geometry) {
  if(!transaction || !geometry || transaction->leaf_count!=axis_leaf_count || !transaction->state)return 1;
  scalar * variables=closure_axisymmetric_transaction_fields();int failures=0;
  foreach(serial) {
    unsigned long k=(unsigned long)leaf_index[];
    if(k>=transaction->leaf_count || leaf_index[]!=(double)k){failures++;continue;}
    int field=0;for(scalar s in variables)transaction->state[k*transaction->fields+field++]=s[];
    if(field!=transaction->fields)failures++;
  }
  free(variables);if(failures)return 2;
  unsigned long face=0;foreach_face(serial) {
    if(face<transaction->face_count)transaction->face_velocity[face++]=uf.x[];
    else failures++;
  }
  if(failures || face!=transaction->face_count)return 2;
  memcpy(transaction->geometry,geometry,axis_leaf_count*sizeof(*geometry));
  transaction->accepted_statistics=axis_statistics;transaction->accepted_flow_statistics=geometric_statistics;
  transaction->valid=1;return 0;
}
static int closure_axisymmetric_transaction_restore(ClosureAxisymmetricTransaction * transaction,
    ClosureAxisymmetricGeometry * geometry) {
  if(!transaction || !geometry || !transaction->valid || transaction->leaf_count!=axis_leaf_count)return 1;
  scalar * variables=closure_axisymmetric_transaction_fields();int failures=0;
  foreach(serial) {
    unsigned long k=(unsigned long)leaf_index[];
    if(k>=transaction->leaf_count || leaf_index[]!=(double)k){failures++;continue;}
    int field=0;for(scalar s in variables)s[]=transaction->state[k*transaction->fields+field++];
    if(field!=transaction->fields)failures++;
  }
  boundary(variables);free(variables);if(failures)return 2;
  unsigned long face=0;foreach_face(serial) {
    if(face<transaction->face_count)uf.x[]=transaction->face_velocity[face++];
    else failures++;
  }
  boundary((scalar *){uf});if(failures || face!=transaction->face_count)return 2;
  memcpy(geometry,transaction->geometry,axis_leaf_count*sizeof(*geometry));
  axis_statistics=transaction->accepted_statistics;geometric_statistics=transaction->accepted_flow_statistics;
  /* Invalidate optional numerical spinodal guesses. Restored physical/cache
   * fields are exact; a later authorized fresh attempt must rediscover these
   * disposable guesses rather than reusing a rejected trial's private path. */
  closure_coupled_phase_caches_free(axis_spinodal_caches);
  axis_spinodal_caches=closure_coupled_phase_caches_new(axis_leaf_count);
  return axis_spinodal_caches?0:3;
}
/* A separate read-only check runs after restoration. It checks every scalar
 * component against its saved object representation; no entropy/energy
 * residual or EOS inversion defines this exact restoration assertion. */
static int closure_axisymmetric_transaction_matches(const ClosureAxisymmetricTransaction * transaction,
    const ClosureAxisymmetricGeometry * geometry) {
  if(!transaction || !transaction->valid || !geometry || transaction->leaf_count!=axis_leaf_count)return 1;
  scalar * variables=closure_axisymmetric_transaction_fields();int failures=0;
  foreach(serial) {
    unsigned long k=(unsigned long)leaf_index[];int field=0;
    if(k>=transaction->leaf_count || leaf_index[]!=(double)k){failures++;continue;}
    for(scalar s in variables) {
      double actual=s[];
      if(memcmp(&actual,transaction->state+k*transaction->fields+field,sizeof(actual)))failures++;
      field++;
    }
    if(field!=transaction->fields)failures++;
  }
  free(variables);
  unsigned long face=0;foreach_face(serial) {
    double actual=uf.x[];
    if(face>=transaction->face_count || memcmp(&actual,transaction->face_velocity+face,sizeof(actual)))failures++;
    face++;
  }
  if(face!=transaction->face_count)failures++;
  if(memcmp(geometry,transaction->geometry,axis_leaf_count*sizeof(*geometry)) ||
     memcmp(&axis_statistics,&transaction->accepted_statistics,sizeof(axis_statistics)) ||
     memcmp(&geometric_statistics,&transaction->accepted_flow_statistics,sizeof(geometric_statistics)))failures++;
  return failures?2:0;
}
static void closure_axisymmetric_transaction_free(ClosureAxisymmetricTransaction * transaction) {
  if(!transaction)return;free(transaction->state);free(transaction->geometry);free(transaction->face_velocity);
  memset(transaction,0,sizeof(*transaction));
}
#endif
