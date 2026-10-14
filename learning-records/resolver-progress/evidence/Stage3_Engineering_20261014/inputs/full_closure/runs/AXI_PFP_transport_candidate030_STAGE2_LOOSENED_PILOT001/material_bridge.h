/* Small, parser-neutral public API. Thermodynamic/source implementations are
 * compiled as ordinary C, while the geometric flow driver uses this header. */
#ifndef CLOSURE_MATERIAL_BRIDGE_H
#define CLOSURE_MATERIAL_BRIDGE_H
typedef struct {
  double a_water,a_pfc,m_water,m_pfc,q_z,q_r,E_water,E_pfc,xi;
} ClosureBridgeZone;
typedef struct {
  double rho_liquid,rho_vapour,p_pfc,T_pfc;
  int liquid_valid,vapour_valid;
} ClosureBridgeCache;
typedef struct {
  double p,T_water,T_pfc,s_water,s_pfc,c_water2,c_pfc2;
  double wood_modulus,thermal_response,mechanical_entropy;
  unsigned long raw_queries,inverse_iterations,inverse_fallbacks;
  unsigned long phase_local_queries,phase_global_queries;
} ClosureBridgeResult;
typedef struct {
  double rho,e,s,p,T,c2,p_e,p_rho,cv;
} ClosureBridgeMaterial;
int closure_bridge_setup(const char * species,const char * water_table);
void closure_bridge_cleanup(void);
int closure_bridge_water_initial(ClosureBridgeMaterial * result);
int closure_bridge_water_rho_T(double rho,double T,ClosureBridgeMaterial * result);
int closure_bridge_water_rho_e(double rho,double e,ClosureBridgeMaterial * result);
int closure_bridge_pfc_PT(double p,double T,double xi,
  ClosureBridgeCache * cache,ClosureBridgeMaterial * result);
int closure_bridge_pfc_rho_e(double rho,double e,double xi,
  ClosureBridgeCache * cache,ClosureBridgeMaterial * result);
/* Transactional fixed-rho/xi caloric query. Nonzero means explicit root,
 * stability or sampled connected-path failure; no cache is committed then.
 * This EOS callback does not replace the additional selected reaction-domain
 * guards, which the production heat/source adapter must enforce. */
int closure_bridge_pfc_rho_T(double rho,double T,double xi,
  ClosureBridgeCache * cache,ClosureBridgeMaterial * result);
int closure_bridge_equilibrate(ClosureBridgeZone * zone,
  ClosureBridgeCache * cache,ClosureBridgeResult * result);
#endif
