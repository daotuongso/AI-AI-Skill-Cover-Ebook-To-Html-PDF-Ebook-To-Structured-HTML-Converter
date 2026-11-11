#!/usr/bin/env python3
"""Independent executable synthetic tests. Uses reportlab only to create synthetic sample PDFs."""
import tempfile,sys
from pathlib import Path
from reportlab.pdfgen import canvas
import fitz
from pdf_to_html import convert
from validate_output import validate

def expect(code,fn):
 try:fn()
 except ValueError as e:
  assert code in str(e),(code,str(e))
  return
 raise AssertionError('Expected '+code)

def main():
 with tempfile.TemporaryDirectory(prefix='bto_ebook_') as t:
  d=Path(t);pdf=d/'SAMPLE.pdf';c=canvas.Canvas(str(pdf));c.setFont('Helvetica',18);c.drawString(50,760,'SAMPLE CHAPTER ONE');c.setFont('Helvetica',11);c.drawString(50,730,'A & B <safe> This is synthetic.');c.showPage();c.setFont('Helvetica',18);c.drawString(50,760,'SAMPLE CHAPTER TWO');c.setFont('Helvetica',11);c.drawString(50,730,'Offline structured HTML sample.');c.save()
  out=d/'site';r=convert(pdf,out,True)
  assert r['page_count']==2 and r['text_characters']>0
  assert len(list((out/'chapters').glob('*.html')))==2
  assert '&lt;safe&gt;' in (out/'chapters/page-0001.html').read_text()
  assert not validate(out),validate(out)
  print('T01 PASS: synthetic two-page native PDF, escaping, TOC, offline structure')
  expect('RIGHTS_NOT_CONFIRMED',lambda:convert(pdf,d/'denied',False));print('T02 PASS: missing rights')
  expect('PDF_NOT_FOUND',lambda:convert(d/'missing.pdf',d/'missing_site',True));print('T03 PASS: missing PDF')
  (d/'bad.pdf').write_bytes(b'%PDF-1.2\nnot real');expect('INVALID_PDF',lambda:convert(d/'bad.pdf',d/'bad_site',True));print('T04 PASS: invalid PDF')
  scan=d/'scan.pdf';x=fitz.open();x.new_page();x.save(str(scan));x.close();expect('NO_TEXT_LAYER_OCR_REQUIRED',lambda:convert(scan,d/'scan_site',True));print('T05 PASS: no text scan')
  assert not validate(out);print('T06 PASS: independent output validator')
  expect('OUTPUT_EXISTS',lambda:convert(pdf,out,True));print('T08 PASS: no overwrite')
  locked=d/'encrypted.pdf';e=fitz.open(str(pdf));e.save(str(locked),encryption=fitz.PDF_ENCRYPT_AES_256,owner_pw='owner-sample',user_pw='user-sample');e.close()
  expect('ENCRYPTED_PDF_UNSUPPORTED',lambda:convert(locked,d/'encrypted_site',True));print('T09 PASS: encrypted source rejected')
 print('TECHNICAL_TESTS_PASS=8; T07 image fixture NOT_RUN; T11 business UAT NOT_RUN')
if __name__=='__main__':main()
