# Scout inputs — 2026-09-02 slot 12:00 YEKT (B21)

## Run context
- topic_market_focus: newbuild_only
- dzen_rf_pack: true
- slot: weekday 12:00 YEKT
- topic_id: B21

## Anti-repeat preflight (DONE)
- used-clusters sync: 2026-09-02, 20 active locks
- live blog today 2026-09-02: «В Тюмени дом сдали без газа и воды — семья не взяла ключи» (KP comms); «В Тюмени оплатили переуступку — застройщик не оформил ДДУ»
- recent newbuild closed: B20 юрлицо+эскроу, бронь+цена 380к, семейная ипотека+эскроу+маткапитал, мокрая стяжка приёмка, траншевая ипотека, B12 срок сдачи+эскроу, переуступка live today

## Proposed cluster (NEW)
- cluster_id: newbuild_developer_installment_balance_increased_before_handover_tyumen
- legal risk: рассрочка в ДДУ / одностороннее изменение остатка перед сдачей
- plot: семья 14 месяцев платила по графику рассрочки от застройщика (~40% цены); за месяц до сдачи корпуса пришло допсоглашение — остаток вырос на ~400 тыс., сроки сжаты; застройщик ссылается на «изменение сметы отделки»; семья отказалась подписывать, застройщик пригрозил расторжением ДДУ
- title draft: В Тюмени платили рассрочку по ДДУ — перед сдачей застройщик поднял остаток
- slug: v-tyumeni-platili-rassrochku-po-ddu-pered-sdachej-zastrojschik-podnyal-ostatok

## Dzen news-casus shape
- event: допсоглашение с новым остатком за месяц до ключей
- risk: потеря внесённых платежей / расторжение ДДУ
- time: «14 месяцев платили» → «за месяц до сдачи»
- finale: отказ подписать → угроза расторжения → семья ищет выход до потери денег
- comment_magnet_angle: «Если в ДДУ прописан график рассрочки — застройщик вообще имеет право поднять остаток за месяц до ключей?»

## Klyshin
- klyshin_hook: none (optional — свежий casus без Klyshin, предпочтительно при риске дубля)

## Wordstat MCP-KV live probes (regions 55+11176 unless noted)
- wordstat_get_user_info: OK
- probe «рассрочка от застройщика тюмень» → 142
- probe «рассрочка от застройщика» (55+11176) → 213; compare RU 225 → 21115
- probe «квартира в рассрочку от застройщика тюмень» → 88
- probe «долгострой тюмень» → 91 (слабее, пересечение с B12 — отклонено)
- probe «штраф застройщику» → 42 (слабее)
- probe «отделка новостроек тюмень» → 44
- rework: hook рассрочка сильный локально; demand spine → «новостройки тюмень» 4649 (55+11176); compare RU 225 → 8792

## Gates pre-check
- topic_focus: PASS (дду)
- scout_helper --check-query: PASS (no duplicate cluster)

## Required handoff fields
Write full `.cursor/excalibur-blog-handoff.md` with all canonical fields per scout SKILL.
