# Schema inputs — B26

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "На приёмке в Тюмени нашли брак — застройщик потребовал 190 тысяч",
  "h1": "На приёмке в Тюмени нашли брак — застройщик потребовал 190 тысяч",
  "slug": "v-tyumeni-ne-podpisali-akt-s-brakom-zastrojschik-vystavil-shtraf-190-tysyach",
  "topic_id": "B26",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B26",
  "h1": "На приёмке в Тюмени нашли брак — застройщик потребовал 190 тысяч",
  "title": "На приёмке в Тюмени нашли брак — застройщик потребовал 190 тысяч",
  "subject": "Приёмка квартиры в тюменской новостройке по ДДУ",
  "angle": "Семья обнаружила дефекты и не подписала акт, но застройщик потребовал около 190 000 ₽ за якобы затягивание приёмки."
}
```

## description (article.meta / Дзен-карточка)

На приёмке в Тюмени нашли брак — застройщик потребовал 190 тысяч

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-ne-podpisali-akt-s-brakom-zastrojschik-vystavil-shtraf-190-tysyach/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/[REDACTED], vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: На приёмке в Тюмени нашли брак — застройщик потребовал 190 тысяч
- description: На приёмке в Тюмени нашли брак — застройщик потребовал 190 тысяч
- datePublished: 2026-09-05
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (нет пар h3+p), theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
