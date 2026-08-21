## LESSON-20260821-0836-B07-early-cta-before-first-h2
status: proposed
topic_id: B07
category: cta
confidence: high

### Evidence
- artifact: shared/quality-bar-9.md § Early — hook + TL;DR + `excalibur-cta-early` **до** первого H2
  finding: `first_screen_html()` в quality-bar-9_gate проверяет TG+MAX только в контенте до `<h2>`.
- artifact: scripts/excalibur_blog_quality_bar_9_gate.py — `check_early_cta()` uses `first_screen_html()`
  finding: early CTA после первого H2 → `early_cta_tg_max_only` FAIL.
- artifact: article.html (final PASS) — 13 opening `<p>` + TL;DR `<ul>` + `<div class="excalibur-cta-early">` **перед** `<h2>Один собственник…`
- artifact: assembled-writer-inputs.md — «Chunk part 1: opening paragraphs + early CTA + H2 1-3 only»
- artifact: quality-bar-9.json — `early_cta_tg_max_only: true` после Writer/Sol chunk plan
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EARLY_CTA_AFTER_H2
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Структура B07: hook (5–7 абзацев) → «Коротко» TL;DR → early CTA → H2#1.
- Writer chunk 1 explicitly включает early CTA zone — предсказуемый PASS.

### Change
- Writer/Sol chunk 1: **никогда** ставить первый `<h2>` до `excalibur-cta-early`.
- Director preflight: если Sol single-shot/chunk 1 заканчивается на H2 без early CTA — re-run chunk 1, не ждать structure_gate.

### Never again
- Не начинать первый H2 сразу после hook без TL;DR + early CTA на longform B-mode.
- Не считать community_cta PASS достаточным — quality-bar-9 проверяет **позицию** early CTA.

### Proposed apply
- Уже в quality-bar-9.md и writer skill chunk plan; lesson фиксирует run evidence B07.
- После repeat на B08+ — checklist item в director runbook.

### Durable applied
- none (contract уже canonical)

### Resolution
status: recorded
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
wp_post_id: 8994
