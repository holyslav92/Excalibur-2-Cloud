# Schema inputs — B29

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени на приёмке новостройки для родителей акт не подписали",
  "h1": "В Тюмени на приёмке новостройки для родителей акт не подписали",
  "slug": "v-tyumeni-novostrojku-vybrali-dlya-roditelej-na-priemke-sorvalos",
  "topic_id": "B29",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-15",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B29",
  "h1": "В Тюмени на приёмке новостройки для родителей акт не подписали",
  "title": "В Тюмени на приёмке новостройки для родителей акт не подписали",
  "subject": "новостройка в Тюмени, купленная для пожилых родителей"
}
```

## description-brief.json

Квартира для родителей выглядела идеальной на экскурсии. Но в день приёмки выяснилось: до подъезда — через дорогу, лифт один, а окна смотрят на магистраль. В Тюмени семья ключи не взяла.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-novostrojku-vybrali-dlya-roditelej-na-priemke-sorvalos/`
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

- headline: В Тюмени на приёмке новостройки для родителей акт не подписали
- description: Квартира для родителей выглядела идеальной на экскурсии. Но в день приёмки выяснилось: до подъезда — через дорогу, лифт один, а окна смотрят на магистраль. В Тюмени семья ключи не взяла.
- datePublished: 2026-09-15
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
