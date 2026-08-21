# Description inputs — B07 — 2026-08-21

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.

## topic_id
B07

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Наследству на квартиру два года. Сын от первого брака отказ не писал

**subject:** покупка квартиры, полученной по наследству: срок меньше трёх лет и наследник первой очереди (сын от первого брака) без нотариального отказа

**angle:** Две короткие реплики в ритме Klyshin: срок наследства + скрытый наследник — весь конфликт сделки в одной строке. Первая часть даёт объект и трёхлетнее окно риска, вторая ломает обещание продавцов «отказа не будет, покупайте так»: отказ бывает только у нотариуса, слова не считаются.

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Квартира выглядела нормально.

**Para 2:** Один продавец. Один собственник в выписке ЕГРН. Свидетельство о праве на наследство на руках. Документы, как говорят на просмотре, «в порядке».

**Para 3 (context only):** Потом всплыла деталь. У наследодателя есть сын от первого брака. Нотариального отказа он не писал. Где он сейчас — продавцы толком не знают.

**Para 4:** Смерть отца — примерно два года назад. Предложение покупателю прозвучало по-домашнему: «Давайте оформим так, а с отказом потом разберёмся».

## Case hook (from research / article)
- Один собственник в ЕГРН, свидетельство о наследстве — «всё чисто»
- Скрытый наследник: сын от первого брака, нотариального отказа нет, местонахождение неизвестно
- Смерть отца ~2 года назад; продавцы: «с отказом потом разберёмся»
- «Он не будет претендовать» ≠ нотариальный отказ (ст. 1157 ГК РФ)
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «наследство квартиры» 968; «отказ от наследства» 301; «квартира наследство продажа» 176
- Buyer risk: аванс, скрытый наследник, устное обещание вместо отказа у нотариуса

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ЕГРН, ЦИАН, Домклик

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B07",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
