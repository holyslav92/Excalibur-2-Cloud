# Cover-scene inputs — B07

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B07
- tenant: The Риэлтор, Тюмень
- H1: Наследству на квартиру два года. Сын от первого брака отказ не писал
- hook (cover-text): «У квартиры может быть наследник» (highlight: «наследник»)
- sticky: «Обещаний продавца мало»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: один собственник в ЕГРН и свидетельство не доказывают отсутствие других наследников; сын от первого брака без нотариального отказа; «отказа не будет» — слова, не документ; смерть ~2 года назад

## Wordstat stickers (PIL overlay x≥0.68, NOT on title)

- «наследство квартиры» — 968
- «вступление в наследство» — 1266
- «наследство квартиры наследники» — 53

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B06: lemon shirt, host right, panoramic window price jump
- B05: terracotta sweater + grey overcoat, host right entrance steps
- B04: black blazer left bust side-eye investigation board
- B03: black blazer left bust jaw-drop board

**Required:** light/bright #FFF high-key, sun flare; meme cat + catalog people-meme small stickers; NO dark cinematic; NO daypart formula; NO Wordstat on canvas (PIL later).

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon shirt right window.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — structure_diagram — «Один собственник в ЕГРН не отвечает на вопрос «кто ещё наследовал»»
Labels: ЕГРН на дату | Один не значит все | Свидетельство не обо всех | Принял без бумаг
Meme sticker: yes (small cat corner)

### inline_2 — comparison_table — «Сын от первого брака: почему он остаётся наследником»
Labels: Первая очередь | Дети равны | Развод не отменяет право | Срок вернёт суд
NO meme

### inline_3 — process_flow — «Отказа не будет» и другие фразы продавца
Labels: Отказ у нотариуса | Слова не отказ | Не принял не отказ | Принял без бумаг
NO meme

### inline_4 — bar_timeline_chart — Шесть месяцев, два года и три года
Labels: Шесть месяцев | Два года прошло | Три года не защита | Считать от смерти
NO meme

### inline_5 — labeled_checklist — Реестр наследственных дел
Labels: Реестр наследственных дел | Поиск по умершему | Наследников не покажет | Это один шаг
Meme sticker: yes (small thinking cat corner)

### inline_6 — process_flow — Кейс: приватизация, смерть отца, сын на службе
Labels: Смерть два года назад | Отказа нет | Аванс не внесли | Проверка 2900 рублей
NO meme

### inline_7 — labeled_checklist — Вопросы продавцу до аванса
Labels: Спросите о браках | Спросите о детях | Отказы у нотариуса | Сверьте дату смерти | Аванс после ответов
Meme sticker: yes (small surprised_guy corner)

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, pink highlight «наследник», ZERO Wordstat on canvas.
