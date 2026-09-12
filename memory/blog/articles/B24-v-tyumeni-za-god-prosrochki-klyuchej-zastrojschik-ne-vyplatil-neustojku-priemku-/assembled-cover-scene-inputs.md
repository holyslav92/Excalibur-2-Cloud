# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик год не платил неустойку — семья остановила приёмку
- hook (cover-text): «Застройщик год тянул — деньги не отдал» (highlight: «деньги»)
- sticky: «Акт без денег?»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: год просрочки → звонок на приёмку без выплаты неустойки → акт без претензий vs зачёт в отделку → письменная претензия вместо подписи

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «неустойка за просрочку застройщика» — 1036
- «взыскание неустойки с застройщика за просрочку» — 218
- «акт приемки квартиры в новостройке» — 9 (Тюмень)

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: wojak
- inline_5: this_is_fine_dog
- inline_7: disappointed_black_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room EGRN vs DDU full-body right
- B22: lemon yellow shirt bank mortgage desk full-body center
- B20: terracotta overshirt MFC corridor
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + long_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location — bright temporary acceptance desk in finished newbuild lobby with wall calendar crossed 365 days, unsigned act with empty payout column, keys pushed aside, calculator showing ~546k.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Год просрочки — и звонят на приёмку без денег (pair with inline_2)
Labels: Год без ключей | Звонок на приёмку | Неустойку не выплатили | Зачёт в отделку | Акт без претензий
Meme: wojak tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Мораторий до декабря | Начисление с 2026 | 1/150 ставки | 90 дней просрочки | Около 546 тысяч ₽
NO meme — moratorium vs payable days table

### inline_3 — realistic_photo — Счёт непростой: мораторий съел полгода
Labels: Акт без претензий | Отделка вместо денег | Неустойка не ремонт | Смета на бумаге | «Потом» не дата
NO meme — acceptance room table with renovation brochure vs cash payout column

### inline_4 — realistic_photo — «Выплатим потом» и зачёт в отделку
Labels: Акт не подписали | Расчёт в претензии | Заказное с описью | Ответ 10–30 дней | Односторонний акт риск
NO meme — post office counter registered letter with claim calculation

### inline_5 — process_flow — Финал: акт не подписали, претензию отправили
Labels: ДДУ и уведомление | Расчёт неустойки | Претензия и отправка | Перечень работ | Юрлицо в договоре
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — Что зафиксировать до подписи акта
Labels: Ипотека не ждёт | Эскроу не выключатель | Регистрация с марта | 31,9 тысячи Росреестру | Банк не платит
NO meme

### inline_7 — structure_diagram — Ипотека и эскроу не ждут спора
Labels: Письменный расчёт | Не устное «потом» | Основа для действий | До акта время | Ключи отдельно
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
    ...
  }
}
```
