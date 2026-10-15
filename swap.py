#!/usr/bin/env python3
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print(f"До: a = {a}, b = {b}")
print(f"id(a) = {id(a)}, id(b) = {id(b)}")

# Способ 1: через временную переменную
temp = a
a = b
b = temp

print(f"Способ 1: a = {a}, b = {b}")
print(f"id(a) = {id(a)}, id(b) = {id(b)}")

# Способ 2: через кортеж
a, b = b, a

print(f"Способ 2: a = {a}, b = {b}")
print(f"id(a) = {id(a)}, id(b) = {id(b)}")
