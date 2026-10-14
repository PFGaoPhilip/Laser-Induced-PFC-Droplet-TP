/* Isolated nonlocal thermal law TH01a/TH02/TH09.
 * RHS is O(nodes+patches); the small dense BE verifier is not a PDE solver.
 * Fixed node mass/volume/composition, actual water/PFC patches, no latent term.
 * EOS callback must reject inaccessible states; no floors or energy resets.
 */
#ifndef CLOSURE_NONLOCAL_THERMAL_H
#define CLOSURE_NONLOCAL_THERMAL_H
#include <math.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  double temperature, entropy, capacity, vapour_volume_fraction;
} ClosureHeatState; /* K, J/K, J/K, dimensionless */
typedef struct { double mass, volume; } ClosureHeatNode; /* kg,m3 */
typedef struct {
  double area, water_conductance; int water_node;
} ClosureHeatPatch; /* m2,W/K,index */
typedef int (*ClosureHeatEOS)(void *,int,double,ClosureHeatState *);
typedef struct {
  int nodes,pfc_nodes,patches;
  const ClosureHeatNode * node;
  const ClosureHeatPatch * patch;
  double inventory,critical_temperature,taper_width_fraction;
  double k_liquid,k_vapour,k_critical;
  ClosureHeatEOS eos; void * eos_context;
} ClosureHeatModel;
typedef struct {
  double volume,radius,conductivity,measured_weight_sum,mean_temperature;
  double entropy_rate,energy_rate_sum,core_entropy_rate,water_entropy_rate;
} ClosureHeatDiagnostics;
typedef struct {
  unsigned long evaluations,rejected_trials,iterations;
  double residual; int failure;
} ClosureHeatSolveStats;

static int closure_heat_conductivity(const ClosureHeatModel * m,
  const ClosureHeatState * s,double * value) {
  double y=(m->critical_temperature-s->temperature)/
    (m->taper_width_fraction*m->critical_temperature);
  double b=y<=0.?0.:y>=1.?1.:y*y*(3.-2.*y);
  /* An undefined redundant supercritical fraction is never queried. */
  if(b>0. && !(s->vapour_volume_fraction>=0. &&
               s->vapour_volume_fraction<=1.)) return 1;
  double phase=b==0.?m->k_critical:
    m->k_liquid*(1.-s->vapour_volume_fraction)+
    m->k_vapour*s->vapour_volume_fraction;
  *value=m->k_critical+b*(phase-m->k_critical);
  return !(*value>0.) || !isfinite(*value);
}

