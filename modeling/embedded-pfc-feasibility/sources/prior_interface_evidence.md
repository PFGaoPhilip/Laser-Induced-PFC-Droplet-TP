> Archived prior interface research. PDF links adapted to the copies beside this file; provenance is in `prior_interface_provenance.json`.

# PFP/PFH capillarity and nanoscale optical-onset follow-up

2026-10-08. Source research for the two-theories 3D assignment. PDF page numbers below are one-based. The public edition links to the original scholarly sources below; the JSON preserves source states, original hashes and scientific limitations.

## Decisive input

A measured room-temperature reference exists for PFP: **9.41 mN/m = 0.00941 N/m**, from Kandadai's author dissertation, printed p. 116 / PDF p. 130, Table 5.2. The measurement is a 99%-pure liquid-PFP pendant drop against **saturated air**, at **24 ± 1 °C**, with images taken 4–5 s after formation (printed pp. 113–114 / PDF pp. 127–128). The table gives an average standard deviation of 1 mN/m across its measurements, without a PFP-specific error bar. This is a liquid–gas surface measurement; it does not establish a pure-vapor, high-temperature, nanoscale or gel interface law. The same research appears in Langmuir DOI 10.1021/la100307r.

A defensible declared room-temperature control uses this value for an **internal PFP vapor/PFP liquid interface**, and a distinct outer liquid–liquid value. Keeping it constant at elevated temperatures remains an approximation. A proposed 8–14 mN/m sensitivity bracket is a modeling choice, not a measured confidence interval.

## Which interface is measured?

| Source and location | Actual interface/state | Value | Applicability |
|---|---|---:|---|
| K2010, PDF pp. 131/133, printed pp. 117/119, Table 5.3 | Liquid PFP / distilled water, 24 ± 1 °C | 54 mN/m | Uncoated outer liquid–liquid reference |
| K2010, same table | Liquid PFP / 0.15 M PBS | 49 mN/m | Distinct aqueous chemistry |
| Z2019, PDF pp. 5/11, manuscript pp. 4/10 | First water/PFP/Krytox emulsion / liposome dispersion, room temperature | 1.14 ± 0.25 mN/m | Particular double-emulsion coating; n=3 |
| Z2019, same locations | Same preparation using PFH | 1.59 ± 0.16 mN/m | PFH formulation, not PFP |
| R2023, PDF pp. 7/21/22, Table 2 | Liquid PFH / gaseous PFH, no surfactant, 20 °C | 12 ± 2 mN/m | Internal liquid–gas interface in source notation |
| R2023, Table 2 | Liquid PFH / water, Krytox; F8–TAC13 | 18 ± 2; 25 ± 2 mN/m | Two outer liquid–liquid compositions |
| R2023, Table 2 | Gaseous PFH / water, Krytox; F8–TAC13; none | 66 ± 2; 38 ± 2; 72 ± 2 mN/m | Gas–aqueous boundary; no gel measurement |

Z2019 measures a macroscopic 0.5 µL pendant drop of the first emulsion in aqueous liposome dispersion. Its nanoscale objects are 300–500 nm **in diameter**, with DPPC:DSPE-PEG5K:stearylamine at 50:15:35 molar ratio, Krytox, and 10 × 59 nm gold nanorods. These low tensions do not describe a naked PFP core or the surface stress of the expanded gas shell. They cannot be assigned automatically to a different lipid/Epolight formulation.

R2023 independently measures its interface tensions by equilibrium macroscopic pendant/spinning drop or bubble shape fits. Its nucleation derivation uses **γ_gl for the internal vapor nucleus**, a different **γ_lc for initial droplet Laplace pressure**, and an interface-dependent heterogeneous nucleation model (PDF pp. 31–33 onward). Its homogeneous model fails to match the measured acoustic thresholds. Hence using a single host-water tension for every stage does not reproduce what the paper models. None of these measurements identifies the effective PAAm/gas surface stress.

For the proposed core-shell control, label the inner and outer surface energies separately. A measured outer PFP/aqueous tension is relevant while a liquid PFP shell remains. After its disappearance, the resulting aqueous-gel/gas boundary and any redistributed coating require a separate assumption or measurement. The earlier σ_eff = 0.072 N/m case can remain a stated aqueous-cavity sensitivity case; its fold is conditional on that interface choice.

## Optical onset near 300 nm

| Source | Measured preparation and exposure | What it constrains |
|---|---|---|
| Z2023, PDF pp. 3–6/12, Fig. 6 | Initial PFP z-average **diameter 309.0 nm**, lipid DSPE-PEG2000:DSPC 9:1 by mass, Epolight 3072; embedded in PAAm at **0 °C**; **1064 nm, 5 ns**, 10 Hz | Population transient-US threshold roughly **18–19.2 mJ/cm²** across conditioned cycles; Fig. 6B mean visually ~18.6 mJ/cm², approximate graph reading |
| H2014, PDF pp. 6/8 | PFP with fluorinated AuNR and Zonyl FSO, population **200–800 nm diameter**, PAAm at **37 °C**, 1064 nm | **4 mJ/cm²** minimum for detectable population US increase; largest droplets activate first; no pulse width specified |
| S2011, PDF pp. 4/5/10 | PFP/PbS, **2–7 µm diameter**, 36 °C; **1064 nm, 700 ps** | Measured loaded-solution absorption **207 / 431 m⁻¹**; lowest observed onset **1.8 / 1.4 J/cm²**, for low/high loading |

