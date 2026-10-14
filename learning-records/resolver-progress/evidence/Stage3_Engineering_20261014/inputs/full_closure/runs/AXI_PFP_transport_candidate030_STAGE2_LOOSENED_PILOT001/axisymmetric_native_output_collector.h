/* Native caller adapter to ROOT's held ordinary-C writer. Source-only draft.
 * Include after the AXI core and read-only snapshot header. Never calculate
 * a source/flux by subtracting physical ledgers; missing hooks stay unknown.
 */
#ifndef CLOSURE_AXISYMMETRIC_NATIVE_OUTPUT_COLLECTOR_H
#define CLOSURE_AXISYMMETRIC_NATIVE_OUTPUT_COLLECTOR_H
#include "coupled_raw_output.h"
#include "axisymmetric_transport_manifest.h"
#include <float.h>
static int closure_axis_raw_emit_fields(FILE * stream,double time,const char * stage,
    ClosureAxisSnapshotCell * properties) {
  if(!stream || !stage || !properties || closure_axis_snapshot_properties(properties))return 1;
  int failures=0;
  foreach(serial) {
    int k=(int)leaf_index[];const ClosureAxisSnapshotCell * state=properties+k;
    double V=closure_axisymmetric_physical_volume(point),rho=M_water[]+M_PFC[];
    ClosureRawLeaf row={.time=time,.z=x,.r=y,.delta=Delta,.volume=V,
      .uz=q.x[]/rho,.ur=q.y[]/rho,.xi=M_PFC[]>0.?Z_PFC[]/M_PFC[]:0.,
      .iz=(uint64_t)(point.i-2),.ir=(uint64_t)(point.j-2),.level=level,.stage=stage};
    if(state->water_present)row.water=(ClosureRawMaterial){(long double)M_water[]*V,
      (long double)E_water[]*V,a_water[],state->water.rho,state->water.e,
      state->water.s,state->water.T,state->water.p,1};
    if(state->PFC_present)row.pfc=(ClosureRawMaterial){(long double)M_PFC[]*V,
      (long double)E_PFC[]*V,f_PFC[],state->pfc.rho,state->pfc.e,
      state->pfc.s,state->pfc.T,state->pfc.p,1};
    row.rho_liquid=state->caloric_cache.rho_liquid;row.rho_vapour=state->caloric_cache.rho_vapour;
    row.liquid_available=state->PFC_present && state->caloric_cache.liquid_valid;
    row.vapour_available=state->PFC_present && state->caloric_cache.vapour_valid;
    int status=closure_raw_field(stream,&row);
    if(status){fprintf(stderr,"AXI canonical field emission refusal leaf=%d status=%d stage=%s\n",k,status,stage);failures++;}
  }
  if(fflush(stream) || ferror(stream))failures++;return failures?2:0;
}
/* These wrappers deliberately require the complete measured masks supplied
 * by the actual operators. They cannot invent a zero for the absent shock or
 * unfinished transport/advection boundary collector. */
static int closure_axis_raw_emit_known_source(FILE * stream,const ClosureRawSource * source) {
  if(!source || source->measured_mask!=CLOSURE_RAW_SOURCE_FULL_MASK)return 1;
  return closure_raw_source(stream,source);
}
static int closure_axis_raw_emit_known_boundary(FILE * stream,const ClosureRawBoundary * boundary) {
  if(!boundary || boundary->measured_mask!=CLOSURE_RAW_BOUNDARY_FULL_MASK)return 1;
  return closure_raw_boundary(stream,boundary);
}
/* Geometry diagnostics retain the structured represented plane independently
 * of every raw field. Caller binds this file to the same complete raw frame
 * fingerprint/nominal inventory/source hashes, before observer adoption. */
