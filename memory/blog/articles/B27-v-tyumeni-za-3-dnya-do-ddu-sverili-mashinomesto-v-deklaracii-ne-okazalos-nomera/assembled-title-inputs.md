# Title inputs — B27 — 2026-09-16

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-za-3-dnya-do-ddu-sverili-mashinomesto-v-deklaracii-ne-okazalos-nomera`

## Scout handoff
- cluster_id: parking_declaration_mismatch_tyumen
- klyshin_hook: none (fresh Tyumen newbuild parking/declaration casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке + отдельное машино-место в паркинге; менеджер включил место в бронь и ипотечный пакет
  - risk: номер машино-места из брони не подтвердился в проектной декларации (раздел 15.3) для выбранного корпуса/очереди на наш.дом.рф — банк не открыл эскроу на полный пакет «квартира + место»
  - time: за 3 дня до подписания ДДУ
  - finale: сделку остановили до аванса; потребовали от застройщика документально подтвердить объект или заменить место
- comment_magnet_angle: брать машино-место отдельным ДДУ или включать в ипотеку вместе с квартирой?
- title_draft (rework allowed): В Тюмени за 3 дня до ДДУ сверили машиноместо — в декларации не оказалось номера
- top_energy_mirror: paper clean then broke — «в брони всё сходилось, в декларации номер исчез»
- newbuild_mechanism: ДДУ на машино-место + проектная декларация ЖК + эскроу-пакет с квартирой
- story_dup_check: PASS — distinct from B21 (кладовка на ключах), B23 (квартира vs апартаменты), B19/B20/B22 (эскроу/ипотека другие механики)
- distinct_plot: расхождение номера машино-места между бронью/планом и проектной декларацией конкретного корпуса; не вторичка парковок

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4475 (55+11176)
- mechanism: «дду машиноместо» — 217 (RU 225)
- support: «купить новостройку в тюмени» — 902
- support: «купить машиноместо дду» — 35
- support: «жк новостройки тюмень» — 204

## Research — subject & conflict
- Subject: новостройка в Тюмени, машино-место в паркинге, бронь с номером, проектная декларация на наш.дом.рф (раздел 15.3), ДДУ, эскроу-пакет с квартирой
- Reader problem: семья думает, что бронь с номером на плане подтверждает объект; за 3 дня до ДДУ сверка с ПД показывает, что номера нет в декларации корпуса/очереди; банк не открывает эскроу на полный пакет
- Casus: редакционный тюменский сюжет (без имён, ЖК, банка); не писать «случай собирательный» в теле
- Surprising fact: гостевые и зависимые машино-места в ПД не продаются по ДДУ — менеджер мог показать номер с разметки, которого нет в 15.3
- Voice angle: «номер на брони» vs «условный номер в разделе 15.3 ПД конкретного корпуса» — два разных языка; путаница корпуса/очереди ломает связку «квартира + парковка» в ипотечном пакете
- Finale: остановили до аванса; потребовали подтверждение или замену места от застройщика
- Distinct from B21 (кладовка по ДДУ на ключах), B23 (апартаменты в ЕГРН), B19 (маткапитал/эскроу), B22 (ставка перед ДДУ), B20 (смена юрлица)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)
«В Тюмени в ДДУ написали квартиру — в выписке оказались апартаменты» (B23 — другой plot)

## Anti-dup published titles
B02–B26 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), апартаменты в ЕГРН (B23), чистовая на приёмке (B25), РВЭ без разрешения (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за 3 дня до ДДУ»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-za-3-dnya-do-ddu-sverili-mashinomesto-v-deklaracii-ne-okazalos-nomera",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
