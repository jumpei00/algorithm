def prime_number(n: int) -> bool:
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i <= n ** (1 / 2):
        if n % i == 0:
            return False
        i += 2

    return True


def eratos_tenes(N: int) -> list:
    isprime = [True for _ in range(N)]
    isprime[0] = isprime[1] = False

    for i in range(2, int(N ** (1 / 2))):
        if isprime[i]:
            j = i + i
            while j < N:
                isprime[j] = False
                j += i

    r = [i for i in range(N) if isprime[i]]
    return r


def gcd(x: int, y: int) -> int:
    x, y = max(x, y), min(x, y)

    while y > 0:
        r = x % y
        x = y
        y = r

    return x


def gcd_rec(x: int, y: int) -> int:
    def _gcd(x, y):
        if x % y == 0:
            return y
        else:
            return _gcd(y, x % y)
    return _gcd(max(x, y), min(x, y))


def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x * x, n / 2)
    elif n % 2 != 0:
        return power(x * x, n // 2) * x


if __name__ == "__main__":
    print(power(2, 128))
