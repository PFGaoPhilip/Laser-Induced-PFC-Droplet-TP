/* Optional numerical acceleration only. Caller-owned, never global mutable.
 * Raw mechanical stiffness and same-input discovery fallback are retained.
 * Finite continuation checks are not a uniform interval branch proof.
 */
#ifndef CLOSURE_PFC_SPINODAL_CACHE_H
#define CLOSURE_PFC_SPINODAL_CACHE_H
#include "pfc_helmholtz.h"
typedef struct {
  const ClosurePFCFluid * fluid;
  double T,rho,stable,unstable,previous_T,previous_rho;
  int valid,previous_valid;
} ClosurePFCSpinodalRecord;
typedef struct {
  ClosurePFCSpinodalRecord liquid,vapour;
  unsigned long same_T_queries,warm_queries,global_queries,rejected_local,raw_K_queries;
} ClosurePFCSpinodalCache;
typedef int (*ClosurePFCSpinodalDiscovery)(const ClosurePFCFluid *,const ClosurePFCPhase *,int,double *);

static double closure_pfc_spinodal_raw_K(const ClosurePFCFluid * f,double rho,double T,
  ClosurePFCSpinodalCache * cache) {
  ClosureHelmholtzJet a,r;double d=rho/f->rhoc;
  if(cache)cache->raw_K_queries++;
  return closure_pfc_potential(f,d,f->Tc/T,&a,&r)?NAN:1.+2.*d*r.d+d*d*r.dd;
}

/* Analytic derivative proposes a Newton coordinate only. Every used bracket
 * sign remains the unchanged native raw-potential K evaluated above.
 * Term third derivatives are phi*(L'^3+3 L'L''+L'''). */
static double closure_pfc_spinodal_K_rho(const ClosurePFCFluid * f,double rho,double T) {
  double delta=rho/f->rhoc,tau=f->Tc/T,rd=0.,rdd=0.,rddd=0.;
  for(int k=0;k<f->npo;k++) {
    double d=f->po_d[k],l=f->po_l[k],damp=l>0.?pow(delta,l):0.;
    double value=f->po_n[k]*pow(delta,d)*pow(tau,f->po_t[k])*exp(-damp);
    double L=d/delta-(l>0.?l*damp/delta:0.);
    double LL=-d/(delta*delta)-(l>0.?l*(l-1.)*damp/(delta*delta):0.);
    double LLL=2.*d/(delta*delta*delta)-(l>0.?l*(l-1.)*(l-2.)*damp/(delta*delta*delta):0.);
    rd+=value*L;rdd+=value*(L*L+LL);rddd+=value*(L*L*L+3.*L*LL+LLL);
  }
  for(int k=0;k<f->nga;k++) {
    double d=f->ga_d[k],dr=delta-f->ga_epsilon[k],tr=tau-f->ga_gamma[k];
    double value=f->ga_n[k]*pow(delta,d)*pow(tau,f->ga_t[k])*exp(-f->ga_eta[k]*dr*dr-f->ga_beta[k]*tr*tr);
    double L=d/delta-2.*f->ga_eta[k]*dr,LL=-d/(delta*delta)-2.*f->ga_eta[k];
    double LLL=2.*d/(delta*delta*delta);
    rd+=value*L;rdd+=value*(L*L+LL);rddd+=value*(L*L*L+3.*L*LL+LLL);
  }
  return (2.*rd+4.*delta*rdd+delta*delta*rddd)/f->rhoc;
}

static int closure_pfc_spinodal_bracket(const ClosurePFCFluid * f,const ClosurePFCPhase * phase,
  int liquid,double center,double width,ClosurePFCSpinodalCache * cache,double * stable,double * unstable) {
  double low=fmin(phase->rho,f->critical_rho),high=fmax(phase->rho,f->critical_rho);
  for(int k=0;k<32;k++) {
    double s=liquid?fmin(high,center+width):fmax(low,center-width);
    double b=liquid?fmax(low,center-width):fmin(high,center+width);
    double Ks=closure_pfc_spinodal_raw_K(f,s,phase->T,cache);
    double Kb=closure_pfc_spinodal_raw_K(f,b,phase->T,cache);
    if(!isfinite(Ks+Kb))return 1;
    if(Ks>0. && Kb<=0. && s!=b) {*stable=s;*unstable=b;return 0;}
    if(s==phase->rho && b==f->critical_rho)break;
    width*=2.;
  }
  return 2;
}

