# Requirements → artifacts → tests trace

| Req | Method | Artifact | Technical test | Business evidence |
|---|---|---|---|---|
| FR-01 PDF read | M01 | tools/pdf_to_html.py | T01/T03/T04 | OPEN |
| FR-02 text extraction | M02 | chapters/*.html | T01/T05 | OPEN |
| FR-03 headings | M03 | chapter h2 | T01 | OPEN: semantic review |
| FR-04 linked TOC | M03/M04 | index.html/toc.json | T01/T06 | OPEN |
| FR-05 images | M03 | assets/images | T07 conditional | OPEN |
| FR-06 tables | M03 | warning/paragraphs | No table fidelity test | OPEN |
| FR-07 HTML5/offline | M04 | index, chapters, css | T01/T06 | OPEN |
| FR-08 Unicode | M02/M04 | UTF-8 output | T01 | OPEN |
| FR-09 conversion report | M04 | conversion-report.json | T01/T06 | OPEN |
| FR-10 OCR | excluded | GAP register | T05 reject | OUT OF SCOPE |
| FR-11 search | excluded | backlog | NOT RUN | OUT OF SCOPE |
| FR-12 reading UI | proposed | CSS baseline only | T01 | OPEN |