Z2023 measures incident output fluence at the optical fiber bundles, then initially gives 10 pulses at 75 mJ/cm² to precondition the droplets. Its threshold is obtained from a sigmoid fitted to population differential-US intensity during repeated three-pulse fluence ramps. Core comparisons were cooled to 0 °C to permit PFP recondensation. Preconditioning changes particle size and concentration. Therefore this is relevant nanoscale evidence, but cannot be read as an exact single, unconditioned 300 nm PFP inclusion threshold at 293 or 310 K. Its PAAm modulus is reported as 100 ± 3.11 kPa (p. 11); this is not the G = 10 kPa illustrative material.

H2014's population onset similarly cannot identify a 300 nm size quantile. S2011's absorption coefficients are measurements for **PbS-loaded solutions**, rather than pure PFP, gold nanorods or dye-loaded lipid droplets. Z2019 supplies an individual-AuNR heat model and successful multi-pulse activation with 800 nm, 100 fs, 80 MHz irradiation (PFP at 52 mW average power, pp. 8/14), but does not measure total absorbed energy in a current model inclusion. None supplies the necessary absorber count and cross section for the user's current inclusion.

## Geometry and energy bookkeeping

If **radius a₀ = 300 nm**, the Laplace jumps 2σ/a₀ are 62.7 kPa for the 9.41 mN/m PFP liquid–gas reference, 360 kPa for 54 mN/m PFP/water, 7.60 kPa for the 1.14 mN/m coated liquid–liquid preparation, and 480 kPa for a 72 mN/m aqueous gas interface. For **diameter 300 nm**, each jump doubles. These are calculations for their respective interfaces, not additive pressures at a common boundary.

At 18.6 mJ/cm², Fπa₀² is 52.6 pJ for radius 300 nm and 13.1 pJ for diameter 300 nm. At 4 mJ/cm² the corresponding values are 11.3 and 2.83 pJ. These quantities are **incident fluence over a geometric projected disk**. They are neither measured absorbed energy nor mechanical bubble energy; plasmonic cross sections, particle count, thermal exchange and shell loading have not been determined. No absorption coefficient, absorption fraction or laser-to-bubble efficiency has been fitted from these numbers.

## Explicit unknowns

- The current model's 300 nm dimension must be declared as radius or diameter; the cited nanodroplet sizes are diameters.
- PFP liquid–vapor tension versus temperature at the computed phase-equilibrium states, and nanometre nucleus curvature corrections.
- Actual inclusion coating and absorber loading; absorption cross section, local fluence and heat transfer at that inclusion.
- Heterogeneous nucleation sites/contact angle and unconditioned single-inclusion onset at the chosen temperature.
- Effective post-expansion gel/gas stress and shell redistribution, dilation or rupture. Neither bulk gel modulus nor the outer droplet tension measures these.

No material-specific activation or gel-failure conclusion follows from these sources alone.

## Source bundle

- **K2010:** [Rheology and interfacial tension of biopolymers](https://collections.lib.utah.edu/dl_files/40/6e/406e61ce35554485df3ea659a68ff430277482b7.pdf); [DOI/source](https://collections.lib.utah.edu/dl_files/40/6e/406e61ce35554485df3ea659a68ff430277482b7.pdf).
- **R2023:** [Acoustic Droplet Vaporization of Perfluorohexane Emulsions Induced by Heterogeneous Nucleation at an Ultrasonic Frequency of 1.1 MHz](https://doi.org/10.1021/acs.langmuir.3c02272); [DOI/source](https://doi.org/10.1021/acs.langmuir.3c02272).
- **Z2019:** [Phase-Transition Temperature of Gold-Nanorod-Coated Nanodroplets to Microbubbles by Pulsed Laser](https://doi.org/10.1021/acs.jpca.9b02566); [DOI/source](https://doi.org/10.1021/acs.jpca.9b02566).
- **Z2023:** [Factors Influencing the Repeated Transient Optical Droplet Vaporization Threshold and Lifetimes of Phase Change, Perfluorocarbon Nanodroplets](https://doi.org/10.3390/nano13152238); [DOI/source](https://doi.org/10.3390/nano13152238).
- **H2014:** [Photoacoustic and ultrasound imaging using dual contrast perfluorocarbon nanodroplets triggered by laser](https://doi.org/10.1364/BOE.5.003042); [DOI/source](https://doi.org/10.1364/BOE.5.003042).
- **S2011:** [Vaporization of perfluorocarbon droplets using optical irradiation](https://doi.org/10.1364/BOE.2.001432); [DOI/source](https://doi.org/10.1364/BOE.2.001432).
