# TSP_Solution
Solution of the traveling salesman problem using many algorithms.

## Group : VIRTUOSOS
- Amine MEKKi
- Ahmed SIDKI 
- Kaiyuan GONG

## Best solution : Greedy algorithm
python solution.py Pb5.txt greedy 60 42 

## 1.Problem Statement
The traveling salesman problem (TSP) is a well-known problem in computer science. It is an NP-hard problem in combinatorial optimization studied in operations research and theoretical computer science. Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city? It is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science.

## 2.Solution
The solution is implemented in python. 
The solution has many algorithms:
- Greedy algorithm
- Simulated Annealing algorithm
- Brute Force algorithm : This algorithm is not efficient for large number of cities. We can use it for small number of cities <= 10.
- Dynamic Programming algorithm : This algorithm is not efficient for large number of cities. We can use it for small number of cities <= 15. And It give the results faster than Brute Force algorithm.
- Genetic algorithm
- Ant Colony algorithm  
- Tabu Search algorithm

## 3.Project Structure
The project is structured as follows:
- `instances` folder contains the instances files in txt.
- `solutions` folder contains the results of the algorithms.
- `src` folder contains the source code of the project.
  - `src/algorithms` contains the implementations of the different algorithms.
  - `src/utils/helpers.py` contains the helper functions. 
- `solution.py` contains the main script to run the solution.


## 4.The used algorithms

### 4.1 Greedy algorithm

#### 4.1.1 Introduction 
The algorithm used in the solution is a type of greedy algorithm that builds up a tour by repeatedly selecting the shortest edge (or arc) that leads to an unvisited vertex. This is also known as the "nearest neighbor" heuristic.

#### 4.1.2 Step-by-step implementation 

- The greedy_tsp function takes several arguments including a random seed, a distance matrix representing the distances between all pairs of locations, the number of locations, a cutoff time to limit the algorithm's run time, and file handling parameters for output.

- The algorithm initializes an output file based on the parameters provided and ensures that the diagonal of the distance matrix is filled with infinity (since we cannot have 0 distance loops).

- It then initializes variables to track the best (shortest) total distance and the best path found so far.

- The algorithm enters a while loop that will continue to execute until the cutoff time is reached.

- Inside the loop, the algorithm chooses a random starting point and initializes the current path with this starting point. All other points are marked as unvisited.

- It then enters another loop where it continuously adds the nearest unvisited neighbor to the current path and updates the total distance.

- Once all vertices are visited, it adds the distance back to the starting point to complete the loop.

- If the total distance of the current path is less than the best distance found so far, it updates the best distance and best path.

- It writes all solutions to a file for every improvement and saves the best solution to another file.

- The algorithm may change the random seed and restart the process if time permits, searching for better solutions.

- Finally, the function returns a list containing the best total distance found, the best path, and the total time spent.


#### 4.1.3 Why It Is Used to Solve the TSP
The greedy algorithm is used for the TSP because it is simple to implement and understand, and it often produces a path that is good enough for many practical purposes.

#### 4.1.4 Advantages

- Speed: The greedy algorithm is very fast, especially compared to more exhaustive solutions like dynamic programming or brute force, which have factorial time complexities.
- Simplicity: The implementation and the idea behind it are straightforward.
- Effectiveness: For certain types of distance matrices (like those that approximate distances in the Euclidean plane), the greedy algorithm can yield very good results.
- Scalability: It can handle larger instances of the TSP reasonably well where other exact algorithms cannot.

#### 4.1.6 Disadvantages

- Suboptimality: The biggest drawback of the greedy algorithm is that it does not always find the optimal solution. It can get "trapped" by local optima.
- Dependency on Start Point: The resulting path can heavily depend on the initial starting point, which is random in this implementation.
- Lack of Guarantee: There is no guarantee about how close to the optimal solution the algorithm will get.


#### 4.1.7 Optimizations Done

The code shows an attempt at optimization by iterating over the process with different starting points (modifying the random seed). This could increase the chances of finding a better path by exploring different parts of the solution space, although it still doesn't guarantee finding the optimal path.

#### 4.1 8 Adding local search algorithms (2-opt, 3-opt) i will add it later
An improvement not shown but commonly used could involve implementing more sophisticated local search algorithms (like 2-opt or 3-opt) after the initial greedy solution to improve the path found.


