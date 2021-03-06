def shell(nums):
    len_nums = len(nums)
    gap = len_nums
    while gap != 1:
        gap = gap // 2
        for i in range(gap, len_nums):
            temp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp
    return nums
