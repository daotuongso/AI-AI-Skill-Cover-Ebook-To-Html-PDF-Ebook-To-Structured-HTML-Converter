# Synthetic positive example (not a real ebook)

Generate 2-page PDF with `ReportLab` containing Vietnamese UTF-8-friendly ASCII test lines and large titles. Expect 2 `chapters/page-NNNN.html`, index with 2 local relative links, toc.json length 2, page count=2, escaped source text (`<safe>` must appear as `&lt;safe&gt;`), a report with warnings/limitations, and validation PASS. This asserts technical mechanics only, not accurate real-book semantics.
