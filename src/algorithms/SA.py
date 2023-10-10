import random
import math

def simulated_annealing(dist_matrix, num_locs, initial_temp, cooling_rate):
    current_path = list(range(1, num_locs + 1))  
    random.shuffle(current_path)
    current_distance = path_distance(current_path, dist_matrix)
    
    best_path = current_path[:]
    best_distance = current_distance
    
    temp = initial_temp
    
    while temp > 1:
        new_path = current_path[:]
        i, j = random.sample(range(num_locs), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        
        new_distance = path_distance(new_path, dist_matrix)
        
        if new_distance < current_distance or math.exp((current_distance - new_distance) / temp) > random.random():
            current_path = new_path
            current_distance = new_distance
            
            if new_distance < best_distance:
                best_path = new_path[:]
                best_distance = new_distance
                
        temp *= cooling_rate
    
    return best_distance, best_path

def path_distance(path, dist_matrix):
    distance = 0
    for i in range(len(path) - 1):
        distance += dist_matrix.at[path[i], path[i + 1]]
    distance += dist_matrix.at[path[-1], path[0]]
    return distance