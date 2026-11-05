#!/usr/bin/python3
def is_valid_dna(dna):
    if len(dna) == 0:
        return False
    for letter in dna:
        if letter != "A" and letter != "T" and letter != "G" and letter != "C":
            return False
    return True

def hamming_distance(s1, s2):
    if is_valid_dna(s1) == False or is_valid_dna(s2) == False:
        return None
    if len(s1) != len(s2):
        return None
        
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count = count + 1
    return count

s1 = input("Введите первую последовательность ДНК: ")
s2 = input("Введите вторую последовательность ДНК: ")

result = hamming_distance(s1, s2)
