import unittest

from build import match_stats


class MatchStatsTests(unittest.TestCase):
    def test_counts_and_win_rate(self):
        self.assertEqual(match_stats(["WIN", "LOSS", "WIN", "LOSS"]), (2, 2, 50))

    def test_empty_session(self):
        self.assertEqual(match_stats([]), (0, 0, 0))

    def test_rejects_invalid_result(self):
        with self.assertRaises(ValueError):
            match_stats(["WON"])
