# Assembled title inputs — B34 (Derouter title role)

**CRITICAL OUTPUT:** Reply with **only** one raw JSON object (fields below). No markdown fences, no commentary, no planning text before or after JSON.

**topic_id:** B34  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** `v-novostrojke-tyumeni-v-broni-obeschali-dvor-bez-mashin-v-proekte-poyavilsya-pro`  
**research_date:** 2026-09-30  
**slot_rubric:** novostroyki

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_master_plan_driveway_added_tyumen`
- **top_energy_mirror:** marketing vs актуальный проект / генплан
- **dzen_casus_shape:** PASS
- **klyshin_hook:** в брони новостройки в Тюмени — «тихий двор без машин»; за **5 дней** до ДДУ семья открыла обновлённую декларацию и раздел проекта → во дворе **проезд 6 м** и **парковка у подъезда** → застройщик «подпишите ДДУ, проезд служебный» → семья **не подписала**; бронь **150 000 ₽**, вернули **90 000 ₽**; эскроу не открывали
- **comment_magnet_angle (Scout):** «Если во дворе внезапно появляется проезд, а бронь уже оплачена — вы бы подписали ДДУ, чтобы не потерять квартиру, или разорвали бы бронь?»

## Editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank, address)

1. Семья с двумя детьми; семейная ипотека одобрена; выбор квартиры ради закрытого двора
2. Бронь + менеджер/стенд: «двор без машин», детская зона
3. **5 дней** до подписания ДДУ — обновлённый раздел проекта и проектная декларация (ЕИСЖС)
4. На схеме: пожарно-сервисный проезд **6 м** + места у подъезда
5. Отказ от ДДU; **150k → 90k** возврат; без эскроу

## voice_angle (research-notes)

Не спорить с пожарным доступом. Напряжение — образ «тихого двора» vs то, что закреплено в документах до подписи ДДU.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 4325 |
| купить новостройку в тюмени | 900 |
| новостройки в тюмени от застройщика | 673 |
| дду новостройка | 17 |

Spine = новостройки Тюмень; механизм = бронь / проектная декларация / благоустройство / двор без машин / ДДU.

## Anti-dupe (published siblings)

- **B27:** земля аренда vs собственность, 4 дня до ДДU — другой plot
- **B28:** газ / сроки сетей в декларации vs бронь, КП — другой plot
- **B34 уникален:** «двор без машин» vs проезд и парковка у подъезда в актуальном проекте → отказ до ДДU + потеря части брони

## Published titles (anti-repeat — not style template)

- B27: За 4 дня до ДДU в Тюмени обещали землю в собственности — декларация показала аренду
- B28: Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч
- B22: В Тюмени банк поднял ставку ипотеки перед ДДU — бронь сгорела

## Champion energy (formula, not copy)

Завершённое событие + противоречие документов/обещания + следствие для покупателя (деньги/отказ от ДДU).

## Klyshin scream (HARD for this slot)

- **Цифра + удар во второй такт:** «5 дней», «60 тысяч» (150−90), «6 метров» — опционально, если укладывается в ~50–70 символов
- Первая часть — бронь/обещание «двор без машин» в новостройке Тюмени; вторая — проект/проезд/отказ/потеря брони
- ~50–70 символов; сильный глагол; subject = новостройка / бронь / двор / ДДU
- Forbidden main hook: чеклист, N шагов, «стоит ли покупать»

## Gates (run after JSON)

- `python3 scripts/excalibur_blog_topic_focus.py --text "<h1>"` — newbuild marker
- `python3 scripts/excalibur_blog_scout_story_dup.py --text "<h1 + hook + slug>" --topic-id B34`

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
- No SEO tail, no «чеклист», no «2026» in h1, no colon+keyword spam
- No naming specific ЖК/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen (adapt Scout angle)
