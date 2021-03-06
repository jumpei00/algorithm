def gnome(nums):
    nums_len = len(nums)
    i = 0
    while i < nums_len - 1:
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1
    return nums
