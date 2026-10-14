/* Conservative pressure-work/equilibrium projection. Original task-local
 * finite-volume implementation of root PRESSURE_WORK_AND_PROJECTION.md.
 * Every trial starts from unchanged post-advection physical targets. */
#ifndef CLOSURE_PRESSURE_WORK_FV_H
#define CLOSURE_PRESSURE_WORK_FV_H
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include "mechanical_relaxation.h"

typedef struct {
  double a,b,mw,mf,q,ew,ef;
} ClosureFlowZone;
typedef struct {
  unsigned long iterations;
  double final_residual,work_defect,mechanical_entropy;
  double minimum_mechanical_entropy,energy_increment_residual;
} ClosurePressureStats;

static double closure_flow_kinetic(const ClosureFlowZone * s) {
  return .5*s->q*s->q/(s->mw+s->mf);
}

static int closure_flow_equilibrate(ClosureFlowZone * s,
  ClosureMaterialEOS water,const void * wc,ClosureMaterialEOS pfc,const void * fc,
  double * pressure,double * sound_speed,double * entropy,double * source_entropy) {
  double kinetic=closure_flow_kinetic(s),rho=s->mw+s->mf;
  double uw=s->ew-(s->mw/rho)*kinetic,uf=s->ef-(s->mf/rho)*kinetic;
  ClosureMaterialState w={0},f={0};
  *source_entropy=0.;
  if(s->mw==0.) {
    if(s->a!=0. || s->b!=1. || pfc(fc,s->mf,uf/s->mf,&f)) return 1;
    *pressure=f.p;*sound_speed=sqrt(f.c2);*entropy=s->mf*f.s;
    return 0;
  }
  if(s->mf==0.) {
    if(s->a!=1. || s->b!=0. || water(wc,s->mw,uw/s->mw,&w)) return 1;
    *pressure=w.p;*sound_speed=sqrt(w.c2);*entropy=s->mw*w.s;
    return 0;
  }
  if(!(s->a>0. && s->b>0.)) return 2;
  ClosureMechanicalCell mixture={s->a,s->b,s->mw,s->mf,uw,uf};
  ClosureMechanicalResult statistics={0};
  if(closure_mechanical_relax(&mixture,water,wc,pfc,fc,1.e-12,1.e-11,400,&statistics)) {
    fprintf(stderr,"mechanical source failure status=%d a=%.17g b=%.17g mw=%.17g mf=%.17g uw=%.17g uf=%.17g gap=%.17g steps=%d rejected=%d\n",
      statistics.status,s->a,s->b,s->mw,s->mf,uw,uf,
      statistics.final_relative_pressure_gap,statistics.steps,statistics.rejected_steps);
    return 3;
  }
  s->a=mixture.water_fraction;s->b=mixture.pfc_fraction;
  s->ew=mixture.water_internal_energy_density+(s->mw/rho)*kinetic;
  s->ef=mixture.pfc_internal_energy_density+(s->mf/rho)*kinetic;
  if(water(wc,s->mw/s->a,mixture.water_internal_energy_density/s->mw,&w) ||
     pfc(fc,s->mf/s->b,mixture.pfc_internal_energy_density/s->mf,&f)) return 4;
  *pressure=.5*(w.p+f.p);
  double modulus=1./(s->a/(s->mw/s->a*w.c2)+s->b/(s->mf/s->b*f.c2));
  *sound_speed=sqrt(modulus/rho);*entropy=s->mw*w.s+s->mf*f.s;
  *source_entropy=statistics.integrated_entropy_source;
  return 0;
}

/* Periodic uniform-grid projection for the initial core verification. The
 * production geometric driver must provide metric-consistent face/cell
 * operators and preserve the same trial/residual/work contract. */
