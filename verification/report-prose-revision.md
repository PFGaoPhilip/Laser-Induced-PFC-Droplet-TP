# Resolver and minimal-model reader revision

Date: 2026-10-14.

The resolver reader is `learning-records/resolver-progress/index.html`.
Its source is `scripts/build_resolver_lesson.py`.
The minimal-model readers are `modeling/minimal-cavitation/index.html` and `STEP_BY_STEP.html`.
Their source files remain inside the model folder.

## Reader changes

- Rewrote eleven resolver sections in English and Chinese.
- Added the Chapter 3 return link.
- Preserved the exact three stage status identifiers.
- Preserved all seven Stage2 waivers and eighteen null objectives.
- Retained the candidate030 endpoint and candidate028 metadata qualification.
- Preserved publication status `HELD_NOT_PUBLISHED`.
- Added explicit positivity conditions beside resolver energy bounds.
- Defined dimensionless identity and circle constants beside their formulas.
- Restored the registered directed-speed selection `w=-u_z=-u.x`.
- Preserved the partial-cell reconstruction caveat and null outputs.
- Rewrote forty-four theory paragraphs in both minimal-model editions.
- Rewrote results, introduction, model navigation and README prose.
- Shortened scientific figure titles in both languages.
- Shortened GUI instructions across the complete guide.
- Retained every operational step, equation and input table.
- Added Appendix A return navigation to both minimal-model readers.
- Set English as the minimal readers' default language.
- Preserved language, theme, deep-link and guide-progress controls.

The minimal-model return link uses the local Appendix A inside the course.
The standalone model folder retains an optional published Appendix A link.
The reader builder now uses the bundled term palette.
It no longer requires excluded website-reference snapshots.
Reader navigation no longer requires a nested copy of its own ZIP.
Model files and GUI inputs remain linked directly.

## Checks performed

Resolver structure and local links passed.
All 284 protected copied-input hashes passed.
All nine resolver formula sources remain present.
The analytical examples passed.
Their illustrative speed is 84.10441740067199 m/s.
Equal-impedance and rigid contact estimates are 63.07831305050399 and 126.15662610100799 MPa.
These remain conditional examples.

Minimal-model bilingual token checks passed.
Both theory editions retain 257 mathematical expressions and 29 displayed blocks.
Both guide editions retain 53 steps and 679 code entries.
Ordered mathematical, code and numerical tokens match the pre-revision local ZIP.
CRLF and LF line endings are treated as equivalent.
Recorded local symbol declarations are preserved.
All 49 native-model, data and GUI files match baseline hashes.
KaTeX prerendering completed without errors.
All reader dependencies and local links passed static portability checks.
All sixteen updated DOM interaction scenarios passed.
These cover language, theme, progress, copying, deep links and return navigation.
Explicit dark-theme queries override stored light mode.
DOM layout and clipboard tests use stated stubs.
They make no real-browser rendering claim.
Four updated scientific plot layouts were visually inspected.
The updated model ZIP passed its integrity check.
The standalone ZIP was extracted into a new temporary folder.
Both readers regenerated there from bundled sources and assets.
Bilingual, preservation and portability checks passed in that moved folder.
`READER_RELOCATION_REVISION_AUDIT.json` records the current relocation check.

Current records are `resolver-reader-prose-audit.json`,
`modeling/minimal-cavitation/verification/READER_PROSE_AUDIT.json`,
`BILINGUAL_CONTENT_AUDIT.json` and `PORTABILITY_AUDIT.json`.
The original `SOURCE_MANIFEST.json` remains unchanged.
`READER_REVISION_MANIFEST.json` records the revised exportable folder.
All final folder and ZIP revision hashes passed.
Historical acceptance and translation-review records remain unchanged.

The resolver verifier now reports checks it actually performs.
It accepts an optional relocated-folder argument.
It no longer relies on a stale temporary directory.
It no longer hardcodes browser success.
The historical resolver `LESSON_QA.json` remains unchanged.

## Limits and integration

This revision adds no simulation or experimental result.
It preserves the existing scientific verdicts.
New independent expert review was not performed.
Token comparisons establish preservation, rather than proving the derivation.
The parent agent owns current real-browser and whole-course relocation checks.
The parent also owns homepage removal and Chapter 3/Appendix A placement.
Frozen Stage3 readers, reports, receipts and logs were preserved.
Task edit scripts, extraction copies, DOM dependencies and Python caches were removed.

The invoked teaching skill guides the reader structure.
Reader creation changes no learner-mastery record.
The invoked Math-Rigor skill guides assumptions, symbol declarations and audit scope.

## Unified frontend update

The resolver, report and guide now use the first chapter's frontend.
Each has `topbar`, `page-layout`, `sidebar`, `reading`, `chapter-header`,
`chapter-body` and `site-footer` wrappers.
Canonical `course.css` supplies fonts, headings, tables, code and math styles.
Bundled copies match the final root stylesheet hashes.
The report and guide also bundle the final bilingual term stylesheet.
Supplemental CSS supplies guide interactions without overriding canonical typography.

All switching controls use one fixed lower-right `theme-tools` group.
Theme precedes language, matching the first chapter.
Canonical `theme-toggle` and `language-toggle` IDs are used.
The model readers use the common `dark` and `light` theme names.
They retain guide progress, disclosure state, copying and deep links.
Navigation titles come from the current `COURSE_SETTINGS.json`.
Standalone regeneration uses bundled navigation and frontend assets.

The resolver uses final root theme/language scripts.
Their toolbar creation race is fixed in the common source.
The Stage3 frozen reader remains byte-identical.
Its teaching-page link is now a bilingual source download.
The link uses `download="STAGE3_FROZEN_READER_SOURCE.html"`.

Parent Chrome verification passed all fourteen active readers.
It compared desktop and mobile typography with Chapter 1.
It checked both switches, toolbar position, width and math rendering.
No external rendering resources were requested.
The independent browser record is `unified-frontend-browser-audit.json`.
This agent's browser tool could not share the parent's running profile.
The parent performed the real-browser checks without disrupting that session.

Protected formula, code, numeric and native-data checks passed after rebuilding.
Static reader links and canonical asset hashes passed.
The updated standalone ZIP is rebuilt from these canonical readers.
