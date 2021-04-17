from typing import List, Tuple


class Queens(object):
    def __init__(self, first_location: List[Tuple], N=8):
        self.first_location = first_location
        self.N = N
        self.board = [[0] * N for _ in range(N)]
        self.row = [False for _ in range(N)]
        self.col = [False for _ in range(N)]
        self.ldig = [False for _ in range(2 * N - 1)]
        self.rdig = [False for _ in range(2 * N - 1)]

    def print_board(self):
        for b in self.board:
            print(b)

    def run(self):
        for i, j in self.first_location:
            self.board[i][j] = 1
            self.row[i] = self.col[j] = \
                self.ldig[i + j] = self.rdig[i - j + self.N - 1] = True

        def _queens(i: int):
            if i == self.N:
                self.print_board()
                return

            if self.row[i]:
                _queens(i + 1)
                return

            for j in range(self.N):
                if not (self.col[j] or self.ldig[i + j] or self.rdig[i - j + self.N - 1]):
                    self.board[i][j] = 1
                    self.row[i] = self.col[j] = \
                        self.ldig[i + j] = self.rdig[i - j + self.N - 1] = True

                    _queens(i + 1)

                    self.board[i][j] = 0
                    self.row[i] = self.col[j] = \
                        self.ldig[i + j] = self.rdig[i - j + self.N - 1] = False

        _queens(0)


if __name__ == "__main__":
    f = [(2, 2), (5, 3)]
    q = Queens(f)
    q.run()
