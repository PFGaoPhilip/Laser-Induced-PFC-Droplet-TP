"""Embed reviewed SCI-PPT English figures and build their offline gallery."""
from pathlib import Path
from html import escape
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/figures-editable'


def integrate():
    rows = []
    for group in ('c1-c2', 'c3-c4', 'c5', 'appendix-studies'):
        folder = BASE / group
        accepted = folder / ('acceptance.json' if group == 'c1-c2' else 'visual-acceptance.json')
        if not accepted.exists():
            raise RuntimeError('Missing visual acceptance: ' + str(accepted))
        for scene in sorted(folder.glob('*.scene.json')):
            ident = scene.name.removesuffix('.scene.json')
            data = json.loads(scene.read_text(encoding='utf-8'))
            text = ' '.join(str(o.get('text','')) for o in data['objects'])
            assert not re.search(r'[\u3400-\u9fff]', text), ident
            row = {'id': ident, 'group': group,
                   'svg': f'{group}/{ident}.svg', 'pptx': f'{group}/{ident}.pptx',
                   'scene': f'{group}/{ident}.scene.json'}
            assert all((BASE / row[k]).is_file() for k in ('svg','pptx','scene'))
            rows.append(row)
            if re.fullmatch(r'(?:c[1-5]|a)-e\d+', ident):
                shutil.copy2(BASE / row['svg'], ROOT / 'assets/figures' / (ident+'.svg'))
    assert len(rows) == 199, len(rows)
    appendix = json.loads((BASE/'appendix-studies/manifest.json').read_text(encoding='utf-8'))
    studies = [r for r in appendix if not r['id'].startswith('a-e')]
    for page in ('modeling/minimal-cavitation/index.html',
                 'modeling/minimal-cavitation/STEP_BY_STEP.html',
                 'modeling/embedded-pfc-feasibility/index.html'):
        path = ROOT/page
        content = path.read_text(encoding='utf-8')
        for row in studies:
            source = Path(row['source'])
            if source.parent.parent != Path(page).parent:
                continue
            stem = source.stem
            target = '../../assets/figures-editable/appendix-studies/'+row['id']+'.svg'
            content = re.sub(r'assets/'+re.escape(stem)+r'(?:\.zh)?\.(?:svg|png)',target,content)
            # The figure itself is English in both course language modes.
            content = re.sub(r'<img\b[^>]*src="'+re.escape(target)+r'"[^>]*>',
                             lambda m:re.sub(r'alt="[^"]*"',
                                 'alt="'+escape(stem.replace('_',' ').replace('-',' '))+'"',m[0]),content)
        path.write_text(content,encoding='utf-8')
    (BASE/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
    cards = []
    for r in rows:
        title = r['id'].upper() if re.fullmatch(r'(?:c[1-5]|a)-e\d+', r['id']) else r['id'].replace('_',' ')
        cards.append(f'<article id="{r["id"]}"><h2>{escape(title)}</h2><img loading="lazy" src="{r["svg"]}" alt="{escape(title)}"><p><a href="{r["pptx"]}">Editable PowerPoint</a> · <a href="{r["svg"]}">SVG</a> · <a href="{r["scene"]}">Scene JSON</a></p></article>')
    html = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>English lesson figures</title>
<style>:root{color-scheme:light;--bg:#f4f6f8;--fg:#142632;--card:#fff}body.dark{color-scheme:dark;--bg:#142632;--fg:#e7f0f3;--card:#213e4b}body{background:var(--bg);color:var(--fg);font:17px Arial,sans-serif;max-width:1280px;margin:auto;padding:24px}a{color:inherit}header{position:sticky;top:0;background:var(--bg);padding:12px;z-index:1}button,input{font:inherit;padding:8px}article{background:var(--card);padding:18px;margin:24px 0;border:1px solid #899ba5;border-radius:8px}img{display:block;width:100%;height:auto}h2{font-size:22px}</style>
<header><button id="theme">Day / night</button> <input id="search" placeholder="Filter figure IDs" aria-label="Filter figure IDs"><p>199 English figures · 189 equation diagrams · 10 study figures.</p></header><h1>English lesson figures</h1><p>Native editable PowerPoint objects accompany every SVG. Physical conventions and actual PowerPoint previews were reviewed before embedding. Quantitative charts retain the accepted source data. Diagrams state their model assumptions.</p>'''+''.join(cards)+'''<script>const b=document.body;b.classList.toggle('dark',localStorage.figureTheme==='dark');document.querySelector('#theme').onclick=()=>{b.classList.toggle('dark');localStorage.figureTheme=b.classList.contains('dark')?'dark':'light'};document.querySelector('#search').oninput=e=>document.querySelectorAll('article').forEach(a=>a.hidden=!a.id.includes(e.target.value.toLowerCase()));</script></html>'''
    (BASE/'index.html').write_text(html,encoding='utf-8')
    return rows


if __name__ == '__main__':
    print(json.dumps({'embedded':len(integrate())}))
