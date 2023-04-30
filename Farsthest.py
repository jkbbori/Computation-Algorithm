data = [(0.0, 0.0)
    , (5.0, 5.0)
    , (0.0, 5.0)
    , (1.0, 1.0)
    , (2.0, 2.0)
    , (3.0, 3.0)
    , (1.0, 2.0)]


def from_file(file_location):
    data = []
    with open(file_location, 'r') as file_handler:
        for lines in file_handler:
            lines = lines.strip().split('\n')
            for line in lines:
                values = line.strip().split(' ')
                point = tuple(map(float, values))
                data.append(point)
    return data

my_data = from_file(r'C:\Users\Bori\Desktop\Test.txt')


def distance(p, q):
    return sum((pi - qi)**2 for pi, qi in zip(p, q))

def FarthestFirstTraversal(k, m, Data):
    Centers = [Data[0]]
    while len(Centers) < k:
        distances = [min(distance(x, c) for c in Centers) for x in Data]
        new_center = Data[distances.index(max(distances))]
        Centers.append(new_center)
    return Centers

print(FarthestFirstTraversal(4, 2, my_data))
