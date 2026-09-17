# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени приложение к ДДУ запретило аренду — инвестор отказался от доплаты 240 тысяч
- hook (cover-text): «В приложении к ДДУ запретили сдавать квартиру» (highlight: «запретили»)
- sticky: «Бронь сгорела»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: инвестор покупал студию под сдачу; менеджер обещал свободное использование; на 14-й странице приложения №3 — запрет аренды до регистрации дома; за 2 дня до банка отказ от ДДУ; альтернативный лот +240 тыс.; эскроу не открывали

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить новостройку в тюмени» — 928
- «квартира в тюмени купить новостройки» — 665
- «студия в тюмени купить в новостройках» — 106

## meme_picks (from cover-text.json)

- cover: james_doakes, doge
- inline_1: wojak
- inline_5: this_is_fine_dog
- inline_7: disappointed_black_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось в последних обложках.

**Recent covers to differ from:**
- B26: olive vest bank desk hide_pain_harold (waist-up right)
- B25: terracotta shirt kneeling empty apartment confused_math_lady
- B23: light blue shirt mustard sweater handover room side_eye_chloe
- B22: lemon yellow shirt bank full-body center disaster_girl

**Required:** light/bright #FFF high-key, sun flare; james_doakes + doge small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright sales office lounge with laptop showing DDU appendix page 14 rental ban, not bank/MFC/handover duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Бронь и ипотека — аренда в расчёте (pair with inline_2)
Labels: Студия под сдачу | Бронь оформлена | Предварительное одобрение | Аренда в расчёте
Meme: wojak tiny corner

### inline_2 — process_flow — pair with inline_1
Labels: Страница 14 | Приложение №3 | До регистрации дома | Согласие УК
NO meme — flow diagram бронь → ипотека → аренда в модели

### inline_3 — realistic_photo — Запрет на 14-й странице приложения №3
Labels: Два дня до банка | Договор не подписан | Эскроу не открывали | Деньги не переводили
NO meme — bright close-up PDF appendix page with rental restriction highlighted

### inline_4 — realistic_photo — Два дня до банка, эскроу не открывали
Labels: Другой лот | Без ограничения | Доплата двести сорок | Новый расчёт
NO meme — bright desk with two floor plans and price delta sticker

### inline_5 — comparison_table — Устное обещание vs текст приложения
Labels: Менеджер обещал | Текст приложения | Формулировка решает | Не устное обещание
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — Инвестор не подписал ДДУ
Labels: Договор не подписан | Бронь сгорела | Эскроу не открывали | Отказ до банка
NO meme — timeline stops before escrow

### inline_7 — structure_diagram — Таблица до подписи vs после регистрации
Labels: До подписи отказ | После регистрации спор | Договор бронирования | Полный проект
Meme: disappointed_black_guy tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    "inline_2": { "scene_hint", "alt" },
    "inline_3": { "scene_hint", "alt" },
    "inline_4": { "scene_hint", "alt" },
    "inline_5": { "scene_hint", "alt", "meme_picks" },
    "inline_6": { "scene_hint", "alt" },
    "inline_7": { "scene_hint", "alt", "meme_picks" }
  }
}
```
