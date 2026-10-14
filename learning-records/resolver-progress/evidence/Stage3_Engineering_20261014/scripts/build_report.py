"""Build the portable Stage3 engineering report from bundled ledger inputs.

No solver is executed. Requires Python 3.9+, pdfLaTeX (TeX Live packages).
The build uses a task-local temporary directory and removes its intermediates.
"""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / 'report'

def esc(s):
    return str(s).replace('&', r'\&').replace('%', r'\%').replace('_', r'\_').replace('#', r'\#')

def write_tables(d):
    dest = REPORT / 'generated'
    dest.mkdir(parents=True, exist_ok=True)
    rows = [r'\begin{tabular}{rrrr}\toprule', r'Water mass (pg) & PFP (m/s) & PFH (m/s) & Scaling\\\midrule']
    for mass in d['scope']['whole_water_mass_pg']:
        vals = [next(x['value'] for x in d['ceilings'] if x['species']==s and x['mass_pg']==mass) for s in ['PFP','PFH']]
        rows.append(f'{mass} & {vals[0]:.4f} & {vals[1]:.4f} & '+r'$m_*^{-1/2}$\\')
    rows.append(r'\bottomrule\end{tabular}')
    (dest/'ceiling_table.tex').write_text('\n'.join(rows)+'\n', encoding='utf-8')
    rows = [r'\begin{longtable}{p{.38\linewidth}rrc}\toprule', r'Historical stored-group quantity & PFP & PFH & Tier\\\midrule\endhead']
    labels = {'slow_in_screen':'Slow-condensation speed (m/s)', 'fast_in_screen':'Fast-condensation speed (m/s)', 'beyond_screen':'Beyond-screen speed (m/s)', 'internal_contact_in_screen':'Internal contact estimate (MPa)', 'receiver_estimate_in_screen':'Receiver estimate (MPa)'}
    for group,label in labels.items():
        v=[next(x for x in d['historical'] if x['species']==s and x['group']==group) for s in ['PFP','PFH']]
        rows.append(f"{label} & {v[0]['value']/(1e6 if v[0]['units']=='Pa' else 1):.4f} & {v[1]['value']/(1e6 if v[1]['units']=='Pa' else 1):.4f} & {v[0]['tier']}\\\\")
    rows.append(r'\bottomrule\end{longtable}')
    (dest/'historical_table.tex').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    rows=[r'\begin{longtable}{p{.28\linewidth}p{.19\linewidth}p{.18\linewidth}>{\raggedright\arraybackslash}p{.20\linewidth}}\toprule',r'Slot & Units/condition & Value & Execution / exit\\\midrule\endhead']
    for x in d['objective_results']:
        if x['value'] is not None: raise ValueError('Report null-objective assumptions changed; amend before build')
        rows.append(esc(x['id'])+' & '+esc(x['units'])+' & null & '+r'NOT\_RUN / WAIVED\\')
    rows.append(r'\bottomrule\end{longtable}')
    (dest/'objectives_table.tex').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    rows=[r'\begin{longtable}{p{.32\linewidth}p{.31\linewidth}p{.28\linewidth}}\toprule',r'Ledger claim & Source record & Qualified use\\\midrule\endhead']
    for x in d['historical']:
        rows.append(r'\path{'+x['id']+'} & '+esc(x['source']['record'])+' & Stored maximum of a historical group; '+x['tier']+r'\\')
    rows.append(r'\bottomrule\end{longtable}')
    (dest/'claim_table.tex').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    review = ROOT / 'review' / 'INDEPENDENT_RECOMPUTE.json'
    if review.exists():
        data=json.loads(review.read_text(encoding='utf-8-sig'))
        (dest/'independent_review_presence.tex').write_text('The independent review is bundled and was available for this build. Its machine-readable record is in '+r'\path{review/INDEPENDENT_RECOMPUTE.json}.'+'\n',encoding='utf-8')
    else:
        (dest/'independent_review_presence.tex').write_text('The independent review is delivered separately in the package; consult the final root integration verdict.\n',encoding='utf-8')

def main():
    REPORT.mkdir(parents=True, exist_ok=True)
    ledger=ROOT/'RESULTS_LEDGER.json'
    d=json.loads(ledger.read_text(encoding='utf-8-sig'))
    write_tables(d)
    binary=shutil.which('pdflatex')
    if not binary: raise RuntimeError('pdfLaTeX is required; no automatic installation is performed')
    env=os.environ.copy()
    env['SOURCE_DATE_EPOCH']='1791936000'
    env['FORCE_SOURCE_DATE']='1'
    with tempfile.TemporaryDirectory(prefix='stage3-tex-',dir=REPORT) as tmp:
        cmd=[binary,'-interaction=nonstopmode','-halt-on-error','-file-line-error',f'-output-directory={tmp}','STAGE3_ENGINEERING_REPORT.tex']
        for _ in range(3):
            p=subprocess.run(cmd,cwd=REPORT,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
            if p.returncode:
                raise RuntimeError(p.stdout[-7000:]+p.stderr[-2000:])
        log=(Path(tmp)/'STAGE3_ENGINEERING_REPORT.log').read_text(encoding='utf-8',errors='replace')
        forbidden=['Overfull \\hbox','Overfull \\vbox','undefined references','undefined on input line','LaTeX Error']
        issues=[w for w in forbidden if w in log]
        if issues:
            (REPORT/'BUILD_LOG.txt').write_text(log,encoding='utf-8')
            lines=log.splitlines()
            for i,line in enumerate(lines):
                if 'Overfull' in line: print('\n'.join(lines[i:i+8]))
            raise RuntimeError('Report build quality failures: '+', '.join(issues))
        shutil.copyfile(Path(tmp)/'STAGE3_ENGINEERING_REPORT.pdf',REPORT/'STAGE3_ENGINEERING_REPORT.pdf')
        (REPORT/'BUILD_LOG.txt').write_text(log,encoding='utf-8')
    result={'status':'PASS','tool':'pdfLaTeX','passes':3,'errors':0,'undefined_references':0,'overfull_boxes':0,'ledger_sha256':hashlib.sha256(ledger.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((REPORT/'STAGE3_ENGINEERING_REPORT.pdf').read_bytes()).hexdigest(),'fixed_SOURCE_DATE_EPOCH':1791936000,'authoring_marker':'NOT_AVAILABLE: supplied container_tools marker absent in Windows runtime; attempted once and recorded','solver_run':False}
    (REPORT/'BUILD_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
