def get_pair(numbers, target):
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_pair_half_sum(numbers):
    sum_numbers = sum(numbers)
    # if sum_numbers % 2 != 0:
    #     return
    # half_sum = int(sum_numbers / 2)

    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return

    cache = set()
    for num in numbers:
        val = half_sum - num
        if val in cache:
            return val, num
        cache.add(num)


if __name__ == "__main__":
    print(get_pair([11, 2, 5, 9, 10, 3], 12))
    print(get_pair_half_sum([11, 2, 5, 9, 10, 3]))
