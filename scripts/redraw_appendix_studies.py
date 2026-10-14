"""English editable redraws for Appendix A and live study readers.
Scientific source equations/data remain unchanged.
"""
from pathlib import Path
import json, math, re, sys, hashlib, csv, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/figures-editable/appendix-studies'
OUT.mkdir(parents=True,exist_ok=True)
COL={'bg':'#142632','fg':'#E7F0F3','muted':'#B4C7D2','accent':'#8EDBD4','area':'#213E4B'}

class Scene:
 def __init__(self,w=980,h=650):self.data={'slide':{'width':w/100,'height':h/100},'background':COL['bg'],'objects':[]}
 def add(self,kind,**kw):
  idx=len(self.data['objects']);self.data['objects'].append(dict(type=kind,id=f'obj-{idx:03d}',name=kw.pop('name',f'{kind} {idx}'),**kw))
 def txt(self,x,y,text,w=800,size=18,color='fg'):
  self.add('text',x=x/100,y=(y-21)/100,w=w/100,h=.34,text=text,font='Arial',font_size=size*.72,color=COL.get(color,color),margin=0,word_wrap=False)
 def line(self,x1,y1,x2,y2,arrow=False,color='accent'):
  self.add('arrow' if arrow else 'line',x1=x1/100,y1=y1/100,x2=x2/100,y2=y2/100,line=COL[color],line_width=1.7)
 def circle(self,x,y,r,fill=None):self.add('ellipse',x=(x-r)/100,y=(y-r)/100,w=2*r/100,h=2*r/100,fill=COL.get(fill,fill),line=COL['muted'],line_width=1.4)
 def rect(self,x,y,w,h,fill='area'):self.add('rect',x=x/100,y=y/100,w=w/100,h=h/100,fill=COL.get(fill,fill),line=COL['muted'],line_width=1.4)

def read_labels(path):
 tree=ET.parse(path);return tree,[n.text or '' for n in tree.iter() if n.tag.endswith('}text')]

