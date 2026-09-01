# Cover-scene inputs — B20

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B20
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик сменил юрлицо — банк не открыл эскроу
- hook (cover-text): «Застройщик сменил компанию — бронь зависла» (highlight: «компанию»)
- sticky: «Вывеска прежняя, бумаги другие»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: реорганизация застройщика → новый ДДУ от другого ООО → банк не открывает эскроу → бронь 72 часа сгорает

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки в тюмени от застройщика» — 651
- «дду эскроу» — 38
- «реорганизация застройщика» — 3

## meme_picks (from cover-text.json)

- cover: two_buttons, surprised_tom
- inline_1: distracted_boyfriend
- inline_5: this_is_fine_dog
- inline_7: wojak

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B19: turquoise polo showroom knee-up right cancel card (YESTERDAY — avoid showroom duplicate)
- B15: white shirt sand vest waist center envelope
- B12: light blue shirt showroom waist right
- B06: lemon yellow shirt medium right window

**Required:** light/bright #FFF high-key, sun flare; two_buttons people-meme + surprised_tom cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT showroom with model like B19.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Техническая» смена ООО — и семья пошла к ДДУ в новостройке
Labels: Первый договор | Четыре месяца | Новая компания | Другие ИНН | Вывеска прежняя
Meme: distracted_boyfriend tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Бронь 72 часа | Счёт не открыт | Проверка владельца | Пауза банка | Бронь истекла
NO meme

### inline_3 — realistic_photo — Через 72 часа бронь сгорела: эскроу так и не открыли
Labels: Вывеска не компания | Другой ИНН | Передаточный акт | Правопреемство проверить
NO meme — sales desk countdown timer + frozen escrow symbol

### inline_4 — realistic_photo — Вывеска та же, ИНН другой: где начинается новый застройщик
Labels: Договор регистрируют | Пять строк сверки | Новый получатель | Банк проверяет заново | Одобрение не бронь
NO meme — office wall sign vs new contract header INN mismatch

### inline_5 — structure_diagram — Новый ДДУ против зарегистрированного: что видит банк
Labels: Три участника | Новая аккредитация | Сроков нет | Бронь отдельно | Деньги не ушли
Meme: this_is_fine_dog tiny corner

### inline_6 — process_flow — Что сверять до подписи — таблица
Labels: ИНН в шапке | Объект и площадь | Цена и оплата | Срок передачи | Реквизиты счёта
NO meme

### inline_7 — bar_timeline_chart — Эскроу, бронь и правопреемство: где ломается цепочка
Labels: Сверить договоры | Письма банку | Сначала открыть счёт | Бронь не кредит | Ждать бумаги
Meme: wojak tiny corner

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
