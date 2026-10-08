"""Shared authoring primitives; chapter workers own only their assigned content."""
from html import escape
import json
import re

EQUATIONS = []

def safe_inline_math(text):
    """Preserve mathematical inequalities before parsing intentional prose HTML."""
    return re.sub(r'(?<!\\)\$([^$\n]+?)(?<!\\)\$',
                  lambda m:'$'+escape(m.group(1),quote=False)+'$',str(text))

def P(en, zh, cls=''):
    return f'<div class="lang-pair {escape(cls)}"><p lang="en">{safe_inline_math(en)}</p><p lang="zh-CN" class="zh">{safe_inline_math(zh)}</p></div>'

def H(en, zh, anchor, level=2):
    return f'<div class="heading-pair"><h{level} id="{escape(anchor)}" lang="en">{safe_inline_math(en)}</h{level}><h{level} lang="zh-CN" class="zh">{safe_inline_math(zh)}</h{level}></div>'

def E(identifier, tex, symbols_en, symbols_zh, kind, diagram, caption_en, caption_zh):
    """Every display has bilingual local definitions and an immediate variable figure.

    diagram: {type: sphere|energy|impulse|laser|phase|nucleation|array|jet|impact|film|cohesive|gel|timescale,
              labels: [plain unicode variable labels], notes: [physical annotations]}.
    Define ALL displayed variables/operators/indices and units in symbols_en/zh.
    tex must have no tag; identifier is printed separately. Sources belong in nearby P().
    """
    item = dict(id=identifier, tex=tex, symbols_en=symbols_en, symbols_zh=symbols_zh,
                kind=kind, diagram=diagram, caption_en=caption_en, caption_zh=caption_zh)
    EQUATIONS.append(item)
    label = escape(identifier.lower())
    return (f'<section class="equation-unit" id="{escape(identifier)}" data-kind="{escape(kind)}">'
            + P(f'<strong>Symbols before Eq. ({identifier}).</strong> '+symbols_en,
                f'<strong>式（{identifier}）前的符号定义。</strong> '+symbols_zh, 'symbols')
            + f'<div class="equation-heading">({escape(identifier)}) · {escape(kind)}</div>'
            + f'<div class="math-display" data-tex="{escape(tex, quote=True)}"></div>'
            + f'<figure class="formula-figure"><img src="../assets/figures/{label}.svg" alt="{escape(caption_en, quote=True)}" loading="lazy">'
            + '<figcaption>'+P(caption_en, caption_zh)+'</figcaption></figure></section>')

def T(headers, rows):
    return '<div class="table-wrap"><table><thead><tr>'+''.join('<th>'+P(*h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+P(*c)+'</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table></div>'

def cite(ref, text=None):
    return f'<a class="citation" href="../reference/sources.html#{escape(ref)}">[{escape(text or ref.upper())}]</a>'

def defense(identifier, question_en, question_zh, answer_html, criteria):
    """Exactly three per chapter; reference answer starts with relevant E() original formulas.
    criteria: three-four tuples (EN,ZH), semantic mastery rubric. No automatic keyword mastery.
    """
    return (f'<article class="defense" id="{escape(identifier)}" data-defense="{escape(identifier)}">'
            +H(question_en,question_zh,identifier+'-question',3)
            +P('Explain this in your own words. Use assumptions, a physical argument, and a limitation; equation memorization is not required.',
               '请用自己的话解释，说明假设、物理推理及适用限制；不要求背诵公式。')
            +f'<label for="response-{escape(identifier)}">Your explanation / 您的解释</label>'
            +f'<textarea id="response-{escape(identifier)}" data-response="{escape(identifier)}" rows="5"></textarea>'
            +'<details class="answer"><summary>Reference answer and mastery criteria / 参考答案与掌握标准</summary>'
            +answer_html+H('What a mastered answer demonstrates','掌握后的回答应体现',identifier+'-rubric',4)
            +'<ul>'+''.join('<li>'+P(*c)+'</li>' for c in criteria)+'</ul></details></article>')

def note(en,zh,kind='callout'):
    return P(en,zh,kind)
