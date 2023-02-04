import resource
import sys
from pathlib import Path
import time

from astar                  import AStar
from bfs                    import BFS
from board_8                import Board_8
from board_8_no_heuristic   import Board_8_no_heuristic
from board_15               import Board_15
from board_15_no_heuristic  import Board_15_no_heuristic
from dfs                    import DFS
from iddfs                  import IDDFS


def string_to_array(str):
    arr = []
    temp = ''
    for i in range(len(str)):

        if str[i] != ',':
            temp += str[i]
        else:
            arr.append(int(temp))
            temp = ''
    arr.append(int(temp))

    return arr

    # size = 3
    # res = []
    # for j in range(size):
    #     temp_arr = []
    #     for k in range(size):
    #         temp_arr.append(arr[j*3 + k])
    #     res.append(temp_arr)

    # return res


def import_instance(filename):
    f = Path(filename)
    if not f.is_file():
        raise BaseException(filename + " does not exist.")
    f = open(filename, 'r')
    line = f.readline()
    puzzle_size, num_of_samples = [int(x) for x in line.split(' ')]
    samples = []

    if(puzzle_size == 8):
        for s in range(num_of_samples):
            line = f.readline()
            sample = []
            for i in range(puzzle_size + 1):
                sample.append(int(line[i]))
            # print(sample)
            samples.append(sample)

    if(puzzle_size == 15):
        for s in range(num_of_samples):
            line = f.readline()
            sample = [int(x) for x in line.split(' ')]
            samples.append(sample)

    f.close()

    return samples
    

def main():
    samples = import_instance(sys.argv[2]);
    # print(samples)

    # # print(string_to_array(sys.argv[2]))
    # p = Board(string_to_array(sys.argv[2]))
    # p_no_heuristic = Board_no_heuristic(string_to_array(sys.argv[2]))
    # # print("p = \n",p)

    alg = sys.argv[1]

    cost            = []
    nodes_expanded  = []
    nodes_generated = []
    running_time    = []
    max_ram_usage   = []

    puzzle_size = len(samples[0])

    if puzzle_size == 9:
        for sample in samples:
            # print(Board_no_heuristic(sample))
            # print(sample)

            start_t = time.time()

            s = None
            if alg == 'bfs':
                s = BFS(Board_8_no_heuristic(sample))
            elif alg == 'ids':
                s = IDDFS(Board_8_no_heuristic(sample))
            elif alg == 'dfs':
                s = DFS(Board_8_no_heuristic(sample))
            elif alg == 'ast':
                s = AStar(Board_8(sample))
            else:
                print("Invalid input, continuing through A*")
                s = AStar(Board_8(sample))
            s.solve()

            run_t = time.time() - start_t

            if s.path != None:
                cost            .append(len(s.path))
                nodes_expanded  .append(s.nodes_expanded)
                nodes_generated .append(len(s.explored_nodes))
                running_time    .append(run_t)
                max_ram_usage   .append(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
            else:
                cost            .append(0)
                nodes_expanded  .append(0)
                nodes_generated .append(0)
                running_time    .append(0)
                max_ram_usage   .append(0)

    elif puzzle_size == 16:
        for sample in samples:
            # print(Board_no_heuristic(sample))
            # print(sample)

            start_t = time.time()

            s = None
            if alg == 'bfs':
                s = BFS(Board_15_no_heuristic(sample))
            elif alg == 'ids':
                s = IDDFS(Board_15_no_heuristic(sample))
            elif alg == 'dfs':
                s = DFS(Board_15_no_heuristic(sample))
            elif alg == 'ast':
                s = AStar(Board_15(sample))
            else:
                print("Invalid input, continuing through A*")
                s = AStar(Board_15(sample))
            s.solve()

            run_t = time.time() - start_t


            if s.path != None:
                cost            .append(len(s.path))
                nodes_expanded  .append(s.nodes_expanded)
                nodes_generated .append(len(s.explored_nodes))
                running_time    .append(run_t)
                max_ram_usage   .append(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
            else:
                cost            .append(0)
                nodes_expanded  .append(0)
                nodes_generated .append(0)
                running_time    .append(0)
                max_ram_usage   .append(0)

    filename = "results/" + alg + "_" + str(puzzle_size - 1) + ".csv"
    result_file = open(filename, "w", buffering=1)
    if(puzzle_size == 9):
        if alg == 'bfs':
            result_file.write("{}\n".format("8-puzzle using BFS "))
        elif alg == 'ids':
            result_file.write("{}\n".format("8-puzzle using DFID"))
        elif alg == 'dfs':
            result_file.write("{}\n".format("8-puzzle using DFS "))
        elif alg == 'ast':
            result_file.write("{}\n".format("8-puzzle using A*  "))
        else:
            result_file.write("{}\n".format("8-puzzle using A*  "))

    elif(puzzle_size == 16):
        if alg == 'bfs':
            result_file.write("{}\n".format("15-puzzle using BFS "))
        elif alg == 'ids':
            result_file.write("{}\n".format("15-puzzle using DFID"))
        elif alg == 'dfs':
            result_file.write("{}\n".format("15-puzzle using DFS "))
        elif alg == 'ast':
            result_file.write("{}\n".format("15-puzzle using A*  "))
        else:
            result_file.write("{}\n".format("15-puzzle using A*  "))

    result_file.write("{},{},{},{},{},{}\n".format("Case", "Cost", "Nodes Expanded", "Nodes Generated", "Running Time / s", "Max Ram Usage / KB"))
    for i in range(len(samples)):
        result_file.write("{},{},{},{},{},{}\n".format(" ".join(str(n) for n in samples[i]),
                                                       cost[i],
                                                       nodes_expanded[i],
                                                       nodes_generated[i],
                                                       running_time[i],
                                                       max_ram_usage[i]))
    result_file.close()
    
    # if alg == 'bfs':
    #     s = BFS(p_no_heuristic)
    # elif alg == 'ids':
    #     s = IDDFS(p_no_heuristic)
    # elif alg == 'dfs':
    #     s = DFS(p_no_heuristic)
    # elif alg == 'ast':
    #     s = AStar(p)
    # else:
    #     print("Invalid input, continuing through A*")
    #     s = AStar(p)
    # s.solve()

    # file = open(f'{alg}_output1.txt', 'w')

    # file.write('path_to_goal: ' + str(s.path) + '\n')
    # file.write('cost_of_path: ' + str(len(s.path)) + '\n')
    # file.write('nodes_expanded: ' + str(s.nodes_expanded) + '\n')
    # file.write('nodes_explored: ' + str(len(s.explored_nodes)) + '\n')
    # file.write('search_depth: ' + str(s.solution.depth) + '\n')
    # file.write('max_search_depth: ' + str(s.max_depth) + '\n')
    # file.write('running_time: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_utime + \
    #                                   resource.getrusage(resource.RUSAGE_SELF).ru_stime) + '\n')
    # file.write('max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))

    # file.close()


if __name__ == "__main__":
    main()
