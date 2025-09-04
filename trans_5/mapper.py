#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("TransID") or line.startswith("CustId"):
        continue

    fields = line.split(",")

    # Transaction file (9+ fields)
    if len(fields) >= 9:
        cust_id = fields[2].strip()
        amount = fields[3].strip()
        game_type = fields[4].strip()
        print(f"{cust_id}\tTXN|{game_type}|{amount}")

    # Player file (5 fields)
    elif len(fields) >= 5:
        cust_id = fields[0].strip()
        first_name = fields[1].strip()
        print(f"{cust_id}\tPLAYER|{first_name}")
