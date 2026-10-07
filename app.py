"""Synthetic relief-access prototype. Local demonstration, not a security boundary."""
import argparse, csv, hashlib, io, json, math, os, sqlite3, uuid
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
AUDIENCES = ('public', 'Aster', 'Bellwether')

class Problem(Exception):
    def __init__(self, message, status=400): self.message, self.status = message, status

class Store:
    def __init__(self, path):
        self.path = str(path)
        with self.connect() as c:
            c.executescript('CREATE TABLE IF NOT EXISTS records(id TEXT PRIMARY KEY, kind TEXT, data TEXT, version INTEGER); CREATE TABLE IF NOT EXISTS history(id TEXT, version INTEGER, data TEXT, at TEXT); CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY, value INTEGER); INSERT OR IGNORE INTO meta VALUES("context",1);')
            if not c.execute('SELECT 1 FROM records').fetchone():
                for row in json.loads((ROOT/'fixtures/baseline.json').read_text()): self.save(c, row['kind'], row['data'], row['id'])
    def connect(self):
        c = sqlite3.connect(self.path); c.row_factory = sqlite3.Row; return c
    def save(self, c, kind, data, ident=None, expected=None):
        ident = ident or uuid.uuid4().hex[:12]
        old = c.execute('SELECT * FROM records WHERE id=?', (ident,)).fetchone()
        if old and (not isinstance(expected,int) or isinstance(expected,bool)): raise Problem('Corrections require the current record version.',409)
        if expected is not None and (not old or old['version'] != expected): raise Problem('Record changed; reload before correcting.',409)
        if old and old['kind'] != kind: raise Problem('Cannot change record category.',409)
        version = old['version']+1 if old else 1
        c.execute('INSERT OR REPLACE INTO records VALUES(?,?,?,?)',(ident,kind,json.dumps(data),version))
        c.execute('INSERT INTO history VALUES(?,?,?,?)',(ident,version,json.dumps(data),datetime.now(timezone.utc).isoformat()))
        return dict(id=ident,kind=kind,data=data,version=version)
    def get(self,c,ident,kind=None):
        r=c.execute('SELECT * FROM records WHERE id=?',(ident,)).fetchone()
        if not r or (kind and r['kind']!=kind): raise Problem('Record not found.',404)
        return dict(id=r['id'],kind=r['kind'],version=r['version'],data=json.loads(r['data']))
    def context(self,c): return c.execute('SELECT value FROM meta WHERE key="context"').fetchone()[0]
    def stale(self,c,result):
        d=result['data']; req=self.get(c,d['request_id'],'request')['data']; action=self.get(c,req['action_id'],'action')
        return req['context_version']!=self.context(c) or req['action_version']!=action['version']
    def state(self,audience='control'):
        if audience not in ('control',)+AUDIENCES: raise Problem('Unknown audience.')
        with self.connect() as c:
            rows=[dict(id=r['id'],kind=r['kind'],version=r['version'],data=json.loads(r['data'])) for r in c.execute('SELECT * FROM records ORDER BY rowid')]
            if audience!='control':
                # Deliberately construct a safe output; never send the controller graph to players.
                visible=[]
                for r in rows:
                    d=r['data']
                    if r['kind'] in ('scenario','environment') and audience in d.get('audiences',[]):
                        visible.append(dict(kind=r['kind'],title=d.get('title'),text=d.get('text')))
                    if r['kind']=='release' and d['audience'] in ('public',audience):
                        superseded=any(other['kind']=='release' and other['data']['decision_id']==d['decision_id'] and other['data']['audience']==d['audience'] and other['data']['decision_version']>d['decision_version'] for other in rows)
                        visible.append(dict(kind='feedback',text=d['text'],issued=d['issued'],correction=d['correction'],revision=d['decision_version'],superseded=superseded))
                return dict(audience=audience,records=visible)
            for r in rows:
                if r['kind']=='result': r['stale']=self.stale(c,r)
                r['history']=[dict(version=h['version'],data=json.loads(h['data']),at=h['at']) for h in c.execute('SELECT * FROM history WHERE id=? ORDER BY version',(r['id'],))]
            return dict(audience=audience,context_version=self.context(c),records=rows)
    def mutate(self,route,b):
        if not isinstance(b,dict): raise Problem('Expected a JSON object.')
        text_fields=('text','actor','context_note','title','record_type','instructions','assessment','effects','uncertainty','relations','carry_forward','recorder','meeting','approval_note','stale_review','correction_reason','action_id','result_id','decision_id','id')
        if any(k in b and not isinstance(b[k],str) for k in text_fields): raise Problem('Record content and identifiers must be text.')
        if 'feedback' in b and (not isinstance(b['feedback'],dict) or any(not isinstance(v,str) for v in b['feedback'].values())): raise Problem('Feedback must map audiences to text.')
        with self.connect() as c:
            if route=='actions':
                if not str(b.get('text','')).strip(): raise Problem('Enter an open-ended action.')
                d=dict(text=b['text'],actor=b.get('actor',''),context_version=self.context(c),context_note=b.get('context_note',''))
                return self.save(c,'action',d,b.get('id'),b.get('expected_version'))
            if route=='context':
                if not b.get('text','').strip(): raise Problem('Enter context or actual communication.')
                if b.get('kind') not in ('scenario','communication'): raise Problem('Choose scenario context or actual communication; claims are not established effects.')
                d=dict(title=b.get('title','Context update'),text=b['text'],audiences=['control'],record_type=b.get('record_type','reported claim/promise'))
                r=self.save(c,b['kind'],d)
                c.execute('UPDATE meta SET value=value+1 WHERE key="context"'); return r
            if route=='requests':
                a=self.get(c,b['action_id'],'action')
                d=dict(action_id=a['id'],action_version=a['version'],context_version=self.context(c),action=a['data']['text'],context_note=a['data']['context_note'],instructions=b.get('instructions','Human translation required; aggregate availability/delay only.'))
                req=self.save(c,'request',d)
                out=io.StringIO(); w=csv.writer(out);w.writerow(['request_id','action_id','action_version','context_version','action','context_note','instructions']);w.writerow([req['id'],a['id'],a['version'],d['context_version'],d['action'],d['context_note'],d['instructions']]);req['csv']=out.getvalue();return req
            if route=='imports':
                raw=b.get('csv',''); mapping=b.get('mapping',{})
                fields=['request_id','availability','delay_days','note']
                if not isinstance(raw,str) or not isinstance(mapping,dict) or any(not isinstance(v,str) for v in mapping.values()) or set(mapping)!=set(fields) or len(set(mapping.values()))!=4: raise Problem('Mapping must name four distinct columns: request_id, availability, delay_days, note.')
                try:
                    reader=csv.DictReader(io.StringIO(raw),strict=True); rows=list(reader)
                    if len(rows)!=1 or not reader.fieldnames or len(set(reader.fieldnames))!=len(reader.fieldnames) or any(v not in reader.fieldnames for v in mapping.values()) or None in rows[0] or any(rows[0].get(v) is None for v in mapping.values()): raise ValueError()
                    row=rows[0]; req=self.get(c,row[mapping['request_id']],'request')
                    availability=float(row[mapping['availability']]); delay=float(row[mapping['delay_days']])
                    if not math.isfinite(availability) or not 0<=availability<=1 or not math.isfinite(delay) or delay<0: raise ValueError()
                except (ValueError,TypeError,KeyError,csv.Error): raise Problem('Expected one complete CSV row; availability is 0–1 and delay_days is nonnegative. No tool compatibility implied.')
                fingerprint=hashlib.sha256(json.dumps(dict(raw=raw,mapping=mapping),sort_keys=True).encode()).hexdigest()
                for old in c.execute('SELECT * FROM records WHERE kind="result"'):
                    if json.loads(old['data'])['fingerprint']==fingerprint: return dict(duplicate=True,id=old['id'],message='Duplicate import retained once; no state effect applied.')
                d=dict(request_id=req['id'],availability=availability,delay_days=delay,note=row[mapping['note']],original_csv=raw,mapping=mapping,fingerprint=fingerprint,source='Synthetic manual CSV; not AFSIM/SWIFT compatible')
                result=self.save(c,'result',d);result['stale']=self.stale(c,result);return result
            if route=='decisions':
                if not b.get('assessment','').strip() or not b.get('recorder','').strip(): raise Problem('Record the assessment and who captured it.')
                action=self.get(c,b['action_id'],'action')
                result=None
                if b.get('result_id'): result=self.get(c,b['result_id'],'result')
                if result and self.get(c,result['data']['request_id'],'request')['data']['action_id'] != b['action_id']: raise Problem('Imported evidence belongs to another action.')
                if result and self.stale(c,result) and not b.get('stale_review','').strip(): raise Problem('Stale evidence: record how the team treated changed assumptions; no automatic application.')
                old=self.get(c,b['id'],'decision') if b.get('id') else None
                if old and not b.get('correction_reason','').strip(): raise Problem('Explain the correction; the original remains in history.')
                d={k:b.get(k,'') for k in ('action_id','result_id','assessment','effects','uncertainty','relations','carry_forward','recorder','meeting','approval_note','stale_review','correction_reason')}
                d.update(status='approved determination' if b.get('consensus') is True and b.get('director_approval') is True else 'draft; effects are proposed',consensus=b.get('consensus') is True,director_approval=b.get('director_approval') is True,feedback={a:b.get('feedback',{}).get(a,'') for a in AUDIENCES},context_version=self.context(c),action_version=action['version'])
                return self.save(c,'decision',d,b.get('id'),b.get('expected_version'))
            if route=='releases':
                dec=self.get(c,b['decision_id'],'decision');d=dec['data']
                if not(d['consensus'] and d['director_approval']): raise Problem('Team consensus and reported verbal director approval are needed before releasing this decision.')
                # Approval is bound to captured context. Context changes require a reviewed decision revision.
                if d['context_version']!=self.context(c) or d.get('action_version')!=self.get(c,d['action_id'],'action')['version']: raise Problem('Decision context changed; review/correct and capture approval again before release.',409)
                if b.get('expected_version')!=dec['version']: raise Problem('Decision changed; reload before release.',409)
                existing=[json.loads(x['data']) for x in c.execute('SELECT data FROM records WHERE kind="release"')]
                if any(x['decision_id']==dec['id'] and x['decision_version']==dec['version'] for x in existing): return dict(duplicate=True,message='This decision revision is already released.')
                issued=datetime.now(timezone.utc).isoformat();released=[]
                for audience in AUDIENCES:
                    if d['feedback'][audience].strip(): released.append(self.save(c,'release',dict(decision_id=dec['id'],decision_version=dec['version'],audience=audience,text=d['feedback'][audience],issued=issued,correction=dec['version']>1,recorder=d['recorder'])))
                if not released: raise Problem('Enter at least one audience feedback account.')
                return dict(released=len(released))
            raise Problem('Unknown operation.',404)

