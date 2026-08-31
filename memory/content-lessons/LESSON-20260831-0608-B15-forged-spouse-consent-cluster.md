## LESSON-20260831-0608-B15-forged-spouse-consent-cluster
status: proposed
topic_id: B15
category: geo
confidence: low

### Evidence
- artifact: quality-bar-9.json
  finding: all_pass — word_count 1968, h2 6, inline_figures 7, sibling_interlinks 4; gates `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `spine_once_no_recap` PASS.
- artifact: scout handoff / research-context
  finding: cluster_id `forged_spouse_consent_blocks_advance`; P0 «согласие супруга на продажу квартиры» 54 (Tyumen+oblast); distinct from `deceased_spouse`, `marital_share_heirs`, `doverennost_svo`; comment_magnet «конверт vs проверка у нотариуса до аванса».
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B08 (умерший супруг/брак), B09 (ипотека/ЕГРН), B14 (справка банка) — document-risk siblings; не дублирует deceased_spouse plot.
- artifact: wp-publish-result.json / wp-publish-log
  finding: post 9368 published; wp_category_slugs dokumenty-i-oformlenie + vtorichka-i-riski + riski-sdelki; live_page_gate PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет CTR/retention для post 9368

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет behavioral ingest)

### Keep
- News-casus: нотариальное согласие в конверте + срыв **перед авансом** — agency landing, не «никогда не покупать».
- Wordstat rework от «мнимая сделка» (cluster collision) к buyer P0 «согласие супруга» — локализация без court_took_apartment dup.
- Triple WP rubric (документы + вторичка + риски сделки) для document-forgery casus.
- Interlink B08 как sibling contrast (умерший супруг vs поддельное согласие живого) — не spine repeat.

### Change
- Scout: закрыть `forged_spouse_consent_blocks_advance` в used-clusters на 30d; sibling defaults → B02/B08/B09/B14 для document-risk P0.
- Description/card: сохранять разрыв H1 («не подтвердили») vs scout title draft («поддельное») — осторожная формулировка без утверждения подделки как факта.

### Never again
- Повторять deceased_spouse / marital_share_heirs spine под видом «согласие супруга».
- Выводить engagement из quality-bar PASS без Metrika cohort.

### Proposed apply
- Scout klyshin bank: tag `forged_spouse_consent` + closed cluster 30d; interlink defaults document-risk siblings.
- После Metrika ingest для 9368 — re-evaluate confidence medium/high если retention совпадает с B02/B08 document-risk cohort.

### Durable applied
- none (один run, evidence SKIP, нет Metrika)

### Resolution
status: recorded
article_dir: memory/blog/articles/B15-v-tyumeni-poddelnoe-soglasie-suprugi-ostanovilo-sdelku-pered-avansom
wp_post_id: 9368
