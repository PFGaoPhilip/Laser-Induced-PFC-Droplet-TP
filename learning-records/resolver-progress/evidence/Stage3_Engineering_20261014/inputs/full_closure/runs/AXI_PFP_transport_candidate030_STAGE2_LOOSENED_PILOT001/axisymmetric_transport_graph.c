#include "axisymmetric_transport_graph.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {long double zz,zr,rz,rr;} AxisGradient;
static int axis_node_valid(const ClosureAxisTransportNode * n) {
  long double mass=n->m_water_kg+n->m_PFC_kg;
  return n->Delta_m>0. && n->r_m>0. && n->volume_m3>0. &&
    n->a_water>=0.L && n->a_PFC>=0.L && fabsl(n->a_water+n->a_PFC-1.L)<=1e-12L &&
    n->m_water_kg>=0.L && n->m_PFC_kg>=0.L && mass>0.L &&
    isfinite(mass+n->q_z_kg_m_s+n->q_r_kg_m_s+n->E_water_J+n->E_PFC_J) &&
    isfinite(n->z_m+n->r_m+n->Delta_m+n->volume_m3) &&
    isfinite(n->T_water_K+n->T_PFC_K+n->cv_water_J_kg_K+n->mu_water_Pa_s+n->mu_PFC_Pa_s) &&
    (!(n->m_water_kg>0.L) || (n->a_water>0. && n->T_water_K>0. && n->cv_water_J_kg_K>0. && n->mu_water_Pa_s>=0.)) &&
    (!(n->m_PFC_kg>0.L) || (n->a_PFC>0. && n->T_PFC_K>0. && n->mu_PFC_Pa_s>=0.));
}
static int axis_face_valid(const ClosureAxisTransportFace * f,int nodes) {
  if(f->normal_axis<0 || f->normal_axis>1 || f->area_m2<0. || !isfinite(f->area_m2) ||
     !isfinite(f->z_m+f->r_m) || !(f->normal_distance_m>0.))return 0;
  int L=f->node_lo,R=f->node_hi;if(L>=nodes || R>=nodes || L==R || (L<0 && R<0))return 0;
  if(L>=0 && R>=0)return f->face_bc==CLOSURE_AXIS_TRANSPORT_INTERIOR;
  return f->face_bc>=CLOSURE_AXIS_TRANSPORT_NO_SLIP && f->face_bc<=CLOSURE_AXIS_TRANSPORT_FREE_SLIP;
}
static long double axis_u(const ClosureAxisTransportNode * n,int component) {
  return (component?n->q_r_kg_m_s:n->q_z_kg_m_s)/(n->m_water_kg+n->m_PFC_kg);
}
static void axis_ghost(const ClosureAxisTransportNode * n,const ClosureAxisTransportFace * f,
    long double * dz,long double * dr,long double * duz,long double * dur) {
  *dz=f->normal_axis==0?2.L*(f->z_m-n->z_m):0.L;
  *dr=f->normal_axis==1?2.L*(f->r_m-n->r_m):0.L;
  long double uz=axis_u(n,0),ur=axis_u(n,1);
  if(f->face_bc==CLOSURE_AXIS_TRANSPORT_NO_SLIP){*duz=-2.L*uz;*dur=-2.L*ur;}
  else if(f->normal_axis==0){*duz=-2.L*uz;*dur=0.L;}
  else {*duz=0.L;*dur=-2.L*ur;}
}
/* Weighted cell-gradient reconstruction from the ACTUAL face graph. Each
 * coarse/fine subface contributes its physical area, without ghost leaf IDs.
 * A linear no-swirl velocity satisfies all interior difference equations. */
