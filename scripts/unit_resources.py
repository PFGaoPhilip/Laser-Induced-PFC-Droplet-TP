"""Teaching resources placed within their owning course units."""
from coursekit import H, P, T


RESOURCES = {
    3: [('resolver-work', 'Three-stage resolver', '三阶段求解器',
         'learning-records/resolver-progress/index.html')],
    5: [('finite-energy-models', 'Finite-energy cavitation models', '有限能量空化模型',
         'modeling/minimal-cavitation/index.html'),
        ('embedded-pfc-study', 'PFC droplets in hydrogel', '水凝胶中的 PFC 液滴',
         'modeling/embedded-pfc-feasibility/index.html')],
}


def resource_links(number, prefix=''):
    items = RESOURCES.get(number, [])
    if not items:
        return ''
    return '<ul class="unit-resources">' + ''.join(
        '<li>' + P(f'<a href="{prefix}{path}">{en}</a>',
                   f'<a href="{prefix}{path}?lang=zh">{zh}</a>') + '</li>'
        for _, en, zh, path in items) + '</ul>'


def resource_sections(number):
    if number == 3:
        return ('<section class="unit-study" data-course-resource="resolver">'
                + H('Three-stage resolver', '三阶段求解器', 'resolver-work')
                + P('Apply the chapter’s balances to a finite-volume solver. '
                    'The worked lesson covers equations, code, output readers, and checks.',
                    '将本章平衡方程用于有限体积求解器。示例课程包括方程、代码、输出读取与核验。')
                + T([('Stage', '阶段'), ('Recorded outcome', '记录结果')], [
                    [('Stage 1: model and solver', '阶段一：模型与求解器'),
                     ('CLOSED_LOOSENED: accepted with recorded waivers.',
                      'CLOSED_LOOSENED：按记录的豁免接受关闭。')],
                    [('Stage 2: calculation campaign', '阶段二：计算任务'),
                     ('STAGE2_LOOSENED_CLOSED: accepted with recorded waivers.',
                      'STAGE2_LOOSENED_CLOSED：按记录的豁免接受关闭。')],
                    [('Stage 3: engineering report', '阶段三：工程报告'),
                     ('Reporting, independent arithmetic, and delivery are complete.',
                      '报告、独立算术核验与交付已完成。')]])
                + P('Maximum: Not established. Missing: 18 attained objectives and certificates.',
                    '最大值：尚未建立。缺少：18 项已达到的目标及证书。')
                + resource_links(number, '../') + '</section>')
    if number == 5:
        return ('<section class="unit-study" data-course-resource="minimal">'
                + H('Finite-energy cavitation models', '有限能量空化模型',
                    'finite-energy-models')
                + P('Compare an existing outlet in rigid and gel-confined cavities. '
                    'At 2 nJ source work and a 5 μm outlet radius, '
                    'peak speeds are 15.376 and 1.625 m/s. '
                    'The sealed control emits zero liquid.',
                    '比较刚性腔体与凝胶约束腔体中的已有出口。'
                    '源功为 2 nJ，出口半径为 5 μm 时，'
                    '峰值速度分别为 15.376 与 1.625 m/s。密闭对照排液量为零。')
                + P('These initialized ideal-gas controls describe expansion through an existing channel. '
                    'Laser activation, PFC phase change, rupture, collapse jets, and impact remain outside their scope.',
                    '这些给定初态的理想气体对照描述经已有通道的膨胀排液。'
                    '激光激活、PFC 相变、破裂、塌缩射流与冲击不在其范围内。')
                + P('<a href="../modeling/minimal-cavitation/index.html">Read the model derivation</a> · '
                    '<a href="../modeling/minimal-cavitation/STEP_BY_STEP.html">53-step COMSOL guide</a>',
                    '<a href="../modeling/minimal-cavitation/index.html?lang=zh">阅读模型推导</a> · '
                    '<a href="../modeling/minimal-cavitation/STEP_BY_STEP.html?lang=zh">53 步 COMSOL 指南</a>')
                + P('<a href="../modeling/minimal-cavitation/Minimal_Cavitation_Models_20261010.zip">Download model files</a>',
                    '<a href="../modeling/minimal-cavitation/Minimal_Cavitation_Models_20261010.zip">下载模型文件</a>')
                + '</section><section class="unit-study" data-course-resource="embedded">'
                + H('PFC droplets in hydrogel', '水凝胶中的 PFC 液滴',
                    'embedded-pfc-study')
                + P('Compare PFP and PFH across droplet size, gel modulus, and viscosity. '
                    'The model retains finite PFC mass and a liquid shell. '
                    'Sixty stationary and six seeded transient comparisons pass.',
                    '按液滴尺寸、凝胶模量与黏度比较 PFP 和 PFH。'
                    '模型保留有限 PFC 质量与液体壳层。'
                    '60 项稳态及 6 项预设种子瞬态对照通过。')
                + P('Reported velocities are radial wall speeds. Exterior emission is zero. '
                    'Target activation, rupture, collapse jets, and impact pressure remain unvalidated.',
                    '报告速度为径向壁面速度。外部排出量为零。'
                    '目标系统的激活、破裂、塌缩射流与冲击压力仍未验证。')
                + P('<a href="../modeling/embedded-pfc-feasibility/index.html">Read the bilingual study and parameter comparison</a>',
                    '<a href="../modeling/embedded-pfc-feasibility/index.html?lang=zh">阅读双语研究与参数比较</a>')
                + P('<a href="../modeling/embedded-pfc-feasibility/Embedded_PFC_Feasibility_Public_20261011.zip">Download study files</a>',
                    '<a href="../modeling/embedded-pfc-feasibility/Embedded_PFC_Feasibility_Public_20261011.zip">下载研究文件</a>')
                + '</section>')
    return ''
