#!/usr/bin/env python3
import sys
from collections import defaultdict

# CustID -> Age
cust_to_age = {}

# GameType -> list of ages
game_summary = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    cust_id, value = line.split("\t", 1)
    parts = value.split("|")

    if parts[0] == "PLAYER":
        # PLAYER|FirstName|Age
        age = None
        try:
            age = int(parts[2])
        except ValueError:
            continue
        cust_to_age[cust_id] = age

    elif parts[0] == "TXN":
        # TXN|GameType|Amount
        game_type = parts[1]
        if cust_id in cust_to_age:
            game_summary[game_type].append(cust_to_age[cust_id])
        else:
            # save for later join (if PLAYER comes after TXN)
            game_summary[game_type].append(cust_id)

# Now finalize: convert any cust_id placeholders into real ages
for game_type, ages in game_summary.items():
    resolved_ages = []
    for a in ages:
        if isinstance(a, int):
            resolved_ages.append(a)
        elif a in cust_to_age:
            resolved_ages.append(cust_to_age[a])
    if not resolved_ages:
        continue
    min_age = min(resolved_ages)
    max_age = max(resolved_ages)
    avg_age = sum(resolved_ages) / len(resolved_ages)
    print(f"{game_type}\t[Min: {min_age}, Max: {max_age}, Avg: {avg_age:.2f}]")
