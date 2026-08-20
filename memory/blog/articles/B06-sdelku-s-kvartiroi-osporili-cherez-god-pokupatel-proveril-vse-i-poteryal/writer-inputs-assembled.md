# Writer inputs — B06 repair

Read research-notes.md and title-brief.json in this article dir.

## JOB
Complete truncated article. Existing partial HTML is below — KEEP case facts, EXPAND to full longform.

Target after Sol: 2000-2600 words, 7+ H2, 7 inline figure placeholders (inline_1..inline_7).

## MUST FIX (Dzen comments)
1. Price: write FULL «от 60 000 до 150 000 рублей» or «от 60 до 150 тысяч рублей» — never chop «руб»
2. New H2 section answering myth: buyer shouldn't care where seller sent money; if voided seller returns cash — explain real life: lose apartment AND wait years for money; добросовестный приобретатель; VS July 2026 — no «гарантия», no zero-risk promise
3. Finish «Сколько стоит спокойствие» section: what accompaniment includes, NOT court-outcome guarantee

## CTA (quality-bar-9)
- After hook + TL;DR: excalibur-cta-early — TG https://t.me/Tyumen_Rieltor + MAX https://max.ru/id561413315447_biz only
- Mid after main checklist: excalibur-cta-mid
- End: excalibur-cta-end — dual CTA consultation OR «сразу в сделку» + full channels (TG, MAX, site, Dzen, VK, guides)
- Phone +7 922 001 65 05 once in body (tel:+79220016505)

## INTERLINK 2-4 (keep in draft)
- /blog/vtorichka-i-riski/raspisku-na-kvartiru-napisali-deneg-na-schete-net/
- /blog/vtorichka-i-riski/doverennost-ne-bronya-prodavec-priletel-odin-a-kvartiru-prodavali-chetvero/
- /blog/vtorichka-i-riski/pochti-vnesli-zadatok-za-48-chasov-do-torgov-kvartiru-podarili-docheri/
- /blog/vtorichka-i-riski/skidku-dva-milliona-obeschali-a-v-kvartire-pryatali-risk/

## H2 OUTLINE (minimum)
H2: Как выглядит эта история изнутри
H2: Почему «все документы чистые» перестало быть гарантией
H2: Что суд считает признаками неосмотрительности (table — columns must DIFFER)
H2: Тюменская специфика: два запрета и одна ловушка
H2: Порядок действий, который реально снижает риск (checklist)
H2: Миф «продавец просто вернёт деньги» — почему это не работает
H2: Сколько стоит сопровождение и что в него входит
H2: Частые вопросы (FAQ 3-4 questions)

## INLINE FIGURES
Each H2 (except FAQ) needs:
```html
<figure class="inline-quad" data-slot="inline_N">
  <img src="cover/inline-0N.png" alt="..." loading="lazy">
</figure>
```
N=1..7

## EXISTING PARTIAL CONTENT (continue from cut point)

Opening TL;DR paragraph (no H1 in writer draft):

Оспаривание сделки с квартирой возможно и через год после регистрации права собственности, если продавец заявляет, что действовал под влиянием обмана или заблуждения. Верховный суд РФ в июле 2026 года разъяснил: сделку жертвы мошенников признают недействительной только тогда, когда покупатель знал или должен был знать об обмане. Главный риск для покупателя — статус добросовестного приобретателя приходится доказывать в суде. Перед сделкой проверяют выписку ЕГРН, историю перехода прав, дееспособность и поведение продавца.

[Then existing H2 sections through cut at:]
Сопровождение покупки в Тюмени у частного риелтора обычно стоит от 60 до 150 тысяч р

## RULES
- Facts only from research-notes.md
- No invented court stats
- Tyumen specifics
- Short paragraphs Klyshin rhythm
- Output: HTML fragment only, no h1
