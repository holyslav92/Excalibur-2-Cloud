# Title inputs — write title-brief.json ONLY

Ты Derouter title. Напиши **только валидный JSON** title-brief.json (no markdown wrapper).

## Inputs
- research-notes.md: B10, мнимая внутрисемейная сделка без денег, наследники оспорили, суд забрал квартиру у покупателя
- scout title draft: «Договор подписали — а денег не было: в Тюмени наследники забрали квартиру»
- comment_magnet_angle: «Если продавец когда-то продавал родственнику без денег — вы бы рискнули?»
- P0 Wordstat: купить квартиру в тюмени 22660
- forbidden H1: чеклист, N шагов, стоит ли покупать
- published: B02-B09 (no duplicate)

## Required JSON fields
```json
{
  "topic_id": "B10",
  "h1": "...",
  "slug": "dogovor-podpisali-a-deneg-ne-bylo-v-tyumeni-nasledniki-zabrali-kvartiru",
  "comment_magnet_angle": "...",
  "wordstat_p0": "купить квартиру в тюмени",
  "wordstat_volume": 22660,
  "h2_candidates": ["...", "..."],
  "forbidden_markers_check": "PASS"
}
```

H1 ~50-70 chars, news-casus, Тюмень, финал намёк. Use scout title or tighten.
