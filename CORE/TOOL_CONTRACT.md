# Tool Contract — TC-01

Permitted: local PyMuPDF text/metadata/image extraction from an authorized PDF; Python stdlib HTML escaping, HTML/CSS/JSON assembly; Python structural tests; optional human semantic inspection. Network, LLM model calls, OCR, browser automation and GitHub writes are **not** required or authorized by this contract.

Execution log must include tool/version, task_id, source filename only (avoid sensitive paths in public logs), page count, output file list, warnings, tests, error codes. Running conversion requires explicit per-document local authorization; Parent G0–G5 authorization is not authorization to process arbitrary ebooks.

Not permitted: uploading source to cloud/AI service, DRM circumvention, rewriting unknown facts, writing into unexpected paths, externally hosted CSS/fonts/scripts, modifying existing documents or using confidential PDFs in public repos. If tools not available, return BLOCKED/manual handoff; do not fabricate an execution report.
