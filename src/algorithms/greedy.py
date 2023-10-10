from time import time
import random
import numpy as np

def heuristic(rand_seed, dist_matrix, num_locs, cutoff):

    unvisited = set(range(1, num_locs + 1))  
    total_distance = 0
    path = []
    start_time = time()
    
    random.seed(rand_seed)
    start = random.randrange(1, num_locs + 1)
    temp = start
    
    while unvisited and (time() - start_time < cutoff):
        unvisited.remove(temp)
        row = dist_matrix.loc[temp]
        sort_index = [i + 1 for i in np.argsort(row)]
        
        min_index = next((i for i in sort_index if i in unvisited), None)
        if min_index is not None:
            dist = dist_matrix.at[temp, min_index]
            path.append([temp, min_index, int(dist)])
            temp = min_index
            total_distance += dist
        else:
            back_distance = dist_matrix.at[temp, start]
            total_distance += back_distance
            path.append([temp, start, int(back_distance)])
            return [int(total_distance)] + path + [round(time() - start_time, 2)]

