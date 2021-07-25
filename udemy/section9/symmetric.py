from typing import List, Tuple, Generator


def symmetric(pairs: List[Tuple[int, int]]) -> Generator[Tuple[int, int], None, None]:
    d = {}
    for x, y in pairs:
        if d.get(y) == x:
            yield (x, y)
            d.pop(y)
        else:
            d[x] = y


if __name__ == "__main__":
    s = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4), (5, 3), (3, 5)]
    for t in symmetric(s):
        print(t)
