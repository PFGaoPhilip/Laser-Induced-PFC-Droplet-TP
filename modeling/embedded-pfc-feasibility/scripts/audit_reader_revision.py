"""Audit bilingual coverage, frozen payload and portable browser controls.

Uses a separate temporary headless Chrome profile. No solver is launched.
Temporary browser/copy files remain inside the study verification directory.
"""
import asyncio
import base64
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

import websockets
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
COURSE=ROOT.parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def static_audit():
    from build_reader import blocks
    page=BeautifulSoup((ROOT/'index.html').read_text(encoding='utf8'),'html.parser')
    documents=['REPORT.md','DERIVATION.md','IMPLEMENTATION_HANDOFF.md','SOURCES.md']
    coverage={}
    for document in documents:
        en=list(blocks((ROOT/document).read_text(encoding='utf8')))
        zh=list(blocks((ROOT/Path(document).with_suffix('.zh.md')).read_text(encoding='utf8')))
        assert len(en)==len(zh)
        for index,((kind,a),(other,b)) in enumerate(zip(en,zh)):
            assert kind==other, (document,index)
            if kind=='equation': assert a==b,(document,index)
            else: assert re.search(r'[\u4e00-\u9fff]',str(b)),(document,index)
        coverage[document]={'blocks':len(en),'translated':sum(k!='equation' for k,v in en)}
    equations=[v for k,v in blocks((ROOT/'DERIVATION.md').read_text(encoding='utf8')) if k=='equation']
    ids=[re.search(r'\\tag\{([^}]+)\}',e)[1] for e in equations]
    assert ids==[f'E{i:02}' for i in range(1,33)]
    archive=ROOT/'Embedded_PFC_Feasibility_Public_20261011.zip'
    with ZipFile(archive) as original:
        candidates=[name for name in original.namelist() if name.endswith('/DERIVATION.md') or name=='DERIVATION.md']
        assert len(candidates)==1
        previous=[v for k,v in blocks(original.read(candidates[0]).decode('utf8')) if k=='equation']
    assert previous==equations,'Displayed equation changed from delivered archive'
    missing=[]
    for node in page.select('[src],link[href]'):
        target=node.get('src') or node.get('href')
        if not target or re.match(r'^(?:[a-z]+:|#|//)',target): continue
        local=(ROOT/unquote(urlsplit(target).path)).resolve()
        if not local.is_file(): missing.append(target)
    assert not missing,missing
    for name in ['course.css','course-language.css','bilingual-terms.css']:
        assert digest(ROOT/'assets'/name)==digest(COURSE/'assets'/name),name
    for selector in ['.topbar','.page-layout','.sidebar','.reading','.chapter-header','.chapter-body','.site-footer']:
        assert page.select_one(selector),selector
    assert len(page.select('.theme-tools'))==1
    assert page.select_one('.theme-tools #theme-toggle') and page.select_one('.theme-tools #language-toggle')
    assert len(page.select('.theme-tools button'))==2 and not page.select('.theme-tools select')
    assert not page.select('.topbar #theme-toggle,.topbar #language-toggle,header #theme-toggle,header #language-toggle')
    settings=json.loads((COURSE/'COURSE_SETTINGS.json').read_text(encoding='utf8'))
    for unit in settings['chapters']+settings['appendices']:
        anchor=page.select_one('.sidebar a[data-course-path="'+unit['file']+'"]')
        assert anchor and unit['title'] in anchor.get_text() and unit['title_zh'] in anchor.get_text(),unit['file']
    copy=json.loads((ROOT/'COPY_MANIFEST.json').read_text(encoding='utf8'))
    frozen=[]
    for row in copy['files']:
        name=row['file']
        protected=(name.startswith(('data/','models/')) or
                   (name.startswith('sources/') and name.endswith('.json') and 'provenance' not in name) or
                   name in ['DERIVATION.tex','output/pdf/FINITE_PFC_DERIVATION.pdf'])
        if protected:
            assert digest(ROOT/name)==row['accepted_source_sha256'],name
            frozen.append(name)
    figure_counts={}
    for name in ['size_species_comparison','radial_viscosity_controls','radial_stability','fracture_budget']:
        a=BeautifulSoup((ROOT/'assets'/f'{name}.svg').read_text(encoding='utf8'),'xml')
        b=BeautifulSoup((ROOT/'assets'/f'{name}.zh.svg').read_text(encoding='utf8'),'xml')
        assert [x.attrs for x in a.select('path,polygon,polyline,circle,rect')]==[x.attrs for x in b.select('path,polygon,polyline,circle,rect')]
        assert len(a.select('text'))==len(b.select('text'))
        figure_counts[name]=len(b.select('text'))
    return {'coverage':coverage,'displayed_equations':len(equations),'equation_ids':ids,'equations_match_prior_archive':True,'unchanged_protected_files':len(frozen),'missing_assets':missing,'translated_plot_geometry_unchanged':figure_counts,'canonical_styles_identical':True,'canonical_navigation_titles':True,'canonical_chapter_wrappers':True,'single_toolbar_outside_header':True}

