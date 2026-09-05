# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела",
  "h1": "В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела",
  "slug": "v-tyumeni-pereustupku-podnyali-za-sutki-do-ddu-bron-sgorela",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела",
  "title": "В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела",
  "subject": "Покупка новостройки в Тюмени по переуступке права требования по ДДУ"
}
```

## description (article.meta — description-brief ещё нет)

В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-pereustupku-podnyali-za-sutki-do-ddu-bron-sgorela/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела
- description: В Тюмени переуступку подняли на 280 тысяч за сутki до ДДУ — бронь сгорела
- datePublished: 2026-09-05
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
