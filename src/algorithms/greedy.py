from time import time
import random
import numpy as np

def heuristic(rand_seed, dist_matrix, num_locs, cutoff):
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
            return [int(total_distance)] + path + [round(time() - start_time, 2)]

