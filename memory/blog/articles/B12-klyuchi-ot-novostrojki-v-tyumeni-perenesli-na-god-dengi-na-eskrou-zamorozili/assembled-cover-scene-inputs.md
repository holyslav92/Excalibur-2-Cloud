# Cover-scene inputs — B12

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B12
- tenant: The Риэлтор, Тюмень
- H1: Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась
- hook (cover-text): «Застройщик перенёс ключи — платёж идёт» (highlight: «перенёс»)
- sticky: «Год без квартиры»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: за три недели до ключей письмо о переносе на 12 месяцев; деньги на эскроу нельзя снять; ипотечный платёж продолжается; письмо ≠ автоматический выход

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4717
- «эскроу счет новостройка» — 344
- «ипотека новостройка тюмень» — 214

## meme_picks (from cover-text.json)

- cover: roll_safe, crying_cat
- inline_1: bad_luck_brian
- inline_5: blinking_white_guy
- inline_7: disappointed_black_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B10: sage cardigan left, elderly phone viewing
- B06: lemon yellow shirt medium right window
- B05: terracotta sweater right entrance steps

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NO keys-as-default-prop cliché unless fresh twist.

## Anti-repeat used-motifs (14d) — avoid collision

B10 apartment viewing phone; B06 panoramic window price chart; B05 entrance discount tag.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — bar_timeline_chart — «Три недели до ключей — и срок отодвигают на год»
Labels: За 3 недели | Перенос на 12 месяцев | Письмо вежливое | Допсоглашение в приложении | ДДУ по старой дате
Meme: bad_luck_brian tiny corner

### inline_2 — comparison_table_ui — «Деньги на эскроу: защита есть, свободного выхода нет»
Labels: Деньги на эскроу | Снять нельзя просто так | Возврат после расторжения | Уведомление не основание | Кнопки «верните» нет
NO meme

### inline_3 — workflow_diagram — «Ипотека не ждёт: платёж идёт, квартиры ещё нет»
Labels: Платёж каждый месяц | Квартиры ещё нет | Двойная нагрузка | Аренда плюс ипотека | Год — это сумма
NO meme

### inline_4 — checklist_board — «Финал: претензия, расторжение и возврат цены ДДУ»
Labels: Письменная претензия | Расторжение по соглашению | Прекращение ДДУ в ЕГРН | Без записи в ЕГРН | Эскроу не двигается
NO meme

### inline_5 — schema_faq_ui — «Срок ввода дома и срок передачи квартиры — не одно и то же»
Labels: Ввод третий квартал 2026 | Ключи до 31 декабря | Две строки в декларации | Срок из вашего ДДУ | Декларация не меняет ДДУ
Meme: blinking_white_guy tiny corner

### inline_6 — tool_screenshot — «Когда письмо о переносе ещё не даёт односторонний отказ»
Labels: Просрочка больше 2 месяцев | До даты отказа нет | Уведомление раньше права | Переговоры или ждать | Допсоглашение не спешите
NO meme

### inline_7 — infographic_card — «Неустойка в 2026: мораторий закончился, отсрочка — отдельная история»
Labels: Мораторий до 31.12.2025 | С 2026 по ставке | Двойной размер гражданину | От даты в ДДУ | Банк-эскроу не платит
Meme: disappointed_black_guy tiny corner

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «перенёс», ONE yellow sticky only, ZERO Wordstat strips on canvas.
