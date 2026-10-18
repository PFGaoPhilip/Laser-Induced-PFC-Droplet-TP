"""Write the Chapter 5 figure acceptance record after the visual review."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/figures-editable/c5'

METHOD = ("All 22 SVG twins were rasterized with headless Microsoft Edge and inspected in six four-panel contact sheets; "
          "changed figures were reinspected individually. The PPTX files were reopened with python-pptx and compared with the same scene JSON. "
          "PowerPoint and LibreOffice were not available, so the PPTX files themselves were not rendered by an Office renderer.")
CHECKS = ["English live labels", "native editable geometry", "text fit and unobstructed labels",
          "geometry and direction match the local equation", "numerical labels retained",
          "data curves drawn from the copied result files", "schematic limitation declared"]

rows = []
for n in range(1, 23):
    ident = f'C5-E{n:02d}'
    rows.append({"id": ident, "scientific_acceptance": True, "visual_acceptance": True,
                 "preview": f"previews/slide-{n:03d}.png", "checks": CHECKS, "review_method": METHOD, "pending": None})
(OUT / 'visual-acceptance.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(rows))