static int closure_heat_evaluate(const ClosureHeatModel * m,const double * E,
  ClosureHeatState * state,double * power,ClosureHeatDiagnostics * d) {
  memset(d,0,sizeof(*d));
  if(!m || !m->eos || m->nodes<1 || m->pfc_nodes<0 ||
     m->pfc_nodes>m->nodes || m->patches<0) return 1;
  for(int a=0;a<m->nodes;a++) {
    power[a]=0.;
    if(!isfinite(E[a]) || !(m->node[a].mass>0.) || !(m->node[a].volume>0.) ||
       !isfinite(m->node[a].mass+m->node[a].volume) ||
       m->eos(m->eos_context,a,E[a],state+a) ||
       !(state[a].temperature>0.) || !(state[a].capacity>0.) ||
       !isfinite(state[a].temperature+state[a].capacity+state[a].entropy))
      return 2;
  }
  if(m->pfc_nodes==0) return m->patches?3:0;
  if(!(m->inventory>0.) || !(m->critical_temperature>0.) ||
     !(m->taper_width_fraction>0.) || !(m->k_liquid>0.) ||
     !(m->k_vapour>0.) || !(m->k_critical>0.)) return 3;
  long double volume=0.L,ksum=0.L,W=0.L,weighted_T=0.L;
  for(int i=0;i<m->pfc_nodes;i++) {
    double k; if(closure_heat_conductivity(m,state+i,&k)) return 4;
    long double w=(long double)m->node[i].mass/m->inventory;
    volume+=m->node[i].volume;ksum+=m->node[i].volume*k;
    W+=w;weighted_T+=w*state[i].temperature;
  }
  if(!(volume>0.L) || !(W>0.L)) return 4;
  long double mean=weighted_T/W,dispersion=0.L;
  for(int i=0;i<m->pfc_nodes;i++) {
    long double w=(long double)m->node[i].mass/m->inventory;
    long double diff=(long double)state[i].temperature-mean;
    dispersion+=w*diff*diff/state[i].temperature;
  }
  long double k=ksum/volume;
  long double R=cbrtl(3.L*volume/(4.L*acosl(-1.L)));
  long double length=R/acosl(-1.L),CA=0.L,centred_sum=0.L;
  long double core_entropy=0.L,water_entropy=0.L;
  for(int j=0;j<m->patches;j++) {
    const ClosureHeatPatch * p=m->patch+j;
    if(!(p->area>=0.) || !(p->water_conductance>=0.) ||
       p->water_node<m->pfc_nodes || p->water_node>=m->nodes) return 5;
    long double C=k*p->area/length,Gw=p->water_conductance,total=W*C+Gw;
    if(total==0.L) continue;
    long double Tw=state[p->water_node].temperature;
    long double difference=mean-Tw,factor=Gw/total;
    long double core_difference=factor*difference;
    long double water_difference=(W*C/total)*difference;
    long double Ti=mean-core_difference;
    if(!(Ti>0.L)) return 5;
    CA+=C;centred_sum+=C*core_difference;
    power[p->water_node]+=(double)(Gw*water_difference);
    core_entropy+=C*(dispersion*Ti/(mean*mean)+
                       W*core_difference*core_difference/(mean*Ti));
    water_entropy+=Gw*water_difference*water_difference/(Ti*Tw);
  }
  for(int i=0;i<m->pfc_nodes;i++) {
    long double w=(long double)m->node[i].mass/m->inventory;
    power[i]=(double)(-w*(CA*((long double)state[i].temperature-mean)+centred_sum));
  }
  long double sum=0.L;
  for(int i=0;i<m->nodes;i++) {if(!isfinite(power[i])) return 6;sum+=power[i];}
  d->volume=(double)volume;d->radius=(double)R;d->conductivity=(double)k;
  d->measured_weight_sum=(double)W;d->mean_temperature=(double)mean;
  d->core_entropy_rate=(double)core_entropy;
  d->water_entropy_rate=(double)water_entropy;
  d->entropy_rate=(double)(core_entropy+water_entropy);
  d->energy_rate_sum=(double)sum;
  return !isfinite(d->entropy_rate) || d->entropy_rate<0.;
}

static int closure_heat_linear_solve(int n,double * A,double * b,double * x) {
  for(int i=0;i<n;i++) {
    int pivot=i;for(int j=i+1;j<n;j++) if(fabs(A[j*n+i])>fabs(A[pivot*n+i])) pivot=j;
    if(!(fabs(A[pivot*n+i])>1.e-14)) return 1;
    if(pivot!=i) {
      for(int k=i;k<n;k++) {double v=A[i*n+k];A[i*n+k]=A[pivot*n+k];A[pivot*n+k]=v;}
      double v=b[i];b[i]=b[pivot];b[pivot]=v;
    }
    for(int j=i+1;j<n;j++) {
      double r=A[j*n+i]/A[i*n+i];A[j*n+i]=0.;
      for(int k=i+1;k<n;k++) A[j*n+k]-=r*A[i*n+k];
      b[j]-=r*b[i];
    }
  }
  for(int i=n-1;i>=0;i--) {
    double r=b[i];for(int j=i+1;j<n;j++) r-=A[i*n+j]*x[j];
    x[i]=r/A[i*n+i];if(!isfinite(x[i])) return 2;
  }
  return 0;
}

/* E_new is written only for an admissible converged candidate.
 * Small dense finite-difference Newton is verification infrastructure only.
 * tolerance is relative to each initial C*T, not an EOS energy-zero choice.
 */
