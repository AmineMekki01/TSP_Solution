from time import time
import random
import numpy as np


def greedy_tsp(rand_seed, dist_matrix, num_locs, cutoff, output_file, instance_name):

    output_file = f"{output_file}/{instance_name}_greedy_{cutoff}_{rand_seed}"

    np.fill_diagonal(dist_matrix, np.inf)

    best_total_distance = np.inf
    best_path = []

    start_time = time()
    end_time = start_time + cutoff

    while time() < end_time:
        if rand_seed is not None:
            random.seed(rand_seed)

        start = random.randrange(num_locs)
        current_path = [start]
        unvisited = set(range(num_locs)) - {start}
        total_distance = 0
        temp = start

        while unvisited:
            nearest = min(unvisited, key=lambda x: dist_matrix[temp, x])
            total_distance += dist_matrix[temp, nearest]
            current_path.append(nearest)
            unvisited.remove(nearest)
            temp = nearest

        total_distance += dist_matrix[temp, start]
        current_path.append(start)

        if total_distance < best_total_distance:
            best_total_distance = total_distance
            best_path = current_path
            print(best_total_distance)

            with open(output_file+"all_solutions.txt", 'a') as f:
                f.write(f"Best Distance: {best_total_distance}\n")

            with open(output_file+".txt", 'w') as f:
                f.write(f"Best Distance: {best_total_distance}\n")
                f.write("Best Path: " + ' -> '.join(map(str, best_path)) + '\n\n')

        rand_seed = (rand_seed + 1) if rand_seed is not None else None

    time_spent = round(time() - start_time, 2)
    return [int(best_total_distance)] + best_path + [time_spent]
