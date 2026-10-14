/* EOS_DIAGNOSTIC_001_BEGIN */#include "eos_diagnostic_api.h"
/* EOS_DIAGNOSTIC_001_END *//* One-potential caloric Mie-Gruneisen water candidate. Sourced Hugoniot;
 * constant Cv/G and tensile continuation are declared original premises.
 * No pressure/temperature/energy floor or compressed-volume extrapolation. */
#ifndef CLOSURE_WATER_MG_H
#define CLOSURE_WATER_MG_H
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
  uint32_t n;
  double cv,G,v0,p0,T0,c0,xmin,xmax;
  double * nodes;
} ClosureWaterMG;
typedef struct {
  double rho,v,T,p,e,s,cp,cv,cT2,c2,p_e,p_rho,ec,ecx,ecxx;
} ClosureWaterState;

static int closure_water_load(const char * filename,ClosureWaterMG * eos) {
  memset(eos,0,sizeof(*eos));
  FILE * stream=fopen(filename,"rb");if(!stream) return 1;
  char magic[8];double values[8];
  int fail=fread(magic,1,8,stream)!=8 || memcmp(magic,"WMCOLD1\0",8) ||
    fread(&eos->n,4,1,stream)!=1 || fread(values,8,8,stream)!=8 || eos->n<2;
  if(fail) {fclose(stream);return 2;}
  eos->cv=values[0];eos->G=values[1];eos->v0=values[2];eos->p0=values[3];
  eos->T0=values[4];eos->c0=values[5];eos->xmin=values[6];eos->xmax=values[7];
  eos->nodes=malloc(3*eos->n*sizeof(double));
  if(!eos->nodes || fread(eos->nodes,8,3*eos->n,stream)!=3*eos->n || fgetc(stream)!=EOF) fail=1;
  fclose(stream);return fail?3:0;
}

static void closure_water_free(ClosureWaterMG * eos) {free(eos->nodes);eos->nodes=NULL;}

static int closure_water_cold_ld_eos_diagnostic_original(const ClosureWaterMG * eos,long double v,long double * ec,long double * ecx,long double * ecxx) {
  if(!(v>0.) || !(eos->n>1) || !eos->nodes) return 1;
  long double x=logl(v/eos->v0);
  if(x<eos->xmin) return 2;
  if(x>=0.) {
    long double d=v-eos->v0,k=(long double)eos->c0*eos->c0/((long double)eos->v0*eos->v0);
    long double th=eos->T0*expl(-eos->G*x),ph=eos->p0-k*d;
    *ec=-eos->p0*d+.5*k*d*d-eos->cv*th;
    *ecx=-v*ph+eos->G*eos->cv*th;
    *ecxx=-v*ph+v*v*k-eos->G*eos->G*eos->cv*th;
    return !isfinite(*ec+*ecx+*ecxx);
  }
  long double h=((long double)eos->xmax-eos->xmin)/(eos->n-1);
  long double position=(x-eos->xmin)/h;
  uint32_t cell=(uint32_t)floorl(position);if(cell>=eos->n-1) cell=eos->n-2;
  long double t=position-cell;double * l=eos->nodes+3*cell,* r=l+3;
  long double c[6]={l[0],h*l[1],.5L*h*h*l[2],0.L,0.L,0.L};
  long double A=r[0]-c[0]-c[1]-c[2],B=h*r[1]-c[1]-2.L*c[2],C=h*h*r[2]-2.L*c[2];
  c[3]=10.*A-4.*B+.5*C;c[4]=-15.*A+7.*B-C;c[5]=6.*A-3.*B+.5*C;
  *ec=c[0]+t*(c[1]+t*(c[2]+t*(c[3]+t*(c[4]+t*c[5]))));
  *ecx=(c[1]+t*(2.*c[2]+t*(3.*c[3]+t*(4.*c[4]+t*5.*c[5]))))/h;
  *ecxx=(2.*c[2]+t*(6.*c[3]+t*(12.*c[4]+t*20.*c[5])))/(h*h);
  return !isfinite(*ec+*ecx+*ecxx);
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_water_cold_ld(const ClosureWaterMG * eos,long double v,long double * ec,long double * ecx,long double * ecxx) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_WATER_COLD_POTENTIAL);
  int value=closure_water_cold_ld_eos_diagnostic_original(eos,v,ec,ecx,ecxx);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_water_cold(const ClosureWaterMG * eos,double v,double * ec,double * ecx,double * ecxx) {
  long double e,ex,exx;
  int status=closure_water_cold_ld(eos,v,&e,&ex,&exx);
  if(!status) {*ec=(double)e;*ecx=(double)ex;*ecxx=(double)exx;}
  return status;
}

