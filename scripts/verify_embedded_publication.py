"""Audit the actual public folder and its forwarding ZIP, without new solves."""
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser
import argparse
import hashlib
import json
import posixpath
import re
import subprocess
import zipfile
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = 'Embedded_PFC_Feasibility_Public_20261011.zip'


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.external_assets = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for attr in ['src', 'href']:
            value = values.get(attr)
            if value:
                self.links.append(value)
                if tag in {'img', 'script', 'link'} and urlsplit(value).scheme:
                    self.external_assets.append(value)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def audit(study):
    study = study.resolve()
    checked = set()
    archived_links = set()
    def local(base, link):
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return
        target = (base / unquote(parsed.path)).resolve()
        assert target.is_relative_to(study), 'External local dependency: ' + link
        assert target.exists(), 'Missing dependency: ' + str(target.relative_to(study))
        checked.add(target.relative_to(study).as_posix())
    def references(relative, text):
        if relative.endswith('.html'):
            parsed = References(); parsed.feed(text)
            assert not parsed.external_assets, parsed.external_assets
            return parsed.links
        if relative.endswith('.css'):
            return re.findall(r'url\([\"\']?([^\)\"\']+)', text)
        if relative.endswith('.md'):
            return re.findall(r'!?\[[^\]]+\]\(([^\)]+)\)', text)
        return []
    for p in study.rglob('*'):
        if not p.is_file() or p.suffix not in {'.html', '.css', '.md'}:
            continue
        text = p.read_text(encoding='utf-8')
        for link in references(p.relative_to(study).as_posix(), text):
            local(p.parent, link)
    page = (study / 'index.html').read_text(encoding='utf-8')
    assert 'id="theme-toggle"' in page and 'assets/reader.js' in page
    assert 'katex-error' not in page and '@@MATH_' not in page
    assert len(BeautifulSoup(page, 'html.parser').select('.equation')) == 32
    assert 'not established' in re.sub(r'<[^>]+>', ' ', page).lower()
    states = json.loads((study / 'data/reader_states.json').read_text(encoding='utf-8'))
    assert len(states) == 30
    payload = json.loads((study / 'COPY_MANIFEST.json').read_text(encoding='utf-8'))['files']
    editorial_path = study / 'verification/EDITORIAL_REVISION_20261014.json'
    editorial = json.loads(editorial_path.read_text(encoding='utf-8')) if editorial_path.is_file() else {}
    revised = {row['file']: row for row in editorial.get('revised_files', [])}
    prose_files = {'REPORT.md', 'DERIVATION.md', 'IMPLEMENTATION_HANDOFF.md'}
    if editorial:
        preservation = editorial['equation_preservation']
        assert preservation['count'] == 32 and preservation['match_prior_archive']
        assert editorial['protected_payload']['unchanged']
    critical = []
    for row in payload:
        path = study / row['file']
        assert digest(path.read_bytes()) == row['public_sha256'], row['file']
        name = row['file']
        if name in prose_files and not row['unchanged']:
            revision = revised.get(name)
            assert revision and revision['public_sha256'] == row['public_sha256'], name
            assert revision['accepted_source_sha256'] == row['accepted_source_sha256'], name
        elif name in {'REPORT.md', 'DERIVATION.md', 'DERIVATION.tex', 'IMPLEMENTATION_HANDOFF.md',
                    'output/pdf/FINITE_PFC_DERIVATION.pdf'} or name.startswith(('data/', 'models/')) or (
                        name.startswith('assets/') and path.suffix in {'.png', '.svg'}):
            assert row['unchanged'] and row['accepted_source_sha256'] == row['public_sha256'], name
            critical.append(name)
    for row in json.loads((study / 'MANIFEST.json').read_text(encoding='utf-8'))['files']:
        data = (study / row['file']).read_bytes()
        assert len(data) == row['bytes'] and digest(data) == row['sha256'], row['file']
    with zipfile.ZipFile(study / ARCHIVE) as archive:
        assert archive.testzip() is None
        prefix = 'Embedded_PFC_Feasibility/'
        names = {name.removeprefix(prefix) for name in archive.namelist()}
        for name in archive.namelist():
            assert name.startswith(prefix) and '..' not in PurePosixPath(name).parts
            rel = name.removeprefix(prefix)
            assert digest(archive.read(name)) == digest((study / rel).read_bytes()), rel
            assert not {'tmp', 'build', '.tools', '__pycache__'}.intersection(PurePosixPath(rel).parts)
            assert not rel.endswith('.log') and rel != 'WORK_LOG.md'
            if rel.endswith('.pdf'):
                assert rel == 'output/pdf/FINITE_PFC_DERIVATION.pdf'
            if rel.endswith(('.html', '.css', '.md')):
                for link in references(rel, archive.read(name).decode('utf-8')):
                    u = urlsplit(link)
                    if u.scheme or u.netloc or not u.path:
                        continue
                    target = posixpath.normpath(posixpath.join(posixpath.dirname(rel), unquote(u.path)))
                    assert not target.startswith('../'), (rel, link)
                    if target == ARCHIVE:
                        # Download links point to the ZIP outside its own payload.
                        continue
                    assert target in names or any(x.startswith(target.rstrip('/') + '/') for x in names), (rel, link)
                    archived_links.add(target)
    logic = subprocess.run(['node', str(study / 'scripts/test_reader_logic.cjs')],
                           capture_output=True, text=True, encoding='utf-8', check=True)
    result = json.loads(logic.stdout)
    assert result['status'] == 'PASS' and result['scenarios'] >= 38
    report = {'status': 'PASS', 'scientific_files_unchanged': len(critical),
              'public_payload_files_checked': len(payload), 'local_dependencies_checked': len(checked),
              'zip_crc_and_payload_hashes': 'PASS', 'zip_relative_dependency_closure': len(archived_links),
              'reader_logic_scenarios': result['scenarios'], 'computed_selector_states': len(states),
              'declared_editorial_files': len(revised),
              'display_equations_preserved': editorial.get('equation_preservation', {}).get('count', 32),
              'scope': 'Preserved equations/data/models, declared prose revisions, moved-folder dependencies, ZIP integrity and reader logic. No new numerical solve or experimental validation.'}
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--study-directory', type=Path, default=ROOT / 'publication/site/modeling/embedded-pfc-feasibility')
    args = parser.parse_args()
    report = audit(args.study_directory)
    (args.study_directory / 'PUBLICATION_AUDIT.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'verification/embedded-pfc-publication-audit.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
