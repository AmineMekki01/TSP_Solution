import itertools
from time import time
"""

i will use multi threading to speed up the brute force algorithm
"""


def distance(city1, city2, dist_matrix):
    return dist_matrix[city1, city2]


def total_distance(route, dist_matrix):
    return sum(distance(route[i], route[i+1], dist_matrix) for i in range(len(route) - 1)) + distance(route[-1], route[0], dist_matrix)


def brute_force(dist_matrix):
    num_cities = dist_matrix.shape[0]
    best_route = None
    best_distance = float('inf')
    start_time = time()

    for route in itertools.permutations(range(num_cities)):
        route_distance = total_distance(route, dist_matrix)
        if route_distance < best_distance:
            best_distance = route_distance
            best_route = route

    result = [int(best_distance)]
    for i in range(len(best_route) - 1):
        result.append((best_route[i], best_route[i + 1],
                      int(distance(best_route[i], best_route[i + 1], dist_matrix))))
    result.append((best_route[-1], best_route[0],
                  int(distance(best_route[-1], best_route[0], dist_matrix))))
    elapsed_time = round(time() - start_time, 2)
    result.append(elapsed_time)
    print(result)
    return result
