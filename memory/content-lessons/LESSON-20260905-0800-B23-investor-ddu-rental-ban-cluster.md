## LESSON-20260905-0800-B23-investor-ddu-rental-ban-cluster
status: proposed
topic_id: B23
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-agent-report.json
  finding: new cluster `newbuild_investor_ddu_rental_ban_before_keys_tyumen`; story_dup PASS vs B22 (ставка ипотеки перед ДДУ), B21 (кладовка), B20 (смена юрлица), B19 (семейная ипотека/эскроу), Sep 2 paid uступка refusal; plot = инвестор бронирует лот под арендный доход → в проекте ДДУ запрет сдачи до акта + обязательный сервис аренды/УК + согласие на переуступку → отказ от подписания → невозвратная бронь.
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: context «новостройки тюмень» 4660; **final P0 «купить новостройку в тюмени» regions 55+11176 freq 856** (compare RU225 1867); weak angles отсечены — семейная ипотека 30 (B19), KP 64, mortgage-heavy 100 (B22 overlap).
- artifact: research-notes.md
  finding: casus modeled (не репортаж); firewall — запрет до акта ≠ автоматически незаконно; ломает модель связка post-keys УК/комиссия/переуступка; 2026 УК-initiative = законопроект, не норма; interlink B19/B21/B20 sibling plots.
- artifact: quality-bar-9.json
  finding: `all_pass: true`, `comment_magnet_question: true`, `no_tldr_opening: true`, `spine_once_no_recap: true`, word_count 2025, 4 sibling interlinks, 6 H2, 7 inline figures.
- artifact: cover/cover_qa.json
  finding: PASS with `ocr_false_positive_escape` (B08/B09/B15 pattern); short hook 5 words «Аренду запретили — бронь сгорела»; no cover-budget exhaust.
- artifact: wp-publish-result.json
  finding: publish PASS post **9723**, live-page PASS, 7 inline uploads, categories dokumenty-i-oformlenie / riski-sdelki / pokupka-kvartiry.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет ingest; behavioral baseline для post 9723 недоступен)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0, no behavioral baseline)

### Keep
- Wordstat rework: при investor-intent — buyer P0 «купить новостройку в тюмени» 856, не generic «новостройки тюмень» 4660 как locked P0; support «сдавать квартиру в аренду в новостройке» 55 (RU225) — secondary hook, не P0.
- Plot differentiation: аренда/инвесторская доходность в ДДУ vs mortgage-rate (B22), escrow/legal entity (B20/B19), defects/delay/кладовка (B21) — отдельный investor-rental cluster.
- Dzen news-casus: agency ending (ДДУ до брони, второй застройщик); comment magnet «законно или крючок»; plain-language разбор «до акта ≠ запрет навсегда» без sugar happy ending.
- Cover: short 5-word hook + OCR escape без budget exhaust — продолжение live canon (см. B15/B20 proposed).

### Change
- Scout: добавить `newbuild_investor_ddu_rental_ban_before_keys_tyumen` в `shared/scout-story-clusters.json` (sync-used-clusters не ловит newbuild-кластеры по regex) — needs-human.
- После Metrika credentials: cohort `cluster:newbuild_investor_ddu_rental_ban_before_keys_tyumen` vs B22 mortgage / B20 escrow siblings по time-on-page и CTA clicks.

### Never again
- Смешивать B23 с блокировкой ипотеки/ставки перед ДДУ (B22).
- Смешивать B23 с эскроу/юрлицом/семейной ипотекой (B19/B20).
- Утверждать «любой запрет аренды в ДДУ ничтожен» или ссылаться на несуществующую практику ВС РФ.
- Считать дефицит аренды в Тюмени гарантией ставки в конкретном ЖК через 2 года.

### Proposed apply
- `memory/scout/used-clusters.json`: lock `newbuild_investor_ddu_rental_ban_before_keys_tyumen` until 2026-10-05 (B23 ledger).
- Scout story-cluster registry entry (human): required_groups инвестор + аренда/наём в ДДУ + бронь сгорела/отказ от подписания.

### Durable applied
- memory/scout/used-clusters.json — добавлен cluster row B23 (content-learner 2026-09-05); rollback: удалить row при erroneous lock

### Resolution
status: recorded
article_dir: memory/blog/articles/B23-v-tyumeni-investor-kupil-novostrojku-pod-sdachu-v-ddu-zapretili-arendu-do-klyuch
wp_post_id: 9723
