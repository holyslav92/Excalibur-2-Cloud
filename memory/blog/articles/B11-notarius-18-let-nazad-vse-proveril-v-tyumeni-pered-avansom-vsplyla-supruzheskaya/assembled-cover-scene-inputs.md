# Cover-scene inputs — B11

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B11
- tenant: The Риэлтор, Тюмень
- H1: Нотариус не выделил супружескую долю — аванс остановили
- hook (cover-text): «Сделку остановили из-за наследников» (highlight: «остановили»)
- sticky: «Проверка не закончена»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- meme_picks cover: blinking_white_guy + polite_cat (from cover-text.json)
- meme_picks inline: inline_1 disappointed_black_guy; inline_5 crying_cat; inline_7 sacrednik_priest
- angle: кооперативная квартира, пай доплачивали в браке, нотариус 18 лет назад «всё проверил», супружеская доля не выделена, наследники неясны, аванс остановили

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить квартиру в тюмени»
- «нотариус при покупке квартиры»
- «наследство квартира продажа»

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B10: sage olive cardigan, host left, elderly seller phone viewing
- B06: lemon yellow shirt, host right, price jump 18→20
- B05: terracotta sweater grey overcoat, host right entrance

**Required:** light/bright #FFF high-key, sun flare; blinking_white_guy + polite_cat small stickers; NO dark cinematic; NO daypart formula; NO Wordstat query strips/bars on canvas.

## Anti-repeat used-motifs (14d) — avoid collision

B10 sage cardigan left elderly phone; B06 lemon shirt right price; B05 terracotta right entrance; B04 black blazer side-eye board.

## Inline slots (scene_hint + alt; labels from cover-text; NO host face on inline)

### inline_1 — comparison_table — «Справка о выплаченном пае — и нотариальный штамп 18 лет назад»
Labels: Справка о пае | Пай закрыт целиком | Нотариус 18 лет назад | «Всё проверил» | Кем и когда платили
Meme: disappointed_black_guy tiny corner

### inline_2 — process_flow — «Кооператив, пай и брак: где прячется супружеская доля»
Labels: Обмен и кооператив | Доплата пая в браке | Статья 34 СК РФ | Доля не выделена | Статья 1150 ГК
NO meme

### inline_3 — labeled_checklist — «Нотариус отказала отвечать — и через 15 минут согласилась переоформить»
Labels: Запросили долю | Запросили наследство | Первый отказ нотариуса | Через 15 минут | Переоформили за 3–4 дня | Справку не дали
NO meme

### inline_4 — comparison_table — «Финал: аванс остановили, пока не разобрались с наследниками»
Labels: Доля на бумаге | Наследники неясны | Ребёнок от первого брака | Родители умершего | Деньги не передали
NO meme

### inline_5 — structure_diagram — «Почему «нотариус всё проверил» не закрывает цепочку»
Labels: Работа с заявленным | Доплата не заявлена | Долю переоформили | Не полная проверка | Справка о пае молчит
Meme: crying_cat tiny corner

### inline_6 — bar_timeline_chart — «Срок давности: три года — но не всегда «с 18-летней давности»»
Labels: Статья 196 ГК | Узнал о нарушении | Статья 200 ГК | 18 лет не гарантия | Доля в наследстве
NO meme

### inline_7 — labeled_checklist — «Что проверить до аванса: доля, наследство и документы»
Labels: Хронология пая | Статус второго супруга | Список наследников | Развести документы | Сначала бумаги, потом деньги
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
    "cover": { "scene_hint": "...", "alt": "...", "cover_emotion": "..." },
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

scene_hint cover: 80–140 chars, named emotion, light/bright, phone CTA, pink highlight «остановили», ZERO Wordstat on canvas.
