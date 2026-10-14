/* Original explicit finite-volume full Newtonian/Fourier operator.
 * Uniform Cartesian (z,r) or axisymmetric, no swirl. This is a transport
 * building block; it contains no fluid advection, pressure or phase reaction.
 * Total energy uses exactly the stress face flux used in momentum. Native
 * incomplete Basilisk viscosity is not called. No thermodynamic floors.
 * Coordinates: z is axial, r is second Cartesian/radial coordinate.
 * Units: SI. mu shear viscosity, zeta nonnegative bulk viscosity.
 */
#ifndef CLOSURE_TRANSPORT_FV_H
#define CLOSURE_TRANSPORT_FV_H
#include <math.h>
#include <stdlib.h>
#include <string.h>

enum ClosureTransportBoundary { CLOSURE_PERIODIC=0, CLOSURE_SLIP=1,
  CLOSURE_NOSLIP=2, CLOSURE_LINEAR_EXTRAPOLATE=3 };
typedef struct {
  int nz,nr,axisymmetric,bz,br;
  double dz,dr;
  double *rho,*qz,*qr,*energy,*temperature,*mu,*zeta,*kappa;
} ClosureTransportGrid;
typedef struct {
  double viscous_entropy_rate,heat_entropy_rate,boundary_energy_rate;
  double maximum_momentum_source,minimum_internal_energy;
} ClosureTransportDiagnostics;

static inline int closure_transport_index (ClosureTransportGrid * g,int i,int j) {
  return i*g->nr+j;
}
static inline double closure_transport_cell (ClosureTransportGrid * g,
                                             const double *field,int i,int j) {
  if (i < 0 || i >= g->nz) {
    if (g->bz == CLOSURE_PERIODIC) i=(i%g->nz+g->nz)%g->nz;
    else if (g->bz == CLOSURE_LINEAR_EXTRAPOLATE) {
      int edge=i<0?0:g->nz-1, next=i<0?1:g->nz-2;
      return 2.*closure_transport_cell(g,field,edge,j)-closure_transport_cell(g,field,next,j);
    } else i=i<0?0:g->nz-1;
  }
  if (j < 0 || j >= g->nr) {
    if (g->br == CLOSURE_PERIODIC && !g->axisymmetric) j=(j%g->nr+g->nr)%g->nr;
    else if (g->br == CLOSURE_LINEAR_EXTRAPOLATE && j >= g->nr) {
      return 2.*field[closure_transport_index(g,i,g->nr-1)]-
        field[closure_transport_index(g,i,g->nr-2)];
    } else j=j<0?0:g->nr-1;
  }
  return field[closure_transport_index(g,i,j)];
}
static inline double closure_transport_velocity (ClosureTransportGrid *g,
                                                  const double *q,int component,
                                                  int i,int j) {
  if (i < 0 || i >= g->nz) {
    if (g->bz == CLOSURE_PERIODIC) i=(i%g->nz+g->nz)%g->nz;
    else if (g->bz == CLOSURE_LINEAR_EXTRAPOLATE) {
      int edge=i<0?0:g->nz-1,next=i<0?1:g->nz-2;
      return 2.*closure_transport_velocity(g,q,component,edge,j)-
        closure_transport_velocity(g,q,component,next,j);
    } else {
      int edge=i<0?0:g->nz-1;
      double parity=component==0 || g->bz==CLOSURE_NOSLIP ? -1.:1.;
      return parity*closure_transport_velocity(g,q,component,edge,j);
    }
  }
  if (j < 0 || j >= g->nr) {
    if (g->br == CLOSURE_PERIODIC && !g->axisymmetric) j=(j%g->nr+g->nr)%g->nr;
    else if (g->br == CLOSURE_LINEAR_EXTRAPOLATE && j >= g->nr) {
      return 2.*closure_transport_velocity(g,q,component,i,g->nr-1)-
        closure_transport_velocity(g,q,component,i,g->nr-2);
    } else {
      int edge=j<0?0:g->nr-1;
      double parity=component==1 || (j>=g->nr && g->br==CLOSURE_NOSLIP) ? -1.:1.;
      return parity*closure_transport_velocity(g,q,component,i,edge);
    }
  }
  int location=closure_transport_index(g,i,j);
  return q[location]/g->rho[location];
}
static inline double closure_transport_gradient (ClosureTransportGrid *g,
                                                 const double*q,int component,
                                                 int direction,int i,int j) {
  return direction==0 ?
    (closure_transport_velocity(g,q,component,i+1,j)-closure_transport_velocity(g,q,component,i-1,j))/(2*g->dz):
    (closure_transport_velocity(g,q,component,i,j+1)-closure_transport_velocity(g,q,component,i,j-1))/(2*g->dr);
}

