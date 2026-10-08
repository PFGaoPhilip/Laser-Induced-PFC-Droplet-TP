"""Compare deployed core pages and representative assets with the curated export."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
import argparse
import hashlib
import json
import time

ROOT=Path(__file__).resolve().parents[1]

def fetch(url):
    request=Request(url,headers={'User-Agent':'Laser-PFC-course-publication-check','Cache-Control':'no-cache'})
    with urlopen(request,timeout=40) as response:
        return response.status,response.read()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--commit',required=True)
    parser.add_argument('--site-directory',type=Path,default=ROOT/'publication/site')
    args=parser.parse_args()
    dest=args.site_directory.resolve()
    settings=json.loads((dest/'COURSE_SETTINGS.json').read_text(encoding='utf-8'))
    base=settings['url'];repo=settings['repository']
    registry=json.loads((dest/'verification/equations.json').read_text(encoding='utf-8'))
    wanted={'index.html','COURSE_SETTINGS.json','PUBLIC_FILE_MANIFEST.json',
            'reference/defense.html','reference/notation.html','reference/sources.html',
            'assets/course.css','assets/course-theme.js','assets/course-progress.js',
            'assets/bilingual-terms.css','assets/vendor/katex/katex.min.css',
            'assets/vendor/katex/fonts/KaTeX_Main-Regular.woff2',
            'assets/vendor/katex/fonts/KaTeX_Math-Italic.woff2'}
    wanted.update(ch['file'] for ch in settings['chapters']+settings.get('appendices',[])+settings.get('legacy_routes',[]))
    for kind in {eq['diagram']['type'] for eq in registry}:
        eq=next(eq for eq in registry if eq['diagram']['type']==kind)
        wanted.add('assets/figures/'+eq['id'].lower()+'.svg')
    for identifier in ['C1-E28','C2-E09','C3-E22','C4-E07','C4-E13','C4-E40','C4-E41','A-E18','A-E20']:
        wanted.add('assets/figures/'+identifier.lower()+'.svg')
    def verify(relative):
        expected=(dest/relative).read_bytes()
        try:
            status,data=fetch(base+relative+'?v='+args.commit[:12])
            digest=hashlib.sha256(data).hexdigest()
            return {'file':relative,'http_status':status,'bytes':len(data),'sha256':digest,
                    'matches_local_export':status==200 and digest==hashlib.sha256(expected).hexdigest()}
        except Exception as error:
            return {'file':relative,'matches_local_export':False,'error':str(error)}
    with ThreadPoolExecutor(max_workers=6) as executor:
        rows=list(executor.map(verify,sorted(wanted)))
    status,commit_data=fetch('https://api.github.com/repos/'+repo+'/commits/main')
    remote_sha=json.loads(commit_data)['sha']
    passed=all(row['matches_local_export'] for row in rows) and remote_sha==args.commit
    report={'status':'passed' if passed else 'failed','repository':repo,'url':base,
            'expected_commit':args.commit,'remote_main_commit':remote_sha,
            'verified_at_unix':int(time.time()),'files_checked':len(rows),'files':rows,
            'scope':'All nine canonical HTML pages and the legacy hydrogel route, settings, manifest, runtime/style assets, two math fonts and representative physical-variable SVGs match the curated export. Full ZIP contents have separate manifest/CRC checks. This verifies deployment, not physical material validation.'}
    (ROOT/'verification/publication-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','repository','url','remote_main_commit','files_checked']}))
    if not passed:print(json.dumps([r for r in rows if not r['matches_local_export']],ensure_ascii=False))
    raise SystemExit(0 if passed else 1)

if __name__=='__main__':main()
