# Domain Method — PDF → Structured Offline HTML

## M01 Intake and preflight
M01.1 Confirm lawful possession and permission to transform the actual ebook; record classification and local processing boundary. M01.2 Preflight: PDF header, encryption, page count, text coverage per page, fonts, page rotation, tables/images, logical outline, columns and suspicious embedded artifacts. M01.3 Mark `BLOCKED` for missing rights, unsupported text-only conversion, unreadable/encrypted PDF or overwrite risks. Never bypass encryption.

## M02 Extract without inventing
M02.1 Use page span text coordinates and font sizes to infer reading order and heading levels. M02.2 Treat existing PDF outline/bookmarks as stronger evidence of chapters, when available; reference prototype currently uses fontsize heuristic only. M02.3 Remove neither repeated headers nor page numbers blindly: log possible artifacts for review. M02.4 Copy text exactly as extraction yields; escape HTML `& < > "` and preserve Unicode; no summarization or translation. M02.5 Keep source page numbers as provenance. Do not claim semantics or reading order correct for complex layouts.

## M03 Semantic organization
M03.1 Set top-level title H1 and heading hierarchy H2/H3 based on document evidence. M03.2 Build deterministic chapter segmentation with stable slugs/page anchors; provide TOC links. M03.3 Put paragraphs inside `<p>` and figures in `<figure>` when image provenance can be located. M03.4 Tables need reliable cell boundaries, headers, row/column spans; otherwise preserve text and warn `TABLE_REVIEW_REQUIRED`, never fabricate a table. M03.5 Cross-page continuation, footnotes, mathematical formulas and two-column text require human review.

## M04 Render and package
M04.1 Generate UTF-8 HTML5 with local CSS and relative navigation only. M04.2 Use semantic `main`, `nav`, `section`, heading tags; set lang and viewport; avoid inline JS. M04.3 Write `toc.json` and `conversion-report.json` listing page counts, detected headings, warnings, skipped image count, tool version and known limitations. M04.4 File-system paths must be controlled; do not overwrite existing output silently. M04.5 No remote links/resources necessary.

## M05 Quality assurance
M05.1 Count source and extracted pages, inspect TOC targets, broken paths and unexpected external dependencies. M05.2 Compare at least cover, early/mid/last page and samples of complex tables/images against original if real source exists; record reviewer and date. M05.3 OCR/scanned pages are `NOT_SUPPORTED` in Pilot; do not substitute guessed text. M05.4 Test negative conditions: missing PDF, insufficient rights, invalid PDF, encrypted PDF, zero text, existing output. M05.5 Separate technical PASS from correctness of reading order, heading hierarchy, image context and rights.

## M06 Traceability / human sign-off
M06.1 Tie each critical claim in the method to source ID in SOURCE_REGISTER and claim status; no unsupported legal/standards assertions. M06.2 Keep owner decisions, risks and limitations OPEN until real evidence. M06.3 Do not publish, host or sell generated HTML without explicit business/IP review.

## Reference implementation limitations
`tools/pdf_to_html.py` is a safe deterministic demonstrator for text-based PDFs. It does **not** use PDF bookmarks, reliably detect true sections, reconstruct tables, or preserve layout; images are best-effort. One HTML chapter per source page is intentional for robust anchors, not a claim about actual chapter boundaries. Improve only under a separately approved change request.
