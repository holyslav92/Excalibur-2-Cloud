# TASK FOR DEROUTER (research role)

You are already running inside `excalibur_blog_derouter_opus_chat.py`. Live fetch and Wordstat are DONE by the conductor. Your only job: write the final markdown research brief using ONLY facts below. Do not refuse. Do not ask for shell. Output markdown sections only (no preamble).

# Assembled research inputs — B34 — 2026-10-05

## Scout handoff (summary)

- topic_id: B34, slot: vtorichka, cluster: bti_area_shortfall_secondary_mortgage_tyumen
- Mechanism: перед подписанием ДКП на вторичке свежий акт БТИ показал площадь на ~6 м² меньше заявленной; банк пересчитал ипотечный лимит / потребовал доп. взнос; за сутки разницу не собрали — ДКП не подписали, аванс не переводили.
- Modeled casus (не репортаж): без имён ЖК, банка, адреса.
- P0 Wordstat: «купить квартиру в тюмени вторичка» — 3453 (регионы 55+11176 MCP 2026-10-05); compare 6315 (225).
- Supporting: «проверка квартиры перед покупкой» — 1765 (55+11176+225).
- comment_magnet: объявление 54 м² vs БТИ 48 м² — доплачивать или снимать объект?
- SERP signal URLs: dzen.ru/a/ar5p5M4BhR87M3aD (вторичка, пересчёт ипотеки Тюмень — fetch blocked), sudzakon.ru, smway.ru 07.07.2026

## Fresh external signals (accessed 2026-10-05)

1. **72.ru 05.10.2026** https://72.ru/text/realty/2026/10/05/76670221/ — сегодня: тюменцы уходят с котлованов, конкуренция вторички с новостройками; рыночная ипотека «заморозила» спрос; контекст слота вторичка.
2. **72.ru 09.09.2026** https://72.ru/text/realty/2026/09/09/76632224/ — 65,6% покупателей выбрали вторичку (август); средняя цена ~5,1 млн; доля ипотеки на вторичке 32%; рыночная ипотека 17–18%.
3. **Trend Radar 2026-10-05** Life Dzen «С 1 октября вырастет спрос на вторичную недвижимость» https://dzen.ru/a/aqcTwkjUgT5jdBjX — механика almost lost перед деньгами.
4. **smway.ru 07.07.2026** https://smway.ru/prichiny-oshibok-v-ploschadi-zdaniya-bti-egrn-i-kak-ispravit/ — БТИ (инстр. №37) суммирует комнаты; ЕГРН (приказ Росреестра) — по внутренним поверхностям наружных стен; обычно ЕГРН ≥ БТИ; расхождения в метры — ошибка/перепланировка/устаревший план; банк и Росреестр стопорят сделки при несовпадении данных.
5. **sudzakon.ru** https://sudzakon.ru/nesovpadenie-ploshhadi-v-egrn-i-otkaz-banka-v-ipoteke-ispravlyaem-kadastrovye-svedeniya/ — банк смотрит на ЕГРН как залог; несовпадение площади → риск, приостановка; исправление через Росреестр/техплан (недели, не «за сутки до нотариуса»).

## Legal / official frames (no bank tariff digits)

- **218-ФЗ** «О государственной регистрации недвижимости» — consultant https://www.consultant.ru/document/cons_doc_LAW_182661/ — единый реестр, характеристики объекта включая площадь.
- **Письмо Росреестра 28.04.2026 № 13-00310/26** (ред. 18.08.2026) — разъяснение по общей площади квартиры, проектная документация (ppt.ru агрегатор).
- **ГК РФ** договор купли-продажи: предмет — квартира с указанием площади; расхождение существенных характеристик — основание для претензий (обзоры, не подменять консультацию юриста).

## Tyumen secondary + mortgage context (media, not bank tariffs)

- Средняя сумма ипотеки на вторичке в Тюмени ~3 млн (72.ru июль 2026).
- При пересчёте кредита банк привязывает сумму к **цене сделки и оценке залога** (целевой кредит ≤ стоимости объекта; обзоры credistory/infullbroker — не единственный источник цифр банка).

## Practical mechanics for Writer (facts, not lead)

- На вторичке покупатель часто видит площадь из **объявления / старого плана / выписки ЕГРН**; **свежий техпаспорт/обмер БТИ** заказывают перед сделкой или по требованию банка/нотариуса.
- Если новый обмер **уменьшает** учтённую площадь (незаконная перепланировка, ошибка старого плана, иная методика «общая» vs «жилая», лоджия/балкон), банк может: снизить одобренную сумму под новую оценку, потребовать **увеличить первоначальный взнос**, пересмотреть заявку.
- Исправление ЕГРН до ДКП обычно **дольше суток** (кадастровый инженер, техплан, Росреестр до 3 мес. приостановки по обзорам).
- Альтернативы до аванса: торг с продавцом под новую площадь/цену; отказ без аванса; проверка **до** брони даты у нотариуса.
- Overlap: B09 — обременение ЕГРН; B06 — оценка банка; B11 — перепланировка/Росреестр; не повторять их каркас — фокус БТИ-площадь × ипотека **до ДКП**.

## Constraints for research output

- research_date: 2026-10-05
- No h2_outline, lead, FAQ skeleton
- No invented news about specific Tyumen family
- No bank %/LTV without official_verifications row
- official_verifications: 218-ФЗ + methodology sources; bank tariffs: not claimed
- writer_safe_urls: https://t.me/Tyumen_Rieltor https://max.ru/id561413315447_biz https://dzen.ru/holyslav

## Required output structure

Same sections as B33 research-notes: research_date, topic_id, cluster_id, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, voice_angle, surprising_fact, official_verifications table, source_table, writer_safe_urls
