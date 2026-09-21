# Description inputs — B33 — 2026-09-21

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## Preconditions (satisfied)
- article.html: final after Sol (pipeline_canon human-first-v2 in article.meta.json)
- title-brief.json: present
- research-notes.md: present

## topic_id
B33

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени УК потребовала 180 тысяч за 3 дня до ключей — в ДДУ их нет

**subject:** Счёт УК на 180 тысяч рублей перед выдачей ключей от новостройки Тюмени, не предусмотренный ДДУ

**angle:** Конфликт суммы в счёте и отсутствия платежа в ДДУ, усиленный сроком до ключей. Семья требует письменное основание вместо оплаты; приёмка и последний ипотечный транш зависают.

**comment_magnet_angle:** Заплатить 180 тысяч, которых нет в ДДУ, ради своевременного получения ключей — или требовать письменное основание, рискуя задержкой приёмки и ипотечного транша?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За три дня до ключей семья в Тюмени получила от УК счёт на 180 000 ₽: в ДДУ такой суммы нет, а без оплаты покупателей обещали не допустить к подписанию акта. Дома двое детей, коробки собраны, приёмка согласована — осталось осмотреть квартиру и получить ключи. Но в личном кабинете появились расходы на «ввод дома в эксплуатацию», «подключение к сетям» и «формирование управляющей компании». Застройщик в ответ сослался на «типовой договор с УК». Для семьи вопрос оказался не только в незапланированных деньгах: без передаточного акта мог задержаться последний ипотечный транш.

**Para 2 (early CTA):** Я — Святослав Шакин, The Риэлтор, Тюмень. В Telegram и MAX разбираю документы по недвижимости простым языком: где обязательство покупателя, а где пока только чужое «так положено».

## Case hook (from research / article)
- Тюмень, новостройка, семья с детьми, за 3 дня до ключей
- Счёт УК ~180k: «ввод», сети, «формирование УК» — в ДДУ и приложениях такой строки нет
- УК связывает оплату с актом; застройщик — «типовой договор»
- Риск: задержка передаточного акта и последнего ипотечного транша
- Композитный кейс, без названий ЖК/УК/банка
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 4395 (регион 55+11176)
- buyer risk: ДДУ vs договор управления, счёт перед ключами, акт приёма-передачи

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, УК

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B33",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
