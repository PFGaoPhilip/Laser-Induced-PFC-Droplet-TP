import com.comsol.model.*;
import com.comsol.model.util.*;

/** Finite PFC / liquid shell / intact spherical gel. No nucleation or outlet. */
public class EmbeddedPfc {
  static final String ROOT="__ROOT__/";
  static void par(Model m,String key,String value,String desc){m.param().set(key,value,desc);}
  static void var(Model m,String key,String value,String desc){m.component("c").variable("v").set(key,value,desc);}

  static Model build(boolean dynamic)throws Exception {
    Model m=ModelUtil.create(dynamic?"embedded_pfc_transient":"embedded_pfc_equilibrium");
    m.label(dynamic?"Embedded PFC: conditional post-nucleation expansion before gel damage":"Embedded PFC: curved finite-inventory phase equilibrium");
    m.modelPath(ROOT+"models");m.save(ROOT+"build/"+(dynamic?"transient":"equilibrium")+"_identity.mph");
    NativePfcEOS.install(m);
    par(m,"Rd","0.3[um]","Initial LIQUID droplet radius, not gas cavity radius");
    par(m,"G","20[kPa]","Neo-Hookean shear modulus, stipulated");
    par(m,"eta","0.01[Pa*s]","Kelvin-Voigt effective viscosity, stipulated");
    par(m,"sigO","0.054[N/m]","Constant liquid-PFC/aqueous outer interface control");
    par(m,"sigI","0.00941[N/m]","Constant PFP liquid/gas reference proxy");
    par(m,"pInf","100[kPa]","Absolute ambient pressure");
    par(m,"rhoHost","1000[kg/m^3]","Undrained effective host density");
    par(m,"cs","1500[m/s]","Mach-screen sound speed");
    par(m,"rhoInit","1623[kg/m^3]","Initial compressed PFC liquid density, independently evaluated");
    par(m,"uInit","20000[J/kg]","Initial PFC specific internal energy, same HEOS reference");
    par(m,"pfh","0","0=PFP, 1=PFH; both real-fluid EOS installed");
    par(m,"lam","2.1","Prescribed stationary stretch; not a fracture prediction");
    par(m,"lamInit","1.2","Explicit post-nucleation seed stretch");
    par(m,"lamLimit","2.1","DECLARED intact-model stopping screen; not measured rupture");
    par(m,"Ts","350[K]","Temperature normalization");
    par(m,"ps","100[kPa]","Pressure normalization");
    par(m,"us","100[kJ/kg]","Specific-energy normalization");
    par(m,"Us","sqrt(ps/rhoHost)","Radial-speed normalization");
    par(m,"tau","Rd/Us","Transient time normalization");
    par(m,"V0","4*pi*Rd^3/3","Initial liquid inclusion volume");
    par(m,"mass","rhoInit*V0","FIXED finite PFC mass");
    par(m,"Es","mass*us","Accounting energy normalization");
    par(m,"Eseed","12[pJ]","Retained supplied-seed energy relative to all-liquid reference; preparation losses omitted");
    par(m,"tStep","tau/100","Output step; solver maximum also bounded");
    m.component().create("c",true);m.component("c").variable().create("v");
    var(m,"R",dynamic?"Rd*rr":"Rd*lam","Outer liquid-shell/gel radius");
    var(m,"W",dynamic?"Us*ww":"0[m/s]","RADIAL speed, not jet speed");
    var(m,"D",dynamic?"Es*dd":"0[J]","Integrated nonnegative host viscous loss");
    var(m,"T","Ts*th","Uniform PFC phase temperature");
    var(m,"rl","1000[kg/m^3]*exp(al)","Liquid PFC density");
    var(m,"rv","10[kg/m^3]*exp(av)","Vapor PFC density");
    var(m,"b","R*exp(ab)","Vapor core radius; requires 0<b<R");
    var(m,"V","4*pi*R^3/3","Whole PFC inclusion volume");
    var(m,"Vb","4*pi*b^3/3","Vapor-core volume");
    var(m,"ml","rl*(V-Vb)","Remaining LIQUID PFC mass");
    var(m,"mv","rv*Vb","VAPOR PFC mass");
    var(m,"pL","if(pfh>0.5,pfhp(T/1[K],rl/1[kg/m^3]),pfpp(T/1[K],rl/1[kg/m^3]))*1[Pa]","Real-fluid liquid pressure");
    var(m,"pV","if(pfh>0.5,pfhp(T/1[K],rv/1[kg/m^3]),pfpp(T/1[K],rv/1[kg/m^3]))*1[Pa]","Real-fluid vapor pressure");
    var(m,"uL","if(pfh>0.5,pfhu(T/1[K],rl/1[kg/m^3]),pfpu(T/1[K],rl/1[kg/m^3]))*1[J/kg]","Liquid specific internal energy");
    var(m,"uV","if(pfh>0.5,pfhu(T/1[K],rv/1[kg/m^3]),pfpu(T/1[K],rv/1[kg/m^3]))*1[J/kg]","Vapor specific internal energy");
    var(m,"gL","if(pfh>0.5,pfhg(T/1[K],rl/1[kg/m^3]),pfpg(T/1[K],rl/1[kg/m^3]))*1[J/kg]","Liquid chemical potential per mass");
    var(m,"gV","if(pfh>0.5,pfhg(T/1[K],rv/1[kg/m^3]),pfpg(T/1[K],rv/1[kg/m^3]))*1[J/kg]","Vapor chemical potential per mass");
    var(m,"pEl","G/2*(5-4*Rd/R-(Rd/R)^4)","Intact spherical neo-Hookean resistance");
    var(m,"pNeed","pInf+pEl+2*sigO/R","STATIC outer liquid pressure required by host");
    var(m,"Egel","2*pi*G*(5*R^3/3-2*Rd*R^2+Rd^4/R-2*Rd^3/3)","Recoverable gel strain energy");
    var(m,"Eint","ml*uL+mv*uV-mass*uInit","PFC internal-energy change from initial LIQUID");
    var(m,"Esurf","4*pi*(sigO*(R^2-Rd^2)+sigI*b^2)","Both interfaces, distinct tensions");
    var(m,"Eamb","pInf*(V-V0)","Work against ambient pressure");
    var(m,"Khost","2*pi*rhoHost*R^3*W^2","Host radial kinetic energy");
    var(m,"Etot","Eint+Egel+Esurf+Eamb+Khost+D","Closed retained-seed-energy accounting");
    var(m,"acc","((pL-pNeed-4*eta*W/R)/rhoHost-1.5*W^2)/R","Incompressible radial host acceleration");
    var(m,"Pdis","16*pi*eta*R*W^2","Nonnegative host viscous-loss power");
    var(m,"massRes","(ml+mv)/mass-1","Finite mass residual");
    var(m,"chemRes","gL-gV","Phase equilibrium residual, J/kg");
    var(m,"innerRes","pV-pL-2*sigI/b","Inner capillary-traction residual, Pa");
    var(m,"outerRes","pL-pNeed","Static host-traction residual, Pa");
    var(m,"energyRes","(Etot-Eseed)/Eseed","Retained-seed-energy residual");
    var(m,"vapFrac","mv/mass","Finite PFC vapor mass fraction");
    var(m,"shell","R-b","Remaining liquid-shell thickness");
    var(m,"emittedMass","0[kg]","No outlet or fracture is modeled");
    m.component("c").physics().create("ge","GlobalEquations");
    if(dynamic) {
      m.component("c").physics("ge").feature("ge1").set("name",new String[]{"rr","ww","dd","th","al","av","ab"});
      m.component("c").physics("ge").feature("ge1").set("equation",new String[]{"tau*(rrt-W/Rd)","tau*(wwt-acc/Us)","tau*(ddt-Pdis/Es)","innerRes/ps","chemRes/us","massRes","(Etot-Eseed)/Es"});
      m.component("c").physics("ge").feature("ge1").set("initialValueU",new String[]{"lamInit","0","0","1","0.33","1.7","-0.3"});
      m.component("c").physics("ge").feature("ge1").set("initialValueUt",new String[]{"0","0","0","0","0","0","0"});
    } else {
      m.component("c").physics("ge").feature("ge1").set("name",new String[]{"th","al","av","ab"});
      m.component("c").physics("ge").feature("ge1").set("equation",new String[]{"outerRes/ps","innerRes/ps","chemRes/us","massRes"});
      m.component("c").physics("ge").feature("ge1").set("initialValueU",new String[]{"1","0.33","1.7","-0.3"});
    }
    m.study().create("std");m.study("std").create(dynamic?"time":"stat",dynamic?"Transient":"Stationary");
    if(dynamic)m.study("std").feature("time").set("tlist","range(0,tStep,50*tau)");
    m.study("std").createAutoSequences("all");
    if(dynamic) {
      m.sol("sol1").feature("t1").set("rtol","1e-8");
      m.sol("sol1").feature("t1").set("tstepsbdf","strict");
      m.sol("sol1").feature("t1").set("consistent","off");
      m.sol("sol1").feature("t1").create("stop","StopCondition");
      m.sol("sol1").feature("t1").feature("stop").set("stopcondarr",new String[]{"c.W","lamLimit-c.R/Rd","0.1-abs(c.W)/cs","c.shell","c.vapFrac","1-c.vapFrac"});
      m.sol("sol1").feature("t1").feature("stop").set("stopcondActive",new String[]{"on","on","on","on","on","on"});
      m.sol("sol1").feature("t1").feature("stop").set("stopcondterminateon",new String[]{"negative","negative","negative","negative","negative","negative"});
      m.sol("sol1").feature("t1").feature("stop").set("stopconddesc",new String[]{"First expansion turning point","Declared intact stretch limit, not rupture","Mach 0.1 screen","Liquid shell exhausted","Vapor inventory exhausted","Liquid inventory exhausted"});
    } else m.sol("sol1").feature("s1").set("stol","1e-10");
    m.result().table().create("tbl","Table");
    m.result().numerical().create("eg","EvalGlobal");m.result().numerical("eg").set("table","tbl");
    m.result().numerical("eg").set("expr",new String[]{dynamic?"t":"0[s]","c.R/Rd","c.T","c.rl","c.rv","c.b","c.pL","c.pV","c.vapFrac","c.Etot","c.pEl","c.shell","c.massRes","c.chemRes","c.innerRes","c.outerRes","c.W","c.D","c.Khost","c.energyRes","c.emittedMass"});
    m.result().numerical("eg").set("descr",new String[]{"time_s","stretch","T_K","liquid_density_kg_m3","vapor_density_kg_m3","bubble_radius_m","liquid_pressure_Pa","vapor_pressure_Pa","vapor_fraction","equilibrium_state_energy_J","gel_pressure_Pa","shell_thickness_m","mass_relative_residual","chemical_residual_J_kg","inner_traction_residual_Pa","outer_static_residual_Pa","radial_speed_m_s","dissipated_J","host_kinetic_J","total_energy_residual","exterior_emitted_mass_kg"});
    for(String tag:new String[]{"phase","energy","motion"}){
      m.result().create(tag,"PlotGroup1D");m.result(tag).create("g","Global");
      if(tag.equals("phase")){m.result(tag).label("Finite PFC vapor MASS fraction");m.result(tag).feature("g").set("expr",new String[]{"c.vapFrac"});}
      if(tag.equals("energy")){m.result(tag).label("Energy destinations and conservation");m.result(tag).feature("g").set("expr",new String[]{"c.Eint/Eseed","c.Egel/Eseed","c.Esurf/Eseed","c.Eamb/Eseed","c.Khost/Eseed","c.D/Eseed"});}
      if(tag.equals("motion")){m.result(tag).label("RADIAL wall speed; no exterior jet");m.result(tag).feature("g").set("expr",new String[]{"c.W"});m.result(tag).feature("g").set("unit",new String[]{"m/s"});}
    }
    return m;
  }

