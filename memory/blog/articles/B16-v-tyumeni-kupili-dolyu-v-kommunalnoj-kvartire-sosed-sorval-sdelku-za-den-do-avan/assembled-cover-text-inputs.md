# Cover-text inputs — B16

ROLE: cover-text. Output valid JSON only, no markdown fences.

## Context
- topic_id: B16
- H1: В Тюмени сосед остановил покупку доли перед авансом
- angle: преимущественное право соседа в коммуналке, аванс остановили до денег

## JSON schema
{
  "hook": "...",
  "highlight": "...",
  "sticky": "...",
  "phone_cta": "+7 922 001 65 05",
  "inline_labels": { "inline_1": [...], ... "inline_7": [...] },
  "meme_picks": { "cover": [...], "inline_1": [...], ... }
}

## Rules
- hook: 5–7 кириллических слов, one line, prefer words ≥5 letters
- NO wordstat_stickers field
- meme_picks: only ids from meme-top100.json; people+cats mix; avoid recent 14d: roll_safe, crying_cat, hide_pain_harold, smudge_cat, distracted_boyfriend
- Suggested: cover → two_buttons + polite_cat; inline_1 → bad_luck_brian; inline_5 → blinking_white_guy; inline_7 → disappointed_black_guy
