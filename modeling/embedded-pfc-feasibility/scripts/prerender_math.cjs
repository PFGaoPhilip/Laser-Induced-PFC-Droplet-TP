const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const katex = require(path.join(root, 'assets', 'vendor', 'katex', 'katex.min.js'));
const requests = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const rendered = requests.map(item => ({token:item.token, html:katex.renderToString(item.tex, {
  displayMode:item.display, throwOnError:true, strict:'error', output:'htmlAndMathml'
})}));
fs.writeFileSync(process.argv[3],JSON.stringify(rendered));
process.stdout.write(JSON.stringify({expressions:rendered.length,displays:requests.filter(x=>x.display).length,errors:0}));
