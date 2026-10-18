"""Real Edge rendering and interaction checks, including a relocated offline copy."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json,sys

ROOT=Path(__file__).resolve().parents[1]
target=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT
out=ROOT/'reports/ch1_defense_revision/browser'
out.mkdir(parents=True,exist_ok=True)
chapter='chapters/01-cavity-pressure-inertia-and-directional-jets.html'
results=[]
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    for name,width,height,lang,theme in [('desktop-en-light',1440,1000,'en','light'),('desktop-zh-dark',1440,1000,'zh','dark'),('mobile-en-dark',390,844,'en','dark'),('mobile-zh-light',390,844,'zh','light')]:
        ctx=browser.new_context(viewport={'width':width,'height':height},device_scale_factor=1,reduced_motion='reduce')
        page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        page.goto((target/chapter).as_uri()+f'?lang={lang}&theme={theme}',wait_until='load')
        page.locator('#C1-E33 details').count() # explicit page parse completion
        page.evaluate('document.fonts.ready');page.locator('details.answer').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
        page.locator('img').evaluate_all('(els)=>els.forEach(e=>e.loading="eager")')
        page.wait_for_function('Array.from(document.images).every(i=>i.complete)')
        state=page.evaluate('''()=>({lang:document.documentElement.dataset.language,theme:document.documentElement.dataset.theme,
          equations:document.querySelectorAll('.equation-unit').length,errors:document.querySelectorAll('.katex-error').length,
          brokenImages:Array.from(document.images).filter(i=>!i.naturalWidth).map(i=>i.src),
          overflow:document.documentElement.scrollWidth>innerWidth+2,
          visibleEnglish:Array.from(document.querySelectorAll('.chapter-body > .lang-pair > p[lang="en"]')).some(e=>getComputedStyle(e).display!=='none'),
          visibleChinese:Array.from(document.querySelectorAll('.chapter-body > .lang-pair > p[lang="zh-CN"]')).some(e=>getComputedStyle(e).display!=='none')})''')
        assert state['equations']==33 and state['errors']==0 and not state['brokenImages'] and not state['overflow'],state
        assert state['lang']==lang and state['theme']==theme
        assert state['visibleEnglish']==(lang=='en') and state['visibleChinese']==(lang=='zh')
        # Verify both toggle buttons and persistence after query-free navigation.
        page.locator('#language-toggle').click();page.locator('#theme-toggle').click()
        changed=page.evaluate('({lang:document.documentElement.dataset.language,theme:document.documentElement.dataset.theme})')
        page.goto((target/chapter).as_uri(),wait_until='load')
        assert page.evaluate('({lang:document.documentElement.dataset.language,theme:document.documentElement.dataset.theme})')==changed
        page.goto((target/chapter).as_uri()+f'?lang={lang}&theme={theme}',wait_until='load')
        page.locator('details.answer').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
        # Freeze smooth scrolling for deterministic capture. Product CSS stays intact.
        page.add_style_tag(content='html{scroll-behavior:auto!important}')
        for ident in ([] if target!=ROOT else ['C1-E05','C1-E11','C1-E14','C1-E21','C1-E28','C1-E30','C1-E33'] if width>400 else ['C1-E05','C1-E30']):
            page.locator('#'+ident).screenshot(path=str(out/f'{name}-{ident}.png'))
        if name=='desktop-en-light' and target==ROOT:
            for box in page.locator('.equation-unit').all():
                box.screenshot(path=str(out/(box.get_attribute('id')+'.png')))
        assert not errors,errors
        results.append({'case':name,**state,'toggle_and_persistence':'passed','javascript_errors':errors})
        ctx.close()
    browser.close()
name='relocated-browser.json' if target!=ROOT else 'browser.json'
(ROOT/'reports/ch1_defense_revision'/name).write_text(json.dumps({'status':'passed','offline_file_origin':True,'cases':results},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','offline':True,'cases':len(results),'relocated':target!=ROOT}))
