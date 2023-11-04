# TSP_Solution
Solution of the traveling salesman problem using many algorithms.

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

#### 4.2.2 Step-by-step implementation

#### 4.2.3 Why It Is Used to Solve the TSP

#### 4.2.4 Advantages   

#### 4.2.5 Disadvantages    

#### 4.2.6 Optimizations Done   


### 4.3 Brute Force algorithm

#### 4.3.1 Introduction

#### 4.3.2 Step-by-step implementation

#### 4.3.3 Why It Is Used to Solve the TSP

#### 4.3.4 Advantages   

#### 4.3.5 Disadvantages    

#### 4.3.6 Optimizations Done   

### 4.4 Dynamic Programming algorithm

#### 4.4.1 Introduction

#### 4.4.2 Step-by-step implementation

#### 4.4.3 Why It Is Used to Solve the TSP

#### 4.4.4 Advantages   

#### 4.4.5 Disadvantages    

#### 4.4.6 Optimizations Done   

### 4.5 Genetic algorithm

#### 4.5.1 Introduction

#### 4.5.2 Step-by-step implementation

#### 4.5.3 Why It Is Used to Solve the TSP

#### 4.5.4 Advantages   

#### 4.5.5 Disadvantages    

#### 4.5.6 Optimizations Done   

### 4.6 Ant Colony algorithm

#### 4.6.1 Introduction

#### 4.6.2 Step-by-step implementation

#### 4.6.3 Why It Is Used to Solve the TSP

#### 4.6.4 Advantages   

#### 4.6.5 Disadvantages    

#### 4.6.6 Optimizations Done   

### 4.7 Tabu Search algorithm

maybe i will add it later

## 5. results



## 6. The best solution to test with large number of cities


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

