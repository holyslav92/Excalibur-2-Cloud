# Assembled title inputs — B33 (Derouter title role)

**topic_id:** B33  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** za-5-dnej-do-ddu-v-proekte-povernuli-dom-iz-okna-vmesto-dvora-shumnaya-ulica  
**research_date:** 2026-09-22

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_section_orientation_window_view_before_ddu_tyumen`
- **top_energy_mirror:** Paper looked clean on the showroom floor plan — then the building orientation in the project docs broke the «quiet courtyard» promise five days before DDU.
- **dzen_casus_shape:** PASS
- **klyshin_hook:** optional — не использован (свежий hot casus без Klyshin)
- **comment_magnet_angle (Scout):** Кто виноват, если «на макете во двор» — а в проекте ДДУ окна на магистраль: покупатель, менеджер или «так и было в декларации»?

## Editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank, street)

1. Семья с детьми, новостройка Тюмени; бронь **120 000 ₽**; ипотека одобрена под объект
2. В офисе, на рендере и при бронировании — тихая сторона, вид во **внутренний двор**
3. **За пять дней** до намеченного подписания ДДУ открывают проект договора, приложение и актуальную проектную документацию
4. Ориентация секции/фасада: окна выбранной квартиры на **оживлённую улицу/магистраль**, не во двор
5. Менеджер: генплан «всегда был таким», макет — маркетинг; в декларации на ЕИСЖС схема согласуется с документами, не с обещанием офиса
6. ДДУ **не подписан**, на эскроу деньги **не переводили**; спор — не входить в сделку и вернуть бронь (условия по соглашению о бронировании, не автоматом по 214-ФЗ)

## voice_angle

«Макет во двор — проект на магистраль»: офис продаёт сторону света и тишину, документы перед ДДУ показывают фасад по конкретному лоту.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 3463 |
| купить новостройку в тюмени | 679 |
| новостройки в тюмени от застройщика | 466 |
| проектная декларация застройщика | 21 |
| субсидированная ипотека от застройщика тюмень | 14 |

Spine = новостройки Тюмень + проверка до ДДУ; механизм = проектная документация / приложение к ДДУ / ориентация секции / вид из окна vs обещание двора.

## Anti-dupe (published siblings — другой plot)

- B27: земля в декларации (аренда vs обещание собственности) — не вид из окна
- B25: чистовая в ДДУ vs приёмка
- B23: квартира vs апартаменты в ДДУ
- B22/B29/B31/B32/B30: банк/страховка/эскроу/уступка перед ДДУ — не ориентация дома
- Избегать клонов формулы «за N дней до ДДУ» без механики **поворот секции / вид из окна / макет vs проект**

## Published titles (anti-repeat only — not style template)

- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B32: За 2 дня до эскроу банк остановил сделку в новостройке Тюмени — в ДДУ чужое юрлицо
- B31: За 2 дня до ДДУ страховка добавила восемнадцать тысяч в месяц — банк снял одобрение ипотеки на новостройку в Тюмени
- B25: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали

## Champion energy (formula, not copy)

«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял» — завершённое событие + противоречие + следствие.

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
- One headline, ~50–70 characters, Klyshin news-casus rhythm
- Clear subject (новостройка / вид из окна / проект ДДУ / ориентация секции)
- Strong verb, active voice; temporal marker («за 5 дней до ДДУ»)
- No SEO tail, no «чеклист», no «2026», no colon+keyword spam
- No naming specific ЖК/developer/bank/street
- `comment_magnet_angle` = sharp debate question for Dzen comments
