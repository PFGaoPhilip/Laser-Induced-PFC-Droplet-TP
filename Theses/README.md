# Theses management

The canonical literature register is `Theses.md` at the project root.
It sits alongside `WORK_LOG.md` and this `Theses/` directory.
Every paper also has an individual Markdown record here.
Entries use DOI or arXiv identifiers whenever available.

Open [index.html](index.html) for the offline searchable reader.
Use its day/night button, lesson filter, and evidence filter.
Read [CHAPTER_MAP.md](CHAPTER_MAP.md) for lesson placement and limits.

## After every paper search

1. Save every returned paper immediately.
2. Resolve the DOI, arXiv identifier, or stable source URL.
3. Record the title, authors, year, and search date.
4. Write two summary sentences.
5. Summarize background and theory in the first sentence.
6. Summarize experiments in the second sentence.
7. Mark unavailable experiment details explicitly.
8. Update the root `Theses.md` register.
9. Update `WORK_LOG.md` and remove disposable intermediates.

## Project commands

Run these commands from the lesson project root.

```powershell
python -B scripts/manage_theses.py search "precise paper question" --count 3
python -B scripts/manage_theses.py ingest-web path-to-search-results.txt
python -B scripts/refresh_theses_metadata.py
python -B scripts/normalize_theses.py
python -B scripts/build_theses.py
python -B scripts/verify_theses.py
```

Search and ingestion commands write records before returning.
They also synchronize `Theses.md` and append the work log.
Metadata refresh preserves authored summaries.
Reviewed summaries are maintained in `reviewed-summaries.json`.
Normalization preserves duplicate-source provenance in `identifier-aliases.json`.

## Evidence interpretation

E: a read primary source supports the stated summary.
I: an explicit inference from identified evidence.
?: methods or paper identity remain unverified.
Title-based summaries identify the topic without claiming verified experiments.
Peripheral search leads remain available for later review.
Book chapters, databases, proceedings collections, and citation fragments are labeled.

## Portability

The HTML reader embeds all styling, controls, and searchable records.
It requires no network access to display the archive.
Primary-source links require network access when opened.
The complete literature delivery includes `Theses.md`, `WORK_LOG.md`, and `Theses/`.
Forward that complete folder or its ZIP.
