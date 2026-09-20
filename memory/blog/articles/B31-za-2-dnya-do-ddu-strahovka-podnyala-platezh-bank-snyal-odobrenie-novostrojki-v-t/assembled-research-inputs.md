# Assembled research inputs — B31 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Do **NOT** output `DEROUTER RESEARCH BLOCKER` or refuse synthesis. Output the full `research-notes.md` body only per SKILL.md from the facts below.

**research_date:** 2026-09-20  
**topic_id:** B31  
**title:** За 2 дня до ДДU страховка подняла платёж на 18 тысяч — банк снял одобрение новостройки в Тюмени  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**cluster_id:** `newbuild_mortgage_insurance_requote_before_ddu_tyumen`  
**top_energy_mirror:** `number_claimed_vs_unpaid`  
**newbuild_mechanism:** семья на финишной прямой покупки **новостройки** Тюмени; предварительное одобрение ипотеки с **ориентировочной** премией личного страхования (жизнь/здоровье) в расчёте платежа; за **2 дня** до подписания ДДU страховщик из списка банка выставил **финальный** полис — анкета здоровья / класс риска объекта → премия выше; полный платёж **+~18 000 ₽/мес**; банк пересчитал ПДН и **отозвал одобрение**; эскроu не открывали; бронь **~60–90 тыс ₽** под спором (composite casus)

## Scout handoff (2026-09-20, slot 12 YEKT)

- **dzen_casus_shape:** PASS  
- **comment_magnet_angle:** «Если страховка в последний день добавляет 18 тысяч к платежу — вы успеваете пересобрать одобрение или откладываете покупку?»  
- **why_newbuild_not_secondary:** ДДU + эскроu + ипотека на строящийся объект, без вторички  
- **anti_dupe_hard:** PASS; не B30 уступка/запрет; не B29 нулевой ПВ; не B22 только ставка  
- **fact boundaries:** composite; без имён ЖК/банка/страховщика; **18k/мес** и **60–90k бронь** — параметры кейса

### Locked editorial spine

1. Семья выбирает квартиру в **новостройке** Тюмени, бронь, одобрение ипотеки «под ключ» с **расчётной** страховкой.  
2. Менеджер и банк показывают платёж с **скидкой за страховку жизни/здоровья** (типичная связка на новостройках).  
3. За **2 дня** до подписания ДДU приходит **финальное** предложение страховщика — не «как в калькуляторе».  
4. Премия выросла (анкета, ИМТ, хроника в декларации, класс строительства/этажность для имущественного блока позже — в casus акцент на **личном** полисе до выдачи).  
5. Банк: новый полный платёж **не проходит** лимит одобрения → **одобрение снято** / нужен новый пакет.  
6. ДДU **не подписали**, эскроu **нет**; семья спорит о **брони** 60–90 тыс.

## Wordstat MCP-KV (live 2026-09-20, region 55 + 11176)

| phrase | volume | note |
|--------|-------:|------|
| купить новostройку в тюмени | **1917** | P0 spine |
| страхование ипотеки | **913** | mechanism (55) |
| приемка квартиры в новостройке тюмень | 29 | local angle |
| ипотека от застройщика тюmenь | 514 | sibling demand |
| полис страхования ипотеки | 93 | jargon |

**wordstat_rework:** «страхование ипотеки новостройка тюмень» weak → spine 1917 + mechanism 913

## Fresh signals (week of 2026-09-20; accessed 2026-09-20)

1. **72.ru — 17.09.2026** — свежий тюменский медиа-сигнал недели. https://72.ru/text/gorod/2026/09/17/76646611/

2. **Закон 102-ФЗ ст. 31** — обязательное страхование **заложенного имущества**; личное страхование — по договору. https://www.consultant.ru/document/cons_doc_LAW_19396/1870b8c7a53147c57594fde9ddd09927b182c871/

3. **Поправки с 01.07.2024** — ограничение роста ставки при отказе от добровольной страховки (уровень «как без страховки на дату договора»). https://www.gipernn.ru/zhurnal/ipoteka/novosti/rost-ipotechnoy-stavki-pri-otkaze-ot-strahovki-ogranichat-s-iyulya-2024-goda

4. **Обзор Sravni.ru** — банки повышают ставку при отказе от личного страхования (ориентиры по банкам, не офicial витрина каждого продукта). https://www.sravni.ru/text/kak-rastyot-stavka-pri-otkaze-ot-strahovki-pri-ipoteke/

5. **UnistroyRF explainer** — на этапе ДДU залог = права требования; имущественный полис часто **после** регистрации; **личное** страхование часто условие сниженной ставки **до** выдачи. https://unistroyrf.ru/blog/strahovanie_kvartiry_pri_ipoteke/

6. **Telegram @Tyumen_Rieltor** — tenant channel. https://t.me/Tyumen_Rieltor

7. **Дзен tenant** https://dzen.ru/holyslav

## official_verifications (required section in notes)

- Verify at least one **major bank** public page on mortgage insurance requirement / accredited insurers list (Sber Domclick or VTB mortgage insurance page) — accessed 2026-09-20, type official in source_table.
- CBR / law refs for 102-ФЗ and 2024 consumer credit amendments — type official/law.

## Overlap published

- **B29** — сняли **нулевой ПВ** / акцию застройщика (+18k платёж) — другой механизм (ПВ vs страховка).  
- **B22** — **ставка** выросла накануне ДДU.  
- **B31** — **финальная премия страховщика** ломает одобрение за 2 дня до ДДU.

Output complete research-notes.md + ensure research-agent-report.json can PASS with fresh community/news + official_verifications.
