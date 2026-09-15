# Assembled research inputs — B27

## research_date
2026-09-15

## topic_id / title
B27: В Тюмени банк снял ЖК с аккредитации — ипотека замерла за сутки до ДДУ

## scout handoff (excalibur-blog-handoff.md)
- top_energy_mirror: stopped_before_money
- newbuild_mechanism: банк снял застройщика/ЖК с списка аккредитации накануне подписания ДДУ — одобренная ипотека замерла, семья не дошла до эскроу
- why_newbuild_not_secondary: ДДУ/ипотека от застройщика; риск в аккредитации банком, не в ЕГРН вторички
- comment_magnet_angle: «Вы бы успели переехать в другой банк за сутки или сняли бы бронь?»
- cluster_id: bank_accreditation_revoked_before_ddu
- P0 Wordstat: «купить новостройку в тюмени» — 909 (Tyumen 55+11176)

## overlap (published-titles-only.md)
Нет публикаций про снятие аккредитации. Близкие соседи: B19 (эскроу/маткапитал), B20 (смена юрлица), B22 (ставка перед ДДУ), B26 (РВЭ/транш).

## wordstat (2026-09-15, regions 55+11176)
- «купить новостройку в тюмени» — 909
- «новостройки в тюмени от застройщика» — 668 (related 875)
- «квартиры в тюмени новостройка ипотека» — 100
- «тюмень застройщик новостройка ипотека» — 96
- «новостройки тюмень купить в ипотеку» — 87
- «ипотека новостройка тюмень» — 189 total cluster
- «аккредитация новостройка ипотека» — Wordstat PARTIAL (пустой ответ API)

## fresh signals this week (required)
1. **72.ru** 14.09.2026 — в Тюмени «Навигатор. Девелопмент» снова открыл беспроцентную рассрочку до 15 мес. в ЖК «Зеленые аллеи» (ГП-9); первый взнос от 20%; ключи планируют в 2027. Контекст: покупатели ищут альтернативы ипотеке, сроки сделки критичны.
2. **tyumen.1000bankov.ru** — витрина ипотеки на новостройки обновлена 14.09.2026; ПСК по банкам (агрегатор, не официальный тариф): Совкомбанк 16,956–24,849%; ДОМ.РФ 16,3–26,06%; Уралсиб 23,59–29,95%; Сбер 25,9–31,88%.
3. **tumentoday.ru** 02.09.2026 — Уралсиб в топ-10 по ипотеке; за 7 мес. 2026 выдал 9 млрд ₽ на первичку; ипотека — востребованный продукт.

## mechanism facts (accreditation + mortgage + DDU)

### What is bank accreditation (sources: morein.pro 17.03.2026, boombob.ru 23.05.2026, darstroy-yug.ru updated 22.06.2026)
- Коммерческое решение конкретного банка: готов ли выдавать ипотеку на конкретный ЖК/корпус/очередь (не на весь бренд застройщика).
- Банк проверяет финансы застройщика, документы (земля, разрешение, проектная декларация, 214-ФЗ), стадию строительства, репутацию.
- Аккредитация ≠ гослицензия; не гарантирует сдачу в срок и качество отделки.
- Пересматривается периодически (ориентир 6–12 мес., boombob/morein); может быть отозвана в любой момент.
- Причины отзыва: замедление стройки, изменение документов, ухудшение финансов застройщика, судебные риски, негативная информация (darstroy, boombob, morein).

### Accreditation vs escrow (darstroy-yug.ru, CBR reform context)
- Эскроу (214-ФЗ): деньги дольщика на счёте до условий раскрытия — защита средств.
- Аккредитация: готов ли банк кредитовать покупателей этого объекта.
- Механизмы разные; эскроу не заменяет проверку аккредитации перед сделкой.

### Pre-approval vs object check (novostroikino.ru 29.07.2026)
- На первичке банк оценивает и заёмщика, и объект.
- Ситуация «одобрили заёмщика, отказали на сделке» регулярна — почти всегда объект: не аккредитован, стадия готовности, оценка ниже цены ДДУ.
- Решение: уточнить причину по объекту; другой банк, аккредитовавший корпус; или другая квартира.

### Revocation before DDU (boombob.ru 23.05.2026)
- Проверять аккредитацию непосредственно перед сделкой.
- Бывают случаи отмены аккредитации за неделю до подписания ДДУ.
- Если подписать ДДУ на неаккредитованный объект — банк может отказать в кредите; придётся гасить обязательства перед застройщиком из своих средств для расторжения.
- До ДДУ/регистрации — не вносить крупные невозвратные суммы.

