# Output Contract — OC-01

Deliver a self-contained static folder (NOT automatically published): `index.html`, `chapters/*.html`, `assets/css/style.css`, optional `assets/images/*`, `toc.json`, `conversion-report.json`. HTML5 semantic headings and navigation. Source page ranges and extraction warnings must be traceable. All links relative; CSS local; content escaped. Do not embed untrusted scripts.

Acceptance **technical**: index exists, HTML heading structure with 1 H1 per chapter, TOC links exist, no external URL dependencies, correct UTF-8 text handling, sane source page mapping, and warnings for non-convertible source. Acceptance **business**: Owner/domain reviewer samples pages against PDF, validates meaning, multi-column/tables/images and confirms rights. Do not claim identical layout or accessibility conformance.

Statuses: `DRAFT`, `READY_FOR_REVIEW`, `ACCEPTED`, `REJECTED`, `NOT_VERIFIED`. System can produce READY_FOR_REVIEW only; ACCEPTED/release require Owner. Synthetic fixtures must be labeled SAMPLE.
