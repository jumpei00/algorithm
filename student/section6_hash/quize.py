def get_pair(nums, target):
    cache = set()
    for num in nums:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_sum_pair(nums):
    sum_nums = sum(nums)

    half_sum, remainder = divmod(sum_nums, 2)
    if remainder != 0:
        return

    cache = set()
    for num in nums:
        val = half_sum - num
        if val in nums:
            return val, num
        cache.add(num)


if __name__ == "__main__":
    print(get_pair([11, 2, 5, 9, 10, 3], 12))
    print(get_sum_pair([11, 2, 5, 9, 10, 3]))
