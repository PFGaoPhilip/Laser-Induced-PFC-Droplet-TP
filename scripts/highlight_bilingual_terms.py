"""Mark corresponding English/Chinese course terms without changing the text.

The saved HTML is self-contained. A shared color map gives different concepts
different colors within paired paragraphs; a native tooltip shows the pair.
"""
from collections import Counter
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import colorsys
import os
import re


# Each entry owns its English and Chinese spellings, including source variants.
# Do not conflate ejection with a jet, or rigid with compliant boundaries.
TERMS = [
    ('absorptance', 'absorptance', '吸收率', []),
    ('absorbed-energy', 'absorbed energy', '吸收能量', ['absorbed laser energy', '吸收激光能量']),
    ('phase-inventory', 'phase inventory', '相存量', ['finite phase inventory', '有限相存量', '相变库存']),
    ('re-entrant-jet', 're-entrant jet', '回入射流', ['re-entrant jets', 'internal collapse jet', 'internal re-entry jet', 're-entry jet', '内部塌缩射流', '再入射流']),
    ('ejected-jet', 'ejected jet', '喷出射流', ['ejected jets', 'exterior jet', 'emitted jet', 'emitted jets', '外部射流']),
    ('liquid-bridge', 'liquid bridge', '液桥', ['liquid bridges', 'liquid bridging', 'capillary bridge', '毛细液桥']),
    ('confinement', 'confinement', '限域', ['confined', '受限']),
    ('traction', 'traction', '牵引', ['tractions', '牵引力']),
    ('absorber', 'absorber', '吸收体', ['absorbers']),
    ('thermal-localization', 'thermal localization', '热局域化', []),
    ('momentum', 'momentum', '动量', []),
    ('microjet', 'microjet', '微射流', ['microjets', 'microjetting', 'micro-jet', 'micro-jets']),
    ('jet-speed', 'jet speed', '射流速度', ['jet velocity', 'jet velocities', 'speed of an observed ejected jet']),
    ('jet', 'jet', '射流', ['jets', 'jetting']),
    ('bubble-dynamics', 'bubble dynamics', '气泡动力学', []),
    ('thermocavitation', 'thermocavitation', '热空化', []),
    ('cavitation-inception', 'cavitation inception', '空化初生', []),
    ('cavitation', 'cavitation', '空化', ['cavitate', 'cavitates', 'cavitating', 'cavitational']),
    ('homogeneous-nucleation', 'homogeneous nucleation', '均相成核', ['均质成核']),
    ('heterogeneous-nucleation', 'heterogeneous nucleation', '异相成核', ['非均相成核']),
    ('nucleation-barrier', 'nucleation barrier', '成核势垒', ['nucleation barriers']),
    ('nucleation', 'nucleation', '成核', ['nucleate', 'nucleated', 'nucleating']),
    ('gas-nuclei', 'gas nuclei', '气核', ['gas nucleus', '气体核']),
    ('critical-radius', 'critical radius', '临界半径', []),
    ('energy-barrier', 'energy barrier', '能垒', ['energy barriers', '能量势垒']),
    ('blake-threshold', 'Blake threshold', 'Blake阈值', ['Blake 阈值', '布莱克阈值']),
    ('rayleigh-plesset', 'Rayleigh–Plesset', '瑞利–普莱塞特', ['Rayleigh-Plesset', 'Rayleigh Plesset', '瑞利-普莱塞特', '瑞利—普莱塞特', '瑞利普莱塞特']),
    ('keller-miksis', 'Keller–Miksis', '凯勒–米克西斯', ['Keller-Miksis', 'Keller Miksis', '凯勒-米克西斯', '凯勒—米克西斯']),
    ('gilmore', 'Gilmore equation', 'Gilmore方程', ['Gilmore 方程', '吉尔摩方程']),
    ('vapor-pressure', 'vapor pressure', '蒸气压', ['vapour pressure', 'vapor pressures', 'vapour pressures', 'vapor-pressure', '蒸汽压', '蒸气压力']),
    ('noncondensable-gas', 'noncondensable gas', '不凝性气体', ['noncondensable gases', 'non-condensable gas', 'non-condensable gases', 'permanent gas', 'permanent-gas', '不可凝气体', '非凝性气体', '非凝结气体', '不凝气体', '不凝气']),
    ('surface-tension', 'surface tension', '表面张力', ['surface-tension', 'interfacial tension', 'interfacial tensions', '界面张力']),
    ('capillary-pressure', 'capillary pressure', '毛细压力', ['毛细压']),
    ('laplace-pressure', 'Laplace pressure', '拉普拉斯压力', ['Laplace 压力', 'Laplace压力']),
    ('inertia', 'inertia', '惯性', ['inertial', 'inertially', 'liquid inertia', '液体惯性', '液体的惯性']),
    ('kinetic-energy', 'kinetic energy', '动能', []),
    ('gas-cushioning', 'gas cushioning', '气体缓冲', []),
    ('collapse-time', 'collapse time', '塌缩时间', ['collapse-time']),
    ('nonspherical-collapse', 'non-spherical collapse', '非球形塌缩', ['nonspherical collapse']),
    ('spherical-collapse', 'spherical collapse', '球形塌缩', []),
    ('rebound', 'rebound', '回弹', ['rebounds']),
    ('compressibility', 'compressibility', '可压缩性', ['compressible', '可压缩']),
    ('incompressibility', 'incompressibility', '不可压缩性', ['incompressible', '不可压缩']),
    ('acoustic-radiation', 'acoustic radiation', '声辐射', []),
    ('acoustic-impedance', 'acoustic impedance', '声阻抗', []),
    ('acoustic-crossing-time', 'acoustic crossing time', '声传播时间', ['acoustic transit time', '声学跨越时间', '声穿越时间']),
    ('mach-number', 'Mach number', '马赫数', []),
    ('pressure-impulse', 'pressure impulse', '压力冲量', []),
    ('kelvin-impulse', 'Kelvin impulse', 'Kelvin冲量', ['Kelvin 冲量', '开尔文冲量']),
    ('water-hammer', 'water hammer', '水锤', ['water-hammer']),
    ('shock-wave', 'shock wave', '激波', ['shock waves']),
    ('peak-pressure', 'peak pressure', '峰值压力', ['pressure peak', 'pressure peaks', 'peak local pressure', 'peak collapse pressure', 'peak film pressure', '压力峰值', '高压峰值']),
    ('stand-off', 'stand-off ratio', '离壁比', ['stand-off', 'standoff', 'stand off', 'stand-off parameter', 'standoff ratio', '离壁参数', '离壁距离比', '距壁比']),
    ('rigid-wall', 'rigid wall', '刚壁', ['rigid walls', '刚性壁面']),
    ('rigid-boundary', 'rigid boundary', '刚性边界', ['rigid boundaries', 'rigid surface', 'rigid surfaces', '刚性表面']),
    ('compliant-boundary', 'compliant boundary', '柔性边界', ['compliant boundaries', '柔顺边界']),
    ('elastic-boundary', 'elastic boundary', '弹性边界', ['elastic boundaries']),
    ('free-surface', 'free surface', '自由表面', ['free surfaces', 'free-surface', '自由面', '自由液面']),
    ('hydrogel', 'hydrogel', '水凝胶', ['hydrogels']),
    ('viscoelasticity', 'viscoelasticity', '黏弹性', ['viscoelastic', '粘弹性']),
    ('viscosity', 'viscosity', '黏度', ['viscous', '粘度', '黏性', '粘性']),
    ('damping', 'damping', '阻尼', []),
    ('heat-transfer', 'heat transfer', '传热', ['heat-transfer', '热传递']),
    ('mass-transfer', 'mass transfer', '传质', ['mass-transfer', '质量传递', '质传递', '质量输运']),
    ('thermal-diffusion', 'thermal diffusion', '热扩散', []),
    ('thermal-diffusivity', 'thermal diffusivity', '热扩散率', []),
    ('phase-change', 'phase change', '相变', ['phase-change', 'phase-changing', 'phase transition', 'phase transitions']),
    ('latent-heat', 'latent heat', '潜热', []),
    ('superheat', 'superheat', '过热', ['superheating', 'superheated']),
    ('vaporization', 'vaporization', '汽化', ['vaporisation', 'vaporize', 'vaporizes', 'vaporized', 'vaporizing', 'vaporise', 'vaporises', 'vaporised', '气化']),
    ('condensation', 'condensation', '凝结', ['condense', 'condenses', 'condensed', 'condensing', 'recondensation', '冷凝']),
    ('polytropic-exponent', 'polytropic exponent', '多方指数', []),
    ('equation-of-state', 'equation of state', '状态方程', ['equations of state', 'EOS']),
    ('resonance', 'resonance', '共振', ['resonant']),
    ('weber-number', 'Weber number', '韦伯数', ['Weber数', 'Weber 数']),
    ('ohnesorge-number', 'Ohnesorge number', '奥内佐格数', ['Ohnesorge数', 'Ohnesorge 数', '欧内佐格数']),
    ('reynolds-number', 'Reynolds number', '雷诺数', ['Reynolds数', 'Reynolds 数']),
    ('pfc', 'perfluorocarbon', '全氟碳', ['perfluorocarbons', 'PFC', '全氟碳化合物']),
    ('nanodroplet', 'nanodroplet', '纳米液滴', ['nanodroplets', 'nano-droplet', 'nano-droplets']),
    ('microbubble', 'microbubble', '微气泡', ['microbubbles']),
    ('optical-breakdown', 'optical breakdown', '光学击穿', []),
    ('optoacoustic', 'optoacoustic', '光声', ['optoacoustics', 'photoacoustic', 'photoacoustics']),
    ('fluence', 'fluence', '激光能量面密度', ['laser fluence', 'optical fluence', '能量面密度', '能量密度', '辐照量']),
    ('absorption-coefficient', 'absorption coefficient', '吸收系数', []),
    ('bubble-cloud', 'bubble cloud', '泡云', ['bubble clouds', '气泡云']),
    ('bubble-interaction', 'bubble interaction', '气泡相互作用', ['bubble interactions', 'bubble-bubble interaction', 'bubble-bubble interactions', '泡间相互作用']),
    ('coalescence', 'coalescence', '聚并', ['coalesce', 'coalesces', 'coalescing', '气泡合并', '并合', '汇合']),
    ('interfacial-adhesion', 'interfacial adhesion', '界面黏附', ['界面粘附']),
    ('interfacial-fracture', 'interfacial fracture', '界面断裂', []),
    ('poisson-ratio', 'Poisson ratio', '泊松比', ["Poisson's ratio", 'Poisson’s ratio']),
    ('young-modulus', "Young's modulus", '杨氏模量', ['Young’s modulus', 'Young modulus']),
    ('bulk-modulus', 'bulk modulus', '体积模量', []),
    ('velocity-potential', 'velocity potential', '速度势', ['velocity potentials']),
    ('potential-flow', 'potential flow', '势流', ['potential-flow']),
    ('boundary-integral', 'boundary integral', '边界积分', ['boundary integrals', 'boundary-integral']),
    ('capillary-instability', 'capillary instability', '毛细失稳', ['capillary instabilities']),
    ('growth-rate', 'growth rate', '增长率', ['growth rates']),
    ('geometric-focusing', 'geometric focusing', '几何聚焦', []),
    ('extensional-viscosity', 'extensional viscosity', '拉伸黏性', ['extensional-viscous', 'extensional viscous', 'extensional-viscosity']),
    ('kinematic-condition', 'kinematic condition', '运动学条件', ['kinematic conditions']),
    ('control-volume', 'control volume', '控制体', ['control volumes', 'control-volume']),
    ('capillary-time', 'capillary time', '毛细时间', ['capillary-time', 'capillary times']),
    ('stiffened-gas', 'stiffened gas', '刚化气体', ['stiffened-gas', 'stiff gas']),
    ('fracture-energy', 'fracture energy', '断裂能', ['fracture energies']),
    ('energy-release-rate', 'energy-release rate', '能量释放率', ['energy release rate', 'energy-release rates']),
    ('cohesive-traction', 'cohesive traction', '内聚牵引', ['cohesive tractions', '内聚力']),
    ('cohesive-strength', 'cohesive strength', '内聚强度', ['peak cohesive strength']),
    ('traction-separation', 'traction–separation', '牵引–分离', ['traction-separation', '牵引—分离', '牵引-分离']),
    ('fracture-toughness', 'fracture toughness', '断裂韧度', ['断裂韧性']),
    ('delamination', 'delamination', '脱层', ['delaminated', '分层']),
    ('blister', 'blister', '鼓泡', ['blisters', 'blistering']),
    ('heat-capacity', 'heat capacity', '热容', ['specific heat capacity', 'heat capacities', '比热容']),
    ('stefan-balance', 'Stefan balance', 'Stefan 热平衡', ['Stefan condition', 'Stefan 条件', 'Stefan平衡', 'Stefan 平衡', '斯特藩条件']),
    ('optical-uniformity', 'optical uniformity', '光学均匀性', []),
    ('activation-probability', 'activation probability', '激活概率', ['activation probabilities']),
    ('neo-hookean', 'neo-Hookean', '新胡克', ['neo-Hookean solid', 'neo–Hookean', 'Neo–Hookean', 'Neo-Hookean']),
    ('poroelastic', 'poroelastic', '孔弹性', ['poroelasticity', '孔弹']),
    ('relaxation-time', 'relaxation time', '松弛时间', ['stress-relaxation time', '应力松弛时间']),
    ('deborah-number', 'Deborah number', 'Deborah 数', ['Deborah数', '德博拉数']),
    ('energy-budget', 'energy budget', '能量预算', ['energy budgets', 'energy ledger', '能量账目']),
]

