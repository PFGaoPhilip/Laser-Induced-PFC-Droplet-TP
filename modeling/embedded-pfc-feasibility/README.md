# Embedded PFC feasibility package

Open `index.html` directly from this folder. Equations, fonts, four scientific plots and the computed-state selector work offline; optional scholarly references lead to their original sites. Move or forward the entire folder, or extract the ZIP before opening it. The reader has a day/night toggle.

The comparison is in `REPORT.md`; the complete 32-equation worked derivation is in `DERIVATION.md`, editable `DERIVATION.tex`, and `output/pdf/FINITE_PFC_DERIVATION.pdf`. `IMPLEMENTATION_HANDOFF.md` specifies the additional spatial models and measured validation gates. `SOURCES.md` separates supported references from stipulated target parameters. Copied prior context and archived EOS coefficients are in `sources/`; scholarly papers are linked through their original sources. See [PUBLICATION.md](PUBLICATION.md) for public-package provenance.

The two `.mph` files in `models/` are native COMSOL 6.4 global-equation controls. Both contain inline analytic real-fluid EOS functions; neither requires the original project or Python to open. The stationary model is saved at PFP radius 0.3 µm, shear modulus 20 kPa, stretch 2.1. The transient is saved at the same liquid radius/modulus, viscosity 0.01 Pa s, a supplied post-nucleation seed at stretch 1.2 and 50 kPa excess liquid traction. It has no outlet, fracture, optical heat source or collapse-jet physics. Its energy parameter `Eseed` is retained seed energy relative to the all-liquid reference under lossless preparation, not a measured optical input.

`data/` contains 132 equilibrium states, 60 native stationary exports, six native/reference transient pairs, stability and budget comparisons, and the exact native inputs. `verification/` contains numerical comparison, reference-method refinement, native fresh-process reload/step refinement, equation-rendering, mathematical review, PDF and portability evidence. Native/reference agreement checks implementation of the same reduced model and constitutive EOS, not independent experimental truth.

Rebuild using Python 3 with the listed requirements, Node.js for static equation rendering, COMSOL 6.4 for native solves, and a LaTeX installation for the optional PDF. Dependency caches, build intermediates, operational logs and third-party paper PDFs are excluded from this public archive. The included scientific audit records describe the accepted source study; publication integrity has a separate audit.

```powershell
python -m pip install -r requirements.txt
python scripts/pfc_model.py
python scripts/audit_parameters.py
python scripts/prepare_native.py
.\Run-Native.ps1
python scripts/verify_results.py
.\Verify-Native.ps1
python scripts/build_comparison.py
python scripts/build_reader.py
New-Item -ItemType Directory -Path build -Force | Out-Null
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build DERIVATION.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build DERIVATION.tex
New-Item -ItemType Directory -Path output/pdf -Force | Out-Null
Copy-Item -LiteralPath build/DERIVATION.pdf -Destination output/pdf/FINITE_PFC_DERIVATION.pdf
```

The two PowerShell wrappers accept `-ComsolBin` for a different COMSOL binary directory. They create fresh compiled Java in `build/`; `Verify-Native.ps1` reruns loaded models in memory and never overwrites the saved `.mph` files. Scripts resolve their own project root, including after relocation. COMSOL version/license compatibility remains a normal native-software requirement.

Parameter comparisons use **initial liquid radius**, not gas seed radius. Reported new speeds are **radial wall speeds**. The stretch-2.1 screen is **stipulated, not a measured fracture limit**. The high-viscosity 0.3 µm-radius reference ends at a time window before its growth is complete. Fracture-work screens are hypothetical retained-energy allocations and never hard proofs of impossibility. Consult the measured/assumed ledger before using any control as a target prediction.
