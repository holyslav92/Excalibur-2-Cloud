# Slot → rubric lock (The Риэлтор)

**Owner:** 2026-09-28 — заменяет legacy «только новостройки» на рубрику по слоту.  
**Гео:** Тюмень. **Форма:** news-casus, engagement bomb (`shared/dzen-news-casus.md`).  
**Анти-дубль:** без изменений (30d cluster, H1 fingerprint, formula spam last-3).

## Расписание (будни, YEKT)

| Слот | Рубрика | Квота/день |
|------|---------|------------|
| 09:00 | `novostroyki` | 2 |
| 12:00 | `novostroyki` | |
| 15:00 | `vtorichka` | 2 |
| 17:00 | `vtorichka` | |
| 19:00 | `arenda` | 1 |

Итого **5** longform/день. Выходные — внешняя routine (отдельно).

## Рубрики

### `novostroyki`

Новостройки Тюмени: ЖК, ДДУ, эскроу, срок сдачи, переуступка, семейная ипотека, КП/ИЖС.  
Запрещены чисто «вторичные» сюжеты без механики новостройки.

### `vtorichka`

Вторичное жильё Тюмень: сделка, ЕГРН/обременения, банкрот продавца, опека, маткапитал, ипотека на вторичку.  
Запрещён retitle вторички в «новостройку» и наоборот.

### `arenda`

Аренда жилья Тюмень: договор, залог, выселение, краткосрочная vs долгосрочная, риски арендатора/собственника.  
Финал — agency к Святославу (покупка/продажа/аренда), не паника.

## Не смешивать рубрики (owner 2026-09-29, Святослав)

**Один слот = одна рубрика везде:** casus, news-hook, право, CTA, comment magnet.  
Слот **новостройки** → только ДДУ, эскроу, бронь, приёмка, застройщик…  
Слот **вторичка** → аванс, ДКП, ЕГРН, дарственная, опека, банкрот продавца…  
Слот **аренда** → договор аренды, залог, выселение, квартирант…  

**FAIL (gate `no_foreign_slot_rubric_mechanism`):** чужая рубрика как механизм в H1/теле — напр. «подключиться до **брони**» в casus про дарственную/аванс (бронь = новостройки).  
**Не FAIL:** общие слова (**ипотека**, банк, квартира, Тюмень), если это не подмена механики сюжета.

Рядом с `no_unrelated_calendar_news_glue`: Trend Radar energy **и** словарь рубрики = слот.

## Scout quad gate

1. **Trend Radar** — hot mechanics/energy с Дзена (`trend-radar.json`, рубрика слота).  
2. **Wordstat** — Tyumen 55+11176, compare RU 225.  
3. **Dzen news-casus** — `dzen_casus_shape: PASS`.  
4. **Anti-dupe HARD** — cluster/fingerprint/formula.

В handoff: `slot_rubric`, `viral_mechanism`, `wordstat_p0`, `comment_magnet_angle`, `anti_dupe_hard: PASS`.

## Cursor Automations (owner)

Добавить **5-ю** automation в будни, **19:00 Asia/Yekaterinburg**, тот же prompt block что и остальные longform, с env `EXCALIBUR_BLOG_SLOT=19:00` (или авто из `excalibur_blog_slot_rubric.py`).  
Существующие 09/12/15/17 — оставить; обновить текст инструкций (Trend Radar → Scout, рубрика из слота, Opus 5.5 Writer/Sol). См. `CLOUD-AUTOMATION.md`.
