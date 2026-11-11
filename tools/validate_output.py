#!/usr/bin/env python3
"""Mechanical offline structure checker, not semantic approval."""
import argparse,json,re,sys
from pathlib import Path

def validate(site):
 errs=[]
 for p in ['index.html','toc.json','conversion-report.json','assets/css/style.css']:
  if not (site/p).is_file():errs.append('MISSING:'+p)
 if errs:return errs
 try:toc=json.loads((site/'toc.json').read_text(encoding='utf-8'));rep=json.loads((site/'conversion-report.json').read_text(encoding='utf-8'))
 except Exception as e:return ['INVALID_JSON:'+str(e)]
 if len(toc)!=rep.get('page_count'):errs.append('PAGE_COUNT_MISMATCH')
 for e in toc:
  href=e.get('href','');p=site/href
  if not href.startswith('chapters/') or '..' in Path(href).parts or not p.is_file():errs.append('INVALID_TOC_TARGET:'+href)
 files=[site/'index.html']+list((site/'chapters').glob('*.html'))
 for f in files:
  txt=f.read_text(encoding='utf-8')
  if '<!doctype html>' not in txt.lower():errs.append('DOCTYPE_MISSING:'+f.name)
  if '<script' in txt.lower():errs.append('SCRIPT_PRESENT:'+f.name)
  if re.search(r'(?:src|href)=["\']https?://',txt,re.I):errs.append('EXTERNAL_ASSET:'+f.name)
 return errs
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--site',type=Path,required=True);a=p.parse_args()
 errs=validate(a.site)
 print('PASS' if not errs else '\n'.join(errs));sys.exit(bool(errs))
