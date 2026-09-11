# Description inputs — B24 — 2026-09-11

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени рассрочку у застройщика просрочили на 4 дня — квартира ушла

**subject:** Рассрочка у застройщика при покупке квартиры в тюменской новостройке

**angle:** Четыре дня просрочки превратили «покупку без банка» в расторжение договора: семье вернули лишь часть первого взноса, а квартиру продали другому.

**comment_magnet_angle:** Рассрочка от застройщика — удобная замена ипотеке или риск, при котором несколько дней задержки могут стоить квартиры и сотен тысяч рублей?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени семья задержала платёж за новостройку на четыре дня — и получила письмо о расторжении, пока квартира уже возвращалась на рынок. Первый взнос в 400 тысяч рублей был внесён, следующий перевод привязали к зарплате, но деньги пришли позже установленной даты. Оплату отправили, однако это не остановило расторжение: квартиру начали показывать другим покупателям. Здесь решает не вывеска «рассрочка без банка», а документ, по которому семья перечисляла деньги и получила ли она уже оформленное право требовать квартиру.

**Para 2 (early CTA):** Разбираю условия покупки новостроек Тюмени в Telegram и MAX: что подписывают, куда уходят деньги и где покупатель остаётся без привычной защиты.

## Case hook (from research / article)
- Тюмень, новостройка, рассрочка «без банка» у застройщика
- Первый взнос 400 тыс. ₽, следующий платёж задержали на 4 дня (ждали зарплату)
- Письмо о расторжении; квартиру снова выставили на продажу
- Вернули 180 тыс. ₽ из 400, удержали 220 тыс.
- Ключевой вопрос: ДДУ с эскроу или бронь/предварительный договор с жёстким штрафом
- «Рассрочка без банка» ≠ автоматическая защита как у ипотеки
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень», «купить новостройку в тюмени в ипотеку» — demand
- buyer risk: рассрочка, первый взнос, график платежей, расторжение, удержание

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакin context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, банк

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B24",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
