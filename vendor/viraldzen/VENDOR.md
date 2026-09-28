# ViralDzen (vendored)

- **Upstream:** https://github.com/Horosheff/ViralDzen
- **License:** MIT (`LICENSE`)
- **Pinned commit:** `44eded1d824736a5de9ec399048d9dce5a3e8098`
- **Scope:** Excalibur BLOG — The Риэлтор only (`tymenrieltor.ru` / `dzen.ru/holyslav`)

Код пакета **не меняем**. Обёртки пайплайна: `scripts/excalibur_blog_viraldzen_wrapper.py`, `scripts/excalibur_blog_trend_radar.py`.

Запуск CLI из корня репозитория:

```bash
PYTHONPATH=vendor/viraldzen python3 -m viraldzen -h
```

Минимальная задержка запросов: `--delay 0.7` (жёстко в обёртках).
