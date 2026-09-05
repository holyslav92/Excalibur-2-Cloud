# Schema inputs — B23

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени инвестор не подписал ДДУ: аренду запретили до ключей",
  "h1": "В Тюмени инвестор не подписал ДДУ: аренду запретили до ключей",
  "slug": "v-tyumeni-investor-kupil-novostrojku-pod-sdachu-v-ddu-zapretili-arendu-do-klyuch",
  "topic_id": "B23",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B23",
  "h1": "В Тюмени инвестор не подписал ДДУ: аренду запретили до ключей",
  "title": "В Тюмени инвестор не подписал ДДУ: аренду запретили до ключей",
  "subject": "Инвестор в тюменской новостройке, ДДУ и запрет аренды до получения ключей"
}
```

## description-brief.json

«В Тюмени бронь уже оплачена, а доходность инвестора тает в приложениях к ДДУ. Шакин разбирает, почему запрет аренды был лишь первой строкой сделки.»

Для BlogPosting.description использовать headline из article.meta (как в B22), не description-brief.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-investor-kupil-novostrojku-pod-sdachu-v-ddu-zapretili-arendu-do-klyuch/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505 (без [REDACTED])

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени инвестор не подписал ДДУ: аренду запретили до ключей
- description: В Тюмени инвестор не подписал ДДУ: аренду запретили до ключей
- datePublished: 2026-09-05
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
