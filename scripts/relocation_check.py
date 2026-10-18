"""Unzip the forwarded lesson into a different folder and load pages in headless Edge."""
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = sys.argv[1]
EDGE = os.environ.get('EDGE_PATH') or (os.environ.get('ProgramFiles(x86)', '') + '/Microsoft/Edge/Application/msedge.exe')
dest = ROOT / 'tmp' / 'relocated copy'
if dest.exists():
    shutil.rmtree(dest)
dest.mkdir(parents=True)
with zipfile.ZipFile(ROOT / 'delivery' / (NAME + '.zip')) as z:
    z.extractall(dest)
base = dest / NAME
SCRIPT = """<script>window.addEventListener('load',function(){setTimeout(function(){
var imgs=[].slice.call(document.images).filter(function(i){return i.src.indexOf('katex')<0});
var bad=imgs.filter(function(i){return !(i.complete&&i.naturalWidth>0)}).map(function(i){return i.getAttribute('src')});
var o={title:document.title,imgs:imgs.length,badImgs:bad,sheets:document.styleSheets.length,
theme:!!document.getElementById('theme-toggle'),lang:!!document.getElementById('language-toggle')||!!document.querySelector('[data-language-toggle],#lang-toggle,.language-toggle'),
katexErr:document.querySelectorAll('.katex-error').length,eq:document.querySelectorAll('.equation-unit').length,
dataTheme:document.documentElement.getAttribute('data-theme'),buttons:[].slice.call(document.querySelectorAll('button')).map(function(b){return b.id+':'+b.textContent.trim()}).slice(0,6)};
var p=document.createElement('pre');p.id='rc';p.textContent=JSON.stringify(o);document.body.appendChild(p);},2000);});</script>"""
pages = ['index.html', 'chapters/05-jet-on-rigid-wall.html', 'chapters/03-arrays-finite-jets-and-impact.html',
         'appendices/90-hydrogel-versus-liquid.html', 'appendices/a-hydrogel-versus-liquid.html',
         'chapters/05-hydrogel-versus-liquid.html', 'reference/defense.html', 'reference/sources.html']
results = {}
for rel in pages:
    src = base / rel
    html = src.read_text(encoding='utf-8').replace('</body>', SCRIPT + '</body>')
    tmp = src.with_name('_rc_' + src.name)
    tmp.write_text(html, encoding='utf-8')
    out = subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--window-size=1400,1000', '--virtual-time-budget=8000',
                          '--dump-dom', tmp.resolve().as_uri() + '?theme=light&lang=zh'], capture_output=True, text=True, encoding='utf-8')
    tmp.unlink()
    m = re.search(r'<pre id="rc">(.*?)</pre>', out.stdout, re.S)
    results[rel] = json.loads(m.group(1).replace('&quot;', '"').replace('&amp;', '&')) if m else 'NO RESULT'
    print(rel, json.dumps(results[rel], ensure_ascii=False)[:330])
(ROOT / 'verification' / ('relocation-check-' + NAME + '.json')).write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
