#!/usr/bin/env python3
import sys

# Input format:
# TransID, Date, CustID, Amount, Game Type, Equipment, City, State, Mode
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("TransID"):  # skip header
        continue

    fields = line.split(",")
    if len(fields) < 9:
        continue

    try:
        amount = float(fields[3])
        game_type = fields[4].strip()
        print(f"{game_type}\t{amount}")
    except ValueError:
        # skip bad records
        continue
