import com.comsol.model.*;
import com.comsol.model.util.*;
import java.util.Arrays;

/** Reload final MPH, rerun in a fresh JVM, then refine the two baselines. */
public class VerifyMinimal {
  static final String ROOT="__ROOT__/";
  static final String[] FILES={"Model_A_Finite_Energy_Pressure_Jet.mph","Model_B_Hydrogel_Confinement_Jet_Transmission.mph"};
  public static Model run() throws Exception {
    Model last=null;
    for(int i=0;i<2;i++) {
      String name=i==0?"A_baseline":"B_open_baseline";
      Model m=ModelUtil.load("verify"+i,ROOT+"models/"+FILES[i]);
      m.modelPath(ROOT+"models");
      String[] physics=m.component("c").physics().tags();
      String type=m.component("c").physics("ge").getType();
      String[] names=m.component("c").physics("ge").feature("ge1").getStringArray("name");
      if(physics.length!=1||!type.equals("GlobalEquations")||names.length!=(i==0?5:7)) throw new RuntimeException("Unexpected native physics/state count");
      if(!m.param().get("tauLaser").equals("10[ns]")) throw new RuntimeException("Unexpected single optical pulse marker");
      System.out.println("AUDIT_NATIVE_FILE="+FILES[i]+" PHYSICS="+Arrays.toString(physics)+" TYPE="+type+" STATES="+Arrays.toString(names));
      m.sol("sol1").runAll();m.result().numerical("eg").setResult();
      m.result().table("tbl").save(ROOT+"verification/"+name+"_fresh_process_baseline.csv");
      m.study("std").feature("time").set("tlist","range(0,2[ns],100[us])");
      m.sol("sol1").feature("t1").set("tlist","range(0,2[ns],100[us])");
      m.sol("sol1").runAll();m.result().numerical("eg").setResult();
      m.result().table("tbl").save(ROOT+"verification/"+name+"_coarse_2ns.csv");
      // This is a pure first-order ODE system; consistency perturbation is unnecessary.
      m.study("std").feature("time").set("tlist","range(0,1[ns],100[us])");
      m.sol("sol1").feature("t1").set("tlist","range(0,1[ns],100[us])");
      m.sol("sol1").feature("t1").set("rtol","1e-9");
      m.sol("sol1").feature("t1").set("consistent","off");
      m.sol("sol1").runAll();m.result().numerical("eg").setResult();
      m.result().table("tbl").save(ROOT+"data/"+name+"_native.csv");
      double[][] v=m.result().numerical("eg").getReal();double peak=0,res=0;
      for(int j=0;j<v[0].length;j++){peak=Math.max(peak,v[2][j]);res=Math.max(res,Math.abs(v[18][j]));}
      if(res>1e-6||!Double.isFinite(peak)) throw new RuntimeException("Refined energy acceptance failed");
      if(Math.abs(v[2][0])>1e-10||Math.abs(v[4][0])>1e-10) throw new RuntimeException("Initialized velocities differ from zero");
      m.save(ROOT+"models/"+FILES[i]);
      System.out.println("REFINED_NATIVE_CASE="+name+" Umax="+peak+" energyResidual="+res+" samples="+v[0].length);
      last=m;
    }
    System.out.println("NATIVE_FRESH_PROCESS_AND_REFINEMENT_COMPLETE");
    return last;
  }
  public static void main(String[] args)throws Exception{run();}
}
