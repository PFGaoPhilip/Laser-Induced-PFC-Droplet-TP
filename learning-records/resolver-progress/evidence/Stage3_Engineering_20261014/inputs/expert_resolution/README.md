# Laser-induced PFC cavitation: conditional limits and unresolved device maximum

Open [READER.html](READER.html) in any current browser, or read the complete [expert report](output/EXPERT_REPORT.pdf). The reader, mathematics, fonts and figures work offline and have a day/night toggle. Download or forward the whole folder. External scholarly links are optional.

The expert report answers the general maximum question by defining the observable and budget, deriving conditional ceilings, and computing an explicit benchmark. **The actual PFC device maximum remains unresolved.** The preparation state, condensation law, geometry and receiver response have not been measured for this device. A finite numerical sample is not a proof of a continuous global optimum.

The six main results, with paired numbers in PFP / PFH order:

1. The homogeneous-nucleation model gives activation temperatures 386.5 / 415.2 K for a 6 µm droplet and a 5 ns hazard interval. The interval is an assumed constant-hot-state observation time; it does not establish a uniform isobaric 5 ns laser preparation. A same-duration temperature ramp may require a higher peak, so these are not proved upper onset temperatures for arbitrary pulse trajectories.
2. The conditional thermal-expansion source-pressure ceilings are 1.265 / 1.085 MPa **absolute**, requiring H0, H2 and H5. They are not collapse or target-impact pressures. The nonequilibrium extension remains unproved.
3. The adopted activated states have exergies 2.72 / 4.62 nJ and conditional maximum cavity radii 23.8 / 24.2 µm. Conservation gives a useful-work ceiling, conditioned on consistent reference availability and no unaccounted external work.
4. For benchmark B1 (one 6 µm droplet in water near a rigid wall, sampled stand-offs 1.25≤γ≤4), nominal N64 slow-closure tip speeds reach 65.3 / 186.9 m/s. These are the largest sampled predictions, qualified by the convergence record below. Fast-closure envelopes approach the 444.6 m/s model screen; neither a physical maximum nor a demonstrated physical lower bound follows from that screen.
5. Among nominal screen-admissible samples, adopted internal liquid-contact pressure scales reach 292 / 307 MPa above ambient. These use a nonlinear jet-side Tait jump against a linear target impedance equal to the water impedance, rather than exact symmetric nonlinear two-water shocks. The separate receiver-wave spreading estimates span 1.7–21 / 2.5–22 MPa above ambient. Contact duration/area, target response and sensor averaging must be specified; no resolved target or sensor pressure is claimed.
6. The device maximum, near-sonic fast jets, direct target contact and gel-embedded directed jets remain unresolved. Section 10 gives the measurements that close each gap. No experimental validation or independent external expert review is claimed.

The earlier 25.28 m/s outlet sample and 512.21 kPa source gauge pressure retain their original meanings. Neither is a theoretical PFC cavitation maximum.

## Claim tiers and numerical evidence

| Tier | Meaning | How to use it |
|---|---|---|
| R | Rigorous under stated hypotheses | A ceiling is conditional on its stated budget, state and reference assumptions. |
| P | Reduced-model prediction | Use only within the model domain and with numerical uncertainty. |
| E | Estimate | Receiver spreading and beyond-screen extrapolation are not solved physical peaks. |
| U | Unresolved | State the missing measurement or missing physics explicitly. |

`R|A` in the result ledger denotes a rigorous relation evaluated at an assumed state. The parameter ledger separately uses M (measured), S (sourced), A (assumed), U (unknown); **no parameter is labelled specimen-measured**.

All 18 requested BIM refinement attempts and 12 KM refinements are recorded. Among completed comparable BIM pairs, the largest tip-speed change is 4.74% for N64→96 and 0.31% for the requested N64 step-halving pairs. The largest uncensored KM N160→320 speed change is 2.59%. The requested BIM set contains 3 aborted runs, retained as failed diagnostics and excluded from speed envelopes. Smaller-step stabilization is labelled separately because it changes both the grid and the step relative to baseline. Read the full comparisons for profile mass/energy sensitivity and any additional refinements. Mach-censored runs have no resolved physical peak; an identical imposed event speed is not convergence evidence. At the matched smaller step, completed N64→N96 stabilized pairs change speed by at most 0.321%. This does not erase the larger-step failures or their resolution sensitivity. The five additional targeted attempts include 1 N128/.01 abort; its pre-impact diagnostic speed is excluded, so N96→N128 convergence remains unresolved. At N96, halving the step in the valid PFH fast case changes tip speed by 4.91%; this sensitivity also remains.

Read [BIM convergence](verification/pfc_bim_convergence.json), [KM refinement](verification/km_refine_summary.json), [input identity checks](verification/pfc_bim_input_checks.json), [original solver checks](verification/bim_unit_tests.json) and [mechanical energy checks](verification/km_energy_conservation.json). The 3–6% offset from the Supponen constant-pressure jet benchmark is a model/benchmark discrepancy, distinct from discretisation changes. A jet-profile mass or energy change is not a conservation residual. The mechanical energy check does not establish complete thermodynamic phase/reference conservation; radiation bookkeeping uses a residual, and the PFP ledger has a roughly 2–3% exergy/reference mismatch. The result ledger retains these diagnostics. An uncensored numerical KM peak can still carry the ideal-vapour pressure-domain warning.