static void closure_pfc_spinodal_store(const ClosurePFCFluid * f,const ClosurePFCPhase * phase,int liquid,
  double rho,double stable,double unstable,ClosurePFCSpinodalRecord * record) {
  if(!record->valid || record->fluid!=f)record->previous_valid=0;
  if(record->valid && record->fluid==f && record->T!=phase->T) {
    record->previous_T=record->T;record->previous_rho=record->rho;record->previous_valid=1;
  }
  record->fluid=f;record->T=phase->T;record->rho=rho;
  record->stable=stable;record->unstable=unstable;record->valid=1;
  (void)liquid;
}

static int closure_pfc_spinodal_cached(const ClosurePFCFluid * f,const ClosurePFCPhase * phase,int liquid,
  ClosurePFCSpinodalCache * cache,ClosurePFCSpinodalDiscovery reference,double * rho_spinodal) {
  if(!cache)return reference(f,phase,liquid,rho_spinodal);
  ClosurePFCSpinodalRecord * rec=liquid?&cache->liquid:&cache->vapour;
  if(!(phase->T<f->critical_T) || !(phase->rho>0.)) {rec->valid=0;return reference(f,phase,liquid,rho_spinodal);}
  double scale=fmax(phase->rho,f->critical_rho);
  int local=rec->valid && rec->fluid==f && isfinite(rec->T+rec->rho+rec->stable+rec->unstable) &&
    fabs(phase->T-rec->T)<=.005*f->critical_T &&
    (liquid?phase->rho>=rec->rho && rec->rho>f->critical_rho:
            phase->rho<=rec->rho && rec->rho<f->critical_rho);
  if(local && closure_pfc_spinodal_raw_K(f,phase->rho,phase->T,cache)>0.) {
    if(phase->T==rec->T) {
      double Ks=closure_pfc_spinodal_raw_K(f,rec->stable,phase->T,cache);
      double Kb=closure_pfc_spinodal_raw_K(f,rec->unstable,phase->T,cache);
      if(Ks>0. && Kb<=0.) {cache->same_T_queries++;*rho_spinodal=rec->rho;return 0;}
    }
    double center=rec->rho;
    if(rec->previous_valid && rec->T!=rec->previous_T) {
      double proposed=center+(rec->rho-rec->previous_rho)/(rec->T-rec->previous_T)*(phase->T-rec->T);
      if(isfinite(proposed) && proposed>fmin(phase->rho,f->critical_rho) && proposed<fmax(phase->rho,f->critical_rho))center=proposed;
    }
    double stable=0.,unstable=0.,width=fmax(4.*fabs(rec->stable-rec->unstable),1.e-6*scale);
    int good=!closure_pfc_spinodal_bracket(f,phase,liquid,center,width,cache,&stable,&unstable);
    if(good)for(int n=1;n<=8;n++) {
      double path=phase->rho+(stable-phase->rho)*n/8.;
      if(!(closure_pfc_spinodal_raw_K(f,path,phase->T,cache)>0.)) {good=0;break;}
    }
    if(good) {
      double x=fmin(fmax(center,fmin(stable,unstable)),fmax(stable,unstable));
      for(int k=0;k<96;k++) {
        if(!(x>fmin(stable,unstable) && x<fmax(stable,unstable)))x=.5*(stable+unstable);
        double K=closure_pfc_spinodal_raw_K(f,x,phase->T,cache);
        if(!isfinite(K)) {good=0;break;}
        if(K>0.)stable=x;else unstable=x;
        if(fabs(stable-unstable)<1.e-13*fmax(stable,unstable)) {
          *rho_spinodal=.5*(stable+unstable);
          closure_pfc_spinodal_store(f,phase,liquid,*rho_spinodal,stable,unstable,rec);
          cache->warm_queries++;return 0;
        }
        double derivative=closure_pfc_spinodal_K_rho(f,x,phase->T);
        double nx=x-K/derivative;
        x=(k%2==0 && isfinite(nx) && nx>fmin(stable,unstable) && nx<fmax(stable,unstable))?
          nx:.5*(stable+unstable);
      }
    }
    cache->rejected_local++;
  }
  cache->global_queries++;
  int status=reference(f,phase,liquid,rho_spinodal);if(status) {rec->valid=0;return status;}
  double stable=0.,unstable=0.,width=2.e-13*fmax(*rho_spinodal,f->critical_rho);
  if(!closure_pfc_spinodal_bracket(f,phase,liquid,*rho_spinodal,width,cache,&stable,&unstable))
    closure_pfc_spinodal_store(f,phase,liquid,*rho_spinodal,stable,unstable,rec);
  else rec->valid=0;
  return 0;
}
#endif
