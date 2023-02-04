import numpy as np
import copy

class Board_8:
    parent = None
    state = None
    move = None
    depth = 0
    zero = None
    cost = 0
    goal_state = None
    index_of_goal_state = None

    def __init__(self, state, parent=None, move=None, depth=0):
        self.goal_state = [1,2,3,4,5,6,7,8,0]
        self.index_of_goal_state = self.index_of_goal_state()
        self.parent = parent
        self.state = state
        self.move = move
        self.depth = depth
        self.zero = self.location_of_blank()
        self.cost = self.depth + self.manhattan()
        

    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            op_pr = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return op_pr[self.move] < op_pr[other.move]

    def __str__(self):
        return str(self.state[:3]) + '\n' + str(self.state[3:6]) + '\n' + str(self.state[6:]) + ' ' + str(self.depth) + str(self.move) + '\n'

    def goal_test(self):
        return (self.state == self.goal_state)

    def location_of_blank(self):
        return self.state.index(0);

    def manhattan(self):
        state = self.index_of_current_state()
        goal = self.index_of_goal_state
        return sum((abs(state // 3 - goal // 3) + abs(state % 3 - goal % 3))[1:])

    def index_of_current_state(self):
        index = np.array(range(9))
        for x, y in enumerate(self.state):
            index[y] = x
        return index

    def index_of_goal_state(self):
        index = np.array(range(9))
        for x, y in enumerate(self.goal_state):
            index[y] = x
        return index

    def swap(self, i, j):
        new_state = copy.deepcopy(self.state)
        temp = new_state[j]
        new_state[j] = new_state[i]
        new_state[i] = temp
        # print(new_state)
        return new_state

    def up(self):
        if self.zero > 2:
            return Board_8(self.swap(self.zero, self.zero - 3), self, 'Up', self.depth + 1)
        else:
            return None

    def down(self):
        if self.zero < 6:
            return Board_8(self.swap(self.zero, self.zero + 3), self, 'Down', self.depth + 1)
        else:
            return None

    def left(self):
        if self.zero % 3 != 0:
            return Board_8(self.swap(self.zero, self.zero - 1), self, 'Left', self.depth + 1)
        else:
            return None

    def right(self):
        if (self.zero + 1) % 3 != 0:
            return Board_8(self.swap(self.zero, self.zero + 1), self, 'Right', self.depth + 1)
        else:
            return None

    def neighbors(self):
        neighbors = []
        up = self.up()
        down = self.down()
        left = self.left()
        right = self.right()
        if (up != None):
            neighbors.append(up)
        if (down != None):
            neighbors.append(down)
        if (left != None):
            neighbors.append(left)
        if (right != None):
            neighbors.append(right)
        # print (neighbors)
        return neighbors

    __repr__ = __str__
