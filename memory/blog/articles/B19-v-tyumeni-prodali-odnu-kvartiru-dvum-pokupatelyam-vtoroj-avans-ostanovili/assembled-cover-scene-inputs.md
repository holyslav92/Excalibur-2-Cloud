# Cover-scene inputs — B19

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B19
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени квартиру продали дважды — второй аванс остановили
- hook (cover-text): «В Тюмени одну квартиру продали дважды» (highlight: «дважды»)
- sticky: «Второй аванс остановили»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: двойная продажа одной квартиры на вторичке; первый аванс лежит, показы второй паре; второй покупатель запросил ЕГРН — сделку остановили до регистрации; контраст с ялуторовским casus (оба заплатили)

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «продал квартиру двум покупателям аванс» — 135
- «продал квартиру двум покупателям» — 3 (Tyumen 11176)
- «двойная продажа квартиры» — weak Tyumen (buyer spine)

## meme_picks (from cover-text.json)

- cover: blinking_white_guy, polite_cat
- inline_1: two_buttons
- inline_5: disappointed_black_guy
- inline_7: sacrednik_priest

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B15: white shirt sand vest envelope center waist
- B12: light blue shirt showroom waist right
- B10: sage cardigan left elderly phone viewing
- B06: lemon yellow shirt medium right window

**Required:** light/bright #FFF high-key, sun flare; blinking_white_guy people-meme + polite_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula.

## Anti-repeat used-motifs (14d) — avoid collision

B15 MFC envelope consent; B12 showroom letter payment; B10 apartment viewing phone; B06 panoramic window price chart.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Второй покупатель запросил выписку — сделку поставили на паузу»
Labels: Аванс уже лежал | Показы продолжались | Вторая пара готова | Объявление активно | Надежда на бумаге
Meme: two_buttons tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Свежая выписка ЕГРН | Запрос до денег | Данные не сходятся | Стоп до аванса | Рычаг у покупателя
NO meme

### inline_3 — realistic_photo — «В Тюмени аванс уже лежал — а квартиру показывали второй паре»
Labels: Договор не право | Запись в ЕГРН | Два покупателя | Один объект | Кто первый в реестре
NO meme — bright apartment viewing / keys on table scene

### inline_4 — realistic_photo — «Почему «я первый» не всегда спасает при двойной продаже»
Labels: Аванс возвращают | Задаток — штраф | Формулировки важны | Предварительный договор | Обеспечительный платёж
NO meme — contract documents closeup on white desk

### inline_5 — bar_timeline_chart — «Что проверить до регистрации, если объект ещё в продаже»
Labels: Фактическое владение | Практика ВС | Убытки второму | Не только дата | Регистрация решает
Meme: disappointed_black_guy tiny corner

### inline_6 — process_flow — «Аванс, задаток и предварительный договор — разные последствия»
Labels: Проверка объявления | Скрин до аванса | Письменный запрос | Эксклюзив в договоре | Роль риэлтора
NO meme

### inline_7 — structure_diagram — «До аванса: таблица сигналов и что фиксировать письменно»
Labels: Сигналы в таблице | Два-три признака | Не переводить сегодня | Расписка и реквизиты | Остановка до денег
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
  "wordstat_stickers": ["...", "...", "..."],
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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «дважды», ONE yellow sticky only, ZERO Wordstat strips on canvas.
