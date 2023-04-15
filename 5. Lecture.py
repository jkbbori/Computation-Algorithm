# The Euler cycler
import numpy as np

data ={1: [2], 2: [3, 4], 3: [4], 4: [1, 5], 5: [6, 7], 6: [7], 7: [2, 5]}

@classmethod
def from_file(cls, file_location):
    adj_list = {}
    with open (file_location, 'r') as file_handler:
        for line in file_handler:
            key = line.split('->')[0].strip()
            value = line.split('->')[-1].strip().split(',')
            adj_list[key] = value
    return cls(adj_list)


def eulet_cycle(orig_grap):
    grap = orig_grap.copy()
    path = []
    beggining = 0
    beg_nod = list(grap.keys())[beggining]
    path.append(beg_nod)
    current_node = beggining
    while True:
        next_node = list(grap.keys())[current_node]
        next_node_values = list(grap.values())[current_node]
        next_node_values_min = sorted(next_node_values)
        if next_node_values_min == []:
            if len(np.array(path)) == len(grap.keys()):
                return path
            else:
                path = []
                grap = orig_grap.copy()
                beggining = beggining + 1
                current_node = beggining
                beg_nod = list(grap.keys())[beggining]
                path.append(beg_nod)
        elif next_node_values_min[0] in grap.keys():
            path.append(next_node_values_min[0])
            current_node = next_node_values_min[0] - 1
            next_node_values_min = next_node_values_min[1:]
            grap[next_node] = next_node_values_min
            print(path)

    return path





print(eulet_cycle(data))





