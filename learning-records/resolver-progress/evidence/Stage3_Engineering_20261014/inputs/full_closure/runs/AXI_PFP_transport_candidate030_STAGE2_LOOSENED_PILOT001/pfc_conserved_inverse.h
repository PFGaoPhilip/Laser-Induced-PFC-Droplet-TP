/* Original conserved-coordinate warm inversion of the unchanged HEOS
 * potential. Global connected-branch discovery remains the cold reference.
 * No target, phase mass, EOS energy reference or physical state is altered. */
#ifndef CLOSURE_PFC_CONSERVED_INVERSE_H
#define CLOSURE_PFC_CONSERVED_INVERSE_H
#include "pfc_helmholtz.h"

typedef struct {
  unsigned long raw_queries,iterations,fast_queries,fallback_queries;
} ClosurePFCInverseStats;

static int closure_pfc_inverse_raw(const ClosurePFCFluid * f,double rho,double T,
  int liquid,int supercritical,ClosurePFCPhase * s,ClosurePFCInverseStats * stats) {
  if(stats) stats->raw_queries++;
  if((T>=f->critical_T)!=supercritical || closure_pfc_raw(f,rho,T,s)) return 1;
  if(!supercritical && (liquid?rho<=f->critical_rho:rho>=f->critical_rho)) return 1;
  return 0;
}

/* Partial pivoting solves a dimensionless three-equation Newton system. */
static int closure_pfc_solve3(double J[3][3],double rhs[3],double solution[3]) {
  double a[3][4];
  for(int i=0;i<3;i++) {
    for(int j=0;j<3;j++) a[i][j]=J[i][j];
    a[i][3]=rhs[i];
  }
  for(int k=0;k<3;k++) {
    int pivot=k;
    for(int i=k+1;i<3;i++) if(fabs(a[i][k])>fabs(a[pivot][k])) pivot=i;
    if(!isfinite(a[pivot][k]) || a[pivot][k]==0.) return 1;
    if(pivot!=k) for(int j=k;j<4;j++) {double tmp=a[k][j];a[k][j]=a[pivot][j];a[pivot][j]=tmp;}
    for(int i=k+1;i<3;i++) {
      double ratio=a[i][k]/a[k][k];
      for(int j=k+1;j<4;j++) a[i][j]-=ratio*a[k][j];
    }
  }
  for(int i=2;i>=0;i--) {
    double residual=a[i][3];
    for(int j=i+1;j<3;j++) residual-=a[i][j]*solution[j];
    solution[i]=residual/a[i][i];
    if(!isfinite(solution[i])) return 1;
  }
  return 0;
}

static double closure_pfc_density_residual(const ClosurePFCPhase * l,
  const ClosurePFCPhase * v,double xi,double vtarget,double utarget,
  double escale,double pscale) {
  return fmax(fabs(l->p-v->p)/pscale,
    fmax(fabs((1.-xi)*l->v+xi*v->v-vtarget)/vtarget,
      fabs((1.-xi)*l->u+xi*v->u-utarget)/escale));
}

/* Pressure equality and the two conserved targets have different numerical
 * condition numbers in a dense-liquid/dilute-vapour mixture. This norm does
 * not alter any target. The original single-tolerance API is retained below. */
static double closure_pfc_density_controlled_residual(const ClosurePFCPhase * l,
  const ClosurePFCPhase * v,double xi,double vtarget,double utarget,
  double escale,double pscale,double ptol,double vtol,double utol) {
  if(ptol==vtol && ptol==utol)
    return closure_pfc_density_residual(l,v,xi,vtarget,utarget,escale,pscale)/ptol;
  return fmax(fabs(l->p-v->p)/(pscale*ptol),
    fmax(fabs((1.-xi)*l->v+xi*v->v-vtarget)/(vtarget*vtol),
      fabs((1.-xi)*l->u+xi*v->u-utarget)/(escale*utol)));
}

static int closure_pfc_inverse_density_path(const ClosurePFCFluid * f,
  const ClosurePFCPhase * old_l,const ClosurePFCPhase * old_v,
  double rho_l,double rho_v,double T,int supercritical,
  ClosurePFCPhase * l,ClosurePFCPhase * v,ClosurePFCInverseStats * stats) {
  if(closure_pfc_inverse_raw(f,rho_l,T,1,supercritical,l,stats) ||
    closure_pfc_inverse_raw(f,rho_v,T,0,supercritical,v,stats)) return 1;
  for(int j=1;j<8;j++) {
    double q=j/8.,nT=old_l->T+q*(T-old_l->T);
    ClosurePFCPhase path;
    if(closure_pfc_inverse_raw(f,old_l->rho+q*(rho_l-old_l->rho),nT,1,
        supercritical,&path,stats) ||
      closure_pfc_inverse_raw(f,old_v->rho+q*(rho_v-old_v->rho),nT,0,
        supercritical,&path,stats)) return 1;
  }
  return 0;
}

