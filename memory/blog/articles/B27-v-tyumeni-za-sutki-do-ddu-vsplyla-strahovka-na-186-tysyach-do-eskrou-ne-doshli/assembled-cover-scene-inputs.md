# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч — до эскроу не дошли
- hook (cover-text): «Застройщик добавил страховку перед ДДУ» (highlight: «страховку»)
- sticky: «186 тысяч внезапно»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: бронь + одобрение → за 24 часа до ДДУ допсоглашение со страховым пакетом 186 000 ₽ → суммы не было в расчёте → партнёр застройщика → семья отказалась → эскроу не открыли → бронь сгорела через 48 часов

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4802
- «страхование ипотеки тюмень» — 29
- «дду тюмень» — 19

## meme_picks (from cover-text.json)

- cover: this_is_fine_dog, woman_yelling_cat
- inline_1: success_kid
- inline_5: doge
- inline_7: stonks

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold tranche denied
- B25: terracotta shirt kneeling bare walls tape measure
- B23: light blue shirt mustard sweater handover room
- B22: lemon shirt mortgage desk disaster_girl rate letter

**Required:** light/bright #FFF high-key, sun flare; this_is_fine_dog + woman_yelling_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright developer sales lounge / signing room with insurance addendum stack, NOT bank desk duplicate B22/B26).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотеку одобрили» — и семья забронировала новостройку (pair with inline_2)
Labels: Новостройка | Бронь оплачена | Банк одобрил | Страховки нет | Расходы не учтены
Meme: success_kid tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: ДДУ завтра | Эскроу после ДДУ | Сообщение вечером | Пакет 186 тысяч | Времени почти нет
NO meme

### inline_3 — realistic_photo — Между бронью и ДДУ оставались сутки
Labels: Файл в мессенджере | Сообщение вечером | До визита сутки | Партнёр застройщика | Без этого нельзя
NO meme — evening phone notification PDF addendum on kitchen table bright window

### inline_4 — realistic_photo — В чате всплыло допсоглашение на 186 тысяч
Labels: 186 тысяч вне расчёта | Считать заново | Спросить банк письменно | Ставка без полиса | Проверить страховую
NO meme — smartphone chat bubble with insurance PDF 186k highlighted

### inline_5 — process_flow — Страховой пакет не был в ипотечном расчёте
Labels: ДДУ не подписали | Эскроу не открыли | Бронь 48 часов | Деньги не ушли | Бронь сгорела
Meme: doge tiny corner

### inline_6 — bar_timeline_chart — Семья остановилась: эскроу не открыли, бронь сгорела
Labels: Все расходы | Бронь и платёж | Страхование жизни | Имущественный полис | ДДУ и эскроу
NO meme

### inline_7 — structure_diagram — Что проверить до подписания ДДУ — таблица
Labels: Позиция банка письменно | Сравнить варианты | Обновить расчёт | Сохранить сообщение | Остановить сделку
Meme: stonks tiny corner

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
