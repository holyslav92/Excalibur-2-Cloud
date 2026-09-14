# Description inputs — B27 — 2026-09-14

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Ребёнку исполнилось 7 лет накануне эскроу — семейная ипотека сорвалась

**subject:** Семейная ипотека на новостройку: ребёнку исполнилось 7 лет до заключения кредитного договора.

**angle:** День рождения между одобрением и кредитным договором разрушил расчёт семьи на льготную ипотеку. Заголовок связывает временной порог с исходом сделки, не создавая ложного впечатления, что маткапитал пропадает после семилетия ребёнка.

**comment_magnet_angle:** Кто должен следить за возрастным порогом между одобрением и кредитным договором — семья или банк, который уже одобрил ипотеку?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Ребёнку исполнилось 7 лет за девять дней до сделки — и семейная ипотека под 6% превратилась для семьи в платёж на 18 тысяч рублей больше. Двушка в тюменской новостройке уже была забронирована, рядом с календарём на кухне лежали расчёты собственных денег и маткапитала, а банк прислал предварительное одобрение. Родители считали, что осталось только подписать документы и открыть эскроу. Но день рождения оказался между банковским «одобрено» и кредитным договором — и именно эта дата решила судьбу льготной ставки.

**Para 2:** (early CTA block — not lead prose)

## Case hook (from research / article)
- Тюмень, новостройка, семейная ипотека 6%, маткапитал в первоначальном взносе
- Предварительное одобрение есть, двушка забронирована, заявление на маткапитал подано через банк
- Ребёнку исполнилось 7 лет за 9 дней до планируемого кредитного договора / эскроу
- Возраст смотрят на дату кредитного договора, не на одобрение и не на бронь
- На финальной сверке банк: семейная ипотека срывается — ребёнку уже 7
- Маткапитал НЕ «завис» из-за возраста 7 лет; сорвалась льготная схема, не сертификат
- Платёж вырос на 18 тыс. ₽/мес; застройщик дал 5 дней на смену программы
- Через 3 дня бронь сняли, эскроу не открыли, деньги на него не ушли
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «семейная ипотека новостройка» 126; «новостройки тюмени семейная ипотека» 40
- buyer risk: возраст ребёнка, кредитный договор vs одобрение, маткапитал, эскроу, бронь

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, СФР
7. Do NOT imply matkapital disappears at age 7 — the family mortgage scheme failed, not the certificate

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

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
