from pathlib import Path

from build import match_stats

results = Path("matches.txt").read_text(encoding="utf-8").splitlines()
wins, losses, win_rate = match_stats(results)

report = (
    "## Match stats\n\n"
    f"- Wins: {wins}\n"
    f"- Losses: {losses}\n"
    f"- Win rate: {win_rate:.0f}%\n"
)

Path("report.md").write_text(report, encoding="utf-8")
