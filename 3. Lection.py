# A brute force algorithm
import random

dna_list = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']

# Implanted Motif Problem

def motif_search(dna_list: list, k: int, d: int) -> set:

    def hamming_dis(seq1, seq2):
        assert len(seq1) == len(seq2), 'Different length input'
        return sum([1 for idx, elem in enumerate(seq1) if elem != seq2[idx]])

    def approx_matching(genome: str, motif: str, d) -> list[int]:
        start_pos = []
        for inx, letter in enumerate(genome):
            if len(genome[inx:inx + (len(motif))]) != len(motif):
                continue
            if hamming_dis(genome[inx:inx + (len(motif))], motif) <= d:
                start_pos.append(inx)
        return start_pos

    def approx_patt_count(genome, motif, d):
        return len(approx_matching(genome, motif, d))

    motifs = set()

    for dna in dna_list:
        print(dna)
        for indx in range(len(dna) - k + 1):
            motif = dna[indx: indx + k]
            counter = 0
            for dna2 in dna_list:
                if approx_patt_count(dna2, motif, d) >= 1:
                    counter += 1
                if counter == len(dna_list):
                    motifs.add(motif)

    return motifs


# Homework

def Count(DNA):
    n = max([len(dna) for dna in dna_list])

    matrix = {base: {index: 0 for index in range(n)}
              for base in 'ACGT'}

    for dna in DNA:
        for idx, base in enumerate(dna):
            matrix[base][idx] += 1

    return matrix


def Consensus(motif):
    consensus = ''
    dna_length = len(motif['A'])
    for i in range(dna_length):
        max_freq = -1
        max_freq_base = None

        for base in 'ACGT':
            if motif[base][i] > max_freq:
                max_freq = motif[base][i]
                max_freq_base = base
            elif motif[base][i] == max_freq:
                max_freq_base = max_freq_base

        consensus += max_freq_base

    return consensus


# motif = Count(dna_list)
# consensus = Consensus(motif)
# print(consensus)

def hamming_distance(string1: str, string2: list):
    all_diff = []
    distance = 0
    for elem in string2:
        for nuc in range(len(elem)):
            if elem[nuc] != string1[nuc]:
                distance += 1
            all_diff.append(distance)
    return max(all_diff)


# print(hamming_distance(consensus, dna_list))

