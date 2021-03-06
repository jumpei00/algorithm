def insersion(nums):
    nums_len = len(nums)
    for i in range(1, nums_len):
        temp_nums = nums[i]
        j = i - 1
        while nums[j] > temp_nums and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp_nums
    return nums
