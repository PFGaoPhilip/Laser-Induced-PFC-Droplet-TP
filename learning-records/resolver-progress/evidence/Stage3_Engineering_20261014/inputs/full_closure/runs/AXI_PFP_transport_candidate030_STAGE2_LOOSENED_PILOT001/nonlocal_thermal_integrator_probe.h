/* Scalable integration of the unchanged TH09 heat law. No Basilisk dependency.
 * O(nodes+patches) storage/work per evaluation/root iteration, no dense matrix.
 * All occupied nodes remain supplied. The caller's caloric domain is enforced
 * in both EOS directions. Output is transactional for the whole invocation.
 * Frozen-conductance BE is a numerical approximation requiring time refinement;
 * its entropy lower bound is not the physical source-entropy integral.
 */
#ifndef CLOSURE_NONLOCAL_THERMAL_INTEGRATOR_H
#define CLOSURE_NONLOCAL_THERMAL_INTEGRATOR_H
#include "nonlocal_thermal.h"
#include <float.h>
#include <limits.h>
#include <stdint.h>

typedef int (*ClosureHeatTemperatureEOS)(void *,int,double,double *,ClosureHeatState *);
enum {CLOSURE_HEAT_AUTO=0,CLOSURE_HEAT_MIDPOINT=1,CLOSURE_HEAT_FROZEN_BE=2};
typedef struct {
  int mode,max_explicit_steps,max_refinements,max_scalar_iterations,max_mean_iterations;
  double guard_fraction,temperature_tolerance,energy_tolerance,entropy_roundoff;
  double maximum_step,implicit_growth;
  unsigned long maximum_accepted_steps;
  double minimum_mean_root_slope;
} ClosureHeatIntegratorControls;
typedef struct {
  unsigned long evaluations,temperature_queries,scalar_iterations,mean_iterations;
  unsigned long rejected_trials,explicit_steps,implicit_steps,trial_domain_failures;
  unsigned long caloric_signed_brackets,caloric_conditioned_only;
  unsigned long mean_root_probes,energy_root_probes;
  double minimum_guard,energy_defect,entropy_increment,physical_entropy_integral;
  double frozen_entropy_lower_bound,entropy_lower_margin;
  double maximum_row_absolute,maximum_row_conditioned_temperature;
  double maximum_caloric_temperature_width,maximum_caloric_energy_width;
  double maximum_mean_residual,maximum_root_temperature_correction;
  double active_energy_scale,active_entropy_scale;
  double accepted_time,last_step;
  double maximum_energy_root_residual,last_energy_root_residual,last_mean_root_residual;
  double minimum_observed_mean_slope;
  int last_rejection_reason;
  int selected_mode,status;
} ClosureHeatIntegratorStats;

typedef struct {
  const ClosureHeatModel * m;
  ClosureHeatTemperatureEOS temperature_eos;
  const ClosureHeatIntegratorControls * c;
  ClosureHeatIntegratorStats * stats;
  double * allocation,*E,*candidate,*half,*power,*other_power,*C,*D;
  double * old_E,*root_E,*derivative;
  ClosureHeatState * state_allocation,*state,*old_state,*root_state,*stage;
  long double W,CA;
} ClosureHeatIntegratorWorkspace;

static int closure_heat_integrator_state_valid(const ClosureHeatState * s) {
  return s->temperature>0. && s->capacity>0. &&
    isfinite(s->temperature) && isfinite(s->capacity) && isfinite(s->entropy);
}
static int closure_heat_integrator_temperature(ClosureHeatIntegratorWorkspace * w,
  int node,double T,double * E,ClosureHeatState * s) {
  w->stats->temperature_queries++;
  if(!(T>0.) || !isfinite(T) ||
     w->temperature_eos(w->m->eos_context,node,T,E,s) ||
     !isfinite(*E) || !closure_heat_integrator_state_valid(s) ||
     fabs(s->temperature-T)>w->c->temperature_tolerance*fmax(1.,fabs(T))) {
    w->stats->trial_domain_failures++; return 1;
  }
  return 0;
}
static int closure_heat_integrator_evaluate(ClosureHeatIntegratorWorkspace * w,
  const ClosureHeatModel * m,const double * E,ClosureHeatState * s,double * P,
  ClosureHeatDiagnostics * d) {
  w->stats->evaluations++;
  int status=closure_heat_evaluate(m,E,s,P,d);
  if(status) w->stats->trial_domain_failures++;
  return status;
}

