# Schema inputs — B34

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (синтез из title-brief + research-context; файла пока нет)

```json
{
  "title": "На вторичке оценка срезала 900 тысяч — ипотеку остановили",
  "h1": "На вторичке оценка срезала 900 тысяч — ипотеку остановили",
  "slug": "v-tyumeni-na-vtorichke-ocenka-na-900-tysyach-nizhe-dkp-bank-snyal-odobrenie",
  "topic_id": "B34",
  "author_id": "svyatoslav-shakin",
  "date": "2026-10-05",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B34",
  "h1": "На вторичке оценка срезала 900 тысяч — ипотеку остановили",
  "title": "На вторичке оценка срезала 900 тысяч — ипотеку остановили",
  "subject": "ипотека на вторичное жильё в Тюмени и банковская оценка квартиры",
  "angle": "Чистая выписка ЕГРН и предварительное одобрение не спасли покупателя: банковская оценка оказалась на 900 тысяч ниже цены в ДКП, поэтому ипотеку приостановили до аванса."
}
```

## description-brief.json

Отсутствует. description для BlogPosting: headline (title-brief.h1) или кратко angle — без выдуманных фактов.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-na-vtorichke-ocenka-na-900-tysyach-nizhe-dkp-bank-snyal-odobrenie/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (только публичные URL без [REDACTED]): https://dzen.ru/holyslav, https://t.me/Tyumen_Rieltor, https://vk.ru/tymenrieltor, https://wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png (можно ImageObject как в B31)

## BlogPosting

- headline: На вторичке оценка срезала 900 тысяч — ипотеку остановили
- description: На вторичке оценка срезала 900 тысяч — ипотеку остановили (или одно предложение из angle)
- datePublished: 2026-10-05 (research-context today_iso)
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p; theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage. Никакого литерала [REDACTED] в JSON.
