# Scout inputs — 2026-08-28 (B12)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-28 (YEKT Friday, slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → **16 active locks**
- Closed clusters (30d): illegal_renovation_rosreestr_blocks_registration (B11), marital_share_heirs_notary_checked, court_took_apartment_relatives_contested, matkapital_opieka_kids_cancel_3y, elderly_seller_led_by_phone, seller_bankruptcy_finmanager_clean_egrn, pnd_3mln_discount, military_summons_stopped_registration, four_months_search_yellow_opinion_lawyers_refused, grandma_owner_missing_viewing_old_poa, egrn_line_blocks_advance, deceased_spouse_share_surprise, inheritance_son_first_marriage_no_refusal, discount_two_million_hidden_risk, doverennost_svo_seller, deposit_before_auction
- Live WP ~20 titles fetched 2026-08-28 via wordpress_get_posts (includes B11 «открытая кухня», Ялуторовск «продали двоим» short — **NOT** our cluster; B12 = эскроу/ДДУ/ключи)
- `shared/published-titles.md` + ledger B02–B11

## Proposed topic (pre-check PASS pending scout_helper)

- **topic_id:** B12
- **title_draft:** В Тюмени раскрыли эскроу — ключи так и не передали
- **slug:** v-tyumeni-raskryli-eskrou-klyuchi-tak-i-ne-peredali
- **cluster_id (new):** escrow_unlocked_keys_not_delivered_ddu
- **story_dup_check:** PASS — другой legal plot: новостройка/ДДУ/эскроу раскрыт по разрешению на ввод, просрочка передачи ключей; NOT вторичка/ЕГРН/наследство/двойная продажа

## Dzen news-casus shape (target PASS)

- **event:** семья купила квартиру в тюменской новостройке по ДДУ с эскроу-счётом; после получения разрешения на ввод банк раскрыл эскроу и перевёл деньги застройщику
- **risk:** эскроу защищает до ввода дома, но не удерживает деньги до фактической передачи ключей; просрочка по дате в ДДУ
- **time:** почти три месяца после срока в договоре (прецедент: Калининский суд Тюмени, ООО «Клевер Строй», ключи вместо 31.12.2023 выдали 18.03.2024); актуальность август 2026 — мораторий на неустойку снят с 01.01.2026
- **finale:** суд частично удовлетворил иск — взыскал убытки (аренда), моральный вред, судебные расходы (~109 тыс. суммарно по делу); покупательница ждала ключи, снимая жильё
- **comment_magnet_angle:** «Эскроу защищает деньги только до разрешения на ввод — вы бы подписали ДДУ, не зная даты ключей в тексте?»

## Klyshin hook

- **klyshin_hook:** none (свежий Tyumen casus без Klyshin — предпочтительно; не дублируем закрытые кластеры)
- **signal_urls (tenant):** https://dzen.ru/holyslav | https://t.me/holyslav92 | {{SITE_BASE}}/blog/ | klyshin_A optional — not used

## Wordstat MCP-KV (live 2026-08-28)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

| probe | regions | freq |
|-------|---------|------|
| неустойка с застройщика | 55+11176 | 50 |
| неустойка с застройщика | 225 | 3645 |
| дду тюмень | 55+11176 | 37 |
| эскроу счет | 55+11176 | 811 (top: счет эскроу) |
| новостройки тюмень | 55+11176 | 4717 |
| купить новостройку в тюмени | 55+11176 | 830 |
| неустойка с застройщика в 2026 | 225 | 502 |

**wordstat_rework log:**
- probe «неустойка с застройщика» 50 (55+11176) → слабый локальный объём, но тема горячая после снятия моратория 01.01.2026
- probe «дду тюмень» 37 → слабый
- probe «эскроу счет» 811 (55+11176) → buyer spine по механике риска
- **final P0:** «новостройки тюмень» **4717** (55+11176); compare RU225 «неустойка с застройщика» **3645**; secondary spine «эскроу счет» **811**

## Research signal URLs (checked)

- https://tumentoday.ru/2025/02/03/v_tyumeni_sud_vzyskal_s_zastroyshchika_100_tysyach_rubley_za_zaderzhku_sdachi_doma/ — тюменский суд, Клевер Строй, задержка ключей ~3 мес
- https://harant.ru/blog/nedvizhimost/eskrou-schyot-raskryt-a-kvartiry-net-pravovaya-kolliziya-o-kotoroj-molchat/ — раскрытие эскроу ≠ передача квартиры
- https://nedvizhimosticeny.ru/moratoreeyi-otmyenyen-dolsheekam-vyernut-dyengee/ — отмена моратория неустойки 2026, Тюменская область
- https://dzen.ru/a/aoMNZq3UpQP2T6uq — prior tenant dzen on escrow mechanics (не дублировать how-to; наш угол = casus с финалом)

## Output required

Write `memory/scout/scout-handoff-B12.md` with all Scout handoff fields per SKILL.md:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS, comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS + cluster_id, topic_id, title_draft, slug, signal_urls.

Lock topic_id B12 for Research.
