# Scout inputs — 2026-09-05 (B23)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-05 (YEKT Saturday weekend automation slot)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-05)
- **FROZEN — DO NOT reuse plot (user + live WP Sep 1–4):**
  - B16 tranche mortgage «как аренда» 10800→86000 (gold stylo; Aug 31 live «платёж вырос в 8 раз»)
  - wet-screed приёмка (2026-09-01 live «мокрая стяжка — ключи не выдали»)
  - B20 `newbuild_developer_legal_entity_change_ddu_escrow_tyumen`
  - B21 `newbuild_ddu_cellar_paid_not_handed_tyumen`
  - B22 `newbuild_mortgage_rate_changed_before_ddu_tyumen` + live rate hike Sep 4
  - bank revoked approval 72h before DDU (Sep 3)
  - finish mismatch чистовая vs предчистовая (Sep 3)
  - keys delay 8mo + certificate instead of penalty (Sep 3)
  - area mismatch at keys (Sep 3)
  - DDU installment hike before handover (Sep 2)
  - KP no gas/water at keys (Sep 2)
  - assignment refused after payment (Sep 2)
  - land category mortgage block for KP house (Sep 4)
  - wrong escrow account / перевод на чужой счёт (Sep 4)
  - acceptance act defects demanded signing (Sep 4)
  - price +380k after booking (Sep 1)
  - B19 family mortgage escrow matkapital
  - B12 keys delay + escrow frozen
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек)
- `excalibur_blog_scout_story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B23
- **title_draft:** В Тюмени одобрили ипотеку на новостройку — банковская оценка оказалась ниже цены в ДДУ
- **slug:** v-tyumeni-odobrili-ipoteku-na-novostroyku-ocenka-banka-nizhe-ceny-ddu
- **cluster_id (new):** newbuild_bank_appraisal_below_ddu_price_tyumen
- **story_dup_check:** PASS — distinct from B22 rate change; distinct from Sep 3 approval revocation; distinct from Sep 1 price hike after booking; distinct from Sep 3 area mismatch (метры vs оценка); plot = ипотека одобрена, бронь оплачена, банк заказал оценку перед выдачей/ДДУ, отчёт оценщика ниже цены в ДДУ → кредит только на % от оценки → разрыв 300–500 тыс. ₽, семья не собрала за 5–7 дней, бронь сгорела

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке, банк одобрил ипотеку и зафиксировал сумму кредита от цены в договоре бронирования
- **risk:** перед подписанием ДДУ банк потребовал отчёт об оценке — оценщик указал рыночную стоимость ниже цены застройщика в ДДУ (например на 350–450 тыс. ₽); банк пересчитал лимит кредита от оценки, а не от ДДУ — не хватило первоначального взноса и собственных средств
- **time:** за 5–7 дней до подписания ДДУ, после 2–3 недель одобрения и оплаченной брони
- **finale:** семья не успела найти разницу / застройщик не снизил цену; ДДУ не подписали, бронь сгорела, оплата за оценку (~3–5 тыс. ₽) не вернулась; лот ушёл в продажу
- **comment_magnet_angle:** «Одобрение есть, а оценка ниже ДДУ — вы бы за неделю нашли недостающие деньги или развернулись, даже если бронь сгорит?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild bank-appraisal casus without Klyshin — preferred; avoids mortgage-rate / revocation / escrow / acceptance clusters)

## Wordstat MCP-KV (live 2026-09-05)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55+11176 | 4683 (context only) |
| ипотека в тюмени на новостройки | 55+11176 | 41 (broader; loses appraisal spine) |
| оценка новостройки для ипотеки | 55+11176 | 3 (weak) |
| оценка квартиры для ипотеки новостройка | 55+11176 | 1 (weak) |
| **оценка квартиры для ипотеки** | **55+11176** | **24** |
| оценка квартиры банком для ипотеки | 55+11176 | 10 (child) |
| оценка квартиры для ипотеки | 225 (compare) | 1578 |
| оценка квартиры в новостройке для ипотеки | 225 (compare) | 125 |
| ставка ипотеки новостройка | 55+11176 | 54 (rejected — B22 cluster) |
| эскроу счет новостройка | 55+11176 | 2 (rejected — B19/B20) |
| новостройки в рассрочку | 55+11176 | 18 (rejected — alternate plot; Sep 2 DDU installment hike overlap risk) |
| траншевая ипотека новостройка | 55+11176 | 4 (rejected — B16 frozen) |

**wordstat_rework log:**
- probe «оценка новостройки для ипотеки» 55+11176 → 3 (weak newbuild-specific)
- probe «оценка квартиры для ипотеки новостройка» 55+11176 → 1 (weak)
- probe «ипотека в тюмени на новостройки» 55+11176 → 41 (higher volume but loses appraisal-gap spine)
- probe «новостройки в рассрочку» 55+11176 → 18 (alternate plot rejected — installment cluster risk)
- probe «ставка ипотеки новостройка» 55+11176 → 54 (rejected — B22 rate-change cluster)
- **rework:** localize Tyumen + newbuild buyer jargon (ипотека, ДДУ, оценка банком) → **final P0 «оценка квартиры для ипотеки» regions 55,11176 freq 24** (compare RU225 1578; child RU «оценка квартиры в новостройке для ипотеки» 125)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст ипотеки на новостройки; не дубль кластера
- https://www.cbr.ru/finmarkets/supervision/svps/ — нормативная база оценки залога (контекст)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B23, title, slug, signal_urls, research angles for Research role.
