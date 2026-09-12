# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "19 дней до 1 октября: банк пересчитал семейную ипотеку — семья остановила ДДУ",
  "h1": "19 дней до 1 октября: банк пересчитал семейную ипотеку — семья остановила ДДУ",
  "slug": "v-tyumeni-odobrili-semejnuyu-ipoteku-na-novostrojku-za-19-dnej-do-1-oktyabrya-ba",
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
  "h1": "19 дней до 1 октября: банк пересчитал семейную ипотеку — семья остановила ДДУ",
  "title": "19 дней до 1 октября: банк пересчитал семейную ипотеку — семья остановила ДДУ",
  "subject": "семейная ипотека на новостройку в Тюмени"
}
```

## description-brief.json

Одобрение на руках, бронь оплачена — казалось, до ДДУ в Тюмени оставался последний шаг. Но банк заново свёл цифры, и семейной ипотеке внезапно понадобился другой первоначальный взнос.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-odobrili-semejnuyu-ipoteku-na-novostrojku-za-19-dnej-do-1-oktyabrya-ba/`
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

- headline: 19 дней до 1 октября: банк пересчитал семейную ипотеку — семья остановила ДДУ
- description: Одобрение на руках, бронь оплачена — казалось, до ДДУ в Тюмени оставался последний шаг. Но банк заново свёл цифры, и семейной ипотеке внезапно понадобился другой первоначальный взнос.
- datePublished: 2026-09-12
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
