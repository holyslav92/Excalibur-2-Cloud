# Description inputs — B27 — 2026-09-15

## IMPORTANT — you are Derouter gpt-6-astra (powerful tier)
You ARE the description writer invoked via excalibur_blog_derouter_opus_chat.py. Write the teaser JSON now. Do NOT return BLOCKER. Return valid description-brief.json with a non-empty description field.

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ

**subject:** Новостройка в Тюмени и ипотека, замершая после снятия ЖК с аккредитации

**angle:** Банк заблокировал объект, хотя ипотека покупателя уже была предварительно одобрена: за сутки до ДДУ семья не дошла до эскроу и вынуждена выбирать между другим банком, продлением брони и сменой квартиры.

**comment_magnet_angle:** Вы бы успели перейти в другой банк за сутки или сняли бы бронь?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени банк снял корпус новостройки с аккредитации примерно за сутки до подписания ДДУ — ипотечная сделка семьи с детьми остановилась. Квартиру уже забронировали и оплатили бронь, а по заёмщикам было предварительное одобрение. На кухне лежал договор бронирования, в телефоне — переписка с застройщиком, и срок удержания квартиры подходил к концу. Казалось, осталось подписать документы, но прежнее решение банка ещё не означало, что он выдаст деньги именно на эту квартиру. Теперь нужно было разобраться с кредитом, пока квартира не вернулась в продажу.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. В Telegram разбираю, что проверять за обещанием «всё одобрено». Материалы и связь — также в MAX.

## Case hook (from research / article)
- Тюмень, новостройка, семья с детьми, предварительное одобрение ипотеки
- «Ипотеку одобрили — значит, сделка есть» — ложный щелчок
- Предодобрение заёмщика ≠ аккредитация корпуса; банк может снять объект с аккредитации в любой момент
- За ~24 часа до ДДУ: банк закрыл новые сделки по корпусу, бронь тикает, эскроу не открыт
- Одобрение на человека осталось, но объект из списка исчез — «эскроу в проекте» не заменяет кредит
- Семья остановилась до подписи ДДУ: деньги застройщику не ушли, выбор — другой банк, продление брони, смена квартиры
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить новостройку в тюмени» 909; «ипотека новостройка тюмень» 189
- buyer risk: аккредитация, предодобрение, бронь, ДДУ, эскроу, снятие с аккредитации

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, банк, аккредитация

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Одобрение было в телефоне, но ставку это не закрепило. Перед ДДУ тюменская семья увидела новый платёж и выбирала: подписывать или оставить бронь банку вместе с деньгами.»

## Required JSON output
```json
{
  "topic_id": "B27",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
