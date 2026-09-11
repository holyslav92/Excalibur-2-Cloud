# Description inputs — B35

## Task

Write `description-brief.json` for Dzen card teaser. Output **only valid JSON** matching the schema in the skill.

## topic_id

B35

## title-brief.json (H1 — do NOT copy)

- h1: В Тюмени ДДУ запретил аренду до ключей — инвестор потерял жильцов
- angle: Условие в приложении к ДДУ сорвало план сдачи ещё до подписания договора: инвестор отказался от сделки, лишился брони и двух будущих жильцов.

## article.html opening (do NOT truncate or repeat)

First paragraph: В Тюмени инвестор договорился с двумя будущими жильцами о въезде в новостройку, а перед подписанием ДДУ обнаружил: сдавать квартиру до передачи по акту и регистрации права запрещает приложение №3. До конца брони оставалось две недели...

## Story spine (for hook energy, not spoiler checklist)

- Investor bought one-room newbuild for rental income; two future tenants lined up.
- Appendix #3 to DDU bans renting until both handover act AND property registration — not either/or.
- Two weeks left on reservation; refused to sign DDU; lost reservation and both tenants went to neighboring project.
- No DDU/escrow money paid — stopped before deal.

## geo / voice

Тюмень, Святослав Шакин / The Риэлтор (facts, not vanity label head).

## Constraints (shared/dzen-description-rules.md)

- 1–2 sentences, ~120–220 chars (max 250)
- Klyshin + news headline rhythm: case hook, intrigue, consequence hint
- ≠ title (casefold)
- ≠ truncated lead / same opening phrase as first <p>
- No SEO checklist blurb, no how-to teaser
- Cyrillic; Latin only for brands (ДДУ, ЕГРН)

## Required JSON output schema

```json
{
  "topic_id": "B35",
  "description": "...",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
