# Conditional cavitation answer for experimental reference

The declared PFP/PFH problem has **no computed attainable velocity or receiver-pressure optimum**. All 18 objectives, maximizing designs, attained lower values and certified upper values remain null. The available answer is conditional: a complete available-work budget bounds the speed of a prescribed participating water mass; a chosen linear-contact model then gives a contact-pressure ceiling. The current evidence supplies neither a certified PFC maximum nor an actual-device maximum. Stage1 and Stage2 remain closed under the accepted loosened policy; Stage3 completes documentation and delivery.

## Accepted ceiling route

The accepted route and its derivation are preserved unchanged in the [original conditional solution](inputs/conditional_termtex/CONDITIONAL_SOLUTION.md), equations E01–E24. Its prescribed illustrative 5 nJ cylindrical water plug gives 84.1044 m/s, 126.1566 MPa against a rigid target, and 63.0783 MPa at equal impedance. The density is 1000 kg/m³, sound speed 1500 m/s, radius 3 µm and length 50 µm. These are lossless energy and weak-compression, normal planar first-contact results before lateral release. They are not computed PFC outputs or finite-disk/window receiver observables. [Source and exact values](inputs/conditional_termtex/verification.json), `numericalChecks`; ledger `linear_example`.

**Symbols before Eq. (A01):** available mechanical work (E_{\rm av}\ge0) (J), prescribed positive participating mass (m_j) (kg), nonnegative uniform or mass-qualified speed (U_j) (m/s), jet impedance (Z_j>0) and target impedance (Z_t\ge0) (Pa·s/m), and contact gauge pressure \(\Delta p_c\) (Pa). Subscripts identify available work, jet, target and contact; “ceiling” identifies the bound in its adopted model.

$$
U_j\le\sqrt{\frac{2E_{\rm av}}{m_j}},\qquad
\Delta p_c^{\rm ceiling}=\frac{Z_jZ_t}{Z_j+Z_t}\sqrt{\frac{2E_{\rm av}}{m_j}}.
$$

The pressure factor approaches (Z_j) for a rigid target and equals (Z_j/2) at equal impedance. For a prescribed positive radius cutoff, the accepted Rayleigh solution has a finite inward spherical wall-speed maximum. It diverges when the imposed cutoff tends to zero; this is a singular limit of an incompressible, inviscid, tension-free spherical model, not a physical maximum. It does not define the jet or averaged receiver objectives. The complete integration, symbol definitions and checks remain in the unchanged E13–E22 source.

## Exact-input available-work allowances

The adopted fully uniform activation of an initially 6 µm droplet gives accepted conditional available work of 2.722572407203039 nJ for PFP and 4.622122564638143 nJ for PFH. These assumed-state thermodynamic values remain conditional. [Preparation source](inputs/full_closure/data/accepted_preparation.json), `fluids.{species}.activated_budget.Phi_J`; ledger `ceilings`.

**Symbols before Eq. (A02):** (m_*>0) is prescribed water mass (kg); (U(m_*,t)\ge0) is its directed mass-qualified speed at time (t) (m/s); (K_w(t)) is full-vector water kinetic energy (J); \(\Phi_a\ge0\) is the adopted activation available work (J). Time is in seconds; subscripts identify water and activation.

$$
\tfrac12m_*U(m_*,t)^2\le K_w(t)\le\Phi_a
\quad\Longrightarrow\quad
U(m_*,t)\le\sqrt{2\Phi_a/m_*}.
$$

The first inequality follows by integrating kinetic energy over at least the prescribed water mass with directed speed above the threshold; full-vector speed is at least its directed component. The second requires a complete consistent availability budget, nonnegative remaining contributions and no further useful input. Those requirements are not demonstrated for the loosened candidate030 trajectory. This table is therefore tier **R|A**, an energy allowance under its hypotheses, not a certified current-model upper interval or an achieved speed.

| Whole-water mass (pg) | PFP allowance (m/s) | PFH allowance (m/s) |
|---:|---:|---:|
| 1 | 2333.48 | 3040.44 |
| 3 | 1347.24 | 1755.40 |
| 10 | 737.91 | 961.47 |
| 30 | 426.03 | 555.10 |
| 100 | 233.35 | 304.04 |

One pg is (10^{-15}) kg. The accepted original ten-picogram illustrations remain **737.5636 and 961.2492 m/s**, using rounded 2.72 and 4.62 nJ inputs. The slightly different exact-input row above uses the unrounded preparation records; it does not revise the original calculation. The [rebuilt CSV](data/CONDITIONAL_ENERGY_CEILINGS.csv) and [results ledger](RESULTS_LEDGER.json) retain the full precision and provenance.

No analogous numerical maximum is supplied for the registered receiver-pressure objectives. The linear-contact ceiling depends on an explicitly chosen participating mass and contact model; it is not a bound automatically applicable to an arbitrary finite pressure disk and averaging window.

## Historical predictions and estimates

The historical processed table has 35 stored rows, whereas older handoff prose describes 40 sampled cases. Reported group values below come from the stored rows; they do not establish 40 valid completed trajectories. Every selected row, closure, stand-off, profile mass and source hash is recorded under `historical` in the ledger. [Historical source](inputs/expert_resolution/data/envelope_rows.json); [original tier definitions](inputs/expert_resolution/tex/09_envelope.tex).

