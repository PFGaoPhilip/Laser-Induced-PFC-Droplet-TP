"""Audit lesson placement, preserved science, translations, and local links."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import ast
import hashlib
import json
import re
from bs4 import BeautifulSoup

AUTHORING = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(root):
    settings = json.loads((root / 'COURSE_SETTINGS.json').read_text(encoding='utf-8'))
    baseline = json.loads((root / 'verification/lesson-revision-baseline.json').read_text(encoding='utf-8'))
    equations = json.loads((root / 'verification/equations.json').read_text(encoding='utf-8'))
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    check({e['id']: e['tex'] for e in equations} == baseline['equations'],
          'Chapter equation formulas changed.')
    for name, expected in baseline['native_models'].items():
        check(sha(root / name) == expected, 'Native model changed: ' + name)
    if (root / 'learning-records/progress.json').is_file():
        units = json.loads((root / 'learning-records/progress.json').read_text(encoding='utf-8'))['units']
        check(units == baseline['learning_units'], 'Learning-unit evidence changed.')
    pages = [Path('index.html'), *(Path(u['file']) for u in settings['chapters'] + settings['appendices']),
             Path('chapters/05-hydrogel-versus-liquid.html'),
             *[p.relative_to(root) for p in (root / 'reference').glob('*.html')],
             Path('learning-records/resolver-progress/index.html'),
             Path('modeling/minimal-cavitation/index.html'),
             Path('modeling/minimal-cavitation/STEP_BY_STEP.html'),
             Path('modeling/embedded-pfc-feasibility/index.html')]
    documents = {p: BeautifulSoup((root / p).read_text(encoding='utf-8'), 'html.parser') for p in pages}
    canonical_css_hash = sha(root / 'assets/course.css')
    frontend_parts = ['.topbar', '.page-layout', '.sidebar', '.reading',
                      '.chapter-header', '.chapter-body', '.site-footer']
    for name, doc in documents.items():
        for selector in frontend_parts:
            check(doc.select_one(selector) is not None,
                  str(name) + ': missing shared chapter component ' + selector)
        shared_styles = [node for node in doc.select('link[rel="stylesheet"][href]')
                         if urlsplit(node['href']).path.endswith('/course.css')]
        check(len(shared_styles) == 1, str(name) + ': needs one canonical course stylesheet.')
        for node in shared_styles:
            css_path = (root / name).parent / unquote(urlsplit(node['href']).path)
            check(css_path.is_file() and sha(css_path) == canonical_css_hash,
                  str(name) + ': course stylesheet differs from Chapter 1.')
    home = documents[Path('index.html')]
    core_pages = pages[:10]
    for name in core_pages:
        check(not documents[name].select('[data-resolver-progress], [data-modeling-link], [data-embedded-pfc-link]'),
              str(name) + ': obsolete banner remains.')
    resolver_card = next((c for c in home.select('.chapter-card')
                          if c.select_one('a[href="chapters/03-arrays-finite-jets-and-impact.html"]')), None)
    appendix_card = next((c for c in home.select('.chapter-card')
                         if c.select_one('a[href="appendices/90-hydrogel-versus-liquid.html"]')), None)
    check(resolver_card is not None and resolver_card.select_one('a[href*="resolver-progress"]') is not None,
          'Chapter 3 card lacks the resolver resource.')
    check(appendix_card is not None and len(appendix_card.select('a[href*="modeling/"]')) == 4,
          'Appendix A card lacks both translated modeling resources.')
    owners = [('chapters/03-arrays-finite-jets-and-impact.html', ['resolver-work']),
              ('appendices/90-hydrogel-versus-liquid.html', ['finite-energy-models', 'embedded-pfc-study'])]
    for name, anchors in owners:
        doc = documents[Path(name)]
        for anchor in anchors:
            check(doc.select_one('.chapter-body #' + anchor) is not None, name + ': missing section ' + anchor)
            check(doc.select_one('.toc a[href="#' + anchor + '"]') is not None, name + ': missing contents entry ' + anchor)
    check(settings.get('resource_ownership') == {'resolver': 'C03', 'minimal_cavitation': 'A', 'embedded_pfc': 'A'},
          'Resource ownership metadata differs.')
    publication_status=settings['resolver_progress']['publication_status']
    if publication_status!='HELD_NOT_PUBLISHED':
        authorization=json.loads((root / settings['publication_authorization']['record']).read_text(encoding='utf-8'))
        check(publication_status=='OWNER_AUTHORIZED_GITHUB_RELEASE' and authorization.get('status')=='AUTHORIZED'
              and authorization.get('owner_instruction')=='Update to GitHub.'
              and authorization.get('repository')==settings['repository'], 'Publication lacks owner authorization.')
    link_count = 0
    anchors = {p.resolve(): {n['id'] for n in doc.select('[id]')} for p, doc in
               ((root / name, doc) for name, doc in documents.items())}
    for name, doc in documents.items():
        path = root / name
        check(doc.select_one('script[src*="theme"], #theme-toggle') is not None, str(name) + ': no theme control.')
        check('katex-error' not in str(doc), str(name) + ': math rendering error.')
        check(len(doc.select('[id]')) == len({n['id'] for n in doc.select('[id]')}), str(name) + ': duplicate anchors.')
        for node in doc.select('[href], [src]'):
            link = node.get('href', node.get('src', ''))
            url = urlsplit(link)
            if url.scheme or url.netloc:
                runtime_asset = (node.name in {'script', 'img'} or
                                 node.name == 'link' and bool(
                                     {'stylesheet', 'preload', 'modulepreload'}.intersection(node.get('rel', []))))
                if runtime_asset:
                    check(url.scheme == 'data', str(name) + ': essential remote asset ' + link)
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            if not url.path and not url.fragment:
                continue
            link_count += 1
            check(target.is_relative_to(root.resolve()) and target.exists(), str(name) + ': missing local link ' + link)
            if target.exists() and url.fragment and target.suffix == '.html':
                if target not in anchors:
                    target_doc = BeautifulSoup(target.read_text(encoding='utf-8'), 'html.parser')
                    anchors[target] = {n['id'] for n in target_doc.select('[id]')}
                check(unquote(url.fragment) in anchors[target], str(name) + ': missing anchor ' + link)
    study = documents[Path('modeling/embedded-pfc-feasibility/index.html')]
    check(study.select_one('[lang="en"]') is not None and study.select_one('[lang="zh-CN"]') is not None,
          'Embedded reader lacks both languages.')
    check(study.select_one('#language-toggle, #language, #language-select, [data-language-choice]') is not None,
          'Embedded reader lacks a language control.')
    inputs = json.loads((root / 'learning-records/resolver-progress/INPUT_MANIFEST.json').read_text(encoding='utf-8'))['copies']
    for row in inputs:
        check(sha(root / 'learning-records/resolver-progress' / row['copy']) == row['sha256'],
              'Sealed resolver input changed: ' + row['copy'])
    for path in (root / 'scripts').glob('*.py'):
        ast.parse(path.read_text(encoding='utf-8'))
    report = {'status': 'passed' if not errors else 'failed', 'reader_pages': len(pages),
              'unified_frontend_pages': len(pages),
              'learning_record_checked': (root / 'learning-records/progress.json').is_file(),
              'local_links_checked': link_count, 'chapter_equations_preserved': len(equations),
              'native_models_preserved': len(baseline['native_models']),
              'sealed_resolver_inputs_preserved': len(inputs), 'errors': errors,
              'scope': 'Placement, local dependencies, math rendering, source syntax, and preserved evidence. Browser interaction is checked separately.'}
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=AUTHORING)
    parser.add_argument('--output', type=Path, default=AUTHORING / 'verification/lesson-revision-audit.json')
    args = parser.parse_args()
    report = audit(args.root.resolve())
    args.output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report))
    assert not report['errors'], report['errors']


if __name__ == '__main__':
    main()
