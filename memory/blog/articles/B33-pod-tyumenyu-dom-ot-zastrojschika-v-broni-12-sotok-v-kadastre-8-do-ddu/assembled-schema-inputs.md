# Schema inputs — B33

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Дом под Тюменью обещали на 12 сотках, но в кадастре 8 — ДДУ остановили",
  "h1": "Дом под Тюменью обещали на 12 сотках, но в кадастре 8 — ДДУ остановили",
  "slug": "pod-tyumenyu-dom-ot-zastrojschika-v-broni-12-sotok-v-kadastre-8-do-ddu",
  "topic_id": "B33",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-25",
  "theme_blocks": { "faq": "skip" }
}
```

## description-brief.json

```json
{
  "description": "«Техническая погрешность», — объяснил застройщик под Тюменью недостающие 400 м² земли. За бронь семья уже отдала 250 000 ₽, а подписать договор ей предложили без пересчёта цены."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/pod-tyumenyu-dom-ot-zastrojschika-v-broni-12-sotok-v-kadastre-8-do-ddu/`
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

- headline: Дом под Тюменью обещали на 12 сотках, но в кадастре 8 — ДДУ остановили
- description: «Техническая погрешность», — объяснил застройщик под Тюменью недостающие 400 м² земли. За бронь семья уже отдала 250 000 ₽, а подписать договор ей предложили без пересчёта цены.
- datePublished: 2026-09-25
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (theme_blocks.faq = skip, нет h3 FAQ-пар).

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
