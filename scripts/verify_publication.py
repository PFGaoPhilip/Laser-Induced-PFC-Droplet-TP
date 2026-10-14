"""Compare deployed core pages and representative assets with the curated export."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, build_opener, ProxyHandler
import argparse
import hashlib
import json
import re
import time

ROOT=Path(__file__).resolve().parents[1]

def fetch(url):
    request=Request(url,headers={'User-Agent':'Laser-PFC-course-publication-check','Cache-Control':'no-cache'})
    with build_opener(ProxyHandler({})).open(request,timeout=40) as response:
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
    figure_manifest=dest/'assets/figures-editable/manifest.json'
    wanted={'index.html','COURSE_SETTINGS.json','PUBLIC_FILE_MANIFEST.json',
            'reference/defense.html','reference/notation.html','reference/sources.html',
            'assets/course.css','assets/course-theme.js','assets/course-progress.js',
            'assets/bilingual-terms.css','assets/vendor/katex/katex.min.css',
            'assets/vendor/katex/fonts/KaTeX_Main-Regular.woff2',
            'assets/vendor/katex/fonts/KaTeX_Math-Italic.woff2'}
    if figure_manifest.is_file():
        wanted.update({'assets/figures-editable/index.html','assets/figures-editable/manifest.json'})
        figures=json.loads(figure_manifest.read_text(encoding='utf-8'))
        wanted.update('assets/figures-editable/'+row['svg'] for row in figures)
        wanted.update('assets/figures/'+row['id']+'.svg' for row in figures
                      if re.fullmatch(r'(?:c[1-4]|a)-e\d+',row['id']))
        wanted.update('assets/figures-editable/'+row['pptx'] for row in figures
                      if row['id'] in {'c1-e07','c2-e01','c3-e24','c4-e07','a-e01','embedded-pfc-feasibility-radial_stability'})
    wanted.update(ch['file'] for ch in settings['chapters']+settings.get('appendices',[])+settings.get('legacy_routes',[]))
    wanted.update({'assets/course-language.js','assets/course-language.css',
        'modeling/minimal-cavitation/index.html','modeling/minimal-cavitation/STEP_BY_STEP.html',
        'modeling/minimal-cavitation/assets/theme.js','modeling/minimal-cavitation/assets/first_event_histories.png',
        'modeling/minimal-cavitation/assets/first_event_histories.zh.png',
        'modeling/minimal-cavitation/assets/vendor/katex/fonts/KaTeX_Main-Regular.woff2',
        'modeling/minimal-cavitation/MODEL_SPEC.md','modeling/minimal-cavitation/MODEL_SPEC.zh.md',
        'modeling/minimal-cavitation/verification/NUMERICAL_AUDIT.json',
        'modeling/minimal-cavitation/models/Model_A_Finite_Energy_Pressure_Jet.mph',
        'modeling/minimal-cavitation/models/Model_B_Hydrogel_Confinement_Jet_Transmission.mph'})
    wanted.update({'learning-records/resolver-progress/index.html',
                   'learning-records/resolver-progress/PROGRESS.json',
                   'learning-records/resolver-progress/INPUT_MANIFEST.json',
                   'learning-records/resolver-progress/assets/course.css',
                   'learning-records/resolver-progress/assets/course-theme.js',
                   'learning-records/resolver-progress/assets/course-language.js',
                   'learning-records/resolver-progress/evidence/Stage3_Engineering_20261014/report/STAGE3_ENGINEERING_REPORT.pdf',
                   'verification/GITHUB_PUBLICATION_AUTHORIZATION_20261014.json'})
    if settings.get('embedded_pfc'):
        study='modeling/embedded-pfc-feasibility/'
        wanted.update(study+name for name in [
            'index.html','REPORT.md','DERIVATION.md','DERIVATION.tex','SOURCES.md',
            'IMPLEMENTATION_HANDOFF.md','README.md','PUBLICATION.md','COPY_MANIFEST.json',
            'MANIFEST.json','PUBLICATION_AUDIT.json','data/reader_states.json',
            'assets/reader.css','assets/reader.js',
            'assets/vendor/katex/fonts/KaTeX_Main-Regular.woff2',
            'assets/vendor/katex/fonts/KaTeX_Math-Italic.woff2',
            'assets/size_species_comparison.svg','assets/radial_viscosity_controls.svg',
            'assets/radial_stability.svg','assets/fracture_budget.svg',
            'output/pdf/FINITE_PFC_DERIVATION.pdf',
            'models/Embedded_PFC_Curved_Equilibrium.mph',
            'models/Embedded_PFC_PostNucleation_Intact_Gel.mph',
            'verification/NUMERICAL_AUDIT.json','verification/PARAMETER_AUDIT.json',
            'verification/NATIVE_RELOAD_AUDIT.json'])
        wanted.add(settings['embedded_pfc']['archive'])
    for kind in {eq['diagram']['type'] for eq in registry}:
        eq=next(eq for eq in registry if eq['diagram']['type']==kind)
        wanted.add('assets/figures/'+eq['id'].lower()+'.svg')
    for identifier in ['C1-E28','C2-E09','C3-E22','C4-E07','C4-E13','C4-E40','C4-E41','A-E18','A-E20']:
        wanted.add('assets/figures/'+identifier.lower()+'.svg')
    def verify(relative):
        expected=(dest/relative).read_bytes()
        for attempt in range(3):
            try:
                status,data=fetch(base+relative+'?v='+args.commit[:12])
                digest=hashlib.sha256(data).hexdigest()
                row={'file':relative,'http_status':status,'bytes':len(data),'sha256':digest,
                     'matches_local_export':status==200 and digest==hashlib.sha256(expected).hexdigest()}
                if row['matches_local_export'] or attempt==2:return row
            except Exception as error:
                if attempt==2:return {'file':relative,'matches_local_export':False,'error':str(error)}
            time.sleep(2)
    with ThreadPoolExecutor(max_workers=6) as executor:
        rows=list(executor.map(verify,sorted(wanted)))
    status,commit_data=fetch('https://api.github.com/repos/'+repo+'/commits/main')
    remote_sha=json.loads(commit_data)['sha']
    passed=all(row['matches_local_export'] for row in rows) and remote_sha==args.commit
    report={'status':'passed' if passed else 'failed','repository':repo,'url':base,
            'expected_commit':args.commit,'remote_main_commit':remote_sha,
            'verified_at_unix':int(time.time()),'files_checked':len(rows),'files':rows,
            'scope':'All course HTML routes, both bilingual ideal-gas modeling readers, the finite-PFC reader/PDF/native models/public ZIP and core study records, representative plots, language/theme assets and local math fonts match the curated export. Full ZIP contents have separate manifest/CRC checks. This verifies deployment, not physical material validation.'}
    (ROOT/'verification/publication-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','repository','url','remote_main_commit','files_checked']}))
    if not passed:print(json.dumps([r for r in rows if not r['matches_local_export']],ensure_ascii=False))
    raise SystemExit(0 if passed else 1)

if __name__=='__main__':main()
