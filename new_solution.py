import random
import sys
import pandas as pd
import numpy as np
from time import time
from scipy.spatial.distance import squareform, pdist
import matplotlib.pyplot as plt
from itertools import permutations
import math

def set_diag_to_inf(matrix):
    np.fill_diagonal(matrix.values, np.inf)


def prepare_data(file_path):

    df = pd.read_csv(f"instances/{file_path}", sep=' ', names=['X', 'Y'], skiprows=1, skipfooter=1, engine='python')
    df.index += 1  
    
    dist_matrix = pd.DataFrame(
        squareform(pdist(df)), 
        columns=df.index,
        index=df.index
    )
    
    set_diag_to_inf(dist_matrix)
    return dist_matrix, len(df)


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



def read_path_from_file(file_path):
    with open(file_path, 'r') as f:
        nodes = list(map(int, f.read().strip().split()))
    return nodes

def plot_graph(df, nodes):
    plt.scatter(df['X'], df['Y'], c='blue')

    for idx, row in df.iterrows():
        plt.text(row['X'], row['Y'], str(idx))

    for i in range(len(nodes) - 1):
        point1 = df.loc[nodes[i]]
        point2 = df.loc[nodes[i + 1]]
        plt.plot([point1['X'], point2['X']], [point1['Y'], point2['Y']], 'k-')

    point1 = df.loc[nodes[-1]]
    point2 = df.loc[nodes[0]]
    plt.plot([point1['X'], point2['X']], [point1['Y'], point2['Y']], 'k-')

    plt.show()
    
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
   
def main(method):
    if len(sys.argv) != 4:
        print("Usage: python script.py <instance_file> <cutoff> <rand_seed>")
        sys.exit(1)
    
    instance_file, cutoff_time, rand_seed = sys.argv[1:4]
    cutoff_time, rand_seed = float(cutoff_time), int(rand_seed)
    
    dist_matrix, num_locs = prepare_data(instance_file)
    if method == "heuristic":
        result = heuristic(rand_seed, dist_matrix, num_locs, cutoff_time)    
    elif method == "SA":
        best_distance, best_path = simulated_annealing(dist_matrix, num_locs, 10000, 0.095)
        print(f"Best distance: {best_distance}")
        print(f"Best path: {best_path}")
        
    instance_name = instance_file.split('.')[0]
    solution_file = f"solutions/{instance_name}_{method}_{cutoff_time}_{rand_seed}.sol"
    trace_file = f"solutions/{instance_name}_{method}_{cutoff_time}_{rand_seed}.trace"
    path_only_file = f"solutions/{instance_name}_{method}_{cutoff_time}_{rand_seed}_path_only.txt"
    
    with open(solution_file, 'w') as handle:
        handle.write(f"{result[0]}\n")
        handle.writelines(f"{a} {b} {c}\n" for a, b, c in result[1:-1])
    
    with open(trace_file, 'w') as handle:
        handle.write(f"{result[-1]:.2f}, {result[0]}")
        
    with open(path_only_file, 'w') as handle:
        handle.write(" ".join(str(a) for a, _, _ in result[1:-1]))

    
if __name__ == '__main__':
    main("heuristic")
    main("SA")
    


