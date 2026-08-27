# Schema inputs — B11

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени квартиру продали дважды — второй покупатель потерял аванс",
  "h1": "В Тюмени квартиру продали дважды — второй покупатель потерял аванс",
  "slug": "kvartiru-prodali-dvazhdy-vtoroj-pokupatel-v-tyumeni-poteryal-avans",
  "topic_id": "B11",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-27",
  "theme_blocks": { "faq": "skip" }
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/kvartiru-prodali-dvazhdy-vtoroj-pokupatel-v-tyumeni-poteryal-avans/`
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

- headline: В Тюмени квартиру продали дважды — второй покупатель потерял аванс
- description: В Тюмени квартиру продали дважды — второй покупатель потерял аванс
- datePublished: 2026-08-27
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip. Есть h3 «Восемь проверок до передачи денег» и «Что видно в выписке» — это не FAQ.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
