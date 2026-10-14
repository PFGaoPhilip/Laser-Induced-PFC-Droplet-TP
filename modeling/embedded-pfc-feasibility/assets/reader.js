(() => {
  'use strict';
  const root = document.documentElement;
  const theme = document.getElementById('theme-toggle');
  const language = document.getElementById('language-toggle');
  const names = ['comparison', 'derivation', 'handoff', 'sources'];
  const read = (key, fallback) => {
    try { return localStorage.getItem(key) || fallback; } catch (_) { return fallback; }
  };
  const save = (key, value) => {
    try { localStorage.setItem(key, value); } catch (_) {}
  };
  const pair = (en, zh, chineseClass = true) => '<span lang="en">' + en + '</span><span lang="zh-CN"' + (chineseClass ? ' class="zh"' : '') + '>' + zh + '</span>';
  const returnLink = document.getElementById('appendix-return');
  if (/\/modeling\/embedded-pfc-feasibility\/index\.html$/i.test(location.pathname)) {
    document.querySelectorAll('[data-course-path]').forEach(a => {
      a.setAttribute('href', '../../' + a.dataset.coursePath);
    });
  }

  function syncLinks() {
    document.querySelectorAll('a[href]').forEach(a => {
      const href = a.getAttribute('href');
      if (!href || href.startsWith('#') || !/\.html(?:[?#]|$)/i.test(href)) return;
      if (/^[a-z]+:/i.test(href) && a !== returnLink && !a.dataset.coursePath) return;
      const parts = href.split('#');
      const query = new URLSearchParams((parts[0].split('?')[1]) || '');
      const mode = root.dataset.language || 'bilingual';
      query.set('lang', a === returnLink || a.dataset.coursePath ? (mode === 'zh' ? 'zh' : 'en') : mode);
      query.set('theme', root.dataset.theme === 'dark' ? 'dark' : 'light');
      a.setAttribute('href', parts[0].split('?')[0] + '?' + query.toString() + (parts[1] ? '#' + parts[1] : ''));
    });
  }

  function setTheme(value) {
    const isNight = value === 'night' || value === 'dark';
    root.dataset.theme = isNight ? 'dark' : 'light';
    theme.innerHTML = pair(isNight ? 'Day mode' : 'Night mode', isNight ? '日间模式' : '夜间模式', false);
    theme.setAttribute('aria-pressed', String(!isNight));
    save('pfc-theme', isNight ? 'night' : 'day');
    save('laser-pfc-tp-theme', isNight ? 'dark' : 'light');
    syncLinks();
  }
  function setLanguage(value) {
    const mode = ['en', 'zh', 'bilingual'].includes(value) ? value : 'bilingual';
    root.dataset.language = mode;
    root.lang = mode === 'zh' ? 'zh-CN' : 'en';
    const next = mode === 'bilingual' ? 'en' : mode === 'en' ? 'zh' : 'bilingual';
    language.dataset.nextLanguage = next;
    language.textContent = next === 'en' ? 'English' : next === 'zh' ? '中文' : 'English + 中文';
    language.setAttribute('aria-label', next === 'zh' ? 'Switch to Chinese' : next === 'en' ? 'Switch to English' : '切换至双语阅读');
    save('embedded-pfc-language', mode);
    if (mode !== 'bilingual') save('laser-pfc-tp-language', mode);
    syncLinks();
  }
  const parameters = new URLSearchParams(location.search);
  const requestedLanguage = parameters.get('lang');
  setLanguage(requestedLanguage || read('embedded-pfc-language', 'bilingual'));
  setTheme(parameters.get('theme') || read('laser-pfc-tp-theme', read('pfc-theme', 'dark')));
  language.addEventListener('click', () => setLanguage(language.dataset.nextLanguage));
  theme.addEventListener('click', () => {
    setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
  });

  function show(name) {
    if (!names.includes(name)) return;
    document.querySelectorAll('.document').forEach(x => { x.hidden = x.id !== name; });
    document.querySelectorAll('[data-doc]').forEach(x => x.setAttribute('aria-pressed', String(x.dataset.doc === name)));
    document.getElementById('selector').hidden = name !== 'comparison';
  }
  document.querySelectorAll('[data-doc]').forEach(x => x.addEventListener('click', () => {
    show(x.dataset.doc);
    history.replaceState(null, '', '#' + x.dataset.doc);
    window.scrollTo({ top: 0, behavior: 'auto' });
  }));
  document.querySelectorAll('a[href^="#"]').forEach(x => x.addEventListener('click', () => show(x.getAttribute('href').slice(1))));
  window.addEventListener('hashchange', () => show(location.hash.slice(1)));
  show(location.hash.slice(1) || 'comparison');

  const data = JSON.parse(document.getElementById('state-data').textContent);
  function update() {
    const fluid = document.getElementById('fluid').value;
    const diameter = Number(document.getElementById('diameter').value);
    const modulus = Number(document.getElementById('modulus').value);
    const state = data.find(x => x.fluid === fluid && Math.abs(x.diameter_um - diameter) < 1e-6 && x.G_kPa === modulus);
    if (!state) throw new Error('Missing solved state');
    const energy = state.Q_pJ >= 1000 ? (state.Q_pJ / 1000).toFixed(3) + ' nJ' : state.Q_pJ.toFixed(2) + ' pJ';
    const card = (title, titleZh, value, note, noteZh) => '<div class="state-card">' + pair(title, titleZh) +
      '<strong>' + value + '</strong>' + pair(note, noteZh) + '</div>';
    document.getElementById('state-output').innerHTML =
      card('State temperature', '状态温度', state.T_K.toFixed(2) + ' K', 'Curved equilibrium', '曲面平衡') +
      card('State energy', '状态能量', energy, 'All-liquid reference', '全液态参考') +
      card('Vapor mass fraction', '蒸气质量分数', (100 * state.vapor_fraction).toFixed(2) + '%', 'Surviving liquid shell', '剩余液体壳层') +
      card('Elastic resistance', '弹性阻力', state.pEl_kPa.toFixed(3) + ' kPa', 'Stipulated intact gel', '预设完整凝胶');
  }
  ['fluid', 'diameter', 'modulus'].forEach(id => document.getElementById(id).addEventListener('change', update));
  update();
})();
