import requests
import pandas as pd
from datetime import datetime

# Config
SPORT = "mlb"  # Change to "nba", "nfl", etc. if needed
DATE = datetime.now().strftime("%Y%m%d")
THRESHOLD = 70  # Minimum public % to track

API_URL = (
    f"https://api.actionnetwork.com/web/v2/scoreboard/publicbetting/"
    f"{SPORT}?bookIds=15,30,75,123,69,68,972,71,247,79&date={DATE}&periods=event"
)

def fetch_betting_data():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()

    data = response.json()
    games = []

    for game in data.get("games", []):
        team_away = game.get("team_away", {}).get("display_name")
        team_home = game.get("team_home", {}).get("display_name")

        if not team_away or not team_home:
            continue  # Skip incomplete games

        matchup = f"{team_away} @ {team_home}"
        public_data = game.get("public_bets", {})

        for bet_type in ["spread", "moneyline", "total"]:
            bet_info = public_data.get(bet_type, {})

            for side_key, team_name in [("away", team_away), ("home", team_home)]:
                percent = bet_info.get(side_key)
                if percent is not None and percent >= THRESHOLD:
                    games.append({
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "matchup": matchup,
                        "type": bet_type.capitalize(),
                        "side": team_name,
                        "percent": percent,
                        "result": "pending"
                    })

    return games

def save_to_csv(games, filename="data/tracked_bets.csv"):
    if not games:
        print("No high public bets found.")
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
    bets = fetch_betting_data()
    save_to_csv(bets)