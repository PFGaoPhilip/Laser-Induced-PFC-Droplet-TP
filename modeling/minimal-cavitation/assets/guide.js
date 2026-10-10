(function(){
  const storageKey='minimal-cavitation-guide-progress-v1';
  const boxes=Array.from(document.querySelectorAll('input[data-step]'));
  let saved=[];
  try{saved=JSON.parse(localStorage.getItem(storageKey)||'[]')}catch(_error){}
  if(!Array.isArray(saved))saved=[];
  const completed=new Set(saved);
  function update(){
    const done=Array.from(completed);
    boxes.forEach(box=>box.checked=completed.has(box.dataset.step));
    boxes.forEach(box=>box.closest('.guide-step').classList.toggle('step-done',box.checked));
    document.querySelectorAll('[data-guide-progress]').forEach(label=>label.textContent=label.closest('.locale-pane').dataset.locale==='zh'?'已完成 '+done.length+' / 53 步':done.length+' of 53 steps completed');
    document.querySelectorAll('[data-guide-progress-bar]').forEach(bar=>bar.value=done.length);
    try{localStorage.setItem(storageKey,JSON.stringify(done))}catch(_error){}
  }
  boxes.forEach(box=>box.addEventListener('change',()=>{box.checked?completed.add(box.dataset.step):completed.delete(box.dataset.step);update()}));
  document.querySelectorAll('[data-reset-progress]').forEach(button=>button.addEventListener('click',()=>{completed.clear();update()}));
  document.querySelectorAll('.copy-block').forEach(button=>button.addEventListener('click',async function(){
    const text=button.nextElementSibling.innerText;
    const zh=button.closest('.locale-pane').dataset.locale==='zh';
    try{await navigator.clipboard.writeText(text);button.textContent=zh?'已复制':'Copied'}catch(_error){
      const range=document.createRange();range.selectNodeContents(button.nextElementSibling);
      const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);
      button.textContent=zh?'已选中文本，请按 Ctrl+C':'Text selected — press Ctrl+C';
    }
  }));
  update();
})();
