# Schema inputs B34 — BlogPosting only (no FAQ section in article.html)

## Instructions
- Output valid JSON-LD with @graph: Organization, Person (author), BlogPosting.
- Use {{SITE_BASE}} for all site URLs — never [REDACTED] or live host.
- Canonical article URL: {{SITE_BASE}}/v-tyumeni-za-5-dnej-do-avansa-na-vtorichke-nashli-neuzakonennuyu-pereplanirovku-bank-snyal-odobrenie/ (no /blog/ prefix).
- datePublished: 2026-10-03
- Do NOT add FAQPage — article has no «Частые вопросы» H2 section (theme_blocks.faq=skip).

## article.meta.json
```json
{
  "title": "В Тюмени на вторичке за 5 дней до аванса банк снял одобрение из-за перепланировки",
  "h1": "В Тюмени на вторичке за 5 дней до аванса банк снял одобрение из-за перепланировки",
  "slug": "v-tyumeni-za-5-dnej-do-avansa-na-vtorichke-nashli-neuzakonennuyu-pereplanirovku-bank-snyal-odobrenie",
  "topic_id": "B34",
  "author_id": "svyatoslav-shakin",
  "date": "2026-10-03"
}
```

## description-brief.json (BlogPosting description)
Красивый «евро»-ремонт в тюменской трёшке скрывал расхождение: на плане БТИ перегородка есть, а в квартире её нет. За пять дней до аванса банк снял одобрение — семья остановила сделку.

## Author (authors-registry id svyatoslav-shakin)
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- Person @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (omit any [REDACTED] URLs): https://dzen.ru/holyslav, https://t.me/Tyumen_Rieltor, https://vk.ru/tymenrieltor, https://wa.me/79220016505, {{SITE_BASE}}/, {{SITE_BASE}}/rieltor-tyumen/, {{SITE_BASE}}/kontakty/

## Organization
- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/

## article.html excerpt (lead only)
За 5 дней до аванса банк отказался принимать эту квартиру в залог — одобрение по объекту сняли. Дело было не в доходе семьи и не в кредитной истории. Ремонт свежий: ровные стены, светлая кухня-гостиная...