static int closure_axis_structured_geometry_header(FILE * stream) {
  if(!stream)return 1;
  fprintf(stream,"stage,time_s,steps,leaf_id,level,iz,ir,z_lower_m,r_lower_m,Delta_m,aW,aF,mW_kg,mF_kg,small_material,raw_small_nz,raw_small_nr,status,has_interface,sign_z,sign_r,preferred_z_m,preferred_r_m,a,b,offset,normal_length,water_vertices,PFC_vertices,segment_X1,segment_Y1,segment_X2,segment_Y2,cell_volume_m3,water_raw_volume_m3,PFC_raw_volume_m3,water_polygon_volume_m3,PFC_polygon_volume_m3,water_volume_defect_m3,PFC_volume_defect_m3,area_m2,distance_water_m,water_conductance_W_K,water_centroid_local_X,water_centroid_local_Y,rounded_primary_complement,rounded_global_endpoints_equal,LD_mantissa_bits,LD_decimal_digits");
  for(int material=0;material<2;material++)for(int vertex=0;vertex<6;vertex++)
    fprintf(stream,",%s%d_X,%s%d_Y,%s%d_h",material?"F":"W",vertex,material?"F":"W",vertex,material?"F":"W",vertex);
  return fputc('\n',stream)==EOF || ferror(stream);
}
static int closure_axis_structured_geometry_rows(FILE * stream,const char * stage,double time,int steps,
    const ClosureAxisTransportNode * node,const ClosureAxisTransportLeaf * leaf,int count) {
  if(!stream || !stage || !node || !leaf || count<1)return 1;
#ifdef LDBL_DECIMAL_DIG
  int digits=LDBL_DECIMAL_DIG;
#else
  int digits=DECIMAL_DIG;
#endif
  for(int k=0;k<count;k++) {
    const ClosureAxisTransportNode * n=node+k;const ClosureAxisTransportLeaf * l=leaf+k;
    const ClosureScaledPLIC * g=&l->geometry;
    fprintf(stream,"%s,%.17g,%d,%d,%d,%d,%d,%.17g,%.17g,%.17g,%.*Lg,%.*Lg,%.*Lg,%.*Lg,%d,%.17g,%.17g,%d,%d,%d,%d",
      stage,time,steps,k,l->level,l->z_index,l->r_index,n->z_m-n->Delta_m/2.,n->r_m-n->Delta_m/2.,n->Delta_m,
      digits,n->a_water,digits,n->a_PFC,digits,n->m_water_kg,digits,n->m_PFC_kg,g->small_material,
      l->raw_small_normal_z,l->raw_small_normal_r,g->status,g->has_interface,g->sign_z,g->sign_r);
    const long double first[]={g->preferred_z_m,g->preferred_r_m,g->a,g->b,g->offset,g->normal_length};
    for(int j=0;j<6;j++)fprintf(stream,",%.*Lg",digits,first[j]);
    fprintf(stream,",%d,%d",g->water_vertices,g->PFC_vertices);
    const long double second[]={g->segment_X1,g->segment_Y1,g->segment_X2,g->segment_Y2,
      g->cell_volume_m3,g->water_raw_volume_m3,g->PFC_raw_volume_m3,g->water_geometry_volume_m3,
      g->PFC_geometry_volume_m3,g->water_geometry_volume_defect_m3,g->PFC_geometry_volume_defect_m3,
      g->area_m2,g->distance_water_m,g->water_conductance_W_K,g->water_centroid_local_X,g->water_centroid_local_Y};
    for(int j=0;j<16;j++)fprintf(stream,",%.*Lg",digits,second[j]);
    fprintf(stream,",%d,%d,%d,%d",g->rounded_primary_complement,g->rounded_global_endpoints_equal,LDBL_MANT_DIG,digits);
    for(int material=0;material<2;material++)for(int vertex=0;vertex<6;vertex++) {
      const ClosureScaledPLICVertex * v=material?g->PFC+vertex:g->water+vertex;
      fprintf(stream,",%.*Lg,%.*Lg,%.*Lg",digits,v->X,digits,v->Y,digits,v->h);
    }
    if(fputc('\n',stream)==EOF || ferror(stream))return 2;
  }
  return fflush(stream) || ferror(stream)?2:0;
}
#endif
