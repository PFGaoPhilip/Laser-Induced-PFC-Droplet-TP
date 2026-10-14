"""English, scientifically audited native SCI-PPT scenes for Chapters 3 and 4."""
from pathlib import Path
import importlib.util
import json
import math
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/figures-editable/c3-c4'
BG, FG, ACC, MUT, AREA = '#142632', '#E7F0F3', '#8EDBD4', '#B4C7D2', '#213E4B'


class Diagram:
    def __init__(self, eq):
        self.eq, self.o = eq, []
        self.text(.3,.15,12.7,.4,eq['id']+' · '+eq['kind'],21,ACC)
    def add(self, typ, **kw):
        kw.update(type=typ, id=f"o{len(self.o):03}", name=f"{self.eq['id']} {typ} {len(self.o)}")
        self.o.append(kw)
    def text(self,x,y,w,h,s,size=17,color=FG):
        self.add('text',x=x,y=y,w=w,h=h,text=s,font='Arial',font_size=size,color=color,word_wrap=True)
    def line(self,x1,y1,x2,y2,arrow=False,color=ACC,width=2):
        self.add('arrow' if arrow else 'line',x1=x1,y1=y1,x2=x2,y2=y2,line=color,line_width=width)
    def rect(self,x,y,w,h,fill=AREA):
        self.add('rect',x=x,y=y,w=w,h=h,fill=fill,line=MUT,line_width=1.5)
    def circle(self,x,y,r,fill=AREA):
        self.add('ellipse',x=x-r,y=y-r,w=2*r,h=2*r,fill=fill,line=MUT,line_width=1.5)
    def curve(self,points,color=ACC):
        for a,b in zip(points,points[1:]): self.line(*a,*b,color=color)
    def finish(self,category,corrections):
        self.line(.3,4.35,13,4.35,color='#405967',width=1)
        labels=self.eq['diagram']['labels']
        for i,s in enumerate(labels):
            col=i%2;row=i//2
            self.text(.35+col*6.45,4.48+row*.255,6.25,.27,'• '+str(s),11.5,MUT)
        y=max(6.12,4.48+math.ceil(len(labels)/2)*.255+.15)
        for s in self.eq['diagram']['notes']:
            self.text(.35,y,12.5,.32,str(s),11.5,ACC);y+=.30
        self.text(.35,7.08,12.5,.28,'Model schematic; geometry is not to scale.',10,MUT)
        return {'slide':{'width':13.333,'height':7.5},'background':BG,'objects':self.o,
                '_audit':{'id':self.eq['id'],'category':category,'corrections':corrections,
                          'scientific_status':'accepted against local equation, definitions and notes',
                          'evidence':['content/chapter03.py' if self.eq['id'].startswith('C3') else 'content/chapter04.py']}}


def bubbles(d,mode):
    if mode=='polygon':
        for cx,n in [(2,3),(6.6,4),(11,5)]:
            pts=[(cx+1.1*math.cos(-math.pi/2+2*math.pi*k/n),2.45+1.1*math.sin(-math.pi/2+2*math.pi*k/n)) for k in range(n)]
            for a,b in zip(pts,pts[1:]+pts[:1]):d.line(*a,*b,color=MUT)
            for x,y in pts:d.circle(x,y,.18)
            d.text(cx-.7,3.75,2,.3,f'N = {n}',17)
        d.text(.5,.8,12,.4,'Regular polygons: pitch s joins adjacent bubble centres; diagonals have different lengths.',16)
    elif mode=='activation':
        for j in range(3):
            for i in range(5):d.circle(1.3+i*.68,1.5+j*.7,.20,AREA if (i+j)%4 else None)
        d.text(5.5,1.25,6.7,.6,'Fabricated sites N_d → activated sites N_b',20)
        d.text(5.5,2.1,6.7,1,'Independent Bernoulli events with probability p_a\nOutline circles indicate inactive sites.',17)
        d.text(5.5,3.25,6.7,.5,'Count reproducibility and complete activation differ.',17,ACC)
    elif mode=='retarded':
        for x,y in [(1.4,1.5),(2.5,2.8),(3.6,1.5)]:
            d.circle(x,y,.32);d.line(x+.35,y,9.3,2.2,True)
        d.circle(9.5,2.2,.12,ACC)
        d.text(8.8,2.6,3,.4,'Observation x, time t',17)
        d.text(4.8,1,5,.4,'Retarded source time: t − r_i/c',19)
        d.text(.8,3.7,11.8,.4,'Volume fraction requires a defined region; travel times govern pulse overlap.',17)
    else:
        d.circle(2.4,2.25,.85);d.circle(9.5,2.25,.85)
        d.text(1.8,2.05,1.6,.4,'j: source',17);d.text(8.9,2.05,1.7,.4,'i: receiver',17)
        d.line(2.4,3.4,9.5,3.4);d.text(5.3,3.5,2,.4,'d_ij',17)
        d.line(3.4,2.25,8.45,2.25,True)
        d.text(4.1,1.75,4.3,.4,'Shared liquid: ρ, p∞',18)
        d.text(.6,.85,12,.45,'Fixed centres; spherical cavities; R_i, R_j ≪ d_ij',18)
        if mode=='collapse':
            d.line(1.15,2.25,1.53,2.25,True);d.line(3.65,2.25,3.27,2.25,True)
            d.text(4.05,2.65,4.5,.5,'Collapse branch: Ṙ < 0',18,ACC)
            d.text(.8,3.95,11.8,.3,'Interaction increases effective liquid inertia; it adds no source energy.',16)
        else:d.text(4,2.65,4.6,.6,'Source-volume acceleration\nsets the pressure correction.',17,ACC)


