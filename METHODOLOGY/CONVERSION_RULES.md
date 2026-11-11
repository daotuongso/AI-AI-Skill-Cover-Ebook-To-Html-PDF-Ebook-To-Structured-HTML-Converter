# Concrete mapping rules (prototype)

1. Input extension `.pdf`, PDF opens, no encryption, rights flag present, and no existing output directory.
2. Each source PDF page becomes `chapters/page-NNNN.html`, preserving page provenance. Grouping by real chapter requires later analysis.
3. Plain text spans are separated into lines; CSS font-size larger than estimated body median by ≥20% becomes a tentative H2. A title is not declared fact without manual validation.
4. All text is escaped using Python `html.escape()`. Text fragments remain in extracted sequence, with known column/line-break limitations.
5. Each chapter page has a stable `id="page-N"` and local link back to index; index contains the TOC.
6. Embedded raster images extracted best-effort to local assets; links in chapter HTML. The source relative position and captions are not always preserved and require reviewer check.
7. No script, remote CSS, untrusted HTML rendering or auto-OCR. Test generated HTML offline.
8. Document can be `READY_FOR_REVIEW` after technical validation only; never automatically `ACCEPTED`.
