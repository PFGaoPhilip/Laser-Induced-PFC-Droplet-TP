/* Task-original, EOS-independent conservative Euler numerical flux.
 * Algebra: Toro (2012), equations 26, 36--39, 48, author lecture.
 * This is NOT a positivity/entropy theorem or a mixed-material solver.
 * Supplied sound speeds must be the selected EOS's adiabatic speeds.
 * Negative reference internal energy and tensile pressure are permitted;
 * physical EOS/domain checks belong to the caller. No floors or resets.
 */
#ifndef CLOSURE_CONSERVATIVE_HLLC_H
#define CLOSURE_CONSERVATIVE_HLLC_H
#include <math.h>
#include <float.h>
#include <string.h>
typedef struct {
  double rho,normal_velocity,tangential_velocity,internal_energy,pressure,sound_speed;
  /* Optional authoritative conservative TOTAL energy, in J/m3. Initialize
   * the whole struct and use flag 0 or 1. With flag 1 the caller must obtain
   * primitive e,p,c from that SAME conservative state/EOS. We check finite
   * energy and representation consistency within 64 binary64 epsilons;
   * this is not permission to independently change its thermodynamic state. */
  long double conserved_total_energy_density;
  int total_energy_supplied;
} ClosureEulerSide;
typedef struct {
  double flux[4]; /* mass, normal momentum, tangential momentum, total energy */
  double left_star[4],right_star[4];
  double left_speed,contact_speed,right_speed,contact_pressure;
  double maximum_signal_speed;
  /* Extended fan diagnostics retain jump-relation arithmetic before the
   * unavoidable binary64 public-state quantization. They are not new states. */
  long double left_star_extended[4],right_star_extended[4],flux_extended[4];
  long double left_speed_extended,contact_speed_extended,right_speed_extended,contact_pressure_extended;
  int branch; /* 0:left data,1:left star,2:right star,3:right data */
} ClosureHLLCResult;

static int closure_euler_side_valid(const ClosureEulerSide * s) {
  int basic=s && s->rho>0. && s->sound_speed>0. && isfinite(s->rho) &&
    isfinite(s->normal_velocity) && isfinite(s->tangential_velocity) &&
    isfinite(s->internal_energy) && isfinite(s->pressure) && isfinite(s->sound_speed);
  if(!basic || (s->total_energy_supplied!=0 && s->total_energy_supplied!=1))return 0;
  if(s->total_energy_supplied) {
    long double rho=s->rho,u=s->normal_velocity,v=s->tangential_velocity;
    long double reconstructed=rho*((long double)s->internal_energy+.5L*(u*u+v*v));
    long double scale=fmaxl(1.L,fmaxl(fabsl(reconstructed),rho*(long double)s->sound_speed*s->sound_speed));
    if(!isfinite(s->conserved_total_energy_density) ||
       fabsl(s->conserved_total_energy_density-reconstructed)>64.L*DBL_EPSILON*scale)return 0;
  }
  return 1;
}
static void closure_euler_vectors_ld(const ClosureEulerSide * s,long double U[4],long double F[4]) {
  long double rho=s->rho,u=s->normal_velocity,v=s->tangential_velocity;
  U[0]=rho;U[1]=rho*u;U[2]=rho*v;
  U[3]=s->total_energy_supplied?s->conserved_total_energy_density:
    rho*((long double)s->internal_energy+.5L*(u*u+v*v));
  F[0]=U[1];F[1]=rho*u*u+s->pressure;F[2]=rho*u*v;
  F[3]=u*(U[3]+s->pressure);
}
/* Explicit speeds permit separately sourced/verified bounds. This function
 * rejects invalid fan order or star density instead of substituting HLLE or
 * changing thermodynamic state. Output is byte-unchanged on every failure. */
