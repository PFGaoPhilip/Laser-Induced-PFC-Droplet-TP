/* Tensor Hermite Gibbs-potential interpolation, original task-owned code.
 * x=log((p+pressure_shift)/pressure_scale), T in kelvin. Every state property
 * is differentiated from this one interpolated potential. There is no
 * independent pressure/energy/entropy interpolant or domain extrapolation.
 * The caller owns nodes and allocates table storage; this header has no I/O.
 */
#ifndef CLOSURE_GIBBS_POTENTIAL_H
#define CLOSURE_GIBBS_POTENTIAL_H
#include <math.h>
#include <stddef.h>

typedef struct { double g, gx, gT, gxT; int valid; } ClosureGibbsNode;
typedef struct {
  size_t nx, nT;
  double * x, * temperature;
  ClosureGibbsNode * nodes;
  double pressure_shift, pressure_scale;
  /* Zero disables routing (analytic generic tables). For HEOS tables the
   * declared common single-fluid root above Tc is the vapour-table root. */
  double shared_supercritical_temperature;
} ClosureGibbsTable;
typedef struct { double g, gp, gT, gpp, gpT, gTT; } ClosureGibbsJet;
typedef struct { double v, rho, u, s, cp, cv, c2, beta, pu, prho; } ClosureGibbsState;
enum ClosureGibbsStatus {
  CLOSURE_GIBBS_OK = 0, CLOSURE_GIBBS_OUTSIDE = 1,
  CLOSURE_GIBBS_INVALID_CELL = 2, CLOSURE_GIBBS_UNSTABLE = 3,
  CLOSURE_GIBBS_NO_CONVERGENCE = 4
};

static inline int closure_interval (const double * grid, size_t n,
                                    double value, size_t * interval) {
  if (n < 2 || value < grid[0] || value > grid[n-1] || !isfinite(value))
    return CLOSURE_GIBBS_OUTSIDE;
  size_t lo = 0, hi = n - 1;
  while (hi - lo > 1) {
    size_t middle = (lo + hi)/2;
    if (value < grid[middle]) hi = middle;
    else lo = middle;
  }
  *interval = value == grid[n-1] ? n - 2 : lo;
  return CLOSURE_GIBBS_OK;
}

static inline void closure_hermite_basis (double t, double * h,
                                          double * dh, double * ddh) {
  h[0] = 2*t*t*t - 3*t*t + 1;
  h[1] = t*t*t - 2*t*t + t;
  h[2] = -2*t*t*t + 3*t*t;
  h[3] = t*t*t - t*t;
  dh[0] = 6*t*t - 6*t;
  dh[1] = 3*t*t - 4*t + 1;
  dh[2] = -6*t*t + 6*t;
  dh[3] = 3*t*t - 2*t;
  ddh[0] = 12*t - 6;
  ddh[1] = 6*t - 4;
  ddh[2] = -12*t + 6;
  ddh[3] = 6*t - 2;
}

