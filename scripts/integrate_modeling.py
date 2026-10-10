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

def integrate():
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
            if nav:
                a = s.new_tag('a', href='../../index.html?lang='+locale)
                a.string = 'Theory course' if locale == 'en' else '理论课程'
                nav.insert(0, a)
        for a in s.select('a[href="WORK_LOG.md"]'): a['href']='PUBLICATION.md'
        for a in s.select('a[href="models/"], a[href="resources/gui/"]'): a['href']='Minimal_Cavitation_Models_20261010.zip'
        for pane in s.select('.locale-pane'):
            nav=pane.select_one('header nav')
            if nav:
                a=s.new_tag('a',href='Minimal_Cavitation_Models_20261010.zip')
                a.string='Download modeling folder' if pane['data-locale']=='en' else '下载完整建模文件夹'
                nav.append(a)
        p.write_text(str(s), encoding='utf-8')
    (TARGET/'PUBLICATION.md').write_text('# Modeling publication\n\nCopied from the accepted 20261010 minimal-cavitation delivery on 2026-10-11. The two native MPH files and all scientific inputs, equations and results are unchanged. Reader navigation and language/theme preferences were adapted for the surrounding course. SOURCE_MANIFEST.json records the source hashes. Operational logs, reference-site snapshots and build dependencies are excluded from the public package. The native numerical and translation audits apply to the unchanged scientific content.\n', encoding='utf-8')
    old_log=TARGET/'WORK_LOG.md'
    if old_log.exists(): old_log.unlink()
    archive=TARGET/'Minimal_Cavitation_Models_20261010.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(TARGET.rglob('*')):
            if f.is_file() and f!=archive: z.write(f, 'Minimal_Cavitation_Models/'+f.relative_to(TARGET).as_posix())

    settings = json.loads((ROOT/'COURSE_SETTINGS.json').read_text(encoding='utf-8'))
    pages = [ROOT/'index.html', *(ROOT/x['file'] for x in settings['chapters']+settings['appendices']+settings['legacy_routes']), *sorted((ROOT/'reference').glob('*.html'))]
    for p in pages:
        s = BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
        relative = '' if p.parent == ROOT else '../'
        if p==ROOT/'index.html' and s.select_one('[data-modeling-link]'):
            s.select_one('.hero').insert_after(s.select_one('[data-modeling-link]').extract())
        if not s.select_one('[data-modeling-link]'):
            block = s.new_tag('section', attrs={'class':'modeling-link callout', 'data-modeling-link':'true'})
            for lang, heading, body in [
                ('en', 'Modeling: finite-energy cavitation and gel confinement', 'Follow the complete worked derivation, 53-step COMSOL guide, two native models and numerical audits. At matched 2 nJ source work and a 5 µm outlet, rigid/open-gel peak speeds are 15.376/1.625 m/s; the sealed control emits no liquid. These are initialized ideal-gas controls for expansion-driven discharge through an existing channel. Laser activation, PFC phase change, internal collapse jets, gel rupture and target impact are outside this model.'),
                ('zh-CN', '建模：有限能量空化与凝胶约束', '阅读完整推导、53 步 COMSOL 指南、两个原生模型及数值核验。在相同的 2 nJ 源功与 5 µm 出口条件下，刚性／开口凝胶的峰值速度为 15.376／1.625 m/s；密闭对照不排出液体。这些模型是以初态代表激活后气源的理想气体对照，描述经已有通道的膨胀驱动排液。激光激活、PFC 相变、内部塌缩射流、凝胶破裂及靶面冲击不在模型范围内。')]:
                div = s.new_tag('div', lang=lang)
                h = s.new_tag('h2'); h.string = heading; div.append(h)
                para = s.new_tag('p'); para.string = body; div.append(para)
                a = s.new_tag('a', href=relative+'modeling/minimal-cavitation/index.html?lang='+('en' if lang=='en' else 'zh'))
                a.string = 'Open modeling report →' if lang=='en' else '打开建模报告 →'; div.append(a)
                block.append(div)
            container = s.select_one('.chapter-header') or s.select_one('main')
            if p.name=='index.html' and s.select_one('.hero'): s.select_one('.hero').insert_after(block)
            else: container.append(block)
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
            if target and target.parent.select_one('[lang="zh-CN"]'):
                en = a.get_text(); zh = target.parent.select_one('[lang="zh-CN"]').get_text()
                a.clear()
                for lang, value in [('en', en), ('zh-CN', zh)]:
                    span = s.new_tag('span', lang=lang); span.string=value; a.append(span)
        for heading in s.select('.equation-heading'):
            for n in list(heading.children):
                if isinstance(n, NavigableString) and str(n).strip()=='/': n.extract()
        s.html['data-language']='en'
        if not s.select_one('script[src$="course-language.js"]'):
            s.head.append(s.new_tag('link', rel='stylesheet', href=relative+'assets/course-language.css'))
            s.head.append(s.new_tag('script', src=relative+'assets/course-language.js', defer=''))
        p.write_text(str(s), encoding='utf-8')
    settings['modeling']={'file':'modeling/minimal-cavitation/index.html','guide':'modeling/minimal-cavitation/STEP_BY_STEP.html','source':'20261010-minimal-cavitation','scope':'Initialized ideal-gas controls; expansion-driven discharge through an existing liquid outlet.'}
    settings['prepared']='2026-10-11'
    (ROOT/'COURSE_SETTINGS.json').write_text(json.dumps(settings, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'Integrated modeling delivery: {len(records)} copied files; {len(pages)} localized course pages')

if __name__=='__main__': integrate()
