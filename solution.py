import sys
from src.algorithms.greedy import heuristic
from src.algorithms.SA import simulated_annealing
from src.algorithms.brute_force import brute_force
from src.utils.helpers import prepare_data
import os

def main(method):
    if len(sys.argv) != 4:
        print("Usage: python script.py <instance_file> <cutoff> <rand_seed>")
        sys.exit(1)
    
    instance_file, cutoff_time, rand_seed = sys.argv[1:4]
    cutoff_time, rand_seed = float(cutoff_time), int(rand_seed)
    print(os.getcwd())
    dist_matrix, num_locs = prepare_data("instances/" + instance_file)
    
    if method == "heuristic":
        result = heuristic(rand_seed, dist_matrix, num_locs, cutoff_time)   
        print(result) 
        print(f"Best distance: {result[0]}")
        print(f"Best path: {result[1:-1]}")
    
    elif method == "SA":
        result = simulated_annealing(rand_seed, dist_matrix, cutoff_time)
     
    elif method == "brute_force":
        result = brute_force(dist_matrix)
      
        
    instance_name = instance_file.split('.')[0]
    solution_file = f"solutions/{instance_name}_{method}_{cutoff_time}_{rand_seed}.sol"
    trace_file = f"solutions/{instance_name}_{method}_{cutoff_time}_{rand_seed}.trace"
    path_only_file = f"solutions/{instance_name}_{method}_{cutoff_time}_{rand_seed}_path_only.txt"
    
    with open(solution_file, 'w') as handle:
        handle.write(f"{result[0]}\n")
        handle.writelines(f"{a} {b} {c}\n" for a, b, c in result[1:-1])
    
    with open(trace_file, 'w') as handle:
        handle.write(f"{result[-1]}, {result[0]}")
        
    with open(path_only_file, 'w') as handle:
        handle.write(" ".join(str(a) for a, _, _ in result[1:-1]))

    
if __name__ == '__main__':
    # main("heuristic")
    main("SA")
    # main("brute_force")
    

