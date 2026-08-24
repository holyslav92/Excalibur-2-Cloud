## LESSON-20260824-0829-B10-designed-hook-bar-false-positive
status: proposed
topic_id: B10
category: other
confidence: medium

### Evidence
- artifact: cover/cover_qa.json#pixel_wordstat_not_opaque_bars vs pixel_no_wordstat_query_strips
  finding: final VIP candidate — `pixel_wordstat_not_opaque_bars=true` (no opaque bar flake) but `pixel_no_wordstat_query_strips=false` (3 Wordstat strip(s), paper_frac=0.1107). Attempt 1 standard had inverse: opaque bar FAIL + 4 strips. Designed hook title bar / layout bands misread as Wordstat query strips or opaque bars depending on tier.
- artifact: cover/cover_qa.json#pixel_designed_thumbnail
  finding: `pixel_designed_thumbnail=false` while host close-up, high-key, hook zone checks partially pass — grsai scene reads as photo collage (white_frac=0.635, blob_count=3) not designed thumbnail.
- artifact: cover/cover-budget-result.json#attempts[0].tiers[0].qa_errors
  finding: `pixel_wordstat_not_opaque_bars FAIL: 1 horizontal opaque bar(s)` on standard tier; same visual layout passed opaque-bars on VIP — tier-sensitive false positive on designed hook bar.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- COVER_PIXEL_WORDSTAT_STRIP_FALSE_POSITIVE
- COVER_PIXEL_DESIGNED_THUMBNAIL_MISMATCH
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Anti Wordstat query strips on cover (canon: no MCP query dumps on PNG) — intent correct.
- Separating opaque-bar check from strip detector — when one passes and other fails, treat as layout-classification issue not content violation.

### Change
- Pixel classifier: exclude top hook title bar band (designed typography zone) from Wordstat strip and opaque-bar heuristics when cover-text declares hook-only top band (no wordstat_pil stickers on cover).
- Align `pixel_designed_thumbnail` threshold with grsai solo output (single scene + overlay text) vs legacy collage template.
- On conflicting pixel signals (opaque PASS + strips FAIL on same PNG) → flag `ASSUMED_BEHAVIOR` for human/OCR escape, not auto FAIL loop.

### Never again
- Не интерпретировать designed hook bar как «Wordstat strip» без OCR confirmation of query text.
- Не regen cover только из-за `pixel_designed_thumbnail` когда face+layout gates pass (B10 budget already exhausted).

### Proposed apply
- Fixer: tune strip detector ROI to skip hook bar y-band; document in `memory/cover/cover-canon.json` designed_hook_bar_exclusion.
- Cross-check with B08/B09 OCR escape tests in `tests/test_cover_budget.py`.

### Durable applied
- none (first B10 occurrence; need ≥2 runs or fixer patch)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil-prodazhu-prodavca
publish_status: BLOCKED (cover_qa FAIL)
