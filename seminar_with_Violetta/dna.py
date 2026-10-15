#!/usr/bin/env python3
import sys

dna = sys.argv[1]

# Обратно-комплементарная цепь
trans_table = str.maketrans('ATCG', 'TAGC')
complement = dna.translate(trans_table)[::-1]

# РНК (T -> U)
rna = dna.replace('T', 'U')

# Позиция старт-кодона ATG (нумерация с 1)
start_pos = dna.find('ATG') + 1

print(f"{complement}, {rna}, {start_pos}")
