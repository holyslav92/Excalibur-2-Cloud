# Schema inputs — B08

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Справка ЗАГС была чистой — банк отказал из-за доли умершей жены",
  "h1": "Справка ЗАГС была чистой — банк отказал из-за доли умершей жены",
  "slug": "skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo",
  "topic_id": "B08",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-22",
  "theme_blocks": { "faq": "skip" }
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/holyslav92, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: Справка ЗАГС была чистой — банк отказал из-за доли умершей жены
- description: Справка ЗАГС была чистой — банк отказал из-за доли умершей жены
- datePublished: 2026-08-22
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
