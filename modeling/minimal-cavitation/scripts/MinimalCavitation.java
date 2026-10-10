import com.comsol.model.*;
import com.comsol.model.util.*;
import java.util.Arrays;

/** Two finite-energy, single-event 0D models. No spatial wave/acoustic physics.
 * Run-Rebuild.ps1 substitutes the extracted project root before compiling.
 */
public class MinimalCavitation {
  static final String ROOT="__ROOT__/";
  static final double RG=15e-6, PAMB=1e5, KAPPA=1.4;

  static double available(double p) {
    double v=4*Math.PI*RG*RG*RG/3;
    double ve=v*Math.pow(p/PAMB,1/KAPPA);
    return p*v/(KAPPA-1)*(1-Math.pow(v/ve,KAPPA-1))-PAMB*(ve-v);
  }
  static double pressureFor(double energy) {
    double lo=PAMB, hi=1e9;
    for(int j=0;j<100;j++) {
      double mid=(lo+hi)/2;
      if(available(mid)>energy) hi=mid; else lo=mid;
    }
    return (lo+hi)/2;
  }
  static void param(Model m,String n,String value,String desc) {m.param().set(n,value,desc);}
  static void variable(Model m,String n,String value,String desc) {m.component("c").variable("v").set(n,value,desc);}

