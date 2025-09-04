#!/usr/bin/env python3
import sys

current_game = None
total_amount = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    game_type, amount = line.split("\t", 1)
    try:
        amount = float(amount)
    except ValueError:
        continue

    if current_game == game_type:
        total_amount += amount
    else:
        if current_game is not None:
            print(f"{current_game}\t{total_amount:.2f}")
        current_game = game_type
        total_amount = amount

# flush last one
if current_game is not None:
    print(f"{current_game}\t{total_amount:.2f}")
