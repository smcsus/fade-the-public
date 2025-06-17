# fade-the-public

**fade-the-public** is a Python project that tracks public betting percentages from [Action Network](https://www.actionnetwork.com/public-betting), logs bets where a large majority of the public is on one side, and eventually compares those picks to actual game results to measure how accurate the public is.

## Current Features

- Scrapes public betting percentages using Action Network’s JSON API (no Selenium required)
- Filters and logs bets where either side (home or away) has ≥ 70% of the public on spread, moneyline, or total
- Outputs data to `data/tracked_bets.csv` with:  
  `date`, `matchup`, `type`, `side`, `percent`, and `result`
- Uses simple, fast, and reliable `requests`-based logic for all data pulls

## In Progress

- Automatic result checking via API or boxscore scraping
- Evaluation logic to determine if the public side won or lost
- Alerts or summaries via Discord or email
- Multi-sport support with CLI toggle (e.g. MLB, NBA, NFL)
- Daily/hourly automation with cron or task scheduler

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/fade-the-public.git
cd fade-the-public
```

### 2. Create and activate the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the scraper

```bash
python src/scrape_bets.py
```

## Requirements

- Python 3.9+
- Internet connection to fetch API data from Action Network

## Notes

- This project **no longer uses ChromeDriver or Selenium**
- All scraping is done directly from Action Network’s structured public API

## Author

Steven Masters