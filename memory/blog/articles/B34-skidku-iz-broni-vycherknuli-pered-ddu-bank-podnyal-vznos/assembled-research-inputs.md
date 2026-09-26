# Assembled research inputs — B34 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Do **NOT** output `DEROUTER RESEARCH BLOCKER`, refuse synthesis, or meta about missing shell. Output **only** the complete `research-notes.md` markdown body per SKILL.md (all required sections: research_date, reader_problem, reader_outcome, practical_facts, constraints, official_verifications table, source_table, writer_safe_urls, voice_angle, surprising_fact, casus_boundary). No h2_outline, no lead paragraph.

**research_date:** 2026-09-26  
**topic_id:** B34  
**cluster_id:** newbuild_booking_discount_revoked_before_ddu_tyumen

## Scout handoff (summary)

- topic_id: B34
- cluster_id: newbuild_booking_discount_revoked_before_ddu_tyumen
- market: Тюмень, newbuild only
- H1 direction: за 3 дня до ДДУ скидку ~380 тыс ₽ из брони вычеркнули — банк поднял первый взнос
- mechanism: бронь + PDF/чат со скидкой → ипотека одобрена под цену со скидкой → в проекте ДДУ скидки нет → банк пересчитывает LTV/ПВ → сделка стоп до пересборки одобрения
- top_energy_mirror: number_claimed_vs_unpaid
- comment_magnet: фиксировать скидку письмом от юрлица застройщика vs PDF в чате
- anti_dupe: PASS; avoid B33 (площадь в акте), same-day planning 54→49 м²
- distinct from B22 (ставка), B29 (нулевой ПВ от застройщика), B31 (страховка)

## Composite casus (editorial — NOT verified reporter case)

- Семья или инвестор, новостройка Тюмень, платная бронь, предварительное одобрение ипотеки
- В брони/КП/PDF зафиксирована скидка ~380 000 ₽ от прайса
- За ~3 календарных дня до подписания ДДУ проект договора без скидки (полная цена)
- Банк пересчитывает первоначальный взнос от полной цены ДДУ и/или уменьшает сумму кредита (LTV)
- Сделка остановлена до нового одобрения или доп. денег
- Нет имён ЖК, банка, застройщика, судов

## Math helper (for Writer, not market stat)

При ПВ 20% от цены ДДУ исчезновение скидки 380 000 ₽ добавляет к требуемому ПВ порядка 76 000 ₽ (20% × 380k). Если банк одновременно режет сумму кредита под LTV, дефicit может быть больше.

## Wordstat MCP-KV (accessed 2026-09-26, region 11176 unless noted)

| phrase | totalCount / top |
|--------|------------------|
| купить новостройку в тюмени | 892 |
| новостройки тюмень | 4326 |
| первоначальный взнос ипотека новостройка | 60 (top: ипотека без первоначального взноса тюмень новостройки — 37) |
| скидка застройщика новостройка | 5 (новостройки скидки от застройщиков — 3) |
| бронирование квартиры новостройка | MCP error empty response (WORDSTAT PARTIAL) |
| скидка застройщика дду | MCP error empty response (WORDSTAT PARTIAL) |

Scout P0 spine locked: «купить новостройку в тюмени» 892; compare «новостройки тюмень» 4326.

## Overlap (published-titles-only.md)

- B22: банк поднял ставку перед ДДУ — другой механизм
- B29: сняли ипотеку без взноса от застройщика
- No duplicate H1/cluster in ledger

## Live sources (accessed_at 2026-09-26)

### Official — ДОМ.РФ семейная ипотека (физлица)

URL: https://xn--h1alcedd.xn--d1aqf.xn--p1ai/instructions/semeinaya-ipoteka/

- Ставка до 6% годовых; ПВ не менее 20% от стоимости жилья
- Лимит льготной части 6 млн ₽ вне Москвы/СПб; комбинированная ипотека до 15 млн ₽ общий кредит
- С 01.02.2026 «одна семья — одна льготная ипотека», супруги — созаёмщики
- Q&A сотрудника организации 25–26.09.2026 (вчера/сегодня на странице): окончательное решение по одобрению каждый банк принимает самостоятельно после полного пакета документов; отдельные ответы про условия с 01.10.2026

### Official regional — Тюменская область, семейная ипотека 2026

URL: https://xn--80aacozicjl1agbl4lraw.xn--p1ai/publications/sila-semi-sila-regiona/semeynaya-ipoteka-v-tyumenskoy-oblasti-v-2026-godu-kak-kupit-zhile-i-poluchit-podderzhku-seme-s-detm/

- Изменения условий семейной ипотеки перенесены на 01.10.2026; до этой даты программа без изменений
- Ставка 6%, ПВ минимум 20%, льготная часть до 6 млн ₽; комбинированная ипотека, рыночная часть «около 20%» в разъяснении (не тариф конкретного банка)
- Совет: не вносить аванс, пока банк не подтвердил одобрение объекта и кредита

### Official — Банк России ключевая ставка

URL: https://www.cbr.ru/press/pr/?file=24072026_133000key.htm

- Ключевая ставка 14,00% годовых (решение о снижении на 25 б.п.) — макрофон, не ставка ипотеки

### Market / expert — бронь фиксирует цену на срок

URL: https://novostroikino.ru/blog/bronirovanie-kvartiry-v-novostroyke-2026/

- datePublished 2026-08-06
- Бронь 3–30 дней фиксирует цену и снимает лот с продажи до ДДУ
- Различие аванса vs невозвратной услуги; ссылка на Роспотребнадзор по возврату аванса (ст. 32 ЗоЗПП)
- Срок брони и автопродление — смотреть в договоре

### Expert — цена в ДДУ vs реклама/бронь

URL: https://docanaliz.ru/blog/proverka-tseny-v-ddu

- Итог в ДДУ может отличаться от рекламы, презентации или соглашения о бронировании
- Проверять формулу цены, скидки, зависимость от способа оплаты и одобрения ипотеки конкретным банком
- Отдельные соглашения на скидку

### Community forum — бронь не включена в ДДУ

URL: https://pronovostroy.ru/topic/36819-включение-суммы-брони-в-дду/

- Живой вопрос: оплачена бронь, в проекте ДДУ сумма брони не учтена / цена иная (форум ProNovostroy)

### Fresh this week (2026-09-20 … 2026-09-26)

1. ДОМ.РФ Q&A 23–26.09.2026 на странице семейной ипотеки — банк решает после полного пакета
2. Telegram tenant channel post 2026-09-26 05:59 UTC — https://t.me/Tyumen_Rieltor/684 (контент про проверку вторички; не доказывает кейс B34, но свежий канал тенанта)
3. Telegram 2026-09-23 — оффер новостройки «семейная от ~3,5%» (риск маркетинговых формулировок vs ДДУ)

### SERP pointers (research-serp.json, not independent verification)

- Dzen titles про «банк перед ДДУ», «скидка снята» — тематический фон, не источник цифр 380k

## Writer-safe URLs (CTA)

- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- https://dzen.ru/holyslav
- tel:+79220016505

## Constraints for notes

- No h2_outline, lead, FAQ skeleton
- No composite disclaimer meta («случай собирательный», «без фамилий») in prose — use casus_boundary factual status instead
- Bank tariff numbers only from official_verifications
- Do not copy B22/B29 research prose
