import sys
from src.algorithms.greedy import greedy_tsp
from src.algorithms.SA import simulated_annealing
from src.algorithms.brute_force import brute_force
from src.utils.helpers import prepare_data
from src.algorithms.DP import TspDynamicProgrammingRecursive
from src.algorithms.ant_colony import ant_colony_optimization
from src.algorithms.GA import TravelingSalesmanGA


def parse_arguments():
    if len(sys.argv) != 5:
        print(
            "Usage: python script.py <instance_file> <algorithm_type> <cutoff> <rand_seed>")
        sys.exit(1)

    return sys.argv[1:5]


def choose_algorithm(algorithm_type, instance_name, rand_seed, dist_matrix, num_locs, cutoff_time):

    if algorithm_type == "greedy":
        solution_path = "solutions/greedy/"
        return greedy_tsp(rand_seed, dist_matrix, num_locs, cutoff_time, solution_path, instance_name), solution_path

    elif algorithm_type == "SA":
        solution_path = "solutions/SA/"
        result = simulated_annealing(
            dist_matrix, num_locs, cutoff_time, solution_path, instance_name, rand_seed)

        return result, "solutions/SA/"

    elif algorithm_type == "brute_force":
        return brute_force(dist_matrix), "solutions/brute_force/"

    elif algorithm_type == "DP":
        solution_path = "solutions/DP/"
        solver = TspDynamicProgrammingRecursive(
            dist_matrix, instance_name, cutoff_time, rand_seed, solution_path)
        return solver.get_metrics()

    elif algorithm_type == "ACO":
        solution_path = "solutions/ACO/"
        return ant_colony_optimization(dist_matrix, instance_name, cutoff_time, rand_seed, solution_path), solution_path

    elif algorithm_type == "GA":
        solution_path = "solutions/GeneticAlgorithm/"
        solver = TravelingSalesmanGA(
            dist_matrix, instance_name, cutoff_time, rand_seed, solution_path)
        return solver.run(time_limit=cutoff_time), solution_path

    else:
        print("Invalid algorithm type")
        sys.exit(1)


def main():

    instance_file, algorithm_type, cutoff_time, rand_seed = parse_arguments()
    cutoff_time, rand_seed = float(cutoff_time), int(rand_seed)
    instance_name = instance_file.split('.')[0]

    dist_matrix, num_locs = prepare_data("instances/" + instance_file)

    result, solution_path = choose_algorithm(
        algorithm_type, instance_file, rand_seed, dist_matrix, num_locs, cutoff_time)

    print("SA result  : ", result)


if __name__ == '__main__':
    main()
