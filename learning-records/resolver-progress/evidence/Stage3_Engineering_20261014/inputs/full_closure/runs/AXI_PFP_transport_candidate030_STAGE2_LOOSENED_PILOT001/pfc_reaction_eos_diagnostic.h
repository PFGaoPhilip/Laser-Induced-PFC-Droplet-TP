/* EOS_DIAGNOSTIC_001_BEGIN */#include "eos_diagnostic_api.h"
/* EOS_DIAGNOSTIC_001_END *//* Original conditional PFC phase-source candidate. Not production accepted.
 * All reaction substeps conserve material rho and specific internal energy.
 * No EOS switch, latent-energy addition, pressure floor or fraction clipping.
 * Source defaults must be preregistered before affected production tests.
 */
#ifndef CLOSURE_PFC_REACTION_H
#define CLOSURE_PFC_REACTION_H
#include <stdlib.h>
#include "pfc_helmholtz_eos_diagnostic.h"
#include "pfc_spinodal_cache_eos_diagnostic.h"

typedef struct {
  double alpha_condensation,area_per_mass; /* 1, m2/kg; area is actual outer A/M */
  double birth_pressure,spinodal_distance_onset,reference_time; /* Pa,1,s */
  double eos_tolerance,xi_tolerance;
  double entropy_quadrature_absolute,entropy_quadrature_relative,time_quadrature_absolute,time_quadrature_relative;
  double primitive_entropy_agreement;
  int eos_iterations,continuation_iterations,root_iterations,path_samples;
  int quadrature_max_depth;unsigned long quadrature_max_nodes;
  ClosurePFCSpinodalCache * spinodal_cache; /* optional caller-owned; NULL is accepted007 reference */
} ClosurePFCReactionParameters;

typedef struct {
  double hks_rate,bulk_rate,unprojected_rate,rate,entropy_rate_specific;
  double affinity_scaled,beta,lambda_birth,lambda_spin;
  double liquid_spinodal_rho,vapour_spinodal_rho,liquid_distance,vapour_distance;
  double p_xi,T_xi;
  int liquid_available,vapour_available,coalesced,endpoint_projected,endpoint_incoming_limit;
} ClosurePFCReactionRate;

typedef struct {
  ClosurePFCMixture state;
  ClosurePFCCache eos_cache;
  double xi_before,xi_after,specific_entropy_change,source_entropy_path;
  double source_entropy_HKS,source_entropy_bulk,source_path_time;
  double entropy_primitive_remainder,entropy_quadrature_error,time_quadrature_error;
  double eos_volume_residual,eos_energy_residual,implicit_composition_residual;
  double root_bracket_lower,root_bracket_upper,root_residual_lower,root_residual_upper;
  double root_bracket_width;
  double canonical_entropy_change,canonical_energy_relative_change,canonical_volume_relative_change;
  unsigned long evaluations,rejected_trials;
  unsigned long quadrature_nodes,quadrature_panels;
  int endpoint_complementarity,canonical_supercritical_label,root_iterations;
  int numerical_sign_bracket,raw_residual_above_coordinate_target;
} ClosurePFCReactionStep;

static ClosurePFCReactionParameters closure_pfc_reaction_defaults(void) {
  ClosurePFCReactionParameters p={0};
  p.alpha_condensation=.3;p.area_per_mass=0.;
  p.birth_pressure=10132.5;p.spinodal_distance_onset=.05;p.reference_time=1.e-9;
  p.eos_tolerance=1.e-11;p.xi_tolerance=1.e-14;
  p.eos_iterations=60;p.continuation_iterations=256;p.root_iterations=80;p.path_samples=8;
  p.entropy_quadrature_absolute=1.e-9;p.entropy_quadrature_relative=1.e-9;
  p.time_quadrature_absolute=1.e-30;p.time_quadrature_relative=1.e-8;p.primitive_entropy_agreement=1.e-6;
  p.quadrature_max_depth=24;p.quadrature_max_nodes=65536;
  return p;
}

