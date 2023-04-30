# Deburjan Graph for a pair of reads

# Sequence alignment

def change_problem(money, coins):
    min_num_point = [0]
    for m in range(1, money + 1):
        min_num_point.append(float('inf'))
        for coin in coins:
            if m - coin >= 0 and min_num_point[m - coin] + 1 < min_num_point[m]:
                min_num_point[m] = min_num_point[m - coin] + 1
    return min_num_point[-1]


# print(change_problem(1256745, [50,25,20,10,5,1]))


n = 4
m = 4
down = [[1, 0, 2, 4, 3],
        [4, 6, 5, 2, 1],
        [4, 4, 5, 2, 1],
        [5, 6, 8, 5, 3]]

right = [[3, 2, 4, 0],
         [3, 2, 4, 2],
         [0, 7, 3, 3],
         [3, 3, 0, 2],
         [1, 3, 2, 2]]


def Manhattan_Tourist_Problem(n, m, Down, Right):
    matrix = [[0 for x in range(m + 1)] for y in range(n + 1)]
    for i in range(1, n + 1):
        matrix[i][0] = matrix[i - 1][0] + Down[i - 1][0]
    for j in range(1, m + 1):
        matrix[0][j] = matrix[0][j - 1] + Right[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] = max(matrix[i - 1][j] + Down[i - 1][j], matrix[i][j - 1] + Right[i][j - 1])
    return matrix[n][m]


# print(Manhattan_Tourist_Problem(m, n, down, right))

def Manhattan_tourist(x, y, down, right):
    tour = [[0] * (y + 1) for _ in range(x + 1)]
    for i in range(y + 1):
        for j in range(y + 1):
            if j == 0 and i == 0:
                continue
            if i == 0:
                tour[i][j] = tour[i][j - 1] + right[i][j - 1]
            elif j == 0:
                tour[i][j] = tour[i - 1][j] + down[i - 1][j]
            else:
                tour[i][j] = max(tour[i][j - 1] + right[i][j - 1], tour[i - 1][j] + down[i - 1][j])

    return tour[x][y]


# print(Manhattan_tourist(m, n, down, right))


seq1 = 'AACCTTGG'
seq2 = 'ACACTGTGA'


def Lonegest_common_subsequence(seq1, seq2):
    aln_matrix = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                aln_matrix[i + 1][j + 1] = aln_matrix[i][j] + 1
            else:
                aln_matrix[i + 1][j + 1] = max(aln_matrix[i + 1][j], aln_matrix[i][j + 1])

    i, j = len(seq1), len(seq2)
    lonest_substring = ''
    while i or j:
        if aln_matrix[i][j] == aln_matrix[i - 1][j]:
            i -= 1
        elif aln_matrix[i][j] == aln_matrix[i][j - 1]:
            j -= 1
        else:
            lonest_substring = seq1[i - 1] + lonest_substring
            i -= 1
            j -= 1
    return lonest_substring


# print(Lonegest_common_subsequence('TTCGCCCGGAATATACTAAGCGTTGTAGGAGACTTCTGAAGTCCCATCGTAATGGGCGTCCCAACCCGGAAGATGGTCTATAAGCGCGCTCGTATGCGTCCCTGCACCGGCACGGTCTCGAATATATTTCATTCGTTAACGCGAGACACCAAGCGCATTCGTCTTTGTACGGACTGATGATGCAGCAAAGGGGAGACAGCGGCGACGACATCGATCTTACCTATAGTTTCACGTTCAGAATCGGGGGCACCTCTCAAACATCTGTAAGCCGGTGCTACAAAATGATCGTAGATTGTACGGTATCACTGCCTAGGTGAGCGCAGGTTGTTTACCCTTCTTTGCGCTTCACCCCAGAAGCTAGTGTTTCGTCGGTATGCATGGTAAAAGCATCGGGATGGTCGCAAAACCGACAAATTATTTACGAGAGACTAGACTCGCCTTCCACACCCTTCCTAGACCGAGTACCAGGATCAATGGGCGGAGTCAGGTCGCAGCGGCCATTTAAGCTGTACTAAGTGAATTTTGCAAAACCGATACCCATTTAAGTTGTACCTTACCCGCCACAGCTATGTTGAAGTTAGTTCGGGGCGCTTGCCCACCGATGTACCGCCTGTACAAGTATACGATCGGTTTCTCAAATTTGTGGAATGAACACACCGTCCCCGCGGGTCAGGCCTTTTTCACTTTTTTCGTGTTTAAGGCCAAATCATTGCCCAACGTCCCTTACTGTCCGCACAGCTGGTATCTCGTCTCATGTGCGGCGGCCTACATGCGATTCTACGTTCAGGTCCCGACAGGCCACCCGAGAGT', 'ACGTGGAATAACAACCCTGAGGCTCGGTCAGCGGAGTTAGGCAGGGACCATATGTATACATCGAAAGCATGGCTACGCGGGTACAGTTGTCGACACATCAAGCGAGTGAGTGGAGAATGTAAGAACACGTTTCTTCCGCAGGCAGTCTGGGCGACCTCTTGGATCATTGAGGATGAGACATGGATCATATGATGTTCAATAAAACGTTCAATCCAATCTGCTGCCCGGCCATCGCTTCTAACGGGGAGTCTTAAAACCGCCCCCCGGACGACCCATCTACCACCCTTCTAGAACGTAATTGGTGAAGGCGGTTATCAATCAAACGCCTAGGGTCAGCAAATATACATCGTCTTAGCGTCTCCCAACACGTTCAAGTCAAAAGTCGAGAGCGAGCAGAGACAGGTATGACTGCTTAAGTTTAAGGACGGATACGAACACTAAATTGGCTACTGTAAGGACGATCCGAGGTGTTTTTCCAAGTCCCCACCAGAATAACGAGGCTCGTACGTTCTGTGCGATGCGGTCGGGCCAAGAGTATTCCAGGGTGACGTGGTGACAGCATGCAGAGTGCCGTCCCTCTGGCGCCCTCATAATTGATCATGCCATACAATCAACAGTTCAAATGCAAAGATTCGTTCTTTGGGAGAGGCGGCATCCGAGGTAGTAATACGGGGAAGGAGTACATCCTGCGGCGTAGGCACGCCCTAGACTATCAGAATCCTATCCGGCAGGCACATCCGGACCAGCAAGCACTAAGTCGCCGTAGTACCAGGATTCGATAGTACGGTGTAGCAGCTCCCCTCCGGCCCACTAAAAGCTGTATAAACGTTAGTTCAGACCAGAGGTGTACGTTGAGTATGTTGACGTGGCACGAATTCGTGGCTTAAAGGCTTAGGGGTCGCCTCTGGGGTGGACCATACTCCCCGAACCCTCCCTTA'))


m = 1
u = -3
g = -1
a = 'ACG'
b = 'ACT'


def Highest_Score(m, u, g, seq1, seq2):
    aln_matrix = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                aln_matrix[i + 1][j + 1] = aln_matrix[i][j] + 1
            else:
                aln_matrix[i + 1][j + 1] = max(aln_matrix[i + 1][j], aln_matrix[i][j + 1])

    print(aln_matrix)

# print(Highest_Score(m, u, g, a, b))
