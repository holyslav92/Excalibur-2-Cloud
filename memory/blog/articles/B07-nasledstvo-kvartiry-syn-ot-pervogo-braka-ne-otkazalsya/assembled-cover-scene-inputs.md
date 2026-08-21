# Cover-scene retry — B07 (pixel QA fix)

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Fix targets (pixel FAIL)

1. NO gold horizontal brush band under highlight — gold Cyrillic LETTERS on «наследник» only
2. NO dark blazer / lapels on chest — cream henley or solo sweater only
3. Phone +7 922 001 65 05 readable bottom-left
4. ZERO Wordstat on canvas (PIL after)

## Context

- hook: «У квартиры может быть наследник» (highlight: «наследник»)
- sticky: «Обещаний продавца мало» — small square pin, NOT horizontal strip
- outfit: cream/off-white henley OR solo knit sweater — NO blazer, NO jacket, NO dark lapels

## JSON schema

Same as before: cover_emotion, cover_motifs (10 fields), slots.cover + inline_1…7 scene_hint/alt.

cover scene_hint: cream henley; wary at family tree; gold LETTERS наследник NO band; phone CTA; NO Wordstat canvas.
