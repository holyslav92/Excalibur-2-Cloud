# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени трейд-ин сорвался накануне ДДУ — квартиру не приняли",
  "h1": "В Тюмени трейд-ин сорвался накануне ДДУ — квартиру не приняли",
  "slug": "v-tyumeni-trejd-in-sorvalsya-nakanune-ddu-zastrojschik-ne-prinyal-ih-kvartiru",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-10",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени трейд-ин сорвался накануне ДДУ — квартиру не приняли",
  "title": "В Тюмени трейд-ин сорвался накануне ДДУ — квартиру не приняли",
  "subject": "трейд-ин старой квартиры у застройщика перед подписанием ДДУ на новостройку в Тюмени"
}
```

## description (из лида статьи)

Семья в Тюмени остановила покупку новостройки за сутки до ДДУ: оценка старой квартиры по trade-in оказалась на 1,2 млн ₽ ниже ориентира менеджера, первоначального взноса не хватило. Святослав Шакин разбирает, почему бронь и ипотека не заменяют подтверждённый выкуп.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-trejd-in-sorvalsya-nakanune-ddu-zastrojschik-ne-prinyal-ih-kvartiru/`
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

- headline: В Тюмени трейд-ин сорвался накануне ДДУ — квартиру не приняли
- description: Семья в Тюмени остановила покупку новостройки за сутки до ДДУ: оценка старой квартиры по trade-in оказалась на 1,2 млн ₽ ниже ориентира менеджера, первоначального взноса не хватило. Святослав Шакин разбирает, почему бронь и ипотека не заменяют подтверждённый выкуп.
- datePublished: 2026-09-10
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
