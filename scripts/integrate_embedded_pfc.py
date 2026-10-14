"""Publish the checked finite-PFC study without private logs or source papers.

The numerical payload is copied from its completed delivery manifest. Changes
are limited to navigation, public provenance and optional scholarly references.
No simulation is rerun or promoted to specimen-level physical validation.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import shutil
import zipfile
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'LEARN_20260929/modeling/20261011-embedded-pfc-feasibility'
TARGET = ROOT / 'modeling/embedded-pfc-feasibility'
ARCHIVE = 'Embedded_PFC_Feasibility_Public_20261011.zip'
SITE_URL = 'https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/'
SKIP_FILES = {'WORK_LOG.md', 'MANIFEST.json', 'scripts/package_delivery.py',
              'scripts/verify_relocation.py', 'verification/native_relocated_stdout.txt'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add_reader_links(text):
    # Plain replacements preserve every previously rendered scientific equation.
    text = text.replace('<nav aria-label="Documents">',
                        '<nav aria-label="Documents"><a href="' + SITE_URL + '">Theory course</a>')
    text = text.replace('<div class="downloads">',
                        '<div class="downloads"><a href="' + ARCHIVE + '">Download study folder</a>')
    return text


def copy_study():
    manifest = json.loads((SOURCE / 'MANIFEST.json').read_text(encoding='utf-8'))
    provenance = json.loads((SOURCE / 'sources/prior_interface_provenance.json').read_text(encoding='utf-8'))
    paper_urls = {Path(row['relative_path']).name: row['url'] for row in provenance['sources'].values()}
    copied = []
    for row in manifest['files']:
        relative = Path(row['file'])
        if row['file'] in SKIP_FILES or relative.suffix == '.log':
            continue
        if relative.suffix == '.pdf' and row['file'] != 'output/pdf/FINITE_PFC_DERIVATION.pdf':
            continue
        source = SOURCE / relative
        assert source.resolve().is_relative_to(SOURCE.resolve()) and source.is_file()
        assert digest(source) == row['sha256'], 'Source changed after acceptance: ' + row['file']
        destination = TARGET / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append(row)

    reader = TARGET / 'index.html'
    reader.write_text(add_reader_links(reader.read_text(encoding='utf-8')), encoding='utf-8')
    builder = TARGET / 'scripts/build_reader.py'
    builder_text = builder.read_text(encoding='utf-8')
    builder.write_text(add_reader_links(builder_text), encoding='utf-8')
    css = TARGET / 'assets/reader.css'
    css.write_text(css.read_text(encoding='utf-8') + '\nheader nav > a{white-space:nowrap;align-self:center;padding:8px 0}\n', encoding='utf-8')

    source_note = ('The prior source-context file is copied as `sources/prior_interface_evidence.md`. '
                   'This public edition links scholarly papers to their original repositories or DOI pages; '
                   'third-party paper PDFs and operational logs are excluded. Archived EOS coefficients, '
                   'the worked derivation, model/data files and scientific audit records are bundled. '
                   'The printable PDF preserves the accepted local study and its original source ledger; '
                   'this page and `PUBLICATION.md` describe the public package contents.')
    sources = TARGET / 'SOURCES.md'
    source_text = sources.read_text(encoding='utf-8')
    old_note = source_text.split('\n\n')[-2] if source_text.endswith('\n\n') else source_text.strip().split('\n\n')[-1]
    assert old_note.startswith('The prior source-context file is copied')
    source_text = source_text.replace(old_note, source_note)
    sources.write_text(source_text, encoding='utf-8')
    text = reader.read_text(encoding='utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    sources_section = soup.select_one('#sources')
    paragraph = next(p for p in sources_section.select('p') if p.get_text().startswith('The prior source-context file is copied'))
    paragraph.clear()
    paragraph.string = source_note.replace('`', '')
    reader.write_text(str(soup), encoding='utf-8')

    context = TARGET / 'sources/prior_interface_evidence.md'
    text = context.read_text(encoding='utf-8').split('\n## Work record\n')[0]
    text = text.replace('All cited local PDFs are bundled in `sources/`; the JSON contains provenance, exact source states, hashes and limitations. The shared project work log remains the parent agent\'s responsibility.',
                        'The public edition links to the original scholarly sources below; the JSON preserves source states, original hashes and scientific limitations.')
    def replace_paper(match):
        ref = match[1]
        name = Path(unquote(urlsplit(ref).path)).name
        return '(' + paper_urls[name] + ')' if name in paper_urls else match[0]
    text = re.sub(r'\(([^\)]+\.pdf)\)', replace_paper, text)
    context.write_text(text.rstrip() + '\n', encoding='utf-8')

    provenance.pop('work_record', None)
    for row in provenance['sources'].values():
        row.pop('local_path', None)
        row['original_pdf_included_in_public_package'] = False
    (TARGET / 'sources/prior_interface_provenance.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8')

    readme = TARGET / 'README.md'
    text = readme.read_text(encoding='utf-8')
    text = text.replace('Copied prior context and six source PDFs are in `sources/`.',
                        'Copied prior context and archived EOS coefficients are in `sources/`; scholarly papers are linked through their original sources. See [PUBLICATION.md](PUBLICATION.md) for public-package provenance.')
    text = text.replace('The local `.tools/` dependency cache and `build/` intermediates are not included in the deliverable archive.',
                        'Dependency caches, build intermediates, operational logs and third-party paper PDFs are excluded from this public archive. The included scientific audit records describe the accepted source study; publication integrity has a separate audit.')
    readme.write_text(text, encoding='utf-8')
    ignore = TARGET / '.gitignore'
    text = ignore.read_text(encoding='utf-8')
    text = '\n'.join(line for line in text.splitlines() if line not in {'models/*.mph', 'sources/accepted_control/models/*.mph', '*.zip'}) + '\n'
    ignore.write_text(text, encoding='utf-8')

    (TARGET / 'PUBLICATION.md').write_text(
        '# Public finite-PFC study\n\n'
        'Published from the completed 2026-10-11 conditional finite-PFC study. '
        'The real-fluid models, parameter/native/reference data, worked scientific derivation, '
        'four plots and accepted printable PDF are unchanged. The public reader adds course '
        'navigation and a downloadable folder. README/source-context/provenance records are '
        'adapted to replace copied scholarly paper PDFs with optional original-source links '
        'and omit private machine paths and operational logs. The printable PDF retains the '
        'original local-study source ledger; its reference to copied papers describes that '
        'original delivery, not this curated public archive.\n\n'
        'The 60 stationary and six supplied-seed transient native/reference checks verify '
        'these reduced equations. The 132 phase states and 30-state selector compare stipulated '
        'species, size and gel properties. New speeds are radial interface speeds and all '
        'embedded controls emit zero exterior mass. Laser activation, gel rupture and a '
        'fluid-filled path, nonspherical collapse jets and sensor/target shock pressures '
        'remain unvalidated for the target system. Consult IMPLEMENTATION_HANDOFF.md for '
        'the additional spatial models and measured acceptance gates.\n\n'
        'COPY_MANIFEST.json compares public payload hashes with the accepted source. '
        'MANIFEST.json and PUBLICATION_AUDIT.json verify this public archive. The original '
        'numerical/reader/PDF/native-reload audits remain source-study evidence; they do '
        'not assert that source-paper files are bundled or that this publication is an '
        'experimental validation. All essential reader assets are local. The course link '
        'and scholarly references are optional external links. Extract the ZIP and move '
        'the entire folder to retain offline reading and day/night controls.\n', encoding='utf-8')

    # Source history remains useful, while public inclusion is stated explicitly.
    source_manifest = TARGET / 'verification/SOURCE_MANIFEST.json'
    source_rows = json.loads(source_manifest.read_text(encoding='utf-8'))
    for row in source_rows:
        p = TARGET / row['file']
        row['included_in_public_package'] = p.is_file()
        if p.is_file():
            row['public_sha256'] = digest(p)
    source_manifest.write_text(json.dumps(source_rows, indent=2) + '\n', encoding='utf-8')
    records = []
    for row in copied:
        p = TARGET / row['file']
        public_sha = digest(p)
        records.append({'file': row['file'], 'accepted_source_sha256': row['sha256'],
                        'public_sha256': public_sha, 'unchanged': public_sha == row['sha256']})
    (TARGET / 'COPY_MANIFEST.json').write_text(json.dumps({'source_study': '20261011-embedded-pfc-feasibility',
        'scope': 'Public curation and integrity; numerical results and models remain accepted conditional controls.',
        'files': records}, indent=2) + '\n', encoding='utf-8')
    package_study()
    return len(records)


def package_study():
    selected = sorted(p for p in TARGET.rglob('*') if p.is_file()
                      and not {'build', 'tmp', '__pycache__', '.tools'}.intersection(p.relative_to(TARGET).parts)
                      and p.name not in {ARCHIVE, 'MANIFEST.json', 'PUBLICATION_AUDIT.json'})
    records = [{'file': p.relative_to(TARGET).as_posix(), 'bytes': p.stat().st_size, 'sha256': digest(p)} for p in selected]
    (TARGET / 'MANIFEST.json').write_text(json.dumps({'date': '2026-10-14', 'accepted_source_date': '2026-10-11',
        'scope': 'Public conditional finite-PFC study; target embedded mechanism not physically validated.',
        'files': records}, indent=2) + '\n', encoding='utf-8')
    selected.append(TARGET / 'MANIFEST.json')
    # This audit describes the payload, without hashing itself or its container.
    if (TARGET / 'PUBLICATION_AUDIT.json').is_file():
        selected.append(TARGET / 'PUBLICATION_AUDIT.json')
    with zipfile.ZipFile(TARGET / ARCHIVE, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for p in selected:
            archive.write(p, 'Embedded_PFC_Feasibility/' + p.relative_to(TARGET).as_posix())
    with zipfile.ZipFile(TARGET / ARCHIVE) as archive:
        assert archive.testzip() is None
        for p in selected:
            assert hashlib.sha256(archive.read('Embedded_PFC_Feasibility/' + p.relative_to(TARGET).as_posix())).hexdigest() == digest(p)


def integrate_links():
    settings = json.loads((ROOT / 'COURSE_SETTINGS.json').read_text(encoding='utf-8'))
    pages = [ROOT / 'index.html', *(ROOT / unit['file'] for unit in settings['chapters'] + settings['appendices'] + settings['legacy_routes']),
             *sorted((ROOT / 'reference').glob('*.html'))]
    for page in pages:
        soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
        old = soup.select_one('[data-embedded-pfc-link]')
        if old:
            old.decompose()
        page.write_text(str(soup), encoding='utf-8', newline='\n')
    settings['embedded_pfc'] = {'parent_unit': 'A', 'file': 'modeling/embedded-pfc-feasibility/index.html',
        'pdf': 'modeling/embedded-pfc-feasibility/output/pdf/FINITE_PFC_DERIVATION.pdf',
        'archive': 'modeling/embedded-pfc-feasibility/' + ARCHIVE,
        'source': '20261011-embedded-pfc-feasibility',
        'scope': 'Finite real-fluid PFC equilibrium and supplied post-nucleation seed in intact spherical gel; target laser/fracture/jet/impact not validated.'}
    (ROOT / 'COURSE_SETTINGS.json').write_text(json.dumps(settings, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if (ROOT/'assets/figures-editable/manifest.json').is_file():
        from integrate_english_figures import integrate as integrate_english
        integrate_english()
    return len(pages)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--refresh-source', action='store_true',
                        help='Explicitly replace the local reader with its accepted source delivery')
    args = parser.parse_args()
    files = copy_study() if args.refresh_source else 0
    pages = integrate_links()
    print(json.dumps({'copied_files': files, 'linked_course_pages': pages,
                      'study': TARGET.relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