  static Model build(boolean gel) throws Exception {
    String tag=gel?"minimal_gel_jet":"minimal_cavity_jet";
    Model m=ModelUtil.create(tag);
    m.label(gel?"Model B: hydrogel confinement and liquid-channel transmission":"Model A: finite-energy pressure and liquid-plug speed");
    m.modelPath(ROOT+"models");
    m.save(ROOT+"build/"+(gel?"B":"A")+"_identity.mph");
    param(m,"tauLaser","10[ns]","One optical pulse, replaced by a post-activation initial state; pulse onset is not solved");
    param(m,"Rg0","15[um]","Post-activation source radius; not a liquid PFC-droplet radius");
    param(m,"Rc0","30[um]","Initially stress-free spherical chamber radius");
    param(m,"a","5[um]","Radius of the pre-existing liquid outlet");
    param(m,"L","50[um]","Effective liquid-column inertance length");
    param(m,"Lbudget","(Vc0-Vg0)/A","Connected chamber liquid inventory divided by outlet area; separate from inertance length");
    param(m,"rho","1000[kg/m^3]","Stipulated water-like carrier density");
    param(m,"rhoG","1000[kg/m^3]","Stipulated undrained gel density");
    param(m,"pInf","100[kPa]","Absolute ambient pressure");
    param(m,"kap","1.4","Adiabatic ideal-gas control exponent; not a validated PFC-vapor EOS");
    param(m,"p0",Double.toString(pressureFor(2e-9))+"[Pa]","Post-activation absolute source pressure, set from available work by the builder");
    param(m,"sigma","0.072[N/m]","Stipulated water-like surface tension");
    param(m,"G","20[kPa]","Intact incompressible neo-Hookean shear modulus");
    param(m,"etaG","0.010[Pa*s]","Kelvin-Voigt effective network viscosity");
    param(m,"Kloss","0","Conditional outlet minor-loss coefficient, dimensionless");
    param(m,"Rloss","0[Pa*s/m]","Measured/fitted pressure-to-speed resistance; not an instantaneous Poiseuille approximation");
    param(m,"outletOpen","1","1 for a pre-existing open liquid channel; 0 for sealed control");
    param(m,"cL","1500[m/s]","Reference communication speed used only for a validity diagnostic");
    param(m,"Us","10[m/s]","Velocity scale for dimensionless state variables");
    param(m,"tau","Rc0/Us","Numerical nondimensionalization time scale");
    param(m,"A","pi*a^2","Liquid-plug cross-section");
    param(m,"Vg0","4*pi*Rg0^3/3","Initial finite gas source volume");
    param(m,"Vc0","4*pi*Rc0^3/3","Initial chamber volume");
    param(m,"Veq","Vg0*(p0/pInf)^(1/kap)","Gas volume at ambient pressure");
    param(m,"E0","p0*Vg0/(kap-1)*(1-(Vg0/Veq)^(kap-1))-pInf*(Veq-Vg0)","Available reversible source work above ambient");
    param(m,"mJet","rho*A*L","Effective liquid-column inertia mass, not emitted mass");
    param(m,"Iscale","mJet*Us","Scaling momentum for the emitted-impulse accumulator");
    param(m,"Uceiling","sqrt(2*E0/mJet)","Energy-only peak outlet-speed bound from column inertia; not an achieved velocity");
    param(m,"qCeiling","E0/(A*L)","Energy-only liquid dynamic-pressure upper bound");
    param(m,"pCap","2*sigma/a","Pinned hemispherical-meniscus resistance");
    param(m,"tObs","1[us]","Declared averaging interval for an impulse-only arrest-pressure bound");
    param(m,"AObs","A","Declared pressure observer area");
    m.component().create("c",true);
    m.component("c").label(gel?"Finite cavity + spherical gel + explicit open/closed outlet":"Finite cavity + explicit liquid plug");
    m.component("c").variable().create("v");
    variable(m,"x","Lbudget*qq","Discharged liquid volume divided by outlet area, m");
    variable(m,"U","Us*vv","Outward liquid-plug speed, m/s");
    variable(m,"R",gel?"Rc0*rr":"Rc0","Chamber wall radius, m");
    variable(m,"Uw",gel?"Us*ww":"0[m/s]","Chamber wall expansion speed, m/s");
    variable(m,"Vg","Vg0+A*x+4*pi*(R^3-Rc0^3)/3","Finite gas volume including expelled liquid and chamber expansion");
    variable(m,"Vdot","A*U+4*pi*R^2*Uw","Total source volume rate");
    variable(m,"pb","p0*(Vg0/Vg)^kap","Uniform absolute pressure of finite ideal-gas control source");
    variable(m,"pEl",gel?"G/2*(5-4*Rc0/R-(Rc0/R)^4)":"0[Pa]","Elastic resistance pressure at spherical gel wall");
    variable(m,"pRes",gel?"pEl+4*etaG*Uw/R":"0[Pa]","Elastic plus viscous gel wall resistance");
    variable(m,"Wgel",gel?"2*pi*G*(5*R^3/3-2*Rc0*R^2+Rc0^4/R-2*Rc0^3/3)":"0[J]","Recoverable elastic gel work");
    variable(m,"Kgel",gel?"2*pi*rhoG*R^3*Uw^2":"0[J]","Spherical gel radial kinetic energy");
    variable(m,"Kjet","mJet*U^2/2","Stored kinetic energy of effective liquid-column inertia; not emitted energy");
    variable(m,"Esurf","pCap*A*x","Reversible meniscus work during outward motion");
    variable(m,"ploss","Rloss*U+rho*Kloss*U*abs(U)/2","Declared dissipative port pressure drop");
    variable(m,"acc","outletOpen*(pb-pInf-pCap-ploss-rho*U^2/2)/(rho*L)","Outlet acceleration from unsteady Bernoulli with discharged kinetic head");
    variable(m,"wallAcc",gel?"((pb-pInf-pRes)/rhoG-1.5*Uw^2)/R":"0[m/s^2]","Spherical gel wall acceleration");
    variable(m,"Pdis","outletOpen*A*(Rloss*U^2+rho*Kloss*abs(U)^3/2)"+(gel?"+16*pi*etaG*R*Uw^2":""),"Nonnegative irreversible port and gel loss power");
    variable(m,"Edis","E0*dd","Accumulated irreversible loss");
    variable(m,"Eout","E0*ee","Kinetic energy actually discharged at the outlet");
    variable(m,"Iout","Iscale*ii","Axial momentum actually discharged at the outlet");
    variable(m,"Mout","rho*A*x","Finite emitted liquid mass");
    variable(m,"Pout","outletOpen*rho*A*U^3/2","Discharged kinetic power on the outward branch");
    variable(m,"energyResidual","(pb*Vg/(kap-1)-p0*Vg0/(kap-1)+pInf*(Vg-Vg0)+Kjet+Kgel+Wgel+Esurf+Edis+Eout)/E0","Normalized energy residual including actual outflow");
    variable(m,"Fconf","pi*R^2*pEl","Axial resultant on one gel hemisphere, not a net force on the whole sphere");
    variable(m,"qJet","rho*U^2/2","Liquid-plug dynamic-pressure scale, not an impact pressure");
    variable(m,"Ijet","mJet*U","Effective column momentum; actual discharged impulse is Iout");
    variable(m,"Fflux","rho*A*U^2","Momentum-flux scale, not a resolved unsteady target force");
    variable(m,"pArrestBound","Iout/(AObs*tObs)","Mean arrest-pressure upper bound from emitted impulse on the declared observer");
    variable(m,"stroke","x/Lbudget","Fraction of the finite discharge-volume budget");
    variable(m,"stretch","R/Rc0","Gel inner-wall circumferential stretch");
    variable(m,"Mjet","abs(U)/cL","Liquid-speed Mach diagnostic");
    variable(m,"Mwall","abs(Uw)/cL","Wall-speed Mach diagnostic");
    variable(m,"communication",(gel?"max(L,2*Rc0)":"L")+"/cL*kap*abs(Vdot)/Vg","Pressure-change communication ratio; no propagation field is solved");
    m.component("c").physics().create("ge","GlobalEquations");
    m.component("c").physics("ge").label(gel?"Four motion states + loss, emitted energy and impulse; first event":"Two outlet motion states + loss, emitted energy and impulse; first event");
    String[] names=gel?new String[]{"qq","vv","rr","ww","dd","ee","ii"}:new String[]{"qq","vv","dd","ee","ii"};
    String[] eq=gel?new String[]{"tau*(qqt-outletOpen*U/Lbudget)","tau*(vvt-acc/Us)","tau*(rrt-Uw/Rc0)","tau*(wwt-wallAcc/Us)","tau*(ddt-Pdis/E0)","tau*(eet-Pout/E0)","tau*(iit-outletOpen*rho*A*U^2/Iscale)"}:new String[]{"tau*(qqt-outletOpen*U/Lbudget)","tau*(vvt-acc/Us)","tau*(ddt-Pdis/E0)","tau*(eet-Pout/E0)","tau*(iit-outletOpen*rho*A*U^2/Iscale)"};
    String[] init=gel?new String[]{"0","0","1","0","0","0","0"}:new String[]{"0","0","0","0","0"};
    String[] zero=gel?new String[]{"0","0","0","0","0","0","0"}:new String[]{"0","0","0","0","0"};
    m.component("c").physics("ge").feature("ge1").set("name",names);
    m.component("c").physics("ge").feature("ge1").set("equation",eq);
    m.component("c").physics("ge").feature("ge1").set("initialValueU",init);
    m.component("c").physics("ge").feature("ge1").set("initialValueUt",zero);
    m.study().create("std");m.study("std").label("Single post-pulse expansion / first ejection episode");
    m.study("std").create("time","Transient");
    m.study("std").feature("time").set("tlist",gel?"range(0,1[ns],100[us])":"range(0,5[ns],100[us])");
    m.study("std").createAutoSequences("all");
    m.sol("sol1").feature("t1").set("rtol","1e-9");
    m.sol("sol1").feature("t1").set("tstepsbdf","strict");
    m.sol("sol1").feature("t1").set("consistent","off");
    m.sol("sol1").feature("t1").create("stop","StopCondition");
    m.sol("sol1").feature("t1").feature("stop").set("stopcondarr",new String[]{"if(outletOpen>0.5,c.U,c.Uw)","Lbudget-c.x","1.2-c.stretch","0.1-max(c.Mjet,c.Mwall)"});
    m.sol("sol1").feature("t1").feature("stop").set("stopcondActive",new String[]{"on","on","on","on"});
    m.sol("sol1").feature("t1").feature("stop").set("stopcondterminateon",new String[]{"negative","negative","negative","negative"});
    m.sol("sol1").feature("t1").feature("stop").set("stopconddesc",new String[]{"First outward ejection ends, or first sealed wall turning point","Connected chamber liquid inventory exhausted","Declared 20% wall-stretch screen (not measured fracture)","Declared Mach 0.1 screen"});
    m.result().table().create("tbl","Table");m.result().table("tbl").label("Single-event conserved energy and finite liquid output");
    m.result().numerical().create("eg","EvalGlobal");m.result().numerical("eg").set("table","tbl");
    String[] ex={"t","c.x","c.U","c.R","c.Uw","c.Vg","c.pb-pInf","c.pEl","c.pRes","c.Fconf","c.qJet","c.Ijet","c.Fflux","c.Kjet","c.Kgel","c.Wgel","c.Esurf","c.Edis","c.energyResidual","c.stroke","c.stretch","c.Mjet","c.Mwall","c.communication","c.acc","c.wallAcc","c.pArrestBound","c.Eout","c.Iout","c.Mout"};
    String[] desc={"time_s","x_m","u_m_s","r_m","wall_speed_m_s","gas_volume_m3","source_gauge_Pa","elastic_Pa","gel_wall_resistance_Pa","confinement_hemisphere_force_N","jet_dynamic_Pa","column_momentum_N_s","momentum_flux_scale_N","kinetic_column_J","kinetic_gel_J","elastic_J","capillary_J","dissipation_J","residual","port_stroke_fraction","wall_stretch","liquid_Mach","wall_Mach","communication_ratio","acceleration_m_s2","wall_acceleration_m_s2","mean_arrest_pressure_bound_Pa","emitted_energy_J","emitted_impulse_N_s","emitted_mass_kg"};
    m.result().numerical("eg").set("expr",ex);m.result().numerical("eg").set("descr",desc);
    for(String group:new String[]{"jet","pressure","energy"}) {
      m.result().create(group,"PlotGroup1D");m.result(group).create("g","Global");
      if(group.equals("jet")) {m.result(group).label("Finite liquid-plug velocity; first event only");m.result(group).feature("g").set("expr",new String[]{"c.U"});m.result(group).feature("g").set("unit",new String[]{"m/s"});}
      if(group.equals("pressure")) {m.result(group).label("Source, elastic resistance and liquid dynamic pressure are distinct");m.result(group).feature("g").set("expr",new String[]{"c.pb-pInf","c.pEl","c.qJet"});m.result(group).feature("g").set("unit",new String[]{"kPa","kPa","kPa"});}
      if(group.equals("energy")) {m.result(group).label("Source energy partition including actual discharged energy");m.result(group).feature("g").set("expr",new String[]{"c.Kjet/E0","c.Kgel/E0","c.Wgel/E0","c.Edis/E0","c.Eout/E0"});}
    }
    m.save(ROOT+"build/"+(gel?"B":"A")+"_configured.mph");
    return m;
  }

