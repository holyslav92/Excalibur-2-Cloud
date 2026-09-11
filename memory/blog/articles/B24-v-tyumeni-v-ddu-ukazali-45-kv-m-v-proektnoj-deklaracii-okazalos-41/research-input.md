# Research inputs — B24 — 2026-09-05

## Date context
today_iso: 2026-09-05 | timezone: Europe/Moscow

## Topic (from Scout handoff)
topic_id: B24
title: В Тюмени в ДДУ указали 45 кв.м — в проектной декларации оказалось 41
cluster: newbuild_ddu_area_vs_project_declaration_mismatch_tyumen
market: newbuild_only Tyumen

## Casus arc for Writer
- Family signed DDU for newbuild, bank preparing mortgage
- DDU states 45 sqm, project declaration (dom.rf / ЕИСЖС) shows 41 sqm for same unit/lot
- Discovered 3 days before registration / before escrow transfer
- Registration stopped, booking at risk, escrow not funded
- comment_magnet: «Смотреть проектную декларацию до ДДУ — паранойя или норма?»

## SERP sources (research-serp.json, accessed 2026-09-05)
1. https://favorit-consult.ru/article/ploshhad-kvartiry-ne-sovpadaet-s-ddu/ — ст. 7 214-ФЗ, возврат при расхождении площади ДДУ vs факт/проект; порог отклонений
2. https://g-m-p.ru/news/verhovnyj-sud-razyasnil-chto-raznicza-mezhdu-proektnoj-i-fakticheskoj-ploshhadyu-kvartiry-po-ddu-ne-yavlyaetsya-nedostatkom/ — ВС РФ: разница проектной и фактической площади не всегда недостаток
3. https://sprosi.pro/articles/prava-potrebitelej/kvartira-po-ploshhadi-menshe-chem-v-dogovore-kak-vernut-pereplatu-za-nedostajushhie-metry/ — алгоритм: кадастровый паспорт, сравнение с ДДУ, претензия
4. https://law03.ru/finance/article/ploshhad-kvartiry-okazalas-menshe-chem-po-ddu — застройщик обязан достоверную информацию; объект должен соответствовать договору и проектной документации
5. https://www.consultant.ru/law/podborki/izmenenie_predmeta_ddu/ — изменение предмета ДДУ, площадь
6. https://tyumn.ru/assets/files/proektnye-deklaracii/ — пример проектных деклараций тюменских застройщиков (tyumenstrojservis)
7. https://lab-sud.ru/novosti-i-stat-i/22-ekspertiza-kvartiry-v-novostrojke-v-2026-godu-chto-izmenilos-posle-novyh-pravil-po-ddu/ — приёмка 2026, права дольщика

## Legal framework (214-ФЗ)
- ст. 4: проектная декларация — обязательный документ застройщика (ЕИСЖС / наш.дом.рф)
- ст. 7: недостатки объекта; расхождение площади свыше допустимого отклонения → компенсация/расторжение
- ДДУ должен соответствовать проектной документации; расхождение ДДУ ↔ декларация = риск до регистрации и эскроу

## Tyumen local angle
- Типичный сценарий: менеджер ОП показывает планировку 45 м², в декларации на dom.rf для лота указано 41 м² (балкон/лоджия по-разному, или ошибка в экспликации)
- Банк сверяет предмет залога с декларацией перед открытием эскроу
- Покупатель узнаёт на стадии «одобрение есть, подписываем ДДУ завтра»

## reader_problem
Семья нашла квартиру в новостройке, одобрила ипотеку, готовится к ДДУ — и внезапно видит, что площадь в договоре не бьётся с проектной декларацией застройщика.

## reader_outcome
Поймёт, что декларацию на dom.rf нужно сверять ДО подписания ДДУ, а не после; узнает, где остановить сделку до эскроу.

## Practical facts for Writer (NOT prose)
- Проектная декларация публикуется на наш.дом.рф / dom.rf
- Расхождение 4 кв.м (45 vs 41) ≈ 8,9% — существенно для цены и ипотеки
- Банк может отказать в открытии эскроу-счёта при несоответствии предмета ДДУ
- Допустимое отклонение по 214-ФЗ — смотреть актуальную редакцию (обычно порог для требования компенсации)
- До перевода денег на эскроу — точка контроля

## Constraints
- No real ЖК/bank names — anonymize
- No composite disclaimer in article body
- Newbuild only, Tyumen geo

## Task
Write research-notes.md per SKILL format: reader_problem, reader_outcome, practical_facts, constraints, source_table with accessed_at 2026-09-05, writer_safe_urls, official_verifications if applicable. Facts only, no H2 outline, no ready lead.
