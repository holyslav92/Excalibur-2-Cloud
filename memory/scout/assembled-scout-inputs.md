# Scout inputs — 2026-09-26 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-26 (YEKT weekday slot — Scout automation)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — recent live ~20)

- NO planning 54→49 m² (2026-09-26)
- NO act acceptance −1.8 m² vs DDU (2026-09-26)
- NO KP 12 sotok→8 kadastr (2026-09-25)
- NO partial commissioning section (2026-09-25)
- NO parking separate DDU (2026-09-25)
- NO developer killed assignment / investor (2026-09-25)
- NO last floor mortgage revoked (2026-09-24)
- NO matkapital SFR escrow (2026-09-24)
- NO kindergarten on render (2026-09-24)
- NO child 7 years family mortgage (2026-09-23)
- NO KP forest strip / neighbor fence (2026-09-23)
- NO furniture package partner (2026-09-23)
- NO frozen clusters in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-26)
- Live WP recent: see EXCALIBUR_RECENT_WP_POSTS 2026-09-26 run
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B33
- **title_draft:** За 6 дней до ДДУ в Тюмени в брони обещали остеклённую лоджию — в договоре холодный балкон, банк урезал ипотеку
- **slug:** za-6-dnej-do-ddu-v-tyumeni-v-broni-obeschali-osteklyonnuyu-lodzhiyu-v-dogovore-holodnyj-balkon
- **article_dir:** memory/blog/articles/B33-za-6-dnej-do-ddu-v-tyumeni-v-broni-obeschali-osteklyonnuyu-lodzhiyu-v-dogovore-holodnyj-balkon
- **cluster_id (new):** newbuild_glazed_loggia_promised_cold_balcony_ddu_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья с ребёнком берёт трёшку в строящемся ЖК Тюмени в ипотеку. В брони и на планировке менеджер отметил «лоджия с остеклением, тёплый контур» и включил площадь лоджии в расчёт «полезных» метров. За 6 дней до подписания ДДУ юрист сверил приложение к договору: в спецификации — **неостеклённый балкон**, остекление «по желанию застройщика/подрядчика» отдельным договором ~280–320 тыс. ₽. Банк пересчитал залоговую стоимость без «тёплой» лоджии и **урезал одобренный лимит на ~450 тыс. ₽** — до эскроу не вышли, бронь 150 тыс. удержали частично (composite casus)
- **why_newbuild_not_secondary:** Сюжет в цепочке покупки квартиры в новостройке: бронь, приложение к ДДУ, спецификация отделки/балкона, ипотека на объект долевого строительства. Нет продавца вторички, ЕГРН, наследников или опеки
- **story_dup_check:** PASS — не пересекается с площадью 54→49 (планировка), акт −1.8 м² (приёмка), паркинг отдельный ДДУ, мебельный пакет, рендер детсада

## Dzen news-casus shape (target PASS)

- **event:** семья выбрала квартиру с «остеклённой лоджией» на стенде застройщика; в брони менеджер поставил галочку «остекление включено»
- **risk:** без остекления лоджия не входит в тёплый контур — меньше жилых метров, выше коммуналка/потери тепла; банк режет лимит; отдельный договор на остекление после ДДУ — ещё +300 тыс. вне ипотеки
- **time:** за 6 дней до назначенного подписания ДДУ и открытия эскроу
- **finale:** в проекте ДДУ — холодный балкон; застройщик предложил «подпишите, остеклим потом по акции»; банк снизил лимит; семья отказалась от ДДУ, эскроу не открывали, часть брони не вернули
- **comment_magnet_angle:** «Если в брони лоджия “с остеклением”, а в ДДУ — холодный балкон: вы доплачиваете из своих или рвёте сделку?»

## Klyshin hook

- **klyshin_hook:** none | original: none

## Wordstat MCP-KV (live 2026-09-26)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4326 |
| купить новостройку в тюмени | 55,11176 | 892 |
| купить новостройку в тюмени | 225 (compare) | 1928 |
| остекление лоджии новостройка | 55,11176 | 2 |
| приемка квартиры в новостройке тюмень | 55,11176 | 28 |
| дду новостройка тюмень | 55,11176 | API empty |
| управляющая компания новостройка | 55,11176 | 3 |

**wordstat_rework log:**
- probe «остекление лоджии новостройка» 55,11176 → 2 (too weak for P0)
- probe «дду новостройка тюмень» 55,11176 → empty
- probe «управляющая компания новостройка» 55,11176 → 3 (rejected alternate)
- **rework:** anchor buyer spine «новостройки тюмень» + mechanism остекление/лоджия в H1
- **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4326 (55+11176) / compare «купить новостройку в тюмени» 1928 (225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — проектные декларации, спецификации
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B33, title, slug, article_dir, signal_urls, research angles for Research role.
