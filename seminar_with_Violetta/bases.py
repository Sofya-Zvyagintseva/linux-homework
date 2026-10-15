#!/usr/bin/env python3
import sys

s = sys.argv[1]
base = int(sys.argv[2])

num = int(s, base)

print(f"2-я: {bin(num)}")
print(f"8-я: {oct(num)}")
print(f"16-я: {hex(num)}")
