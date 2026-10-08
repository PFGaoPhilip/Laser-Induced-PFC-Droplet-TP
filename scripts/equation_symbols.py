"""Render reviewed equation-local definitions with a continuous table rule."""
from functools import lru_cache
from html import escape
import json
from pathlib import Path

@lru_cache(maxsize=1)
def definitions():
    root=Path(__file__).resolve().parents[1]
    return json.loads((root/'content/equation_symbol_rows.json').read_text(encoding='utf-8'))

def symbol_panel(identifier,pair):
    data=definitions()[identifier]
    rows=data['rows']
    output=[f'<div class="symbols" data-symbol-table="{escape(identifier)}">',
            pair(f'<strong>Symbols before Eq. ({identifier}).</strong>',
                 f'<strong>式（{identifier}）前的符号定义。</strong>','symbol-panel-heading'),
            '<div class="symbol-table-scroll"><table class="symbol-definitions">',
            '<thead class="visually-hidden"><tr><th scope="col">First individual definition / 第一项单独定义</th><th scope="col">Second individual definition / 第二项单独定义</th></tr></thead><tbody>']
    for index in range(0,len(rows),2):
        output.append('<tr>')
        for item in rows[index:index+2]:
            output.append(f'<td class="symbol-definition" data-symbol="{escape(item["symbol"],quote=True)}" data-unit="{escape(item["unit"],quote=True)}">'
                          +pair(item['en'],item['zh'])+'</td>')
        if len(rows[index:index+2])==1:
            output.append('<td class="symbol-placeholder" aria-hidden="true"></td>')
        output.append('</tr>')
    output.append('</tbody></table></div>')
    if data['notes_en'] or data['notes_zh']:
        output.append(pair('<strong>Conventions and conditions.</strong> '+'; '.join(data['notes_en'])+'.',
                           '<strong>约定与条件。</strong> '+'；'.join(data['notes_zh'])+'。','symbol-conventions'))
    output.append('</div>')
    return ''.join(output)
