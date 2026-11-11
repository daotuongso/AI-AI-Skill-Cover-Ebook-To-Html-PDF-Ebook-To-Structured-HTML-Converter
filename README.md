# PDF Ebook to Structured HTML Converter

**Skill ID:** `AI-Skill-Cover-Ebook-To-Html` (exact Owner-assigned Pilot identifier)

## What it does
Converts a rights-cleared text-native PDF to an offline HTML5 document with inferred hierarchical sections, page anchors, optional extracted embedded images, and a linked table of contents. Produces machine-readable conversion diagnostics. Structure extraction is heuristic; headings, reading order and figures require review.

## Exclusions
OCR/scanned PDFs, password removal, true table reconstruction, exact page-by-page visual fidelity, complex multi-column flow, mathematical formula recognition, accessibility certification, commercial republication, JS search, DRM bypass and unlicensed redistribution are out of scope for this Pilot. All remain explicit GAPs or future owner decisions.

## Governance
Parent Rev.1 FINAL BASELINE and Core Rev.0 DRAFT_FOR_PLANNING are referenced, **not copied wholesale**. Exact commits and evidence in SOURCES/SOURCE_REGISTER.md. Local technical test does not prove domain accuracy, legal rights, business UAT or production readiness. Owner controls approval separately from upload.

## Operation
Read START_HERE.md and linked ten-document Read Contract. Follow INPUT–TOOL–OUTPUT. `tools/pdf_to_html.py` offers a deterministic offline reference path (PyMuPDF); `tools/validate_output.py` checks basic consistency but cannot review semantics. See QA/TEST_REPORT.md.
