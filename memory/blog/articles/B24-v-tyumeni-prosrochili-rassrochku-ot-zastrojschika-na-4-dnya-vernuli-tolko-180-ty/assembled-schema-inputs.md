# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени рассрочку у застройщика просрочили на 4 дня — квартира ушла",
  "h1": "В Тюмени рассрочку у застройщика просрочили на 4 дня — квартира ушла",
  "slug": "v-tyumeni-prosrochili-rassrochku-ot-zastrojschika-na-4-dnya-vernuli-tolko-180-ty",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-11",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени рассрочку у застройщика просрочили на 4 дня — квартира ушла",
  "title": "В Тюмени рассрочку у застройщика просрочили на 4 дня — квартира ушла",
  "subject": "Рассрочка у застройщика при покупке квартиры в тюменской новостройке",
  "angle": "Четыре дня просрочки превратили «покупку без банка» в расторжение договора: семье вернули лишь часть первого взноса, а квартиру продали другому."
}
```

## description (для BlogPosting.description)

Четыре дня просрочки по рассрочке у застройщика в Тюмени обернулись расторжением: семье вернули 180 тысяч из 400, а квартиру ушла другому. Святослав Шакин разбирает, какой договор стоит за «покупкой без банка» и где заканчивается защита 214-ФЗ.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-prosrochili-rassrochku-ot-zastrojschika-na-4-dnya-vernuli-tolko-180-ty/`
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

- headline: В Тюмени рассрочку у застройщика просрочили на 4 дня — квартира ушла
- description: Четыре дня просрочки по рассрочке у застройщика в Тюмени обернулись расторжением: семье вернули 180 тысяч из 400, а квартиру ушла другому. Святослав Шакин разбирает, какой договор стоит за «покупкой без банка» и где заканчивается защита 214-ФЗ.
- datePublished: 2026-09-11
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
