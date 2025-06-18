from utils import read_bets_csv, write_bets_csv
from check_results import check_result

bets = read_bets_csv("data/tracked_bets.csv")
updated = []

for bet in bets:
    if bet["result"] != "pending":
        updated.append(bet)
        continue

    result = check_result(bet["matchup"], bet["date"], bet["side"])
    bet["result"] = result
    updated.append(bet)

write_bets_csv("data/tracked_bets.csv", updated)
print("Evaluation complete.")