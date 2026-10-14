const fs = require('fs');
const path = require('path');
const katex = require(path.join(__dirname,'../assets/vendor/katex/katex.min.js'));
const filename = process.argv[2];
let source = fs.readFileSync(filename,'utf8');
let count = 0;
source = source.replace(/<(div|span) class="([^"]*\bmath\b[^"]*)" data-tex="([A-Za-z0-9+/=]+)"><\/\1>/g, (_match, tag, classes, data) => {
  const display=classes.split(/\s+/).includes('display');
  const tex = Buffer.from(data,'base64').toString('utf8');
  count++;
  let rendered;
  try {
    rendered = katex.renderToString(tex,{displayMode:!!display,throwOnError:true,strict:'error'});
  } catch (error) {
    console.error('KATEX_EXPRESSION_'+count+': '+error.message+'\n'+tex);
    process.exit(1);
  }
  return '<'+tag+' class="'+classes+'">'+rendered+'</'+tag+'>';
});
if (source.includes('data-tex=')) throw new Error('Unrendered mathematical slot remains');
fs.writeFileSync(filename,source,'utf8');
console.log('KATEX_RENDERED_EXPRESSIONS='+count);
