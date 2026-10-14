"""Deduplicate DOI, repository, and preprint records; retain discovery provenance."""
from pathlib import Path
from urllib.parse import quote
import hashlib
import json
import re
from manage_theses import ARCHIVE, DATE, archive_record, fetch, metadata, safe_name, save_json, sync_register, log_operation
from refresh_theses_metadata import update

URL_DOIS = {
    "url_01ee5e35e40d5f68.md": "10.3791/53728",
    "url_0531f3ec8a38a2e5.md": "10.1021/acsami.5c11300",
    "url_0697e67dab4b24c3.md": "10.1039/C5RA14119B",
    "url_092d1c52b9eef659.md": "10.1016/j.jmbbm.2024.106776",
    "url_0a8d793c6908935d.md": "10.3390/ijms23126636",
    "url_0ddedf1add21cf81.md": "10.1016/j.jmbbm.2024.106776",
    "url_16610fe7fd0724f7.md": "10.1016/j.ultsonch.2024.106754",
    "url_1852d12c20d3da0a.md": "10.1364/BOE.2.001432",
    "url_1af5d4bd60d50af4.md": "10.3390/nano13152238",
    "url_22301a810279e98c.md": "10.1016/j.apsusc.2014.01.069",
    "url_75e0a6c8f3ee6859.md": "10.1364/BOE.2.001432",
    "url_be86a4dfc46282df.md": "10.1016/j.jmbbm.2024.106776",
    "url_cc9ad40302c60edf.md": "10.1063/1.5060717",
    "url_e222f8152c1ac261.md": "10.1103/PhysRevFluids.9.L091601",
    "10.1016_j.jmbbm.2024.106776Get.md": "10.1016/j.jmbbm.2024.106776",
    "10.3389_fphy.2022.932050_full.md": "10.3389/fphy.2022.932050",
    "10.3389_fphy.2022.932050_pdf.md": "10.3389/fphy.2022.932050",
    "10.3791_53728-v.md": "10.3791/53728",
}


def main():
    cache = json.loads((ARCHIVE / "canonical-metadata.json").read_text(encoding="utf-8"))
    aliases_path = ARCHIVE / "identifier-aliases.json"
    aliases = json.loads(aliases_path.read_text(encoding="utf-8")) if aliases_path.exists() else {}
    mappings = dict(URL_DOIS)
    for identifier, entry in cache.items():
        meta = entry.get("metadata")
        if meta and meta.get("arxiv") and meta.get("doi"):
            mappings[safe_name("arxiv_" + meta["arxiv"])] = meta["doi"]
    for source_name, doi in mappings.items():
        source = ARCHIVE / source_name
        if not source.exists():
            continue
        key = doi.lower()
        meta = cache.get(key, {}).get("metadata")
        if not meta:
            try:
                meta = metadata(fetch("https://api.crossref.org/works/" + quote(doi, safe=""))["message"])
                cache[key] = {"metadata": meta, "error": None}
            except Exception as error:
                cache[key] = {"metadata": None, "error": str(error)}
        target_name = safe_name(meta.get("doi", doi) if meta else doi)
        candidates = [p for p in ARCHIVE.glob("10.*.md") if p.name.lower() == target_name.lower()]
        target = candidates[0] if candidates else ARCHIVE / target_name
        archive_record({"identifier": meta.get("doi", doi) if meta else doi, "kind": "doi", "origins": []}, meta)
        if meta:
            update(target, meta)
        if target.resolve() == source.resolve():
            continue
        prior = source.read_text(encoding="utf-8")
        provenance = []
        url = re.search(r"^- Source URL: (.+)$", prior, re.M)
        if url:
            provenance.append(url.group(1))
        provenance += re.findall(r"^- `(.+)`$", prior, re.M)
        content = target.read_text(encoding="utf-8")
        if source_name not in content:
            content += "\n## Merged discovery " + source_name + "\n\n"
            content += "\n".join("- " + item for item in provenance) + "\n"
        target.write_text(content, encoding="utf-8")
        aliases[source_name] = {"canonical_file": target.name, "doi": doi, "provenance": provenance}
        source.unlink()
    # These are damaged citation fragments, not valid paper identifiers.
    for name in ["10.1016_j.ijheatmas.md", "10.1002_(sici)1096-9101(1997)21_3.md"]:
        path = ARCHIVE / name
        if path.exists():
            target = ARCHIVE / ("citation_fragment_" + hashlib.sha256(name.encode()).hexdigest()[:12] + ".md")
            content = path.read_text(encoding="utf-8")
            content = content.replace("- Evidence level: Unverified imported lead", "- Evidence level: Malformed citation fragment; paper identity unresolved")
            content += "\nThis imported fragment is incomplete; a valid DOI remains missing.\n"
            target.write_text(content, encoding="utf-8")
            aliases[name] = {"canonical_file": target.name, "classification": "Malformed citation fragment"}
            path.unlink()
    # DataCite registers the database and institutional book DOIs.
    for doi in ["10.18434/T4D303", "10.7907/WPQB-2W24"]:
        try:
            attrs = fetch("https://api.datacite.org/dois/" + quote(doi, safe=""))["data"]["attributes"]
            meta = {"title": attrs["titles"][0]["title"], "authors": [creator["name"] for creator in attrs["creators"]],
                    "year": attrs["publicationYear"], "doi": doi, "venue": attrs.get("publisher", ""),
                    "type": attrs["types"]["resourceTypeGeneral"], "source": "https://api.datacite.org/dois/" + doi}
            path = ARCHIVE / safe_name(doi)
            update(path, meta)
            cache[doi.lower()] = {"metadata": meta, "error": None}
        except Exception as error:
            print(doi, error)
    save_json("identifier-aliases.json", aliases)
    save_json("canonical-metadata.json", cache)
    sync_register()
    log_operation("Normalized DOI, repository, and preprint aliases; synchronized Theses.md and preserved provenance.")
    print("Merged aliases", len(aliases), "individual records", len(list(ARCHIVE.glob("10.*.md"))) + len(list(ARCHIVE.glob("arxiv_*.md"))))


if __name__ == "__main__":
    main()
