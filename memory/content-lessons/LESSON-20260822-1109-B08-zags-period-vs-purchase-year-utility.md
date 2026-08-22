## LESSON-20260822-1109-B08-zags-period-vs-purchase-year-utility
status: proposed
topic_id: B08
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: quality-bar-9 PASS — word_count 2439, h2_count 9, 4 sibling interlinks; opening-meta PASS; html-linter PASS.
- artifact: title-brief.json + description-brief.json
  finding: H1 и Дзен-карточка якорятся на документе (ЗАГС) и финале (банк отказал); description ≠ title, geo Тюмень, rhythm klyshin_case_hook.
- artifact: article.html — TL;DR ul сразу после лида + механика «год начала периода в справке vs год приобретения квартиры».
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EVIDENCE_SKIPPED
- LOW_SAMPLE (Metrika absent)

### Keep
- Лид = сцена (справка на руках, ЕГРН чистая) → twist одной строчкой (период справки) → TL;DR перед early CTA — buyer checklist до длинного разбора.
- Практическая формула в теле: сравнить **год начала периода ЗАГС** с **годом ДКП/приобретения**; если период позже — справка не закрывает брачный риск на дату покупки.
- H2 «Почему „в ЕГРН чисто" не закрыл риск» — отделяет реестровый срез от внереестровых долей (супружеская + наследственная цепочка).

### Change
- Для document-casus про ЗАГС/брак — в Writer brief требовать явный checklist-блок (2 числа: период справки vs год сделки) в первых 500 словах.
- Description: сохранять «не равно title» + один конкретный документный gap (как B08: «не захватывала год покупки»).

### Never again
- Принимать справку ЗАГС «как доказательство отсутствия брака» без привязки периода к дате приобретения объекта.
- Термин-дамп про форму №15 и ЕГР ЗАГС в открытии — факты ушли в H2 после сцены (human-first-v2 opening rules соблюдены).

### Proposed apply
- Review-only note для Research/Writer assembled inputs: `required_buyer_check: zags_period_vs_purchase_year` на document-risk темах.
- Без автоматического изменения writer-master-prompt.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B08-skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo
wp_post_id: 9073
