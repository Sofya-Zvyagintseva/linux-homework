# --- Задание 1: Подсчет нуклеотидов ДНК ---
dna = input().strip()
print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))

# --- Задание 2: Транскрипция ДНК в РНК ---
dna = input().strip()
rna = dna.replace('T', 'U')
print(rna)

# --- Задание 3: Обратный комплемент ДНК ---
dna = input().strip()
trans_table = str.maketrans('ATCG', 'TAGC')
complement = dna.translate(trans_table)[::-1]
print(complement)

# --- Задание 4: Содержание GC ---
dna = input().strip()
gc_count = dna.count('G') + dna.count('C')
gc_percent = (gc_count / len(dna)) * 100
print(f"{gc_percent:.2f}%")

# --- Задание 5: Поиск мотива в последовательности ДНК ---
s = input().strip()
t = input().strip()
positions = []
start = 0
while True:
    pos = s.find(t, start)
    if pos == -1:
        break
    positions.append(str(pos + 1))
    start = pos + 1
print(" ".join(positions))
