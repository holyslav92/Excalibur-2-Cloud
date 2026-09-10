# Assembled research inputs — B24

research_date: 2026-09-10
topic_id: B24
title: В Тюмени бронь на новостройку сгорела за сутки — застройщик поднял цену на 450 тысяч
cluster_id: booking_expired_price_hike_tyumen
market_focus: newbuild_only (Tyumen)

## Scout handoff (preserve casus)

- event: семья в Тюмени выбрала квартиру в новостройке, внесла 50 000 ₽ за бронь, получила фиксацию цены и планировки на 48 часов
- risk: за сутки до дедлайна застройщик поднял стоимость на 450 000 ₽; без доплаты бронь прекращается
- time: последние 24 часа брони, накануне подписания ДДУ и открытия эскроу
- finale: семья не успела доплатить; бронь сняли; квартиру забронировали другие; 50 000 ₽ удержали по оферте; ДДУ не подписан
- comment_magnet: «Бронь на двое суток и внезапные +450 тысяч: вы бы доплатили, чтобы не потерять планировку, или искали бы другой ЖК — даже если ипотека уже одобрена?»
- DDU and escrow NOT yet opened/signed in plot
- NOT secondary housing plot

## Wordstat (MCP-KV live, regions 55+11176 unless noted)

| phrase | volume 55+11176 | note |
|--------|-----------------|------|
| купить новостройку в тюмени | 885 | scout P0 |
| новостройки тюмень | 4642 | supporting |
| бронь новостройки | 3 | weak direct demand |
| бронь новостройки (RU 225) | 288 | compare |

Top related (купить новостройку в тюмени): от застройщика 461; ипотека 93-94; студии 60-92.

## Fresh signals this week (required)

1. **72.ru, 08.09.2026** — «Квартиры со скидкой до 400 тысяч рублей: в Тюмени заканчивают строительство нового дома» (ЖК «Концепт», Тюменская слобода). Скидка до 400 тыс. ₽ на отдельные лоты (пример: 5,0 млн вместо 5,4 млн). Контекст: застройщики активно меняют прайс/акции; «ограниченное количество квартир в акции». URL: https://72.ru/text/realty/2026/09/08/76619954/

2. **Infox.ru, 24.08.2026** — Тюмень 3-е место по доле сделок со скидками (58,4% в июле 2026, Объектив.РФ); средняя скидка 8,9%; разброс 489 тыс.–2,2 млн ₽. Рынок покупателя; коррекция цен как инструмент продаж. URL: https://www.infox.ru/news/299/385287-tumen-vosla-v-cislo-liderov-po-prodazam-novostroek-so-skidkami

3. **Tenant channel signal** — dzen.ru/holyslav (scout); TG https://t.me/Tyumen_Rieltor (tenant CTA). TG fetch blocked 409 from cloud; channel listed in tenant-config.

## Booking mechanics — market / legal (live sources)

### Novostroikino, 06.08.2026
- Бронь = платный/бесплатный депозит 3–30 дней; фиксирует цену и снимает лот
- Бесплатная: 1–3 дня; платная: от нескольких тыс. до 1–2% цены квартиры
- Ключевой юридический вопрос: аванс в счёт ДДУ (ст. 32 ЗоЗПП, возврат за вычетом расходов) vs оплата услуги «бронирование» (услуга считается оказанной в момент подписания — невозврат)
- Пример формулировок: 50 000 ₽ как аванс vs как услуга бронирования на 14 дней
- Обязательные пункты договора: точный объект, фиксированная цена отдельным пунктом, срок с датой окончания, что происходит по истечении срока
- Бронь ≠ ДДУ; деньги за бронь не эскроу
- URL: https://novostroikino.ru/blog/bronirovanie-kvartiry-v-novostroyke-2026/

### Cian explainer
- Фиксированная цена — важнейший пункт; без чёткой обязанности сохранить цену застройщик может поднять к моменту основного договора
- Повышение после брони с прописанной фиксацией — основание для расторжения и возврата
- URL: https://www.cian.ru/stati-dogovor-bronirovanija-pri-pokupke-kvartiry-chto-eto-zachem-nuzhen-i-stoit-li-zakljuchat-340793/

### Yandex Realty journal
- Сроки брони: несколько дней — 2 недели
- Штрафные санкции часто = невозврат обеспечительного платежа при отказе покупателя
- URL: https://realty.yandex.ru/journal/post/bronirovanie-kvartiry-vnovostroyke-chtonuzhno-znat/

## Official developer booking offers (verified samples)

### Brusnika Tyumen — official site offer
- URL: https://tyumen.brusnika.ru/agreement_pantry/
- Срок бронирования: **3 календарных дня**
- Сумма резервирования: **5 000 ₽** (предавторизация; перечисление после регистрации ДДУ)
- п. 3.1.3: обязательство заключить договор **по цене, действовавшей на момент заключения соглашения**
- Если покупатель не обратился за 3 дня — обязательства прекращаются, сумма возвращается
- Акцептант/оферент вправе отказаться односторонне — возврат за 5 дней

