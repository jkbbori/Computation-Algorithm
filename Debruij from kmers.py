import requests

genome = ['GAGG',
'CAGG',
'GGGG',
'GGGA',
'CAGG',
'AGGG',
'GGAG']


def String_Composition_Problem(k: int, genome: list):
    k_mers = set()
    for i in genome:
        for elem in range(len(i) - k + 1):
            k_mer = i[elem:elem + k]
            k_mers.add(k_mer)
    return k_mers

#k_mer = (String_Composition_Problem(3, genome))



def overlap_grap(kmers, genome):
    asj_lst = {kmer: [] for kmer in kmers}
    for kmer1 in kmers:
        for kmer2 in genome:
            if kmer1 == kmer2[:-1]:
                asj_lst[kmer1].append(kmer2[1:])
    return asj_lst

#print(overlap_grap(k_mer, genome))

class Graph(dict):
    def __init__(self, dct):
        super().__init__(dct)

    def __str__(self):
        return '\n'.join(['{} -> {}'.format(node, ','.join(edges)) for node, edges in self.items()])

    @classmethod
    def form_kmers(cls, kmers):
        asj_lst = {kmer: [] for kmer in kmers}
        for kmer1 in kmers:
            for kmer2 in kmers:
                if kmer1[1:] == kmer2[:-1] and kmer1 != kmer2:
                    asj_lst[kmer1].append(kmer2)
        return cls(asj_lst)

    @property
    def num_nodes(self):
        return len(self)

def debruij_from_kmer(kmer):
    k = len(kmer[0]) - 1
    comp = String_Composition_Problem(k, kmer)
    p = overlap_grap(comp, kmer)
    return p

response = requests.get(
    'http://gerdos.web.elte.hu/edu/bioinformatics_algorithms/data/week4/DeBruijnFromKmers/dataset_200_8.txt')
rep = response.text.splitlines()

print(Graph(debruij_from_kmer(rep)))


