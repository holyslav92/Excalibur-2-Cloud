## LESSON-20260821-0615-B06-derouter-524-chunk-fallback
status: validated
topic_id: B06
category: other
confidence: medium

### Evidence
- artifact: derouter-opus-stamp-writer-part{1,2,3}.json + derouter-opus-stamp-sol-part{1,2,3}.json
  finding: Writer/Sol single-shot к Derouter REST вернул HTTP 524 (Cloudflare timeout); recovery через 3-part chunk (`excalibur_blog_writer_chunk.py` / Sol chunk) — все части PASS, финальный article.html собран.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID)

### Named blockers
- DEROUTER_HTTP_524
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Longform Writer/Sol: **3 части на первом проходе** (skill writer-excalibur-blog) — не ждать 524 на single-shot.
- Chunk fallback идемпотентен: stamps per-part, merge в drafts/writer.html → article.html.

### Change
- Директор: для 7-inline longform сразу вызывать chunk scripts, не `--single-shot`.
- При 524 на powerful tier — автоматический retry через chunk без ручного Composer.

### Never again
- Не запускать Writer/Sol single-shot на longform B-mode (2300+ слов, 7 inline) — предсказуемый 524.

### Proposed apply
- Подтвердить в director runbook: preflight longform → chunk-only (уже в skills/writer-excalibur-blog).
- После второго run с тем же паттерном — durable gate в research_start или director checklist.

### Durable applied
- none (writer skill уже документирует; validated вторым run B08 — LESSON-20260822-0753-B08-writer-chunk-first-pass-validated)

### Resolution
status: recorded
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami
wp_post_id: 8984
validated_by: LESSON-20260822-0753-B08-writer-chunk-first-pass-validated (B08 chunk-first, no 524)
