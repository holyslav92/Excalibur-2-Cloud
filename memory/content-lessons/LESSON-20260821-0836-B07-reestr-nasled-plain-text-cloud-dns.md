## LESSON-20260821-0836-B07-reestr-nasled-plain-text-cloud-dns
status: proposed
topic_id: B07
category: utility
confidence: high

### Evidence
- artifact: cloud curl `https://reestr-nasled.ru/` → `Could not resolve host: reestr-nasled.ru` (DNS failure, no HTTP status)
  finding: домен не резолвится из Cloud egress; не «404 dead link», а resolver/DNS gap.
- artifact: research-notes.md + drafts/writer.html — источник `https://reestr-nasled.ru/` в official table; Writer упоминает сервис как plain text `reestr-nasled.ru` (без `<a href>`).
- artifact: drafts/variant-a.html — `<a href="https://reestr-nasled.ru">` (hyperlinked) — **would FAIL** link_verify в cloud.
- artifact: article.html (published) — только plain text `reestr-nasled.ru` в чеклисте; link-verify.json PASS (11 links, 0 failed).
- artifact: link-verify.json — reestr-nasled.ru не в списке проверок (нет href)
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- CLOUD_DNS_REESTR_NASLED
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Упоминание реестра наследственных дел ФНП в чеклисте до аванса — utility для buyer.
- Plain-text hostname в финале — publish-safe в cloud.

### Change
- Research/Writer: для reestr-nasled.ru в cloud pipeline — **plain text** или «сайт ФНП reestr-nasled.ru» без `<a href>`; не полагаться на live HEAD из Cloud.
- link_verify: при hyperlinked reestr-nasled — ожидать hard FAIL или добавить в soft-external/DNS-tolerant list (fixer queue INC-20260821-0836).
- Live site: readers in RF могут открыть; cloud pre-publish check ≠ reader experience.

### Never again
- Не вставлять `<a href="https://reestr-nasled.ru">` в Writer/Sol без проверки cloud DNS или soft-verify policy.
- Не удалять utility mention из чеклиста — только сменить формат ссылки.

### Proposed apply
- Scout/Research skill note: FNP registry = plain text in article body under cloud.
- Fixer: evaluate SOFT_EXTERNAL or dedicated `FNP_OFFICIAL_HOSTS` for DNS-only failures (after repeat).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
wp_post_id: 8994