/* Patch elimination and shared-water grouping. F row upper bound avoids a
 * potentially ill-conditioned subtraction of tiny other-node weights. */
static int closure_heat_integrator_graph(ClosureHeatIntegratorWorkspace * w,
  const ClosureHeatDiagnostics * d,const ClosureHeatState * s,double * guard) {
  const ClosureHeatModel * m=w->m; w->W=d->measured_weight_sum; w->CA=0.L;
  memset(w->D,0,(size_t)m->nodes*sizeof(double));
  *guard=DBL_MAX;
  if(!m->pfc_nodes) return 0;
  if(!(d->radius>0.) || !(d->conductivity>0.) || !(w->W>0.L)) return 1;
  long double length=(long double)d->radius/acosl(-1.L);
  for(int k=0;k<m->patches;k++) {
    const ClosureHeatPatch * p=m->patch+k;
    long double C=(long double)d->conductivity*p->area/length;
    long double G=p->water_conductance,total=w->W*C+G;
    if(C<0.L || G<0.L || !isfinite(C+G) || !isfinite(total)) return 1;
    w->C[k]=(double)C; w->CA+=C;
    if(total>0.L) w->D[p->water_node]+=(double)(w->W*C*G/total);
  }
  if(!isfinite(w->CA)) return 1;
  for(int a=0;a<m->nodes;a++) {
    long double outgoing=a<m->pfc_nodes?
      (long double)m->node[a].mass/m->inventory*w->CA:w->D[a];
    if(outgoing>0.L) {
      long double local=(long double)w->c->guard_fraction*s[a].capacity/outgoing;
      if(!(local>0.L) || !isfinite(local) || local<DBL_MIN) return 2;
      if(local<*guard) *guard=(double)local;
    }
  }
  if(*guard<DBL_MAX && (w->stats->minimum_guard==0. ||
                       *guard<w->stats->minimum_guard)) w->stats->minimum_guard=*guard;
  return 0;
}
static void closure_heat_integrator_scales(ClosureHeatIntegratorWorkspace * w,
  const ClosureHeatState * s,long double * energy,long double * entropy,
  double * Tmin,double * Tmax) {
  *energy=*entropy=0.L; *Tmin=DBL_MAX; *Tmax=0.;
  for(int a=0;a<w->m->nodes;a++)
    if((a<w->m->pfc_nodes && w->CA>0.L) || w->D[a]>0.) {
      *energy+=(long double)s[a].capacity*s[a].temperature;
      *entropy+=s[a].capacity;
      if(s[a].temperature<*Tmin) *Tmin=s[a].temperature;
      if(s[a].temperature>*Tmax) *Tmax=s[a].temperature;
    }
}

/* Solve E(T)-Eold+hD(T-target)=0 on an actual signed connected bracket.
 * An inaccessible far target is shortened toward a known valid state; it is
 * not itself accepted as physical failure. No caloric-energy offset is added. */
