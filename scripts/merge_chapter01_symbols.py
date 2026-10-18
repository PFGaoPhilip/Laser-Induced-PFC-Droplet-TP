"""Merge derivation declarations into the existing compact bilingual tables.

Owner layout correction, 2026-10-19. Equations and derivations stay unchanged.
Each TSV record defines one symbol. Existing rows retain their wording.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# equation | symbol | English meaning | Chinese meaning | unit
ROWS = r'''
01|\rho|positive carrier density|正载液密度|kg m⁻³
01|p_b|bubble pressure|气泡压力|Pa
01|\sigma|constant surface tension|常数表面张力|N m⁻¹
01|\mu|dynamic viscosity|动力黏度|Pa s
01|\ddot R|wall acceleration|壁面加速度|m s⁻²
02|\rho|positive constant liquid density|正常数液体密度|kg m⁻³
02|\delta r|positive fixed shell thickness|固定球壳正厚度|m
02|\pi|circle constant|圆周率|1
02|\partial_r|radial derivative at fixed time|固定时间的径向导数|m⁻¹
03|\boldsymbol u|liquid velocity vector|液体速度矢量|m s⁻¹
03|\boldsymbol e_r|outward radial unit vector|向外径向单位矢量|1
03|\nabla\times|spatial curl operator|空间旋度算子|m⁻¹
03|\boldsymbol0|zero vorticity vector|零涡量矢量|s⁻¹
03|g(t)|velocity-potential gauge function|速度势规范函数|m² s⁻¹
05|\boldsymbol u|liquid velocity, $\nabla\phi$|液体速度，即 $\nabla\phi$|m s⁻¹
05|\nabla|spatial gradient operator|空间梯度算子|m⁻¹
05|\nabla\cdot|spatial divergence operator|空间散度算子|m⁻¹
05|\nabla\times|spatial curl operator|空间旋度算子|m⁻¹
05|\nabla^2|vector Laplacian operator|矢量拉普拉斯算子|m⁻²
05|u_i|Cartesian velocity component indexed by $i$|指标 $i$ 对应的笛卡尔速度分量|m s⁻¹
05|u_j|Cartesian velocity component indexed by $j$|指标 $j$ 对应的笛卡尔速度分量|m s⁻¹
05|i|Cartesian component index, 1, 2 or 3|笛卡尔分量指标，取 1、2 或 3|1
05|j|Cartesian component index, 1, 2 or 3|笛卡尔分量指标，取 1、2 或 3|1
05|\partial_i|coordinate derivative indexed by $i$|指标 $i$ 对应的坐标导数|m⁻¹
05|\partial_j|coordinate derivative indexed by $j$|指标 $j$ 对应的坐标导数|m⁻¹
05|\sum|summation over the indicated index|对指定指标求和|1
05|B_0(t)|Bernoulli integration function|伯努利积分函数|m² s⁻²
05|p|local liquid pressure|局部液体压力|Pa
06|\boldsymbol n|unit normal directed from liquid into gas|液体指向气体的单位法向|1
06|\boldsymbol e_r|outward radial unit vector|向外径向单位矢量|1
06|\kappa|signed interface curvature|带符号界面曲率|m⁻¹
06|\nabla_s\cdot|surface divergence operator|表面散度算子|m⁻¹
06|\nabla\cdot|volume divergence operator|体散度算子|m⁻¹
08|i|component index: PFC vapor, water vapor or permanent gas|组分指标：PFC 蒸气、水蒸气或非凝结气体|1
08|p_i|component partial pressure|组分分压|Pa
08|n_i|component amount of substance|组分物质的量|mol
08|V_b|positive bubble volume|气泡正体积|m³
08|\mathcal R|universal gas constant|通用气体常数|J mol⁻¹ K⁻¹
08|T_b|positive common gas temperature|共同气体正温度|K
09|dV|spherical shell volume element|球壳体积元|m³
09|\theta|polar angle, $0\le\theta\le\pi$|极角，$0\le\theta\le\pi$|1
09|\psi|azimuthal angle, $0\le\psi\le2\pi$|方位角，$0\le\psi\le2\pi$|1
09|b|finite outer cutoff radius, $b>R$|有限外截断半径，$b>R$|m
12|\mu|viscosity, set to zero in this control|黏度，在此对照中置零|Pa s
12|\sigma|surface tension, set to zero in this control|表面张力，在此对照中置零|N m⁻¹
12|p_b|bubble pressure|气泡压力|Pa
13|y'|radius derivative $dy/dR$|半径导数 $dy/dR$|m s⁻²
13|I|positive integrating factor, $I(R_{\max})=1$|正积分因子，$I(R_{\max})=1$|1
13|I'|radius derivative $dI/dR$|半径导数 $dI/dR$|m⁻¹
13|s|positive dummy radius|正积分哑半径|m
13|R_{\max}|maximum cavity radius|最大空腔半径|m
13|\ln|natural logarithm with positive dimensionless argument|自变量为正无量纲数的自然对数|1
13|\exp|exponential with dimensionless argument|自变量无量纲的指数函数|1
17|V_b|cavity volume, $4\pi R^3/3$|空腔体积，$4\pi R^3/3$|m³
17|V|dummy volume variable|积分哑体积变量|m³
17|t|time|时间|s
17|\dot R|wall speed|壁面速度|m s⁻¹
19|x|normalized radius, $R/R_{\max}$|无量纲半径，$R/R_{\max}$|1
19|R|current cavity radius|当前空腔半径|m
20|q|gauge pressure|表压|Pa
20|N|positive integer subdivision count|正整数分段数|1
20|k|time-sample index|时间采样指标|1
20|t_k|sample time|采样时刻|s
20|\Delta t|time-step width|时间段宽度|s
20|\boldsymbol J_p|gauge-pressure mechanical impulse on the liquid control volume|作用于液体控制体的表压机械冲量|N s
20|S(t)|liquid control-volume surface|液体控制体表面|m²
20|\boldsymbol n|outward unit normal to the control surface|控制表面向外单位法向|1
20|dA|area element|面积元|m²
21|p|local liquid pressure|局部液体压力|Pa
21|p_{\mathrm{ref}}|spatially uniform reference pressure|空间均匀参考压力|Pa
21|\nabla|spatial gradient operator|空间梯度算子|m⁻¹
21|\nabla^2|vector Laplacian operator|矢量拉普拉斯算子|m⁻²
21|\partial_t|time derivative at fixed position|固定位置的时间导数|s⁻¹
22|t_0|fixed event start time|固定事件起始时刻|s
22|t_1|fixed event end time|固定事件终止时刻|s
22|t|time|时间|s
22|\boldsymbol u|liquid velocity|液体速度|m s⁻¹
22|\nabla|spatial gradient operator|空间梯度算子|m⁻¹
22|\nabla\cdot|spatial divergence operator|空间散度算子|m⁻¹
22|\nabla^2|spatial Laplacian operator|空间拉普拉斯算子|m⁻²
23|s|dummy axial integration coordinate|轴向积分哑坐标|m
25|\theta|polar angle, $0\le\theta\le\pi$|极角，$0\le\theta\le\pi$|1
25|\psi|azimuthal angle, $0\le\psi\le2\pi$|方位角，$0\le\psi\le2\pi$|1
26|\boldsymbol T|Cauchy stress tensor|柯西应力张量|Pa
26|\boldsymbol I|identity tensor|单位张量|1
26|D/Dt|material time derivative|物质时间导数|s⁻¹
26|\partial_t|time derivative at fixed position|固定位置的时间导数|s⁻¹
26|\nabla|spatial gradient operator|空间梯度算子|m⁻¹
26|\nabla\cdot|spatial divergence operator|空间散度算子|m⁻¹
26|\nabla^2|spatial Laplacian operator|空间拉普拉斯算子|m⁻²
27|F|smooth dimensionless level set increasing into gas|向气体侧增加的光滑无量纲水平集|1
27|\boldsymbol x|position|位置|m
27|t|time|时间|s
27|\boldsymbol T_g|gas stress, $-p_b\boldsymbol I$|气体应力，$-p_b\boldsymbol I$|Pa
27|\boldsymbol T_l|liquid stress, $-p_l\boldsymbol I+2\mu\boldsymbol D$|液体应力，$-p_l\boldsymbol I+2\mu\boldsymbol D$|Pa
27|\boldsymbol I|identity tensor|单位张量|1
27|\nabla|spatial gradient operator|空间梯度算子|m⁻¹
27|\nabla_s\cdot|surface divergence operator|表面散度算子|m⁻¹
27|\partial_t|time derivative at fixed position|固定位置的时间导数|s⁻¹
28|p_l|liquid-side interface pressure|界面液体侧压力|Pa
28|\nabla|spatial gradient operator|空间梯度算子|m⁻¹
28|\nabla^2|spatial Laplacian operator|空间拉普拉斯算子|m⁻²
28|D/Dt|material time derivative|物质时间导数|s⁻¹
28|\partial_t|time derivative at fixed position|固定位置的时间导数|s⁻¹
29|t|time|时间|s
30|\rho_0|positive uniform background density|均匀背景正密度|kg m⁻³
30|\rho'|small acoustic density perturbation|小幅声学密度扰动|kg m⁻³
30|p'|small acoustic pressure perturbation|小幅声学压力扰动|Pa
30|\boldsymbol u'|small acoustic velocity perturbation|小幅声学速度扰动|m s⁻¹
30|\nabla\cdot|spatial divergence operator|空间散度算子|m⁻¹
30|\nabla^2|spatial Laplacian operator|空间拉普拉斯算子|m⁻²
30|\partial_t|time derivative at fixed position|固定位置的时间导数|s⁻¹
30|t|time|时间|s
30|t_a|one-way acoustic travel time|单程声传播时间|s
31|p_l|liquid-side wall pressure|壁面液体侧压力|Pa
32|y|squared wall speed|壁面速度平方|m² s⁻²
32|x|normalized radius, $R/R_{\max}$|无量纲半径，$R/R_{\max}$|1
32|V_b|cavity volume, $4\pi R^3/3$|空腔体积，$4\pi R^3/3$|m³
32|V_{\max}|maximum volume, $4\pi R_{\max}^3/3$|最大体积，$4\pi R_{\max}^3/3$|m³
32|V|dummy volume variable|积分哑体积变量|m³
33|\boldsymbol u|liquid velocity|液体速度|m s⁻¹
33|\nu|kinematic viscosity|运动黏度|m² s⁻¹
33|U|characteristic speed|特征速度|m s⁻¹
33|\tau|event duration, $t_1-t_0$|事件时长，$t_1-t_0$|s
33|z|column coordinate, $0\le z\le L$|液柱坐标，$0\le z\le L$|m
33|\Delta u_z|axial speed increment|轴向速度增量|m s⁻¹
33|\nabla|spatial gradient operator|空间梯度算子|m⁻¹
33|\nabla\cdot|spatial divergence operator|空间散度算子|m⁻¹
33|\nabla^2|spatial Laplacian operator|空间拉普拉斯算子|m⁻²
'''

NOTES = {
 1: ('All pressures share an absolute reference', '全部压力采用同一绝对参考值'),
 2: (r'The fixed shell stays liquid; $r\ge R(t)>0$', r'固定球壳始终属于液体；$r\ge R(t)>0$'),
 5: (r'Zero vorticity gives $\partial_j u_i=\partial_i u_j$; smooth fields permit derivative exchange; $|\ |$ denotes Euclidean magnitude; $\infty$ denotes the far-field limit', r'无旋条件给出 $\partial_j u_i=\partial_i u_j$；光滑场允许交换导数；$|\ |$ 表示欧氏模长；$\infty$ 表示远场极限'),
 6: ('Extend the unit normal radially without radial variation; its normal derivative vanishes, so surface and volume divergences agree at the sphere', '将单位法向沿径向作不变延拓；其法向导数为零，因此表面散度与体散度在球面一致'),
 19: (r'Teaching inputs use the preceding density and pressure, with $c=1500$ m s⁻¹ and chosen $M_*=0.1$', r'教学输入采用前述密度和压差，并取 $c=1500$ m s⁻¹、选定 $M_*=0.1$'),
 20: ('Brackets denote units; fixed-surface reduction requires fixed orientation and all sampled points remaining liquid', '方括号表示单位；固定表面约化要求方向固定且全部采样点始终位于液体中'),
 22: (r'$\sim$ denotes a scale estimate, rather than an equality or rigorous error bound', r'$\sim$ 表示尺度估计，并非等式或严格误差界'),
 23: ('The uniform-speed column is an inviscid core benchmark; no-slip wall layers are omitted', '匀速液柱是无黏核心流基准；省略无滑移壁面层'),
 25: ('Angles are dimensionless radians; tuple entries are Cartesian vector components', '角度以无量纲弧度计；有序三元组为笛卡尔矢量分量'),
 26: (r'Superscript $\mathsf T$ denotes transpose; body forces are omitted; the density derivative is displayed before imposing constant density', r'上标 $\mathsf T$ 表示转置；忽略体力；密度导数写在施加常密度条件之前'),
 27: ('The level-set gradient is nonzero on the interface', '水平集在界面上的梯度非零'),
 28: (r'Interface markers $\boldsymbol X(t)$ follow liquid particles; $D\phi/Dt$ has units m² s⁻²; assume single-valued potential and a smooth pre-impact interface', r'界面标记点 $\boldsymbol X(t)$ 随液体质点运动；$D\phi/Dt$ 单位为 m² s⁻²；假设速度势单值且撞击前界面光滑'),
 29: (r'$d/dt$ follows the spherical interface', r'$d/dt$ 跟随球形界面'),
 30: (r'Primes denote small acoustic perturbations; ns is 10⁻⁹ s; linearization assumes inviscid barotropic liquid and constant $c$', r'撇号标记小幅声学扰动；ns 为 10⁻⁹ s；线性化假设液体无黏、正压且声速恒定'),
 33: (r'$\ll$ denotes an asymptotic smallness condition', r'$\ll$ 表示渐近很小条件'),
}

def main():
    path=ROOT/'content/equation_symbol_rows.json'
    data=json.loads(path.read_text(encoding='utf-8'))
    before={k:v for k,v in data.items() if not k.startswith('C1-')}
    added=0
    for line in ROWS.strip().splitlines():
        number,symbol,en,zh,unit=line.split('|')
        entry=data[f'C1-E{number}']
        old=next((r for r in entry['rows'] if r['symbol']==symbol),None)
        row={'symbol':symbol,'en':f'${symbol}$ — {en} ({unit})',
                             'zh':f'${symbol}$ — {zh}（{unit}）','unit':unit,
                             'source':'chapter01 derivation declarations, merged 2026-10-19'}
        if old is None:
            entry['rows'].append(row)
            added+=1
        elif old.get('source')==row['source']:
            old.update(row)
    for number,(en,zh) in NOTES.items():
        entry=data[f'C1-E{number:02d}']
        for lang,value in [('en',en),('zh',zh)]:
            if value not in entry[f'notes_{lang}']:entry[f'notes_{lang}'].append(value)
    # Operator definitions now have their own individual compact cells.
    entry=data['C1-E21']
    entry['notes_en']=[x for x in entry['notes_en'] if not x.startswith('$\\nabla$ is spatial gradient')]
    entry['notes_zh']=[x for x in entry['notes_zh'] if not x.startswith('$\\nabla$ 为空间梯度')]
    assert before=={k:v for k,v in data.items() if not k.startswith('C1-')}
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'added_individual_definitions':added,'non_chapter01_definitions_preserved':len(before)}))

if __name__=='__main__':main()
