# Cover-scene inputs — B07

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B07
- tenant: The Риэлтор, Тюмень
- H1: Квартиру унаследовал один. Сын от первого брака отказ не писал
- hook (cover-text): «Проверь наследников до аванса» (highlight: «Проверь»)
- sticky: «Выписки мало»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: один собственник в ЕГРН и свидетельство — но сын от первого брака не писал нотариальный отказ; два года после смерти риск не закрыт; проверка реестра ФНП и круга наследников до аванса

## Wordstat stickers (PIL overlay x≥0.68, NOT on title)

- «реестр наследственных дел» — 601
- «вступление в наследство» — 41 (via «вступление в наследство на квартиру» cluster)
- P0 cluster: «наследство квартира» — 942

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B06: lemon yellow shirt, host right, apartment window, price jump 18→20
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04: black blazer left bust side-eye investigation board
- B03: black blazer left bust jaw-drop board

**Required:** light/bright #FFF high-key, sun flare; meme cat + catalog people-meme small stickers; NO dark cinematic; NO daypart formula; NO Wordstat text on canvas (PIL later at x≥0.68).

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon shirt right apartment.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table_ui — «Коротко: что нужно понять про наследство»
Labels: Один в ЕГРН | Дети первой очереди | Шесть месяцев принятия | Отказ потом невозможен
Meme sticker: yes (small cat corner)

### inline_2 — structure_diagram — «Почему ЕГРН и свидетельство не отвечают»
Labels: ЕГРН сегодня | Круг наследников скрыт | Свидетельство заявителя | Проверь до аванса
NO meme

### inline_3 — workflow_diagram — «Сын от первого брака — первая очередь»
Labels: Дети первой очереди | Брак не важен | Статус без отказа | Не семейная драма
NO meme

### inline_4 — labeled_checklist — «Шесть месяцев прошло — риск остался»
Labels: Шесть месяцев принятия | Восстановление через суд | Согласие без срока | Меньше трёх лет
NO meme

### inline_5 — checklist_board — «Реестр наследственных дел ФНП»
Labels: Поиск по ФИО | Номер дела | Отказы не видны | Не даёт гарантий
Meme sticker: yes (small serious_cat or thinking_cat corner)

### inline_6 — schema_faq_ui — «Пример: два года, отказа нет»
Labels: Два года спустя | Сын без отказа | Разговор не документ | От сделки отказались
NO meme

### inline_7 — tool_screenshot — «Что собрать до аванса»
Labels: ЕГРН и переходы | Свидетельство наследства | Реестр по ФИО | Все дети первой очереди | Отказы у нотариуса
Meme sticker: yes (small roll_safe or woman_yelling_cat corner)

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": {
    "composition": "...",
    "location": "...",
    "meme": "...",
    "prop_set": "...",
    "sticker_set": "...",
    "joke": "...",
    "outfit": "...",
    "emotion": "...",
    "pose_framing": "...",
    "action": "..."
  },
  "slots": {
    "cover": {
      "scene_hint": "...",
      "alt": "...",
      "cover_emotion": "..."
    },
    "inline_1": { "scene_hint": "...", "alt": "..." },
    "inline_2": { "scene_hint": "...", "alt": "..." },
    "inline_3": { "scene_hint": "...", "alt": "..." },
    "inline_4": { "scene_hint": "...", "alt": "..." },
    "inline_5": { "scene_hint": "...", "alt": "..." },
    "inline_6": { "scene_hint": "...", "alt": "..." },
    "inline_7": { "scene_hint": "...", "alt": "..." }
  }
}
```

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, pink highlight «Проверь», ZERO Wordstat on canvas.
