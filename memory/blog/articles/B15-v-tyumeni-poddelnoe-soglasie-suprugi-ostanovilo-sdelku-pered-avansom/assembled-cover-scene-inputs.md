# Cover-scene inputs — B15

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B15
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени не подтвердили согласие супруги — аванс остановили
- hook (cover-text): «Проверка согласия супруги остановила аванс» (highlight: «остановила»)
- sticky: «Конверт не доказательство»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: ипотека одобрена, выписка «чистая», согласие в конверте — подлинность не подтвердили перед авансом; банк и риэлтор остановили перевод

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «нотариальное согласие супруга» — 138
- «согласие супруга на продажу квартиры» — 54
- «нужно ли согласие супруга на продажу квартиры» — 20

## meme_picks (from cover-text.json)

- cover: blinking_white_guy, polite_cat
- inline_1: two_buttons
- inline_5: disappointed_black_guy
- inline_7: sacrednik_priest

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B12: light blue shirt showroom waist right
- B10: sage cardigan left elderly phone viewing
- B06: lemon yellow shirt medium right window
- B14: sage green cardigan kitchen comparing documents

**Required:** light/bright #FFF high-key, sun flare; blinking_white_guy people-meme + polite_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula.

## Anti-repeat used-motifs (14d) — avoid collision

B12 showroom letter payment; B10 apartment viewing phone; B06 panoramic window price chart.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Почему «чистая» выписка ЕГРН не закрывает вопрос супруга»
Labels: Ипотека одобрена | Выписка чистая | Согласие в конверте | Аванс сегодня | Банк подпись не проверил
Meme: two_buttons tiny corner
Pair with inline_2 on same H2

### inline_2 — structure_diagram — pair with inline_1
Labels: Один в выписке | Права у двоих | Статья 34 — брак | Статья 35 — согласие | Реестр не про брак
NO meme

### inline_3 — realistic_photo — «В Тюмени деньги к авансу уже стояли — в конверте лежало согласие»
Labels: ЕГРН — титул | Не режим имущества | Брачный договор отдельно | Документы-основания | Один ≠ нет второго
NO meme — MFC/bank desk envelope scene

### inline_4 — realistic_photo — «Подлинность не подтвердили: перевод остановили на пороге»
Labels: ФИО нотариуса | Регистрационный номер | Адрес объекта | Вид сделки | Подпись и печать
NO meme — notary consent document closeup

### inline_5 — comparison_table — «Что сверять в нотариальном согласии до перевода денег»
Labels: Совместная собственность | Реквизиты согласия | Совпадение со сделкой | Проверка через ФНП | Возврат при отказе
Meme: disappointed_black_guy tiny corner

### inline_6 — labeled_checklist — «Отсутствие согласия, подделка и отзыв — разные риски»
Labels: Реестр нотариата | Реестровый номер | Нотариальная тайна | Сервис не оценит режим | Запрос от продавца
NO meme

### inline_7 — process_flow — «До аванса: таблица проверок и условия возврата»
Labels: Деньги не ушли | Продавец ищет новое | Сделка рассыпалась | Бумага — не факт | Проверка до аванса
Meme: sacrednik_priest tiny corner

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «остановила», ONE yellow sticky only, ZERO Wordstat strips on canvas.
