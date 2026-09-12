# Title inputs — B24 — 2026-09-10

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-bron-na-novostrojku-sgorela-za-sutki-zastrojschik-podnyal-cenu-na-450-`

## Scout handoff
- cluster_id: booking_expired_price_hike_tyumen
- klyshin_hook: none (fresh Tyumen newbuild booking/price casus without Klyshin)
- top_energy_mirror: almost_lost_home
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке, внесла 50 000 ₽ за бронь, получила фиксацию цены и планировки на 48 часов; ипотека предварительно одобрена
  - risk: за 24 часа до дедлайна застройщик поднял стоимость выбранного лота на 450 000 ₽; без согласия на новую цену бронь прекращается
  - time: последние 24 часа брони — накануне подписания ДДУ и открытия эскроу
  - finale: семья не успела доплатить разницу; бронь сняли; квартиру забронировали другие; 50 000 ₽ удержали по оферте как услуга/штраф; ДДУ не подписан, эскроу не открыт
- comment_magnet_angle: «Бронь на двое суток и внезапные +450 тысяч: вы бы доплатили, чтобы не потерять планировку, или искали бы другой ЖК — даже если ипотека уже одобрена?»
- title_draft (rework allowed): В Тюмени бронь на новостройку сгорела за сутки — застройщик поднял цену на 450 тысяч
- story_dup_check: PASS — distinct from B22 (bank raised mortgage rate before DDU, not developer price hike)
- distinct_plot: платная бронь 48 ч + рост прайса застройщика накануне ДДУ (не банк/ставка B22, не эскроу/маткапитал B19, не смена юрлица B20)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 885 (55+11176; compare225: 1903)
- support: «новостройки тюмень» — 4642
- weak direct: «бронь новостройки» — 3 (55+11176; compare225: 288)

## Research — subject & conflict
- Subject: платная бронь новостройки в Тюмени, фиксация цены на 48 часов, рост прайса застройщика на 450 000 ₽ за сутки до дедлайна, удержание 50 000 ₽, ипотека одобрена но ДДУ/эскроу ещё не открыты
- Reader problem: семья считает бронь «закрепила» квартиру и цену, а ипотека одобрена — до ДДУ осталась формальность; бронь ≠ ДДУ ≠ эскроу
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, застройщика)
- Surprising fact: 50 000 ₽ может быть удержана полностью как «услуга бронирования», даже если ДДУ не подписали — одна фраза в оферте важнее одобрения ипотеки
- Voice angle: столкновение «ипотека одобрена, квартира моя» с коротким платным окном и пересчётом прайса
- Finale: не доплатили → бронь сняли → лот ушёл другим → 50 тыс. удержали

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot: банк/ставка, не застройщик/цена)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), открытая кухня (B11), перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), банк поднял ставку перед ДДУ (B22), апартаменты в ДДУ (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за сутки», «накануне ДДУ», «за 48 часов»)
- One variant only
- Include slug confirmation in JSON

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-bron-na-novostrojku-sgorela-za-sutki-zastrojschik-podnyal-cenu-na-450-",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
