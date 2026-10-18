"""Select complete scientific passages without rewriting the supplied reasoning."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'sources/chapter01-handoff-20261019'

def main():
    passages={}
    def add(number,name,start,end=None,supplement=False):
        p=SOURCE/name
        original=p.read_text(encoding='utf-8')
        a=original.index(start) if start else 0
        b=original.index(end,a) if end else len(original)
        excerpt=original[a:b].strip()
        assert excerpt
        passages.setdefault(f'C1-E{number:02d}',{'supplement':supplement,'passages':[]})['passages'].append({
            'source':name,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
            'first_line':original[:a].count('\n')+1,'last_line':original[:b].count('\n')+1,
            'excerpt_sha256':hashlib.sha256(excerpt.encode('utf-8')).hexdigest(),'markdown':excerpt})
    def defense(number,name,start,end=None,supplement=False):
        add(number,'defense_originals/'+name+'.md',start,end,supplement)
    defense(1,'Defense_C1_E01_Initial_Wall_Velocity','**English**',supplement=True)
    defense(3,'Defense_C1_E03_Why_Velocity_Potential','## 1.','**Source:**')
    bernoulli='Defense_C1_E05_Missing_Bernoulli_Derivation'
    defense(4,bernoulli,'From C1-E03,\n','The kinematic boundary condition',True)
    defense(5,bernoulli,'## 1.','## Defense conclusion')
    kinetic='Defense_C1_Energy_Kinetic_Expression'
    defense(9,kinetic,'## 1.','## 2.')
    energy='Defense_C1_Mechanical_Energy_Balance'
    defense(10,energy,'The left-hand side','Move the capillary term',True)
    defense(11,energy,'## 2.','**Defense conclusion:')
    collapse='Defense_C1_Ideal_Collapse_Rdot_Derivation'
    defense(12,collapse,'## Complete derivation','Define the squared wall velocity',True)
    defense(13,collapse,'Define the squared wall velocity','Integrate from')
    defense(14,collapse,'Integrate from','**Revision observation')
    defense(17,kinetic,'## 2.','**Defense conclusion.')
    defense(19,'Defense_C1_Mach_Threshold_Radius_2026-10-19','## 1.','**Defense conclusion:')
    impulse='Defense_C1_Section_1_6_Pressure_Impulse'
    defense(20,impulse,'## 1.','## 5.')
    integration='Defense_C1_E22_Time_Integration'
    defense(21,integration,'## 1.','## 4.')
    defense(22,integration,'## 4.','## 5.',True)
    defense(23,impulse,'## 5.',"For the course's illustrative pressure difference",True)
    defense(23,integration,'## 5.','## Defense conclusion',True)
    defense(24,impulse,"For the course's illustrative pressure difference",'**Defense decision',True)
    defense(26,integration,'## 1.','## 2.',True)
    moving='Defense_C1_E29_Moving_Interface_Closure_2026-10-19'
    defense(27,moving,'## 3.','## 4.',True)
    defense(28,moving,'**Core answer','## 7.')
    defense(29,moving,'## 7.','## Defense outcome')
    add(30,'Chapter_1_C1_E31_Compressibility_Test_EN_ZH.md','## 1.')
    target=ROOT/'content/chapter01_handoff.json'
    target.write_text(json.dumps(passages,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'groups_with_original_passages':len(passages),'passages':sum(len(v['passages']) for v in passages.values())}))

if __name__=='__main__':main()