static int closure_heat_backward_euler(const ClosureHeatModel * m,
  const double * old,double dt,double tolerance,int max_iterations,
  double difference_step,double * E_new,ClosureHeatSolveStats * stats) {
  int n=m->nodes,status=1;
  memset(stats,0,sizeof(*stats));
  if(!(dt>=0.) || !(tolerance>0.) || !(difference_step>0.) ||
      !isfinite(dt+tolerance+difference_step) ||
      n<1 || n>64 || max_iterations<1) {stats->failure=1;return 1;}
  double * work=calloc((size_t)(n*n+9*n),sizeof(double));
  ClosureHeatState * states=calloc((size_t)n,sizeof(*states));
  if(!work || !states) {free(work);free(states);stats->failure=2;return 2;}
  double * A=work,* E=A+n*n,* scale=E+n,* power=scale+n,* residual=power+n;
  double * candidate=residual+n,* power_trial=candidate+n,* trial_residual=power_trial+n;
  double * rhs=trial_residual+n,* step=rhs+n;
  ClosureHeatDiagnostics d;
  memcpy(E,old,(size_t)n*sizeof(double));
  stats->evaluations++;
  if(closure_heat_evaluate(m,E,states,power,&d)) {status=3;goto end;}
  for(int i=0;i<n;i++) {
    scale[i]=states[i].capacity*states[i].temperature;
    if(!(scale[i]>0.) || !isfinite(scale[i])) {status=3;goto end;}
  }
  for(int iteration=0;iteration<max_iterations;iteration++) {
    stats->iterations++;
    stats->evaluations++;
    if(closure_heat_evaluate(m,E,states,power,&d)) {status=4;goto end;}
    double norm=0.;
    for(int i=0;i<n;i++) {
      residual[i]=(E[i]-old[i]-dt*power[i])/scale[i];
      if(fabs(residual[i])>norm) norm=fabs(residual[i]);
    }
    stats->residual=norm;
    if(norm<=tolerance) {
      memcpy(E_new,E,(size_t)n*sizeof(double));status=0;goto end;
    }
    for(int j=0;j<n;j++) {
      double eps=difference_step;int found=0;
      for(int attempt=0;attempt<12;attempt++) {
        memcpy(candidate,E,(size_t)n*sizeof(double));
        double direction=(attempt%2)?-1.:1.;
        candidate[j]+=direction*eps*scale[j];
        stats->evaluations++;
        if(!closure_heat_evaluate(m,candidate,states,power_trial,&d)) {
          for(int i=0;i<n;i++) {
            double rp=(candidate[i]-old[i]-dt*power_trial[i])/scale[i];
            A[i*n+j]=(rp-residual[i])/(direction*eps);
          }
          found=1;break;
        }
        stats->rejected_trials++;
        if(attempt%2) eps*=.25;
      }
      if(!found) {status=5;goto end;}
    }
    for(int i=0;i<n;i++) {rhs[i]=-residual[i];step[i]=0.;}
    if(closure_heat_linear_solve(n,A,rhs,step)) {status=6;goto end;}
    double damping=1.;int accepted=0;
    for(int line=0;line<25;line++) {
      for(int i=0;i<n;i++) candidate[i]=E[i]+damping*step[i]*scale[i];
      stats->evaluations++;
      if(!closure_heat_evaluate(m,candidate,states,power_trial,&d)) {
        double next=0.;
        for(int i=0;i<n;i++) {
          trial_residual[i]=(candidate[i]-old[i]-dt*power_trial[i])/scale[i];
          if(fabs(trial_residual[i])>next) next=fabs(trial_residual[i]);
        }
        if(next<norm) {memcpy(E,candidate,(size_t)n*sizeof(double));accepted=1;break;}
      }
      stats->rejected_trials++;damping*=.5;
    }
    if(!accepted) {status=7;goto end;}
  }
  status=8;
end:
  stats->failure=status;free(work);free(states);return status;
}
#endif

