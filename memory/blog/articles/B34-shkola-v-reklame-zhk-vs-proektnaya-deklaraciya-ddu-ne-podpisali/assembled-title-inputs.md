# Assembled title inputs — B34 (Derouter title role)

**topic_id:** B34  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** `shkola-v-reklame-zhk-vs-proektnaya-deklaraciya-ddu-ne-podpisali`  
**research_date:** 2026-10-01  
**slot_rubric:** novostroyki

## Scout H1 draft (refine/fix, do not weaken)

В Тюмени за две недели до ДДУ семья сверила школу из рекламы — в проектной декларации срок 2030, подписание остановили

**short title (internal):** Школа в рекламе ЖК vs проектная декларация — ДДУ не подписали

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_pd_school_deadline_vs_ads_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **dzen_casus_shape:** PASS
- **newbuild_mechanism:** реклама/рендер «школа рядом/скоро» vs документальный срок соцобъекта в проектной декларации — стоп перед подписанием ДДУ
- **klyshin_hook:** семья с детьми, новостройка Тюмень, ипотека одобрена; на стенде «школа рядом», менеджер «к сдаче дома»; за **~14 дней** до ДДУ открыли **актуальную** PD на ЕИСЖС → школа/сад **не в проекте** или плановый ввод **2030** (вне семейного плана) → в типовом ДДУ нет строки «построить школу к дате X» → **не подписали** ДДУ, эскроу не открывали; бронь и сроки ипотеки под вопросом
- **comment_magnet_angle (Scout):** «Если в декларации школа через пять лет — вы всё равно берёте квартиру под ребёнка?»

## Editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank, address)

1. Family with children; **newbuild** Tyumen; mortgage approved; booking / DDU signing schedule
2. Ads / stand / manager: «school nearby», «opens soon», renders; oral «by house handover»
3. **~14 days** before DDU — open current project declaration on dom.rf / EISZhS
4. School/daycare **not in project** OR planned commissioning **2030** (or other year outside family plan)
5. Typical DDU does not bind school date; obligations tie to **PD / construction project**, not ad slogan
6. Refused DDU; no escrow; booking + mortgage approval timing at risk

## voice_angle (research)

Спокойная преддоговорная проверка: школа на визуализации может быть реальным будущим объектом, но семье нужен документальный календарь, а не красивый образ района.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 3553 |
| купить новостройку в тюмени | 686 |
| проектная декларация застройщика | 31 |
| школа рядом с новостройкой | 1 |

Spine = новостройки Тюмень; механизм = проектная декларация / школа в рекламе / ДДУ / ЕИСЖС.

## Anti-dupe (published siblings)

- **B28:** газ в КП vs срок в PD 2028, бронь 60k — **другой объект** (газ/КП)
- **B27:** земля аренда vs собственность в PD, 4 дня до ДДУ
- **B25:** чистовая в ДДУ vs приёмка
- **B34 уникален:** школа/сад в рекламе vs срок в PD, стоп ДДУ, семейный горизонт ребёнка

## Published titles (anti-repeat — not style template)

- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B28: Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч
- B25: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали

## Champion energy (formula, not copy)

Завершённое событие + противоречие рекламы и документа + следствие (ДДУ не подписали).

## Klyshin scream (HARD for this slot)

- **Цифра + удар во второй такт:** «две недели» / «14 дней», **«2030»** (срок из PD casus) — допустимо в H1 как stakes
- Первая часть — школа в рекламе ЖК / «рядом»; вторая — проектная декларация / отказ подписать ДДУ
- ~50–70 символов; сильный глагол; subject = новостройка / школа / проектная декларация / ДДУ
- **Forbidden:** «vs» в заголовке как label; «чеклист», «N шагов», SEO «2026»

## Gates (run after JSON)

- `python3 scripts/excalibur_blog_topic_focus.py --text "<h1>"` — need newbuild marker (ДДУ, бронь, новострой…)
- `python3 scripts/excalibur_blog_scout_story_dup.py --text "<h1 + hook + slug>" --topic-id B34`
- `python3 scripts/excalibur_blog_slot_rubric.py --article-dir <dir>` if available

## Task

Output **only** valid JSON for `title-brief.json`:

```json
{
  "topic_id": "B34",
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
- Prefer refining Scout H1 draft if it already passes gates; fix rhythm/length if needed
- No SEO tail, no «чеклист», no «2026» in h1, no colon+keyword spam, avoid «vs» as headline label
- No naming specific ЖК/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen (adapt Scout angle)
