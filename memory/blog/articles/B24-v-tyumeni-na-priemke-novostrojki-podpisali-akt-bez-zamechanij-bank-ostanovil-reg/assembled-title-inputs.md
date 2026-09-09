# Title inputs — B24 (2026-09-09)

topic_id: B24
cluster: acceptance_defects_penalty
tenant: The Риэлтор — Святослав Шакин, Тюмень
slug: v-tyumeni-na-priemke-novostrojki-podpisali-akt-bez-zamechanij-bank-ostanovil-reg

## Scout title draft (starting point — shorten to ~50–70 chars)

В Тюмени на приёмке новостройки подписали акт без замечаний — банк остановил регистрацию из-за дефектов

## Scout handoff

- top_energy_mirror: paper_clean_then_broke
- newbuild_mechanism: акт приёмки-передачи по ДДУ — семья подписала «без замечаний» под давлением менеджера («потом исправим»), через несколько дней независимая приёмка нашла дефекты; банк приостановил регистрацию права и выдачу остатка ипотеки; застройщик отказался устранять по уже подписанному акту
- why_newbuild_not_secondary: сюжет только про сдачу объекта по ДДУ от застройщика, акт приёмки-передачи и ипотечную регистрацию новостройки
- klyshin_hook: none (fresh Tyumen newbuild acceptance casus)
- dzen_casus_shape: PASS
  - event: семья получила ключи, на приёмке подписала акт без замечаний
  - risk: скрытые дефекты + подписанный акт; банк не регистрирует право при открытых недоделках
  - time: через 5 дней после подписания акта, этап подачи документов
  - finale: банк остановил регистрацию и выдачу транша; застройщик отказал в бесплатном устранении — ипотека «в подвешенном состоянии»
- comment_magnet_angle (from Scout): «Менеджер сказал „подпишите, потом исправим“ — вы бы подписали акт без замечаний или отказались от ключей в тот же день?»

## Wordstat demand spine (P0, regions 55+11176, live 2026-09-09)

| phrase | volume |
|--------|--------|
| приемка квартиры в новостройке | 122 |
| приемка квартиры в новостройке тюмень | 32 |
| акт приемки передачи квартиры | 37 |
| приемка квартиры в новостройке на что обратить | 16 |

Final P0: **приемка квартиры в новостройке тюмень** (32); parent spine 122.

Do NOT paste raw SEO phrase into H1. Use as demand spine under news-casus headline.

## Research core conflict (from research-notes.md)

- Менеджер торопит подписать акт «без замечаний», обещает исправить позже.
- После подписи независимая приёмка находит дефекты отделки/окон/инженерии.
- Банк ставит на паузу ипотечный пакет / транш (не тождественно отказу Росреестра — Writer уточнит).
- Читатель не понимает разницу: чистый акт vs фиксация недостатков vs смотровой лист.
- surprising_fact: с 01.03.2025 застройщик обязан подать регистрацию ≤30 раб. дней после акта.

## Published titles to avoid duplicating angle

- B11: открытая кухня остановила регистрацию (layout/planning)
- B09: обременение в ЕГРН сорвало регистрацию
- B12: сдвиг сдачи ЖК — ипотека осталась
- B19/B20/B22/B23: эскроу, ставка, апартаменты — other mechanisms

## Title task

Write ONE title-brief.json (valid JSON only, no markdown fence):

```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-na-priemke-novostrojki-podpisali-akt-bez-zamechanij-bank-ostanovil-reg",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```

Requirements:
- Klyshin news-casus rhythm: завершённое событие + противоречие + следствие
- Clear subject: приёмка новостройки / акт без замечаний / ипотека
- ~50–70 characters for h1
- Strong verb, active voice, Tyumen when it strengthens
- NO checklist hooks, NO SEO tail, NO «полный гайд», NO «2026»
- h1 and title must match
- comment_magnet_angle: sharp debate question for Dzen comments
