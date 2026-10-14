"""Refresh imported metadata while preserving reviewed scientific summaries."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen
from urllib.parse import quote
import json
import re
import sys
from bs4 import BeautifulSoup
from manage_theses import ARCHIVE, DATE, fetch, metadata, save_json, sync_register, log_operation

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def update(path, meta):
    content = path.read_text(encoding="utf-8")
    content = re.sub(r"^# .*", "# " + meta["title"], content, count=1, flags=re.M)
    fields = {"Title": meta["title"], "Authors": "; ".join(meta["authors"]), "Year": str(meta["year"])}
    for key, value in fields.items():
        content = re.sub(r"^- " + key + r": .*", lambda match: "- " + key + ": " + value, content, flags=re.M)
    if "Background and theory remain unverified pending a readable primary source." in content:
        content = content.replace("Background and theory remain unverified pending a readable primary source.",
                                  "This work addresses " + meta["title"].rstrip(".") + ".")
        content = content.replace("Metadata verified; scientific summary pending review", "Metadata verified; title-based topic summary; experiments unverified")
        content = content.replace("Unverified imported lead", "Metadata verified; title-based topic summary; experiments unverified")
    if meta.get("source") and meta["source"] not in content:
        content += "\nCanonical metadata verified on " + DATE + ": " + meta["source"] + "\n"
    path.write_text(content, encoding="utf-8")


def main():
    cache = json.loads((ARCHIVE / "canonical-metadata.json").read_text(encoding="utf-8"))
    for search in json.loads((ARCHIVE / "search-ledger.json").read_text(encoding="utf-8")):
        for row in search["results"]:
            cache[row["metadata"]["doi"].lower()] = {"metadata": row["metadata"], "error": None}
    paths = [path for path in ARCHIVE.glob("*.md") if path.name.startswith(("10.", "arxiv_"))]
    jobs = []
    for path in paths:
        content = path.read_text(encoding="utf-8")
        if path.name.startswith("10."):
            identifier = re.search(r"^- DOI: (.+)$", content, re.M).group(1)
            key = identifier.lower()
            if cache.get(key, {}).get("metadata"):
                update(path, cache[key]["metadata"])
            else:
                jobs.append((path, identifier, "doi"))
        else:
            identifier = path.stem.removeprefix("arxiv_")
            jobs.append((path, identifier, "arxiv"))
    def resolve(job):
        path, identifier, kind = job
        try:
            if kind == "doi":
                meta = metadata(fetch("https://api.crossref.org/works/" + quote(identifier, safe=""))["message"])
            else:
                url = "https://arxiv.org/abs/" + identifier
                with urlopen(Request(url, headers={"User-Agent": "LessonLiteratureArchive/1.0"}), timeout=25) as response:
                    soup = BeautifulSoup(response.read(), "html.parser")
                title = soup.find("meta", attrs={"name": "citation_title"})
                if not title:
                    raise ValueError("Canonical arXiv metadata unavailable")
                date = soup.find("meta", attrs={"name": "citation_date"})
                abstract = soup.find("blockquote", class_="abstract")
                journal_doi = soup.find("meta", attrs={"name": "citation_doi"})
                meta = {"title": title["content"], "authors": [tag["content"] for tag in soup.find_all("meta", attrs={"name": "citation_author"})],
                        "year": date["content"][:4] if date else "Unverified", "source": url,
                        "abstract": abstract.get_text(" ", strip=True).removeprefix("Abstract:") if abstract else "",
                        "arxiv": identifier, "doi": journal_doi["content"] if journal_doi else "", "venue": "arXiv"}
            return path, identifier.lower(), meta, None
        except Exception as error:
            return path, identifier.lower(), None, str(error)
    with ThreadPoolExecutor(max_workers=2) as pool:
        for future in as_completed([pool.submit(resolve, job) for job in jobs]):
            path, key, meta, error = future.result()
            cache[key] = {"metadata": meta, "error": error}
            if meta:
                update(path, meta)
            print(path.name, "verified" if meta else error, flush=True)
    save_json("canonical-metadata.json", cache)
    sync_register()
    log_operation("Refreshed canonical citation metadata and synchronized Theses.md; authored summaries preserved.")
    print("Canonical records", len(cache), "unresolved", sum(not item["metadata"] for item in cache.values()))


if __name__ == "__main__":
    main()