static inline int closure_gibbs_eval (const ClosureGibbsTable * table,
                                      double p, double T,
                                      ClosureGibbsJet * output) {
  double shifted = p + table->pressure_shift;
  if (!(shifted > 0.) || !(T > 0.) || !(table->pressure_scale > 0.))
    return CLOSURE_GIBBS_OUTSIDE;
  double x = log(shifted/table->pressure_scale);
  size_t ix, it;
  if (closure_interval(table->x, table->nx, x, &ix) ||
      closure_interval(table->temperature, table->nT, T, &it))
    return CLOSURE_GIBBS_OUTSIDE;
  double dx = table->x[ix+1] - table->x[ix];
  double dT = table->temperature[it+1] - table->temperature[it];
  double a[4][4] = {{0}};
  for (size_t i = 0; i < 2; i++) for (size_t j = 0; j < 2; j++) {
    ClosureGibbsNode node = table->nodes[(ix+i)*table->nT + it+j];
    if (!node.valid) return CLOSURE_GIBBS_INVALID_CELL;
    a[2*i][2*j] = node.g;
    a[2*i+1][2*j] = node.gx*dx;
    a[2*i][2*j+1] = node.gT*dT;
    a[2*i+1][2*j+1] = node.gxT*dx*dT;
  }
  double hx[4], hT[4], dhx[4], dhT[4], ddhx[4], ddhT[4];
  closure_hermite_basis((x-table->x[ix])/dx, hx, dhx, ddhx);
  closure_hermite_basis((T-table->temperature[it])/dT, hT, dhT, ddhT);
  double g = 0., gx = 0., gT = 0., gxx = 0., gxT = 0., gTT = 0.;
  for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) {
    g += a[i][j]*hx[i]*hT[j];
    gx += a[i][j]*dhx[i]*hT[j]/dx;
    gT += a[i][j]*hx[i]*dhT[j]/dT;
    gxx += a[i][j]*ddhx[i]*hT[j]/(dx*dx);
    gxT += a[i][j]*dhx[i]*dhT[j]/(dx*dT);
    gTT += a[i][j]*hx[i]*ddhT[j]/(dT*dT);
  }
  *output = (ClosureGibbsJet) {g, gx/shifted, gT,
    (gxx-gx)/(shifted*shifted), gxT/shifted, gTT};
  return CLOSURE_GIBBS_OK;
}

static inline ClosureGibbsJet closure_gibbs_mix (ClosureGibbsJet liquid,
                                               ClosureGibbsJet vapour,
                                               double xi) {
  ClosureGibbsJet mixture;
  double a = 1. - xi;
  mixture.g = a*liquid.g + xi*vapour.g;
  mixture.gp = a*liquid.gp + xi*vapour.gp;
  mixture.gT = a*liquid.gT + xi*vapour.gT;
  mixture.gpp = a*liquid.gpp + xi*vapour.gpp;
  mixture.gpT = a*liquid.gpT + xi*vapour.gpT;
  mixture.gTT = a*liquid.gTT + xi*vapour.gTT;
  return mixture;
}

static inline int closure_gibbs_state (ClosureGibbsJet jet,
                                       double p, double T,
                                       ClosureGibbsState * output) {
  double cp = -T*jet.gTT;
  double det = jet.gpp*cp + T*jet.gpT*jet.gpT;
  if (!(T > 0.) || !(jet.gp > 0.) || !(jet.gpp < 0.) ||
      !(cp > 0.) || !(det < 0.) || !isfinite(det))
    return CLOSURE_GIBBS_UNSTABLE;
  double rho = 1./jet.gp;
  double uT = cp - p*jet.gpT;
  *output = (ClosureGibbsState) {
    jet.gp, rho, jet.g-T*jet.gT-p*jet.gp, -jet.gT, cp,
    cp + T*jet.gpT*jet.gpT/jet.gpp,
    -cp/(rho*rho*det), jet.gpT/jet.gp,
    -jet.gpT/det, -uT/(rho*rho*det)
  };
  return CLOSURE_GIBBS_OK;
}

static inline int closure_gibbs_eval_mix (const ClosureGibbsTable * liquid,
                                         const ClosureGibbsTable * vapour,
                                         double xi, double p, double T,
                                         ClosureGibbsJet * mixture,
                                         ClosureGibbsState * state) {
  if (!(xi >= 0. && xi <= 1.)) return CLOSURE_GIBBS_OUTSIDE;
  if (liquid->shared_supercritical_temperature > 0. &&
      T >= liquid->shared_supercritical_temperature) {
    int status = closure_gibbs_eval(vapour,p,T,mixture);
    return status ? status : closure_gibbs_state(*mixture,p,T,state);
  }
  ClosureGibbsJet l, v;
  int sl = closure_gibbs_eval(liquid, p, T, &l);
  int sv = closure_gibbs_eval(vapour, p, T, &v);
  if (xi == 0.) {
    if (sl) return sl;
    *mixture = l;
  } else if (xi == 1.) {
    if (sv) return sv;
    *mixture = v;
  } else {
    if (sl) return sl;
    if (sv) return sv;
    *mixture = closure_gibbs_mix(l, v, xi);
  }
  return closure_gibbs_state(*mixture, p, T, state);
}