# Short forms are used only when the peer paragraph explicitly names the term.
# Shared-head constructions (e.g. "Weber and Ohnesorge numbers") need this pass.
CONTEXT_ALIASES = {
    'acoustic-crossing-time': {'en': ['acoustic travel time', 'crossing times', 'acoustic travel', 'sound-crossing time', 'sound crossing time']},
    'acoustic-impedance': {'en': ['longitudinal impedance']},
    'acoustic-radiation': {'en': ['radiation', 'radiative']},
    'bubble-cloud': {'en': ['cloud', 'clouds', 'cloud radius', 'uniform-cloud']},
    'cavitation-inception': {'en': ['inception']},
    'energy-barrier': {'en': ['barrier', 'barriers']},
    'gas-nuclei': {'en': ['nucleus', 'nuclei']},
    'capillary-pressure': {'en': ['capillary']},
    'noncondensable-gas': {'en': ['noncondensable', 'non-condensable']},
    'velocity-potential': {'en': ['potential', 'potentials']},
    'confinement': {'zh': ['约束']},
    'mach-number': {'en': ['Mach'], 'zh': ['Mach数', 'Mach 数']},
    'weber-number': {'en': ['Weber', 'Weber numbers']},
    'ohnesorge-number': {'en': ['Ohnesorge', 'Ohnesorge numbers']},
    'shock-wave': {'en': ['shock', 'shocks'], 'zh': ['冲击波']},
    'latent-heat': {'en': ['latent']},
    'damping': {'en': ['damped', 'undamped', 'underdamped', 'overdamped']},
    'rebound': {'en': ['recoil']},
    'hydrogel': {'en': ['gel'], 'zh': ['凝胶']},
    'homogeneous-nucleation': {'en': ['homogeneous']},
    'heterogeneous-nucleation': {'en': ['heterogeneous']},
    'nanodroplet': {'en': ['nanoscale, coated droplet', 'nanoscale droplet']},
    'jet-speed': {'en': ['speed of an observed ejected jet', 'local jet velocity']},
    'jet': {'zh': ['喷射']},
    'stand-off': {'zh': ['离壁']},
    'optoacoustic': {'en': ['optical/acoustic']},
    'kinetic-energy': {'en': ['kinetic']},
    'phase-change': {'en': ['phase species', 'phase timescales', 'phase data', 'phase energy',
                          'phase-energy', 'phase costs', 'phase mass exchange', 'laser/phase']},
    'pressure-impulse': {'en': ['impulse'], 'zh': ['单位面积冲量']},
    'vapor-pressure': {'en': ['saturation pressure']},
    'thermal-diffusion': {'en': ['diffusion-controlled thermal', 'diffusion-limited thermal']},
    'heat-transfer': {'en': ['heat exchange', 'thermal exchange']},
}
CONTEXT_REGEX = {
    'heat-transfer': {'en': [r'\bheat(?=\s*(?:and|/)\s*mass\s+(?:transfer|rates?))'],
                      'zh': [r'热(?=质传递)']},
    'mass-transfer': {'en': [r'\bmass(?=\s+rates?)'], 'zh': [r'(?<=热)质(?=传递)']},
}
BLOCKS = 'p,h1,h2,h3,h4,h5,h6,li,td,th,summary,figcaption'
TERM_MARK = re.compile(r'<span class="keyword technical-term" data-term="([a-z-]+)" title="[^"]*">([\s\S]*?)</span>')

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}
BLOCKED_TAGS = {'head', 'script', 'style', 'pre', 'code', 'math', 'svg',
                'textarea', 'template', 'button', 'nav', 'footer'}
