# Test plan

- T01: synthetic two-page text PDF, linked HTML, escaped text, offline style and Unicode.
- T02: missing rights flag denied.
- T03: nonexistent PDF denied.
- T04: invalid PDF bytes denied.
- T05: scan-only/zero-text PDF denied.
- T06: output validator checks index/chapters/toc/report and no remote references.
- T07: PDF embedded image extraction, best effort (may remain NOT_RUN).
- T08: existing target output denied.
- T09: password-protected PDF denied.
- T10: Child Pack Read Contract, paths, markdown links, Manifest SHA-256 and extraction byte identity.
- T11: business review against real ebook (NOT_RUN).