class Handler(BaseHTTPRequestHandler):
    def respond(self,status,data,ctype='application/json'):
        raw=json.dumps(data).encode() if ctype=='application/json' else data
        self.send_response(status);self.send_header('Content-Type',ctype);self.send_header('Content-Length',str(len(raw)));self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(raw)
    def do_GET(self):
        from urllib.parse import urlparse,parse_qs
        url=urlparse(self.path)
        try:
            if url.path=='/api/state': return self.respond(200,self.server.store.state(parse_qs(url.query).get('audience',['control'])[0]))
            names={'/':'index.html','/app.js':'app.js','/style.css':'style.css'}
            name=names.get(url.path)
            if not name: raise Problem('Not found.',404)
            ctype={'html':'text/html; charset=utf-8','js':'text/javascript; charset=utf-8','css':'text/css; charset=utf-8'}[name.split('.')[-1]]
            self.respond(200,(ROOT/'static'/name).read_bytes(),ctype)
        except Problem as e:self.respond(e.status,dict(error=e.message))
    def do_POST(self):
        try:
            if self.headers.get('X-Prototype-View')!='control': raise Problem('Demo player views are read-only.',403)
            size=int(self.headers.get('Content-Length','0'))
            if not 0<size<=100000:raise Problem('Prototype request too large.',413)
            b=json.loads(self.rfile.read(size));result=self.server.store.mutate(self.path.removeprefix('/api/'),b);self.respond(200,result)
        except Problem as e:self.respond(e.status,dict(error=e.message))
        except (ValueError,TypeError,KeyError,json.JSONDecodeError):self.respond(400,dict(error='Invalid request.'))
    def log_message(self,*args):pass

def server(path,port=8000):
    s=ThreadingHTTPServer(('127.0.0.1',port),Handler);s.store=Store(path);return s
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--db',default='prototype.sqlite3');p.add_argument('--port',type=int,default=8000);a=p.parse_args()
    s=server(a.db,a.port);print(f'Synthetic prototype: http://127.0.0.1:{s.server_port}',flush=True);s.serve_forever()
