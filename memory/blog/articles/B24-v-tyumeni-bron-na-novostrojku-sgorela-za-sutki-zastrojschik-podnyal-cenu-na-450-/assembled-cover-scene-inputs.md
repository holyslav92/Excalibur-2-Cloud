# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч
- hook (cover-text): «Застройщик поднял цену — бронь сгорела» (highlight: «сгорела»)
- sticky: «Бронь не равна ДДУ»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: платная бронь 48 часов, ипотека одобрена, за сутки до дедлайна +450 000 ₽, бронь сняли, 50 000 ₽ удержали как услугу, ДДУ и эскроу не открыли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4642
- «купить новостройку в тюмени» — 885
- «бронь новостройки» — 288 (RU compare)

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: james_doakes
- inline_5: this_is_fine_dog
- inline_7: stonks

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt handover room full-body right DDU vs EGRN
- B22: yellow shirt bank mortgage desk disaster_girl full-body center
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + long_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright newbuild sales pavilion with digital countdown timer and price board, NOT bank/MFC/handover).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотеку одобрили» — и семья забронировала новостройку (pair with inline_2)
Labels: Ипотека одобрена | Бронь 50 тысяч | Планировка выбрана | ДДУ ещё нет | Цену не фиксирует
Meme: james_doakes tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Срок 48 часов | Цена заморожена | Таймер тикает | Пятница вечер | Не эскроу
NO meme — compare бронь vs ДДУ vs эскроу columns

### inline_3 — realistic_photo — Сорок восемь часов: цена «заморожена», пока тикает таймер
Labels: Оферта брони | Скидка в условиях | Способ оплаты | Календарь риск | Два дня мало
NO meme — bright office wall clock + 48h countdown card

### inline_4 — realistic_photo — За сутки до дедлайна застройщик поднял цену на 450 тысяч
Labels: Плюс 450 тысяч | За сутки до конца | Ставка не менялась | Лот подорожал | Переписка с менеджером
NO meme — smartphone chat screenshot + price tag +450000 on bright desk

### inline_5 — process_flow — Доплаты не хватило — бронь сняли, лот ушёл другим
Labels: Доплаты нет | Бронь сняли | Лот другим | 48 часов кончились | Эскроу не открыли
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — Пятьдесят тысяч удержали — ДДУ так и не подписали
Labels: 50 тысяч удержали | Услуга брони | Не аванс | ДДУ не подписан | Возврата нет
NO meme — timeline бронь→услуга→удержание

### inline_7 — structure_diagram — Что проверить в оферте бронирования — таблица
Labels: Объект в оферте | Цена без условий | Дата и время | Аванс или услуга | Возврат прописан
Meme: stonks tiny corner

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
