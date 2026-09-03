## LESSON-20260903-1001-B22-showroom-ddu-finish-cluster
status: proposed
topic_id: B22
category: geo
confidence: low

### Evidence
- artifact: .cursor/excalibur-blog-handoff.md, research-notes.md
  finding: new cluster `newbuild_showroom_finish_ddu_mismatch_tyumen`; story_dup PASS vs B21 (кладовка), B20 (смена юрлица), B12 (эскроу delay); plot = шоу-рум чистовая vs приложение предчистовая → отказ до аванса → снятие брони → доплата 420–480 тыс.
- artifact: scout Wordstat (handoff)
  finding: P0 «новостройки тюмень» 4683, «купить новостройку в тюмени» 866 — strong newbuild demand spine.
- artifact: quality-bar-9.json
  finding: `all_pass: true` after end CTA path fix + solo cover regen; word_count 1821, 7 inline, 4 sibling interlinks, comment_magnet PASS.
- artifact: wp-publish-result.json
  finding: publish PASS post **9588**, featured 9589, 7 inline uploads, inbound interlink ×3.
- artifact: cover/cover_qa.json
  finding: solo cover attempt 1 PASS (quad-split cover failed phone/hook/meme pixels).
- artifact: stylo-report.json
  finding: initial FAIL δ=3.06 → stylo Sol rewrite PASS δ=1.60; rewrite briefly broke `excalibur-cta-*` div classes (manual restore).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- STYLO_CTA_CLASS_REGRESSION (manual fix in article.html)

### Keep
- Newbuild showroom vs DDU appendix casus — high engagement comment magnet («подписываете ДДУ при предчистовой в приложении?»).
- Solo cover regen after quad-split pixel FAIL — budget 1/2 attempts, PASS without OCR escape.
- End CTA: literal `/` and `/gajdy/` paths required by quality-bar gate (not only `{{SITE_BASE}}`).

### Change
- Stylo Sol rewrite contract: preserve `excalibur-cta-early|mid|end` class names; never collapse to generic `cta-block`.
- `research_start` slug vs `title-brief` slug divergence — align early or stamp canonical slug in article.meta before publish.

### Never again
- Publish with incomplete `article.meta.json` (missing `theme_blocks`, `editorial_swarm`).
- Rely on quad-split cover panel for OCR-critical hook+phone without solo cover fallback.

### Proposed apply
- `shared/scout-story-clusters.json`: cluster `newbuild_showroom_finish_ddu_mismatch_tyumen` (fixer 2026-09-03).
- `memory/scout/used-clusters.json`: lock until 2026-10-03.

### Durable applied
- shared/scout-story-clusters.json — cluster registry entry
- memory/scout/used-clusters.json — B22 lock row

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-na-pokaze-byla-chistovaya-v-ddu-okazalas-predchistovaya
wp_post_id: 9588
