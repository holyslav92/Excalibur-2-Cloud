# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ДДУ расторгли из-за пяти дней просрочки — удержали 180 тысяч
- hook (cover-text): «Застройщик удержал взнос за пять дней» (highlight: «удержал»)
- sticky: «Пять дней — не шутка»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: рассрочка по ДДУ, платёж +5 дней, уведомление о расторжении, удержание 180 тыс., претензия, досудебный спор, ~3 недели до сдачи

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4670
- «купить новостройку в тюмени» — 870
- «рассрочка новостройка тюмень» — 12

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: disappointed_black_guy
- inline_5: this_is_fine_dog
- inline_7: wojak

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B23: handover room, light blue shirt mustard sweater, full-body right, side_eye_chloe
- B22: bank mortgage desk, yellow shirt, full-body center, disaster_girl
- B20: MFC corridor terracotta overshirt, two_buttons
- B19: showroom turquoise polo knee-up

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/showroom/handover duplicate; NEW location (bright home kitchen table with DDU stack, wall calendar +5 days marked, red termination notice, bank receipt).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Квартиру снова выставили: претензия и досудебный спор (pair with inline_2)
Labels: ДДУ зарегистрирован | Пять дней просрочки | График рассрочки | Уведомление о расторжении | Выписка и поручение
Meme: disappointed_black_guy tiny corner — bright developer sales office window with «квартира в продаже» card on desk, no people faces

### inline_2 — comparison_table — pair with inline_1
Labels: Первый взнос внесён | Неустойка в уведомлении | Сто восемьдесят тысяч | Расчёт пени нужен | Эскроу отдельно
NO meme — gold torn-paper table: column «удержано 180 тыс» vs «пеня 1/300 от просрочки»

### inline_3 — realistic_photo — Пять дней задержки — уведомление о расторжении
Labels: Претензия покупателей | Квартира в продаже | Ключи не передали | Досудебный спор | Три недели до сдачи
NO meme — bright kitchen table with registered DDU, calendar +5, red termination envelope, no faces

### inline_4 — realistic_photo — Застройщик удержал 180 тысяч: график рассрочки
Labels: Три нарушения за год | Два месяца просрочки | Пять дней — мало | Предупреждение 30 дней | 1/300 ставки ЦБ
NO meme — payment schedule printout on bright desk with highlighted «5 дней» vs «2 месяца» threshold line

### inline_5 — process_flow — Что на самом деле говорит 214-ФЗ про рассрочку
Labels: Эскроу или взнос | Выписка банка | Прекращение ДДУ | Обеспечительный платёж | Переписка менеджера
Meme: this_is_fine_dog tiny corner — flowchart 214-ФЗ thresholds: 3×/12мес or 2 months, then 30-day warning

### inline_6 — bar_timeline_chart — Куда ушли деньги — эскроу, взнос, обещание менеджера
Labels: График платежей | Дата зачисления | Предупреждение письмом | Расчёт неустойки | Статья 333 ГК
NO meme — timeline bars: payment sent → credited +5d → warning letter → termination notice

### inline_7 — structure_diagram — Что проверить до следующего платежа — таблица
Labels: Срок из графика | Отправка денег | Зачисление на счёт | Получение уведомления | Последовательность событий
Meme: wojak tiny corner — checklist diagram before next payment date

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
