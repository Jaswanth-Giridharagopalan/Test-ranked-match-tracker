from pathlib import Path


def match_stats(results):
    wins = 0
    losses = 0

    for result in results:
        if result == "WIN":
            wins += 1
        elif result == "LOSS":
            losses += 1
        else:
            raise ValueError(f"Expected WIN or LOSS, got {result!r}")

    total = wins + losses
    win_rate = 0
    if total > 0:
        win_rate = wins / total * 100

    return wins, losses, win_rate


if __name__ == "__main__":
    results = Path("matches.txt").read_text(encoding="utf-8").splitlines()
    wins, losses, win_rate = match_stats(results)

    page = f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ranked Match Tracker</title>
<body style="background:#141b2d;color:#eef4ff;font:1.2rem system-ui;padding:2rem">
  <main>
    <h1>Ranked Match Tracker</h1>
    <p>Wins <strong>{wins}</strong> · Losses <strong>{losses}</strong></p>
    <p>Win rate <strong>{win_rate:.0f}%</strong></p>
  </main>
</body>
</html>
"""

    Path("site").mkdir(exist_ok=True)
    Path("site/index.html").write_text(page, encoding="utf-8")
