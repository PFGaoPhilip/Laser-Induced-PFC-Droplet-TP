'use strict';
// Execute the shipped scripts against small DOM adapters for actual storage,
// clipboard and theme failure paths. This is not a visual-browser audit.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'..'),checks=[];
function check(name,fn){fn();checks.push(name);}
function el(){return {children:[],attributes:{},handlers:{},value:'',hidden:true,
  appendChild(x){this.children.push(x);},setAttribute(k,v){this.attributes[k]=v;},
  getAttribute(k){return this.attributes[k];},addEventListener(k,v){this.handlers[k]=v;},
  focus(){this.focused=true;},select(){this.selected=true;}};}
function theme(query='',saved=null,denied=false){
 const attrs={},store={'laser-pfc-tp-theme':saved},registry={},ready={};
 const a=el(),external=el();a.attributes.href='02-optical-heating-and-finite-pfc-inventory.html#heating';external.attributes.href='https://webbook.nist.gov/';
 const context={URL,URLSearchParams,location:{href:'https://example.test/course/chapters/01.html'+query,search:query},
   localStorage:{getItem(k){if(denied)throw Error('denied');return store[k];},setItem(k,v){if(denied)throw Error('denied');store[k]=v;}},
   document:{documentElement:{setAttribute(k,v){attrs[k]=v;}},readyState:'loading',getElementById:k=>registry[k],
    querySelectorAll:()=>[a,external],createElement:el,addEventListener(k,v){ready[k]=v;},
    body:{firstChild:null,insertBefore(x){x.children.forEach(b=>registry[b.id]=b);}}}};
 vm.runInNewContext(fs.readFileSync(path.join(root,'assets/course-theme.js'),'utf8'),context);ready.DOMContentLoaded();
 return {attrs,store,a,external,button:registry['theme-toggle']};
}
function progress(saved={},denied=false,clipboardDenied=false,appendix=false){
 const store={...saved},status=el(),fallback=el(),copy=el(),download=el(),copied=[];
 const questionPrefix=appendix?'A-Q':'C1-Q';
 const boxes=[1,2,3].map(i=>{const x=el();x.dataset={response:questionPrefix+i};x.closest=()=>({dataset:{defense:questionPrefix+i},querySelector:()=>({textContent:'Defense '+i})});return x;});
 const registry={'save-status':status,'submission-fallback':fallback,'copy-responses':copy,'download-responses':download};
 const context={Blob,URL:{createObjectURL:()=> 'blob:response-check',revokeObjectURL(){}},
  localStorage:{getItem(k){if(denied)throw Error('denied');return store[k];},setItem(k,v){if(denied)throw Error('denied');store[k]=v;}},
  navigator:{clipboard:{async writeText(x){if(clipboardDenied)throw Error('denied');copied.push(x);}}},
  document:{querySelector(q){if(q==='[data-chapter]'||q==='[data-unit]')return {dataset:{chapter:appendix?'A':'C01',unitKind:appendix?'appendix':'chapter'}};return {textContent:appendix?'Hydrogel versus liquid':'Cavity pressure'};},
   querySelectorAll:()=>boxes,getElementById:k=>registry[k],createElement(){const a=el();a.click=()=>{context.lastDownload=a;};return a;}}};
 vm.runInNewContext(fs.readFileSync(path.join(root,'assets/course-progress.js'),'utf8'),context);
 return {store,status,fallback,copy,download,boxes,copied,context};
}
(async()=>{
 const t=theme();check('Default night',()=>assert.equal(t.attrs['data-theme'],'dark'));
 t.button.handlers.click();check('Day toggle and ARIA',()=>{assert.equal(t.attrs['data-theme'],'light');assert.equal(t.button.attributes['aria-pressed'],'true');});
 check('Choice persistence',()=>assert.equal(t.store['laser-pfc-tp-theme'],'light'));
 check('Relative link and anchor retained',()=>assert.equal(t.a.attributes.href,'02-optical-heating-and-finite-pfc-inventory.html?theme=light#heating'));
 check('External scholarly link unchanged',()=>assert.equal(t.external.attributes.href,'https://webbook.nist.gov/'));
 t.button.handlers.click();check('Night toggle',()=>assert.equal(t.attrs['data-theme'],'dark'));
 check('Saved mode restored',()=>assert.equal(theme('','light').attrs['data-theme'],'light'));
 check('URL mode overrides saved mode',()=>assert.equal(theme('?theme=dark','light').attrs['data-theme'],'dark'));
 const td=theme('?theme=light',null,true);td.button.handlers.click();check('Storage-denied theme remains usable',()=>assert.equal(td.attrs['data-theme'],'dark'));
 const p=progress({'laser-pfc-tp-v1:C1-Q1':'A saved explanation.'});
 check('Saved learner explanation restored',()=>assert.equal(p.boxes[0].value,'A saved explanation.'));
 p.boxes[0].value='Pressure accelerates liquid.';p.boxes[0].handlers.input();
 check('Editing persists exact response',()=>assert.equal(p.store['laser-pfc-tp-v1:C1-Q1'],'Pressure accelerates liquid.'));
 await p.copy.handlers.click();check('Missing explanations prevent empty submission',()=>{assert.equal(p.copied.length,0);assert(p.boxes[1].focused);});
 p.boxes[1].value='Finite energy constrains mass-weighted velocity.';p.boxes[2].value='The spatial impulse gradient drives velocity.';
 await p.copy.handlers.click();check('Three explanations copied with question IDs',()=>{assert.equal(p.copied.length,1);for(const id of ['C1-Q1','C1-Q2','C1-Q3'])assert(p.copied[0].includes(id));});
 check('Copy requests semantic review rather than granting mastery',()=>assert(p.copied[0].includes('if all three show understanding')));
 const pd=progress({},true,true);pd.boxes.forEach((b,i)=>b.value='Explanation '+i);pd.boxes[0].handlers.input();
 check('Storage failure tells learner to export',()=>assert(pd.status.textContent.includes('storage unavailable')));
 await pd.copy.handlers.click();check('Clipboard failure reveals selectable full text',()=>{assert.equal(pd.fallback.hidden,false);assert(pd.fallback.selected);assert(pd.fallback.value.includes('C1-Q3'));});
 pd.download.handlers.click();check('Download available without clipboard or storage',()=>assert.equal(pd.context.lastDownload.download,'Laser-PFC-TP-C01-responses.txt'));
 const pa=progress({'laser-pfc-tp-v1:C5-Q1':'A previous hydrogel draft.'},false,false,true);
 check('Old hydrogel draft migrated into Appendix A',()=>{assert.equal(pa.boxes[0].value,'A previous hydrogel draft.');assert.equal(pa.store['laser-pfc-tp-v1:A-Q1'],'A previous hydrogel draft.');});
 const current=progress({'laser-pfc-tp-v1:C5-Q1':'Older draft.','laser-pfc-tp-v1:A-Q1':'Newer appendix draft.'},false,false,true);
 check('Existing appendix draft takes precedence',()=>assert.equal(current.boxes[0].value,'Newer appendix draft.'));
 const cleared=progress({'laser-pfc-tp-v1:C5-Q1':'Older draft.','laser-pfc-tp-v1:A-Q1':''},false,false,true);
 check('Cleared appendix draft is not resurrected',()=>assert.equal(cleared.boxes[0].value,''));
 pa.boxes[1].value='Network work is finite.';pa.boxes[2].value='Transfer requires useful load.';
 await pa.copy.handlers.click();check('Appendix export requests appendix review',()=>{assert(pa.copied[0].includes('mark this appendix mastered'));assert(pa.copied[0].includes('A-Q1'));assert(!pa.copied[0].includes('C5-Q1'));});
 pa.download.handlers.click();check('Appendix download is labeled A',()=>assert.equal(pa.context.lastDownload.download,'Laser-PFC-TP-A-responses.txt'));
 const result={status:'passed',checks_count:checks.length,checks,scope:'Executable DOM-adapter checks for shipped theme and response scripts; not a visual-browser audit or learner-mastery decision.'};
 fs.writeFileSync(path.join(root,'verification/interface-audit.json'),JSON.stringify(result,null,2)+'\n');
 process.stdout.write(JSON.stringify({status:result.status,checks_count:checks.length}));
})().catch(e=>{process.stderr.write(e.stack);process.exitCode=1;});