static int closure_heat_integrator_caloric(ClosureHeatIntegratorWorkspace * w,
  int node,double target,long double hD,double * E,ClosureHeatState * s) {
  const ClosureHeatState old=w->old_state[node];
  if(hD==0.L) {*E=w->old_E[node];*s=old;return 0;}
  double T=old.temperature,e;ClosureHeatState state;
  if(closure_heat_integrator_temperature(w,node,T,&e,&state)) return 1;
  long double f=(long double)e-w->old_E[node]+hD*((long double)T-target);
  long double denom=state.capacity+hD;
  double tol=w->c->temperature_tolerance*fmax(1.,fabs(T));
  double lo=T,hi=T,elo=e,ehi=e;long double flo=f,fhi=f;
  ClosureHeatState slo=state,shi=state;
  if(fabsl(f)/denom<=tol) goto solved;
  /* The normal target has opposite sign by caloric monotonicity. If an
   * inverse roundoff mismatch is larger than the source, a nearby Newton
   * target is used instead, without shifting the physical energy. */
  double endpoint=target;
  if((f>0.L && !(target<T)) || (f<0.L && !(target>T)))
    endpoint=T-(double)(f/denom)*2.;
  if(!(endpoint>0.) || endpoint==T || !isfinite(endpoint)) return 2;
  double valid=T,invalid=endpoint,probe=endpoint;
  int found=0;
  for(int k=0;k<w->c->max_scalar_iterations;k++) {
    w->stats->scalar_iterations++;
    double ep;ClosureHeatState sp;
    if(closure_heat_integrator_temperature(w,node,probe,&ep,&sp)) {
      invalid=probe; probe=valid+.5*(invalid-valid);
      if(probe==valid || probe==invalid) return 3;
      continue;
    }
    long double fp=(long double)ep-w->old_E[node]+hD*((long double)probe-target);
    if((f<=0.L && fp>=0.L) || (f>=0.L && fp<=0.L)) {
      if(probe<T) {lo=probe;elo=ep;flo=fp;slo=sp;hi=T;ehi=e;fhi=f;shi=state;}
      else {lo=T;elo=e;flo=f;slo=state;hi=probe;ehi=ep;fhi=fp;shi=sp;}
      found=1;break;
    }
    valid=probe;
    probe=valid+.5*(invalid-valid);
    if(probe==valid || probe==invalid) return 3;
  }
  if(!found || !(flo<=0.L && fhi>=0.L)) return 4;
  T=lo+.5*(hi-lo);
  for(int k=0;k<w->c->max_scalar_iterations;k++) {
    w->stats->scalar_iterations++;
    if(closure_heat_integrator_temperature(w,node,T,&e,&state)) return 5;
    f=(long double)e-w->old_E[node]+hD*((long double)T-target);
    denom=state.capacity+hD;
    tol=w->c->temperature_tolerance*fmax(1.,fabs(T));
    if(fabsl(f)/denom<=tol || hi-lo<=tol) goto solved;
    if(f<0.L) {lo=T;elo=e;flo=f;slo=state;}
    else {hi=T;ehi=e;fhi=f;shi=state;}
    double next=T-(double)(f/denom);
    if(!(next>lo && next<hi) || next==T) next=lo+.5*(hi-lo);
    if(next==lo || next==hi) {
      if(fabsl(flo)/(slo.capacity+hD)<fabsl(fhi)/(shi.capacity+hD))
        {T=lo;e=elo;f=flo;state=slo;}
      else {T=hi;e=ehi;f=fhi;state=shi;}
      denom=state.capacity+hD;goto solved;
    }
    T=next;
  }
  return 6;
solved:
  if(fabsl(f)/denom>w->c->temperature_tolerance*fmax(1.,fabs(T))*2.) return 7;
  if((double)fabsl(f)>w->stats->maximum_row_absolute)
    w->stats->maximum_row_absolute=(double)fabsl(f);
  if((double)(fabsl(f)/denom)>w->stats->maximum_row_conditioned_temperature)
    w->stats->maximum_row_conditioned_temperature=(double)(fabsl(f)/denom);
  if(hi-lo>w->stats->maximum_caloric_temperature_width)
    w->stats->maximum_caloric_temperature_width=hi-lo;
  if(fabs(ehi-elo)>w->stats->maximum_caloric_energy_width)
    w->stats->maximum_caloric_energy_width=fabs(ehi-elo);
  if(lo<hi) w->stats->caloric_signed_brackets++;
  else w->stats->caloric_conditioned_only++;
  *E=e;*s=state;return 0;
}

/* All-water scalar rows are grouped by node. Each mean probe is linear pass.
 * The energy root is exactly equivalent to the mean root, not an energy fix. */
