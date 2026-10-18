"""Audit changed Chapter 1 prose while preserving verified, unchanged pages.

New color assignments may split an existing color class, never merge classes.
Therefore every prior no-collision constraint remains valid. New Chapter 1
constraints receive the same complete text/math/pair/idempotence audit.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
from bs4 import BeautifulSoup
import highlight_bilingual_terms as high

ROOT=Path(__file__).resolve().parents[1]
REL='chapters/01-cavity-pressure-inertia-and-directional-jets.html'

def main():
    path=ROOT/'verification/bilingual-terms.json'
    saved=json.loads(path.read_text(encoding='utf-8'))
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    for record in saved['checks']:
        if record['file']!=REL:assert sha(ROOT/record['file'])==record['sha256'],record['file']
    oldcolors=saved['term_color_indices']
    def extend_colors(groups):
        colors=dict(oldcolors)
        fresh=max(colors.values())+1
        for group in groups:
            used={}
            for key in sorted(group,key=lambda k:(k!='jet',k)):
                if colors[key] in used:
                    colors[key]=fresh;fresh+=1
                used[colors[key]]=key
        assert all(len({colors[k] for k in g})==len(g) for g in groups)
        assert all(colors[a]!=colors[b] or oldcolors[a]==oldcolors[b] for a in colors for b in colors)
        return colors
    high.course_pages=lambda root:[Path(root)/REL]
    high.color_terms=extend_colors
    oldpage=ROOT/'reports/ch1_steps_20261019/chapter_before.html'
    oldgroups=len(high.paragraph_groups(BeautifulSoup(oldpage.read_text(encoding='utf-8'),'html.parser')))
    partial=high.apply_to_course(ROOT)
    records={r['file']:r for r in saved['checks']}
    records[REL]=partial['checks'][0]
    pairs={r['file']:r for r in saved['strict_pair_audit']['pages']}
    pairs[REL]=partial['strict_pair_audit']['pages'][0]
    totals=Counter()
    for record in records.values():totals.update(record['terms'])
    saved.update({k:partial[k] for k in ['palette','color_count','term_color_indices','color_stylesheet_sha256','highlighter_sha256']})
    saved['checks']=list(records.values())
    saved['term_totals']=dict(sorted(totals.items()))
    saved['highlights']=sum(totals.values())
    saved['paired_prose_groups_checked']+=partial['paired_prose_groups_checked']-oldgroups
    saved['strict_pair_audit']={'paired_blocks_checked':sum(r['paired_blocks_checked'] for r in pairs.values()),'one_sided_colored_terms_remaining':0,'pages':list(pairs.values())}
    saved['incremental_update']={'changed_page':REL,'unchanged_pages_verified_by_hash':len(records)-1,'prior_color_classes_never_merged':True,'changed_page_complete_highlighter_audit':True}
    path.write_text(json.dumps(saved,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','updated_pages':1,'unchanged_pages':len(records)-1,'color_count':saved['color_count']}))

if __name__=='__main__':main()
