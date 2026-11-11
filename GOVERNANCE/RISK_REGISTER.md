# RSK-01 — Risk register

| Risk | Severity | Mitigation | Residual |
|---|---|---|---|
| R01 No rights for ebook | HIGH | Require explicit rights flag and per-document review | OPEN |
| R02 Multi-column/complex reading order | HIGH | Report limitations; real manual review | OPEN |
| R03 Embedded figures/captions orphaned | MEDIUM | Extract where possible; review originals | OPEN |
| R04 False hierarchy/TOC | HIGH | Mark inferred H2; Owner validates | OPEN |
| R05 Scanned-only pages | HIGH | Reject or explicitly request OCR scope | OPEN |
| R06 Disclosure of confidential content | HIGH | Offline only; no remote storage; no source in repo | OPEN |
| R07 Untrusted text/script injection | MEDIUM | html.escape, no embedded JS | CONTROLLED_TECHNICAL |
| R08 Accessibility/SEO compliance unknown | MEDIUM | Do not assert certifications, manual QA | OPEN |
| R09 Output overwrite/data loss | HIGH | Reject existing output | CONTROLLED_TECHNICAL |
