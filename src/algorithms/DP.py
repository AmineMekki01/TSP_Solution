
class TspDynamicProgrammingRecursive:
    def __init__(self, distance, instance_name, time_limit, rand_seed, solution_path):

        self.N = len(distance)
        self.START_NODE = 0
        self.FINISHED_STATE = (1 << self.N) - 1
        self.distance = distance
        self.minTourCost = float('inf')
        self.tour = []
        self.ranSolver = False
        self.memo = {}
        self.instance_name = instance_name
        self.time_limit = time_limit
        self.rand_seed = rand_seed
        self.solution_path = solution_path

    def get_metrics(self):

        if len(self.distance) > 15:
            print("Number of cities is too large! A solution will not be found in a reasonable amount of time. Choose a smaller number of cities <= 15.")
            return None, None

        if not self.ranSolver:
            self.solve()

        self.save_solution(self.instance_name,
                           self.time_limit, self.rand_seed, self.solution_path)

        return self.minTourCost, self.tour

    def solve(self):
        state = 1 << self.START_NODE
        self.minTourCost = self.tsp(self.START_NODE, state)

        index = self.START_NODE
        while True:
            self.tour.append(index)
            next_index = self.find_next_index(index, state)
            if next_index is None:
                break
            next_state = state | (1 << next_index)
            state = next_state
            index = next_index
        self.tour.append(self.START_NODE)
        self.ranSolver = True

    def tsp(self, i, state):
        if state == self.FINISHED_STATE:
            return self.distance[i][self.START_NODE]

        if (i, state) in self.memo:
            return self.memo[(i, state)]

        min_cost = float('inf')
        index = -1
        for next_node in range(self.N):
            if (state & (1 << next_node)) != 0:
                continue
            next_state = state | (1 << next_node)
            new_cost = self.distance[i][next_node] + \
                self.tsp(next_node, next_state)
            if new_cost < min_cost:
                min_cost = new_cost
                index = next_node

        self.memo[(i, state)] = min_cost
        return min_cost

    def find_next_index(self, i, state):
        min_cost = float('inf')
        index = None
        for next_node in range(self.N):
            if (state & (1 << next_node)) != 0:
                continue
            cost = self.distance[i][next_node]
            if cost < min_cost:
                min_cost = cost
                index = next_node
        return index

    def save_solution(self, instance_name, time_limit, rand_seed, solution_path):
        solution_path = f"{solution_path}/{instance_name}_DP_{time_limit}_{rand_seed}"
        with open(solution_path+".txt", 'w') as f:
            f.write(f"Best Distance: {self.minTourCost}\n")
            f.write("Best Path: " + ' -> '.join(map(str, self.tour)) + '\n\n')
