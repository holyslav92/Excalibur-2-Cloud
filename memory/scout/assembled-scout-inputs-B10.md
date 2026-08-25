# Scout assembled inputs — B10 (2026-08-25)

**CRITICAL:** Ты уже вызван через `excalibur_blog_derouter_opus_chat.py --role scout`. НЕ запускай shell и НЕ пиши BLOCKER. Верни **только** полный markdown handoff (YAML frontmatter + body). Cursor запишет твой ответ в `.cursor/excalibur-blog-handoff.md`.

## Run context
- run_date: 2026-08-25
- tenant: The Риэлтор, Тюмень
- topic_id: B10
- dzen_rf_pack: true (rules read)

## Selected hook (triple gate PASS)
- hook_id: phone_scammers_notary
- original Klyshin: «Нотариус не спасает от мошенников. И теперь это подтверждают цифры»
- angle: телефонные мошенники давят на пожилого продавца; нотариус удостоверяет сделку; суд потом отменяет — исследование: из нотариальных сделок с телефонным мошенничеством устояли только 40%
- klyshin_signal_url: https://t.me/klyshin_A (post Aug 2026: 40% notarial deals fail vs phone fraud; notary ≠ psychiatrist; elderly seller under remote control)
- rejected_hooks: matkapital_child_shares (39% overlap LIVE-NA-MATKAPITAL), summons_registration_stop (64% overlap LIVE-AVANS-POVESTKA), tired_buyer (38% overlap LIVE-TRI-MESYACA), notary_70k generic (40% overlap LIVE-NOTARIUS)

## Title draft (Klyshin news headline rhythm)
Сделку у нотариуса провели — а суд отменил: продавца месяцами вели мошенники по телефону

## slug_hint
sdelku-u-notariusa-proveli-sud-otmenil-moshenniki-po-telefonu

## article_dir
memory/blog/articles/B10-sdelku-u-notariusa-proveli-sud-otmenil-moshenniki-po-telefonu

## localize
Casus city = Тюмень (tenant); H1 без дублирования live WP slug «v-tyumeni-notarius-udostoveril…» — другой plot (телефонные мошенники vs generic seller return 4,3 млн).

## dzen_casus_shape (Scout pre-fill — Derouter must keep PASS)
- event: нотариальная сделка с квартирой в Тюмени прошла «чисто», покупатель внёс расчёт
- risk: телефонное мошенническое давление на пожилого продавца; нотариус не видит скрытую волю
- time: «через полгода после регистрации»
- safe_person: покупатель и банк считали нотариальную форму достаточной защитой
- finale: суд отменил регистрацию / сделку оспорили; деньги и квартира — спор
- dzen_casus_shape: PASS

## comment_magnet_angle
«Нотариальная сделка — это броня или иллюзия, если продавца вели по телефону?»

## Wordstat preflight
wordstat_get_user_info OK (MCP-KV Yandex Cloud, folder b1g6bq34gkivjj20be06)

## Wordstat live probes (regions 55+11176 unless noted)
| probe | Tyumen 55+11176 | RU 225 |
|-------|-----------------|--------|
| «мошенники при покупке квартиры» | 1 | — |
| «юридическая проверка квартиры» | 5 | — |
| «проверка квартиры перед покупкой» | 8 | 1872 |
| «купить квартиру в тюмени» | 22652 | 39858 |

## wordstat_rework log
probe «мошенники при покупке квартиры» 1 → probe «юридическая проверка квартиры» 5 → rework «проверка квартиры перед покупкой» 8 (RU225 1872) → final P0 «купить квартиру в тюмени» 22652 (RU225 39858)

## wordstat final line
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени» 22652 | secondary «проверка квартиры перед покупкой» 8 (RU225 1872) | sticker «юридическая проверка квартиры» 5

## story_dup check
scout_helper --check-query PASS (2026-08-25): NO CANNIBALIZATION, TOPIC FOCUS PASS, STORY DUP PASS

## signal_urls (today)
1. https://t.me/klyshin_A — post «Нотариус не спасает от мошенников» (40% notarial deals fail; phone fraud on elderly sellers)
2. https://dzen.ru/holyslav — fresh casus «Скидка в 3 млн скрыла ПНД» (Tyumen elderly seller risk context)
3. https://t.me/holyslav92 — tenant channel
4. {{SITE_BASE}}/blog/ — site blog

## wp_category hint
vtorichka-i-riski (legal risk secondary market)

## Output instruction for Derouter
Write complete `.cursor/excalibur-blog-handoff.md` with YAML frontmatter (role, topic_id, article_dir, status PASS, completed_at ISO, incident_report none) and body marker `=== EXCALIBUR BLOG SCOUT ===` including ALL required fields:
topic_id, title_draft, slug_hint, primary_query, external_signal, signal_urls, klyshin_hook, wordstat_preflight, dzen_casus_shape, comment_magnet_angle, wordstat_rework, wordstat, story_dup_check, wp_category_slugs, research_angle, incident_report none.
