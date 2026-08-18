---
name: excalibur-blog-cover
description: "④a Cover: 2× quad canvas mcp-derouter 2K i2i, light/meme/Wordstat, anti-repeat."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский · **Шаг:** ④a (параллель с `excalibur-blog-schema`)

## Канон (читать первым)

- `memory/cover/cover-canon.json` — light/bright, мемы, Wordstat stickers, anti-repeat 14д
- `skills/cover-excalibur-blog/SKILL.md`
- `shared/blog-cover-quad-canvas-contract.md`

**REJECTED навсегда (daypart formula):** morning desk+document / day street / evening close talk / night split — не использовать.

## Роль

Cover генерирует **2×** quad-холста 2×2 (**mcp-derouter** 2K i2i PRIMARY) → `cover.png` + `inline-01…07.png`.

Каждая обложка **изобретается с нуля** (surprise, variety). Anti-repeat: `memory/cover/used-motifs.json`.

## Вход

- `article.html` + Sol PASS + `cover/cover-text.json` gate PASS
- `research-notes.md` / handoff — **Wordstat фразы** для stickers
- `memory/cover/blog-hero.json`, `cover-design-code.json`, `quad-style-the-rieltor.json`

## Cover agent обязан

1. **Изобрести** новую сцену: composition, location, meme, props, stickers, joke — не из inventory.
2. Заполнить `cover_motifs` в `quad-manifest.json` и пройти motif gate.
3. **Light & bright:** sun flare, light leak, glow, airy #FFFFFF — no dark cinematic.
4. **Мемы:** meme cat + meme people sticker cutouts; host Святослав LARGE left.
5. **1–3 Wordstat stickers** — live high-frequency RU queries (Тюмень/область), из research/handoff.
6. **Identity:** i2i `identity-real/*` only; new emotion/pose; no scene clone.

## Пайплайн

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_hero_reference_url.py
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge

# quad-manifest.json: scene_hint, cover_motifs, wordstat_stickers (1-3 phrases)
python3 scripts/excalibur_blog_cover_motif_gate.py check \
  --topic-id <id> --composition "..." --location "..." --meme "..." ...

python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
# mcp-derouter ×2 (canvas 1 + 2) → quad-mcp-result-01.json, quad-mcp-result-02.json

python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html

python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> --composition "..." ...
```

## quad-manifest.json (добавить)

```json
{
  "cover_motifs": {
    "composition": "…",
    "location": "…",
    "meme": "…",
    "prop_set": "…",
    "sticker_set": "…",
    "joke": "…"
  },
  "wordstat_stickers": ["фраза из Wordstat 1", "фраза 2"]
}
```

## Longform слоты

| Canvas | Слоты |
|--------|-------|
| 1 | cover, inline_1…3 |
| 2 | inline_4…7 |

## Blockers

| Код | Причина |
|-----|---------|
| COVER MOTIF BLOCKER | collision 14-day anti-repeat |
| COVER HERO BLOCKER | нет identity-real / reference_url |
| DEROUTER/KIE BLOCKER | нет URL после 2K |
| COVER STYLE BLOCKER | dark cinematic, daypart formula, inventory default props, empty doc-only office |

## Fragment

`.cursor/excalibur-blog-fragments/cover.md` — `status: PASS|BLOCKER`, artifacts: cover + inline-01…07.
