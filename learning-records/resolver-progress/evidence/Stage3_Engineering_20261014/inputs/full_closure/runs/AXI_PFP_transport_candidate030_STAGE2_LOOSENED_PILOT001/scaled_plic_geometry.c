#include <math.h>
#include <string.h>
#include "scaled_plic_geometry.h"
typedef struct {long double area,I,Xr,Yr,r2,H;} ClosureScaledMoments;

static int closure_scaled_moments(const ClosureScaledPLICVertex * p,int count,
  const ClosureScaledPLICInput * in,int sign_r,ClosureScaledMoments * m) {
  memset(m,0,sizeof(*m));
  if(count<3)return 1;
  for(int i=1;i<count-1;i++) {
    ClosureScaledPLICVertex v[3]={p[0],p[i],p[i+1]};
    long double S=fabsl((v[1].X-v[0].X)*(v[2].Y-v[0].Y)-
      (v[2].X-v[0].X)*(v[1].Y-v[0].Y))/2.L;
    if(!isfinite(S))return 2;
    if(S==0.L)continue;
    long double sx=0.L,sy=0.L,sr=0.L,sr2=0.L,sh=0.L,sxr=0.L,syr=0.L,shr=0.L;
    for(int j=0;j<3;j++) {
      long double local_r=sign_r>0?v[j].Y:1.L-v[j].Y;
      long double r=in->r_lower_m+(long double)in->Delta_m*local_r;
      if(r<0.L || v[j].h<0.L || !isfinite(r+v[j].h))return 3;
      sx+=v[j].X;sy+=v[j].Y;sr+=r;sr2+=r*r;sh+=v[j].h;
      sxr+=v[j].X*r;syr+=v[j].Y*r;shr+=v[j].h*r;
    }
    m->area+=S;m->I+=S*sr/3.L;m->Xr+=S*(sx*sr+sxr)/12.L;
    m->Yr+=S*(sy*sr+syr)/12.L;m->r2+=S*(sr*sr+sr2)/12.L;
    m->H+=S*(sh*sr+shr)/12.L;
  }
  return !(m->area>0.L && m->I>0.L && isfinite(m->I+m->Xr+m->Yr+m->r2+m->H));
}

static void closure_scaled_swap(ClosureScaledPLICVertex * p,int count) {
  for(int i=0;i<count;i++){long double x=p[i].X;p[i].X=p[i].Y;p[i].Y=x;}
}

