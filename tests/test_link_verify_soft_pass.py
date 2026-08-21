"""Link verify soft-pass tests for RF official hosts."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class LinkVerifySoftPassTests(unittest.TestCase):
    def test_notariat_timeout_is_soft_external(self) -> None:
        from excalibur_blog_link_verify import is_soft_external_failure

        result = {"status": None, "error": "The read operation timed out"}
        self.assertTrue(
            is_soft_external_failure("https://notariat.ru/", result)
        )

    def test_notariat_404_is_soft_external(self) -> None:
        from excalibur_blog_link_verify import is_soft_external_failure

        result = {"status": 404, "error": "HTTP 404"}
        self.assertTrue(
            is_soft_external_failure("https://notariat.ru/", result)
        )

    def test_notariat_200_is_not_soft_external(self) -> None:
        from excalibur_blog_link_verify import is_soft_external_failure

        result = {"status": 200, "ok": True}
        self.assertFalse(
            is_soft_external_failure("https://notariat.ru/", result)
        )


if __name__ == "__main__":
    unittest.main()
