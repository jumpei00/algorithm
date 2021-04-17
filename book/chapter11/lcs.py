def lcs(x: str, y: str) -> int:
    len_x = len(x)
    len_y = len(y)

    length = [[0] * (len_y + 1) for _ in range(len_x + 1)]
    max_len = 0

    for x_i in range(1, len_x + 1):
        for y_i in range(1, len_y + 1):
            if x[x_i - 1] == y[y_i - 1]:
                length[x_i][y_i] = length[x_i - 1][y_i - 1] + 1
            else:
                length[x_i][y_i] = max(
                    length[x_i][y_i - 1], length[x_i - 1][y_i])
            max_len = max(max_len, length[x_i][y_i])

    return max_len


if __name__ == "__main__":
    x = 'abc'
    y = 'bc'
    print(lcs(x, y))
