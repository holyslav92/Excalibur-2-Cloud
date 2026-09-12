# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Перед ДДУ ребёнку исполнилось 7 лет — семейную ипотеку пересчитали",
  "h1": "Перед ДДУ ребёнку исполнилось 7 лет — семейную ипотеку пересчитали",
  "slug": "rebenku-7-let-nakanune-ddu-semejnuyu-ipoteku-pereschitali",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-09",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "Перед ДДУ ребёнку исполнилось 7 лет — семейную ипотеку пересчитали",
  "title": "Перед ДДУ ребёнку исполнилось 7 лет — семейную ипотеку пересчитали",
  "subject": "семейная ипотека на новостройку и возраст ребёнка"
}
```

## description-brief.json

До ДДУ оставалось шесть дней, когда банк заново посмотрел на возраст ребёнка. В Тюмени одобренная семейная ипотека перестала сходиться с бронью — почему решает не дата заявки.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/rebenku-7-let-nakanune-ddu-semejnuyu-ipoteku-pereschitali/`
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

- headline: Перед ДДУ ребёнку исполнилось 7 лет — семейную ипотеку пересчитали
- description: До ДДУ оставалось шесть дней, когда банк заново посмотрел на возраст ребёнка. В Тюмени одобренная семейная ипотека перестала сходиться с бронью — почему решает не дата заявки.
- datePublished: 2026-09-09
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
