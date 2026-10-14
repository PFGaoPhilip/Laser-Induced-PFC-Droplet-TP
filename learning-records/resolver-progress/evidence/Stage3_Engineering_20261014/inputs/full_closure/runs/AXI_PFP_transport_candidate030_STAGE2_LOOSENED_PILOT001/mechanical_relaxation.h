/* Original conservative instantaneous two-material pressure relaxation.
 * Governing path and entropy identity are derived in MIXED_CELL_RELAXATION.md.
 * No material mass, total energy or momentum is reset. This isolated operator
 * has no advection, capillarity, heat flux, reaction or shock partition. */
#ifndef CLOSURE_MECHANICAL_RELAXATION_H
#define CLOSURE_MECHANICAL_RELAXATION_H
#include <math.h>
#include <string.h>

typedef struct {
  double p,T,s,c2,p_e,p_rho;
} ClosureMaterialState;
typedef int (*ClosureMaterialEOS)(const void *,double,double,ClosureMaterialState *);
typedef struct {
  double water_fraction,pfc_fraction,water_mass_density,pfc_mass_density;
  double water_internal_energy_density,pfc_internal_energy_density;
} ClosureMechanicalCell;
typedef struct {
  double initial_entropy_density,final_entropy_density,integrated_entropy_source;
  double final_relative_pressure_gap,relative_energy_residual;
  int steps,rejected_steps,status;
} ClosureMechanicalResult;

typedef struct {
  ClosureMaterialEOS water_eos,pfc_eos;
  const void * water_context,* pfc_context;
  double water_mass,pfc_mass,total_energy;
} ClosureMechanicalProblem;
typedef struct {
  ClosureMaterialState water,pfc;
  double p_interface,gap,scaled_gap_derivative,entropy_density,entropy_path_derivative;
} ClosureMechanicalPoint;

static int closure_mechanical_point(const ClosureMechanicalProblem * problem,
  double a,double b,double Ew,double Ef,ClosureMechanicalPoint * state) {
  if(!(a>0. && b>0.) || fabs((a+b)-1.)>2.e-14) return 1;
  double rw=problem->water_mass/a,rf=problem->pfc_mass/b;
  if(problem->water_eos(problem->water_context,rw,Ew/problem->water_mass,&state->water) ||
     problem->pfc_eos(problem->pfc_context,rf,Ef/problem->pfc_mass,&state->pfc)) return 2;
  if(!(state->water.T>0.) || !(state->pfc.T>0.) ||
     !(state->water.c2>0.) || !(state->pfc.c2>0.)) return 3;
  double zw=rw*sqrt(state->water.c2),zf=rf*sqrt(state->pfc.c2);
  state->gap=state->water.p-state->pfc.p;
  state->p_interface=(zf*state->water.p+zw*state->pfc.p)/(zw+zf);
  /* The derivative d(pW-pF)/da diverges arithmetically for an otherwise
   * valid subnormal positive fraction. Its min(a,b)-scaled value is finite:
   * no fraction, mass or thermodynamic state is changed by this coordinate
   * scaling. Even an already-equilibrated state must be evaluable first. */
  double fraction_scale=fmin(a,b);
  state->scaled_gap_derivative=-(rw*state->water.p_rho+
    state->water.p_e*state->p_interface/rw)*(fraction_scale/a)
    -(rf*state->pfc.p_rho+state->pfc.p_e*state->p_interface/rf)*(fraction_scale/b);
  state->entropy_density=problem->water_mass*state->water.s+problem->pfc_mass*state->pfc.s;
  state->entropy_path_derivative=state->gap*(zw/state->water.T+zf/state->pfc.T)/(zw+zf);
  return !isfinite(state->p_interface) || !isfinite(state->gap) ||
    !isfinite(state->scaled_gap_derivative) || !isfinite(state->entropy_density) ||
    !isfinite(state->entropy_path_derivative);
}

/* RK4 integrates paired equal/opposite energy increments and the independent
 * local entropy source. Never obtain a tiny populated energy by subtracting
 * the dominant component from a rounded total. Summed conservation roundoff
 * is measured independently, rather than hidden in an energy reset. */
