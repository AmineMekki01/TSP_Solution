import time
import random
import numpy as np
import math


def total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i - 1], tour[i]] for i in range(len(tour)))


def swap_cities(tour, i, j):
    new_tour = tour[:]
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour


def simulated_annealing(dist_matrix, num_cities, time_limit, solution_path, instance_name, rand_seed):

    solution_path = f"{solution_path}/{instance_name}_SA_{time_limit}_{rand_seed}"

    current_tour = list(np.random.permutation(num_cities))
    current_distance = total_distance(current_tour, dist_matrix)
    best_tour = current_tour[:]
    best_distance = current_distance
    T = 1.0
    T_min = 0.00001
    alpha = 0.99
    start_time = time.time()

    while time.time() - start_time < time_limit:
        i, j = np.random.randint(0, num_cities, size=2)
        new_tour = swap_cities(current_tour, i, j)
        new_distance = total_distance(new_tour, dist_matrix)
        delta_distance = new_distance - current_distance

        if delta_distance < 0 or np.random.rand() < np.exp(-delta_distance / T):
            current_tour = new_tour
            current_distance = new_distance

            if new_distance < best_distance:
                best_tour = new_tour
                best_distance = new_distance

                with open(solution_path+"all_solutions.txt", 'a') as f:
                    f.write(f"Best Distance: {best_distance}\n")

                with open(solution_path+".txt", 'w') as f:
                    f.write(f"Best Distance: {best_distance}\n")
                    f.write("Best Path: " +
                            ' -> '.join(map(str, best_tour)) + '\n\n')

        T *= alpha

    return best_tour, best_distance
