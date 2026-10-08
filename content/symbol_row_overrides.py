"""Second-pass corrections to individually expanded local declarations.

These resolve shared units, embedded parameters, and context changes. They do
not change governing equations or numerical inputs. The complete old bilingual
fragments remain in the JSON as source provenance.
"""
import re
from symbol_row_vocabulary import VOCABULARY

def review_rows(data,equations):
    originals={e['id']:e for e in equations}

    def put(eid,symbol,en,zh,unit,shown=None):
        shown=shown or symbol
        item=dict(symbol=symbol,en=f'${shown}$ — {en} ({"dimensionless" if unit=="1" else unit})',
                  zh=f'${shown}$ — {zh}（{"无量纲" if unit=="1" else unit}）',unit=unit,
                  source_en=None,source_zh=None,review='Explicit individual definition checked against the original declaration.')
        current=data[eid]['rows']
        for index,row in enumerate(current):
            if row['symbol']==symbol: current[index]=item;return
        current.append(item)

    def from_vocabulary(eid,symbol):
        chapter=5 if eid.startswith('A-') else int(eid[1])
        en,zh,unit=VOCABULARY[chapter][symbol]
        put(eid,symbol,en,zh,unit)

    def notes(eid,en,zh):
        data[eid]['notes_en'].append(en)
        data[eid]['notes_zh'].append(zh)

    def move(eid,symbol):
        for row in list(data[eid]['rows']):
            if row['symbol']==symbol:
                data[eid]['rows'].remove(row)
                notes(eid,row['en'],row['zh'])

    units={
        1:{r'R(t)':'m',r'\boldsymbol u(\boldsymbol x,t)':'m s⁻¹',r'K_l/E_B':'1',r'd\Omega':'1',r'S^2':'—',r'\boldsymbol0':'1'},
        2:{r'T/\mathrm K':'1'},
        3:{r'm_j':'kg',r'U_{\mathrm{rms}}':'m s⁻¹',r'SR':'1',r't-r_i/c':'s',r'[Av]':'m³ s⁻¹'},
        4:{r'K_n':'Pa m⁻¹',r'm_f':'kg',r'A_f':'m²',r'\boldsymbol0':'1',r'\mathscr L_r(r^2)':'1',r'\mathscr L_r(r^4)':'m²'},
        5:{r'K_g^{\mathrm{bulk}}':'Pa',r'k_{\mathrm{perm}}':'m²',r'\mu_l':'Pa s'},
    }
    for eid,d in data.items():
        chapter=5 if eid.startswith('A-') else int(eid[1])
        for row in d['rows']:
            unit=units.get(chapter,{}).get(row['symbol'])
            if unit:
                row['unit']=unit
                # Always attach the unit to THIS variable, not a neighbor.
                if not re.search(r'\([^()]*\)|（[^（）]*）|dimensionless|无量纲',row['en']):
                    row['en']+=f' ({"dimensionless" if unit=="1" else unit})'
                    row['zh']+=f'（{"无量纲" if unit=="1" else unit}）'
        # A condition is a statement, not an additional physical variable.
        for symbol in (r'\min',r'\approx',r'\Delta',r'[\ ]_0^b',r'[f(q)]_a^b',r'[\ ]_{R_{\mathrm{ref}}}^{R}'):
            move(eid,symbol)

    # C1-E06 exactly follows the requested physical pairing.
    put('C1-E06','u','Radial liquid velocity','液体径向速度','m s⁻¹')
    put('C1-E06',r'\dot R','Bubble-wall radial velocity','气泡壁面径向速度','m s⁻¹')
    put('C1-E06','r','Radial liquid position','液体径向位置','m')
    put('C1-E06','R','Positive cavity radius','正的空腔半径','m',r'R>0')
    put('C1-E06','p_l','Liquid-side pressure at the cavity wall','空腔壁面处的液体侧压力','Pa')
    put('C1-E06','p_b','Spatially uniform bubble pressure','空间均匀的气泡压力','Pa')
    put('C1-E06',r'\sigma','Nonnegative surface tension','非负表面张力','N m⁻¹',r'\sigma\ge0')
    put('C1-E06',r'\mu','Nonnegative carrier dynamic viscosity','非负载液动力黏度','Pa s',r'\mu\ge0')
    put('C1-E06',r'\partial_r u','Radial strain rate, evaluated at the wall','在壁面取值的径向应变率','s⁻¹')
    order=['u',r'\dot R','r','R','p_l','p_b',r'\sigma',r'\mu',r'\partial_r u']
    data['C1-E06']['rows'].sort(key=lambda x:order.index(x['symbol']))

    # Local numerical/physical context that was embedded in shared clauses.
    put('C1-E19',r'\rho','Substituted carrier density','代入的载液密度','kg m⁻³',r'\rho=1000')
    data['C1-E19']['notes_en']=[s for s in data['C1-E19']['notes_en'] if not s.startswith('Substituted inputs')]
    data['C1-E19']['notes_zh']=[s for s in data['C1-E19']['notes_zh'] if not s.startswith('代入输入')]
    for s in ('w','g'): move('C1-E08',s)

    for eid in ('C2-E01','C2-E14','C2-E17','C2-E24','C2-E33','C2-E34'):
        if eid=='C2-E01': from_vocabulary(eid,'r')
        if eid in ('C2-E14','C2-E33'): from_vocabulary(eid,'T_i')
        if eid in ('C2-E17','C2-E34'):
            from_vocabulary(eid,'T');from_vocabulary(eid,'p')
        if eid=='C2-E24':from_vocabulary(eid,'N_s')
    put('C2-E06',r'\mathcal R_\lambda','Front-face reflected energy fraction','前表面反射能量比例','1',r'\mathcal R_\lambda\in[0,1]')
    from_vocabulary('C2-E06',r'\lambda')
    from_vocabulary('C2-E31',r'\lambda')
    for eid in ('C2-E22','C2-E23','C2-E24'):
        put(eid,'s','Species index, from 1 through the declared species count','从 1 到所声明组分数的组分指标','1',r's=1,\ldots,N_s')
        from_vocabulary(eid,'N_s')

    for eid in ('C3-E03','C3-E04'):
        from_vocabulary(eid,'d_{ij}')
        if eid=='C3-E03':from_vocabulary(eid,r'\xi')
    put('C3-E03','d_{ij}','Fixed separation between source j and observation center i','源 j 与观察中心 i 之间的固定距离','m',r'd_{ij}>0')
    from_vocabulary('C3-E04','N_b')
    for symbol in (r'\mathbb E',r'\operatorname{Var}',r'\Pr'):
        from_vocabulary('C3-E01',symbol)
    from_vocabulary('C3-E06',r'\pi')
    notes('C3-E06',r'$\sum$ sums the stated polygon steps; $k$ runs from 1 to $N-1$.',r'$\sum$ 对规定多边形步数求和；$k$ 从 1 遍历至 $N-1$。')
    for eid in ('C3-E04','C3-E05','C3-E31'):
        for s in ('i','j'):
            put(eid,s,'Bubble index over the declared activated sources','遍历声明的已激活源的气泡指标','1')
    notes('C3-E04',r'$i\ne j$; each index runs from 1 to $N_b$; Newton dots on a radius denote its time derivatives.',r'$i\ne j$；每个指标从 1 遍历至 $N_b$；半径上的牛顿点号表示其时间导数。')
    for eid in ('C3-E05','C3-E31'):
        for s in (r'\dot R_j',r'\ddot R_j'):from_vocabulary(eid,s)
        put(eid,r'\dot R_i','Wall radial velocity of bubble i','气泡 i 的壁面径向速度','m s⁻¹')
        put(eid,r'\ddot R_i','Wall radial acceleration of bubble i','气泡 i 的壁面径向加速度','m s⁻²')
    for eid in ('C3-E07','C3-E08','C3-E09'):
        from_vocabulary(eid,r'\dot R');from_vocabulary(eid,r'\ddot R')
    put('C3-E11','b_i','Volume-source strength of bubble i','气泡 i 的体积源强度','m³ s⁻¹',r'b_i=R_i^2\dot R_i')
    put('C3-E11','b_j','Volume-source strength of bubble j','气泡 j 的体积源强度','m³ s⁻¹',r'b_j=R_j^2\dot R_j')
    put('C3-E12',r'\dot V_i','First time derivative of bubble-i volume','气泡 i 体积的一阶时间导数','m³ s⁻¹')
    put('C3-E12',r'\ddot V_i','Second time derivative of bubble-i volume','气泡 i 体积的二阶时间导数','m³ s⁻²')
    put('C3-E17',r'a_{\mathrm{in}}','Solid-tube inlet radius','固体管入口半径','m')
    from_vocabulary('C3-E17','a_j')
    put('C3-E17',r'\alpha','Jet-to-inlet cross-sectional area ratio','射流截面积与入口截面积之比','1')
    notes('C3-E17',r'$a_{\mathrm{in}}>a_j>0$; $\alpha=(a_j/a_{\mathrm{in}})^2$ and $0<\alpha<1$.',r'$a_{\mathrm{in}}>a_j>0$；$\alpha=(a_j/a_{\mathrm{in}})^2$ 且 $0<\alpha<1$。')
    put('C3-E19',r'\xi','Dummy axial integration coordinate','轴向积分哑坐标','m')
    from_vocabulary('C3-E19',r'd\xi')
    put('C3-E20','r','Radial position measured from the liquid-jet axis','从液体射流轴线计量的径向位置','m',r'r\in[0,a]')
    put('C3-E20','z','Axial liquid-jet coordinate','液体射流轴向坐标','m')
    put('C3-E21','r','Radial position measured from the liquid-jet axis','从液体射流轴线计量的径向位置','m')
    put('C3-E21','g','Positive temporal growth rate, not gravitational acceleration','正的时间增长率，并非重力加速度','s⁻¹',r'g>0')
    notes('C3-E21',r'$0<\delta_0\le\delta(t)\ll a_0$ defines the small-disturbance regime.',r'$0<\delta_0\le\delta(t)\ll a_0$ 定义微小扰动范围。')
    from_vocabulary('C3-E22',r'\delta_0');from_vocabulary('C3-E22',r'\delta_{\mathrm{crit}}')
    notes('C3-E22',r'$\delta_0<\delta_{\mathrm{crit}}\ll a_0$; the chosen threshold remains within linear theory.',r'$\delta_0<\delta_{\mathrm{crit}}\ll a_0$；所选阈值仍处于线性理论范围。')
    for eid in ('C3-E26','C3-E33'):
        put(eid,r'\xi','Dummy time in the pressure-observation integral','压力观察积分中的时间哑变量','s')
    put('C3-E28','k','Species index, not the jet-instability wavenumber','组分指标，并非射流失稳波数','1')
    from_vocabulary('C3-E29',r'\lambda')
    put('C3-E30','L_j','Specified emitted jet length','指定喷出射流长度','m',r'L_j=50\times10^{-6}')
    from_vocabulary('C3-E33',r'\boldsymbol x')

    # Distinguish variational notation from physical cohesive opening.
    move('C4-E05',r'\delta')
    data['C4-E05']['notes_en']=[s.replace(' (m)','') if s.startswith(r'$\delta$') else s for s in data['C4-E05']['notes_en']]
    data['C4-E05']['notes_zh']=[s.replace('（m）','') if s.startswith(r'$\delta$') else s for s in data['C4-E05']['notes_zh']]
    for eid in ('C4-E02','C4-E35'):
        for s in ('t_a','t_b','t','dt'):from_vocabulary(eid,s)
        notes(eid,r'$t_a<t_b$ fixes the integration interval.',r'$t_a<t_b$ 确定积分区间。')
    for symbol in (r'\alpha',r'\beta'):
        put('C4-E40',symbol,'Cartesian in-plane direction index, taking 1 or 2','取 1 或 2 的笛卡尔面内方向指标','1')
    notes('C4-E40',r'$\sum_{\alpha,\beta=1}^{2}$ sums all four index pairs.',r'$\sum_{\alpha,\beta=1}^{2}$ 对四种指标组合求和。')
    for eid in ('C4-E04','C4-E41'):
        for s in ('K_f','U_b','U_T'):from_vocabulary(eid,s)
    for s in ('U_b','U_T'):from_vocabulary('C4-E05',s)
    for s in ('C_1','C_2'):from_vocabulary('C4-E14',s)
    for s in ('C_3','C_4'):from_vocabulary('C4-E15',s)
    for eid in ('C4-E22',):
        for s in (r'G_{\bar V}',r'G_{p_0}'):from_vocabulary(eid,s)

    # Elastic tensor components are physical stresses, not bare index labels.
    from_vocabulary('A-E02',r'\mathbf T^e')
    for s in (r'T^e_{rr}',r'T^e_{\theta\theta}',r'T^e_{\phi\phi}'):
        from_vocabulary('A-E02',s)
    data['A-E02']['notes_en']=[s for s in data['A-E02']['notes_en'] if not s.startswith((r'$\theta\theta$',r'$\phi\phi$'))]
    data['A-E02']['notes_zh']=[s for s in data['A-E02']['notes_zh'] if not s.startswith((r'$\theta\theta$',r'$\phi\phi$'))]
    notes('A-E02','Elastic stress is positive in tension.','弹性应力以拉伸为正。')
    for s in (r'\mathbf T',r'\mathbf T^e',r'\mathbf D',r'T_{rr}',r'T_{\theta\theta}',r'T^e_{rr}',r'T^e_{\theta\theta}'):
        from_vocabulary('A-E09',s)
    for s,en,zh in [(r'D_{rr}','Radial strain-rate component','径向应变率分量'),(r'D_{\theta\theta}','Polar tangential strain-rate component','极角切向应变率分量'),(r'D_{\phi\phi}','Azimuthal tangential strain-rate component','方位角切向应变率分量')]:
        put('A-E09',s,en,zh,'s⁻¹')
    put('A-E10','r','Current material radial position outside the cavity','空腔外部的当前物质径向位置','m',r'r\geq R>0')
    from_vocabulary('A-E10','R')
    put('A-E13','G_g','Substituted network shear modulus','代入的网络剪切模量','Pa','G_g=20000')
    put('A-E13',r'R_{\mathrm{ref}}','Substituted reference cavity radius','代入的参考空腔半径','m',r'R_{\mathrm{ref}}=5\times10^{-6}')
    put('A-E13','R','Substituted current cavity radius','代入的当前空腔半径','m',r'R=30\times10^{-6}')
    data['A-E13']['notes_en']=['The numbers 5 and 30 in radius ratios both use µm. Powers denote numerical exponents; Pa means pascal, J joule, and the cross denotes multiplication.']
    data['A-E13']['notes_zh']=['半径比值中的数值 5 与 30 均采用 µm。幂表示数值指数；Pa 为帕斯卡，J 为焦耳，叉号表示乘法。']
    notes('C1-E17',r'$x,q\in[0,1]$ and $q=x^3$ define the substitution domain.',r'$x,q\in[0,1]$ 且 $q=x^3$ 确定换元范围。')
    put('C1-E12',r'\theta','Polar direction label in the strain-rate components','应变率分量中的极角方向标记','—')
    put('C1-E12',r'\psi','Azimuthal direction label, distinct from velocity potential','与速度势区别使用的方位角方向标记','—')
    put('C2-E29','T_*','Selected final vapor temperature on the constant-pressure path','恒压路径上选定的最终蒸气温度','K')
    put('C4-E07','w','Film displacement along the same positive direction as PVC displacement','与 PVC 位移采用相同正方向的薄膜位移','m')

    # Parameters defined inside another variable's sentence also receive their
    # own row. Only explicitly named vocabulary entries are added; this is not
    # a guess from a partial letter match inside a larger TeX expression.
    for eid,d in data.items():
        chapter=5 if eid.startswith('A-') else int(eid[1])
        present={row['symbol'] for row in d['rows']}
        for raw in re.findall(r'\$([^$]+)\$',originals[eid]['symbols_en']+' '+originals[eid]['symbols_zh']):
            name=re.split(r'\\(?:geq?|leq?|ne|in|ll)(?![A-Za-z])|[><=]',raw,maxsplit=1)[0].strip()
            if name in VOCABULARY[chapter] and name not in present:
                if eid=='C4-E05' and name==r'\delta':continue
                if re.match(r'^(?:\\partial|\\nabla|d/|D/)',name):continue
                from_vocabulary(eid,name);present.add(name)

    # Complete metadata for every remaining single definition, including
    # geometric labels that intentionally have no numerical SI dimension.
    for eid,d in data.items():
        for row in d['rows']:
            if row['unit']=='defined in text':
                tail=re.sub(r'\$[^$]+\$','',row['en'])
                match=re.search(r'\(([^()]+)\)',tail)
                if match: row['unit']=match[1].replace('dimensionless','1')
                elif 'dimensionless' in tail: row['unit']='1'
                else: row['unit']='—'
            unit=row['unit']
            if unit not in ('1','—'):
                if unit not in row['en']:row['en']+=f' ({unit})'
                if unit not in row['zh']:row['zh']+=f'（{unit}）'
        assert len({r['symbol'] for r in d['rows']})==len(d['rows']),eid
