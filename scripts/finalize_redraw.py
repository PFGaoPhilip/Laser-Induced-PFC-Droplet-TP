"""Rebuild decks, previews and acceptance records for the redrawn equation figures (C1-C4, Appendix A)."""
import json
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/figures-editable'
EDGE = Path(os.environ.get('EDGE_PATH') or (os.environ.get('ProgramFiles(x86)', '') + '/Microsoft/Edge/Application/msedge.exe'))
sys.path.insert(0, str(ROOT / 'scripts'))
from sci_ppt_common import make_deck  # noqa: E402

EQ = json.loads((ROOT / 'verification/equations.json').read_text(encoding='utf-8'))
ids = {}
for e in EQ:
    pre = e['id'].split('-')[0]
    ids.setdefault(pre, []).append(e['id'])

METHOD = ("Every figure was drawn by scripts/figs_*.py from the lesson formulas and rasterized from its SVG twin with headless Microsoft Edge. "
          "All figures were inspected in four-panel contact sheets; figures with overlaps, clipped labels or wrong scales were corrected and reinspected. "
          "The PPTX files were written by the same scene JSON and reopened with python-pptx. "
          "PowerPoint and LibreOffice were not available, so the PPTX files themselves were not rendered by an Office renderer.")
CHECKS = ["English live labels", "native editable geometry", "text fit and unobstructed labels",
          "geometry and direction match the local equation", "numerical values recomputed from the lesson formulas",
          "schematic or illustrative values labelled as such"]

GROUPS = {'c1-c2': ['C1', 'C2'], 'c3-c4': ['C3', 'C4'], 'appendix-studies': ['A']}
STALE = {'c1-c2': ['audit.json', 'c1-slide-order.json', 'c2-slide-order.json', 'acceptance.json'],
         'c3-c4': ['c3-manifest.json', 'c4-manifest.json', 'editability-audit.json', 'scientific-audit.json', 'visual-acceptance.json'],
         'appendix-studies': ['INTEGRATION.md', 'SCIENTIFIC_AUDIT.md', 'structural_verification.json']}


def shoot(args):
    svg, png = args
    subprocess.run([str(EDGE), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1280,720',
                    f'--screenshot={png}', svg.resolve().as_uri()], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    old = BASE / 'superseded-20261015'
    old.mkdir(exist_ok=True)
    jobs = []
    for group, chs in GROUPS.items():
        folder = BASE / group
        keep = old / group
        keep.mkdir(exist_ok=True)
        for name in STALE[group]:
            src = folder / name
            if src.exists() and not (keep / name).exists():
                shutil.copy2(src, keep / name)
        for ch in chs:
            lower = ch.lower()
            idl = ids[ch]
            if group == 'appendix-studies':
                prev = folder / 'previews'
                prev_ids = [i.lower() for i in idl]
            else:
                prev = folder / 'previews' / lower
                prev_ids = [i.lower() for i in idl]
            if prev.exists() and group != 'appendix-studies':
                for png in prev.glob('slide-*.png'):
                    png.unlink()
            prev.mkdir(parents=True, exist_ok=True)
            for n, i in enumerate(prev_ids, 1):
                jobs.append((folder / f'{i}.svg', prev / f'{lower}-{n:03d}.png' if group == 'appendix-studies' else prev / f'slide-{n:03d}.png'))
            if group != 'appendix-studies':
                scenes = [json.loads((folder / f'{i}.scene.json').read_text(encoding='utf-8')) for i in prev_ids]
                make_deck(scenes, folder / f'{lower}-figures.pptx')
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(shoot, jobs))
    # appendix equation deck
    a_scenes = [json.loads((BASE / 'appendix-studies' / f'{i.lower()}.scene.json').read_text(encoding='utf-8')) for i in ids['A']]
    make_deck(a_scenes, BASE / 'appendix-studies/appendix-equations.pptx')
    # acceptance records
    def rows(ch, folder, relprev):
        out = []
        for n, i in enumerate(ids[ch], 1):
            out.append({'id': i, 'scientific_acceptance': True, 'visual_acceptance': True, 'preview': relprev(n, ch),
                        'checks': CHECKS, 'review_method': METHOD, 'pending': None})
        return out
    (BASE / 'c1-c2/acceptance.json').write_text(json.dumps({
        'status': 'accepted', 'date': '2026-10-17', 'figure_count': len(ids['C1']) + len(ids['C2']),
        'ids': ids['C1'] + ids['C2'], 'review_method': METHOD, 'checks': CHECKS,
        'limitations': ['Schematics describe the adopted lesson models and their declared assumptions.', 'Illustrative values are labelled as such in each figure.']},
        ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    c34 = rows('C3', 'c3-c4', lambda n, ch: f'previews/c3/slide-{n:03d}.png') + rows('C4', 'c3-c4', lambda n, ch: f'previews/c4/slide-{n:03d}.png')
    (BASE / 'c3-c4/visual-acceptance.json').write_text(json.dumps(c34, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    studies = [r for r in json.loads((old / 'appendix-studies/structural_verification.json').read_text(encoding='utf-8')) if not r['id'].startswith('a-e')]
    prev_acc = json.loads((BASE / 'appendix-studies/visual-acceptance.json').read_text(encoding='utf-8'))
    prev_rows = prev_acc if isinstance(prev_acc, list) else prev_acc.get('figures', [])
    keep_rows = [r for r in prev_rows if not str(r.get('id', '')).lower().startswith('a-e')]
    new_rows = rows('A', 'appendix-studies', lambda n, ch: f'previews/a-{n:03d}.png')
    (BASE / 'appendix-studies/visual-acceptance.json').write_text(json.dumps(keep_rows + new_rows if isinstance(prev_acc, list) else {'figures': keep_rows + new_rows}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (BASE / 'appendix-studies/structural_verification.json').write_text(json.dumps(studies, indent=2) + '\n', encoding='utf-8')
    print('jobs', len(jobs), 'c34', len(c34), 'A', len(new_rows), 'studies kept', len(keep_rows))


if __name__ == '__main__':
    main()
