/* Task-original representation of the UNCHANGED MC01--MC08 mechanical path.
 * Separate long-double material subvolumes/extensives; EOS receives intrinsic
 * double rho/e only after a checked wide ratio. No mass/state is discarded.
 * Not adopted by geometric production. Paired rounding/work defects remain
 * explicit and require subsequent complete native field/ledger coverage.
 */
#ifndef CLOSURE_MECHANICAL_WIDE_REPRESENTATION_H
#define CLOSURE_MECHANICAL_WIDE_REPRESENTATION_H
#include "mechanical_relaxation.h"
#include <float.h>
typedef struct {double high,low;int exponent;} ClosureWideStored;
static int closure_wide_pack(long double x,ClosureWideStored * output) {
  if(!output || !isfinite(x))return 1;
  ClosureWideStored r={0};
  if(x!=0.L) {
    long double m=frexpl(x,&r.exponent);r.high=(double)m;
    r.low=(double)(m-(long double)r.high);
    if(r.high==0.)return 2;
  }
  *output=r;return 0;
}
static int closure_wide_unpack(const ClosureWideStored * input,long double * output) {
  if(!input || !output || !isfinite(input->high) || !isfinite(input->low))return 1;
  long double x=ldexpl((long double)input->high+input->low,input->exponent);
  if(!isfinite(x) || ((input->high!=0. || input->low!=0.) && x==0.L))return 2;
  *output=x;return 0;
}
typedef struct {
  long double water_fraction,pfc_fraction,water_mass_density,pfc_mass_density;
  long double water_internal_energy_density,pfc_internal_energy_density;
} ClosureMechanicalWideCell;
typedef struct {
  long double initial_entropy_density,final_entropy_density,integrated_entropy_source;
  long double paired_energy_roundoff,paired_volume_roundoff;
  long double final_relative_pressure_gap,relative_energy_residual;
  int steps,rejected_steps,status;
} ClosureMechanicalWideResult;
typedef struct {
  ClosureMaterialEOS water_eos,pfc_eos;
  const void * water_context,*pfc_context;
  long double water_mass,pfc_mass,total_energy;
} ClosureMechanicalWideProblem;
typedef struct {
  ClosureMaterialState water,pfc;
  long double p_interface,gap,scaled_gap_derivative,entropy_density,entropy_path_derivative;
} ClosureMechanicalWidePoint;

