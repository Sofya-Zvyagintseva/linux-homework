#!/usr/bin/env python3
rna = input().strip()
stop_codons = ["UAA", "UAG", "UGA"]
count = 0
stop_codon = ""
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    if len(codon) < 3:
        break
    if codon in stop_codons:
        stop_codon = codon
        break
    count += 1
print(f"Количество кодирующих кодонов: {count}")
print(f"Стоп-кодон: {stop_codon}")