### After revocation / already issued mortgage (morein, boombob, vladis, banki.ru Q&A)
- Уже заключённые ДДУ и выданная ипотека обычно остаются в силе; банк не поднимает ставку из-за потери аккредитации застройщика.
- Новые покупатели в этом банке на этот объект — не получат ипотеку.
- Потеря аккредитации — сигнал проверить причину у банка и застройщика, проектную декларацию, ход стройки.

### Lgot programs (nedvizhimosticeny.ru, market; verify via DOM.RF for Writer)
- Семейная, IT, военная — только аккредитованные ЖК конкретным банком + ДДУ через эскроу.
- Апартаменты и переуступка под льготные ставки обычно не подходят.

### Parallel SERP casus energy (dzen snippets, NOT verified facts for B27)
- SERP mentions casus «банк снял одобрение за 72 часа до ДДУ — бронь сгорела, квартиру купил другой» on tenant Dzen. Treat as editorial energy mirror only, NOT documentary source.

## model editorial case (NOT public reportage)
- Tyumen family, newbuild purchase, children in household.
- Booking paid; mortgage pre-approved for borrower in Bank A.
- Accreditation for specific corpus was true at booking; not re-checked day before DDU.
- ~24 hours before scheduled DDU signing: bank notifies object removed from accreditation list for NEW deals; pre-approval cannot proceed on this JK in Bank A.
- Family cannot open escrow path with that bank on schedule; booking timer running.
- Apartment returned to market; another buyer later (SERP narrative — use only as dramatic parallel, no names).
- Money did NOT reach escrow — stopped_before_money.
- NO real bank name, JK name, address, sums in Writer output unless added later from verified source.

## practical checks (from sources)
- Confirm accreditation of exact corpus/queue in chosen bank on day of deal (phone + written).
- Ask bank: reason for revocation, does it affect YOUR pending approval, expiry of pre-approval.
- Check domclick/VTB/Sber accredited lists for same corpus in other banks.
- Read booking contract: refund if mortgage fails due to object, extension possible.
- Check наш.дом.рф: project declaration, builder, construction stage.
- Do not sign DDU until mortgage object confirmed and credit agreement terms fixed.
- If accreditation lost for systemic reasons (builder finances) — switching bank may not help.

## official / macro (verified fetch 2026-09-15)
- CBR key rate 14.00% from 27.07.2026; next board meeting scheduled 11.09.2026 (press release 24.07.2026).
- Family mortgage program params: use DOM.RF instruction URL (punycode) as in B22 if needed — ставка до 6%, взнос от 20%, лимит 6 млн вне МСК/СПб, one per family from 01.02.2026.

## constraints for Writer
- No composite disclaimer in article body.
- No invented bank/JK names.
- Distinguish: accreditation revocation (object) vs rate change (B22) vs escrow/matkapital (B19) vs legal entity change (B20).
- Bank vitrine rates from 1000bankov — aggregator only, not official bank tariffs.
- Casus is modeled Tyumen scenario aligned with scout cluster, not court-documented case.

## writer_safe_urls / CTA
- https://cbr.ru/press/pr/?file=24072026_133000key.htm
- https://72.ru/text/realty/2026/09/14/76634868/
- https://tumentoday.ru/2026/09/02/bank_uralsib__v_top10_reytinga_po_obyemam_ipotechnogo_kreditovaniya_/
- https://morein.pro/blog/akkreditaciya-obekta
- https://boombob.ru/akkreditacia-zastrojsika-v-banke-cto-eto-znacit-dla-pokupatela-novostrojki
- https://novostroikino.ru/blog/otkaz-v-ipoteke-na-novostroyku-prichiny-i-chto-delat-2026/
- https://darstroy-yug.ru/articles/novostroyka-akkreditovana-chto-eto-znachit-dlya-pokupatelya-kvartiry/
- https://tyumen.1000bankov.ru/kredit/ipotek/na-novostrojku/
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- https://dzen.ru/holyslav

## output instructions for Derouter research role
Write research-notes.md in Russian with sections:
research_date, topic, reader_problem, reader_outcome, case_status, practical_facts, constraints, practical_checks_before_signing (or similar), local_context, wordstat, voice_angle, surprising_fact, official_verifications (table), source_table (with accessed_at 2026-09-15), writer_safe_urls.
NO h2_outline, NO lead, NO FAQ skeleton.
Mark modeled case clearly in case_status.