  static void solveCase(Model m,String name,double energy,double radius,double g,double eta,double loss,int open,boolean save) throws Exception {
    m.param().set("p0",Double.toString(pressureFor(energy))+"[Pa]");m.param().set("a",Double.toString(radius)+"[m]");
    m.param().set("G",Double.toString(g)+"[Pa]");m.param().set("etaG",Double.toString(eta)+"[Pa*s]");
    m.param().set("Kloss",Double.toString(loss));m.param().set("outletOpen",Integer.toString(open));
    m.sol("sol1").runAll();m.result().numerical("eg").setResult();
    m.result().table("tbl").save(ROOT+"data/"+name+"_native.csv");
    double[][] data=m.result().numerical("eg").getReal();
    double peak=0,res=0,ce=0;
    for(int i=0;i<data[0].length;i++){peak=Math.max(peak,data[2][i]);res=Math.max(res,Math.abs(data[18][i]));ce=Math.max(ce,data[23][i]);}
    if(!Double.isFinite(peak)||!Double.isFinite(res)||res>1e-5) throw new RuntimeException("Conservation acceptance failed: "+name+" residual "+res);
    System.out.println("NATIVE_CASE="+name+" Umax="+peak+" energyResidual="+res+" communication="+ce+" samples="+data[0].length);
    if(save) {
      m.save(ROOT+"models/"+(name.startsWith("A")?"Model_A_Finite_Energy_Pressure_Jet.mph":"Model_B_Hydrogel_Confinement_Jet_Transmission.mph"));
      System.out.println("SAVED_FINAL="+m.label()+" PHYSICS="+Arrays.toString(m.component("c").physics().tags()));
    }
  }

