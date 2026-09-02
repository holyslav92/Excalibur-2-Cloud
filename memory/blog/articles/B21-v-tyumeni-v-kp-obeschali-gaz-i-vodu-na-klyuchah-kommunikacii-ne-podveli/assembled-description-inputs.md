# Description inputs — B21 — 2026-09-02

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B21

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени дом сдали без газа и воды — семья не взяла ключи

**subject:** дом от застройщика в коттеджном посёлке под Тюменью, где к выдаче ключей не подвели газ и воду

**angle:** Новостной casus: обещанные сети в посёлке не стали подключением к конкретному дому, поэтому семья отказалась подписывать акт.

**comment_magnet_angle:** Дом в коттеджном посёлке без газа и воды у забора — вы подпишете акт приёмки ради ключей и ипотеки или будете ждать, пока застройщик подведёт коммуникации?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Семья с двумя детьми приехала за ключами от дома в коттеджном посёлке под Тюменью. Год после регистрации ДДУ. У забора пусто: ни точки газа, ни точки воды. Граница участка в выписке легла не так, как на генплане. Акт не подписали, ключи не взяли. Транш по ипотеке банк тоже не выдал.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. Такие приёмки разбираю по документам, а не по буклетам: Telegram — Tyumen_Rieltor и MAX. Сомневаетесь в формулировке про газ и воду в своём ДДУ — пришлите её текстом, посмотрим вместе.

## Case hook (from research / article)
- Тюмень, коттеджный посёлок, семья с двумя детьми, год после регистрации ДДУ
- День ключей: у забора пусто — ни газа, ни воды, хотя на презентации стояли значки «газ» и «вода»
- Менеджер: «газ в посёлке есть, вода на улице, подключение — отдельные заявки»; предлагает подписать акт, иначе будет односторонний
- В ДДУ — только «техническая возможность», не ввод на участок
- Граница участка в ЕГРН не совпала с генпланом из офиса
- Мотивированный отказ с фото/видео; ключи не взяли
- Банк не выдал следующий транш по ипотеке (по условиям кредитного договора)
- Ловушка: «газ в посёлке» ≠ точка подключения у вашего забора
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- загородный дом / КП / ДДУ / коммуникации / приёмка / мотивированный отказ
- buyer risk: газ и вода на ключах, граница участка, односторонний акт, ипотечный транш

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler, no how-to blurb
6. Cyrillic; brands OK: ДДУ, ЕГРН, КП

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B21",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
