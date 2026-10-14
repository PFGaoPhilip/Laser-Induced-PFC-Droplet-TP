/* EOS_DIAGNOSTIC_001_BEGIN */#include "eos_diagnostic_api.h"
/* EOS_DIAGNOSTIC_001_END *//* Original exact Helmholtz implementation for two declared PFC fluids.
 * No tabulation, property clipping, empirical refit or EOS switch is used.
 * Coefficient JSON exports and MIT provenance are adjacent.
 * A failed phase root/inversion is an explicit numerical/model failure.
 */
#ifndef CLOSURE_PFC_HELMHOLTZ_H
#define CLOSURE_PFC_HELMHOLTZ_H
#include <math.h>
#include <stddef.h>
#include <string.h>

typedef struct {
  const char * name;
  double R, Tc, rhoc, critical_T, critical_rho, a1, a2, a_log;
  int npe; const double * pe_n, * pe_t;
  int npo; const double * po_n, * po_d, * po_t, * po_l;
  int nga; const double * ga_n, * ga_d, * ga_t, * ga_eta, * ga_epsilon, * ga_beta, * ga_gamma;
} ClosurePFCFluid;
#include "pfc_coefficients.h"

typedef struct { double a,d,t,dd,dt,tt; } ClosureHelmholtzJet;
typedef struct {
  double p,T,rho,v,u,s,h,g,cv,cp,c2,vp,vT,up,uT,fugacity,log_fugacity_Pa;
} ClosurePFCPhase;
typedef struct {
  ClosurePFCPhase liquid,vapour;
  double p,T,xi,v,rho,u,s,cp,cv,c2,vp,vT,up,uT;
  int liquid_available,vapour_available,coalesced;
} ClosurePFCMixture;

static void closure_helmholtz_add(ClosureHelmholtzJet * a, double value,
  double ld,double lt,double ldd,double ltt) {
  a->a+=value; a->d+=value*ld; a->t+=value*lt;
  a->dd+=value*(ld*ld+ldd); a->dt+=value*ld*lt;
  a->tt+=value*(lt*lt+ltt);
}

