def read_file(path_of_file):
    in_file = open(path_of_file)
    kmer = []
    for elem in in_file:
        data = elem.strip(' \t\n\r')
        if len(data) == 0:
            break
        else:
            kmer.append(data)
    return kmer


def Contig(k_mer):
    kmer = read_file(k_mer)
    print(kmer)
    position = len(kmer[0]) - 1
    branching = []
    in_and_out_edge = []
    for _, km in enumerate(kmer):  # ATG
        prefix = km[0:position]  # AT
        in_in = 0  # 2
        out = 0  # 2
        for _, kmr in enumerate(kmer):  # ATG
            prefix_all = kmr[0:position]  # AT
            suffix_all = kmr[len(kmr) - position:len(kmr)]  # TG
            if prefix == prefix_all:
                in_in += 1
            if prefix == suffix_all:
                out += 1
        if in_in == 1 and out == 1:
            in_and_out_edge.append(km)
        else:
            branching.append(km)

    i = 0
    while len(in_and_out_edge) > 0:
        elem = in_and_out_edge[i]
        elem_prefix = elem[0:position]
        for x in branching:
            if elem_prefix in x:
                branching.append(x + elem[position:len(elem)])
                branching.remove(x)
                in_and_out_edge.remove(elem)
                i = -1
                break
        i += 1

    contig = []
    for _, km in enumerate(sorted(branching)):
        contig.append(km)

    return contig

print(Contig(r"C:\Users\Bori\Desktop\test.txt"))
