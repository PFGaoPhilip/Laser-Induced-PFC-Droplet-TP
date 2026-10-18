"""Faithful bilingual source passages with short, explained formula displays.

Markdown is an authoring dependency. The generated reader has no remote assets.
Source prose is retained verbatim; equation references follow the owner map.
"""
from html import escape
import json
from pathlib import Path
import re
import markdown
from bs4 import BeautifulSoup
from coursekit import P
from equation_symbols import equation_label
from chapter01_narrative import rows

PASSAGES=json.loads(Path(__file__).with_suffix('.json').read_text(encoding='utf-8'))
DISPLAY=re.compile(r'\$\$([\s\S]*?)\$\$|\\\[([\s\S]*?)\\\]')
INLINE=re.compile(r'\\\(([\s\S]*?)\\\)|(?<!\\)\$([^$\n]+?)(?<!\\)\$')

def references(text):
    def remap(m):
        old=int(m[1]); assert old!=12,'Deleted dissipation material must stay excluded'
        new=old if old<12 else old-1
        return equation_label(f'C1-E{new:02d}')
    return re.sub(r'\bC1-E(\d{2})\b',remap,text)

# These are added explanations for individual rows in preserved source chains.
# The original complete source paragraphs still precede the first row.
ROW_REASONS={
 ('C1-E03',0,5):[
  ('Use the material-wall condition to identify liquid speed at the interface.','利用物质壁面的运动学条件确定界面处液体速度。'),
  ('Evaluate Bernoulli at the wall and isolate the pressure difference.','在壁面计算伯努利关系，并解出压力差。'),
  ('Insert the fixed-position derivative and combine the squared-speed terms.','代入固定位置导数，并合并速度平方项。')],
 ('C1-E05',0,12):[
  ('Remove the outer minus sign while retaining the kinetic contribution.','展开外部负号，同时保留动能项。'),
  ('Combine two minus one half to obtain three halves.','将二减去二分之一合并为二分之三。')],
 ('C1-E09',0,1):[
  ('Substitute the inverse-square radial velocity into the kinetic-energy density.','将平方反比径向速度代入动能密度。'),
  ('Collect factors independent of the shell radius outside the integral.','将与球壳径向坐标无关的因子提出积分号。'),
  ('Use the antiderivative of the inverse-square shell-radius factor.','使用球壳半径平方反比项的原函数。'),
  ('Evaluate the infinite and wall endpoints, then cancel one radius factor.','计算无穷远端点与壁面端点，再约去一个半径因子。')],
 ('C1-E17',0,1):[
  ('Cancel density and expand the cube of the radius ratio.','约去密度，并展开半径比例的三次方。'),
  ('Distribute the radius cubed to obtain the difference of cavity volumes.','将半径三次方乘入括号，得到空腔体积之差对应的表达式。')],
 ('C1-E21',0,3):[
  ('Define this endpoint difference as the fixed-position velocity increment.','将该端点差定义为固定位置的速度增量。')],
 ('C1-E21',0,6):[
  ('The spatially uniform reference contributes zero gradient; commute the remaining gradient and integral.','空间均匀参考压强的梯度为零；交换剩余梯度与积分的次序。')],
}
ADJACENT_REASONS={
 ('C1-E20',0,0):('At one fixed liquid position, integrate pressure excess over the stated event interval. This defines pressure impulse.','在固定液体位置，对给定事件区间内的超压作时间积分。由此定义压力冲量。'),
 ('C1-E19',0,7):('Add one to both sides to isolate the inverse cube of the radius ratio.','两侧加一，分离出半径比例的负三次方。'),
 ('C1-E19',0,8):('The radius ratio is positive; take the negative one-third power of both sides.','半径比例为正；对两侧取负三分之一次幂。'),
}
TRANSITION_REASONS={
 ('C1-E05',0,2):('Apply the spatial chain rule to one half of the squared radial speed.','对径向速度平方的一半应用空间链式法则。'),
 ('C1-E05',0,7):('Insert the far-field value of the integration function and use velocity as the potential gradient.','代入积分函数的远场值，并将速度写成速度势的梯度。'),
 ('C1-E17',0,2):('Identify each spherical volume as four thirds pi times its radius cubed.','将每个球体积识别为其半径三次方乘以三分之四圆周率。'),
 ('C1-E19',0,2):('Substitute the normalized radius into the collapse speed and take its magnitude.','将归一化半径代入塌缩速度，并取速度大小。'),
 ('C1-E19',0,6):('Divide by the positive pressure coefficient to isolate the radius-dependent factor.','除以正的压力系数，分离出随半径变化的因子。'),
 ('C1-E28',0,12):('Combine the negative half and positive whole squared-speed contributions.','合并负二分之一与正一倍的速度平方项。'),
}

