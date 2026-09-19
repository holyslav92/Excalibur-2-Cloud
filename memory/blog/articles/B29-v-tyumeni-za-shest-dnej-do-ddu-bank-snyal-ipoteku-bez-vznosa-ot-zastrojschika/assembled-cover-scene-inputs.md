# Cover-scene inputs — B29

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B29
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени за шесть дней до ДДУ банк снял ипотеку без взноса от застройщика — семья не успела собрать первоначальный платёж
- hook (cover-text): «Банк снял нулевой взнос за шесть дней» (highlight: «взнос»)
- sticky: «Акция закончилась»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: офис продаж обещал «ипотека без взноса от застройщика» → бронь 50–80 тыс. → предварительное одобрение → за 6 дней до ДДУ банк закрыл программу нулевого взноса → платёж +18 000 ₽ → своих денег на взнос нет → ДДУ не подписали, эскроу не открыли, часть брони удержали

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «ипотека от застройщика тюмень» — 514
- «ипотека без первоначального взноса» — demand spine
- «новостройки тюмень» — 4430

## meme_picks (from cover-text.json)

- cover: two_buttons, crying_cat
- inline_1: bad_luck_brian
- inline_5: wojak
- inline_7: blinking_white_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B28: KP pavilion sand jacket gas pipe roll_safe
- B27: sales office terracotta overshirt declaration disappointed_black_guy
- B26: bank mortgage desk olive vest hide_pain_harold
- B25: kneeling empty apartment tape measure

**Required:** light/bright #FFF high-key, sun flare; two_buttons people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright ипотечный уголок в лобби ЖК с табло «0% взнос» и письмом банка об отмене субсидии — NOT duplicate B27 sales desk, NOT B26 bank back office, NOT KP pavilion).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотека без взноса от застройщика» — так звучало в офисе продаж (pair with inline_2)
Labels: Офис продаж | Ипотека без взноса | За счёт кого | Не семейная льгота | Документ на вход
Meme: bad_luck_brian tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Бронь оплачена | Предварительное одобрение | Платёж в бюджете | Недели до ДДУ | Бронь не эскроу
NO meme — table: обещание «0% взнос» vs условия брони и срок одобрения

### inline_3 — realistic_photo — Бронь оплачена, предварительное одобрение легло в семейный бюджет
Labels: Шесть дней до ДДУ | Программа закрылась | Два расчёта | Письменный запрос | Квартира та же
NO meme — кухонный стол, два калькулятора, банковское SMS на телефоне (без лиц)

### inline_4 — realistic_photo — За шесть дней до ДДУ: программа с нулевым взносом закрылась
Labels: Плюс восемнадцать тысяч | Взноса нет | Две задачи | Новый расчёт | Бюджет не сходится
NO meme — календарь «6 дней», письмо банка, перечёркнутый плакат 0%

### inline_5 — process_flow — Ежемесячный платёж прибавил восемнадцать тысяч — своих денег на взнос нет
Labels: ДДУ не подписали | Эскроу не открыли | Удержали бронь | Пятьдесят — восемьдесят | Семья остановилась
Meme: wojak tiny corner

### inline_6 — bar_timeline_chart — ДДУ не подписали, эскроу не открыли, часть платы за бронь удержали
Labels: Срок акции | Привязка к лоту | Банковское решение | Отмена субсидии | Плата за бронь
NO meme — timeline бронь → отмена программы → удержание части брони

### inline_7 — structure_diagram — Что зафиксировать письменно до оплаты брони — таблица
Labels: Предварительное не вечно | ДОМ точка рф | Пауза до аванса | Программа и срок | Вопрос до эскроу
Meme: blinking_white_guy tiny corner

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
