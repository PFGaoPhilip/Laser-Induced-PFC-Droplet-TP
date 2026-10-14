# Chapter prose revision — 2026-10-14

## Scope

Revised `content/chapter01.py` through `content/chapter05.py`.
Chapter 5 supplies Appendix A.
Every explanatory paragraph, heading and note was rewritten bilingually.
The revision covers 259 English/Chinese blocks.
Chapter summaries, prerequisites and 15 question prompts were also revised.
English explanatory text decreased from 16,329 to 11,254 words.

## Editorial changes

- Split dense paragraphs into short, direct statements.
- Keep each derivation operation beside its equation.
- Replace repeated disclaimers with the specific unresolved result.
- Preserve source assumptions beside the affected calculations.
- Distinguish inventory states, radial motion, emission and interface release.
- Preserve experimental observations and their geometry-specific limits.
- Keep mastery criteria separate from demonstrated learning.

## Scientific audit

Compared authoring calls against the existing Git version.
All 168 equation calls remain exactly equal as Python ASTs.
This preserves LaTeX, local symbol definitions, units and numerical inputs.
It also preserves diagrams, captions, premise labels and citation calls.
All equation identifiers remain unique.
All 15 question identifiers remain unchanged.
Question rubrics and learning records remain unchanged.

A separate prose pass checked transitions and branch conditions.
It corrected ambiguous exponential-endpoint wording.
It also clarified bubble-count pair summation and constant-coefficient factoring.
No governing equation, constitutive assumption or numerical result was changed.
No new physical validation is claimed.

## Execution checks

All five sources compile and import successfully.
Each produces three defense questions with the expected identifiers.
Every emitted language-pair block contains English and Chinese.
The sources emit 168 equation sections in total.
Original CRLF conventions were preserved.
Whitespace checks pass with Git's `cr-at-eol` convention enabled.
Detailed counts are recorded in `chapter-prose-audit.json`.

## Coordination and cleanup

The parent owns navigation, report integration and generated HTML.
No generated page, shared asset or build script was edited here.
No frozen simulation evidence or learning record was changed.
This record serves as the subtask work log.
The temporary replacement script was removed after verification.
