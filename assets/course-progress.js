(function(){
  'use strict';
  var root=document.querySelector('[data-unit]')||document.querySelector('[data-chapter]');
  var prefix='laser-pfc-tp-v1:';
  var status=document.getElementById('save-status');
  var responses=Array.from(document.querySelectorAll('textarea[data-response]'));
  function tell(en,zh){if(status)status.textContent=en+' / '+zh;}
  function read(key){try{return localStorage.getItem(prefix+key);}catch(e){return null;}}
  function get(key){
    var current=read(key);if(current!==null&&current!==undefined)return current;
    var old=/^A-Q([123])$/.exec(key);
    if(old){var saved=read('C5-Q'+old[1]);if(saved!==null&&saved!==undefined){put(key,saved);return saved;}}
    return '';
  }
  function put(key,value){try{localStorage.setItem(prefix+key,value);return true;}catch(e){return false;}}
  responses.forEach(function(box){box.value=get(box.dataset.response);box.addEventListener('input',function(){
    var ok=put(box.dataset.response,box.value);
    tell(ok?'Draft saved in this browser; mastery awaits teacher review.':'Browser storage unavailable; copy or download your answers.',ok?'草稿已保存在本浏览器；掌握状态待教师审阅。':'浏览器存储不可用；请复制或下载回答。');
  });});
  function submission(){
    if(!root)return null;
    var missing=responses.filter(function(box){return !box.value.trim();});
    if(missing.length){tell('Complete all three responses before submitting for review.','请先完成三个回答，再提交审阅。');missing[0].focus();return null;}
    var title=document.querySelector('h1[lang="en"]').textContent;
    var appendix=root.dataset.unitKind==='appendix';
    return title+'\n\n'+responses.map(function(box){var article=box.closest('.defense');return article.dataset.defense+' — '+article.querySelector('h3[lang="en"]').textContent+'\n'+box.value.trim();}).join('\n\n')+'\n\nPlease review these explanations and mark this '+(appendix?'appendix':'chapter')+' mastered if all three show understanding.\n请审阅这些解释；若三个回答均体现理解，请将'+(appendix?'本附录':'本章')+'标记为已掌握。\n';
  }
  var copy=document.getElementById('copy-responses');
  if(copy)copy.addEventListener('click',async function(){var text=submission();if(!text)return;try{await navigator.clipboard.writeText(text);tell('Copied. Paste into the teaching chat for review.','已复制。请粘贴到教学对话中审阅。');}catch(e){
    var box=document.getElementById('submission-fallback');box.hidden=false;box.value=text;box.focus();box.select();tell('Select and copy the prepared text, or download it.','请选择并复制整理后的文本，或下载。');
  }});
  var download=document.getElementById('download-responses');
  if(download)download.addEventListener('click',function(){var text=submission();if(!text)return;var url=URL.createObjectURL(new Blob([text],{type:'text/plain;charset=utf-8'}));var a=document.createElement('a');a.href=url;a.download='Laser-PFC-TP-'+root.dataset.chapter+'-responses.txt';a.click();URL.revokeObjectURL(url);tell('Responses downloaded for review; this does not mark mastery.','回答已下载供审阅；此操作不会标记掌握。');});
  if(responses.length)tell('Answers stay in this browser until you copy or download them.','回答仅保留在本浏览器，直至您复制或下载。');
})();
