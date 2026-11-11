# START HERE — AI-Skill-Cover-Ebook-To-Html Rev.0 Draft 01

**Pilot outside Catalogue · NOT APPROVED · NOT RELEASED.** The Skill converts rights-cleared, text-based PDF ebooks into a static structured HTML site; it does not guarantee facsimile reproduction.

## Mandatory Child Read Contract (10, ordered)
1. [README.md](README.md)
2. [VERSION.json](VERSION.json)
3. [SKILL.md](SKILL.md)
4. [skill_manifest.json](skill_manifest.json)
5. [CORE/INPUT_CONTRACT.md](CORE/INPUT_CONTRACT.md)
6. [CORE/TOOL_CONTRACT.md](CORE/TOOL_CONTRACT.md)
7. [CORE/OUTPUT_CONTRACT.md](CORE/OUTPUT_CONTRACT.md)
8. [WORKFLOW/G0_G7.md](WORKFLOW/G0_G7.md)
9. [METHODOLOGY/DOMAIN_METHOD.md](METHODOLOGY/DOMAIN_METHOD.md)
10. [QA/QA_POLICY.md](QA/QA_POLICY.md)

## Copyable startup prompt
> Áp dụng AI-Skill-Cover-Ebook-To-Html Rev.0 Draft 01. Đọc đủ mười tài liệu Read Contract theo START_HERE và xác nhận trạng thái từng tệp. Chỉ tiếp nhận PDF Owner có quyền xử lý; kiểm tra Input–Tool–Output, dữ liệu nhạy cảm và hạn chế kỹ thuật trước khi chạy. Không tự OCR, không gửi file cho dịch vụ bên ngoài, không xuất bản hoặc phê duyệt. Nếu thiếu quyền/dữ liệu hãy BLOCKED. Tạo bản HTML offline, log trang/heading/các lỗi và QA nếu được giao thực thi.

## Quick start (local, optional, ONLY with authorized PDF)
`python -m pip install -r requirements.txt`
`python tools/pdf_to_html.py --input /path/to/rights-cleared.pdf --output ./out/ebook --rights-confirmed`
`python tools/validate_output.py --site ./out/ebook`

These scripts are a controlled **prototype technical reference**, not a proven production/accessible publication converter. No real ebook supplied; only synthetic QA has been run. No uploads.
