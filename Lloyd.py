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


data = from_file(r'C:\Users\Bori\Desktop\Test.txt')

import math


def distance(p1, p2):
    # Compute the Euclidean distance between two points
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))


def assign_points_to_centers(data, centers):
    # Assign each point in data to the nearest center
    clusters = [[] for _ in range(len(centers))]
    for point in data:
        distances = [distance(point, center) for center in centers]
        min_distance = min(distances)
        index = distances.index(min_distance)
        clusters[index].append(point)
    return clusters


def compute_centers(clusters):
    # Compute the mean of each cluster and use it as the new center
    return [tuple(sum(x) / len(x) for x in zip(*cluster)) for cluster in clusters]


def k_means_clustering(data, k):
    # Select the first k points from data as the initial centers
    centers = data[:k]
    while True:
        # Assign each point in data to the nearest center
        clusters = assign_points_to_centers(data, centers)
        # Compute the mean of each cluster and use it as the new center
        new_centers = compute_centers(clusters)
        # Check if the centers have converged
        if new_centers == centers:
            break
        centers = new_centers
    return centers


print(k_means_clustering(data, 2))