static double closure_pfc_reaction_K_eos_diagnostic_original(const ClosurePFCFluid * f,double rho,double T) {
  ClosureHelmholtzJet a,r;double d=rho/f->rhoc;
  if(closure_pfc_potential(f,d,f->Tc/T,&a,&r)) return NAN;
  return 1.+2.*d*r.d+d*d*r.dd;
}/* EOS_DIAGNOSTIC_001_BEGIN */
static double closure_pfc_reaction_K(const ClosurePFCFluid * f,double rho,double T) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_SPINODAL_K);
  double value=closure_pfc_reaction_K_eos_diagnostic_original(f,rho,T);
  closure_eos_diag_leave(token,!isfinite(value));
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

/* Locate the first mechanical stability boundary from an already labelled
 * physical stable root toward the critical density. Finite discovery is
 * explicitly not an interval completeness proof. This function does not
 * evaluate a singular cp at the spinodal or replace its mechanical derivative.
 */
static int closure_pfc_reaction_spinodal_eos_diagnostic_original(const ClosurePFCFluid * f,
  const ClosurePFCPhase * phase,int liquid,double * rho_spinodal) {
  if(!(phase->T<f->critical_T) ||
     (liquid?phase->rho<=f->critical_rho:phase->rho>=f->critical_rho)) return 1;
  double previous=phase->rho,kprevious=closure_pfc_reaction_K(f,previous,phase->T);
  if(!(kprevious>0.)) return 2;
  for(int i=1;i<=512;i++) {
    double current=phase->rho+(f->critical_rho-phase->rho)*i/512.;
    double kcurrent=closure_pfc_reaction_K(f,current,phase->T);
    if(!isfinite(kcurrent)) return 2;
    if(kcurrent<=0.) {
      double stable=previous,unstable=current;
      for(int j=0;j<80;j++) {
        double mid=.5*(stable+unstable),value=closure_pfc_reaction_K(f,mid,phase->T);
        if(!isfinite(value)) return 2;
        if(value>0.)stable=mid;else unstable=mid;
        if(fabs(stable-unstable)<=1.e-13*fmax(stable,unstable))break;
      }
      *rho_spinodal=.5*(stable+unstable);return 0;
    }
    previous=current;kprevious=kcurrent;
  }
  return 3; /* physical topology/discovery unresolved; never a synthetic root */
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_reaction_spinodal(const ClosurePFCFluid * f,
  const ClosurePFCPhase * phase,int liquid,double * rho_spinodal) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_SPINODAL_DISCOVERY);
  int value=closure_pfc_reaction_spinodal_eos_diagnostic_original(f,phase,liquid,rho_spinodal);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_pfc_reaction_rates(const ClosurePFCFluid * f,
  const ClosurePFCMixture * m,const ClosurePFCReactionParameters * par,
  ClosurePFCReactionRate * r) {
  memset(r,0,sizeof(*r));
  if(!(par->alpha_condensation>=0. && par->alpha_condensation<=1.) ||
     !(par->area_per_mass>=0.) || !(par->reference_time>0.) ||
     !(par->birth_pressure>0.) || !(par->spinodal_distance_onset>0.)) return 1;
  r->liquid_available=m->liquid_available;r->vapour_available=m->vapour_available;
  r->coalesced=m->coalesced;
  if(m->coalesced || !m->liquid_available || !m->vapour_available)return 0;
  if(!(m->p>0.) || !(m->T>0.)) return 2;
  /* Remove only the endpoint rate projection for the implicit normal-cone
   * residual. Thermodynamic phase properties and actual xi stay unchanged.
   */
  ClosurePFCMixture kinetic=*m;kinetic.xi=.5;
  double j=0.,sigma=0.;
  if(closure_pfc_kinetic_flux(f,&kinetic,par->alpha_condensation,&j,&sigma))return 3;
  r->hks_rate=par->area_per_mass*j;
  double affinity=m->liquid.g-m->vapour.g;
  r->affinity_scaled=affinity/(f->R*m->T);r->beta=tanh(r->affinity_scaled);
  if(closure_pfc_spinodal_cached(f,&m->liquid,1,par->spinodal_cache,closure_pfc_reaction_spinodal,&r->liquid_spinodal_rho) ||
     closure_pfc_spinodal_cached(f,&m->vapour,0,par->spinodal_cache,closure_pfc_reaction_spinodal,&r->vapour_spinodal_rho))return 4;
  r->liquid_distance=m->liquid.rho/r->liquid_spinodal_rho-1.;
  r->vapour_distance=1.-m->vapour.rho/r->vapour_spinodal_rho;
  double distance=m->xi==0.?r->liquid_distance:m->xi==1.?r->vapour_distance:
    fmin(r->liquid_distance,r->vapour_distance);
  if(!(distance>0.))return 5;
  r->lambda_spin=fmax(0.,pow(par->spinodal_distance_onset/distance,2.)-1.)/par->reference_time;
  r->lambda_birth=m->xi<1.?fmax(0.,pow(par->birth_pressure/m->p,2.)-1.)/par->reference_time:0.;
  r->bulk_rate=(r->lambda_spin+r->lambda_birth)*r->beta;
  r->unprojected_rate=r->hks_rate+r->bulk_rate;
  /* An outward endpoint value may be represented by the interior incoming
   * limit for the implicit normal-cone inequality. Projection still makes the
   * physical instantaneous rate exactly zero. This handles finite phase
   * extinction, without clipping or a p/T/u/s reset when a guard switches off
   * as a populated mass becomes exactly zero. Inward endpoint rates retain
   * their declared populated-phase guard definition.
   */
  if((m->xi==0. && r->beta<0.) || (m->xi==1. && r->beta>0.)) {
    double di=fmin(r->liquid_distance,r->vapour_distance);
    double ls=fmax(0.,pow(par->spinodal_distance_onset/di,2.)-1.)/par->reference_time;
    double lp=fmax(0.,pow(par->birth_pressure/m->p,2.)-1.)/par->reference_time;
    r->unprojected_rate=r->hks_rate+(ls+lp)*r->beta;
    r->endpoint_incoming_limit=1;
  }
  r->rate=r->unprojected_rate;
  if((m->xi==0. && r->rate<0.) || (m->xi==1. && r->rate>0.)) {
    r->rate=0.;r->endpoint_projected=1;
  }
  r->entropy_rate_specific=affinity/m->T*r->rate;
  double D=m->vp*m->cv,dv=m->vapour.v-m->liquid.v,dh=m->vapour.h-m->liquid.h;
  r->p_xi=-(m->cp*dv-m->vT*dh)/D;
  r->T_xi=-(m->T*m->vT*dv+m->vp*dh)/D;
  if(!isfinite(r->rate+r->entropy_rate_specific+r->p_xi+r->T_xi) ||
     r->entropy_rate_specific<0.)return 6;
  return 0;
}

