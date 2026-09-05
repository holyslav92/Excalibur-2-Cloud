# Cover-scene inputs — B26

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B26
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени не подписали акт с браком — застройщик выставил штраф 190 тысяч
- hook (cover-text): «Застройщик требует деньги за найденный брак» (highlight: «требует»)
- sticky: «Ключей всё ещё нет»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья на приёмке новостройки нашла кривые стены, щели, мёртвую вентиляцию → отказалась подписать передаточный акт → застройщик выставил претензию ~190 000 ₽ за «уклонение» → банк не выдал второй транш → аренда + ипотека → встречная претензия, ключей нет

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 3640
- «приемка новостройки» — 110
- «приемка квартиры в новостройке тюмень» — 20

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, long_cat
- inline_1: confused_math_lady
- inline_5: wojak
- inline_7: this_is_fine_dog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось в последних обложках.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room full-body right DDU vs EGRN (side_eye_chloe)
- B22: lemon shirt milk sweater bank mortgage desk full-body center (disaster_girl)
- B20: terracotta overshirt MFC corridor two DDU INN (two_buttons)
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT handover room duplicate; NEW location (unfinished apartment inspection with level tool / defect list / penalty claim letter).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Семья пришла на приёмку с чек-листом — и увидела брак (pair with inline_2)
Labels: Семь рабочих дней | Кривые стены | Щели в окнах | Фото дефектов
Meme: confused_math_lady tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Четырнадцать дней | Около 190 тысяч | 0,1% в день | Штрафа нет в законе
NO meme

### inline_3 — realistic_photo — Односторонний акт vs обоснованный отказ
Labels: Односторонний акт | Обоснованный отказ | Не раньше двух месяцев | Два механизма
NO meme — bright DDU clause pages on table, no people

### inline_4 — realistic_photo — Банк не выдал финальный транш — аренда и ипотека одновременно
Labels: Траншевая ипотека | Второй транш | Аренда параллельно | Два платежа
NO meme — mortgage statement + rent receipt on bright kitchen table

### inline_5 — structure_diagram — Встречная претензия вместо подписи «без претензий»
Labels: Без претензий не подписали | Встречная претензия | Дефекты зафиксированы | Ключей пока нет
Meme: wojak tiny corner

### inline_6 — process_flow — Досудебный маршрут и статья 8
Labels: Пункт про уклонение | Явка семь дней | Статья 8 часть 5 | Условие второго транша
NO meme

### inline_7 — bar_timeline_chart — Что проверить в ДДУ и на приёмке — таблица
Labels: Раздел передачи | Уведомление готовности | Кредитный договор | Читать до приёмки
Meme: this_is_fine_dog tiny corner

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
