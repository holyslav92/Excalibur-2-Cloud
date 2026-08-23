# Schema inputs — B10

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Бабушку-собственницу не нашли на осмотре — аванс остановили",
  "h1": "Бабушку-собственницу не нашли на осмотре — аванс остановили",
  "slug": "kvartira-v-tyumeni-babushka-sobstvennik-v-obyavlenii-na-osmotre-pered-avansom-ee",
  "topic_id": "B10",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-23",
  "theme_blocks": { "faq": "skip" }
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/kvartira-v-tyumeni-babushka-sobstvennik-v-obyavlenii-na-osmotre-pered-avansom-ee/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- url: {{SITE_BASE}}/rieltor-tyumen/
- sameAs: {{SITE_BASE}}/, {{SITE_BASE}}/rieltor-tyumen/, {{SITE_BASE}}/kontakty/, dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/holyslav92, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: Бабушку-собственницу не нашли на осмотре — аванс остановили
- description: Бабушку-собственницу не нашли на осмотре — аванс остановили
- datePublished: 2026-08-23
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