static int closure_hllc_with_speeds(const ClosureEulerSide * left,const ClosureEulerSide * right,
    double left_speed,double right_speed,ClosureHLLCResult * output) {
  if(!output || !closure_euler_side_valid(left) || !closure_euler_side_valid(right))return 1;
  if(!isfinite(left_speed) || !isfinite(right_speed) || !(left_speed<right_speed))return 2;
  long double sl=left_speed,sr=right_speed,ul=left->normal_velocity,ur=right->normal_velocity;
  long double al=(long double)left->rho*(sl-ul),ar=(long double)right->rho*(sr-ur);
  if(!(al<0.L && ar>0.L))return 2;
  long double denominator=al-ar;
  long double sm=((long double)right->pressure-left->pressure+al*ul-ar*ur)/denominator;
  if(!(sl<sm && sm<sr) || !isfinite(sm))return 2;
  /* The two star-pressure formulas are algebraically identical. This symmetric
   * form avoids using either side as an unrecorded numerical preference. */
  long double ps=(ar*left->pressure-al*right->pressure+al*ar*(ur-ul))/(ar-al);
  long double ulv[4],urv[4],fl[4],fr[4],ls[4],rs[4],fsl[4],fsr[4];
  closure_euler_vectors_ld(left,ulv,fl);closure_euler_vectors_ld(right,urv,fr);
  const ClosureEulerSide * sides[2]={left,right};
  long double * states[2]={ulv,urv},* stars[2]={ls,rs},* fluxes[2]={fsl,fsr};
  long double speeds[2]={sl,sr};
  for(int k=0;k<2;k++) {
    long double uk=sides[k]->normal_velocity,sk=speeds[k],a=sk-uk,d=sk-sm;
    long double * us=stars[k],* fs=fluxes[k],* U=states[k];
    us[0]=(long double)sides[k]->rho*a/d;
    if(!(us[0]>0.L))return 2;
    us[1]=us[0]*sm;us[2]=us[0]*sides[k]->tangential_velocity;
    us[3]=(a*U[3]-(long double)sides[k]->pressure*uk+ps*sm)/d;
    fs[0]=us[0]*sm;fs[1]=us[0]*sm*sm+ps;
    fs[2]=us[0]*sm*sides[k]->tangential_velocity;
    fs[3]=sm*(us[3]+ps);
  }
  int branch=sl>=0.L?0:(sm>=0.L?1:(sr>0.L?2:3));
  long double * selected=branch==0?fl:(branch==1?fsl:(branch==2?fsr:fr));
  ClosureHLLCResult result;
  memset(&result,0,sizeof(result));
  for(int j=0;j<4;j++) {
    result.flux[j]=(double)selected[j];
    result.left_star[j]=(double)ls[j];result.right_star[j]=(double)rs[j];
    result.flux_extended[j]=selected[j];
    result.left_star_extended[j]=ls[j];result.right_star_extended[j]=rs[j];
    if(!isfinite(selected[j]) || !isfinite(ls[j]) || !isfinite(rs[j]) ||
       !isfinite(result.flux[j]) || !isfinite(result.left_star[j]) || !isfinite(result.right_star[j]))return 3;
  }
  result.left_speed=left_speed;result.contact_speed=(double)sm;result.right_speed=right_speed;
  result.contact_pressure=(double)ps;
  result.left_speed_extended=sl;result.contact_speed_extended=sm;
  result.right_speed_extended=sr;result.contact_pressure_extended=ps;
  result.maximum_signal_speed=fmax(fabs(left_speed),fabs(right_speed));result.branch=branch;
  if(!isfinite(result.contact_pressure) || !isfinite(result.maximum_signal_speed))return 3;
  *output=result;return 0;
}
/* Davis min/max characteristic estimate, Toro (2012) Eq.48. It is an
 * approximation: strong/nonconvex-EOS outer-wave enclosure is not proved. */
static int closure_hllc_davis(const ClosureEulerSide * left,const ClosureEulerSide * right,
    ClosureHLLCResult * output) {
  if(!closure_euler_side_valid(left) || !closure_euler_side_valid(right))return 1;
  double sl=fmin(left->normal_velocity-left->sound_speed,right->normal_velocity-right->sound_speed);
  double sr=fmax(left->normal_velocity+left->sound_speed,right->normal_velocity+right->sound_speed);
  return closure_hllc_with_speeds(left,right,sl,sr,output);
}
#endif