def finite_jet(d,mode):
    d.rect(.8,1.65,5.4,.8);d.line(1.1,2.05,5.8,2.05,True)
    d.text(1.6,1.15,4.3,.4,'Finite emitted liquid: m_j, E_j, U_j',18)
    d.line(.8,2.85,6.2,2.85);d.text(3,2.95,2,.4,'L_j',17)
    d.line(.5,1.65,.5,2.45);d.text(.15,2.6,1.8,.35,'d_j = 2a_j',14)
    if mode=='impact':
        d.rect(9.2,1.05,.4,1.8);d.line(6.3,2.05,9.15,2.05,True)
        d.text(9.85,1.1,3,.6,'Receiver\nZ_r, v_i',18)
        d.text(6.6,3.15,5.9,.8,'Early pressure: acoustic matching\nImpulse: finite momentum change',17,ACC)
    elif mode=='steady':
        d.rect(9.2,1.05,.4,2.55);d.line(6.3,2.05,9.15,2.05,True)
        d.line(8.85,2.05,8.85,.95,True);d.line(8.85,2.05,8.85,3.45,True)
        d.text(9.85,1.4,2.8,1,'Redirected flow\nzero axial\noutlet momentum',16)
        d.text(1,3.65,11,.45,'F_steady = ρ A_j U_j²; q_j = ρ U_j²/2 is a pressure scale.',18,ACC)
    elif mode=='wave':
        d.line(6.2,2.05,9.2,2.05,True);d.rect(9.2,1.05,.15,1.8)
        d.line(8.8,1.35,6.8,1.35,True);d.line(9.6,1.35,11.8,1.35,True)
        d.text(5.9,.8,3.25,.45,'Liquid deceleration wave ←',14)
        d.text(9.6,.8,3.2,.45,'Receiver wave →',16)
        d.text(6.7,3.1,5.9,.9,'Common contact velocity v_i\nCommon compressive pressure p_early',17,ACC)
    elif mode=='observer':
        d.rect(9.15,1,.35,1.9);d.rect(9.1,1.75,.45,.7,ACC)
        d.line(6.3,2.05,9.1,2.05,True)
        d.text(9.8,1.7,2.9,.8,'Fixed footprint A_o\nFixed window τ_o',17)
        d.text(6.8,3.25,5.8,.5,'p_obs: area and time average',17,ACC)
    elif mode=='growth':
        d.line(6.3,2.05,11.5,2.05,True);d.rect(11.6,1.15,.2,2.4)
        d.text(8,2.5,2,.4,'Gap H',17)
        pts=[(6.5+i*.065,1.65-.10*(1+i/30)*math.cos(i*.27)) for i in range(70)]
        d.curve(pts);d.text(6.4,.9,5.8,.4,'δ₀ → δ_arr during H/U_j',18)
        d.text(1.2,3.7,11,.4,'Linear growth applies while disturbances remain small relative to radius.',16,ACC)
    else:
        d.line(6.7,2.05,11.8,2.05,True);d.text(7,1.3,5,.8,'Finite mass defines speed\nand useful momentum.',20)
        d.text(7,2.6,5,.8,'P_j² ≤ 2 m_j E_j\nE_j ≤ E_avail',20,ACC)


