# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени за 7 дней до ДДУ созаёмщика убрали — ипотеки не хватило",
  "h1": "В Тюмени за 7 дней до ДДУ созаёмщика убрали — ипотеки не хватило",
  "slug": "v-tyumeni-semejnuyu-ipoteku-odobrili-na-dvoih-pered-ddu-sozaemschika-isklyuchili",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-07",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени за 7 дней до ДДУ созаёмщика убрали — ипотеки не хватило",
  "title": "В Тюмени за 7 дней до ДДУ созаёмщика убрали — ипотеки не хватило",
  "subject": "Семейная ипотека на новостройку с двумя созаёмщиками"
}
```

## description (для BlogPosting.description)

Семейную ипотеку в Тюмени одобрили на двоих, но за неделю до ДДУ банк исключил созаёмщика — лимита не хватило на сделку. Святослав Шакин разбирает, почему предодобрение не равно финальному кредиту.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-semejnuyu-ipoteku-odobrili-na-dvoih-pered-ddu-sozaemschika-isklyuchili/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (без [REDACTED]): dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени за 7 дней до ДДУ созаёмщика убрали — ипотеки не хватило
- description: Семейную ипотеку в Тюмени одобрили на двоих, но за неделю до ДДУ банк исключил созаёмщика — лимита не хватило на сделку. Святослав Шакин разбирает, почему предодобрение не равно финальному кредиту.
- datePublished: 2026-09-07
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
