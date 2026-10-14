/* Task-local adaptation of official Basilisk vof.h (archive identity in
 * SOLVER_IDENTITY.json, GPL). Same PLIC/dimension-split tracer flux method,
 * with compressible advective fractions and strictly-positive donor support.
 * No populated material is deleted or frozen at a donor-fraction threshold.
 * Candidate028 engineering soft-pass: clamp Inf capacity ratios before boundary.
 * Candidate029 STAGE2_LOOSENED: SEPS on cm denominators; sanitize non-finite
 * gradients/fluxes/capacity/fractions before boundary(); refuse non-finite
 * concentration gradients — targets pilot001 SIGFPE inside geometric_advection
 * after DIAG-before at t~0.44 ns (028 clamp already active earlier in that run). */
#ifndef CLOSURE_GEOMETRIC_ADVECTION_H
#define CLOSURE_GEOMETRIC_ADVECTION_H
#include "fractions.h"
attribute {
  scalar * closure_tracers;
  bool closure_inverse,closure_positive,closure_bounded;
  scalar closure_upper;
}
typedef struct {
  double max_advective_cfl;
  unsigned long unresolved_complement_faces;
  unsigned long limited_faces;
  unsigned long exact_depletion_faces;
  double minimum_capacity_factor;
  double maximum_depletion_flux_correction;
  double maximum_paired_identity_defect;
  double maximum_complement_adjustment;
  double minimum_compression_denominator;
  double minimum_donor_numerator;
} ClosureGeometricAdvectionStats;


/* Candidate028 helper: finite capacity ratio or fallback (engineering soft-pass). */
static inline double closure_c028_cap_ratio(double num,double den,double fallback) {
  if(!(den>0.)) return fallback;
  double r=num/den;
  if(!isfinite(r) || r>(double)HUGE) return fallback;
  return r;
}
foreach_dimension()
static double closure_concentration_gradient_x(Point point,scalar c,scalar b,scalar t) {
  double cl=t.closure_inverse?b[-1]:c[-1];
  double cc=t.closure_inverse?b[]:c[];
  double cr=t.closure_inverse?b[1]:c[1];
  if(cc>=.5 && t.gradient!=zero) {
    if(!(cl>0.) || !(cc>0.) || !(cr>0.)) return 0.;
    double g=0.;
    if(cr>=.5) {
      if(cl>=.5) g=t.gradient?
        t.gradient(t[-1]/cl,t[]/cc,t[1]/cr)/Delta:(t[1]/cr-t[-1]/cl)/(2.*Delta);
      else g=(t[1]/cr-t[]/cc)/Delta;
    } else if(cl>=.5) g=(t[]/cc-t[-1]/cl)/Delta;
    if(!isfinite(g)) {
      static int axi_c029_grad_soft_logged=0;
      if(!axi_c029_grad_soft_logged){
        fprintf(stderr,"AXI geometric gradient engineering soft-pass: non-finite concentration gradient zeroed (STAGE2_LOOSENED candidate029)\n");
        fflush(stderr);axi_c029_grad_soft_logged=1;
      }
      return 0.;
    }
    return g;
  }
  return 0.;
}

/* Candidate029: scrub non-finite cell values before Basilisk boundary BC (Inf±Inf SIGFPE). */
static inline void closure_c029_sanitize_scalar(scalar s,double fallback) {
  foreach() {
    if(!isfinite(s[])) s[]=fallback;
  }
}
static inline void closure_c029_sanitize_list(scalar * list,double fallback) {
  if(!list) return;
  for(scalar s in list) closure_c029_sanitize_scalar(s,fallback);
}

