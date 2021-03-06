def counting(nums, place):
    count = [0] * 10
    result = [0] * len(nums)

    for num in nums:
        index = int(num / place) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(nums) - 1, -1, -1):
        index = int(nums[i] / place) % 10
        result[count[index] - 1] = nums[i]
        count[index] -= 1

    return result


def radix(nums):
    max_num = max(nums)
    place = 1

    while place < max_num:
        nums = counting(nums, place)
        place *= 10

    return nums
