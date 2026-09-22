# Assembled research inputs — B33 (2026-09-22)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Do **NOT** output `DEROUTER RESEARCH BLOCKER` or refuse synthesis. Output the full `research-notes.md` body only per SKILL.md from the facts below.

## Meta

- research_date: 2026-09-22 (Europe/Moscow)
- topic_id: B33
- article_dir: memory/blog/articles/B33-za-5-dnej-do-ddu-v-deklaracii-sdvinuli-sdachu-na-dva-kvartala-bank-urezal-ipotek
- cluster_id: newbuild_declaration_completion_slip_before_ddu_tyumen
- market: Тюмень, новостройка, ДДУ, эскроу, ипотека
- casus: **composite editorial** — не называть конкретный ЖК, застройщика, банк, фамилии; механика из Scout handoff

## Scout mechanism (composite)

- Семья с одобренной ипотекой готовится подписать ДДУ на квартиру в строящемся ЖК Тюмени.
- За **5 дней** до подписания на dom.rf / ЕИСЖС появляется **новая редакция** проектной декларации.
- Срок передачи объекта в разделе 17.2 сдвигается с **II кв. 2027** на **IV кв. 2027** (два квартала ≈ полгода).
- В соглашении о бронировании и черновике ДДУ остаётся старый квартал.
- Банк после сверки объекта **уменьшает одобренную сумму** и/или требует новый пакет (ПВ, доход, страховка).
- Семья **останавливает сделку до перевода на эскроу**.
- Бронь ориентировочно **150–200 тыс. ₽** — риск удержания по условиям брони (не универсальная цифра).

## Overlap (published-titles-only.md only)

- Близкие сюжеты: B27 (земля в декларации за 4 дня до ДДУ), B28 (газ/КП vs декларация), B12 (сдвиг сдачи после эскроу), B22 (ставка перед ДДУ), B29/B31/B32 (банк перед ДДУ/эскроу).
- Отличие B33: именно **сдвиг п. 17.2 (срок передачи)** в свежей декларации vs бронь/черновик ДДУ → пересчёт ипотеки **до эскроу**.

## Wordstat (MCP-KV 2026-09-22)

- Live API: **499 flake** на повторных вызовах research-агента.
- Scout snapshot (PASS): «купить новостройку в тюмени» **902** (регионы 55+11176); compare RU 225 **1914**; spine «новостройки тюмень» **8234**.
- Узкие «срок сдачи новостройка тюмень» — empty/flake; demand anchor = buyer spine выше.
- Mark WORDSTAT PARTIAL in report, not blocker.

## Fresh signals (week of 2026-09-22)

### Official EISZhS PDFs — Tyumen, сентябрь 2026 (live fetch)

Публичные декларации с датами редакции **07–14.09.2026** (подтверждают, что в Тюмени декларации обновляются в сентябре; не объект casus):

| № декларации | дата PDF | URL |
|--------------|----------|-----|
| 72-001380 | 07.09.2026 | https://ij.cdnstroy.ru/jud91osulwkna_1daae7b.pdf |
| 72-001382 | 09.09.2026 | https://ik.cdnstroy.ru/km72mqtcdx34a_1vc1cf3.pdf |
| 72-001397 | 09.09.2026 | https://i8.cdnstroy.ru/883stiew7tiqa_ajddlh.pdf |
| 72-001308 | 14.09.2026 | https://ii.cdnstroy.ru/izk1k3vc9v0yu_i8bvcy.pdf |

Форма: раздел **17.2** — первоначальная и планируемая дата передачи объекта (пример в 72-001397: планируемая дата **03.12.2028**; в 72-001308 по корпусам встречается **30.06.2027**). Покупатель сверяет **17.2.1 / 17.2.2** с проектом ДДУ.

### Community — Telegram tenant (live 2026-09-22)

https://t.me/s/Tyumen_Rieltor — свежие посты о новостройках Тюмени: промо с **сдачей I кв. 2027** (ЖК «Отличие»), пост о рисках застройщиков («Самолёт», проверять проект целиком), призыв сравнивать акции. Не юридический источник по casus, но **локальный сигнал недели**.

### Domclick (Sber ecosystem, official explainer for individuals)

