import sys


def get_sequence_max_sum(nums: list):
    len_nums = len(nums)
    res = nums[0]
    area = []
    for i in range(len_nums):
        for j in range(i, len_nums):
            if sum(nums[i:j]) > res:
                res = sum(nums[i:j])
                area = nums[i:j]

    return res, tuple(area)


def maximum_circular_subarray_sum(nums: list):
    len_nums = len(nums)
    res = -sys.maxsize
    area = []
    for i in range(len_nums):
        j = i + 1
        while j != i:
            if i < j and sum(nums[i:j]) > res:
                res = sum(nums[i:j])
                area = nums[i:j]
            elif j < i and sum(nums[i:]) + sum(nums[:j]) > res:
                res = sum(nums[i:]) + sum(nums[:j])
                area = nums[i:] + nums[:j]

            if j == len_nums:
                j = -1
            j += 1

    return res, tuple(area)


if __name__ == "__main__":
    nums = [1, -2, 3, 6, -1, 2, 4, -5, 2]
    print(get_sequence_max_sum(nums))
    print(maximum_circular_subarray_sum(nums))
