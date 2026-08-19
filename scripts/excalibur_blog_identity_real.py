"""Rotate identity-real live photo per article for Derouter/Kie i2i."""

from __future__ import annotations

import hashlib

IDENTITY_FILES: tuple[dict[str, str], ...] = (
    {"id": "hoodie_airpods", "file": "face-hoodie-airpods.jpeg"},
    {"id": "office_selfie", "file": "face-office-selfie.jpeg"},
    {"id": "greenhouse_yahweh", "file": "face-greenhouse-yahweh.png"},
    {"id": "immortal_regiment", "file": "face-immortal-regiment.jpeg"},
)


def pick_identity_reference(topic_id: str, slug: str = "") -> dict[str, str]:
    seed = f"{topic_id.strip()}:{slug.strip()}".encode("utf-8")
    digest = hashlib.md5(seed).hexdigest()
    idx = int(digest[:8], 16) % len(IDENTITY_FILES)
    return dict(IDENTITY_FILES[idx])
