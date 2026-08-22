## LESSON-20260822-0753-B08-ipoteka-cross-rubric-interlink
status: proposed
topic_id: B08
category: structure
confidence: medium

### Evidence
- artifact: wp-categories-gate.json — PASS category_slugs `ipoteka`, `proverka-pered-pokupkoj` (ids 32, 34)
- artifact: interlink-gate.json + link-verify.json — 4 outbound sibling links на `vtorichka-i-riski` (B02, B04, B05, B06), all HTTP 200
- artifact: quality-bar-9.json — `interlink_siblings_2_4: true`, sibling_interlinks=4
- artifact: wp-publish-log.md — первый publish в `/blog/ipoteka/`; permalink rubric ≠ sibling rubric
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (нет behavioral data для cross-rubric CTR)

### Keep
- Ипотечный casus (B08) в рубрике `ipoteka` + `proverka-pered-pokupkoj`, но interlink на risk-siblings из vtorichka — контекстно (аванс, выписка, обременение).
- 4 sibling links — верхняя граница quality-bar; все ledger-based slugs.

### Change
- Scout/Writer: для ipoteka-кластера заранее планировать 2–4 sibling из vtorichka-i-riski (EGRN/аванс/доверенность), не только ipoteka-slugs (пока мало опубликованных).
- Publish: dual category `ipoteka` + `proverka-pered-pokupkoj` для buyer-checklist угла.

### Never again
- Не оставлять ipoteka-статью без outbound interlink только потому, что siblings в другой WP-рубрике.

### Proposed apply
- Добавить в interlink-contract пример cross-rubric mapping ipoteka ↔ vtorichka-i-riski для EGRN/аванс hooks.

### Durable applied
- none (первый ipoteka publish; ждём второй run)

### Resolution
status: recorded
article_dir: memory/blog/articles/B08-ipoteku-odobrili-a-registraciyu-otmenili-stroka-v-egrn
wp_post_id: 9063
