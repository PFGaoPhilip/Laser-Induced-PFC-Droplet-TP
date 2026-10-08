"""Render individual physical-symbol glossary rows without grouping identifiers."""
from html import escape
from pathlib import Path
import sys
import re
from coursekit import P
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'content'))
from symbol_glossaries import GLOSSARIES

def glossary(number):
    rows=GLOSSARIES[number]
    assert len({r[0] for r in rows})==len(rows)
    out='<div class="table-wrap"><table class="symbol-glossary"><thead><tr>'
    out+=''.join('<th>'+P(en,zh)+'</th>' for en,zh in [('Symbol','符号'),('Physical meaning','物理意义'),('SI units','SI 单位'),('Role and convention','作用与约定')])
    out+='</tr></thead><tbody>'
    for symbol,en,zh,unit,role_en,role_zh in rows:
        outside_subscripts=re.sub(r'\{[^{}]*\}','',symbol)
        assert ',' not in outside_subscripts and ';' not in outside_subscripts,(number,symbol)
        out+='<tr><td class="symbol-cell">$'+escape(symbol)+'$</td><td>'+P(en,zh)+'</td><td>'+escape(unit)+'</td><td>'+P(role_en,role_zh)+'</td></tr>'
    return out+'</tbody></table></div>'