static int closure_pfc_potential_eos_diagnostic_original(const ClosurePFCFluid * f, double delta,
  double tau, ClosureHelmholtzJet * ideal, ClosureHelmholtzJet * residual) {
  if (!(delta>0.) || !(tau>0.) || !isfinite(delta+tau)) return 1;
  memset(ideal,0,sizeof(*ideal)); memset(residual,0,sizeof(*residual));
  ideal->a=log(delta)+f->a1+f->a2*tau+f->a_log*log(tau);
  ideal->d=1./delta; ideal->dd=-1./(delta*delta);
  ideal->t=f->a2+f->a_log/tau; ideal->tt=-f->a_log/(tau*tau);
  for(int k=0;k<f->npe;k++) {
    double z=f->pe_t[k]*tau, ez=exp(-z), em=-expm1(-z);
    if (!(em>0.)) return 1;
    ideal->a+=f->pe_n[k]*log(em);
    ideal->t+=f->pe_n[k]*f->pe_t[k]*ez/em;
    ideal->tt-=f->pe_n[k]*f->pe_t[k]*f->pe_t[k]*ez/(em*em);
  }
  for(int k=0;k<f->npo;k++) {
    double d=f->po_d[k], t=f->po_t[k], l=f->po_l[k];
    double damping=l>0.?pow(delta,l):0.;
    double value=f->po_n[k]*pow(delta,d)*pow(tau,t)*exp(-damping);
    double ld=d/delta-(l>0.?l*damping/delta:0.);
    double ldd=-d/(delta*delta)-(l>0.?l*(l-1.)*damping/(delta*delta):0.);
    closure_helmholtz_add(residual,value,ld,t/tau,ldd,-t/(tau*tau));
  }
  for(int k=0;k<f->nga;k++) {
    double d=f->ga_d[k],t=f->ga_t[k],dr=delta-f->ga_epsilon[k],tr=tau-f->ga_gamma[k];
    double value=f->ga_n[k]*pow(delta,d)*pow(tau,t)*exp(-f->ga_eta[k]*dr*dr-f->ga_beta[k]*tr*tr);
    closure_helmholtz_add(residual,value,d/delta-2.*f->ga_eta[k]*dr,
      t/tau-2.*f->ga_beta[k]*tr,-d/(delta*delta)-2.*f->ga_eta[k],
      -t/(tau*tau)-2.*f->ga_beta[k]);
  }
  return !(isfinite(ideal->a+ideal->t+ideal->tt+residual->a+residual->d+residual->t+residual->dd+residual->dt+residual->tt));
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_potential(const ClosurePFCFluid * f, double delta,
  double tau, ClosureHelmholtzJet * ideal, ClosureHelmholtzJet * residual) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_POTENTIAL);
  int value=closure_pfc_potential_eos_diagnostic_original(f,delta,tau,ideal,residual);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_pfc_raw_eos_diagnostic_original(const ClosurePFCFluid * f,double rho,double T,
  ClosurePFCPhase * state) {
  if (!(rho>0.) || !(T>0.)) return 1;
  double delta=rho/f->rhoc,tau=f->Tc/T;
  ClosureHelmholtzJet ideal,residual;
  if(closure_pfc_potential(f,delta,tau,&ideal,&residual)) return 1;
  double at=ideal.t+residual.t,att=ideal.tt+residual.tt;
  double Z=1.+delta*residual.d;
  double K=1.+2.*delta*residual.d+delta*delta*residual.dd;
  double B=Z-delta*tau*residual.dt;
  state->rho=rho; state->T=T; state->v=1./rho;
  state->p=rho*f->R*T*Z;
  state->u=f->R*T*tau*at;
  state->s=f->R*(tau*at-ideal.a-residual.a);
  state->h=state->u+state->p/rho;
  state->g=state->h-T*state->s;
  state->cv=-f->R*tau*tau*att;
  state->cp=state->cv+f->R*B*B/K;
  state->c2=f->R*T*(K-B*B/(tau*tau*att));
  state->vp=-1./(rho*rho*f->R*T*K);
  state->vT=B/(rho*T*K);
  state->up=-T*state->vT-state->p*state->vp;
  state->uT=state->cp-state->p*state->vT;
  state->log_fugacity_Pa=log(rho*f->R*T)+residual.a+delta*residual.d;
  state->fugacity=exp(state->log_fugacity_Pa);
  if(!(K>0.) || !(state->cv>0.) || !(state->cp>0.) || !(state->c2>0.) ||
    !isfinite(state->u+state->s+state->cp+state->c2+state->vp+state->vT+state->log_fugacity_Pa)) return 2;
  return 0;
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_raw(const ClosurePFCFluid * f,double rho,double T,
  ClosurePFCPhase * state) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_CALORIC_RAW);
  int value=closure_pfc_raw_eos_diagnostic_original(f,rho,T,state);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_pfc_pressure_stiffness_eos_diagnostic_original(const ClosurePFCFluid * f,double rho,double T,
  double * pressure,double * stiffness) {
  ClosureHelmholtzJet ideal,residual;
  double delta=rho/f->rhoc;
  if(closure_pfc_potential(f,delta,f->Tc/T,&ideal,&residual)) return 1;
  *pressure=rho*f->R*T*(1.+delta*residual.d);
  *stiffness=f->R*T*(1.+2.*delta*residual.d+delta*delta*residual.dd);
  return !isfinite(*pressure+*stiffness);
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_pressure_stiffness(const ClosurePFCFluid * f,double rho,double T,
  double * pressure,double * stiffness) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_PRESSURE_STIFFNESS);
  int value=closure_pfc_pressure_stiffness_eos_diagnostic_original(f,rho,T,pressure,stiffness);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static double closure_pfc_pressure(const ClosurePFCFluid * f,double rho,double T) {
  double pressure,stiffness;
  return closure_pfc_pressure_stiffness(f,rho,T,&pressure,&stiffness)?NAN:pressure;
}

