# Cover-scene inputs — B34

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B34
- tenant: The Риэлтор, Тюмень
- H1: За 4 дня до эскроу новостройка в Тюмени ушла в «сдам» — семейную ипотеку сняли
- hook (cover-text): «Банк отменил семейную ипотеку перед эскроу» (highlight: «ипотеку»)
- sticky: «А объявление было «сдам»»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: бронь оплачена, предодобрение семейной ипотеки; за 4 дня до эскроу на агрегаторе объявление «сдам» с той же планировкой; банк снял одобрение, эскроу не открыли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека тюмень» — 1494
- «купить новостройку в тюмени» — 900

## meme_picks (from cover-text.json)

- cover: confused_math_lady, woman_yelling_cat
- inline_1: surprised_pikachu
- inline_5: this_is_fine_dog
- inline_7: grumpy_cat

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:** B33 kitchen utility debt; B29 bank lobby 0%; B27 sales office declaration rent.

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady + woman_yelling_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «В Тюмени казалось, что новостройка уже их — бронь и семейная ипотека»
Labels: Бронь оплачена | Семейная ипотека | До эскроу 4 дня | Предодобрение банка
Meme: surprised_pikachu tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Объявление «сдам» | Тот же корпус | Та же планировка | Скрин ночью
NO meme

### inline_3 — realistic_photo — «За четыре дня до эскроу на агрегаторе всплыло «сдам» с их планировкой»
Labels: Предодобрение не кредит | Финальная проверка | Решение банка | Эскроу не открыли
NO meme — smartphone screen with rental listing blur, newbuild lobby background

### inline_4 — realistic_photo — «Предодобрение не равно кредиту: что сказал менеджер банка»
Labels: Созаёмщики в офисе | Документы на руках | Шаг до эскроу | Проверка сделки
NO meme — bright bank mortgage desk, documents stack, no faces

### inline_5 — process_flow — «Финал: одобрение сняли, эскроу не открыли, подписи не поставили»
Labels: Одобрение сняли | ДДУ не подписали | Эскроу не открыли | Сделка сорвалась
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — «Что зафиксировать по лоту и объявлению до открытия эскроу»
Labels: Скрин с датой | Письмо застройщику | Сохранить объявление | Зафиксировать время
NO meme

### inline_7 — structure_diagram — «Короткая таблица: бронь, ДДУ, декларация и карточка аренды»
Labels: Бронь | ДДУ | Декларация | Карточка аренды | Сравнить данные
Meme: grumpy_cat tiny corner

Output cover/scene-draft.json with cover_hook, cover_hook_highlight, slots.cover (scene_hint, alt, cover_emotion, cover_motifs), all inline scene_hint/alt/fact_labels.
