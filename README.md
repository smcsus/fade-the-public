# fade-the-public

**fade-the-public** is a Python project that tracks public betting percentages from [Action Network](https://www.actionnetwork.com/public-betting), logs bets where a large majority of the public is on one side, and eventually compares those picks to actual game results to measure how accurate the public is.

## Current Features

- Uses a headless Chrome browser via Selenium to scrape betting data
- Filters and logs games with 70% or more public action on any side (Spread, Moneyline, or Total)
- Stores logged bets in `data/tracked_bets.csv` with date, matchup, type, percent, and result
- All scraping is fully automated and browser-accurate (JS-rendered content supported)

## In Progress

- Automatic result tracking (scraping or API-based)
- Evaluation logic to mark public bets as win/loss
- Daily summary reports or alert notifications (Discord or email)
- Scheduled background execution (hourly or daily)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/fade-the-public.git
cd fade-the-public
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install ChromeDriver v115 (to match local Chrome browser)

Download and install ChromeDriver manually if needed (see project notes).

### 5. Run the scraper

```bash
python src/scrape_bets.py
```

## Requirements

- Python 3.9+
- Google Chrome browser
- ChromeDriver v115 (or matching version for your installed Chrome)

## Author

Steven Masters