class CDP:
    def __init__(self,socket): self.socket=socket;self.index=0
    async def call(self,method,params=None):
        self.index+=1;index=self.index
        await self.socket.send(json.dumps({'id':index,'method':method,'params':params or {}}))
        while True:
            message=json.loads(await self.socket.recv())
            if message.get('id')==index:
                if 'error' in message: raise RuntimeError(message['error'])
                return message.get('result',{})
    async def evaluate(self,expression):
        result=await self.call('Runtime.evaluate',{'expression':expression,'returnByValue':True,'awaitPromise':True})
        if 'exceptionDetails' in result: raise RuntimeError(result['exceptionDetails'])
        return result.get('result',{}).get('value')
    async def load(self,url,selector='#state-output strong'):
        await self.call('Page.navigate',{'url':url})
        for _ in range(100):
            if await self.evaluate("document.readyState==='complete' && !!document.querySelector("+json.dumps(selector)+")"):
                await self.evaluate('document.fonts.ready.then(()=>true)')
                return
            await asyncio.sleep(.1)
        raise TimeoutError(url)
    async def screenshot(self,name):
        result=await self.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
        (COURSE/'verification'/name).write_bytes(base64.b64decode(result['data']))

async def browser_audit():
    chrome=Path(os.environ.get('CHROME_BINARY') or shutil.which('google-chrome')
                or shutil.which('chromium') or shutil.which('chrome')
                or str(Path(os.environ.get('PROGRAMFILES', ''))/'Google/Chrome/Application/chrome.exe'))
    assert chrome.is_file()
    # Resolved temporary targets are confined to this known verification root.
    verification=(ROOT/'verification').resolve()
    with tempfile.TemporaryDirectory(prefix='reader-browser-',dir=verification) as folder:
        temp=Path(folder).resolve();assert temp.is_relative_to(verification)
        profile=temp/'chrome-profile'
        process=subprocess.Popen([str(chrome),'--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--remote-debugging-port=0','--remote-allow-origins=*','--user-data-dir='+str(profile),'--window-size=1440,1000','about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            port_file=profile/'DevToolsActivePort'
            for _ in range(100):
                if port_file.exists(): break
                await asyncio.sleep(.1)
            port=int(port_file.read_text().splitlines()[0])
            tabs=json.loads(urllib.request.urlopen(f'http://localhost:{port}/json/list').read())
            tab=next(t for t in tabs if t['type']=='page')
            async with websockets.connect(tab['webSocketDebuggerUrl'],max_size=16*1024*1024) as socket:
                cdp=CDP(socket);await cdp.call('Page.enable')
                await cdp.call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1000,'deviceScaleFactor':1,'mobile':False})
                typography_script="""(()=>{const holder=document.createElement('div');holder.style.cssText='position:absolute;left:-9999px;width:800px';holder.innerHTML='<div class="lang-pair"><p lang="en">Typography</p><p class="zh" lang="zh-CN">排版</p></div><h2>Heading</h2><h3>Heading</h3><h4>Heading</h4><table><tbody><tr><td>Cell</td></tr></tbody></table><code>Code</code><div class="math-display"><span class="katex">Math</span></div>';document.querySelector('.chapter-body').appendChild(holder);const props=['fontFamily','fontSize','fontWeight','lineHeight','letterSpacing'];const snapshot=e=>Object.fromEntries(props.map(p=>[p,getComputedStyle(e)[p]]));const result={body:snapshot(document.body),h1:snapshot(document.querySelector('.chapter-header h1[lang=en]')),chineseH1:snapshot(document.querySelector('.chapter-header h1[lang=zh-CN]')),topbar:snapshot(document.querySelector('.topbar')),paragraph:snapshot(holder.querySelector('p[lang=en]')),chineseParagraph:snapshot(holder.querySelector('p.zh')),h2:snapshot(holder.querySelector('h2')),h3:snapshot(holder.querySelector('h3')),h4:snapshot(holder.querySelector('h4')),table:snapshot(holder.querySelector('table')),code:snapshot(holder.querySelector('code')),math:snapshot(holder.querySelector('.math-display')),katex:snapshot(holder.querySelector('.katex'))};holder.remove();return result})()"""
                await cdp.load((COURSE/'chapters/01-cavity-pressure-inertia-and-directional-jets.html').as_uri()+'?lang=en&theme=light','.chapter-body')
                canonical_typography=await cdp.evaluate(typography_script)
                await cdp.load((ROOT/'index.html').as_uri()+'?lang=en&theme=light')
                reader_typography=await cdp.evaluate(typography_script)
                assert reader_typography==canonical_typography,{'canonical':canonical_typography,'reader':reader_typography}
                toolbar_script="""(()=>{const e=document.querySelector('.theme-tools'),r=e.getBoundingClientRect();return {position:getComputedStyle(e).position,right:document.documentElement.clientWidth-r.right,bottom:innerHeight-r.bottom,left:r.left,top:r.top,width:r.width,height:r.height,themeInside:e.contains(document.querySelector('#theme-toggle')),languageInside:e.contains(document.querySelector('#language-toggle')),buttonCount:e.querySelectorAll('button').length,selectCount:e.querySelectorAll('select').length,headerControls:document.querySelectorAll('.topbar #theme-toggle,.topbar #language-toggle,header #theme-toggle,header #language-toggle').length}})()"""
                toolbar_desktop=await cdp.evaluate(toolbar_script)
                assert toolbar_desktop['position']=='fixed' and 0<=toolbar_desktop['right']<48 and 0<=toolbar_desktop['bottom']<48
                assert toolbar_desktop['themeInside'] and toolbar_desktop['languageInside'] and toolbar_desktop['headerControls']==0 and toolbar_desktop['buttonCount']==2 and toolbar_desktop['selectCount']==0
                await cdp.load((ROOT/'index.html').as_uri()+'?lang=zh&theme=dark')
                incoming=await cdp.evaluate("({language:document.documentElement.dataset.language,theme:document.documentElement.dataset.theme,returnLink:document.querySelector('#appendix-return').getAttribute('href'),sharedTheme:localStorage.getItem('laser-pfc-tp-theme')})")
                assert incoming['language']=='zh' and incoming['theme']=='dark' and incoming['sharedTheme']=='dark'
                assert 'lang=zh' in incoming['returnLink'] and 'theme=dark' in incoming['returnLink']
                await cdp.load((ROOT/'index.html').as_uri()+'?lang=bilingual&theme=light')
                await cdp.evaluate("document.querySelector('#theme-toggle').click();document.querySelector('#theme-toggle').click()")
                await cdp.screenshot('embedded-reader-bilingual-day.png')
                modes=[]
                for mode in ['bilingual','en','zh']:
                    result=await cdp.evaluate("(()=>{const wanted="+json.dumps(mode)+";for(let i=0;i<3&&document.documentElement.dataset.language!==wanted;i++)document.querySelector('#language-toggle').click();return {language:document.documentElement.dataset.language,en:[...document.querySelectorAll('[lang=en]')].filter(e=>e.getClientRects().length).length,zh:[...document.querySelectorAll('[lang=zh-CN]')].filter(e=>e.getClientRects().length).length}})()")
                    assert result['language']==mode
                    if mode=='en': assert result['zh']==0
                    if mode=='zh': assert result['en']==0
                    if mode=='bilingual': assert result['en']>0 and result['zh']>0
                    modes.append(result)
                theme=await cdp.evaluate("(()=>{let b=document.querySelector('#theme-toggle');b.click();let a=document.documentElement.dataset.theme;b.click();return [a,document.documentElement.dataset.theme]})()")
                assert set(theme)=={'light','dark'}
                await cdp.evaluate("document.querySelector('#theme-toggle').click()")
                await cdp.screenshot('embedded-reader-chinese-night.png')
                docs=[]
                for name in ['comparison','derivation','handoff','sources']:
                    state=await cdp.evaluate("(()=>{document.querySelector('[data-doc="+name+"]').click();return {visible:[...document.querySelectorAll('.document')].filter(e=>!e.hidden).map(e=>e.id),selectorHidden:document.querySelector('#selector').hidden}})()")
                    assert state['visible']==[name]
                    assert state['selectorHidden']==(name!='comparison')
                    docs.append(state)
                states=await cdp.evaluate("(()=>{document.querySelector('[data-doc=comparison]').click();let results=[];let ids=['fluid','diameter','modulus'];for(const f of document.querySelector('#fluid').options)for(const d of document.querySelector('#diameter').options)for(const g of document.querySelector('#modulus').options){for(const [id,value] of ids.map((id,i)=>[id,[f.value,d.value,g.value][i]])){const el=document.getElementById(id);el.value=value;el.dispatchEvent(new Event('change'));}results.push([...document.querySelectorAll('#state-output strong')].map(n=>n.textContent));}return results;})()")
                assert len(states)==30 and all(len(s)==4 for s in states)
                await cdp.evaluate("for(let i=0;i<3&&document.documentElement.dataset.language!=='zh';i++)document.querySelector('#language-toggle').click();Promise.all([...document.images].map(i=>{i.loading='eager';return i.decode().catch(()=>null)}))")
                plot_images=[]
                for name in ['size_species_comparison','radial_viscosity_controls','radial_stability','fracture_budget']:
                    clip=await cdp.evaluate("(()=>{const img=document.querySelector('img[src=\"assets/"+name+".zh.svg\"]');img.scrollIntoView({block:'center'});const r=img.getBoundingClientRect();return {x:r.x,y:r.y+scrollY,width:r.width,height:r.height,scale:1}})()")
                    result=await cdp.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'clip':clip})
                    filename='embedded-reader-'+name+'-chinese.png'
                    (COURSE/'verification'/filename).write_bytes(base64.b64decode(result['data']))
                    plot_images.append(filename)
                await cdp.evaluate("document.querySelector('[data-doc=derivation]').click();for(let i=0;i<3&&document.documentElement.dataset.language!=='bilingual';i++)document.querySelector('#language-toggle').click()")
                await cdp.screenshot('embedded-reader-derivation-night.png')
                await cdp.call('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True})
                toolbar_mobile=await cdp.evaluate(toolbar_script)
                assert toolbar_mobile['position']=='fixed' and 0<=toolbar_mobile['right']<24 and 0<=toolbar_mobile['bottom']<24 and toolbar_mobile['left']>=0
                assert toolbar_mobile['themeInside'] and toolbar_mobile['languageInside'] and toolbar_mobile['headerControls']==0 and toolbar_mobile['buttonCount']==2 and toolbar_mobile['selectCount']==0
                await cdp.screenshot('embedded-reader-mobile.png')
                width=await cdp.evaluate('({viewport:innerWidth,document:document.documentElement.scrollWidth})')
                assert width['document']<=width['viewport'],width
                await cdp.load((COURSE/'chapters/01-cavity-pressure-inertia-and-directional-jets.html').as_uri()+'?lang=en&theme=light','.chapter-body')
                canonical_mobile_typography=await cdp.evaluate(typography_script)
                await cdp.load((ROOT/'index.html').as_uri()+'?lang=en&theme=light')
                reader_mobile_typography=await cdp.evaluate(typography_script)
                assert reader_mobile_typography==canonical_mobile_typography,{'canonical_mobile':canonical_mobile_typography,'reader_mobile':reader_mobile_typography}
                # Copy the essential reader to a differently named folder.
                relocated=temp/'forwarded-study';relocated.mkdir()
                shutil.copy2(ROOT/'index.html',relocated/'index.html')
                shutil.copytree(ROOT/'assets',relocated/'assets')
                await cdp.load((relocated/'index.html').as_uri()+'?lang=zh#comparison')
                await cdp.evaluate("Promise.all([...document.images].map(i=>{i.loading='eager';return i.decode().then(()=>true).catch(()=>false)}))")
                moved=await cdp.evaluate("({mode:document.documentElement.dataset.language,states:document.querySelectorAll('#state-output strong').length,returnLink:document.querySelector('#appendix-return').getAttribute('href'),brokenImages:[...document.images].filter(i=>getComputedStyle(i).display!=='none'&&(!i.complete||i.naturalWidth===0)).map(i=>i.src),math:document.querySelectorAll('.katex-error').length})")
                assert moved['mode']=='zh' and moved['states']==4 and not moved['brokenImages'] and moved['math']==0,moved
                assert moved['returnLink'].startswith('https://')
                persisted=await cdp.evaluate("(()=>{for(let i=0;i<3&&document.documentElement.dataset.language!=='en';i++)document.querySelector('#language-toggle').click();return localStorage.getItem('embedded-pfc-language')})()")
                assert persisted=='en'
                await cdp.load((relocated/'index.html').as_uri())
                assert await cdp.evaluate('document.documentElement.dataset.language')=='en'
                return {'appendix_entry_and_return':incoming,'language_modes':modes,'theme_states':theme,'document_tabs':docs,'selector_states_checked':len(states),'mobile_width':width,'relocated_reader':moved,'language_persistence':True,'canonical_typography_desktop':canonical_typography,'canonical_typography_mobile':canonical_mobile_typography,'typography_matches_first_chapter':True,'toolbar_desktop':toolbar_desktop,'toolbar_mobile':toolbar_mobile,'screenshots':['embedded-reader-bilingual-day.png','embedded-reader-chinese-night.png','embedded-reader-derivation-night.png','embedded-reader-mobile.png']+plot_images}
        finally:
            process.terminate()
            try: process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill();process.wait(timeout=10)

def main():
    report={'status':'PASS','date':'2026-10-14','static':static_audit(),'browser':asyncio.run(browser_audit()),'simulations_rerun':False}
    (ROOT/'verification/READER_REVISION_AUDIT.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__': main()