### AAG / «А Эстейт» public offer PDF (ред. 15.02.2024)
- URL: https://media.aag.company/aag.company/docs/publicoffer.pdf
- Плата за бронь квартиры: **50 000 ₽** (совпадает с суммой в scout casus как рыночная вилка)
- Срок бронирования: **10 рабочих дней**
- п. 2.2: на весь срок фиксируется стоимость объекта
- Услуга считается оказанной при бездействии акцептанта после истечения срока (кроме п. 4.2 — отказ 3+ банков по ипотеке → возврат)
- Договор НЕ является предварительным договором купли-продажи

### MIG-Estate / kvartaly-otrada — оферта 12.02.2026 (PDF)
- URL: https://kvartaly-otrada.ru/uploads/main/02a/4ba51343775e1ccd949f6b8002763ccd83096057d4dd769c8181da3f5819f70b/oferta_12.02.2026.pdf
- Цена услуги бронирования: **40 000 ₽**
- Срок: 7 дней (100%/рассрочка) или 10 дней (ипотека); может сокращаться при акционной скидке
- **Лазейка цены**: «стоимость объекта может быть изменена (увеличена) при изменении способа оплаты, рассрочки, субсидированной ипотеки, отмене скидок»
- п. 5.5: при отказе покупателя от забронированного объекта — **цена услуг не возвращается**, услуга считается оказанной
- Услуга = договор оказания услуг, не ДДУ

### Rodina Park offer (sample)
- Срок основного бронирования: 7 календарных дней
- Плата за бронь квартиры: от 20 000 ₽; машино-место 50 000 ₽
- URL: https://rodinapark.ru/dogovor-oferta

## 214-FZ legal context (consultant, red. 09.04.2026)
- URL: https://www.consultant.ru/document/cons_doc_LAW_64629/
- Регулирует привлечение денежных средств по **договору участия в долевом строительстве**
- Привлечение денег граждан для строительства — через ДДУ + эскроу (ст. 1 ч. 2, ст. 3)
- Договор бронирования **не является** ДДУ и не даёт статуса участника долевого строительства
- Платёж за бронь — отдельная сделка (услуга/аванс), не защищён механизмом эскроу 214-ФЗ
- Scout signal URL LAW_51057 on consultant redirects to ЖК РФ — use LAW_64629 for 214-ФЗ

## ZоЗПП ст. 16 (consultant)
- URL: https://www.consultant.ru/document/cons_doc_LAW_305/9eb0f127ead4dc57e7d0a9d4954cf264c4b3cea8/
- Запрет навязывания доп. платных услуг как условия основной сделки
- При навязанной обязательной брони — право требовать возврат

## Tyumen market context (price volatility)

- 72.ru 04.06.2026: рынок Тюмени → «рынок покупателя»; дисконт по отдельным лотам 15–20%; застройщики широкий арсенал акций
- Infox: 58,4% сделок со скидкой (июль 2026); средняя скидка 8,9%
- RBC Tyumen (апрель 2026): предложение выросло; готовое жильё иногда дешевле строящегося на 8,2%
- Контекст для casus: прайс-лист и «акционная цена» могут меняться; бронь на 48 ч — короткое окно на фоне волатильности

## Case status for Writer

- Сюжет **собирательный редакционный casus**, не подтверждённый публичный репортаж с фамилиями/ЖК
- Суммы 50 000 ₽ бронь и +450 000 ₽ — параметры scout-сценария; 50 000 ₽ подтверждается как типичная вилка оферт (AAG 50k; MIG 40k; Brusnika 5k резерв)
- 48 часов — короткий срок внутри рыночной вилки (1–3 дня бесплатно, 3–14 дней платно; Brusnika 3 дня)
- Нельзя выдавать за документально подтверждённый кейс конкретного ЖК

## Overlap check

published-titles-only.md: no duplicate «бронь + рост цены застройщик»; cluster booking_expired_price_hike_tyumen unique; B22 = bank rate hike before DDU (different mechanism)

## writer_safe_urls

- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_64629/
- https://tyumen.brusnika.ru/agreement_pantry/
- https://novostroikino.ru/blog/bronirovanie-kvartiry-v-novostroyke-2026/
- https://72.ru/text/realty/2026/09/08/76619954/
- https://www.infox.ru/news/299/385287-tumen-vosla-v-cislo-liderov-po-prodazam-novostroek-so-skidkami
- https://www.domrf.ru/

## Constraints for Writer

- Do NOT present as confirmed news report with names/ЖК/bank
- Distinguish booking agreement vs DDU vs escrow
- 450k price hike — plot parameter unless tied to «оферта разрешает пересмотр при смене способа оплаты/отмене скидки»
- Retention of 50k depends on contract wording (service fee vs advance)
- No secondary housing angles
- No h2 outline / lead / FAQ skeleton in notes output
