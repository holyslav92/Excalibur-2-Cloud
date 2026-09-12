# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Под Тюменью дом от застройщика не приняли из-за брака на 850 тысяч",
  "h1": "Под Тюменью дом от застройщика не приняли из-за брака на 850 тысяч",
  "slug": "pod-tyumenyu-dom-ot-zastrojshchika-ne-prinyali-iz-za-braka-na-850-tysyach",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-12",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "Под Тюменью дом от застройщика не приняли из-за брака на 850 тысяч",
  "title": "Под Тюменью дом от застройщика не приняли из-за брака на 850 тысяч",
  "subject": "Дом от застройщика под Тюменью: отказ от приёмки из-за строительных дефектов",
  "slug": "pod-tyumenyu-dom-ot-zastrojshchika-ne-prinyali-iz-za-braka-na-850-tysyach"
}
```

## description (teaser для BlogPosting)

Под Тюменью семья остановила приёмку нового дома: тепловизор выявил промерзание, продувание окон и брак кровли, а смета переделок дошла до 850 тысяч. Святослав Шакин разбирает, почему нельзя подписывать чистый акт под обещание гарантийного ремонта.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/pod-tyumenyu-dom-ot-zastrojshchika-ne-prinyali-iz-za-braka-na-850-tysyach/`
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

- headline: Под Тюменью дом от застройщика не приняли из-за брака на 850 тысяч
- description: Под Тюменью семья остановила приёмку нового дома: тепловизор выявил промерзание, продувание окон и брак кровли, а смета переделок дошла до 850 тысяч. Святослав Шакин разбирает, почему нельзя подписывать чистый акт под обещание гарантийного ремонта.
- datePublished: 2026-09-12
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
