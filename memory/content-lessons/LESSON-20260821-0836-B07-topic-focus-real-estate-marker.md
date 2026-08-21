## LESSON-20260821-0836-B07-topic-focus-real-estate-marker
status: proposed
topic_id: B07
category: other
confidence: high

### Evidence
- artifact: memory/scout/assembled-scout-input.md — hook `heirs_first_marriage_3y` («дети от первого брака / отказы / 3 года») без buyer-маркера
  finding: Klyshin angle про наследников не содержит `квартир/егрн/сделк/…` → `research_start --title` с таким текстом = TOPIC FOCUS BLOCKER.
- artifact: scripts/excalibur_blog_topic_focus.py live probe
  finding: `--text "Сын от первого брака не отказался от наследства"` → BLOCK; `--text "Наследство квартиры: …"` → PASS (`allow_hit=квартир`).
- artifact: research-context.json + title-brief.json — финальный title/H1 с «квартиру/квартиры»; research_start прошёл после Title.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- TOPIC_FOCUS_NO_REAL_ESTATE_MARKER
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Scout Wordstat rework до P0 «наследство квартиры» (968 Tyumen) — buyer spine найден.
- Title с объектом сделки («квартиру/квартиры») + Klyshin rhythm — on-focus и читабельно.

### Change
- Scout handoff: до `research_start` title draft **обязан** содержать real-estate marker (`REAL_ESTATE_ALLOW_PATTERNS`); hook-only строка — angle, не title для research_start.
- Title role: если Scout дал hook без маркера — добавить «квартиру/квартиры/ЕГРН/сделку» в первую часть H1, не SEO-хвост.
- Preflight Scout: `python3 scripts/excalibur_blog_topic_focus.py --text "<draft title>"` до handoff.

### Never again
- Не вызывать `research_start` с Klyshin hook без buyer-маркера на real_estate tenant.
- Не полагаться на «наследство» как sufficient marker — только наследственные юридические кластеры без объекта сделки блокируются.

### Proposed apply
- Scout skill/checklist: localize hook → «наследство **квартиры**» / «**квартиру** по наследству» перед handoff.
- После второго run с тем же BLOCK — durable note в scout-excalibur-blog skill (не writer-master-prompt).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
wp_post_id: 8994
