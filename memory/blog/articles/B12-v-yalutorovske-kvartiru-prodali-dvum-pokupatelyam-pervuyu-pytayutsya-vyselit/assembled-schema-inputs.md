# Schema inputs — B12

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Ялуторовске квартиру продали двоим — покупательнице грозит выселение",
  "h1": "В Ялуторовске квартиру продали двоим — покупательнице грозит выселение",
  "slug": "v-yalutorovske-kvartiru-prodali-dvum-pokupatelyam-pervuyu-pytayutsya-vyselit",
  "topic_id": "B12",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-28",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B12",
  "h1": "В Ялуторовске квартиру продали двоим — покупательнице грозит выселение",
  "title": "В Ялуторовске квартиру продали двоим — покупательнице грозит выселение"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Ялуторовске квартиру продали двоим — покупательнице грозит выселение».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-yalutorovske-kvartiru-prodali-dvum-pokupatelyam-pervuyu-pytayutsya-vyselit/`
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

- headline: В Ялуторовске квартиру продали двоим — покупательнице грозит выселение
- description: В Ялуторовске квартиру продали двоим — покупательнице грозит выселение
- datePublished: 2026-08-28
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