def appendix_scene(path):
 tree,labels=read_labels(path);vb=tree.getroot().get('viewBox').split();s=Scene(float(vb[2]),float(vb[3]));ident=path.stem.upper()
 n=int(ident.split('E')[1]);s.txt(28,36,ident+' · Physical variable map',size=20,color='accent')
 start=labels.index('Variables in this equation / 本式变量')
 # All variable and validity labels are English in the authoritative figure.
 bottom=labels[start+1:]
 if n in [7,12,14,22]:
  s.circle(180,179,77);s.circle(180,179,29,'area');s.line(180,179,257,179,True);s.txt(220,158,'R',w=90)
  s.txt(110,290,'Rref → R',w=240);s.txt(82,92,'Cavity pressure work: pb dV',w=390)
  s.rect(436,125,410,123);s.txt(459,164,'Elastic storage: Wg',w=380);s.txt(459,207,'Viscous loss: Ḋg ≥ 0',w=380)
  s.line(273,180,431,180,True);s.txt(436,287,'Gg , ηg ; intact network',w=450)
  s.txt(82,335,'Jet energy requires a separate load path and budget',w=850,size=17)
 elif n in [16,17,18,19,23]:
  if n==18:
   s.txt(97,88,'Comparison of two declared controls',w=800)
   s.rect(109,119,610,40);s.txt(130,146,'ts = 6.70820 µs — shear transit',w=560)
   s.rect(109,207,250,40);s.txt(130,234,'tc,liq = 2.74404 µs',w=230,size=16)
   s.txt(390,236,'Ideal liquid collapse',w=410,size=17)
   s.txt(110,313,'ts / tc,liq = 2.44464 ; Lg = Rmax = 30 µm',w=820)
  else:
   terms={16:['τe: transient event duration','τrel: material stress memory','De = τrel / τe'],17:['Unloaded Kelvin–Voigt shear: Tsh = 0','Strain recovers after unloading','τKV = ηg / Gg'],19:['cL: longitudinal wave speed','tL = Lg / cL','Mw = |Ṙ| / cL'],23:['De = τrel / τe','ts = Lg √(ρg / Gg)','tporo ≈ μl Lg² / (kperm Md)']}[n]
   s.txt(99,88,'Response times and dimensionless comparisons',w=820)
   for y,t in zip([142,205,268],terms):s.rect(109,y-25,740,38);s.txt(129,y,t,w=710)
   s.txt(110,334,'Equal boxes list definitions; lengths do not encode time',w=840,size=16)
 elif n==20:
  for x in range(105,625,45):s.line(x,112,x,266,color='muted')
  for y in range(116,269,38):s.line(96,y,622,y,color='muted')
  for y in [140,193,244]:s.line(118,y,710,y,True)
  s.txt(105,88,'Solvent flow relative to an intact network',w=810)
  s.txt(735,180,'jl →',w=170);s.line(510,290,215,290,True);s.txt(560,298,'∇ppore ←',w=320)
  s.txt(156,334,'Lg , kperm , μl , Md ; tporo',w=740)
 elif n==24:
  # Explicit cross-section: upward liquid traction lifts film; release front is separate.
  s.rect(107,230,760,55);s.rect(107,150,760,16)
  s.txt(108,100,'Target film: loaded footprint At',w=800)
  for x in [260,450,640]:s.line(x,225,x,172,True)
  s.txt(300,210,'tload ; t₀ → t₁',w=430);s.txt(120,315,'Donor / support',w=300)
  s.txt(520,315,'Release area Arel ; Γc',w=410)
  s.txt(108,353,'Impulse: Jtarget     Minimum separation work: Wsep,min',w=820,size=17)
 else:
  # A material shell maps between configurations with equal enclosed network volume.
  rr=(80**3+78**3-36**3)**(1/3)
  s.circle(196,180,80);s.circle(196,180,36,'area');s.line(196,180,232,180,True);s.txt(192,160,'Rref',w=120)
  s.line(196,180,252.5685,236.5685,True);s.txt(252,255,'r₀',w=90)
  s.circle(610,180,rr);s.circle(610,180,78,'area');s.line(610,180,688,180,True);s.txt(651,160,'R',w=70)
  s.line(610,180,610+rr/math.sqrt(2),180+rr/math.sqrt(2),True);s.txt(697,265,'r',w=70)
  s.line(295,180,480,180,True);s.txt(310,146,'Material map',w=250)
  s.txt(110,303,'Reference',w=250);s.txt(530,312,'Deformed: λr , λθ',w=370)
  s.txt(748,106,'Gg , ηg',w=180);s.txt(748,153,'σrr , σθθ',w=200);s.txt(748,201,'p∞',w=150);s.txt(576,205,'pb',w=90)
  s.txt(95,348,'r₀³ − Rref³ = r³ − R³ ; radial coordinates point outward',w=850,size=16)
 s.txt(28,400,'Variables and physical limits',size=18,color='accent')
 y=438
 for t in bottom:
  if not t.strip():continue
  # Original wrapping is retained for the variable list.
  s.txt(40,y,t,w=920,size=16);y+=23
 s.data['slide']['height']=max(s.data['slide']['height'],(y+20)/100)
 return s.data


