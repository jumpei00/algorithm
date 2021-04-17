import sys


def coin_problem(coin: list, pay: int) -> list:
    minimum_coin = [sys.maxsize for _ in range(pay + 1)]

    minimum_coin[0] = 0
    for i in range(len(coin)):
        for j in range(coin[i], pay + 1):
            minimum_coin[j] = min(
                minimum_coin[j], minimum_coin[j - coin[i]] + 1)

    return minimum_coin


def napzack(items: list, capacity: int) -> list:
    items.insert(0, [0, 0])
    selection = [[0] * (capacity + 1) for _ in range(len(items))]

    for i in range(1, len(items)):
        for j in range(1, capacity + 1):
            if j - items[i][1] < 0:
                selection[i][j] = selection[i - 1][j]
            else:
                selection[i][j] = max(
                    selection[i - 1][j], selection[i - 1][j - items[i][1]] + items[i][0])

    return items, selection


def binary_search(L: list, value: int) -> int:
    if len(L) == 1:
        return 0

    left = 0
    right = len(L) - 1

    while left < right:
        mid = (left + right) // 2
        if L[mid] == value:
            return mid + 1

        elif L[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return mid + int(L[mid] < value)


def Lis(A: list) -> list:
    L = [A[0]]
    for i in range(len(A)):
        if A[i] > L[-1]:
            L.append(A[i])
        else:
            L[binary_search(L, A[i])] = A[i]

    return L


def large_squre(tile: list, H: int, W: int) -> list:
    dp = []
    for h in range(H):
        dp_h = []
        for w in range(W):
            dp_h.append((tile[h][w] + 1) % 2)
        dp.append(dp_h)

    max_width = 0

    for h in range(1, H):
        for w in range(1, W):
            if not tile[h][w]:
                dp[h][w] = min(
                    dp[h][w - 1], dp[h - 1][w - 1], dp[h - 1][w]) + 1
                max_width = max(max_width, dp[h][w])

    for h in range(H):
        print(dp[h])

    return max_width


def large_rectangle(tile: list, H: int, W: int) -> int:
    hist = [[(t + 1) % 2 for t in tile[0]]]
    for i in range(1, H):
        r = []
        for j in range(W):
            if tile[i][j] == 0:
                r.append(hist[i - 1][j] + 1)
            else:
                r.append(0)
        r.append(0)
        hist.append(r)

    max_area = 0

    for hist_one_line in hist:
        stack = []
        for width, height in enumerate(hist_one_line):
            if not stack:
                stack.append((width, height))
            elif stack[-1][1] < height:
                stack.append((width, height))
            elif stack[-1][1] > height:
                while stack and stack[-1][1] > height:
                    top_w, top_h = stack.pop()
                    max_area = max(max_area, (width - top_w) * top_h)
                stack.append((top_w, height))

    return max_area


if __name__ == "__main__":
    tile = [[0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0]]
    print(large_rectangle(tile, 4, 5))