static int closure_pfc_reaction_trial(const ClosurePFCFluid * f,double rho,double u,
  double xi,const ClosurePFCMixture * previous,const ClosurePFCCache * cache,
  const ClosurePFCReactionParameters * par,ClosurePFCMixture * after,
  ClosurePFCCache * after_cache,ClosurePFCReactionRate * rate) {
  if(!(xi>=0. && xi<=1.))return 1;
  *after_cache=*cache;double p=previous->p,T=previous->T;
  if(closure_pfc_invert_cached(f,rho,u,xi,after_cache,&p,&T,
                             par->eos_tolerance,par->eos_iterations))return 2;
  if(closure_pfc_mixture_PT_cached(f,p,T,xi,after_cache,after))return 3;
  return closure_pfc_reaction_rates(f,after,par,rate);
}

/* Independent local Gibbs-source quadrature along the already selected fixed
 * rho/u path. Four signed integrands: entropy,HKS share,bulk share,path time.
 * Endpoint rates here are ONE-SIDED INTERIOR LIMITS only for integration;
 * actual blocked endpoint source remains zero in closure_pfc_reaction_rates.
 * No primitive subtraction is clipped or assigned to physical destruction.
 */
typedef struct {
  ClosurePFCMixture state;ClosurePFCCache cache;double x,value[4];
} ClosurePFCReactionQuadPoint;

