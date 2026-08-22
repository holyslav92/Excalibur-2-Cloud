#!/usr/bin/env python3
"""BLOCKER: Kie image API is FORBIDDEN forever for The Риэлтор tenant.

Owner override (2026-08-22): all cover/inline images ONLY via Derouter
(REST api-direct.derouter.ai preferred; DEROUTER MCP if REST down).
Never call Kie again. If Derouter fails → DEROUTER BLOCKER, STOP.
"""

from __future__ import annotations

import sys


def main() -> int:
    print(
        "KIE IMAGE BLOCKER: excalibur_blog_kie_gpt_image2_api.py is forbidden for The Риэлтор.\n"
        "Use scripts/excalibur_blog_derouter_gpt_image2_api.py (api-direct REST).\n"
        "If REST down → retry/fix Derouter or invoke DEROUTER MCP from conductor.\n"
        "Do NOT use Kie. Do NOT use PIL mashup. See shared/kie-gpt-image-api-contract.md.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
