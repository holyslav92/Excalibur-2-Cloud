# Scout handoff — B33

**topic_id:** B33  
**run_date:** 2026-09-28  
**slot:** 17:00 Asia/Yekaterinburg  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень  
**status:** LOCKED

## Topic

**cluster_id:** `newbuild_mandatory_partner_finishing_before_escrow_tyumen`

**Title draft / H1 direction:**

> В Тюмени за 4 дня до ДДУ застройщик привязал чистовую к подрядчику — без допсоглашения эскроу не открыли

**slug:** `za-4-dnya-do-ddu-zastrojschik-privyazal-chistovuyu-k-podryadchiku-bez-dop-soglasheniya-eskrou`

**article_dir:** `memory/blog/articles/B33-za-4-dnya-do-ddu-zastrojschik-privyazal-chistovuyu-k-podryadchiku-bez-dop-soglasheniya-eskrou`

**P0:** «новостройки тюмень» — **4350** (регионы 55+11176); сравнение RU 225 — **8246**  
**Wordstat source:** live MCP-KV Wordstat

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: stopped_before_money
newbuild_mechanism: семья с детьми покупает квартиру в новостройке Тюмени с обещанной чистовой в брони; за 4 дня до ДДУ застройщик выдаёт отдельный договор на отделку только у «партнёрского» подрядчика (~520–580 тыс. ₽), не включённый в цену ДДУ; банк при ипотеке требует прозрачности обязательств перед открытием эскроу — без подписания допсоглашения или отказа от подрядчика счёт не открывают, сделку останавливают до перевода денег
why_newbuild_not_secondary: только цепочка новостройки — бронь, ДДУ, навязанный подрядчик отделки, банк и эскроу; нет продавца вторички, ЕГРН-сюрпризов, наследников, опеки или соседской доли
klyshin_hook: optional | none | original: none | signal: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: 17 active locks 2026-09-28; исключены сегодняшние созаёмщик/второй санузел/ЕИСЖС и перечисленные в cron forbidden angles
dzen_casus_shape: PASS | event: семья выбрала трёшку «с чистовой по прайсу» в новостройке Тюмени | risk: отдельный договор с подрядчиком вне ДДУ = скрытый платёж сотни тысяч; банк может не открыть эскроу; отказ грозит потерей брони | time: за 4 дня до подписания ДДУ и открытия эскроу | finale: банк поставил сделку на паузу; семья отказалась от договора с подрядчиком; бронь вернули частично (~80%); ДДУ не подписали, эскроу не открывали
comment_magnet_angle: «Если чистовую можно купить только у “партнёра” за полмиллиона сверх ДДУ — вы подпишете допсоглашение или снимете бронь, даже если квартира “горит”?»
wordstat_rework: probe «отделка новостройка тюмень» → 23; probe «новостройки тюмени от застройщика с отделкой» → 11; probe «эскроу счет новостройка» → 1; rework → demand spine «новостройки тюмень» 4350 с механикой навязанной чистовой в H1
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» → 4350 (55+11176) | RU «новостройки тюмень» → 8246 (225)
story_dup_check: PASS | cluster_id: newbuild_mandatory_partner_finishing_before_escrow_tyumen
h1_fingerprint_check: PASS | fingerprint: four_days_before_DDU + mandatory_partner_finishing_addendum_blocked_escrow
formula_spam_check: PASS | last3_mechanisms: escrow co-borrower; second bathroom appendix mismatch; EISZHS construction stop — текущий угол: навязанный подрядчик чистовой до эскроу
anti_dupe_hard: PASS
```

## Demand probes

| Запрос | Регионы | Результат |
|---|---|---:|
| новостройки тюмень | 55,11176 | 4350 |
| новостройки тюмень | 225 | 8246 |
| купить новостройку в тюмени | 55,11176 | 891 |
| ремонт новостроек тюмень | 55,11176 | 270 |
| отделка новостройка тюмень | 55,11176 | 23 |
| новостройки тюмени от застройщика с отделкой | 55,11176 | 11 |

## signal_urls

- {{SITE_BASE}}/blog/
- https://dzen.ru/holyslav
- https://www.domrf.ru/
- https://www.consultant.ru/document/cons_doc_LAW_51040/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A (не использован)

## Research angles

1. Как в типовом ДДУ и приложениях фиксируется отделка: входит в цену, опция, отдельный договор.
2. Почему банк может задержать открытие эскроу при параллельных обязательствах с подрядчиком вне ДДУ.
3. Условия возврата брони при отказе от «партнёрской» отделки (удержания, сроки).
4. Различие «чистовая в брони» vs формулировки в проекте ДДУ и допсоглашении.
5. Локальный контекст Тюмени: семьи с детьми, ипотека на новостройку, stakes до перевода на эскроу.

## Anti-dupe record (2026-09-28)

- 09:00 — созаёмщик до эскроу  
- 12:00 — второй санузел в приложении к ДДУ  
- 15:00 — приостановка в ЕИСЖС до эскроу  
- **17:00 B33** — навязанный подрядчик чистовой, эскроу не открыли  
