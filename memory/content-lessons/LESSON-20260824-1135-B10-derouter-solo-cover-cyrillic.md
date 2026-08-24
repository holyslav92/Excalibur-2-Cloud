## LESSON-20260824-1135-B10-derouter-solo-cover-cyrillic
status: proposed
topic_id: B10
category: other
confidence: high

### Evidence
- artifact: cover/quad-solo-result-cover.json
  finding: Derouter REST `responses` + `image_generation`, model gpt-5.4, 2048×1152 → resized; host i2i face-studio-2026-06-23; source derouter-responses-api.
- artifact: cover/quad-solo-batch-cover.json
  finding: Pipeline `quad_solo_panel_regen_derouter` после grsai budget fail; prompt TEXT LOCK Russian Cyrillic — hook EXACT «Чистая выписка — сделку оспорили позже», phone EXACT «+7 922 001 65 05», sticky «Выписка не гарантия»; NO Wordstat strips on cover.
- artifact: cover/cover-budget-result.json vs cover/cover_qa.json
  finding: grsai 4 tier attempts all Cyrillic OCR FAIL; Derouter solo cover → cover_qa PASS (typography_cyrillic_clean, pixel_hook_title_cyrillic, pixel_phone_readable).
- artifact: wp-publish-result.json
  finding: Published post=9141, featured_image=9142, cover decode_verified, 7 inline uploads OK.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- GRSai_CYRILLIC_RENDER_FAIL
- METRIKA_CREDENTIALS_MISSING

### Keep
- Derouter solo cover как **fallback** для кириллического hook/phone после grsai budget exhausted — within canon (optional Derouter image fallback).
- cover-text.json exact strings в prompt — не paraphrase для OCR.
- Inline quads остаются на grsai MCP batch (quad-mcp-batch-01/02); только **cover slot** через Derouter solo.

### Change
- Cover agent: при `cover-budget-result.json` status FAIL + last_errors содержат `pixel_hook_title_cyrillic` → автоматический `quad_solo_panel_regen_derouter` без ожидания human.
- Директор timebox: Derouter cover regen ≤1 attempt после grsai budget (не +2 grsai loops).

### Never again
- Не публиковать без readable Cyrillic hook на cover когда grsai исчерпал бюджет — Derouter fallback обязателен.
- Не смешивать Wordstat query strips на cover (Scout Wordstat topic-only) — B10 prompt явно BAN strips.

### Proposed apply
- Зафиксировать в cover-excalibur-blog skill: post-budget Derouter solo для cover Cyrillic (B10 evidence).
- После второго run с тем же grsai→Derouter pattern — durable checklist в director pre-Cover-QA.

### Durable applied
- none (первый production run Derouter solo cover после grsai Cyrillic fail)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-vypiske-vse-chisto-prodavec-vladel-tri-mesyaca
wp_post_id: 9141