### 4.2 Simulated Annealing algorithm

#### 4.2.1 Introduction
Simulated Annealing (SA) is a probabilistic technique used for approximating the global optimum of a given function. Specifically, it is a metaheuristic to approximate global optimization in a large search space. It is often used when the search space is discrete (e.g., all possible orders in which to visit a set of cities). For problems like the TSP, which are known to be NP-hard, SA helps in finding an acceptable solution in a more reasonable timeframe compared to exhaustive search, which is often computationally infeasible.

#### 4.2.2 Step-by-step implementation
The SA algorithm can be conceptualized as an analogy to the process of annealing in metallurgy. Here is a step-by-step description of the SA algorithm applied to the TSP, referring to the code you've used:

I- nitial Setup: Choose an initial tour at random (in your case using np.random.permutation) and set an initial temperature T high enough. Also, define a minimum temperature T_min and a cooling rate alpha.
- Main Loop: While the elapsed time is less than a predefined time limit:
- City Swap: Randomly select two cities and swap their positions in the current tour (as performed by swap_cities), creating a potential new tour.
- Distance Calculation: Calculate the total distance of the new tour (total_distance).
- Acceptance Criteria: Decide whether to accept the new tour based on whether the new distance is shorter or by probabilistic acceptance of worse solutions (to escape local minima) controlled by the temperature T.
-Cooling Schedule: Reduce the temperature T by a factor of alpha (typically, alpha is set just below 1).
Recording: If a new best tour is found, it is recorded to a file, tracking the best solution found so far.

- Cooling Down: The loop continues, gradually cooling the system until the time limit is reached.

#### 4.2.3 Why It Is Used to Solve the TSP
SA is used to solve the TSP due to its ability to escape local optima, a common issue with many optimization algorithms. TSP has a large number of potential solutions that increase factorially with the number of cities. SA allows for an extensive search of the solution space by probabilistically accepting worse solutions, thereby avoiding the trap of local optima and providing a means to explore the solution space more effectively.

#### 4.2.4 Advantages   
- Flexibility: SA is versatile and can be applied to any problem where an objective function can be formulated.
- Simplicity: The algorithm is conceptually simple and easy to implement.
- Escaping Local Optima: It probabilistically accepts worse solutions, allowing it to potentially escape local minima.
- No Gradient Information Required: Unlike gradient-descent-based methods, it does not require gradient information, which makes it suitable for a wide range of problems.
#### 4.2.5 Disadvantages    
- Computationally Intensive: It can be slow, particularly as the size of the problem grows.
- Parameter Sensitivity: The performance of SA is highly dependent on the cooling schedule and other parameters which require careful tuning.
- No Guarantee of Optimal Solution: SA does not guarantee that the optimal solution will be found.
-Randomness: The stochastic nature of the algorithm means that different runs may yield different results.

#### 4.2.6 Optimizations Done   
In the context of the code provided, the optimizations include the implementation of an efficient way to evaluate the impact of a swap operation on the tour's length, and the use of a cooling schedule to gradually reduce the temperature with also adaptive cooling.

### 4.3 Brute Force algorithm

#### 4.3.1 Introduction

#### 4.3.2 Step-by-step implementation

#### 4.3.3 Why It Is Used to Solve the TSP

#### 4.3.4 Advantages   

#### 4.3.5 Disadvantages    

#### 4.3.6 Optimizations Done   

### 4.4 Dynamic Programming algorithm

#### 4.4.1 Introduction
The brute force algorithm, as applied to the Traveling Salesman Problem (TSP), is the most straightforward approach to find the shortest possible route that visits each city exactly once and returns to the origin city. The concept behind this algorithm is to enumerate all possible permutations of the cities and calculate the total distance for each permutation to identify the one with the smallest total distance.
#### 4.4.2 Step-by-step implementation
The implementation provided can be broken down into several key steps:

- Distance Calculation:

distance(city1, city2, dist_matrix): A function to calculate the distance between two cities, city1 and city2, using a distance matrix, dist_matrix.

- Total Distance Computation:

total_distance(route, dist_matrix): Computes the total distance of a given route by summing up the distances between consecutive cities and adding the distance from the last city back to the first.

- Brute Force Search:

