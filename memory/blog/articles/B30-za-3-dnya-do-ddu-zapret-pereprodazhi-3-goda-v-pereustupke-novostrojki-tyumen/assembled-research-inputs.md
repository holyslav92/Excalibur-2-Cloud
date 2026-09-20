# Assembled research inputs — B30 (for Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Do **NOT** output `DEROUTER RESEARCH BLOCKER` or refuse synthesis. Output the full `research-notes.md` body only per SKILL.md from the facts below (SERP/Wordstat already assembled for you).

**research_date:** 2026-09-20  
**topic_id:** B30  
**title:** За 3 дня до ДДU в проекте переуступки всплыл запрет перепродажи на 3 года — сделку в Тюмени остановили до эскроu  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**cluster_id:** `newbuild_assignment_resale_ban_ddu_tyumen`  
**top_energy_mirror:** `paper_clean_then_broke`  
**newbuild_mechanism:** покупатель (инвестор или семья) берёт **переуступку** на квартиру в строящемся доме Тюмени; в переписке и кратком описании уступки — цена, срок, объект; за **3 дня** до подписания нового ДДU в проекте договора появляется пункт **запрета отчуждения / новой уступки / перепродажи на 3 года** (или «до ввода + N месяцев»); покупатель рассчитывал выйти до ключей или перепродать право; **остановка до эскроu**; под риском комиссия/задаток по уступке **~80–120 тыс ₽** (composite casus)

## Scout handoff

- **comment_magnet:** «Если в переуступке всплывает запрет продажи на 3 года — вы подписываете или ищете другой лот?»
- **why_newbuild_not_secondary:** только переуступка прав по ДДU, не вторичка
- **anti_dupe:** distinct from live «28 дней ждали переуступку — продали другому» (other buyer took object)
- **fact boundaries:** composite; без фамилий, ЖК, застройщика, банка; 3 года и 80–120k — editorial parameters

### Locked editorial spine

1. Покупатель находит лот по переуступке в тюменской новостройке (ниже цены застройщика / быстрый вход).  
2. Согласование с первым дольщиком и застройщиком, предоплата комиссии/задатка по уступке.  
3. Юрист или риэлтор запрашивает **проект ДДU** для нового дольщика.  
4. За **3 дня** до подписания в приложении/разделе «права и обязанности» — **запрет уступки/продажи 3 года**.  
5. Покупатель понимает, что **выход до ключей закрыт** — стоп **до эскроu**.  
6. Спор: что было в договоре уступки vs что застройщик вкладывает в типовой ДДU.

## Overlap (published-titles-only.md in article dir)

- Live **2026-09-18** — 28 дней регистрации переуступки, лот ушёл **другому** (механика time/queue, не ban clause).  
- **B29/B27/B28** — другие механики. Не смешивать.

## Wordstat MCP-KV (2026-09-20, regions 55+11176)

| phrase | volume |
|--------|-------:|
| купить новостройку в тюмени | **920** |
| купить новостройку в тюмени от застройщика | 455 |
| купить новостройку в тюмени в ипотеку | 83 |
| переуступка новостройка тюмень | MCP empty |

## SERP (research-serp.json, 2026-09-20)

- SmartAgent 2026 — переуступка ДДU риски для риэлтора  
- realo.ru guide pereustupka-ddu-2026 — 214-ФЗ, двойная переуступка  
- pravo-pro, fedelis, mapestate — цессия до акта приёма-передачи  
Use for **mechanism** only, not as single fact source for Tyumen casus.

## Official / legal (verify accessed 2026-09-20)

- **214-ФЗ** ст. 12 — уступка права требования по ДДU (согласие застройщика, регистрация) — consultant.ru or garant reference  
- **dom.rf** / застройщик типовые ограничения в ДДU — mention that developers may insert resale restrictions; verify generic domrf FAQ on assignment if available  
Fill `official_verifications` — no invented bank % or developer name

## Community / fresh signal (week 2026-09-20)

- Channel context: https://t.me/Tyumen_Rieltor — Tyumen newbuild buyers ask about переуступка before keys (paraphrase as community pain, not quoted post unless fetched)  
- Dzen holyslav — newbuild casus format reference only

## Writer constraints

- Composite Tyumen casus; plain Russian; no «собирательный случай» disclaimer in article body  
- Target length hint for Writer: facts for **1400–1600** word Sol pass  
- Interlink siblings: published articles on ipoteka/novostrojka from published-titles-only.md

Output complete research-notes.md + ensure research-agent-report.json fields described in SKILL.

## OUTPUT LIMIT (HARD for API)

Keep `research-notes.md` **compact**: target **≤5500 characters** total. Short bullets in practical_facts; one row per official_verifications claim; minimal source_table (8–10 rows). Do not skip required section headers.
