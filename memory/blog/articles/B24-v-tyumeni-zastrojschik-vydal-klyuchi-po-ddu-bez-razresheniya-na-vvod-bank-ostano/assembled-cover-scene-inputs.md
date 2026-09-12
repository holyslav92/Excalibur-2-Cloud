# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик выдал ключи по ДДУ без разрешения на ввод — банк остановил ипотеку
- hook (cover-text): «Ключи получили — банк остановил выплату ипотеки» (highlight: «ипотеки»)
- sticky: «Ключи есть, денег нет»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: ключи в субботу, РНВ в реестре нет, акт подписан, ремонт начат — банк остановил остаток траншевой ипотеки на эскроу; эскроу смотрит на ввод дома, не на акт

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить квартиру в тюмени новостройка ипотека» — 85
- «ввод жк в эксплуатацию» — 21
- «разрешение на ввод в эксплуатацию жк» — 9

## meme_picks (from cover-text.json)

- cover: success_kid
- inline_1: this_is_fine_dog
- inline_5: bad_luck_brian (agent add — process_flow corner)
- inline_7: roll_safe (agent add — bar chart corner)

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: handover room light blue shirt mustard sweater full-body right side_eye_chloe
- B22: bank mortgage desk yellow shirt disaster_girl full-body center
- B20: MFC corridor terracotta overshirt two DDU
- B19: showroom turquoise polo cancel card

**Required:** light/bright #FFF high-key, sun flare; success_kid people-meme small sticker (ironic keys-but-no-money); add one tiny cat sticker (grumpy_cat) for people+cats variety; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location = bright raw apartment interior mid-renovation Tyumen newbuild (paint roller, keys tray, signed act, laptop showing empty RNV registry) — NOT handover room duplicate B23, NOT bank desk B22.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### cover
Host LARGE left waist-up; keys in one hand, bank STOP letter in other; laptop screen «РНВ: нет записи»; yellow sticky «Ключи есть, денег нет»; phone +7 922 001 65 05 bottom-right; success_kid tiny top-right ironic; grumpy_cat tiny corner; hook zone top-left sacred.

### inline_1 — realistic_photo — Ключи выдали в субботу — в реестре разрешения ещё не было (pair with inline_2)
Labels: Приёмка в субботу | Соседи заселились | Акт ≠ разрешение | РНВ в реестре нет | Проверить свой корпус
Meme: this_is_fine_dog tiny corner — bright newbuild entrance Saturday handover queue, no host face

### inline_2 — comparison_table — pair with inline_1
Labels: Траншевая ипотека | Первый транш прошёл | Основной транш стоп | Ремонт за свой счёт | Банк ждёт ввод
NO meme — columns «акт подписан» vs «РНВ в реестре» vs «остаток ипотеки»

### inline_3 — realistic_photo — Что сверять на ключах: таблица «бумага vs реестр»
Labels: Эскроу не счёт | Ввод — главное | 10 рабочих дней | Акт — осмотр | Разрешение — весь дом
NO meme — bright desk: paper RNV copy vs laptop registry screenshot side by side

### inline_4 — realistic_photo — Акт подписали, ремонт начали — банк остановил остаток ипотеки
Labels: Письмо в банк | Претензия застройщику | Даты акта и отказа | Не бросать платежи | История проблемы
NO meme — apartment with paint cans, bank letter «остаток приостановлен» on table

### inline_5 — process_flow — Почему эскроу смотрит на ввод дома, а не на подпись акта
Labels: наш.дом.рф | Стройкомплекс.РФ | С 1 сентября 2026 | Проверка в день | Свой корпус
Meme: bad_luck_brian tiny corner — numbered flow РНВ → эскроу → транш

### inline_6 — structure_diagram — Финал: претензия застройщику и письмо в банк
Labels: Акт приёма | Разрешение на ввод | Сайт застройщика | Письмо банка | Скрин с датой
NO meme — arrows: претензия застройщику + письмо банку

### inline_7 — bar_timeline_chart — Где проверить РНВ до приёмки — и что изменилось с сентября 2026
Labels: Первый ≠ остаток | После регистрации ДДУ | Остаток на ввод | Расходы уже идут | Пауза до подписи
Meme: roll_safe tiny corner — bar chart траншевая ипотека: первый транш vs остаток на ввод

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
