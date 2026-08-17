"""Канон панелей обложки: 2 холста 2K 2×2 → 8 панелей (cover + 7 inline)."""

INLINE_COUNT = 7
INLINE_SLOT_KEYS = tuple(f"inline_{i}" for i in range(1, INLINE_COUNT + 1))
ALL_SLOT_KEYS = ("cover",) + INLINE_SLOT_KEYS
INLINE_FILES = {key: f"inline-{idx:02d}.png" for idx, key in enumerate(INLINE_SLOT_KEYS, start=1)}

# Два 2K-кадра 2048×1152; первое изображение: cover + 3 inline; второе: 4 inline.
CANVAS_SLOT_GROUPS = (
    ("cover", "inline_1", "inline_2", "inline_3"),
    ("inline_4", "inline_5", "inline_6", "inline_7"),
)
CANVAS_FILES = ("cover/canvas-quad-01.png", "cover/canvas-quad-02.png")
CANVAS_COUNT = 2
QUADRANT_ORDER = ("top_left", "top_right", "bottom_left", "bottom_right")

DEFAULT_SLOT_MAP = {
    "cover": "top_left",
    "inline_1": "top_right",
    "inline_2": "bottom_left",
    "inline_3": "bottom_right",
    "inline_4": "top_left",
    "inline_5": "top_right",
    "inline_6": "bottom_left",
    "inline_7": "bottom_right",
}

PIPELINE_ID = "dual_2k_quad_8_panels"
IMAGE_PROVIDER = "derouter"
MCP_SERVER = "DEROUTER"
RESOLUTION = "2K"
MIN_H2_FOR_INLINE = INLINE_COUNT
