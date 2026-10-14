#include "axisymmetric_transport_manifest.h"
#include <math.h>
#include <stdlib.h>
#include <string.h>
typedef struct {int dim,plane,lo,hi,cell,side;} AxisLeafEdge;
typedef struct {int anchor;long double offset;} AxisRetainedCoordinate;
typedef struct {AxisRetainedCoordinate lo,hi;int positive;} AxisWaterInterval;
static int axis_edge_compare(const void * av,const void * bv) {
  const AxisLeafEdge * a=av,*b=bv;
  if(a->dim!=b->dim)return a->dim<b->dim?-1:1;
  if(a->plane!=b->plane)return a->plane<b->plane?-1:1;
  if(a->side!=b->side)return a->side<b->side?-1:1;
  if(a->lo!=b->lo)return a->lo<b->lo?-1:1;
  if(a->hi!=b->hi)return a->hi<b->hi?-1:1;
  return a->cell<b->cell?-1:a->cell>b->cell;
}
static AxisRetainedCoordinate axis_coordinate(int anchor,long double offset) {
  /* Nearest integer normalization retains a tiny corner displacement rather
   * than adding it to a large cell origin. Large offsets can still have a
   * native arithmetic representation error, which is not a physical floor. */
  long double integral=roundl(offset);
  return (AxisRetainedCoordinate){anchor+(int)integral,offset-integral};
}
static long double axis_coordinate_difference(AxisRetainedCoordinate a,AxisRetainedCoordinate b) {
  return (long double)(a.anchor-b.anchor)+(a.offset-b.offset);
}
static AxisRetainedCoordinate axis_coordinate_min(AxisRetainedCoordinate a,AxisRetainedCoordinate b) {
  return axis_coordinate_difference(a,b)<=0.L?a:b;
}
static AxisRetainedCoordinate axis_coordinate_max(AxisRetainedCoordinate a,AxisRetainedCoordinate b) {
  return axis_coordinate_difference(a,b)>=0.L?a:b;
}
static int axis_leaf_water_interval(const AxisLeafEdge * edge,const ClosureAxisTransportLeaf * leaf,
    const ClosureAxisTransportNode * node,int span,AxisWaterInterval * water) {
  water->lo=(AxisRetainedCoordinate){edge->lo,0.L};water->hi=(AxisRetainedCoordinate){edge->hi,0.L};
  water->positive=0;if(node->m_water_kg==0.L)return 0;
  if(node->m_PFC_kg==0.L){water->positive=1;return 0;}
  const ClosureScaledPLIC * g=&leaf->geometry;
  if(g->status || !g->has_interface || !(g->offset>0.L) || (g->sign_z!=1 && g->sign_z!=-1) ||
     (g->sign_r!=1 && g->sign_r!=-1))return 1;
  int normal_sign=edge->dim?g->sign_r:g->sign_z;
  int tangent_sign=edge->dim?g->sign_z:g->sign_r;
  long double normal_coefficient=edge->dim?g->b:g->a;
  long double tangent_coefficient=edge->dim?g->a:g->b;
  /* side=-1 is the lower face, side=+1 the upper. The fixed local
   * preferred-corner coordinate is exactly 0 or 1. */
  int fixed=(edge->side==normal_sign);
  long double intercept=g->offset-normal_coefficient*fixed;
  int inside_small=g->small_material==1;
  if(tangent_coefficient==0.L) {
    int small_everywhere=intercept>=0.L;
    water->positive=inside_small?small_everywhere:!small_everywhere;return 0;
  }
  long double cut=intercept/tangent_coefficient;
  if(!isfinite(cut))return 2;
  if(cut<=0.L){water->positive=!inside_small;return 0;}
  if(cut>=1.L){water->positive=inside_small;return 0;}
  int preferred=tangent_sign>0?edge->lo:edge->hi;
  AxisRetainedCoordinate endpoint=axis_coordinate(preferred,tangent_sign*(long double)span*cut);
  /* The water occupies an interval toward the preferred corner if it is
   * the small material; otherwise it occupies the complementary interval. */
  if((tangent_sign>0)==inside_small)water->hi=endpoint;else water->lo=endpoint;
  water->positive=axis_coordinate_difference(water->hi,water->lo)>0.L;
  if(!water->positive)return 3; /* Positive local cut cannot vanish silently. */
  return 0;
}
static int axis_water_normal_distance(const AxisLeafEdge * edge,const ClosureAxisTransportLeaf * leaf,
    const ClosureAxisTransportNode * node,long double * distance) {
  if(!(node->m_water_kg>0.L))return 1;
  long double D=node->Delta_m;
  if(node->m_PFC_kg==0.L) {
    if(edge->dim==0){*distance=D/2.L;return 0;}
    long double displacement=D*D/(12.L*node->r_m);
    *distance=D/2.L-edge->side*displacement;
  } else {
    const ClosureScaledPLIC * g=&leaf->geometry;
    int normal_sign=edge->dim?g->sign_r:g->sign_z;
    long double coordinate=edge->dim?g->water_centroid_local_Y:g->water_centroid_local_X;
    *distance=D*(edge->side==normal_sign?1.L-coordinate:coordinate);
  }
  return !(*distance>0.L && isfinite(*distance));
}
static int axis_add_manifest_face(const AxisLeafEdge * node_lo,const AxisLeafEdge * node_hi,int lo,int hi,
    int count,const ClosureAxisTransportNode * node,const ClosureAxisTransportLeaf * leaf,
    int finest,long double unit,ClosureAxisTransportManifest * out,int * capacity) {
  const AxisLeafEdge * any=node_lo?node_lo:node_hi;
  if(!any || !(lo<hi))return 1;
  int k=out->faces;
  if(k==*capacity) {
    int next=*capacity?2*(*capacity):4*count;
    ClosureAxisTransportFace * newface=realloc(out->face,(size_t)next*sizeof(*newface));
    if(!newface)return 2;out->face=newface;
    ClosureAxisTransportFaceGeometry * newgeometry=realloc(out->geometry,(size_t)next*sizeof(*newgeometry));
    if(!newgeometry)return 2;out->geometry=newgeometry;*capacity=next;
  }
  ClosureAxisTransportFace * f=out->face+k;memset(f,0,sizeof(*f));
  ClosureAxisTransportFaceGeometry * g=out->geometry+k;memset(g,0,sizeof(*g));
  f->node_lo=node_lo?node_lo->cell:-1;f->node_hi=node_hi?node_hi->cell:-1;f->normal_axis=any->dim;
  int domain=1<<finest;long double plane=any->plane*unit,width=(hi-lo)*unit;
  long double lower=lo*unit,center=(lo+(long double)(hi-lo)/2.L)*unit;
  if(any->dim==0) {
    f->z_m=(double)plane;f->r_m=(double)(center+width*width/(12.L*center));
    f->area_m2=2.L*acosl(-1.L)*center*width;
  } else {
    f->z_m=(double)center;f->r_m=(double)plane;f->area_m2=2.L*acosl(-1.L)*plane*width;
  }
  f->normal_distance_m=(node_lo?(long double)node[node_lo->cell].Delta_m/2.L:0.L)+
    (node_hi?(long double)node[node_hi->cell].Delta_m/2.L:0.L);
  f->face_bc=node_lo && node_hi?CLOSURE_AXIS_TRANSPORT_INTERIOR:
    any->dim==0 && any->plane==0?CLOSURE_AXIS_TRANSPORT_NO_SLIP:
    any->dim==1 && any->plane==0?CLOSURE_AXIS_TRANSPORT_AXIS:CLOSURE_AXIS_TRANSPORT_FREE_SLIP;
  if(!(node_lo && node_hi) && any->plane!=0 && any->plane!=domain)return 3;
  g->normal_axis=any->dim;g->plane_index=any->plane;g->lower_index=lo;g->upper_index=hi;
  g->node_lo=f->node_lo;g->node_hi=f->node_hi;g->face_bc=f->face_bc;
  if(node_lo && node_hi) {
    AxisWaterInterval wl,wr;
    int sl=1<<(finest-leaf[node_lo->cell].level),sr=1<<(finest-leaf[node_hi->cell].level);
    if(axis_leaf_water_interval(node_lo,leaf+node_lo->cell,node+node_lo->cell,sl,&wl) ||
       axis_leaf_water_interval(node_hi,leaf+node_hi->cell,node+node_hi->cell,sr,&wr))return 4;
    if(wl.positive && wr.positive) {
      AxisRetainedCoordinate low=axis_coordinate_max(axis_coordinate_max(wl.lo,wr.lo),(AxisRetainedCoordinate){lo,0.L});
      AxisRetainedCoordinate high=axis_coordinate_min(axis_coordinate_min(wl.hi,wr.hi),(AxisRetainedCoordinate){hi,0.L});
      long double retained_width=axis_coordinate_difference(high,low);
      if(retained_width>0.L) {
        long double dl,dr;if(axis_water_normal_distance(node_lo,leaf+node_lo->cell,node+node_lo->cell,&dl) ||
          axis_water_normal_distance(node_hi,leaf+node_hi->cell,node+node_hi->cell,&dr))return 5;
        long double water_width=retained_width*unit;
        long double water_lower=low.anchor*unit+low.offset*unit;
        f->water_overlap_area_m2=any->dim==0?2.L*acosl(-1.L)*(water_lower+water_width/2.L)*water_width:
          2.L*acosl(-1.L)*plane*water_width;
        f->water_centroid_distance_m=dl+dr;
        if(!(water_width>0.L && f->water_overlap_area_m2>0.L && f->water_centroid_distance_m>0.L) ||
           !isfinite(f->water_overlap_area_m2+f->water_centroid_distance_m) || f->water_overlap_area_m2>f->area_m2)return 6;
        g->water_lower_anchor=low.anchor;g->water_upper_anchor=high.anchor;
        g->water_lower_offset=low.offset;g->water_upper_offset=high.offset;g->water_overlap_width_m=water_width;
        out->positive_water_overlaps++;
      }
    }
    out->interior_faces++;
  } else {
    out->boundary_faces++;
    if(any->dim==0)out->axial_boundary_area_m2+=f->area_m2;else out->radial_boundary_area_m2+=f->area_m2;
  }
  (void)lower;out->faces++;return 0;
}
int closure_axis_transport_manifest_build(int count,const ClosureAxisTransportNode * node,
    const ClosureAxisTransportLeaf * leaf,double length,int finest,ClosureAxisTransportManifest * out) {
  if(!out)return 1;memset(out,0,sizeof(*out));
  if(!node || !leaf || count<1 || !(length>0. && isfinite(length)) || finest<0 || finest>20)return 1;
  AxisLeafEdge * edges=malloc((size_t)4*count*sizeof(*edges));if(!edges)return 2;
  int domain=1<<finest,capacity=0,status=0;long double unit=(long double)length/domain;
  out->nodes=count;out->finest_level=finest;
  for(int i=0;i<count;i++) {
    int level=leaf[i].level;
    if(level<0 || level>finest || leaf[i].z_index<0 || leaf[i].r_index<0 ||
       leaf[i].z_index>=(1<<level) || leaf[i].r_index>=(1<<level) || leaf[i].geometry.status){status=3;goto end;}
    int s=1<<(finest-level),z=leaf[i].z_index*s,r=leaf[i].r_index*s;
    edges[4*i]=(AxisLeafEdge){0,z,r,r+s,i,-1};edges[4*i+1]=(AxisLeafEdge){0,z+s,r,r+s,i,1};
    edges[4*i+2]=(AxisLeafEdge){1,r,z,z+s,i,-1};edges[4*i+3]=(AxisLeafEdge){1,r+s,z,z+s,i,1};
  }
  qsort(edges,(size_t)4*count,sizeof(*edges),axis_edge_compare);
  for(int start=0;start<4*count;) {
    int finish=start+1;while(finish<4*count && edges[finish].dim==edges[start].dim && edges[finish].plane==edges[start].plane)finish++;
    int split=start;while(split<finish && edges[split].side==-1)split++;
    for(int k=start+1;k<split;k++)if(edges[k].lo<edges[k-1].hi){status=4;goto end;}
    for(int k=split+1;k<finish;k++)if(edges[k].lo<edges[k-1].hi){status=4;goto end;}
    int plane=edges[start].plane;
    if(plane==0 || plane==domain) {
      if((plane==0 && split!=finish) || (plane==domain && split!=start)){status=5;goto end;}
      int expected=0;
      for(int k=start;k<finish;k++) {
        if(edges[k].lo!=expected){status=6;goto end;}expected=edges[k].hi;
        int failure=axis_add_manifest_face(plane==domain?edges+k:NULL,plane==0?edges+k:NULL,
          edges[k].lo,edges[k].hi,count,node,leaf,finest,unit,out,&capacity);
        if(failure){status=10+failure;goto end;}
      }
      if(expected!=domain){status=6;goto end;}
    } else {
      int node_hi=start,node_lo=split;if(node_hi==split || node_lo==finish){status=7;goto end;}
      int right_used=edges[node_hi].lo,left_used=edges[node_lo].lo;
      while(node_hi<split && node_lo<finish) {
        if(right_used!=left_used){status=8;goto end;}
        int high=edges[node_hi].hi<edges[node_lo].hi?edges[node_hi].hi:edges[node_lo].hi;
        int failure=axis_add_manifest_face(edges+node_lo,edges+node_hi,right_used,high,count,node,leaf,finest,unit,out,&capacity);
        if(failure){status=10+failure;goto end;}
        right_used=left_used=high;
        if(high==edges[node_hi].hi){node_hi++;if(node_hi<split)right_used=edges[node_hi].lo;}
        if(high==edges[node_lo].hi){node_lo++;if(node_lo<finish)left_used=edges[node_lo].lo;}
      }
      if(node_hi!=split || node_lo!=finish){status=9;goto end;}
    }
    start=finish;
  }
end:
  free(edges);if(status)closure_axis_transport_manifest_free(out);return status;
}
void closure_axis_transport_manifest_free(ClosureAxisTransportManifest * out) {
  if(!out)return;free(out->face);free(out->geometry);memset(out,0,sizeof(*out));
}
