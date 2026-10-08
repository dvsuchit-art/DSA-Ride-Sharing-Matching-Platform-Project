import json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse,parse_qs
from .engine import scenario,compare_solvers
ROOT=Path(__file__).resolve().parent.parent
class H(BaseHTTPRequestHandler):
 def send(self,s,b,t):
  b=b.encode(); self.send_response(s); self.send_header("Content-Type",t); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
 def do_GET(self):
  p=urlparse(self.path)
  if p.path=="/api/match":
   q=parse_qs(p.query); n=max(2,min(100,int(q.get("n",["6"])[0]))); seed=int(q.get("seed",["7"])[0])
   d,r=scenario(n,seed); self.send(200,json.dumps(compare_solvers(d,r)),"application/json"); return
  f=ROOT/"frontend"/("index.html" if p.path=="/" else p.path.lstrip("/"))
  if not f.is_file(): self.send(404,"Not found","text/plain"); return
  self.send(200,f.read_text(encoding="utf-8"),"text/html")
if __name__=="__main__":
 print("RideSim: http://127.0.0.1:8000"); ThreadingHTTPServer(("127.0.0.1",8000),H).serve_forever()
