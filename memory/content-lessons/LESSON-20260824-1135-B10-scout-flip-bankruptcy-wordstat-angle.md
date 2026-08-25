## LESSON-20260824-1135-B10-scout-flip-bankruptcy-wordstat-angle
status: proposed
topic_id: B10
category: geo
confidence: medium

### Evidence
- artifact: memory/scout/assembled-scout-inputs-b10.md
  finding: Klyshin hook `five_court_schemes` → sub-angle **быстрый переход права / flip**; Wordstat rework от слабого «проверка квартиры перед покупкой» (8) к P0 «купить квартиру в тюмени» (22660) + risk sticker «банкротство продавца квартиры» (28); dzen_casus_shape PASS с финалом финуправляющего.
- artifact: description-brief.json + article.html
  finding: Опубликованный casus — чистая выписка ЕГРН + 3 месяца владения продавца + иск по ст. 61.2 банкротства через полгода; comment magnet про стоп-сигнал «три месяца».
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID absent)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Scout: Klyshin flip как **угол**, не как единственный P0-запрос — Wordstat rework к buyer P0 + risk cluster.
- Triple gate: original hook + final P0 phrase+volume + `dzen_casus_shape: PASS` + `comment_magnet_angle` в handoff.
- Контент: flip ≠ мошенничество (явный абзац в article.html) — снижает ложный moral panic, держит stakes на банкротстве.

### Change
- Scout skill/runbook: при flip-хуке из Klyshin сразу логировать **парный** risk-cluster («банкротство продавца», «переход прав», «срок владения») даже при слабом объёме — для Writer stakes и cover-text inline labels.
- Sticker cluster: risk phrase (28) + geo buyer P0 (22660) — не дропать flip ради чеклиста.

### Never again
- Не публиковать flip-casus только как «короткий срок = мошенник» без банкротного финала и практики до аванса.
- Не skip Wordstat rework при volume<100 на первом probe — локализовать Тюмень + buyer jargon.

### Proposed apply
- Добавить в scout-excalibur-blog пример handoff: flip hook → bankruptcy/EGRN-clean finale (B10 pattern).
- После Metrika ingest — проверить retention на H2 «Банкротство продавца» vs лид.

### Durable applied
- none (первый именованный run flip+bankruptcy; ждём ≥2 runs или Metrika cohort)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-vypiske-vse-chisto-prodavec-vladel-tri-mesyaca
wp_post_id: 9141
