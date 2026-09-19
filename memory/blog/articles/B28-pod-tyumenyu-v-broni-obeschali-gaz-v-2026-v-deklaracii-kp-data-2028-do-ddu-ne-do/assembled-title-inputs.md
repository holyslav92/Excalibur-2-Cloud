# Assembled title inputs — B28 (Derouter title role)

**topic_id:** B28  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** `pod-tyumenyu-v-broni-obeschali-gaz-v-2026-v-deklaracii-kp-data-2028-do-ddu-ne-do`  
**research_date:** 2026-09-19

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_kp_gas_declaration_date_mismatch_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **dzen_casus_shape:** PASS
- **klyshin_hook:** в офисе КП под Тюменью — «газ на участке, подключение в 2026»; в брони те же слова → за **6 дней** до ДДУ открыли проектную декларацию в ЕИСЖС → в блоке инженерных сетей **ввод газопровода IV квартал 2028** → застройщик «подпишите ДДУ, раньше вытянем по графику» → семья **не подписала** ДДУ; бронь **200 000 ₽**, вернули **140 000 ₽**, удержали **60 000 ₽**; эскроу не открывали
- **comment_magnet_angle (Scout):** «Если в брони газ в 2026, а в декларации КП — 2028, вы бы подписали ДДУ, чтобы не потерять бронь, или ушли бы сразу?»

## Editorial spine (composite Tyumen casus — do NOT name КП, developer, bank, address)

1. Family with two children; **ready house** in cottage settlement under Tyumen; DDU path
2. Booking + manager: gas / communications, connection **2026** (oral + booking text — casus only)
3. **6 days** before planned DDU signing — open declaration on dom.rf / EISZhS
4. Engineering networks: **gas pipeline commissioning IV quarter 2028** (not 2026)
5. Developer: sign DDU, earlier on internal schedule
6. Refused DDU; booking **200k → 140k** return, **60k** withheld; no escrow

## voice_angle

«Газ на табличке» vs бумага: семья считает отопление, а в декларации другой горизонт по сетям.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 4430 |
| коттеджные поселки тюмень | 1455 |
| проектная декларация застройщика | 25 |
| дду | 44 |

Spine = новостройки/КП Тюмень; механизм = проектная декларация / инженерные сети / газ / бронь / ДДУ.

## Anti-dupe (published siblings)

- **B27:** земля **аренда vs собственность** в разделе 12, 4 дня до ДДУ — **другой plot**
- B22 ставка ипотеки; B25 отделка; B26 РВЭ/транш
- **B28 уникален:** газ / сроки сетей в декларации vs обещание в брони → отказ до ДДУ + потеря части брони

## Published titles (anti-repeat — not style template)

- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B22: В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела
- B25: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали

## Champion energy (formula, not copy)

Завершённое событие + противоречие документов + следствие для покупателя.

## Klyshin scream (HARD for this slot)

- **Цифра + удар во второй такт** (после тире/поворота): напр. «6 дней», «60 тысяч», «2028» (срок из декларации casus), **не** календарный SEO-хвост «2026» в H1
- Первая часть — обещание/бронь/КП под Тюменью; вторая — декларация / отказ / потеря денег
- ~50–70 символов; сильный глагол; subject = дом в КП / газ / проектная декларация / ДДУ

## Gates (run after JSON)

- `python3 scripts/excalibur_blog_topic_focus.py --text "<h1>"` — need newbuild marker (ДДУ, бронь, коттедж, КП, новострой…)
- `python3 scripts/excalibur_blog_scout_story_dup.py --text "<h1 + hook + slug>" --topic-id B28`

## Task

Output **only** valid JSON for `title-brief.json`:

```json
{
  "topic_id": "B28",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```

Constraints:
- One headline; Klyshin news-casus rhythm; truth **only** from spine above
- No SEO tail, no «чеклист», no «2026» in h1, no colon+keyword spam
- No naming specific КП/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen (можно адаптировать Scout angle; без 2026 в magnet если возможно — фокус на бронь vs декларация)
