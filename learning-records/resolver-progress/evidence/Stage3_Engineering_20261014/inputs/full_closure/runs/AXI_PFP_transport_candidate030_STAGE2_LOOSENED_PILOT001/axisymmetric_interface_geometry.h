/* Parser-neutral API for actual single-PLIC outer-interface geometry.
 * Formula/convention reference: verification/THERMAL_GEOMETRY_CONVENTION.md.
 * No mass, fraction, EOS state or conductance distance is repaired here.
 * Caller retains every positive conservative material in the full ledger
 * even when this geometry query refuses a represented interface. */
#ifndef CLOSURE_AXISYMMETRIC_INTERFACE_GEOMETRY_H
#define CLOSURE_AXISYMMETRIC_INTERFACE_GEOMETRY_H
typedef struct {
  double z_m,r_m,Delta_m;
  double n_z,n_r,alpha; /* PFC: n_z*x+n_r*y <= alpha, local unit square */
  double a_pfc,a_water,m_pfc_kg,m_water_kg;
  double water_conductivity_W_m_K;
} ClosureAxisymmetricGeometryInput;
typedef struct {
  double cell_volume_m3,PFC_raw_volume_m3,water_raw_volume_m3;
  double PFC_geometry_volume_m3,water_geometry_volume_m3;
  double water_geometry_volume_defect_m3,PFC_geometry_volume_defect_m3;
  double water_meridional_fraction,PFC_meridional_fraction;
  double z1_m,r1_m,z2_m,r2_m,area_m2;
  double water_centroid_z_m,water_centroid_r_m;
  double water_centroid_local_x,water_centroid_local_y;
  double distance_water_m,water_conductance_W_K;
  double single_PLIC_area_upper_m2,plane_endpoint_residual;
  double raw_paired_fraction_defect;
  int has_interface,water_polygon_vertices,PFC_polygon_vertices;
  int positive_water_mass,positive_PFC_mass,rounded_primary_complement;
  int status;
} ClosureAxisymmetricGeometry;
enum {
  CLOSURE_GEOMETRY_OK=0,CLOSURE_GEOMETRY_INVALID_INPUT=1,
  CLOSURE_GEOMETRY_UNRESOLVED_INTERFACE=2,CLOSURE_GEOMETRY_INVALID_POLYGON=3,
  CLOSURE_GEOMETRY_INVALID_DISTANCE=4,CLOSURE_GEOMETRY_NONFINITE_OUTPUT=5
};
/* Output diagnostics always describe the query. A nonzero result is explicit
 * geometry uncertainty/refusal, never a declaration of absent material. */
int closure_axisymmetric_interface_geometry(const ClosureAxisymmetricGeometryInput *,
  ClosureAxisymmetricGeometry *);
#endif
