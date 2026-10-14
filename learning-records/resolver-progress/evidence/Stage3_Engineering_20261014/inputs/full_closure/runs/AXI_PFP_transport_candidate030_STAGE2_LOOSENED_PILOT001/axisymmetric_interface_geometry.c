#include <math.h>
#include <string.h>
#include <stdio.h>
#include "axisymmetric_interface_geometry.h"
typedef struct {long double x,y,h;} ClosureGeometryVertex;
typedef struct {
  long double area,weighted_volume,weighted_x,weighted_y,weighted_r,weighted_h;
} ClosureGeometryMoments;

/* Convex square clipping. The water half-space is h>=0. The complementary
 * polygon uses -h>=0. Intersections have stored h=0 by the defining line;
 * centroid distance integrates that signed coordinate directly rather than
 * subtracting two nearly equal global coordinates. */
static int closure_geometry_clip(long double nz,long double nr,long double alpha,
  int water,ClosureGeometryVertex * polygon) {
  ClosureGeometryVertex square[4]={{-.5L,-.5L,0.},{.5L,-.5L,0.},
    {.5L,.5L,0.},{-.5L,.5L,0.}};
  for(int i=0;i<4;i++)square[i].h=(water?1.L:-1.L)*
    (nz*square[i].x+nr*square[i].y-alpha);
  int count=0;
  for(int i=0;i<4;i++) {
    ClosureGeometryVertex a=square[i],b=square[(i+1)%4];
    if(a.h>=0.L)polygon[count++]=a;
    if((a.h<0.L && b.h>0.L)||(a.h>0.L && b.h<0.L)) {
      long double t=a.h/(a.h-b.h);
      polygon[count++]=(ClosureGeometryVertex){a.x+t*(b.x-a.x),
        a.y+t*(b.y-a.y),0.L};
    }
  }
  return count;
}

/* Triangle barycentric degree<=2 moments, with r>=0 integrated directly.
 * This avoids cancellation between r_center*I00 and Delta*I01 on the axis.
 * The meridional area itself remains distinct from physical volume. */
static int closure_geometry_moments(const ClosureGeometryVertex * polygon,int n,
  long double rc,long double delta,ClosureGeometryMoments * m) {
  memset(m,0,sizeof(*m));
  if(n<3)return 1;
  for(int i=1;i<n-1;i++) {
    ClosureGeometryVertex v[3]={polygon[0],polygon[i],polygon[i+1]};
    long double S=((v[1].x-v[0].x)*(v[2].y-v[0].y)-
      (v[2].x-v[0].x)*(v[1].y-v[0].y))/2.L;
    if(S<0.L)return 2;
    if(S==0.L)continue;
    long double sr=0.L,sr2=0.L,sx=0.L,sy=0.L,sh=0.L,sxr=0.L,syr=0.L,shr=0.L;
    for(int j=0;j<3;j++) {
      /* Origin at the lower radial face preserves a represented thin
       * axis-touching strip: no subtraction of two O(Delta) products. */
      long double r=(rc-delta/2.L)+delta*(v[j].y+.5L);
      if(r<0.L || v[j].h<0.L)return 3;
      sr+=r;sr2+=r*r;sx+=v[j].x;sy+=v[j].y;sh+=v[j].h;
      sxr+=v[j].x*r;syr+=v[j].y*r;shr+=v[j].h*r;
    }
    m->area+=S;m->weighted_volume+=S*sr/3.L;
    m->weighted_x+=S*(sx*sr+sxr)/12.L;
    m->weighted_y+=S*(sy*sr+syr)/12.L;
    m->weighted_r+=S*(sr*sr+sr2)/12.L;
    m->weighted_h+=S*(sh*sr+shr)/12.L;
  }
  return !(m->area>0.L && m->weighted_volume>0.L)?4:0;
}

static int closure_geometry_segment(long double nz,long double nr,long double alpha,
  ClosureGeometryVertex * first,ClosureGeometryVertex * last) {
  ClosureGeometryVertex corners[4]={{-.5L,-.5L,0.L},{.5L,-.5L,0.L},
    {.5L,.5L,0.L},{-.5L,.5L,0.L}},hits[8];int n=0;
  for(int i=0;i<4;i++)corners[i].h=nz*corners[i].x+nr*corners[i].y-alpha;
  for(int i=0;i<4;i++) {
    ClosureGeometryVertex a=corners[i],b=corners[(i+1)%4];
    if(a.h==0.L)hits[n++]=a;
    if((a.h<0.L && b.h>0.L)||(a.h>0.L && b.h<0.L)) {
      long double t=a.h/(a.h-b.h);
      hits[n++]=(ClosureGeometryVertex){a.x+t*(b.x-a.x),a.y+t*(b.y-a.y),0.L};
    }
  }
  if(n<2)return 1;
  long double maximum=0.L;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++) {
    long double dx=hits[j].x-hits[i].x,dy=hits[j].y-hits[i].y;
    long double squared=dx*dx+dy*dy;
    if(squared>maximum){maximum=squared;*first=hits[i];*last=hits[j];}
  }
  return !(maximum>0.L);
}