/* Newton with backtracking is an inversion algorithm; it never modifies
 * conserved rho,u,xi or clips a physical state. Explicit failure is returned
 * when no valid thermodynamic root is found. Guesses are caller-owned. */
static inline int closure_gibbs_invert (const ClosureGibbsTable * liquid,
                                       const ClosureGibbsTable * vapour,
                                       double rho, double u, double xi,
                                       double * pressure, double * temperature,
                                       double tolerance, int max_iterations) {
  if (!(rho > 0.) || !(tolerance > 0.)) return CLOSURE_GIBBS_OUTSIDE;
  double p = *pressure, T = *temperature;
  for (int iteration = 0; iteration < max_iterations; iteration++) {
    ClosureGibbsJet jet; ClosureGibbsState state;
    int status = closure_gibbs_eval_mix(liquid, vapour, xi, p, T, &jet, &state);
    if (status) return status;
    double rv = state.v - 1./rho, ru = state.u - u;
    double uscale = fabs(u) + state.cp*T;
    double norm = fmax(fabs(rv)*rho, fabs(ru)/uscale);
    if (norm < tolerance) { *pressure = p; *temperature = T; return 0; }
    double up = -T*jet.gpT - p*jet.gpp;
    double uT = -T*jet.gTT - p*jet.gpT;
    double det = jet.gpp*uT - jet.gpT*up;
    double dp = (-rv*uT + ru*jet.gpT)/det;
    double dT = (-ru*jet.gpp + rv*up)/det;
    int accepted = 0;
    for (double fraction = 1.; fraction >= 1./4096.; fraction *= .5) {
      double pn = p + fraction*dp, Tn = T + fraction*dT;
      ClosureGibbsJet trialjet; ClosureGibbsState trial;
      int trial_status = closure_gibbs_eval_mix(liquid, vapour, xi, pn, Tn, &trialjet, &trial);
      if (trial_status) continue;
      double trial_norm = fmax(fabs(trial.v-1./rho)*rho, fabs(trial.u-u)/uscale);
      if (trial_norm < norm) { p = pn; T = Tn; accepted = 1; break; }
    }
    if (!accepted) return CLOSURE_GIBBS_NO_CONVERGENCE;
  }
  return CLOSURE_GIBBS_NO_CONVERGENCE;
}

/* A local multi-seed inversion is an algorithmic search over unchanged
 * conserved inputs, not a physical-state reset. Exact nearby table anchors
 * are useful near phase-mask boundaries. No masked root is ever filled. */
static inline int closure_gibbs_invert_safeguarded (const ClosureGibbsTable * liquid,
                                                  const ClosureGibbsTable * vapour,
                                                  double rho,double u,double xi,
                                                  double *pressure,double *temperature,
                                                  double tolerance,int max_iterations) {
  double original_p=*pressure,original_T=*temperature;
  int status=closure_gibbs_invert(liquid,vapour,rho,u,xi,pressure,temperature,tolerance,max_iterations);
  if(!status) return 0;
  const ClosureGibbsTable * tables[2]={liquid,vapour};
  for(int branch=0;branch<2;branch++) {
    const ClosureGibbsTable *table=tables[branch];
    if(original_p+table->pressure_shift<=0.) continue;
    size_t ix,jt;
    if(closure_interval(table->x,table->nx,log((original_p+table->pressure_shift)/table->pressure_scale),&ix) ||
       closure_interval(table->temperature,table->nT,original_T,&jt)) continue;
    for(int di=-1;di<=2;di++)for(int dj=-1;dj<=2;dj++) {
      long ci=(long)ix+di,cj=(long)jt+dj;
      if(ci<0||cj<0||ci>=(long)table->nx||cj>=(long)table->nT)continue;
      double p=table->pressure_scale*exp(table->x[ci])-table->pressure_shift,T=table->temperature[cj];
      int candidate=closure_gibbs_invert(liquid,vapour,rho,u,xi,&p,&T,tolerance,max_iterations);
      if(!candidate){*pressure=p;*temperature=T;return 0;}
    }
  }
  *pressure=original_p;*temperature=original_T;return status;
}
#endif
