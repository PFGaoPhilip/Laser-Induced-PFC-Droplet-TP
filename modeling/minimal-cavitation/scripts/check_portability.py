"""Check delivered local links, rendered math and byte-identical native files.

Run against an extracted/moved package, e.g. python scripts/check_portability.py.
This is an artifact/dependency check; it does not substitute for a browser test.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()
        self.display_math = 0
        self.theme_button = False
        self.language_button = False
        self.step_checks = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        self.theme_button |= tag == 'button' and attrs.get('id') == 'theme-toggle'
        self.language_button |= tag == 'button' and attrs.get('id') == 'language-toggle'
        self.display_math += 'katex-display' in attrs.get('class', '').split()
        if tag == 'input' and attrs.get('type') == 'checkbox' and attrs.get('data-step'):
            self.step_checks.append(int(attrs['data-step']))
        for key in ('src', 'href'):
            if attrs.get(key):
                self.refs.append((attrs[key], tag == 'a'))


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    local_files = set()
    external_citations = set()
    missing = []

    def check_link(value, origin, citation=False, ids=None):
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc:
            if parsed.scheme == 'data':
                return
            if citation and parsed.scheme in ('https', 'http', 'mailto'):
                external_citations.add(value)
                return
            raise AssertionError('External runtime dependency: ' + value)
        if not parsed.path:
            if parsed.fragment and ids is not None and parsed.fragment not in ids:
                missing.append(str(origin.relative_to(root)) + ':' + value)
            return
        target = (origin.parent / unquote(parsed.path)).resolve()
        if not target.is_relative_to(root):
            raise AssertionError('Reference leaves the delivered folder: ' + value)
        if not target.exists():
            missing.append(str(origin.relative_to(root)) + ':' + value)
        else:
            local_files.add(str(target.relative_to(root)))

    pages = []
    for path in sorted(root.rglob('*.html')):
        if any(part in ('build', 'tmp', '__pycache__', 'practice', '.git')
               for part in path.relative_to(root).parts):
            continue
        page = Page()
        source = path.read_text(encoding='utf-8')
        page.feed(source)
        if not page.theme_button or not page.language_button:
            raise AssertionError('Missing language or day/night toggle: ' + str(path))
        if 'data-tex=' in source or 'katex-error' in source:
            raise AssertionError('Unrendered or failed math expression')
        for value, citation in page.refs:
            check_link(value, path, citation, page.ids)
        pages.append({'file': str(path.relative_to(root)), 'rendered_display_equations': page.display_math,
                      'day_night_button_present': page.theme_button,
                      'language_button_present': page.language_button,
                      'numbered_step_checkboxes': len(page.step_checks)})
        if path.name == 'STEP_BY_STEP.html':
            if page.step_checks != list(range(1, 54))*2 or not all(
                    f'{locale}-step-{n:02d}' in page.ids for locale in ('en','zh') for n in range(1, 54)):
                raise AssertionError('Expected 53 complete guide cards in each language')
    expected = {'index.html': 58, 'STEP_BY_STEP.html': 0}
    if {p['file']: p['rendered_display_equations'] for p in pages} != expected:
        raise AssertionError('Expected the reader with 29 equations and the complete GUI guide')

    for path in root.glob('assets/**/*.css'):
        for value in re.findall(r'url\(([^)]+)\)', path.read_text(encoding='utf-8')):
            check_link(value.strip(' \"\''), path)
    for path in root.glob('*.md'):
        source = path.read_text(encoding='utf-8')
        if any(ord(c) < 32 and c not in '\n\r\t' for c in source):
            raise AssertionError('Nonprinting source character: ' + path.name)
        for value in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', source):
            check_link(value, path, citation=True)
    if missing:
        raise AssertionError('Missing local dependencies: ' + repr(missing))

    audit = json.loads((root / 'verification/NUMERICAL_AUDIT.json').read_text(encoding='utf-8'))
    native = []
    for row in audit['native_files']:
        path = root / 'models' / row['file']
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != row['sha256'] or path.stat().st_size != row['bytes']:
            raise AssertionError('Native model differs from the final audited file: ' + path.name)
        native.append({'file': path.name, 'bytes': path.stat().st_size, 'sha256': digest})
    if len(native) != 2 or audit['status'] != 'PASS':
        raise AssertionError('Two accepted native files required')
    record = root / 'verification/GUIDE_NATIVE_IMPORT_CHECK.txt'
    required = ('PASS_A_IMPORT', 'PASS_B_PATCH_AND_CONVERSION', 'PASS_B_FULL_IMPORT',
                'GUIDE_NATIVE_IMPORT_CONVERSION_COMPLETE')
    if not record.is_file() or not all(marker in record.read_text(encoding='utf-8-sig') for marker in required):
        raise AssertionError('Missing completed native import/conversion evidence')
    previous_path = root / 'verification/PORTABILITY_AUDIT.json'
    previous = json.loads(previous_path.read_text(encoding='utf-8')) if previous_path.is_file() else {}
    dom_path = root / 'verification/READER_DOM_AUDIT.json'
    dom_audit = json.loads(dom_path.read_text(encoding='utf-8')) if dom_path.is_file() else {}
    results = {'status': 'PASS', 'scope': 'Static dependencies, complete math rendering and native-file integrity',
               'html': pages, 'local_dependency_count': len(local_files),
               'external_links': sorted(external_citations), 'native_files': native,
               'guide_native_import_conversion': 'Completed record included; see GUIDE_NATIVE_IMPORT_CHECK.txt. This static check does not rerun COMSOL.',
               'browser_visual_validation': 'NOT_RUN_BY_THIS_SCRIPT. Current real-browser checks are recorded separately by the course revision.',
               'historical_DOM_browser_note': dom_audit.get('browser_visual_validation', 'No historical note included.')}
    if previous.get('native_files') == native:
        if 'moved_native_reload' in previous:
            results['moved_native_reload'] = previous['moved_native_reload']
        for key in ('moved_folder_test', 'moved_reader_regeneration', 'moved_guide_regeneration'):
            old = 'pre_bilingual_' + key
            if old in previous or key in previous:
                results[old] = previous.get(old, previous.get(key))
    moved_path = root / 'verification/BILINGUAL_RELOCATION_AUDIT.json'
    if moved_path.is_file():
        moved = json.loads(moved_path.read_text(encoding='utf-8'))
        results['historical_bilingual_relocation'] = {'status': moved['status'], 'record': moved_path.name,
                                                    'scope': 'Earlier edition; current relocation is checked separately.'}
    (root / 'verification/PORTABILITY_AUDIT.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
