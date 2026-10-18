"""One-time collision-safe migration from the frozen pre-defense chapter.

Re-running against an already migrated tree is intentionally rejected.
"""
from pathlib import Path
import json,re,shutil,zipfile,io,hashlib

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/'reports/ch1_defense_revision'

def remap(text):
    # Two passes avoid cascading through numeric collisions.
    def stash(m):
        old=int(m[2]); new=old if old<12 else old-1
        if old==12: return m[0]  # deleted semantic blocks are removed separately
        return f'__CH1MIGRATION_{m[1]}_{new:02d}__'
    text=re.sub(r'(C1-E|c1-e)(\d{2})',stash,text)
    return re.sub(r'__CH1MIGRATION_(C1-E|c1-e)_(\d{2})__',r'\1\2',text)

def main():
    p=ROOT/'content/chapter01.py'; source=p.read_text(encoding='utf-8')
    assert 'eq("C1-E34"' in source and 'chapter01_steps' not in source,'Already migrated'
    start=source.index('body += P("Check dissipation directly')
    stop=source.index('body += P("Confinement',start)
    source=source[:start]+source[stop:]
    source=remap(source)
    source=source.replace('from symbol_tables import glossary','from symbol_tables import glossary\nimport sys\nfrom pathlib import Path\nsys.path.insert(0,str(Path(__file__).resolve().parent))\nfrom chapter01_steps import STEPS')
    before='''    return E(identifier, tex, en, zh, kind,
             {"type": typ, "labels": labels, "notes": notes}, cap_en, cap_zh)'''
    after='''    steps = STEPS[identifier]
    tex = r"\\begin{gathered}" + steps["tex"] + r"\\\\[6pt]" + tex + r"\\end{gathered}"
    en += " " + steps["symbols_en"]
    zh += " " + steps["symbols_zh"]
    block = E(identifier, tex, en, zh, kind,
             {"type": typ, "labels": labels, "notes": notes}, cap_en, cap_zh)
    # Keep the established symbol-table and figure layout. Extra declarations
    # immediately precede the full derivation within the same equation column.
    marker = '<div class="math-display"'
    block = block.replace(marker, P(en,zh,'symbol-conventions') + marker, 1)
    return (P('<strong>Derivation.</strong> '+steps['en'],
              '<strong>推导。</strong> '+steps['zh']) + block
            + P('<strong>Check and interpretation.</strong> '+steps['check_en'],
                '<strong>检验与解释。</strong> '+steps['check_zh']))'''
    assert before in source; p.write_text(source.replace(before,after),encoding='utf-8')
    # Dictionary keys and semantic references move from one frozen snapshot.
    p=ROOT/'content/equation_symbol_rows.json'; data=json.loads(p.read_text(encoding='utf-8'))
    data={remap(k):v for k,v in data.items() if k!='C1-E12'}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # All figure bytes are captured before any destination is overwritten.
    folder=ROOT/'assets/figures-editable/c1-c2'
    originals={p.name:p.read_bytes() for p in folder.glob('c1-e*') if p.is_file()}
    for name,raw in originals.items():
        match=re.match(r'c1-e(\d{2})',name)
        old=int(match[1])
        if old<=12: continue
        target=folder/remap(name)
        if name.endswith('.pptx'):
            output=io.BytesIO()
            with zipfile.ZipFile(io.BytesIO(raw)) as zin,zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    content=zin.read(item.filename)
                    if item.filename.endswith(('.xml','.rels')): content=remap(content.decode('utf-8')).encode('utf-8')
                    zout.writestr(item,content)
            target.write_bytes(output.getvalue())
        elif name.endswith(('.json','.svg')):target.write_text(remap(raw.decode('utf-8')),encoding='utf-8')
        else:target.write_bytes(raw)
    # Last old ID is obsolete; old E12 was overwritten by old E13.
    for name in originals:
        if name.startswith('c1-e34'):(folder/name).unlink()
    for p in [ROOT/'assets/figures/c1-e34.svg']:
        if p.exists():p.unlink()
    # Active authoring and checks migrate; dated evidence/learner records stay frozen.
    exclude={'revise_chapter01_20261019.py'}
    for folder in ('scripts','content'):
        for p in (ROOT/folder).glob('*.py'):
            if p.name in exclude or p.name in {'chapter01.py','chapter01_steps.py'}:continue
            raw=p.read_text(encoding='utf-8'); changed=remap(raw)
            if changed!=raw:p.write_text(changed,encoding='utf-8')
    for f in ('verification/chapter01-check.py',):
        p=ROOT/f;s=remap(p.read_text(encoding='utf-8')).replace('range(1,35)','range(1,34)');p.write_text(s,encoding='utf-8')
    for f in ('scripts/integrate_english_figures.py','scripts/verify_english_figures.py'):
        p=ROOT/f;s=p.read_text(encoding='utf-8').replace('len(rows) == 200','len(rows) == 199').replace('len(rows)==200','len(rows)==199').replace('200 English figures · 190 equation diagrams','199 English figures · 189 equation diagrams');p.write_text(s,encoding='utf-8')
    shutil.copy2(ROOT/'sources/chapter01-handoff-20261019/CH1_EQUATION_RENUMBER_MAP.csv',REPORT/'EQUATION_MAP.csv')
    (REPORT/'MIGRATION.json').write_text(json.dumps({'old_equations':34,'deleted_old':'C1-E12','new_equations':33,'strategy':'two-pass placeholders and frozen figure bytes','external_bookmarks':'Old E12 and later fragments require the explicit equation map. No backward aliases are installed.','historical_records':'Dated reports, frozen evidence, handoff originals and private learner records retain original numbering.'},indent=2)+'\n',encoding='utf-8')
    print('Migrated source, metadata, editable figures and current generator references')

if __name__=='__main__':main()
