// Pure DOM-event logic regression. Does not claim an actual browser rendering.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'..');
const states=JSON.parse(fs.readFileSync(path.join(root,'data','reader_states.json'),'utf8'));
class Element {
  constructor(id){this.id=id;this.handlers={};this.attributes={};this.dataset={};this.hidden=false;this.value='';this.textContent='';this.innerHTML='';}
  addEventListener(name,callback){this.handlers[name]=callback;}
  setAttribute(name,value){this.attributes[name]=value;}
  getAttribute(name){return this.attributes[name];}
  dispatch(name){this.handlers[name]();}
}
const ids=['theme-toggle','selector','fluid','diameter','modulus','state-output','state-data','comparison','derivation','handoff','sources'];
const el=Object.fromEntries(ids.map(id=>[id,new Element(id)]));
el['state-data'].textContent=JSON.stringify(states);el.fluid.value='n-Perfluoropentane';el.diameter.value='0.6';el.modulus.value='20';
const docs=['comparison','derivation','handoff','sources'].map(id=>el[id]);
const buttons=docs.map(d=>{const e=new Element(d.id+'-button');e.dataset.doc=d.id;return e;});
const links=docs.map(d=>{const e=new Element(d.id+'-link');e.attributes.href='#'+d.id;return e;});
const document={documentElement:{dataset:{}},getElementById:id=>el[id],querySelectorAll:q=>q==='.document'?docs:q==='[data-doc]'?buttons:links};
const store={};const context={document,localStorage:{getItem:k=>store[k],setItem:(k,v)=>store[k]=v},
  location:{hash:''},history:{replaceState:()=>{}},window:{addEventListener:()=>{}},console};
vm.runInNewContext(fs.readFileSync(path.join(root,'assets','reader.js'),'utf8'),context);
let scenarios=0;
assert(el['state-output'].innerHTML.includes('339.79 K'));scenarios++;
for(const s of states){
  el.fluid.value=s.fluid;el.diameter.value=String(s.diameter_um);el.modulus.value=String(s.G_kPa);el.fluid.dispatch('change');
  assert(el['state-output'].innerHTML.includes(s.T_K.toFixed(2)+' K'));
  assert(el['state-output'].innerHTML.includes((100*s.vapor_fraction).toFixed(2)+'%'));scenarios++;
}
el['theme-toggle'].dispatch('click');assert(document.documentElement.dataset.theme==='night');assert(store['pfc-theme']==='night');scenarios++;
el['theme-toggle'].dispatch('click');assert(document.documentElement.dataset.theme==='day');scenarios++;
for(let i=0;i<buttons.length;i++){
  buttons[i].dispatch('click');assert(docs.filter(x=>!x.hidden).length===1);assert(!docs[i].hidden);assert(el.selector.hidden===(i!==0));scenarios++;
}
links[1].dispatch('click');assert(!el.derivation.hidden);scenarios++;
const result={status:'PASS',scenarios,selector_states:states.length,theme_and_document_events:true,
  scope:'Pure JavaScript/event logic with a minimal DOM test double; no CSS/layout or real-browser rendering claim.',
  browser_inspection:'Unavailable: cua inventory returned no enabled apps or browsers.'};
fs.writeFileSync(path.join(root,'verification','READER_LOGIC_AUDIT.json'),JSON.stringify(result,null,2));
process.stdout.write(JSON.stringify(result)+'\n');
