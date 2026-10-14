"""Inventory lesson citations and immediately archive scholarly search results.

Uses Crossref's public REST API. No credentials or PDF downloads.
Never rewrites authored summaries during metadata refreshes.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen
from urllib.parse import quote, urlencode
import argparse
import datetime
import html
import hashlib
import json
import os
import re
import time
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "Theses"
DATE = datetime.date.today().isoformat()
DOI = re.compile(r"10\.\d{4,9}/[A-Za-z0-9._;()/:+\-]+", re.I)
ARXIV = re.compile(r"https?://arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
EXCLUDE = {".git", "publication", "delivery", "Theses", "tmp", "temp", "assets",
           "node_modules", "__pycache__", "checkpoint_history", "skill-upgrades",
           "revision-guidance-20261014", "sessions", "basilisk", "runs", "execution", "data",
           "full_closure", "evidence", "verification", "inputs", "output", "accepted_control"}


def safe_name(identifier):
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", identifier).rstrip(". ") + ".md"


def clean_doi(value):
    value = value.rstrip(".,;:")
    value = value.removesuffix("Get")
    value = re.sub(r"/(?:full|pdf|abstract)$", "", value, flags=re.I)
    while value.endswith(")") and value.count(")") > value.count("("):
        value = value[:-1].rstrip(".,;:")
    return value


def save_json(name, data):
    ARCHIVE.mkdir(exist_ok=True)
    (ARCHIVE / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sync_register():
    """The owner's canonical format is one root-level Theses.md register."""
    paths = sorted(path for path in ARCHIVE.glob("*.md") if path.name.startswith(("10.", "arxiv_", "url_", "citation_fragment_")))
    lines = ["# Theses", "", "Search and metadata verification date: " + DATE + ".", "",
             "This register sits alongside WORK_LOG.md.",
             "Each entry includes title, authors, identifier, and two summary sentences.",
             "Unverified experimental details are explicitly marked.", "",
             "[Chapter evidence map](Theses/CHAPTER_MAP.md) · [Offline literature reader](Theses/index.html)", ""]
    for path in paths:
        content = path.read_text(encoding="utf-8")
        doi = re.search(r"^- DOI: (.+)$", content, re.M)
        identifier = doi.group(1) if doi and not doi.group(1).startswith("Unavailable") else path.stem.removeprefix("arxiv_")
        if identifier.startswith("url_"):
            url = re.search(r"^- Source URL: (.+)$", content, re.M)
            identifier = url.group(1) if url else identifier
        lines += ["## " + identifier, "", "Individual record: [" + path.name + "](Theses/" + quote(path.name, safe="._-") + ")", "",
                  re.sub(r"^# .+\n", "", content, count=1).replace("\n## ", "\n### ").strip(), ""]
    (ROOT / "Theses.md").write_text("\n".join(lines), encoding="utf-8")
    return len(paths)


def log_operation(message):
    path = ROOT / "WORK_LOG.md"
    content = path.read_text(encoding="utf-8") if path.exists() else "# Work log\n"
    path.write_text(content + "\n- " + DATE + " — " + message + "\n", encoding="utf-8")


def inventory():
    found = {}
    paths = []
    for directory, folders, files in os.walk(ROOT):
        folders[:] = [folder for folder in folders if folder not in EXCLUDE]
        paths.extend(Path(directory) / filename for filename in files)
    for path in paths:
        relative = path.relative_to(ROOT)
        if (EXCLUDE.intersection(relative.parts)
                or path.suffix.lower() not in {".md", ".html", ".bib", ".tex", ".py", ".json", ".txt"}
                or path.name == "Theses.md" or "theses" in path.name.lower() and path.suffix == ".py"):
            continue
        try:
            if not path.is_file() or path.stat().st_size > 8000000:
                continue
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for number, line in enumerate(content.splitlines(), 1):
            for match in DOI.finditer(line):
                identifier = clean_doi(match.group())
                key = identifier.lower()
                row = found.setdefault(key, {"identifier": identifier, "kind": "doi", "origins": []})
                location = f"{relative.as_posix()}:{number}"
                if location not in row["origins"]:
                    row["origins"].append(location)
            for match in ARXIV.finditer(line):
                key = "arxiv:" + match.group(1)
                row = found.setdefault(key, {"identifier": match.group(1), "kind": "arxiv", "origins": []})
                row["origins"].append(f"{relative.as_posix()}:{number}")
    save_json("existing-citation-inventory.json", {"date": DATE, "scope": "Project textual files; generated duplicates excluded", "records": list(found.values())})
    return list(found.values())


