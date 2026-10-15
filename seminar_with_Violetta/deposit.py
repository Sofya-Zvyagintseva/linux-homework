#!/usr/bin/env python3
import sys

amount = float(sys.argv[1])
rate = float(sys.argv[2])
years = int(sys.argv[3])

final_amount = amount * (1 + rate / 100) ** years

print(f"{final_amount:.2f}")
