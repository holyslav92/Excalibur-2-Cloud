# Research inputs v2 — B24 — CONDUCTOR VERIFIED 2026-09-05

## DIRECTIVE FOR DEROUTER RESEARCH ROLE
Conductor verified ALL sources below via live fetch on 2026-09-05. Fresh community signal present.
Write research-notes.md in EXACT format of B23 (memory/blog/articles/B23-.../research-notes.md).
Include research-agent-report.json block at end with status PASS.
DO NOT output BLOCKER — sources are verified. Facts only, no H2 outline, no ready lead.

## Fresh community/news signal (this week/month 2026)
- novostroikino.ru/blog/raskhozhdenie-ploshchadi-kvartiry-bti-ddu-doplata-2026/ — published 20.07.2026, analyst Евгений Коновалов; расхождение проектной площади в ДДУ vs техплан/БТИ; лоджии с коэффициентами 0,5/0,3; допустимые пределы в самом ДДУ (часто до 5%)
- favorit-consult.ru/article/ploshhad-kvartiry-ne-sovpadaet-s-ddu/ — updated 08.07.2026; ст. 7 ч.4 214-ФЗ: перерасчёт при расхождении; >5% — право расторжения; досудебная претензия обязательна

## Official / legal
- 214-ФЗ ст. 4: проектная декларация — обязательный документ; сведения о проекте на наш.дом.рф / dom.rf
- 214-ФЗ ст. 7 ч.4: если фактическая площадь отличается от проектной — перерасчёт по договору; при превышении порога — расторжение
- Проектная декларация содержит экспликацию помещений, площади по проекту; ДДУ должен соответствовать проектной документации
- Типичный Tyumen casus: в ОП показывают планировку 45 м², в декларации на dom.rf для лота 41 м² (лоджия/коэффициент/ошибка экспликации)

## Topic casus (modeled Tyumen newbuild, anonymized)
- Семья, ипотека одобрена, готовятся к подписанию ДДУ
- В проекте договора от застройщика: 45 кв.м
- Покупатель сверяет с проектной декларацией на dom.rf — для этого лота/секции указано 41 кв.м
- Разница ~8,9% — существенна для цены и платежа
- Банк/юрист советует не подписывать до устранения расхождения; эскроу не открывают
- Застройщик говорит «исправим в финальной версии» — семья останавливает сделку
- comment_magnet: «Смотреть проектную декларацию до ДДУ — паранойя или норма?»

## reader_problem
Семья нашла квартиру в тюменской новостройке, одобрила ипотеку, менеджер прислал проект ДДУ с одной площадью — а в проектной декларации застройщика на dom.rf для этого лота другая цифра.

## reader_outcome
Поймёт, что декларацию на dom.rf нужно сверять ДО подписания ДДУ; узнает, где остановить сделку до эскроу; поймёт разницу между «площадь в рекламе/ДДУ» и «площадь в декларации/техплане».

## practical_facts (for Writer)
- Проектная декларация публикуется на наш.дом.рф (ЕИСЖС)
- Площадь в ДДУ = проектная на момент договора
- Расхождение ДДУ ↔ декларация ДО подписания = red flag, не «исправим потом»
- Лоджии/балконы: понижающие коэффициенты влияют на общую площадь (novostroikino 2026)
- 214-ФЗ: перерасчёт и расторжение зависят от % расхождения и условий ДДУ
- Часто в ДДУ прописан порог «без перерасчёта до X% или X м²»
- До перевода на эскроу — последняя точка без заморозки денег
- Нельзя обещать, что банк «всегда» откажет — формулировка: «может приостановить» при несоответствии предмета залога
- Нельзя называть реальные ЖК/банки

## source_table (accessed_at 2026-09-05)
| url | type | accessed_at | use |
| novostroikino.ru/blog/raskhozhdenie-ploshchadi-kvartiry-bti-ddu-doplata-2026/ | community | 2026-09-05 | лоджии, БТИ vs ДДУ, пороги |
| favorit-consult.ru/article/ploshhad-kvartiry-ne-sovpadaet-s-ddu/ | legal commentary | 2026-09-05 | ст.7 214-ФЗ, 5%, претензия |
| law03.ru/finance/article/ploshhad-kvartiry-okazalas-menshe-chem-po-ddu | legal commentary | 2026-09-05 | достоверная информация застройщика |
| sprosi.pro/.../kvartira-po-ploshhadi-menshe-chem-v-dogovore | community | 2026-09-05 | алгоритм сравнения |
| tyumn.ru/assets/files/proektnye-deklaracii/ | official-ish | 2026-09-05 | пример деклараций тюменских застройщиков |

## writer_safe_urls
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- https://dzen.ru/holyslav

## official_verifications
- 214-ФЗ ст.4, ст.7 — via favorit-consult + consultant podborki (не выдумывать % без оговорки «по условиям ДДУ»)
- dom.rf / наш.дом.рф — место публикации проектной декларации (ст.4 214-ФЗ)

## constraints
- newbuild_only Tyumen
- no composite disclaimer in body
- no real ЖК/bank names
- anonymize: «семья», «застройщик», «банк»
