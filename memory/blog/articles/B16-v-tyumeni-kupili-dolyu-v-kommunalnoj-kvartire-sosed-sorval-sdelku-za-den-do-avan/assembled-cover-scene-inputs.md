# Cover-scene inputs — B16

ROLE: cover-scene. Output valid JSON only.

## Context
- topic_id: B16
- H1: В Тюмени сосед остановил покупку доли перед авансом
- hook: «Сосед остановил покупку доли до аванса» (highlight: остановил)
- sticky: Деньги не ушли зря
- phone: +7 922 001 65 05
- angle: коммуналка, преимущественное право, аванс остановили

## meme_picks
cover: two_buttons, polite_cat
inline_1: bad_luck_brian
inline_5: blinking_white_guy
inline_7: disappointed_black_guy

## Variety (HARD)
i2i face-studio-2026-06-23.jpg only. INVENT outfit/action/emotion.
FORBIDDEN: black blazer left bust (B03/B04 clone)
Differ from B12 light blue showroom, B10 sage cardigan viewing
Suggest: burgundy henley + light grey chinos, bright communal corridor MFС queue, incredulous raised brows, holding neighbor refusal letter envelope, host waist-left dynamic

## Inline H2 anchors
1. За день до аванса сосед заговорил о преимущественном праве
2. Коммунальная квартира: отдельная комната и общий сосед
3. Выписка была чистой — а риск остался
4. Финал: аванс не внесли и ушли на другую квартиру
5. Преимущественное право: что это в быту
6. Тридцать дней и нотариальный отказ
7. Что проверить до аванса, если в коммуналке

Use inline_labels from cover-text.json.

## JSON schema
{
  "cover_emotion": "...",
  "cover_motifs": { outfit, emotion, pose_framing, action, composition, location, meme, prop_set, sticker_set, joke },
  "wordstat_stickers": [{ phrase, volume }] log only,
  "slots": { "cover": { scene_hint, cover_emotion }, "inline_1" ... "inline_7": { visual_type, scene_hint, placement_group?, labels } }
}
