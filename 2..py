import requests


# Patter Count Algorithm

def pattern_count(text: str, pattern: str) -> int:
    count = 0
    for elem in range(len(text) - len(pattern)):
        if text[elem:elem + len(pattern)] == pattern:
            count = count + 1
    return count


# Patter Matching Problem

def pattern_matching_problem(pattern: str, genome: str) -> list[int]:
    start_pos = []
    for elem in range(len(genome) - len(pattern)):
        if genome[elem:elem + len(pattern)] == pattern:
            start_pos.append(elem)
    return start_pos


# Frequent Words Problem

def frequent_words(text, k):
    occ = 0
    for ind, _ in enumerate(text):
        word = text[ind:ind + k]
        if len(word) != k:
            continue
        cnt = pattern_count(text, word)
        if cnt > occ:
            occ = cnt
            words = {word: cnt}
        elif cnt == occ:
            words[word] = cnt
    return list(words.keys())


def frequent_words(text, k):
    counts = [pattern_count(text, text[x:x + k]) for x in range(len(text) - k)]
    return set([text[x:x + k] for x in range(len(text) - k) if counts[x] == max(counts)])


# Revers Complement Problem


def revers_complemet(sequenc: str) -> str:
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(sequenc))
    return reverse_complement


# Hamming Distance

def hamming_dis(seq1, seq2):
    assert len(seq1) == len(seq2), 'Different length input'
    return sum([1 for idx, elem in enumerate(seq1) if elem != seq2[idx]])


def approx_matching(text: str, pattern: str, d) -> list[int]:
    start_pos = []
    for inx, letter in enumerate(text):
        if len(text[inx:inx + (len(pattern))]) != len(pattern):
            continue
        if hamming_dis(text[inx:inx + (len(pattern))], pattern) <= d:
            start_pos.append(inx)
    return start_pos




import itertools

kmer = []

for elem in itertools.product(['A,', "C", 'T', "G"], repeat=4):
    kmers = ''.join(elem)
    kmer.append(kmers)

# print(itertools.product(['A,', "C", 'T', "G"], repeat=3))

# Brute force algorith

# for i in itertools.product(['A,', "C", 'T', "G"], repeat=5):
#    print(''.join(i))


# Homework cods
import itertools


# Frequent Words With Mismatches

def frequent_words_with_mismatch(text: str, k: int, d: int) -> list:
    possible_kmers = {}
    current = 0

    def hamming_dis(seq1, seq2):
        assert len(seq1) == len(seq2), 'Different length input'
        return sum([1 for idx, elem in enumerate(seq1) if elem != seq2[idx]])

    def approx_pattern_count(text: str, pattern: str, d) -> list[int]:
        position = 0
        for inx, letter in enumerate(text):
            if len(text[inx:inx + (len(pattern))]) != len(pattern):
                continue
            if hamming_dis(text[inx:inx + (len(pattern))], pattern) <= d:
                position = position + 1
        return position

    for elem in itertools.product(['A', "C", 'T', "G"], repeat=k):
        kmers = ''.join(elem)
        new = approx_pattern_count(text, kmers, d)
        if current < new:
            current = new
            possible_kmers = {kmers: new}
        elif current == new:
            possible_kmers[kmers] = new

    return list(possible_kmers.keys())


# Culimp finding Problem

def clump_finding(genome: str, k, L, t):
    out = []
    for nuc in range(len(genome) - L + 1):
        window = genome[nuc:nuc + L]
        counts = {}
        for i in range(len(window) - k + 1):
            if window[i:i + k] not in counts:
                counts[window[i:i + k]] = 0
            counts[window[i:i + k]] += 1
        for kmer in counts:
            if counts[kmer] >= t and kmer not in out:
                out.append(kmer)
    return out
