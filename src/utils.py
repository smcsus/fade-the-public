import csv
from typing import List, Dict

def read_bets_csv(path: str) -> List[Dict]:
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def write_bets_csv(path: str, rows: List[Dict]):
    if not rows:
        return
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)