import itertools

from solver import Solver


class IDDFS(Solver):
    def __init__(self, initial_state):
        super(IDDFS, self).__init__(initial_state)
        self.open_list = []

    def dls(self, limit):
        self.open_list.append(self.initial_state)
        while self.open_list:

            if len(self.explored_nodes) > 250000:
                # run out of time
                return

            board = self.open_list.pop()
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                return self.solution
            if board.depth < limit:
                for neighbor in board.neighbors()[::-1]:
                    if tuple(neighbor.state) not in self.explored_nodes:
                        self.open_list.append(neighbor)
                        self.explored_nodes.add(tuple(neighbor.state))
                        self.max_depth = max(self.max_depth, neighbor.depth)
        return None

    def solve(self):
        for i in itertools.count():
            self.open_list = []
            self.explored_nodes = set()
            self.max_depth = 0
            self.open_list.append(self.initial_state)
            sol = self.dls(i)
            if sol is not None:
                break
        return
