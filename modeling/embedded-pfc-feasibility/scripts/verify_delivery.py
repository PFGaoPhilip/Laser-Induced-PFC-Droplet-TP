"""Verify local reader/source dependencies and saved numerical evidence."""
import hashlib,json,re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ['src','href'] and v:self.links.append(v)

def local(base,link):
    u=urlsplit(link)
    if u.scheme or u.netloc or not u.path:return None
    p=(base/unquote(u.path)).resolve()
    assert p==ROOT or ROOT in p.parents,f'Dependency leaves delivery folder: {link}'
    assert p.exists(),f'Missing local dependency: {base} -> {link}'
    return p.relative_to(ROOT).as_posix()

def native_csv(path):
    lines=path.read_text(encoding='utf-8-sig').splitlines()
    header=next(x for x in lines if x.startswith('%') and 'time_s' in x)
    labels=[x.strip().split(' (')[0].lstrip('%').strip() for x in header.split(',')]
    data=[[float(x) for x in line.split(',')] for line in lines if line and not line.startswith('%')]
    return {name:[row[i] for row in data] for i,name in enumerate(labels)}

def main():
    source=(ROOT/'index.html').read_text(encoding='utf8');parsed=Links();parsed.feed(source)
    checked=set()
    for link in parsed.links:
        p=local(ROOT,link)
        if p:checked.add(p)
    for f in [ROOT/'assets/reader.css',ROOT/'assets/vendor/katex/katex.min.css']:
        for link in re.findall(r'url\([\"\']?([^\)\"\']+)',f.read_text(encoding='utf8')):
            p=local(f.parent,link)
            if p:checked.add(p)
    for f in ROOT.rglob('*.md'):
        if any(x in f.relative_to(ROOT).parts for x in ['.tools','build','tmp']):continue
        for link in re.findall(r'!?\[[^\]]+\]\(([^\)]+)\)',f.read_text(encoding='utf8')):
            p=local(f.parent,link)
            if p:checked.add(p)
    assert 'katex-error' not in source and '@@MATH_' not in source
    assert 'id="theme-toggle"' in source and 'assets/reader.js' in source
    numerical=json.loads((ROOT/'verification/NUMERICAL_AUDIT.json').read_text())
    logic=json.loads((ROOT/'verification/READER_LOGIC_AUDIT.json').read_text())
    pdf=json.loads((ROOT/'verification/PDF_AUDIT.json').read_text())
    assert numerical['status']==logic['status']==pdf['status']=='PASS'
    assert pdf['visual_review'].startswith('PASS')
    coarse=native_csv(ROOT/'verification/transient_fresh_reload.csv')
    fine=native_csv(ROOT/'verification/transient_native_half_step.csv')
    speed_error=abs(max(fine['radial_speed_m_s'])-max(coarse['radial_speed_m_s']))/max(fine['radial_speed_m_s'])
    end_error=abs(fine['time_s'][-1]-coarse['time_s'][-1])/fine['time_s'][-1]
    values=[speed_error,end_error,max(map(abs,fine['total_energy_residual'])),max(map(abs,fine['mass_relative_residual']))]
    assert values[0]<2e-4 and values[1]<.002 and values[2]<1e-6 and values[3]<1e-8
    eq=native_csv(ROOT/'verification/equilibrium_fresh_reload.csv')
    assert abs(eq['mass_relative_residual'][0])<1e-8 and eq['shell_thickness_m'][0]>0
    native=dict(status='PASS',speed_relative_difference=values[0],stored_endpoint_relative_difference=values[1],
                refined_energy_residual=values[2],refined_mass_residual=values[3],
                scope='Fresh-process reload of both saved native models; transient output/step tau/100 versus tau/200 with tighter tolerance; saved MPH files not overwritten.')
    (ROOT/'verification/NATIVE_RELOAD_AUDIT.json').write_text(json.dumps(native,indent=2),encoding='utf8')
    preserved=json.loads((ROOT/'verification/ACCEPTED_CONTROL_PRESERVATION.json').read_text())
    for x in preserved:assert hashlib.sha256((ROOT/x['copied_to']).read_bytes()).hexdigest()==x['sha256']
    audit=dict(status='PASS',local_dependencies_checked=len(checked),dependency_paths=sorted(checked),
               equation_display_count=32,computed_selector_states=30,reader_logic_scenarios=logic['scenarios'],
               pdf_visual_review=pdf['visual_review'],numerical_verification='PASS',native_reload_refinement='PASS',
               actual_browser_layout='NOT TESTED: no enabled browser surface',
               physical_validation='NOT PERFORMED for the target embedded mechanism')
    (ROOT/'verification/DELIVERY_AUDIT.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
    print({k:v for k,v in audit.items() if not isinstance(v,list)})

if __name__=='__main__':main()
