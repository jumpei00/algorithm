def momoize(f):
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper


@momoize
def long_func(num):
    r = 0
    for i in range(10000000):
        r += num * i
    return r


def test(f):
    print('outer wrapper')

    def _wrapper(n):
        print('wrapper start')
        f(n)
        print('wrapper end')
    return _wrapper


@test
def func(a):
    print(a)


# func(10)
# func(10)
