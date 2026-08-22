#!/usr/bin/env python3
"""BLOCKER: Kie image API is FORBIDDEN forever for The Риэлтор tenant.

Owner override (2026-08-22): all cover/inline images via grsai grsai standard image model
(scripts/excalibur_blog_grsai_gpt_image2_api.py). Never call Kie again.
If grsai fails → GRSAI IMAGE BLOCKER, STOP.
"""

from __future__ import annotations

import sys


def main() -> int:
    print(
        "KIE IMAGE BLOCKER: excalibur_blog_kie_gpt_image2_api.py is forbidden for The Риэлтор.\n"
        "Use scripts/excalibur_blog_grsai_gpt_image2_api.py (grsai grsai standard image model REST).\n"
        "Optional: EXCALIBUR_IMAGE_FALLBACK_DEROUTER=1 for Derouter image fallback.\n"
        "Do NOT use Kie. Do NOT use PIL mashup. See shared/kie-gpt-image-api-contract.md.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
