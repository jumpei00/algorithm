def snake_display(chars: str, depth: int) -> list:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = depth // 2

    def pos(i):
        return i + 1

    def neg(i):
        return i - 1

    op = neg

    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')
        if insert_index == 0:
            op = pos
        if insert_index == depth - 1:
            op = neg
        insert_index = op(insert_index)

    return result


if __name__ == "__main__":
    import string
    t = string.ascii_letters

    for line in snake_display(t, 5):
        print(''.join(line))
