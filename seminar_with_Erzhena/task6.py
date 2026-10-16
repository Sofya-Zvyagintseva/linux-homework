#!/usr/bin/env python3
sequences = [
    "AACG",
    "AATG",
    "TATG",
    "TTTG"
]
for i in range(len(sequences)):
    row = []
    for j in range(len(sequences)):
        dist = 0
        for k in range(len(sequences[i])):
            if sequences[i][k] != sequences[j][k]:
                dist += 1
        row.append(str(dist))
    print(" ".join(row))
