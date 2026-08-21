# Cover-scene inputs — B06

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B06
- tenant: The Риэлтор, Тюмень
- H1: Автооценка занизила цену — и квартира подорожала за сутки
- hook (cover-text): «Квартира подорожала после оценки» (highlight: «подорожала»)
- sticky: «Цена оказалась ниже спроса»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: автооценка ЦИАН/Домклик показала ~18 млн, живой спрос ~20 млн; 2000 просмотров, 10 записей, 7 авансов; продавец снял и поднял цену

## Wordstat stickers (PIL overlay x≥0.68, NOT on title)

- «вторичка в тюмени» — 5799
- «купить квартиру в тюмени» — 23066

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04: black blazer left bust side-eye investigation board
- B03: black blazer left bust jaw-drop board

**Required:** light/bright #FFF high-key, sun flare; meme cat + catalog people-meme small stickers; NO dark cinematic; NO daypart formula; NO Wordstat on canvas (PIL later).

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table — «Коротко: что нужно понять про автооценку»
Labels: Ориентир не сделка | Очередь не видна | Звонки до аванса | Три варианта цены
Meme sticker: yes (small cat corner)

### inline_2 — process_flow — «Дёшево в сервисе» vs «можно купить»
Labels: Похожие квартиры | Эту квартиру купят | Очередь не учтена | Цифра не гарантия
NO meme

### inline_3 — labeled_checklist — ЦИАН.Оценка и Домклик
Labels: ЦИАН ищет похожие | Домклик: три месяца | Очередь не видна | Документы не проверяет | Мало дорогих аналогов
NO meme

### inline_4 — process_flow — Кейс 18 vs 20 млн
Labels: 18 против 20 миллионов | Разница 2 миллиона | 2000 просмотров в сутки | 10 записей на показ | 7 авансов | Седьмой в очереди
NO meme

### inline_5 — structure_diagram — Три версии низкой цены
Labels: Спрос выше оценки | Скидка за риск | Модель отстала | Плохие аналоги | Три разных действия
Meme sticker: yes (small stonks or confused_math_lady corner)

### inline_6 — comparison_table — Очередь на просмотр
Labels: Очередь значит дешевле | Показы не сделка | Сначала проверка | Не вносите сразу
NO meme

### inline_7 — fact_card — Аналоги и звонки
Labels: 5–7 похожих квартир | История цены важнее | Звонки всем продавцам | Кто подписывает сделку | До аванса спросите
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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, pink highlight «подорожала», ZERO Wordstat on canvas.