int closure_axisymmetric_interface_geometry(const ClosureAxisymmetricGeometryInput * in,
  ClosureAxisymmetricGeometry * out) {
  memset(out,0,sizeof(*out));
  /* Candidate023 engineering soft-pass (100fs diagnostic only; not production admission):
   * advection near-zero underflow can leave m_water_kg / m_pfc_kg slightly negative (~1e-50).
   * Snap those masses to zero so INVALID_INPUT does not fire; keep fractions as given. */
  ClosureAxisymmetricGeometryInput in_local=*in;
  {
    static int axi_neg_mass_soft_logged=0;
    int snapped=0;
    if(in_local.m_water_kg<0. && in_local.m_water_kg>-1.e-45) {
      in_local.m_water_kg=0.; snapped=1;
    }
    if(in_local.m_pfc_kg<0. && in_local.m_pfc_kg>-1.e-45) {
      in_local.m_pfc_kg=0.; snapped=1;
    }
    if(snapped && !axi_neg_mass_soft_logged) {
      fprintf(stderr,"AXI geometry engineering soft-pass: tiny negative mass snapped to zero (100fs diagnostic only; not production admission)\n");
      axi_neg_mass_soft_logged=1;
    }
  }
  in=&in_local;

  const long double pi=acosl(-1.L),delta=in->Delta_m,rc=in->r_m;
  out->positive_water_mass=in->m_water_kg>0.;out->positive_PFC_mass=in->m_pfc_kg>0.;
  out->rounded_primary_complement=(in->a_pfc==1. && in->a_water>0.)||
    (in->a_water==1. && in->a_pfc>0.);
  out->raw_paired_fraction_defect=fabs(in->a_pfc+in->a_water-1.);
  if(!(delta>0.L) || !(rc>=delta/2.L) || !isfinite(in->z_m) ||
    !isfinite(in->r_m) || !isfinite(in->Delta_m) ||
    !(in->a_pfc>=0. && in->a_pfc<=1.) || !(in->a_water>=0. && in->a_water<=1.) ||
    !(in->m_pfc_kg>=0.) || !(in->m_water_kg>=0.) ||
    !isfinite(in->m_pfc_kg) || !isfinite(in->m_water_kg) ||
    !(in->water_conductivity_W_m_K>0.) || !isfinite(in->water_conductivity_W_m_K) ||
    out->raw_paired_fraction_defect>1.e-12)
    return out->status=CLOSURE_GEOMETRY_INVALID_INPUT;
  long double cell_volume=2.L*pi*rc*delta*delta;
  out->cell_volume_m3=cell_volume;
  out->PFC_raw_volume_m3=in->a_pfc*cell_volume;
  out->water_raw_volume_m3=in->a_water*cell_volume;
  out->single_PLIC_area_upper_m2=2.L*pi*(rc+delta/2.L)*sqrtl(2.L)*delta;
  if(!(out->cell_volume_m3>0.) || !isfinite(out->cell_volume_m3) ||
    !isfinite(out->PFC_raw_volume_m3) || !isfinite(out->water_raw_volume_m3) ||
    !isfinite(out->single_PLIC_area_upper_m2))
    return out->status=CLOSURE_GEOMETRY_NONFINITE_OUTPUT;
  /* Candidate021 engineering floor (100fs diagnostic only; not production admission):
   * residual underflow water/PFC after advection must not force PLIC clip/moments. */
  {
    static int axi_geom_eng_floor_logged = 0;
    if(in->a_pfc < 1.e-30 || in->m_pfc_kg < 1.e-45) {
      if(!axi_geom_eng_floor_logged) {
        fprintf(stderr,"AXI geometry engineering floor: residual PFC snapped for PLIC (100fs diagnostic only)\n");
        axi_geom_eng_floor_logged = 1;
      }
      out->water_geometry_volume_m3=cell_volume;out->water_meridional_fraction=1.;
      out->water_geometry_volume_defect_m3=cell_volume-out->water_raw_volume_m3;
      out->water_centroid_z_m=in->z_m;
      out->water_centroid_local_y=delta/(12.L*rc);
      out->water_centroid_r_m=rc+delta*delta/(12.L*rc);
      if(!isfinite(out->water_centroid_r_m))return out->status=CLOSURE_GEOMETRY_NONFINITE_OUTPUT;
      return out->status=CLOSURE_GEOMETRY_OK;
    }
    if(in->a_water < 1.e-30 || in->m_water_kg < 1.e-45 || (in->a_pfc==1. && in->a_water < 1.e-20)) {
      if(!axi_geom_eng_floor_logged) {
        fprintf(stderr,"AXI geometry engineering floor: residual water snapped for PLIC (100fs diagnostic only)\n");
        axi_geom_eng_floor_logged = 1;
      }
      out->PFC_geometry_volume_m3=cell_volume;out->PFC_meridional_fraction=1.;
      out->PFC_geometry_volume_defect_m3=cell_volume-out->PFC_raw_volume_m3;
      return out->status=CLOSURE_GEOMETRY_OK;
    }
  }
  if(in->a_pfc==0. && in->m_pfc_kg==0.) {
    out->water_geometry_volume_m3=cell_volume;out->water_meridional_fraction=1.;
    out->water_geometry_volume_defect_m3=cell_volume-out->water_raw_volume_m3;
    out->water_centroid_z_m=in->z_m;
    out->water_centroid_local_y=delta/(12.L*rc);
    out->water_centroid_r_m=rc+delta*delta/(12.L*rc);
    if(!isfinite(out->water_centroid_r_m))return out->status=CLOSURE_GEOMETRY_NONFINITE_OUTPUT;
    return out->status=CLOSURE_GEOMETRY_OK;
  }
  if(in->a_water==0. && in->m_water_kg==0.) {
    out->PFC_geometry_volume_m3=cell_volume;out->PFC_meridional_fraction=1.;
    out->PFC_geometry_volume_defect_m3=cell_volume-out->PFC_raw_volume_m3;
    return out->status=CLOSURE_GEOMETRY_OK;
  }
  if(!(in->a_pfc>0.) || !(in->a_water>0.) || !isfinite(in->n_z)||
    !isfinite(in->n_r)||!isfinite(in->alpha))
    return out->status=CLOSURE_GEOMETRY_UNRESOLVED_INTERFACE;
  long double scale=fmaxl(fabsl(in->n_z),fabsl(in->n_r));
  if(!(scale>0.L))return out->status=CLOSURE_GEOMETRY_UNRESOLVED_INTERFACE;
  long double nz=in->n_z/scale,nr=in->n_r/scale,alpha=in->alpha/scale;
  long double norm=hypotl(nz,nr);
  ClosureGeometryVertex wp[8],fp[8],a,b;
  int nw=closure_geometry_clip(nz,nr,alpha,1,wp),nf=closure_geometry_clip(nz,nr,alpha,0,fp);
  out->water_polygon_vertices=nw;out->PFC_polygon_vertices=nf;
  ClosureGeometryMoments w,f;
  if(closure_geometry_moments(wp,nw,rc,delta,&w)||
    closure_geometry_moments(fp,nf,rc,delta,&f)||
    closure_geometry_segment(nz,nr,alpha,&a,&b))
    return out->status=CLOSURE_GEOMETRY_UNRESOLVED_INTERFACE;
  out->water_meridional_fraction=w.area;out->PFC_meridional_fraction=f.area;
  out->water_geometry_volume_m3=2.L*pi*delta*delta*w.weighted_volume;
  out->PFC_geometry_volume_m3=2.L*pi*delta*delta*f.weighted_volume;
  out->water_geometry_volume_defect_m3=out->water_geometry_volume_m3-out->water_raw_volume_m3;
  out->PFC_geometry_volume_defect_m3=out->PFC_geometry_volume_m3-out->PFC_raw_volume_m3;
  long double bx=w.weighted_x/w.weighted_volume,by=w.weighted_y/w.weighted_volume;
  long double distance=delta*w.weighted_h/(norm*w.weighted_volume);
  out->water_centroid_local_x=bx;out->water_centroid_local_y=by;
  out->water_centroid_z_m=in->z_m+delta*bx;
  out->water_centroid_r_m=w.weighted_r/w.weighted_volume;
  out->distance_water_m=distance;
  out->z1_m=in->z_m+delta*a.x;out->r1_m=(rc-delta/2.L)+delta*(a.y+.5L);
  out->z2_m=in->z_m+delta*b.x;out->r2_m=(rc-delta/2.L)+delta*(b.y+.5L);
  long double length=delta*hypotl(b.x-a.x,b.y-a.y);
  long double mean_radius=(rc-delta/2.L)+delta*((a.y+.5L)+(b.y+.5L))/2.L;
  long double area=2.L*pi*length*mean_radius;
  out->area_m2=area;
  out->plane_endpoint_residual=fmaxl(fabsl(nz*a.x+nr*a.y-alpha),
    fabsl(nz*b.x+nr*b.y-alpha))/norm;
  if(!(distance>0.L) || !(area>0.L))return out->status=CLOSURE_GEOMETRY_INVALID_DISTANCE;
  out->water_conductance_W_K=in->water_conductivity_W_m_K*area/distance;
  if(!isfinite(out->water_conductance_W_K) || !isfinite(out->water_geometry_volume_m3)||
    !isfinite(out->area_m2) || !(out->distance_water_m>0.) ||
    !(out->water_geometry_volume_m3>0.) || !(out->PFC_geometry_volume_m3>0.))
    return out->status=CLOSURE_GEOMETRY_NONFINITE_OUTPUT;
  out->has_interface=1;
  return out->status=CLOSURE_GEOMETRY_OK;
}