static int closure_heat_integrator_mean_probe(ClosureHeatIntegratorWorkspace * w,
  double b,double h,long double * residual,long double * derivative,
  long double * mean_residual,long double * mean_slope,double * maximum_state_derivative) {
  const ClosureHeatModel * m=w->m;
  memcpy(w->root_E,w->old_E,(size_t)m->nodes*sizeof(double));
  memcpy(w->root_state,w->old_state,(size_t)m->nodes*sizeof(ClosureHeatState));
  memset(w->derivative,0,(size_t)m->nodes*sizeof(double));
  for(int j=m->pfc_nodes;j<m->nodes;j++) if(w->D[j]>0.) {
    long double hD=(long double)h*w->D[j];
    int status=closure_heat_integrator_caloric(w,j,b,hD,w->root_E+j,w->root_state+j);
    if(status) {fprintf(stderr,"CALORIC_W_FAIL node=%d code=%d target=%.17g oldT=%.17g oldE=%.17g hD=%.21Lg\n",j,status,b,w->old_state[j].temperature,w->old_E[j],hD);return 1;}
    w->derivative[j]=(double)(hD/(w->root_state[j].capacity+hD));
  }
  long double centre=0.L,Bprime=0.L;
  for(int k=0;k<m->patches;k++) {
    const ClosureHeatPatch * p=m->patch+k;
    long double C=w->C[k],G=p->water_conductance,total=w->W*C+G;
    if(total>0.L) {
      centre+=C*G/total*((long double)w->root_state[p->water_node].temperature-b);
      Bprime+=C*(w->W*C+G*w->derivative[p->water_node])/total;
    }
  }
  double target=b+(double)(centre/w->CA);
  long double weighted=0.L,weighted_derivative=0.L;
  for(int i=0;i<m->pfc_nodes;i++) {
    long double omega=(long double)m->node[i].mass/m->inventory;
    long double hD=(long double)h*omega*w->CA;
    int status=closure_heat_integrator_caloric(w,i,target,hD,w->root_E+i,w->root_state+i);
    if(status) {fprintf(stderr,"CALORIC_F_FAIL node=%d code=%d target=%.17g oldT=%.17g oldE=%.17g hD=%.21Lg\n",i,status,target,w->old_state[i].temperature,w->old_E[i],hD);return 2;}
    w->derivative[i]=(double)((long double)h*omega*Bprime/
      (w->root_state[i].capacity+hD));
    weighted+=omega*w->root_state[i].temperature;
    weighted_derivative+=omega*w->derivative[i];
  }
  *residual=*derivative=0.L;*maximum_state_derivative=0.;
  for(int a=0;a<m->nodes;a++) {
    *residual+=(long double)w->root_E[a]-w->old_E[a];
    *derivative+=(long double)w->root_state[a].capacity*w->derivative[a];
    if(w->derivative[a]>*maximum_state_derivative)
      *maximum_state_derivative=w->derivative[a];
  }
  *mean_residual=weighted/w->W-b;
  *mean_slope=1.L-weighted_derivative/w->W;
  return !isfinite(*residual+*derivative+*mean_residual) || !(*derivative>0.L);
}

