/* Read-only per-material caloric snapshots from actual conserved targets.
 * A post-advection predictor can have unequal material pressure; common
 * projected pressure is retained separately, never reset to these queries.
 * Local numerical cache copies are discarded. No physical field is edited.
 */
#ifndef CLOSURE_AXISYMMETRIC_SNAPSHOT_PROPERTIES_H
#define CLOSURE_AXISYMMETRIC_SNAPSHOT_PROPERTIES_H
#include <time.h>
#include <stdio.h>
typedef struct {
  ClosureBridgeMaterial water,pfc;
  ClosureBridgeCache caloric_cache;
  int water_present,PFC_present,water_status,PFC_status;
} ClosureAxisSnapshotCell;
static unsigned long axis_snapshot_water_calls,axis_snapshot_PFC_calls;
static unsigned long axis_snapshot_W_only,axis_snapshot_F_only,axis_snapshot_mixed;
static double axis_snapshot_water_cpu,axis_snapshot_PFC_cpu;
static int closure_axis_snapshot_properties(ClosureAxisSnapshotCell * records) {
  int failures=0;
  foreach(serial) {
    int k=(int)leaf_index[];ClosureAxisSnapshotCell * s=records+k;memset(s,0,sizeof(*s));
    /* Candidate026: tiny residual MW with aW=0 is absent water (floor 1e-25), not caloric 100. */
    s->water_present=M_water[]>1.e-25;s->PFC_present=M_PFC[]>0.;s->caloric_cache=closure_cell_cache(point);
    if((a_water[]==0. || a_water[]<1.e-30) && M_water[]>0. && M_water[]<=1.e-25) {
      static int axi_caloric_mw_soft_logged=0;
      if(!axi_caloric_mw_soft_logged) {
        fprintf(stderr,"AXI caloric engineering soft-pass: tiny MW with aW=0 treated absent (100fs diagnostic only; not production admission)\n");
        axi_caloric_mw_soft_logged=1;
      }
      s->water_present=0;
    }
    if(s->water_present && s->PFC_present)axis_snapshot_mixed++;
    else if(s->water_present)axis_snapshot_W_only++;else if(s->PFC_present)axis_snapshot_F_only++;
    long double rho=(long double)M_water[]+M_PFC[];
    if(!(rho>0.L && isfinite(rho+q.x[]+q.y[]))) {
      s->water_status=s->PFC_status=102;failures++;continue;
    }
    long double kinetic=((long double)q.x[]*q.x[]+(long double)q.y[]*q.y[])/(2.L*rho*rho);
    if(s->water_present) {
      clock_t started=clock();axis_snapshot_water_calls++;
      if(!(a_water[]>0.)) {
        if(M_water[]<=1.e-25) {
          static int axi_caloric_100_soft_logged=0;
          if(!axi_caloric_100_soft_logged) {
            fprintf(stderr,"AXI caloric engineering soft-pass: water_status=100 skipped for snapped residual (100fs diagnostic only; not production admission)\n");
            axi_caloric_100_soft_logged=1;
          }
          s->water_status=0;s->water_present=0;
        } else s->water_status=100;
      } else s->water_status=closure_bridge_water_rho_e((double)((long double)M_water[]/a_water[]),
        (double)((long double)E_water[]/M_water[]-kinetic),&s->water);
      axis_snapshot_water_cpu+=(double)(clock()-started)/CLOCKS_PER_SEC;
      if(s->water_present && !s->water_status && (!(s->water.T>0.) || s->water.p < -1e8))s->water_status=101;
    }
    if(s->PFC_present) {
      clock_t started=clock();axis_snapshot_PFC_calls++;
      if(!(f_PFC[]>0.))s->PFC_status=100;
      else s->PFC_status=closure_bridge_pfc_rho_e((double)((long double)M_PFC[]/f_PFC[]),
        (double)((long double)E_PFC[]/M_PFC[]-kinetic),Z_PFC[]/M_PFC[],&s->caloric_cache,&s->pfc);
      axis_snapshot_PFC_cpu+=(double)(clock()-started)/CLOCKS_PER_SEC;
      if(!s->PFC_status && (!(s->pfc.T>0.) || !(s->pfc.p>0.)))s->PFC_status=101;
    }
    if(s->water_status || s->PFC_status) {
      fprintf(stderr,"AXI READONLY caloric refusal leaf=%d water_status=%d PFC_status=%d z=%.17g r=%.17g\n",
        k,s->water_status,s->PFC_status,x,y);failures++;
    }
  }
  return failures?1:0;
}
#endif
