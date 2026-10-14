// DOM-event regression. Rendering evidence lives in READER_REVISION_AUDIT.json.
const fs = require('fs'), path = require('path'), vm = require('vm'), assert = require('assert');
const { URLSearchParams } = require('url');
const root = path.resolve(__dirname, '..');
const states = JSON.parse(fs.readFileSync(path.join(root, 'data', 'reader_states.json'), 'utf8'));
const script = fs.readFileSync(path.join(root, 'assets', 'reader.js'), 'utf8');
const docNames = ['comparison', 'derivation', 'handoff', 'sources'];
const canonical = 'https://pfgaophilip.github.io/Laser-Induced-PFC-Droplet-TP/appendices/a-hydrogel-versus-liquid.html';

class Element {
  constructor(id) {
    Object.assign(this, { id, handlers: {}, attributes: {}, dataset: {}, hidden: false, value: '', textContent: '', innerHTML: '' });
  }
  addEventListener(name, callback) { this.handlers[name] = callback; }
  setAttribute(name, value) { this.attributes[name] = String(value); }
  getAttribute(name) { return this.attributes[name] || null; }
  dispatch(name) { assert(this.handlers[name], 'Missing event handler: ' + this.id + '/' + name); this.handlers[name](); }
}

function fixture(options = {}) {
  const ids = ['theme-toggle', 'language-toggle', 'appendix-return', 'selector', 'fluid', 'diameter', 'modulus', 'state-output', 'state-data', ...docNames];
  const el = Object.fromEntries(ids.map(id => [id, new Element(id)]));
  el['state-data'].textContent = JSON.stringify(states);
  el.fluid.value = 'n-Perfluoropentane'; el.diameter.value = '0.6'; el.modulus.value = '20';
  el['appendix-return'].setAttribute('href', canonical);
  el['appendix-return'].dataset.coursePath = 'appendices/a-hydrogel-versus-liquid.html';
  const docs = docNames.map(id => el[id]);
  const buttons = docs.map(d => { const e = new Element(d.id + '-button'); e.dataset.doc = d.id; return e; });
  const links = docs.map(d => { const e = new Element(d.id + '-link'); e.setAttribute('href', '#' + d.id); return e; });
  const readerLink = new Element('reader-link'); readerLink.setAttribute('href', 'index.html?keep=1#derivation');
  const external = new Element('external-reference'); external.setAttribute('href', 'https://example.org/source.html');
  const markdown = new Element('markdown-source'); markdown.setAttribute('href', 'REPORT.md');
  const allLinks = [...links, el['appendix-return'], readerLink, external, markdown];
  const document = {
    documentElement: { dataset: {}, lang: 'en' },
    getElementById: id => el[id],
    querySelectorAll: q => {
      if (q === '.document') return docs;
      if (q === '[data-doc]') return buttons;
      if (q === 'a[href]') return allLinks;
      if (q === '[data-course-path]') return allLinks.filter(a => a.dataset.coursePath);
      if (q === 'a[href^="#"]') return links;
      throw new Error('Unimplemented selector: ' + q);
    }
  };
  const store = { ...(options.store || {}) }, windowEvents = {}, scrollCalls = [];
  const location = { pathname: options.pathname || '/course/modeling/embedded-pfc-feasibility/index.html', search: options.search || '', hash: options.hash || '' };
  const context = {
    document, URLSearchParams, location, console,
    localStorage: {
      getItem: key => { if (options.storageUnavailable) throw new Error('Storage unavailable'); return store[key] || null; },
      setItem: (key, value) => { if (options.storageUnavailable) throw new Error('Storage unavailable'); store[key] = String(value); }
    },
    history: { replaceState: (_, __, url) => { location.hash = url.slice(url.indexOf('#')); } },
    window: { addEventListener: (name, callback) => { windowEvents[name] = callback; }, scrollTo: value => scrollCalls.push(value) }
  };
  vm.runInNewContext(script, context);
  return { el, docs, buttons, links, readerLink, external, markdown, document, store, location, windowEvents, scrollCalls };
}

const f = fixture({ store: { 'laser-pfc-tp-theme': 'light' } });
assert.strictEqual(f.el['theme-toggle'].getAttribute('aria-pressed'), 'true');
let originalScenarios = 0, interfaceScenarios = 0;
assert(f.el['state-output'].innerHTML.includes('339.79 K')); originalScenarios++;
for (const s of states) {
  f.el.fluid.value = s.fluid; f.el.diameter.value = String(s.diameter_um); f.el.modulus.value = String(s.G_kPa); f.el.fluid.dispatch('change');
  assert(f.el['state-output'].innerHTML.includes(s.T_K.toFixed(2) + ' K'));
  assert(f.el['state-output'].innerHTML.includes((100 * s.vapor_fraction).toFixed(2) + '%'));
  originalScenarios++;
}
f.el['theme-toggle'].dispatch('click');
assert.strictEqual(f.document.documentElement.dataset.theme, 'dark');
assert.strictEqual(f.el['theme-toggle'].getAttribute('aria-pressed'), 'false');
assert.strictEqual(f.store['pfc-theme'], 'night');
assert.strictEqual(f.store['laser-pfc-tp-theme'], 'dark'); originalScenarios++;
f.el['theme-toggle'].dispatch('click');
assert.strictEqual(f.document.documentElement.dataset.theme, 'light');
assert.strictEqual(f.el['theme-toggle'].getAttribute('aria-pressed'), 'true');
assert.strictEqual(f.store['laser-pfc-tp-theme'], 'light'); originalScenarios++;
for (let i = 0; i < f.buttons.length; i++) {
  f.buttons[i].dispatch('click');
  assert.strictEqual(f.docs.filter(x => !x.hidden).length, 1);
  assert(!f.docs[i].hidden); assert.strictEqual(f.el.selector.hidden, i !== 0); originalScenarios++;
}
f.links[1].dispatch('click'); assert(!f.el.derivation.hidden); originalScenarios++;
assert.strictEqual(originalScenarios, 38);

