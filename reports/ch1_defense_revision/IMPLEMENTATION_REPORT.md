# Chapter 1 defense revision — 2026-10-19

## Executive outcome

Chapter 1 was rewritten from the supplied failed-defense handoff.
All 33 surviving equation columns contain multiple derivation lines.
Each includes paired English/Chinese premises, definitions, intermediate mathematics and checks.
The original defense verdict and saved learner records remain unchanged.

## Changed files

- `content/chapter01.py` and `content/chapter01_steps.py`: complete derivation expansions and readable final relations.
- `content/equation_symbol_rows.json`: collision-safe numbering migration and deletion of old E12 metadata.
- `chapters/01-cavity-pressure-inertia-and-directional-jets.html`, its editable Markdown and aggregate `text/course.md`: rebuilt bilingual reader.
- `assets/figures/` and `assets/figures-editable/c1-c2/`: migrated equation identifiers, preserved native geometry, updated gallery and 33-slide Chapter 1 deck.
- Current generators and checks: migrated semantic references and figure counts.
- `verification/chapter01-revision-20261019.json`: separate authorized amendment; original lesson baseline remains intact.

## Old→new equation mapping

See `EQUATION_MAP.csv`.
Old E01–E11 retain their numbers.
Old E12 was deleted.
Old E13–E34 become E12–E33.
No backward aliases duplicate the new anchors.
External old-version bookmarks require migration.
Historical source attachments, learner records and dated evidence retain their original labels.

## Examiner challenge resolution

See `EXAMINER_RESOLUTION.md` for all D01–D12 dispositions.
The deleted tensor-component dissipation exposition is absent from Chapter 1.
The mechanical loss term in E11 remains derived.
General interface strain stress remains necessary in E27.

## Verification evidence

The numerical checker reproduces collapse, kinetic energy, viscous power, potential derivatives, Mach cutoff and column impulse values.
The independent source reviewer reproduced representative chains and reviewed every group.
All six review findings were repaired.
`VERIFICATION_REPORT.json` records the 33 multiline groups and preserved non-Chapter-1 equations.
The original numerical examples are illustrative inputs, without experimental claims.

## Frontend/language regression results

The established frontend styles, layout, theme controls and language controls are retained.
The bilingual highlighter recomputed term assignments within its existing color palette.
The base stylesheet and both control scripts are byte-identical to the frozen baseline.
Browser tests exercise desktop/mobile English/Chinese and light/dark views.
They check all equation anchors, image loading, math errors, page overflow, toggles and persistence.
Current rendered mathematical blocks are retained in the local `browser/` evidence folder.
The portable public export excludes private learner responses and user-supplied attachments.
Offline relocation is checked separately before release.

## Known limitations

See `UNRESOLVED_ISSUES.md`.
The source review was independent, but it was not blinded.
No new simulation, experimental validation, actual-device maximum or learner mastery is claimed.
Existing figure geometry is preserved; no new Office-rendered PPTX validation is claimed.

## How to run locally

Open `index.html` from the complete course folder.
Use the language and day/night buttons.
All reader assets and rendered mathematics are local.

Rebuild with `python -B scripts/build_course.py`.
Then run `python -B scripts/highlight_bilingual_terms.py`.
Run `scripts/verify_course.py`, `scripts/verify_language_labels.py`,
`scripts/verify_lesson_revision.py`, `scripts/verify_english_figures.py`,
`scripts/verify_chapter01_revision.py` and `verification/chapter01-check.py` with Python.
Browser verification uses `scripts/browser_chapter01_revision.py` with Playwright and installed Edge.
Source inspection and numerical checks do not require a new COMSOL model.

The owner explicitly authorized GitHub publication on 2026-10-19.
Publication receipts are recorded after the verified export is pushed.
