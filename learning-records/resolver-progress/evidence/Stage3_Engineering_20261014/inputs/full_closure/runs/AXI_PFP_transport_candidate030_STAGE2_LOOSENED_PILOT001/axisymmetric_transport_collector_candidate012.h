/* Actual fixed-tree collector for the separate transport candidate. Include
 * after axisymmetric_coupled_core.h and snapshot_properties.h. Uncompiled,
 * unadopted. Uses the independently stored smaller material's reconstruction
 * normal; retains its preferred-corner plane and all local polygon vertices.
 */
#ifndef CLOSURE_AXISYMMETRIC_TRANSPORT_COLLECTOR_CANDIDATE011_H
#define CLOSURE_AXISYMMETRIC_TRANSPORT_COLLECTOR_CANDIDATE011_H
#include "axisymmetric_transport_manifest.h"
#include <float.h>
static int closure_axis_transport_PFC_viscosity(const ClosureAxisSnapshotCell * state,
    double xi,double critical,double * viscosity) {
  if(!state || !viscosity || !(critical>0.) || !(xi>=0. && xi<=1.) ||
     !(state->pfc.T>0. && state->pfc.rho>0.))return 1;
  if(state->pfc.T>=critical){*viscosity=.0001;return 0;}
  long double phi=0.L;
  if(xi>0.) {
    if(!state->caloric_cache.vapour_valid || !(state->caloric_cache.rho_vapour>0.))return 2;
    phi=(long double)state->pfc.rho*xi/state->caloric_cache.rho_vapour;
  }
  if(!(phi>=0.L && phi<=1.L && isfinite(phi)))return 3;
  long double y=(critical-state->pfc.T)/(.02L*critical);
  long double b=y>=1.L?1.L:3.L*y*y-2.L*y*y*y;
  long double mu=.0001L+b*((1.L-phi)*.001L+phi*.00001L-.0001L);
  if(!(mu>0.L && isfinite(mu)))return 4;*viscosity=(double)mu;return 0;
}
static int closure_axis_transport_collect(ClosureAxisTransportNode * node,
    ClosureAxisTransportLeaf * leaf,ClosureAxisSnapshotCell * properties) {
  if(!node || !leaf || !properties || closure_axis_snapshot_properties(properties))return 1;
  vector normalF[],normalW[];scalar alphaF[],alphaW[];
  reconstruction(f_PFC,normalF,alphaF);reconstruction(a_water,normalW,alphaW);
  int failures=0;
  foreach(serial) {
    int k=(int)leaf_index[],small_water=a_water[]<f_PFC[];
    const ClosureAxisSnapshotCell * s=properties+k;
    double volume=closure_axisymmetric_physical_volume(point),muF=0.;
    if(s->PFC_present && closure_axis_transport_PFC_viscosity(s,Z_PFC[]/M_PFC[],
        axis_critical_temperature,&muF)){failures++;continue;}
    node[k]=(ClosureAxisTransportNode){.z_m=x,.r_m=y,.Delta_m=Delta,.volume_m3=volume,
      .a_water=a_water[],.a_PFC=f_PFC[],.m_water_kg=(long double)M_water[]*volume,
      .m_PFC_kg=(long double)M_PFC[]*volume,.q_z_kg_m_s=(long double)q.x[]*volume,
      .q_r_kg_m_s=(long double)q.y[]*volume,.E_water_J=(long double)E_water[]*volume,
      .E_PFC_J=(long double)E_PFC[]*volume,.T_water_K=s->water.T,.T_PFC_K=s->pfc.T,
      .cv_water_J_kg_K=s->water.cv,.mu_water_Pa_s=.001,.mu_PFC_Pa_s=muF};
    leaf[k].level=level;leaf[k].z_index=point.i-2;leaf[k].r_index=point.j-2;
    leaf[k].raw_small_normal_z=small_water?normalW.x[]:normalF.x[];
    leaf[k].raw_small_normal_r=small_water?normalW.y[]:normalF.y[];
    ClosureScaledPLICInput geometry={x-Delta/2.,y-Delta/2.,Delta,
      leaf[k].raw_small_normal_z,leaf[k].raw_small_normal_r,
      a_water[],f_PFC[],node[k].m_water_kg,node[k].m_PFC_kg,.598,small_water};
    int status=closure_scaled_plic_geometry(&geometry,&leaf[k].geometry);
    if(status) {
      fprintf(stderr,"AXI transport geometry refusal leaf=%d status=%d raw_aW=%.17g raw_aF=%.17g\n",
        k,status,a_water[],f_PFC[]);failures++;
    }
  }
  return failures?2:0;
}
/* This conversion guard is a source-domain guard, distinct from geometry's
 * optional binary64 geometry conversion flag. No positive extensive momentum
 * or energy may silently become zero. Error records remain independent. */
