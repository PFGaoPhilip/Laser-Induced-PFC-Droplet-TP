(function(){
  const root=document.documentElement;
  const panes=Array.from(document.querySelectorAll('.locale-pane'));
  const languageButton=document.getElementById('language-toggle');
  const themeButton=document.getElementById('theme-toggle');
  const languageKey='laser-pfc-tp-language';
  const themeKey='minimal-cavitation-theme';
  if(location.pathname.includes('/modeling/minimal-cavitation/')){
    document.querySelectorAll('[data-course-return="appendix-a"]').forEach(link=>{
      link.href='../../appendices/a-hydrogel-versus-liquid.html';
    });
  }
  function stored(key,fallback){try{return localStorage.getItem(key)||fallback}catch(_error){return fallback}}
  function remember(key,value){try{localStorage.setItem(key,value)}catch(_error){}}
  function labels(){
    const zh=root.dataset.language==='zh',day=root.dataset.theme==='light';
    languageButton.textContent=zh?'English':'中文';
    languageButton.setAttribute('aria-label',zh?'切换到英文':'Switch to Chinese');
    themeButton.textContent=zh?(day?'夜间模式':'日间模式'):(day?'Night mode':'Day mode');
    themeButton.setAttribute('aria-label',zh?'切换日间与夜间模式':'Switch between day and night modes');
    themeButton.setAttribute('aria-pressed',day?'true':'false');
    languageButton.parentElement.setAttribute('aria-label',zh?'阅读设置':'Reader settings');
    document.querySelectorAll('[data-course-path]').forEach(link=>{
      if(location.pathname.includes('/modeling/minimal-cavitation/')){
        link.href='../../'+link.dataset.coursePath+'?lang='+(zh?'zh':'en')+'&theme='+(day?'light':'dark');
      }
    });
    document.querySelectorAll('a[href]').forEach(link=>{
      const href=link.getAttribute('href');
      if(!href||/^[a-z]+:/i.test(href)||href.startsWith('//')||href.startsWith('#'))return;
      const url=new URL(href,location.href);
      if(!/\.html$/i.test(url.pathname))return;
      const base=href.split('#')[0].split('?')[0];
      url.searchParams.set('lang',zh?'zh':'en');
      url.searchParams.set('theme',day?'light':'dark');
      link.setAttribute('href',base+'?'+url.searchParams.toString()+url.hash);
    });
    const active=panes.find(pane=>!pane.hidden);
    if(active)document.title=active.querySelector('h1').textContent.replace(/\s+/g,' ').trim();
    if(location.pathname.includes('/modeling/minimal-cavitation/')){
      document.querySelectorAll('[data-course-return="appendix-a"]').forEach(link=>{
        link.href='../../appendices/a-hydrogel-versus-liquid.html?lang='+(zh?'zh':'en')+'&theme='+(day?'light':'dark');
      });
    }
  }
  function canonicalHash(){return location.hash.replace(/^#(?:en|zh)-/,'').replace(/^#/,'')}
  function chooseLanguage(language,preservePosition){
    language=language==='en'?'en':'zh';
    const previous=panes.find(pane=>!pane.hidden);let anchor=null,oldTop=0;
    const disclosure=previous?Array.from(previous.querySelectorAll('details[data-anchor]')).map(node=>({anchor:node.dataset.anchor,open:node.open})):[];
    if(preservePosition&&previous){
      const candidates=Array.from(previous.querySelectorAll('[data-anchor]')).filter(node=>node.getBoundingClientRect().top<=140&&node.getBoundingClientRect().bottom>=0);
      anchor=candidates[candidates.length-1]||null;if(anchor)oldTop=anchor.getBoundingClientRect().top;
    }
    panes.forEach(pane=>{pane.hidden=pane.dataset.locale!==language});
    disclosure.forEach(state=>{const next=document.getElementById(language+'-'+state.anchor);if(next)next.open=state.open});
    root.dataset.language=language;root.lang=language==='zh'?'zh-CN':'en';remember(languageKey,language);labels();
    const hash=canonicalHash();
    if(hash&&document.getElementById(language+'-'+hash)){try{history.replaceState(null,'','#'+language+'-'+hash)}catch(_error){}}
    if(anchor){const next=document.getElementById(language+'-'+anchor.dataset.anchor);if(next)window.scrollTo({top:window.scrollY+next.getBoundingClientRect().top-oldTop,behavior:'instant'})}
    document.dispatchEvent(new CustomEvent('reader-language-change',{detail:{language}}));
  }
  const requestedTheme=new URLSearchParams(location.search).get('theme');
  const selectedTheme=requestedTheme||stored('laser-pfc-tp-theme','dark');
  root.dataset.theme=(selectedTheme==='light'||selectedTheme==='day')?'light':'dark';chooseLanguage(new URLSearchParams(location.search).get('lang')||stored(languageKey,'en'),false);
  languageButton.addEventListener('click',()=>chooseLanguage(root.dataset.language==='zh'?'en':'zh',true));
  themeButton.addEventListener('click',()=>{root.dataset.theme=root.dataset.theme==='light'?'dark':'light';remember(themeKey,root.dataset.theme);remember('laser-pfc-tp-theme',root.dataset.theme==='light'?'light':'dark');labels()});
  function revealHash(){const hash=canonicalHash(),target=hash&&document.getElementById(root.dataset.language+'-'+hash);if(target){const details=target.closest('details');if(details)details.open=true;target.scrollIntoView({block:'start'})}}
  revealHash();window.addEventListener('hashchange',revealHash);
})();
