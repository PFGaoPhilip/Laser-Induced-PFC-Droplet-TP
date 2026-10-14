# Finite-energy outlet discharge and gel confinement

Read [the report](index.html) for results and the worked derivation.
Use [the 53-step COMSOL guide](STEP_BY_STEP.html) to build both models.
The [English](STEP_BY_STEP.md) and [Chinese](STEP_BY_STEP.zh.md) guides are included.

Both readers provide English/Chinese and day/night buttons.
English is the default.
Language, theme and guide checks persist across pages.
Keep this folder together when moving or forwarding it.
Scripts, styles, figures and math fonts are bundled.
The Appendix A link opens the local course when available.
The standalone model folder uses the published Appendix A link.

| Model | Calculation |
|---|---|
| [A: rigid chamber](models/Model_A_Finite_Energy_Pressure_Jet.mph) | Finite source work, outlet inertia, meniscus resistance and emitted output. |
| [B: gel confinement](models/Model_B_Hydrogel_Confinement_Jet_Transmission.mph) | Model A plus gel motion, elastic storage and viscous loss. Includes open and sealed controls. |

The saved MPH files contain solutions, tables and time histories.
Open them in COMSOL 6.4.
Model A has five scalar states; Model B has seven.
Both use Global Equations and a transient study.
They require no spatial mesh.

These are initialized ideal-gas source controls.
The nominal 10 ns pulse supplies post-activation initial data.
An existing channel permits expansion-driven liquid discharge.
Optical heating, PFC phase conversion and collapse jets are excluded.
Gel rupture, planar-layer mechanics and target impact are excluded.
Material predictions require calibration.

The highest sampled speed is 25.28 m/s.
Its source work is 5 nJ; outlet radius is 3 µm.
Source overpressure is 512.21 kPa; outlet dynamic pressure is 319.53 kPa.
This maximum belongs to the declared sampled family.
A universal cavitation maximum is not established.

The matched baseline uses 2 nJ and a 5 µm outlet.
Rigid and open-gel peak speeds are 15.376 and 1.625 m/s.
Peak elastic resistance is 9.143 kPa.
One-hemisphere axial elastic force reaches 33.77 µN.
Speed transmission is 10.57%.
Emitted-energy transmission is 0.00980%; impulse transmission is 0.08731%.
The sealed control emits zero liquid.
Definitions and complete results appear in [RESULTS.md](RESULTS.md).

## Inputs and validity

Default gas radius is 15 µm; chamber radius is 30 µm.
Effective liquid inertance length is 50 µm.
Connected chamber liquid separately sets the finite discharge budget.
Carrier density is 1000 kg/m³.
Ambient pressure is 100 kPa; surface tension is 0.072 N/m.
Gel shear modulus is 20 kPa; viscosity is 0.010 Pa s.

Edit parameters in **Global Definitions → Parameters**.
`outletOpen=1` selects an existing channel.
`outletOpen=0` selects a sealed control.
`p0` is absolute initial pressure.
`E0` follows from pressure and volume.
Changing `tauLaser` alone leaves the solution unchanged.
It records the initialization assumption.

For fixed work, invert [MODEL_SPEC.md](MODEL_SPEC.md), Step 2.
Java `pressureFor` and Python `source_pressure` implement this inversion.
Update builder constants when changing source radius or ambient pressure.
Python `Case` stores each input explicitly.

Interpret the first outward ejection.
Stop at speed return, inventory exhaustion, 20% stretch or Mach 0.1.
The stretch threshold is a stipulated screen.
Measured fracture strain is missing.
Require pressure-communication ratio below 0.1 for uniform pressure.
Recheck conservation and validity after changing inputs.

## Rebuild and checks

The saved readers and models open without rebuilding.
The native rebuild requires licensed COMSOL 6.4.
PowerShell runners accept `-ComsolBin` for another executable directory.
Rebuilding replaces generated MPH and CSV files in this folder.

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
python scripts/package.py
```

`make_delivery.py` needs Node.js for local KaTeX prerendering.
Chinese plot regeneration needs a supported CJK font.
The supplied images need no plotting software to open.
`build_guide.py` extracts tables from the accepted MPH files.
`Run-CheckGuide.ps1` checks imports and A-to-B conversion in memory.
Its record appears in [GUIDE_NATIVE_IMPORT_CHECK.txt](verification/GUIDE_NATIVE_IMPORT_CHECK.txt).

The independent reference uses SciPy DOP853.
COMSOL uses BDF.
[NUMERICAL_AUDIT.json](verification/NUMERICAL_AUDIT.json) preserves the accepted 17-case checks.
Maximum normalized energy residual is 1.26e-7.
Reader changes preserve the native models and GUI expressions.
Current translation checks appear in [BILINGUAL_CONTENT_AUDIT.json](verification/BILINGUAL_CONTENT_AUDIT.json).
Structural portability checks appear in [PORTABILITY_AUDIT.json](verification/PORTABILITY_AUDIT.json).
Those static checks do not rerun COMSOL.
Browser checks are recorded separately.

## Editable sources and provenance

- [MODEL_SPEC.md](MODEL_SPEC.md) and [MODEL_SPEC.zh.md](MODEL_SPEC.zh.md) contain the derivation.
- [THEORY_DERIVATION.tex](THEORY_DERIVATION.tex) is editable English LaTeX for LuaLaTeX.
- `data/` contains histories, inputs and the accepted case register.
- `resources/gui/` contains parameter, variable, equation and evaluation tables.
- `sources/guide/` and `sources/i18n/` contain guide and translation sources.
- [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) preserves original copied-file hashes.
- [READER_REVISION_MANIFEST.json](READER_REVISION_MANIFEST.json) records revised reader hashes.
- [PUBLICATION.md](PUBLICATION.md) records the course copy and editorial scope.

Scientific evidence, model inputs and accepted numerical results remain unchanged.
Historical acceptance records retain their original wording.
