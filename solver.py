from abc import ABC, abstractmethod


class Solver(ABC):
    solution = None
    open_list = None
    nodes_expanded = 0
    max_depth = 0
    explored_nodes = set()
    initial_state = None

    def __init__(self, initial_state):
        self.solution = None
        self.open_list = None
        self.nodes_expanded = 0
        self.max_depth = 0
        self.explored_nodes = set()
        self.initial_state = initial_state
        


    def ancestral_chain(self):
        current = self.solution
        # print(self.solution)

        if(current == None):
            return None

        chain = [current]
        while current.parent is not None:
            chain.append(current.parent)
            current = current.parent
        return chain

    @property
    def path(self):
        
        chain = self.ancestral_chain()
        
        if chain == None:
            return None
        
        path = [node.move for node in chain[-2::-1]]

        return path

    @abstractmethod
    def solve(self):
        pass

    def set_solution(self, board):
        self.solution = board
        self.nodes_expanded = len(self.explored_nodes) - len(self.open_list) - 1
        # return self.solution
