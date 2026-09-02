# Schema inputs — B21

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени оплатили переуступку — застройщик не оформил ДДУ",
  "h1": "В Тюмени оплатили переуступку — застройщик не оформил ДДУ",
  "slug": "v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat-",
  "topic_id": "B21",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-02",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B21",
  "h1": "В Тюмени оплатили переуступку — застройщик не оформил ДДУ",
  "title": "В Тюмени оплатили переуступку — застройщик не оформил ДДУ",
  "subject": "Переуступка права по ДДУ в новостройке",
  "angle": "Покупатель заплатил продавцу переуступки, но до регистрации цессии не стал новым дольщиком: застройщик отказал в переоформлении ДДУ, сделка остановилась до открытия эскроу."
}
```

## description-brief.json

```json
{
  "topic_id": "B21",
  "description": "Расчёт начали не с того конца: семья отдала аванс продавцу переуступки, а застройщик не пустил её в ДДУ. До эскроу оставались два дня — и квартира вернулась в продажу."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat-/`
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

- headline: В Тюмени оплатили переуступку — застройщик не оформил ДДУ
- description: Расчёт начали не с того конца: семья отдала аванс продавцу переуступки, а застройщик не пустил её в ДДУ. До эскроу оставались два дня — и квартира вернулась в продажу.
- datePublished: 2026-09-02
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
