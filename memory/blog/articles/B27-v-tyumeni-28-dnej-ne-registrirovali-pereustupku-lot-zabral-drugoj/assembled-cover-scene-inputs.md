# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени 28 дней ждали переуступку — квартиру продали другому
- hook (cover-text): «Переуступка не прошла — квартира ушла другому» (highlight: «Переуступка»)
- sticky: «Ждали четыре недели»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья подписала договор уступки и внесла бронь; 28 дней обещали регистрацию; за сутки до эскроу лот забрал другой покупатель — подпись ≠ ЕГРН ≠ эскроу

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить новостройку в тюмени» — 923 (55+11176)
- «переуступка квартиры» — 63 (55+11176)
- «новостройки тюмень» — buyer spine

## meme_picks (from cover-text.json)

- cover: sacrednik_priest, crying_cat
- inline_1: surprised_pikachu
- inline_5: capybara_indifference
- inline_7: doge

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive knit vest bank mortgage desk hide_pain_harold (waist-up right)
- B25: terracotta shirt kneeling bare apartment confused_math_lady
- B23: light blue shirt handover room side_eye_chloe full-body
- B22: lemon shirt bank mortgage disaster_girl full-body center

**Required:** light/bright #FFF high-key, sun flare; sacrednik_priest people-meme + crying_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright developer sales office with floor-plan wall and assignment contract stack, NOT bank/MFC/handover/bare apartment).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Переуступку подписали в офисе — а в выписке ЕГРН по-прежнему первый дольщик» (pair with inline_2)
Labels: Договор уступки | Выписка ЕГРН | Первый дольщик | Бронь отдельно | Подпись не регистрация
Meme: surprised_pikachu tiny corner

### inline_2 — structure_diagram — pair with inline_1
Labels: Письменное согласие | Условие в ДДУ | Четыре недели | Пакет не подан | Дата эскроу
NO meme

### inline_3 — realistic_photo — «Бронь внесли, регистрацию не подали: 28 дней между словами и Росреестром»
Labels: 28 дней ожидания | Нет номера заявления | Росреестр не принял | Опись не показали | Бронь оплачена
NO meme — bright MFC reception desk with empty receipt tray and calendar showing 28 days

### inline_4 — realistic_photo — три статуса одной квартиры (pair context)
Labels: Первый дольщик | Покупатель вместе | Согласие получено | Опись с номером | Не оформляем
NO meme — bright office desk with three status cards: бронь / уступка / эскроу

### inline_5 — comparison_table — «Согласие застройщика будет на этой неделе» — и четыре недели тишины
Labels: Звонок менеджера | Сутки до эскроу | Лот у другого | Статья 15.5 | Нет записи ЕГРН
Meme: capybara_indifference tiny corner

### inline_6 — process_flow — «За сутки до открытия эскроу менеджер звонит: лот уже у другого покупателя»
Labels: Эскроу не открыли | Частичный возврат | Претензия по уступке | Лот ушёл | Цена выросла
NO meme

### inline_7 — bar_timeline_chart — «Эскроу не открыли, бронь вернули частично — лот ушёл»
Labels: Три статуса | Бронь не ДДУ | Уступка в ЕГРН | Эскроу после регистрации | Три вопроса до брони
Meme: doge tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    ...
  }
}
```
