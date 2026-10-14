/* DOM interaction checks. This does not launch or render a browser. */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const project = path.resolve(__dirname, '..');
const root = process.argv[2] ? path.resolve(process.argv[2]) : project;
const {JSDOM, VirtualConsole} = require(path.join(project, 'build/dom-test/node_modules/jsdom'));
const version = require(path.join(project, 'build/dom-test/node_modules/jsdom/package.json')).version;
const checks = [];
const languageKey = 'laser-pfc-tp-language';
const themeKey = 'laser-pfc-tp-theme';
const progressKey = 'minimal-cavitation-guide-progress-v1';
function check(name, action) { action(); checks.push(name); }
function load(file, options = {}) {
  const errors = [], scrolling = [], copied = [];
  const virtualConsole = new VirtualConsole();
  virtualConsole.on('jsdomError', error => errors.push(String(error)));
  const dom = new JSDOM(fs.readFileSync(path.join(root, file), 'utf8'), {
    url: 'https://reader.test/' + (options.urlPath || file) + (options.query || '') + (options.hash || ''),
    runScripts: 'outside-only', pretendToBeVisual: true, virtualConsole
  });
  const w = dom.window;
  // Layout/clipboard are controlled stubs; all DOM and application code are real.
  w.scrollTo = value => scrolling.push(value);
  w.HTMLElement.prototype.scrollIntoView = function () { scrolling.push({anchor: this.id}); };
  Object.defineProperty(w.HTMLElement.prototype, 'innerText', {get() {return this.textContent;}});
  Object.defineProperty(w.navigator, 'clipboard', {value: {writeText: async text => copied.push(text)}});
  if (options.blockedStorage) {
    Object.defineProperty(w, 'localStorage', {get() {throw new Error('Storage disabled for test');}});
  } else {
    for (const [key, value] of Object.entries(options.storage || {})) w.localStorage.setItem(key, value);
  }
  w.eval(fs.readFileSync(path.join(root, 'assets/theme.js'), 'utf8'));
  if (file === 'STEP_BY_STEP.html') w.eval(fs.readFileSync(path.join(root, 'assets/guide.js'), 'utf8'));
  return {dom, w, d: w.document, errors, scrolling, copied};
}
function active(t, language) {
  const visible = Array.from(t.d.querySelectorAll('.locale-pane')).filter(p => !p.hidden);
  assert.equal(visible.length, 1);
  assert.equal(visible[0].dataset.locale, language);
  assert.equal(t.d.documentElement.lang, language === 'zh' ? 'zh-CN' : 'en');
}
function progress(t, number) {
  assert.equal(t.d.querySelector('[data-locale="zh"] [data-guide-progress]').textContent, `已完成 ${number} / 53 步`);
  assert.equal(t.d.querySelector('[data-locale="en"] [data-guide-progress]').textContent, `${number} of 53 steps completed`);
  for (const bar of t.d.querySelectorAll('progress')) assert.equal(bar.value, number);
}
function complete(t, language, step) {
  const input = t.d.querySelector(`[data-locale="${language}"] input[data-step="${step}"]`);
  input.checked = true;
  input.dispatchEvent(new t.w.Event('change', {bubbles: true}));
  for (const twin of t.d.querySelectorAll(`input[data-step="${step}"]`)) {
    assert(twin.checked); assert(twin.closest('.guide-step').classList.contains('step-done'));
  }
}
async function main() {
  const defaults = load('STEP_BY_STEP.html');
  check('English default with one complete visible edition', () => {
    active(defaults, 'en'); progress(defaults, 0);
    assert.equal(defaults.d.getElementById('language-toggle').textContent, '中文');
  });
  const guide = load('STEP_BY_STEP.html', {storage: {[languageKey]: 'zh'}});
  check('Selected Chinese edition with canonical controls', () => {
    active(guide, 'zh'); progress(guide, 0);
    assert.equal(guide.d.getElementById('language-toggle').textContent, 'English');
    assert.equal(guide.d.getElementById('theme-toggle').textContent, '日间模式');
    assert.deepEqual(Array.from(guide.d.querySelectorAll('.theme-tools button'), b => b.id), ['theme-toggle', 'language-toggle']);
    assert.equal(guide.d.querySelector('[data-locale="zh"] .copy-block').textContent, '复制文本');
  });
  check('Theme switches and its labels follow the selected language', () => {
    guide.d.getElementById('theme-toggle').click();
    assert.equal(guide.d.documentElement.dataset.theme, 'light');
    assert.equal(guide.d.getElementById('theme-toggle').textContent, '夜间模式');
    assert.equal(guide.w.localStorage.getItem(themeKey), 'light');
  });
  check('Completion in Chinese is synchronized without doubling the 53-step count', () => {
    complete(guide, 'zh', '1'); progress(guide, 1);
    guide.d.getElementById('language-toggle').click(); active(guide, 'en');
    assert.equal(guide.d.getElementById('language-toggle').textContent, '中文');
    assert.equal(guide.d.getElementById('theme-toggle').textContent, 'Night mode');
    complete(guide, 'en', '32'); progress(guide, 2);
  });
  check('Reading position is mapped to the corresponding step when switching', () => {
    for (const node of guide.d.querySelectorAll('[data-anchor]')) {
      node.getBoundingClientRect = () => ({top: 1000, bottom: 1001});
    }
    guide.d.getElementById('en-step-32').getBoundingClientRect = () => ({top: 80, bottom: 400});
    guide.d.getElementById('zh-step-32').getBoundingClientRect = () => ({top: 105, bottom: 425});
    Object.defineProperty(guide.w, 'scrollY', {value: 700});
    guide.d.getElementById('language-toggle').click(); active(guide, 'zh');
    assert.equal(guide.scrolling.at(-1).top, 725);
  });
  const storage = Object.fromEntries([languageKey, themeKey, progressKey].map(k => [k, guide.w.localStorage.getItem(k)]));
  const reloaded = load('STEP_BY_STEP.html', {storage});
  const report = load('index.html', {storage});
  check('Language, theme and step completion persist across reload and both readers', () => {
    active(reloaded, 'zh'); active(report, 'zh'); progress(reloaded, 2);
    assert.equal(report.d.documentElement.dataset.theme, 'light');
    for (const step of ['1', '32']) assert(reloaded.d.querySelector(`input[data-step="${step}"]`).checked);
    reloaded.d.getElementById('language-toggle').click(); active(reloaded, 'en');
    const englishReport = load('index.html', {storage: {[languageKey]: 'en', [themeKey]: 'light'}});
    active(englishReport, 'en'); assert.equal(englishReport.d.getElementById('theme-toggle').textContent, 'Night mode');
    assert.equal(englishReport.errors.length, 0); englishReport.dom.window.close();
  });
  check('Reset clears both editions and saved progress', () => {
    reloaded.d.querySelector('[data-locale="en"] [data-reset-progress]').click(); progress(reloaded, 0);
    assert.equal(reloaded.d.querySelectorAll('input:checked').length, 0);
    assert.equal(reloaded.w.localStorage.getItem(progressKey), '[]');
  });
  const codeButton = guide.d.querySelector('[data-locale="zh"] .copy-block');
  codeButton.click(); await new Promise(resolve => setTimeout(resolve, 0));
  check('Copy preserves the input block and provides Chinese feedback', () => {
    assert.equal(guide.copied.at(-1), codeButton.nextElementSibling.textContent);
    assert.equal(codeButton.textContent, '已复制');
  });
  guide.w.navigator.clipboard.writeText = async () => {throw new Error('Clipboard blocked for test');};
  codeButton.click(); await new Promise(resolve => setTimeout(resolve, 0));
  check('Clipboard rejection selects the original input text for manual copying', () => {
    assert.equal(guide.w.getSelection().toString(), codeButton.nextElementSibling.textContent);
    assert.equal(codeButton.textContent, '已选中文本，请按 Ctrl+C');
  });
  const linked = load('index.html', {hash: '#en-theory', storage: {[languageKey]: 'zh'}});
  check('Deep links map to the current edition and disclosure remains open after switching', () => {
    active(linked, 'zh'); assert(linked.d.getElementById('zh-theory').open);
    assert.equal(linked.w.location.hash, '#zh-theory');
    linked.d.getElementById('language-toggle').click(); active(linked, 'en');
    assert(linked.d.getElementById('en-theory').open);
    assert.equal(linked.w.location.hash, '#en-theory');
    assert(linked.d.title.includes('Minimal cavitation'));
    linked.d.getElementById('en-theory').open = false;
    linked.d.getElementById('language-toggle').click(); assert(!linked.d.getElementById('zh-theory').open);
  });
  const noStorage = load('STEP_BY_STEP.html', {blockedStorage: true});
  const corruptStorage = load('STEP_BY_STEP.html', {storage: {[progressKey]: '{broken'}});
  check('Disabled or malformed storage does not prevent switching or progress', () => {
    active(noStorage, 'en'); noStorage.d.getElementById('language-toggle').click(); active(noStorage, 'zh');
    complete(noStorage, 'zh', '2'); progress(noStorage, 1); progress(corruptStorage, 0);
  });
  check('Canonical frontend and one lower-right reading group are present', () => {
    for (const page of [guide, report]) {
      assert.equal(page.d.querySelectorAll('.theme-tools').length, 1);
      assert(page.d.querySelector('link[href="assets/course.css"]'));
      assert(page.d.querySelector('.topbar'));
      const pane=page.d.querySelector('[data-locale="en"]');
      for (const selector of ['.page-layout','.sidebar','.reading','.chapter-header h1','.chapter-body']) assert(pane.querySelector(selector));
    }
    const css = fs.readFileSync(path.join(root, 'assets/course.css'), 'utf8');
    assert(/\.theme-tools\s*\{[^}]*position\s*:\s*fixed/s.test(css));
    assert(/right\s*:\s*1\.2rem/.test(css));
    assert(/bottom\s*:\s*1\.2rem/.test(css));
  });
  const course = load('index.html', {urlPath: 'modeling/minimal-cavitation/index.html'});
  check('Course paths return to local Appendix A', () => {
    assert.equal(course.d.querySelector('[data-course-return]').getAttribute('href'), '../../appendices/a-hydrogel-versus-liquid.html?lang=en&theme=dark');
  });
  const queried = load('index.html', {query: '?lang=zh&theme=dark', storage: {[themeKey]: 'light'}});
  check('Explicit language and dark theme override stored light theme', () => {
    active(queried, 'zh');
    assert.equal(queried.d.documentElement.dataset.theme, 'dark');
  });
  check('Standalone paths retain optional published Appendix A', () => {
    assert(defaults.d.querySelector('[data-course-return]').href.startsWith('https://pfgaophilip.github.io/'));
  });
  const all = [defaults, guide, reloaded, report, linked, noStorage, corruptStorage, course, queried];
  check('No application JavaScript errors occurred in the tested DOM scenarios', () => {
    for (const item of all) assert.deepEqual(item.errors, []);
  });
  const audit = {
    status: 'PASS', engine: 'JSDOM ' + version, checks,
    scope: 'DOM interaction tests of delivered HTML and JS; layout, scrolling and clipboard have explicit stubs.',
    browser_visual_validation: 'Not performed by this DOM test. Real-browser verification is recorded separately by the course revision.',
    figures: 'This DOM audit makes no figure-rendering or screenshot claim.'
  };
  fs.writeFileSync(path.join(root, 'verification/READER_DOM_AUDIT.json'), JSON.stringify(audit, null, 2) + '\n');
  for (const item of all) item.dom.window.close();
  console.log(JSON.stringify(audit, null, 2));
}
main().catch(error => {console.error(error); process.exitCode = 1;});