/* Face tensor: output normal stress and axial/radial off-diagonal stress. */
static inline void closure_transport_stress (ClosureTransportGrid*g,int direction,
                                            int i,int j,double*normal,double*shear) {
  int il=i-(direction==0),jl=j-(direction==1);
  double mu=.5*(closure_transport_cell(g,g->mu,il,jl)+closure_transport_cell(g,g->mu,i,j));
  double bulk=.5*(closure_transport_cell(g,g->zeta,il,jl)+closure_transport_cell(g,g->zeta,i,j));
  double zz,rr,zr,rz,theta=0.;
  if (direction==0) {
    zz=(closure_transport_velocity(g,g->qz,0,i,j)-closure_transport_velocity(g,g->qz,0,il,jl))/g->dz;
    rz=(closure_transport_velocity(g,g->qr,1,i,j)-closure_transport_velocity(g,g->qr,1,il,jl))/g->dz;
    rr=.5*(closure_transport_gradient(g,g->qr,1,1,i,j)+closure_transport_gradient(g,g->qr,1,1,il,jl));
    zr=.5*(closure_transport_gradient(g,g->qz,0,1,i,j)+closure_transport_gradient(g,g->qz,0,1,il,jl));
    if(g->axisymmetric) theta=.5*(closure_transport_velocity(g,g->qr,1,i,j)+
      closure_transport_velocity(g,g->qr,1,il,jl))/((j+.5)*g->dr);
  } else {
    rr=(closure_transport_velocity(g,g->qr,1,i,j)-closure_transport_velocity(g,g->qr,1,il,jl))/g->dr;
    zr=(closure_transport_velocity(g,g->qz,0,i,j)-closure_transport_velocity(g,g->qz,0,il,jl))/g->dr;
    zz=.5*(closure_transport_gradient(g,g->qz,0,0,i,j)+closure_transport_gradient(g,g->qz,0,0,il,jl));
    rz=.5*(closure_transport_gradient(g,g->qr,1,0,i,j)+closure_transport_gradient(g,g->qr,1,0,il,jl));
    if(g->axisymmetric) theta=j==0 ? rr : .5*(closure_transport_velocity(g,g->qr,1,i,j)+
      closure_transport_velocity(g,g->qr,1,il,jl))/(j*g->dr);
  }
  double divergence=zz+rr+theta;
  *normal=2*mu*((direction==0?zz:rr)-divergence/3.)+bulk*divergence;
  *shear=mu*(zr+rz);
}

