from enum import Enum
from typing import List
import heapq


class Kind(Enum):
    OPEN = 1
    CLOSE = 0


class State(object):
    def __init__(self, board: List, space: int, count: int, prev=None):
        self.board = board
        self.space = space
        self.prev = prev
        self.count = count


class StateFifth(object):
    def __init__(self, board: List, space: int, prev):
        self.distance = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 1, 2, 3, 2, 3, 4],
            [1, 0, 1, 2, 1, 2, 3, 2, 3],
            [2, 1, 0, 3, 2, 1, 4, 3, 2],
            [1, 2, 3, 0, 1, 2, 1, 2, 3],
            [2, 1, 2, 1, 0, 1, 2, 1, 2],
            [3, 2, 1, 2, 1, 0, 3, 2, 1],
            [2, 3, 4, 1, 2, 3, 0, 1, 2],
            [3, 2, 3, 2, 1, 2, 1, 0, 1]
        ]
        self.board = board
        self.space = space
        self.prev = prev
        if prev is None:
            self.cost = self.manhattan_distance(board)
        else:
            prev_value = board[prev.space]
            self.cost = prev.cost - \
                self.distance[prev_value][space] + \
                self.distance[prev_value][prev.space]

    def manhattan_distance(self, board: List) -> int:
        d = 0
        for index, value in enumerate(board):
            d += self.distance[value][index]
        return d

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost


class AState(object):
    def __init__(self, board, space, prev, move=0, kind=Kind.OPEN):
        self.distance = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 1, 2, 3, 2, 3, 4],
            [1, 0, 1, 2, 1, 2, 3, 2, 3],
            [2, 1, 0, 3, 2, 1, 4, 3, 2],
            [1, 2, 3, 0, 1, 2, 1, 2, 3],
            [2, 1, 2, 1, 0, 1, 2, 1, 2],
            [3, 2, 1, 2, 1, 0, 3, 2, 1],
            [2, 3, 4, 1, 2, 3, 0, 1, 2],
            [3, 2, 3, 2, 1, 2, 1, 0, 1]
        ]
        self.board = board
        self.space = space
        self.prev = prev
        self.move = move
        if prev is None:
            self.cost = self.manhattan_distance(board)
        else:
            prev_value = board[prev.space]
            self.cost = prev.cost - \
                self.distance[prev_value][space] + \
                self.distance[prev_value][prev.space] + 1
        self.kind = kind

    def manhattan_distance(self, board: List) -> int:
        d = 0
        for index, value in enumerate(board):
            d += self.distance[value][index]
        return d

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost


class EightPuzzle(object):
    def __init__(self, start: List):
        self.start = start
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.adj_board_index = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4, 6],
            [1, 3, 5, 7],
            [2, 4, 8],
            [3, 7],
            [4, 6, 8],
            [5, 7]
        ]

    def breath_first_search(self) -> State:
        first_state = State(self.start, self.start.index(0), 0)
        queue = []
        checked = {}

        queue.append(first_state)
        checked[tuple(self.start)] = True

        while queue:
            current_state = queue.pop(0)
            counter = current_state.count

            for adj_index in self.adj_board_index[current_state.space]:
                board = current_state.board.copy()
                board[current_state.space], board[adj_index] = board[adj_index], 0

                if tuple(board) not in checked:
                    next_state = State(
                        board, adj_index, counter + 1, current_state)
                    if board == self.goal:
                        return next_state

                    queue.append(next_state)
                    checked[tuple(board)] = True

    def run(self):
        state = self.breath_first_search()
        print(state.count)
        while state is not None:
            for i in range(3):
                print(state.board[3 * i:3 * i + 3])
            print()
            state = state.prev


