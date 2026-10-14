"""Create a standalone, movable literature folder and forwarding archive."""
from pathlib import Path
import hashlib
import json
import shutil
import zipfile
from manage_theses import ROOT, ARCHIVE, DATE, save_json


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    audit = json.loads((ARCHIVE / "VALIDATION.json").read_text(encoding="utf-8"))
    assert audit["status"] == "passed"
    destination = ROOT / "delivery/Theses_20261014"
    assert destination.resolve().is_relative_to((ROOT / "delivery").resolve())
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "Theses.md", destination / "Theses.md")
    work_log = (ROOT / "WORK_LOG.md").read_text(encoding="utf-8")
    marker = "## 2026-10-14 — Theses management and lesson literature research"
    extract = work_log[work_log.index(marker):]
    (destination / "WORK_LOG.md").write_text("# Literature delivery work log\n\nExtracted from the project WORK_LOG.md. Earlier project work remains in the lesson workspace.\n\n" + extract, encoding="utf-8")
    for source in ARCHIVE.iterdir():
        if source.is_file():
            target = destination / "Theses" / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    for source in (ROOT / "scripts").glob("*theses*.py"):
        target = destination / "scripts" / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    (destination / "README.md").write_text(
        "# Lesson literature delivery\n\nOpen [Theses/index.html](Theses/index.html) for the searchable offline reader.\n"
        "Read [Theses.md](Theses.md) for the complete register.\n"
        "Read [the chapter evidence map](Theses/CHAPTER_MAP.md) for lesson placement.\n\n"
        "Forward this complete folder. Reader styling and controls are embedded.\n"
        "Primary-source links require network access when opened.\n"
        "The included management scripts require Python and BeautifulSoup4.\n"
        "The reader and Markdown records require no Python installation.\n", encoding="utf-8")
    selected = sorted(path for path in destination.rglob("*") if path.is_file() and path.name != "FILE_MANIFEST.json")
    manifest = {"date": DATE, "entry": "Theses/index.html", "records": audit["register_entries"],
                "files": [{"file": path.relative_to(destination).as_posix(), "sha256": digest(path), "bytes": path.stat().st_size} for path in selected]}
    (destination / "FILE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    archive_path = destination.with_suffix(".zip")
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(destination.rglob("*")):
            if path.is_file():
                archive.write(path, destination.name + "/" + path.relative_to(destination).as_posix())
    with zipfile.ZipFile(archive_path) as archive:
        assert archive.testzip() is None
        for row in manifest["files"]:
            assert hashlib.sha256(archive.read(destination.name + "/" + row["file"])).hexdigest() == row["sha256"]
    result = {"status": "passed", "date": DATE, "folder": destination.relative_to(ROOT).as_posix(),
              "zip": archive_path.relative_to(ROOT).as_posix(), "files": len(selected) + 1,
              "sha256": digest(archive_path), "crc": "passed", "manifest_hashes": "passed"}
    # Keep the ZIP audit outside the archive to avoid self-referential hashes.
    (ROOT / "verification/theses-package-20261014.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
