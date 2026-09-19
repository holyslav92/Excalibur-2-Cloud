# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени обещали землю в собственности — декларация показала аренду",
  "h1": "В Тюмени обещали землю в собственности — декларация показала аренду",
  "slug": "v-tyumeni-v-proektnoj-deklaracii-zemlya-pod-zhk-v-arende-v-broni-obeschali-sobst",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-19",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду",
  "title": "За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду",
  "subject": "земля под новостройкой и проектная декларация"
}
```

## description (article.meta.json — description-brief ещё нет)

В Тюмени обещали землю в собственности — декларация показала аренду

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-proektnoj-deklaracii-zemlya-pod-zhk-v-arende-v-broni-obeschali-sobst/`
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

- headline: В Тюмени обещали землю в собственности — декларация показала аренду
- description: В Тюмени обещали землю в собственности — декларация показала аренду
- datePublished: 2026-09-19
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
