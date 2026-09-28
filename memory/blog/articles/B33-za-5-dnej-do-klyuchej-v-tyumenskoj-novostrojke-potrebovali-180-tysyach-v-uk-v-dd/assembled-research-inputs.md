# Research assembly — B33 (2026-09-27)

## research_date / topic

- research_date: 2026-09-27 (Europe/Moscow, воскресенье)
- topic_id: B33
- title: За 5 дней до ключей в тюменской новостройке потребовали 180 тысяч в УК — в ДДУ этой строки не было
- cluster_id: newbuild_uk_membership_fee_before_keys_not_in_ddu_tyumen
- market: newbuild_only, Tyumen

## Scout handoff (LOCKED)

- top_energy_mirror: stopped_before_money
- newbuild_mechanism: семья на финале новостройки Тюмени; за 5 дней до ключей застройщик/ОП требует «взнос в УК» / членский взнос ~180 тыс ₽ до подписания акта; в ДДУ и брони строки нет; банк не открывает финальный транш / семья не вносит наличные — стоп до акта приёмки
- why_newbuild_not_secondary: объект по ДДУ на этапе ввода/ключей; риск навязанных платежей до регистрации права
- dzen_casus_shape: PASS | event: ключи | risk: внезапный взнос УК | time: 5 дней до ключей | finale: стоп, проверка ДДУ/214-ФЗ, agency до акта
- comment_magnet_angle: требовали ли оплатить УК/«членский взнос» до ключей при отсутствии строки в ДДУ
- anti_dupe_hard: PASS
- P0 Wordstat (scout live MCP): «новостройки тюмень» 8242 (reg 55); «купить новостройку в тюмени» 1928

## Overlap (published-titles-only only)

- B21 кладовка по ДДУ на ключах — другой механизм (помещение), не UK fee
- B25 чистовая на приёмке — акт/отделка, не УК
- B12 срок сдачи/эскроу — другой кластер
- Нет опубликованного заголовка про взнос УК ~180 тыс до ключей

## research-serp.json summary (searched 2026-09-27)

- SERP часто тянет соседние тюменские сюжеты с «180 тысяч» (просрочка платежа по рассрочке ДДУ / удержание при расторжении): https://dzen.ru/a/ap6ljsSWjwEstOtz — **не путать** с механизмом scout (взнос УК до акта)
- https://dzen.ru/a/apgnGspJF0LmJaPv — кладовка по ДДУ (близко к B21)
- Domclick/Kontur 2026 — неустойка застройщика после отмены моратория с 01.01.2026 (контекст ключей, не UK fee)
- nashgorod.ru — компенсации за срыв сроков сдачи

## Wordstat live (MCP-KV, accessed 2026-09-27)

| phrase | region | totalCount / top |
|--------|--------|------------------|
| новостройки тюмень | 55 | 3504 (scout preflight same day reported 8242 — wider window/aggregation; оба зафиксировать) |
| купить новостройку в тюмени | 55 | 678 (scout 1928 — расхождение, не выдумывать единую цифру; P0 spine = новостройки тюмень) |
| передача ключей новостройка | 55 | 3 (слабый хвост → rework на spine) |
| взнос управляющая компания новостройка | 225 | PARTIAL totalCount only: 1 |
| членский взнос управляющая компания | 225 | PARTIAL totalCount only: 21 |

Top under «новостройки тюмень» (55): квартиры в тюмени новостройки 802; купить новостройку в тюмени 678; от застройщика 469; жк новостройки 133.

## Fresh signal this week (required)

1. **InvestFuture** — статья обновлена **26.09.2026** про «первую квитанцию» и незаконные начисления УК до АПП; ссылка на ст. 153 ЖК РФ; URL: https://investfuture.ru/articles/pervaya-kvitantsiya-v-novostroyke-s-podvokhom-skrytaya-ulovka-uk-iz-za-kotoroy-novosely-platyat-zastroyschiku
2. **Pravoved.ru Q&A** — кейс 2026: начисления ЖКУ до акта приёма-передачи при ДДУ неправомерны; п. 6 ч. 2 ст. 153 ЖК РФ; https://pravoved.ru/question/5012637/
3. Tenant channels (signal): https://t.me/Tyumen_Rieltor , https://dzen.ru/holyslav

