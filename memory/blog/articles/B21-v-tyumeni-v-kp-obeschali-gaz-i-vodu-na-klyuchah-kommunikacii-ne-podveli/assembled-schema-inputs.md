# Schema inputs — B21

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени дом сдали без газа и воды — семья не взяла ключи",
  "h1": "В Тюмени дом сдали без газа и воды — семья не взяла ключи",
  "slug": "v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli",
  "topic_id": "B21",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-02",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B21",
  "h1": "В Тюмени дом сдали без газа и воды — семья не взяла ключи",
  "title": "В Тюмени дом сдали без газа и воды — семья не взяла ключи",
  "subject": "дом от застройщика в коттеджном посёлке под Тюменью, где к выдаче ключей не подвели газ и воду"
}
```

## description (article.meta.json — description-brief ещё нет)

В Тюмени дом сдали без газа и воды — семья не взяла ключи

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (только публичные URL, БЕЗ [REDACTED]): dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени дом сдали без газа и воды — семья не взяла ключи
- description: В Тюмени дом сдали без газа и воды — семья не взяла ключи
- datePublished: 2026-09-02
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage. Без литерала [REDACTED] нигде в JSON.
