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
    position = len(kmer[0]) - 1
    branching = []
    in_and_out_edge = []
    for _, km in enumerate(kmer):  # ATG
        prefix = km[0:position]  # AT
        in_in = 0
        out = 0
        for _, kmr in enumerate(kmer):
            prefix_all = kmr[0:position]  # AT
            suffix_all = kmr[len(kmr) - position:len(kmr)]  # TG
            if prefix == prefix_all:
                in_in += 1
            if prefix == suffix_all:
                out += 1
        if in_in == 1 and out == 1:  # if it is 1 it will have 1 branch, if it is bigger it will have more branch
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
        print(km, end=' ')


print(Contig(r"C:\Users\Bori\Desktop\test.txt"))
