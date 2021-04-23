import sys


def fermer(number: int, pow_num: int) -> list:
    result = {}

    max_z = int(pow((number - 1) ** 2 + number ** 2, 1.0 / pow_num))
    for x in range(1, number + 1):
        for y in range(x + 1, number + 1):
            for z in range(y + 1, max_z):
                if pow(x, pow_num) + pow(y, pow_num) == pow(z, pow_num):
                    result[pow(z, pow_num)] = (x, y, z)

    return result


def fermer_v2(number: int, pow_num: int) -> list:
    result = []

    for x in range(1, number + 1):
        for y in range(x + 1, number + 1):
            pow_sum = pow(x, pow_num) + pow(y, pow_num)

            if pow_sum > sys.maxsize:
                raise ValueError(x, y, pow_num, pow_sum)

            z = pow(pow_sum, 1.0 / pow_num)

            if not z.is_integer():
                continue

            z = int(z)
            z_pow = pow(z, pow_num)
            if z_pow == pow_sum:
                result.append((x, y, z))

    return result


if __name__ == "__main__":
    print(fermer_v2(10, 2))
