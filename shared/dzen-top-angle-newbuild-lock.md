# Dzen Top-Angle → Newbuild Lock (HARD — owner permanent)

**Владелец:** Святослав Шакин  
**Дата:** 2026-09-05  
**Статус:** `LOCKED_ON_MAIN` — не ослаблять без явного owner override.

## Контекст (Studio 2026-09-05)

- Канал ~398 подписчиков; **top-10 по opens — вся вторичка** (ЕГРН до аванса, бабушка на осмотре, «всё проверил — проиграл», банкрот продавца…).
- Новостройки: сотни показов, слабые opens, часто 0 комментариев / 0 подписок.
- **Мандат:** не резать до 2 слотов — **4/day (09/12/15/17 YEKT)** остаются. Качество > retitle. Scout **крадёт энергию top-10**, но **plot = ONLY newbuild** (квартиры + дома КП/ИЖС).

См. также: `shared/newbuild-focus-lock.md`, `shared/scout-story-clusters.json`, `memory/scout/used-clusters.json`.

## Расписание (не менять)

4 weekday-слота YEKT: **09:00, 12:00, 15:00, 17:00** — `shared/tenant-config.json` → `publish_schedule.runs_per_day: 4`.  
Weekend automation **не** запускать без отдельного owner-запроса.

## Разрешённая ENERGY (не plot)

Scout **не копирует вторичный сюжет**. Берёт **эмоциональный угол** из top-10 и переводит в **новостройку Тюмень**:

| top_energy_id | Энергия (что цепляет во вторичке) | Newbuild plot (Тюмень) — примеры механики |
|---------------|-----------------------------------|---------------------------------------------|
| `almost_lost_home` | «Почти потеряли квартиру» — stakes до денег | Бронь сгорела за 48 ч; условия ДДУ изменились накануне подписания; trade-in «забрали объект» |
| `stopped_before_money` | Остановили **до** аванса / до перевода | Эскроу не открыли после одобрения ипотеки; банк поднял ставку накануне ДДУ; рассрочка от застройщика — штраф за просрочку платежа |
| `paper_clean_then_broke` | «На бумаге чисто» — потом сломалось | В ДДУ «квартира», в выписке — апартаменты; оценка банка ниже цены ДДУ; проектная декларация vs факт на приёмке |
| `someone_else_took_object` | Объект забрали / ушёл другому | Переуступку купили раньше; бронь сняли — «квартира уже в брони»; trade-in: застройщик не принял старую квартиру |
| `clock_ran_out` | Время вышло — дедлайн | Срок брони; срок рассрочки; неустойка за просрочку ключей; 214-ФЗ срок сдачи + штраф не выплатили |
| `number_in_claim_vs_zero_paid` | Цифра в документе ≠ факт оплаты | Сумма в ДДУ vs внесено на эскроу; «в договоре 500 тыс брони» — на счёте 0; неустойка в акте ≠ выплате |

### FORBIDDEN plots (вторичка — не retitle)

Запрещено recycling secondary casus, даже с «новостройкой» в H1:

- бабушка / пожилой продавец / доверенность на осмотре
- банкротство **продавца** вторички / финуправляющий
- соседская доля / коммуналка / преимущественное право
- опека / маткапитал **на вторичке** / детские доли
- «чистая ЕГРН оспорили» как **secondary** casus (наследники, суд через 2 года)
- 4 месяца поиска вторички / жёлтое заключение
- ПНД / повестка / прописанные

Gate: `shared/scout-story-clusters.json` → `frozen_secondary: true` + `scripts/excalibur_blog_topic_focus.py`.

### FORBIDDEN shape

- Спокойные «как устроена…», «гайд», «N шагов», чеклист вместо news-casus
- TL;DR / «Быстрый инсайт» / bullet-dump в лиде

## Scout handoff (обязательные поля)

Каждый pick **до** research_start:

```text
top_energy_mirror: <almost_lost_home|stopped_before_money|paper_clean_then_broke|someone_else_took_object|clock_ran_out|number_in_claim_vs_zero_paid>
newbuild_mechanism: «…» (конкретная механика: бронь/эскроу/уступка/…)
why_newbuild_not_secondary: «…» (1–2 предложения)
story_dup_check: PASS | cluster_id: <уникальный>
h1_fingerprint_check: PASS | fingerprint: <number:mechanism или mechanism-only>
formula_spam_check: PASS | last3_mechanisms: <…>
anti_dupe_hard: PASS
```

## HARD anti-dupe (сильнее soft 30d)

Конфиг: `shared/scout-story-clusters.json` → `anti_dupe_hard`.

| Gate | Окно | Действие |
|------|------|----------|
| **cluster lock** | 30 дней | Same `cluster_id` в `used-clusters.json` = FAIL даже при новом title |
| **H1 fingerprint** | 30 дней | Тот же **number + mechanism** (напр. «бронь сгорела + 500 тысяч») = FAIL, если механика не явно другая |
| **formula spam** | last 3 published | Три подряд с одним skeleton (бронь/ДДУ/застройщик Тюмень без новой механики) → Scout FAIL, другой mechanism |
| **same-day dup** | 0 дней | Тот же fingerprint или cluster в тот же день = FAIL |
| **topic_id** | 30 дней | Повтор `topic_id` в ledger = FAIL |

Скрипты:

```bash
python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters
python3 scripts/excalibur_blog_scout_helper.py --check-query "<title + hook + slug>"
python3 scripts/excalibur_blog_scout_story_dup.py --text "<title + hook + slug>"
```

`research_start` вызывает тот же gate **до Writer** — duplicate = BLOCKER до пайплайна.

## Примеры allowed Scout pitches (mapped from top-10 energy)

| top_energy | Scout pitch (H1 draft) | cluster_id | Почему newbuild |
|------------|------------------------|------------|-----------------|
| `stopped_before_money` | «В Тюмени одобрили семейную ипотеку на новостройку — эскроу так и не открыли, ДДУ остановили» | `escrow_not_opened_after_mortgage` | ДДУ/эскроу/застройщик, не вторичка |
| `almost_lost_home` | «Бронь на квартиру в ЖК сгорела за сутки — застройщик поднял цену на 400 тысяч» | `booking_expired_price_hike` | Бронь/застройщик, stakes до денег |
| `paper_clean_then_broke` | «В ДДУ написали «квартира» — в выписке оказались апартаменты, банк отказал» | `ddu_apartment_vs_apartments_mismatch` | Документ новостройки, не ЕГРН-вторичка |
| `someone_else_took_object` | «Держали переуступку — другой покупатель внёс бронь на ту же планировку» | `assignment_lost_to_faster_buyer` | Переуступка новостройки |
| `clock_ran_out` | «Срок сдачи сдвинули на год — неустойку в договоре обещали, на счёт не пришло» | `keys_delay_penalty_unpaid` | ДДУ/срок сдачи/неустойка |
| `number_in_claim_vs_zero_paid` | «В ДДУ — 600 тысяч брони, на эскроу за неделю до подписания — ноль» | `ddu_amount_vs_escrow_zero` | Цифра в ДДУ vs факт оплаты |

## Кто читает этот lock

Scout, Director, CLOUD-AUTOMATION, `shared/pipeline-canon.json`, Derouter `--role scout` system file, AGENTS.md.
