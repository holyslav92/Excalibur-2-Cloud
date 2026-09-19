# Schema inputs — B28

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

(файл отсутствует — поля из title-brief.json и research-context)

```json
{
  "title": "Под Тюменью дом в КП не приняли — потолки на 25 см ниже обещанного",
  "h1": "Под Тюменью дом в КП не приняли — потолки на 25 см ниже обещанного",
  "slug": "v-tyumeni-v-dome-kp-potolki-nizhe-ddu-na-25-santimetrov-zamer-na-sdache-pokazal-",
  "topic_id": "B28",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-19",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B28",
  "h1": "Под Тюменью дом в КП не приняли — потолки на 25 см ниже обещанного",
  "title": "Под Тюменью дом в КП не приняли — потолки на 25 см ниже обещанного",
  "subject": "Дом от застройщика в КП под Тюменью: потолки ниже указанной в ДДУ высоты на 25 см."
}
```

## description (teaser для BlogPosting.description)

В приложении к ДДУ было 2,7 м, лазер на сдаче показал 2,45 м в гостиной и спальнях. Застройщик предложил 80 тысяч за подпись акта — семья отказалась. Согласились бы вы на такую скидку или вышли из сделки?

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-dome-kp-potolki-nizhe-ddu-na-25-santimetrov-zamer-na-sdache-pokazal-/`
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

- headline: Под Тюменью дом в КП не приняли — потолки на 25 см ниже обещанного
- description: В приложении к ДДУ было 2,7 м, лазер на сдаче показал 2,45 м в гостиной и спальнях. Застройщик предложил 80 тысяч за подпись акта — семья отказалась. Согласились бы вы на такую скидку или вышли из сделки?
- datePublished: 2026-09-19
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
