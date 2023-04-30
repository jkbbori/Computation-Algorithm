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


data = from_file(r'C:\Users\Bori\Desktop\Test1.txt')
center = from_file(r'C:\Users\Bori\Desktop\Test.txt')


def squared_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance


def Squared_Error_Distortion(k, m, centers, data):
    total_distance = 0
    for elem in data:
        min_distance = float('inf')
        for center in centers:
            distance = squared_distance(elem, center)
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance
    return total_distance / len(data)


print(Squared_Error_Distortion(6, 4, center, data))
