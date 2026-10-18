"""Apply reviewed summaries and build the canonical register and offline reader."""
from html import escape
from urllib.parse import quote
import json
import re
from manage_theses import ROOT, ARCHIVE, DATE, safe_name, save_json, sync_register, log_operation


def field(content, name):
    match = re.search(r"^- " + re.escape(name) + r": (.*)$", content, re.M)
    return match.group(1) if match else "Unverified"


def set_field(content, name, value):
    return re.sub(r"^- " + re.escape(name) + r": .*$", lambda match: "- " + name + ": " + value, content, flags=re.M)


def apply_reviews():
    reviews = json.loads((ARCHIVE / "reviewed-summaries.json").read_text(encoding="utf-8"))
    cache = json.loads((ARCHIVE / "canonical-metadata.json").read_text(encoding="utf-8"))
    for path in ARCHIVE.glob("*.md"):
        if path.name.startswith(("10.", "arxiv_")):
            content = path.read_text(encoding="utf-8")
            doi = field(content, "DOI")
            key = path.stem.removeprefix("arxiv_") if path.name.startswith("arxiv_") else doi.lower()
            record_type = ((cache.get(key) or {}).get("metadata") or {}).get("type", "preprint" if path.name.startswith("arxiv_") else "scholarly record")
            if "- Record type:" not in content:
                content = content.replace("- Date searched:", "- Record type: " + record_type + "\n- Date searched:")
            path.write_text(content, encoding="utf-8")
        elif path.name.startswith("url_"):
            content = path.read_text(encoding="utf-8")
            content = set_field(content, "Evidence level", "?: proceedings/program collection; individual paper identity unverified")
            if "- Record type:" not in content:
                content = content.replace("- Date searched:", "- Record type: proceedings/program collection\n- Date searched:")
            path.write_text(content, encoding="utf-8")
        elif path.name.startswith("citation_fragment_"):
            content = path.read_text(encoding="utf-8")
            if "- Record type:" not in content:
                content = content.replace("- Date searched:", "- Record type: unresolved citation fragment\n- Date searched:")
            path.write_text(content, encoding="utf-8")
    # Normalize deposited title markup without changing scholarly identifiers.
    for path in ARCHIVE.glob("*.md"):
        if not path.name.startswith(("10.", "arxiv_", "url_", "citation_fragment_")):
            continue
        content = path.read_text(encoding="utf-8")
        # Remove continuation lines introduced by deposited multiline title markup.
        content = re.sub(r"^# .*?\n(?=- Title:)", "", content, flags=re.S)
        content = re.sub(r"(^- Title:.*?)\n(?=- Authors:)", lambda match: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", match.group(1))) + "\n", content, flags=re.M | re.S)
        title = field(content, "Title")
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", title)).strip()
        content = set_field(content, "Title", title)
        content = "# " + title + "\n\n" + content.lstrip()
        if path.name == "10.1103_physrevfluids.9.l091601.md":
            title = "Laser-induced cavitation in liquid ⁴He near the liquid-vapor critical point"
            content = set_field(content, "Title", title)
            content = re.sub(r"^# .*", lambda match: "# " + title, content, count=1, flags=re.M)
        content = re.sub(r"This work addresses .*?\.\nExperiments performed", lambda match: "This work addresses " + title.rstrip(".") + ".\nExperiments performed", content, flags=re.S)
        if "- Lesson mapping: Pending evidence review." in content:
            content = content.replace("- Lesson mapping: Pending evidence review.", "- Lesson mapping: Background or peripheral citation; placement unreviewed.")
        path.write_text(content, encoding="utf-8")
    for identifier, review in reviews.items():
        name = safe_name("arxiv_" + identifier.removeprefix("arxiv:")) if identifier.startswith("arxiv:") else safe_name(identifier)
        candidates = [path for path in ARCHIVE.glob("*.md") if path.name.lower() == name.lower()]
        if not candidates:
            raise ValueError("Reviewed paper missing: " + identifier)
        path = candidates[0]
        content = path.read_text(encoding="utf-8")
        content = set_field(content, "Lesson mapping", review["unit"])
        content = set_field(content, "Evidence level", review["evidence"])
        if review.get("year"):
            content = set_field(content, "Year", str(review["year"]))
        access = "Open access verified; publisher full text read." if "publisher full text" in review["evidence"] else (
            "Author-hosted or repository copy verified; see evidence locator." if "full text" in review["evidence"] or "preprint" in review["evidence"] or "manuscript" in review["evidence"] else
            "Metadata and abstract evidence; full-text access not verified.")
        content = set_field(content, "Access status", access)
        content = re.sub(r"(## Two-sentence summary\n\n).*?(\n\n## Provenance)", lambda match:
                         match.group(1) + review["background"] + "\n" + review["experiments"] + match.group(2), content, flags=re.S)
        content = re.sub(r"(## Applicability and gaps\n\n).*?(?=\n## |\Z)", lambda match:
                         match.group(1) + review["limits"] + "\n", content, flags=re.S)
        content = re.sub(r"\n## Evidence review.*\Z", "", content, flags=re.S)
        source = review.get("source")
        if not source:
            if "Europe PMC" in review["evidence"]:
                source = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + "query=DOI%3A" + quote(identifier, safe="") + "&resultType=core&format=json"
            else:
                source = cache.get(identifier.lower(), {}).get("metadata", {}).get("source", "Preserved local lesson citation")
        content += "\n## Evidence review\n\n- Date read: " + DATE + "\n- Source read: " + source + "\n- Locator: " + review["locator"] + "\n"
        path.write_text(content, encoding="utf-8")
    # One database DOI serves three material subentries.
    path = ARCHIVE / "10.18434_T4D303.md"
    content = path.read_text(encoding="utf-8")
    content = set_field(content, "Lesson mapping", "Chapter 2; Appendix A")
    content = set_field(content, "Evidence level", "I: property scopes preserved from the lesson; database identity verified")
    content = re.sub(r"(## Two-sentence summary\n\n).*?(\n\n## Provenance)", lambda match:
                     match.group(1) + "The database compiles thermochemistry and phase-equilibrium properties for named compounds.\nPublished measurements and correlations are indexed with source-specific temperatures and validity ranges." + match.group(2), content, flags=re.S)
    if "## Material subentries" not in content:
        content += "\n## Material subentries\n\n- PFP (R8): https://webbook.nist.gov/cgi/cbook.cgi?ID=C678262&Mask=4\n- PFH (R9): https://webbook.nist.gov/cgi/cbook.cgi?ID=C355420&Mask=4\n- Water (R15): https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=4\n\n1997 is the database publication year. Property datum dates differ.\n"
    path.write_text(content, encoding="utf-8")


def build_reader():
    cards = []
    paths = sorted(path for path in ARCHIVE.glob("*.md") if path.name.startswith(("10.", "arxiv_", "url_", "citation_fragment_")))
    for path in paths:
        content = path.read_text(encoding="utf-8")
        title, unit, evidence = [field(content, key) for key in ("Title", "Lesson mapping", "Evidence level")]
        summary = re.search(r"## Two-sentence summary\n\n(.*?)\n\n## ", content, re.S).group(1)
        reviewed = evidence.startswith("E:")
        label = "Reviewed evidence" if reviewed else "Metadata or unresolved lead"
        cards.append('<article data-reviewed="' + str(reviewed).lower() + '"><p class="tag">' + escape(label) + ' · ' + escape(unit) + '</p><h2>' + escape(title) + '</h2><p class="meta">' + escape(field(content, "Authors")) + ' · ' + escape(field(content, "Year")) + '</p><p>' + escape(summary).replace('\n', '</p><p>') + '</p><p class="meta">' + escape(evidence) + '</p><p><a href="' + quote(path.name, safe="._-") + '">Full Markdown record</a> · <a href="' + escape(field(content, "Source URL"), quote=True) + '">Primary identifier</a></p><details><summary>Provenance and limits</summary><pre>' + escape(content) + '</pre></details></article>')
    page = '''<!doctype html><html lang="en" data-theme="dark"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Theses · Laser PFC droplet transfer</title>
<style>:root{color-scheme:dark;--bg:#111820;--panel:#19232f;--fg:#edf2f6;--muted:#a7b9ca;--line:#324354;--accent:#80c5dd}[data-theme=light]{color-scheme:light;--bg:#f3f2ed;--panel:#fff;--fg:#203040;--muted:#596b7c;--line:#cbd3d8;--accent:#12607c}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 system-ui,sans-serif}header,main{max-width:1100px;margin:auto;padding:30px}header{border-bottom:1px solid var(--line)}h1{font:42px/1.2 Georgia,serif;margin:12px 0}h2{font:24px/1.35 Georgia,serif;margin:10px 0}a{color:var(--accent)}article{padding:24px;background:var(--panel);border:1px solid var(--line);border-radius:10px;margin:18px 0}p{margin:8px 0}.tag,.meta{color:var(--muted);font-size:14px}.tag{letter-spacing:.025em}input,select,button{font:inherit;background:var(--panel);color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:10px}input[type=search]{width:min(100%,560px)}.controls{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-top:20px}#theme{position:fixed;right:18px;bottom:18px;box-shadow:0 2px 20px #0004}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 ui-monospace,monospace}summary{cursor:pointer}.hidden{display:none}@media(max-width:600px){header,main{padding:18px}h1{font-size:32px}article{padding:18px}}</style>
<header><p class="tag">Laser-induced PFC droplet transfer · ''' + DATE + '''</p><h1>Theses and lesson evidence</h1><p>Every discovered paper has a Markdown entry. Experimental evidence and unresolved leads are labeled.</p><p><a href="CHAPTER_MAP.md">Chapter evidence map</a> · <a href="RESEARCH.md">Research decisions and limits</a> · <a href="README.md">Management workflow</a></p><div class="controls"><input id="search" type="search" placeholder="Search title, author, DOI, or topic" aria-label="Search papers"><select id="unit" aria-label="Lesson unit"><option value="">All lesson units</option><option>Chapter 1</option><option>Chapter 2</option><option>Chapter 3</option><option>Chapter 4</option><option>Appendix A</option></select><label><input id="reviewed" type="checkbox"> Reviewed evidence</label></div><p id="count" class="meta" aria-live="polite"></p></header><main>''' + ''.join(cards) + '''</main><button id="theme" type="button" aria-label="Switch day or night theme">Day / night</button><script>const root=document.documentElement;let mode='dark';try{mode=localStorage.getItem('theses-theme')||'dark'}catch{}root.dataset.theme=mode;document.querySelector('#theme').onclick=()=>{root.dataset.theme=root.dataset.theme==='dark'?'light':'dark';try{localStorage.setItem('theses-theme',root.dataset.theme)}catch{}};const search=document.querySelector('#search'),unit=document.querySelector('#unit'),reviewed=document.querySelector('#reviewed'),cards=[...document.querySelectorAll('article')];function filter(){let count=0;for(const card of cards){const text=card.textContent.toLowerCase();const show=text.includes(search.value.toLowerCase())&&text.includes(unit.value.toLowerCase())&&(!reviewed.checked||card.dataset.reviewed==='true');card.classList.toggle('hidden',!show);count+=show?1:0}document.querySelector('#count').textContent=count+' / '+cards.length+' records'}for(const control of [search,unit,reviewed])control.addEventListener('input',filter);filter();</script></html>'''
    (ARCHIVE / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    apply_reviews()
    count = sync_register()
    build_reader()
    log_operation("Built the complete Theses.md register and offline reader from reviewed summaries.")
    print("Register entries", count)
