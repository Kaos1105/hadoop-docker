import sys

current_game = None
total_amount = 0.0
players = []    # unique IDs

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    game_type, value = line.split("\t", 1)
    try:
        cust_id, amount = value.split(",", 1)
        amount = float(amount)
    except ValueError:
        continue

    if current_game == game_type:
        players.append(cust_id)
        total_amount += amount
    else:
        if current_game is not None:
            players_list = "[" + ",".join(players) + "]"
            print(f"{current_game}\t{players_list}\t{total_amount:.2f}")
        current_game = game_type
        players = [cust_id]
        total_amount = amount

# flush last group
if current_game is not None:
    players_list = "[" + ",".join(players) + "]"
    print(f"{current_game}\t{players_list}\t{total_amount:.2f}")