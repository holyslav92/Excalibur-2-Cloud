## LESSON-20260822-1109-B08-inheritance-sibling-cluster-anti-dup
status: proposed
topic_id: B08
category: structure
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: Scout `story_dup: PASS` — plot отделён от B07 (`inheritance_son_first_marriage`); hook `zags_dead_wife_marital_share` vs B07 «сын от первого брака / отказ наследника».
- artifact: research-agent-report.json#overlap_check
  finding: anti_dup_notes явно фиксируют различие кластеров: ЗАГС не на дату покупки + умершая супруга + супружеская доля ≠ наследник-сын.
- artifact: interlink-gate.json — outbound включает B07 slug; article.html содержит контрастный абзац «Только не путайте…» перед ссылкой на B07.
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (low sample / no behavioral cohort)

### Named blockers
- EVIDENCE_SKIPPED
- LOW_SAMPLE (Metrika absent)

### Keep
- Scout triple gate: при слабом Wordstat по «брачная доля квартиры» (3) — rework на buyer spine «наследство квартира продажа» (157) + P0 «купить квартиру в тюмени» (22880), без drop casus.
- Явный in-body контраст с ближайшим sibling (B07) вместо повторения «наследство/сын/отказ» паттерна.
- Title H1 document-forward («Справка ЗАГС…») вместо длинного scout headline — не дублирует B07 angle.

### Change
- При следующем наследственном casus в кластере «вторичка + скрытый собственник» — до Writer сверять `published-titles-only.md` + plot cluster tag (не только slug overlap).
- В Writer brief явно указывать «contrast sibling» URL и forbidden plot overlap (как в assembled-title-inputs B08).

### Never again
- Публиковать второй casus «наследники мешают сделке» без явного plot diff и контрастной перелинковки на B07/B08.
- Drop Klyshin hook только из-за слабого volume узкого юридического жаргона без buyer rework.

### Proposed apply
- Scout handoff template: поле `plot_cluster` + `contrast_sibling_topic_id` для inheritance-adjacent тем.
- Review-only; Writer prompt не трогать автоматически.

### Durable applied
- none — первый явный PASS sibling-cluster diff B07↔B08; ждём повтор в ≥2 runs.

### Resolution
status: recorded
article_dir: memory/blog/articles/B08-skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo
wp_post_id: 9073
