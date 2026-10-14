# Embedded PFC feasibility package

Open `index.html`. Use the lower-right language button to cycle **English + 中文 → English → 中文**. The adjacent **Day mode / Night mode** button changes theme. The page uses the first chapter’s layout and typography. Equations, fonts, four plots and all 30 selector states work offline. Move the entire folder or extract its ZIP. Appendix A navigation uses a local link inside the full course. The standalone study uses an optional course URL.

`REPORT.md` gives the edited comparison. `DERIVATION.md` contains all 32 equations and their local definitions. `IMPLEMENTATION_HANDOFF.md` lists spatial models and measured validation gates. `SOURCES.md` records supported claims. Each document has a matching `.zh.md` source. The original accepted English PDF and its LaTeX remain in `output/pdf/FINITE_PFC_DERIVATION.pdf` and `DERIVATION.tex`.

The two native COMSOL 6.4 models contain inline real-fluid EOS functions. The stationary model is saved at PFP radius 0.3 µm, shear modulus 20 kPa and stretch 2.1. The transient adds viscosity 0.01 Pa s and a supplied seed at stretch 1.2. Its liquid pressure exceeds static host traction by 50 kPa. Retained seed energy uses the all-liquid reference. Optical absorption, seed formation, fracture, outlets and collapse jets need additional models.

`data/` contains the accepted 132 equilibria, 60 stationary exports and six transient comparisons. `verification/` contains numerical, mathematical, native-reload and publication records. Solver agreement checks the stated equations. Target experimental validation remains unresolved.

Rebuild the edited reader without rerunning simulations:

```powershell
python scripts/build_reader.py
```

Python, BeautifulSoup and Node.js are required. KaTeX is bundled. The reader build preserves the accepted PDF and LaTeX. `scripts/reader_text.py` contains the paired prose. `scripts/reader_figures.py` creates Chinese copies of the accepted plots. Plot curves and numerical payload remain unchanged.

Reproduce the original numerical study with the recorded dependencies:

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

The PowerShell wrappers accept `-ComsolBin` for another COMSOL installation. They compile into `build/`. Native reload checks preserve saved models. Scripts resolve their own study root after relocation.

The optional reader audit uses installed Chrome and Python `websockets`. Run `python scripts/audit_reader_revision.py` to check language modes, theme, tabs, selector states, viewport width and relocation. Its browser profile is temporary. The accepted numerical checks are preserved as source-study evidence.

Sizes describe **initial liquid radius or diameter**, as labelled. New speeds describe **radial wall motion**. Stretch 2.1 is a stipulated screen. The small high-viscosity case still grows at its time cutoff. Fracture costs use hypothetical slit geometry and assigned seed energy. Target activation, rupture and jet predictions remain unresolved.
