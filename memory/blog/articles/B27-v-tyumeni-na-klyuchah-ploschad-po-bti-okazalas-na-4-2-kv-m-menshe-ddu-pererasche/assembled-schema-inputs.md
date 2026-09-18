# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени БТИ «съело» 4,2 кв.м ДДУ — в перерасчёте отказали",
  "h1": "В Тюмени БТИ «съело» 4,2 кв.м ДДУ — в перерасчёте отказали",
  "slug": "v-tyumeni-na-klyuchah-ploschad-po-bti-okazalas-na-4-2-kv-m-menshe-ddu-pererasche",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-18",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени БТИ «съело» 4,2 кв.м ДДУ — в перерасчёте отказали",
  "title": "В Тюмени БТИ «съело» 4,2 кв.м ДДУ — в перерасчёте отказали",
  "subject": "Расхождение площади БТИ и ДДУ в новостройке",
  "angle": "На выдаче ключей площадь квартиры оказалась на 4,2 кв.м меньше, но застройщик отказал в перерасчёте."
}
```

## description (from title-brief angle)

На выдаче ключей площадь квартиры оказалась на 4,2 кв.м меньше, но застройщик отказал в перерасчёте.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-na-klyuchah-ploschad-po-bti-okazalas-na-4-2-kv-m-menshe-ddu-pererasche/`
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

- headline: В Тюмени БТИ «съело» 4,2 кв.м ДДУ — в перерасчёте отказали
- description: На выдаче ключей площадь квартиры оказалась на 4,2 кв.м меньше, но застройщик отказал в перерасчёте.
- datePublished: 2026-09-18
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
