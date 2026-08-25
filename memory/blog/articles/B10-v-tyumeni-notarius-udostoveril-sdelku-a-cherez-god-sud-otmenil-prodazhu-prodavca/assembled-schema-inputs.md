# Schema inputs — B10 — 2026-08-24

## Task
Output **only** valid JSON-LD for `schema.jsonld` per skill. Use `{{SITE_BASE}}` placeholder for all site URLs (never `[REDACTED]`). No markdown fences in output file.

## topic_id
B10

## Site base
- Placeholder for git artifact: `{{SITE_BASE}}`
- Canonical article URL: `{{SITE_BASE}}/v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil-prodazhu-prodavca/`
- **Never** use `/blog/` prefix in URLs.

## datePublished
2026-08-24 (from research-context today_iso)

## title-brief.json
```json
{
  "topic_id": "B10",
  "h1": "В Тюмени суд отменил продажу: продавец должна вернуть 4,3 млн",
  "title": "В Тюмени суд отменил продажу: продавец должна вернуть 4,3 млн",
  "subject": "Оспоренная продажа квартиры в Тюмени после давления телефонных мошенников и реституция 4,3 млн рублей",
  "angle": "Завершённая сделка была отменена судом, но победившая в споре продавец осталась обязана вернуть покупателям деньги, уже ушедшие мошенникам.",
  "comment_magnet_angle": "Если пожилой продавец странно реагирует на звонки и не отпускает телефон, вы продолжите сделку или остановите её даже после всех проверок?",
  "verdict": "PASS"
}
```

## article.meta.json
```json
{
  "title": "В Тюмени суд отменил продажу: продавец должна вернуть 4,3 млн",
  "h1": "В Тюмени суд отменил продажу: продавец должна вернуть 4,3 млн",
  "slug": "v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil-prodazhu-prodavca",
  "topic_id": "B10",
  "author_id": "svyatoslav-shakin",
  "description": "В Тюмени суд отменил продажу: продавец должна вернуть 4,3 млн",
  "date": "2026-08-24",
  "theme_blocks": {
    "faq": "skip",
    "quiz": "skip",
    "side_stickers": "skip"
  }
}
```

## Author (from shared/authors-registry.json — author_id svyatoslav-shakin)
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- Person @id: `{{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin`
- url: `{{SITE_BASE}}/rieltor-tyumen/`
- sameAs: `{{SITE_BASE}}/`, `{{SITE_BASE}}/rieltor-tyumen/`, `{{SITE_BASE}}/kontakty/`, https://dzen.ru/holyslav, https://t.me/Tyumen_Rieltor, https://t.me/holyslav92, https://vk.ru/tymenrieltor, https://wa.me/79220016505

## Organization
- name: The Риэлтор
- @id: `{{SITE_BASE}}/#organization`
- url: `{{SITE_BASE}}/`
- logo: `{{SITE_BASE}}/wp-content/uploads/logo.png`

## FAQ section
**NONE** — `theme_blocks.faq` = skip. Article HTML has no `<h2>Частые вопросы</h2>` section.
**Do NOT** add FAQPage. BlogPosting only.

## Required @graph structure (match B01/B02 pattern)
1. Organization
2. Person (author)
3. BlogPosting with headline, description, datePublished, inLanguage ru-RU, author @id ref, publisher @id ref, url, mainEntityOfPage

## Output
Single JSON object with @context and @graph. Valid JSON only.
