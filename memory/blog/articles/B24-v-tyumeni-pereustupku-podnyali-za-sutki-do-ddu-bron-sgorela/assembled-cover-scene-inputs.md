# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела
- hook (cover-text): «Продавец поднял цену перед самой сделкой» (highlight: «поднял»)
- sticky: «Бронь сгорела за сутки»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: переуступка права по ДДУ дешевле витрины → неделя согласований → за сутки до регистрации цедент требует +280 000 ₽ → объяснения меняются → отказ доплатить → бронь истекла → лот другому

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «договор уступки права требования» — 85
- «переуступка новостройка» — 13
- «купить квартиру в тюмени новостройка» — demand spine

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, doge
- inline_1: side_eye_chloe
- inline_5: this_is_fine_dog
- inline_7: expanding_brain

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). Body build refs: hoodie-airpods + office-selfie (medium-slim). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo:** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B22: lemon shirt bank mortgage desk disaster_girl
- B20: terracotta overshirt MFC corridor
- B19: turquoise polo showroom
- B15: white shirt sand vest envelope center

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + doge small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright glass negotiation nook with assignment papers / developer assignment desk — NOT bank, NOT MFC, NOT showroom model duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — pair with inline_2 (Отказ доплатить H2)
Labels: Дешевле отдела продаж | Скидка 10–15% | Право требования по ДДУ | Не квартира со скидкой | Исходный договор чистый
Meme: side_eye_chloe tiny corner

### inline_2 — process_flow — pair with inline_1
Labels: Аванс цеденту отдельно | Бронь у застройщика | Бронь не эскроу | Госпошлина 350 рублей | Регистрация завтра
NO meme

### inline_3 — realistic_photo — За сутки до подачи +280k (labels from cover-text)
Labels: За сутки до подачи | Плюс 280 тысяч | Цены у застройщика выросли | Не обсуждение — цифра | Семья уже в сделке
NO meme — evening phone message on kitchen table with assignment folder

### inline_4 — realistic_photo — Неделя согласований
Labels: Вечер накануне подачи | Двести восемьдесят тысяч | Цена в договоре | Прайс не меняет цену | Полная цена в бумаге
NO meme — stack of DDU + assignment agreement on bright desk

### inline_5 — bar_timeline_chart — Три версии за день
Labels: Утром — индексация | К обеду — ошибка | Три версии за день | Срок брони свой | Без продавца не оформить
Meme: this_is_fine_dog tiny corner

### inline_6 — comparison_table — Объяснения менялись
Labels: Не доплатили | Продавец не вышел | Срок брони истёк | Лот другому покупателю | Аванс по тексту соглашения
NO meme

### inline_7 — structure_diagram — Что проверить до денег
Labels: Исходный ДДУ | Полная цена уступки | Согласие застройщика | Возврат аванса | Срок брони
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
  },
  "meme_picks": { "cover": [...], "inline_1": [...], ... }
}
```
