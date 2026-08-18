# Blog cover quad canvas contract

> **TENANT:** The Риэлтор / tymenrieltor.ru — `memory/cover/*`, `shared/tenant-config.json`.

# Excalibur BLOG — Quad Canvas (mcp-derouter 2K)

Cover после `article.html` + Sol PASS.

## Longform: 8 изображений

- `cover.png` 1200×675
- `inline-01.png` … `inline-07.png` (7× `figure.inline-quad`, data-slot `inline_1`…`inline_7`)
- **2 canvas** `2048×1152` (2×2, панели 16:9)

| Canvas | Файл | Слоты |
|--------|------|-------|
| 1 | `canvas-quad-01.png` | cover, inline_1…3 |
| 2 | `canvas-quad-02.png` | inline_4…7 |

PRIMARY: **mcp-derouter**, `resolution: 2K`. Kie — legacy fallback.

## Hero identity lock

- `memory/cover/assets/identity-real/*` — **4 live photos** (28 лет, round face, sandy hair). i2i ротация.
- `scene-composition-only/hero-ref-*.jpg` — mood ONLY, **never FACE source**
- `blog-hero.json` → `emotion_bank`, `composition_rule`

**Каждая обложка:** новая эмоция/поза/сцена. **Запрещён** copy-paste композиции эталонов.

## Workflow

```bash
python3 scripts/excalibur_blog_hero_reference_url.py
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_quad_manifest.py --article-dir <dir> --merge
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir <dir> --write-batch
# mcp-derouter ×2 → quad-mcp-result-01.json, quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
```

## Visual locks (The Риэлтор)

- Панели `#FFFFFF`; ink `#141821`; gold `#dcc5a1` один accent
- Cover: host LARGE left, smart-casual blazer, identity-real face lock, tiny deal-prop right
- Inline: без людей; 3–6 RU labels; тот же collage-язык
- Запреты: plastic/uncanny face, AI hero-ref as face, white hoodie, pink-cat, EXCALIBUR stamp, beige gradient, clone any reference scene

## Blockers

- нет reference / canvas 1 без `input_urls`
- `DEROUTER BLOCKER` / `KIE API BLOCKER` — нет URL после 2K gen
- 8 отдельных image jobs вместо 2 canvas — запрещено
- отсутствует любой из `inline-01…07.png` или inject `data-slot`
- inline с людьми/лицами или empty gray placeholders
- cover клонирует эталонный кадр офиса/балкона 1-в-1
