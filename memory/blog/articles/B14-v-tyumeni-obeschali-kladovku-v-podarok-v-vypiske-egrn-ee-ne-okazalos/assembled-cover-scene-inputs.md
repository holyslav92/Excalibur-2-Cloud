# Cover-scene inputs — B14

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B14
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было
- hook (cover-text): «Кладовка остановила сделку до аванса» (highlight: «Кладовка»)
- sticky: «Словам верить нельзя»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: продавец обещал кладовку в подарок; ключи и фото клетки в подвале; за 3 дня до аванса расширенная выписка ЕГРН показала только квартиру; аванс не внесли; сделку остановили

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «выписка ЕГРН» — 4244
- «купить квартиру в тюмени вторичка» — regional
- «кладовка егрн» — 3 (WORDSTAT PARTIAL)

## meme_picks (from cover-text.json)

- cover: side_eye_chloe, cheems
- inline_1: expanding_brain
- inline_5: sacrednik_priest
- inline_7: crying_jordan

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B13: steel grey blazer left, MFC lobby, EGRN ban stamp, shocked disbelief
- B12: light blue shirt waist right, showroom delay letter
- B10: sage cardigan left, elderly phone viewing

**Required:** light/bright #FFF high-key, sun flare; side_eye_chloe people-meme + cheems small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; basement/storage cage as fresh twist OK.

## Anti-repeat used-motifs (14d) — avoid collision

B13 mfc_lobby egrn_ban; B12 showroom delay letter; B10 apartment viewing phone.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table — «Кладовку назвали подарком — и квартира выглядела выгоднее соседних»
Labels: Бонус на весах | Две квартиры | Спрос −60% | Меньше сотни в месяц | Слово без документа
Meme: expanding_brain tiny corner

### inline_2 — structure_diagram — «За три дня до аванса заказали выписку ЕГРН»
Labels: 3 дня до аванса | Расширенная выписка | Ипотека одобрена | Дата в МФЦ | Выписка — одна квартира
NO meme

### inline_3 — process_flow — «Финал: в документе только квартира, сделку остановили»
Labels: Только квартира | Нет кадастрового номера | Ключи — не право | Аванс не внесли | Есть другая запись
NO meme

### inline_4 — bar_timeline_chart — «Ключи, фотографии и привычка пользоваться — это не право»
Labels: Ключи — не документ | 10 лет пользования | Право — в реестре | Фото клетки | Бонус усиливает цену
NO meme

### inline_5 — labeled_checklist — «Когда кладовка — самостоятельный объект в ЕГРН»
Labels: Отдельный кадастровый номер | Своя выписка ЕГРН | Продавец — правообладатель | Сверка построчно | Спросите номер
Meme: sacrednik_priest tiny corner

### inline_6 — fact_card — «Подвальная клетка и общее имущество многоквартирного дома»
Labels: Подвал — общее имущество | Статья 36 ЖК РФ | Доля не отчуждается | Самовольная перегородка | Решает собрание
NO meme

### inline_7 — workflow_diagram — ««Подарок» на словах: устное обещание и дарение»
Labels: Номер кладовки | Отдельная выписка ЕГРН | Сверить правообладателя | Договор и объявление | Аванс после документов
Meme: crying_jordan tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": {
    "composition": "...",
    "location": "...",
    "meme": "...",
    "prop_set": "...",
    "sticker_set": "...",
    "joke": "...",
    "outfit": "...",
    "emotion": "...",
    "pose_framing": "...",
    "action": "..."
  },
  "slots": {
    "cover": {
      "scene_hint": "...",
      "alt": "...",
      "cover_emotion": "..."
    },
    "inline_1": { "scene_hint": "...", "alt": "..." },
    "inline_2": { "scene_hint": "...", "alt": "..." },
    "inline_3": { "scene_hint": "...", "alt": "..." },
    "inline_4": { "scene_hint": "...", "alt": "..." },
    "inline_5": { "scene_hint": "...", "alt": "..." },
    "inline_6": { "scene_hint": "...", "alt": "..." },
    "inline_7": { "scene_hint": "...", "alt": "..." }
  }
}
```

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «Кладовка», ONE yellow sticky only, ZERO Wordstat strips on canvas.