static int closure_pfc_invert_density_local_controls(const ClosurePFCFluid * f,
  double rho,double u,double xi,ClosurePFCCache * cache,double * pressure,
  double * temperature,double ptol,double vtol,double utol,int maximum_iterations,
  ClosurePFCInverseStats * stats) {
  if(!(rho>0.) || !(xi>0. && xi<1.) || !cache->liquid_valid ||
    !cache->vapour_valid || cache->liquid.T>=f->critical_T ||
    cache->vapour.T>=f->critical_T ||
    fabs(cache->liquid.T-cache->vapour.T)>1.e-10*cache->liquid.T) return 1;
  double a=1.-xi,b=xi,vtarget=1./rho,escale=fmax(1.e5,fabs(u));
  ClosurePFCPhase l=cache->liquid,v=cache->vapour;
  double T=l.T;
  for(int k=0;k<maximum_iterations;k++) {
    if(stats) stats->iterations++;
    double pscale=fmax(1.e5,fmax(fabs(l.p),fabs(v.p)));
    double residual=closure_pfc_density_controlled_residual(&l,&v,xi,vtarget,u,
      escale,pscale,ptol,vtol,utol);
    if(residual<1.) {
      /* Use the pressure of the softer phase, avoiding dense-liquid pressure
       * roundoff amplification in a very dilute, highly compressible vapour. */
      double stiffness_l=-1./(l.rho*l.vp),stiffness_v=-1./(v.rho*v.vp);
      *pressure=stiffness_l<stiffness_v?l.p:v.p;*temperature=T;
      cache->liquid=l;cache->vapour=v;
      if(stats) stats->fast_queries++;
      return 0;
    }
    double plT=-l.vT/l.vp,pvT=-v.vT/v.vp;
    double J[3][3]={
      {-1./(l.rho*l.vp)/pscale,1./(v.rho*v.vp)/pscale,T*(plT-pvT)/pscale},
      {-a*l.v/vtarget,-b*v.v/vtarget,0.},
      {a*(l.p-T*plT)*l.v/escale,b*(v.p-T*pvT)*v.v/escale,
       T*(a*l.cv+b*v.cv)/escale}
    };
    double rhs[3]={-(l.p-v.p)/pscale,-(a*l.v+b*v.v-vtarget)/vtarget,
      -(a*l.u+b*v.u-u)/escale},step[3]={0.};
    if(closure_pfc_solve3(J,rhs,step)) return 2;
    double trust=fmax(fmax(fabs(step[0])/.25,fabs(step[1])/.25),fabs(step[2])/.025);
    if(trust>1.) for(int j=0;j<3;j++) step[j]/=trust;
    int accepted=0;
    for(int j=0;j<28;j++) {
      double factor=ldexp(1.,-j),nT=T*exp(factor*step[2]);
      double nl=l.rho*exp(factor*step[0]),nv=v.rho*exp(factor*step[1]);
      ClosurePFCPhase trial_l,trial_v;
      if(!closure_pfc_inverse_density_path(f,&l,&v,nl,nv,nT,0,
          &trial_l,&trial_v,stats) &&
        closure_pfc_density_controlled_residual(&trial_l,&trial_v,xi,vtarget,u,
          escale,pscale,ptol,vtol,utol)<residual) {
        l=trial_l;v=trial_v;T=nT;accepted=1;break;
      }
    }
    if(!accepted) return 5;
  }
  return 6;
}

static int closure_pfc_invert_density_local(const ClosurePFCFluid * f,
  double rho,double u,double xi,ClosurePFCCache * cache,double * pressure,
  double * temperature,double tolerance,int maximum_iterations,
  ClosurePFCInverseStats * stats) {
  return closure_pfc_invert_density_local_controls(f,rho,u,xi,cache,pressure,
    temperature,tolerance,tolerance,tolerance,maximum_iterations,stats);
}