static int closure_water_rho_e_eos_diagnostic_original(const ClosureWaterMG * eos,double rho,double e,ClosureWaterState * state) {
  if(!(rho>0.) || !isfinite(e)) return 1;
  state->rho=rho;state->v=1./rho;state->e=e;
  if(closure_water_cold(eos,state->v,&state->ec,&state->ecx,&state->ecxx)) return 2;
  state->T=(e-state->ec)/eos->cv;if(!(state->T>0.)) return 3;
  state->p=(-state->ecx+eos->G*(e-state->ec))/state->v;
  state->s=eos->cv*(log(state->T/eos->T0)+eos->G*log(state->v/eos->v0));
  state->cv=eos->cv;
  state->cT2=state->ecxx-state->ecx+eos->G*eos->cv*state->T;
  state->c2=state->cT2+eos->G*eos->G*eos->cv*state->T;
  if(!(state->cT2>0.) || !(state->c2>0.)) return 4;
  state->cp=eos->cv+eos->G*eos->G*eos->cv*eos->cv*state->T/state->cT2;
  state->p_e=eos->G/state->v;
  state->p_rho=state->ecxx-(1.-eos->G)*state->ecx+eos->G*(e-state->ec);
  return !isfinite(state->p+state->T+state->s+state->cp+state->c2+state->p_e+state->p_rho);
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_water_rho_e(const ClosureWaterMG * eos,double rho,double e,ClosureWaterState * state) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_WATER_CALORIC_RAW);
  int value=closure_water_rho_e_eos_diagnostic_original(eos,rho,e,state);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_water_rho_T_eos_diagnostic_original(const ClosureWaterMG * eos,double rho,double T,ClosureWaterState * state) {
  if(!(rho>0.) || !(T>0.)) return 1;
  double ec,ecx,ecxx;
  if(closure_water_cold(eos,1./rho,&ec,&ecx,&ecxx)) return 2;
  return closure_water_rho_e(eos,rho,ec+eos->cv*T,state);
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_water_rho_T(const ClosureWaterMG * eos,double rho,double T,ClosureWaterState * state) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_WATER_RHO_T_ENTRY);
  int value=closure_water_rho_T_eos_diagnostic_original(eos,rho,T,state);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */

static int closure_water_rho_p_eos_diagnostic_original(const ClosureWaterMG * eos,double rho,double p,ClosureWaterState * state) {
  if(!(rho>0.) || !isfinite(p)) return 1;
  double ec,ecx,ecxx,v=1./rho;
  if(closure_water_cold(eos,v,&ec,&ecx,&ecxx)) return 2;
  return closure_water_rho_e(eos,rho,ec+(p*v+ecx)/eos->G,state);
}/* EOS_DIAGNOSTIC_001_BEGIN */
static int closure_water_rho_p(const ClosureWaterMG * eos,double rho,double p,ClosureWaterState * state) {
  ClosureEOSDiagToken token=closure_eos_diag_enter(CLOSURE_EOS_WATER_RHO_P_ENTRY);
  int value=closure_water_rho_p_eos_diagnostic_original(eos,rho,p,state);
  closure_eos_diag_leave(token,value);
  return value;
}
/* EOS_DIAGNOSTIC_001_END */
#endif
