def counting(nums):
    max_num = max(nums)
    count = [0] * (max_num + 1)
    result = [0] * len(nums)

    for num in nums:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(nums) - 1, -1, -1):
        index = nums[i]
        result[count[index] - 1] = nums[i]
        count[index] -= 1

    return result
