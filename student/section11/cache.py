from functools import lru_cache
import time


@lru_cache()
def add_num(num):
    r = 0
    for i in range(10000000):
        r += num * i
    return r


def momoize(f):
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper


@momoize
def add_num_v2(num):
    r = 0
    for i in range(10000000):
        r += num * i

    return r


if __name__ == "__main__":
    start = time.time()
    for i in range(10):
        print(add_num_v2(i))
    print(time.time() - start)

    start = time.time()
    for i in range(10):
        print(add_num_v2(i))
    print(time.time() - start)
