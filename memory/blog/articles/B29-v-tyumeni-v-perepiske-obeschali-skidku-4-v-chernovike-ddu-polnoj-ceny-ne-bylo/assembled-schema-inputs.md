# Schema inputs — B29

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

**RUNTIME:** вызов из `excalibur_blog_derouter_opus_chat.py --role schema` с рабочим DEROUTER API. **Запрещено** возвращать BLOCKER/status JSON — только JSON-LD @graph.

## article.meta.json

```json
{
  "title": "В Тюмени обещали скидку 4% — проект ДДУ без неё остановил сделку",
  "h1": "В Тюмени обещали скидку 4% — проект ДДУ без неё остановил сделку",
  "slug": "v-tyumeni-v-perepiske-obeschali-skidku-4-v-chernovike-ddu-polnoj-ceny-ne-bylo",
  "topic_id": "B29",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-19",
  "description": "Скидка в переписке и цена в проекте ДДУ",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B29",
  "h1": "В Тюмени обещали скидку 4% — проект ДДУ без неё остановил сделку",
  "title": "В Тюмени обещали скидку 4% — проект ДДУ без неё остановил сделку",
  "subject": "Обещанная скидка 4% на новостройку, которую не включили в проект ДДУ"
}
```

## research-context

- datePublished: 2026-09-19 (today_iso from research-context.json)

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-perepiske-obeschali-skidku-4-v-chernovike-ddu-polnoj-ceny-ne-bylo/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505 (без [REDACTED] в sameAs)

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени обещали скидку 4% — проект ДДУ без неё остановил сделку
- description: Скидка в переписке и цена в проекте ДДУ
- datePublished: 2026-09-19
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
