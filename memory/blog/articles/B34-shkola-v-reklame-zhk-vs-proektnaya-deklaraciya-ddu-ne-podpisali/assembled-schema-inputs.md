# Schema inputs — B34

ROLE: schema. **Ответ — ТОЛЬКО один JSON-LD объект** (valid JSON, `@context` + `@graph`). Без markdown fences, без пояснений, без bash, без «не могу».

## BlogPosting

- headline: Школа в рекламе ЖК — в декларации 2030, ДДУ не подписали
- description (teaser, не дубль title): На рендере школа была «рядом», а в декларации — через четыре года. Тюменская семья сверила даты до ДДУ и поняла: ребёнка ждёт совсем другой маршрут.
- datePublished: 2026-10-01
- inLanguage: ru-RU
- url / mainEntityOfPage @id: `{{SITE_BASE}}/shkola-v-reklame-zhk-vs-proektnaya-deklaraciya-ddu-ne-podpisali/` (без `/blog/`)
- author Person @id: `{{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin` (Святослав Шакин, registry svyatoslav-shakin)
- publisher Organization @id: `{{SITE_BASE}}/#organization` name The Риэлтор
- FAQPage: **не создавать** (theme_blocks faq skip)

## Placeholders

Все URL только `{{SITE_BASE}}`, никогда `[REDACTED]`.

## Эталон структуры (B33-style @graph)

Organization + Person + BlogPosting в одном @graph.
