# Schema inputs — B33

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени ребёнку исполнилось 7 в день подписания ДДУ — семейная ипотека под угрозой",
  "h1": "В Тюмени ребёнку исполнилось 7 в день подписания ДДУ — семейная ипотека под угрозой",
  "slug": "v-den-podpisaniya-ddu-rebenku-ispolnilos-7-let-bank-snyal-semejnuyu-ipoteku-na-n",
  "topic_id": "B33",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-23",
  "description": "«Нам же уже одобрили»: семья в Тюмени готовилась к сделке, а банк пересмотрел право на льготу. Теперь на кону оплаченная бронь, а ключ к льготной ставке — в дате кредитного договора.",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B33",
  "h1": "В Тюмени ребёнку исполнилось 7 в день подписания ДДУ — семейная ипотека под угрозой",
  "title": "В Тюмени ребёнку исполнилось 7 в день подписания ДДУ — семейная ипотека под угрозой",
  "subject": "Семейная ипотека на новостройку в Тюмени при семилетии ребёнка в день подписания ДДУ"
}
```

## research_date

2026-09-23 (datePublished)

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-den-podpisaniya-ddu-rebenku-ispolnilos-7-let-bank-snyal-semejnuyu-ipoteku-na-n/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (без [REDACTED]): dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени ребёнку исполнилось 7 в день подписания ДДУ — семейная ипотека под угрозой
- description: «Нам же уже одобрили»: семья в Тюмени готовилась к сделке, а банк пересмотрел право на льготу. Теперь на кону оплаченная бронь, а ключ к льготной ставке — в дате кредитного договора.
- datePublished: 2026-09-23
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
