from collections import Counter


def delete_nums_min(x: list, y: list):
    x_count = Counter(x)
    y_count = Counter(y)
    X = []
    Y = []

    for key in x_count:
        if x_count.get(key) == y_count.get(key):
            X += [key] * x_count.get(key)
        elif y_count.get(key) is None or y_count.get(key) < x_count.get(key):
            X += [key] * x_count.get(key)

    for key in y_count:
        if y_count.get(key) == x_count.get(key):
            Y += [key] * y_count.get(key)
        elif x_count.get(key) is None or y_count.get(key) > x_count.get(key):
            Y += [key] * y_count.get(key)

    return X, Y


def min_count_remove(x, y):
    x_counter = Counter(x)
    y_counter = Counter(y)

    for x_key, x_value in x_counter.items():
        y_value = y_counter.get(x_key)
        if y_value:
            if y_value > x_value:
                x[:] = [i for i in x if i != x_key]
            elif y_value < x_value:
                y[:] = [i for i in y if i != x_key]


if __name__ == "__main__":
    X = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    Y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    print(delete_nums_min(X, Y))
    min_count_remove(X, Y)
    print(X)
    print(Y)
