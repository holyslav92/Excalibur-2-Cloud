# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: 19 дней до 1 октября: банк пересчитал семейную ипотеку — семья остановила ДДУ
- hook (cover-text): «Одобрили ипотеку — взнос не сошёлся» (highlight: «взнос»)
- sticky: «Сверьте расчёт до ДДУ»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: предварительное одобрение семейной ипотеки → бронь новостройки → за 19 дней до 1 октября банк пересчитал лимит комбо-кредита → первоначальный взнос 20% перестал сходиться → ДДУ остановили → деньги на эскроу не ушли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека в тюмени» — 740
- «семейная ипотека октябрь 2026» — 323
- «семейная ипотека с 1 октября 2026» — 231

## meme_picks (from cover-text.json)

- cover: confused_math_lady, cheems
- inline_1: this_is_fine_dog
- inline_5: wojak
- inline_7: disappointed_black_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: newbuild handover room, light blue + mustard sweater (side_eye_chloe)
- B22: bank mortgage office, lemon-yellow shirt (disaster_girl)
- B20: terracotta overshirt MFC corridor
- B19: turquoise polo showroom

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + cheems cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank office duplicate (B22); NEW location (bright newbuild sales pavilion with combo mortgage chart and reservation contract).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Семейную ипотеку одобрили» — и семья забронировала новостройку (pair with inline_2)
Labels: Трёшка на востоке | Бронь оплачена | Льгота до 6 млн | Взнос 20% в бюджете | Одобрение не договор
Meme: this_is_fine_dog tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: 19 дней до октября | Лимит комбо-кредита | Правила меняются | Ставка сохранилась | Причина не календарь
NO meme

### inline_3 — realistic_photo — За 19 дней до 1 октября банк пересчитал лимит
Labels: Льготные 6 млн | Рыночный хвост дороже | Лимит до 15 млн | Проверка долговой нагрузки | Расчёт банка письменно
NO meme — bright desk with combo mortgage split chart and bank letter

### inline_4 — realistic_photo — Комбо-ипотека: шесть миллионов под шесть процентов — и рыночный хвост
Labels: 20% уже мало | Платёж выше бюджета | ДДУ не подписали | Бронь отдельным договором | Эскроу не открыли
NO meme — calculator showing down payment gap, DDU folder unopened

### inline_5 — structure_diagram — Первоначальный взнос перестал сходиться — ДДУ остановили
Labels: Бронь не эскроу | Бронь не взнос | Срок фиксации | Запросили расчёт | Пауза до ДДУ
Meme: wojak tiny corner

### inline_6 — process_flow — Бронь тикает, деньги не на эскроу
Labels: Срок решения банка | Кредит и взнос | Структура комбо | Платёж и ПДН | Объект и застройщик
NO meme

### inline_7 — bar_timeline_chart — Что сверять до подписания ДДУ и открытия эскроу — таблица
Labels: Срок и цена брони | Условия выхода | ДДУ обязывает купить | Эскроу счёт сделки | Сначала документы
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
