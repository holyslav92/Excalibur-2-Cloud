# Description inputs — B06 — 2026-08-21

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.

## topic_id
B06

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Автооценка занизила цену — и квартира подорожала за сутки

**subject:** автооценка квартиры в сервисах (ЦИАН, Домклик, Авито) против реальной цены сделки на тюменской вторичке

**angle:** Klyshin-ритм: алгоритм показал цену ниже рынка, покупатель бежит на просмотр по цене которой уже нет. Очередь на показ, собственник снимает объявление и поднимает цену. НЕ B05 (там скидка от продавца + срочный задаток).

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Каждую осень мне приходит одно и то же письмо. Меняются только адреса.

**Para 2:** Покупатель присылает ссылку на объявление и скриншот из сервиса оценки. «Смотрите: алгоритм говорит восемнадцать. Продавец просит восемнадцать. Значит, восемнадцать — и есть настоящая цена. А вы мне про двадцать рассказывали».

**Para 3 (context only):** Звоним по объявлению. Запись на просмотр — через два дня, потому что перед нами семь человек. На следующее утро объявление исчезает. Через неделю та же квартира появляется снова — и теперь она дороже рынка, а не дешевле.

## Case hook (from research / article)
- Сервис показывает ~18 млн, живой спрос ~20 млн
- Покупатель принимает «рекомендованную цену» за гарантию сделки
- Очередь на просмотр (7 человек впереди), объявление снято, цена выше рынка
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить квартиру в тюмени» 23066; «вторичка в тюмени» 5799
- Buyer risk: аванс, очередь, цена сделки ≠ оценка сервиса

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ЦИАН, Домклик, ЕГРН

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B06",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
