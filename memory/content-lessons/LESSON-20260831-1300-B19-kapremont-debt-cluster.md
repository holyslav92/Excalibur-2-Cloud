## LESSON-20260831-1300-B19-kapremont-debt-cluster
status: proposed
topic_id: B19
category: geo
confidence: low

### Evidence
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2117, h2 6, inline_figures 7, sibling_interlinks 4; gates `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `spine_once_no_recap`, `dzen_reading_time_ok` (11 min est) PASS.
- artifact: scout handoff / memory/scout/assembled-scout-inputs.md
  finding: cluster_id `kapremont_debt_new_owner_blocks_sale`; plot-demand «долг по капремонту» 29 (Tyumen 55+11176); final P0 buyer spine «купить квартиру в тюмени вторичка» 4146; distinct from egrn_line_blocks_advance, fssp_arrest, communal_share, forged_spouse_consent; comment_magnet «Справку из УК о долгах по капремонту вы запрашиваете всегда — или считаете, что „чистой“ выписки ЕГРН достаточно?»; klyshin none (fresh casus preferred).
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B09 (ипотека/ЕГРН), B14 (справка банка), B15 (согласие супруги) — document-risk + hidden-liability siblings; inbound updates B06, B04, B09.
- artifact: cover/cover_qa.json + cover/quad-solo-result-cover.json
  finding: grsai standard attempt 1 PASS; `ocr_false_positive_escape` applied (B08/B09/B15 pattern); hook 6 слов «Чистая ЕГРН скрыла долг по капремонту»; sticky «Аванс остановили вовремя»; no cover_budget_exhausted.
- artifact: wp-publish-result.json / article.meta.json
  finding: post 9398 published; wp_category_slugs `vtorichka-i-riski` only; live_page_gate PASS; 7 inline uploads OK.
- artifact: memory/scout/used-clusters.json
  finding: `kapremont_debt_new_owner_blocks_sale` **not yet synced** post-publish (ledger gap vs scout handoff PASS).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет ingest для post 9398

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет behavioral ingest)
- CLUSTER_LEDGER_GAP (scout cluster not in used-clusters.json after publish)

### Keep
- News-casus: «чистая» ЕГРН + скрытый долг капремонта/УК → срыв **за три дня до аванса**; agency landing (выйти до денег), не «вторичка — мина».
- Scout Wordstat rework: niche plot-demand 29 + buyer P0 spine 4146 — локализация без novostroyka/DDU (B12) и без egrn-line dup.
- Cover hook contrasts ЕГРН vs капремонт — on-topic buyer jargon; attempt 1 success с OCR escape flakes only (не budget exhaust).
- Interlink B09/B14/B15 как sibling contrast (ЕГРН строка / справка банка / согласие супруги) — не spine repeat.

### Change
- Scout post-publish: sync `kapremont_debt_new_owner_blocks_sale` в `used-clusters.json` (30d lock).
- Scout klyshin bank: tag `kapremont_debt` + interlink defaults B02/B09/B14/B15 для hidden-liability P0.
- Director: рассмотреть dual rubric `dokumenty-i-oformlenie` + `vtorichka-i-riski` для УК/справка casus (B19 только vtorichka — proposal, не auto-apply).

### Never again
- Повторять egrn_line_blocks_advance / fssp_arrest spine под видом «долг капремонта».
- Считать scout story_dup PASS закрытым без ledger sync в used-clusters.
- Выводить engagement из quality-bar PASS без Metrika cohort.

### Proposed apply
- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` после publish B19 → lock cluster 30d.
- После Metrika ingest для 9398 — re-evaluate confidence medium/high если retention совпадает с B09/B14 document-risk cohort.

### Durable applied
- none (один run, evidence SKIP, нет Metrika, cluster ledger gap)

### Resolution
status: recorded
article_dir: memory/blog/articles/B19-v-tyumeni-dolg-po-kapremontu-ostanovil-sdelku-spravka-uk-za-tri-dnya-do-avansa
wp_post_id: 9398
