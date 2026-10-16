#!/usr/bin/env python3
lengths = []
while True:
    s = input().strip()
    if s == "STOP":
        break
    is_valid = True
    for char in s:
        if char not in "ATGC":
            is_valid = False
            break
    if is_valid:
        lengths.append(len(s))
    else:
        print("Предупреждение: неверный символ в последовательности")
print(len(lengths))
print(lengths)