BLOCKED_CLASSES = {'equation', 'math-placeholder', 'variable-map', 'eyebrow'}


def _literal_pattern(value):
    if value == '气化':
        # "蒸气化学" means vapor chemistry, not vaporization.
        return r'(?<!蒸)气化(?!学)'
    pattern = re.escape(value).replace(r'\ ', r'(?:[ \t\r\n]+|[-\u2010-\u2015])')
    pattern = pattern.replace(r'\-', r'[-\u2010-\u2015]')
    if re.match(r'[A-Za-z]', value):
        pattern = r'(?<![A-Za-z0-9_])' + pattern
    if re.search(r'[A-Za-z0-9]$', value):
        pattern += r'(?![A-Za-z0-9_])'
    return pattern


def _compile_terms():
    aliases = {}
    for key, en, zh, variants in TERMS:
        for value in [en, zh, *variants]:
            assert value.casefold() not in aliases or aliases[value.casefold()][0] == key
            aliases[value.casefold()] = (key, en, zh, value)
    groups, lookup = [], {}
    for i, entry in enumerate(sorted(aliases.values(), key=lambda x: -len(x[3]))):
        key, en, zh, value = entry
        pattern = _literal_pattern(value)
        group = f'a{i}'
        groups.append(f'(?P<{group}>{pattern})')
        lookup[group] = (key, en, zh)
    return re.compile('|'.join(groups), re.I), lookup


