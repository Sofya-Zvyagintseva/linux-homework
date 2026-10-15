#!/usr/bin/env python3
import sys

num_str = sys.argv[1]
n = int(num_str)

sum_slice = int(num_str[0]) + int(num_str[1]) + int(num_str[2])
rev_slice = int(num_str[::-1])

print(f"{sum_slice}, {rev_slice}")