static int closure_pfc_pressure_root_eos_diagnostic_original(const ClosurePFCFluid * f,double p,double T,
  double low,double high,ClosurePFCPhase * state) {
  double fl=closure_pfc_pressure(f,low,T)-p,fh=closure_pfc_pressure(f,high,T)-p;
  if(!isfinite(fl+fh) || (fl!=0. && fh!=0. && fl*fh>0.)) return 1;
  for(int j=0;j<70;j++) {
    double mid=.5*(low+high),fm=closure_pfc_pressure(f,mid,T)-p;
    if(fl*fm<=0.) high=mid; else {low=mid;fl=fm;}
    if(high-low<=1.e-13*fmax(low,high)) break;
  }
  double root=.5*(low+high);
  if(closure_pfc_raw(f,root,T,state) || fabs(state->p-p)>2.e-8*(fabs(p)+1.e5)) return 2;
  return 0;
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_pressure_root(const ClosurePFCFluid * f,double p,double T,
  double low,double high,ClosurePFCPhase * state) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_PRESSURE_ROOT);
  int value=closure_pfc_pressure_root_eos_diagnostic_original(f,p,T,low,high,state);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

/* Sampled branch discovery, not exhaustive interval isolation. Physical phase
 * labels are the stable components connected to dilute rho or the dense side;
 * interior EOS islands remain diagnosed in root_count. First/last sampled
 * instability disconnects those islands. Spinodal/tangent pairs can be missed
 * at finite sampling; root-grid refinement and continuity checks remain needed
 * over every production state. Bounds are algorithmic, not state floors. */
