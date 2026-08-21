# Cover-scene inputs — B08

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B08
- tenant: The Риэлтор, Тюмень
- H1: Квартиру в Тюмени ищут четвёртый месяц. Уже согласны на риск
- hook (cover-text): «Четвёртый месяц — проверьте квартиру» (highlight: «проверьте»)
- sticky: «Усталость не повод рисковать»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья 3–4 месяца ищет вторичку, «согласны на риск» vs «сделайте безопасно»; проверка ЕГРН до аванса; усталость меняет критерии

## Wordstat stickers (manifest log ONLY — FORBIDDEN on cover canvas)

- «купить квартиру в тюмени» — 22990
- «вторичка в тюмени» — 5813
- «купить квартиру в тюмени вторичка» — 3965

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B06: lemon yellow shirt, panoramic window, host medium right, 18→20 price jump
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04: black blazer left bust side-eye investigation board
- B03: black blazer left bust jaw-drop board

**Required:** light/bright #FFF high-key, sun flare; meme cat + catalog people-meme small stickers; NO dark cinematic; NO daypart formula; **NO Wordstat query strips/bars on canvas** (owner ban forever).

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon shirt panoramic window right.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — labeled_checklist — «Коротко: четвёртый месяц поиска»
Labels: 17,8 тыс. объявлений | 3–4 месяца поиска | Документы не компромисс | Риск станет видимым | Заключение до аванса
Meme sticker: yes (small tired cat corner)

### inline_2 — comparison_table_ui — «Парадox рынка»
Labels: 17,8 тыс. объявлений | Минус 4% за год | 113 дней вместо 150 | Однушка около 5 млн | Ипотека: плюс 271%
NO meme

### inline_3 — workflow_diagram — «Как усталость меняет критерии»
Labels: Первый месяц: район | Четвёртый: хоть эту | Ремонт можно менять | Документы не исправить | Аванс сегодня — давление
NO meme

### inline_4 — process_flow — «Безопасная сделка vs осознанный риск»
Labels: Проверка не обнуляет | Всё чисто не бывает | Знайте цену риска | Риск до аванса | Заключение на бумаге
NO meme

### inline_5 — structure_diagram — «Что проверяют в ЕГРН»
Labels: Собственник сейчас | Обременения и запреты | История переходов права | Основание регистрации | Срок владения продавца
Meme sticker: yes (small serious cat corner)

### inline_6 — checklist_board — «Типовые юридические сигналы»
Labels: Продажа по доверенности | Право перешло недавно | Переходы за год | Супруг не в сделке | Дети не учтены
NO meme

### inline_7 — schema_faq_ui — «Главный чеклист: риски до аванса»
Labels: Свежая выписка ЕГРН | Все собственники участвуют | Обременения понятны | Расчёт через аккредитив | Заключение до аванса
Meme sticker: yes (small roll_safe corner)

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, pink highlight «проверьте», ZERO Wordstat on canvas.
