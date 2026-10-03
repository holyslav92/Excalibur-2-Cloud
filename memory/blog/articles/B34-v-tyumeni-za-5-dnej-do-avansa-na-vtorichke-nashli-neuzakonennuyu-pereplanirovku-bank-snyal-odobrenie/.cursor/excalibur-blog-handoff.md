# Scout handoff — B34 — 2026-10-03 15:00 YEKT

**slot_rubric:** vtorichka (owner `rubric_per_slot` — `shared/slot-rubric-lock.md`, NOT newbuild-only for this slot)

## Topic lock

| field | value |
|-------|-------|
| topic_id | B34 |
| title_draft | В Тюмени за 5 дней до аванса на вторичке нашли неузаконенную перепланировку — банк снял одобрение |
| slug | v-tyumeni-za-5-dnej-do-avansa-na-vtorichke-nashli-neuzakonennuyu-pereplanirovku-bank-snyal-odobrenie |
| cluster_id | secondary_illegal_redevelopment_bti_mismatch_tyumen |
| viral_mechanism | almost lost перед ключами/деньгами |
| top_energy_mirror | paper_clean_then_broke |

## Casus (dzen_casus_shape: PASS)

- **event:** семья с одобренной ипотекой выбирает трёшку на вторичке в Тюмени; ремонт «евро», кухня и гостиная визуально объединены  
- **risk:** план БТИ не совпадает с фактом → отказ регистрации, штрафы, демонтаж; банк снимает одобрение  
- **time:** за 5 дней до планового аванса, после повторного замера  
- **finale:** банк снял одобрение; продавец предлагал скидку и «узаконим после» — аванс не внесли  
- **comment_magnet_angle:** «Если ремонт красивый, а в БТИ план старый — внесли бы аванс под обещание узаконить или остановили сделку?»

## Wordstat

wordstat_preflight: mcp-kv wordstat_get_user_info OK  
wordstat_rework: niche «перепланировка» weak → anchor «вторичка в тюмени»  
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «вторичка в тюмени» 5459 (55+11176) / RU 9750 (225)

## Anti-dupe

anti_repeat_preflight: live_blog_20 + used-clusters sync OK  
story_dup_check: PASS | cluster_id: secondary_illegal_redevelopment_bti_mismatch_tyumen  
h1_fingerprint_check: PASS  
formula_spam_check: PASS  
anti_dupe_hard: PASS

klyshin_hook: none