PATTERN, LOOKUP = _compile_terms()


class _MarkupPass(HTMLParser):
    """Collect exact source offsets; never serialize math or other existing tags."""
    def __init__(self, source, unwrap=False, pattern=None, lookup=None):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.unwrap = unwrap
        self.pattern = pattern or PATTERN
        self.lookup = lookup or LOOKUP
        self.lines = [0] + [m.end() for m in re.finditer('\n', source)]
        self.stack = []
        self.edits = []

    def source_position(self):
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set((attrs.get('class') or '').split())
        blocked = bool(self.stack and self.stack[-1][1]) or tag in BLOCKED_TAGS
        blocked = blocked or bool(classes & BLOCKED_CLASSES) or any(c.startswith('katex') for c in classes)
        blocked = blocked or (not self.unwrap and 'technical-term' in classes)
        remove = self.unwrap and tag == 'span' and not blocked and bool(classes & {'keyword', 'technical-term'})
        if remove:
            start = self.source_position()
            self.edits.append((start, start + len(self.get_starttag_text()), ''))
        if tag not in VOID:
            self.stack.append((tag, blocked, remove))

    def handle_startendtag(self, tag, attrs):
        depth = len(self.stack)
        self.handle_starttag(tag, attrs)
        del self.stack[depth:]

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                if self.stack[i][2]:
                    start = self.source_position()
                    self.edits.append((start, self.source.index('>', start) + 1, ''))
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.unwrap or not self.stack or self.stack[-1][1]:
            return
        if not any(frame[0] == 'body' for frame in self.stack):
            return
        start = self.source_position()
        for match in self.pattern.finditer(data):
            key, en, zh = self.lookup[match.lastgroup]
            title = escape(en + ' / ' + zh, quote=True)
            mark = f'<span class="keyword technical-term" data-term="{key}" title="{title}">{match[0]}</span>'
            self.edits.append((start + match.start(), start + match.end(), mark))

    def result(self):
        self.feed(self.source)
        self.close()
        pieces, cursor = [], 0
        for start, end, replacement in sorted(self.edits):
            assert start >= cursor
            pieces.extend([self.source[cursor:start], replacement])
            cursor = end
        pieces.append(self.source[cursor:])
        return ''.join(pieces)


