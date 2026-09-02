## LESSON-20260902-0619-B21-pereustupka-developer-refused-cluster
status: proposed
topic_id: B21
category: geo
confidence: low

### Evidence
- artifact: research-agent-report.json
  finding: cluster_id `newbuild_assignment_developer_refused_dd_reregistration_tyumen`; `story_dup_check: PASS`; P0 «купить новостройку в тюмени» 874 (Tyumen+oblast) после rework от «переуступка новостройки» (10); support «переуступка квартиры в новостройке риски» 2.
- artifact: assembled-research-inputs.md
  finding: plot firewall — **не** B12 (эскроу заморожен), **не** B19 (семейная ипотека/маткапитал), **не** B20 (смена юрлица); B21 стоп **до** эскроу — аванс цеденту, право требования не закрепилось.
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2117, h2 6, inline_figures 7, sibling_interlinks 4; `comment_magnet_question`, `spine_once_no_recap`, `no_composite_disclaimer` PASS.
- artifact: interlink-plan.json
  finding: outbound B02 (расписка/аванс), B12 (эскроу freeze contrast), B19 (ипотека/эскроу), B20 (юрлицо/ДДУ) — newbuild sibling firewall; inbound B06/B04/B09.
- artifact: wp-publish-result.json
  finding: post 9510 published; wp_category_slugs dokumenty-i-oformlenie + riski-sdelki + pokupka-kvartiry; live_page_gate PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет behavioral ingest для post 9510

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет Metrika cohort)

### Keep
- News-casus: оплата переуступки ≠ статус дольщика; agency landing «проверить до аванса», не «никогда не покупать переуступку».
- Wordstat rework: слабый tail «переуступка» (10) → buyer P0 «купить новостройку в тюмени» (874) без ухода во вторичку.
- Plot differentiation в тексте и interlink: B12/B19/B20 anchors как firewall, не spine repeat.
- Triple WP rubric (документы + риски + покупка новостройки) для assignment/цессия casus.

### Change
- Scout: закрыть `newbuild_assignment_developer_refused_dd_reregistration_tyumen` в used-clusters на 30d.
- Interlink defaults для assignment cluster → B02/B12/B19/B20 (advance vs escrow vs mortgage vs legal entity).

### Never again
- Смешивать B21 с заморозкой эскроу (B12), маткапиталом (B19) или сменой юрлица (B20) как один сюжет.
- Drop hook при слабом «переуступка» Wordstat без rework на newbuild buyer P0.
- Выводить engagement из quality-bar PASS без Metrika cohort.

### Proposed apply
- Scout story-cluster bank: tag `newbuild_assignment_developer_refused` + 30d lock; sibling defaults assignment-risk quartet.
- После Metrika ingest для 9510 — re-evaluate confidence medium/high если retention совпадает с B12/B20 newbuild-document cohort.

### Durable applied
- none (один run, evidence SKIP, нет Metrika)

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat-/
wp_post_id: 9510
