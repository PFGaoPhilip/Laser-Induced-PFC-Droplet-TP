"""Build equation figures for one chapter: python scripts/build_figs.py c1 [n n ...]

Writes scene JSON, SVG and PPTX into the figure group folder and copies the SVG into assets/figures.
"""
import importlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
GROUP = {'c1': 'c1-c2', 'c2': 'c1-c2', 'c3': 'c3-c4', 'c4': 'c3-c4', 'a': 'appendix-studies'}
PREFIX = {'c1': 'C1', 'c2': 'C2', 'c3': 'C3', 'c4': 'C4', 'a': 'A'}


def kinds():
    eq = json.loads((ROOT / 'verification/equations.json').read_text(encoding='utf-8'))
    return {e['id']: e['kind'] for e in eq}


def main():
    from figlib import Fig
    from sci_ppt_common import scene_to_svg, render_scene
    ch = sys.argv[1]
    only = [int(a) for a in sys.argv[2:]]
    mod = importlib.import_module('figs_' + ch)
    out = ROOT / 'assets/figures-editable' / GROUP[ch]
    out.mkdir(parents=True, exist_ok=True)
    (ROOT / 'assets/figures').mkdir(exist_ok=True)
    kind = kinds()
    bad = 0
    for n, fn in sorted(mod.FIGS.items()):
        if only and n not in only:
            continue
        ident = f'{PREFIX[ch]}-E{n:02d}'
        f = Fig(ident, kind[ident])
        fn(f)
        for w in f.check():
            print('WARN', ident, w)
            bad += 1
        scene = f.scene()
        key = ident.lower()
        (out / f'{key}.scene.json').write_text(json.dumps(scene, ensure_ascii=False, indent=1), encoding='utf-8')
        scene_to_svg(scene, out / f'{key}.svg')
        render_scene(scene, out / f'{key}.pptx')
        shutil.copy2(out / f'{key}.svg', ROOT / 'assets/figures' / f'{key}.svg')
    print('built', len([n for n in mod.FIGS if not only or n in only]), 'figures;', bad, 'warnings')


if __name__ == '__main__':
    main()
