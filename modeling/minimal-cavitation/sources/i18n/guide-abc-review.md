# Chinese translation review — introduction and sections A–C

Scope: the complete introduction and Steps 01–31 from `STEP_BY_STEP.md`, ending immediately before section D. The translated fragment is `guide-abc.zh.md`. All prose, table descriptions, headings, link labels, image alt text and captions were translated. English COMSOL interface names and exact settings remain available for locating the Desktop controls; menu paths and executable entries remain unchanged.

Shared terminology follows `TERMINOLOGY.csv`, including 空化, 水凝胶, 约束, 射流, 出口, 可用功, 激活后, 超压, 动压, 排出动能, 排出冲量, 液体存量, 弯月面, 新胡克, 半球合力 and 能量残差. “Arrest pressure” is rendered as “制动压力”; it retains the source's mean impulse-based bound, not an impact peak. “Screen” is rendered as “筛选阈值” or “筛选量,” retaining the distinction from a measured rupture criterion.

Audit against the English source segment passed:

- 31 ordered step headings and all three lettered sections retained.
- 451 inline-code entries match exactly and in their original order.
- The code-fence language and contents match exactly.
- All 15 link/image destinations match exactly and in their original order.
- Every numeric token matches, including precision and scientific notation; the numeric-token multiset has no additions or omissions.
- All 188 Markdown table lines are retained.

Scientific limitations remain explicit: optical activation is represented by a post-activation initial state; available work is not incident laser energy; spatial fields, phase exchange, rebound, rupture and target impact are excluded; the nine-case maximum is conditional; stored column quantities are distinct from actual emitted quantities; actual material properties require calibration. No unresolved translation uncertainty was identified. This review checks translation fidelity, not a new physics validation or live Desktop click-through.