typedef struct {
  const ClosurePFCFluid * fluid;const ClosurePFCReactionParameters * parameters;
  double rho,u,direction;ClosurePFCReactionStep * output;
} ClosurePFCReactionQuadrature;

static int closure_pfc_reaction_quad_values(ClosurePFCReactionQuadrature * context,
  ClosurePFCReactionQuadPoint * q) {
  ClosurePFCMixture interior=q->state;interior.xi=.5;
  ClosurePFCReactionRate rate;
  if(closure_pfc_reaction_rates(context->fluid,&interior,context->parameters,&rate))return 1;
  if(interior.coalesced || !interior.liquid_available || !interior.vapour_available ||
     !(context->direction*rate.unprojected_rate>0.))return 2;
  double affinity=(q->state.liquid.g-q->state.vapour.g)/q->state.T;
  if(!(context->direction*affinity>=0.))return 3;
  q->value[0]=affinity;
  q->value[1]=affinity*rate.hks_rate/rate.unprojected_rate;
  q->value[2]=affinity*(rate.unprojected_rate-rate.hks_rate)/rate.unprojected_rate;
  q->value[3]=1./rate.unprojected_rate;
  context->output->quadrature_nodes++;
  if(context->output->quadrature_nodes>context->parameters->quadrature_max_nodes)return 4;
  return 0;
}

static int closure_pfc_reaction_quad_point(ClosurePFCReactionQuadrature * context,double x,
  const ClosurePFCReactionQuadPoint * warm,ClosurePFCReactionQuadPoint * result) {
  result->cache=warm->cache;double p=warm->state.p,T=warm->state.T;
  if(closure_pfc_invert_cached(context->fluid,context->rho,context->u,x,&result->cache,
      &p,&T,context->parameters->eos_tolerance,context->parameters->eos_iterations) ||
     closure_pfc_mixture_PT_cached(context->fluid,p,T,x,&result->cache,&result->state))return 1;
  result->x=x;context->output->evaluations++;
  return closure_pfc_reaction_quad_values(context,result);
}

static void closure_pfc_reaction_simpson(const ClosurePFCReactionQuadPoint * a,
  const ClosurePFCReactionQuadPoint * m,const ClosurePFCReactionQuadPoint * b,double values[4]) {
  for(int k=0;k<4;k++)values[k]=(b->x-a->x)*(a->value[k]+4.*m->value[k]+b->value[k])/6.;
}

typedef struct {
  ClosurePFCReactionQuadPoint a,m,b,l,r;double integral[4],error[4];int depth;
} ClosurePFCReactionQuadPanel;

static int closure_pfc_reaction_quad_measure(ClosurePFCReactionQuadrature * context,
  const ClosurePFCReactionQuadPoint * a,const ClosurePFCReactionQuadPoint * m,
  const ClosurePFCReactionQuadPoint * b,int depth,ClosurePFCReactionQuadPanel * panel) {
  panel->a=*a;panel->m=*m;panel->b=*b;panel->depth=depth;
  if(closure_pfc_reaction_quad_point(context,.5*(a->x+m->x),a,&panel->l) ||
     closure_pfc_reaction_quad_point(context,.5*(m->x+b->x),m,&panel->r))return 1;
  double coarse[4],left[4],right[4];
  closure_pfc_reaction_simpson(a,m,b,coarse);
  closure_pfc_reaction_simpson(a,&panel->l,m,left);closure_pfc_reaction_simpson(m,&panel->r,b,right);
  for(int k=0;k<4;k++) {
    panel->integral[k]=left[k]+right[k];
    panel->error[k]=fabs(panel->integral[k]-coarse[k])/15.;
  }
  return 0;
}

/* Global-error adaptive positive Simpson sum. Refining the largest scaled
 * error panel avoids assigning a vanishing accuracy budget to a tiny onset
 * panel. Every panel estimate contributes to the unchanged full-path target.
 * These estimates do not include all EOS/source noise and are not bounds.
 */
