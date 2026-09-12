# Title inputs — B24 — 2026-09-12

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier, gpt-6-astra). Output **valid JSON only** per schema below. No BLOCKER refusals — generate the title now.

## Task
Invent ONE Klyshin-style screaming H1 for topic B24. verdict: PASS.

**topic_id:** B24  
**slug:** transhevaya-ipoteka-vtoroj-transh-vyros-na-480-tysyach-semya-ostanovila-ddu  
**tenant:** Святослав Шакин / Тюмень  
**research_date:** 2026-09-12

## Task

Produce exactly ONE `title-brief.json` object (valid JSON only, no markdown wrapper):

```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "что за тема, входит в h1",
  "angle": "почему этот заголовок",
  "comment_magnet_angle": "острый вопрос/угол спора для комментариев Дзена",
  "slug": "transhevaya-ipoteka-vtoroj-transh-vyros-na-480-tysyach-semya-ostanovila-ddu",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```

## Scout handoff (2026-09-12)

- **klyshin_hook:** none
- **dzen_casus_shape:** PASS
  - **event:** одобрили траншевую ипотеку и забронировали квартиру в новостройке
  - **risk:** второй транш/платёж вырос на 480 тыс., график не сходится с бюджетом
  - **time:** за 1 день до подписания ДДУ
  - **finale:** остановили до эскроу, пересчитали условия
- **comment_magnet_angle (scout):** кто виноват — банк, застройщик или покупатель, что не прочитал график траншей до брони?
- **newbuild_mechanism:** траншевая ипотека на новостройку — второй транш/платёж вырос на 480 тыс. накануне подписания ДДУ, семья остановила сделку до перевода на эскроу
- **why_newbuild_not_secondary:** только ДДУ + эскроу + строящийся ЖК
- **anti_dupe_hard:** PASS | fingerprint: `amount:tranche_second_jump_480k`

## Wordstat (MCP-KV live 2026-09-12, regions 55+11176)

- P0 «новостройки тюмень» — **4560** (demand spine — не вставлять в H1)
- «ипотека на новостройки тюмень» — **49**
- «траншевая ипотека новостройка» — **4** (узкий хвост)

## Research facts (truth only)

**Topic:** Траншевая ипотека на новостройку: второй транш увеличил нагрузку на 480 000 ₽, семья остановила сделку до подписания ДДУ.

**Case status:** Собирательный редакционный кейс. Публичного репортажа о конкретной тюменской семье, ЖК, банке и сумме 480 000 ₽ нет. 480 000 ₽ — редакционный параметр сценария (рост нагрузки/платежа после второго транша), не рыночная статистика.

**Spine:**
- Семья в Тюмени бронирует квартиру в новостройке, получает одобрение траншевой ипотеки.
- В рекламе — низкий платёж на период стройки (малый первый транш).
- За **1 день** до подписания ДДУ — обновлённый график: второй транш и итоговый платёж существенно выше витринной калькуляции.
- Нагрузка не сходится с бюджетом — параметр **+480 000 ₽**.
- Семья **останавливает** подписание ДДУ **до** открытия эскроу.

**Mechanism (for subject clarity):** Траншевая ипотека — кредит на новостройку выдается частями на эскроу; после второго транша платёж резко растёт. Отличается от B22 (там банк менял **ставку**, здесь — **график траншей**).

**voice_angle:** Напряжение между временным платежом «на стройке» и обязательством после выдачи всей суммы. Остановка за день до ДДУ — редкая дисциплина.

## Anti-dupe (published titles — do NOT repeat angle)

- B22: «В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (rate change, not tranche)
- B19: ипотеку одобрили — эскроу сорвал маткапитал
- B12: застройщик сдвинул сдачу ЖК — ипотека осталась
- B20: застройщик сменил юрлицо — банк не открыл эскроу

B24 plot = **траншевая ипотека**, скачок при **втором транше**, остановка **до эскроу**, цифра **480 тысяч**.

## H1 requirements (Klyshin news-casus rhythm)

- News headline: завершённое событие + противоречие + следствие
- **Digit + punch:** 480 тысяч, 1 день до ДДУ
- **Subject clear:** траншевая ипотека / новостройка / второй транш
- **Strong verb**, active voice, ~50–70 chars
- **Тюмень** when strengthens local intent (prefer «В Тюмени» like B22)
- NO: checklist, N шагов, SEO tail, «2026», colon+keyword, label head
- NO: how-to hook («как купить», «стоит ли»)
- Champion energy (don't copy): «Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Forbidden main hooks

«чеклист», «N шагов», «стоит ли покупать сейчас», «как купить без риелтора»