int closure_scaled_plic_geometry(const ClosureScaledPLICInput * in,ClosureScaledPLIC * out) {
  memset(out,0,sizeof(*out));out->small_material=in->small_material;
  long double pi=acosl(-1.L),D=in->Delta_m,lo=in->r_lower_m;
  if(!isfinite(in->z_lower_m)||!isfinite(in->r_lower_m)||!isfinite(in->Delta_m)||
    !(D>0.L)||lo<0.L||!isfinite(in->a_water)||!isfinite(in->a_pfc)||
    !(in->a_water>=0. && in->a_water<=1.)||!(in->a_pfc>=0. && in->a_pfc<=1.)||
    !isfinite(in->m_water_kg)||!isfinite(in->m_pfc_kg)||
    !(in->m_water_kg>=0.L)||!(in->m_pfc_kg>=0.L)||
    (in->m_water_kg>0.L)!=(in->a_water>0.)||(in->m_pfc_kg>0.L)!=(in->a_pfc>0.)||
    (in->small_material!=0 && in->small_material!=1)||
    !isfinite(in->water_conductivity_W_m_K)||!(in->water_conductivity_W_m_K>0.))
    return out->status=CLOSURE_SCALED_PLIC_INVALID_INPUT;
  out->raw_paired_fraction_defect=fabsl((long double)in->a_water+in->a_pfc-1.L);
  if(out->raw_paired_fraction_defect>1.e-12L)return out->status=CLOSURE_SCALED_PLIC_INVALID_INPUT;
  out->rounded_primary_complement=(in->a_water>0. && in->a_pfc==1.)||
    (in->a_pfc>0. && in->a_water==1.);
  /* Factored annular integral avoids a squared-radius difference. */
  out->cell_volume_m3=2.L*pi*(lo+D/2.L)*D*D;
  out->water_raw_volume_m3=in->a_water*out->cell_volume_m3;
  out->PFC_raw_volume_m3=in->a_pfc*out->cell_volume_m3;
  if(!isfinite(out->cell_volume_m3)||!(out->cell_volume_m3>0.L))
    return out->status=CLOSURE_SCALED_PLIC_NONFINITE;
  if(in->a_pfc==0.) {
    out->water_geometry_volume_m3=out->cell_volume_m3;out->water_meridional_fraction=1.L;
    out->water_geometry_volume_defect_m3=out->cell_volume_m3-out->water_raw_volume_m3;
    out->water_centroid_z_m=in->z_lower_m+D/2.L;
    long double rc=lo+D/2.L;out->water_centroid_r_m=rc+D*D/(12.L*rc);
    return out->status=CLOSURE_SCALED_PLIC_OK;
  }
  if(in->a_water==0.) {
    out->PFC_geometry_volume_m3=out->cell_volume_m3;out->PFC_meridional_fraction=1.L;
    out->PFC_geometry_volume_defect_m3=out->cell_volume_m3-out->PFC_raw_volume_m3;
    return out->status=CLOSURE_SCALED_PLIC_OK;
  }
  long double c=in->small_material?in->a_water:in->a_pfc;
  long double other=in->small_material?in->a_pfc:in->a_water;
  if(!(c>0.L && c<=.5L && c<=other)||!isfinite(in->small_normal_z)||
    !isfinite(in->small_normal_r))return out->status=CLOSURE_SCALED_PLIC_UNRESOLVED;
  long double scale=fmaxl(fabsl(in->small_normal_z),fabsl(in->small_normal_r));
  if(!(scale>0.L))return out->status=CLOSURE_SCALED_PLIC_UNRESOLVED;
  long double nz=(long double)in->small_normal_z/scale,nr=(long double)in->small_normal_r/scale;
  long double a=fabsl(nz),b=fabsl(nr),N=hypotl(a,b),A=fmaxl(a,b),B=fminl(a,b);
  out->a=a;out->b=b;out->normal_length=N;
  out->sign_z=nz>=0.L?1:-1;out->sign_r=nr>=0.L?1:-1;
  out->preferred_z_m=in->z_lower_m+(out->sign_z>0?0.L:D);
  out->preferred_r_m=lo+(out->sign_r>0?0.L:D);
  ClosureScaledPLICVertex small[6],large[6];int ns=0,nl=0;long double d,X1,Y1,X2,Y2,length;
  if(B>0.L && c<=B/(2.L*A)) {
    d=sqrtl(2.L*a*b*c);long double u=d/A,v=d/B;
    if(!(d>0.L && u>0.L && v>0.L && u<=1.L && v<=1.L))
      return out->status=CLOSURE_SCALED_PLIC_UNRESOLVED;
    small[0]=(ClosureScaledPLICVertex){0.L,0.L,d};
    small[1]=(ClosureScaledPLICVertex){u,0.L,0.L};
    small[2]=(ClosureScaledPLICVertex){0.L,v,0.L};ns=3;
    large[0]=small[1];large[1]=(ClosureScaledPLICVertex){1.L,0.L,A-d};
    large[2]=(ClosureScaledPLICVertex){1.L,1.L,A+B-d};
    large[3]=(ClosureScaledPLICVertex){0.L,1.L,B-d};large[4]=small[2];nl=5;
    X1=u;Y1=0.L;X2=0.L;Y2=v;length=D*d*N/(a*b);out->branch=1;
  } else {
    d=A*c+B/2.L;long double u0=d/A,u1=(d-B)/A;
    if(!(d>0.L && u0>0.L && u1>=0.L && u0<=1.L && u1<=1.L))
      return out->status=CLOSURE_SCALED_PLIC_UNRESOLVED;
    small[0]=(ClosureScaledPLICVertex){0.L,0.L,d};
    small[1]=(ClosureScaledPLICVertex){u0,0.L,0.L};
    small[2]=(ClosureScaledPLICVertex){u1,1.L,0.L};
    small[3]=(ClosureScaledPLICVertex){0.L,1.L,d-B};ns=4;
    large[0]=small[1];large[1]=(ClosureScaledPLICVertex){1.L,0.L,A-d};
    large[2]=(ClosureScaledPLICVertex){1.L,1.L,A+B-d};large[3]=small[2];nl=4;
    X1=u0;Y1=0.L;X2=u1;Y2=1.L;length=D*N/A;out->branch=2;
  }
  out->offset=d;
  if(b>a) {
    closure_scaled_swap(small,ns);closure_scaled_swap(large,nl);
    long double x=X1;X1=Y1;Y1=x;x=X2;X2=Y2;Y2=x;
  }
  ClosureScaledMoments ms,ml;
  if(closure_scaled_moments(small,ns,in,out->sign_r,&ms)||
    closure_scaled_moments(large,nl,in,out->sign_r,&ml))
    return out->status=CLOSURE_SCALED_PLIC_LOST_POSITIVE;
  const ClosureScaledMoments * w=in->small_material?&ms:&ml;
  const ClosureScaledMoments * f=in->small_material?&ml:&ms;
  out->water_vertices=in->small_material?ns:nl;out->PFC_vertices=in->small_material?nl:ns;
  memcpy(out->water,in->small_material?small:large,out->water_vertices*sizeof(*small));
  memcpy(out->PFC,in->small_material?large:small,out->PFC_vertices*sizeof(*small));
  out->small_fraction_reconstruction_relative_error=fabsl(ms.area-c)/c;
  out->water_meridional_fraction=w->area;out->PFC_meridional_fraction=f->area;
  out->water_geometry_volume_m3=2.L*pi*D*D*w->I;
  out->PFC_geometry_volume_m3=2.L*pi*D*D*f->I;
  /* Keep the complementary continuous-polygon identity in a stable defect.
   * A tiny positive small volume must not disappear in large-minus-large. */
  if(in->small_material) {
    out->water_geometry_volume_defect_m3=out->water_geometry_volume_m3-out->water_raw_volume_m3;
    out->PFC_geometry_volume_defect_m3=(1.L-(long double)in->a_pfc)*out->cell_volume_m3-
      out->water_geometry_volume_m3;
  } else {
    out->PFC_geometry_volume_defect_m3=out->PFC_geometry_volume_m3-out->PFC_raw_volume_m3;
    out->water_geometry_volume_defect_m3=(1.L-(long double)in->a_water)*out->cell_volume_m3-
      out->PFC_geometry_volume_m3;
  }
  out->water_centroid_local_X=w->Xr/w->I;out->water_centroid_local_Y=w->Yr/w->I;
  out->water_centroid_z_m=out->preferred_z_m+out->sign_z*D*out->water_centroid_local_X;
  out->water_centroid_r_m=w->r2/w->I;
  out->distance_water_m=D*w->H/(N*w->I);
  out->segment_X1=X1;out->segment_Y1=Y1;out->segment_X2=X2;out->segment_Y2=Y2;
  out->segment_length_m=length;
  long double rr1=lo+D*(out->sign_r>0?Y1:1.L-Y1);
  long double rr2=lo+D*(out->sign_r>0?Y2:1.L-Y2);
  out->r1_m=rr1;out->r2_m=rr2;
  out->z1_m=out->preferred_z_m+out->sign_z*D*X1;
  out->z2_m=out->preferred_z_m+out->sign_z*D*X2;
  out->area_m2=2.L*pi*length*(rr1+rr2)/2.L;
  out->rounded_global_endpoints_equal=out->z1_m==out->z2_m && out->r1_m==out->r2_m;
  if(!(out->area_m2>0.L && out->distance_water_m>0.L && out->water_geometry_volume_m3>0.L &&
      out->PFC_geometry_volume_m3>0.L))return out->status=CLOSURE_SCALED_PLIC_LOST_POSITIVE;
  out->water_conductance_W_K=in->water_conductivity_W_m_K*out->area_m2/out->distance_water_m;
  if(!isfinite(out->water_conductance_W_K)||!(out->water_conductance_W_K>0.L)||
      !isfinite(out->water_geometry_volume_m3+out->PFC_geometry_volume_m3+out->area_m2+
      out->water_centroid_z_m+out->water_centroid_r_m+out->distance_water_m))
    return out->status=CLOSURE_SCALED_PLIC_NONFINITE;
  out->has_interface=1;return out->status=CLOSURE_SCALED_PLIC_OK;
}

int closure_scaled_plic_binary64_geometry_representable(const ClosureScaledPLIC * out) {
  if(out->status!=CLOSURE_SCALED_PLIC_OK)return 0;
  const long double values[]={out->water_geometry_volume_m3,out->PFC_geometry_volume_m3,
    out->area_m2,out->distance_water_m,out->water_conductance_W_K};
  int count=out->has_interface?5:2;
  for(int i=0;i<count;i++) {
    if(!out->has_interface && values[i]==0.L)continue;
    double value=(double)values[i];if(!(value>0.)||!isfinite(value))return 0;
  }
  return 1;
}
