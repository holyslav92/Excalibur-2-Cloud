---
status: PASS
topic_id: B35
agent: excalibur-blog-cover
---

## Artifacts

- `cover/cover.png` — 1200×675, solo grsai attempt 2/2, cover_qa PASS
- `cover/inline-01.png` … `cover/inline-07.png` — 1200×675 each, quad canvas split
- `cover/canvas-quad-01.png` — i2i (cover+inline_1..3 source)
- `cover/canvas-quad-02.png` — t2i (inline_4..7 source)
- `cover/quad-manifest.json` — scene + meme_picks + cover_motifs
- `cover/cover_qa.json` — PASS (md5=6f970c41c2d14d5ca93762baecf79462)

## Pipeline

1. quad grsai canvas 1 (i2i) + canvas 2 (t2i)
2. quad_apply → split + HTML inject
3. solo cover regen (attempt 1 FAIL QA → attempt 2 PASS)

## Hook

«Аренду запретили — жильцы ушли к соседям» + phone +7 922 001 65 05

## Memes

cover: disappointed_black_guy, long_cat | inline_1: expanding_brain | inline_5: stonks | inline_7: james_doakes
