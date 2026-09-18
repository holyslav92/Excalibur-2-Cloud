# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (derived — файла ещё нет)

```json
{
  "title": "В Тюмени 28 дней ждали переуступку — квартиру продали другому",
  "h1": "В Тюмени 28 дней ждали переуступку — квартиру продали другому",
  "slug": "v-tyumeni-28-dnej-ne-registrirovali-pereustupku-lot-zabral-drugoj",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-18",
  "description": "Договор уступки подписали, бронь внесли — но 28 дней регистрацию не подали, и за сутки до эскроу лот забрал другой покупатель",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени 28 дней ждали переуступку — квартиру продали другому",
  "title": "В Тюмени 28 дней ждали переуступку — квартиру продали другому",
  "subject": "Переуступка прав по ДДУ в тюменской новостройке: ожидание регистрации и потеря квартиры",
  "slug": "v-tyumeni-28-dnej-ne-registrirovali-pereustupku-lot-zabral-drugoj"
}
```

## research-context (datePublished)

- today_iso: 2026-09-18

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-28-dnej-ne-registrirovali-pereustupku-lot-zabral-drugoj/`
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

- headline: В Тюмени 28 дней ждали переуступку — квартиру продали другому
- description: Договор уступки подписали, бронь внесли — но 28 дней регистрацию не подали, и за сутки до эскроу лот забрал другой покупатель
- datePublished: 2026-09-18
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (нет h3 FAQ-пар), theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
