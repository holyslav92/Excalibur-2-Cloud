# Schema inputs — B33

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени на рендере новостройки обещали детсад — в декларации его нет",
  "h1": "В Тюмени на рендере новостройки обещали детсад — в декларации его нет",
  "slug": "v-tyumeni-na-rendere-novostrojki-obeschali-detskij-sad-v-deklaracii-ego-net",
  "topic_id": "B33",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-24",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B33",
  "h1": "В Тюмени на рендере новостройки обещали детсад — в декларации его нет",
  "title": "В Тюмени на рендере новостройки обещали детсад — в декларации его нет",
  "subject": "Детский сад на рендере новостройки и проектная декларация"
}
```

## description-brief.json (BlogPosting description)

На картинке обещали сад, в ЕИСЖС его не нашли. Семья в Тюмени уже внесла 150 тысяч за бронь — и остановилась за пять дней до ДДУ. Что оказалось важнее красивого рендера?

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-na-rendere-novostrojki-obeschali-detskij-sad-v-deklaracii-ego-net/`
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

- headline: В Тюмени на рендере новостройки обещали детсад — в декларации его нет
- description: На картинке обещали сад, в ЕИСЖС его не нашли. Семья в Тюмени уже внесла 150 тысяч за бронь — и остановилась за пять дней до ДДУ. Что оказалось важнее красивого рендера?
- datePublished: 2026-09-24
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (theme_blocks.faq = skip).

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
