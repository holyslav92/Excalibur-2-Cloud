# Schema inputs — B28

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (synthesized from title-brief + research-context)

```json
{
  "title": "В Тюмени за 5 дней до ДДУ сорвалась фиксация цены",
  "h1": "В Тюмени за 5 дней до ДДУ сорвалась фиксация цены",
  "slug": "v-tyumeni-sorvalas-fiksaciya-ceny-novostrojki",
  "topic_id": "B28",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-15",
  "description": "В Тюмени семья уже открыла эскроу и получила одобрение ипотеки. Но в проекте ДДУ появилась индексация — обещанная цена исчезла за пять дней до сделки.",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B28",
  "h1": "В Тюмени за 5 дней до ДДУ сорвалась фиксация цены",
  "title": "В Тюмени за 5 дней до ДДУ сорвалась фиксация цены",
  "subject": "фиксация цены на новостройку в Тюмени перед подписанием ДДУ"
}
```

## description-brief.json

```json
{
  "topic_id": "B28",
  "description": "В Тюмени семья уже открыла эскроу и получила одобрение ипотеки. Но в проекте ДДУ появилась индексация — обещанная цена исчезла за пять дней до сделки."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-sorvalas-fiksaciya-ceny-novostrojki/`
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

- headline: В Тюмени за 5 дней до ДДУ сорвалась фиксация цены
- description: В Тюмени семья уже открыла эскроу и получила одобрение ипотеки. Но в проекте ДДУ появилась индексация — обещанная цена исчезла за пять дней до сделки.
- datePublished: 2026-09-15
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
