# Description inputs — B34 — 2026-09-30

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B34

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Во вторичке Тюмени — запрет пристава сорвал аванс за 4 дня

**subject:** вторичная квартира в Тюмени и запрет пристава на регистрационные действия

**angle:** Свежая ЕГРН не показала ипотечного обременения, но расширенная проверка до аванса выявила запрет на регистрацию — покупатели не стали вносить деньги.

**comment_magnet_angle:** Если перед авансом всплывает запрет пристава, а продавец клянётся «снимут за два дня» — вы бы внесли аванс или развернулись?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За 4 дня до нотариуса покупатели вторички в Тюмени столкнулись с запретом пристава — и остановили перевод аванса около 400 тысяч рублей. Переоформить квартиру продавца сейчас было нельзя: в ЕГРН висело ограничение ФССП на регистрацию. До этого всё выглядело гладко: банк предварительно одобрил ипотеку, свежая выписка без залога, согласие супруга на месте. Расширенная проверка нашла исполнительные производства примерно на 620 тысяч. Продавец спокойно сказал: «Снимут за два дня, нотариуса не переносим». Покупатели на слово верить не стали, и деньги так и не ушли.

**Para 2 (CTA block):** Проверяем квартиры на вторичке в Тюмени до аванса: ЕГРН, база ФССП, исполнительные производства. Напишите: Telegram или MAX.

## Case hook (from research / article)
- Тюмень, вторичка, 4 дня до нотариуса
- Ипотека одобрена, ЕГРН без ипотеки — все успокоились
- Расширенная проверка ФССП: долг ~620 000 ₽, запрет регистрационных действий
- Продавец: «снимут за два дня», торопит с авансом ~400 000 ₽
- Покупатели спросили про постановление пристава — показать не смог
- Аванс не ушёл; ждут отмену запрета и свежую ЕГРН
- Не самозапрет, не коммуналка — мера пристава по 229-ФЗ
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- buyer risk: запрет пристава, ФССП, ЕГРН, аванс, вторичка Тюмень

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ЕГРН, ФССП

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B34",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
