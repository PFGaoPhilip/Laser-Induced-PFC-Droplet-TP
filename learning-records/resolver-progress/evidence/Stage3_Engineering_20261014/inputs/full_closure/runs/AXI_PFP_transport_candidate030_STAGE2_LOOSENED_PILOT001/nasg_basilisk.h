/* NASG closure for Basilisk all-Mach two-phase solver.
 * Original expressions for pressure and mixture bulk compressibility are
 * adapted from official compressible/NASG.h (GPL-3.0-or-later).
 * The pure-phase sound speed is corrected to include b and q. The official
 * header's sound_speed copied stiffened-gas pressure recovery, whereas its
 * average_pressure already uses NASG. Phase kinetic energy is removed using
 * phase mass, as required by the documented definition fEi=fi*rhoi*Etot_i.
 * Mixture bulk compressibility remains the official arithmetic closure;
 * it must be tested separately before any production two-phase claim.
 */
#include "eos_nasg.h"
double gamma1 = 1.4, gamma2 = 1.4, PI1 = 0., PI2 = 0.;
double b1 = 0., b2 = 0., q1 = 0., q2 = 0., cv1 = 1., cv2 = 1.;

double sound_speed (Point point) {
  double density = frho1[] + frho2[];
  double u2 = 0.;
  foreach_dimension() u2 += sq(q.x[]/density);
  double c21 = 0., c22 = 0.;
  if (f[] > 1.e-10 && frho1[] > 0.) {
    ClosureNASG eos = {gamma1, PI1, b1, cv1, q1};
    double rho = frho1[]/f[];
    double e = fE1[]/frho1[] - .5*u2;
    c21 = nasg_c2(eos, rho, nasg_p(eos, rho, e));
  }
  if (1. - f[] > 1.e-10 && frho2[] > 0.) {
    ClosureNASG eos = {gamma2, PI2, b2, cv2, q2};
    double rho = frho2[]/(1. - f[]);
    double e = fE2[]/frho2[] - .5*u2;
    c22 = nasg_c2(eos, rho, nasg_p(eos, rho, e));
  }
  if (!isfinite(c21) || !isfinite(c22)) return NAN;
  return sqrt(max(c21, c22));
}

#define CLOSURE_NASG_MIXTURE \
  double fc = f[], \
    d = (fc - frho1[]*b1)/(gamma1 - 1.) + \
      (1. - fc - frho2[]*b2)/(gamma2 - 1.), \
    c = (fc - frho1[]*b1)*gamma1*PI1/(gamma1 - 1.) + frho1[]*q1 + \
      (1. - fc - frho2[]*b2)*gamma2*PI2/(gamma2 - 1.) + frho2[]*q2

double average_pressure (Point point) {
  CLOSURE_NASG_MIXTURE;
  double ek = 0.;
  foreach_dimension() ek += sq(q.x[]);
  ek /= 2.*(frho1[] + frho2[]);
  return (fE1[] + fE2[] - ek - c)/d;
}

double bulk_compressibility (Point point) {
  double fc = f[], a = 0., b = 0.;
  if (fc > 0.) a = fc*gamma1*(p[] + PI1)/(1. - b1*frho1[]/fc);
  if (fc < 1.) b = (1. - fc)*gamma2*(p[] + PI2)/(1. - b2*frho2[]/(1. - fc));
  return a + b;
}

double internal_energy (Point point, double pure_fraction) {
  /* Basilisk's refinement API evaluates this at pure-fraction 0 or 1;
   * the documented mixture internal-energy expression uses current f[]. */
  CLOSURE_NASG_MIXTURE;
  return p[]*d + c;
}
