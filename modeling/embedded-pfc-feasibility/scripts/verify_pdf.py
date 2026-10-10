"""Structural PDF checks plus a contact sheet for required visual inspection."""
import hashlib,json,re
from pathlib import Path
import fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]

def main():
    path=ROOT/'output/pdf/FINITE_PFC_DERIVATION.pdf';doc=fitz.open(path)
    pages=[];text='';fonts=set();local_links=0
    for i,p in enumerate(doc):
        t=p.get_text();text+=t
        assert len(t)>100,f'Unexpected near-empty page {i+1}'
        for x0,y0,x1,y1,*_ in p.get_text('blocks'):
            assert x0>=-1 and y0>=-1 and x1<=p.rect.width+1 and y1<=p.rect.height+1,(i+1,x0,y0,x1,y1)
        fonts.update(x[0] for x in p.get_fonts())
        for link in p.get_links():
            if link.get('file'):
                target=(path.parent/link['file']).resolve()
                assert ROOT in target.parents and target.exists(),f'Broken PDF dependency: {link}'
                local_links+=1
        pages.append(dict(page=i+1,characters=len(t),width_pt=p.rect.width,height_pt=p.rect.height))
    tags=set(re.findall(r'E\d{2}',text));assert {f'E{i:02d}' for i in range(1,33)}<=tags
    assert all(len(doc.extract_font(x)[3])>0 for x in fonts),'Unembedded PDF font'
    images=sorted((ROOT/'tmp/pdf').glob('page-*.png'))
    assert len(images)==len(doc)
    w,h=290,435;sheet=Image.new('RGB',(4*w,((len(images)+3)//4)*h),'#cbd1d3');draw=ImageDraw.Draw(sheet)
    for i,path0 in enumerate(images):
        im=Image.open(path0).convert('RGB');im.thumbnail((w-16,h-24))
        x=(i%4)*w+(w-im.width)//2;y=(i//4)*h+20
        sheet.paste(im,(x,y));draw.text(((i%4)*w+8,(i//4)*h+4),f'Page {i+1}',fill='black')
    sheet.save(ROOT/'tmp/pdf/contact_sheet.png')
    audit=dict(status='PASS',pages=len(doc),page_details=pages,equation_identifiers=sorted(tags),embedded_fonts=len(fonts),
               out_of_page_text_blocks=0,pdf_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
               latex_source_sha256=hashlib.sha256((ROOT/'DERIVATION.tex').read_bytes()).hexdigest(),
               resolved_local_pdf_links=local_links,
               visual_review='Pending visual inspection of the Poppler renders; structural checks alone do not establish layout quality.')
    (ROOT/'verification/PDF_AUDIT.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
    print({k:v for k,v in audit.items() if not isinstance(v,list)})

if __name__=='__main__':main()
