#!/usr/bin/python3
def count_nucleotide(dna, nucleotide):
    return dna.count(nucleotide)

dna = input("Введите код днк ", )
nuc = input("Введите количество каких нуклеотидов необходимо посчитать ", )
print(count_nucleotide(dna, nuc))
