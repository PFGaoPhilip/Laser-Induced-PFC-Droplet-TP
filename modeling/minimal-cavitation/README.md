# Two minimal laser-cavitation models

Start with the [53-step COMSOL walkthrough](STEP_BY_STEP.html) to build both models from a blank model. It includes click paths, complete input tables, checkpoints, solver settings, stopping rules, plots, output evaluations, expected results and troubleshooting. The [Markdown version](STEP_BY_STEP.md) is also included. Its format follows the requested [M1 lesson](https://pfgaophilip.github.io/cavitation-course/comsol/lessons/M1.html).

Open [index.html](index.html) for the offline report, plots and complete derivation. Both HTML readers show one complete language at a time, with **Chinese as the default**. The **English / 中文** button sits above the **day/night** button in a fixed stack at the lower right. Language and theme are remembered across both pages. The guide's 53-step progress and open theory section survive switching. Technical terms retain the newer reference site's multicolor palette in both themes and languages.

The complete [Chinese guide](STEP_BY_STEP.zh.md), [Chinese theory](MODEL_SPEC.zh.md) and [Chinese results](RESULTS.zh.md) are included, together with Chinese figure labels. COMSOL menu paths, executable entries, symbols and units retain their original spelling. All reader scripts, styles, images and math fonts are local: keep this entire folder together when moving or forwarding it.

The models follow the finite-energy and mechanism distinctions in the [new theory](https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/). They retain only scalar source, liquid-outlet and hydrogel mechanics needed for the two questions. A single nominal 10 ns pulse is represented by a post-activation initial state. Optical activation, periodic forcing, vibration studies and spatial wave fields are absent.

| Native file | Question and retained mechanics |
|---|---|
| [Model A](models/Model_A_Finite_Energy_Pressure_Jet.mph) | Conditional source pressure and first-ejection outlet speed: finite source work, liquid inertance, outgoing kinetic head, meniscus resistance and optional outlet loss. |
| [Model B](models/Model_B_Hydrogel_Confinement_Jet_Transmission.mph) | Confinement pressure/force and actual emitted output: Model A plus two gel-wall states, elastic work and viscous loss; an open-channel case and a sealed control. |

Each saved MPH opens in COMSOL 6.4 with its solution, result table and time-history plots. A has five scalar states; B has seven. Each uses one Global Equations interface and a transient study; no spatial mesh is required. The previous two models were preserved.

The largest speed in the declared sampled family is **25.28 m/s**, at **5 nJ of available source work** and a **3 µm outlet radius**. That case has **512.21 kPa source overpressure** and **319.53 kPa outlet dynamic pressure**. These are defined conditional outputs, not a universal cavitation maximum or an impact-pressure prediction.

For the matched 2 nJ, 5 µm-outlet baseline, the rigid and open-gel peak speeds are **15.376 and 1.625 m/s**. The gel's maximum elastic resistance is **9.143 kPa**, with **33.77 µN** axial resultant on one hemisphere. Open-gel transmission is **10.57% in peak speed**, **0.00980% in emitted energy**, and **0.08731% in emitted impulse**. The sealed control emits zero liquid. See [RESULTS.md](RESULTS.md) for definitions and interpretation.

## Inputs and parameter changes

The native default is a 15 µm gas pocket in a 30 µm chamber, with 50 µm effective liquid inertance length. The connected initial chamber-liquid inventory sets the discharge budget independently of that length. The illustrative carrier density is 1000 kg/m³, ambient pressure 100 kPa and surface tension 0.072 N/m. Model B uses shear modulus 20 kPa and effective Kelvin–Voigt viscosity 0.010 Pa s.

In **Global Definitions → Parameters**, edit `a`, `L`, `Rg0`, `Rc0`, `p0`, `G`, `etaG`, `Rloss` or `Kloss`, then rerun the transient study. `outletOpen=1` selects an existing liquid channel; `outletOpen=0` selects the sealed control. `p0` is **absolute** initial source pressure. `E0` is calculated from that pressure and source volume; it is not an independently imposed pressure pulse. Changing `tauLaser` alone does not change the solution because activation has been replaced by initial data.

For a comparison at fixed available work, calculate `p0` from the adiabatic work relation in [MODEL_SPEC.md](MODEL_SPEC.md), Step 2. The Java builder's `pressureFor` and Python reference's `source_pressure` perform that inversion. The supplied Java family holds the source radius and ambient pressure fixed; update its corresponding constants together with parameters if changing those controls. The Python `Case` stores the inputs explicitly.

Interpret only the complete first outward ejection, terminated at zero outward speed, liquid-inventory exhaustion, 20% wall stretch or Mach 0.1. The stretch threshold is a declared screen, not measured rupture. Require the pressure-communication diagnostic to stay below 0.1 before using the uniform-pressure approximation. Recheck conservation and these screens after any parameter change.

## Rebuild and verification

The existing saved models and report need no rebuild. For reproducible development, use Windows PowerShell and an installed COMSOL 6.4 license:

```powershell
.\Run-Rebuild.ps1
.\Run-Verify.ps1
.\Run-CheckGuide.ps1
python -m pip install -r requirements.txt
python scripts/reference.py
python scripts/verify_results.py
python scripts/make_delivery.py
python scripts/build_guide.py
python scripts/verify_bilingual.py
python scripts/check_portability.py
```

The rebuild and verification runners accept `-ComsolBin` for another COMSOL binary directory. They resolve the current folder and substitute it into the Java templates, so the source files can be moved. Rebuilding replaces this folder's generated MPH and CSV files. `Run-Verify.ps1` reloads the two baselines in a fresh process, reruns them and saves the final 1 ns baselines after a 2 ns comparison. `make_delivery.py` also requires Node.js for offline mathematical prerendering; it uses the included KaTeX assets when they already exist. Regenerating Chinese plots requires an installed CJK font (Microsoft YaHei or a supported fallback); opening the delivered PNG/SVG figures requires no plotting software.

`Run-CheckGuide.ps1` accepts the same `-ComsolBin` option. It imports the guide's parameter/variable files and converts A to B in memory without rewriting either accepted MPH. The conversion reproduces B's 1.62538458 m/s peak, seven states and energy residual below `1e-6`; see [the native check record](verification/GUIDE_NATIVE_IMPORT_CHECK.txt). `build_guide.py` extracts all input tables from the accepted MPH files and regenerates the 53-step HTML/Markdown guide. A Desktop click-through is not claimed.

The independent dimensional reference uses SciPy DOP853; COMSOL uses its BDF solver. [NUMERICAL_AUDIT.json](verification/NUMERICAL_AUDIT.json) records all 17 accepted cases, conservation, waveform comparisons, fresh-process checks, temporal checks and symbolic identities. The maximum normalized energy residual is 1.26e-7. Numerical checks and self-audit are distinguished from independent expert review.

The bilingual delivery was extracted into another folder and both readers regenerated with the included assets. Each language retains all 53 guide cards and 29 displayed theory equations; all 257 source math expressions, numbers and executable entries match across translations. The two accepted MPH hashes and all nine GUI input/reference files remain unchanged. [BILINGUAL_CONTENT_AUDIT.json](verification/BILINGUAL_CONTENT_AUDIT.json), [BILINGUAL_RELOCATION_AUDIT.json](verification/BILINGUAL_RELOCATION_AUDIT.json) and [PORTABILITY_AUDIT.json](verification/PORTABILITY_AUDIT.json) record those checks. Earlier native reload/import records remain applicable to the unchanged MPH and GUI inputs: [MOVED_NATIVE_RELOAD.txt](verification/MOVED_NATIVE_RELOAD.txt), [GUIDE_RELOCATION_AUDIT.json](verification/GUIDE_RELOCATION_AUDIT.json) and [GUIDE_MOVED_IMPORT_CHECK.txt](verification/GUIDE_MOVED_IMPORT_CHECK.txt).

The language/theme buttons, progress synchronization/persistence, deep links, disclosure state and copy fallback passed [DOM interaction tests](verification/READER_DOM_AUDIT.json). These tests use JSDOM with explicit layout/clipboard stubs, and do not claim browser rendering. Browser control was unavailable in this session; Chinese scientific plots and schematic image renders were inspected directly. To rerun the optional development test, install JSDOM under `build/dom-test` using `npm install --prefix build/dom-test --no-package-lock --ignore-scripts jsdom@30.1.2`, then run `node scripts/test_reader_dom.cjs`. The readers themselves need no npm installation. Run `python scripts/package.py` to recreate the delivery ZIP; test dependencies and build/tmp/cache/practice folders are excluded.

## Files and physical scope

- [MODEL_SPEC.md](MODEL_SPEC.md), [MODEL_SPEC.zh.md](MODEL_SPEC.zh.md) and [THEORY_DERIVATION.tex](THEORY_DERIVATION.tex): complete worked derivation with assumptions, local symbol definitions, checks and validity limits. The editable English TeX source targets LuaLaTeX.
- `data/`: native and independent histories, explicit case inputs and the case register. `assets/`: four scientific PNG/SVG plot pairs in each language, localized guide schematics, reader styling, language/theme code and local math fonts.
- `resources/gui/`: headerless, two-column parameter/variable imports plus headed equation/evaluation/stopping-rule references. `practice/` is reserved for your own builds and is excluded from the delivery ZIP.
- `sources/reference-lesson/`: the requested M1 source and readable copy, parameter-import example, URL and SHA-256 provenance. `sources/native-guide-evidence/` records the current models' extracted tables/settings.
- `sources/interface-reference/`: local copies of both requested reference sites and their interface/term styles, with URL/SHA-256 provenance. `sources/i18n/`: chapter translation sources, terminology glossary and cross-review records.
- `sources/theory/published-course-source.txt`: copied theory source, with URL and SHA-256 in `provenance.json`. `sources/prior-models/`: copied documentation and metadata of the previous pair. These copies were saved inside this project for traceability.
- [WORK_LOG.md](WORK_LOG.md): decisions, corrections and acceptance record. Historical preliminary values in the log are superseded by the final results.

The source is a finite closed adiabatic **ideal-gas control**, not a calibrated PFC phase/EOS model. This architecture predicts expansion-driven discharge through a pre-existing liquid channel. PFC phase inventory, laser conversion, real gel rate properties and outlet geometry still need experimental calibration. Internal collapse jets, gel rupture, planar-layer mechanics, jet breakup and target impact pressure are outside these two minimal models. The model does not establish a highest pressure or velocity without specifying source work, source volume and geometry.
