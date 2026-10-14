"""Verify prose revision against signatures from the pre-revision local ZIP."""
from pathlib import Path
import hashlib
import json
import re
from package import SUPERSEDED_VERIFICATION

ROOT=Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def normalized(value):
    if isinstance(value,(list,tuple)):
        return [normalized(item) for item in value]
    return value.replace('\r\n','\n')

def main():
    baseline=json.loads((ROOT/'verification/READER_BASELINE_SIGNATURES.json').read_text(encoding='utf-8'))
    checks=[]
    for name,previous in baseline['reader_signatures'].items():
        text=(ROOT/name).read_text(encoding='utf-8')
        current={
            'math':re.findall(r'\$\$.*?\$\$|\$(?:[^$\n]+)\$',text,re.S),
            'codes':re.findall(r'```[^\n]*\n(.*?)```|(?<!`)`([^`\n]+)`(?!`)',text,re.S),
            'numeric_tokens':re.findall(r'\d+(?:\.\d+)?(?:[eE][-+]?\d+)?',text),
            'symbols':[line for line in text.splitlines() if line.startswith('**Symbols before') or line.startswith('**式 ') or line.startswith('**公式 ')],
        }
        for kind,value in current.items():
            assert normalized(value)==normalized(previous[kind]),f'{name}: changed {kind}'
        checks.append({'file':name,'formula_expressions':len(current['math']),'code_entries':len(current['codes']),'numeric_tokens':len(current['numeric_tokens']),'status':'PASS'})
    protected=[]
    for archived,expected in baseline['scientific_file_hashes'].items():
        relative=Path(archived).relative_to('Minimal_Cavitation_Models')
        assert digest(ROOT/relative)==expected,f'Protected scientific file changed: {relative}'
        protected.append(relative.as_posix())
    result={
        'status':'PASS','baseline':baseline['baseline_archive'],
        'scope':'Exact formula, code, numeric token and recorded local symbol declaration preservation; CRLF/LF normalization permitted.',
        'reader_checks':checks,'protected_native_data_GUI_files':len(protected),
        'semantic_review':'Self-review of revised bilingual prose; assumptions, branches and limitations retained. No new independent expert review.',
        'equation_derivation':'Existing derivation retained; this script does not prove it.',
        'new_COMSOL_runs':'NOT_RUN','new_physical_validation':'NOT_ESTABLISHED',
    }
    (ROOT/'verification/READER_PROSE_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    paths=[path for path in ROOT.rglob('*') if path.is_file() and path.suffix not in ('.zip','.pyc','.class') and not any(part in ('build','tmp','__pycache__','practice') for part in path.relative_to(ROOT).parts) and path.name!='READER_REVISION_MANIFEST.json' and not (path.relative_to(ROOT).parts[0]=='verification' and path.name in SUPERSEDED_VERIFICATION)]
    manifest={'revision_date':'2026-10-14','scope':'Current exportable course copy after bilingual reader prose revision. Original accepted copy hashes remain in SOURCE_MANIFEST.json.','files':[{'path':path.relative_to(ROOT).as_posix(),'sha256':digest(path)} for path in sorted(paths)]}
    (ROOT/'READER_REVISION_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(f"PASS: {len(checks)} source editions, {len(protected)} protected scientific files.")

if __name__=='__main__':
    main()
