"""Read-only package manifest and optional ZIP CRC verification; stdlib only."""
import hashlib,json,sys,zipfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'FILE_MANIFEST.json').read_text(encoding='utf-8'))
failures=[]
for row in manifest['files']:
    p=(root/row['path']).resolve()
    if not p.is_relative_to(root):failures.append(row['path']+': unsafe path');continue
    if not p.exists():failures.append(row['path']+': missing');continue
    if hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:failures.append(row['path']+': hash differs')
archive=None
if len(sys.argv)>1:
    with zipfile.ZipFile(sys.argv[1]) as z:
        archive={'CRC':'PASS' if z.testzip() is None else 'FAIL','members':len(z.namelist())}
        if archive['CRC']!='PASS':failures.append('ZIP CRC')
print(json.dumps({'manifest':'PASS' if not failures else 'FAIL','checked_files':len(manifest['files']),'failures':failures,'archive':archive},indent=2))
raise SystemExit(bool(failures))