static int closure_pfc_invert_endpoint_local(const ClosurePFCFluid * f,
  double rho,double u,double xi,ClosurePFCCache * cache,double * pressure,
  double * temperature,double tolerance,int maximum_iterations,
  ClosurePFCInverseStats * stats) {
  if(!(xi==0. || xi==1.)) return 1;
  int liquid=xi==0.;
  ClosurePFCPhase previous=liquid?cache->liquid:cache->vapour;
  if(!(liquid?cache->liquid_valid:cache->vapour_valid)) return 1;
  int supercritical=previous.T>=f->critical_T;
  double T=previous.T,escale=fmax(1.e5,fabs(u));
  ClosurePFCPhase s;
  /* Target density must be reachable along the same sampled stable component. */
  for(int j=1;j<=8;j++) {
    if(closure_pfc_inverse_raw(f,previous.rho+(rho-previous.rho)*j/8.,T,
        liquid,supercritical,&s,stats)) return 2;
  }
  for(int k=0;k<maximum_iterations;k++) {
    if(stats) stats->iterations++;
    if(closure_pfc_inverse_raw(f,rho,T,liquid,supercritical,&s,stats)) return 2;
    double residual=s.u-u;
    if(fabs(residual)/escale<tolerance) {
      *pressure=s.p;*temperature=T;
      if(liquid) {cache->liquid=s;cache->liquid_valid=1;}
      else {cache->vapour=s;cache->vapour_valid=1;}
      if(stats) stats->fast_queries++;
      return 0;
    }
    double dT=-residual/s.cv;
    int accepted=0;
    for(int j=0;j<28;j++) {
      double factor=ldexp(1.,-j),nT=T+factor*dT;
      if(!(nT>0.) || fabs(nT-T)>.025*T) continue;
      ClosurePFCPhase trial;
      if(closure_pfc_inverse_raw(f,rho,nT,liquid,supercritical,&trial,stats)) continue;
      int connected=1;
      for(int n=1;n<8;n++) {
        ClosurePFCPhase path;
        if(closure_pfc_inverse_raw(f,rho,T+(nT-T)*n/8.,liquid,
            supercritical,&path,stats)) {connected=0;break;}
      }
      if(connected && fabs(trial.u-u)<fabs(residual)) {T=nT;accepted=1;break;}
    }
    if(!accepted) return 5;
  }
  return 6;
}

static int closure_pfc_invert_conserved(const ClosurePFCFluid * f,
  double rho,double u,double xi,ClosurePFCCache * cache,double * pressure,
  double * temperature,double tolerance,int maximum_iterations,
  ClosurePFCInverseStats * stats) {
  if(!(rho>0.) || !(xi>=0. && xi<=1.)) return 1;
  ClosurePFCCache trial=*cache;
  double p=*pressure,T=*temperature;
  int status=(xi==0. || xi==1.)?
    closure_pfc_invert_endpoint_local(f,rho,u,xi,&trial,&p,&T,tolerance,
      maximum_iterations,stats):
    closure_pfc_invert_density_local(f,rho,u,xi,&trial,&p,&T,tolerance,
      maximum_iterations,stats);
  if(!status) {*cache=trial;*pressure=p;*temperature=T;return 0;}
  if(stats) stats->fallback_queries++;
  return closure_pfc_invert_cached(f,rho,u,xi,cache,pressure,temperature,
    tolerance,maximum_iterations);
}

static int closure_pfc_invert_conserved_controls(const ClosurePFCFluid * f,
  double rho,double u,double xi,ClosurePFCCache * cache,double * pressure,
  double * temperature,double ptol,double vtol,double utol,int maximum_iterations,
  ClosurePFCInverseStats * stats) {
  if(!(rho>0.) || !(xi>=0. && xi<=1.) || !(ptol>0. && vtol>0. && utol>0.)) return 1;
  ClosurePFCCache trial=*cache;
  double p=*pressure,T=*temperature;
  int status=(xi==0. || xi==1.)?
    closure_pfc_invert_endpoint_local(f,rho,u,xi,&trial,&p,&T,utol,
      maximum_iterations,stats):
    closure_pfc_invert_density_local_controls(f,rho,u,xi,&trial,&p,&T,
      ptol,vtol,utol,maximum_iterations,stats);
  if(!status) {*cache=trial;*pressure=p;*temperature=T;return 0;}
  if(stats) stats->fallback_queries++;
  /* The same-potential PT fallback preserves fixed rho/u/xi. Its common PT
   * branch roots are subject to the independently saved raw pressure check. */
  return closure_pfc_invert_cached(f,rho,u,xi,cache,pressure,temperature,
    fmin(vtol,utol),maximum_iterations);
}
#endif