brute_force(dist_matrix): Executes the brute force search. It first initializes variables to store the best route and distance found. It then iterates over all possible city permutations using itertools.permutations and checks each one's total distance.
If a new permutation has a shorter distance than the previously recorded best, it updates the best distance and route.
The function finally returns the best route, its distances, and the time taken to compute it.

### 4.5 Genetic algorithm

#### 4.5.1 Introduction
The genetic algorithm (GA) is an optimization heuristic that draws inspiration from the process of natural selection. This algorithm reflects the process of natural evolution, where the fittest individuals are selected for reproduction to produce offspring of the next generation. In the context of the Traveling Salesman Problem (TSP), a genetic algorithm searches for the most efficient route that connects all cities without visiting any one of them more than once.

#### 4.5.2 Step-by-step implementation
The genetic algorithm for the TSP can be implemented in the following steps:

- Initialization:
Generate an initial population of possible solutions (routes). Each individual in the population represents a possible solution to the TSP.

- Fitness Function:
Evaluate each individual's fitness by calculating the total distance of the tour represented by the individual. The shorter the distance, the higher the fitness.

- Selection:
Select individuals for reproduction. A common method used here is a tournament selection, where a number of individuals are chosen randomly, and the best among them is selected.

- Crossover:
Combine parts of two selected individuals to produce a new offspring. The crossover operation ensures that a portion of the parent's path is preserved, which may hold the sequence of beneficial cities' arrangement.

- Mutation:
Introduce variations by randomly swapping cities in an individual's tour. This step maintains genetic diversity within the population and potentially leads to new solutions.

- Evolution:
Replace the old population with the new one that has been generated through selection, crossover, and mutation.

- Iteration:
Repeat the selection, crossover, and mutation processes for several generations or until a stopping criterion (such as a time limit) is reached.

- Solution Extraction:
The best individual in the last generation is considered as the best solution found by the algorithm.
#### 4.5.3 Why It Is Used to Solve the TSP
GAs are used for the TSP because they are good at searching large, complex, and multimodal landscapes, which is often the case with TSP. They can provide good approximations for the global optimum in a relatively short amount of time, especially when the search space is too large for exact methods (like the brute force approach) to be feasible.

#### 4.5.4 Advantages   
- Robustness: GA can handle a variety of optimization problems with little modification needed for the underlying model.
- Flexibility: It can adapt to changes in the problem's parameters or constraints without needing a significant redesign.
- Parallelism: GA naturally allows for parallel computation, as multiple individuals (solutions) can be evaluated simultaneously.
- Global Perspective: They work with a population of solutions and hence, have a better chance of avoiding local optima compared to algorithms that incrementally improve a single solution.
- 
#### 4.5.5 Disadvantages    
- Convergence: There is no guarantee of convergence to the global optimum. The solution may also converge prematurely to a local optimum.
- Parameter Setting: GA requires careful tuning of parameters like population size, mutation rate, and crossover rate, which can significantly affect performance.
- Computationally Intensive: Evaluating fitness can be computationally expensive, particularly if the population size is large or if the number of generations is high.
#### 4.5.6 Optimizations Done   
In the provided implementation, optimizations could include:

- Tournament Selection: To ensure a good balance between exploration and exploitation.
Preservation of Elite Individuals: To make sure that the best solutions are carried over to the next generation without modification.
- Mutation Rate Control: Adjusting the mutation rate during the evolution process to balance the exploration of the search space with the exploitation of the best solutions found.
- Time-limit-based Stopping Condition: This allows the algorithm to run as best as it can within a practical time constraint.
- Crossover Implementation: Ensures a mix of both parents' paths, preserving good paths that may have evolved.

### 4.6 Ant Colony algorithm

#### 4.6.1 Introduction
The Ant Colony Optimization (ACO) algorithm is a probabilistic technique for solving computational problems which can be reduced to finding good paths through graphs. Conceptualized by Marco Dorigo in his PhD thesis in 1992, the algorithm simulates the behavior of ants in finding paths from the colony to food. In the context of the Traveling Salesman Problem (TSP), ACO is used to find a tour that minimizes the total distance traveled.

#### 4.6.2 Step-by-step implementation
ACO can be implemented for TSP as follows:

- Initialization:
Create and initialize pheromone levels on the edges between cities. The pheromone matrix is typically initialized with a small constant value to allow exploration.

