from heapq import *
import pickle
import numpy as np
import time
import sys
from pathlib import Path
import resource

def import_instance(filename):
    f = Path(filename)
    if not f.is_file():
        raise BaseException(filename + " does not exist.")
    f = open(filename, 'r')
    line = f.readline()
    puzzle_size, num_of_samples = [int(x) for x in line.split(' ')]
    samples = []

    if puzzle_size == 8:
        for s in range(num_of_samples):
            line = f.readline()
            sample = []
            for i in range(puzzle_size + 1):
                sample.append(int(line[i]))
            # print(sample)
            samples.append(sample)
    f.close()

    return samples

class Solver():

    cost = 0
    running_time = 0.0
    nodes_expanded = 0
    nodes_generated = 0

    def __init__(self, init_state):
        self.__init_state = init_state
        self.__pattern_database_A = None
        self.__pattern_database_B = None
        self.__is_loaded = False
        self.cost = 0
        self.running_time = 0.0
        self.nodes_expanded = 0
        self.nodes_generated = 0

    def load_pattern_database(self):
        file = open("8_A_database", "rb")
        self.__pattern_database_A = pickle.load(file)
        file.close()

        file = open("8_B_database", "rb")
        self.__pattern_database_B = pickle.load(file)
        file.close()

        self.__is_loaded = True

    def get_heuristic_value(self, cur_state):
        A = [a if a in [1, 2, 3, 4] else 0 for a in cur_state]
        B = [b if b in [5, 6, 7, 8] else 0 for b in cur_state]
        ret = 0
        ret += self.__pattern_database_A[str(A)]
        ret += self.__pattern_database_B[str(B)]
        return ret

    def a_star(self):
        self.load_pattern_database()
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        start_t = time.time()

        init_state = self.__init_state
        init_step = 0
        init_heur = self.get_heuristic_value(init_state) + init_step

        visited = set()
        hq = [] # heap

        visited.add(str(init_state))
        heappush(hq, (init_heur, init_step, init_state))

        generated = 0
        


        while hq:
            cur_heur, cur_step, cur_state = heappop(hq)
            if cur_heur == cur_step:
                # print("answer :", cur_step)
                # print("time :", time.time() - start_t)
                # print("nodes :", len(visited))
                self.cost = cur_step
                self.running_time = time.time() - start_t
                self.nodes_generated = generated
                self.nodes_expanded = len(visited)
                break

            empty_tile = cur_state.index(0)
            i, j = empty_tile // 3, empty_tile % 3
            for dx, dy in zip(dxs, dys):
                x, y = i + dx, j + dy
                new_state = np.array(cur_state).reshape(3, 3)
                if 0 <= x < 3 and 0 <= y < 3:
                    new_state[i, j], new_state[x, y] = new_state[x, y], new_state[i, j]
                    new_state = new_state.flatten().tolist()
                    generated += 1
                    if str(new_state) not in visited:
                        new_step = cur_step + 1
                        new_huer = self.get_heuristic_value(new_state) + new_step
                        visited.add(str(new_state))
                        heappush(hq, (new_huer, new_step, new_state))

    def solve(self, search_algorithm = "astar"):
        if search_algorithm == "astar":
            self.a_star()


if __name__ == "__main__":

    samples = import_instance(sys.argv[1]);
    # print(samples)
    cost            = []
    nodes_expanded  = []
    nodes_generated = []
    running_time    = []
    max_ram_usage   = []

    for sample in samples:
        test = Solver(sample)
        test.solve()
        cost.append(test.cost)
        nodes_expanded.append(test.nodes_expanded)
        nodes_generated.append(test.nodes_generated)
        running_time.append(test.running_time)
        max_ram_usage.append(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)

    filename = "results/" + "PDB_8.csv"
    result_file = open(filename, "w", buffering=1)
    result_file.write("{}\n".format("8-puzzle using A* with PDB"))
    result_file.write("{},{},{},{},{},{}\n".format("Case", "Cost", "Nodes Expanded", "Nodes Generated", "Running Time / s", "Max Ram Usage / KB"))
    for i in range(len(samples)):
        result_file.write("{},{},{},{},{},{}\n".format(" ".join(str(n) for n in samples[i]),
                                                       cost[i],
                                                       nodes_expanded[i],
                                                       nodes_generated[i],
                                                       running_time[i],
                                                       max_ram_usage[i]))
    result_file.close()