static int closure_pfc_phase_PT_eos_diagnostic_original(const ClosurePFCFluid * f,double p,double T,
  int liquid,ClosurePFCPhase * state,int * root_count) {
  if(!isfinite(p+T) || !(T>0.) || (!liquid && !(p>0.))) return 1;
  const int nodes=1024;
  double critical_delta=f->critical_rho/f->rhoc;
  double low=liquid && T<f->critical_T ? critical_delta : 1.e-12;
  double high=!liquid && T<f->critical_T ? critical_delta : 16.;
  double previous=low*f->rhoc;
  double pp,kp;
  if(closure_pfc_pressure_stiffness(f,previous,T,&pp,&kp)) return 2;
  int count=0,selected=0,gas_connected=1; ClosurePFCPhase candidate={0},last_root={0};
  for(int k=1;k<=nodes;k++) {
    double current=f->rhoc*exp(log(low)+(log(high)-log(low))*k/nodes);
    double pc,kc;
    if(closure_pfc_pressure_stiffness(f,current,T,&pc,&kc)) return 2;
    /* Insert an actual mechanical pressure extremum before pressure bracketing.
     * A narrow stable/unstable pair may have equal-sign pressure residuals at
     * coarse endpoints but opposite-sign pressure derivatives. */
    double bounds[3]={previous,current,current},pressures[3]={pp,pc,pc};int segments=1;
    if(kp*kc<0.) {
      double a=previous,b=current,ka=kp;
      for(int j=0;j<70;j++) {
        double mid=.5*(a+b),pm,km;
        if(closure_pfc_pressure_stiffness(f,mid,T,&pm,&km)) return 2;
        if(ka*km<=0.) b=mid;else {a=mid;ka=km;}
        if(b-a<=1.e-13*fmax(a,b)) break;
      }
      bounds[1]=.5*(a+b);bounds[2]=current;segments=2;
      pressures[1]=closure_pfc_pressure(f,bounds[1],T);
    }
    for(int segment=0;segment<segments;segment++) {
      double fl=pressures[segment]-p,fh=pressures[segment+1]-p;
      if(fl!=0. && fh!=0. && fl*fh>0.) continue;
      ClosurePFCPhase trial;
      if(!closure_pfc_pressure_root(f,p,T,bounds[segment],bounds[segment+1],&trial) &&
         (T>=f->critical_T || (liquid?trial.rho>f->critical_rho:trial.rho<f->critical_rho))) {
        double root=trial.rho;
        if(!count || fabs(root-last_root.rho)>1.e-8*root) {
          last_root=trial;count++;
          if(liquid || gas_connected) {candidate=trial;selected=1;}
        }
      }
    }
    ClosurePFCPhase sampled;
    if(closure_pfc_raw(f,current,T,&sampled)) {
      if(liquid) selected=0;
      else gas_connected=0;
    }
    previous=current;pp=pc;kp=kc;
  }
  if(root_count) *root_count=count;
  if(!selected) return 3;
  *state=candidate;
  return 0;
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_phase_PT(const ClosurePFCFluid * f,double p,double T,
  int liquid,ClosurePFCPhase * state,int * root_count) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_PT_DISCOVERY);
  int value=closure_pfc_phase_PT_eos_diagnostic_original(f,p,T,liquid,state,root_count);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_pfc_combine(double p,double T,double xi,ClosurePFCMixture * state) {
  state->p=p;state->T=T;state->xi=xi;
  double a=1.-xi,b=xi;
  state->v=a*state->liquid.v+b*state->vapour.v;state->rho=1./state->v;
  state->u=a*state->liquid.u+b*state->vapour.u;
  state->s=a*state->liquid.s+b*state->vapour.s;
  state->cp=a*state->liquid.cp+b*state->vapour.cp;
  state->vp=a*state->liquid.vp+b*state->vapour.vp;
  state->vT=a*state->liquid.vT+b*state->vapour.vT;
  state->up=a*state->liquid.up+b*state->vapour.up;
  state->uT=a*state->liquid.uT+b*state->vapour.uT;
  /* Exact Schur-complement identity. This avoids cancellation of large
   * opposite terms in vp*Cp+T*vT^2 near isothermal spinodals. */
  double kl=-state->liquid.vp,kv=-state->vapour.vp,k=a*kl+b*kv;
  double response=state->liquid.vT/kl-state->vapour.vT/kv;
  double harmonic=1./(a/kv+b/kl);
  state->cv=a*state->liquid.cv+b*state->vapour.cv+T*a*b*harmonic*response*response;
  double D=-k*state->cv;
  state->c2=state->cp/(state->rho*state->rho*k*state->cv);
  if(!(D<0.) || !(state->c2>0.) || !isfinite(state->c2)) return 2;
  return 0;
}

