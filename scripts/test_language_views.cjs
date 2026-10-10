/* DOM tests with explicit scroll/clipboard stubs; no browser rendering claim. */
const fs=require('node:fs'), path=require('node:path'), assert=require('node:assert/strict');
const {JSDOM}=require(process.argv[2]);
const root=path.resolve(__dirname,'..'), checks=[];
function load(file,query='') {
  const dom=new JSDOM(fs.readFileSync(path.join(root,file),'utf8'),{url:'https://course.test/'+file+query,runScripts:'outside-only',pretendToBeVisual:true});
  const w=dom.window; w.scrollTo=()=>{}; w.HTMLElement.prototype.scrollIntoView=function(){};
  for(const link of w.document.querySelectorAll('link[rel="stylesheet"]')) {
    if(link.href.includes('/vendor/'))continue;
    const p=path.resolve(root,path.dirname(file),link.getAttribute('href'));
    const style=w.document.createElement('style');style.textContent=fs.readFileSync(p,'utf8');w.document.head.appendChild(style);
  }
  for(const script of w.document.querySelectorAll('script[src]')) {
    const p=path.resolve(root,path.dirname(file),script.getAttribute('src'));
    w.eval(fs.readFileSync(p,'utf8'));
  }
  w.document.dispatchEvent(new w.Event('DOMContentLoaded'));
  return dom;
}
const config=JSON.parse(fs.readFileSync(path.join(root,'COURSE_SETTINGS.json')));
const files=['index.html',...config.chapters.map(x=>x.file),...config.appendices.map(x=>x.file),'reference/notation.html','reference/sources.html','reference/defense.html'];
for(const file of files) {
  const dom=load(file,'?lang=en'),w=dom.window,d=w.document;
  assert.equal(d.documentElement.dataset.language,'en');
  assert.equal(w.getComputedStyle(d.querySelector('body [lang="zh-CN"]')).display,'none');
  d.getElementById('language-toggle').click();
  assert.equal(d.documentElement.lang,'zh-CN');
  assert.equal(w.getComputedStyle(d.querySelector('body [lang="en"]')).display,'none');
  assert.equal(w.localStorage.getItem('laser-pfc-tp-language'),'zh');
  assert.equal(d.getElementById('theme-toggle').textContent,'日间模式');
  d.getElementById('theme-toggle').click();assert.equal(d.documentElement.dataset.theme,'light');
  assert.equal(d.getElementById('theme-toggle').textContent,'夜间模式');
  assert.ok([...d.querySelectorAll('a[href*="modeling/"]')].every(a=>new URL(a.href).searchParams.get('lang')==='zh'));
  const response=d.querySelector('textarea[data-response]');
  if(response){response.value='Shared draft';response.dispatchEvent(new w.Event('input'));d.getElementById('language-toggle').click();assert.equal(response.value,'Shared draft');assert.ok(d.getElementById('save-status').textContent.startsWith('Draft saved'));}
  assert.equal(new Set([...d.querySelectorAll('[id]')].map(n=>n.id)).size,d.querySelectorAll('[id]').length);
  checks.push(file+': separate views, language/theme buttons, shared response state, unique anchors');dom.window.close();
}
for(const file of ['modeling/minimal-cavitation/index.html','modeling/minimal-cavitation/STEP_BY_STEP.html']) {
  const dom=load(file,'?lang=en&theme=light'),d=dom.window.document;
  assert.equal(d.documentElement.dataset.language,'en');assert.equal(d.documentElement.dataset.theme,'day');
  assert.equal(d.querySelector('.locale-pane[data-locale="zh"]').hidden,true);
  d.getElementById('language').click();assert.equal(d.documentElement.dataset.language,'zh');
  assert.equal(d.querySelector('.locale-pane[data-locale="en"]').hidden,true);
  assert.equal(dom.window.localStorage.getItem('laser-pfc-tp-language'),'zh');
  assert.ok(d.querySelector('a[href="../../index.html?lang=zh"]'));
  checks.push(file+': separate panes, course return link and shared preferences');dom.window.close();
}
const report={status:'passed',scope:'JSDOM interaction and CSS visibility checks; layout/clipboard are not browser rendering.',checks};
fs.writeFileSync(path.join(root,'verification/language-views-audit.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,pages:checks.length}));
