# Scout handoff — B33

**status: LOCKED**

- `run_date`: 2026-09-23
- `slot`: ~10:00 YEKT
- `tenant`: The Риэлтор / Святослав Шакин, Тюмень
- `topic_market_focus`: newbuild_only
- `topic_id`: B33
- `cluster_id`: `newbuild_co_borrower_refused_three_days_before_escrow_tyumen`

## Final topic

**H1 / title:**  
**За 3 дня до эскроу созаёмщик отказался подписывать — банк заморозил ипотеку на новостройку в Тюмени**

- `slug`: `za-3-dnya-do-eskrou-sozaemschik-otkazalsya-bank-zamorozil-ipoteku-novostrojka-tyumen`
- `top_energy_mirror`: `clock_ran_out / stopped_before_money`
- `newbuild_mechanism`: семья покупает строящуюся новостройку в Тюмени по ДДУ; ипотека оформляется на двух созаёмщиков. За 3 дня до открытия эскроу один из них отказывается подписывать комплект документов. Банк приостанавливает ипотечную сделку, эскроу не открывается, бронь около 50–90 тыс. ₽ оказывается под угрозой.
- `why_newbuild_not_secondary`: сюжет строится только вокруг ДДУ, эскроу, ипотеки на строящийся объект и сделки с застройщиком. Вторичный рынок не используется.
- `klyshin_hook`: none
- `klyshin_signal`: none

## Dzen news-casus shape

`dzen_casus_shape: PASS`

- `event`: за 3 дня до планового открытия эскроу созаёмщик отказался подписывать ипотечный комплект.
- `risk`: банк заморозил одобрение; эскроу не открыт; бронь новостройки и сроки сделки оказались под угрозой.
- `time`: последние 3 дня до открытия эскроу.
- `finale`: покупка не считается завершённой до повторного согласования состава заёмщиков и документов банком; деньги на эскроу не ушли.
- `editorial_status`: composite editorial casus на основе проверенной типовой банковской механики; не выдавать его за отдельный подтверждённый репортаж о конкретной семье.

`comment_magnet_angle:`  
**Если второй созаёмщик перед эскроу «передумал» — банк успеет заменить его или покупку новостройки придётся откладывать?**

## Wordstat

`wordstat_preflight: mcp-kv wordstat_get_user_info OK`

`wordstat: mcp_kv live | regions 55,11176,compare225`

| Запрос | Тюмень, 55 | Область, 11176 | РФ, 225 |
|---|---:|---:|---:|
| купить новостройку в Тюмени | **679** | **902** | **1914** |

Дополнительные buyer/mechanism-запросы:

| Запрос | Регион | Частота |
|---|---|---:|
| ипотека Тюмень новостройки от застройщика | 55 | **66** |
| квартира в ипотеку в Тюмени новостройки | 55 | **65** |

`wordstat_rework:`  
probe «ипотека Тюмень новостройки от застройщика» — **66** → усилен buyer-spine «купить новостройку в Тюмени» → final P0 «купить новостройку в Тюмени» — **679** в Тюмени / **902** в области / **1914** по РФ.

`final_p0:`  
**купить новостройку в Тюмени — 679 / 902 / 1914**

## Anti-repeat gates

- `anti_repeat_preflight`: live blog anti-dupe + ledger sync выполнены.
- `sync_status`: `excalibur_blog_scout_story_dup.py --sync-used-clusters` — OK.
- `live_blog_skips`: potolki/show-room, kladovaya, za-5-dney bank vznos, okna dvor, sdacha sdvinula.
- `closed_clusters`: закрытые кластеры из live sync; перечисленные выше сюжеты исключены.
- `story_dup_check`: **PASS**
- `h1_fingerprint_check`: **PASS**
- `fingerprint`: `co_borrower_refused_three_days_escrow_frozen`
- `formula_spam_check`: **PASS**
- `last3_mechanisms`: B32 — escrow beneficiary; B31 — insurance; B30 — assignment.
- `anti_dupe_hard`: **PASS**
- `scout_helper_check`: **PASS** — anti-dupe + topic focus.
- `newbuild_focus_check`: **PASS** — только новостройка, ДДУ, эскроу и ипотека от застройщика.

## Editorial guardrails

1. Не превращать материал в спокойный чеклист или общий ипотечный гайд.
2. Не переносить сюжет на вторичное жильё.
3. Не утверждать, что конкретная семья и конкретный банк подтверждены публичным репортажем.
4. Финал должен показать: до повторного решения банка эскроу не открыт, а сделка с новостройкой зависла.
5. Сохранять спорный вопрос для комментариев: можно ли заменить созаёмщика в последние дни и кто несёт риск брони.
