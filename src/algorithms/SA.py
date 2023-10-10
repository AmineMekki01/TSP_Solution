import random
import numpy as np
from time import time 
def simulated_annealing(rand_seed, dist_matrix, cutoff):
    num_locs = dist_matrix.shape[0]
    unvisited = set(range(num_locs))
    total_distance = 0
    path = []
    start_time = time()
    
    random.seed(rand_seed)
    start = random.randrange(num_locs)
    temp = start

    while unvisited and (time() - start_time < cutoff):
        unvisited.remove(temp)
        row = dist_matrix[temp, :]
        
        min_index = -1
        min_value = np.inf
        for idx in unvisited:
            if row[idx] < min_value:
                min_value = row[idx]
                min_index = idx

        if min_index != -1:
            path.append([temp, min_index, int(min_value)])
            total_distance += min_value
            temp = min_index
        else:
            back_distance = dist_matrix[temp, start]
            total_distance += back_distance
            path.append([temp, start, int(back_distance)])
            elapsed_time = round(time() - start_time, 2)
            return [int(total_distance)] + path + [elapsed_time]

    return [int(total_distance)] + path + [round(time() - start_time, 2)]



def path_distance(path, dist_matrix):
    distance = 0
    for i in range(len(path) - 1):
        distance += dist_matrix[path[i] - 1, path[i + 1] - 1]
    distance += dist_matrix[path[-1] - 1, path[0] - 1]
    return distance