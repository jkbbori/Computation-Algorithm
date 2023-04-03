# The Euler cycler

data = {1: 2, 2: [4, 3], 3: 4, 4: [1, 5], 5: [6, 7], 6: 7, 7: [5, 2]}

def eulet_cycle(grap):
    path = []
    beggining = 0
    beg_nod = list(grap.keys())[beggining]
    beg_nod_values = list(grap.values())[beggining]
    path.append(beg_nod)
    for elem in list(grap.keys()):
        current_node = 0
        next_node = list(grap.keys())[current_node]
        next_node_values = list(grap.values())[current_node]
        if next_node_values in grap.keys():
            path.append(next_node_values)
            current_node += 1

    return path







print(eulet_cycle(data))