def highlight_html(source):
    return _highlight_with_audit(source)[0]


def _highlight_with_audit(source):
    # Unwrap the old jet-only marks first, including "micro<span>jets</span>".
    # Matching the resulting whole phrase avoids split or nested highlights.
    clean = _MarkupPass(source, unwrap=True).result()
    marked = _MarkupPass(clean).result()
    return align_term_pairs(marked)


def _is_chinese(node):
    if 'zh' in node.get('class', []) or node.get('lang') == 'zh-CN':
        return True
    # A bilingual table cell is not a Chinese peer for the source-label cell
    # immediately to its left. Pair its own English and .zh fragments instead.
    if node.select_one('.zh'):
        return False
    if node.name in {'td', 'th'} and ' / ' in node.get_text():
        return False
    return len(re.findall(r'[\u4e00-\u9fff]', node.get_text())) >= 6


def paired_nodes(soup):
    """Pair translations with prose/title text, never author/DOI metadata."""
    pairs, used = [], set()
    for en in soup.select(BLOCKS):
        if _is_chinese(en) or en.select_one(BLOCKS) or en.select_one('.zh'):
            continue
        peer = en.find_next_sibling()
        if en.name == 'h3' and en.get('id', '').startswith('src-s'):
            for candidate in en.find_next_siblings():
                if candidate.name == 'h3':
                    break
                if candidate.name == 'p' and candidate.get_text().lstrip().startswith('中文题名'):
                    peer = candidate
                    break
        if not peer or not _is_chinese(peer):
            continue
        if peer.name != en.name and not (en.name == 'h3' and en.get('id', '').startswith('src-s')):
            continue
        if peer.get_text().lstrip().startswith('中文题名') and en.name != 'h3':
            continue
        if id(peer) in used:
            continue
        pairs.append((en, peer)); used.add(id(peer))
    # Tables and navigation-style study lists can pair text inside one cell.
    for zh in soup.select('td > .zh, th > .zh'):
        parent = zh.parent
        if not parent.select_one('p,h1,h2,h3,h4,li,td,th'):
            pairs.append((parent, zh))
    for cell in soup.select('td,th'):
        if cell.select_one(BLOCKS) or cell.select_one('.zh'):
            continue
        text = cell.get_text()
        if ' / ' in text:
            en, zh = text.rsplit(' / ', 1)
            if re.search(r'[A-Za-z]', en) and re.search(r'[\u4e00-\u9fff]', zh):
                pairs.append((cell, cell))
    return pairs


def _node_range(node, source, lines):
    assert node.sourceline is not None and node.sourcepos is not None
    start = lines[node.sourceline - 1] + node.sourcepos
    pattern = re.compile(r'</?' + node.name + r'''\b(?:[^>"']|"[^"]*"|'[^']*')*>''', re.I)
    depth = 0
    for tag in pattern.finditer(source, start):
        if tag[0].startswith('</'):
            depth -= 1
        elif not tag[0].endswith('/>'):
            depth += 1
        if depth == 0:
            return start, tag.end()
    raise AssertionError(f'Missing closing tag: {node.name}')


