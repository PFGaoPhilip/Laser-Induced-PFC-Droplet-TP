"""Render reviewed equation-local definitions with a continuous table rule."""
from functools import lru_cache
from html import escape
import json
import re
from pathlib import Path

def equation_label(identifier):
    """Use the containing Chapter 1 subsection in displayed equation labels.

    Stable IDs remain unchanged for anchors, figures, and source provenance.
    The worked example belongs to 1.5; oral reference answers belong to 1.8.
    """
    match=re.fullmatch(r'C1-E(\d{2})',identifier)
    if not match:return identifier
    number=int(match[1])
    for last,section in [(1,2),(8,3),(11,4),(19,5),(25,6),(30,7),(33,8)]:
        if number<=last:return f'C1.{section}-E{number:02d}'
    raise ValueError(identifier)

def relabel_chapter01_references(html):
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(html,'html.parser')
    for node in list(soup.find_all(string=True)):
        if 'C1-E' in str(node):
            node.replace_with(re.sub(r'C1-E\d{2}',lambda m:equation_label(m[0]),str(node)))
    return str(soup)

@lru_cache(maxsize=1)
def definitions():
    root=Path(__file__).resolve().parents[1]
    return json.loads((root/'content/equation_symbol_rows.json').read_text(encoding='utf-8'))

def symbol_panel(identifier,pair,position='before'):
    data=definitions()[identifier]
    rows=data['rows']
    label=equation_label(identifier)
    output=[f'<div class="symbols" data-symbol-table="{escape(identifier)}">',
            pair(f'<strong>Symbols {"for" if position == "after" else "before"} Eq. ({label}).</strong>',
                 f'<strong>式（{label}）{"的" if position == "after" else "前的"}符号定义。</strong>','symbol-panel-heading'),
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
