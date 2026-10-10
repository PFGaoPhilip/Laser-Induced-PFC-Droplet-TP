(() => {
  const root=document.documentElement;
  const theme=document.getElementById('theme-toggle');
  let saved='day';try{saved=localStorage.getItem('pfc-theme')||'day';}catch(e){}
  const setTheme=value=>{root.dataset.theme=value;theme.textContent=value==='night'?'Day mode':'Night mode';theme.setAttribute('aria-pressed',String(value==='night'));};
  setTheme(saved);
  theme.addEventListener('click',()=>{const value=root.dataset.theme==='night'?'day':'night';setTheme(value);try{localStorage.setItem('pfc-theme',value);}catch(e){}});
  const names=['comparison','derivation','handoff','sources'];
  function show(name){
    if(!names.includes(name))return;
    document.querySelectorAll('.document').forEach(x=>x.hidden=x.id!==name);
    document.querySelectorAll('[data-doc]').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.doc===name)));
    document.getElementById('selector').hidden=name!=='comparison';
  }
  document.querySelectorAll('[data-doc]').forEach(x=>x.addEventListener('click',()=>{show(x.dataset.doc);history.replaceState(null,'','#'+x.dataset.doc);}));
  document.querySelectorAll('a[href^="#"]').forEach(x=>x.addEventListener('click',()=>show(x.getAttribute('href').slice(1))));
  window.addEventListener('hashchange',()=>show(location.hash.slice(1)));
  show(location.hash.slice(1)||'comparison');
  const data=JSON.parse(document.getElementById('state-data').textContent);
  const ids=['fluid','diameter','modulus'];
  function update(){
    const fluid=document.getElementById('fluid').value;
    const diameter=Number(document.getElementById('diameter').value),G=Number(document.getElementById('modulus').value);
    const s=data.find(x=>x.fluid===fluid&&Math.abs(x.diameter_um-diameter)<1e-6&&x.G_kPa===G);
    if(!s)throw new Error('Missing solved state');
    const energy=s.Q_pJ>=1000?(s.Q_pJ/1000).toFixed(3)+' nJ':s.Q_pJ.toFixed(2)+' pJ';
    document.getElementById('state-output').innerHTML='<div>State temperature<strong>'+s.T_K.toFixed(2)+' K</strong>Curved equilibrium</div><div>State energy<strong>'+energy+'</strong>Relative to all-liquid reference</div><div>Vapor mass fraction<strong>'+(100*s.vapor_fraction).toFixed(2)+'%</strong>Surviving liquid shell</div><div>Elastic resistance<strong>'+s.pEl_kPa.toFixed(3)+' kPa</strong>Stipulated intact gel</div>';
  }
  ids.forEach(id=>document.getElementById(id).addEventListener('change',update));update();
})();