class _TranslationDivider(_MarkupPass):
    """Find explicit prose separators outside formulas, code and attributes."""
    def __init__(self, source):
        super().__init__(source)
        self.dividers = []

    def handle_data(self, data):
        if not self.stack or self.stack[-1][1]:
            return
        start = self.source_position()
        self.dividers.extend((start + m.start(), start + m.end())
                             for m in re.finditer(r' / ', data))


def _context_mark(fragment, keys, language):
    entries = []
    labels = {k: (en, zh) for k, en, zh, _ in TERMS}
    for key in sorted(keys):
        for alias in CONTEXT_ALIASES.get(key, {}).get(language, []):
            entries.append((key, _literal_pattern(alias)))
        for pattern in CONTEXT_REGEX.get(key, {}).get(language, []):
            entries.append((key, pattern))
    # A previous mark can split "heat and <span>mass transfer</span>".
    visible = re.sub(r'<[^>]*>', '', fragment)
    if language == 'en' and 'heat-transfer' in keys and re.search(r'\bheat\s*(?:and|/)\s*mass\b', visible, re.I):
        entries.append(('heat-transfer', r'\bheat\b'))
    if not entries:
        return fragment
    groups, lookup = [], {}
    for i, (key, pattern) in enumerate(sorted(entries, key=lambda x: -len(x[1]))):
        group = f'c{i}'
        groups.append(f'(?P<{group}>{pattern})'); lookup[group] = (key, *labels[key])
    wrapped = '<body>' + fragment + '</body>'
    marked = _MarkupPass(wrapped, pattern=re.compile('|'.join(groups), re.I), lookup=lookup).result()
    return marked[len('<body>'):-len('</body>')]


def align_term_pairs(source):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(source, 'html.parser')
    lines = [0] + [m.end() for m in re.finditer('\n', source)]
    edits, omitted, repaired = [], [], []
    pairs = paired_nodes(soup)
    for en, zh in pairs:
        en_range, zh_range = _node_range(en, source, lines), _node_range(zh, source, lines)
        if en is zh:
            start, end = en_range
            fragment = source[start:end]
            divider = _TranslationDivider('<body>' + fragment + '</body>')
            divider.feed(divider.source); divider.close()
            assert divider.dividers, 'Missing explicit bilingual separator'
            left, right = divider.dividers[-1]
            left += start - len('<body>'); right += start - len('<body>')
            opening = source.index('>', start) + 1
            closing = source.rfind('</', start, end)
            en_range, zh_range = (opening, left), (right, closing)
        elif zh.parent is en:
            en_range = (source.index('>', en_range[0]) + 1, zh_range[0])
        a, b = [source[start:end] for start, end in [en_range, zh_range]]
        keys = lambda text: {m[1] for m in TERM_MARK.finditer(text)}
        before_a, before_b = keys(a), keys(b)
        a = _context_mark(a, before_b - before_a, 'en')
        b = _context_mark(b, before_a - before_b, 'zh')
        after_a, after_b = keys(a), keys(b)
        common = after_a & after_b
        additions = common - (before_a & before_b)
        if additions:
            repaired.append({'line': en.sourceline, 'terms': sorted(additions)})
        if after_a != after_b:
            omitted.append({'line': en.sourceline, 'English': BeautifulSoup(a, 'html.parser').get_text(' ', strip=True),
                            'Chinese': BeautifulSoup(b, 'html.parser').get_text(' ', strip=True),
                            'English_only': sorted(after_a - after_b), 'Chinese_only': sorted(after_b - after_a),
                            'action': 'Leave these nonmatched occurrences plain; preserve both source paragraphs and do not invent an equivalent term.'})
        a = TERM_MARK.sub(lambda m: m[0] if m[1] in common else m[2], a)
        b = TERM_MARK.sub(lambda m: m[0] if m[1] in common else m[2], b)
        assert keys(a) == keys(b)
        for bounds, replacement in [(en_range, a), (zh_range, b)]:
            if replacement != source[bounds[0]:bounds[1]]:
                edits.append((*bounds, replacement))
    chunks, cursor = [], 0
    for start, end, replacement in sorted(edits):
        assert start >= cursor, f'Overlapping prose-pair edits at {start}:{end}, previous end {cursor}: {replacement[:240]}'
        chunks.extend([source[cursor:start], replacement]); cursor = end
    chunks.append(source[cursor:])
    return ''.join(chunks), {'paired_blocks_checked': len(pairs), 'contextual_matches': repaired,
                             'nonliteral_occurrences_left_plain': omitted,
                             'one_sided_colored_terms_remaining': 0}