| Historical group | PFP | PFH | Tier and meaning |
|---|---:|---:|---|
| Largest stored slow-condensation in-screen speed | 65.27 m/s | 186.95 m/s | P: reduced-model sample |
| Largest stored fast-condensation in-screen speed | 360.17 m/s | 377.51 m/s | P: reduced-model sample |
| Largest stored beyond-screen speed | 481.53 m/s | 715.48 m/s | E: extrapolation beyond working screen |
| Largest stored in-screen internal contact-pressure estimate | 292.32 MPa | 307.47 MPa | E: mixed-contact estimate |
| Largest stored in-screen receiver-pressure estimate | 21.03 MPa | 22.37 MPa | E: assumed propagation/spreading estimate |

The historical screen is Mach 0.3 in an incompressible model; it is a working cutoff, not an error certificate. Historical speeds use a geometric sampled jet profile rather than the declared whole-water quantile. The sampled axial kinetic energy is a lower bound on the full-vector kinetic energy of the sampled region. Historical pressure estimates are neither solved wall loads nor the registered disk/window averages. None is an attained continuous optimum, certified lower bound or current engineering envelope.

## Fixed objective scope and missing evidence

PFP and PFH are optimized separately in axisymmetric water above a rigid plane, with accommodation coefficient \(\alpha_c\in[0,1]\) and stand-off \(\gamma=h/R_m\ge1.25\). The centre height is (h>0), and (R_m>0) must be the free-field maximum radius of the **same model**. There is no finite upper application bound on stand-off; a scan cutoff cannot enclose the unsampled tail. Same-model (R_m) and candidate030 stand-off qualification remain unresolved.

Directed speed is toward the plane: (w=-u_z). The mass quantile includes all water fractions without a geometric jet mask. Its objective ends at first axial liquid–liquid contact inside the cavity or the first post-growth collapse minimum if no earlier impact exists. Tiny initial preparation extrema do not replace the post-growth event. Pressure is gauge pressure averaged over the prescribed rigid-plane disk and a time window wholly inside the interval ending at the first rebound maximum. That event must exist and the interval must contain the averaging duration; the nominal simulation horizon is not a substitute. Wall viscous normal stress requires a separate check. [Exact definitions and event conditions](inputs/full_closure/PROBLEM_STATEMENT.md), P02–P06.

| Objective IDs | Conditions | Attained value, design, lower/upper pair |
|---|---|---|
| PFP_U_1pg, PFP_U_3pg, PFP_U_10pg, PFP_U_30pg, PFP_U_100pg | PFP; all-water masses 1, 3, 10, 30, 100 pg | Each null / NOT_COMPUTED |
| PFH_U_1pg, PFH_U_3pg, PFH_U_10pg, PFH_U_30pg, PFH_U_100pg | PFH; same masses | Each null / NOT_COMPUTED |
| PFP_P_2um_2ns, PFP_P_2um_20ns, PFP_P_10um_2ns, PFP_P_10um_20ns | PFP; disk radii 2, 10 µm × windows 2, 20 ns | Each null / NOT_COMPUTED |
| PFH_P_2um_2ns, PFH_P_2um_20ns, PFH_P_10um_2ns, PFH_P_10um_20ns | PFH; same disks/windows | Each null / NOT_COMPUTED |

The target certificate gaps remain 5% for velocity and 10% for pressure, numerical error at most one third of the respective tolerance and domain sensitivity at most one tenth. No such intervals, numerical errors, domain sensitivities, maximizing designs or global bounds are established. Every absent field stays null, not zero.

## Diagnostic evidence, accepted waivers and verdict

Candidate030’s transferred history ends at **0.43 ns and 43 accepted steps**, line 432. This is a partial static snapshot; it demonstrates no completed objective event or full-cycle trajectory. Its `meta.json` belongs to the old candidate028 run, so the zero exit code does not establish candidate030 completion. Candidate030’s `pilot_run_meta.txt` has no completion receipt. Earlier candidate028 failed at 0.44 ns, and candidate029 stopped on the heat gate at 0.37 ns. The local candidate030 snapshot does not prove advancement beyond the 0.44 ns failure. Historical closeout prose and the external run status at that time do not replace later transferred evidence. [Source records](inputs/full_closure/runs/AXI_PFP_transport_candidate030_STAGE2_LOOSENED_PILOT001/history.csv); ledger `diagnostics` and `metadata_caveats`.

The accepted candidate018–030 soft-pass stack remains in force. The seven Stage2 exit waivers cover full-cycle pilot/horizon; 108-case coverage and all 18 objectives; same-model radius/stand-off qualification; PFH route; registered observers; hold-outs/refinement/certification; and strict production C4. These dispositions are **WAIVED**, not measured scientific PASS. The strict production-admission failure and all historical failures remain recorded. [Owner-accepted closeout](inputs/full_closure/verification/STAGE2_LOOSENED_CLOSED_20261013.md); [verified entry receipt002](inputs/full_closure/verification/STAGE2_LOOSENED_CLOSE_VERIFY_STAGE3_ENTRY_20261014_002.json).

The dominant assumption’s effect on an attainable optimum is itself unresolved: no sensitivity ranking or optimum exists. Uniform activation, thermodynamic reference consistency, condensation closure, compressible flow, content uniformity and wall geometry could change reachable output. The fixed problem excludes optical breakdown, device energy deposition/transfer, gel/air loading and attached-cavity mechanisms outside the accepted detached scope. The adopted constitutive laws and continuum approximation are assumptions, not device validation.

**Engineering verdict:** documentation and available-number review can be completed under the loosened policy, with the scientific maximum unresolved. [Independent review](review/INDEPENDENT_REVIEW.md), [integrated gate review](INTERNAL_REVIEW.md) and [delivery README](README.md) specify checks actually performed and reproducibility limits. No strict acceptance, certified PFC maximum or actual-device maximum is claimed.