  static void setCase(Model m,double[] q){
    String[] keys={"Rd","G","eta","sigO","sigI","rhoInit","uInit","pfh","lam","Eseed"};
    String[] units={"m","Pa","Pa*s","N/m","N/m","kg/m^3","J/kg","1","1","J"};
    for(int i=0;i<keys.length;i++)m.param().set(keys[i],q[i]+"["+units[i]+"]");
  }

  static void check(Model m,String name,boolean dynamic)throws Exception{
    m.sol("sol1").runAll();m.result().numerical("eg").setResult();
    double[][] d=m.result().numerical("eg").getReal();
    double mr=0,cr=0,ir=0,er=0,peak=0;
    for(int i=0;i<d[0].length;i++){
      mr=Math.max(mr,Math.abs(d[12][i]));cr=Math.max(cr,Math.abs(d[13][i]));
      ir=Math.max(ir,Math.abs(d[14][i]));er=Math.max(er,Math.abs(d[19][i]));peak=Math.max(peak,d[16][i]);
      if(!(d[8][i]>0&&d[8][i]<1&&d[11][i]>0))throw new RuntimeException("Invalid inventory/shell: "+name);
    }
    if(mr>1e-5||cr>0.2||ir>2||(dynamic&&er>1e-5))throw new RuntimeException("Closure failed: "+name+" "+mr+" "+cr+" "+ir+" "+er);
    m.result().table("tbl").save(ROOT+"data/"+name+"_native.csv");
    System.out.println("PFC_NATIVE_CASE="+name+" mass="+mr+" chem="+cr+" traction="+ir+" energy="+er+" radial_peak="+peak+" samples="+d[0].length);
  }