def course_pages(root):
    root = Path(root)
    settings = root / 'COURSE_SETTINGS.json'
    if settings.exists():
        course = json.loads(settings.read_text(encoding='utf-8'))
        return sorted([root/'index.html', *(root/c['file'] for c in course['chapters']+course.get('appendices',[])), *(root/c['file'] for c in course.get('legacy_routes',[])), *root.glob('reference/*.html')])
    return sorted([*root.glob('*.html'), *root.glob('course/**/*.html'),
                   *root.glob('chapters/*.html'), *root.glob('lessons/*.html'),
                   *root.glob('reference/*.html')])


def paragraph_groups(soup):
    """Use leaf prose blocks; combine each English block with its Chinese peer."""
    blocks = 'p,h1,h2,h3,h4,h5,h6,li,td,th,summary,figcaption'
    groups = []
    for node in soup.select(blocks):
        if node.select_one(blocks):
            continue
        keys = {n['data-term'] for n in node.select('.technical-term')}
        peer = node.find_next_sibling()
        if peer and peer.name == node.name and ('zh' in peer.get('class', []) or
                peer.get('lang') == 'zh-CN' or re.search(r'[\u4e00-\u9fff]', peer.get_text())):
            keys.update(n['data-term'] for n in peer.select('.technical-term'))
        if keys:
            groups.append(keys)
    return groups


def color_terms(groups):
    # Graph coloring makes the same term stable throughout the whole course,
    # while forbidding shared colors between distinct terms in any prose pair.
    graph = {term[0]: set() for term in TERMS}
    for group in groups:
        for key in group:
            graph[key].update(group - {key})
    colors = {'jet': 0}
    while len(colors) < len(graph):
        key = max((k for k in graph if k not in colors),
                  key=lambda k: (len({colors[n] for n in graph[k] if n in colors}),
                                 len(graph[k]), k))
        used = {colors[n] for n in graph[key] if n in colors}
        colors[key] = next(i for i in range(len(graph)) if i not in used)
    assert all(len({colors[k] for k in group}) == len(group) for group in groups)
    return colors


def _rgb(hue, saturation, lightness):
    return tuple(round(v * 255) for v in colorsys.hls_to_rgb(hue / 360, lightness, saturation))


def _hex(rgb):
    return '#' + ''.join(f'{v:02x}' for v in rgb)


def _contrast(ink, background):
    def luminance(rgb):
        linear = [v / 255 / 12.92 if v / 255 <= .04045 else ((v / 255 + .055) / 1.055) ** 2.4 for v in rgb]
        return sum(w * v for w, v in zip([.2126, .7152, .0722], linear))
    a, b = sorted([luminance(ink), luminance(background)], reverse=True)
    return (a + .05) / (b + .05)


def write_color_styles(root, colors):
    count = max(colors.values()) + 1
    hues = [35, 195, 125, 300, 255, 5, 215, 60, 165, 280, 90, 335,
            180, 20, 235, 145, 315, 75, 270, 110, 350, 205, 45, 155]
    assert count <= len(hues), f'Need {count} perceptually distinct term colors'
    palette = []
    for hue in hues[:count]:
        dark = _rgb(hue, .86, .76)
        light = _rgb(hue, .70, .25)
        wash = _rgb(hue, .70, .94)
        dark_background = tuple(round(.14 * a + .86 * b) for a, b in zip(dark, (16, 27, 38)))
        contrast = {'dark': round(_contrast(dark, dark_background), 2), 'light': round(_contrast(light, wash), 2)}
        assert min(contrast.values()) >= 4.5, contrast
        palette.append({'dark': _hex(dark), 'light': _hex(light), 'wash': _hex(wash), 'rgb': dark,
                        'contrast_ratio': contrast})
    css = ['/* Shared English/Chinese term colors; generated from prose co-occurrence. */',
           '.technical-term[data-term] { color: var(--term-ink); background: var(--term-wash);',
           '  -webkit-box-decoration-break: clone; box-decoration-break: clone; }']
    for key in sorted(colors):
        p = palette[colors[key]]
        rgb = ', '.join(str(v) for v in p['rgb'])
        css.append(f'.technical-term[data-term="{key}"] {{ --term-ink: {p["dark"]}; --term-wash: rgba({rgb}, .14); }}')
        css.append(f'html[data-theme="light"] .technical-term[data-term="{key}"] {{ --term-ink: {p["light"]}; --term-wash: {p["wash"]}; }}')
    css.append('@media print {')
    for key in sorted(colors):
        p = palette[colors[key]]
        css.append(f'  html .technical-term[data-term="{key}"] {{ --term-ink: {p["light"]}; --term-wash: {p["wash"]}; }}')
    css.append('}')
    (root / 'assets/bilingual-terms.css').write_bytes(('\n'.join(css) + '\n').encode('utf-8'))
    return palette


