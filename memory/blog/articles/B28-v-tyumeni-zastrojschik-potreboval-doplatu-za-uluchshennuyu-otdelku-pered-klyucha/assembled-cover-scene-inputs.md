# Cover-scene inputs — B28

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B28
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик запросил 300 тысяч перед ключами — их нет в ДДУ
- hook (cover-text): «Перед ключами потребовали триста тысяч рублей» (highlight: «потребовали»)
- sticky: «В договоре этого нет»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: перед передачей ключей застройщик требует ~300 тыс. за «улучшенный пакет» отделки, которого нет в зарегистрированном ДДУ; устное обещание менеджера vs предчистовая в договоре

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4660
- «отделка новостройка» — 269
- «новостройки с предчистовой отделкой» — 40

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: james_doakes
- inline_5: sacrednik_priest
- inline_7: disappointed_black_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater full-body right handover room (YESTERDAY — avoid duplicate handover room)
- B22: lemon yellow shirt bank mortgage desk full-body center
- B20: terracotta overshirt MFC corridor two_buttons
- B19: turquoise polo showroom knee-up right

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT generic handover desk like B23 — invent fresh location (e.g. keys tray + invoice + DDU spec mismatch at bright developer office counter).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Ключи на столе — и счёт на триста тысяч за отделку
Labels: Дом уже сдан | Деньги на эскроу | Счёт триста тысяч | Оплата перед ключами
Meme: james_doakes tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Обещали ламинат | Обещали сантехнику | В договоре предчистовая | Устное не меняет договор
NO meme

### inline_3 — realistic_photo — На показе обещали ламинат, в ДДУ написано «предчистовая»
Labels: Триста тысяч сразу | Нет сметы | Нет приложения | Так принято у нас
NO meme — showroom brochure vs DDU spec page contrast

### inline_4 — realistic_photo — В офисе выдачи: «улучшенный пакет» без приложения к договору
Labels: Отказ платить | Письменная претензия | Квартиру приняли | Спор по документам
NO meme — developer handover counter invoice without appendix

### inline_5 — structure_diagram — Что в договоре реально определяет состав отделки — таблица
Labels: Зарегистрированный договор | Спецификация отделки | Отдельное соглашение | Буклет не заменяет договор | Проверка на дом.рф
Meme: sacrednik_priest tiny corner

### inline_6 — process_flow — Финал: претензия, отказ платить и ожидание передачи по ДДУ
Labels: Нужен перечень работ | Не перерасчёт площади | Эскроу не согласие | Проверьте пункт договора
NO meme

### inline_7 — labeled_checklist — Акт приёмки: формулировки, которые закрывают спор не в вашу пользу
Labels: Претензий не имею | С доплатой согласен | Смета до подписи | Разделите передачу и оплату | Зафиксируйте обращение
Meme: disappointed_black_guy tiny corner

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