class FifteenPuzzle(object):
    def __init__(self, start: List):
        self.start = start
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.adj_board_index = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4, 6],
            [1, 3, 5, 7],
            [2, 4, 8],
            [3, 7],
            [4, 6, 8],
            [5, 7]
        ]
        self.distance = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 1, 2, 3, 2, 3, 4],
            [1, 0, 1, 2, 1, 2, 3, 2, 3],
            [2, 1, 0, 3, 2, 1, 4, 3, 2],
            [1, 2, 3, 0, 1, 2, 1, 2, 3],
            [2, 1, 2, 1, 0, 1, 2, 1, 2],
            [3, 2, 1, 2, 1, 0, 3, 2, 1],
            [2, 3, 4, 1, 2, 3, 0, 1, 2],
            [3, 2, 3, 2, 1, 2, 1, 0, 1]
        ]
        self.isgoal = False

    def interactive_deeping_dfs(self):
        board = self.start
        move_piece = [None] * 32

        def _dfs(limit: int, move: int, space: int):
            if move == limit:
                if board == self.goal:
                    self.isgoal = True
            else:
                for adj_index in self.adj_board_index[space]:
                    adj_zero_value = board[adj_index]
                    if move_piece[move] == adj_zero_value:
                        continue

                    board[adj_index], board[space] = 0, adj_zero_value
                    move_piece[move + 1] = adj_zero_value

                    _dfs(limit, move + 1, adj_index)
                    board[adj_index], board[space] = adj_zero_value, 0

        limit = 0
        while not self.isgoal:
            limit += 1
            _dfs(limit, 0, board.index(0))

        return limit

    def manhattan_distance(self, board: List) -> int:
        d = 0
        for index, value in enumerate(board):
            d += self.distance[value][index]
        return d

    def ida(self):
        board = self.start

        def _ida(limit: int, move: int, space: int, lower: int):
            if move == limit:
                if board == self.goal:
                    self.isgoal = True
            else:
                for adj_index in self.adj_board_index[space]:
                    adj_zero_value = board[adj_index]
                    board[adj_index], board[space] = 0, adj_zero_value

                    next_lower = lower - \
                        self.distance[adj_zero_value][adj_index] + \
                        self.distance[adj_zero_value][space]

                    if move + next_lower <= limit:
                        _ida(limit, move + 1, adj_index, next_lower)

                    board[adj_index], board[space] = adj_zero_value, 0

        limit = 0
        while not self.isgoal:
            limit += 1
            _ida(limit, 0, board.index(0), self.manhattan_distance(board))

        return limit

    def hill_climb(self):
        def _hill_climb(board: list, space: int, distance: int, history: list):
            if board == self.goal:
                for b in history:
                    print(b)
                return True
            else:
                buff = []
                for adj_index in self.adj_board_index[space]:
                    adj_zero_value = board[adj_index]
                    current_board = board.copy()
                    current_board[adj_index], current_board[space] = 0, adj_zero_value

                    if current_board not in history:
                        cost = distance - \
                            self.distance[adj_zero_value][adj_index] + \
                            self.distance[adj_zero_value][space]

                        buff.append((current_board, adj_index, cost))

                buff.sort(key=lambda t: t[2])
                for b, i, c in buff:
                    history.append(b)
                    if _hill_climb(b, i, c, history):
                        return True
                    history.pop()
            return False

        return _hill_climb(
            self.start, self.start.index(0), self.manhattan_distance(self.start), [self.start])

    def best_first_search(self):
        def _best_first_search(board: List, space: int, prev: StateFifth):
            first_state = StateFifth(board, space, prev)
            heap = []
            checked = {}

            heapq.heappush(heap, first_state)
            checked[tuple(self.start)] = True

            while heap:
                current_state = heapq.heappop(heap)
                for adj_zero_index in self.adj_board_index[current_state.space]:
                    board = current_state.board[:]
                    board[adj_zero_index], board[current_state.space] = 0, board[adj_zero_index]

                    if tuple(board) not in checked:
                        next_state = StateFifth(
                            board, board.index(0), current_state)
                        if board == self.goal:
                            return next_state
                        heapq.heappush(heap, next_state)
                        checked[tuple(board)] = True

        state = _best_first_search(self.start, self.start.index(0), None)
        while state:
            print(state.cost, state.board)
            state = state.prev

    def a(self):
        def _a():
            heap = []
            tables = {}
            state = AState(self.start, self.start.index(0), None)

            heapq.heappush(heap, state)
            tables[tuple(self.start)] = state
            while heap:
                current_state = heapq.heappop(heap)
                if current_state.kind == Kind.CLOSE:
                    continue
                current_state.kind = Kind.CLOSE

                for adj_zero_index in self.adj_board_index[current_state.space]:
                    board = current_state.board[:]
                    board[adj_zero_index], board[current_state.space] = 0, board[adj_zero_index]
                    current_key = tuple(board)

                    if current_key not in tables:
                        next_state = AState(
                            board, adj_zero_index, current_state, current_state.move + 1)
                        if board == self.goal:
                            return next_state
                        heapq.heappush(heap, next_state)
                        tables[current_key] = next_state
                    else:
                        state = tables[current_key]
                        if current_state.cost < state.cost:
                            if state.kind == Kind.OPEN:
                                # もしOPENだったら、その状態はCLOSEして、その代わりに新しいOPEN状態を生成して追加する
                                state.kind = Kind.CLOSE
                                next_state = AState(
                                    board, adj_zero_index, current_state, current_state.move + 1)
                                tables[current_key] = next_state
                            else:
                                state.kind = Kind.OPEN
                                state.prev = current_state
                                state.cost = state.cost
                                state.move = current_state.move + 1

                            heapq.heappush(heap, state)

            # failure search
            return False

        state = _a()
        if not state:
            return state
        while state:
            print(state.cost, state.board)
            state = state.prev


if __name__ == "__main__":
    start = [8, 6, 7, 2, 5, 4, 3, 0, 1]
    # p = EightPuzzle(start)
    # p.run()
    p = FifteenPuzzle(start)
    # p.best_first_search()
    # print(p.hill_climb())
    p.a()
