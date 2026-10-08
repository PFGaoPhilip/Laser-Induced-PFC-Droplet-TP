"""Original physical-variable diagrams, one SVG for each equation.

Figures show geometry/force/flow first and retain every supplied variable label.
They are diagrams of the adopted model, not claimed simulation results.
"""
from html import escape
import textwrap
import re

def clean(value):
    value = str(value).replace('$','')
    replacements={r'\rho':'ρ',r'\sigma':'σ',r'\mu':'μ',r'\Delta':'Δ',r'\Pi':'Π',r'\Gamma':'Γ',r'\infty':'∞',r'\tau':'τ',r'\eta':'η',r'\lambda':'λ',r'\kappa':'κ',r'\alpha':'α',r'\varphi':'φ',r'\phi':'φ',r'\partial':'∂',r'\nabla':'∇',r'\theta':'θ',r'\delta':'δ',r'\nu':'ν',r'\pi':'π',r'\chi':'χ',r'\dot R':'Ṙ',r'\ddot R':'R̈',r'\ge':'≥',r'\le':'≤'}
    for a,b in sorted(replacements.items(),key=lambda x:-len(x[0])):value=value.replace(a,b)
    value=re.sub(r'\\(?:mathrm|text|boldsymbol|mathbf|operatorname)\{([^{}]*)\}',r'\1',value)
    return value.replace('{','').replace('}','').replace('\\,',' ').replace('\\!','')

