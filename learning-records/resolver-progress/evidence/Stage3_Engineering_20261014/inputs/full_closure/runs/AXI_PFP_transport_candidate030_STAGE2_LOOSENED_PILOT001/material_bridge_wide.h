/* Separate optional long-double conservative representation, not adopted by
 * the geometric or physical-source production APIs. No default API change. */
#ifndef CLOSURE_MATERIAL_BRIDGE_WIDE_H
#define CLOSURE_MATERIAL_BRIDGE_WIDE_H
#include "material_bridge.h"
typedef struct {
  long double a_water,a_pfc,m_water,m_pfc,q_z,q_r,E_water,E_pfc;
  double xi;
} ClosureBridgeWideZone;
typedef struct {
  ClosureBridgeResult material;
  long double mechanical_entropy_density;
  long double paired_volume_roundoff,paired_energy_roundoff;
  long double authoritative_water_fraction,authoritative_pfc_fraction;
  long double relative_water_fraction_quantization,relative_pfc_fraction_quantization;
  int native_mechanical_status,legacy_entropy_conversion_underflow;
  /* mechanical_entropy_density is authoritative. The legacy double slot
   * is NAN when a positive source cannot survive binary64 conversion. */
} ClosureBridgeWideResult;
int closure_bridge_wide_equilibrate(ClosureBridgeWideZone *,ClosureBridgeCache *,ClosureBridgeWideResult *);
#endif
