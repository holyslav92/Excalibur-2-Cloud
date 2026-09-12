# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В ДДУ в Тюмени указали 4,2 млн — на эскроу был ноль
- hook (cover-text): «Эскроу пуст, хотя деньги указали» (highlight: «пуст»)
- sticky: «Сначала проверьте счёт»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: в проекте ДДУ указано 4,2 млн на эскроу, но за 7 дней до подписания банк видит ноль; первый перевод ушёл застройщику по обещанию «зачтём в эскроу»; сделку остановили, предложили платить повторно

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4583
- «эскроу счет» — 863
- «счет эскроу дду» — 27

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: disappointed_black_guy
- inline_5: this_is_fine_dog
- inline_7: pepe_frog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B23: blue shirt mustard sweater handover room EGRN keys (full-body right)
- B22: lemon-yellow shirt bank mortgage desk disaster_girl (full-body center)
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank mortgage desk duplicate / NOT handover room / NOT MFC; NEW location (bright escrow verification counter at newbuild sales office with printed bank statement showing zero vs DDU draft).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Финал: сделку остановили, предложили платить второй раз (pair with inline_2)
Labels: Новостройка в Тюмени | Договор — 4,2 млн | Первый взнос | Эскроу — ноль | Одобрение не равно деньгам
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Перевод не на эскроу | Обещание менеджера | Статья 15.5 | Бронь не равна цене | Нужен письменный зачёт
NO meme

### inline_3 — realistic_photo — В проекте ДДУ — 4,2 млн, а на эскроу пусто
Labels: Бронь — услуга | Аванс не эскроу | Цена в договоре | Зачёт письменно | Устное не считается
NO meme — bright DDU draft page with 4.2M line next to empty escrow balance printout

### inline_4 — realistic_photo — «Мы зачтём в эскроу» — и перевод на реквизиты застройщика
Labels: Проверка банка | За 7 дней | Остаток — ноль | Переписка не пополнение | Одобрение не эскроу
NO meme — payment receipt to developer requisites vs escrow account details side by side

### inline_5 — bar_timeline_chart — За семь дней до подписания банк увидел ноль
Labels: Повторно 4,2 млн | Риск двойной оплаты | Подпись остановили | Бронь под угрозой | Письмо о зачёте
Meme: this_is_fine_dog tiny corner

### inline_6 — process_flow — Бронь, аванс и цена ДДУ — три разных платежа
Labels: Цена и эскроу | Реквизиты счёта | Выписка банка | Регистрация договора | Первый платёж и зачёт
NO meme

### inline_7 — structure_diagram — Что сверить до подписания — таблица
Labels: Договор и кредит | Счёт эскроу | Остаток подтверждён | Росреестр и банк | Без повторной оплаты
Meme: pepe_frog tiny corner

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