static int closure_pressure_project_periodic_1d(int n,double dx,double dt,
  const ClosureFlowZone * advected,const double * pressure_seed,
  ClosureFlowZone * accepted,double * pressure,double * face_velocity,
  ClosureMaterialEOS water,const void * wc,ClosureMaterialEOS pfc,const void * fc,
  double tolerance,int maximum_iterations,ClosurePressureStats * stats) {
  double * trial_p=malloc(n*sizeof(double)),* new_p=malloc(n*sizeof(double));
  double * face_p=malloc(n*sizeof(double)),* face_u=malloc(n*sizeof(double));
  double * sound=malloc(n*sizeof(double)),* entropy=malloc(n*sizeof(double));
  double * sources=malloc(n*sizeof(double));
  ClosureFlowZone * trial=malloc(n*sizeof(ClosureFlowZone));
  if(!trial_p || !new_p || !face_p || !face_u || !sound || !entropy || !sources || !trial) return 10;
  memcpy(trial_p,pressure_seed,n*sizeof(double));
  int status=6;
  for(int iteration=0;iteration<maximum_iterations;iteration++) {
    if(stats) stats->iterations++;
    for(int j=0;j<n;j++) {
      int left=(j+n-1)%n;
      double rl=advected[left].mw+advected[left].mf,rr=advected[j].mw+advected[j].mf;
      face_p[j]=.5*(trial_p[left]+trial_p[j]);
      face_u[j]=.5*(advected[left].q/rl+advected[j].q/rr)-
        dt*2./(rl+rr)*(trial_p[j]-trial_p[left])/dx;
    }
    double residual=0.,work_defect=0.,source_sum=0.,source_min=0.,increment_error=0.;
    for(int j=0;j<n;j++) {
      int right=(j+1)%n;
      trial[j]=advected[j];
      trial[j].q-=dt*(face_p[right]-face_p[j])/dx;
      double de=-dt*(face_p[right]*face_u[right]-face_p[j]*face_u[j])/dx;
      double dk=closure_flow_kinetic(&trial[j])-closure_flow_kinetic(&advected[j]);
      double rho=advected[j].mw+advected[j].mf,yw=advected[j].mw/rho,yf=advected[j].mf/rho;
      double dew=advected[j].a*de+(yw-advected[j].a)*dk;
      double def=advected[j].b*de+(yf-advected[j].b)*dk;
      trial[j].ew+=dew;trial[j].ef+=def;
      increment_error+=fabs(dew+def-de)*dx;
      double divergence=(face_u[right]-face_u[j])/dx;
      work_defect+=fabs(de-dk+dt*trial_p[j]*divergence)*dx;
      if(closure_flow_equilibrate(&trial[j],water,wc,pfc,fc,&new_p[j],
          &sound[j],&entropy[j],&sources[j])) {status=3;goto finish;}
      double pscale=fmax(1.,fmax(fabs(new_p[j]),fabs(trial_p[j])));
      residual=fmax(residual,fabs(new_p[j]-trial_p[j])/pscale);
      source_sum+=sources[j]*dx;source_min=fmin(source_min,sources[j]);
    }
    if(stats) {
      stats->final_residual=residual;stats->work_defect=work_defect;
      stats->mechanical_entropy=source_sum;
      stats->minimum_mechanical_entropy=source_min;
      stats->energy_increment_residual=increment_error;
    }
    if(residual<tolerance) {
      memcpy(accepted,trial,n*sizeof(ClosureFlowZone));
      /* Accepted EOS pressure is the result; face velocity was computed from
       * the final trial pressure whose EOS residual is explicitly bounded. */
      memcpy(pressure,new_p,n*sizeof(double));memcpy(face_velocity,face_u,n*sizeof(double));
      status=0;goto finish;
    }
    /* Underrelaxation is a numerical iteration, not an EOS state reset. */
    for(int j=0;j<n;j++) trial_p[j]=new_p[j];
  }
finish:
  free(trial_p);free(new_p);free(face_p);free(face_u);free(sound);
  free(entropy);free(sources);free(trial);return status;
}
#endif
