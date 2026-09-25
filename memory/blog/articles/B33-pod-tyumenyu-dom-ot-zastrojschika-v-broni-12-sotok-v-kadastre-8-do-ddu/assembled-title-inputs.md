# Assembled title inputs — B33 (Derouter title role)

**topic_id:** B33  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** `pod-tyumenyu-dom-ot-zastrojschika-v-broni-12-sotok-v-kadastre-8-do-ddu`  
**research_date:** 2026-09-25

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_kp_land_area_mismatch_cadastre_before_ddu_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **dzen_casus_shape:** PASS
- **klyshin_hook:** none (original casus; fresh Klyshin not required)
- **comment_magnet_angle (Scout):** «Если в брони 12 соток, а в выписке 8 — вы требуете пересчёт цены или всё равно подписываете договор?»

## Editorial spine (composite Tyumen casus — do NOT name КП, developer, bank, address)

1. Family chooses **house with land** in cottage settlement **under Tyumen**; DDU path with developer
2. Presentation + booking document: **12 sotok**, lot number
3. **Few days before** planned contract signing — cadastre / EGRN extract: **8 sotok** (800 m²), possibly different cadastral contour
4. ~**4 sotok / 400 m²** missing (~one third of promised land) — not dismissible as normal measurement error
5. Signing **stopped** until boundaries, area, contract appendices, price «house + land», bank appraisal aligned
6. No escrow yet at this stage; risk = wrong object + booking terms + mortgage re-approval

## voice_angle

«12 on booking paper» vs «8 in cadastre» — conflict **before** signing, not after move-in. Practical tone: don’t accuse developer upfront, but don’t swallow «just a technical glitch».

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| купить новостройку в тюмени | 892 |
| купить дом в тюмени от застройщика | 118 |
| дома с участком от застройщика тюмень | 24 |
| коттеджные поселки тюмень | 1393 |
| выписка егрн | 4358 |

Spine = новостройка/дом от застройщика под Тюменью; механизм = бронь / кадастр / площадь участка / ДДУ / выписка ЕГРН.

## Anti-dupe (published siblings)

- **B27:** декларация — **аренда vs собственность** на землю, 4 дня до ДДУ — **другой plot**
- **B28:** газ **2026 vs 2028** в брони vs декларация КП — **другой plot**
- B22 ставка; B25 отделка; B26 РВЭ; B32 эскроу/юрлицо
- **B33 уникален:** **12 vs 8 соток** — бронь/презентация vs **кадастровые сведения** до подписания договора на дом + землю

## Published titles (anti-repeat only — not style template)

- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B28: Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч
- B23: (apartments vs flat in DDU — different)

## Champion energy (formula, not copy)

Завершённое событие + противоречие документов + следствие для покупателя (остановили подписание / не подписали до сверки).

## Klyshin scream (HARD for this slot)

- **Цифра + удар во второй такт:** **12** vs **8** соток (или «12 соток — 8 в кадастре»)
- Первая часть — бронь/обещание под Тюменью; вторая — кадастр/выписка **до ДДУ** / подписание остановили
- ~50–70 символов; сильный глагол; subject = дом от застройщика / участок / бронь / кадастр / ДДУ
- Temporal marker if it helps: «за несколько дней до ДДУ», «перед подписанием договора»

## Gates (run after JSON)

- `python3 scripts/excalibur_blog_topic_focus.py --text "<h1>"`
- `python3 scripts/excalibur_blog_scout_story_dup.py --text "<h1 + hook + slug>" --topic-id B33`

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
- One headline; Klyshin news-casus rhythm; truth **only** from spine above
- No SEO tail, no «чеклист», no «2026», no colon+keyword spam
- No naming specific КП/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen (adapt Scout angle)
