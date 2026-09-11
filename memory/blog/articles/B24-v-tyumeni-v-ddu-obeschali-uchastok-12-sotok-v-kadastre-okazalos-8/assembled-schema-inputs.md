# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени в ДДУ обещали 12 соток — кадастр показал 8",
  "h1": "В Тюмени в ДДУ обещали 12 соток — кадастр показал 8",
  "slug": "v-tyumeni-v-ddu-obeschali-uchastok-12-sotok-v-kadastre-okazalos-8",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-06",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени в ДДУ обещали 12 соток — кадастр показал 8",
  "title": "В Тюмени в ДДУ обещали 12 соток — кадастр показал 8",
  "subject": "ДДУ на дом в коттеджном посёлке и расхождение площади участка с кадастром"
}
```

## description (из лида статьи — description-brief ещё нет)

В тюменском коттеджном посёлке семья готовилась подписать ДДУ на дом с двенадцатью сотками, а за неделю до сделки кадастр показал восемь — банк остановил эскроу. Святослав Шакин разбирает, где рендер расходится с реестром и почему доплата за «недостающие» сотки опасна.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-obeschali-uchastok-12-sotok-v-kadastre-okazalos-8/`
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

- headline: В Тюмени в ДДУ обещали 12 соток — кадастр показал 8
- description: (см. выше)
- datePublished: 2026-09-06
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
