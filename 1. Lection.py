import requests


def fasta_reader(fasta_as_string):
    global header
    fasta = {}
    for line in fasta_as_string.splitlines():
        if line.startswith('>'):
            header = line.strip()
            fasta[header] = ''
        elif line.strip():
            fasta[header] += line.strip()
    return fasta


def skew(seq: str) -> list:
    positional_skew = [0]
    point = 0
    for num in seq:
        if num == 'C':
            point -= 1
        elif num == 'G':
            point += 1
        positional_skew.append(point)
    min_pos, min_value = [], float('inf')
    for ind, val in enumerate(positional_skew):
        if val < min_value:
            min_value = val
            min_pos = [ind]
        elif val == min_value:
            min_pos.append(ind)
    return min_pos

url = "https://gerdos.web.elte.hu/edu/bioinformatics_algorithms/data/week1/ecoli.fasta"
response = requests.get(url)

sequence: str
#for header, sequence in fasta_reader(response.text).items():
#    plt.plot(skew(sequence))
#    plt.show()

positional_skwe = skew(sequence)
#min_skew = min(positional_skwe)
#print(positional_skwe.index(min_skew))

# These two are the same
# This code is really inefficient because it takes too much time

#print([n for n, i in enumerate(positional_skwe) if i == min_skew])

#pos = []
#for idx, value in enumerate(positional_skwe):
#    if value == min_skew:
#        pos.append(idx)
#print(pos)

skew(url)