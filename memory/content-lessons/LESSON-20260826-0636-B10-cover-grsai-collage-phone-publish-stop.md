## LESSON-20260826-0636-B10-cover-grsai-collage-phone-publish-stop
status: proposed
topic_id: B10
category: other
confidence: high

### Evidence
- artifact: cover/cover_qa.json#pixel_errors
  finding: Cover-QA FAIL после исчерпания cover budget (2× grsai solo). Fails: `pixel_no_collage_inset` (white_frac=0.164, inset_face=True), `pixel_phone_readable` / `pixel_phone_not_clipped` (digits clipped, OCR `+792200165`), `pixel_hook_title_not_truncated` (missing «квартиру», «после», «покупки»), `pixel_no_wordstat_query_strips` (1 strip), `pixel_designed_thumbnail`. grsai сгенерировал polaroid/inset collage вместо designed thumbnail.
- artifact: cover/cover-budget-result.json
  finding: `status: FAIL`, `reason: cover_budget_exhausted`, оба attempt qa_fail; fixer regen (INC-20260826-0629) не снял pixel fails.
- artifact: quality-bar-9.json
  finding: все текстовые checks PASS (word_count 2176, 7 inline, comment_magnet, interlink 4); единственный FAIL — `cover_qa_pass: false` → Publish STOP.
- artifact: cover-text-gate.json, schema-gate.json, opening-meta-gate.json, research-official-gate.json
  finding: Scout→Research→Title→Writer→Sol→Description→Cover-text||Schema — PASS; блокер только визуал обложки.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (INC-20260821-0615-content-learner-metrika-credentials); ingest не выполнен, cohort B10 недоступен

### Named blockers
- COVER_QA_PIXEL_FAIL
- COVER_BUDGET_EXHAUSTED
- PUBLISH_STOP_COVER
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Fail-fast cover budget (max 2 attempts) + `cover-budget-result.json` — не бесконечный Cover-QA loop.
- Текстовый пайплайн B10: news-casus, comment magnet, 7 inline, early TG+MAX, interlink 4 — все гейты до Cover-QA.
- Hook cover-text «Суд вернул квартиру банкроту через год» (8 слов) — в пределах 5–7 канона по смыслу, но OCR на PNG не читает полностью.

### Change
- До Publish: human review cover.png или regen с shorter hook (5–6 слов) + усиленный `collage_inset_ban_prompt_block` (уже в fixer 7fe8c61 — повторить после owner decision).
- Рассмотреть OCR escape только если визуально OK и падают **только** truncation flakes (B08/B09 pattern) — здесь также `pixel_no_collage_inset` и clipped phone, escape не применим.
- `wordstat_stickers` в cover-text — topic-log only; не рендерить query strips на PNG (preflight warn уже добавлен fixer).

### Never again
- Publish при `cover_qa.json` status FAIL без owner manual PASS или успешного regen.
- PIL mashup / Kie для «починки» collage или phone.
- Deep-dive `cover_qa_pixels.py` после исчерпания budget — переход к Indexer/human per canon.

### Proposed apply
- Owner: визуальный PASS stamp или regen Cover с hook ≤6 кириллических слов.
- После второго run с collage+phone FAIL на grsai standard — durable negative prompt в `cover-design-code.json` + рассмотреть Derouter image fallback (optional contract).
- Metrika: добавить credentials в Cloud Secrets, повторить ingest post-publish.

### Durable applied
- none — fixer prompt blocks (7fe8c61) уже applied, B10 regen всё ещё FAIL; ждём owner или ≥2-й повтор паттерна

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-kupili-kvartiru-v-tyumeni-cherez-god-finupravlyayuschij-osporil-sdelku
incident_cover: memory/pipeline-fix-queue.md#INC-20260826-0629-cover-qa-pixel-b10
incident_metrika: memory/pipeline-fix-queue.md#INC-20260821-0615-content-learner-metrika-credentials
