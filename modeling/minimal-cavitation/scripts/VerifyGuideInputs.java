import com.comsol.model.*;
import com.comsol.model.util.*;
import java.util.Arrays;

/** Verify the tutorial's imports and its A-to-B conversion in memory. */
public class VerifyGuideInputs {
  static final String ROOT="__ROOT__/";
  static void require(boolean ok,String message) {
    if(!ok)throw new RuntimeException(message);
  }
  public static Model run()throws Exception {
    Model a=ModelUtil.load("guidePractice",ROOT+"models/Model_A_Finite_Energy_Pressure_Jet.mph");
    a.param().loadFile(ROOT+"resources/gui/A_parameters_import.txt");
    a.component("c").variable("v").loadFile(ROOT+"resources/gui/A_variables_import.txt");
    require(a.param().varnames().length==32,"Parameter import count");
    require(a.component("c").variable("v").varnames().length==33,"Variable import count");
    require(a.component("c").variable("v").get("R").equals("Rc0"),"Rigid imported radius");
    require(a.component("c").variable("v").get("Eout").equals("E0*ee"),"Emitted energy expression");
    require(a.component("c").variable("v").get("acc").contains("-rho*U^2/2"),"Outgoing kinetic head");
    System.out.println("PASS_A_IMPORT parameters=32 variables=33 available_work_J="+a.param().evaluate("E0"));
    a.param().loadFile(ROOT+"resources/gui/B_parameters_import.txt");
    a.component("c").variable("v").loadFile(ROOT+"resources/gui/B_variables_patch_import.txt");
    require(a.component("c").variable("v").varnames().length==33,"Patch must retain other variable names");
    require(a.component("c").variable("v").get("R").equals("Rc0*rr"),"Gel radius patch");
    require(a.component("c").variable("v").get("communication").startsWith("max(L,2*Rc0)"),"Gel communication patch");
    String[] names={"qq","vv","rr","ww","dd","ee","ii"};
    String[] equations={"tau*(qqt-outletOpen*U/Lbudget)","tau*(vvt-acc/Us)","tau*(rrt-Uw/Rc0)","tau*(wwt-wallAcc/Us)","tau*(ddt-Pdis/E0)","tau*(eet-Pout/E0)","tau*(iit-outletOpen*rho*A*U^2/Iscale)"};
    a.component("c").physics("ge").feature("ge1").set("name",names);
    a.component("c").physics("ge").feature("ge1").set("equation",equations);
    a.component("c").physics("ge").feature("ge1").set("initialValueU",new String[]{"0","0","1","0","0","0","0"});
    a.component("c").physics("ge").feature("ge1").set("initialValueUt",new String[]{"0","0","0","0","0","0","0"});
    a.sol("sol1").runAll();
    a.result().numerical("eg").setResult();
    double[][] values=a.result().numerical("eg").getReal();
    double peak=0,residual=0;
    for(int j=0;j<values[0].length;j++) {
      peak=Math.max(peak,values[2][j]);residual=Math.max(residual,Math.abs(values[18][j]));
    }
    require(Math.abs(peak-1.6253845827345195)<1e-6,"A-to-B converted peak differs from accepted B");
    require(residual<1e-6,"Converted energy balance");
    require(a.sol("sol1").getSize()[0]==7,"Converted state count");
    System.out.println("PASS_B_PATCH_AND_CONVERSION states="+Arrays.toString(names)+" peak_m_s="+peak+" maximum_energy_residual="+residual+" stored="+Arrays.toString(a.sol("sol1").getSize()));
    Model b=ModelUtil.create("guideFreshImports");b.component().create("c",true);b.component("c").variable().create("v");
    b.param().loadFile(ROOT+"resources/gui/B_parameters_import.txt");
    b.component("c").variable("v").loadFile(ROOT+"resources/gui/B_variables_import.txt");
    require(b.param().varnames().length==32 && b.component("c").variable("v").varnames().length==33,"Full B import counts");
    for(String name:a.component("c").variable("v").varnames()) {
      require(a.component("c").variable("v").get(name).equals(b.component("c").variable("v").get(name)),"Full B import and patched B disagree at "+name);
    }
    System.out.println("PASS_B_FULL_IMPORT parameters=32 variables=33 matches_converted_B");
    System.out.println("GUIDE_NATIVE_IMPORT_CONVERSION_COMPLETE: models were tested in memory; no native model file was rewritten.");
    return a;
  }
  public static void main(String[]args)throws Exception{run();}
}
