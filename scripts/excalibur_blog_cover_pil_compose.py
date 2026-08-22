#!/usr/bin/env python3
"""BLOCKER: PIL template mashup is FORBIDDEN on the publish path.

Emergency glue that pastes B06-template layers (erase masks, inset collage,
foreign hook text) is banned forever. One coherent generated cover only via
Derouter REST image API → Kie i2i fallback.

If both image APIs fail → report DEROUTER/KIE BLOCKER and STOP.
Do NOT upload mashup. Do NOT stamp Cover-QA PASS on PIL output.
"""

from __future__ import annotations

import sys


def main() -> int:
    print(
        "COVER PIL MASHUP BLOCKER: excalibur_blog_cover_pil_compose.py is forbidden.\n"
        "Use excalibur_blog_quad_regen_panels.py --slots cover (Derouter → Kie).\n"
        "If Derouter+Kie fail → STOP; do not upload template glue.\n"
        "See shared/blog-cover-quad-canvas-contract.md § PIL mashup ban.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
