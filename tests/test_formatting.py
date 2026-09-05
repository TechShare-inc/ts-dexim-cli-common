"""Tests for shared CLI formatting helpers."""

import unittest

from dexim.cli.common.formatting import status_badge


class StatusBadgeTests(unittest.TestCase):
    """Verify the public status badge strings."""

    def test_online_status_uses_ascii_marker(self) -> None:
        self.assertEqual(status_badge(ok=True), "[success]* ONLINE[/]")

    def test_offline_status_uses_ascii_marker(self) -> None:
        self.assertEqual(status_badge(ok=False), "[error]* OFFLINE[/]")


if __name__ == "__main__":
    unittest.main()
