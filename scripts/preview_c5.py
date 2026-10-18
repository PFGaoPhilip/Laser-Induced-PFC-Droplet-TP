import os
"""Rasterize the Chapter 5 SVG twins with headless Edge for visual review (PowerPoint is not required)."""
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/figures-editable/c5'
PREV = OUT / 'previews'
EDGE = Path(os.environ.get('EDGE_PATH') or (os.environ.get('ProgramFiles(x86)', '') + '/Microsoft/Edge/Application/msedge.exe'))


def main():
    PREV.mkdir(exist_ok=True)
    images = []
    for n in range(1, 23):
        svg = OUT / f'c5-e{n:02d}.svg'
        png = PREV / f'slide-{n:03d}.png'
        subprocess.run([str(EDGE), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1280,720',
                        f'--screenshot={png}', svg.resolve().as_uri()], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        images.append(png)
    sheets = PREV / 'contact-sheets'
    sheets.mkdir(exist_ok=True)
    for k in range(0, 22, 4):
        sheet = Image.new('RGB', (2560, 1440), '#d3dbe0')
        for j, png in enumerate(images[k:k + 4]):
            im = Image.open(png).convert('RGB')
            sheet.paste(im, ((j % 2) * 1280, (j // 2) * 720))
        sheet.save(sheets / f'sheet-{k // 4 + 1:02d}.png')
    print('previews', len(images), 'sheets', (22 + 3) // 4)


if __name__ == '__main__':
    sys.exit(main())
