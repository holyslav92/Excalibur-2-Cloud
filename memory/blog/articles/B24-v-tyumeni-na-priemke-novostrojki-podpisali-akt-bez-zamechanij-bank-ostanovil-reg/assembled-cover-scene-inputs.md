# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени банк остановил транш после приёмки без замечаний: 10 дефектов через 2 суток
- hook (cover-text): «Чистый акт поставил ипотеку на паузу» (highlight: «паузу»)
- sticky: «Потом исправим?»
- phone_cta: +7 922 001 65 05 (обязательно на обложке bottom-right)
- angle: менеджер торопит подписать акт без замечаний → через 2 суток приёмщик находит ~10 дефектов → банк ставит ипотечный транш на паузу (не Росреестр)

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «приемка квартиры в новостройке» — 122
- «приемка квартиры в новостройке тюмень» — 32
- «акт приемки передачи квартиры» — 37

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, woman_yelling_cat
- inline_1: this_is_fine_dog
- inline_5: wojak
- inline_7: expanding_brain

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B23: light blue shirt handover room side_eye_chloe full-body right
- B22: yellow shirt bank mortgage desk disaster_girl full-body center
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy + woman_yelling_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/showroom duplicate; NEW scene — bright unfinished apartment at handover with clean acceptance act vs defect list, pause stamp from bank letter.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — На приёмке менеджер просит подписать акт без замечаний (pair with inline_2)
Labels: Потом исправим | Ключи рядом | Устное обещание | Чистый акт | Замечания не внесли
Meme: this_is_fine_dog tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Около десяти недостатков | Отделка и стеклопакеты | Осмотр через двое суток | Фото с датой | Поздно, но возможно
NO meme

### inline_3 — realistic_photo — Через двое суток приёмщик находит десяток дефектов
Labels: Ипотека на паузе | Не Росреестр | Ответ банка письменно | Операция остановлена | Деньги отдельно
NO meme — bright defect inspection clipboard with dated photos

### inline_4 — realistic_photo — Банк ставит на паузу транш — и это не Росреестр
Labels: Акт без замечаний | Акт о несоответствии | Гарантия три года | Отделка один год | Три процента договора
NO meme — bank pause letter on bright desk next to mortgage folder

### inline_5 — structure_diagram — Чистый акт против акта о несоответствии
Labels: Дефектная ведомость | Свой экземпляр | Фото крупным планом | До подписи | Срок ремонта
Meme: wojak tiny corner

### inline_6 — process_flow — Что фиксировать до подписи
Labels: Акт приёма-передачи | Перечень дефектов | Письмо от банка | Не одна подпись | Специалист до акта
NO meme

### inline_7 — bar_timeline_chart — Три документа на приёмке — таблица
Labels: Акт приёма-передачи | Акт о несоответствии | Ответ банка письменно | Что не подтверждает | Разделите задачи
Meme: expanding_brain tiny corner

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