No universal finite scalar maximum follows without an energy/inventory/geometric/observer constraint. Fix a participating mass to interpret an energy-based velocity ceiling; fix area, duration and receiver response to interpret impact pressure. The zero-radius incompressible singularity does not supply a physical endpoint.

## Rebuild from the included results

Opening the reader or PDF requires no development tools. For a document rebuild use Python 3.11 with the recorded versions in [requirements.txt](requirements.txt), Node.js 24 and TeX Live 2025 (or compatible installations). From this folder:

```powershell
python scripts/build_documents.py
```

This regenerates tables, figures, ledgers, this guide, static HTML mathematics and the PDF from the retained data. It does **not** rerun scientific sweeps. The helper compiles at least three times, then continues until the reference/contents state is unchanged and no rerun diagnostic remains (at most six passes). Rebuilding the final PDF/HTML changes their audit hashes; repeat their visual/browser verification before representing a rebuilt version as audited.

Individual steps are:

```powershell
python scripts/make_tables.py
python scripts/prepare_ledgers.py
python scripts/verify_ledgers.py
python scripts/write_readme.py
python scripts/build_reader.py
New-Item -ItemType Directory -Force build | Out-Null
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build EXPERT_REPORT.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build EXPERT_REPORT.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build EXPERT_REPORT.tex
Copy-Item -LiteralPath build/EXPERT_REPORT.pdf -Destination output/EXPERT_REPORT.pdf
```

For the individual commands, continue TeX passes until the references/contents settle; the helper performs that check automatically. `prepare_ledgers.py --copy-context` is an original-workspace import option; default rebuilding uses only included files. Do not use that import option in a relocated copy.

## Optional full scientific reproduction

The completed science is retained, so these commands are optional and expensive. Use script files rather than stdin for Windows multiprocessing. Drivers limit BLAS to one thread. Preserve checkpoint results and logs; numerical screening is not a physical peak.

```powershell
python scripts/pfc_thermo.py
python scripts/receiver.py
python scripts/gel_rupture.py
python scripts/km_sweep.py sweep
python scripts/km_sweep.py convergence
python scripts/verify_km_energy.py
python scripts/verify_psrc.py
python scripts/bim_runs.py validate
python scripts/bim_runs.py validate_jet
python scripts/bim_runs.py pfc
python scripts/verify_bim.py
python -u scripts/bim_runs.py pfc_converge 12
python -u scripts/bim_runs.py pfc_converge_stabilize 4
python -u scripts/bim_runs.py pfc_converge_extra 2
python -u scripts/km_sweep.py refine 6
python scripts/analyze_convergence.py
python scripts/build_documents.py
```

The refinement drivers skip recorded checkpoint cases, including retained numerical aborts. See [convergence work notes](verification/convergence_work.md) for the original and resume logs. A full original sweep would replace its output file; run it in a separate copy if the accepted evidence must be retained byte for byte.

## Files and provenance

| Location | Contents |
|---|---|
| `EXPERT_REPORT.tex`, `tex/` | Complete LaTeX derivations, audit, assumptions, glossary, references and experimental program. |
| `output/EXPERT_REPORT.pdf` | Final readable report; current hash/page audit in `verification/pdf_visual_audit.json`. |
| `READER.html`, `assets/` | Portable reader; local KaTeX, fonts and figure assets. |
| `PARAMETER_LEDGER.json`, `RESULTS_LEDGER.json` | Parameter status, provenance, validity and result claim tiers. |
| `data/` | Original thermodynamic, spherical and jet results plus requested BIM refinements. |
| `generated/`, `figures/` | Reproducible numbers, tables and plots; do not hand-edit generated LaTeX. |
| `scripts/` | Scientific solvers, verification drivers and document/package generators. |
| `verification/` | Numerical checks, final PDF/browser audits, relocation/release checks and run/work logs. |
| `sources/context/` | Byte-identical copies of ten selected prior project evidence files, with provenance. |
| `sources/literature/PROVENANCE.json` | Original scholarly links, access date, hashes, uses and redistribution decisions. |
| `THIRD_PARTY_NOTICES.md` | Reuter CC BY 4.0 and KaTeX MIT attribution; other cached full texts excluded from ZIP. |
| `NEXT_AGENT_HANDOFF.md`, `WORK_LOG.md` | Historical assignment/checkpoints and completion log. Latest log/audits supersede historical draft claims. |

The prior COMSOL/native files and complete parent packages remain in their original project; they are not duplicated as if reproduced here. The selected context copies support the report's audit. A prior review contained in those copied files reviews that prior work, not this expert report.

Create the licensing-aware archive with `python scripts/delivery.py zip`. `python scripts/delivery.py relocate` extracts and rebuilds it inside task-owned `build/relocation/`. Real-browser verification of that extracted reader is recorded separately, then `python scripts/delivery.py audit` checks release acceptance and writes a hash manifest. Regenerate the ZIP after final audits/log changes. Build folders, previews, caches, old draft PDFs and excluded scholarly full texts are omitted from the archive; provenance retains their source links.

No Git commit was made and existing history was preserved. The report and reader are research deliverables, not experimental confirmation of the actual device maximum.
