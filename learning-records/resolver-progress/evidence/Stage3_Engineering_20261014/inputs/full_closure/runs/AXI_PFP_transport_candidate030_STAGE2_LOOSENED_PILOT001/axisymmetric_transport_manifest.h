/* Exact dyadic leaf-face ownership and retained-plane water overlap.
 * Uncompiled candidate. No fraction minimum, inferred min(aW) overlap,
 * rounded global interface endpoint or centred alpha is used.
 * The caller's tree IDs and geometric planes require separate acceptance.
 */
#ifndef CLOSURE_AXISYMMETRIC_TRANSPORT_MANIFEST_H
#define CLOSURE_AXISYMMETRIC_TRANSPORT_MANIFEST_H
#include "axisymmetric_transport_graph.h"
#include "scaled_plic_geometry.h"
typedef struct {
  int level,z_index,r_index; /* Exact nominal tree coordinates at own level. */
  double raw_small_normal_z,raw_small_normal_r;
  ClosureScaledPLIC geometry;
} ClosureAxisTransportLeaf;
typedef struct {
  int normal_axis,plane_index,lower_index,upper_index,node_lo,node_hi,face_bc;
  /* Endpoints are fine-grid integer anchors plus retained signed offsets.
   * They are never collapsed into a global coordinate for intersection. */
  int water_lower_anchor,water_upper_anchor;
  long double water_lower_offset,water_upper_offset;
  long double water_overlap_width_m;
} ClosureAxisTransportFaceGeometry;
typedef struct {
  int nodes,faces,finest_level;
  ClosureAxisTransportFace * face;
  ClosureAxisTransportFaceGeometry * geometry;
  long double axial_boundary_area_m2,radial_boundary_area_m2;
  unsigned long interior_faces,boundary_faces,positive_water_overlaps;
} ClosureAxisTransportManifest;
/* Output is zeroed/empty on refusal; owned buffers only on success. All actual
 * subfaces occur once. The physical domain is [0,L]z x [0,L]r. */
int closure_axis_transport_manifest_build(int count,const ClosureAxisTransportNode * nodes_in,
  const ClosureAxisTransportLeaf * leaves_in,double length_m,int finest_level,
  ClosureAxisTransportManifest *);
void closure_axis_transport_manifest_free(ClosureAxisTransportManifest *);
#endif
