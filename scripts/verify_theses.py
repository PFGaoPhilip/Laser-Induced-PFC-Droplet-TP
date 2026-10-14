"""Audit every discovered identifier, register entry, summary, and portable link."""
from pathlib import Path
from urllib.parse import unquote, urlparse
from collections import Counter
import json
import re
from bs4 import BeautifulSoup
from manage_theses import ROOT, ARCHIVE, DATE, safe_name, save_json


def main():
    records = sorted(path for path in ARCHIVE.glob("*.md") if path.name.startswith(("10.", "arxiv_", "url_", "citation_fragment_")))
    names = {path.name.lower(): path.name for path in records}
    aliases = json.loads((ARCHIVE / "identifier-aliases.json").read_text(encoding="utf-8"))
    failures = []
    def present(name):
        visited = set()
        while name in aliases and name not in visited:
            visited.add(name)
            name = aliases[name]["canonical_file"]
        return name.lower() in names
    discovery_count = 0
    baseline = json.loads((ARCHIVE / "existing-citation-inventory.json").read_text(encoding="utf-8"))
    for row in baseline["records"]:
        name = safe_name(row["identifier"] if row["kind"] == "doi" else "arxiv_" + row["identifier"])
        if not present(name):
            failures.append("Existing identifier missing: " + name)
        discovery_count += 1
    for path in ARCHIVE.glob("*-ledger.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        searches = data if isinstance(data, list) else [data]
        for search in searches:
            for row in search.get("results", []) + search.get("secondary_citation_leads", []):
                if not present(row["file"]):
                    failures.append("Search result missing: " + row["file"])
                discovery_count += 1
    types = Counter()
    evidence = Counter()
    for path in records:
        content = path.read_text(encoding="utf-8")
        for field in ["Title", "Authors", "Year", "DOI", "arXiv ID/URL", "Source URL", "Date searched", "Evidence level", "Lesson mapping", "Record type"]:
            if not re.search(r"^- " + re.escape(field) + r": .+$", content, re.M):
                failures.append(path.name + ": missing " + field)
        match = re.search(r"## Two-sentence summary\n\n(.*?)\n\n## ", content, re.S)
        lines = match.group(1).splitlines() if match else []
        if len(lines) != 2 or any(not line.rstrip().endswith(".") for line in lines):
            failures.append(path.name + ": two summary sentences required")
        if "<mml:" in content:
            failures.append(path.name + ": raw deposited title markup")
        evidence.update(["reviewed primary evidence" if "- Evidence level: E:" in content else "metadata, inference, or unresolved"])
        types.update([re.search(r"^- Record type: (.+)$", content, re.M).group(1)])
    register = (ROOT / "Theses.md").read_text(encoding="utf-8")
    if len(re.findall(r"^## ", register, re.M)) != len(records):
        failures.append("Register entry count differs from individual records")
    for path in records:
        if "Theses/" + path.name not in unquote(register):
            failures.append("Register link missing: " + path.name)
    link_count = 0
    for path in [ROOT / "Theses.md", *ARCHIVE.glob("*.md"), ARCHIVE / "index.html"]:
        content = path.read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)]+)\)", content) if path.suffix == ".md" else [tag["href"] for tag in BeautifulSoup(content, "html.parser").find_all(href=True)]
        for link in links:
            parsed = urlparse(link)
            if parsed.scheme or link.startswith("#"):
                continue
            target = path.parent / unquote(parsed.path)
            if not target.is_file():
                failures.append("Broken local link: " + str(path.relative_to(ROOT)) + " -> " + link)
            link_count += 1
    soup = BeautifulSoup((ARCHIVE / "index.html").read_text(encoding="utf-8"), "html.parser")
    if len(soup.find_all("article")) != len(records):
        failures.append("Offline reader count differs from register")
    if not soup.find(id="theme"):
        failures.append("Day/night toggle missing")
    if soup.select("script[src],link[href],img[src]"):
        failures.append("Offline reader has external assets")
    result = {"status": "failed" if failures else "passed", "date": DATE,
              "register_entries": len(records), "scholarly_records": sum(count for kind, count in types.items() if kind not in {"proceedings/program collection", "unresolved citation fragment"}),
              "existing_identifiers_covered": len(baseline["records"]),
              "discovery_references_checked": discovery_count, "identifier_aliases": len(aliases),
              "evidence_levels": dict(evidence), "record_types": dict(types),
              "local_links_checked": link_count, "failures": failures}
    save_json("VALIDATION.json", result)
    print(json.dumps(result, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
