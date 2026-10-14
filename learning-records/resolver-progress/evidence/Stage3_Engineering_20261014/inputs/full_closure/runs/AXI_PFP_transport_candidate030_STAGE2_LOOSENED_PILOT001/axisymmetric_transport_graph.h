/* Parser-neutral physical transport on an actual leaf/face manifest.
 * Masses/energies/momenta are PHYSICAL EXTENSIVES, with the2pi metric.
 * Caller must supply every actual paired interior face/subface once, exact
 * water/water intersection area and positive centroid-face distance. No
 * temperature/area/fraction floor is accepted. Geometry uncertainty refuses.
 * TS01--TS08 constitutive laws are unchanged. Runtime verification pending.
 */
#ifndef CLOSURE_AXISYMMETRIC_TRANSPORT_GRAPH_H
#define CLOSURE_AXISYMMETRIC_TRANSPORT_GRAPH_H
typedef struct {
  double z_m,r_m,Delta_m,volume_m3;
  long double a_water,a_PFC;
  long double m_water_kg,m_PFC_kg,q_z_kg_m_s,q_r_kg_m_s,E_water_J,E_PFC_J;
  double T_water_K,T_PFC_K,cv_water_J_kg_K,mu_water_Pa_s,mu_PFC_Pa_s;
} ClosureAxisTransportNode;
enum {CLOSURE_AXIS_TRANSPORT_INTERIOR=0,CLOSURE_AXIS_TRANSPORT_NO_SLIP=1,
  CLOSURE_AXIS_TRANSPORT_AXIS=2,CLOSURE_AXIS_TRANSPORT_FREE_SLIP=3};
typedef struct {
  int node_lo,node_hi,normal_axis,face_bc;
  double z_m,r_m;
  long double area_m2,normal_distance_m;
  long double water_overlap_area_m2,water_centroid_distance_m;
} ClosureAxisTransportFace;
typedef struct {
  long double viscous_entropy_J_K,Fourier_entropy_J_K;
  long double viscous_energy_boundary_out_J,Fourier_energy_boundary_out_J;
  long double paired_energy_roundoff_J,paired_momentum_roundoff_kg_m_s;
  long double viscous_intrinsic_work_defect_J,Fourier_linear_solve_energy_defect_J;
  long double Fourier_endpoint_entropy_change_J_K,Fourier_time_entropy_defect_J_K;
  long double minimum_viscous_intrinsic_increment_J,maximum_viscous_force_N;
  double maximum_temperature_iteration_change_K;
  unsigned long face_count,water_edge_count,Fourier_iterations;
  int status;
} ClosureAxisTransportStats;
/* Transactional: input immutable and output byte unchanged on every failure.
 * No private automatic retry. Explicit viscosity needs actual timestep/grid
 * convergence. Fourier BE is a positive finite network solve; its physical
 * entropy integral uses the final sampled gradient and requires time-error
 * assessment, rather than being defined from endpoint entropy change. */
int closure_axis_transport_viscous(int nodes,const ClosureAxisTransportNode * input,
  int faces,const ClosureAxisTransportFace * face_table,double interval_s,ClosureAxisTransportNode * output,
  ClosureAxisTransportStats *);
int closure_axis_transport_water_Fourier(int nodes,const ClosureAxisTransportNode * input,
  int faces,const ClosureAxisTransportFace * face_table,double interval_s,double temperature_tolerance_K,
  double relative_energy_tolerance,int maximum_iterations,ClosureAxisTransportNode * output,
  ClosureAxisTransportStats *);
#endif
