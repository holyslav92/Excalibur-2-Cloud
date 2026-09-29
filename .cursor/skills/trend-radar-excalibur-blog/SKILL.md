---
name: trend-radar-excalibur-blog
description: "Trend Radar before Scout: ViralDzen → trend-radar.json (mechanics/energy, 3 rubrics)."
---

# Trend Radar (The Риэлтор)

Перед Scout **каждый слот**.

```bash
python3 scripts/excalibur_blog_slot_rubric.py --slot "${EXCALIBUR_BLOG_SLOT:-15:00}" --json
python3 scripts/excalibur_blog_trend_radar.py --slot <HH:MM> --max-sources 5
```

- Каналы: `memory/blog/trend-radar/channels.json`
- Handoff: `memory/blog/trend-radar/trend-radar.json`
- ViralDzen: `vendor/viraldzen` (`--delay` ≥ 0.7)
- Skill сбора: `.cursor/skills/viraldzen-collect/SKILL.md`

**Запрещено:** копировать сюжеты/тексты с Дзена — только headline formula, hook energy, mechanism.

**HARD — same mechanism only:** энергия Trend Radar переносится в Scout/Writer **только если механизм = механизм casus** (вторичка/дарение/аванс ≠ семейная ипотека 1 октября, эскроу-новости и т.д.). Календарный viral headline **другой рубрики** в теле статьи → `no_unrelated_calendar_news_glue` FAIL. Читатели знают закон и ленту — не «склеивать» новости ради срочности.
