class Graph(dict):
    def __init__(self, dct):
        self.graph = dct
        super().__init__(dct)

    def __str__(self):
        return '\n'.join(['{} -> {}'.format(node, ','.join(edges)) for node, edges in self.items()])

    @classmethod
    def read_kmers_from_file(cls, file_location):
        kmer_list = []
        with open(file_location, 'r') as file_handler:
            for line in file_handler:
                kmer_list.append(line.strip())
        k_1mer_keys = []
        for kmer in kmer_list:
            k_1mer_keys.append(kmer[:-1])
        adj_list = {read: [] for read in k_1mer_keys}
        for read1 in set(k_1mer_keys):
            for read2 in kmer_list:
                if read1 == read2[:-1]:
                    adj_list[read1].append(read2[1:])
        return cls(adj_list)

    @classmethod
    def from_file(cls, file_location):
        adj_list = {}
        with open(file_location, 'r') as file_handler:
            for line in file_handler:
                key = line.split('->')[0].strip()
                value = line.split('->')[-1].strip().split(',')
                adj_list[key] = value
        return cls(adj_list)

    @property
    def num_nodes(self):
        return len(self)

    def Euler_Path(adj_list):
        graph = adj_list.graph
        path = []
        start_pos = 0
        start_nod = list(graph.keys())[start_pos]
        path.append(start_nod)

        for node in graph:
            if len(graph[node]) > len([elem for elem in graph if node in graph[elem]]):  # find starting node
                beg_node = node
        for node in graph:
            if len(graph[node]) < len([elem for elem in graph if node in graph[elem]]):  # find last node
                end_node = node
                graph[end_node].append(beg_node)  # add an edge going from 'end_node' to 'start'
        if 'end_node' not in locals():
            end_node = list(set([val for sublist in graph.values() for val in sublist]) - set(graph.keys()))[
                0]  # find key of last node
            graph[end_node] = [beg_node]

        while any(graph.values()):
            if graph[path[-1]] != []:
                path.append(graph[path[-1]][0])
                graph[path[-2]] = graph[path[-2]][1:]
            else:
                for i in range(len(path)):
                    if graph[path[i]] != []:
                        path = path[i:] + path[1:i] + [path[i]]
                        break

        end_of_path = path.index(end_node)
        move_on_path = end_of_path + 1
        while path[end_of_path] != end_node or path[move_on_path] != beg_node:
            end_of_path = move_on_path
            move_on_path += 1
        path = path[move_on_path:] + path[1:end_of_path + 1]

        cycle=''.join([path[0]]+[kmer[-1] for kmer in path[1:]])

        return cycle


adj_list = Graph.from_file(r'C:\Users\Bori\Desktop\test1.txt')


def to_adj_list(graph):
    adj_list = {}
    key = []
    value = []
    for elem in graph.keys():
        key.append(elem)
    for elem in graph.values():
        value.append(elem)
    for elem in key:
        for val in value:
            adj_list[int(elem)] = list(map(int, val))
            value.remove(val)
            break
    return adj_list


def eulerian_cycle(adjust_list):
    path = []
    graph = to_adj_list(adjust_list)
    start_pos = 0
    start = list(graph.keys())[start_pos]
    nodes = [start]

    while len(nodes) > 0:
        node = nodes[-1]
        if graph[node]:
            negh = graph[node].pop(0)
            nodes.append(negh)
        else:
            node_to_path = nodes.pop()
            path.insert(0, node_to_path)
        print(path)

    for node in graph.keys():
        if graph[node]:
            return None

    cycle = '->'.join(str(x) for x in path)

    return cycle


def Euler_Cycle(adj_list):
    graph = adj_list.graph
    path = []
    start_pos = 0
    start_nod = list(graph.keys())[start_pos]
    path.append(start_nod)

    while any(graph.values()):
        if graph[path[-1]] != []:
            path.append(graph[path[-1]][0])
            graph[path[-2]] = graph[path[-2]][1:]
        else:
            for i in range(len(path)):
                if graph[path[i]] != []:
                    path = path[i:] + path[1:i] + [path[i]]
                    break
    cycle = '->'.join(str(x) for x in path)

    return cycle


def Euler_Path(adj_list):
    graph = adj_list.graph
    path = []
    start_pos = 0
    start_nod = list(graph.keys())[start_pos]
    path.append(start_nod)

    for node in graph:
        if len(graph[node]) > len([elem for elem in graph if node in graph[elem]]):  # find starting node
            beg_node = node
    for node in graph:
        if len(graph[node]) < len([elem for elem in graph if node in graph[elem]]):  # find last node
            end_node = node
            graph[end_node].append(beg_node)  # add an edge going from 'end_node' to 'start'
    if 'end_node' not in locals():
        end_node = list(set([val for sublist in graph.values() for val in sublist]) - set(graph.keys()))[
            0]  # find key of last node
        graph[end_node] = [beg_node]

    while any(graph.values()):
        if graph[path[-1]] != []:
            path.append(graph[path[-1]][0])
            graph[path[-2]] = graph[path[-2]][1:]
        else:
            for i in range(len(path)):
                if graph[path[i]] != []:
                    path = path[i:] + path[1:i] + [path[i]]
                    break

    end_of_path = path.index(end_node)
    move_on_path = end_of_path + 1
    while path[end_of_path] != end_node or path[move_on_path] != beg_node:
        end_of_path = move_on_path
        move_on_path += 1
    path = path[move_on_path:] + path[1:end_of_path + 1]

    cycle = '->'.join(str(x) for x in path)

    return cycle


#print(Euler_Path(adj_list))

import requests

rep = requests.get(
    'http://gerdos.web.elte.hu/edu/bioinformatics_algorithms/data/week4/GenomeAssembly/dataset_203_7.txt')
rep = rep.text.splitlines()
rep = rep[1:]


def overlap_grap(kmers):
    asj_lst = {kmer: [] for kmer in kmers}
    for kmer1 in kmers:
        for kmer2 in kmers:
            if kmer1[1:] == kmer2[:-1]:
                asj_lst[kmer1].append(kmer2)
    return asj_lst


overlap = Graph.read_kmers_from_file(r'C:\Users\Bori\Desktop\assembly.txt')
print(overlap.Euler_Path())