def blister(d):
    d.line(.8,3.15,8.1,3.15,color=MUT)
    pts=[(1.1+6.7*i/80,3.15-1.7*(1-((i-40)/40)**2)**2) for i in range(81)]
    d.curve(pts);d.rect(.85,2.9,.3,.5);d.rect(7.75,2.9,.3,.5)
    d.line(4.45,3.1,4.45,1.5,True);d.text(4.6,2.1,2.8,.45,'w(r) ↑',18)
    for x in [2.5,4.45,6.4]:d.line(x,3.9,x,3.25,True)
    d.text(3.1,3.95,4,.3,'p₀: maintained pressure',16)
    d.line(4.45,3.5,7.8,3.5);d.text(6,3.55,1,.3,'b',16)
    d.circle(10.55,2.25,1.05,None);d.line(10.55,2.25,11.6,2.25,True)
    d.text(10.8,1.8,1,.3,'b',17);d.text(9.3,3.6,3,.4,'A_c = π b²',18)
    d.text(.75,.8,12,.4,'Clamped circular blister: w(b) = 0; w′(b) = 0; regular centre.',18,ACC)


def plate(d,mode):
    if mode=='pvc':
        d.rect(1.2,1.45,8.9,.25);d.rect(1.2,2.45,8.9,.35)
        d.text(1.3,1,9,.35,'Payload film: w, m_A, D_f, T₀',18)
        d.text(1.3,4.0,9,.3,'Intact PVC: w_P, m_A,P, D_P, T_P',16)
        for x in [3,5.5,8]:d.line(x,3.9,x,2.85,True);d.line(x,2.4,x,1.75,True)
        d.text(10.4,2.05,2.5,.8,'t_P→f\ntransmitted load',16)
        d.text(10.4,3.4,2.5,.6,'Liquid load ↑',16)
        d.text(.3,1.85,2.5,.6,'Contact or bond',14,ACC)
    elif mode=='thickness':
        d.rect(1.3,1.5,8.2,1.25);d.line(1.1,2.125,9.8,2.125,color=ACC)
        d.line(10.1,2.125,10.1,.95,True);d.text(10.35,1,1,.4,'+z',18)
        d.line(.9,1.5,.9,2.75);d.text(.3,2.9,2,.4,'h_f',18)
        d.text(3,2.15,5,.4,'z = 0: neutral midplane',18)
        d.text(1.3,3.4,11,.5,'m_A = ρ_f h_f; bending weights each layer by z².',19,ACC)
    else:
        d.line(1,2.7,10,2.7,color=MUT)
        d.curve([(1.2+i*.105,2.7-.85*math.sin(math.pi*i/80)**2) for i in range(81)])
        d.rect(.95,2.4,.3,.6);d.rect(9.55,2.4,.3,.6)
        for x in [3,5.4,7.8]:d.line(x,3.75,x,2.85,True)
        d.line(5.4,1,5.4,1.65,True)
        d.text(6,1.05,6,.45,'t_coh ↓: opening resistance',18)
        d.text(2.4,3.8,7,.35,'p_load ↑: applied positive departure load',17)
        d.text(1,.8,4,.4,'Film: w ↑; fixed clamps',18)
        d.text(10.2,2.1,2.7,.9,'Inertia\nBending\nPretension',17,ACC)


def cohesive(d):
    d.line(1.1,3.55,11.9,3.55,True);d.line(1.2,3.6,1.2,.9,True)
    d.curve([(1.2,3.55),(4,1.25),(10.8,3.55)])
    d.line(4,1.25,4,3.55,color=MUT)
    d.text(.35,.7,3,.4,'t_n: tensile resistance',17)
    d.text(4.15,1.0,3,.4,'T_max',18);d.text(3.65,3.75,2,.3,'δ₀',18)
    d.text(10.55,3.75,1.4,.3,'δ_c',18);d.text(11.8,3.75,1,.3,'δ',18)
    d.text(5.2,2.6,5,.45,'Full area = Γ',20,ACC)
    d.text(6.5,.8,5,.4,'Monotonic tensile opening branch',17)


