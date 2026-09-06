#!/usr/bin/env python3
"""Единый identity lock для cover: только face-studio-2026-06-23.jpg."""

from __future__ import annotations

from pathlib import Path

from excalibur_blog_site_base import expand_site_base, resolve_public_base_from_env

FACE_PRIMARY = Path("memory/cover/assets/identity-real/face-studio-2026-06-23.jpg")
IDENTITY_PUBLIC_PATH = "/wp-content/uploads/2026/06/2026-06-23-15.57.42.jpg"
COVER_PHONE = "+7 922 001 65 05"

BODY_LOCK = (
    "medium slim build (NOT chubby/puffy/thick neck); black blazer over black tee unless scene needs otherwise"
)
I2I_EXPRESSION_LOCK = (
    "same person identity from reference photo — NEW invented expression for hook; "
    "do NOT copy reference studio smile/pose; preserve jaw/stubble/hairline/eyes"
)
IDENTITY_SUFFIX = (
    "\nIDENTITY LOCK (mandatory): exact same man as reference photo (Svyatoslav Shakin, Tyumen realtor) — "
    "28 years old, medium-slim build, round-oval face, dark brown short hair tapered sides, "
    "warm dark brown eyes, full dark brows. "
    "MANDATORY visible dark five-o'clock-shadow stubble on jaw, chin and upper lip — "
    "same density and pattern as reference; NEVER clean-shaven, NEVER fashion-model jaw. "
    "Bone structure, hairline, stubble pattern, eye shape MUST match studio portrait. "
    "Black blazer over black tee like reference when outfit not specified. "
    "BAN: beige vest, mustard shirt, yellow sweater, sage-green shirt, brown knit vest — generic stock outfits. "
    "NEW invented emotion/scene — do NOT clone reference studio smile/pose/background."
)
COVER_I2I_BANS = (
    "BAN HARD: ANY text on clothes/chest; Wordstat/search strips; blue halos on hair; "
    "generic stock-model face; different person than reference; mustard+navy vest repeat; "
    "beige waistcoat; yellow hoodie sweater; sage office shirt; clean-shaven young model; "
    "dark cinematic; chubby host; polite studio smile copy from reference."
)


def identity_public_url() -> str:
    live = resolve_public_base_from_env()
    placeholder = f"{{{{SITE_BASE}}}}{IDENTITY_PUBLIC_PATH}"
    if live:
        return expand_site_base(placeholder, live)
    return placeholder


def ensure_face_reference(root: Path) -> Path:
    path = root / FACE_PRIMARY
    if not path.is_file():
        from excalibur_blog_identity_real import ensure_identity_reference

        path = ensure_identity_reference(root)
    if not path.is_file():
        raise FileNotFoundError(f"FACE i2i BLOCKER: missing {FACE_PRIMARY}")
    return path