static int axis_gradients(int count,const ClosureAxisTransportNode * n,int nf,
    const ClosureAxisTransportFace * faces,AxisGradient * gradients) {
  long double (*a)[7]=calloc((size_t)count,sizeof(*a));if(!a)return 1;
  for(int k=0;k<nf;k++) {
    const ClosureAxisTransportFace * f=faces+k;
    for(int side=0;side<2;side++) {
      int i=side?f->node_hi:f->node_lo,j=side?f->node_lo:f->node_hi;if(i<0)continue;
      long double dz,dr,duz,dur;
      if(j>=0) {dz=(long double)n[j].z_m-n[i].z_m;dr=(long double)n[j].r_m-n[i].r_m;
        duz=axis_u(n+j,0)-axis_u(n+i,0);dur=axis_u(n+j,1)-axis_u(n+i,1);}
      else axis_ghost(n+i,f,&dz,&dr,&duz,&dur);
      long double distance2=dz*dz+dr*dr;if(!(distance2>0.L)){free(a);return 2;}
      long double area=f->area_m2;
      /* The zero-area axis still supplies its smooth reflected stencil,
       * with its meridional width as reconstruction weight only. It adds no
       * physical flux, stress area, energy, heat or entropy face measure. */
      if(area==0.L && f->face_bc==CLOSURE_AXIS_TRANSPORT_AXIS)
        area=2.L*acosl(-1.L)*n[i].r_m*n[i].Delta_m;
      long double w=area/distance2;a[i][0]+=w*dz*dz;a[i][1]+=w*dz*dr;a[i][2]+=w*dr*dr;
      a[i][3]+=w*dz*duz;a[i][4]+=w*dr*duz;a[i][5]+=w*dz*dur;a[i][6]+=w*dr*dur;
    }
  }
  for(int i=0;i<count;i++) {
    long double det=a[i][0]*a[i][2]-a[i][1]*a[i][1];if(!(det>0.L)){free(a);return 3;}
    gradients[i]=(AxisGradient){(a[i][2]*a[i][3]-a[i][1]*a[i][4])/det,
      (a[i][0]*a[i][4]-a[i][1]*a[i][3])/det,
      (a[i][2]*a[i][5]-a[i][1]*a[i][6])/det,(a[i][0]*a[i][6]-a[i][1]*a[i][5])/det};
  }
  free(a);return 0;
}
static long double axis_mu(const ClosureAxisTransportNode * n) {
  return (long double)n->a_water*n->mu_water_Pa_s+(long double)n->a_PFC*n->mu_PFC_Pa_s;
}
static void axis_face_velocity(const ClosureAxisTransportNode * n,const AxisGradient * g,
    const ClosureAxisTransportFace * f,long double * uz,long double * ur) {
  if(f->node_lo<0 || f->node_hi<0) {
    int i=f->node_lo>=0?f->node_lo:f->node_hi;
    if(f->face_bc==CLOSURE_AXIS_TRANSPORT_NO_SLIP){*uz=*ur=0.L;return;}
    *uz=f->normal_axis==0?0.L:axis_u(n+i,0);*ur=f->normal_axis==1?0.L:axis_u(n+i,1);return;
  }
  *uz=*ur=0.L;
  for(int side=0;side<2;side++) {
    int i=side?f->node_hi:f->node_lo;long double dz=(long double)f->z_m-n[i].z_m,dr=(long double)f->r_m-n[i].r_m;
    *uz+=.5L*(axis_u(n+i,0)+g[i].zz*dz+g[i].zr*dr);
    *ur+=.5L*(axis_u(n+i,1)+g[i].rz*dz+g[i].rr*dr);
  }
}
static void axis_face_stress(const ClosureAxisTransportNode * n,const AxisGradient * g,
    const ClosureAxisTransportFace * f,long double * normal,long double * shear) {
  int L=f->node_lo,R=f->node_hi,i=L>=0?L:R;long double zz=g[i].zz,rr=g[i].rr,zr=g[i].zr,rz=g[i].rz;
  long double mu=axis_mu(n+i),uz,ur;axis_face_velocity(n,g,f,&uz,&ur);
  if(L>=0 && R>=0) {
    long double mL=axis_mu(n+L),mR=axis_mu(n+R);mu=mL>0.L && mR>0.L?2.L*mL*mR/(mL+mR):0.L;
    zz=.5L*(g[L].zz+g[R].zz);rr=.5L*(g[L].rr+g[R].rr);zr=.5L*(g[L].zr+g[R].zr);rz=.5L*(g[L].rz+g[R].rz);
    /* Normal derivatives include tangential centre offsets through the
     * least-squares reconstruction to the actual subface centre. */
    long double uL=axis_u(n+L,f->normal_axis),uR=axis_u(n+R,f->normal_axis);
    if(f->normal_axis==0) {
      uL+=g[L].zr*((long double)f->r_m-n[L].r_m);uR+=g[R].zr*((long double)f->r_m-n[R].r_m);
      zz=(uR-uL)/f->normal_distance_m;
    } else {
      uL+=g[L].rz*((long double)f->z_m-n[L].z_m);uR+=g[R].rz*((long double)f->z_m-n[R].z_m);
      rr=(uR-uL)/f->normal_distance_m;
    }
  } else {
    long double un=axis_u(n+i,f->normal_axis);long double direction=L>=0?1.L:-1.L;
    if(f->normal_axis==0)zz=-direction*un/f->normal_distance_m;
    else rr=-direction*un/f->normal_distance_m;
    if(f->face_bc!=CLOSURE_AXIS_TRANSPORT_NO_SLIP){zr=rz=0.L;}
  }
  long double hoop=f->r_m>0.?ur/f->r_m:rr,theta=zz+rr+hoop;
  *normal=2.L*mu*((f->normal_axis==0?zz:rr)-theta/3.L);*shear=mu*(zr+rz);
  if((L<0 || R<0) && f->face_bc!=CLOSURE_AXIS_TRANSPORT_NO_SLIP)*shear=0.L;
}
int closure_axis_transport_viscous(int count,const ClosureAxisTransportNode * input,int nf,
    const ClosureAxisTransportFace * face,double dt,ClosureAxisTransportNode * output,ClosureAxisTransportStats * stats) {
  if(!input || !face || !output || !stats || count<1 || nf<1 || !(dt>=0. && isfinite(dt)))return 1;
  memset(stats,0,sizeof(*stats));stats->minimum_viscous_intrinsic_increment_J=INFINITY;
  for(int i=0;i<count;i++)if(!axis_node_valid(input+i))return stats->status=2;
  for(int k=0;k<nf;k++)if(!axis_face_valid(face+k,count))return stats->status=3;
  ClosureAxisTransportNode * trial=malloc(count*sizeof(*trial)),*midpoint=malloc(count*sizeof(*midpoint));
  AxisGradient * oldg=malloc(count*sizeof(*oldg)),*midg=malloc(count*sizeof(*midg));
  long double (*force)[2]=calloc(count,sizeof(*force)),*dE=calloc(count,sizeof(*dE));
  long double (*stress)[2]=calloc(nf,sizeof(*stress)),*heat=calloc(count,sizeof(*heat));
  if(!trial || !midpoint || !oldg || !midg || !force || !dE || !stress || !heat){stats->status=4;goto end;}
  memcpy(trial,input,count*sizeof(*trial));memcpy(midpoint,input,count*sizeof(*midpoint));
  if(axis_gradients(count,input,nf,face,oldg)){stats->status=5;goto end;}
  for(int k=0;k<nf;k++) {
    axis_face_stress(input,oldg,face+k,&stress[k][0],&stress[k][1]);
    long double fz=(face[k].normal_axis?stress[k][1]:stress[k][0])*face[k].area_m2;
    long double fr=(face[k].normal_axis?stress[k][0]:stress[k][1])*face[k].area_m2;
    if(face[k].node_lo>=0){force[face[k].node_lo][0]+=fz;force[face[k].node_lo][1]+=fr;}
    if(face[k].node_hi>=0){force[face[k].node_hi][0]-=fz;force[face[k].node_hi][1]-=fr;}
  }
  for(int i=0;i<count;i++) {
    long double zz=oldg[i].zz,rr=oldg[i].rr,hoop=axis_u(input+i,1)/input[i].r_m;
    long double theta=zz+rr+hoop,shear=.5L*(oldg[i].zr+oldg[i].rz);
    long double norm=(zz-theta/3.L)*(zz-theta/3.L)+(rr-theta/3.L)*(rr-theta/3.L)+
      (hoop-theta/3.L)*(hoop-theta/3.L)+2.L*shear*shear;
    if(norm==0.L && (zz-theta/3.L!=0.L || rr-theta/3.L!=0.L || hoop-theta/3.L!=0.L || shear!=0.L)) {
      stats->status=8;goto end;
    }
    force[i][1]-=2.L*axis_mu(input+i)*(hoop-theta/3.L)*input[i].volume_m3/input[i].r_m;
    long double hW=2.L*input[i].a_water*input[i].mu_water_Pa_s*norm*input[i].volume_m3;
    long double hF=2.L*input[i].a_PFC*input[i].mu_PFC_Pa_s*norm*input[i].volume_m3;heat[i]=hW+hF;
    if(norm>0.L && ((input[i].m_water_kg>0.L && input[i].mu_water_Pa_s>0. && !(hW>0.L)) ||
       (input[i].m_PFC_kg>0.L && input[i].mu_PFC_Pa_s>0. && !(hF>0.L)))) {stats->status=8;goto end;}
    if(input[i].m_water_kg>0.L) {
      long double entropy=dt*hW/input[i].T_water_K;
      if(dt>0. && hW>0.L && !(entropy>0.L)){stats->status=8;goto end;}
      stats->viscous_entropy_J_K+=entropy;
    }
    if(input[i].m_PFC_kg>0.L) {
      long double entropy=dt*hF/input[i].T_PFC_K;
      if(dt>0. && hF>0.L && !(entropy>0.L)){stats->status=8;goto end;}
      stats->viscous_entropy_J_K+=entropy;
    }
    trial[i].q_z_kg_m_s+=dt*force[i][0];trial[i].q_r_kg_m_s+=dt*force[i][1];
    stats->paired_momentum_roundoff_kg_m_s+=fabsl((trial[i].q_z_kg_m_s-input[i].q_z_kg_m_s)-dt*force[i][0])+
      fabsl((trial[i].q_r_kg_m_s-input[i].q_r_kg_m_s)-dt*force[i][1]);
    midpoint[i].q_z_kg_m_s=.5L*(input[i].q_z_kg_m_s+trial[i].q_z_kg_m_s);
    midpoint[i].q_r_kg_m_s=.5L*(input[i].q_r_kg_m_s+trial[i].q_r_kg_m_s);
    stats->maximum_viscous_force_N=fmaxl(stats->maximum_viscous_force_N,hypotl(force[i][0],force[i][1]));
  }
  if(axis_gradients(count,midpoint,nf,face,midg)){stats->status=6;goto end;}
  for(int k=0;k<nf;k++) {
    long double uz,ur;axis_face_velocity(midpoint,midg,face+k,&uz,&ur);
    long double energy=dt*face[k].area_m2*(face[k].normal_axis?
      stress[k][1]*uz+stress[k][0]*ur:stress[k][0]*uz+stress[k][1]*ur);
    if(face[k].node_lo>=0)dE[face[k].node_lo]+=energy;else stats->viscous_energy_boundary_out_J+=energy;
    if(face[k].node_hi>=0)dE[face[k].node_hi]-=energy;else stats->viscous_energy_boundary_out_J-=energy;
  }
  for(int i=0;i<count;i++) {
    long double mass=input[i].m_water_kg+input[i].m_PFC_kg;
    long double dK=dt*(axis_u(midpoint+i,0)*force[i][0]+axis_u(midpoint+i,1)*force[i][1]),intrinsic=dE[i]-dK;
    stats->minimum_viscous_intrinsic_increment_J=fminl(stats->minimum_viscous_intrinsic_increment_J,intrinsic);
    stats->viscous_intrinsic_work_defect_J+=fabsl(intrinsic-dt*heat[i]);
    /* candidate018 Stage1 loosening (user-authorized): keep diagnostics on raw intrinsic;
       clamp negative viscous intrinsic to 0 before energy update; refuse only non-finite E/q. */
    if(intrinsic<0.L){
      static int clamped_once=0;
      if(!clamped_once){fprintf(stderr,"AXI transport candidate018: clamping negative viscous intrinsic (first cell)\n");clamped_once=1;}
      intrinsic=0.L;
    }
    long double mu=axis_mu(input+i),yw=input[i].m_water_kg/mass;
    long double bw=mu>0.L?(long double)input[i].a_water*input[i].mu_water_Pa_s/mu:yw;
    trial[i].E_water_J+=yw*dK+bw*intrinsic;trial[i].E_PFC_J+=(1.L-yw)*dK+(1.L-bw)*intrinsic;
    stats->paired_energy_roundoff_J+=(trial[i].E_water_J-input[i].E_water_J)+(trial[i].E_PFC_J-input[i].E_PFC_J)-dE[i];
    if(!isfinite(trial[i].E_water_J+trial[i].E_PFC_J+trial[i].q_z_kg_m_s+trial[i].q_r_kg_m_s)){stats->status=7;goto end;}
  }
  memcpy(output,trial,count*sizeof(*trial));stats->face_count=nf;
end:
  free(trial);free(midpoint);free(oldg);free(midg);free(force);free(dE);free(stress);free(heat);return stats->status;
}
int closure_axis_transport_water_Fourier(int count,const ClosureAxisTransportNode * input,int nf,
    const ClosureAxisTransportFace * faces,double dt,double Ttol,double Etol,int maximum,
    ClosureAxisTransportNode * output,ClosureAxisTransportStats * stats) {
  if(!input || !faces || !output || !stats || count<1 || nf<1 ||
     !(dt>=0. && isfinite(dt) && Ttol>0. && isfinite(Ttol) && Etol>0. && isfinite(Etol)) || maximum<1)return 1;
  memset(stats,0,sizeof(*stats));
  for(int i=0;i<count;i++)if(!axis_node_valid(input+i))return stats->status=2;
  for(int k=0;k<nf;k++)if(!axis_face_valid(faces+k,count))return stats->status=3;
  long double * C=calloc(count,sizeof(*C)),*T=calloc(count,sizeof(*T)),*sumG=calloc(count,sizeof(*sumG));
  long double * G=calloc(nf,sizeof(*G)),*energy=calloc(count,sizeof(*energy));
  ClosureAxisTransportNode * trial=malloc(count*sizeof(*trial));
  int * offset=calloc((size_t)count+1,sizeof(*offset)),*adjacency=malloc((size_t)2*nf*sizeof(*adjacency));
  int * cursor=calloc(count,sizeof(*cursor));
  if(!C || !T || !sumG || !G || !energy || !trial || !offset || !adjacency || !cursor){stats->status=4;goto end;}
  memcpy(trial,input,count*sizeof(*trial));
  for(int i=0;i<count;i++){C[i]=input[i].m_water_kg*input[i].cv_water_J_kg_K;T[i]=input[i].T_water_K;}
  for(int k=0;k<nf;k++) {
    const ClosureAxisTransportFace * f=faces+k;if(f->node_lo<0 || f->node_hi<0)continue; /* Declared adiabatic boundaries. */
    if(!(f->water_overlap_area_m2>=0. && f->water_overlap_area_m2<=f->area_m2) || !isfinite(f->water_overlap_area_m2)){stats->status=5;goto end;}
    if(f->water_overlap_area_m2==0.)continue;
    if(!(C[f->node_lo]>0.L && C[f->node_hi]>0.L && f->water_centroid_distance_m>0. && isfinite(f->water_centroid_distance_m))){stats->status=6;goto end;}
    G[k]=.598L*f->water_overlap_area_m2/f->water_centroid_distance_m;
    if(!(G[k]>0.L && isfinite(G[k])) || (dt>0. && !(dt*G[k]>0.L))) {stats->status=9;goto end;}
    sumG[f->node_lo]+=G[k];sumG[f->node_hi]+=G[k];offset[f->node_lo+1]++;offset[f->node_hi+1]++;
    stats->water_edge_count++;
  }
  for(int i=1;i<=count;i++)offset[i]+=offset[i-1];memcpy(cursor,offset,count*sizeof(*cursor));
  for(int k=0;k<nf;k++)if(G[k]>0.L){adjacency[cursor[faces[k].node_lo]++]=k;adjacency[cursor[faces[k].node_hi]++]=k;}
  for(int iteration=0;iteration<maximum;iteration++) {
    long double maximum_change=0.L;
    for(int i=0;i<count;i++) {
      if(C[i]==0.L)continue;long double numerator=C[i]*input[i].T_water_K,denominator=C[i]+dt*sumG[i];
      for(int edge=offset[i];edge<offset[i+1];edge++) {
        int k=adjacency[edge],j=faces[k].node_lo==i?faces[k].node_hi:faces[k].node_lo;
        numerator+=dt*G[k]*T[j];
      }
      long double next=numerator/denominator;if(!(next>0.L && isfinite(next))){stats->status=7;goto end;}
      maximum_change=fmaxl(maximum_change,fabsl(next-T[i]));T[i]=next;
    }
    stats->Fourier_iterations++;stats->maximum_temperature_iteration_change_K=(double)maximum_change;
    memset(energy,0,count*sizeof(*energy));
    for(int k=0;k<nf;k++)if(G[k]>0.L) {
      int L=faces[k].node_lo,R=faces[k].node_hi;long double exchange=dt*G[k]*(T[R]-T[L]);energy[L]+=exchange;energy[R]-=exchange;
    }
    long double error=0.L;
    for(int i=0;i<count;i++)if(C[i]>0.L) {
      long double scale=C[i]*input[i].T_water_K;
      if(!(scale>0.L && isfinite(scale))){stats->status=9;goto end;}
      error=fmaxl(error,fabsl(C[i]*(T[i]-input[i].T_water_K)-energy[i])/scale);
    }
    if(maximum_change<=Ttol && error<=Etol) {
      for(int i=0;i<count;i++) {
        trial[i].E_water_J+=energy[i];if(C[i]>0.L)trial[i].T_water_K=(double)T[i];
        stats->Fourier_linear_solve_energy_defect_J+=fabsl(C[i]*(T[i]-input[i].T_water_K)-energy[i]);
        stats->paired_energy_roundoff_J+=(trial[i].E_water_J-input[i].E_water_J)-energy[i];
        if(C[i]>0.L) {
          long double relative=(trial[i].E_water_J-input[i].E_water_J)/(C[i]*input[i].T_water_K);
          if(!(relative>-1.L && isfinite(relative))){stats->status=10;goto end;}
          stats->Fourier_endpoint_entropy_change_J_K+=C[i]*log1pl(relative);
        }
      }
      for(int k=0;k<nf;k++)if(G[k]>0.L) {
        int L=faces[k].node_lo,R=faces[k].node_hi;long double difference=T[R]-T[L];
        long double entropy=dt*G[k]*difference*difference/(T[L]*T[R]);
        if(dt>0. && difference!=0.L && !(entropy>0.L)){stats->status=9;goto end;}
        stats->Fourier_entropy_J_K+=entropy;
      }
      stats->Fourier_time_entropy_defect_J_K=stats->Fourier_endpoint_entropy_change_J_K-stats->Fourier_entropy_J_K;
      memcpy(output,trial,count*sizeof(*trial));stats->face_count=nf;goto end;
    }
  }
  stats->status=8;
end:
  free(C);free(T);free(sumG);free(G);free(energy);free(trial);free(offset);free(adjacency);free(cursor);return stats->status;
}