def fetch(url):
    for attempt in range(2):
        try:
            request = Request(url, headers={"User-Agent": "LessonLiteratureArchive/1.0 (scholarly metadata research)", "Accept": "application/json"})
            with urlopen(request, timeout=25) as response:
                return json.load(response)
        except Exception:
            if attempt == 1:
                raise
            time.sleep(1)


def metadata(item):
    authors = []
    for author in item.get("author", []):
        authors.append(" ".join(filter(None, [author.get("given"), author.get("family")])) or author.get("name", "Unverified author"))
    dates = [item.get(key, {}).get("date-parts", [[None]])[0][0]
             for key in ("published", "published-print", "published-online", "issued")]
    plain_title = html.unescape(re.sub(r"<[^>]+>", "", (item.get("title") or ["Title unverified"])[0]))
    plain_title = re.sub(r"\s+", " ", plain_title).strip()
    return {"title": plain_title,
            "authors": authors or ["Authors unverified"],
            "year": next((date for date in dates if date), "Unverified"),
            "doi": item.get("DOI", ""), "venue": (item.get("container-title") or [""])[0],
            "abstract": html.unescape(re.sub(r"<[^>]+>", " ", item.get("abstract", ""))).strip(),
            "type": item.get("type", ""),
            "source": "https://api.crossref.org/works/" + quote(item.get("DOI", ""), safe=""),
            "url": item.get("URL", "")}


def archive_record(row, meta=None, error=None, query=None):
    identifier = row["identifier"]
    filename_id = identifier if row["kind"] == "doi" else ("arxiv_" + identifier if row["kind"] == "arxiv" else "url_" + hashlib.sha256(identifier.encode()).hexdigest()[:16])
    path = ARCHIVE / safe_name(filename_id)
    if path.exists():
        return path.name
    meta = meta or {}
    url = "https://doi.org/" + identifier if row["kind"] == "doi" else ("https://arxiv.org/abs/" + identifier if row["kind"] == "arxiv" else identifier)
    content = ["# " + meta.get("title", "Unverified citation: " + identifier), "",
               "- Title: " + meta.get("title", "Unverified; identifier imported from project citations."),
               "- Authors: " + "; ".join(meta.get("authors", ["Unverified"])),
               "- Year: " + str(meta.get("year", "Unverified")),
               "- DOI: " + (identifier if row["kind"] == "doi" else "Unavailable; see stable source identifier"),
               "- arXiv ID/URL: " + (url if row["kind"] == "arxiv" else "Not yet checked"),
               "- Source URL: " + url,
               "- Date searched: " + DATE,
               "- Record origin: " + ("New search" if query else "Existing project citation"),
               "- Evidence level: " + ("Metadata verified; scientific summary pending review" if meta else "Unverified imported lead"),
               "- Access status: Metadata only; full-text access not yet checked.",
               "- Lesson mapping: Pending evidence review.", "", "## Two-sentence summary", "",
               ("This work addresses " + meta["title"].rstrip(".") + "." if meta.get("title") else "Background and theory remain unverified pending a readable primary source."),
               "Experiments performed remain unverified pending methods or explicit abstract evidence.", "", "## Provenance", ""]
    if meta and meta.get("source"):
        content.extend(["Canonical metadata: " + meta["source"], "", "Venue: " + meta.get("venue", ""), ""])
    if query:
        content.extend(["Search query: " + query, ""])
    if error:
        content.extend(["Metadata resolution failure: " + str(error), ""])
    content.extend(["Local citation locations:", ""] + ["- `" + origin + "`" for origin in row.get("origins", [])] + ["", "## Applicability and gaps", "", "Project-specific thresholds and transfer performance remain unverified.", ""])
    path.write_text("\n".join(content), encoding="utf-8")
    return path.name