def svg_for(eq):
    d=eq['diagram']
    kind=d.get('type','sphere')
    labels=[clean(v if not isinstance(v,(tuple,list)) else ' / '.join(v)) for v in d.get('labels',[])]
    notes=[clean(v if not isinstance(v,(tuple,list)) else ' / '.join(v)) for v in d.get('notes',[])]
    lines=[]
    for label in labels:
        lines.extend(textwrap.wrap('• '+label,width=71,break_long_words=False,break_on_hyphens=False) or [''])
    note_lines=[]
    for v in notes:note_lines.extend(textwrap.wrap(v,108,break_long_words=False,break_on_hyphens=False))
    cols=2 if len(lines)>7 else 1
    if cols==2:
        # Wrap independent labels in balanced cells, keeping each entry together.
        cells=[textwrap.wrap('• '+v,53,break_long_words=False,break_on_hyphens=False) or [''] for v in labels]
        left,right=[],[]
        for cell in cells:(left if len(left)<=len(right) else right).extend(cell)
        rows=max(len(left),len(right))
    else:left,right=lines,[];rows=len(left)
    height=450+max(1,rows)*24+len(note_lines)*23
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 {height}" role="img" aria-labelledby="title desc">',
           f'<title id="title">{escape(eq["id"])} — {escape(eq["caption_en"])}</title>',
           f'<desc id="desc">{escape("; ".join(labels+notes))}</desc>',
           '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0 L8 4 L0 8Z" fill="#8edbd4"/></marker></defs>',
           f'<rect width="980" height="{height}" rx="8" fill="#142632"/>',
           '<style>text{font-family:Arial,"Microsoft YaHei",sans-serif;fill:#e7f0f3;font-size:20px}.muted{fill:#b4c7d2;font-size:17px}.accent{fill:#8edbd4}.line{fill:none;stroke:#8edbd4;stroke-width:3}.thin{fill:none;stroke:#b4c7d2;stroke-width:2}.arrow{fill:none;stroke:#8edbd4;stroke-width:3;marker-end:url(#arrow)}.area{fill:#213e4b;stroke:#b4c7d2;stroke-width:2}</style>',
           f'<text x="28" y="36" class="accent">{escape(eq["id"])} · Physical variable map / 物理变量图</text>']
    def text(x,y,s,cls=''):parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>')
    def path(v,cls='line'):parts.append(f'<path d="{v}" class="{cls}"/>')
    def circle(x,y,r,cls='area'):parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/>')
    def rect(x,y,w,h,cls='area'):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="{cls}"/>')
    combined=' '.join(labels)
    initial_core=(kind=='sphere' and (eq['id'].startswith('C2-') or 'PFC-core' in combined or 'a₀' in combined))
    nucleus=kind=='nucleation'
    if kind=='gel':
        if eq['id']=='C5-E20':
            for x in range(105,625,45):path(f'M{x} 112 V266','thin')
            for y in range(116,269,38):path(f'M96 {y} H622','thin')
            for y in [140,193,244]:path(f'M118 {y} H710','arrow')
            text(105,88,'Solvent through network / 溶剂穿过网络')
            text(737,180,'jl →')
            path('M510 290 H215','arrow');text(561,296,'∇ppore ←')
            text(156,334,'Lg , kperm , μl , Md ; tporo')
        else:
            circle(196,180,80,'thin');circle(196,180,36)
            path('M196 180 H232','arrow');text(190,160,'Rref')
            path('M196 180 L259 231','arrow');text(254,240,'r₀')
            circle(610,180,116,'thin');circle(610,180,78)
            path('M610 180 H688','arrow');text(650,162,'R')
            path('M610 180 L700 253','arrow');text(699,261,'r')
            path('M298 180 H472','arrow');text(307,146,'Material map / 材料映射')
            text(82,302,'Reference / 参考状态');text(513,322,'Deformed / 变形状态: λr , λθ')
            text(757,106,'Gg , ηg');text(753,153,'σrr , σθθ');text(753,201,'p∞')
            text(583,187,'pb')
    elif kind in {'sphere','nucleation','phase'}:
        radius='a₀' if initial_core and ('a₀' in combined or eq['id']=='C2-E27') else ('a' if initial_core else ('rn' if nucleus else 'R(t)'))
        circle(310,185,78);path('M310 185 H388','arrow');text(337,169,radius)
        if nucleus:
            text(284,196,'pv');text(109,91,'PFC liquid / PFC 液相: pd , Ti')
            text(105,299,'New interface / 新界面: σvp')
        elif initial_core:
            text(270,198,'pd , ρd');text(583,157,'Carrier / 载液: pc')
            text(583,189,'Interface / 界面: σpc , Πshell')
            text(92,311,'Finite PFC core / 有限 PFC 液核')
        else:
            path('M310 185 L457 263','arrow');text(398,226,'r ≥ R')
            text(277,193,'pb');text(610,166,'p∞ , ρ , μ , σ' if kind!='gel' else 'p∞ , ρg , Gg , ηg')
            text(610,194,'Surrounding medium / 周围介质')
            for x,y,ex,ey in [(310,78,310,54),(201,185,167,185),(419,185,459,185)]:path(f'M{x} {y} L{ex} {ey}','arrow')
            text(100,312,'Signed wall motion / 有符号壁运动: Ṙ, R̈')
            text(129,75,'+r direction / +r 方向','muted')
        if kind=='phase':
            circle(295,195,27);text(590,244,'Liquid ↔ vapor / 液体 ↔ 蒸气','muted')
            text(590,271,'ml , mv , j , Q̇ , Tb')
        if kind=='nucleation':
            path('M595 279 H922','arrow');path('M617 324 V93','arrow')
            path('M620 279 C655 278 676 133 731 155 S796 279 853 318')
            path('M710 148 V279','thin');text(714,130,'r* , W*','muted')
            text(572,94,'W(rn)');text(865,299,'rn','muted')
    elif kind=='timescale':
        if eq['id'] in {'C1-E16','C1-E17','C3-E10'}:
            circle(197,184,83);circle(426,184,37)
            path('M285 184 H377','arrow');text(120,294,'Rmax , Ṙ(0) = 0');text(386,264,'R ↓')
            path('M638 288 H923','arrow');path('M660 291 V94','arrow')
            path('M665 118 C778 120 857 143 904 282')
            text(683,96,'R / Rmax');text(843,315,'t / tc')
            text(584,336,'Formal collapse / 形式塌缩','muted')
        elif eq['id']=='C1-E20':
            circle(247,181,96);circle(247,181,36,'thin')
            path('M247 181 H283','arrow');text(254,160,'RM')
            path('M392 181 H716','arrow');text(446,153,'c = 1500 m/s')
            path('M363 227 H280','arrow');text(341,258,'|Ṙ| = M* c')
            text(112,314,'Rmax → RM ; xM = RM / Rmax')
            text(588,289,'Mw = |Ṙ| / c');text(588,322,'Flag: M* = 0.1 / 检查阈值','muted')
        elif eq['id']=='C1-E31':
            circle(171,181,57);path('M228 181 H855','arrow')
            text(118,275,'R , Ṙ');text(303,145,'Pressure information / 压力信息: c')
            path('M231 286 H854','thin');text(470,312,'Le ; ta = Le / c')
            rect(596,89,92,52);text(608,122,'τe')
            text(107,82,'Moving cavity / 运动腔体');text(538,239,'Compare transit with event / 传播与事件比较','muted')
        elif eq['id'].startswith('C2-'):
            rect(99,113,63,152);circle(546,191,78);circle(546,191,59,'thin')
            path('M166 191 H466','arrow');text(245,164,'Lh');text(492,314,'PFC core / PFC 液核')
            text(91,89,'Absorber / 吸收体');text(658,165,'δT ~ √(α τh)')
            text(653,200,'α = k / (ρ cp)');text(653,240,'tth ~ Lh² / α')
            text(215,286,'Diffusive heating / 扩散加热','muted')
        elif eq['id']=='C3-E22':
            path('M94 158 C171 144 211 173 282 158 S400 144 474 158','line')
            path('M94 222 C171 236 211 207 282 222 S400 236 474 222','line')
            path('M124 190 H448','arrow');text(248,129,'δ₀ , a₀');text(237,190,'Uj')
            path('M487 190 H761','arrow');rect(796,101,34,180)
            text(567,162,'H');text(551,261,'tflight = H / Uj')
            text(113,314,'Growth / 增长: δarr = δ₀ exp(gmax tflight)')
            text(551,311,'δcrit ; tlin ; tσ','muted')
        elif eq['id']=='C5-E18':
            text(97,90,'Two declared models / 两个声明的模型')
            rect(109,119,610,40);text(130,146,'ts = 6.70820 µs — shear transit / 剪切传播')
            rect(109,207,250,40);text(130,232,'tc,liq = 2.74404 µs')
            text(464,244,'Ideal liquid collapse / 理想液体塌缩','muted')
            text(131,314,'ts / tc,liq = 2.44464 ; Lg = Rmax = 30 µm')
        else:
            text(99,98,'Time definitions / 时间定义')
            relevant=[v.split(':')[0].split(';')[0] for v in labels if any(k in v for k in ['τ','time','t_','tσ','t_s','t_D','De','ts =','tc,','tL','τrel'])][:3]
            if not relevant:relevant=labels[:3]
            for y,label in zip([142,205,268],relevant):
                rect(109,y-25,560,38);text(129,y,label);path(f'M109 {y+25} H669','thin')
            text(110,334,'Equal boxes identify definitions, not a time ratio / 等宽框列定义，不代表时间比','muted')
    elif kind=='laser':
        if eq['id'] in {'C2-E01','C2-E02','C2-E04'}:
            circle(257,193,103,'thin');path('M257 193 H360','arrow');text(308,175,'r , w')
            if eq['id']=='C2-E04':circle(257,193,52);text(240,221,'rt')
            text(125,322,'Beam cross-section / 光束截面')
            path('M598 284 H922','arrow');path('M626 285 V99','arrow')
            path('M628 123 C687 123 727 176 770 229 S850 280 912 282')
            path('M797 260 V284','thin');text(791,312,'w');text(924,302,'r')
            text(590,93,'F(r)');text(639,121,'F₀');text(761,183,'F₀ e⁻²','muted')
            text(123,91,'EL = ∫ F(r) 2πr dr')
        else:
            rect(302,95,124,190);rect(426,95,210,190);text(302,318,'Absorber / 吸收体');text(476,318,'PFC / 全氟碳')
            for y in [135,188,240]:path(f'M75 {y} H302','arrow');path(f'M328 {y} H475','arrow')
            text(81,106,'F(r), I(r,t), EL');text(336,79,'Qabs');text(447,123,'T(x,t)')
            path('M683 266 H925','arrow');path('M696 274 V105','arrow');path('M700 257 C737 249 751 137 790 155 S854 251 914 257')
            text(873,294,'t, τh');text(717,109,'f(t)','muted');text(690,322,'α , Lh , δT , tth','muted')
            path('M302 336 H426','arrow');text(342,353,'z , ha','muted')
    elif kind=='energy':
        if eq['id'].startswith('C1-'):
            circle(230,188,113,'thin');circle(230,188,78,'thin');circle(230,188,48)
            path('M230 188 H278','arrow');text(246,169,'R')
            path('M302 188 H355','arrow');text(303,169,'u(r,t)')
            text(91,320,'Shell / 液壳: 4πr²dr , ρ')
            rect(539,123,353,119);text(558,157,'Kℓ = ∫ ρu²/2 dV');text(558,196,'Pressure work / 压力功: pb dV')
            path('M368 188 H532','arrow');text(537,293,'Surface + viscous work / 表面及黏性功','muted')
        elif eq['id'].startswith('C4-'):
            rect(48,128,260,108);rect(359,128,260,108);rect(670,128,260,108)
            text(67,160,'External work / 外力功');text(72,204,'∫ tl · vf dt dA')
            text(379,160,'Solid / 固体: Kf , Ub');text(384,204,'PVC / 传递')
            text(687,160,'Fracture / 断裂: Γ Ac');text(686,204,'Motion / 运动: mf , vf')
            path('M308 182 H359','arrow');path('M619 182 H670','arrow')
            path('M482 236 V285','arrow');text(521,287,'Dissipation / 耗散 ≥ 0','muted')
            text(75,91,'Load control matters / 必须声明载荷控制')
            text(90,324,'Energy and impulse are separate budgets / 能量与冲量分别核算','muted')
        elif eq['id'].startswith('C5-'):
            circle(180,179,77,'line');circle(180,179,29);path('M180 179 H257','arrow');text(220,158,'R')
            text(126,285,'Rref → R');text(98,98,'Cavity / 腔体: pb dV')
            rect(436,125,410,123);text(459,164,'Elastic storage / 弹性储能: Wg')
            text(460,207,'Viscous loss / 黏性耗散: Ḋg ≥ 0')
            path('M273 180 H431','arrow');text(467,294,'Gg , ηg ; intact network / 完整网络','muted')
            text(93,329,'Stored work is not automatically jet energy / 储存功不自动转为射流能','muted')
        else:
            rect(68,120,180,110);rect(392,120,210,110);rect(748,120,160,110)
            text(85,157,'Source / 能源');text(91,198,'Eabs , Q');text(412,158,'Bubble / 气泡');text(418,199,'pb dV , Kℓ');text(766,158,'Output / 输出');text(775,198,'Ej , W')
            path('M248 176 H392','arrow');path('M602 176 H748','arrow');path('M500 230 V280','arrow')
            text(300,104,'Conservation / 守恒');text(541,294,'Dissipation / 耗散: Ḋ ≥ 0')
    elif kind=='impulse':
        if eq['id'].startswith('C4-'):
            rect(103,165,470,39);text(126,88,'Film / 薄膜: mA , Df , T₀')
            for x in [225,340,455]:path(f'M{x} 271 V208','arrow')
            path('M340 103 V155','arrow');text(396,85,'tcoh + bending / 内聚及弯曲','muted')
            text(196,307,'Applied JA / 施加面冲量')
            path('M668 269 H915','arrow');path('M680 274 V104','arrow')
            path('M681 249 L700 249 L717 143 L814 143 L835 249 L899 249')
            text(714,126,'pload','muted');text(803,307,'ta → tb','muted')
        else:
            rect(100,127,530,128);path('M130 206 H604','arrow');path('M664 269 H915','arrow');path('M680 275 V103','arrow')
            path('M681 249 L700 249 L717 143 L814 143 L835 249 L899 249')
            text(93,105,'Driven end / 驱动端: Π0');text(423,111,'Outlet / 出口: Π = 0','muted')
            path('M108 282 H627','thin');text(345,310,'L');text(265,181,'Δu = −∇Π / ρ');text(728,131,'p − pref','muted');text(883,301,'t, τ','muted')
    elif kind=='array':
        for y in [122,207,292]:
            for x in [144,254,364]:circle(x,y,22)
        path('M164 122 H232','thin');text(186,107,'dij , s')
        text(100,77,'Sites / 位点: i , j , Nd');text(443,156,'Individual phase inventories / 各相存量')
        text(443,188,'pb,i(t), Ri(t), activation delay / 激活延迟')
        path('M493 262 H894','arrow');text(535,291,'Propagation / 传播: ri / c')
    elif kind in {'jet','impact'}:
        if eq['id'] in {'C1-E27','C1-E28','C1-E29','C1-E30'}:
            path('M88 101 H700 M88 274 H700','thin');circle(258,186,52)
            path('M700 101 C640 154 640 222 700 274','line')
            path('M318 186 H270','arrow');text(303,160,'n → gas / 指向气相')
            path('M258 126 H320','arrow');text(261,104,'s')
            text(234,195,'pb');text(477,197,'Liquid / 液体: u , p , ρ , μ')
            path('M670 187 H753','arrow');text(732,165,'Γ , X(t)')
            text(777,207,'p∞');text(105,316,'Moving interface / 运动界面: Vn , κ , φ')
        else:
            rect(88,146,535,78);path('M110 202 H577','arrow');text(282,127,'a , dj , Aj');text(250,180,'Uj , mj , Pj , Ej');text(268,261,'Finite liquid / 有限液体: Lj')
        if kind=='impact':
            rect(747,77,45,235);path('M623 177 H747','arrow');text(696,338,'Receiver / 接收体: Zr, vi')
            text(804,151,'p, traction');text(804,183,'Ao, τo')
        elif eq['id'] not in {'C1-E27','C1-E28','C1-E29','C1-E30'}:
            path('M672 177 H905','arrow');text(720,147,'Flight gap / 飞行间隙: H')
            path('M744 192 C770 220 794 138 821 177 S868 217 903 177','thin');text(728,269,'δ(t), smax, κj','muted')
    elif kind=='film':
        if eq['id']=='C4-E01':
            rect(127,126,669,36);rect(127,241,669,39)
            text(143,107,'Exposed film face / 薄膜外露面')
            for x in [283,463,638]:path(f'M{x} 227 V169','arrow')
            path('M720 165 V214','arrow');text(736,207,'nf ↓')
            text(272,313,'Liquid / 液体: u , p , μ , Du')
            text(354,192,'tl = Tl nf','muted')
        elif eq['id']=='C4-E40':
            path('M96 242 H889','thin');path('M115 242 C279 242 295 128 494 128 S691 242 869 242')
            rect(91,220,28,48);rect(866,220,28,48)
            text(262,101,'Ωf : film interior / 薄膜内部')
            text(585,281,'∂Ωf , dℓ ; n outward / 外法向')
            path('M868 206 H924','arrow');text(909,190,'n')
            text(93,323,'Clamp / 夹持: δw = 0 ; ∂n δw = 0')
            text(357,204,'δUb , δUT','muted')
        elif eq['id']=='C4-E07':
            rect(119,126,703,28);rect(119,233,703,40)
            text(135,111,'Film / 薄膜: w , mA , Df');text(138,314,'Intact PVC / 完整 PVC: wP , mA,P , DP')
            for x in [303,486,669]:path(f'M{x} 303 V276','arrow');path(f'M{x} 226 V162','arrow')
            text(328,198,'tP→f : transmitted traction / 传递牵引')
            text(651,337,'Liquid load / 液体载荷','muted')
        elif eq['id'].startswith('C4-') and (13<=int(eq['id'].split('E')[1])<=24 or eq['id']=='C4-E37'):
            path('M80 263 H603','thin');path('M92 263 C195 263 191 146 347 146 S499 263 590 263')
            rect(77,243,26,45);rect(579,243,26,45)
            path('M342 259 V150','arrow');text(355,218,'w(r)');text(259,319,'p₀ ↑ ; Vbl')
            path('M344 282 H588','thin');text(467,302,'b');text(337,280,'0')
            circle(783,196,85,'thin');path('M783 196 H868','arrow');text(817,184,'b')
            text(722,317,'Ac = π b²');text(101,91,'Clamped blister / 夹持鼓泡')
            text(624,102,'w(b)=0 ; slope=0 / 边缘斜率为零','muted')
        else:
            rect(107,205,760,65);path('M145 205 C276 205 295 106 482 106 S686 205 828 205')
            for x in [305,465,635]:path(f'M{x} 206 V150','arrow')
            text(150,297,'Donor / 供体');text(326,95,'Film / 薄膜: Ef, hf, ρf, Df')
            path('M124 321 H825','thin');text(433,343,'Crack / 裂纹: b , Ac');text(298,181,'pload , w , tcoh')
    elif kind=='cohesive':
        path('M120 287 H859','arrow');path('M145 298 V90','arrow');path('M145 287 L343 110 L779 287')
        path('M343 110 V287','thin');text(91,92,'tn , Tmax');text(299,317,'δ0');text(750,317,'δc');text(815,318,'δ')
        text(386,221,'Area = Γ / 面积 = Γ');text(196,206,'Kn');text(583,91,'Opening only / 仅张开分支')
    else:
        rect(115,112,270,150);rect(609,112,270,150);path('M385 189 H609','arrow');text(145,188,'Inputs / 输入');text(638,188,'Outputs / 输出')
    parts.append('<path d="M28 356 H952" stroke="#405967"/>')
    text(30,382,'Variables in this equation / 本式变量','muted')
    y0=409
    for i,s in enumerate(left):text(30,y0+24*i,s,'muted')
    for i,s in enumerate(right):text(508,y0+24*i,s,'muted')
    start=y0+max(len(left),len(right))*24+18
    for i,s in enumerate(note_lines):text(30,start+23*i,s,'muted')
    parts.append('</svg>')
    return '\n'.join(parts)+'\n'
