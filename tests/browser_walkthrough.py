"""Browser integration test against a disposable real SQLite/HTTP server."""
import json, tempfile, threading, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import server
from playwright.sync_api import sync_playwright
with tempfile.TemporaryDirectory() as tmp:
 s=server(Path(tmp)/'browser.db',0);threading.Thread(target=s.serve_forever,daemon=True).start();base=f'http://127.0.0.1:{s.server_port}'
 with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=browser.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(base);page.wait_for_selector('#environment .card')
  page.locator('#action-form [name=text]').fill('Offer aggregate relief support pending access agreement')
  page.locator('#action-form [name=actor]').fill('PRIVATE CONTROL ACTOR')
  page.locator('#action-form [name=context_note]').fill('Lark port; agreement is a promise, not execution')
  page.locator('#action-form button[type=submit], #action-form button:not([type])').click()
  page.wait_for_function("document.getElementById('exchange-action').options.length===1")
  with page.expect_download() as dl:page.locator('#request').click()
  assert 'Offer aggregate relief' in Path(dl.value.path()).read_text()
  page.wait_for_function("document.querySelector('#requests').textContent.includes('Request ')")
  page.locator('#instructions').fill('SECRET HUMAN PREPARATION NOTE')
  page.locator('#sample').click();page.locator('#import-form button:not([type])').click();page.wait_for_function("document.querySelector('#results').textContent.includes('REVIEW ONLY')")
  page.locator('#import-form button:not([type])').click();page.wait_for_function("document.querySelector('#message').textContent.includes('Duplicate import')")
  page.locator('#context-form [name=text]').fill('Late agreement changes assumptions; access remains unexecuted')
  page.locator('#context-form button').click();page.wait_for_function("document.querySelector('#results').textContent.includes('STALE')")
  page.locator('#decision-result').select_option(index=1)
  for k,v in dict(recorder='Synthetic recorder',meeting='Synthetic consensus discussion',assessment='Political access may offset delay; confidence remains uncertain',effects='Aggregate support availability estimated; access execution not established',uncertainty='Economic response uncertain',relations='Bellwether agreement relates to Aster offer',carry_forward='Review actual access execution next discussion',stale_review='Team treats original aggregate estimate as conditional after late agreement',public='Public relief remains delayed',Aster='ASTER FEEDBACK ONLY: contribution conditional',Bellwether='BELLWETHER FEEDBACK ONLY: access promise needs execution').items():page.locator(f'#decision-form [name="{k}"]').fill(v)
  page.locator('#decision-form [name=consensus]').check();page.locator('#decision-form [name=director_approval]').check();page.locator('#decision-form button:not([type])').click()
  page.wait_for_selector('#decisions .card');page.get_by_role('button',name='Release captured audience accounts').click();page.wait_for_function("document.querySelector('#message').textContent.includes('Released 3')")
  # Player JSON and DOM must not contain other-cell intelligence, feedback or internal rationale.
  page.route('**/api/state?audience=Aster',lambda route: (page.wait_for_timeout(250),route.continue_()))
  page.locator('#view').select_option('Aster')
  assert page.locator('#environment .card').count()==0 and page.locator('#feedback .card').count()==0
  page.wait_for_function("document.querySelector('#control').hidden")
  page.wait_for_function("document.querySelector('#feedback').textContent.includes('ASTER FEEDBACK')")
  page.unroute('**/api/state?audience=Aster')
  body=page.locator('body').inner_text();assert 'BELLWETHER PRIVATE' not in body and 'BELLWETHER FEEDBACK' not in body and 'Political access may' not in body
  assert 'Political access may' not in page.content() and 'BELLWETHER PRIVATE' not in page.content()
  assert 'PRIVATE CONTROL ACTOR' not in page.content()
  assert page.locator('#instructions').input_value()==''
  for ident in ['exchange-action','decision-action','decision-result']: assert page.locator('#'+ident+' option').count()==0
  data=page.request.get(base+'/api/state?audience=Aster').text();assert 'BELLWETHER' not in data and 'Synthetic recorder' not in data
  assert page.request.post(base+'/api/actions',data={'text':'unauthorized demo write'},headers={'X-Prototype-View':'Aster'}).status==403
  page.locator('#view').select_option('control');page.wait_for_function("!document.querySelector('#control').hidden")
  page.get_by_role('button',name='Revise / correct').click();assert not page.locator('#decision-form [name=consensus]').is_checked()
  assert not page.locator('#decision-form [name=director_approval]').is_checked()
  page.locator('#decision-form [name=effects]').fill('Corrected aggregate consequence')
  page.locator('#decision-form [name=correction_reason]').fill('Later team review corrected estimate')
  page.locator('#decision-form [name=Aster]').fill('CORRECTED ASTER FEEDBACK: delay revised')
  page.locator('#decision-form [name=consensus]').check();page.locator('#decision-form [name=director_approval]').check();page.locator('#decision-form button:not([type])').click()
  page.wait_for_function("document.querySelector('#decisions').textContent.includes('v2')")
  page.get_by_role('button',name='Release captured audience accounts').click();page.wait_for_function("document.querySelector('#message').textContent.includes('Released 3')")
  with page.expect_download() as dl:page.locator('#handover').click()
  handover=json.loads(Path(dl.value.path()).read_text());d=next(r for r in handover['records'] if r['kind']=='decision');assert len(d['history'])==2 and d['data']['effects']=='Corrected aggregate consequence';assert 'Review actual access' in d['data']['carry_forward']
  page.reload();page.wait_for_function("document.querySelector('#decisions').textContent.includes('v2')")
  Path('artifacts').mkdir(exist_ok=True);page.screenshot(path='artifacts/controller.png',full_page=True)
  page.locator('#view').select_option('Aster');page.wait_for_function("document.querySelector('#feedback').textContent.includes('CORRECTED ASTER')");assert page.locator('#feedback').inner_text().count('Historical account · superseded')==2
  assert page.locator('#feedback').inner_text().count('Current released account')==2
  page.screenshot(path='artifacts/player-aster.png',full_page=True)
  assert not errors,errors;browser.close()
 s.shutdown();s.server_close()
print('PASS: browser action/export/mapped import/duplicate/stale review/consensus/verbal approval/release/player leakage/correction/handover/reload; no browser errors')
