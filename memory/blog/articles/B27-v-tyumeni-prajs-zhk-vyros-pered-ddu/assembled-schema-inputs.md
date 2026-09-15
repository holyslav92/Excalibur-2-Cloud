# Schema inputs — B27 ONLY

CRITICAL: topic_id=B27, slug=v-tyumeni-prajs-zhk-vyros-pered-ddu. НЕ B28, НЕ другой slug/headline.

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (синтез из title-brief + description-brief)

```json
{
  "title": "В Тюмени за 9 дней до ДДУ подорожал прайс ЖК — до аванса не дошли",
  "h1": "В Тюмени за 9 дней до ДДУ подорожал прайс ЖК — до аванса не дошли",
  "slug": "v-tyumeni-prajs-zhk-vyros-pered-ddu",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-15",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени за 9 дней до ДДУ подорожал прайс ЖК — до аванса не дошли",
  "title": "В Тюмени за 9 дней до ДДУ подорожал прайс ЖК — до аванса не дошли",
  "subject": "Подорожание по прайсу ЖК в Тюмени перед подписанием ДДУ и остановка сделки до аванса",
  "slug": "v-tyumeni-prajs-zhk-vyros-pered-ddu"
}
```

## description-brief.json

```json
{
  "topic_id": "B27",
  "description": "Одобрение ипотеки уже было в телефоне, но прайс ЖК в Тюмени внезапно вырос на 480 тысяч. До ДДУ оставалось девять дней — семья решала, искать деньги или уходить из сделки."
}
```

## research-notes

- research_date: 2026-09-15
- topic_id: B27

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-prajs-zhk-vyros-pered-ddu/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505
- НЕ включать sameAs с [REDACTED] или {{SITE_BASE}} дубликаты в sameAs автора

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени за 9 дней до ДДУ подорожал прайс ЖК — до аванса не дошли
- description: Одобрение ипотеки уже было в телефоне, но прайс ЖК в Тюмени внезапно вырос на 480 тысяч. До ДДУ оставалось девять дней — семья решала, искать деньги или уходить из сделки.
- datePublished: 2026-09-15
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (нет h3 FAQ-пар), theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
