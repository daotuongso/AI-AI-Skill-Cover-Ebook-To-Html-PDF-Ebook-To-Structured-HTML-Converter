# G5 Independent Technical QA — actual execution

**Date:** 2026-11-11. **Fixture:** synthetic 2-page text-native PDF generated offline via ReportLab. **No real ebook tested.**

## Executed test evidence

Command: `python tools/technical_tests.py` (PyMuPDF 1.26.7 / Python, ReportLab synthetic PDF). All eight executed checks passed:

- T01 PASS — two-page native PDF to 2 HTML page chapters, TOC, UTF-8 escaping and offline CSS.
- T02 PASS — missing rights confirmation rejected.
- T03 PASS — nonexistent PDF rejected.
- T04 PASS — malformed PDF rejected.
- T05 PASS — no-text/scan-like PDF rejected (no OCR).
- T06 PASS — independent output validator on generated site.
- T08 PASS — existing output directory rejected without overwrite.
- T09 PASS — AES-256 encrypted PDF rejected.

**Not run:** T07 embedded image fidelity; T11 real source/manual domain Business UAT. Page-based HTML is technically valid, not verified true chapter inference. Domain reviewer UNASSIGNED. This test set does not prove business correctness or rights.

## Pack QA
Static Child Read Contract paths, manifest byte-SHA, Markdown links, ZIP paths and clean extraction are checked by independent finalization script outside the Child Pack; the resulting PASS status is reported in `QA/PACK_VERIFICATION.json`. Parent upstream `tools/full_builder.py` and `tools/validate_child.py` were **not** executed unmodified against this pack; claim is independent equivalent structural validation only. No GitHub CI or remote verification performed.

**Final Gate status:** G0–G5 completed at *Draft/technical QA* level; not Owner accepted. No publication/Push. G6 REPO_NAME_PROPOSED only after ZIP handoff.
