# Title role inputs — B33

**task:** One H1/title in Klyshin news-casus rhythm (~50–70 chars preferred; draft may be tightened). Base on Scout **title_draft**. JSON only in output file per skill schema.

**topic_id:** B33

## Scout title_draft (use as base — refine length/rhythm, keep mechanism)

За 4 дня до ДДУ в Тюмени в декларации всплыло частичное введение дома — банк снял ипотеку на новостройку

## Casus (completed event + stakes + finale)

- Family, Tyumen multi-section newbuild, DDU + mortgage planned; sales said «дом сдаётся».
- 4 days before DDU: project declaration on dom.rf shows **partial commissioning** — buyer's section not commissioned.
- Bank withdraws mortgage approval on collateral; escrow not opened; booking partly retained; mortgage reworked on another lot.
- **Not B26** (no RVE whole building). **Not B27** (land lease in declaration).

## dzen_casus_shape

PASS — event, risk, time (4 days), finale, comment magnet.

## comment_magnet_angle (from Scout — pass through or sharpen)

«Если в декларации частичный ввод, а вам обещали “уже сдано”, вы подпишете ДДУ ради сохранения брони или дождётесь полного ввода секции?»

## klyshin_hook

optional — none

## Wordstat demand spine (do NOT paste raw SEO into H1)

- P0: «купить новостройку в тюмени» — 892 (scout handoff; research assembly 678)
- Context: «новостройки тюмень» — 3504
- Mechanism phrases weak in Wordstat — story spine = partial commissioning in declaration + bank before DDU

## h1_fingerprint (must preserve for anti-dupe)

`4-дня-до-ДДУ + частичное-введение-секции + банк-снял-ипотеку`

## published-titles-only — avoid duplicate angle

- B27: «За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду» (different mechanism: land lease)
- B26: whole building no RVE
- B22/B29/B31/B32: other bank-before-DDU mechanics (rate, zero down, insurance, escrow entity)
- No existing title for partial commissioning + declaration + bank before DDU

## Forbidden

Checklist/N steps hooks; SEO tail «полный гайд», «2026»; label head; colon+keyword; copy Klyshin verbatim.

## Required JSON fields

topic_id, h1, title (same as h1), subject, angle, comment_magnet_angle, verdict: PASS
