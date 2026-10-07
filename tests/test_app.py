import json,tempfile,unittest
from pathlib import Path
from app import Store,Problem
class Workflow(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.path=Path(self.tmp.name)/'test.db';self.s=Store(self.path)
  self.action=self.s.mutate('actions',dict(text='Offer relief support',actor='Aster',context_note='Conditional access'))
  self.req=self.s.mutate('requests',dict(action_id=self.action['id']))
  self.csv=f"job,capacity,days,assumption\n{self.req['id']},0.55,3,Access unconfirmed\n"
  self.mapping=dict(request_id='job',availability='capacity',delay_days='days',note='assumption')
 def tearDown(self): self.tmp.cleanup()
 def imported(self): return self.s.mutate('imports',dict(csv=self.csv,mapping=self.mapping))
 def decision(self,**kwargs):
  b=dict(action_id=self.action['id'],recorder='Recorder',assessment='Human economic/diplomatic assessment',effects='Established aggregate effect',carry_forward='Access promise not execution',consensus=True,director_approval=True,feedback=dict(public='Public account',Aster='Aster feedback',Bellwether='Bellwether feedback'));b.update(kwargs);return self.s.mutate('decisions',b)
 def test_persistence_and_request_reuse(self):
  self.assertIn('Offer relief support',self.req['csv']);self.assertEqual(Store(self.path).state()['context_version'],1)
  self.assertTrue(any(r['id']==self.action['id'] for r in Store(self.path).state()['records']))
 def test_duplicate_original_retained(self):
  first=self.imported();second=self.imported();self.assertTrue(second['duplicate']);self.assertEqual(first['id'],second['id']);self.assertEqual(first['data']['original_csv'],self.csv)
 def test_explicit_mapping_invalid_numeric(self):
  for value in ['nan','1.5','-1']:
   with self.assertRaises(Problem):self.s.mutate('imports',dict(csv=self.csv.replace('0.55',value),mapping=self.mapping))
 def test_stale_after_context_and_action_correction(self):
  result=self.imported();self.assertFalse(result['stale'])
  self.s.mutate('actions',dict(id=self.action['id'],expected_version=1,text='Corrected action'))
  self.assertTrue(next(r for r in self.s.state()['records'] if r['id']==result['id'])['stale'])
  with self.assertRaises(Problem):self.decision(result_id=result['id'])
  self.assertTrue(self.decision(result_id=result['id'],stale_review='Team disregarded outdated estimate'))
 def test_context_staleness_and_release_guard(self):
  d=self.decision();self.s.mutate('context',dict(kind='communication',text='Late conditional agreement'))
  self.assertTrue(self.imported()['stale'])
  with self.assertRaises(Problem):self.s.mutate('releases',dict(decision_id=d['id'],expected_version=1))
 def test_governance_release_and_projection(self):
  d=self.decision(director_approval=False)
  with self.assertRaises(Problem):self.s.mutate('releases',dict(decision_id=d['id'],expected_version=1))
  d=self.decision();self.s.mutate('releases',dict(decision_id=d['id'],expected_version=1))
  a=json.dumps(self.s.state('Aster'));self.assertIn('ASTER PRIVATE',a);self.assertNotIn('BELLWETHER PRIVATE',a);self.assertNotIn('Human economic',a);self.assertNotIn('Recorder',a);self.assertNotIn('Bellwether feedback',a)
  public=json.dumps(self.s.state('public'));self.assertNotIn('PRIVATE',public);self.assertNotIn('Aster feedback',public)
 def test_correction_history_handover_release(self):
  d=self.decision();self.s.mutate('releases',dict(decision_id=d['id'],expected_version=1))
  revised=self.decision(id=d['id'],expected_version=1,correction_reason='New information',effects='Corrected effect',feedback=dict(public='Correction account',Aster='Corrected Aster'))
  self.s.mutate('releases',dict(decision_id=d['id'],expected_version=2))
  record=next(r for r in self.s.state()['records'] if r['id']==d['id']);self.assertEqual(len(record['history']),2);self.assertEqual(record['history'][0]['data']['effects'],'Established aggregate effect');self.assertEqual(record['data']['effects'],'Corrected effect')
  self.assertIn('Access promise not execution',record['data']['carry_forward']);self.assertIn('Correction account',json.dumps(self.s.state('public')))
  accounts=[r for r in self.s.state('public')['records'] if r['kind']=='feedback'];self.assertEqual([r['superseded'] for r in accounts],[True,False]);self.assertEqual([r['revision'] for r in accounts],[1,2])
 def test_optimistic_conflict_and_repeat_release(self):
  with self.assertRaises(Problem):self.s.mutate('actions',dict(id=self.action['id'],expected_version=4,text='Lost update'))
  d=self.decision();self.s.mutate('releases',dict(decision_id=d['id'],expected_version=1));self.assertTrue(self.s.mutate('releases',dict(decision_id=d['id'],expected_version=1))['duplicate'])
 def test_wrong_record_category_and_evidence_link(self):
  with self.assertRaises(Problem):self.s.mutate('actions',dict(id='road',expected_version=1,text='Overwrite scenario'))
  result=self.imported();other=self.s.mutate('actions',dict(text='Different player action'))
  with self.assertRaises(Problem):self.decision(action_id=other['id'],result_id=result['id'])
 def test_release_after_action_correction_requires_review(self):
  d=self.decision();self.s.mutate('actions',dict(id=self.action['id'],expected_version=1,text='Changed offer'))
  with self.assertRaises(Problem):self.s.mutate('releases',dict(decision_id=d['id'],expected_version=1))
  corrected=self.decision(id=d['id'],expected_version=1,correction_reason='Reviewed changed offer')
  self.assertEqual(corrected['data']['action_version'],2)
  self.assertEqual(self.s.mutate('releases',dict(decision_id=d['id'],expected_version=2))['released'],3)
 def test_correction_requires_version(self):
  with self.assertRaises(Problem):self.s.mutate('actions',dict(id=self.action['id'],text='Unversioned overwrite'))
  self.assertEqual(next(r for r in self.s.state()['records'] if r['id']==self.action['id'])['version'],1)
 def test_malformed_csv_mapping_unknown_request_no_partial_records(self):
  bad=[dict(csv=self.csv.rsplit(',',1)[0],mapping=self.mapping),dict(csv='job,capacity,days,assumption\n"unterminated',mapping=self.mapping),dict(csv=self.csv,mapping=[]),dict(csv=self.csv,mapping=dict(self.mapping,note=['bad'])),dict(csv=self.csv.replace(self.req['id'],'unknown'),mapping=self.mapping)]
  for b in bad:
   with self.assertRaises(Problem):self.s.mutate('imports',b)
  self.assertFalse(any(r['kind']=='result' for r in self.s.state()['records']))
 def test_draft_effects_and_nontext_payload(self):
  d=self.decision(consensus=False);self.assertEqual(d['data']['status'],'draft; effects are proposed')
  with self.assertRaises(Problem):self.s.mutate('actions',dict(text=[]))
  with self.assertRaises(Problem):self.s.mutate('decisions',dict(assessment='test',recorder='r',feedback=[]))
  with self.assertRaises(Problem):self.s.mutate('requests',dict(action_id='unknown'))
 def test_claims_not_effects(self):
  state=self.s.state();agreement=next(r for r in state['records'] if r['id']=='agreement');self.assertIn('not yet established',agreement['data']['text']);self.assertFalse(any(r['kind']=='decision' for r in state['records']))
if __name__=='__main__':unittest.main()