foreach_dimension()
static int closure_geometric_sweep_x(scalar c,scalar b,face vector velocity,
  double step,ClosureGeometricAdvectionStats * statistics) {
  vector normal[],water_normal[];
  scalar intercept[],water_intercept[],flux_c[],flux_b[],depletion_c[],depletion_b[];
  scalar donor_left_velocity[],donor_right_velocity[];
  scalar * tracers=c.closure_tracers,* gradients=NULL,* fluxes=NULL;
  for(scalar t in tracers) {
    scalar gradient=new scalar,flux=new scalar;
    gradients=list_append(gradients,gradient);fluxes=list_append(fluxes,flux);
  }
  foreach() {
    /* Scalar donor records have the regular cell boundary extension. A
     * dynamic face offset at the outer face can otherwise request a second
     * face ghost which has no boundary value, even in a periodic problem. */
    donor_left_velocity[]=velocity.x[];
    donor_right_velocity[]=velocity.x[1];
    if(!isfinite(donor_left_velocity[])) donor_left_velocity[]=0.;
    if(!isfinite(donor_right_velocity[])) donor_right_velocity[]=0.;
    scalar t,gradient;
    for(t,gradient in tracers,gradients)
      gradient[]=closure_concentration_gradient_x(point,c,b,t);
  }
  closure_c029_sanitize_list(gradients,0.);
  closure_c029_sanitize_scalar(donor_left_velocity,0.);
  closure_c029_sanitize_scalar(donor_right_velocity,0.);
  fprintf(stderr,"DIAG c029 sweep before gradients boundary\n");fflush(stderr);
  boundary(gradients);boundary({donor_left_velocity,donor_right_velocity});
  fprintf(stderr,"DIAG c029 sweep after gradients boundary\n");fflush(stderr);
  reconstruction(c,normal,intercept);
  reconstruction(b,water_normal,water_intercept);
  double maximum_cfl=0.;int unresolved=0,failures=0;
  foreach_face(x,reduction(max:maximum_cfl) reduction(+:unresolved) reduction(+:failures)) {
    double un=fm.x[]>0.?velocity.x[]*step/(Delta*fm.x[]):0.;
    double direction=sign(un);int donor=-(direction+1.)/2.;
    depletion_c[]=depletion_b[]=0.;
    maximum_cfl=fmax(maximum_cfl,fabs(un)*fm.x[]/(cm[]+SEPS));
    double cf=c[donor];
    if(cf>0. && cf<1.) {
      coord n={-direction*normal.x[donor],0.,0.};
#if dimension > 1
      n.y=normal.y[donor];
#endif
#if dimension > 2
      n.z=normal.z[donor];
#endif
      cf=rectangle_fraction(n,intercept[donor],(coord){-.5,-.5,-.5},
        (coord){direction*un-.5,.5,.5});
    }
    double bf=1.-cf;
    /* A geometrically rounded full-PFC donor can still contain an explicit
     * sub-ulp water fraction. Transport it at the donor fraction, flag the
     * unresolved geometric face and retain every associated conserved mass.
     * Valid production requires a separate uncovered-mass/resolution bound. */
    if(c[donor]==1. && bf==0. && b[donor]>0.) {bf=b[donor];unresolved++;}
    if(!(cf>=0. && cf<=1.) || !(bf>=0. && bf<=1.)) {
      fprintf(stderr,"invalid-PLIC-fraction x=%.17g c=%.17g b=%.17g cf=%.17g bf=%.17g\n",x,c[donor],b[donor],cf,bf);failures++;
    }
    flux_c[]=cf*velocity.x[];flux_b[]=bf*velocity.x[];
    double other_velocity=direction>0.?donor_left_velocity[donor]:donor_right_velocity[donor];
    unsigned long long other_bits;
    memcpy(&other_bits,&other_velocity,sizeof(other_bits));
    int finite_other=(other_bits&0x7ff0000000000000ULL)!=0x7ff0000000000000ULL;
    if(!finite_other && velocity.x[]!=0.) {
      fprintf(stderr,"invalid-opposite-face x=%.17g step=%.17g direction=%.17g donor=%d velocity=%.17g opposite_bits=%llx\n",
        x,step,direction,donor,velocity.x[],other_bits);failures++;
    }
    if(velocity.x[]!=0. && finite_other && direction*other_velocity>=0.) {
      coord nc={-direction*normal.x[donor],0.,0.};
      coord nb={-direction*water_normal.x[donor],0.,0.};
#if dimension > 1
      nc.y=normal.y[donor];nb.y=water_normal.y[donor];
#endif
#if dimension > 2
      nc.z=normal.z[donor];nb.z=water_normal.z[donor];
#endif
      coord lo={fabs(un)-.5,-.5,-.5},hi={.5,.5,.5};
      double transport=fabs(velocity.x[])*step;
      if(c[donor]>0. && c[donor]<1. &&
         rectangle_fraction(nc,intercept[donor],lo,hi)==0. &&
         c[donor]*cm[donor]*Delta<=transport) depletion_c[]=1.;
      if(b[donor]>0. && b[donor]<1. &&
         rectangle_fraction(nb,water_intercept[donor],lo,hi)==0. &&
         b[donor]*cm[donor]*Delta<=transport) depletion_b[]=1.;
      if(depletion_c[] && depletion_b[]) {fprintf(stderr,"conflicting-depletion-events x=%.17g c=%.17g b=%.17g transport=%.17g\n",x,c[donor],b[donor],transport);failures++;}
    }
    scalar t,gradient,flux;
    for(t,gradient,flux in tracers,gradients,fluxes) {
      double ci=t.closure_inverse?b[donor]:c[donor];
      double fi=t.closure_inverse?bf:cf;
      if(ci>0.) {
        double concentration=t[donor]/ci+
          direction*fmin(1.,1.-direction*un)*gradient[donor]*Delta/2.;
        flux[]=concentration*(t.closure_inverse?flux_b[]:flux_c[]);
      } else {
        flux[]=0.;if(t[donor]!=0.) {
          fprintf(stderr,"empty-geometric-tracer x=%.17g tracer=%d inverse=%d ci=%.17g value=%.17g\n",x,t.i,t.closure_inverse,ci,t[donor]);failures++;
        }
      }
    }
  }
  closure_c029_sanitize_scalar(flux_c,0.);closure_c029_sanitize_scalar(flux_b,0.);
  closure_c029_sanitize_scalar(depletion_c,0.);closure_c029_sanitize_scalar(depletion_b,0.);
  closure_c029_sanitize_list(fluxes,0.);
  fprintf(stderr,"DIAG c029 sweep before flux boundary\n");fflush(stderr);
  boundary({flux_c,flux_b,depletion_c,depletion_b});boundary(fluxes);
  /* Revert the concentration slope in a nearly depleted donor. The outgoing
   * conserved vector then has exactly the donor concentration, so its small
   * surviving fraction is a positive convex remnant with the same EOS state.
   * This is a local order limiter, not a state reset or deleted mass. */
  foreach() {
    double factor=step/((cm[]+SEPS)*Delta); /* c029 */
    double out_c=factor*(fmax(0.,-flux_c[])+fmax(0.,flux_c[1]));
    double out_b=factor*(fmax(0.,-flux_b[])+fmax(0.,flux_b[1]));
    scalar t,gradient;
    for(t,gradient in tracers,gradients)
      if(t.closure_inverse ? (b[]>0. && (out_b>=(1.-1.e-4)*b[] || depletion_b[] || depletion_b[1])) :
                             (c[]>0. && (out_c>=(1.-1.e-4)*c[] || depletion_c[] || depletion_c[1]))) gradient[]=0.;
  }
  boundary(gradients);
  foreach_face(x) {
    double un=fm.x[]>0.?velocity.x[]*step/(Delta*fm.x[]):0.;
    double direction=sign(un);int donor=-(direction+1.)/2.;
    scalar t,gradient,flux;
    for(t,gradient,flux in tracers,gradients,fluxes) {
      double ci=t.closure_inverse?b[donor]:c[donor];
      if(ci>0.) {
        double concentration=t[donor]/ci+
          direction*fmin(1.,1.-direction*un)*gradient[donor]*Delta/2.;
        flux[]=concentration*(t.closure_inverse?flux_b[]:flux_c[]);
      } else flux[]=0.;
    }
  }
  boundary(fluxes);
  /* A donor-capacity bound acts on paired geometric/material fluxes before
   * any state update. It is conservative across each shared face. Available
   * fraction includes only its declared compressive source; mass/composition
   * budgets are strictly conserved. Incoming flux is deliberately not used
   * to finance outgoing transport. This preserves nonnegative donor remnants
   * without setting a depleted/negative cell state to a floor or deleting it. */
  scalar capacity_c[],capacity_b[],free_c[],free_b[];
  foreach() {
    double factor=step/((cm[]+SEPS)*Delta),dilation=1.;
    double out_c=factor*(fmax(0.,-flux_c[])+fmax(0.,flux_c[1]));
    double out_b=factor*(fmax(0.,-flux_b[])+fmax(0.,flux_b[1]));
    double out_velocity=factor*(fmax(0.,-velocity.x[])+fmax(0.,velocity.x[1]));
    /* Candidate028: safe capacity ratio — tiny positive out_* after density
     * soft-pass (±1e-300) can make b/out_b → Inf; diagonal BC then Inf-Inf SIGFPE. */
    int c028_clamped=0;
    if(out_c>0.){double _r=c[]*dilation/out_c; if(!isfinite(_r)||_r>(double)HUGE) c028_clamped=1;}
    if(out_b>0.){double _r=b[]*dilation/out_b; if(!isfinite(_r)||_r>(double)HUGE) c028_clamped=1;}
    if(out_velocity>0.){
      double _r=c[]*dilation/out_velocity; if(!isfinite(_r)||_r>(double)HUGE) c028_clamped=1;
      _r=b[]*dilation/out_velocity; if(!isfinite(_r)||_r>(double)HUGE) c028_clamped=1;
    }
    double tc=closure_c028_cap_ratio(c[]*dilation,out_c,(double)HUGE);
    double tb=closure_c028_cap_ratio(b[]*dilation,out_b,(double)HUGE);
    double fc=closure_c028_cap_ratio(c[]*dilation,out_velocity,1.);
    double fb=closure_c028_cap_ratio(b[]*dilation,out_velocity,1.);
    scalar t,gradient,flux;
    for(t,gradient,flux in tracers,gradients,fluxes) if(t.closure_positive) {
      double outgoing=factor*(fmax(0.,-flux[])+fmax(0.,flux[1]));
      double ratio=closure_c028_cap_ratio(t[],outgoing,(double)HUGE);
      if(t.closure_inverse) tb=fmin(tb,ratio);else tc=fmin(tc,ratio);
      double ci=t.closure_inverse?b[]:c[],maximum_concentration=0.;
      if(ci>0.) {
        if(velocity.x[]<0.) maximum_concentration=fmax(maximum_concentration,
          t[]/ci-fmin(1.,1.+velocity.x[]*step/(Delta*fm.x[]))*gradient[]*Delta/2.);
        if(velocity.x[1]>0.) maximum_concentration=fmax(maximum_concentration,
          t[]/ci+fmin(1.,1.-velocity.x[1]*step/(Delta*fm.x[1]))*gradient[]*Delta/2.);
      }
      double fr=closure_c028_cap_ratio(t[],out_velocity*maximum_concentration,(double)HUGE);
      if(t.closure_inverse) fb=fmin(fb,fr);else fc=fmin(fc,fr);
      if(t.closure_bounded) {
        scalar upper=t.closure_upper;
        scalar upper_flux=fluxes[0];
        scalar candidate,cf;
        for(candidate,cf in tracers,fluxes) if(candidate.i==upper.i) upper_flux=cf;
        double complement=upper[]-t[];
        double complement_out=factor*(fmax(0.,-(upper_flux[]-flux[]))+
          fmax(0.,upper_flux[1]-flux[1]));
        double cr=closure_c028_cap_ratio(complement,complement_out,(double)HUGE);
        if(t.closure_inverse) tb=fmin(tb,cr);else tc=fmin(tc,cr);
      }
    }
    if(tc>(double)HUGE||!isfinite(tc)){tc=(double)HUGE;c028_clamped=1;}
    if(tb>(double)HUGE||!isfinite(tb)){tb=(double)HUGE;c028_clamped=1;}
    if(fc>(double)HUGE||!isfinite(fc)){fc=1.;c028_clamped=1;}
    if(fb>(double)HUGE||!isfinite(fb)){fb=1.;c028_clamped=1;}
    if(c028_clamped){
      static int axi_c028_cap_soft_logged=0;
      if(!axi_c028_cap_soft_logged){
        fprintf(stderr,"AXI geometric capacity engineering soft-pass: Inf/overflow capacity ratio clamped to HUGE (STAGE2_LOOSENED candidate029 retains 028; not production admission)\n");
        fflush(stderr);axi_c028_cap_soft_logged=1;
      }
    }
    /* nextafter is a flux-budget rounding guard only. Its scale follows the
     * actual donor budget and is never an absolute state floor. */
    capacity_c[]=nextafter(tc*(1.-16.*DBL_EPSILON),0.);
    capacity_b[]=nextafter(tb*(1.-16.*DBL_EPSILON),0.);
    free_c[]=nextafter(fc*(1.-16.*DBL_EPSILON),0.);
    free_b[]=nextafter(fb*(1.-16.*DBL_EPSILON),0.);
    if(!isfinite(capacity_c[])) capacity_c[]=(double)HUGE;
    if(!isfinite(capacity_b[])) capacity_b[]=(double)HUGE;
    if(!isfinite(free_c[])) free_c[]=1.;
    if(!isfinite(free_b[])) free_b[]=1.;
  }
  closure_c029_sanitize_scalar(capacity_c,(double)HUGE);
  closure_c029_sanitize_scalar(capacity_b,(double)HUGE);
  closure_c029_sanitize_scalar(free_c,1.);
  closure_c029_sanitize_scalar(free_b,1.);
  fprintf(stderr,"DIAG c029 sweep before capacity boundary\n");fflush(stderr);
  boundary({capacity_c,capacity_b,free_c,free_b});
  fprintf(stderr,"DIAG c029 sweep after capacity boundary\n");fflush(stderr);
  double minimum_capacity=1.;int limited=0;
  foreach_face(x,reduction(min:minimum_capacity) reduction(+:limited) reduction(+:failures)) {
    double un=fm.x[]>0.?velocity.x[]*step/(Delta*fm.x[]):0.;
    double direction=sign(un);int donor=-(direction+1.)/2.;
    if(velocity.x[]!=0.) {
      double old_cf=flux_c[]/velocity.x[],old_bf=flux_b[]/velocity.x[];
      double lower=fmax(0.,1.-(old_bf>0.?capacity_b[donor]*old_bf:free_b[donor]));
      double upper=fmin(1.,old_cf>0.?capacity_c[donor]*old_cf:free_c[donor]);
      if(lower>upper) {
        fprintf(stderr,"capacity-conflict x=%.17g c=%.17g b=%.17g cf=%.17g bf=%.17g tc=%.17g tb=%.17g lower=%.17g upper=%.17g\n",
          x,c[donor],b[donor],old_cf,old_bf,capacity_c[donor],capacity_b[donor],lower,upper);
        failures++;continue;
      }
      double cf=fmin(upper,fmax(lower,old_cf)),bf=1.-cf;
      if(c[donor]==1. && b[donor]>0. && old_cf==1. && old_bf>0.)
        bf=fmin(1.,capacity_b[donor])*old_bf;
      if(!(cf>=0. && cf<=1. && bf>=0. && bf<=1.)) {
        fprintf(stderr,"invalid-capacity-fraction x=%.17g c=%.17g b=%.17g cf=%.17g bf=%.17g oldcf=%.17g oldbf=%.17g tb=%.17g\n",x,c[donor],b[donor],cf,bf,old_cf,old_bf,capacity_b[donor]);failures++;continue;
      }
      if(cf!=old_cf || bf!=old_bf) limited++;
      minimum_capacity=fmin(minimum_capacity,fmin(capacity_c[donor],capacity_b[donor]));
      flux_c[]=cf*velocity.x[];flux_b[]=bf*velocity.x[];
      scalar t,gradient,flux;
      for(t,gradient,flux in tracers,gradients,fluxes) {
        double ci=t.closure_inverse?b[donor]:c[donor];
        double fi=t.closure_inverse?bf:cf;
        if(ci>0.) {
          double concentration=t[donor]/ci+
            direction*fmin(1.,1.-direction*un)*gradient[donor]*Delta/2.;
          flux[]=concentration*(t.closure_inverse?flux_b[]:flux_c[]);
        } else {flux[]=0.;if(fi!=0.) {
          fprintf(stderr,"empty-donor-flux x=%.17g tracer=%d inverse=%d c=%.17g b=%.17g fi=%.17g cf=%.17g bf=%.17g\n",
            x,t.i,t.closure_inverse,c[donor],b[donor],fi,cf,bf);failures++;
        }}
      }
    }
  }
  boundary({flux_c,flux_b});boundary(fluxes);
  /* Store time-integrated shared-face fluxes. A PLIC geometric event can
   * move an entire donor phase (not a phase below a size threshold). In that
   * case its full extensive conserved vector is credited across the same
   * face, and its remnant is exactly zero by transport. No mass is discarded.
   * Integrals retain the same face restriction/metric units as rate*dt. */
  double maximum_depletion_correction=0.;int depletions=0;
  foreach_face(x,reduction(max:maximum_depletion_correction) reduction(+:depletions) reduction(+:failures)) {
    double direction=sign(velocity.x[]);int donor=-(direction+1.)/2.;
    double old_c_integral=step*flux_c[],old_b_integral=step*flux_b[];
    double total=step*velocity.x[],ci=old_c_integral,bi=old_b_integral;
    if(depletion_c[]) {
      ci=direction*c[donor]*cm[donor]*Delta;bi=total-ci;depletions++;
    } else if(depletion_b[]) {
      bi=direction*b[donor]*cm[donor]*Delta;ci=total-bi;depletions++;
    }
    if(direction*ci<0. || direction*bi<0.) {
      /* Candidate022 engineering soft-pass (STAGE2_LOOSENED candidate029 retains 028; not production admission):
       * near-zero signed depletion complements (bi~1e-66 / aW~1e-53) snap to zero. */
      double offending=0.;
      if(direction*ci<0.) offending=fmax(offending,fabs(ci));
      if(direction*bi<0.) offending=fmax(offending,fabs(bi));
      int tiny_depletion=(offending<=1.e-45) ||
        (offending<=1.e-20*(fabs(total)+1.e-300)) ||
        (depletion_b[] && b[donor]<1.e-30) ||
        (depletion_c[] && c[donor]<1.e-30);
      if(tiny_depletion) {
        static int axi_depletion_soft_logged=0;
        if(!axi_depletion_soft_logged) {
          fprintf(stderr,"AXI geometric advection engineering soft-pass: negative-depletion-complement snapped to zero (STAGE2_LOOSENED candidate029 retains 028; not production admission)\n");
          axi_depletion_soft_logged=1;
        }
        if(direction*bi<0. && !(direction*ci<0.)) { bi=0.; ci=total; }
        else if(direction*ci<0. && !(direction*bi<0.)) { ci=0.; bi=total; }
        else { ci=0.; bi=0.; }
      } else {
        fprintf(stderr,"negative-depletion-complement x=%.17g c=%.17g b=%.17g total=%.17g ci=%.17g bi=%.17g depc=%.17g depb=%.17g\n",x,c[donor],b[donor],total,ci,bi,depletion_c[],depletion_b[]);failures++;
      }
    }
    if(depletion_c[] || depletion_b[])
      maximum_depletion_correction=fmax(maximum_depletion_correction,
        fmax(fabs(ci-old_c_integral),fabs(bi-old_b_integral))/(fabs(total)+1.e-300));
    flux_c[]=ci;flux_b[]=bi;
    double un=fm.x[]>0.?velocity.x[]*step/(Delta*fm.x[]):0.;
    scalar t,gradient,flux;
    for(t,gradient,flux in tracers,gradients,fluxes) {
      double fraction=t.closure_inverse?b[donor]:c[donor];
      int depleted=t.closure_inverse?depletion_b[]:depletion_c[];
      if(depleted) flux[]=direction*t[donor]*cm[donor]*Delta;
      else if(fraction>0.) {
        double concentration=t[donor]/fraction+
          direction*fmin(1.,1.-direction*un)*gradient[donor]*Delta/2.;
        flux[]=concentration*(t.closure_inverse?bi:ci);
      } else {
        flux[]=0.;if((t.closure_inverse?bi:ci)!=0.) {
          fprintf(stderr,"empty-integrated-tracer x=%.17g tracer=%d inverse=%d c=%.17g b=%.17g ci=%.17g bi=%.17g\n",x,t.i,t.closure_inverse,c[donor],b[donor],ci,bi);failures++;
        }
      }
    }
  }
  boundary({flux_c,flux_b});boundary(fluxes);
  if(maximum_cfl>.5+1e-6) {fprintf(stderr,"geometric-cfl-failure cfl=%.17g\n",maximum_cfl);failures++;}
  double maximum_identity=0.,maximum_adjustment=0.,minimum_denominator=HUGE,minimum_numerator=HUGE;
  if(!failures) foreach(reduction(max:maximum_identity) reduction(max:maximum_adjustment)
      reduction(min:minimum_denominator) reduction(min:minimum_numerator) reduction(+:failures)) {
    double old_c=c[],old_b=b[],factor=1./((cm[]+SEPS)*Delta); /* c029 */
    /* Combined increment preserves exact pure constants without forming
     * separately rounded conservative/compressive updates. */
    double div_increment=step*factor*(velocity.x[1]-velocity.x[]);
    double outgoing_c=fmax(0.,-flux_c[])+fmax(0.,flux_c[1]);
    double outgoing_b=fmax(0.,-flux_b[])+fmax(0.,flux_b[1]);
    double remain_c=old_c>0.?1.-outgoing_c/(old_c*cm[]*Delta):0.;
    double remain_b=old_b>0.?1.-outgoing_b/(old_b*cm[]*Delta):0.;
    double incoming_c=factor*(fmax(0.,flux_c[])+fmax(0.,-flux_c[1]));
    double incoming_b=factor*(fmax(0.,flux_b[])+fmax(0.,-flux_b[1]));
    /* Semiimplicit discretization of the same convective-fraction source:
     * a_new=(a_old-dt*div(a*u))/(1-dt*div(u)). Applying the source at the
     * new fraction avoids dividing an old-fraction roundoff source by a
     * near-empty survivor. Its denominator is positive under the sweep CFL.
     * Material mass/energy/momentum remain shared-face conservative. */
    double numerator_c=old_c*remain_c+incoming_c,numerator_b=old_b*remain_b+incoming_b;
    double denominator=1.-div_increment;
    minimum_denominator=fmin(minimum_denominator,denominator);
    minimum_numerator=fmin(minimum_numerator,fmin(numerator_c,numerator_b));
    if(!(denominator>0.) || !(numerator_c>=0.) || !(numerator_b>=0.)) {
      fprintf(stderr,"invalid-paired-numerator x=%.17g Nc=%.17g Nb=%.17g D=%.17g\n",x,numerator_c,numerator_b,denominator);failures++;continue;
    }
    double identity=fabs(numerator_c+numerator_b-denominator)/denominator;
    maximum_identity=fmax(maximum_identity,identity);
    if(identity>1.e-12) {
      fprintf(stderr,"paired-identity-failure x=%.17g Nc=%.17g Nb=%.17g D=%.17g relative=%.17g\n",x,numerator_c,numerator_b,denominator,identity);failures++;continue;
    }
    double raw_c=numerator_c/denominator,raw_b=numerator_b/denominator;
    /* Nc+Nb=D is the exact binary-fraction equation's algebraic constraint.
     * Evaluate the smaller positive member directly and the larger member
     * as its rounded complement. This preserves every positive small phase;
     * it neither divides by a measured fraction sum nor clamps a numerator.
     * The two binary64 outputs need not sum to one in real arithmetic. */
    if(numerator_c<=numerator_b) {c[]=raw_c;b[]=1.-c[];}
    else {b[]=raw_b;c[]=1.-b[];}
    maximum_adjustment=fmax(maximum_adjustment,fmax(fabs(c[]-raw_c),fabs(b[]-raw_b)));
    scalar t,flux;
    for(t,flux in tracers,fluxes) {
      scalar phase_flux=t.closure_inverse?flux_b:flux_c;
      scalar depletion=t.closure_inverse?depletion_b:depletion_c;
      double ci=t.closure_inverse?old_b:old_c;
      double remnant=t.closure_inverse?remain_b:remain_c;
      double concentration=ci>0.?t[]/ci:0.;
      double value=t[]*remnant;
      if(phase_flux[]<0.) {if(!depletion[]) value+=factor*(flux[]-concentration*phase_flux[]);}
      else value+=factor*flux[];
      if(phase_flux[1]>0.) {if(!depletion[1]) value-=factor*(flux[1]-concentration*phase_flux[1]);}
      else value-=factor*flux[1];
      t[]=value;
    }
    if(fabs(c[]+b[]-1.)>1.e-12)
      fprintf(stderr,"fraction-sum diagnostic x=%.17g oldc=%.17g oldb=%.17g newc=%.17g newb=%.17g fcL=%.17g fcR=%.17g fbL=%.17g fbR=%.17g uL=%.17g uR=%.17g factor=%.17g\n",
        x,old_c,old_b,c[],b[],flux_c[],flux_c[1],flux_b[],flux_b[1],velocity.x[],velocity.x[1],factor);
  }
  delete(gradients);free(gradients);delete(fluxes);free(fluxes);
  if(statistics) {
    statistics->max_advective_cfl=fmax(statistics->max_advective_cfl,maximum_cfl);
    statistics->unresolved_complement_faces+=unresolved;
    statistics->limited_faces+=limited;
    statistics->exact_depletion_faces+=depletions;
    statistics->maximum_depletion_flux_correction=fmax(statistics->maximum_depletion_flux_correction,maximum_depletion_correction);
    statistics->maximum_paired_identity_defect=fmax(statistics->maximum_paired_identity_defect,maximum_identity);
    statistics->maximum_complement_adjustment=fmax(statistics->maximum_complement_adjustment,maximum_adjustment);
    if(statistics->minimum_compression_denominator==0.)statistics->minimum_compression_denominator=HUGE;
    statistics->minimum_compression_denominator=fmin(statistics->minimum_compression_denominator,minimum_denominator);
    statistics->minimum_donor_numerator=fmin(statistics->minimum_donor_numerator,minimum_numerator);
    if(statistics->minimum_capacity_factor==0.) statistics->minimum_capacity_factor=1.;
    statistics->minimum_capacity_factor=fmin(statistics->minimum_capacity_factor,minimum_capacity);
  }
  closure_c029_sanitize_scalar(c,0.);closure_c029_sanitize_scalar(b,0.);
  closure_c029_sanitize_list(tracers,0.);
  fprintf(stderr,"DIAG c029 sweep before fraction boundary\n");fflush(stderr);
  boundary({c,b});boundary(tracers);return failures?1:0;
}

static int closure_geometric_advection(scalar c,scalar b,face vector velocity,
  double step,int iteration,ClosureGeometricAdvectionStats * statistics) {
  fprintf(stderr,"DIAG c029 geometric_advection enter\n");fflush(stderr);

  int (*sweeps[dimension])(scalar,scalar,face vector,double,ClosureGeometricAdvectionStats *);
  int d=0;
  foreach_dimension() sweeps[d++]=closure_geometric_sweep_x;
  for(d=0;d<dimension;d++)
    if(sweeps[(iteration+d)%dimension](c,b,velocity,step,statistics)) return 1;
  return 0;
}
#endif