def boxes(d,mode,labels):
    for i,s in enumerate(labels):
        x=.65+i*4.25;d.rect(x,1.55,3.5,1.45);d.text(x+.18,1.78,3.14,1,s,18)
        if i<2:d.line(x+3.5,2.25,x+4.2,2.25,True)
    d.text(.8,3.55,11.8,.5,mode,18,ACC)


def scene(eq):
    d=Diagram(eq);eid=eq['id'];n=int(eid.split('E')[1]);changes=[]
    if eid.startswith('C3'):
        if n==1:cat='activation';bubbles(d,cat)
        elif n==2:
            cat='beam uniformity';d.circle(3.4,2.4,1.4,None);d.circle(3.4,2.4,.65,None)
            d.line(3.4,2.4,4.8,2.4,True);d.text(4.25,1.9,2,.4,'w',18)
            d.line(3.4,2.4,3.4,1.75,True);d.text(2.35,1.65,2,.4,'R_A',17)
            d.text(6,1.3,6.4,1,'Beam axis and array centre coincide.\nInner circle encloses array sites.',19)
            d.text(6,2.65,6.3,.9,'F(R_A)/F₀ ≥ 1 − ε\nUniformity is an optical condition.',19,ACC)
            changes=['Replaced absorber/PFC heating picture with concentric beam and array radii.']
        elif n in [3,4,5,6,7,8,9,12,31]:
            cat='polygon' if n==6 else 'retarded' if n==12 else 'collapse' if n in [7,8,9] else 'coupling'
            bubbles(d,cat);changes=['Replaced generic nine-site array with equation-specific source/receiver, polygon, or retarded geometry.']
        elif n==10:
            cat='collapse time';d.line(1.2,3.6,11.8,3.6,True);d.line(1.2,3.6,1.2,.9,True)
            d.curve([(1.2+9.9*i/80,1.2+2.4*(i/80)**3) for i in range(81)])
            d.text(.4,.65,3,.4,'R/R_max',18);d.text(10.7,3.8,2,.3,'t/t_c',18)
            d.text(3.0,2.25,7.5,.7,'Initial radius R_max; initial speed zero.\nFormal endpoint R → 0.',18)
        elif n in [11,27,29]:
            cat='energy allocation'
            labels= ['Pressure-work reservoir','K_N: self + pair kinetic energy','K_N + remaining work: conserved'] if n==11 else ['Source allocation','Outgoing wave E_w','Finite A_o, τ_o observer'] if n==27 else ['E_L = 25 μJ','E_abs,total = 10 μJ','E_j,total = 50 nJ']
            boxes(d,'Each energy allocation belongs to the same finite source budget.',labels)
            changes=['Removed generic bubble/source diagram; displayed the stated budget and allocation.']
        elif n in [13,14,15]:
            cat='moving boundaries';d.rect(.9,1.15,10.8,2.6,None);d.circle(3.1,2.45,.7)
            d.text(2.65,2.25,1.5,.4,'p_g',17);d.text(5.1,2.05,4.7,.6,'Liquid Ω(t): u = ∇φ',19)
            d.line(4.4,2.45,3.85,2.45,True);d.text(4,2.85,5,.4,'n: liquid → cavity gas',16)
            d.line(9.6,2.2,10.5,2.2,True);d.text(8.6,1.3,3,.4,'Outlet / meniscus',17)
            d.text(1.1,.65,11,.4,'Walls, cavity and outlet are distinct boundaries.',18,ACC)
            if n==15:d.text(1.3,3.9,11,.3,'Cavity κ = −2/R; exterior cylindrical jet κ = +1/a_j.',17,ACC)
            changes=['Separated cavity, solid walls and outlet; fixed liquid-to-gas normal and signed curvatures.']
        elif n==16:
            cat='pressure impulse';d.rect(1.1,1.55,10,1.1);d.line(1.4,2.1,10.8,2.1,True)
            d.text(1.1,1,4,.4,'z = 0: Π = Π₀',19);d.text(8.3,1,4,.4,'z = L: Π = 0',19)
            d.text(2.6,3,9,.6,'Δu = −∇Π/ρ; Π decreases in the launch direction.',18,ACC)
        elif n==17:
            cat='focusing';d.curve([(1,1.25),(4,1.25),(7,1.85),(11.7,1.85)]);d.curve([(1,3.25),(4,3.25),(7,2.65),(11.7,2.65)])
            d.line(1.3,2.25,11.5,2.25,True);d.text(1, .7,4,.4,'Solid inlet: a_in, U_in, p_in',18)
            d.text(7.3,.95,5,.6,'Free jet: a_j, U_j\np_j = p_g + σ_j/a_j',18)
            d.text(1.2,3.7,11,.4,'Continuity fixes flux; the pressure budget must support acceleration.',17,ACC)
            changes=['Replaced constant-width finite jet with solid-inlet to free-outlet focusing geometry.']
        elif n in [19,20]:
            cat='slender conservation';d.rect(2.1,1.6,7.2,1.1,None)
            d.line(.8,2.15,3.5,2.15,True);d.line(7.8,2.15,11.9,2.15,True)
            d.text(.6,2.85,4,.5,'Incoming flux A v |z',18)
            d.text(8.1,2.85,4.5,.5,'Outgoing flux A v |z+Δz',18)
            d.text(4.2,1.8,4,.6,'Fixed axial slice Δz\nA(z,t) = πa²',18)
            d.text(.8,.85,12,.4,'Slender liquid: axial velocity v(z,t); radius a(z,t)',19,ACC)
            if n==20:
                d.text(1,3.65,11.6,.4,'Axial extension: τ_zz − τ_rr = 3μ ∂zv; capillary force follows ∂zκ.',17)
            else:d.text(1,3.65,11.6,.4,'Storage changes by incoming minus outgoing volume flux.',18)
            changes=['Added fixed finite-volume slice with distinct face fluxes.']
        elif n==28:
            cat='compressible control volume';d.rect(3.7,1.15,5.8,2.4,None)
            d.line(.7,2.35,3.6,2.35,True);d.line(9.6,2.35,12.4,2.35,True)
            d.text(4.1,1.6,5,.9,'Conserved state\nρ, ρu, ρe_t',23)
            d.text(.8,2.9,3,.65,'Mass, momentum\nand energy in',16)
            d.text(9.7,2.9,3,.65,'Mass, momentum\nand energy out',16)
            d.line(6.4,.75,6.4,1.1,True);d.text(7,.7,5,.4,'Q_abs: source counted once',17)
            d.text(3.7,3.8,8,.35,'Closure: p = P(ρ,e,{Y_k}); stress and heat flux required.',16,ACC)
            changes=['Replaced impact cartoon with conservative compressible control volume and closure.']
        else:
            cat='steady' if n==23 else 'wave' if n==24 else 'observer' if n==26 else 'growth' if n in [21,22,32] else 'impact' if n in [25,28,30,33] else 'finite'
            finite_jet(d,cat)
            if n in [19,20]:d.text(1.6,.75,10,.3,'Slender liquid section: radius a(z,t), axial velocity v(z,t)',17,ACC)
            changes=['Separated finite jet geometry, acoustic matching, steady redirection, growth, and observer definitions.']
    else:
        if n in [13,14,15,16,17,18,20,21,23,24,37]:cat='clamped blister';blister(d)
        elif n in [25,26,27,38]:cat='cohesive law';cohesive(d)
        elif n==3:cat='plate thickness';plate(d,'thickness');changes=['Added thickness coordinate and neutral midplane.']
        elif n==7:cat='PVC load path';plate(d,'pvc');changes=['Separated liquid/PVC load, PVC-to-film transmission and payload response.']
        elif n in [4,5,40]:
            cat='plate variation';d.rect(1.3,1.3,7.5,2.35,None)
            d.text(3,2,5.5,.6,'Reference film plane Ω_f\nw(x,y,t), variation δw',20)
            d.line(8.85,2.45,10.1,2.45,True);d.text(10.3,2.2,2.5,.6,'n: outward\nin-plane normal',16)
            d.line(1.5,3.85,3.5,3.85,True);d.text(3.7,3.7,1,.3,'x',17)
            d.line(1.5,3.85,1.5,2.9,True);d.text(.8,3.1,1,.3,'y',17)
            d.text(2.0,.8,10.5,.35,'Fixed boundary: δw = 0; ∂ₙδw = 0',19,ACC)
            d.text(5.3,3.85,7,.3,'Curvature stores U_b; slope stores U_T.',17,ACC)
            changes=['Replaced forced blister with reference-plane variational domain and in-plane boundary normal.']
        elif n in [1,2,35]:
            cat='surface traction';d.rect(1.1,1.4,10,.4)
            for x in [3,6,9]:d.line(x,3.1,x,1.9,True)
            d.line(10.5,1.85,10.5,2.8,True);d.text(10.75,2.2,2,.6,'n_f ↓\nsolid → liquid',16)
            d.text(1.1,.8,10,.4,'Film / solid; positive departure and velocity v_f ↑',18)
            d.text(1.3,3.4,10,.5,'Liquid below: t_l = T_l n_f; pressure traction opposes n_f.',18,ACC)
            changes=['Removed spurious second solid; fixed solid-to-liquid normal and compressive traction direction.']
        elif n==34 or n==39:
            cat='placement';d.rect(1.2,1,2,.25);d.rect(1,3.7,11.3,.3)
            d.line(2.2,1.35,2.2,3.65,color=MUT);d.line(2.2,1.35,5,3.65,True)
            d.line(2.2,3.3,5,3.3);d.text(3.15,2.95,2,.3,'Δx',18)
            d.text(.45,2.2,1.6,.4,'H_f',18);d.text(2.5,1.7,2,.3,'θ',18)
            d.text(6.4,1.6,5.5,1,'Normal gap H_f\nLateral error Δx = H_f tan θ',20)
            changes=['Added actual departure trajectory, receiver plane and angular placement geometry.']
        elif n==28:cat='finite input';finite_jet(d,'finite')
        elif n in [12,19,22,29,30,31,32,33,36,41]:
            cat='energy and momentum'
            labels=['Applied solid power','Kinetic + elastic storage','Interface power + losses'] if n in [12,41] else ['Plate storage U_b','Source potential −p₀V_bl','System potential P'] if n==19 else ['Fixed pressure: G ∝ b⁴','Fixed volume: G ∝ b⁻⁸','Different crack evolution'] if n==22 else ['Incoming finite budgets','Transmitted E_solid, I_net','Release + departure cost']
            boxes(d,'Work, storage, fracture consumption and net impulse retain separate meanings.',labels)
            changes=['Replaced generic sequential energy reservoir arrows with equation-specific budget.']
        elif n==10:
            cat='response times';boxes(d,'Compare actual pulse duration with each applicable response time.', ['Bending: t_b,scale','Pretension: t_T,scale','Cohesion: t_n,scale'])
        else:cat='transient film';plate(d,'film')
    return d.finish(cat,changes)


