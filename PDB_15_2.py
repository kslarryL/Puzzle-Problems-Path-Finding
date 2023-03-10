from collections import deque
import numpy as np
import pickle

class Pattern_generater():
    def __init__(self, A_pattern, B_pattern):
        self.__A_pattern = A_pattern
        self.__B_pattern = B_pattern

    def generate_bfs(self, init_pattern):
        pattern_database = dict()
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        pattern_numbers = [n for n in init_pattern if n != 0]

        queue = deque([(init_pattern, 0)])
        pattern_database[str(init_pattern)] = 0

        while queue:
            cur_state, cur_moves = queue.popleft()

            for pattern_number in pattern_numbers:
                move_tile = cur_state.index(pattern_number)
                i, j = move_tile // 4, move_tile % 4
                for dx, dy in zip(dxs, dys):
                    x, y = i + dx, j + dy
                    new_state = np.array(np.array(cur_state).reshape(4, 4))
                    if 0 <= x < 4 and 0 <= y < 4 and new_state[x, y] == 0:
                        new_state[i, j], new_state[x, y] = new_state[x, y], new_state[i, j]
                        new_state = new_state.flatten().tolist()
                        if str(new_state) not in pattern_database:
                            queue.append((new_state, cur_moves + 1))
                            pattern_database[str(new_state)] = cur_moves + 1
        return pattern_database

    def generate_pattern(self):
        print("start generating ...")

        A_pattern_database = self.generate_bfs(self.__A_pattern)
        database = open("15_D_database", "wb")
        pickle.dump(A_pattern_database, database)
        database.close()
        print("15_D_database generated")

        B_pattern_database = self.generate_bfs(self.__B_pattern)
        database = open("15_E_database", "wb")
        pickle.dump(B_pattern_database, database)
        database.close()
        print("15_E_database generated")


if __name__ == "__main__":
    A = list(map(int, "1 2 3 4 5 6 7 8 0 0 0 0 0 0 0 0".split()))
    B = list(map(int, "0 0 0 0 0 0 0 0 9 10 11 12 13 14 15 0".split()))
    test_generater = Pattern_generater(A, B)
    test_generater.generate_pattern()