- Solution Construction:
Ants are placed on starting cities (either randomly or fixed) and construct solutions by moving to the next city according to a probabilistic transition rule that depends on pheromone levels and the distance to the next city.

- Transition Rule:

The probability of moving from city i to city j depends on the amount of pheromone on the edge (i,j) and the visibility (1/distance(i,j)).

- Update Pheromones:
Once all ants have completed their tours, update the pheromone levels on the edges. Pheromones evaporate on all edges, and new pheromones are deposited based on the quality of each ant's solution.

- Daemon Actions (Optional):
Apply additional operations such as local search or global update rules that can potentially enhance the search process.

- Repeat:
Repeat the process for a number of iterations or until a stopping condition is met.

- Solution Output:
The best solution found after all iterations is output as the problem's solution.

#### 4.6.3 Why It Is Used to Solve the TSP
ACO is particularly suited to the TSP because:

- It is a constructive metaheuristic that excels at finding good solutions incrementally.
- Ants are simple agents that in isolation have simple behavior but collectively can solve complex problems through indirect communication via pheromone trails.
- It naturally exploits good solutions by reinforcing the paths used in such solutions, thus converging over time to shorter and shorter tours.

#### 4.6.4 Advantages   
- Positive Feedback: Good solutions are quickly reinforced, leading to better solutions in subsequent iterations.
- Distributed Computation: The algorithm is inherently parallel, allowing for efficient implementation on distributed systems.
- Flexibility: ACO can be adapted to address additional constraints or changes in the problem structure without major conceptual changes.
- Robustness: ACO is less likely to get stuck in local optima due to exploration driven by pheromone evaporation.

#### 4.6.5 Disadvantages    
- Parameter Sensitivity: ACO requires careful tuning of its parameters (such as the number of ants, evaporation rate, and initial pheromone levels) to achieve good performance.
- Computationally Intensive: The algorithm can be computationally demanding, especially for larger instances of TSP.
- Convergence Speed: ACO can be slower to converge to the optimal or near-optimal solutions compared to other optimization methods.

#### 4.6.6 Optimizations Done   
In the provided implementation, optimizations could include:

- Evaporation Rate Adjustment: To prevent the convergence to a local optimum and to encourage exploration of new paths.
- Dynamic Pheromone Update Strategy: Adjusting the amount of pheromone laid based on the length of the tour or using a rank-based pheromone update.
- Time-Limited Execution: Implementing a real-time limit to ensure the algorithm provides a solution within a practical time frame.
- Daemon Actions: Such as a global update where only the best ant or a certain number of the best ants are allowed to deposit pheromones.

### 4.7 Tabu Search algorithm

#### 4.7.1 Introduction
The Tabu Search algorithm, a metaheuristic optimization method developed by Fred Glover in 1986, is designed to guide a local heuristic search procedure to explore the solution space beyond local optimality. This is accomplished by using memory structures that describe the visited solutions or user-defined moves. By allowing non-improving moves to escape local optima and prohibiting certain moves (making them "tabu") to prevent cycling back to previously visited solutions, Tabu Search enhances the performance of local search algorithms.



#### 4.7.2 Step-by-step implementation
The implementation of Tabu Search for the Traveling Salesman Problem (TSP) includes several key components:

- Initial Solution Generation: An initial solution is obtained, typically by a greedy heuristic such as the nearest neighbor algorithm. This provides a starting point for the search.

- Cost Calculation: The total cost or distance of a TSP tour is calculated. This serves as the objective function to minimize.

- Neighbor Generation: A neighborhood of solutions is produced using a method such as the 2-opt swap, which iteratively reverses segments of the tour to yield new potential solutions.

- Tabu Conditions: Certain moves are classified as tabu to prevent the algorithm from revisiting recent solutions, thus enforcing exploration.

- Tabu List Management: The tabu list is dynamically updated, adding new moves and expiring old ones based on a predefined tabu tenure.

- Search Process: The algorithm explores neighbors, comparing their costs and selecting the best non-tabu move. The search continues, updating the best known solution until a stopping criterion, such as a time limit, is reached.

- Result Output: The best solution found within the time frame is outputted, along with its cost. Intermediate solutions may also be recorded for analysis.

