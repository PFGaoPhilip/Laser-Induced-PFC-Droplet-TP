// Rendering through stdin/stdout keeps essential mathematics available offline.
'use strict';
const fs=require('fs');
const path=require('path');
const katex=require(path.resolve(__dirname,'../assets/vendor/katex/katex.js'));
let raw='';process.stdin.setEncoding('utf8');
process.stdin.on('data',s=>raw+=s);
process.stdin.on('end',()=>{
  const input=JSON.parse(raw);
  const result=input.map(x=>katex.renderToString(x.tex,{displayMode:!!x.display,throwOnError:true,strict:'error',trust:false,output:'htmlAndMathml'}));
  process.stdout.write(JSON.stringify(result));
});
