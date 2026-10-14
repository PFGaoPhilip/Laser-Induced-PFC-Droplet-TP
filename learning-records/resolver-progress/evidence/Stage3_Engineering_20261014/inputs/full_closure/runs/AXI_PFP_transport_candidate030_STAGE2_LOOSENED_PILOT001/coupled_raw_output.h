/* Original ordinary-C emission contract for the coupled axisymmetric solver.
 * This writer does not calculate or infer any physical flux/source. */
#ifndef CLOSURE_COUPLED_RAW_OUTPUT_H
#define CLOSURE_COUPLED_RAW_OUTPUT_H
#include <stdint.h>
#include <stdio.h>

typedef struct {
  /* Extensive physical mass [kg] and raw conserved TOTAL material energy [J],
   * including that material's assigned full-vector kinetic energy. The e
   * below is the independently reconstructed specific INTERNAL EOS energy
   * [J/kg]. Neither quantity replaces the other in a conservation audit. */
  long double mass,energy;
  double fraction,rho,e,s,T,p;
  int present;
} ClosureRawMaterial;

typedef struct {
  double time,z,r,delta,volume,uz,ur,xi;
  uint64_t iz,ir;
  unsigned level;
  const char *stage;
  ClosureRawMaterial water,pfc;
  double rho_liquid,rho_vapour;
  int liquid_available,vapour_available;
} ClosureRawLeaf;

enum { CLOSURE_RAW_BOUNDARY_COLUMNS=13,CLOSURE_RAW_SOURCE_COLUMNS=7 };
#define CLOSURE_RAW_BOUNDARY_FULL_MASK ((UINT32_C(1)<<13)-1)
#define CLOSURE_RAW_SOURCE_FULL_MASK ((UINT32_C(1)<<7)-1)

typedef struct {
  double start,end,z,r,nz,nr,area;
  const char *stage,*face_id;
  /* Exact order is the public CSV header below. Outward increments signed. */
  long double increments[CLOSURE_RAW_BOUNDARY_COLUMNS];
  uint32_t measured_mask;
} ClosureRawBoundary;

typedef struct {
  double start,end;
  const char *stage,*source_id;
  /* phase HKS, phase bulk, mechanical, interface heat, water Fourier,
   * viscosity, shock jump. Numerical defects are never substituted here. */
  long double increments[CLOSURE_RAW_SOURCE_COLUMNS];
  uint32_t measured_mask;
} ClosureRawSource;

typedef struct {
  double time,area,volume;
  const char *stage;
  long double capillary_work,pressure_work;
  double area_advection,area_mechanical,area_reaction,area_heat,area_amr;
} ClosureRawGeometry;

typedef struct {
  double time,r_inner,r_outer,p_water,tau_zz;
  int water_present,film_resolved;
} ClosureRawWall;

/* All row routines validate before writing. Missing measurements are errors,
 * not implicit zero. Status0 means emission success only, not a physical gate. */
int closure_raw_field_header(FILE *);
int closure_raw_boundary_header(FILE *);
int closure_raw_source_header(FILE *);
int closure_raw_geometry_header(FILE *);
int closure_raw_wall_header(FILE *);
int closure_raw_field(FILE *,const ClosureRawLeaf *);
int closure_raw_boundary(FILE *,const ClosureRawBoundary *);
int closure_raw_source(FILE *,const ClosureRawSource *);
int closure_raw_geometry(FILE *,const ClosureRawGeometry *);
int closure_raw_wall(FILE *,const ClosureRawWall *);
#endif
