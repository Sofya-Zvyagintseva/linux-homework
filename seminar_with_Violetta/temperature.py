#!/usr/bin/env python3
import sys

c = float(sys.argv[1])
f = c * 9 / 5 + 32
k = c + 273.15

print(f"{f:.1f}°F, {k:.2f} K")