def ingest_web(path):
    content = path.read_text(encoding="utf-8")
    headings = list(re.finditer(r"^(.+?) \((https?://[^\s]+)\)\n", content, re.M))
    blocks = [content[match.start():headings[index + 1].start() if index + 1 < len(headings) else len(content)]
              for index, match in enumerate(headings)]
    ledger = []
    for block in blocks:
        match = re.search(r"^(.+?) \((https?://[^\s]+)\)\n", block)
        if not match:
            continue
        title, url = match.groups()
        doi = DOI.search(block)
        arxiv = ARXIV.search(url)
        if doi:
            identifier, kind = clean_doi(doi.group()), "doi"
        elif arxiv:
            identifier, kind = arxiv.group(1), "arxiv"
        else:
            identifier, kind = url, "url"
        row = {"identifier": identifier, "kind": kind, "origins": []}
        filename = archive_record(row, {"title": title}, query=path.name)
        ledger.append({"title": title, "url": url, "identifier": identifier, "kind": kind, "file": filename})
    secondary = []
    for match in DOI.finditer(content):
        identifier = clean_doi(match.group())
        if identifier.lower() in {row["identifier"].lower() for row in ledger + secondary}:
            continue
        row = {"identifier": identifier, "kind": "doi", "origins": []}
        filename = archive_record(row, query=path.name + " (secondary citation lead)")
        secondary.append({"identifier": identifier, "kind": "doi", "file": filename})
    save_json(path.stem + "-ledger.json", {"date": DATE, "database": "Web search; all returned result leads retained", "results": ledger, "secondary_citation_leads": secondary})
    sync_register()
    log_operation("Archived every web-search result and secondary identifier from " + path.name + "; updated Theses.md.")
    print(json.dumps(ledger, ensure_ascii=False, indent=2))


def import_existing():
    rows = inventory()
    # Write leads before network operations, so failures cannot lose discoveries.
    for row in rows:
        archive_record(row)
    resolved = {}
    def resolve(row):
        if row["kind"] != "doi":
            return row, None, "arXiv requires separate canonical verification"
        try:
            return row, metadata(fetch("https://api.crossref.org/works/" + quote(row["identifier"], safe=""))["message"]), None
        except Exception as error:
            return row, None, str(error)
    with ThreadPoolExecutor(max_workers=5) as pool:
        for future in as_completed([pool.submit(resolve, row) for row in rows]):
            row, meta, error = future.result()
            resolved[row["identifier"].lower()] = {"metadata": meta, "error": error}
            # Replace the just-created unresolved placeholder, never authored work.
            path = ARCHIVE / safe_name(row["identifier"] if row["kind"] == "doi" else "arxiv_" + row["identifier"])
            if meta and "# Unverified citation:" in path.read_text(encoding="utf-8"):
                path.unlink()
                archive_record(row, meta)
            print(row["identifier"], "verified" if meta else error, flush=True)
    save_json("canonical-metadata.json", resolved)
    sync_register()
    log_operation("Imported " + str(len(rows)) + " existing project citation identifiers into Theses.md and Theses/.")
    print("Imported", len(rows), "unique identifiers")


def search(query, count):
    params = urlencode({"query.bibliographic": query, "rows": count})
    url = "https://api.crossref.org/works?" + params
    result = fetch(url)["message"]["items"]
    archive = []
    for item in result:
        meta = metadata(item)
        row = {"identifier": meta["doi"], "kind": "doi", "origins": []}
        filename = archive_record(row, meta, query=query)
        archive.append({"file": filename, "metadata": meta})
    path = ARCHIVE / "search-ledger.json"
    ledger = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    ledger.append({"date": DATE, "database": "Crossref", "query": query, "url": url, "results": archive})
    save_json("search-ledger.json", ledger)
    sync_register()
    log_operation("Crossref query: " + query + "; archived all " + str(len(archive)) + " returned records and updated Theses.md.")
    print(json.dumps(archive, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("inventory")
    commands.add_parser("import-existing")
    web = commands.add_parser("ingest-web")
    web.add_argument("path", type=Path)
    find = commands.add_parser("search")
    find.add_argument("query")
    find.add_argument("--count", type=int, default=3)
    args = parser.parse_args()
    ARCHIVE.mkdir(exist_ok=True)
    if args.command == "inventory":
        rows = inventory()
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    elif args.command == "import-existing":
        import_existing()
    elif args.command == "ingest-web":
        ingest_web(args.path)
    else:
        search(args.query, args.count)
