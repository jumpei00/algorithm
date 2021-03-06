def cocktail(nums):
    for_limit = 0
    back_limit = len(nums)
    swap = True

    while swap:
        swap = False
        for fw_i in range(for_limit, back_limit - 1):
            if nums[fw_i] > nums[fw_i + 1]:
                nums[fw_i], nums[fw_i + 1] = nums[fw_i + 1], nums[fw_i]
                swap = True

        if not swap:
            break

        swap = False
        back_limit -= 1

        for bw_i in range(back_limit, for_limit, -1):
            if nums[bw_i - 1] > nums[bw_i]:
                nums[bw_i - 1], nums[bw_i] = nums[bw_i], nums[bw_i - 1]
                swap = True

        for_limit += 1

    return nums