static int closure_axis_transport_density_conversion(long double extensive,double volume,double * density,
    long double * defect) {
  if(!(volume>0. && isfinite(volume)) || !isfinite(extensive))return 1;
  long double value=extensive/volume;double rounded=(double)value;
  if(!isfinite(rounded) || (value!=0.L && rounded==0.))return 2;
  *density=rounded;*defect=(long double)rounded*volume-extensive;return 0;
}
typedef struct {
  long double converted_energy_roundoff_J,converted_momentum_roundoff_kg_m_s;
  ClosureAxisTransportStats physical;
} ClosureAxisTransportCommitStats;
/* Separate source half-step. A caller-provided whole macrostep transaction
 * must restore on any refused post-source equilibration or geometry. */
static int closure_axis_transport_source(double interval,double length,int finest,int viscosity,
    ClosureAxisSnapshotCell * properties,ClosureAxisTransportCommitStats * report) {
  if(!report || !(interval>=0.) || (viscosity!=0 && viscosity!=1))return 1;
  memset(report,0,sizeof(*report));
  ClosureAxisTransportNode * input=calloc(axis_leaf_count,sizeof(*input));
  ClosureAxisTransportNode * output=calloc(axis_leaf_count,sizeof(*output));
  ClosureAxisTransportLeaf * leaf=calloc(axis_leaf_count,sizeof(*leaf));
  double (*converted)[4]=calloc(axis_leaf_count,sizeof(*converted));
  ClosureAxisTransportManifest manifest={0};int status=0;
  if(!input || !output || !leaf || !converted){status=2;goto end;}
  if(closure_axis_transport_collect(input,leaf,properties)){status=3;goto end;}
  if(closure_axis_transport_manifest_build(axis_leaf_count,input,leaf,length,finest,&manifest)){status=4;goto end;}
  status=viscosity?closure_axis_transport_viscous(axis_leaf_count,input,manifest.faces,manifest.face,interval,
    output,&report->physical):closure_axis_transport_water_Fourier(axis_leaf_count,input,
    manifest.faces,manifest.face,interval,1e-10,1e-13,10000,output,&report->physical);
  if(status){fprintf(stderr,"AXI transport operator refusal viscosity=%d status=%d\n",viscosity,status);status=5;goto end;}
  for(unsigned long k=0;k<axis_leaf_count;k++) {
    long double values[4]={output[k].q_z_kg_m_s,output[k].q_r_kg_m_s,output[k].E_water_J,output[k].E_PFC_J};
    for(int j=0;j<4;j++) {
      long double defect;
      if(closure_axis_transport_density_conversion(values[j],input[k].volume_m3,&converted[k][j],&defect)){status=6;goto end;}
      if(j<2)report->converted_momentum_roundoff_kg_m_s+=fabsl(defect);
      else report->converted_energy_roundoff_J+=defect;
    }
  }
  foreach(serial) {
    int k=(int)leaf_index[];q.x[]=converted[k][0];q.y[]=converted[k][1];
    E_water[]=converted[k][2];E_PFC[]=converted[k][3];
  }
  boundary({q,E_water,E_PFC});
  if(closure_axisymmetric_relax_after_local_source())status=7;
end:
  closure_axis_transport_manifest_free(&manifest);free(input);free(output);free(leaf);free(converted);return status;
}
#endif
