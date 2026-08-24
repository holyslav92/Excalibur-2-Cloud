## LESSON-20260824-0829-B10-phone-scammers-notary-angle
status: proposed
topic_id: B10
category: structure
confidence: medium

### Evidence
- artifact: assembled-writer-inputs.md#HANDOFF
  finding: hook_id `phone_scammers_notary`; dzen_casus_shape PASS; Klyshin original «нотариус не спасает от мошенников; ~40% нотариальных сделок устояли»; comment_magnet «пожилой продавец странно реагирует на звонки»; P0 Wordstat «купить квартиру в тюмени» 39961 RU / 22660 Tyumen.
- artifact: quality-bar-9.json
  finding: editorial PASS — 2557 words, comment_magnet_question, interlink 4 siblings, news-casus gates (no TL;DR, early TG+MAX).
- artifact: article.meta.json
  finding: title stakes-forward «суд отменил продажу: продавец должна вернуть 4,3 млн»; wp_category_slugs vtorichka-i-riski + riski-sdelki.
- artifact: assembled-writer-inputs.md#CRITICAL CONSTRAINTS
  finding: writer kept Тюмень кейс Назаровой **не нотариальным**; contrast Ольга (нотариус устоял) vs Назарова vs ВС РФ — angle honest, not bait-and-switch.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; no post-publish Dzen engagement baseline

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- PUBLISH_BLOCKED_COVER_QA (cover only; editorial ready)

### Keep
- **phone_scammers_notary** hook: local Tyumen casus (4,3 млн restitution) + federal contrast (ВС 1,9 млн, Красноуфимск устояла) + «~40%» scoped to notarial subset only.
- Comment magnet on buyer decision at signing (phones, elderly seller) — Dzen engagement bomb aligned.
- Scout constraint: не утверждать нотариальное удостоверение в тюменском кейсе — credibility preserved.

### Change
- Scout bank: tag `phone_scammers_notary` as high-stakes vtorichka P0; pair with buyer-intent Wordstat (купить квартиру тюмень) not «нотариус» tail alone.
- Description/cover hook: lead with money+суд outcome (4,3 млн) before «нотариус» keyword — matches title-brief and avoids misleading slug.

### Never again
- Не смешивать Назарову (агентство СОВА) с нотариальным делом Ольги в одном абзаце без явного контраста.
- Не обещать «нотариус защитит» — hook is skepticism + практика для покупателя.

### Proposed apply
- Add `phone_scammers_notary` to scout/klyshin-topic-bank notes as validated B10 angle (review-only in content-lessons; scout skill update only after human).
- After Metrika credentials fixed + publish — measure Dzen comments on comment_magnet question.

### Durable applied
- none (editorial pattern validated once; Metrika feedback pending)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil-prodazhu-prodavca
publish_status: BLOCKED (cover_qa only)
