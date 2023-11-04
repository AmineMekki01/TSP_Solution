import numpy as np
import time
from collections import deque


def generate_initial_solution(dist_matrix):
    n = len(dist_matrix)
    solution = [0]
    unvisited = set(range(1, n))
    while unvisited:
        last = solution[-1]
        next_city = min(unvisited, key=lambda city: dist_matrix[last][city])
        unvisited.remove(next_city)
        solution.append(next_city)
    return solution


def calculate_cost(solution, dist_matrix):
    return sum(dist_matrix[solution[i - 1]][solution[i]] for i in range(1, len(solution))) + \
        dist_matrix[solution[0]][solution[-1]]


def generate_neighbor(solution, i, k):
    neighbor = solution[:]
    neighbor[i:k] = reversed(neighbor[i:k])
    return neighbor


def incremental_cost_change(solution, new_solution, dist_matrix, base_cost):
    start, end = None, None
    for i in range(1, len(solution)):
        if solution[i - 1:i + 1] != new_solution[i - 1:i + 1]:
            start = i - 1
            break
    for i in range(len(solution) - 1, 0, -1):
        if solution[i - 1:i + 1] != new_solution[i - 1:i + 1]:
            end = i + 1
            break
    if start is None or end is None:
        return base_cost

    cost = base_cost - dist_matrix[solution[start]][solution[start + 1]]
    cost -= dist_matrix[solution[end - 1]][solution[end % len(solution)]]
    cost += dist_matrix[new_solution[start]][new_solution[start + 1]]
    cost += dist_matrix[new_solution[end - 1]
                        ][new_solution[end % len(new_solution)]]
    return cost


def tabu_search(dist_matrix, instance_name, time_limit, rand_seed, solution_path):
    np.random.seed(rand_seed)
    start_time = time.time()
    best_solution = generate_initial_solution(dist_matrix)
    best_cost = calculate_cost(best_solution, dist_matrix)
    tabu_list = deque(maxlen=5)
    solution_path = f"{solution_path}/{instance_name}_TS_{time_limit}_{rand_seed}"

    while time.time() - start_time < time_limit:
        current_cost = best_cost
        best_neighbor = None
        best_neighbor_cost = float('inf')

        for i in range(1, len(best_solution) - 2):
            for k in range(i + 1, len(best_solution)):
                if time.time() - start_time >= time_limit:

                    break
                if k - i == 1:
                    continue
                neighbor = generate_neighbor(best_solution, i, k)
                move = (best_solution[i], best_solution[k - 1])

                neighbor_cost = incremental_cost_change(
                    best_solution, neighbor, dist_matrix, current_cost)
                if move not in tabu_list or neighbor_cost < best_cost:
                    if neighbor_cost < best_neighbor_cost:
                        best_neighbor = neighbor
                        best_neighbor_cost = neighbor_cost

                        print(best_neighbor_cost)

                        with open(solution_path+"_all_solutions.txt", 'a') as f:
                            f.write(f"Best Distance: {best_cost}\n")

                        with open(solution_path+".txt", 'w') as f:
                            f.write(f"Best Distance: {best_cost}\n")
                            f.write("Best Path: " +
                                    ' -> '.join(map(str, best_solution)) + '\n\n')

            if time.time() - start_time >= time_limit:

                break

        if best_neighbor:
            best_solution = best_neighbor
            best_cost = best_neighbor_cost
            tabu_list.append(move)

    final_time = time.time()
    execution_time = final_time - start_time

    return best_solution, best_cost, execution_time
