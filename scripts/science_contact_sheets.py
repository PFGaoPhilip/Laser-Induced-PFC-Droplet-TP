"""Make readable four-panel sheets from actual saved-PPTX renders."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import argparse


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('directory',type=Path)
    args=parser.parse_args()
    paths=sorted(args.directory.glob('slide-*.png'))
    destination=args.directory/'contact-sheets'
    destination.mkdir(exist_ok=True)
    font=ImageFont.truetype('arial.ttf',20)
    for start in range(0,len(paths),4):
        group=paths[start:start+4]
        tiles=[]
        for path in group:
            img=Image.open(path).convert('RGB')
            img.thumbnail((1000,850))
            tile=Image.new('RGB',(1020,890),'#d3dbe0')
            tile.paste(img,((1020-img.width)//2,32))
            ImageDraw.Draw(tile).text((12,4),path.name,fill='#111111',font=font)
            tiles.append(tile)
        sheet=Image.new('RGB',(2040,1780),'#d3dbe0')
        for i,tile in enumerate(tiles):sheet.paste(tile,((i%2)*1020,(i//2)*890))
        sheet.save(destination/f'sheet-{start//4+1:02}.png')
    print(destination, len(paths),'slides', (len(paths)+3)//4,'sheets')


if __name__=='__main__':main()
