"""Build the detailed GUI guide and input files from the accepted native MPH.

No solver settings or saved native model is changed by this script.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
GUI = ROOT / 'resources/gui'
GUI.mkdir(parents=True, exist_ok=True)

VARIABLE_UNITS = dict(zip(
    ['x','U','R','Uw','Vg','Vdot','pb','pEl','pRes','Wgel','Kgel','Kjet','Esurf',
     'ploss','acc','wallAcc','Pdis','Edis','Eout','Iout','Mout','Pout',
     'energyResidual','Fconf','qJet','Ijet','Fflux','pArrestBound','stroke',
     'stretch','Mjet','Mwall','communication'],
    ['m','m/s','m','m/s','m^3','m^3/s','Pa','Pa','Pa','J','J','J','J',
     'Pa','m/s^2','m/s^2','W','J','J','N*s','kg','W','1','N','Pa','N*s',
     'N','Pa','1','1','1','1','1']))

EVAL = [
    ('t','s','Time after initialization'),('c.x','m','Discharged volume / outlet area'),
    ('c.U','m/s','Outward outlet speed'),('c.R','m','Chamber wall radius'),
    ('c.Uw','m/s','Wall expansion speed'),('c.Vg','m^3','Gas source volume'),
    ('c.pb-pInf','Pa','Source gauge pressure'),('c.pEl','Pa','Elastic gel pressure'),
    ('c.pRes','Pa','Elastic plus viscous gel resistance'),('c.Fconf','N','Elastic hemisphere force'),
    ('c.qJet','Pa','Outlet dynamic-pressure scale'),('c.Ijet','N*s','Effective column momentum'),
    ('c.Fflux','N','Momentum-flux scale'),('c.Kjet','J','Stored column kinetic energy'),
    ('c.Kgel','J','Gel radial kinetic energy'),('c.Wgel','J','Gel elastic work'),
    ('c.Esurf','J','Constant meniscus-load work'),('c.Edis','J','Irreversible loss'),
    ('c.energyResidual','1','Normalized energy residual'),('c.stroke','1','Liquid budget fraction'),
    ('c.stretch','1','Inner wall stretch'),('c.Mjet','1','Liquid Mach diagnostic'),
    ('c.Mwall','1','Wall Mach diagnostic'),('c.communication','1','Pressure communication screen'),
    ('c.acc','m/s^2','Outlet acceleration'),('c.wallAcc','m/s^2','Wall acceleration'),
    ('c.pArrestBound','Pa','Declared mean arrest-pressure bound'),
    ('c.Eout','J','Actually emitted kinetic energy'),('c.Iout','N*s','Actually emitted axial impulse'),
    ('c.Mout','kg','Actually emitted liquid mass')]


def decoded_array(value):
    return [x.replace(r'\,', ',') for x in re.findall(r"'([^']*)'", value)]


def extract(path):
    with zipfile.ZipFile(path) as archive:
        tree = ET.fromstring(archive.read('dmodel.xml'))
    params = [dict(e.attrib) for e in tree.findall('./ModelParam/expressions')]
    node = next(e for e in tree.iter('Expr') if e.get('tag') == 'v')
    variables = [dict(e.attrib) for e in node.findall('expressions')]
    ge = next(e for e in tree.iter('PhysicsFeature') if e.get('tag') == 'ge1')
    props = {e.get('param'): e.get('value') for e in ge.findall('param')}
    equations = list(zip(*(decoded_array(props[key]) for key in
                          ('name','equation','initialValueU','initialValueUt'))))
    solver = next(e for e in tree.iter('SolverFeature') if e.get('tag') == 't1')
    settings = {e.get('name'): e.get('value', e.get('valueMatrix'))
                for e in solver.findall('propertyValue') if e.get('name') != 'p:message'}
    stop = next(e for e in tree.iter('SolverFeature') if e.get('tag') == 'stop')
    stop_settings = {e.get('name'): e.get('value', e.get('valueMatrix'))
                     for e in stop.findall('propertyValue')}
    conditions = list(zip(*(decoded_array(stop_settings['p:'+key]) for key in
                            ('stopcondarr','stopcondterminateon','stopcondActive','stopconddesc'))))
    if len(params) != 32 or len(variables) != 33:
        raise AssertionError('Native parameter/variable count changed')
    if settings['p:rtol'] != '1e-9' or settings['p:consistent'] != 'off' or settings['p:tstepsbdf'] != 'strict':
        raise AssertionError('Native solver settings differ from the lesson')
    if settings['p:tlist'] != 'range(0,1[ns],100[us])':
        raise AssertionError('Lesson targets the accepted refined baselines')
    if len(conditions) != 4 or any(row[1:3] != ('negative','on') for row in conditions):
        raise AssertionError('Native stop conditions differ from the lesson')
    return dict(file=path.name, parameters=params, variables=variables, equations=equations,
                solver=settings, conditions=conditions, equation_quantities={
                    key: decoded_array(props[key]) for key in ('DependentVariableQuantity','SourceTermQuantity')})


def table(headers, rows):
    def clean(value):
        return str(value).replace('|',r'\|').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(headers)+' |',
                       '| '+' | '.join('---' for _ in headers)+' |']+
                      ['| '+' | '.join(clean(x) for x in row)+' |' for row in rows])


def code(value):
    return '`'+str(value)+'`'


def variables_table(rows):
    return table(['Name','Expression — enter exactly','Unit','Meaning'],
                 [(code(r['name']),code(r['expr']),code(VARIABLE_UNITS[r['name']]),r['descr']) for r in rows])


def headerless(path, rows):
    path.write_text(''.join(r['name']+'\t'+r['expr']+'\n' for r in rows),encoding='utf-8')


def schematic_files():
    common='''<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#526d83"/></marker></defs>'''
    mechanism='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 340" role="img" aria-label="Finite source routes to liquid outlet and hydrogel wall"><rect width="1120" height="340" fill="#f7fafc"/>'''+common+'''<g font-family="Segoe UI,Arial,sans-serif" fill="#183348">
    <rect x="30" y="100" width="310" height="160" rx="16" fill="#dcebf6" stroke="#8caac2"/><text x="52" y="136" font-size="22" font-weight="600">Finite initialized source</text><text x="52" y="172" font-size="18">p0 + gas volume → available E0</text><text x="52" y="205" font-size="17">Pressure falls as Vg grows</text><text x="52" y="238" font-size="17">One short activation; initial data</text>
    <rect x="590" y="35" width="490" height="115" rx="16" fill="#e2edf9" stroke="#8caac2"/><text x="613" y="72" font-size="22" font-weight="600">Liquid outlet — A and open B</text><text x="613" y="106" font-size="18">U → emitted mass, energy Eout, impulse Iout</text><text x="613" y="135" font-size="16">Column storage Kjet remains a separate output</text>
    <rect x="590" y="195" width="490" height="115" rx="16" fill="#eee3f4" stroke="#aa90b7"/><text x="613" y="231" font-size="22" font-weight="600">Gel wall — Model B</text><text x="613" y="265" font-size="18">R, Uw → elastic pressure and hemisphere force</text><text x="613" y="294" font-size="16">Radial inertia + stored elastic work + loss</text>
    <path d="M340 153 C420 153 420 94 580 94" fill="none" stroke="#526d83" stroke-width="3" marker-end="url(#arrow)"/><path d="M340 208 C420 208 420 253 580 253" fill="none" stroke="#526d83" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="362" y="71" font-size="16">Discharge increases Vg</text><text x="357" y="298" font-size="16">Wall expansion increases Vg</text><text x="32" y="38" font-size="19" font-weight="600">A: fixed wall     B open: two energy routes     B sealed: wall route, zero discharge</text></g></svg>'''
    interface='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 340" role="img" aria-label="Model Builder, Settings, Graphics and result areas"><rect width="1120" height="340" fill="#f7fafc"/><g font-family="Segoe UI,Arial,sans-serif" fill="#183348"><rect x="20" y="20" width="300" height="240" rx="10" fill="#e3ebf2"/><rect x="335" y="20" width="425" height="240" rx="10" fill="#eef3f7"/><rect x="775" y="20" width="325" height="240" rx="10" fill="#e6eef8"/><text x="38" y="53" font-size="23" font-weight="600">1 · Model Builder</text><text x="354" y="53" font-size="23" font-weight="600">2 · Settings</text><text x="794" y="53" font-size="23" font-weight="600">3 · Graphics</text><g font-size="17"><text x="38" y="92">Global Definitions</text><text x="59" y="124">Parameters 1</text><text x="38" y="156">Component c</text><text x="59" y="188">Definitions → Variables</text><text x="59" y="221">Global Equations 1</text><text x="354" y="96">Selected equation row:</text><text x="354" y="132">Name: vv</text><text x="354" y="166">f: tau*(vvt-acc/Us)</text><text x="354" y="202">Initial u: 0     Initial ut: 0</text><text x="354" y="237">Commit cells with Tab</text></g><path d="M807 220 H1076 M807 220 V86" fill="none" stroke="#627b91" stroke-width="2"/><path d="M807 219 C817 115 858 100 883 118 S959 193 1075 220" fill="none" stroke="#3479cb" stroke-width="4"/><text x="814" y="81" font-size="17">U(t)</text><text x="943" y="245" font-size="16">First ejection time</text><rect x="20" y="275" width="1080" height="45" rx="8" fill="#dce6ef"/><text x="40" y="304" font-size="18">Bottom: Progress · Messages · Log · numerical result tables</text></g></svg>'''
    (ROOT/'assets/guide-mechanisms.svg').write_text(mechanism,encoding='utf-8')
    (ROOT/'assets/guide-interface.svg').write_text(interface,encoding='utf-8')


def make_html(source):
    from bilingual_reader import write_guide
    write_guide(source)


def main():
    audit=json.loads((ROOT/'verification/NUMERICAL_AUDIT.json').read_text(encoding='utf-8'))
    models=[extract(ROOT/'models'/r['file']) for r in audit['native_files']]
    a,b=models
    for info,row in zip(models,audit['native_files']):
        if hashlib.sha256((ROOT/'models'/row['file']).read_bytes()).hexdigest()!=row['sha256']:
            raise AssertionError('Native evidence hash changed')
    ap,bp={r['name']:r for r in a['parameters']},{r['name']:r for r in b['parameters']}
    av,bv={r['name']:r for r in a['variables']},{r['name']:r for r in b['variables']}
    patch=[r for r in b['variables'] if r['expr']!=av[r['name']]['expr']]
    if len(patch)!=9 or len(a['equations'])!=5 or len(b['equations'])!=7:
        raise AssertionError('Unexpected A-to-B conversion')
    for key,model in [('A',a),('B',b)]:
        headerless(GUI/f'{key}_parameters_import.txt',model['parameters'])
        headerless(GUI/f'{key}_variables_import.txt',model['variables'])
        (GUI/f'{key}_equations.tsv').write_text('Name\tf(u,ut,utt,t)\tu_0\tut_0\n'+''.join('\t'.join(r)+'\n' for r in model['equations']),encoding='utf-8')
    headerless(GUI/'B_variables_patch_import.txt',patch)
    (GUI/'global_evaluation.tsv').write_text('Expression\tUnit\tDescription\n'+''.join('\t'.join(r)+'\n' for r in EVAL),encoding='utf-8')
    (GUI/'stop_conditions.tsv').write_text('Expression\tStop if\tActive\tDescription\n'+''.join(r[0]+'\tNegative (<0)\tYes\t'+r[3]+'\n' for r in a['conditions']),encoding='utf-8')
    reg=json.loads((ROOT/'data/native_case_register.json').read_text(encoding='utf-8'))
    ar=next(r for r in reg if r['name']=='A_baseline');br=next(r for r in reg if r['name']=='B_open_baseline')
    from reference import Case,source_pressure
    base=Case()
    vg=4*3.141592653589793*base.gas_radius**3/3
    vc=4*3.141592653589793*base.chamber_radius**3/3
    area=3.141592653589793*base.port_radius**2
    checks=[('Initial gas volume `Vg0`',f'{vg:.9e} m³'),('Initial chamber volume `Vc0`',f'{vc:.9e} m³'),
            ('Outlet area `A`',f'{area:.9e} m²'),('Finite budget `Lbudget`',f'{(vc-vg)/area*1e6:.6f} µm'),
            ('Inertance length `L`','50 µm'),('Meniscus pressure `pCap`','28.8 kPa'),
            ('Time scale `tau`','3 µs'),('Initial absolute `p0`','379.631631 kPa'),
            ('Available work `E0`','2 nJ'),('Column-speed bound `Uceiling`',f"{ar['energy_only_speed_ceiling_m_s']:.6f} m/s")]
    def endpoint(r):
        last=r['last_native_state']
        return table(['Expression','Unit','Accepted last stored value'],[
            ('`t`','`us`',f"{r['last_time_s']*1e6:.4f}"),('`c.Eout`','`nJ`',f"{last['emitted_energy_J']*1e9:.9f}"),
            ('`c.Iout`','`N*s`',f"{last['emitted_impulse_N_s']:.9e}"),('`c.Mout`','`ng`',f"{last['emitted_mass_kg']*1e12:.7f}"),
            ('`c.x`','`um`',f"{last['x_m']*1e6:.7f}"),('`c.U`','`m/s`',f"{last['u_m_s']:.7g}"),
            ('`c.energyResidual`','`1`',f"{last['residual']:.4e}")])
    family=[]
    for energy in [0.5,2,5]:
        p=source_pressure(Case(energy=energy*1e-9))
        for radius in [3,5,10]:
            name=f'A_E{energy:g}nJ_a{radius}um'
            r=next(r for r in reg if r['name']==name)
            family.append((name,f'{energy:g}',code(f'{p:.10f}[Pa]'),code(f'{radius}[um]'),f"{r['native_max_jet_speed_m_s']:.6f}"))
    sr=ar['last_native_state']
    ratios=[('`c.U/('+str(ar['native_max_jet_speed_m_s'])+'[m/s])`','All → Maximum','Peak-speed ratio'),
            ('`c.qJet/('+str(ar['native_max_jet_dynamic_Pa'])+'[Pa])`','All → Maximum','Peak dynamic-pressure ratio'),
            ('`c.Eout/('+str(sr['emitted_energy_J'])+'[J])`','Last → None','Emitted-energy ratio'),
            ('`c.Iout/('+str(sr['emitted_impulse_N_s'])+'[N*s])`','Last → None','Emitted-impulse ratio')]
    controls=[]
    inputs=json.loads((ROOT/'data/case_inputs.json').read_text(encoding='utf-8'))
    if isinstance(inputs,dict): inputs=list(inputs.values())
    for r in reg:
        if r['name'].startswith('B_'):
            i=next(c for c in inputs if c['name']==r['name'])
            controls.append((r['name'],code(f"{i['shear_modulus']/1000:g}[kPa]"),code(f"{i['gel_viscosity']:g}[Pa*s]"),code(i['loss_coefficient']),code(int(i['open_port'])),f"{r['native_max_jet_speed_m_s']:.6f}"))
    groups=[['x','U','R','Uw','Vg','Vdot','pb'],['pEl','pRes','Wgel','Kgel','Kjet','Esurf','ploss']]
    rest=[r for r in a['variables'] if r['name'] not in sum(groups,[])]
    replacements={
        'A_PARAMETERS':table(['Name','Expression — enter exactly','Meaning'],[(code(r['name']),code(r['expr']),r['descr']) for r in a['parameters']]),
        'PARAMETER_CHECKS':table(['Quantity','Expected value'],checks),
        'A_SOURCE_VARIABLES':variables_table([av[n] for n in groups[0]]),
        'A_MECHANICS_VARIABLES':variables_table([av[n] for n in groups[1]]),
        'A_ACCOUNTING_VARIABLES':variables_table(rest),
        'A_EQUATIONS':table(['Name','f(u,ut,utt,t) — enter exactly','u_0','ut_0'],[[code(x) for x in r] for r in a['equations']]),
        'B_EQUATIONS':table(['Name','f(u,ut,utt,t) — enter exactly','u_0','ut_0'],[[code(x) for x in r] for r in b['equations']]),
        'STOP_CONDITIONS':table(['Stop expression','Stop if','Active','Description'],[(code(r[0]),'Negative (<0)','Yes',r[3]) for r in a['conditions']]),
        'GLOBAL_EVALUATION':table(['Expression','Unit','Description'],[(code(e),code(u),d) for e,u,d in EVAL]),
        'A_ENDPOINT':endpoint(ar),'B_ENDPOINT':endpoint(br),'B_PATCH':variables_table(patch),
        'PRESSURE_WORK_MAP':table(['Available work','Absolute p0 — enter exactly'],[(f'{e:g} nJ',code(f'{source_pressure(Case(energy=e*1e-9)):.10f}[Pa]')) for e in [0.5,2,5]]),
        'A_FAMILY':table(['Case','E0 (nJ)','p0','a','Expected peak U (m/s)'],family),
        'TRANSMISSION_EXPRESSIONS':table(['Expression (Unit 1)','Time selection → Transformation','Meaning'],ratios),
        'B_CONTROLS':table(['Case','G','etaG','Kloss','outletOpen','Expected peak U (m/s)'],controls)}
    source=(ROOT/'sources/guide/STEP_BY_STEP.template.md.txt').read_text(encoding='utf-8')
    for key,value in replacements.items(): source=source.replace('@'+key+'@',value)
    if re.search(r'@[A-Z_]+@',source): raise AssertionError('Unresolved content placeholder')
    if any(ord(c)<32 and c not in '\n\r\t' for c in source): raise AssertionError('Nonprinting source character')
    (ROOT/'STEP_BY_STEP.md').write_text(source,encoding='utf-8')
    schematic_files();make_html(source)
    manifest={'status':'PASS','steps':53,'languages':['en','zh'],'default_language':'en','parameters_per_model':32,'variables_per_model':33,'state_counts':[5,7],
              'changed_A_to_B_variables':[r['name'] for r in patch],'native_models':audit['native_files'],
              'resources':sorted(p.name for p in GUI.iterdir() if p.is_file()),
              'scope':'Exact table extraction and guide generation; native import/conversion check is separately recorded.'}
    (ROOT/'verification/GUIDE_CONTENT_AUDIT.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print('Detailed guide generated:',len(source.split()),'words; 53 steps; 32 parameters / 33 variables; 9 exact B replacements.')


if __name__=='__main__': main()
