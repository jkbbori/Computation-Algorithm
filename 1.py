a = ['tcgggggttttt',
     'ccggtgacttac',
     'acggggattttc',
     'ttggggactttt',
     'aaggggacttcc',
     'ttggggacttcc',
     'tcggggattcat',
     'tcggggattcct',
     'taggggaactac',
     'tcgggtataacc']


def profile_generator(alignment: list) -> dict:
    profile = {x: [0] * len(alignment[0]) for x in set(''.join(alignment))}
    for motif in alignment:
        for idx, nuc in enumerate(motif):
            profile[nuc][idx] += 1
    for nuc, scores in profile.items():
        for idx, scores in enumerate(scores):
            profile[nuc][idx] = scores / len(alignment)
    return profile


# print(profile_generator(a))

dna = 'GCCTCTACACTCGAAATTGCCTGTTCCATACTATACGCATATATCTCGAGTGTAACGAGTCTCCTCCTGTGGGGTAAGCGACAATTGGGATCCGAAGCCCGAACGGCTTCAGTCGGAAGATAGAACTTTGTCTCTATTGAGATGCACTTTCTCTCGTAAGCACGCTTAGTACGTGGTCCTTTGCCTCAGAGTCCAGGCCTCCAAACGTCGCAGGCTATTATTCGCATCTCGACGCGTGGGTGCAGACCGGGCTTATTACATGGTCCACAGCACGACCTGACGCGTAGCGTAGATTAGACATACGTATTTTGGCCATCGATTGCGGCTCTCGGCCAATTGGCGAGGACCACCGAGTCTGCAGTCTTAACTCCGATCCCCGATGCAATAAACGTTTCTAACACCTGCTACCGCCCCTGGTAAGTTATTGCGCCGGTTGCAACCTGTGTTCGTTTCAATGTAGACGGCTTACGTTGCCTGTGGAACCGACAGTTACGGTAATCGCAGGGGACGCCTAGGTCTCGTCCCTTACCCCGTGCCAACCGCGCGTGGGATACCATTACTAACCAGGCTGTGCACCTAAGCGTTCCAAGCCCTCTATGTGCGGTGATCGGAGTATTCGGACGTTTCTGCTCCCGCGCTATCTTGTCAACTCCTACGCAAAGAGATCTAAAATATCAGAATTCCTCATGATGAACGAGTTAAGGCCGGCATCACGGTAGCATTCTCTTAGAGCTGGCGACGACGTGCTCGGCTACTTCCAGGAAGTGGGAGGAGTACATATAACCGCCGTAGAAGTGCCTGCTGCTCAAACGGCTGGTGTAGCATGGTTACGCGGACCGTCTCAGTCCGTGGAGTGAGTTGCTGTTTGTCCCAGCTGTACCATGCCAGAATGCTGCCTTCCTGTCTGGGTTGTAGCAGGAAAAGACGCTCTGCAAGCCATAGATTCAGCCGGCGGCGATAGCCATCCATCCCGCGATCGAAGACAAGGTACCCCCATCTT'
k = 13
data = """0.237 0.263 0.197 0.237 0.184 0.316 0.25 0.263 0.211 0.171 0.276 0.25 0.237
0.25 0.184 0.211 0.237 0.25 0.211 0.289 0.25 0.316 0.197 0.276 0.25 0.224
0.263 0.211 0.276 0.342 0.355 0.263 0.197 0.303 0.263 0.342 0.211 0.224 0.211
0.25 0.342 0.316 0.184 0.211 0.211 0.263 0.184 0.211 0.289 0.237 0.276 0.329"""

profile = {nuc: list(map(float, data.splitlines()[idx].split())) for idx, nuc in enumerate(['A', 'C', 'G', 'T'])}


def score(motif, profile):
    motif_score = 1
    for idx2, nuc in enumerate(motif):
        motif_score *= profile[nuc][idx2]
    return motif_score


def profile_most_probable_kmer(dna: str, k: int, profile: dict) -> str:
    max_score = -float('inf')
    most_probable_kmer = ''
    for idx in range(len(dna) - k + 1):
        motif = dna[idx:idx + k]
        assert len(motif) == k
        motif_score = score(motif, profile)
        if motif_score > max_score:
            max_score = motif_score
            most_probable_kmer = motif
    return most_probable_kmer


# Median String

import itertools


def hamming_dis(seq1, seq2):
    assert len(seq1) == len(seq2), 'Different length input'
    return sum([1 for idx, elem in enumerate(seq1) if elem != seq2[idx]])


def min_hamming_distance(pattern, text):
    min_distance = float('inf')
    for idx in range(len(text) - len(pattern) + 1):
        distance = hamming_dis(pattern, text[idx:idx+len(pattern)])
        if distance < min_distance:
            min_distance = distance
    return min_distance


def median_string(dna_list, k):
    min_distance = float('inf')
    median = ''
    for motif in itertools.product(['A', "C", 'T', "G"], repeat=k):
        motif = ''.join(motif)
        distance_to_motif = 0
        for dna in dna_list:
            distance_to_motif += min_hamming_distance(motif, dna)
        if distance_to_motif < min_distance:
            min_distance = distance_to_motif
            median = motif
    return median


print(median_string(['ATATAAAGTGTCACCTTGCGACACTGAGAGAATGGAAAGCTT',
'GGGAAGCGATACTCGTGTTTCTCAAAGAACTCATGGAGCAGA',
'CGAAACCTCGACCTGGTGCTTCCGTGCCTCTCGATGACGTCT',
'GCAGGCGGAATCGGGACAGAGCTACGAAACAAACCGGAGGAC',
'TTCAGTATGTTGACGCGGTAGCGGGTCTCGTATAGTCGAAAC',
'CTTTTTTAAGGTTAATTGTCTTGCCGAGACTAGAATGAGAAT',
'GCACTTACGACACGACACTGAAAATCCCTTGTAAATTGCGTA',
'CTATCTCGACACCCGGCTACGAGGAAGTAGACTATTTAATTG',
'GCATAAATTGGTGAACAAGGAAAAGAGATTCGAGACATGGAA',
'GTAGGTCCGGTGCAATACCGAGACCCTATAGTATTGTTACCT'], 6))
