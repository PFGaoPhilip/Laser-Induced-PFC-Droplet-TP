// Raster review of original SVG diagrams; no source figure or remote media editing.
'use strict';
const fs=require('fs');const path=require('path');
const sharp=require(process.env.SHARP_PATH||'sharp');
const root=path.resolve(__dirname,'..');
(async()=>{
  const es=JSON.parse(fs.readFileSync(path.join(root,'verification/equations.json'),'utf8'));
  const types=['sphere','energy','impulse','laser','phase','nucleation','array','jet','impact','film','cohesive','gel','timescale'];
  const selected=[...types.map(t=>es.find(e=>e.diagram.type===t)).filter(Boolean)];
  for(const id of ['C1-E20','C1-E28','C2-E09','C3-E22','C4-E07','C4-E08','C4-E13','C4-E40','C4-E41','C5-E01','C5-E07','C5-E18','C5-E20']){
    const eq=es.find(e=>e.id===id);if(eq&&!selected.some(e=>e.id===id))selected.push(eq);
  }
  const width=620,pad=24,header=34;
  const pages=[];
  for(let page=0;page*8<selected.length;page++){
  const chosen=selected.slice(page*8,page*8+8);
  let rows=[],height=pad;
  for(let i=0;i<chosen.length;i+=2){
    const pair=chosen.slice(i,i+2),buffers=[];
    for(const eq of pair){
      let buf=await sharp(path.join(root,'assets/figures',eq.id.toLowerCase()+'.svg')).resize({width}).png().toBuffer();
      let meta=await sharp(buf).metadata();buffers.push({buf,height:meta.height,eq});
    }
    rows.push({y:height,buffers});height+=Math.max(...buffers.map(b=>b.height))+pad+header;
  }
  const overall=2*width+3*pad;let layers=[];
  for(const row of rows)for(let j=0;j<row.buffers.length;j++){
    const b=row.buffers[j],x=pad+j*(width+pad);
    const title=Buffer.from(`<svg width="${width}" height="${header}"><rect width="100%" height="100%" fill="#09141d"/><text x="4" y="23" font-family="Arial" font-size="17" fill="#b4c7d2">${b.eq.id} — ${b.eq.diagram.type}</text></svg>`);
    layers.push({input:title,left:x,top:row.y},{input:b.buf,left:x,top:row.y+header});
  }
  const dest=path.join(root,'verification/diagram-review-'+String(page+1).padStart(2,'0')+'.png');
  await sharp({create:{width:overall,height,channels:3,background:'#09141d'}}).composite(layers).png().toFile(dest);
  pages.push({file:path.basename(dest),figures:chosen.map(e=>e.id),width:overall,height});
  }
  const result={pages,scope:'Raster contact sheets of original physical-variable SVGs for visual inspection.'};
  fs.writeFileSync(path.join(root,'verification/diagram-review.json'),JSON.stringify(result,null,2)+'\n');
  process.stdout.write(JSON.stringify(result));
})();
