# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В КП Тюмени купили 12 соток — намерили 9,7 и остались без ключей",
  "h1": "В КП Тюмени купили 12 соток — намерили 9,7 и остались без ключей",
  "slug": "v-tyumeni-v-dogovore-kp-obeschali-12-sotok-na-klyuchah-okazalos-9-7",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-13",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В КП Тюмени купили 12 соток — намерили 9,7 и остались без ключей",
  "title": "В КП Тюмени купили 12 соток — намерили 9,7 и остались без ключей",
  "subject": "Площадь участка при покупке дома у застройщика в коттеджном посёлке Тюмени: договорные 12 соток против фактических 9,7."
}
```

## description (из лида article.html)

В Тюмени семья купила дом с участком 12 соток, а за три дня до передачи получила межевой план на 9,7 — и осталась без ключей. Застройщик предложил принять уменьшенный участок без пересчёта цены или доплатить за соседний фрагмент.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-dogovore-kp-obeschali-12-sotok-na-klyuchah-okazalos-9-7/`
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

- headline: В КП Тюмени купили 12 соток — намерили 9,7 и остались без ключей
- description: В Тюмени семья купила дом с участком 12 соток, а за три дня до передачи получила межевой план на 9,7 — и осталась без ключей. Застройщик предложил принять уменьшенный участок без пересчёта цены или доплатить за соседний фрагмент.
- datePublished: 2026-09-13
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
