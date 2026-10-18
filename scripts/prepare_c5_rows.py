"""Register Chapter 5 local symbol rows, Chinese equation titles and glossary hook.

Idempotent. Run before scripts/build_course.py whenever content/chapter05_spec.py changes.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'content'))
from chapter05_spec import EQS  # noqa: E402


def unit_text(unit, zh):
    if unit == '1':
        return '无量纲' if zh else 'dimensionless'
    return unit


def row(symbol, en, zh, unit):
    tail_en = '' if unit in ('defined in text', 'mixed') else f' ({unit_text(unit, False)})'
    tail_zh = '' if unit in ('defined in text', 'mixed') else f'（{unit_text(unit, True)}）'
    return dict(symbol=symbol, en=f'${symbol}$ — {en}{tail_en}', zh=f'${symbol}$ — {zh}{tail_zh}',
                unit=unit, source_en=None, source_zh=None,
                review='Individual definition written for Chapter 5.')


def main():
    path = ROOT / 'content/equation_symbol_rows.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    for key in [k for k in data if k.startswith('C5-')]:
        del data[key]
    for e in EQS:
        ident = f"C5-E{e['n']:02d}"
        rows = [row(*r) for r in e['rows']]
        data[ident] = dict(rows=rows, notes_en=e['notes_en'], notes_zh=e['notes_zh'],
                           source_fragments_en=[], source_fragments_zh=[],
                           expanded_groups_en=[], expanded_groups_zh=[])
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    titles = ROOT / 'scripts/equation_titles.py'
    text = titles.read_text(encoding='utf-8')
    text = re.sub(r"\n    # Chapter 5 begin.*?# Chapter 5 end\n", "\n", text, flags=re.S)
    block = "\n    # Chapter 5 begin\n" + ''.join(
        f"    {e['kind']!r}: {e['kind_zh']!r},\n" for e in EQS) + "    # Chapter 5 end\n"
    marker = "\n}\n\n\ndef equation_title_zh"
    assert marker in text
    text = text.replace(marker, block + "}\n\n\ndef equation_title_zh", 1)
    titles.write_text(text, encoding='utf-8')

    glossary = ROOT / 'content/symbol_glossaries.py'
    g = glossary.read_text(encoding='utf-8')
    hook = "\nfrom chapter05_spec import GLOSSARY5\nGLOSSARIES[5] = GLOSSARY5\n"
    if hook not in g:
        glossary.write_text(g.rstrip('\n') + '\n' + hook, encoding='utf-8')
    print(f'Registered {len(EQS)} Chapter 5 equations.')


if __name__ == '__main__':
    main()
