import com.comsol.model.*;
import com.comsol.model.util.*;

/** Fresh-process reload and transient step refinement; originals are read-only. */
public class VerifyEmbedded {
  static final String ROOT="__ROOT__/";
  static double[] inspect(Model m, String name)throws Exception {
    m.sol("sol1").runAll();m.result().numerical("eg").setResult();
    m.result().table("tbl").save(ROOT+"verification/"+name+".csv");
    double[][] d=m.result().numerical("eg").getReal();
    double peak=0,er=0,mr=0;
    for(int i=0;i<d[0].length;i++) {
      peak=Math.max(peak,d[16][i]);er=Math.max(er,Math.abs(d[19][i]));mr=Math.max(mr,Math.abs(d[12][i]));
      if(!(d[3][i]>d[4][i]&&d[4][i]>0&&d[8][i]>0&&d[8][i]<1&&d[11][i]>0))
        throw new RuntimeException("Native reload phase/domain failure");
    }
    if(er>1e-6||mr>1e-8)throw new RuntimeException("Native reload conservation failure");
    return new double[]{peak,d[0][d[0].length-1],er,mr};
  }
  public static Model run()throws Exception {
    Model eq=ModelUtil.load("reload_equilibrium",ROOT+"models/Embedded_PFC_Curved_Equilibrium.mph");
    if(eq.component("c").physics("ge").feature("ge1").getStringArray("name").length!=4)
      throw new RuntimeException("Unexpected stationary state count");
    inspect(eq,"equilibrium_fresh_reload");ModelUtil.remove("reload_equilibrium");
    Model tr=ModelUtil.load("reload_transient",ROOT+"models/Embedded_PFC_PostNucleation_Intact_Gel.mph");
    if(tr.component("c").physics("ge").feature("ge1").getStringArray("name").length!=7)
      throw new RuntimeException("Unexpected transient state count");
    double[] base=inspect(tr,"transient_fresh_reload");
    tr.param().set("tStep","tau/200");
    tr.study("std").feature("time").set("tlist","range(0,tStep,50*tau)");
    tr.sol("sol1").feature("t1").set("tlist","range(0,tStep,50*tau)");
    tr.sol("sol1").feature("t1").set("rtol","2e-9");
    double[] fine=inspect(tr,"transient_native_half_step");
    double speedErr=Math.abs(fine[0]-base[0])/fine[0];
    double endErr=Math.abs(fine[1]-base[1])/fine[1];
    // Output sample rounding near stop conditions is bounded by one coarse step.
    if(speedErr>2e-4||endErr>0.002)throw new RuntimeException("Native refinement failed: "+speedErr+" "+endErr);
    System.out.println("EMBEDDED_NATIVE_RELOAD_REFINEMENT_PASS speed_relative="+speedErr+" endpoint_relative="+endErr+
      " energy_residual="+fine[2]+" mass_residual="+fine[3]);
    return tr;
  }
  public static void main(String[] args)throws Exception{run();}
}
