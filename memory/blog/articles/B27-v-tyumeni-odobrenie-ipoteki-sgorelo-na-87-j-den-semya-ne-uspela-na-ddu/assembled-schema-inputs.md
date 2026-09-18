# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались",
  "h1": "В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались",
  "slug": "v-tyumeni-odobrenie-ipoteki-sgorelo-na-87-j-den-semya-ne-uspela-na-ddu",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-18",
  "description": "В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались",
  "title": "В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались",
  "subject": "одобрение ипотеки на новостройку и подписание ДДУ"
}
```

## description-brief.json

```json
{
  "description": "«Ждём договор» в Тюмени обернулось 87 днями ожидания. Когда банк закрыл старое решение, переодобрение уменьшило сумму и подняло ставку — бронь на новостройку сняли."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-odobrenie-ipoteki-sgorelo-na-87-j-den-semya-ne-uspela-na-ddu/`
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

- headline: В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались
- description: «Ждём договор» в Тюмени обернулось 87 днями ожидания. Когда банк закрыл старое решение, переодобрение уменьшило сумму и подняло ставку — бронь на новостройку сняли.
- datePublished: 2026-09-18
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