#### 4.7.3 Why It Is Used to Solve the TSP
Tabu Search is particularly suitable for solving the TSP due to its capability to escape local optima—a common challenge with TSP landscapes. The TSP requires exploring a vast number of permutations, and traditional methods like exhaustive search are computationally infeasible for large instances. Tabu Search's intelligent exploration of the search space can provide high-quality solutions within a reasonable amount of time.

#### 4.7.4 Advantages   
- Escape from Local Optima: Tabu Search can escape local optima by allowing non-improving moves.
- Flexible Memory Usage: It uses memory-based strategies which can be tuned for diverse problem instances.
- Good for Large Problems: It often performs well on large, complex problems where other methods fail to provide good solutions.
- Integrative Framework: It can be integrated with other heuristics to enhance their performance.

#### 4.7.5 Disadvantages    
- Parameter Sensitivity: The performance is highly dependent on the correct setting of parameters like tabu tenure.
- No Guarantee of Optimality: There's no assurance that Tabu Search will find the global optimum.
- Complexity: Implementing a tabu search can be more complex compared to simple heuristics.
- Stochastic Nature: The random elements can make the algorithm's behavior less predictable.

#### 4.7.6 Optimizations Done   
In the provided implementation, several optimizations are applied:

- Initial Solution Quality: Using the nearest neighbor heuristic ensures a reasonably good starting point, which is critical for the overall search quality.
- Efficient Neighbor Generation: The 2-opt approach for neighbor generation is efficient and effective in exploring the solution space.
- Dynamic Tabu Tenure: Adjusting the tabu tenure can help to balance between exploration and exploitation.
- Result Recording: Intermediate results are recorded, enabling the analysis of the search progress and providing insights into the search dynamics.
- Stopping Criterion: A time-based stopping criterion ensures the algorithm terminates in a practical amount of time, making it suitable for real-world applications.

maybe i will add it later

## 5. results

|    Algorithms | Pb0.txt with 10 cities    |  Pb1.txt with  100 cities    | Pb2.txt with   200 cities  |  Pb3.txt with  400 cities   |  Pb4.txt with 800 cities    |  Pb5.txt with  1000 cities  |
|    :---:  |    :---: |    :---: |    :---: |    :---: |    :---: |:---: |
|    Brute Force |    784.6654472573633 (10.22 s)   |    NaN   |    NaN |    NaN   |    NaN   |
|    Dynamic Programming |    784.6654472573634 (0.0065)   |    NaN   |    NaN |    NaN   |    NaN   |
|    Simulated Annealing (For 60 seconds) |    784.6654472573636   |    464.178085177807   |    791.9270639813909 |  4194.464799325995  |    24266.88550750139   |    42904.13889077514   |
|    Ant Colony (For 60 seconds) |    784.6654472573634   |    595.4409673851723   |    1176.2720769153627 | 11562.601899018644  |    68046.72970647867   |    121786.97962025172   |
|    Genetic algorithm  (For 60 seconds)|    784.6654472573634   |    932.935827344496   |  2465.989238437759  |    17430.7913502942 |    99750.00710570102   |    167715.98925446678   |
|    Greedy (For 60 seconds) |    818.912011072169   |    313.19471677756997   |    433.4932644935255 |  1939.9457999976025   |   6651.264894812741   |    10203.117488662452   |
|    Tabu Search (For 60 seconds) |    784.6654472573634   |    284.61602142365183   |    404.4892241554489   |   1981.6527706160684   |    6893.1532301336265   | 10988.374653856785 |

## 6. The best solution to test with large number of cities

The best solution to test with large number of cities is the greedy algorithm. It gives the best results in 60 seconds.

## 7. How to run the solution ?

### 7.1 Requirements
install the requirements file using the following command:
pip install -r requirements.txt

### 7.2 Run the solution
use the following command in the terminal in the root directory where the main is to run the solution:

python solution.py <file_name> <algorithm_type> <time_limit> <seed>

- file_name : is the name of the file in the instances folder with the extension.
- algorithm_type = greedy or SA or brute_force ...
- seed : if you don't specify it, the algorithm will use a default seed which is 42. 
- time_limit : is optional, if you don't specify it, the algorithm will use a default time limit which is 60 seconds.
  
### 7.3 Example
python solution.py Pb1.txt greedy 60 42

