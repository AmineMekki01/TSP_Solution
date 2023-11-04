import numpy as np
import time
from itertools import permutations

# Set a random seed for reproducibility
np.random.seed(42)


class TravelingSalesmanGA:
    def __init__(self, dist_matrix, instance_name, time_limit, rand_seed, solution_path, population_size=100, mutation_rate=0.01, tournament_size=5):
        self.dist_matrix = dist_matrix
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.best_solution = None
        self.best_cost = float('inf')
        self.instance_name = instance_name
        self.time_limit = time_limit
        np.random.seed(rand_seed)
        self.rand_seed = rand_seed
        self.solution_path = solution_path

    def initial_population(self):
        population = []
        for _ in range(self.population_size):
            individual = np.random.permutation(len(self.dist_matrix))
            population.append(individual)
        return population

    def fitness(self, individual):
        return sum(self.dist_matrix[individual[i - 1], individual[i]] for i in range(len(individual)))

    def select(self, population):
        selected = []
        for _ in range(self.tournament_size):
            selected.append(population[np.random.randint(0, len(population))])
        selected.sort(key=self.fitness)
        return selected[0]

    def crossover(self, parent1, parent2):
        size = len(self.dist_matrix)
        child = [-1] * size
        start, end = sorted(np.random.choice(size, 2, replace=False))
        child[start:end] = parent1[start:end]
        child_pos = end
        for gene in parent2:
            if gene not in child:
                if child_pos >= size:
                    child_pos = 0
                child[child_pos] = gene
                child_pos += 1
        return child

    def mutate(self, individual):
        for swapped in range(len(individual)):
            if np.random.random() < self.mutation_rate:
                swap_with = int(np.random.random() * len(individual))
                individual[swapped], individual[swap_with] = individual[swap_with], individual[swapped]
        return individual

    def evolve(self, population):
        new_population = []
        for _ in range(len(population)):
            parent1 = self.select(population)
            parent2 = self.select(population)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            new_population.append(child)
        return new_population

    def run(self, time_limit=60):
        population = self.initial_population()
        start_time = time.time()

        while time.time() - start_time < time_limit:
            population = self.evolve(population)
            current_best = min(population, key=self.fitness)
            current_cost = self.fitness(current_best)
            if current_cost < self.best_cost:
                self.best_cost = current_cost
                self.best_solution = current_best
                print("Best cost:", self.best_cost)

                self.save_solution(self.instance_name,
                                   self.time_limit, self.rand_seed, self.solution_path)
        print("Best solution:", self.best_solution)
        return self.best_solution, self.best_cost

    def save_solution(self, instance_name, time_limit, rand_seed, solution_path):

        solution_path = f"{solution_path}/{instance_name}_DP_{time_limit}_{rand_seed}"
        with open(solution_path+"_all_solutions.txt", 'a') as f:
            f.write(f"Best Distance: {self.best_cost}\n")

        with open(solution_path+".txt", 'w') as f:
            f.write(f"Best Distance: {self.best_cost}\n")
            f.write("Best Path: " +
                    ' -> '.join(map(str, self.best_solution)) + '\n\n')
