## LESSON-20260904-0551-B22-acceptance-defect-act-pressure-cluster
status: proposed
topic_id: B22
category: geo
confidence: low

### Evidence
- artifact: research-context.json / title-brief.json
  finding: P0 hook «приёмка новостройки — дефекты — застройщик потребовал подписать акт»; newbuild-only priemka casus (давление подписать акт без ключей).
- artifact: article.html
  finding: plot = семья на приёмке, дефекты в акте, ультиматум «подпишите сегодня»; agency ending (решить дома до дня приёмки); comment magnet preserved; 4 sibling interlinks (B12 escrow delay, kladovka, etc.).
- artifact: cover/cover_qa.json
  finding: PASS with OCR false-positive escape (B08/B09 pattern); hook «Ключи требуют — дефекты оставляют вам»; meme priest+cat; no Wordstat strips on cover.
- artifact: stylo-report.json
  finding: stylo_pass true (delta 2.47 < 2.85); no stylo-driven Sol rewrite — length/CTA issues handled post-Sol.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; post-publish behavioral baseline unavailable

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0)

### Keep
- Priemka/defect pressure cluster as distinct from wet-screed daily (`newbuild_acceptance_wet_screed_keys_denied`) — plot = **акт с дефектами / отказ подписать**, not material defect type alone.
- Early TG+MAX after prose lead; ending landing agency (подготовка до приёмки), not panic.

### Change
- Scout: tag cluster `newbuild_acceptance_defect_act_pressure_tyumen`; 30d anti-repeat vs wet-screed priemka and B12 escrow-delay.
- Cover: priemka hooks work with «Не спечите» sticky + tape/measuring props — reuse for sibling priemka plots with 14d motif anti-repeat.

### Never again
- Retitle priemka casus into вторичка plot (newbuild-only lock).
- Drop comment magnet on legal-heavy priemka posts — engagement bomb pillar.

### Proposed apply
- Add cluster id to scout ledger when next priemka hook scouted (human review `shared/scout-story-clusters.json`).
- Metrika cohort tag `priemka_defect_act` after credentials fixed — compare vs B12/B20 newbuild clusters.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-na-priemke-naschitali-defekty-zastrojschik-potreboval-podpisat-akt
wp_post_id: 9614
