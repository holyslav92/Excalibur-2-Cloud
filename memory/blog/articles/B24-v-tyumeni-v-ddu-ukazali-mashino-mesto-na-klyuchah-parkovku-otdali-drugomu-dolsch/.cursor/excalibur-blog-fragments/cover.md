---
status: FAIL
topic_id: B24
pipeline: grsai_solo_cover_regen
budget_exhausted: true
grsai_canvas_attempts: 1
solo_cover_attempts: 1
cover_attempts_total: 2
---

# Cover fragment — B24

## Artifacts

- `cover/cover.png` — quad split top-left (canvas 1, i2i identity-real)
- `cover/inline-01.png` … `cover/inline-07.png` — quad canvas split (7 inlines)
- `cover/canvas-quad-01.png` (i2i cover+inline1-3), `cover/canvas-quad-02.png` (t2i inline4-7)
- `cover/quad-manifest.json`, `cover/scene-draft.json`
- `cover/cover-registry.json` — image_caption_builder applied (inline alt gate flakes on H2 overlap)

## Canon

- hook: «Чужая машина заняла ваше место»
- phone: +7 922 001 65 05
- sticky: Это не опечатка
- meme_picks: confused_math_lady, this_is_fine_dog (cover); james_doakes, cheems, disappointed_black_guy (inlines)
- NO Wordstat strips on cover (manifest log only)
- light/bright underground parking P-42, pine-green jacket, anti-repeat motifs recorded

## Regen attempt 2 (solo cover API)

- Fixed: `pixel_manifest_outfit_matches` PASS — хвойно-зелёная куртка (not black blazer)
- Fixed: `pixel_hook_title_not_truncated` PASS — full hook readable
- Visual: 3 Wordstat P0 stickers top-left, confused_math_lady + this_is_fine_dog memes, phone +7 922 001 65 05
- Still FAIL pixel: host_face (crouch pose), mean_lum 155, collage_inset, pixel_no_wordstat_query_strips (2 strips detected)
- `cover/cover-budget-result.json` — budget exhausted (2/2)

## Next

→ Cover-QA re-run or Indexer per budget-exhausted canon