  public static Model run()throws Exception{
    Model eq=build(false);
    for(int k=0;k<NativeCases.EQUILIBRIUM.length;k++){
      double[] q=NativeCases.EQUILIBRIUM[k];setCase(eq,q);
      eq.component("c").physics("ge").feature("ge1").set("initialValueU",new String[]{Double.toString(q[10]*1.001/350),Double.toString(Math.log(q[11]*.999/1000)),Double.toString(Math.log(q[12]*1.001/10)),Double.toString(Math.log(q[13]*.999))});
      check(eq,NativeCases.EQ_NAMES[k],false);
    }
    eq.save(ROOT+"models/Embedded_PFC_Curved_Equilibrium.mph");ModelUtil.remove("embedded_pfc_equilibrium");
    Model tr=build(true);
    for(int k=0;k<NativeCases.TRANSIENT.length;k++){
      double[] q=NativeCases.TRANSIENT[k];setCase(tr,q);
      tr.component("c").physics("ge").feature("ge1").set("initialValueU",new String[]{"lamInit","0","0",Double.toString(q[10]/350),Double.toString(Math.log(q[11]/1000)),Double.toString(Math.log(q[12]/10)),Double.toString(Math.log(q[13]))});
      check(tr,NativeCases.TR_NAMES[k],true);
      if(NativeCases.TR_NAMES[k].equals("PFP_r0.3um_eta0.01"))tr.save(ROOT+"models/Embedded_PFC_PostNucleation_Intact_Gel.mph");
    }
    System.out.println("EMBEDDED_PFC_NATIVE_COMPLETE");return tr;
  }
  public static void main(String[] args)throws Exception{run();}
}