https://blog.domclick.ru/ipoteka/post/vam-odobrili-ipoteku-sber-banka-chto-dalshe — после одобрения **до 90 дней** на выбор объекта; нужно **одобрение недвижимости в банке** (~3–5 рабочих дней); условия в ЛК Домклик.

## Legal / regulatory facts (consultant.ru + pravo.gov.ru)

1. **Ст. 19 214-ФЗ** — проектная декларация в ЕИСЖС; изменения о застройщике и проекте — **ежемесячно, не позднее 10-го числа** месяца, следующего за отчётным (ч. 4). После ввода всех объектов по проекту изменения не требуются.
2. После договора с **первым** дольщиком в декларацию нельзя менять всё подряд — исключения включают **сроки строительства/передачи** (консультант подборка / ч. 1 ст. 19).
3. **Ст. 6 ч. 3 214-ФЗ** — если стройка не завершится в срок по **уже заключённому** ДДУ: застройщик **не позднее чем за 2 месяца** до истечения срока направляет информацию и предложение изменить договор. Уведомление **само** срок не меняет; нужно допсоглашение (контекст RG 05.02.2026, logos-pravo).
4. **ПП РФ № 2226 от 30.12.2025** (pravo.gov.ru 0001202512310020) — особенности передачи в **2026**: индивидуальный перенос срока **после получения РВЭ**, **без** изменения декларации. **Не путать** с сюжетом B33 (покупатель **ещё не** подписал ДДУ; сдвиг виден в **новой декларации** до сделки).
5. ДДУ должен соответствовать сведениям проектной декларации (ст. 4 214-ФЗ — проверять через consultant).
6. Деньги дольщиков на **эскроу** — после регистрации ДДУ (проектное финансирование / 214-ФЗ); до эскроу риск в основном **бронь** и время одобрения банка.

## Bank / mortgage (no invented tariff %)

- Банк оценивает объект, срок строительства, застройщика, лимиты программы (семейная/базовая). Увеличение срока до сдачи может ухудшить параметры одобрения (сумма, ПВ, срок кредита) — **только как механизм**, без выдуманных процентов урезания.
- Официально для физлиц (Сбер/Домклик): **90 дней** на подбор объекта после одобрения заявки; отдельное одобрение квартиры/ДДУ.
- Точную сумму после пересчёта Writer берёт только из **письменного решения банка**, не из обзоров.

## SERP (research-serp.json 2026-09-22)

- Много статей про **неустойку 2026** после отмены моратория — полезен фон, но не ядро casus (покупатель ещё без ДДУ).
- Domclick: задержка сдачи, перенос сроков по ДДУ (401 при fetch — использовать SERP title only).

## Constraints for Writer

- Composite casus — no composite disclaimer meta в теле (канон quality-bar).
- Не утверждать, что сдвиг в декларации автоматически даёт неустойку до подписания ДДУ.
- Не путать ПП 2226 (после РВЭ) с проверкой декларации **до** первого ДДУ.
- Не называть точный % урезания ипотеки без official_verifications.
- Бронь 150–200 тыс. — editorial casus range; возврат по тексту соглашения о бронировании.
- Newbuild only — без вторички/ЕГРН продавца.

## voice_angle / surprising_fact hints

- voice: «квартал в рекламе» vs «дата в п. 17.2 свежей декларации».
- surprise: декларацию **законно** обновляют каждый месяц до 10-го числа — покупатель до ДДУ может увидеть новый квартал внезапно, хотя в брони ещё старый.

## writer_safe_urls (tenant CTA)

- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- tel:+79220016505
- https://dzen.ru/holyslav
- https://www.domrf.ru/
- https://www.consultant.ru/document/cons_doc_LAW_51038/
- https://blog.domclick.ru/ipoteka/post/vam-odobrili-ipoteku-sber-banka-chto-dalshe
- http://publication.pravo.gov.ru/document/0001202512310020

## Output instructions for Derouter research role

Produce `research-notes.md` in Russian with sections:
research_date, topic_id, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, local_context, voice_angle, surprising_fact, official_verifications (table), source_table (accessed_at 2026-09-22 each), writer_safe_urls.

NO h2_outline, lead, FAQ, action_outline.

official_source_audit: required for legal norms + Domclick 90-day claim; no bank tariff digits without verification.