def formula_parts(identifier,passage,index,tex):
    """Split genuine transformations; keep a single wrapped equality intact."""
    tag=re.search(r'\\tag\{([^}]*)\}\s*$',tex)
    content=tex[:tag.start()].strip() if tag else tex.strip()
    matched=re.fullmatch(r'\\begin\{aligned\}([\s\S]*)\\end\{aligned\}',content)
    if matched and not re.search(r'\\\\\s*&\s*(?:[+-]|\\quad[+-])',matched[1]):
        parts=rows(content)
        notes=ROW_REASONS.get((identifier,passage,index),[])
        assert len(notes)==len(parts)-1,(identifier,passage,index,len(parts),len(notes))
        for n,part in enumerate(parts):
            part['note']=notes[n-1] if n else None
        if tag:parts[-1]['display_tex']+=tag[0]
        return parts
    return [dict(source_tex=content,display_tex=tex.strip(),note=None)]

def render_passage(identifier,pindex,source):
    text=references(source['markdown'])
    displays=[];inlines=[]
    def stash_display(m):
        displays.append(next(x for x in m.groups() if x).strip())
        return '\n\n<div class="handoff-formula" data-index="'+str(len(displays)-1)+'"></div>\n\n'
    text=DISPLAY.sub(stash_display,text)
    def stash_inline(m):
        inlines.append(next(x for x in m.groups() if x))
        return f'HANDOFFINLINE{len(inlines)-1}TOKEN'
    text=INLINE.sub(stash_inline,text)
    html=markdown.markdown(text,extensions=['tables','sane_lists'])
    soup=BeautifulSoup(html,'html.parser')
    output=[];pending=[];pending_kind=None;block=0
    def inner(node):return ''.join(str(c) for c in node.contents)
    def bilingual(value):
        # Bilingual source lines use a spaced slash. Slashes inside math/code
        # do not meet this delimiter and retain their literal meaning.
        if ' / ' in value:
            a,b=value.split(' / ',1)
            if re.search('[\u3400-\u9fff]',BeautifulSoup(b,'html.parser').get_text()):return a,b
        return None
    def pair(a,b,kind='p'):
        nonlocal block
        attr=f'data-handoff-text="{block}"';block+=1
        if kind.startswith('h'):
            return f'<div class="heading-pair" {attr}><h4 lang="en">{a}</h4><h4 lang="zh-CN" class="zh">{b}</h4></div>'
        return f'<div class="lang-pair derivation-reason" {attr}><p lang="en">{a}</p><p lang="zh-CN" class="zh">{b}</p></div>'
    def flush():
        nonlocal pending,pending_kind
        if not pending:return
        ens=[];zhs=[]
        for value in pending:
            both=bilingual(value)
            if both:ens.append(both[0]);zhs.append(both[1]);continue
            plain=BeautifulSoup(value,'html.parser').get_text()
            if plain.strip() in ['English','中文']:continue
            (zhs if re.search('[\u3400-\u9fff]',plain) else ens).append(value)
        assert len(ens)==len(zhs),(identifier,pindex,pending_kind,len(ens),len(zhs),pending)
        output.extend(pair(a,b,pending_kind) for a,b in zip(ens,zhs))
        pending=[];pending_kind=None
    for node in soup.find_all(recursive=False):
        if node.name in ['p','h1','h2','h3','h4']:
            kind='h4' if node.name.startswith('h') else 'p'
            if pending_kind and pending_kind!=kind:flush()
            pending_kind=kind;pending.append(inner(node))
            continue
        flush()
        if node.name=='div' and 'handoff-formula' in node.get('class',[]):
            i=int(node['data-index']);tex=displays[i]
            adjacent=not output or 'math-display' in output[-1] or 'class="heading-pair"' in output[-1]
            if adjacent:
                note=ADJACENT_REASONS.get((identifier,pindex,i))
                assert note,(identifier,pindex,i,'missing explanation between source displays')
                output.append(P(*note,'derivation-reason source-supplement'))
            transition=TRANSITION_REASONS.get((identifier,pindex,i))
            if transition:output.append(P(*transition,'derivation-reason source-supplement'))
            for r,part in enumerate(formula_parts(identifier,pindex,i,tex)):
                if part['note']:output.append(P(*part['note'],'derivation-reason source-supplement'))
                output.append(f'<div class="math-display" data-handoff-formula="{i}" data-handoff-row="{r}" '
                    f'data-source-tex="{escape(part["source_tex"],quote=True)}" '
                    f'data-tex="{escape(part["display_tex"],quote=True)}"></div>')
        elif node.name in ['ol','ul']:
            items=[inner(li) for li in node.find_all('li',recursive=False)]
            merged=[];ens=[];zhs=[]
            for item in items:
                both=bilingual(item)
                if both:merged.append(pair(*both));continue
                (zhs if re.search('[\u3400-\u9fff]',BeautifulSoup(item,'html.parser').get_text()) else ens).append(item)
            assert len(ens)==len(zhs),(identifier,'list parity')
            merged.extend(pair(a,b) for a,b in zip(ens,zhs))
            output.append('<'+node.name+'>'+''.join('<li>'+x+'</li>' for x in merged)+'</'+node.name+'>')
        elif node.name=='table':
            for cell in node.select('td,th'):
                both=bilingual(inner(cell));assert both,(identifier,'table parity',str(cell))
                rendered=BeautifulSoup(pair(*both),'html.parser');cell.clear();cell.extend(rendered.contents)
            output.append('<div class="table-wrap">'+str(node)+'</div>')
        else:raise AssertionError((identifier,'unhandled source block',str(node)))
    flush()
    result=(f'<div class="handoff-passage" data-handoff-passage="{pindex}" '
            f'data-excerpt-sha256="{source["excerpt_sha256"]}">'+''.join(output)+'</div>')
    # Restore math after the HTML structure is complete. Literal inequality
    # signs must never enter an intermediate HTML parse as angle brackets.
    for n,tex in enumerate(inlines):result=result.replace(f'HANDOFFINLINE{n}TOKEN','$'+escape(tex,quote=False)+'$')
    return result

def handoff_flow(identifier,supplement):
    """Use supplied passages directly; supplement derivations absent in them."""
    record=PASSAGES.get(identifier)
    if not record:return None
    content=''.join(render_passage(identifier,i,p) for i,p in enumerate(record['passages']))
    if record['supplement']:
        content+=P('<strong>Additional worked steps.</strong> The following steps supply details beyond the preserved handoff passage.',
                   '<strong>补充的完整步骤。</strong> 以下步骤补充所保留交接材料之外的细节。','derivation-reason')
        for part in supplement:
            content+=P(part['en'],part['zh'],'derivation-reason')
            content+=(f'<div class="math-display" data-phase="{escape(part["phase"])}" '
                      f'data-source-tex="{escape(part["source_tex"],quote=True)}" '
                      f'data-tex="{escape(part["display_tex"],quote=True)}"></div>')
    return '<div class="derivation-flow" data-source-mode="handoff">'+content+'</div>'
