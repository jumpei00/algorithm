def snake_string_v1(chars: str):
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')

    return result


def snake_string_v2(chars: str, depth: int):
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    def pos(i):
        return i + 1

    def neg(i):
        return i - 1

    op = neg

    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')
        if insert_index <= 0:
            op = pos
        if insert_index >= depth - 1:
            op = neg
        insert_index = op(insert_index)

    return result


if __name__ == "__main__":
    import string
    # for line in snake_string_v1('01234'):
    #     print(''.join(line))

    for line in snake_string_v2(string.ascii_lowercase, 10):
        print(''.join(line))