static int closure_pfc_mixture_PT_eos_diagnostic_original(const ClosurePFCFluid * f,double p,double T,
  double xi,ClosurePFCMixture * state) {
  if(!(xi>=0. && xi<=1.)) return 1;
  memset(state,0,sizeof(*state));
  int roots;
  if(T>=f->critical_T) {
    if(closure_pfc_phase_PT(f,p,T,0,&state->vapour,&roots)) return 3;
    state->liquid=state->vapour; state->coalesced=1;
    state->liquid_available=state->vapour_available=1;
  } else {
    state->liquid_available=!closure_pfc_phase_PT(f,p,T,1,&state->liquid,&roots);
    if(!state->liquid_available && xi!=1.) return 3;
    state->vapour_available=!closure_pfc_phase_PT(f,p,T,0,&state->vapour,&roots);
    if(!state->vapour_available && xi!=0.) return 3;
    if(!state->liquid_available) state->liquid=state->vapour;
    if(!state->vapour_available) state->vapour=state->liquid;
  }
  return closure_pfc_combine(p,T,xi,state);
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_mixture_PT(const ClosurePFCFluid * f,double p,double T,
  double xi,ClosurePFCMixture * state) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_MIXTURE_PT);
  int value=closure_pfc_mixture_PT_eos_diagnostic_original(f,p,T,xi,state);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_pfc_invert_eos_diagnostic_original(const ClosurePFCFluid * f,double rho,double u,
  double xi,double * pressure,double * temperature,double tolerance,int maximum_iterations) {
  if(!(rho>0.) || !(xi>=0. && xi<=1.)) return 1;
  double p=*pressure,T=*temperature,vtarget=1./rho;
  double escale=fmax(1.e5,fabs(u)),vscale=vtarget;
  for(int k=0;k<maximum_iterations;k++) {
    ClosurePFCMixture s;
    if(closure_pfc_mixture_PT(f,p,T,xi,&s)) return 3;
    double rv=s.v-vtarget,re=s.u-u;
    double norm=fmax(fabs(rv)/vscale,fabs(re)/escale);
    if(norm<tolerance) {*pressure=p;*temperature=T;return 0;}
    double D=s.vp*s.cv;
    if(!isfinite(D) || !(D<0.)) return 2;
    double dp=(-rv*s.uT+s.vT*re)/D;
    double dT=(-s.vp*re+s.up*rv)/D;
    int accepted=0;
    for(int j=0;j<28;j++) {
      double step=ldexp(1.,-j),np=p+step*dp,nT=T+step*dT;
      ClosurePFCMixture trial;
      if(nT>0. && !closure_pfc_mixture_PT(f,np,nT,xi,&trial)) {
        double n=fmax(fabs(trial.v-vtarget)/vscale,fabs(trial.u-u)/escale);
        if(n<norm) {p=np;T=nT;accepted=1;break;}
      }/* EOS_DIAGNOSTIC_001_BEGIN */
      closure_eos_diag_note(CLOSURE_EOS_PFC_PT_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */
    }
    if(!accepted) return 5;
  }
  return 6;
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_invert(const ClosurePFCFluid * f,double rho,double u,
  double xi,double * pressure,double * temperature,double tolerance,int maximum_iterations) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_INVERSE_PT);
  int value=closure_pfc_invert_eos_diagnostic_original(f,rho,u,xi,pressure,temperature,tolerance,maximum_iterations);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

typedef struct {
  ClosurePFCPhase liquid,vapour;
  int liquid_valid,vapour_valid;
  unsigned long local_queries,global_queries;
} ClosurePFCCache;

/* Acceleration changes the numerical root algorithm only. A local path is
 * used only from a previously globally-labelled state and on small p/T moves.
 * It checks positive thermodynamic stability along sampled continuation paths;
 * failures fall back to the same connected-component discovery at the same
 * target p/T, never to a different constitutive state or inserted phase.
 * Finite continuation sampling is not an interval proof of branch exclusion. */
static int closure_pfc_phase_PT_cached_eos_diagnostic_original(const ClosurePFCFluid * f,double p,double T,
  int liquid,ClosurePFCPhase * cached,int * valid,ClosurePFCPhase * state,
  unsigned long * local_queries,unsigned long * global_queries) {
  int local=*valid && ((T>=f->critical_T)==(cached->T>=f->critical_T)) &&
    fabs(T-cached->T)<=.02*cached->T && fabs(p-cached->p)<=.05*(fabs(cached->p)+1.e5);
  double rho=local?cached->rho:0.;
  if(local) {
    for(int j=1;j<=8;j++) {
      ClosurePFCPhase path;
      if(closure_pfc_raw(f,rho,cached->T+(T-cached->T)*j/8.,&path)) {local=0;break;}
    }
  }
  if(local) {
    for(int k=0;k<45;k++) {
      ClosurePFCPhase s;
      if(closure_pfc_raw(f,rho,T,&s)) break;
      if(T<f->critical_T && (liquid?rho<=f->critical_rho:rho>=f->critical_rho)) break;
      double residual=s.p-p;
      /* Use local compressibility: ambient-pressure scaling is too loose
       * for dilute vapour and can stall a conserved-volume Newton solve. */
      if(fabs(residual)*rho*(-s.vp)<=2.e-13) {
        *state=s;*cached=s;*valid=1;(*local_queries)++;/* EOS_DIAGNOSTIC_001_BEGIN */closure_eos_diag_note(CLOSURE_EOS_PFC_PT_LOCAL_ACCEPTED,1);/* EOS_DIAGNOSTIC_001_END */return 0;
      }
      double drho=residual*rho*rho*s.vp;
      int accepted=0;
      for(int j=0;j<24;j++) {
        double step=ldexp(1.,-j),nr=rho+step*drho;
        if(!(nr>0.) || fabs(nr-rho)>.25*rho) /* EOS_DIAGNOSTIC_001_BEGIN */{ /* EOS_DIAGNOSTIC_001_END *//* EOS_DIAGNOSTIC_001_BEGIN */closure_eos_diag_note(CLOSURE_EOS_PFC_PT_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */continue;/* EOS_DIAGNOSTIC_001_BEGIN */ }/* EOS_DIAGNOSTIC_001_END */
        ClosurePFCPhase trial;
        if(closure_pfc_raw(f,nr,T,&trial) ||
          (T<f->critical_T && (liquid?nr<=f->critical_rho:nr>=f->critical_rho))) /* EOS_DIAGNOSTIC_001_BEGIN */{ /* EOS_DIAGNOSTIC_001_END *//* EOS_DIAGNOSTIC_001_BEGIN */closure_eos_diag_note(CLOSURE_EOS_PFC_PT_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */continue;/* EOS_DIAGNOSTIC_001_BEGIN */ }/* EOS_DIAGNOSTIC_001_END */
        int continuous=1;
        for(int n=1;n<8;n++) {
          ClosurePFCPhase path;
          if(closure_pfc_raw(f,rho+(nr-rho)*n/8.,T,&path)) {continuous=0;break;}
        }
        if(continuous && fabs(trial.p-p)<fabs(residual)) {rho=nr;accepted=1;break;}/* EOS_DIAGNOSTIC_001_BEGIN */
        closure_eos_diag_note(CLOSURE_EOS_PFC_PT_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */
      }
      if(!accepted) break;
    }
  }
  int roots;(*global_queries)++;/* EOS_DIAGNOSTIC_001_BEGIN */closure_eos_diag_note(CLOSURE_EOS_PFC_PT_GLOBAL_FALLBACK,1);/* EOS_DIAGNOSTIC_001_END */
  int status=closure_pfc_phase_PT(f,p,T,liquid,state,&roots);
  if(!status) {*cached=*state;*valid=1;} else *valid=0;
  return status;
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_phase_PT_cached(const ClosurePFCFluid * f,double p,double T,
  int liquid,ClosurePFCPhase * cached,int * valid,ClosurePFCPhase * state,
  unsigned long * local_queries,unsigned long * global_queries) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_PT_CACHED);
  int value=closure_pfc_phase_PT_cached_eos_diagnostic_original(f,p,T,liquid,cached,valid,state,local_queries,global_queries);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_pfc_mixture_PT_cached_eos_diagnostic_original(const ClosurePFCFluid * f,double p,double T,
  double xi,ClosurePFCCache * cache,ClosurePFCMixture * state) {
  if(!(xi>=0. && xi<=1.)) return 1;
  memset(state,0,sizeof(*state));
  if(T>=f->critical_T) {
    if(closure_pfc_phase_PT_cached(f,p,T,0,&cache->vapour,&cache->vapour_valid,
      &state->vapour,&cache->local_queries,&cache->global_queries)) return 3;
    state->liquid=state->vapour;state->coalesced=1;
    state->liquid_available=state->vapour_available=1;
    cache->liquid=cache->vapour;cache->liquid_valid=1;
  } else {
    state->liquid_available=!closure_pfc_phase_PT_cached(f,p,T,1,&cache->liquid,&cache->liquid_valid,
      &state->liquid,&cache->local_queries,&cache->global_queries);
    if(!state->liquid_available && xi!=1.) return 3;
    state->vapour_available=!closure_pfc_phase_PT_cached(f,p,T,0,&cache->vapour,&cache->vapour_valid,
      &state->vapour,&cache->local_queries,&cache->global_queries);
    if(!state->vapour_available && xi!=0.) return 3;
    if(!state->liquid_available) state->liquid=state->vapour;
    if(!state->vapour_available) state->vapour=state->liquid;
  }
  return closure_pfc_combine(p,T,xi,state);
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_mixture_PT_cached(const ClosurePFCFluid * f,double p,double T,
  double xi,ClosurePFCCache * cache,ClosurePFCMixture * state) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_MIXTURE_PT_CACHED);
  int value=closure_pfc_mixture_PT_cached_eos_diagnostic_original(f,p,T,xi,cache,state);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_pfc_invert_cached_eos_diagnostic_original(const ClosurePFCFluid * f,double rho,double u,
  double xi,ClosurePFCCache * cache,double * pressure,double * temperature,
  double tolerance,int maximum_iterations) {
  if(!(rho>0.) || !(xi>=0. && xi<=1.)) return 1;
  double p=*pressure,T=*temperature,vtarget=1./rho;
  double escale=fmax(1.e5,fabs(u)),vscale=vtarget;
  for(int k=0;k<maximum_iterations;k++) {
    ClosurePFCMixture s;
    if(closure_pfc_mixture_PT_cached(f,p,T,xi,cache,&s)) return 3;
    double rv=s.v-vtarget,re=s.u-u;
    double norm=fmax(fabs(rv)/vscale,fabs(re)/escale);
    if(norm<tolerance) {*pressure=p;*temperature=T;return 0;}
    double D=s.vp*s.cv;
    if(!isfinite(D) || !(D<0.)) return 2;
    double dp=(-rv*s.uT+s.vT*re)/D;
    double dT=(-s.vp*re+s.up*rv)/D;
    int accepted=0;
    for(int j=0;j<28;j++) {
      double step=ldexp(1.,-j),np=p+step*dp,nT=T+step*dT;
      ClosurePFCMixture trial;ClosurePFCCache trial_cache=*cache;
      if(nT>0. && !closure_pfc_mixture_PT_cached(f,np,nT,xi,&trial_cache,&trial)) {
        double n=fmax(fabs(trial.v-vtarget)/vscale,fabs(trial.u-u)/escale);
        if(n<norm) {p=np;T=nT;*cache=trial_cache;accepted=1;break;}
      }/* EOS_DIAGNOSTIC_001_BEGIN */
      closure_eos_diag_note(CLOSURE_EOS_PFC_PT_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */
    }
    if(!accepted) return 5;
  }
  return 6;
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_invert_cached(const ClosurePFCFluid * f,double rho,double u,
  double xi,ClosurePFCCache * cache,double * pressure,double * temperature,
  double tolerance,int maximum_iterations) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_INVERSE_PT_CACHED);
  int value=closure_pfc_invert_cached_eos_diagnostic_original(f,rho,u,xi,cache,pressure,temperature,tolerance,maximum_iterations);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_pfc_kinetic_flux(const ClosurePFCFluid * f,
  const ClosurePFCMixture * state,double alpha_condensation,
  double * j,double * entropy_source) {
  if(!(alpha_condensation>=0. && alpha_condensation<=1.)) return 1;
  *j=0.;*entropy_source=0.;
  if(state->coalesced || !state->liquid_available || !state->vapour_available) return 0;
  double affinity=state->liquid.g-state->vapour.g;
  double a=affinity/(f->R*state->T);
  double difference=a>=0.?exp(state->liquid.log_fugacity_Pa)*(-expm1(-a)):
    exp(state->vapour.log_fugacity_Pa)*expm1(a);
  double mobility=a>=0.?1.:alpha_condensation/(2.-alpha_condensation);
  *j=2.*mobility*difference/sqrt(2.*acos(-1.)*f->R*state->T);
  if((state->xi==0. && *j<0.) || (state->xi==1. && *j>0.)) *j=0.;
  *entropy_source=*j*affinity/state->T;
  if(!isfinite(*j+*entropy_source) || *entropy_source<0.) return 2;
  return 0;
}
#endif
