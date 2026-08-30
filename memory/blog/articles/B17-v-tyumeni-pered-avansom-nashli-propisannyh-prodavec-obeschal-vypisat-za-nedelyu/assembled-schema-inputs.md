# Schema inputs — B17

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Перед авансом в Тюмени нашли прописанных — сделку остановили",
  "h1": "Перед авансом в Тюмени нашли прописанных — сделку остановили",
  "slug": "v-tyumeni-pered-avansom-nashli-propisannyh-prodavec-obeschal-vypisat-za-nedelyu",
  "topic_id": "B17",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-30",
  "description": "Перед авансом в Тюмени нашли прописанных — сделку остановили",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B17",
  "h1": "Перед авансом в Тюмени нашли прописанных — сделку остановили",
  "title": "Перед авансом в Тюмени нашли прописанных — сделку остановили"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Перед авансом в Тюмени нашли прописанных — сделку остановили».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-pered-avansom-nashli-propisannyh-prodavec-obeschal-vypisat-za-nedelyu/`
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

- headline: Перед авансом в Тюмени нашли прописанных — сделку остановили
- description: Перед авансом в Тюмени нашли прописанных — сделку остановили
- datePublished: 2026-08-30
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