static int closure_mechanical_rk4(const ClosureMechanicalProblem * problem,
  double a,double b,double Ew,double Ef,double h,double * energy_water,
  double * energy_pfc,double * entropy_integral) {
  ClosureMechanicalPoint s1,s2,s3,s4;
  if(closure_mechanical_point(problem,a,b,Ew,Ef,&s1) ||
     closure_mechanical_point(problem,a+.5*h,b-.5*h,Ew-.5*h*s1.p_interface,
       Ef+.5*h*s1.p_interface,&s2) ||
     closure_mechanical_point(problem,a+.5*h,b-.5*h,Ew-.5*h*s2.p_interface,
       Ef+.5*h*s2.p_interface,&s3) ||
     closure_mechanical_point(problem,a+h,b-h,Ew-h*s3.p_interface,
       Ef+h*s3.p_interface,&s4)) return 1;
  double transfer=h*(s1.p_interface+2.*s2.p_interface+2.*s3.p_interface+s4.p_interface)/6.;
  *energy_water=Ew-transfer;*energy_pfc=Ef+transfer;
  *entropy_integral=h*(s1.entropy_path_derivative+2.*s2.entropy_path_derivative+
                       2.*s3.entropy_path_derivative+s4.entropy_path_derivative)/6.;
  return !isfinite(*energy_water+*energy_pfc+*entropy_integral);
}

static int closure_mechanical_relax(ClosureMechanicalCell * cell,
  ClosureMaterialEOS water_eos,const void * water_context,
  ClosureMaterialEOS pfc_eos,const void * pfc_context,
  double pressure_tolerance,double path_tolerance,int maximum_steps,
  ClosureMechanicalResult * result) {
  memset(result,0,sizeof(*result));
  double a=cell->water_fraction,b=cell->pfc_fraction,Ew=cell->water_internal_energy_density,
    Ef=cell->pfc_internal_energy_density;
  if((a==0. && cell->water_mass_density==0.) ||
     (a==1. && cell->pfc_mass_density==0.)) return 0;
  if(!(a>0. && b>0.) || !(cell->water_mass_density>0.) || !(cell->pfc_mass_density>0.)) return result->status=1;
  ClosureMechanicalProblem problem={water_eos,pfc_eos,water_context,pfc_context,
    cell->water_mass_density,cell->pfc_mass_density,
    cell->water_internal_energy_density+cell->pfc_internal_energy_density};
  ClosureMechanicalPoint current;
  if(closure_mechanical_point(&problem,a,b,Ew,Ef,&current)) return result->status=2;
  result->initial_entropy_density=current.entropy_density;
  double energy_scale=fmax(1.e5,fmax(fabs(Ew),fabs(problem.total_energy-Ew)));
  for(int step=0;step<maximum_steps;step++) {
    double pressure_scale=fmax(1.e5,fmax(fabs(current.water.p),fabs(current.pfc.p)));
    result->final_relative_pressure_gap=fabs(current.gap)/pressure_scale;
    if(result->final_relative_pressure_gap<=pressure_tolerance) {
      cell->water_fraction=a;cell->pfc_fraction=b;cell->water_internal_energy_density=Ew;
      cell->pfc_internal_energy_density=Ef;
      result->final_entropy_density=current.entropy_density;
      result->relative_energy_residual=fabs(cell->water_internal_energy_density+
        cell->pfc_internal_energy_density-problem.total_energy)/energy_scale;
      result->steps=step;return 0;
    }
    if(!(current.scaled_gap_derivative<0.)) return result->status=3;
    double h=(-.8*current.gap/current.scaled_gap_derivative)*fmin(a,b);
    double bound=.05*fmin(a,b);
    if(fabs(h)>bound) h=copysign(bound,h);
    int accepted=0;
    for(int trial=0;trial<40;trial++) {
      double coarse,coarse_f,Sc,half,half_f,Sh,fine,fine_f,Sf;
      ClosureMechanicalPoint candidate;
      int fail=closure_mechanical_rk4(&problem,a,b,Ew,Ef,h,&coarse,&coarse_f,&Sc) ||
        closure_mechanical_rk4(&problem,a,b,Ew,Ef,.5*h,&half,&half_f,&Sh) ||
        closure_mechanical_rk4(&problem,a+.5*h,b-.5*h,half,half_f,.5*h,&fine,&fine_f,&Sf) ||
        closure_mechanical_point(&problem,a+h,b-h,fine,fine_f,&candidate);
      if(!fail && fmax(fabs(fine-coarse),fabs(fine_f-coarse_f))<=path_tolerance*energy_scale &&
         current.gap*candidate.gap>=0. && fabs(candidate.gap)<fabs(current.gap) &&
         Sh+Sf>=0.) {
        /* Direct entropy production is the physical acceptance condition.
         * Near-reference bulk-water entropy subtraction can have much larger
         * roundoff than a tiny populated phase's entropy increment. Save the
         * endpoint subtraction independently; never replace the source by it.
         * Step doubling controls path error and all EOS states stay stable. */
        a+=h;b-=h;Ew=fine;Ef=fine_f;current=candidate;
        result->integrated_entropy_source+=Sh+Sf;accepted=1;break;
      }
      h*=.5;result->rejected_steps++;
    }
    if(!accepted) return result->status=4;
  }
  return result->status=5;
}
#endif
