# Input Contract — IC-01

| Field | Type | Mandatory | Rule |
|---|---|---|---|
| skill_id | string | YES | Exact `AI-Skill-Cover-Ebook-To-Html` |
| input_pdf | local path | YES | Existing readable `.pdf`; no remote URL |
| rights_confirmation | Boolean | YES | Owner has rights to process; MUST be true for execution |
| authorization | enum | YES | `AUTHORIZED_LOCAL` required before running reference script |
| data_classification | enum | YES | Public/Internal/Confidential; output directory must comply |
| output_directory | local path | YES | Explicit local destination; no overwrite unless reviewed |
| language | string | NO | Default `vi`, must not alter source text |
| require_images | Boolean | NO | Default true; image extraction best-effort |
| pdf_type | enum | NO | Text/Scan/Mixed/Unknown; no automatic OCR |
| acceptance_criteria | list | YES | Owner-reviewed; default contract is provisional |

INPUT_PARTIAL on missing information. BLOCKED when rights absent, remote-only input, encrypted/scan-only unsupported or potentially unsafe output. Never treat synthetic example as real customer data. User's submission does not imply redistribution rights.