static int closure_pfc_reaction_quad_global(ClosurePFCReactionQuadrature * context,
  const ClosurePFCReactionQuadPoint * a,const ClosurePFCReactionQuadPoint * m,
  const ClosurePFCReactionQuadPoint * b,double integral[4],double errors[4]) {
  size_t count=1,capacity=16;
  ClosurePFCReactionQuadPanel * panels=malloc(capacity*sizeof(*panels));if(!panels)return 4;
  if(closure_pfc_reaction_quad_measure(context,a,m,b,0,&panels[0])){free(panels);return 1;}
  for(;;) {
    for(int k=0;k<4;k++)integral[k]=errors[k]=0.;
    for(size_t j=0;j<count;j++)for(int k=0;k<4;k++){
      integral[k]+=panels[j].integral[k];errors[k]+=panels[j].error[k];
    }
    double targets[4];int pass=1;
    for(int k=0;k<4;k++){
      targets[k]=(k==3?context->parameters->time_quadrature_absolute:
        context->parameters->entropy_quadrature_absolute)+
        (k==3?context->parameters->time_quadrature_relative:
        context->parameters->entropy_quadrature_relative)*fabs(integral[k]);
      if(errors[k]>targets[k])pass=0;
    }
    if(pass){context->output->quadrature_panels=count;free(panels);return 0;}
    size_t worst=0;double worst_score=-1.;
    for(size_t j=0;j<count;j++)for(int k=0;k<4;k++)if(errors[k]>targets[k]){
      double score=panels[j].error[k]/targets[k];
      if(score>worst_score){worst_score=score;worst=j;}
    }
    if(panels[worst].depth>=context->parameters->quadrature_max_depth){free(panels);return 2;}
    if(count==capacity){
      capacity*=2;ClosurePFCReactionQuadPanel * larger=realloc(panels,capacity*sizeof(*panels));
      if(!larger){free(panels);return 4;}panels=larger;
    }
    ClosurePFCReactionQuadPanel parent=panels[worst];
    if(closure_pfc_reaction_quad_measure(context,&parent.a,&parent.l,&parent.m,parent.depth+1,&panels[worst]) ||
       closure_pfc_reaction_quad_measure(context,&parent.m,&parent.r,&parent.b,parent.depth+1,&panels[count])){
      free(panels);return 1;
    }
    count++;
  }
}

static int closure_pfc_reaction_entropy_integral(const ClosurePFCFluid * f,double rho,double u,
  double x0,double x1,const ClosurePFCMixture * before,const ClosurePFCCache * before_cache,
  const ClosurePFCMixture * after,const ClosurePFCCache * after_cache,
  const ClosurePFCReactionParameters * par,ClosurePFCReactionStep * out) {
  if(x0==x1)return 0;
  ClosurePFCReactionQuadrature context={f,par,rho,u,x1>x0?1.:-1.,out};
  ClosurePFCReactionQuadPoint a={0},b={0},m={0};
  a.x=x0;a.state=*before;a.cache=*before_cache;b.x=x1;b.state=*after;b.cache=*after_cache;
  if(closure_pfc_reaction_quad_values(&context,&a) || closure_pfc_reaction_quad_values(&context,&b) ||
     closure_pfc_reaction_quad_point(&context,.5*(x0+x1),&a,&m))return 1;
  double integral[4],errors[4];
  if(closure_pfc_reaction_quad_global(&context,&a,&m,&b,integral,errors))return 2;
  for(int k=0;k<4;k++)if(!(integral[k]>=0. && isfinite(integral[k])))return 3;
  out->source_entropy_path=integral[0];out->source_entropy_HKS=integral[1];
  out->source_entropy_bulk=integral[2];out->source_path_time=integral[3];
  out->entropy_quadrature_error=fmax(errors[0],fmax(errors[1],errors[2]));
  out->time_quadrature_error=errors[3];return 0;
}

/* One conservative backward-Euler substep on the connected composition path.
 * Search proceeds from xi0 toward the local entropy-increasing direction. A
 * physical endpoint is accepted only by the implicit normal-cone inequality;
 * there is no clipping of an overshot endpoint. Trial failures are returned or
 * locally retried and counted. Caller must refine dt and cannot call a failed
 * step an attained physical state. Numerical path sampling is not a proof of
 * global branch completeness or reaction uniqueness. An interior stop
 * certifies only the width of a numerical sign bracket. The raw residual and
 * EOS/source uncertainty must be independently checked: a stiff raw residual
 * is not a composition error, and this is not interval arithmetic.
 */