def native_stability_source(source):
 """Replace imshow raster tiles with exact data-backed native vector cells."""
 import matplotlib
 from matplotlib.colors import TwoSlopeNorm, to_hex
 tree=ET.parse(source);root=tree.getroot();ns='{http://www.w3.org/2000/svg}'
 rows=list(csv.DictReader((source.parents[1]/'data/stability_comparison.csv').open(encoding='utf8')))
 norm=TwoSlopeNorm(0,vmin=-100,vmax=200);cmap=matplotlib.colormaps['RdBu']
 images=[(parent,node) for parent in root.iter() for node in list(parent) if node.tag==ns+'image']
 for index,(parent,node) in enumerate(images):
  group=ET.Element(ns+'g',{'id':f'native-heatmap-{index}'})
  x=float(node.get('x'));w=float(node.get('width'));h=float(node.get('height'))
  y=-float(node.get('y'))
  if index<2:
   fluid=['n-Perfluoropentane','n-Perfluorohexane'][index]
   for i,radius in enumerate([.15,.3,1.5,3,6]):
    for j,stretch in enumerate([1.2,1.5,1.8,2.1]):
     row=next(r for r in rows if r['fluid']==fluid and float(r['shear_Pa'])==20000 and abs(float(r['radius_m'])-radius*1e-6)<1e-15 and float(r['stretch'])==stretch and not r['name'].startswith('PFP_interface'))
     value=float(row['closed_energy_restoring_Pa_per_stretch'])/1000
     ET.SubElement(group,ns+'rect',{'x':str(x+j*w/4),'y':str(y+i*h/5),'width':str(w/4+.001),'height':str(h/5+.001),'fill':to_hex(cmap(norm(value))),'stroke':'none'})
  else:
   for i in range(270):
    # The original colorbar is uniformly spaced in normalized color coordinates.
    ET.SubElement(group,ns+'rect',{'x':str(x),'y':str(y+i*h/270),'width':str(w),'height':str(h/270+.001),'fill':to_hex(cmap(1-(i+.5)/270)),'stroke':'none'})
  parent.insert(list(parent).index(node),group);parent.remove(node)
 target=OUT/'embedded-pfc-feasibility-radial_stability.vector-source.svg';tree.write(target,encoding='utf8',xml_declaration=True)
 return target

def repair_rotated_glyph_labels(scene,source):
 """Place path-font SVG labels using their actual original baseline advances."""
 from matplotlib.font_manager import FontProperties
 from matplotlib.textpath import TextToPath
 root=ET.fromstring(source.read_text(encoding='utf8'),parser=ET.XMLParser(target=ET.TreeBuilder(insert_comments=True)))
 width=float(root.get('viewBox').split()[2]);scale=scene['slide']['width']/width
 used=set()
 for parent in root.iter():
  if not isinstance(parent.tag,str) or not parent.get('id','').startswith('text_'):continue
  comments=[c.text.strip() for c in parent if c.tag is ET.Comment]
  child=next((c for c in parent if isinstance(c.tag,str) and c.get('transform')),None)
  if not comments or child is None or 'rotate(-90)' not in child.get('transform',''):continue
  match=re.search(r'translate\(([-.\d]+) ([-.\d]+)\)',child.get('transform'));px,py=map(float,match.groups())
  label=comments[0];obj=next(o for o in scene['objects'] if o.get('text')==label and o['id'] not in used);used.add(obj['id'])
  advance=TextToPath().get_text_width_height_descent(label,FontProperties(family='DejaVu Sans',size=10),False)[0]*scale
  h=obj['h'];w=advance*1.13+.04
  obj.update(x=px*scale-h*.35-w/2,y=py*scale-advance/2-h/2,w=w)

def restore_chart_markers(scene,source):
 """Preserve exact source sample locations as native circle markers."""
 root=ET.parse(source).getroot();ns='{http://www.w3.org/2000/svg}'
 parents={c:p for p in root.iter() for c in p};defs={n.get('id'):n for n in root.iter() if n.get('id')}
 scale=scene['slide']['width']/float(root.get('viewBox').split()[2])
 for node in root.iter():
  if node.tag!=ns+'use' or not node.get('x'):continue
  href=node.get('{http://www.w3.org/1999/xlink}href','').lstrip('#')
  if not href.startswith('m') or href not in defs:continue
  style=node.get('style','');col=re.search(r'fill:\s*(#[0-9a-fA-F]{6})',style)
  if not col:continue
  ancestor=parents.get(node);clipped=False
  while ancestor is not None:
   clipped=clipped or bool(ancestor.get('clip-path'));ancestor=parents.get(ancestor)
  if not clipped:continue
  d=defs[href].get('d','');match=re.match(r'M\s+0\s+([.\d]+)',d)
  if not match or 'C' not in d:continue
  radius=float(match.group(1))*scale;x=float(node.get('x'))*scale;y=float(node.get('y'))*scale
  index=len(scene['objects']);scene['objects'].append({'type':'ellipse','id':f'sample-marker-{index}','name':f'Original data sample marker {index}','x':x-radius,'y':y-radius,'w':2*radius,'h':2*radius,'fill':col.group(1),'line':col.group(1),'line_width':.6})