def _with_styles(source, path, root):
    if re.search(r'<link\b[^>]*\bbilingual-terms\.css', source, re.I):
        return source
    href = os.path.relpath(root / 'assets/bilingual-terms.css', path.parent).replace('\\', '/')
    return re.sub(r'</head\s*>', f'<link href="{href}" rel="stylesheet"/></head>', source, count=1, flags=re.I)


def apply_to_course(root, report_path=None):
    from bs4 import BeautifulSoup
    root = Path(root)
    records, totals, groups, prepared, pair_audits = [], Counter(), [], [], []
    for path in course_pages(root):
        source = path.read_bytes().decode('utf-8')
        print(f'Auditing {path.relative_to(root).as_posix()}', flush=True)
        try:
            marked, pair_audit = _highlight_with_audit(source)
        except AssertionError as error:
            raise AssertionError(f'{path.relative_to(root)}: {error}') from error
        result = _with_styles(marked, path, root)
        pair_audits.append({'file': path.relative_to(root).as_posix(), **pair_audit})
        before, after = [BeautifulSoup(s, 'html.parser') for s in [source, result]]
        assert before.get_text() == after.get_text(), path
        protected = '.equation,.katex,math,svg,pre,code,script,style'
        assert [str(n) for n in before.select(protected)] == [str(n) for n in after.select(protected)], path
        def refs(soup):
            return [(n.name, n.get('href'), n.get('src'), n.get('id')) for n in soup.find_all(['a', 'img', 'link', 'script']) if not n.get('href', '').endswith('bilingual-terms.css')]
        assert refs(before) == refs(after), path
        assert highlight_html(result) == result, f'Non-idempotent highlight: {path}'
        marks = after.select('.technical-term')
        assert not after.select('.technical-term .technical-term'), path
        counts = Counter(n['data-term'] for n in marks)
        groups.extend(paragraph_groups(after))
        totals.update(counts)
        records.append({'file': path.relative_to(root).as_posix(), 'highlights': len(marks),
                        'terms': dict(sorted(counts.items())), 'text_and_math_unchanged': True,
                        'links_and_anchors_unchanged': True, 'idempotent': True,
                        'sha256': hashlib.sha256(result.encode('utf-8')).hexdigest()})
        prepared.append((path, source, result))
    colors = color_terms(groups)
    palette = write_color_styles(root, colors)
    for path, source, result in prepared:
        if result != source:
            path.write_bytes(result.encode('utf-8'))
    report = {'scope': 'Every authored HTML lesson, chapter, appendix, reference and course entry page.',
              'style': 'Different concepts have different colors within each English/Chinese prose pair. Each term keeps the same color throughout the course, with day/night variants.',
              'dictionary_terms': len(TERMS), 'pages': len(records), 'highlights': sum(totals.values()),
              'color_count': len(palette), 'paired_prose_groups_checked': len(groups),
              'no_distinct_terms_share_a_color_in_any_paired_prose_group': True,
              'palette': palette, 'term_color_indices': dict(sorted(colors.items())),
              'strict_pair_audit': {'paired_blocks_checked': sum(x['paired_blocks_checked'] for x in pair_audits),
                                    'one_sided_colored_terms_remaining': 0, 'pages': pair_audits},
              'highlighter_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'color_stylesheet_sha256': hashlib.sha256((root/'assets/bilingual-terms.css').read_bytes()).hexdigest(),
              'term_totals': dict(sorted(totals.items())), 'checks': records,
              'all_text_math_links_and_anchors_preserved': True}
    if report_path:
        Path(report_path).write_bytes((json.dumps(report, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    return report


def ensure_course_highlights(root, report_path):
    root, report_path = Path(root), Path(report_path)
    if report_path.is_file() and (root/'assets/bilingual-terms.css').is_file():
        saved = json.loads(report_path.read_text(encoding='utf-8'))
        pages = {p.relative_to(root).as_posix(): p for p in course_pages(root)}
        rows = {r['file']: r for r in saved.get('checks', [])}
        current_code = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        current_css = hashlib.sha256((root/'assets/bilingual-terms.css').read_bytes()).hexdigest()
        if (saved.get('highlighter_sha256') == current_code and saved.get('color_stylesheet_sha256') == current_css
                and pages.keys() == rows.keys()
                and all(hashlib.sha256(p.read_bytes()).hexdigest() == rows[name]['sha256'] for name, p in pages.items())):
            return saved
    return apply_to_course(root, report_path)


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    result = apply_to_course(root, root / 'verification/bilingual-terms.json')
    print(json.dumps({k: result[k] for k in ['dictionary_terms', 'pages', 'highlights', 'color_count', 'paired_prose_groups_checked', 'all_text_math_links_and_anchors_preserved']}))
    print(json.dumps({'strict_pairs_checked': result['strict_pair_audit']['paired_blocks_checked'], 'one_sided_colored_terms_remaining': 0}))