static int closure_pfc_reaction_step(const ClosurePFCFluid * f,double rho,double u,
  double xi0,double p0,double T0,double dt,ClosurePFCCache * cache,
  const ClosurePFCReactionParameters * par,ClosurePFCReactionStep * out) {
  memset(out,0,sizeof(*out));out->xi_before=xi0;out->xi_after=xi0;
  if(!(dt>=0.) || !(xi0>=0. && xi0<=1.) || !(rho>0.) ||
     !(par->eos_tolerance>0.) || !(par->xi_tolerance>0.) ||
     !(par->entropy_quadrature_absolute>0.) || !(par->entropy_quadrature_relative>0.) ||
     !(par->time_quadrature_absolute>0.) || !(par->time_quadrature_relative>0.) ||
     !(par->primitive_entropy_agreement>0.) ||
     par->quadrature_max_depth<1 || par->quadrature_max_nodes<5 ||
     par->path_samples<1 || par->root_iterations<1 || par->continuation_iterations<1)return 1;
  ClosurePFCMixture initial;ClosurePFCReactionRate rate0;
  ClosurePFCCache initial_cache=*cache;
  if(closure_pfc_invert_cached(f,rho,u,xi0,&initial_cache,&p0,&T0,
                             par->eos_tolerance,par->eos_iterations) ||
     closure_pfc_mixture_PT_cached(f,p0,T0,xi0,&initial_cache,&initial))return 2;
  out->evaluations++;
  if(closure_pfc_reaction_rates(f,&initial,par,&rate0))return 3;
  ClosurePFCMixture final=initial;ClosurePFCCache final_cache=initial_cache;
  double accepted=xi0,residual=0.;
  if(dt>0. && fabs(dt*rate0.rate)>par->xi_tolerance) {
    double direction=rate0.rate>0.?1.:-1.;
    double a=xi0,Fa=-dt*rate0.unprojected_rate,b=xi0,Fb=Fa;
    ClosurePFCMixture last=initial,right=initial;
    ClosurePFCCache last_cache=initial_cache,right_cache=initial_cache;
    ClosurePFCReactionRate last_rate=rate0,right_rate=rate0;
    int bracketed=0;
    for(int k=0;k<par->continuation_iterations;k++) {
      double increment=.02;
      if(last_rate.p_xi!=0.) increment=fmin(increment,.02*(fabs(last.p)+101325.)/fabs(last_rate.p_xi));
      if(last_rate.T_xi!=0.) increment=fmin(increment,.01*last.T/fabs(last_rate.T_xi));
      increment=fmin(increment,direction>0.?1.-a:a);
      if(!(increment>0.))return 4;
      int good=0;
      for(int reject=0;reject<32;reject++) {
        b=a+direction*increment;
        if(b==a)return 5;
        good=1;
        ClosurePFCMixture path=last;ClosurePFCCache path_cache=last_cache;
        for(int n=1;n<=par->path_samples;n++) {
          double nx=a+(b-a)*n/par->path_samples;
          out->evaluations++;
          if(closure_pfc_reaction_trial(f,rho,u,nx,&path,&path_cache,par,
                                       &right,&right_cache,&right_rate)) {good=0;break;}
          path=right;path_cache=right_cache;
        }
        if(good)break;
        out->rejected_trials++;/* EOS_DIAGNOSTIC_001_BEGIN */closure_eos_diag_note(CLOSURE_EOS_PHASE_SOURCE_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */increment*=.5;
      }
      if(!good)return 6;
      Fb=b-xi0-dt*right_rate.unprojected_rate;
      if(Fa*Fb<=0.) {bracketed=1;break;}
      if((b==1. && Fb<=0.) || (b==0. && Fb>=0.)) {
        accepted=b;final=right;final_cache=right_cache;residual=Fb;
        out->endpoint_complementarity=1;bracketed=2;break;
      }
      a=b;Fa=Fb;last=right;last_cache=right_cache;last_rate=right_rate;
    }
    if(!bracketed)return 7;
    if(bracketed==1) {
      for(int k=0;k<par->root_iterations;k++) {
        double c=.5*(a+b);ClosurePFCMixture trial;ClosurePFCCache trial_cache;
        ClosurePFCReactionRate trial_rate;out->evaluations++;out->root_iterations=k+1;
        /* Warm from a current bracket endpoint, not the now distant original
         * continuation-left state. Both endpoints were reached on the same
         * conserved connected path. A numerical failure retries the SAME
         * target from the opposite endpoint; it never changes EOS or xi. */
        int use_right=fabs(c-b)<=fabs(c-a);
        int trial_status=closure_pfc_reaction_trial(f,rho,u,c,
          use_right?&right:&last,use_right?&right_cache:&last_cache,par,
          &trial,&trial_cache,&trial_rate);
        if(trial_status) {
          out->rejected_trials++;/* EOS_DIAGNOSTIC_001_BEGIN */closure_eos_diag_note(CLOSURE_EOS_PHASE_SOURCE_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */out->evaluations++;
          trial_status=closure_pfc_reaction_trial(f,rho,u,c,
            use_right?&last:&right,use_right?&last_cache:&right_cache,par,
            &trial,&trial_cache,&trial_rate);
          if(trial_status) {out->rejected_trials++;/* EOS_DIAGNOSTIC_001_BEGIN */closure_eos_diag_note(CLOSURE_EOS_PHASE_SOURCE_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */return 8;}
        }
        double Fc=c-xi0-dt*trial_rate.unprojected_rate;
        accepted=c;final=trial;final_cache=trial_cache;residual=Fc;
        if(fabs(b-a)<=par->xi_tolerance) {
          out->numerical_sign_bracket=1;
          out->root_bracket_lower=fmin(a,b);out->root_bracket_upper=fmax(a,b);
          out->root_residual_lower=a<b?Fa:Fb;out->root_residual_upper=a<b?Fb:Fa;
          out->root_bracket_width=fabs(b-a);
          out->raw_residual_above_coordinate_target=fabs(Fc)>par->xi_tolerance;
          break;
        }
        if(Fa*Fc<=0.) {b=c;Fb=Fc;right=trial;right_cache=trial_cache;right_rate=trial_rate;}
        else {a=c;Fa=Fc;last=trial;last_cache=trial_cache;last_rate=trial_rate;}
        if(k==par->root_iterations-1)return 9;
      }
    }
  } else residual=-dt*rate0.rate;
  out->specific_entropy_change=final.s-initial.s;
  if(closure_pfc_reaction_entropy_integral(f,rho,u,xi0,accepted,&initial,&initial_cache,
      &final,&final_cache,par,out))return 13;
  out->entropy_primitive_remainder=out->specific_entropy_change-out->source_entropy_path;
  if(fabs(out->entropy_primitive_remainder)>par->primitive_entropy_agreement)return 14;
  if(final.coalesced) {
    double label=rho>f->critical_rho?0.:rho<f->critical_rho?1.:.5;
    ClosurePFCMixture relabel;
    if(closure_pfc_mixture_PT_cached(f,final.p,final.T,label,&final_cache,&relabel))return 11;
    out->canonical_energy_relative_change=(relabel.u-final.u)/fmax(1.e5,fabs(final.u));
    out->canonical_volume_relative_change=(relabel.v-final.v)/final.v;
    out->canonical_entropy_change=relabel.s-final.s;
    if(fabs(out->canonical_energy_relative_change)>1.e-12 ||
       fabs(out->canonical_volume_relative_change)>1.e-12 ||
       fabs(out->canonical_entropy_change)>1.e-9)return 12;
    accepted=label;final=relabel;out->canonical_supercritical_label=1;
  }
  out->xi_after=accepted;out->state=final;out->eos_cache=final_cache;
  out->eos_volume_residual=(final.v-1./rho)*rho;
  out->eos_energy_residual=(final.u-u)/fmax(1.e5,fabs(u));
  out->implicit_composition_residual=residual;*cache=final_cache;
  return 0;
}
#endif
