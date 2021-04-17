def permutation(nums: list):
    first_nums = nums.copy()
    len_nums = len(nums)

    while True:
        for i in range(len_nums - 1):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            print(tuple(nums))
        if nums == first_nums:
            break


def permutation_v2(nums: list):
    r = []
    if len(nums) <= 1:
        return [nums]

    # [2, 3] -> [[2, 3], [3, 2]]
    # [3] -> [3]
    for perm in permutation_v2(nums[1:]):
        for i in range(len(nums)):
            # [1, 2, 3] -> [1] and [2, 3], [1] and [3, 2]
            # [2, 3] -> [2] and [3]
            r.append(perm[:i] + nums[:1] + perm[i:])

    return r


def permutation_v3(nums: list):
    if len(nums) <= 1:
        yield nums
    else:
        # [1, 2] -> perm = [1, 2], [2, 1]
        # [2] -> perm = [2]
        for perm in permutation_v3(nums[1:]):
            for i in range(len(nums)):
                yield perm[:i] + nums[:1] + perm[i:]


if __name__ == "__main__":
    nums = [1, 2, 3]
    for p in permutation_v3(nums):
        print(p)
