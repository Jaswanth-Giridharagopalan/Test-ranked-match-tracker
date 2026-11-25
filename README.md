# Test-ranked-match-tracker
# Ranked Match Tracker

A small Python dashboard for tracking my Valorant ranked matches. I built it to learn how a change in GitHub goes through automated tests and ends up on a live website.

## What it tracks

Each line in `matches.txt` represents one match and contains either `WIN` or `LOSS`. The dashboard shows total wins, total losses, and win rate. For example, two wins and two losses gives a **50% win rate**.

## How the CI/CD pipeline works

1. **Commit a change.** I add a match result to `matches.txt` and commit it to `main`.
2. **Test and build (CI).** GitHub Actions runs the Python tests. If they pass, `build.py` reads the match results and generates the dashboard.
3. **Publish (CD).** GitHub Pages publishes the new dashboard after a successful build. If a test fails, the previous version stays online.

## Project files

| File | What it does |
| --- | --- |
| `matches.txt` | Stores match results, one per line. |
| `build.py` | Counts wins and losses, calculates win rate, and generates the HTML page. |
| `test_build.py` | Tests the calculations, an empty match history, and invalid input. |
| `.github/workflows/ci-cd.yml` | Defines when GitHub runs the tests, builds the dashboard, and publishes it. |

## Run locally

With Python installed, run these commands from the project folder:

```bash
python -m unittest -v
python build.py
```

Open `site/index.html` in your browser to see the dashboard.
