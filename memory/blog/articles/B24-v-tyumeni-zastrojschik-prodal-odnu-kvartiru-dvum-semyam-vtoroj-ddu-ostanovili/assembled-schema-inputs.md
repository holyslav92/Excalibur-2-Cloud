# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени застройщик продал 1 квартиру 2 семьям — второй ДДУ остановили",
  "h1": "В Тюмени застройщик продал 1 квартиру 2 семьям — второй ДДУ остановили",
  "slug": "v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-semyam-vtoroj-ddu-ostanovili",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-06",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени застройщик продал 1 квартиру 2 семьям — второй ДДУ остановили",
  "title": "В Тюмени застройщик продал 1 квартиру 2 семьям — второй ДДУ остановили",
  "subject": "Новостройка в Тюмени: застройщик продал один лот двум семьям, банк остановил второй ДДУ"
}
```

## description (article.meta + lead)

На одну квартиру в новостройке на севере Тюмени претендовали две семьи — вторую сделку остановили до внесения денег на эскроу. Святослав Шакин разбирает, почему CRM и бронь не равны зарегистрированному ДДУ.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-semyam-vtoroj-ddu-ostanovili/`
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

- headline: В Тюмени застройщик продал 1 квартиру 2 семьям — второй ДДУ остановили
- description: На одну квартиру в новостройке на севере Тюмени претендовали две семьи — вторую сделку остановили до внесения денег на эскроу. Святослав Шакин разбирает, почему CRM и бронь не равны зарегистрированному ДДУ.
- datePublished: 2026-09-06
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