def main():
    import coursekit
    from sci_ppt_common import scene_to_svg, render_scene, make_deck
    for n in [3,4]:
        spec=importlib.util.spec_from_file_location(f'chapter{n}',ROOT/f'content/chapter{n:02}.py')
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    OUT.mkdir(parents=True,exist_ok=True)
    scenes=[]
    for eq in coursekit.EQUATIONS:
        if not eq['id'].startswith(('C3-','C4-')):continue
        sc=scene(eq);scenes.append(sc)
        (OUT/(eq['id'].lower()+'.scene.json')).write_text(json.dumps(sc,ensure_ascii=False,indent=2),encoding='utf-8')
        scene_to_svg(sc,OUT/(eq['id'].lower()+'.svg'))
        render_scene(sc,OUT/(eq['id'].lower()+'.pptx'))
    for n in [3,4]:
        subset=sorted([s for s in scenes if s['_audit']['id'].startswith(f'C{n}-')],key=lambda s:s['_audit']['id'])
        make_deck(subset,OUT/f'c{n}-figures.pptx')
        (OUT/f'c{n}-manifest.json').write_text(json.dumps([s['_audit']['id'] for s in subset],indent=2),encoding='utf-8')
    (OUT/'scientific-audit.json').write_text(json.dumps([s['_audit'] for s in scenes],ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Created {len(scenes)} English native scenes in {OUT}')


if __name__=='__main__':main()
