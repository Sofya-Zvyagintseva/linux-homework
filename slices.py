#!/usr/bin/env python3
import sys

s = sys.argv[1]

print(f"Длина: {len(s)}")
print(f"Первый: {s[0]}")
print(f"Последний: {s[-1]}")
print(f"Средний: {s[len(s)//2]}")
print(f"Каждый второй: {s[::2]}")
print(f"Наоборот: {s[::-1]}")
print(f"Палиндром: {s == s[::-1]}")
