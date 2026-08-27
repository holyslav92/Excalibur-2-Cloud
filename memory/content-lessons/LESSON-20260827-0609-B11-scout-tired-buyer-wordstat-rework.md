## LESSON-20260827-0609-B11-scout-tired-buyer-wordstat-rework
status: proposed
topic_id: B11
category: structure
confidence: medium

### Evidence
- artifact: .cursor/scout-b11-input.md / memory/scout/klyshin-topic-bank.json
  finding: hook_id `tired_buyer_bad_flat` — «уставший покупатель берёт плохую квартиру»; Klyshin signal ~17.8K views (август 2026); casus: 4 мес поиска, жёлтое заключение, третий наследник, суд через ~2 года.
- artifact: scout handoff
  finding: weak hook probes «проверка квартиры перед покупкой» 3, «риски при покупке квартиры» 17 → rework на buyer spine «купить квартиру в тюмени» 22833 (RU225 40089); sticker cluster «вторичка в тюмени» 6068.
- artifact: research-agent-report.json / assembled-writer-inputs.md
  finding: dzen_casus_shape PASS; отклонены notary_70k (LIVE 39%), summons (WP povestka), matkapital (WP opека), five_court (B03/B04); plot отделён от B07 «сын от первого брака».
- artifact: title-brief.json
  finding: H1 news-casus rhythm без SEO-хвоста; comment_magnet «жёлтое заключение + 4-й месяц — внесли бы аванс?»
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; post 9191 ingest недоступен

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish)

### Keep
- Klyshin hook как angle, Wordstat как evaluate+rework (не binary skip при 3–17 на hook probes).
- Локализация Тюмень + buyer spine до P0 ≥20k («купить квартиру в тюмени»).
- Явный plot guard: третий наследник ≠ B07 сын от первого брака; финал «суд оспорил после регистрации» ≠ превентивный стоп до аванса.
- comment_magnet_angle в handoff — stakes «усталость vs жёлтое заключение».

### Change
- Scout bank: tag `tired_buyer_bad_flat` + default sibling interlink B02/B05/B07/B09 для risk-cluster (как B11 interlink-plan).
- При weak hook probes логировать sticker cluster рядом с final P0 (6068/4071) — cover без Wordstat strips, но H2/spine согласованы.

### Never again
- Drop casus «уставший покупатель» ради чеклиста при отсутствии buyer P0 после rework.
- Путать B11 (третий наследник, post-deal суд) с B07 (сын, отказ) или B10 (телефон до аванса).

### Proposed apply
- `memory/scout/klyshin-topic-bank.md`: B11 row validated — rework path 3→22833 как этalon weak-hook→Tyumen spine.
- После Metrika ingest 9191 — re-evaluate confidence если retention на risk/inheritance cohort выше baseline.

### Durable applied
- none (scout bank уже обновлён в run 5686cb2; behavioral signals отсутствуют)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-v-tyumeni-chetyre-mesyaca-iskali-vtorichku-ustavshij-pokupatel-soglasilsya-na-ri
wp_post_id: 9191
