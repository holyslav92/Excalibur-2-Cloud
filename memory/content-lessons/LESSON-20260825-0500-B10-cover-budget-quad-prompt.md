## LESSON-20260825-0500-B10-cover-budget-quad-prompt
status: proposed
topic_id: B10
category: other
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: grsai solo cover 2×2 attempts exhausted; best_candidate PNG fails OCR on hook Cyrillic + phone digits; wordstat strips detected despite wordstat_stickers=[] in cover-text.json.
- artifact: cover/quad-mcp-batch BLOCKER (pre-fix)
  finding: MCP prompt 3564 chars > 3500 — inline quad canvas never generated; 7 inline PNG missing.
- artifact: derouter-opus-stamp-sol-part{1,2,3}.json
  finding: Sol single-shot HTTP 524; recovery via 3-part chunk merge — PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- COVER_BUDGET_EXHAUSTED
- COVER_OCR_HOOK_PHONE_FAIL
- QUAD_PROMPT_OVER_3500
- DEROUTER_HTTP_524
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 solo attempts → Indexer without infinite Cover-QA loop.
- wordstat_stickers=[] on cover-text — correct for meme canon v1 (no query strips).
- Writer/Sol 3-part chunk on longform — predictable recovery from 524.

### Change
- Fixer reclaimed ~250 chars from shared quad prompt locks (ban/reference/wordstat_line) so B10 canvas batches fit ≤3500.
- Next run with cover budget: prefer quad canvas path after prompt fix; solo cover prompt may need stronger TEXT LOCK for Cyrillic hook+phone OCR.

### Never again
- Do not block Indexer on cover regen after budget exhausted.
- Do not publish without quality-bar-9 all_pass (cover_qa_pass).

### Proposed apply
- After second run with solo OCR hook/phone fail — tighten solo cover prompt TEXT LOCK or add early OCR pre-check before VIP tier.
- Quad prompt shared locks stay compact; scene_hint targets unchanged.

### Durable applied
- scripts/excalibur_blog_cover_quad_prompt.py — shared lock compaction + pick_identity_reference import (INC-20260825-0500)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-dogovor-podpisali-a-deneg-ne-bylo-v-tyumeni-nasledniki-zabrali-kvartiru
wp_post_id: none (draft, publish blocked)
