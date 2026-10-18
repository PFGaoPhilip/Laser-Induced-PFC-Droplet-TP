"""Copy the accepted modeling delivery and prepare separate course language views."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import os
import zipfile
from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'LEARN_20260929/modeling/20261010-minimal-cavitation'
TARGET = ROOT / 'modeling/minimal-cavitation'

def copy_modeling():
    # Copy the supplied, already verified delivery without changing the accepted models.
    records = []
    source_files=[]
    for directory, folders, files in os.walk(SOURCE):
        folders[:]=[x for x in folders if x not in ('build','tmp','__pycache__','practice','.git')]
        if Path(directory)==SOURCE/'sources': folders[:]=[x for x in folders if x in ('guide','i18n')]
        source_files.extend(Path(directory)/x for x in files)
    for path in sorted(source_files):
        rel = path.relative_to(SOURCE)
        if not path.is_file() or any(x in ('build', 'tmp', '__pycache__', 'practice', '.git') for x in rel.parts):
            continue
        if path.suffix in ('.class', '.pyc', '.zip') or path.name == 'WORK_LOG.md' or path.name.endswith(('.log', '.lock', '.recovery')):
            continue
        dest = TARGET / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        records.append({'path': rel.as_posix(), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    if records:
        (TARGET / 'SOURCE_MANIFEST.json').write_text(json.dumps({'source_project': '20261010-minimal-cavitation', 'copied_files': records}, indent=2)+'\n', encoding='utf-8')
    # Readers share language/theme choices with the surrounding theory course.
    theme = TARGET / 'assets/theme.js'
    js = theme.read_text(encoding='utf-8').replace("'minimal-cavitation-language-v1'", "'laser-pfc-tp-language'")
    js = js.replace("chooseLanguage(stored(languageKey,'zh'),false)", "chooseLanguage(new URLSearchParams(location.search).get('lang')||stored(languageKey,'en'),false)")
    js = js.replace("root.dataset.theme=stored(themeKey,'night')==='day'?'day':'night';", "root.dataset.theme=(new URLSearchParams(location.search).get('theme')==='light'||stored('laser-pfc-tp-theme','dark')==='light')?'day':'night';")
    js = js.replace("remember(themeKey,root.dataset.theme);labels()", "remember(themeKey,root.dataset.theme);remember('laser-pfc-tp-theme',root.dataset.theme==='day'?'light':'dark');labels()")
    theme.write_text(js, encoding='utf-8')
    for name in ('index.html', 'STEP_BY_STEP.html'):
        p = TARGET/name
        s = BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
        for pane in s.select('.locale-pane'):
            locale = pane['data-locale']
            nav = pane.select_one('header nav')
            if nav and not nav.select_one('a[href^="../../index.html"]'):
                a = s.new_tag('a', href='../../index.html?lang='+locale)
                a.string = 'Theory course' if locale == 'en' else '理论课程'
                nav.insert(0, a)
        for a in s.select('a[href="WORK_LOG.md"]'): a['href']='PUBLICATION.md'
        for a in s.select('a[href="models/"], a[href="resources/gui/"]'): a['href']='Minimal_Cavitation_Models_20261010.zip'
        for pane in s.select('.locale-pane'):
            nav=pane.select_one('header nav')
            if nav and not nav.select_one('a[href="Minimal_Cavitation_Models_20261010.zip"]'):
                a=s.new_tag('a',href='Minimal_Cavitation_Models_20261010.zip')
                a.string='Download modeling folder' if pane['data-locale']=='en' else '下载完整建模文件夹'
                nav.append(a)
        p.write_text(str(s), encoding='utf-8', newline='\n')
    (TARGET/'PUBLICATION.md').write_text('# Modeling publication\n\nCopied from the accepted 20261010 minimal-cavitation delivery on 2026-10-11. The two native MPH files and all scientific inputs, equations and results are unchanged. Reader navigation and language/theme preferences were adapted for the surrounding course. SOURCE_MANIFEST.json records the source hashes. Operational logs, reference-site snapshots and build dependencies are excluded from the public package. The native numerical and translation audits apply to the unchanged scientific content.\n', encoding='utf-8')
    old_log=TARGET/'WORK_LOG.md'
    if old_log.exists(): old_log.unlink()
    archive=TARGET/'Minimal_Cavitation_Models_20261010.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(TARGET.rglob('*')):
            if f.is_file() and f!=archive: z.write(f, 'Minimal_Cavitation_Models/'+f.relative_to(TARGET).as_posix())

    return len(records)

def language_label(soup, node, en, zh):
    """Replace a label from authoritative text, never from a prior rendered label."""
    spans=node.find_all('span',recursive=False)
    if (len(spans)==2 and [n.get('lang') for n in spans]==['en','zh-CN']
            and [n.get_text() for n in spans]==[en,zh]
            and not any(isinstance(n,NavigableString) and str(n).strip() for n in node.children)):
        return
    node.clear()
    for lang, text in [('en', en), ('zh-CN', zh)]:
        span=soup.new_tag('span', lang=lang)
        span.string=text
        node.append(span)

def integrate(include_modeling=True):
    copied=copy_modeling() if include_modeling else 0
    settings = json.loads((ROOT/'COURSE_SETTINGS.json').read_text(encoding='utf-8'))
    pages = [ROOT/'index.html', *(ROOT/x['file'] for x in settings['chapters']+settings['appendices']+settings['legacy_routes']), *sorted((ROOT/'reference').glob('*.html'))]
    for p in pages:
        s = BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
        relative = '' if p.parent == ROOT else '../'
        banner=s.select_one('.home-header .eyebrow, .hero .eyebrow')
        if banner:
            language_label(s,banner,'PROJECT-CENTERED THEORY · FIVE CHAPTERS + APPENDIX A',
                           '项目导向理论 · 五章 + 附录 A')
        sidebar=s.select_one('.sidebar')
        if sidebar:
            for node, labels in zip(sidebar.find_all('h2',recursive=False),
                                    [('Course','课程'),('In this unit','本单元内容')]):
                language_label(s,node,*labels)
            for a in sidebar.select('nav:not(.toc) a[href]'):
                route=a['href'].split('?')[0].removeprefix('../')
                unit=next((u for u in settings['chapters']+settings['appendices'] if u['file']==route),None)
                if unit:
                    language_label(s,a,unit['label']+' · '+unit['title'],unit['label_zh']+' · '+unit['title_zh'])
        header=s.select_one('.chapter-header .eyebrow')
        if header:
            route=p.relative_to(ROOT).as_posix()
            unit=next((u for u in settings['chapters']+settings['appendices'] if u['file']==route),None)
            if not unit and route in {x['file'] for x in settings['legacy_routes']}:unit=settings['appendices'][0]
            if unit:
                language_label(s,header,unit['label']+' · THEORY → DERIVATION → DEFENSE',
                               unit['label_zh']+' · 理论 → 推导 → 答辩')
        for block in s.select('[data-modeling-link], [data-embedded-pfc-link], [data-resolver-progress]'):
            block.decompose()
        # Language-tag bilingual UI text without disturbing math or scientific prose.
        for node in list(s.find_all(string=True)):
            if not node.parent or any(x.name in ('script','style','math','svg') or (x.has_attr('lang') and x.name!='html') for x in node.parents):
                continue
            text = str(node)
            if ' / ' not in text or not re.search('[\u4e00-\u9fff]', text):
                continue
            en, zh = text.split(' / ', 1)
            # Keep shared arrow/section suffixes in both localized labels.
            if ' · ' in zh:
                zh, suffix = zh.split(' · ', 1)
                en += ' · '+suffix
            a = s.new_tag('span', lang='en'); a.string = en
            b = s.new_tag('span', lang='zh-CN'); b.string = zh
            node.replace_with(a, b)
        for a in s.select('.toc a[href^="#"]'):
            target = s.find(id=a['href'][1:])
            translation=target.parent.find(target.name,attrs={'lang':'zh-CN'},recursive=False) if target else None
            if target and translation:
                language_label(s,a,target.get_text(),translation.get_text())
        for heading in s.select('.equation-heading'):
            for n in list(heading.children):
                if isinstance(n, NavigableString) and str(n).strip()=='/': n.extract()
        s.html['data-language']='en'
        if not s.select_one('script[src$="course-language.js"]'):
            s.head.append(s.new_tag('link', rel='stylesheet', href=relative+'assets/course-language.css'))
            s.head.append(s.new_tag('script', src=relative+'assets/course-language.js', defer=''))
        p.write_text(str(s), encoding='utf-8', newline='\n')
    settings['modeling']={'parent_unit':'A','file':'modeling/minimal-cavitation/index.html','guide':'modeling/minimal-cavitation/STEP_BY_STEP.html','source':'20261010-minimal-cavitation','scope':'Initialized ideal-gas controls; expansion-driven discharge through an existing liquid outlet.'}
    settings['prepared']='2026-10-14'
    (ROOT/'COURSE_SETTINGS.json').write_text(json.dumps(settings, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'Integrated modeling delivery: {copied} copied files; {len(pages)} localized course pages')
    if (ROOT/'assets/figures-editable/manifest.json').is_file():
        from integrate_english_figures import integrate as integrate_english
        integrate_english()

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--course-only',action='store_true',help='Update language views without recopying the accepted modeling delivery')
    parser.add_argument('--refresh-source',action='store_true',help='Explicitly replace the local study with its accepted source delivery')
    args=parser.parse_args()
    integrate(include_modeling=args.refresh_source and not args.course_only)
