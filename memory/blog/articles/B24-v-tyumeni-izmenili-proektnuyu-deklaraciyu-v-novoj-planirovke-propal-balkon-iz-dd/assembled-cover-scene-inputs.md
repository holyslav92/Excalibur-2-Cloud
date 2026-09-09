# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени пропал балкон на ключах — через 2 дня банк заморозил транш
- hook (cover-text): «Застройщик убрал балкон — деньги заморозили» (highlight: «балкон»)
- sticky: «Акт пока не подписан»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: план ДДУ с балконом → застройщик обновил декларацию → на приёмке глухая стена → акт не подписан → банк заморозил транш через 2 дня

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4642
- «балкон новостройка» — 25
- «приемка квартиры в новостройке тюмень» — 30

## meme_picks (from cover-text.json)

- cover: wojak, long_cat
- inline_1: this_is_fine_dog
- inline_5: cheems
- inline_7: distracted_boyfriend

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B23: handover room light blue shirt mustard sweater full-body right
- B22: yellow shirt bank mortgage desk full-body center
- B20: terracotta overshirt MFC corridor two DDU

**Required:** light/bright #FFF high-key, sun flare; wojak people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/showroom duplicate; NEW location (bright raw apartment at key handover — blank wall where balcony should be, floor plan on folding table, declaration printout).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — На плане был застеклённый балкон — семья шла на ключи (pair with inline_2)
Labels: Новостройка по ДДУ | План с балконом | Контур и площадь | Эскроу открыт | Декларация обновлена
Meme: this_is_fine_dog tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Балкон сняли по проекту | Наш.дом.рф | Дата изменения | Не допсоглашение | Сверка с ДДУ
NO meme

### inline_3 — realistic_photo — Акт не подписали: претензия и заморозка сделки
Labels: Распечатанный план | Глухая стена | Фото и видео | Акт осмотра | Претензия застройщику
NO meme — bright acceptance wall vs DDU plan on clipboard

### inline_4 — realistic_photo — Застройщик показал обновлённую проектную декларацию
Labels: Через два дня | Транш на паузе | Акт не подписан | Эскроу не раскрыт | Ключи не выдали
NO meme — bright desk with paused mortgage letter and declaration page

### inline_5 — process_flow — На приёмке вместо балкона — глухая стена
Labels: Статья 7 214-ФЗ | Устранить или снизить цену | Коэффициент 0,3 | Акт с замечаниями | Документы сохранены
Meme: cheems tiny corner

### inline_6 — structure_diagram — Банк остановил последний ипотечный транш
Labels: Контур балкона | Площадь и цена | Проектная декларация | Реклама против ДДУ | Условия передачи
NO meme

### inline_7 — bar_timeline_chart — Что сверить до подписания ДДУ — таблица
Labels: Наш.дом.рф | Красный флаг | План в приложении | Кредитный договор | Одна строка решает
Meme: distracted_boyfriend tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    "inline_2": { "scene_hint", "alt" },
    "inline_3": { "scene_hint", "alt" },
    "inline_4": { "scene_hint", "alt" },
    "inline_5": { "scene_hint", "alt", "meme_picks" },
    "inline_6": { "scene_hint", "alt" },
    "inline_7": { "scene_hint", "alt", "meme_picks" }
  }
}
```
