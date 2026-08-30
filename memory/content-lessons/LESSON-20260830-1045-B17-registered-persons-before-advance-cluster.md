## LESSON-20260830-1045-B17-registered-persons-before-advance-cluster
status: proposed
topic_id: B17
category: structure
confidence: low

### Evidence
- artifact: scout-handoff.md
  finding: cluster `registered_persons_block_sale_before_advance` — story_dup PASS; P0 «прописка при покупке квартиры» vol 10 (Tyumen 55+11176); `dzen_casus_shape: PASS`; comment_magnet «Продавец клянётся, что прописанные уйдут сами за неделю — вы бы поверили и внесли аванс?»
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2159 (target 1800–2200), h2 7, inline_figures 7, sibling_interlinks 3; `no_tldr_opening`, `comment_magnet_question`, `spine_once_no_recap`, `ending landing` gates PASS.
- artifact: description-brief.json
  finding: Klyshin rhythm, geo Тюмень, `not_equal_title: true` — карточка про «ЕГРН чистый / справка до аванса», не дублирует H1.
- artifact: cover-text.json
  finding: hook 6 слов «Нашли прописанных — аванс не внесли»; sticky «Сначала справка, потом деньги» зеркалит agency finale.
- artifact: cover/cover_qa.json
  finding: PASS with `ocr_false_positive_escape` (B08/B09 pattern) — visual core OK, OCR flakes overridden only.
- artifact: derouter-opus-stamp-sol.json
  finding: Sol claude-opus-5, 3 chunks merged — длинный casus без превышения hard max 2400.
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B09 (ЕГРН/ипотека), B14 (справка банка) — risk-cluster siblings; inbound planned B06, B04, B09.
- artifact: wp-publish-result.json
  finding: post 9342 published, 7 inline uploads, live-page PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет CTR/retention для post 9342

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет behavioral ingest)

### Keep
- News-casus shape: зарегистрированные лица (бывшая жена + взрослый сын) обнаружены **до аванса** — отказ до денег, не суд после покупки; отличать от B08 (наследники/ЗАГС), B07 (наследство), B10 (пожилой по телефону).
- Scout Wordstat rework: слабые хвосты «выписка из квартиры» → buyer P0 «прописка при покупке квартиры» — локализация без drop hook.
- Cover hook + sticky пара «аванс не внесли» / «Сначала справка, потом деньги» — stakes и comment-magnet без checklist-лида.
- Description gap: «ЕГРН чистый, а прописанные в справке» — полезный разрыв title/card для Дзена.
- Sol 3-chunk merge уложился в word_count target — без повторного trim-loop (контраст с B12).

### Change
- Scout bank: tag `registered_persons_before_advance` + anti-dup notes vs B08/B07/B10/B11 — plot «справка МФЦ / не собственники» ≠ «обременение ЕГРН» ≠ «наследники».
- Interlink defaults для cluster: B02 (деньги/расписка), B09 (ЕГРН строка), B14 (справка vs факт) — контекстные sibling, не SEO-хвосты.

### Never again
- Путать «чистый ЕГРН» с отсутствием зарегистрированных — ключевой механизм риска B17.
- Sugar ending «все выписались за неделю» — финал = остановка до денег, agency not panic.
- Выводить engagement из quality-bar PASS без Metrika cohort (причина не подтверждена).

### Proposed apply
- Scout story-cluster registry: `registered_persons_block_sale_before_advance` locked 30d после B17 publish.
- После Metrika ingest для post 9342 — re-evaluate confidence medium/high если retention/comment-magnet cohort совпадает с pre-advance-stop casus.

### Durable applied
- none (один run, нет Metrika, evidence SKIP)

### Resolution
status: recorded
article_dir: memory/blog/articles/B17-v-tyumeni-pered-avansom-nashli-propisannyh-prodavec-obeschal-vypisat-za-nedelyu
wp_post_id: 9342