  public static Model run() throws Exception {
    Model a=build(false);
    solveCase(a,"A_baseline",2e-9,5e-6,2e4,0.01,0,1,true);
    for(double e:new double[]{0.5,2,5}) for(double radius:new double[]{3,5,10}) {
      String name="A_E"+(e==0.5?"0.5":Integer.toString((int)e))+"nJ_a"+Integer.toString((int)radius)+"um";
      solveCase(a,name,e*1e-9,radius*1e-6,2e4,0.01,0,1,false);
    }
    ModelUtil.remove("minimal_cavity_jet");
    Model b=build(true);
    solveCase(b,"B_open_baseline",2e-9,5e-6,2e4,0.01,0,1,true);
    solveCase(b,"B_sealed_control",2e-9,5e-6,2e4,0.01,0,0,false);
    solveCase(b,"B_open_loss_K1",2e-9,5e-6,2e4,0.01,1,1,false);
    solveCase(b,"B_open_G5kPa",2e-9,5e-6,5e3,0.01,0,1,false);
    solveCase(b,"B_open_G100kPa",2e-9,5e-6,1e5,0.01,0,1,false);
    solveCase(b,"B_open_eta0",2e-9,5e-6,2e4,0,0,1,false);
    solveCase(b,"B_open_eta0p1",2e-9,5e-6,2e4,0.1,0,1,false);
    System.out.println("NATIVE_MINIMAL_MODELS_COMPLETE");
    return b;
  }
  public static void main(String[] args) throws Exception {run();}
}
