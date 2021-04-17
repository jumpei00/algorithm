import sys


def warshall_floyd(A: list):
    n = len(A)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])

    return A


if __name__ == "__main__":
    A = [
        [0, 2, 5, 1],
        [sys.maxsize, 0, 2, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 2, 0]
    ]
    print(warshall_floyd(A))
