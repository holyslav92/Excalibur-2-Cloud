# Schema inputs — B13

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Маткапитал нашли без детских долей — в Тюмени сделку остановили",
  "h1": "Маткапитал нашли без детских долей — в Тюмени сделку остановили",
  "slug": "matkapital-potratili-a-detyam-doli-ne-vydelili-v-tyumeni-sdelku-razvernuli-do-de",
  "topic_id": "B13",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-29",
  "description": "Маткапитал нашли без детских долей — в Тюмени сделку остановили",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B13",
  "h1": "Маткапитал нашли без детских долей — в Тюмени сделку остановили",
  "title": "Маткапитал нашли без детских долей — в Тюмени сделку остановили"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Маткапитал нашли без детских долей — в Тюмени сделку остановили».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/matkapital-potratili-a-detyam-doli-ne-vydelili-v-tyumeni-sdelku-razvernuli-do-de/`
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

- headline: Маткапитал нашли без детских долей — в Тюмени сделку остановили
- description: Маткапитал нашли без детских долей — в Тюмени сделку остановили
- datePublished: 2026-08-29
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