def main():
 from sci_ppt_common import render_scene, scene_to_svg, make_deck, svg_to_scene
 manifest=[]
 preserved=ROOT/'assets/figures-editable/source-svg'
 source_dir=preserved if (preserved/'a-e01.svg').exists() else ROOT/'assets/figures'
 for source in sorted(source_dir.glob('a-*.svg')):
  scene=appendix_scene(source);name=source.stem
  (OUT/f'{name}.scene.json').write_text(json.dumps(scene,indent=2,ensure_ascii=False),encoding='utf8')
  render_scene(scene,OUT/f'{name}.pptx');scene_to_svg(scene,OUT/f'{name}.svg')
  manifest.append({'id':name,'source':str(source.relative_to(ROOT)).replace('\\','/'),'scene':f'{name}.scene.json','pptx':f'{name}.pptx','svg':f'{name}.svg','kind':'physical schematic','audit':'English labels; material shell preserves incompressible volume; signs and units retained; network assumed intact.'})
 for folder,names in [('minimal-cavitation',['first_event_histories','conditional_velocity_envelope','energy_and_transmission','gel_confinement','guide-mechanisms','guide-interface']),('embedded-pfc-feasibility',['size_species_comparison','radial_viscosity_controls','radial_stability','fracture_budget'])]:
  for name in names:
   source=ROOT/'modeling'/folder/'assets'/f'{name}.svg'
   scene=svg_to_scene(native_stability_source(source) if name=='radial_stability' else source)
   if folder=='minimal-cavitation':repair_rotated_glyph_labels(scene,source)
   restore_chart_markers(scene,source)
   if name=='guide-mechanisms':
    scale=scene['slide']['width']/1120
    for j,y in enumerate([94,253]):scene['objects'].append({'type':'arrow','id':f'route-head-{j}','name':f'Energy route arrow {j+1}','x1':560*scale,'y1':y*scale,'x2':580*scale,'y2':y*scale,'line':'#526D83','line_width':2})
   target=f'{folder}-{name}'
   (OUT/f'{target}.scene.json').write_text(json.dumps(scene,indent=2,ensure_ascii=False),encoding='utf8')
   render_scene(scene,OUT/f'{target}.pptx');scene_to_svg(scene,OUT/f'{target}.svg')
   manifest.append({'id':target,'source':str(source.relative_to(ROOT)).replace('\\','/'),'scene':f'{target}.scene.json','pptx':f'{target}.pptx','svg':f'{target}.svg','kind':'guide schematic' if name.startswith('guide-') else 'quantitative plot','audit':'Exact original English vector geometry retained; numerical series, axes, units, limits, and conditional qualifiers preserved.'})
 for row in manifest:
  source=ROOT/row['source'];row['source_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
  if row['kind']=='quantitative plot':row['numeric_provenance']=[str(x.relative_to(ROOT)).replace('\\','/') for x in sorted((source.parents[1]/'data').glob('*')) if x.suffix in ['.csv','.json']]
 (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
 make_deck([OUT/m['pptx'] for m in manifest],OUT/'appendix-studies.pptx')
 print('Generated',len(manifest),'figures')

if __name__=='__main__':main()