static int closure_heat_integrator_implicit(ClosureHeatIntegratorWorkspace * w,
  double h,double Tmin,double Tmax,long double energy_scale,
  double * physical_integral,double * frozen_lower) {
  const ClosureHeatModel * m=w->m;
  long double mean=0.L;
  for(int i=0;i<m->pfc_nodes;i++)
    mean+=(long double)m->node[i].mass/m->inventory*w->old_state[i].temperature;
  double b=(double)(mean/w->W),lo=Tmin,hi=Tmax,last_valid=b;
  long double residual,derivative,mean_residual,mean_slope;double state_derivative;
  int obtained=0;
  for(int k=0;k<w->c->max_mean_iterations;k++) {
    w->stats->mean_iterations++;
    if(closure_heat_integrator_mean_probe(w,b,h,&residual,&derivative,
        &mean_residual,&mean_slope,&state_derivative)) {
      double next=last_valid+.5*(b-last_valid);
      if(next==last_valid || next==b) return 1;
      b=next;continue;
    }
    last_valid=b;
    long double root_residual,root_derivative;
    if(mean_slope>=w->c->minimum_mean_root_slope) {
      root_residual=-mean_residual;root_derivative=mean_slope;w->stats->mean_root_probes++;
    } else {
      root_residual=residual;root_derivative=derivative;w->stats->energy_root_probes++;
    }
    w->stats->last_energy_root_residual=(double)residual;
    w->stats->last_mean_root_residual=(double)mean_residual;
    if((double)fabsl(residual)>w->stats->maximum_energy_root_residual)
      w->stats->maximum_energy_root_residual=(double)fabsl(residual);
    if(mean_slope<w->stats->minimum_observed_mean_slope)
      w->stats->minimum_observed_mean_slope=(double)mean_slope;
    double correction=(double)(fabsl(root_residual)/root_derivative)*state_derivative;
    if((double)fabsl(mean_residual)>w->stats->maximum_mean_residual)
      w->stats->maximum_mean_residual=(double)fabsl(mean_residual);
    if(correction>w->stats->maximum_root_temperature_correction)
      w->stats->maximum_root_temperature_correction=correction;
    if(fabsl(residual)<=w->c->energy_tolerance*energy_scale &&
       correction<=w->c->temperature_tolerance*fmax(1.,Tmax)*2.) {
      obtained=1;break;
    }
    if(root_residual<0.L) lo=b;else hi=b;
    double next=b-(double)(root_residual/root_derivative);
    if(!(next>lo && next<hi) || next==b) next=lo+.5*(hi-lo);
    if(next==lo || next==hi || next==b) return 2;
    b=next;
  }
  if(!obtained) return 3;
  memcpy(w->candidate,w->root_E,(size_t)m->nodes*sizeof(double));
  ClosureHeatDiagnostics old_d,new_d,mid_d,frozen_d;
  if(closure_heat_integrator_evaluate(w,m,w->old_E,w->stage,w->power,&old_d) ||
     closure_heat_integrator_evaluate(w,m,w->candidate,w->state,w->power,&new_d)) return 4;
  for(int a=0;a<m->nodes;a++) w->half[a]=.5*w->old_E[a]+.5*w->candidate[a];
  if(closure_heat_integrator_evaluate(w,m,w->half,w->stage,w->other_power,&mid_d)) return 5;
  ClosureHeatModel frozen=*m;
  /* Recover the frozen conductivity from the already-frozen graph. */
  long double old_k=0.L,volume=0.L;
  for(int i=0;i<m->pfc_nodes;i++) {
    double value;if(closure_heat_conductivity(m,w->old_state+i,&value)) return 6;
    volume+=m->node[i].volume;old_k+=(long double)m->node[i].volume*value;
  }
  frozen.k_liquid=frozen.k_vapour=frozen.k_critical=(double)(old_k/volume);
  if(closure_heat_integrator_evaluate(w,&frozen,w->candidate,w->stage,
                                     w->other_power,&frozen_d)) return 7;
  *physical_integral=h/6.*(old_d.entropy_rate+4.*mid_d.entropy_rate+new_d.entropy_rate);
  *frozen_lower=h*frozen_d.entropy_rate;
  long double row_entropy=0.L;
  for(int a=0;a<m->nodes;a++)
    row_entropy+=((long double)w->candidate[a]-w->old_E[a]-(long double)h*w->other_power[a])/
      w->stage[a].temperature;
  *frozen_lower+=(double)row_entropy;
  return !isfinite(*physical_integral+*frozen_lower);
}

/* Return zero only on a fully completed, committed invocation. Nonzero output
 * remains byte unchanged. Caller cache/diagnostic side effects must likewise be
 * transactional; callbacks may retain diagnostic counters, not physical trials. */
