#!/usr/bin/env python3
import sys
from collections import defaultdict

cust_to_name = {}  # CustID -> FirstName
game_summary = defaultdict(lambda: {"players": set(), "amount": 0.0, "ids": []})

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    cust_id, value = line.split("\t", 1)
    parts = value.split("|")

    if parts[0] == "PLAYER":
        first_name = parts[1]
        cust_to_name[cust_id] = first_name

    elif parts[0] == "TXN":
        game_type = parts[1]
        try:
            amount = float(parts[2])
        except ValueError:
            continue
        game_summary[game_type]["amount"] += amount
        game_summary[game_type]["ids"].append(cust_id)

# Resolve names
for game_type, data in game_summary.items():
    players = set()
    for cid in data["ids"]:
        name = cust_to_name.get(cid, cid)  # fallback: use ID if no name
        players.add(name)
    players_list = "[" + ",".join(sorted(players)) + "]"
    print(f"{game_type}\t{players_list}\t{data['amount']:.2f}")
