## LESSON-20260902-1056-B21-installment-balance-ddu-cluster
status: proposed
topic_id: B21
category: geo
confidence: low

### Evidence
- artifact: memory/scout/scout-inputs-2026-09-02-b21.md, assembled-scout-inputs.md
  finding: new cluster `newbuild_developer_installment_balance_increased_before_handover_tyumen`; story_dup PASS vs B12 (`ddu_escrow_handover_delay_tyumen` — перенос сдачи / заморозка эскроу после внесения), B20 (`newbuild_developer_legal_entity_change_ddu_escrow_tyumen` — смена юрлица до эскроу), live booking/price-bump plots; plot = 14 мес. рассрочка по графику ДДУ → допсоглашение с ростом остатка ~400k и сжатием сроков за месяц до ключей → угроза расторжения при отказе подписать.
- artifact: scout Wordstat log (scout-inputs-2026-09-02-b21.md)
  finding: hook P0 «рассрочка от застройщика тюмень» **142** (55+11176); compare «рассрочка от застройщика» RU225 **21115**; demand spine rework → «новостройки тюмень» **4649** (compare RU225 8792); отклонён «долгострой тюмень» 91 (пересечение B12).
- artifact: research-notes.md
  finding: editorial firewall — отказ от допсоглашения ≠ автоматическое основание расторжения (ст.9 214-ФЗ требует фактической просрочки по **исходному** графику); ст.5 214-ФЗ — цена/график меняются только при явном пункте ДДУ; «изменение сметы отделки» без пункта — не основание; modeled casus без ЖК/застройщика/банка.
- artifact: derouter-opus-stamp-sol-trim.json, quality-bar-9.json
  finding: Sol TRIM 2223→2154 слов (legal-heavy 6-H2); final quality-bar `word_count: 2113`, `spine_once_no_recap: true`, `comment_magnet_question: true`; stylo PASS (delta 2.368) при spine_overlap 0.071 выше gold — gate не FAIL.
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape: true` (B08/B09/B15/B20 pattern), budget not exhausted, gate PASS — 6-й live OCR escape (cross_run duplicate, отдельный lesson не нужен).
- artifact: interlink-gate.json
  finding: 4 outbound siblings incl. B12, B20, B19 family-ipoteka — explicit plot differentiation в тексте.
- artifact: wp-publish-result.json
  finding: publish PASS post **9536**, live-page PASS, 7 inline uploads, categories dokumenty-i-oformlenie / riski-sdelki / pokupka-kvartiry.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет ingest; behavioral baseline для post 9536 недоступен)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0, no behavioral baseline)

### Keep
- Wordstat rework: при сильном hook «рассрочка от застройщика тюмень» 142 — spine «новостройки тюмень» 4649 как demand anchor; не брать «долгострой» 91 (B12 collision).
- Plot differentiation: рассрочка+допсоглашение на остаток **до** ключей vs B12 escrow freeze **после** внесения vs B20 смена юрлица **до** эскроу vs booking-only price bump — четыре разных DDU-кластера.
- Dzen news-casus: 14 мес. платежей → допсоглашение за месяц до сдачи → agency ending (сравнить проект с зарегистрированным ДДУ, не подписывать под давлением); comment magnet «имеет ли право поднять остаток за месяц до ключей».
- Sol TRIM brief: явный список spine-once targets (ст.5 214-ФЗ, «близость ключей», «отдел продаж») без потери H2/inline/CTA/interlinks — 2-й успешный прогон (см. LESSON-20260901-1338-B20-sol-trim-spine-once).

### Change
- Scout: добавить `newbuild_developer_installment_balance_increased_before_handover_tyumen` в `shared/scout-story-clusters.json` (sync-used-clusters ledger only) — needs-human.
- После Metrika credentials: cohort `cluster:newbuild_developer_installment_balance_increased_before_handover_tyumen` vs B12/B20 DDU siblings.

### Never again
- Смешивать B21 с переносом сдачи / заморозкой эскроу после внесения (B12).
- Смешивать B21 со сменой юрлица / неоткрытым эскроу до внесения (B20).
- Писать, что отказ от допсоглашения = автоматическое основание расторжения без проверки просрочки по исходному графику.
- Брать «долгострой тюмень» как P0 при риске дубля B12.

### Proposed apply
- `memory/scout/used-clusters.json`: lock `newbuild_developer_installment_balance_increased_before_handover_tyumen` until 2026-10-02 (B21 ledger).
- Scout story-cluster registry entry (human): required_groups рассрочка/график ДДУ + допсоглашение на остаток + угроза расторжения.

### Durable applied
- memory/scout/used-clusters.json — добавлен cluster row B21 (content-learner 2026-09-02); rollback: удалить row при erroneous lock

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-platili-rassrochku-po-ddu-pered-sdachej-zastrojschik-podnyal-ostatok
wp_post_id: 9536
