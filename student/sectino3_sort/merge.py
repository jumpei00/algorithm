def merge(nums):
    if len(nums) <= 1:
        return nums

    center = len(nums) // 2
    left_nums = nums[:center]
    right_nums = nums[center:]

    merge(left_nums)
    merge(right_nums)

    i = li = ri = 0
    while li < len(left_nums) and ri < len(right_nums):
        if left_nums[li] <= right_nums[ri]:
            nums[i] = left_nums[li]
            li += 1
        else:
            nums[i] = right_nums[ri]
            ri += 1
        i += 1

    while li < len(left_nums):
        nums[i] = left_nums[li]
        li += 1
        i += 1

    while ri < len(right_nums):
        nums[i] = right_nums[ri]
        ri += 1
        i += 1

    return nums
