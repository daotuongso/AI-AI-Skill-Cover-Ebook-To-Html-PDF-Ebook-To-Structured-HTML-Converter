#!/usr/bin/env python3
"""Offline, permission-gated PDF-to-HTML demonstrator; not a full ebook reconstruction engine."""
import argparse, html, json, re, sys
from pathlib import Path
import fitz

def html_doc(title,body,css):
 return '<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>'+html.escape(title)+'</title><link rel="stylesheet" href="'+css+'"></head><body>'+body+'</body></html>\n'

def convert(src,out,rights):
 if not rights: raise ValueError('RIGHTS_NOT_CONFIRMED')
 if src.suffix.lower()!='.pdf' or not src.is_file(): raise ValueError('PDF_NOT_FOUND_OR_UNSUPPORTED_PATH')
 if out.exists(): raise ValueError('OUTPUT_EXISTS_NO_OVERWRITE')
 try: doc=fitz.open(str(src))
 except Exception as e: raise ValueError('INVALID_PDF') from e
 try:
  if doc.needs_pass: raise ValueError('ENCRYPTED_PDF_UNSUPPORTED')
  if not doc.page_count: raise ValueError('EMPTY_PDF')
  lines_per_page=[]; images_per_page=[]; chars=0
  for page in doc:
   lines=[]
   data=page.get_text('dict',sort=True)
   for block in data.get('blocks',[]):
    if block.get('type')!=0:continue
    for line in block.get('lines',[]):
     text=''.join(s.get('text','') for s in line.get('spans',[])).strip()
     if text:
      size=max((s.get('size',0) for s in line.get('spans',[])),default=0)
      lines.append((text,float(size)))
      chars+=len(text)
   lines_per_page.append(lines)
   images_per_page.append(page.get_images(full=True))
  if not chars: raise ValueError('NO_TEXT_LAYER_OCR_REQUIRED')
  out.mkdir(parents=True)
  (out/'chapters').mkdir()
  (out/'assets'/'css').mkdir(parents=True)
  (out/'assets'/'images').mkdir()
  css=(Path(__file__).resolve().parent.parent/'assets/css/style.css').read_text(encoding='utf-8')
  (out/'assets/css/style.css').write_text(css,encoding='utf-8')
  all_sizes=sorted(s for ls in lines_per_page for _,s in ls if s>0)
  median=all_sizes[len(all_sizes)//2] if all_sizes else 11.0
  toc=[]; warnings=['INFERRED_STRUCTURE_REQUIRES_MANUAL_REVIEW','MULTICOLUMN_AND_TABLE_READING_ORDER_NOT_VERIFIED']
  image_total=0; image_failures=0
  for i,(lines,images) in enumerate(zip(lines_per_page,images_per_page),1):
   ch=f'page-{i:04d}.html'; heading=next((t for t,s in lines if s>=median*1.2),f'Trang {i}')
   body=['<header><a href="../index.html">← Mục lục</a></header>',f'<main id="page-{i}"><h1>Trang {i}</h1>']
   for t,s in lines:
    tag='h2' if s>=median*1.2 and len(t)<200 else 'p'
    body.append(f'<{tag}>'+html.escape(t) +f'</{tag}>')
   seen=set()
   for n,img in enumerate(images,1):
    xref=img[0]
    if xref in seen:continue
    seen.add(xref)
    try:
     pix=fitz.Pixmap(doc,xref)
     if pix.n>4:pix=fitz.Pixmap(fitz.csRGB,pix)
     name=f'page-{i:04d}-image-{n:03d}.png'; pix.save(str(out/'assets/images'/name))
     body.append('<figure><img src="../assets/images/'+name+'" alt="Hình trích từ trang '+str(i)+' (cần kiểm tra chú thích)"></figure>')
     image_total+=1
    except Exception:
     image_failures+=1
   body.append('</main>')
   (out/'chapters'/ch).write_text(html_doc(f'Trang {i}', ''.join(body),'../assets/css/style.css'),encoding='utf-8')
   toc.append({'title':heading,'page':i,'href':'chapters/'+ch,'text_lines':len(lines)})
  contents='<main><h1>Ebook – mục lục theo trang</h1><nav aria-label="Mục lục"><ol>'+''.join('<li><a href="'+x['href']+'">'+html.escape(x['title'])+' (trang '+str(x['page'])+')</a></li>' for x in toc)+'</ol></nav></main>'
  (out/'index.html').write_text(html_doc('Ebook – mục lục',contents,'assets/css/style.css'),encoding='utf-8')
  (out/'toc.json').write_text(json.dumps(toc,ensure_ascii=False,indent=2),encoding='utf-8')
  if image_failures:warnings.append('IMAGE_EXTRACTION_FAILURES')
  if any(not ls for ls in lines_per_page):warnings.append('PAGES_WITHOUT_TEXT_PRESENT')
  report={'status':'READY_FOR_HUMAN_REVIEW','source_pdf_filename':src.name,'page_count':doc.page_count,'text_characters':chars,'image_files':image_total,'image_failures':image_failures,'warnings':warnings,'tool':'PyMuPDF','tool_version':fitz.VersionBind,'ocr_performed':False,'business_uat':'NOT_RUN','rights_confirmed_by_operator':True,'limitations':['page_based_chapters_not_real_semantic_chapters','tables_not_reconstructed','layout_not_guaranteed']}
  (out/'conversion-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
  return report
 finally:doc.close()

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--rights-confirmed',action='store_true')
 a=p.parse_args()
 try:
  r=convert(Path(a.input),Path(a.output),a.rights_confirmed)
  print(json.dumps(r,ensure_ascii=False));sys.exit(0)
 except Exception as e:
  print('BLOCKED: '+str(e),file=sys.stderr);sys.exit(2)
