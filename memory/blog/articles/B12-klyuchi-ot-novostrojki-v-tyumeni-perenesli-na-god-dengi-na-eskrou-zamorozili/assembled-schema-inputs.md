# Schema inputs — B12

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась",
  "h1": "Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась",
  "slug": "klyuchi-ot-novostrojki-v-tyumeni-perenesli-na-god-dengi-na-eskrou-zamorozili",
  "topic_id": "B12",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-28",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B12",
  "h1": "Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась",
  "title": "Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/klyuchi-ot-novostrojki-v-tyumeni-perenesli-na-god-dengi-na-eskrou-zamorozili/`
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

- headline: Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась
- description: Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась
- datePublished: 2026-08-28
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
