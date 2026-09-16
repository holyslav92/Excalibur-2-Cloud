# OUTPUT INSTRUCTION (HARD)
You are invoked by `excalibur_blog_derouter_opus_chat.py`. Your response text is saved automatically to `.cursor/excalibur-blog-handoff.md` by the shell script. **Do NOT refuse or ask to run scripts — they already ran.** Output ONLY the handoff markdown body in the format from scout SKILL.md § Handoff. No preamble, no meta-commentary.

# Scout inputs — 2026-09-16 slot 12:00 YEKT (verified)

## Run context
- tenant: The Риэлтор / tymenrieltor.ru
- topic_market_focus: newbuild_only
- date: 2026-09-16
- topic_id: B27

## Verification completed (this run)
```bash
python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters  # OK
python3 scripts/excalibur_blog_scout_helper.py --check-query "В Тюмени за 3 дня до ДДУ сверили машиноместо — в декларации не оказалось номера"
# → ✅ ANTI-DUPE HARD PASS, ✅ TOPIC FOCUS PASS
python3 scripts/excalibur_blog_topic_focus.py --text "..."  # PASS
python3 scripts/excalibur_blog_wordstat_gate.py doctor  # OK
```

## Title draft (news-casus, stop before escrow — NOT completed sale)
**В Тюмени за 3 дня до ДДУ сверили машиноместо — в декларации не оказалось номера**

## Story
Семья в Тюмени выбрала квартиру в новостройке и отдельное машиноместо в паркинге. Менеджер застройщика включил место в бронь и приложил к пакету для банка. За три дня до подписания ДДУ юрист сверил номер машиноместа с проектной декларацией на наш.дом.рф — в реестре этого номера в указанном корпусе не было (или место числилось в другой очереди/корпусе). Банк не открыл эскроу на полный пакет, семья остановила сделку до аванса.

## Canon fields
- **top_energy_mirror:** paper clean then broke — «в брони всё сходилось, в декларации номер исчез»
- **newbuild_mechanism:** ДДУ на машиноместо + проектная декларация ЖК + эскроу-пакет с квартирой
- **why_newbuild_not_secondary:** только покупка у застройщика по ДДУ, не рынок парковок между физлицами
- **klyshin_hook:** none
- **dzen_casus_shape:** PASS (событие + stakes + время + финал + comment magnet)
- **comment_magnet_angle:** брать машиноместо отдельным ДДУ или включать в ипотеку вместе с квартирой?
- **anti_dupe_hard:** PASS (cluster new: parking_declaration_mismatch_tyumen)

## Wordstat rework log
| phrase | region | volume | note |
|--------|--------|--------|------|
| новостройки тюмень | 55+11176 | 4475 | P0 spine |
| купить новостройку в тюмени | 55+11176 | 902 | buyer demand |
| дду машиноместо | 225 compare | 217 | mechanism spine |
| купить машиноместо дду | 225 | 35 | long-tail |
| жк новостройки тюмень | 55+11176 | 204 | local JK |

**Final P0:** новостройки тюмень (4475) + дду машиноместо (217 RU)

## signal_urls (public, Tyumen newbuild)
1. https://i4.cdnstroy.ru/4u2e0huifd1n7_1c2eltw.pdf — проектная декларация ЖК Тюмень, раздел машино-мест (68 мест, Червишевский тракт)
2. https://tyumenskaya.kvmeter.ru/jk/sosedi/ — ЖК «Соседи», 374 машиноместа, продажа по ДДУ
3. https://tyumen.brusnika.ru/projects/rechnoj-port/ — документация застройщика, шаблон ДДУ
4. https://dzen.ru/a/ajrYV_OqTyVciJYz — чеклист: сверка ДДУ с проектной декларацией (Святослав Шакин)

## Anti-repeat
- NOT overlapping: acceptance_defects, insurance before escrow, keys delay, co-borrower, assignment, cellar B21
- formula spam: distinct mechanism (parking declaration mismatch)

## Task
Write `.cursor/excalibur-blog-handoff.md` in standard handoff format with all required fields for research_start.
