# Identity-real — live photos (SOURCE OF TRUTH)

**Только эти четыре файла** задают лицо Святослава Шакина (28 лет) для i2i. Это live-фото, не AI.

| Файл | Роль |
|------|------|
| `face-hoodie-airpods.jpeg` | PRIMARY geometry lock (родинки, крупный план) |
| `face-office-selfie.jpeg` | Круглое лицо, щетина |
| `face-greenhouse-yahweh.png` | Full-body likeness; **не клонировать** оранжерею |
| `face-immortal-regiment.jpeg` | **Только лицо**; не клонировать марш/портрет |

Копии держать в `memory/setup/visual-inbox/`.

## i2i rotation

`blog-hero.json` → `i2i_reference_rotation` — derouter/Kie ротирует по `topic_id`.

## Запрещено как FACE source

- `scene-composition-only/hero-ref-*.jpg` (AI-стилизованные обложки)
- `portrait.jpg` / `portrait-landing.jpg` (старый navy-blazer set, не primary)

## Staging

```bash
python3 scripts/excalibur_blog_identity_real.py --stage-from-inbox
python3 scripts/excalibur_blog_identity_real.py --check
```
