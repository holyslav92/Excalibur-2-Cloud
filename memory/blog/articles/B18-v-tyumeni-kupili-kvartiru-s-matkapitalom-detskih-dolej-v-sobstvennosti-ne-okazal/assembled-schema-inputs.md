# Schema inputs — B18

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Квартиру с маткапиталом не купили: детских долей не было в ЕГРН",
  "h1": "Квартиру с маткапиталом не купили: детских долей не было в ЕГРН",
  "slug": "v-tyumeni-kupili-kvartiru-s-matkapitalom-detskih-dolej-v-sobstvennosti-ne-okazal",
  "topic_id": "B18",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-30",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B18",
  "h1": "Квартиру с маткапиталом не купили: детских долей не было в ЕГРН",
  "title": "Квартиру с маткапиталом не купили: детских долей не было в ЕГРН"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Квартиру с маткапиталом не купили: детских долей не было в ЕГРН».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-kupili-kvartiru-s-matkapitalom-detskih-dolej-v-sobstvennosti-ne-okazal/`
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

- headline: Квартиру с маткапиталом не купили: детских долей не было в ЕГРН
- description: Квартиру с маткапиталом не купили: детских долей не было в ЕГРН
- datePublished: 2026-08-30
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
