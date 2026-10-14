"""Build a portable local lesson folder and ZIP without publishing."""
from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'delivery/Lesson_Revision_20261014'
ARCHIVE = ROOT / 'delivery/Lesson_Revision_20261014.zip'
EXCLUDED = {'.git', '__pycache__', 'build', 'tmp', 'temp', '.tools'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert DEST.resolve().is_relative_to(ROOT.resolve())
    folders = ['assets', 'chapters', 'appendices', 'reference', 'text', 'content',
               'scripts', 'modeling/minimal-cavitation',
               'modeling/embedded-pfc-feasibility',
               'learning-records/resolver-progress', 'sources/ui-feedback-20261014',
               'sources/revision-guidance-20261014', 'sources/historical-handoffs']
    selected = {Path(name) for name in ['index.html', 'README.md', 'MISSION.md',
                                      'RESOURCES.md', 'WORK_LOG.md', 'HANDOFF.md', 'COURSE_SETTINGS.json', '.nojekyll']}
    selected.update(Path('sources') / name for name in [
        'Laser_PFC_Cavitation_Jet_Transfer_Course_EN.md',
        'Cavitation_Course_Before_After_Comparison_EN_ZH.md'])
    selected.update(Path('verification') / name for name in [
        'equations.json', 'lesson-revision-audit.json',
        'lesson-revision-baseline.json', 'chapter-prose-revision.md',
        'report-prose-revision.md', 'embedded-bilingual-revision.md',
        'chapter-prose-audit.json', 'independent-editorial-review.md',
        'course-audit.json', 'language-labels-audit.json',
        'lesson-revision-browser-audit.json', 'bilingual-terms.json',
        'resolver-reader-prose-audit.json', 'embedded-pfc-publication-audit.json',
        'unified-frontend-browser-audit.json', 'unified-frontend-independent-review.md',
        'local-revision-relocation.json', 'local-revision-forwarded-browser.json',
        'report-unified-frontend-audit.json'])
    selected.update(Path('verification') / f'chapter0{n}-check.py' for n in range(1, 6))
    selected.update(p.relative_to(ROOT) for p in (ROOT / 'verification').glob('embedded-reader*.png'))
    for folder in folders:
        for path in (ROOT / folder).rglob('*'):
            relative = path.relative_to(ROOT)
            if (path.is_file() and not EXCLUDED.intersection(relative.parts)
                    and path.suffix not in {'.pyc', '.class', '.log', '.lock'}):
                selected.add(relative)
    selected = {p for p in selected if (ROOT / p).is_file()}
    for relative in sorted(selected):
        target = DEST / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)
    forwarded_path = ROOT / 'verification/local-revision-forwarded-browser.json'
    forwarded_hashes = {}
    if forwarded_path.is_file():
        forwarded = json.loads(forwarded_path.read_text(encoding='utf-8'))
        assert forwarded['status'] == 'passed'
        forwarded_hashes = forwarded.get('verified_reader_asset_hashes', {})
        for relative, expected in forwarded_hashes.items():
            assert digest(DEST / relative) == expected, 'Changed forwarded reader asset: ' + relative
    manifest = {'scope': 'Local lesson revision; no deployment.', 'entry': 'index.html',
                'files': [{'file': p.as_posix(), 'bytes': (DEST / p).stat().st_size,
                           'sha256': digest(DEST / p)} for p in sorted(selected)]}
    (DEST / 'FILE_MANIFEST.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for relative in [*sorted(selected), Path('FILE_MANIFEST.json')]:
            archive.write(DEST / relative, DEST.name + '/' + relative.as_posix())
    with zipfile.ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None
        for row in manifest['files']:
            assert hashlib.sha256(archive.read(DEST.name + '/' + row['file'])).hexdigest() == row['sha256']
    report = {'status': 'passed', 'files': len(selected), 'zip': ARCHIVE.name,
              'zip_bytes': ARCHIVE.stat().st_size, 'zip_sha256': digest(ARCHIVE),
              'crc_and_hashes': 'passed', 'forwarded_reader_assets_bound': len(forwarded_hashes),
              'published': False}
    (ROOT / 'verification/local-revision-package.json').write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
