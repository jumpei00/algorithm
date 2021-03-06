def select(nums):
    nums_len = len(nums)

    for start in range(0, nums_len - 1):
        temp_index = start
        for i in range(start + 1, nums_len):
            if nums[i] < nums[temp_index]:
                temp_index = i

        nums[start], nums[temp_index] = nums[temp_index], nums[start]

    return nums
