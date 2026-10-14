"""Chinese labels for the four accepted SVG plots; curves stay unchanged."""
from pathlib import Path
from bs4 import BeautifulSoup

LABELS = {
 'Initial liquid droplet diameter (µm)': '初始液滴直径 (µm)',
 'Equilibrium temperature (K)': '平衡温度 (K)',
 'Equilibrium state energy (pJ)': '平衡状态能量 (pJ)',
 'Finite PFC: equal stretch 2.1, G = 20 kPa, stipulated outer tension 54 mN/m': '有限 PFC：伸长比 2.1；G = 20 kPa；外张力 54 mN/m',
 'State budgets and temperatures; not activation thresholds': '状态能量与温度；激活阈值未确立',
 'Time after prescribed seed (µs)': '种子后时间 (µs)',
 'Radial wall speed (m/s)': '径向壁速 (m/s)',
 'Initial diameter 0.6 µm': '初始直径 0.6 µm',
 'Initial diameter 6 µm': '初始直径 6 µm',
 'Outer-radius stretch': '外半径伸长比',
 'Conditional insulated expansion; no outlet and no jet': '有条件绝热膨胀；无出口与射流',
 'Equal retained seed energy within each size; 2.1 is a declared stopping screen': '同尺寸保留能量相同；2.1 为预设停止值',
 'Initial radius (µm)': '初始半径 (µm)',
 'Closed-energy restoring slope (kPa per stretch)': '闭能量恢复斜率 (kPa／单位伸长比)',
 'Local reduced radial stability: positive restores, negative destabilizes': '局部径向稳定性：正值恢复，负值失稳',
 'Internal phase/core stability is a separate fixed-(T,V,m) check': '内部相态／核稳定性另作固定 (T,V,m) 检验',
 'Stipulated fracture energy (J/m²)': '预设断裂能 (J/m²)',
 'Retained seed energy / slit work': '种子保留能量／狭缝功',
 'Diameter 0.6 µm; half-width 0.5 µm': '直径 0.6 µm；半宽 0.5 µm',
 'Diameter 6 µm; half-width 0.5 µm': '直径 6 µm；半宽 0.5 µm',
 'Cover 1 µm': '覆盖 1 µm',
 'Cover 1 µm *': '覆盖 1 µm *',
 'Cover 5 µm': '覆盖 5 µm',
 'Cover 20 µm': '覆盖 20 µm',
 'Cover 50 µm': '覆盖 50 µm',
 'Slit work comparison only: other energy changes and crack coupling omitted': '假定狭缝功比较；省略其他能量变化与裂纹耦合',
 '* Infinite-host trajectory intersects the initial free-surface plane': '* 无限基质轨迹与初始自由表面平面相交',
}

def translate_figures(root):
    records={}
    for name in ['size_species_comparison','radial_viscosity_controls','radial_stability','fracture_budget']:
        source=root/'assets'/f'{name}.svg'
        soup=BeautifulSoup(source.read_text(encoding='utf8'),'xml')
        changed=0
        for text in soup.select('text'):
            label=text.get_text()
            if label not in LABELS:
                # Numeric ticks, species identifiers and parameter formulae
                # are language-independent. Every prose label must be known.
                if any(word in label for word in ['Time','Initial','State','Cover','energy','stretch','speed','radius','temperature','Conditional','Local','Internal','Finite','work','tension']):
                    raise ValueError(f'Untranslated SVG label: {source.name}: {label}')
                continue
            text.clear();text.string=LABELS[label]
            style=text.get('style','')
            style=style.replace("'DejaVu Sans'", "'Microsoft YaHei', 'Noto Sans CJK SC', sans-serif")
            text['style']=style
            changed+=1
        (root/'assets'/f'{name}.zh.svg').write_text(str(soup),encoding='utf8')
        records[name]=changed
    return records
