/* Separate preferred-corner/fraction-normal PLIC candidate.
 * Original geometry002 is held unchanged. Definitions: SG01--05.
 * Global endpoints are diagnostics; local offset/vertices define the plane. */
#ifndef CLOSURE_SCALED_PLIC_GEOMETRY_H
#define CLOSURE_SCALED_PLIC_GEOMETRY_H
typedef struct {
  double z_lower_m,r_lower_m,Delta_m;
  double small_normal_z,small_normal_r;
  double a_water,a_pfc;
  long double m_water_kg,m_pfc_kg;
  double water_conductivity_W_m_K;
  int small_material; /* 0=PFC, 1=water, on n.X <= retained offset */
} ClosureScaledPLICInput;
typedef struct {long double X,Y,h;} ClosureScaledPLICVertex;
typedef struct {
  long double cell_volume_m3,water_raw_volume_m3,PFC_raw_volume_m3;
  long double water_geometry_volume_m3,PFC_geometry_volume_m3;
  long double water_geometry_volume_defect_m3,PFC_geometry_volume_defect_m3;
  long double water_meridional_fraction,PFC_meridional_fraction;
  long double preferred_z_m,preferred_r_m,offset,a,b,normal_length;
  long double segment_X1,segment_Y1,segment_X2,segment_Y2;
  long double segment_length_m,area_m2,distance_water_m,water_conductance_W_K;
  long double water_centroid_local_X,water_centroid_local_Y;
  long double water_centroid_z_m,water_centroid_r_m;
  long double z1_m,r1_m,z2_m,r2_m;
  long double small_fraction_reconstruction_relative_error,raw_paired_fraction_defect;
  int sign_z,sign_r,small_material,has_interface,branch;
  int rounded_primary_complement,rounded_global_endpoints_equal;
  int water_vertices,PFC_vertices,status;
  ClosureScaledPLICVertex water[6],PFC[6];
} ClosureScaledPLIC;
enum { CLOSURE_SCALED_PLIC_OK=0,CLOSURE_SCALED_PLIC_INVALID_INPUT=1,
  CLOSURE_SCALED_PLIC_UNRESOLVED=2,CLOSURE_SCALED_PLIC_NONFINITE=3,
  CLOSURE_SCALED_PLIC_LOST_POSITIVE=4 };
int closure_scaled_plic_geometry(const ClosureScaledPLICInput *,ClosureScaledPLIC *);
/* Geometry conversion only; raw mass/EOS/source-state guards are separate.
 * Refusal never permits omitting a tiny positive material or patch. */
int closure_scaled_plic_binary64_geometry_representable(const ClosureScaledPLIC *);
#endif
