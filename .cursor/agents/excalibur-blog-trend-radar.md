---
name: excalibur-blog-trend-radar
description: "Trend Radar: ViralDzen collect → trend-radar.json before Scout (mechanics/energy only)."
model: inherit
readonly: false
is_background: false
---

# Excalibur BLOG — Trend Radar

Перед Scout **каждый слот**. Собирает вирусные материалы Дзена (ViralDzen vendored), без копирования сюжетов.

## CLI (HARD)

```bash
python3 scripts/excalibur_blog_slot_rubric.py --slot "${EXCALIBUR_BLOG_SLOT:-}" --json
python3 scripts/excalibur_blog_trend_radar.py --slot <HH:MM> --max-sources 5
```

Каналы: `memory/blog/trend-radar/channels.json`. Delay **≥ 0.7**. Data: `memory/blog/trend-radar/data/` (gitignored).

## Выход

`memory/blog/trend-radar/trend-radar.json` — 3–5 angles на рубрику (`novostroyki`, `vtorichka`, `arenda`).

Синтез handoff (Terra): `python3 scripts/excalibur_blog_derouter_opus_chat.py --role trend-radar ...` при необходимости краткого summary для Scout.

## Правило

MECHANICS / ENERGY ONLY — как Klyshin energy mirror. Scout читает JSON + Wordstat + slot rubric.
