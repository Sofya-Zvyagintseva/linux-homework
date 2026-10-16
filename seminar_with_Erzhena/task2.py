#!/usr/bin/env python3
reference = input().strip()
sample = input().strip()

for i, ref_char in enumerate(reference, start=1):
    samp_char = sample[i - 1]
    if ref_char != samp_char:
        print(f"{i}: {ref_char} > {samp_char}")
