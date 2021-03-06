def bubble(nums):
    begin = 0
    end = len(nums) - 1
    for i in range(begin, end):
        for j in range(begin, end - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