static int closure_mechanical_wide_point(const ClosureMechanicalWideProblem * problem,
    long double a,long double b,long double Ew,long double Ef,ClosureMechanicalWidePoint * s) {
  if(!(a>0.L && b>0.L) || fabsl(a+b-1.L)>2e-14L)return 1;
  long double rw=problem->water_mass/a,rf=problem->pfc_mass/b;
  long double ew=Ew/problem->water_mass,ef=Ef/problem->pfc_mass;
  if(!(rw>0.L && rf>0.L) || !isfinite(rw+rf+ew+ef) ||
     !((double)rw>0. && (double)rf>0.) || !isfinite((double)rw) || !isfinite((double)rf) ||
     !isfinite((double)ew) || !isfinite((double)ef))return 2;
  if(problem->water_eos(problem->water_context,(double)rw,(double)ew,&s->water) ||
     problem->pfc_eos(problem->pfc_context,(double)rf,(double)ef,&s->pfc))return 3;
  if(!(s->water.T>0. && s->pfc.T>0. && s->water.c2>0. && s->pfc.c2>0.))return 4;
  long double zw=rw*sqrtl(s->water.c2),zf=rf*sqrtl(s->pfc.c2),scale=fminl(a,b);
  s->gap=(long double)s->water.p-s->pfc.p;
  s->p_interface=(zf*s->water.p+zw*s->pfc.p)/(zw+zf);
  s->scaled_gap_derivative=-(rw*s->water.p_rho+s->water.p_e*s->p_interface/rw)*(scale/a)
    -(rf*s->pfc.p_rho+s->pfc.p_e*s->p_interface/rf)*(scale/b);
  s->entropy_density=problem->water_mass*s->water.s+problem->pfc_mass*s->pfc.s;
  s->entropy_path_derivative=s->gap*(zw/s->water.T+zf/s->pfc.T)/(zw+zf);
  return !isfinite(s->p_interface+s->gap+s->scaled_gap_derivative+s->entropy_density+s->entropy_path_derivative);
}
static int closure_mechanical_wide_rk4(const ClosureMechanicalWideProblem * problem,
    long double a,long double b,long double Ew,long double Ef,long double h,
    long double * energy_water,long double * energy_pfc,long double * entropy) {
  ClosureMechanicalWidePoint s1,s2,s3,s4;
  if(closure_mechanical_wide_point(problem,a,b,Ew,Ef,&s1) ||
     closure_mechanical_wide_point(problem,a+.5L*h,b-.5L*h,Ew-.5L*h*s1.p_interface,Ef+.5L*h*s1.p_interface,&s2) ||
     closure_mechanical_wide_point(problem,a+.5L*h,b-.5L*h,Ew-.5L*h*s2.p_interface,Ef+.5L*h*s2.p_interface,&s3) ||
     closure_mechanical_wide_point(problem,a+h,b-h,Ew-h*s3.p_interface,Ef+h*s3.p_interface,&s4))return 1;
  long double transfer=h*(s1.p_interface+2.L*s2.p_interface+2.L*s3.p_interface+s4.p_interface)/6.L;
  *energy_water=Ew-transfer;*energy_pfc=Ef+transfer;
  *entropy=h*(s1.entropy_path_derivative+2.L*s2.entropy_path_derivative+2.L*s3.entropy_path_derivative+s4.entropy_path_derivative)/6.L;
  return !isfinite(*energy_water+*energy_pfc+*entropy);
}
static int closure_mechanical_wide_relax(ClosureMechanicalWideCell * cell,
    ClosureMaterialEOS water_eos,const void * water_context,ClosureMaterialEOS pfc_eos,const void * pfc_context,
    double pressure_tolerance,double path_tolerance,int maximum_steps,ClosureMechanicalWideResult * result) {
  if(!cell || !result || !water_eos || !pfc_eos || !(pressure_tolerance>0. && path_tolerance>0.) || maximum_steps<1)return 1;
  memset(result,0,sizeof(*result));
  long double a=cell->water_fraction,b=cell->pfc_fraction;
  long double Ew=cell->water_internal_energy_density,Ef=cell->pfc_internal_energy_density;
  if((a==0.L && cell->water_mass_density==0.L) || (b==0.L && cell->pfc_mass_density==0.L))return 0;
  if(!(a>0.L && b>0.L && cell->water_mass_density>0.L && cell->pfc_mass_density>0.L))return result->status=1;
  ClosureMechanicalWideProblem problem={water_eos,pfc_eos,water_context,pfc_context,
    cell->water_mass_density,cell->pfc_mass_density,Ew+Ef};
  ClosureMechanicalWidePoint current;
  if(closure_mechanical_wide_point(&problem,a,b,Ew,Ef,&current))return result->status=2;
  result->initial_entropy_density=current.entropy_density;
  long double energy_scale=fmaxl(1e5L,fmaxl(fabsl(Ew),fabsl(Ef)));
  for(int step=0;step<maximum_steps;step++) {
    long double pscale=fmaxl(1e5L,fmaxl(fabsl(current.water.p),fabsl(current.pfc.p)));
    result->final_relative_pressure_gap=fabsl(current.gap)/pscale;
    if(result->final_relative_pressure_gap<=pressure_tolerance) {
      cell->water_fraction=a;cell->pfc_fraction=b;cell->water_internal_energy_density=Ew;cell->pfc_internal_energy_density=Ef;
      result->final_entropy_density=current.entropy_density;
      result->relative_energy_residual=fabsl(Ew+Ef-problem.total_energy)/energy_scale;
      result->steps=step;return 0;
    }
    if(!(current.scaled_gap_derivative<0.L))return result->status=3;
    long double h=(-.8L*current.gap/current.scaled_gap_derivative)*fminl(a,b),bound=.05L*fminl(a,b);
    if(fabsl(h)>bound)h=copysignl(bound,h);
    int accepted=0;
    for(int trial=0;trial<40;trial++) {
      long double coarse,coarse_f,Sc,half,half_f,Sh,fine,fine_f,Sf;
      ClosureMechanicalWidePoint candidate;
      int fail=closure_mechanical_wide_rk4(&problem,a,b,Ew,Ef,h,&coarse,&coarse_f,&Sc) ||
        closure_mechanical_wide_rk4(&problem,a,b,Ew,Ef,.5L*h,&half,&half_f,&Sh) ||
        closure_mechanical_wide_rk4(&problem,a+.5L*h,b-.5L*h,half,half_f,.5L*h,&fine,&fine_f,&Sf) ||
        closure_mechanical_wide_point(&problem,a+h,b-h,fine,fine_f,&candidate);
      if(!fail && fmaxl(fabsl(fine-coarse),fabsl(fine_f-coarse_f))<=path_tolerance*energy_scale &&
         current.gap*candidate.gap>=0.L && fabsl(candidate.gap)<fabsl(current.gap) && Sh+Sf>=0.L) {
        long double next_a=a+h,next_b=b-h;
        result->paired_volume_roundoff+=(next_a-a)+(next_b-b);
        result->paired_energy_roundoff+=(fine-Ew)+(fine_f-Ef);
        a=next_a;b=next_b;Ew=fine;Ef=fine_f;current=candidate;
        result->integrated_entropy_source+=Sh+Sf;accepted=1;break;
      }
      h*=.5L;result->rejected_steps++;
    }
    if(!accepted)return result->status=4;
  }
  return result->status=5;
}
#endif
