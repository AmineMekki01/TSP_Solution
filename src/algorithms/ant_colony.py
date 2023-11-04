import numpy as np
from time import time


def select_next_city(current, visited, pheromones, dist_matrix):
    n = len(dist_matrix)
    probabilities = []
    unvisited = [i for i in range(n) if i not in visited]

    total = 0
    for next_city in unvisited:
        total += pheromones[current][next_city] / \
            dist_matrix[current][next_city]

    probabilities = [(pheromones[current][next_city] / dist_matrix[current]
                      [next_city]) / total for next_city in unvisited]

    selected_next_city = np.random.choice(unvisited, 1, p=probabilities)[0]
    return selected_next_city


def ant_colony_optimization(dist_matrix, instance_name, time_limit, rand_seed, solution_path, num_ants=10, evaporation_rate=0.1, num_iterations=100):

    solution_path = f"{solution_path}/{instance_name}_ACO_{time_limit}_{rand_seed}"

    n = len(dist_matrix)
    pheromones = np.ones((n, n))
    best_cost = float('inf')
    best_path = []

    start_time = time()
    end_time = start_time + time_limit

    while time() < end_time:
        for iteration in range(num_iterations):
            if time() >= end_time:
                break
            for _ in range(num_ants):
                if time() >= end_time:
                    break
                current = 0
                visited = set([current])
                path = [current]
                cost = 0

                for _ in range(n - 1):
                    next_city = select_next_city(
                        current, visited, pheromones, dist_matrix)
                    visited.add(next_city)
                    path.append(next_city)
                    cost += dist_matrix[current][next_city]
                    pheromones[current][next_city] *= (1 - evaporation_rate)
                    pheromones[current][next_city] += (1 /
                                                       dist_matrix[current][next_city])
                    current = next_city

                cost += dist_matrix[current][0]
                path.append(0)

                if cost < best_cost:
                    best_cost = cost
                    best_path = path

                    with open(solution_path+"all_solutions.txt", 'a') as f:
                        f.write(f"Best Distance: {best_cost}\n")

                    with open(solution_path+".txt", 'w') as f:
                        f.write(f"Best Distance: {best_cost}\n")
                        f.write("Best Path: " +
                                ' -> '.join(map(str, best_path)) + '\n\n')
    return best_cost, best_path
