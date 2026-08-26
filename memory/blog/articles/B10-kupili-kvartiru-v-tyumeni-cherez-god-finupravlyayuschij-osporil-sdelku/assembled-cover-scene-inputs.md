# Cover-scene inputs — B10

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B10
- tenant: The Риэлтор, Тюмень
- H1: Купили квартиру в Тюмени — через год финуправляющий оспорил сделку
- hook (cover-text): «Суд забрал квартиру через год после покупки» (highlight: «забрал»)
- sticky: «Долги нашли позже»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: чистая выписка ЕГРН не спасает от оспаривания при банкротстве продавца; год жили спокойно — суд отменил регистрацию

## Wordstat stickers (manifest log only — NEVER paint query strips on cover)

- «купить квартиру в тюмени» — 22652
- «купить квартиру в тюмени вторичка» — 3968
- «банкротство продавца квартиры» — 2075

## Meme picks (from cover-text.json)

- cover: hide_pain_harold + smudge_cat
- inline_1: bad_luck_brian
- inline_5: crying_cat
- inline_7: roll_safe

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo:** чёрный пиджак + бюст слева + боковой взгляд (B03/B04); terracotta sweater (B05/B09); navy/charcoal blazer (B01/B02).

**Required:** light/bright #FFF high-key, sun flare; meme people+cats small stickers; NO Wordstat query strips/bars on cover; NO dark cinematic; NO daypart formula.

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon yellow linen apartment window.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — process_flow — «Чистая выписка ЕГРН в день сделки»
Labels: Выписка на дату | Арест виден | Долги не видны | Банкротства ещё нет | Риэлтор ищет долги
Meme: bad_luck_brian tiny corner

### inline_2 — comparison_table — «Кейс в Тюмени: год жили спокойно»
Labels: Двушка на вторичке | Цена ниже рынка | Часть — наличными | Год жили спокойно | Продавец банкрот
NO meme

### inline_3 — comparison_table_ui — «Один год и три года»
Labels: Один год назад | До трёх лет | От даты заявления | Цена неравноценна | Вред кредиторам
NO meme

### inline_4 — workflow_diagram — «Что суд оценивает»
Labels: Цена не отдельно | Суд смотрит контекст | Авито и Домклик | Расчёт через ячейку | Наличные без следа
NO meme

### inline_5 — bar_timeline_chart — «Финал: суд отменил регистрацию»
Labels: Договор недействителен | Квартира в массу | Деньги в очередь | Запись ЕГРН отменена | Обзор ВС № 12/2026
Meme: crying_cat tiny corner

### inline_6 — checklist_board — «Что проверить до аванса»
Labels: Федресурс до аванса | ФССП с датой | Обосновать цену | Расчёт документально | Заверения в договоре
NO meme

### inline_7 — structure_diagram — «Федресурс, арбитраж и ФССП»
Labels: ЕГРН — про объект | Картотека арбитража | Банк данных ФССП | Проверить дважды | Наличные — худший вариант
Meme: roll_safe tiny corner

## JSON schema (обязательные поля)

Return JSON with: cover_emotion, cover_motifs (composition, location, meme, prop_set, sticker_set, joke, outfit, emotion, pose_framing, action), wordstat_stickers, slots.cover (scene_hint, alt, cover_emotion), slots.inline_1..7 (scene_hint, alt).
