from typing import List


def eratostenes(number: int) -> List[int]:
    is_primnumber = [True] * (number + 1)
    is_primnumber[0], is_primnumber[1] = False, False

    for i in range(2, int(number ** (1 / 2) + 1)):
        if is_primnumber[i]:
            j = i + i
            while j <= number:
                is_primnumber[j] = False
                j += i

    return [i for i, is_prime in enumerate(is_primnumber) if is_prime]


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(num ** (1 / 2)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True


if __name__ == "__main__":
    # import time

    # start = time.time()
    # print(eratostenes(50))
    # print(time.time() - start)
    print(is_prime(37))
