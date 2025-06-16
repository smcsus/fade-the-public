from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime

def scrape_with_selenium():
    options = Options()
    options.add_argument("--headless")  # run in background
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.actionnetwork.com/public-betting")

    driver.get("https://www.actionnetwork.com/public-betting")

    # Dump the page content to inspect what loaded
    with open("debug.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("Page loaded and saved to debug.html")

    # Wait up to 10 seconds for the table to fully load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='public-betting-table'] tbody tr"))
    )

    rows = driver.find_elements(By.CSS_SELECTOR, "[data-testid='public-betting-table'] tbody tr")
    games = []

    for row in rows:
        try:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) < 4:
                continue

            matchup = cols[0].text
            spread = cols[1].text
            moneyline = cols[2].text
            total = cols[3].text

            def parse_percent(value):
                try:
                    return int(value.replace("%", "").strip())
                except:
                    return 0

            for bet_type, percent_str in zip(["Spread", "Moneyline", "Total"], [spread, moneyline, total]):
                percent = parse_percent(percent_str)
                if percent >= 70:  # you can raise this back to 90 later
                    games.append({
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "matchup": matchup,
                        "type": bet_type,
                        "percent": percent,
                        "result": "pending"
                    })

        except Exception as e:
            print(f"Error parsing row: {e}")

    driver.quit()
    return games

def save_to_csv(games, filename="data/tracked_bets.csv"):
    if not games:
        print("No 70%+ bets found.")
        return

    df = pd.DataFrame(games)
    try:
        existing = pd.read_csv(filename)
        df = pd.concat([existing, df], ignore_index=True).drop_duplicates()
    except FileNotFoundError:
        pass

    df.to_csv(filename, index=False)
    print(f"Saved {len(games)} bets to {filename}.")

if __name__ == "__main__":
    bets = scrape_with_selenium()
    save_to_csv(bets)