import os
"""Rasterize SVGs with headless Edge and build contact sheets: python scripts/sheets.py OUTDIR id1 id2 ... (ids like c1-e01)."""
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
EDGE = Path(os.environ.get('EDGE_PATH') or (os.environ.get('ProgramFiles(x86)', '') + '/Microsoft/Edge/Application/msedge.exe'))


def raster(svg, png, w=1280, h=720):
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--window-size={w},{h}',
                    f'--screenshot={png}', Path(svg).resolve().as_uri()], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    ids = sys.argv[2:]
    pngs = []
    for i in ids:
        png = out / f'{i}.png'
        raster(ROOT / 'assets/figures' / f'{i}.svg', png)
        pngs.append(png)
    per = 4
    for k in range(0, len(pngs), per):
        sheet = Image.new('RGB', (2560, 1440), '#d3dbe0')
        for j, p in enumerate(pngs[k:k + per]):
            sheet.paste(Image.open(p).convert('RGB'), ((j % 2) * 1280, (j // 2) * 720))
        sheet.save(out / f'sheet-{k // per + 1:02d}.png')
    print(len(pngs), 'figures,', (len(pngs) + per - 1) // per, 'sheets in', out)


if __name__ == '__main__':
    main()
