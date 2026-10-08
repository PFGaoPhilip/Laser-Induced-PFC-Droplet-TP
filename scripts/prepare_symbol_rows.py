"""Authoring aid: split existing declarations without silently guessing groups.

The rendered course consumes the reviewed JSON, not this punctuation parser.
Every source fragment is retained as either an individual definition or a note.
Ambiguous groups must be supplied explicitly in symbol_row_overrides.py.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATH = re.compile(r'\$([^$]+)\$')

def fragments(text, zh=False):
    text = re.sub(r'^(Original[^:]*:|原始[^：]*：)\s*', '', text)
    result, start, in_math, depth = [], 0, False, 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == '$':
            in_math = not in_math
        if not in_math:
            if ch in '(（': depth += 1
            if ch in ')）': depth -= 1
            length = 0
            if depth == 0:
                if ch in ';；。': length = 1
                elif ch == '.' and (i + 1 == len(text) or text[i+1] == ' '): length = 1
                else:
                    # Only a new math-led declaration starts a comma/and clause.
                    pattern = r'(?:,\s*(?:and |whereas )?| and |，|、)(?=\$)'
                    match = re.match(pattern, text[i:])
                    if match:
                        next_math=MATH.match(text[i+len(match[0]):])
                        # Keep mathematical convention lists grammatical.
                        if not next_math or not OPERATORS.match(next_math[1]):
                            length = len(match[0])
            if length:
                value = text[start:i].strip()
                if value: result.append(value)
                i += length
                start = i
                continue
        i += 1
    value = text[start:].strip(' .。;；')
    if value: result.append(value)
    return result

def group_keys(tex):
    # Commas in indices/function arguments are not variable separators.
    parts, start, depth = [], 0, 0
    for i, ch in enumerate(tex):
        if ch in '{([': depth += 1
        if ch in '})]': depth -= 1
        if ch == ',' and depth == 0:
            parts.append(tex[start:i].strip()); start = i+1
    parts.append(tex[start:].strip())
    return parts

def canon(tex):
    result=key(tex)
    result=re.sub(r'\\(?:geq|leq)\b',lambda m:m[0][:-1],result)
    return result

def declared_names(tex):
    # A range inside an individual declaration is not a list of variables.
    prefix=key(tex)
    if prefix=='0' and '\\delta' in tex:
        return [r'\delta_0',r'\delta(t)']
    if prefix=='-1' and '\\nu_f' in tex: return [r'\nu_f']
    if tex==r't_a<t_b': return ['t_a','t_b']
    names=group_keys(prefix)
    if tex.startswith(r'R\geq R_{\mathrm{ref}}') or tex.startswith(r'R>R_{\mathrm{ref}}'):
        names.append(r'R_{\mathrm{ref}}')
    return names

SI=re.compile(r'(?<![A-Za-z])(?:kg\b|Pa\b|N\b|J\b|W\b|K\b|mol\b|rad\b|m(?:[²³⁻]|(?=\s|\)|）))|s(?:[⁻]|(?=\s|\)|）))|dimensionless\b|无量纲)')
OPERATORS=re.compile(r'^(?:\\(?:partial|nabla|int|oint|sum|ln|log|exp|sin|tan|sqrt|lim|infty|Rightarrow|simeq|sim|propto|cdot|otimes)|d/|D/Dt|O$|e\^|\|)')

def collect(text):
    rows={};notes=[];groups=[]
    pieces=fragments(text)
    for index,fragment in enumerate(pieces):
        match=MATH.match(fragment)
        if not match:
            notes.append(fragment);continue
        tex=match[1];tail=fragment[match.end():].strip()
        names=declared_names(tex)
        if tail.startswith(('上的上标','上的点','上的圆点')):
            notes.append(fragment);continue
        # Explanatory evaluations/identities stay as conventions, not a second
        # definition of an already introduced physical variable.
        explanatory=bool(re.match(r'(?:is not|does not|has units|is dimensionless|vanishes|follows|excludes|为零矢量|为.*微元)',tail))
        if (OPERATORS.match(tex) and tex!=r'\partial_r u') or re.match(r'^\d',names[0]) or names[0]=='' or tex in (r'\mathsf T',r'\times',r'\mathrm{Pa}',r'\mathrm J','*'):
            notes.append(fragment);continue
        if tex in (r'\theta\theta',r'\phi\phi'):
            notes.append(fragment);continue
        already=all(name in rows for name in names)
        for name in names:
            if name not in rows:
                rows[name]=dict(text=fragment,tex=tex,fragment=index,group=len(names)>1,
                               bare=not tail,explanatory=explanatory)
        if len(names)>1: groups.append(fragment)
        if already: notes.append(fragment)
    return rows,notes,pieces,groups

def compile_rows(e):
    from symbol_row_vocabulary import VOCABULARY
    chapter=5 if e['id'].startswith('A-') else int(e['id'][1])
    en,en_notes,en_pieces,en_groups=collect(e['symbols_en'])
    zh,zh_notes,zh_pieces,zh_groups=collect(e['symbols_zh'])
    names=list(en)+[name for name in zh if name not in en]
    records=[];unresolved=[]
    for name in names:
        a=en.get(name);b=zh.get(name)
        v=VOCABULARY[chapter].get(name)
        # A grouped/shared description is rewritten using the reviewed,
        # individually defined vocabulary. Direct single definitions retain
        # the original wording, including numerical state and qualifiers.
        direct=bool(a and b and not a['group'] and not b['group'] and not a['bare'] and not b['bare'])
        if direct and ' are ' in a['text']: direct=False
        if not direct and not v:
            unresolved.append((name,a,b));continue
        if direct:
            en_text=a['text'];zh_text=b['text']
            if v and not SI.search(MATH.sub('',en_text)):
                unit=v[2];suffix='dimensionless' if unit=='1' else unit
                en_text+=f' ({suffix})';zh_text+=f'（{"无量纲" if unit=="1" else unit}）'
        else:
            unit=v[2];suffix='dimensionless' if unit=='1' else unit
            shown=name
            if a:
                for piece in group_keys(a['tex']):
                    if canon(piece)==name:
                        shown=piece;break
            constant=bool(a and a['group'] and 'constant ' in a['text'])
            if v and 'constant' in v[0].lower(): constant=False
            en_text=f'${shown}$ — {"Constant " if constant else ""}{v[0]} ({suffix})'
            zh_text=f'${shown}$ — {"恒定的" if constant else ""}{v[1]}（{"无量纲" if unit=="1" else unit}）'
        records.append(dict(symbol=name,en=en_text,zh=zh_text,
                            unit=v[2] if v else 'defined in text',
                            source_en=a['fragment'] if a else None,
                            source_zh=b['fragment'] if b else None))
    return dict(rows=records,notes_en=en_notes,notes_zh=zh_notes,
                source_fragments_en=en_pieces,source_fragments_zh=zh_pieces,
                expanded_groups_en=en_groups,expanded_groups_zh=zh_groups),unresolved

def key(tex):
    # Keep the actual operator/function, strip only declarative conditions.
    return re.split(r'\\(?:geq?|leq?|ne|in|ll)(?![A-Za-z])|[><=]',tex,maxsplit=1)[0].strip()

def draft(e):
    values={}
    notes={}
    issues=[]
    for lang in ('en','zh'):
        source=fragments(e['symbols_'+lang],lang=='zh')
        rows=[]; other=[]
        for n,fragment in enumerate(source):
            match=MATH.match(fragment)
            if not match:
                other.append(fragment); continue
            tex=match[1]; tail=fragment[match.end():].strip()
            keys=group_keys(tex)
            if len(keys)>1 or not tail or tail in ('and','和','与'):
                issues.append((lang,n,fragment)); continue
            rows.append(dict(symbol=key(tex),text=fragment,source=n))
        values[lang]=rows; notes[lang]=other
    a=[r['symbol'] for r in values['en']]
    b=[r['symbol'] for r in values['zh']]
    if a!=b: issues.append(('pair',-1,str((a,b))))
    return dict(rows=values,notes=notes),issues

if __name__=='__main__':
    sys.path.insert(0,str(ROOT/'content'))
    equations=json.loads((ROOT/'verification/equations.json').read_text(encoding='utf-8'))
    result={};bad=[]
    for e in equations:
        data,issues=compile_rows(e)
        result[e['id']]=data
        if issues:
            for issue in issues: bad.append((e['id'],issue))
    if not bad:
        from symbol_row_overrides import review_rows
        review_rows(result,equations)
    for eid,issue in bad: print(eid,issue)
    if not bad:
        (ROOT/'content/equation_symbol_rows.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'Prepared {len(result)} equation declarations, {sum(len(d["rows"]) for d in result.values())} individual entries.')