static inline int closure_transport_step (ClosureTransportGrid*g,double dt,
                                          ClosureTransportDiagnostics*out) {
  if(g->nz<2 || g->nr<2 || !(dt>0.) || !(g->dz>0.) || !(g->dr>0.) ||
     (g->axisymmetric && g->br==CLOSURE_PERIODIC)) return 1;
  int size=g->nz*g->nr;
  double *sourcez=calloc(size,sizeof(double)),*sourcer=calloc(size,sizeof(double));
  double *midz=malloc(size*sizeof(double)),*midr=malloc(size*sizeof(double));
  double *energy_source=calloc(size,sizeof(double));
  if(!sourcez||!sourcer||!midz||!midr||!energy_source) return 2;
  memset(out,0,sizeof(*out)); out->minimum_internal_energy=INFINITY;
  for(int i=0;i<g->nz;i++) for(int j=0;j<g->nr;j++) {
    int c=closure_transport_index(g,i,j);
    if(!(g->rho[c]>0.) || !(g->temperature[c]>0.) || g->mu[c]<0. ||
       g->zeta[c]<0. || g->kappa[c]<0.) return 3;
  }
  for(int d=0;d<2;d++) for(int i=0;i<g->nz+(d==0);i++)
    for(int j=0;j<g->nr+(d==1);j++) {
      int il=i-(d==0),jl=j-(d==1);
      double normal,shear;closure_transport_stress(g,d,i,j,&normal,&shear);
      double area=(d==0?g->dr:g->dz)*(g->axisymmetric?(d==0?(j+.5)*g->dr:j*g->dr):1.);
      double fluxz=(d==0?normal:shear)*area,fluxr=(d==0?shear:normal)*area;
      if(il>=0&&jl>=0&&il<g->nz&&jl<g->nr) {
        int c=closure_transport_index(g,il,jl); sourcez[c]+=fluxz;sourcer[c]+=fluxr;
      }
      if(i<g->nz&&j<g->nr) {
        int c=closure_transport_index(g,i,j);sourcez[c]-=fluxz;sourcer[c]-=fluxr;
      }
    }
  for(int i=0;i<g->nz;i++) for(int j=0;j<g->nr;j++) {
    int c=closure_transport_index(g,i,j);double r=(j+.5)*g->dr;
    double volume=g->dz*g->dr*(g->axisymmetric?r:1.);
    double zz=closure_transport_gradient(g,g->qz,0,0,i,j),rr=closure_transport_gradient(g,g->qr,1,1,i,j);
    double theta=g->axisymmetric?closure_transport_velocity(g,g->qr,1,i,j)/r:0.;
    double off=.5*(closure_transport_gradient(g,g->qz,0,1,i,j)+closure_transport_gradient(g,g->qr,1,0,i,j));
    double div=zz+rr+theta;
    double tau_theta=2*g->mu[c]*(theta-div/3.)+g->zeta[c]*div;
    if(g->axisymmetric) sourcer[c]-=tau_theta*volume/r;
    sourcez[c]/=volume;sourcer[c]/=volume;
    out->maximum_momentum_source=fmax(out->maximum_momentum_source,fmax(fabs(sourcez[c]),fabs(sourcer[c])));
    midz[c]=g->qz[c]+.5*dt*sourcez[c];midr[c]=g->qr[c]+.5*dt*sourcer[c];
    double dissipation=2*g->mu[c]*((zz-div/3.)*(zz-div/3.)+(rr-div/3.)*(rr-div/3.)+
      (theta-div/3.)*(theta-div/3.)+2*off*off)+g->zeta[c]*div*div;
    out->viscous_entropy_rate+=dissipation*volume/g->temperature[c];
  }
  for(int d=0;d<2;d++) for(int i=0;i<g->nz+(d==0);i++)
    for(int j=0;j<g->nr+(d==1);j++) {
      int il=i-(d==0),jl=j-(d==1);
      double normal,shear;closure_transport_stress(g,d,i,j,&normal,&shear);
      double uz=.5*(closure_transport_velocity(g,midz,0,i,j)+closure_transport_velocity(g,midz,0,il,jl));
      double ur=.5*(closure_transport_velocity(g,midr,1,i,j)+closure_transport_velocity(g,midr,1,il,jl));
      double Tl=closure_transport_cell(g,g->temperature,il,jl),Tr=closure_transport_cell(g,g->temperature,i,j);
      double kl=closure_transport_cell(g,g->kappa,il,jl),kr=closure_transport_cell(g,g->kappa,i,j);
      double k=kl>0.&&kr>0.?2*kl*kr/(kl+kr):0.;
      double h=d==0?g->dz:g->dr,gradient=(Tr-Tl)/h;
      double area=(d==0?g->dr:g->dz)*(g->axisymmetric?(d==0?(j+.5)*g->dr:j*g->dr):1.);
      double flux=((d==0?normal*uz+shear*ur:shear*uz+normal*ur)+k*gradient)*area;
      int left=il>=0&&jl>=0&&il<g->nz&&jl<g->nr,right=i<g->nz&&j<g->nr;
      if(left) energy_source[closure_transport_index(g,il,jl)]+=flux;
      if(right) energy_source[closure_transport_index(g,i,j)]-=flux;
      if(!left) out->boundary_energy_rate-=flux;
      if(!right) out->boundary_energy_rate+=flux;
      /* Half boundary faces avoid double-counting periodic equivalents. */
      out->heat_entropy_rate+=k*gradient*gradient/(Tl*Tr)*area*h*(left&&right?1.:.5);
    }
  for(int i=0;i<g->nz;i++) for(int j=0;j<g->nr;j++) {
    int c=closure_transport_index(g,i,j);double volume=g->dz*g->dr*(g->axisymmetric?(j+.5)*g->dr:1.);
    g->qz[c]+=dt*sourcez[c];g->qr[c]+=dt*sourcer[c];g->energy[c]+=dt*energy_source[c]/volume;
    double internal=g->energy[c]-(g->qz[c]*g->qz[c]+g->qr[c]*g->qr[c])/(2*g->rho[c]);
    out->minimum_internal_energy=fmin(out->minimum_internal_energy,internal);
  }
  free(sourcez);free(sourcer);free(midz);free(midr);free(energy_source);return 0;
}
#endif
