## LESSON-20261001-0611-B34-school-pd-deadline-cluster
status: proposed
topic_id: B34
category: geo
confidence: low

### Evidence
- artifact: research-notes.md
  finding: cluster `newbuild_pd_school_deadline_vs_ads_tyumen`; composite casus «школа на рендере vs раздел 22 PD / срок 2030»; anti-dupe vs B27/B28; Wordstat P0 «новостройки тюмень» ~3553, узкие «школа+декларация» слабее — spine через newbuild проверку до ДДУ.
- artifact: quality-score-notes.md + article-quality-score.json
  finding: первый Sol FAIL (lead consequence, finale-third-retell, lecture-tail 214-ФЗ); **один** repair → PASS, `word_count` 1413 в target 1400–1600.
- artifact: quality-bar-9.json + wp-publish-result.json
  finding: all PASS; publish post **11359**, live-page PASS, 7 inline, OCR escape cover PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 11359)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE

### Keep
- Scout cluster: PD school deadline vs ads — отдельный от escrow/apartments/gas plots.
- Quality-score repair без padding: trim finale retell + убрать law-dump хвост, не трогая факты writer.html.

### Change
- После Metrika credentials: cohort `cluster:newbuild_pd_school_deadline_vs_ads_tyumen`.

### Never again
- Подавать «2030 в декларации» как репортаж о конкретном ЖК (composite только в research-notes).
- Повторять mid-scene «передадут если школа оформлена» в closing beat.

### Proposed apply
- Scout ledger: `newbuild_pd_school_deadline_vs_ads_tyumen` (B34 lock 2026-10-01).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B34-shkola-v-reklame-zhk-vs-proektnaya-deklaraciya-ddu-ne-podpisali
wp_post_id: 11359