for (const mode of ['en', 'zh', 'bilingual']) {
  f.el['language-toggle'].dispatch('click');
  assert.strictEqual(f.document.documentElement.dataset.language, mode);
  assert.strictEqual(f.document.documentElement.lang, mode === 'zh' ? 'zh-CN' : 'en');
  assert.strictEqual(f.store['embedded-pfc-language'], mode);
  const returnQuery = new URLSearchParams(f.el['appendix-return'].getAttribute('href').split('?')[1]);
  assert.strictEqual(returnQuery.get('lang'), mode === 'zh' ? 'zh' : 'en');
  assert.strictEqual(returnQuery.get('theme'), 'light');
  interfaceScenarios++;
}
assert.strictEqual(f.store['laser-pfc-tp-language'], 'zh'); // Bilingual does not erase the last single-language choice.
assert(f.readerLink.getAttribute('href').includes('keep=1'));
assert(f.readerLink.getAttribute('href').endsWith('#derivation'));
assert(f.readerLink.getAttribute('href').includes('lang=bilingual'));
assert.strictEqual(f.external.getAttribute('href'), 'https://example.org/source.html');
assert.strictEqual(f.markdown.getAttribute('href'), 'REPORT.md'); interfaceScenarios++;

for (const [query, expected, shared] of [['dark', 'dark', 'dark'], ['night', 'dark', 'dark'], ['light', 'light', 'light'], ['day', 'light', 'light']]) {
  const q = fixture({ search: '?lang=zh&theme=' + query, store: { 'embedded-pfc-language': 'en', 'laser-pfc-tp-theme': 'light', 'pfc-theme': 'night' } });
  assert.strictEqual(q.document.documentElement.dataset.language, 'zh');
  assert.strictEqual(q.document.documentElement.dataset.theme, expected);
  assert.strictEqual(q.store['laser-pfc-tp-theme'], shared);
  assert(q.el['appendix-return'].getAttribute('href').startsWith('../../appendices/'));
  assert(q.el['appendix-return'].getAttribute('href').includes('lang=zh&theme=' + shared));
  interfaceScenarios++;
}
const sharedPreference = fixture({ store: { 'laser-pfc-tp-theme': 'light', 'pfc-theme': 'night', 'embedded-pfc-language': 'zh' } });
assert.strictEqual(sharedPreference.document.documentElement.dataset.theme, 'light');
assert.strictEqual(sharedPreference.document.documentElement.dataset.language, 'zh'); interfaceScenarios++;
const legacyPreference = fixture({ store: { 'pfc-theme': 'night' } });
assert.strictEqual(legacyPreference.document.documentElement.dataset.theme, 'dark'); interfaceScenarios++;
const standalone = fixture({ pathname: '/forwarded-study/index.html', search: '?lang=zh&theme=dark' });
assert.strictEqual(standalone.el['appendix-return'].getAttribute('href'), canonical + '?lang=zh&theme=dark'); interfaceScenarios++;
const noStorage = fixture({ storageUnavailable: true });
assert.strictEqual(noStorage.document.documentElement.dataset.language, 'bilingual');
noStorage.el['theme-toggle'].dispatch('click'); assert.strictEqual(noStorage.document.documentElement.dataset.theme, 'light');
noStorage.el['language-toggle'].dispatch('click'); noStorage.el['language-toggle'].dispatch('click');
assert.strictEqual(noStorage.document.documentElement.dataset.language, 'zh'); interfaceScenarios++;
const deepLink = fixture({ hash: '#sources' });
assert(!deepLink.el.sources.hidden); assert(deepLink.el.selector.hidden);
deepLink.location.hash = '#handoff'; deepLink.windowEvents.hashchange(); assert(!deepLink.el.handoff.hidden); interfaceScenarios++;
assert.strictEqual(f.scrollCalls.length, 4); assert(f.scrollCalls.every(x => x.top === 0)); interfaceScenarios++;

const result = {
  status: 'PASS', scenarios: originalScenarios + interfaceScenarios, original_scenarios: originalScenarios,
  interface_scenarios: interfaceScenarios, selector_states: states.length, theme_and_document_events: true,
  language_modes: ['bilingual', 'en', 'zh'], query_theme_aliases: ['light', 'dark', 'day', 'night'],
  theme_aria_pressed: 'light',
  scope: 'JavaScript events with browser API stubs. CSS/layout checks use the separate real-browser audit.',
  browser_inspection: 'verification/READER_REVISION_AUDIT.json', revision_date: '2026-10-14'
};
fs.writeFileSync(path.join(root, 'verification', 'READER_LOGIC_REVISION_20261014.json'), JSON.stringify(result, null, 2) + '\n');
process.stdout.write(JSON.stringify(result) + '\n');