## Community / media — UK fees before keys (not official tariffs)

- РБК Недвижимость: после ввода дома застройщик в 5 дней заключает договор с УК (ч. 14 ст. 161 ЖК); обязанность дольщика платить ЖКУ — после АПП или регистрации права (ст. 153 ЖК); https://realty.rbc.ru/news/69a060be9a79478a370de1f7
- Всеостройке.рф 2026: платежи «задним числом» до передачи — на застройщике; https://xn--b1agapfwapgcl.xn--p1ai/platezhki-zadnim-chislom-bolshe-nezakonny-kogda-dolshhik-realno-objazan-platit-za-zhku-v-2026-godu/
- T-J 2026: УК не может менять тариф содержания без ОСС; https://t-j.ru/ask/uk-podnyala-tseny/
- Тюмень: АиФ/МегаТюмень — тариф УК озвучивают на встрече **перед передачей ключей** (Брусника, не цена ДДУ): https://tmn.aif.ru/realty/pochemu-tarify-na-soderzhanie-zhilya-takie-dorogie-obyasnyaet-developer
- URA.RU 29.01.2026 — конфликт тарифа УК «Брусника» в тюменской новостройке (78 ₽/м², ~7800 ₽/мес на 100 м²) — **другой сюжет** (тариф после заселения/голосование), но локальный heat по УК в новостройках Тюмени: https://ura.news/news/1053064091

## 214-FZ / DDU constraints (official law — Consultant)

- ФЗ-214: https://www.consultant.ru/document/cons_doc_LAW_51038/
- **Ст. 5** — цена договора: определяется как сумма, которую участник обязан уплатить застройщику; изменение цены — только в случаях, предусмотренных законом и договором (Writer: платежи вне цены ДДУ требуют отдельного основания)
- **Ст. 8** — передача объекта: застройщик обязан передать объект в срок; участник обязан принять объект; приёмка по акту; просрочка передачи — неустойка (ст. 10)
- **Ст. 4** — договор должен содержать существенные условия, в т.ч. цену (связка с ст. 5)
- Эскроу: ст. 15.4–15.5 — расчёты через счёт эскроу; навязанный «взнос УК» не является основанием для банка открыть финальный транш, если не в ипотечном/ДДУ пакете (механика кейса scout)

## ЖК РФ (official — для UK/JKU timing)

- **Ст. 153 ЖК РФ** (ч. 6 ч. 2): обязанность участника долевого строительства оплачивать ЖКУ с момента подписания передаточного акта (или иного документа о передаче); до этого — застройщик (разъяснения Минстроя цитируются в РБК, Pravoved, IF)
- **Ст. 161 ЖК РФ ч. 14**: временный договор управления после ввода — застройщик; это не обязывает дольщика платить **до** своего АПП
- «Членский взнос» — категория ТСЖ/кооператива; обычная УК взимает плату за содержание по договору управления/тарифу, утверждённому собственниками, а не произвольный lump-sum «взнос» как условие выдачи ключей

## Casus editorial boundary (for Writer)

- Композитный тюменский newbuild-кейс: сумма **~180 000 ₽** как параметр сюжета scout, **не** рыночный стандарт и не тариф УК из официального прайса
- Не называть конкретный ЖК/застройщика/УК без источника; не утверждать, что «все так делают»
- Отделить от SERP-истории «5 дней просрочки рассрочки → удержание 180 тыс при расторжении ДДУ»
- Банк: не придумывать комиссии; финальный транш — по кредитному договору и эскроу-процедуре банка (без точных % без official person-page)

## CTA / writer_safe_urls base

- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- tel:+79220016505
- https://dzen.ru/holyslav

## Task for research-notes.md

Produce Russian research-notes.md with sections: research_date, topic_id, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, local_context, voice_angle, surprising_fact, official_verifications (214-FZ, ЖК 153/161 — consultant URLs; no bank tariff claims), source_table (accessed_at 2026-09-27), writer_safe_urls. No h2_outline, no lead, no FAQ skeleton.
