## LESSON-20260829-0602-B13-cover-budget-phone-wordstat-publish-block
status: proposed
topic_id: B13
category: structure
confidence: high

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2 grsai standard attempts exhausted (`cover_budget_exhausted`); attempt 1 — phone clipped (`79220016505`), hook OCR partial; attempt 2 — phone clipped (`1792200`), hook truncated («Чистая»/«спасла» missing), 2 opaque Wordstat bar bands + 1 query strip, collage inset, `pixel_designed_thumbnail` FAIL.
- artifact: cover/cover_qa.json
  finding: `gate_status: FAIL`; no `ocr_false_positive_escape` — real phone clip + wordstat strips on PNG, not B08/B09/B10 flake pattern.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: false` — единственный FAIL; text gates PASS (word_count 2547, h2 8, inline 7, interlink 4, comment_magnet, no_tldr).
- artifact: cover/quad-mcp-prompt-01.txt
  finding: conflicting prefix — line 1 «1-3 Wordstat stickers (Тюмень)» vs line 5 «ZERO Wordstat/search-keyword strips»; grsai attempt 2 painted gold bar strips at right edge anyway.
- artifact: cover/cover-text.json
  finding: hook 6 слов «Чистая выписка не спасла сделку», phone `+7 922 001 65 05`, sticky «Аванс остановили вовремя» — on-topic; pixel QA не спасла clipped phone.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post не опубликован; ingest skipped)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- PUBLISH_BLOCKED_COVER_QA_FAIL
- COVER_PHONE_OCR_CLIP_FAIL
- COVER_WORDSTAT_STRIP_ON_COVER
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 grsai attempts → `cover-budget-result.json` → Indexer (не бесконечный Cover-QA loop) — выполнено; llms.txt обновлён.
- Short hook 6 слов + sticky «Аванс остановили вовремя» — stakes до аванса, зеркалит casus.
- Текстовый пайплайн complete: Sol/writer/description/schema/cover-text gates PASS; publish блокирует только cover.

### Change
- После budget exhaust с **реальным** phone clip + wordstat strips (не OCR escape): Director → **Fixer** cover regen (phone-in-hand close-up, strip-ban solo prompt) **до** Publish — B13 застрял на `cover_qa_pass: false`, в отличие от B10/B12 escape path.
- Убрать legacy «1-3 Wordstat stickers» из cover quad prefix **до** первого grsai call (B12 proposed + B13 подтверждает на attempt 2).
- Hook highlight «спасла» — при длинном hook держать phone CTA в safe zone (+80px от края); attempt 2 обрезал digits и hook head.

### Never again
- `apply_ocr_false_positive_escape` когда phone `clipped=True` и wordstat strips на canvas — это не flake.
- Publish при `cover_qa_pass: false` / quality-bar FAIL.
- Deep-dive pixel OCR после budget exhaust — Fixer regen вместо loop.

### Proposed apply
- Director runbook: budget exhaust + phone clip OR wordstat strip → Fixer (не Indexer-only handoff к Publish).
- `memory/cover/quad-style-the-rieltor.json` cover-panel prefix: NO Wordstat strips (B12 proposal + B13 second run — checklist для fixer).
- Cover-scene default: phone-in-hand close-up для guardianship/elderly casus (sibling B10 pattern).

### Durable applied
- none (publish blocked; fixer path pending)

### Resolution
status: recorded
article_dir: memory/blog/articles/B13-v-tyumeni-rodstvenniki-oformili-opeku-nad-prodavcom-za-den-do-avansa-sdelku-osta
wp_post_id: none (publish blocked)
