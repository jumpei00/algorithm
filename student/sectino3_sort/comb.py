def comb(nums):
    nums_len = len(nums)
    swap = True
    gap = int(nums_len // 1.3)

    while gap > 1 or swap:
        swap = False
        for i in range(nums_len - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swap = True

        gap = int(gap // 1.3)
        if gap < 1:
            gap = 1

    return nums
