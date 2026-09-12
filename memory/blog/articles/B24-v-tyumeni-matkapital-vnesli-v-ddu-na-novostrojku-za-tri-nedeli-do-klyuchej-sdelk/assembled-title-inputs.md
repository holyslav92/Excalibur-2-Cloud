# Assembled title inputs — B24 TITLE UPDATE (for Derouter title role)

**TASK:** TITLE UPDATE only — fix H1 for article-quality-score gate. Current H1 FAIL: `h1: no number or deadline in H1`.

**Current H1 (FAIL):** «В Тюмени ДДУ с маткапиталом остановили — доли детям не оформили»

**REQUIRED:** New H1 must include **number or deadline** (e.g. «3 недели до ключей», «за 21 день до ключей»). Keep subject (ДДУ + маткапитал + детские доли), Klyshin news-casus rhythm, consequence in second beat. No SEO tail. ~50–70 chars. Preserve `slug`, `slug_confirmed`, `comment_magnet_angle` unless sharper variant.

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output **only** valid JSON for `title-brief.json` per SKILL.md schema. One variant. `verdict: PASS`.

**topic_id:** B24  
**slug (locked):** v-tyumeni-matkapital-vnesli-v-ddu-na-novostrojku-za-tri-nedeli-do-klyuchej-sdelk  
**market_focus:** newbuild_only (Тюмень, новостройка, ДДУ, маткапитал, семейная ипотека)

## Scout handoff (2026-09-08)

- **klyshin_hook:** none (fresh Tyumen newbuild casus without Klyshin)
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** маткапитал + семейная ипотека на ДДУ новостройки — обязательство выделить доли детям не зафиксировано в договоре; СФР/банк блокируют регистрацию за 3 недели до ключей
- **why_newbuild_not_secondary:** цепочка ДДУ/застройщик/эскроу/ипотека на новостройку; не B18 (вторичка, детские доли в ЕГРН продавца)
- **dzen_casus_shape:** PASS
  - event: семья в Тюмени купила новостройку с маткапиталом и семейной ипотекой; деньги на эскроу, дом сдан
  - risk: маткапитал использован, но обязательство выделить доли детям не зафиксировано в ДДУ/приложениях/заявлении СФР; банк блокирует регистрацию права
  - time: за три недели до акта приёмки и ключей
  - finale: сделку остановили; допсоглашение через юриста; ключи перенесли на месяц; риск возврата маткапитала
- **comment_magnet_angle (scout):** «Доли детям — прямо в ДДУ или отдельным соглашением до подписания: где бы вы поставили красную линию, если ключи уже «на подходе»?»
- **anti_dupe_hard:** PASS — distinct from B18, B19

## Wordstat demand spine (MCP-KV live 2026-09-08)

- P0: «новостройки с маткапиталом» — **175** (regions 55+11176)
- mechanism: «выделение долей детям маткапитал» — **872** (RU 225)
- supporting: «маткапитал новостройка» 349; «маткапитал ипотека новостройка» 102
- **Do NOT paste raw SEO phrase into H1.** Spine under news headline.

## Research casus (from research-notes.md)

- Семья с детьми, семейная ипотека, маткапитал в первоначальный взнос, ДДУ зарегистрирован, эскроу открыт, дом сдан
- За ~3 недели до ключей: расхождение в пакете документов о будущих детских долях между ДДУ, кредитным пакетом и СФР
- Банк приостановил регистрацию права; СФР не согласовал; застройщик не переподписал ДДУ бесплатно
- Ключи перенесли ~на месяц; modeled composite Tyumen casus (no real ЖК/банк names in H1)

## Published titles (anti-dup only — do not copy)

| topic_id | title |
|----------|-------|
| B19 | В Тюмени ипотеку одобрили — эскроу сорвал маткапитал |
| B22 | В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела |
| B23 | В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты |
| B12 | Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась |

**B24 must differ:** stop **before keys** because of **child shares / matkapital in DDU**, not escrow-at-approval (B19), not rate hike (B22), not apartments (B23).

## Scout title_draft (starting point — refine if sharper)

В Тюмени маткапитал внесли в ДДУ на новостройку — за три недели до ключей сделку остановили

## Title rules reminder

- Klyshin news-casus rhythm: completed event + contradiction + consequence
- Clear subject: маткапитал / ДДУ / новостройка / детские доли
- ~50–70 chars preferred; em dash OK; Tyumen when it strengthens
- FORBIDDEN: checklist, N steps, SEO tail, «2026», colon+keyword, label heads
- One JSON object only
