/* EOS_DIAGNOSTIC_001_BEGIN */#include "eos_diagnostic_api.h"
/* EOS_DIAGNOSTIC_001_END *//* Same-potential fixed-rho/xi caloric temperature inverse in phase densities.
 * Separate pressure equality and conserved-volume tolerances avoid a stricter
 * volume target being limited by an independently stopped PT phase root.
 * Stable path sampling is numerical evidence, not interval root isolation. */
#ifndef CLOSURE_PFC_TEMPERATURE_INVERSE_H
#define CLOSURE_PFC_TEMPERATURE_INVERSE_H
#include "pfc_helmholtz_eos_diagnostic.h"
typedef struct {unsigned long raw_queries,iterations,rejected_trials;} ClosurePFCTemperatureInverseStats;

static int closure_pfc_temperature_phases(const ClosurePFCFluid * f,
  double rho_l,double rho_v,double T,ClosurePFCPhase * l,ClosurePFCPhase * v,
  ClosurePFCTemperatureInverseStats * statistics) {
  statistics->raw_queries+=2;
  if(closure_pfc_raw(f,rho_l,T,l) || closure_pfc_raw(f,rho_v,T,v))return 1;
  if(T<f->critical_T && (rho_l<=f->critical_rho || rho_v>=f->critical_rho))return 2;
  return 0;
}

static int closure_pfc_temperature_inverse_eos_diagnostic_original(const ClosurePFCFluid * f,double rho,
  double T,double xi,ClosurePFCCache * cache,ClosurePFCMixture * result,
  double pressure_tolerance,double volume_tolerance,int maximum_iterations,
  ClosurePFCTemperatureInverseStats * statistics) {
  memset(statistics,0,sizeof(*statistics));
  if(!(rho>0.) || !(T>0.) || !(xi>0. && xi<1.) ||
    !(pressure_tolerance>0.) || !(volume_tolerance>0.) ||
    !cache->liquid_valid || !cache->vapour_valid)return 1;
  ClosurePFCPhase liquid,vapour;
  double rl=cache->liquid.rho,rv=cache->vapour.rho,target=1./rho;
  if(closure_pfc_temperature_phases(f,rl,rv,T,&liquid,&vapour,statistics))return 2;
  double scale=fmax(101325.,fmax(fabs(liquid.p),fabs(vapour.p)));
  for(int iteration=0;iteration<maximum_iterations;iteration++) {
    statistics->iterations++;
    double pressure=(liquid.p-vapour.p)/scale;
    double volume=((1.-xi)/rl+xi/rv)/target-1.;
    double norm=fmax(fabs(pressure)/pressure_tolerance,fabs(volume)/volume_tolerance);
    if(norm<=1.) {
      ClosurePFCMixture state={0};state.liquid=liquid;state.vapour=vapour;
      state.liquid_available=state.vapour_available=1;
      state.coalesced=T>=f->critical_T;
      if(closure_pfc_combine(.5*(liquid.p+vapour.p),T,xi,&state))return 3;
      cache->liquid=liquid;cache->vapour=vapour;
      cache->liquid_valid=cache->vapour_valid=1;*result=state;return 0;
    }
    double j00=-1./(rl*liquid.vp*scale),j01=1./(rv*vapour.vp*scale);
    double j10=-(1.-xi)/(rl*target),j11=-xi/(rv*target);
    double determinant=j00*j11-j01*j10;
    if(!(determinant<0.) || !isfinite(determinant))return 4;
    double dl=(-pressure*j11+j01*volume)/determinant;
    double dv=(j10*pressure-j00*volume)/determinant;
    double correction=fmax(fabs(dl),fabs(dv));
    if(!(correction>0.) || !isfinite(correction))return 4;
    double damping=fmin(1.,.15/correction),accepted=0.;
    for(int attempt=0;attempt<32;attempt++) {
      double theta=ldexp(damping,-attempt),trial_l=rl*exp(theta*dl),trial_v=rv*exp(theta*dv);
      ClosurePFCPhase l,v;int path_failure=0;
      for(int sample=1;sample<=8;sample++) {
        double a=sample/8.;
        if(closure_pfc_temperature_phases(f,rl*exp(a*theta*dl),rv*exp(a*theta*dv),
            T,&l,&v,statistics)) {path_failure=1;break;}
      }
      if(!path_failure) {
        double pe=(l.p-v.p)/scale,ve=((1.-xi)/trial_l+xi/trial_v)/target-1.;
        double trial_norm=fmax(fabs(pe)/pressure_tolerance,fabs(ve)/volume_tolerance);
        if(trial_norm<norm) {
          rl=trial_l;rv=trial_v;liquid=l;vapour=v;accepted=1.;break;
        }
      }
      statistics->rejected_trials++;/* EOS_DIAGNOSTIC_001_BEGIN */closure_eos_diag_note(CLOSURE_EOS_PFC_TEMPERATURE_TRIAL_REJECTED,1);/* EOS_DIAGNOSTIC_001_END */
    }
    if(!accepted)return 5;
  }
  return 6;
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_pfc_temperature_inverse(const ClosurePFCFluid * f,double rho,
  double T,double xi,ClosurePFCCache * cache,ClosurePFCMixture * result,
  double pressure_tolerance,double volume_tolerance,int maximum_iterations,
  ClosurePFCTemperatureInverseStats * statistics) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_PFC_TEMPERATURE_INVERSE);
  int value=closure_pfc_temperature_inverse_eos_diagnostic_original(f,rho,T,xi,cache,result,pressure_tolerance,volume_tolerance,maximum_iterations,statistics);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */
#endif
