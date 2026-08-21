# Scout assembled inputs — B08 slot 2026-08-21 12:00 YEKT

## Assignment
topic_id: B08
tenant: The Рiэлтор / Святослав Шакин / Тюмень
dzen_rf_pack: true (read and obey)

## Selected hook (NOT used in B01-B07)
hook_id: tired_buyer_bad_flat
original: «Клиенты все чаще готовы купить плохую квартиру. Просто потому что нормальных почти нет»
angle: усталость на рынке 3–4 месяца поиска → согласие на риск; риэлтор не «рисует безопасность», а детектор рисков
klyshin_signal: пост @klyshin_A август 2026 — «уставший покупатель — самый опасный»; ~10% негативных заключений; «сделайте так, чтобы безопасно купили» при невозможности безопасности
signal_url: https://t.me/klyshin_A

## Rejected hooks (why)
- matkapital_child_shares — live WP «na-matkapital-kupili-detskie-doli-proverte» (story cluster matkapital)
- summons_registration_stop — live WP «povestka-prodavcu-sdelka-vstanet»
- notary_not_shield_70k — live WP «notarius-vse-proveril-a-na-sdelke-cena-vyrosla-na-70-tysyach»
- five_court_schemes — overlap B03/B04 + matkapital on site
- phone_scammers_notary — weak buyer P0 after rework (мошенники 1)
- heirs/matkapital/svo/deposit/discount — used B02-B07

## Anti-dup
published B02-B07 in shared/published-articles.md
B07 cluster inheritance_son_first_marriage — DO NOT repeat
scout_helper --check-query: PASS (no cannibalization, topic focus pass)

## Wordstat preflight
wordstat_get_user_info: OK (MCP-KV Yandex Cloud API)

## Wordstat rework log (live MCP-KV, regions 55+11176)
probe «проверка квартиры перед покупкой» 9 (Tyumen) — weak legal jargon
probe «вторичка тюмень» 7867 → cluster «вторичка в тюмени» 5813
probe «новостройки тюмень» 4684
rework «купить квартиру в тюмени вторичка» 3965
final P0 «купить квартиру в тюмени» 22990 (RU225 compare 40318)

Stickers/H2 from rework: вторичка в тюмени 5813; проверка квартиры перед покупкой 9 (risk angle, not P0)

## Title draft (Klyshin rhythm — for handoff)
«Три месяца искали квартиру в Тюмени — и согласились на риск»
slug_suggestion: ustalis-iskat-kvartiru-soglasilis-na-risk

## External signals (today)
1. https://t.me/klyshin_A — live channel (автооценка + уставший покупатель posts)
2. https://t.me/holyslav92 — tenant personal Telegram
3. {{SITE_BASE}}/blog/ — site blog ledger B02-B07

## Write handoff to .cursor/excalibur-blog-handoff.md with required fields:
- topic_id B08
- title draft
- slug suggestion
- klyshin_hook line
- wordstat_rework line
- wordstat line (mcp_kv live)
- wordstat_preflight line
- external_signal summary
- signal_urls list
- story_dup_check result