static int closure_heat_integrate(const ClosureHeatModel * m,
  ClosureHeatTemperatureEOS temperature_eos,double interval,const double * input,
  double * output,const ClosureHeatIntegratorControls * c,
  ClosureHeatIntegratorStats * stats) {
  memset(stats,0,sizeof(*stats));
  stats->minimum_observed_mean_slope=1.;
  if(!m || !m->eos || !input || !output || !c || m->nodes<1 || m->patches<0 ||
     !(interval>=0.) || !isfinite(interval) || c->mode<CLOSURE_HEAT_AUTO ||
     c->mode>CLOSURE_HEAT_FROZEN_BE || c->max_explicit_steps<1 || c->max_refinements<0 ||
     c->max_scalar_iterations<1 || c->max_mean_iterations<1 ||
     !(c->guard_fraction>0. && c->guard_fraction<1.) ||
     !(c->temperature_tolerance>0.) || !(c->energy_tolerance>0.) ||
     !(c->entropy_roundoff>=0.) || !(c->maximum_step>0.) ||
     !(c->implicit_growth>=1.) || !isfinite(c->maximum_step+c->implicit_growth) ||
     c->maximum_accepted_steps<1 ||
     !(c->minimum_mean_root_slope>0. && c->minimum_mean_root_slope<1.))
    {stats->status=1;return 1;}
  ClosureHeatIntegratorWorkspace w={0};w.m=m;w.temperature_eos=temperature_eos;
  w.c=c;w.stats=stats;
  size_t n=(size_t)m->nodes,k=(size_t)m->patches;
  if(n>(SIZE_MAX-k)/10 || 10*n+k>SIZE_MAX/sizeof(double) ||
     n>SIZE_MAX/(4*sizeof(ClosureHeatState))) {stats->status=2;return 2;}
  w.allocation=calloc(10*n+k,sizeof(double));
  w.state_allocation=calloc(4*n,sizeof(ClosureHeatState));
  if(!w.allocation || !w.state_allocation) {stats->status=2;goto finish;}
  w.E=w.allocation;w.candidate=w.E+n;w.half=w.candidate+n;w.power=w.half+n;
  w.other_power=w.power+n;w.D=w.other_power+n;w.old_E=w.D+n;
  w.root_E=w.old_E+n;w.derivative=w.root_E+n;w.C=w.derivative+n;
  w.state=w.state_allocation;w.old_state=w.state+n;
  w.root_state=w.old_state+n;w.stage=w.root_state+n;
  memcpy(w.E,input,n*sizeof(double));
  ClosureHeatDiagnostics d;
  if(closure_heat_integrator_evaluate(&w,m,w.E,w.state,w.power,&d))
    {stats->status=3;goto finish;}
  double guard;
  if(closure_heat_integrator_graph(&w,&d,w.state,&guard))
    {stats->status=4;goto finish;}
  long double initial_energy_scale,initial_entropy_scale;
  double Tmin,Tmax;
  closure_heat_integrator_scales(&w,w.state,&initial_energy_scale,
    &initial_entropy_scale,&Tmin,&Tmax);
  stats->active_energy_scale=(double)initial_energy_scale;
  stats->active_entropy_scale=(double)initial_entropy_scale;
  if(interval==0. || initial_energy_scale==0.L || Tmin==Tmax) {
    memcpy(output,input,n*sizeof(double));stats->status=0;goto finish;
  }
  int mode=c->mode;
  if(mode==CLOSURE_HEAT_AUTO)
    mode=interval/guard>c->max_explicit_steps?CLOSURE_HEAT_FROZEN_BE:CLOSURE_HEAT_MIDPOINT;
  stats->selected_mode=mode;
  if(mode==CLOSURE_HEAT_FROZEN_BE && !temperature_eos)
    {stats->status=5;goto finish;}
  double h=fmin(interval,fmin(c->maximum_step,guard));
  long double elapsed=0.L,entropy_integral=0.L,lower_integral=0.L;
  unsigned long steps=0;
  while(elapsed<(long double)interval) {
    if(steps>=c->maximum_accepted_steps) {stats->status=12;goto finish;}
    double remaining=(double)((long double)interval-elapsed);
    if(h>remaining) h=remaining;
    if(!(h>0.) || elapsed+(long double)h==elapsed)
      {stats->status=6;goto finish;}
    if(closure_heat_integrator_evaluate(&w,m,w.E,w.old_state,w.power,&d) ||
       closure_heat_integrator_graph(&w,&d,w.old_state,&guard))
      {stats->status=7;goto finish;}
    long double step_energy_scale,step_entropy_scale;double step_min,step_max;
    closure_heat_integrator_scales(&w,w.old_state,&step_energy_scale,
      &step_entropy_scale,&step_min,&step_max);
    memcpy(w.old_E,w.E,n*sizeof(double));
    if(mode==CLOSURE_HEAT_MIDPOINT && h>guard) h=guard;
    int accepted=0;double physical=0.,lower=0.;
    for(int retry=0;retry<=c->max_refinements;retry++) {
      int failed=0;
      stats->last_step=h;
      if(mode==CLOSURE_HEAT_MIDPOINT) {
        for(int a=0;a<m->nodes;a++) w.half[a]=w.old_E[a]+.5*h*w.power[a];
        ClosureHeatDiagnostics mid_d;double mid_guard;
        failed=closure_heat_integrator_evaluate(&w,m,w.half,w.stage,w.other_power,&mid_d);
        if(!failed) {
          failed=closure_heat_integrator_graph(&w,&mid_d,w.stage,&mid_guard);
          if(!failed && h>mid_guard) failed=1;
        }
        if(!failed) {
          for(int a=0;a<m->nodes;a++) w.candidate[a]=w.old_E[a]+h*w.other_power[a];
          ClosureHeatDiagnostics final_d;
          failed=closure_heat_integrator_evaluate(&w,m,w.candidate,w.state,
                                                  w.other_power,&final_d);
          physical=h*mid_d.entropy_rate;lower=0.;
        }
      } else failed=closure_heat_integrator_implicit(&w,h,step_min,step_max,
                                                     step_energy_scale,&physical,&lower);
      if(failed) stats->last_rejection_reason=(mode==CLOSURE_HEAT_MIDPOINT?200:100)+failed;
      long double balance=0.L,delta_entropy=0.L;
      if(!failed) for(int a=0;a<m->nodes;a++) {
        balance+=(long double)w.candidate[a]-w.old_E[a];
        delta_entropy+=(long double)w.state[a].entropy-w.old_state[a].entropy;
        double tolerance=2.*c->temperature_tolerance*fmax(1.,step_max);
        if(w.state[a].temperature<step_min-tolerance ||
           w.state[a].temperature>step_max+tolerance) {
          /* Nonincident nodes may lie outside the active temperature range. */
          if((a<m->pfc_nodes && w.CA>0.L) || w.D[a]>0.)
            {failed=1;stats->last_rejection_reason=300;}
        }
      }
      if(!failed && fabsl(balance)>c->energy_tolerance*step_energy_scale)
        {failed=1;stats->last_rejection_reason=310;}
      if(!failed && delta_entropy < -c->entropy_roundoff*step_entropy_scale)
        {failed=1;stats->last_rejection_reason=320;}
      if(!failed && mode==CLOSURE_HEAT_FROZEN_BE &&
           delta_entropy-lower < -c->entropy_roundoff*step_entropy_scale)
        {failed=1;stats->last_rejection_reason=330;}
      if(!failed) {
        memcpy(w.E,w.candidate,n*sizeof(double));
        entropy_integral+=physical;lower_integral+=lower;
        elapsed+=(long double)h;accepted=1;steps++;
        stats->accepted_time=(double)elapsed;
        if(mode==CLOSURE_HEAT_MIDPOINT) stats->explicit_steps++;else stats->implicit_steps++;
        break;
      }
      stats->rejected_trials++;h*=.5;
      if(!(h>0.) || elapsed+(long double)h==elapsed) break;
    }
    if(!accepted) {stats->status=8;goto finish;}
    if(mode==CLOSURE_HEAT_MIDPOINT && steps>= (unsigned long)c->max_explicit_steps &&
        elapsed<(long double)interval) {
      if(c->mode==CLOSURE_HEAT_MIDPOINT || !temperature_eos) {stats->status=9;goto finish;}
      mode=CLOSURE_HEAT_FROZEN_BE;stats->selected_mode=mode;
    }
    h=fmin(c->maximum_step,h*(mode==CLOSURE_HEAT_FROZEN_BE?c->implicit_growth:2.));
  }
  {
    ClosureHeatDiagnostics final_d;
    if(closure_heat_integrator_evaluate(&w,m,w.E,w.state,w.power,&final_d) ||
       closure_heat_integrator_evaluate(&w,m,input,w.old_state,w.other_power,&final_d))
      {stats->status=10;goto finish;}
    long double balance=0.L,entropy=0.L;
    for(int a=0;a<m->nodes;a++) {
      balance+=(long double)w.E[a]-input[a];
      entropy+=(long double)w.state[a].entropy-w.old_state[a].entropy;
    }
    stats->energy_defect=(double)balance;stats->entropy_increment=(double)entropy;
    stats->physical_entropy_integral=(double)entropy_integral;
    stats->frozen_entropy_lower_bound=(double)lower_integral;
    stats->entropy_lower_margin=(double)(entropy-lower_integral);
    if(fabsl(balance)>c->energy_tolerance*initial_energy_scale ||
       entropy< -c->entropy_roundoff*initial_entropy_scale)
      {stats->status=11;goto finish;}
  }
  memcpy(output,w.E,n*sizeof(double));stats->status=0;
finish:
  free(w.allocation);free(w.state_allocation);return stats->status;
}
#endif
