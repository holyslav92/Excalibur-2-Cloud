# Cover-scene inputs — B22

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B22
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ключи задержали на 8 месяцев — неустойку дали сертификатом
- hook (cover-text): «Задержка ключей — сертификат вместо денег» (highlight: «сертификат»)
- sticky: «Сначала подпись — потом ключи»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: 8 месяцев просрочки по ДДУ, ипотека+аренда, в день ключей менеджер предлагает сертификат на отделку вместо ~1,47 млн неустойки

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «неустойка застройщик» — 257 (55+11176)
- «неустойка застройщик дду» — 33
- «приемка квартиры в новостройке» — 92

## meme_picks (from cover-text.json)

- cover: sacrednik_priest, long_cat
- inline_1: crying_jordan
- inline_5: confused_math_lady
- inline_7: disappointed_black_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B20: terracotta overshirt MFCC two_buttons (2 days ago)
- B19: turquoise polo showroom knee-up right
- B15: white shirt sand vest waist center envelope
- B12: light blue shirt showroom waist right

**Required:** light/bright #FFF high-key, sun flare; sacrednik_priest people-meme + long_cat cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT MFCC corridor; NOT showroom with model.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — День ключей в офисе продаж: «подпишите — и сертификат ваш»
Labels: Восемь месяцев ожидания | Ипотека и аренда | Срок в ДДУ прежний | Письмо не меняет дату | 1/150 ставки за день
Meme: crying_jordan tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Уведомление одностороннее | Дата только допсоглашением | Закон 214-ФЗ | Просрочка от старой даты | Ставка 14%
NO meme

### inline_3 — realistic_photo — Что проверить в бумагах в день ключей — таблица
Labels: Акт и допсоглашение | Сертификат на отделку | Без подписи нет ключей | Ребёнок устал в очереди | Пауза до вечера
NO meme — bright handover desk with stacked papers, keys tray, child chair in waiting area (no faces)

### inline_4 — realistic_photo — Восемь месяцев ипотеки и аренды — пока в ДДУ тикал чужой срок
Labels: Номинал ниже закона | Около 1,47 млн | Сертификат 200–400 тысяч | Ипотека списалась обычно | Претензий не имею
NO meme — apartment calendar with 8 months crossed, mortgage receipt + rent invoice on bright kitchen table

### inline_5 — process_flow — Подписали — и деньги за просрочку так и не увидели
Labels: Неустойка — деньги | Сертификат — товар | Не закрывает ипотеку | Не закрывает аренду | Статья 333 снизит
Meme: confused_math_lady tiny corner

### inline_6 — bar_timeline_chart — Сертификат и законная неустойка: не одно и то же
Labels: Акт приёма-передачи | Допсоглашение о сроке | Соглашение о компенсации | Сверить две даты | Претензия до подписи
NO meme

### inline_7 — structure_diagram — Мораторий сняли, а бонусы остались: почему застройщик торгуется
Labels: Мораторий с 2026 отменён | Сертификат выгоднее денег | Посчитать до подписи | Отказ — не отказ | Пауза до вечера
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
