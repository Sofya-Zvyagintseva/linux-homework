#!/usr/bin/env python3
growth = [
    [0, 2, 4, 8],
    [0, 1, 1, 2],
    [0, 3, 6, 9]
]
for culture in growth:
    found = False
    for i, val in enumerate(culture):
        if val >= 5:
            print(i)
            found = True
            break
    if not found:
        print("отсутствует")
