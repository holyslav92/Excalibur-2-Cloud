# Assembled title inputs — B33 (Derouter title role)

You ARE the Derouter `title` role inside `excalibur_blog_derouter_opus_chat.py`. You MUST output **only** valid JSON with non-null `h1`, `title`, `angle`, `comment_magnet_angle`, and `verdict: "PASS"`. Do NOT return DEROUTER TITLE BLOCKER — generation is happening now.

**topic_id:** B33  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** `v-tyumeni-za-chas-do-ddu-snyali-bron-doma-v-kp-lot-prodali-drugomu`  
**research_date:** 2026-09-26

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_kp_booking_cancelled_same_lot_sold_other_buyer_tyumen`
- **top_energy_mirror:** someone_else_took_object (+ clock_ran_out)
- **dzen_casus_shape:** PASS
- **klyshin_hook:** none (original Tyumen KP casus)
- **newbuild_mechanism:** семья с детьми и частный инвестор параллельно смотрят **дома от застройщика** в коттеджном посёлке под Тюменью. Семья внесла бронь **250 000 ₽**, дата подписания ДДУ через **12 дней**. **За час** до визита в офис: лот №14 снят с брони — **другой покупатель подписал ДДУ** на этот дом. Бронь аннулировали; предложили соседний участок **+680 000 ₽** или возврат **180 000 ₽** из 250. ДДУ семьи не подписали, **эскроу не открывали**.
- **comment_magnet_angle (Scout):** «Если за час до ДДУ застройщик снимает бронь и продаёт тот же дом другому — вы берёте «соседний лот» или забираете деньги и уходите?»

## Editorial spine (composite Tyumen casus — do NOT name КП, developer, bank, address, real lot)

1. Paid developer booking on a **house lot** in KP under Tyumen (newbuild / DDU chain, not secondary)
2. Clock: **1 hour** before scheduled sales-office visit for DDU path
3. Manager: same lot off booking — **another buyer already signed DDU** on that house
4. Fork: pricier neighboring lot or partial refund of booking (180k of 250k casus)
5. Legal gap: booking ≠ registered DDU; 214-FZ escrow protection not yet on; double-sale jurisprudence → often damages not “get that exact house”

## voice_angle

«Бронь держит лот в голове и в WhatsApp», а дом в КП часто достаётся тому, кто первым **подписал и зарегистрировал ДДУ** — иногда за час до визита в офис.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume (55+11176) |
|--------|------------------:|
| коттеджный поселок тюмень купить дом | 44 |
| дома под тюменью от застройщика | 44 |
| дом от застройщика тюмень (phrase cluster) | 344 |

Spine = КП / дом от застройщика под Тюменью; механизм = бронь → ДДУ → эскроу; конфликт = тот же лот / другой покупатель / час до визита.

## Anti-dupe (published siblings — change angle if too close)

- **B28:** газ в декларации КП vs бронь, −60 тыс — **другой plot**
- **B27:** земля аренда vs собственность, 4 дня до ДДУ
- **B22:** банк поднял ставку перед ДДУ — бронь сгорела (ипотека, не double sale)
- **B32:** чужое юрлицо в реквизитах эскроу
- **B33 уникален:** платная бронь на **дом в КП** → за **час** до ДДУ лот ушёл **другому** с подписанным ДДУ; вилка соседний лот дороже / частичный возврат брони

## Published titles (anti-repeat — not style template)

- B28: Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч
- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B22: В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела

## Champion energy (formula, not copy)

Завершённое событие + кто-то другой забрал объект + следствие для семьи с бронью (деньги / другой лот).

## Title craft (HARD)

- **Цифра + удар во второй такт:** «за час до ДДУ» (preferred), «другому покупателю» / «лот ушёл другому»
- **H1 MUST include newbuild marker:** ДДУ, бронь, КП/коттеджный посёлок, застройщик, or новострой — `topic_focus` FAIL on bare «дом» without these
- **Do NOT lead H1 with сумма брони «250 тысяч»** — triggers `h1_fingerprint_same_day amount:booking_expired` BLOCKER
- Subject clear: **дом в КП** / бронь / ДДУ / тот же лот
- ~50–70 символов; сильный глагол; активный залог; Тюмень
- Scout title_draft **passes gates** (use as baseline rhythm, may tighten): «В Тюмени за час до ДДУ сняли бронь дома в коттеджном посёлке — лот продали другому покупателю»

## Task

Output **only** valid JSON for `title-brief.json`:

```json
{
  "topic_id": "B33",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```

Constraints:
- One headline; Klyshin news-casus rhythm; facts **only** from spine above
- No SEO tail, no «чеклист», no «2026», no colon+keyword spam, no «полный гайд»
- No naming specific КП/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen (adapt Scout angle: соседний лот vs уйти с деньгами)
