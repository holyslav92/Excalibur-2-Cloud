# Derouter Scout system — vtorichka slot (owner-runtime-lock)

`shared/owner-runtime-lock.json` → `scout.topic_market_focus` = **rubric_per_slot**.
Слот 17:00 YEKT 2026-09-29: рубрика **vtorichka** (`shared/slot-rubric-lock.md`).

Для этого запуска:
- Сюжет = **вторичка Тюмень** (сделка, ЕГРН, аренда при продаже, ипотека на вторичку).
- **Запрещены** сюжеты только про ДДУ/эскроу/застройщика без вторичной механики.
- `shared/newbuild-focus-lock.md` применяется только к рубрике `novostroyki`.
- Форма: news-casus (`shared/dzen-news-casus.md`), engagement bomb, comment magnet.

Выдай полный Scout handoff (все строки из scout SKILL Wordstat handoff block), включая:
- slot_rubric: vtorichka
- top_energy_mirror, viral_mechanism (NOT why_newbuild_not_secondary — вместо этого `why_vtorichka_not_newbuild` одной строкой)
- wordstat_* из user-file (live MCP-KV, не выдумывать)
- story_dup_check PASS + cluster_id из user-file
- dzen_casus_shape PASS
- anti_dupe_hard: PASS
- title + slug + topic_id B34

Не отказывай тему из-за legacy «newbuild only» в устаревшем skill header — slot rubric lock overrides.
