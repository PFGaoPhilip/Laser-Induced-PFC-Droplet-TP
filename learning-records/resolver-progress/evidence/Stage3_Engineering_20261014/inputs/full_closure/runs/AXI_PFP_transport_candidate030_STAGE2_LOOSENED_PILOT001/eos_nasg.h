/* Thermodynamically complete pure-phase NASG functions.
 * Sources: Le Metayer & Saurel, Phys Fluids 28,046102 (2016),
 * doi:10.1063/1.4945981; Radulescu arXiv:2004.08750 Eqs 1,2,9,11.
 * Symbols: gamma=Cp/Cv, Pi stiffening pressure [Pa], b covolume [m3/kg],
 * cv heat capacity [J/(kg K)], q reference internal energy [J/kg].
 * No input-domain clipping is performed; invalid states produce NAN.
 */
#ifndef CLOSURE_EOS_NASG_H
#define CLOSURE_EOS_NASG_H
#include <math.h>
typedef struct { double gamma, Pi, b, cv, q; } ClosureNASG;

static inline int nasg_valid_density (ClosureNASG eos, double rho) {
  return rho > 0. && eos.gamma > 1. && eos.cv > 0.
    && 1. - eos.b*rho > 0.;
}
static inline double nasg_p (ClosureNASG eos, double rho, double e) {
  if (!nasg_valid_density(eos, rho)) return NAN;
  return (eos.gamma - 1.)*rho*(e - eos.q)/(1. - eos.b*rho)
    - eos.gamma*eos.Pi;
}
static inline double nasg_e_p (ClosureNASG eos, double rho, double p) {
  if (!nasg_valid_density(eos, rho) || p + eos.Pi <= 0.) return NAN;
  return (p + eos.gamma*eos.Pi)*(1./rho - eos.b)/(eos.gamma - 1.)
    + eos.q;
}
static inline double nasg_T (ClosureNASG eos, double rho, double p) {
  if (!nasg_valid_density(eos, rho) || p + eos.Pi <= 0.) return NAN;
  return (p + eos.Pi)*(1./rho - eos.b)/((eos.gamma - 1.)*eos.cv);
}
static inline double nasg_rho_pT (ClosureNASG eos, double p, double T) {
  if (eos.gamma <= 1. || eos.cv <= 0. || T <= 0. || p + eos.Pi <= 0.)
    return NAN;
  return 1./(eos.b + (eos.gamma - 1.)*eos.cv*T/(p + eos.Pi));
}
static inline double nasg_c2 (ClosureNASG eos, double rho, double p) {
  if (!nasg_valid_density(eos, rho) || p + eos.Pi <= 0.) return NAN;
  return eos.gamma*(p + eos.Pi)/(rho*(1. - eos.b*rho));
}
static inline double nasg_s_relative (ClosureNASG eos, double rho, double T,
                                      double rho_ref, double T_ref) {
  if (!nasg_valid_density(eos, rho) || !nasg_valid_density(eos, rho_ref)
      || T <= 0. || T_ref <= 0.) return NAN;
  return eos.cv*log(T/T_ref) + (eos.gamma - 1.)*eos.cv*
    log((1./rho - eos.b)/(1./rho_ref - eos.b));
}
#endif
