"""Local lesson integration. No publication, simulation, or history operations."""
from pathlib import Path
import argparse, datetime, hashlib, json, shutil
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
F=ROOT/'reports/Cavitation_Limits_20261011/full_closure'
LESSON=ROOT/'learning-records/resolver-progress'
SOURCE=F/'delivery/Stage3_Engineering_20261014'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()
def save(p,obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def copy_inputs():
    LESSON.mkdir(parents=True,exist_ok=True)
    mf=json.loads((SOURCE/'FILE_MANIFEST.json').read_text(encoding='utf-8'))
    for r in mf['files']:
        if sha(SOURCE/r['path'])!=r['sha256']:raise ValueError('Changed sealed input '+r['path'])
    target=LESSON/'evidence/Stage3_Engineering_20261014'
    shutil.copytree(SOURCE,target,dirs_exist_ok=True)
    rows=[]
    for p in sorted(SOURCE.rglob('*')):
        if p.is_file():rows.append({'original':p.relative_to(ROOT).as_posix(),'copy':(target/p.relative_to(SOURCE)).relative_to(LESSON).as_posix(),'sha256':sha(p)})
    extras={'verification/STAGE3_FINAL_SEAL_20261014.json':'receipts/STAGE3_FINAL_SEAL_20261014.json','verification/STAGE3_FINAL_REPORTING_OUTPUT_FREEZE_006.json':'receipts/STAGE3_FINAL_REPORTING_OUTPUT_FREEZE_006.json','verification/STAGE1_LOOSENED_CLOSE_ACCEPTED_20261014.md':'receipts/STAGE1_LOOSENED_CLOSE_ACCEPTED_20261014.md','verification/STAGE2_LOOSENED_CLOSED_20261013.md':'receipts/STAGE2_LOOSENED_CLOSED_20261013.md','NATIVE_RAW_READER_CONTRACT.md':'receipts/NATIVE_RAW_READER_CONTRACT.md','verification/stage2_loosened_build_028_local_003_linux_tmp.sh':'receipts/HISTORICAL_BUILD_028.sh'}
    for src,dst in extras.items():
        p=F/src;q=LESSON/dst;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
        rows.append({'original':p.relative_to(ROOT).as_posix(),'copy':dst,'sha256':sha(p)})
    archive=F/'solver/downloads/basilisk.tar.gz'
    q=LESSON/'native/basilisk.tar.gz';q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(archive,q)
    rows.append({'original':archive.relative_to(ROOT).as_posix(),'copy':q.relative_to(LESSON).as_posix(),'sha256':sha(q)})
    shutil.copytree(ROOT/'assets/vendor/katex',LESSON/'assets/vendor/katex',dirs_exist_ok=True)
    for name in ['course.css','course-theme.js','course-language.js','course-language.css']:
        q=LESSON/'assets'/name;shutil.copy2(ROOT/'assets'/name,q)
    seal=json.loads((LESSON/'receipts/STAGE3_FINAL_SEAL_20261014.json').read_text())
    record={'schema':'local_three_stage_resolver_progress_v1','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'publication_status':'HELD_NOT_PUBLISHED','published':False,'owner_instruction':'Update lesson progress; teach formulas and key code; preserve bilingual/theme controls; do not publish.','strict_acceptance':False,'stages':[{'id':'Stage1','status':'CLOSED_LOOSENED','meaning':'Owner-accepted model engineering closure.','missing':'Strict production qualification; full calibration and whole-path consistency.','evidence':'receipts/STAGE1_LOOSENED_CLOSE_ACCEPTED_20261014.md'},{'id':'Stage2','status':'STAGE2_LOOSENED_CLOSED','meaning':'Owner-accepted diagnostic/campaign closure.','missing':'18 computed objectives; completed observer trajectories; global certificates.','evidence':'receipts/STAGE2_LOOSENED_CLOSED_20261013.md'},{'id':'Stage3','status':seal['status'],'meaning':'Independent arithmetic, engineering reporting, reader and package delivered.','delivery_checks_passed':seal['delivery_checks_passed'],'PDF_pages_checked':seal['PDF_pages_visually_checked'],'evidence':'receipts/STAGE3_FINAL_SEAL_20261014.json'}],'all_objective_values_null':True,'objective_count':18,'model_identity':'candidate030; inherited018-030 assumptions','history_endpoint':{'time_ns':0.43,'accepted_steps':43,'completion_established':False,'legacy_meta_caveat':'Transferred meta.json belongs to candidate028.'},'same_model_radius_qualification':'NOT_ESTABLISHED','maximum':'Cannot compute maximum: missing event-complete observers, feasible designs, refinement and global bounds.','mastery':'Research closure does not change learner mastery.','preserved_source_archive_SHA256':sha(archive),'sealed_delivery_archive_sha256':seal['archive_sha256']}
    save(LESSON/'PROGRESS.json',record)
    save(LESSON/'INPUT_MANIFEST.json',{'schema':'resolver_lesson_input_manifest_v1','scope':'Copied local teaching inputs; immutable originals preserved.','copies':rows})
    print(json.dumps({'copied_evidence_files':len(rows),'source':'local sealed Stage3 delivery','publication':'HELD_NOT_PUBLISHED'}))
def integrate_links():
    if not (LESSON/'PROGRESS.json').is_file():return
    record=json.loads((LESSON/'PROGRESS.json').read_text(encoding='utf-8'))
    settings_path=ROOT/'COURSE_SETTINGS.json';settings=json.loads(settings_path.read_text(encoding='utf-8'))
    authorization_path=ROOT/'verification/GITHUB_PUBLICATION_AUTHORIZATION_20261019.json'
    if not authorization_path.is_file():
        authorization_path=ROOT/'verification/GITHUB_PUBLICATION_AUTHORIZATION_20261014.json'
    authorization=json.loads(authorization_path.read_text(encoding='utf-8')) if authorization_path.is_file() else {}
    authorized=(authorization.get('status')=='AUTHORIZED' and authorization.get('owner_instruction')=='Update to GitHub.' and authorization.get('repository')==settings['repository'])
    settings['resolver_progress']={'file':'learning-records/resolver-progress/index.html','record':'learning-records/resolver-progress/PROGRESS.json','parent_unit':'C03','publication_status':'OWNER_AUTHORIZED_GITHUB_RELEASE' if authorized else 'HELD_NOT_PUBLISHED','published':authorized,'stages':{r['id']:r['status'] for r in record['stages']},'strict_acceptance':False}
    if authorized:settings['publication_authorization']={'record':authorization_path.relative_to(ROOT).as_posix(),'owner_instruction':authorization['owner_instruction'],'date':authorization['date']}
    save(settings_path,settings)
    p=ROOT/'learning-records/progress.json';progress=json.loads(p.read_text(encoding='utf-8'));units=progress['units']
    progress['resolver_progress']=dict(settings['resolver_progress']);save(p,progress)
    assert json.loads(p.read_text(encoding='utf-8'))['units']==units
    p=ROOT/'index.html';soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    for block in soup.select('[data-resolver-progress]'):block.decompose()
    p.write_text(str(soup),encoding='utf-8',newline='\n')
    print('Updated Chapter 3 resolver metadata; homepage banners removed.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--links-only',action='store_true')
    ap.add_argument('--refresh-inputs',action='store_true',help='Explicitly recopy the sealed resolver evidence')
    args=ap.parse_args()
    if args.refresh_inputs and not args.links_only:copy_inputs()
    integrate_links()
