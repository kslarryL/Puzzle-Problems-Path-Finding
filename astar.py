import heapq

from solver import Solver


class AStar(Solver):
    def __init__(self, initial_state):
        super(AStar, self).__init__(initial_state)
        self.open_list = []

    def solve(self):
        heapq.heappush(self.open_list, self.initial_state)
        while self.open_list:

            if len(self.explored_nodes) > 250000:
                # run out of time
                return

            board = heapq.heappop(self.open_list)
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                break
            for neighbor in board.neighbors():
                if tuple(neighbor.state) not in self.explored_nodes:
                    heapq.heappush(self.open_list, neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return
