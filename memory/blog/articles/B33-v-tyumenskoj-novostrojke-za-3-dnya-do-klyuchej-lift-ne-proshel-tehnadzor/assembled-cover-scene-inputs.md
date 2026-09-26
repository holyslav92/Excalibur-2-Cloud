# Cover-scene inputs — B33

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B33
- tenant: The Риэлтор, Тюмень
- H1: За 3 дня до ключей в тюменской новостройке лифт не прошёл осмотр — заселение перенесли
- hook (cover-text): «За три дня лифт не прошёл осмотр» (highlight: «осмотр»)
- sticky: «Ключи перенесли»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: за 3 дня до ключей лифт не допущен к эксплуатации; приёмку перенесли; семья платит ипотеку и аренду; акт не подписан

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «квартира в тюмени купить новостройки»
- «приемка новостройки тюмень»

## meme_picks (from cover-text.json)

- cover: blinking_white_guy, polite_cat
- inline_1: meme allowed (pick one small people or cat from meme-top100 on-topic)
- inline_5: meme allowed
- inline_7: meme allowed

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:** B25–B29 terracotta/olive/sage variants; B19 turquoise polo showroom.

**Required:** light/bright #FFF high-key, sun flare; blinking_white_guy + polite_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; elevator/newbuild lobby context.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — За три дня до ключей: семейная ипотека и квартира на высоком этаже
Labels: Три дня до ключей | Семейная ипотека | Высокий этаж | Лифт без допуска | Аренда не снята
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Лифт не допущен | Приёмку перенесли | Акт не подписали | Акт освидетельствования | Ждут документы
NO meme

### inline_3 — realistic_photo — В подъезде лифт не допущен — приёмку перенесли
Labels: Двойная касса | Ипотека и аренда | График не стоп | Новая дата | Письменный след
NO meme — bright newbuild entrance elevator doors closed inspection tape

### inline_4 — realistic_photo — Передаточный акт не подписали — ждут документы на лифт
Labels: Акт без подписи | Паспорт лифта | Ввод в эксплуатацию | Договор обслуживания | Не на авось
NO meme — transfer act folder elevator passport on bright desk

### inline_5 — process_flow — Двойная касса: кредит уже списывается, аренда не отменилась
Labels: Разрешение на ввод | Паспорт и декларация | Реестр оборудования | Пробная поездка | Акт осмотра
Meme tiny corner optional

### inline_6 — bar_timeline_chart — Что проверить по лифту до подписи акта
Labels: Просрочка передачи | Неустойка с 2026 | Мораторий до 2025 | Претензия письменно | Сохранить переписку
NO meme

### inline_7 — structure_diagram — Просрочка передачи и неустойка после 2026 года
Labels: Без паники | Документ вместо обещания | Лифт до ключей | Расходы на учёте | Позиция семьи
Meme tiny corner optional

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    ...
  }
}
```
