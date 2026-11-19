# Задание 1 и 2
def read_fasta(filename):
    records = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                records.append({"metadata": line[1:], "data": ""})
            else:
                records[-1]["data"] += line
    return records

cds = read_fasta("cds.fna")
gene = read_fasta("gene.fna")

# Задание 3
def gc_content(seq):
    gc = 0
    for letter in seq:
        if letter == "G" or letter == "C":
            gc += 1
    return (gc / len(seq)) * 100 if len(seq) > 0 else 0

for rec in cds:
    print(gc_content(rec["data"]))

# Задание 4
def find_motif(seq, motif):
    coords = []
    i = 0
    while True:
        i = seq.find(motif, i)
        if i == -1:
            break
        coords.append(i)
        i += 1
    return len(coords), coords

print(find_motif(cds[0]["data"], "ATG"))
