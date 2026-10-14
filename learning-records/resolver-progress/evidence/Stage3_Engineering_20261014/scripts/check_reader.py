"""Static portability checks; actual-browser evidence remains separately recorded."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
class Audit(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.remote_resources=[]; self.math=0; self.toggle=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='a' and 'href' in a: self.links.append(a['href'])
        if tag=='math': self.math+=1
        if tag=='button' and a.get('id')=='theme-toggle': self.toggle=True
        for k in ['src','href']:
            if k in a and tag!='a' and a[k].startswith(('http:','https:','//')): self.remote_resources.append(a[k])
p=ROOT/'READER.html'
a=Audit(); a.feed(p.read_text(encoding='utf-8'))
bad=[]
for x in set(a.links):
    u=urlsplit(x)
    if u.scheme or u.netloc: bad.append({'href':x,'reason':'nonrelative link'})
    elif u.path:
        target=(ROOT/unquote(u.path)).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file(): bad.append({'href':x,'reason':'missing or outside package'})
    elif u.fragment not in a.ids: bad.append({'href':x,'reason':'missing anchor'})
result={'check':'static reader portability, not browser QA','reader_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'links':len(a.links),'unique_links':len(set(a.links)),'bad_links':bad,'remote_resources':a.remote_resources,'mathml_equations':a.math,'day_night_toggle':a.toggle,'status':'PASS' if not bad and not a.remote_resources and a.math==2 and a.toggle else 'FAIL'}
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['status']=='PASS' else 1)
