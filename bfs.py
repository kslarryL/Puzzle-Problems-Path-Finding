from collections import deque

from solver import Solver


class BFS(Solver):
    def __init__(self, initial_state):
        super(BFS, self).__init__(initial_state)
        self.open_list = deque()

    def solve(self):
        self.open_list.append(self.initial_state)

        # print(self.open_list)
        
        while (len(self.open_list) != 0):

            if len(self.explored_nodes) > 250000:
                # run out of time
                return

            board = self.open_list.popleft()
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                # print(self.explored_nodes)
                break
            for neighbor in board.neighbors():
                if tuple(neighbor.state) not in self.explored_nodes:
                    self.open_list.append(neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return
