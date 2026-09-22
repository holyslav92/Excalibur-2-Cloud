# Schema inputs — B33

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "За 5 дней до ДДУ в декларации сдвинули срок сдачи новостройки в Тюмени — банк урезал ипотеку",
  "h1": "За 5 дней до ДДУ в декларации сдвинули срок сдачи новостройки в Тюмени — банк урезал ипотеку",
  "slug": "za-5-dnej-do-ddu-v-deklaracii-sdvinuli-sdachu-na-dva-kvartala-bank-urezal-ipotek",
  "topic_id": "B33",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-22",
  "theme_blocks": { "faq": "skip" }
}
```

## description-brief.json

```json
{
  "description": "В Тюмени застройщик тихо переписал дату в проектной декларации — до подписания ДДУ оставались считаные дни. Банк заметил сдвиг и пересмотрел сумму кредита."
}
```

## title-brief.json

```json
{
  "topic_id": "B33",
  "h1": "За 5 дней до ДДУ в декларации сдвинули срок сдачи новостройки в Тюмени — банк урезал ипотеку",
  "title": "За 5 дней до ДДУ в декларации сдвинули срок сдачи новостройки в Тюмени — банк урезал ипотеку",
  "subject": "Срок сдачи новостройки в Тюмени, проектная декларация и ипотека перед ДДУ"
}
```

## research-context (datePublished)

- today_iso: 2026-09-22

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/za-5-dnej-do-ddu-v-deklaracii-sdvinuli-sdachu-na-dva-kvartala-bank-urezal-ipotek/`
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

- headline: За 5 дней до ДДУ в декларации сдвинули срок сдачи новостройки в Тюмени — банк урезал ипотеку
- description: В Тюмени застройщик тихо переписал дату в проектной декларации — до подписания ДДУ оставались считаные дни. Банк заметил сдвиг и пересмотрел сумму кредита.
- datePublished: 2026-09-22
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
